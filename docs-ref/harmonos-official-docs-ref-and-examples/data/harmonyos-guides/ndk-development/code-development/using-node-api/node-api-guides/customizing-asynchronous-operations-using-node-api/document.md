# Customizing Asynchronous Operations Using Node-API

#### Introduction

Node-API provides APIs for customizing asynchronous (async for short) operations to handle time-consuming tasks that may block event loops while maintaining quick response and high performance of applications.

#### Basic Concepts

Async operations are used to complete I/O-intensive or compute-intensive tasks, which usually need to be executed without blocking the main thread. Before you get started, understand the following concepts:

-   Async model: Node-API provides APIs that implement async operations using a promise or a callback. Promise is a programming model based on future values. It allows results of async operations to be encapsulated in objects and called in a chain. Callback is a traditional async programming mode. It uses callback functions to process async operation results.
-   Temporary result: When a native method (Node-API) is called, it immediately returns a temporary result to the ArkTS caller. The temporary result is usually a flag indicating an async operation being performed or a handle for subsequent processing of an async operation result.
-   Callback/Promise: When an async operation is complete, the result is returned to the ArkTS caller through a callback function or a promise object. This allows the processing of the subsequent logic after the async operation is complete.

#### Available APIs

The following table lists the APIs provided by the Node-API module for customizing async operations. You can use these APIs to implement ArkTS callbacks and manage the resource lifecycle in C/C++. These APIs help implement complex async operations and effective interaction with ArkTS. The following table lists the use cases of these APIs.

| API | Description |
| :-- | :-- |
| napi\_async\_init, napi\_async\_destroy | Creates/Destroys an async context. You can use these APIs to handle time-consuming tasks, such as file I/O operations and network requests, without blocking the main thread. You can use **napi\_async\_init** to create an async context for executing the task, and use **napi\_async\_destroy** after the task is complete to destroy and release related resources. |
| napi\_make\_callback | Executes an ArkTS callback function in an async context and returns the operation result to ArkTS. |
| napi\_open\_callback\_scope, napi\_close\_callback\_scope | Opens/Closes a callback scope. You can use these APIs to execute ArkTS code and manage its context during the async operation. |

#### Example

If you are just starting out with Node-API, see [Node-API Development Process](../../node-api-development-process/document.md). The following demonstrates only the C++ and ArkTS code involved in the APIs for customizing async operations.

## napi\_async\_init and napi\_async\_destroy

Use **napi\_async\_init** to create an async context, and use **napi\_async\_destroy** to destroy an async context. Note that these APIs do not support capabilities related to **async\_hook**.

## napi\_make\_callback

When writing a Node-API module, you must call the ArkTS callback function after an async operation is completed. You can use **napi\_async\_init** to create an async resource context, then use **napi\_make\_callback** to execute the ArkTS callback function.

## napi\_open\_callback\_scope, napi\_close\_callback\_scope

Use **napi\_open\_callback\_scope** to create a scope for the callback, and then use **napi\_close\_callback\_scope** to close the scope after the asynchronous operation is complete.

CPP code:

#include "napi/native\_api.h"

static constexpr int INT\_ARG\_2 = 2; // Input parameter index.
static constexpr int INT\_ARG\_3 = 3; // Input parameter index

static napi\_value AsynchronousWork(napi\_env env, napi\_callback\_info info)
{
    // Initialize an array to hold four parameters.
    size\_t argc = 4;
    napi\_value args\[4\] = {nullptr};
    // Obtain parameters from the callback information.
    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    // Extract resources, receiver objects, and functions from the parameters.
    napi\_value resource = args\[0\];
    napi\_value recv = args\[1\];
    napi\_value func = args\[INT\_ARG\_2\];
    napi\_value argv\[1\] = {nullptr};
    argv\[0\] = args\[INT\_ARG\_3\];
    // Obtain the function type.
    napi\_valuetype funcType;
    napi\_typeof(env, func, &funcType);
    // Create a string named "test".
    napi\_value resourceName = nullptr;
    napi\_create\_string\_utf8(env, "test", NAPI\_AUTO\_LENGTH, &resourceName);
    // Initialize the async context.
    napi\_async\_context context;
    napi\_status status = napi\_async\_init(env, resource, resourceName, &context);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_async\_init fail");
        return nullptr;
    }
    // Open a callback scope.
    napi\_callback\_scope scope = nullptr;
    status = napi\_open\_callback\_scope(env, resource, context, &scope);
    if (status != napi\_ok) {
        napi\_async\_destroy(env, context);
        napi\_throw\_error(env, nullptr, "napi\_open\_callback\_scope fail");
        return nullptr;
    }
    // Invoke the callback function defined.
    napi\_value result = nullptr;
    if (funcType == napi\_function) {
        napi\_make\_callback(env, context, recv, func, 1, argv, &result);
    } else {
        napi\_async\_destroy(env, context);
        napi\_close\_callback\_scope(env, scope);
        napi\_throw\_error(env, nullptr, "Unexpected argument type");
        return nullptr;
    }
    // Close the callback scope.
    status = napi\_close\_callback\_scope(env, scope);
    if (status != napi\_ok) {
        napi\_throw\_error(env, nullptr, "napi\_close\_callback\_scope fail");
        return nullptr;
    }
    // Destroy the async context.
    napi\_async\_destroy(env, context);
    return result;
}

API declaration:

index.d.ts

export const asynchronousWork: (object: Object, obj: Object, fun: Function, num: number) => number | undefined;

ArkTS code:

Modules to import:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';
import { process } from '@kit.ArkTS';

Test code:

try {
  hilog.info(0x0000, 'testTag', 'Test Node-API asynchronousWork: %{public}d',
    testNapi.asynchronousWork({}, process.ProcessManager, (num: number) => {
      return num;
    }, 123));
  // ···
} catch (error) {
  hilog.error(0x0000, 'testTag', 'Test Node-API asynchronousWork error: %{public}s', error.message);
  // ···
}

To print logs in the native CPP, add the following information to the **CMakeLists.txt** file and add the header file by using **#include "hilog/log.h"**.

// CMakeLists.txt
add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
