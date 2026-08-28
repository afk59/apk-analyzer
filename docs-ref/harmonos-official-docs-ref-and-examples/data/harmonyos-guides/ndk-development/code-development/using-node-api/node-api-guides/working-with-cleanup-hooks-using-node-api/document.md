# Working with Cleanup Hooks Using Node-API

#### Introduction

Node-API provides APIs for adding and removing cleanup hooks, which are called to release resources when the environment exits.

#### Basic Concepts

Before using Node-API to add or remove cleanup hooks, understand the following concepts:

-   Resource management
    
    In ArkTS, you need to manage system resources, such as memory, file handles, and network connections. Properly creating, using, and releasing these resources during the lifecycle of the Node-API module can prevent resource leaks and application breakdown. Resource management usually includes initializing resources, clearing resources when required, and performing necessary operations when clearing resources, such as closing a file or disconnecting from the network.
    
-   Hook function
    
    A hook function is a callback that is automatically executed at the specified time or upon a specific event. When an environment or a process exits, not all the resources can be automatically reclaimed immediately. In the context of a Node-API module, the cleanup hooks are a supplement that ensures release of all the resources occupied.
    

So far, you've learnt resource management in ArkTS and cleanup hook functions. Read on to learn the Node-API interfaces that you can use to perform resource management with cleanup hooks.

#### Available APIs

The following table lists the APIs for using different types of cleanup hooks.

| API | Description |
| :-- | :-- |
| napi\_add\_env\_cleanup\_hook | Adds an environment cleanup hook function, which will be called when the Node-API environment exits. |
| napi\_remove\_env\_cleanup\_hook | Removes an environment cleanup hook function. |
| napi\_add\_async\_cleanup\_hook | Adds an async cleanup hook function, which will be executed asynchronously when the Node-API process exits. |
| napi\_remove\_async\_cleanup\_hook | Removes an async cleanup hook function. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in the APIs for cleanup hooks.

## napi\_add\_env\_cleanup\_hook

Call **napi\_add\_env\_cleanup\_hook** to add an environment cleanup hook function, which will be executed when the environment exits. This ensures that resources are released before the environment is destroyed.

Note that **napi\_add\_env\_cleanup\_hook** does not support binding multiple callbacks to the same **arg**. If **env** is destroyed but the **cleanup** callback has not been executed, you can locate the failed calls with "AddCleanupHook Failed, data cannot register multiple times." on HiLog if the ArkTS runtime [multi-thread check](../../../../../coding-and-debugging/analyzing-logs-and-faults/fault-analysis/arkcompiler-runtime-detection/document.md) is enabled.

## napi\_remove\_env\_cleanup\_hook

Call **napi\_remove\_env\_cleanup\_hook** to remove the previously added environment cleanup hook function. You may need to use this API when an addon is uninstalled or resources are reallocated.

CPP code:

#include <hilog/log.h>
#include <string>
#include "napi/native\_api.h"
#include "uv.h"

// Define the memory struct, including the pointer to the data and the data size.
typedef struct {
    char \*data;
    size\_t size;
} Memory;

// Callback for clearing the external buffer. It is used to release the allocated memory.
void ExternalFinalize(napi\_env env, void \*finalizeData, void \*finalizeHint)
{
    Memory \*wrapper = (Memory \*)finalizeHint;
    // ...
    free(wrapper->data);
    free(wrapper);
    OH\_LOG\_INFO(LOG\_APP, "Node-API napi\_add\_env\_cleanup\_hook ExternalFinalize");
}

// Perform cleanup operations when the environment is closed, for example, clear global variables or other resources.
static void Cleanup(void \*arg)
{
    // Perform the cleanup operation.
    OH\_LOG\_INFO(LOG\_APP, "Node-API napi\_add\_env\_cleanup\_hook cleanuped: %{public}d", \*(int \*)(arg));
}

