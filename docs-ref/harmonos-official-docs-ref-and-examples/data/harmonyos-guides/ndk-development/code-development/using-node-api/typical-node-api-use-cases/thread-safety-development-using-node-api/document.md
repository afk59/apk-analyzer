# Thread Safety Development Using Node-API

#### When to Use

[napi\_create\_threadsafe\_function](https://developer.huawei.com/consumer/en/doc/harmonyos-references/napi#napi_create_threadsafe_function) is a Node-API used to create a thread-safe JS function, which can be called from multiple threads without race conditions or deadlocks. The following scenarios are involved:

-   Asynchronous computing: If a time-consuming computing or I/O operation needs to be performed, you can create a thread-safe function to have the computing or I/O operation executed in a dedicated thread. This ensures normal running of the main thread and improves the response speed of your application.
    
-   Data sharing: When multiple threads need to access the same data, using a thread-safe function can prevent race conditions or deadlocks during data read and write operations.
    
-   Multithread programming: In the case of multithread programming, a thread-safe function can ensure communication and synchronization between multiple threads.
    

#### Example

1.  Configure the **CMakeLists.txt** file.
    
    \# the minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.5.0)
    project(MyApplication3)
    
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    if(DEFINED PACKAGE\_FIND\_FILE)
        include(${PACKAGE\_FIND\_FILE})
    endif()
    add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
    add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    
    add\_library(entry SHARED napi\_init.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    
    add\_library(entry1 SHARED thread\_safety.cpp)
    target\_link\_libraries(entry1 PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    
2.  Define a thread-safe function at the native entry.
    
    #include "napi/native\_api.h"
    #include "hilog/log.h"
    #include <future>
    
    static constexpr int INT\_ARG\_2 = 2; // Input parameter index.
    static constexpr int INT\_BUF\_32 = 32; // Input parameter index.
    
    struct CallbackData {
        napi\_threadsafe\_function tsfn;
        napi\_async\_work work;
    };
    
    // Call ExecuteWork in the worker thread and execute the thread-safe function.
    static void ExecuteWork(napi\_env env, void \*data)
    {
        CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data);
        std::promise<std::string> promise;
        auto future = promise.get\_future();
        napi\_acquire\_threadsafe\_function(callbackData->tsfn);
        napi\_call\_threadsafe\_function(callbackData->tsfn, &promise, napi\_tsfn\_nonblocking);
        napi\_release\_threadsafe\_function(callbackData->tsfn, napi\_tsfn\_release);
        try {
            auto result = future.get();
            OH\_LOG\_INFO(LOG\_APP, "XXX, Result from JS %{public}s", result.c\_str());
        } catch (const std::exception &e) {
            OH\_LOG\_INFO(LOG\_APP, "XXX, Result from JS %{public}s", e.what());
        }
    }
    
    static napi\_value ResolvedCallback(napi\_env env, napi\_callback\_info info)
    {
        void \*data = nullptr;
        size\_t argc = 1;
        napi\_value argv\[1\];
        if (napi\_get\_cb\_info(env, info, &argc, argv, nullptr, &data) != napi\_ok) {
            return nullptr;
        }
        size\_t result = 0;
        char buf\[32\] = {0};
        napi\_get\_value\_string\_utf8(env, argv\[0\], buf, INT\_BUF\_32, &result);
        reinterpret\_cast<std::promise<std::string> \*>(data)->set\_value(std::string(buf));
        return nullptr;
    }
    
    static napi\_value RejectedCallback(napi\_env env, napi\_callback\_info info)
    {
        void \*data = nullptr;
        if (napi\_get\_cb\_info(env, info, nullptr, nullptr, nullptr, &data) != napi\_ok) {
            return nullptr;
        }
        reinterpret\_cast<std::promise<std::string> \*>(data)->set\_exception(
            std::make\_exception\_ptr(std::runtime\_error("Error in jsCallback")));
        return nullptr;
    }
    
    static void CallJs(napi\_env env, napi\_value jsCb, void \*context, void \*data)
    {
        if (env == nullptr) {
            return;
        }
        napi\_value undefined = nullptr;
        napi\_value promise = nullptr;
        napi\_get\_undefined(env, &undefined);
        napi\_call\_function(env, undefined, jsCb, 0, nullptr, &promise);
        napi\_value thenFunc = nullptr;
        if (napi\_get\_named\_property(env, promise, "then", &thenFunc) != napi\_ok) {
            return;
        }
        napi\_value resolvedCallback;
        napi\_value rejectedCallback;
        napi\_create\_function(env, "resolvedCallback", NAPI\_AUTO\_LENGTH, ResolvedCallback, data, &resolvedCallback);
        napi\_create\_function(env, "rejectedCallback", NAPI\_AUTO\_LENGTH, RejectedCallback, data, &rejectedCallback);
        napi\_value argv\[2\] = {resolvedCallback, rejectedCallback};
        napi\_call\_function(env, promise, thenFunc, INT\_ARG\_2, argv, nullptr);
    }
    
    // After the task is complete, clear and reclaim resources.
    static void WorkComplete(napi\_env env, napi\_status status, void \*data)
    {
        CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data);
        napi\_release\_threadsafe\_function(callbackData->tsfn, napi\_tsfn\_release);
        napi\_delete\_async\_work(env, callbackData->work);
        callbackData->tsfn = nullptr;
        callbackData->work = nullptr;
        delete callbackData;
    }
    
    static napi\_value StartThread(napi\_env env, napi\_callback\_info info)
    {
        CallbackData \*callbackData = new CallbackData();
        size\_t argc = 1;
        napi\_value jsCb = nullptr;
        napi\_get\_cb\_info(env, info, &argc, &jsCb, nullptr, nullptr);
    
        // Create a thread-safe function.
        napi\_value resourceName = nullptr;
        napi\_create\_string\_utf8(env, "Thread-safe Function Demo", NAPI\_AUTO\_LENGTH, &resourceName);
        napi\_create\_threadsafe\_function(env, jsCb, nullptr, resourceName, 0, 1, callbackData, nullptr, callbackData, CallJs,
                                        &callbackData->tsfn);
    
        // Create an asynchronous work object.
        // ExecuteWork is executed on a non-JS thread created by libuv.
        // napi\_create\_async\_work is used to simulate the scenario where the napi\_call\_threadsafe\_function API is used to submit a task to the JS thread from a non-JS thread.
        napi\_create\_async\_work(env, nullptr, resourceName, ExecuteWork, WorkComplete, callbackData, &callbackData->work);
    
        // Add the asynchronous work object to the asynchronous task queue.
        napi\_queue\_async\_work(env, callbackData->work);
        return nullptr;
    }
    
3.  Module registration.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"startThread", nullptr, StartThread, nullptr, nullptr, nullptr, napi\_default, nullptr}
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry1",
        .nm\_priv = ((void \*)0),
        .reserved = {0},
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }
    
