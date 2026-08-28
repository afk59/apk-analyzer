# FAQs About Memory Leaks

#### Is there any mechanism to check whether napi\_ref leaks

-   Question: When **napi\_create\_reference** is used to create a reference to a JS object, **napi\_delete\_reference** needs to be used to release the JS object. If **napi\_delete\_reference** is not used, the JS object memory may leak. Is there any mechanism to check or test whether **napi\_ref** leaks?
-   Answer:

Use Allocation provided by DevEco Studio.

For details, see [Memory Analysis: Allocation](../../../../../performance-optimization/memory-analysis-allocation/document.md).

The internal implementation of the **napi\_create\_reference** API creates a C++ object. Therefore, if you forget to use the **napi\_delete\_reference** API, the new C++ object will leak. In this case, you can use Allocation to print the allocation stack of the unreleased objects, where you can check whether **napi\_ref** leaks.

#### How do I locate and resolve memory leaks during Node-API development

The memory usage increases when the button is clicked, and the memory cannot be reclaimed even if GC is triggered. How do I locate and resolve memory leaks during Node-API development?

-   Answer:

You need to understand the Node-API lifecycle mechanism. The references are as follows:

[Performing Lifecycle Management Using Node-API](../../node-api-guides/performing-lifecycle-management-using-node-api/document.md)

Common causes of memory leaks during Node-API development:

1.  **napi\_value** is not managed by **napi\_handle\_scope**. As a result, the ArkTS object held by **napi\_value** cannot be released. This problem often occurs in [direct use of uv\_queue\_work](../../node-api-development-specifications/document.md#asynchronous-tasks). To solve this problem, add the **napi\_open\_handle\_scope** and **napi\_close\_handle\_scope** APIs.
    
    You can analyze the snapshot to locate the cause of the leak. If the **distance** of the leaked ArkTS object is **1**, the object may be held by native (**napi\_value** is a pointer to the native owner), and **napi\_value** is not within the range of **napi\_handle\_scope**.
    
2.  A strong reference (with the **initial\_refcount** parameter greater than 0) is created for the ArkTS object using **napi\_create\_reference**, and the reference is not deleted. As a result, the ArkTS object cannot be reclaimed. The **napi\_create\_reference** API creates a C++ object internally. Therefore, both the ArkTS object and native object are leaked. You can use Allocation to capture the native object leak stack and check whether stack frames related to **napi\_create\_reference** exist.
    
    For details, see [Memory Analysis: Allocation](../../../../../performance-optimization/memory-analysis-allocation/document.md).
    
3.  The leaked object is held by another active ArkTS object. In this case, check the owner of the leaked object using snapshot.
    

#### What should I do if memory leaks when napi\_threadsafe\_function is used

When **napi\_threadsafe\_function** (tsfn for short) is used, **napi\_acquire\_threadsafe\_function** is often called to change the reference count of tsfn to ensure that tsfn is not released unexpectedly. When all the tsfn calls are complete, **napi\_release\_threadsafe\_function** should be called in **napi\_tsfn\_release** mode in a timely manner to ensure that the reference count returns to the value before **napi\_acquire\_threadsafe\_function** is called. tsfn can be correctly released only when the reference count is **0**.

When **env** is about to exit but the reference count of tsfn is not 0, **napi\_release\_threadsafe\_function** should be called in **napi\_tsfn\_abort** mode to ensure that tsfn is not held or used by **env** after **env** is released. If **env** continues to hold tsfn after exiting, the application may crash.

The following code shows how to register **env\_cleanup** to ensure that tsfn is no longer held by **env** after **env** exits.

//napi\_init.cpp
#include "napi/native\_api.h"
#include <hilog/log.h> // To output logs, link libhilog\_ndk.z.so.
#include <thread> // Include the thread module to create and manage threads.
#include <unistd.h> // Include unistd.h to suspend the execution of the calling thread.

// Define the log domain and tag.
#undef LOG\_DOMAIN
#undef LOG\_TAG
#define LOG\_DOMAIN 0x2342
#define LOG\_TAG "MY\_TSFN\_DEMO"

/\*
  To construct a scenario in which the env lifecycle is shorter than the native lifecycle,
  the following uses worker, taskpool, and napi\_create\_ark\_runtime
  to create an ArkTS running environment for a worker thread and manually stop the thread in advance.
\*/

// Define a struct to simulate the scenario where tsfn is stored.
class MyTsfnContext {
public:
// MyTsfnContext is constructed only in an ArkTS thread because Node-API is used.
MyTsfnContext(napi\_env env, napi\_value workName) {
    // Register the env\_cleanup\_hook function.
    napi\_add\_env\_cleanup\_hook(env, Cleanup, this);
    // Create a thread-safe function.
    if (napi\_create\_threadsafe\_function(env, nullptr, nullptr, workName, 1, 1, this,
            TsfnFinalize, this, TsfnCallJs, &tsfn\_) != napi\_ok) {
        OH\_LOG\_INFO(LOG\_APP, "tsfn is created failed");
        return;
    };
};

~MyTsfnContext() { OH\_LOG\_INFO(LOG\_APP, "MyTsfnContext is deconstructed"); };

napi\_threadsafe\_function GetTsfn() {
    std::unique\_lock<std::mutex> lock(mutex\_);
    return tsfn\_;
}

bool Acquire() {
    if (GetTsfn() == nullptr) {
        return false;
    };
    return (napi\_acquire\_threadsafe\_function(GetTsfn()) == napi\_ok);
};

bool Release() {
    if (GetTsfn() == nullptr) {
        return false;
    };
    return (napi\_release\_threadsafe\_function(GetTsfn(), napi\_tsfn\_release) == napi\_ok);
};

bool Call(void \*data) {
    if (GetTsfn() == nullptr) {
        return false;
    };
    return (napi\_call\_threadsafe\_function(GetTsfn(), data, napi\_tsfn\_blocking) == napi\_ok);
};

private:
// Ensure correct read and write of tsfn by multiple threads.
std::mutex mutex\_;
napi\_threadsafe\_function tsfn\_ = nullptr;

// Call napi\_add\_env\_cleanup\_hook.
static void Cleanup(void \*data) {
    MyTsfnContext \*that = reinterpret\_cast<MyTsfnContext \*>(data);
    napi\_threadsafe\_function tsfn = that->GetTsfn();
    std::unique\_lock<std::mutex> lock(that->mutex\_);
    that->tsfn\_ = nullptr;
    lock.unlock();
    OH\_LOG\_WARN(LOG\_APP, "cleanup is called");
    napi\_release\_threadsafe\_function(tsfn, napi\_tsfn\_abort);
};

// Callback to be invoked when tsfn is released.
static void TsfnFinalize(napi\_env env, void \*data, void \*hint) {
    MyTsfnContext \*ctx = reinterpret\_cast<MyTsfnContext \*>(data);
    OH\_LOG\_INFO(LOG\_APP, "tsfn is released");
    napi\_remove\_env\_cleanup\_hook(env, MyTsfnContext::Cleanup, ctx);
    // Cleanup releases the thread-safe function in advance. To avoid UAF, enable the caller to trigger the release.
    if (ctx->GetTsfn() != nullptr) {
        OH\_LOG\_INFO(LOG\_APP, "ctx is released");
        delete ctx;
    }
};

// Callback sent by tsfn to the ArkTS thread for execution.
static void TsfnCallJs(napi\_env env, napi\_value func, void \*context, void \*data) {
    MyTsfnContext \*ctx = reinterpret\_cast<MyTsfnContext \*>(context);
    char \*str = reinterpret\_cast<char \*>(data);
    OH\_LOG\_INFO(LOG\_APP, "tsfn is called, data is: \\"%{public}s\\"", str);
    // The service logic is omitted, which should include the logic for releasing resources that you create.
};
};

// Register the myTsfnDemo method with the module Index.d.ts. The myTsfnDemo method is defined as follows:
// export const myTsfnDemo: () => void;
napi\_value MyTsfnDemo(napi\_env env, napi\_callback\_info info) {
    OH\_LOG\_ERROR(LOG\_APP, "MyTsfnDemo is called");
    napi\_value workName = nullptr;
    napi\_create\_string\_utf8(env, "MyTsfnWork", NAPI\_AUTO\_LENGTH, &workName);
    MyTsfnContext \*myContext = new MyTsfnContext(env, workName);
    if (myContext->GetTsfn() == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "failed to create tsfn");
        delete myContext;
        return nullptr;
    };
    char \*data0 = new char\[\]{"Im call in ArkTS Thread"};
    if (!myContext->Call(data0)) {
        OH\_LOG\_INFO(LOG\_APP, "call tsfn failed");
    };

    // Create a thread to simulate an asynchronous operation.
    std::thread(
        \[\](MyTsfnContext \*myCtx) {
            if (!myCtx->Acquire()) {
                OH\_LOG\_ERROR(LOG\_APP, "acquire tsfn failed");
                return;
            };
            char \*data1 = new char\[\]{"Im call in std::thread"};
            // This operation is optional and used only to check whether the asynchronous tsfn is still valid.
            if (!myCtx->Call(data1)) {
                OH\_LOG\_ERROR(LOG\_APP, "call tsfn failed");
            };
            // Suspend the thread for 5 seconds to simulate a time-consuming operation, which is not complete when env exits.
            sleep(5);
            // When the asynchronous operation is complete, tsfn has been released and set to nullptr.
            char \*data2 = new char\[\]{"Im call after work"};
            if (!myCtx->Call(data2) && !myCtx->Release()) {
                OH\_LOG\_ERROR(LOG\_APP, "call and release tsfn failed");
                delete myCtx;
            }
        },
        myContext)
        .detach();
    return nullptr;
};

//Index.d.ts
export const myTsfnDemo: () => void;

The following is the main thread logic, which creates worker threads and instruct them to execute tasks.

// Main thread Index.ets
import  {worker, MessageEvents } from '@kit.ArkTS';

const mWorker = new worker.ThreadWorker('../workers/worker');
mWorker.onmessage = (e: MessageEvents) => {
    const action: string | undefined = e.data?.action;
    if (action === 'kill') {
        mWorker.terminate();
    }
}

// The registration of the triggering mode is omitted.
mWorker.postMessage({action: 'tsfn-demo'});

The following is the worker thread logic, which triggers native tasks.

// worker.ets
import  {worker, ThreadWorkerGlobalScope, MessageEvents} from '@kit.ArkTS';
import napiModule from 'libentry.so'; // libentry.so is the module name of the Node-API library.

const workerPort: ThreadWorkerGlobalScope = worker.workerPort;

workerPort.onmessage = (e: MessageEvents) => {
    const action: string | undefined = e.data?.action;
    if (action === 'tsfn-demo') {
        // Trigger the tsfn demo in C++.
        napiModule.myTsfnDemo();
        // Instruct the main thread to terminate the worker.
        workerPort.postMessage({action: 'kill'});
    };
}