// Create an external buffer and add the environment cleanup hook function.
static napi\_value NapiEnvCleanUpHook(napi\_env env, napi\_callback\_info info)
{
    // Allocate memory and copy the string to the memory.
    std::string str("Hello from Node-API!");
    Memory \*wrapper = (Memory \*)malloc(sizeof(Memory));
    if (wrapper == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "malloc for wrapper failed");
        return nullptr;
    }
    wrapper->data = static\_cast<char \*>(malloc(str.size() + 1));
    if (wrapper->data == nullptr) {
        free(wrapper);
        OH\_LOG\_ERROR(LOG\_APP, "malloc for wrapper->data failed");
        return nullptr;
    }
    std::copy\_n(str.c\_str(), str.size() + 1, wrapper->data);
    wrapper->size = str.size();
    // Create an external buffer object and specify the cleanup callback function.
    // Note: The memory release of wrapper->data depends on the ExternalFinalize callback. ExternalFinalize is called only when the buffer is correctly held and finally reclaimed by GC. Otherwise, memory leaks occur.
    napi\_value buffer = nullptr;
    napi\_status status = napi\_create\_external\_buffer(env, wrapper->size, (void \*)wrapper->data,
                                                     ExternalFinalize, wrapper, &buffer);
    if (status != napi\_ok) {
        // If the creation fails, proactively release the memory to avoid memory leaks.
        free(wrapper->data);
        free(wrapper);
        OH\_LOG\_ERROR(LOG\_APP, "napi\_create\_external\_buffer failed.");
        return nullptr;
    }
    // Use static variables as hook function parameters.
    static int hookArg = 42;
    static int hookParameter = 1;
    // Add a cleanup hook function for releasing resources when the environment exits.
    status = napi\_add\_env\_cleanup\_hook(env, Cleanup, &hookArg);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "Test Node-API napi\_add\_env\_cleanup\_hook failed.");
        return nullptr;
    }
    // Add the environment cleanup hook function. The hook function is not removed here to make it called to simulate some cleanup operations, such as releasing resources and closing files, when the ArkTS environment is destroyed.
    status = napi\_add\_env\_cleanup\_hook(env, Cleanup, &hookParameter);
    if (status != napi\_ok) {
        OH\_LOG\_ERROR(LOG\_APP, "Test Node-API napi\_add\_env\_cleanup\_hook failed.");
        return nullptr;
    }
    // Remove the environment cleanup hook function immediately.
    // The hook function can be removed when it is no longer needed. If you want the hook function to execute when the environment exits, do not remove it.
    napi\_remove\_env\_cleanup\_hook(env, Cleanup, &hookArg);
    napi\_remove\_env\_cleanup\_hook(env, Cleanup, &hookParameter);
    // Return the created external buffer object.
    return buffer;
}

API declaration:

export const napiEnvCleanUpHook: () => Object | undefined;

ArkTS code:

let wk = new worker.ThreadWorker('entry/ets/workers/worker.ts');
// Send a message to the worker thread.
wk.postMessage('test NapiEnvCleanUpHook');
// Process the message from the worker thread.
wk.onmessage = (message) => {
  hilog.info(0x0000, 'testTag', 'Test Node-API message from worker: %{public}s',
    JSON.stringify(message));
  wk.terminate();
};

import { hilog } from '@kit.PerformanceAnalysisKit';
import { worker } from '@kit.ArkTS';
import testNapi from 'libentry.so';

let parent = worker.workerPort;
// Process messages from the main thread.
parent.onmessage = (message) => {
  hilog.info(0x0000, 'testTag', 'Test Node-API message from main thread: %{public}s', JSON.stringify(message));
  // Send a message to the main thread.
  parent.postMessage('Test Node-API worker:' + testNapi.napiEnvCleanUpHook());
};

For details about the worker development, see:

[Worker Introduction](../../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md)

## napi\_add\_async\_cleanup\_hook

Call **napi\_add\_async\_cleanup\_hook** to add an async cleanup hook function, which will be executed asynchronously when the environment exits. Unlike a sync hook, an async hook allows a longer operation without blocking the process exit.

## napi\_remove\_async\_cleanup\_hook