4.  ArkTS code:
    
    export const startThread: (a: () => Promise<string>) => void;
    
    Import the header files.
    
    import nativeModule from 'libentry1.so';
    
    // index.ets
    let callback = (): Promise<string> => {
      return new Promise((resolve) => {
        setTimeout(() => {
          resolve('string from promise');
        }, 5000);
      });
    }
    nativeModule.startThread(callback);
    

#### Child Thread Interaction Scenarios

-   **napi\_threadsafe\_function** is used the same way in the main thread and child thread. The following is an example of using **napi\_threadsafe\_function** in the child thread.

## C++ and ArkTS Child Thread Interaction Based on [Worker](../../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md)

1.  Configure the **CMakeLists.txt** file.
    
    \# the minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.5.0)
    project(MyApplication3)
    
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    if(DEFINED PACKAGE\_FIND\_FILE)
        include(${PACKAGE\_FIND\_FILE})
    endif()
    add\_definitions( "-DLOG\_DOMAIN=0xd0d0" )
    add\_definitions( "-DLOG\_TAG=\\"testTag\\"" )
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    
    add\_library(entry SHARED napi\_init.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    
    add\_library(entry1 SHARED thread\_safety.cpp)
    target\_link\_libraries(entry1 PUBLIC libace\_napi.z.so libhilog\_ndk.z.so)
    
2.  Define a thread-safe function and create a child thread at the native entry.
    
    #include "napi/native\_api.h"
    #include "hilog/log.h"
    #include <future>
    // ...
    
    struct TsfnContext {
        napi\_ref callbackRef;
    };
    
    struct ThreadData {
        std::string inputStr;
        napi\_threadsafe\_function tsfn;
    };
    
    // C++ child thread.
    void NativeThread(void\* arg)
    {
        auto\* data = static\_cast<ThreadData\*>(arg);
        OH\_LOG\_INFO(LOG\_APP, "\[C++ SubThread\] Received from Worker: %{public}s\\n", data->inputStr.c\_str());
        std::string str = "Hello from C++!";
        std::string msg = "Echo of " + str;
        char\* cstr = strdup(msg.c\_str());
        napi\_call\_threadsafe\_function(data->tsfn, cstr, napi\_tsfn\_nonblocking);
        napi\_release\_threadsafe\_function(data->tsfn, napi\_tsfn\_release);
        delete data;
    }
    
    // Callback executed in the JS thread.
    void CallJsCallback(napi\_env env, napi\_value jsCallback, void\* context, void\* data)
    {
        if (data == nullptr) {
            return;
        }
        char\* message = static\_cast<char\*>(data);
        napi\_value jsStr;
        napi\_create\_string\_utf8(env, message, NAPI\_AUTO\_LENGTH, &jsStr);
        napi\_value global;
        napi\_get\_global(env, &global);
        napi\_value result;
        napi\_call\_function(env, global, jsCallback, 1, &jsStr, &result);
        free(message);
    }
    
    // Callback triggered when the tsfn is destroyed.
    void TsfnFinalizeCallback(napi\_env env, void\* finalizeData, void\* finalizeHint)
    {
        TsfnContext\* ctx = static\_cast<TsfnContext\*>(finalizeData);
        if (ctx && ctx->callbackRef) {
            napi\_delete\_reference(env, ctx->callbackRef);
            delete ctx;
        }
    }
    
    // Entry function called by ArkTS.
    napi\_value StartWithCallback(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 2;
        napi\_value args\[2\];
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        size\_t length = 0;
        napi\_status status = napi\_get\_value\_string\_utf8(env, args\[0\], nullptr, 0, &length);
        if (status != napi\_ok) {
            OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_value\_string\_utf8 failed");
            return nullptr;
        }
        char\* inputStr = new char\[length + 1\];
        std::fill(inputStr, inputStr + (length + 1), 0);
        status = napi\_get\_value\_string\_utf8(env, args\[0\], inputStr, length + 1, &length);
        if (status != napi\_ok) {
            if (inputStr) {
                delete\[\] inputStr;
            }
            OH\_LOG\_ERROR(LOG\_APP, "napi\_get\_value\_string\_utf8 failed");
            return nullptr;
        }
        std::string inputString(inputStr, length);
        delete\[\] inputStr;
        TsfnContext\* ctx = new TsfnContext();
        napi\_create\_reference(env, args\[1\], 1, &ctx->callbackRef);
        napi\_value resourceName;
        napi\_create\_string\_utf8(env, "TSFN\_WorkerToCpp", NAPI\_AUTO\_LENGTH, &resourceName);
        napi\_threadsafe\_function tsfn;
        napi\_create\_threadsafe\_function(env, args\[1\], nullptr, resourceName,
                                        0, 1, ctx, TsfnFinalizeCallback, nullptr, CallJsCallback, &tsfn);
        auto\* threadData = new ThreadData{std::move(inputString), tsfn};
        std::thread nativethread(NativeThread, threadData);
        nativethread.detach();
        return nullptr;
    }
    
3.  Module registration.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"startWithCallback", nullptr, StartWithCallback, nullptr, nullptr, nullptr, napi\_default, nullptr}
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry1",
        .nm\_priv = ((void \*)0),
        .reserved = {0},
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void) { napi\_module\_register(&demoModule); }
    