Call **napi\_remove\_async\_cleanup\_hook** to remove an async cleanup hook function that is no longer required.

CPP code:

typedef struct {
    napi\_env env;
    void \*testData;
    uv\_async\_s asyncUv;
    napi\_async\_cleanup\_hook\_handle cleanupHandle;
} AsyncContent;

// Delete the async work object and remove the hook function.
static void FinalizeWork(uv\_handle\_s \*handle)
{
    AsyncContent \*asyncData = reinterpret\_cast<AsyncContent \*>(handle->data);
    // Remove the hook function from the environment when it is no longer required.
    napi\_status result = napi\_remove\_async\_cleanup\_hook(asyncData->cleanupHandle);
    if (result != napi\_ok) {
        napi\_throw\_error(asyncData->env, nullptr, "Test Node-API napi\_remove\_async\_cleanup\_hook failed");
    }
    // Release AsyncContent.
    free(asyncData);
}

// Asynchronously clear the environment.
static void AsyncWork(uv\_async\_s \*async)
{
    // Perform cleanup operations, for example, release the dynamically allocated memory.
    AsyncContent \*asyncData = reinterpret\_cast<AsyncContent \*>(async->data);
    if (asyncData != nullptr && asyncData->testData != nullptr) {
        free(asyncData->testData);
        asyncData->testData = nullptr;
    }
    // Close the libuv handle and trigger the FinalizeWork callback to clear the handle.
    uv\_close((uv\_handle\_s \*)async, FinalizeWork);
}

// Create and trigger an async cleanup operation in an event loop.
static void AsyncCleanup(napi\_async\_cleanup\_hook\_handle handle, void \*info)
{
    AsyncContent \*data = reinterpret\_cast<AsyncContent \*>(info);
    // Obtain a libuv loop instance and initialize a handle for subsequent async work.
    uv\_loop\_s \*uvLoop;
    napi\_get\_uv\_event\_loop(data->env, &uvLoop);
    uv\_async\_init(uvLoop, &data->asyncUv, AsyncWork);

    data->asyncUv.data = data;
    data->cleanupHandle = handle;
    // Send an async signal to trigger the AsyncWork function to perform cleanup.
    uv\_async\_send(&data->asyncUv);
}

static napi\_value NapiAsyncCleanUpHook(napi\_env env, napi\_callback\_info info)
{
    // Allocate the AsyncContent memory.
    AsyncContent \*data = reinterpret\_cast<AsyncContent \*>(malloc(sizeof(AsyncContent)));
    // ...
    data->env = env;
    data->cleanupHandle = nullptr;
    // Allocate memory and copy string data.
    const char \*testDataStr = "TestNapiAsyncCleanUpHook";
    data->testData = strdup(testDataStr);
    if (data->testData == nullptr) {
        free(data);
        napi\_throw\_error(env, nullptr, "Test Node-API data->testData is nullptr");
        return nullptr;
    }
    // Add an async cleanup hook function.
    napi\_status status = napi\_add\_async\_cleanup\_hook(env, AsyncCleanup, data, &data->cleanupHandle);
    if (status != napi\_ok) {
        free(data->testData);
        free(data);
        napi\_throw\_error(env, nullptr, "Test Node-API napi\_add\_async\_cleanup\_hook failed");
        return nullptr;
    }
    napi\_value result = nullptr;
    napi\_get\_boolean(env, true, &result);
    return result;
}

Since the uv.h library is used, add the following configuration to the CMakeLists file:

// CMakeLists.txt
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libuv.so)

API declaration:

export const napiAsyncCleanUpHook: () => boolean | undefined;

ArkTS code:

try {
  hilog.info(0x0000, 'testTag', 'Test Node-API napi\_add\_async\_cleanup\_hook: %{public}s',
    testNapi.napiAsyncCleanUpHook());
  // ...
} catch (error) {
  hilog.error(0x0000, 'testTag',
    'Test Node-API napi\_add\_async\_cleanup\_hook error.message: %{public}s',
    error.message);
  // ...
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