4.  DevEco Studio supports generation of Worker templates with a single click. In the corresponding {moduleName} directory, right-click anywhere and choose **New > Worker** to automatically generate the Worker template files and configuration information. In this example, we will create a Worker named "Worker".
    
    "buildOption": {
      "sourceOption": {
        "workers": \[
          "./src/main/ets/workers/Worker.ets"
         \]
      },
    }
    
5.  Sample code of the worker thread.
    
    // entry/src/main/ets/workers/Worker.ets
    
    import nativeModule from 'libentry1.so';
    import { worker, MessageEvents } from '@kit.ArkTS';
    
    const port = worker.workerPort;
    
    port.onmessage = (e: MessageEvents) => {
      console.info('Worker thread received:' + e.data);
      nativeModule.startWithCallback('Hello', (result: string) => {
        console.info('\[Worker\] Got from native:', result);
        port.postMessage(result);
      });
    }
    
6.  Description of the API in the .d.ts file.
    
    export const startWithCallback: (input: string, callback: (msg: string) => void) => void;
    
7.  Call APIs from ArkTS.
    
    import nativeModule from 'libentry1.so';
    import { worker } from '@kit.ArkTS';
    
    // index.ets
    const wk = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
    wk.postMessage('Start');
    wk.onmessage = (msg) => {
      console.info('\[Main\] Received:', msg.data);
      wk.terminate();
    }
    
    Execution result:
    Worker thread received:Start
    \[C++ SubThread\] Received from Worker: Hello
    \[Worker\] Got from native: Echo of Hello from C++!
    \[Main\] Received: Echo of Hello from C++
    

## C++ and ArkTS Child Thread Interaction Based on [Taskpool](../../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/taskpool/document.md)

1.  The implementation code and module registration on the native side are the same as those in "C++ and ArkTS Child Thread Interaction Based on Worker". You can directly reuse the code.
    
2.  ArkTS code:
    
    import nativeModule from 'libentry1.so';
    import { taskpool } from '@kit.ArkTS';
    
    @Concurrent
    function nativeCall(input : string): void {
      console.info('Taskpool thread received:%s', input);
      nativeModule.startWithCallback('Hello', (result: string) => {
        console.info('\[Taskpool\] Got from native:', result);
      });
    }
    
    async function testTaskpool() : Promise<void> {
      try {
        const task = new taskpool.Task(nativeCall, 'Start');
        await taskpool.execute(task);
      } catch (e) {
        console.error(\`Taskpool execute error: ${e}\`);
      }
    }
    
    // index.ets
    testTaskpool();
    
    Execution result:
    Taskpool thread received:Start
    \[C++ SubThread\] Received from Worker: Hello
    \[Taskpool\] Got from native: Echo of Hello from C++!
