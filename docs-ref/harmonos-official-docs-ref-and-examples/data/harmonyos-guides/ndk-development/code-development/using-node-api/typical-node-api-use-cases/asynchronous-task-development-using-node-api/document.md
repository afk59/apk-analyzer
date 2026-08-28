# Asynchronous Task Development Using Node-API

#### When to Use

For time-consuming operations, you can use [napi\_create\_async\_work](https://developer.huawei.com/consumer/en/doc/harmonyos-references/napi#napi_create_async_work) to create an asynchronous work object to prevent the ArkTS thread where env exists from being blocked while ensuring the performance and response speed of your application. You can use asynchronous work objects in the following scenarios:

-   File operations: You can use asynchronous work objects in complex file operations or when a large file needs to be read to prevent the ArkTS thread where env exists from being blocked.
    
-   Network request: When your application needs to wait for a response to a network request, using an asynchronous worker object can improve its response performance without affecting the main thread.
    
-   Database operation: Using asynchronous work objects in complex database query or write operations can improve the concurrency performance of your application without compromising the running of the main thread.
    
-   Image processing: When large images need to be processed or complex image algorithms need to be executed, asynchronous work objects can ensure normal running of the main thread and improve the real-time performance of your application.
    

**napi\_queue\_async\_work** uses the **uv\_queue\_work** capability and manages the lifecycle of **napi\_value** in the callback.

You can use a callback or a promise to implement asynchronous calls as required. The following is sample code for the two methods:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/ljic6C2ES-mGErcwEVaROQ/en-us_image_0000002568765019.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062131Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5BCA625EB6658265F2AF9630B64971093F9D2DBA4F7D5749C1209B4073223D7)

#### Example (Promise)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/jEtpmW_SS5yxN2NVp2Co2g/en-us_image_0000002537765294.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062131Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4D39F695C2DE6A299132AB1B16849F36D0AC4FB81AFCABB9400A0F1056A4E11)

1.  Configure the **CMakeLists.txt** file.
    
    \# the minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.5.0)
    project(NodeAPIAsynchronousTask)
    
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    if(DEFINED PACKAGE\_FIND\_FILE)
        include(${PACKAGE\_FIND\_FILE})
    endif()
    
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    
    add\_library(entry SHARED napi\_init.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so)
    
    add\_library(entry1 SHARED callback.cpp)
    target\_link\_libraries(entry1 PUBLIC libace\_napi.z.so)
    
2.  Call **napi\_create\_async\_work** to create an asynchronous work object, and call **napi\_queue\_async\_work** to add the object to a queue.
    
    #include "napi/native\_api.h"
    // Data context provided by the caller. The data is transferred to the execute and complete functions.
    struct CallbackData {
        napi\_async\_work asyncWork = nullptr;
        napi\_deferred deferred = nullptr;
        napi\_ref callback = nullptr;
        double args = 0;
        double result = 0;
    };
    
    // ...
    
    static napi\_value AsyncWork(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 1;
        napi\_value args\[1\];
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
    
        napi\_value promise = nullptr;
        napi\_deferred deferred = nullptr;
        napi\_create\_promise(env, &deferred, &promise);
    
        auto callbackData = new CallbackData();
        callbackData->deferred = deferred;
        napi\_get\_value\_double(env, args\[0\], &callbackData->args);
    
        napi\_value resourceName = nullptr;
        napi\_create\_string\_utf8(env, "AsyncCallback", NAPI\_AUTO\_LENGTH, &resourceName);
        // Create an asynchronous work object.
        napi\_create\_async\_work(env, nullptr, resourceName, ExecuteCB, CompleteCB, callbackData, &callbackData->asyncWork);
        // Add the asynchronous work object to a queue.
        napi\_queue\_async\_work(env, callbackData->asyncWork);
    
        return promise;
    }
    
3.  Define the first callback of the asynchronous work object. This callback is executed in a worker thread to process specific service logic.
    
    static void ExecuteCB(napi\_env env, void \*data)
    {
        CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data);
        callbackData->result = callbackData->args;
    }
    
4.  Define the second callback of the asynchronous work object. This callback is executed in the main thread to return the result to the ArkTS side.
    
    static void CompleteCB(napi\_env env, napi\_status status, void \*data)
    {
        CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data);
        napi\_value result = nullptr;
        napi\_create\_double(env, callbackData->result, &result);
        if (callbackData->result > 0) {
            napi\_resolve\_deferred(env, callbackData->deferred, result);
        } else {
            napi\_reject\_deferred(env, callbackData->deferred, result);
        }
    
        napi\_delete\_async\_work(env, callbackData->asyncWork);
        delete callbackData;
        callbackData = nullptr;
    }
    
5.  Register the module and call the API from the ArkTS side.
    
    // Initialize the module.
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "asyncWork", nullptr, AsyncWork, nullptr, nullptr, nullptr, napi\_default, nullptr }
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    
    Description of the API in the .d.ts file.
    
    // index.d.ts
    export const asyncWork: (data: number) => Promise<number>;
    
    API calls from the ArkTS side.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import testNapi from 'libentry.so';
    
    testNapi.asyncWork(1024).then((result: number) => {
      hilog.info(0x0000, 'XXX', 'result is %{public}d', result);
    });
    
    Result: \*\*result is 1024\*\*
    

#### Example (Callback)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/mpnX7HLaTGe_sCfSXT8Oag/en-us_image_0000002537925234.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062131Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1999F273EA411B11332C2A69856B1E482A2BF650D5416DDED367410FBD750AA9)

1.  Call **napi\_create\_async\_work** to create an asynchronous work object, and call **napi\_queue\_async\_work** to add the object to a queue.
    
    #include "napi/native\_api.h"
    
    static constexpr int INT\_ARGS\_2 = 2; // Input parameter index.
    
    // Data context provided by the caller. The data is transferred to the execute and complete functions.
    struct CallbackData {
        napi\_async\_work asyncWork = nullptr;
        napi\_ref callbackRef = nullptr;
        double args\[2\] = {0};
        double result = 0;
    };
    
    // ...
    napi\_value AsyncWork(napi\_env env, napi\_callback\_info info)
    {
        size\_t argc = 3;
        napi\_value args\[3\];
        napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);
        auto asyncContext = new CallbackData();
        // Save the received parameters to callbackData.
        napi\_get\_value\_double(env, args\[0\], &asyncContext->args\[0\]);
        napi\_get\_value\_double(env, args\[1\], &asyncContext->args\[1\]);
        // Convert the callback to napi\_ref to extend its lifecycle to prevent it from being garbage-collected.
        napi\_create\_reference(env, args\[INT\_ARGS\_2\], 1, &asyncContext->callbackRef);
        napi\_value resourceName = nullptr;
        napi\_create\_string\_utf8(env, "asyncWorkCallback", NAPI\_AUTO\_LENGTH, &resourceName);
        // Create an asynchronous work object.
        napi\_create\_async\_work(env, nullptr, resourceName, ExecuteCB, CompleteCB,
                               asyncContext, &asyncContext->asyncWork);
        // Add the asynchronous work object to a queue.
        napi\_queue\_async\_work(env, asyncContext->asyncWork);
        return nullptr;
    }
    
2.  Define the first callback of the asynchronous work object. This callback is executed in a worker thread to process specific service logic.
    
    static void ExecuteCB(napi\_env env, void \*data)
    {
        CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data);
        callbackData->result = callbackData->args\[0\] + callbackData->args\[1\];
    }
    
3.  Define the second callback of the asynchronous work object. This callback is executed in the main thread to return the result to the ArkTS side.
    
    static void CompleteCB(napi\_env env, napi\_status status, void \*data)
    {
        CallbackData \*callbackData = reinterpret\_cast<CallbackData \*>(data);
        napi\_value callbackArg\[1\] = {nullptr};
        napi\_create\_double(env, callbackData->result, &callbackArg\[0\]);
        napi\_value callback = nullptr;
        napi\_get\_reference\_value(env, callbackData->callbackRef, &callback);
        // Execute the callback.
        napi\_value result;
        napi\_value undefined;
        napi\_get\_undefined(env, &undefined);
        napi\_call\_function(env, undefined, callback, 1, callbackArg, &result);
        // Delete the napi\_ref object and asynchronous work object.
        napi\_delete\_reference(env, callbackData->callbackRef);
        napi\_delete\_async\_work(env, callbackData->asyncWork);
        delete callbackData;
        callbackData = nullptr;
    }
    
4.  Register the module and call the API from the ArkTS side.
    
    The export method name is the same as that above. You can reuse the module registration code.
    
    // Initialize the module.
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            { "asyncWork", nullptr, AsyncWork, nullptr, nullptr, nullptr, napi\_default, nullptr }
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    
    Description of the API in the .d.ts file.
    
    export const asyncWork: (arg1: number, arg2: number, callback: (result: number) => void) => void;
    
    API calls from the ArkTS side.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import nativeModule from 'libentry1.so';
    let num1: number = 123;
    let num2: number = 456;
    
    nativeModule.asyncWork(num1, num2, (result: number) => {
      hilog.info(0x0000, 'XXX', 'result is %{public}d', result);
    });
    
    Result: \*\*result is 579\*\*
    

#### Child Thread Interaction Scenarios

-   The **napi\_queue\_async\_work** API creates a C++ child thread. Therefore, the native code can directly reuse the code that uses the callback mode. The following shows the usage differences on the ArkTS side.

## C++ and ArkTS Child Thread Interaction Based on [Worker](../../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/worker/document.md)

-   DevEco Studio supports generation of Worker templates with a single click. In the corresponding {moduleName} directory, right-click anywhere and choose **New > Worker** to automatically generate the Worker template files and configuration information. In this example, we will create a Worker named "Worker".

1.  Configure the Worker.
    
    "buildOption": {
      "sourceOption": {
        "workers": \[
          "./src/main/ets/workers/Worker.ets"
         \]
      },
    }
    
2.  Sample code of the worker thread.
    
    // entry/src/main/ets/workers/Worker.ets
    
    import nativeModule from 'libentry1.so';
    import { worker, MessageEvents } from '@kit.ArkTS';
    
    const port = worker.workerPort;
    
    port.onmessage = (e : MessageEvents) => {
        console.info('Worker thread received data:', e.data.num1 + ', ' + e.data.num2);
        nativeModule.asyncWork(e.data.num1, e.data.num2, (result: number) => {
            port.postMessage(result);
        });
    }
    
3.  ArkTS thread code.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { worker } from '@kit.ArkTS';
    let num1: number = 123;
    let num2: number = 456;
    
    const wk = new worker.ThreadWorker('entry/ets/workers/Worker.ets');
    wk.postMessage({num1, num2});
    wk.onmessage = (msg) => {
      console.info('result is:', msg.data);
      wk.terminate();
    }
    
    Execution result:
    Worker thread received data: 123, 456
    result is 579
    

## C++ and ArkTS Child Thread Interaction Based on [Taskpool](../../../../../application-framework/arkts/arkts-concurrency/multithreaded-concurrency/taskpool/document.md)

1.  ArkTS thread code.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { taskpool } from '@kit.ArkTS';
    import nativeModule from 'libentry1.so';
    let num1: number = 123;
    let num2: number = 456;
    
    @Concurrent
    function nativeCall(num1 : number, num2 : number): void {
      console.info('Taskpool thread received data:', + num1 + ', ' + num2);
      nativeModule.asyncWork(num1, num2, (result: number) => {
        hilog.info(0x0000, 'XXX', 'result is: %{public}d', result);
      });
    }
    
    async function testTaskpool() : Promise<void> {
      try {
        const task = new taskpool.Task(nativeCall, num1, num2);
        await taskpool.execute(task);
      } catch (e) {
        console.error(\`Taskpool execute error: ${e}\`);
      }
    }
    
    testTaskpool();
    
    Execution result:
    Taskpool thread received data: 123, 456
    result is 579
    

#### NOTE

-   When the **napi\_cancel\_async\_work** API is called, **napi\_ok** is returned regardless of whether the underlying UV fails. If the task fails to be canceled due to the underlying UV, the corresponding error value is transferred to **status** in the complete callback. You need to perform the corresponding operation based on the value of **status**.
-   It is recommended that the asynchronous work item of Node-API (**napi\_async\_work**) be used only once. After **napi\_queue\_async\_work** is called, you should release it through **napi\_delete\_async\_work** during or after the execution of the **complete** callback. The same **napi\_async\_work** can be released only once. Repeated release attempts will cause undefined behavior.
-   The **execute\_cb** of **napi\_async\_work** runs in an independent work thread, which is obtained from the uv thread pool. Different worker threads do not affect each other. The service logic in the **execute\_cb** function is executed in the worker thread instead of the original ArkTS thread. Therefore, you cannot use the input parameter **env** (the **env** of the original ArkTS thread) to construct **napi\_value**.
-   **napi\_async\_work** only ensures that **complete\_cb** is executed after **execute\_cb**. **execute\_cb** of different **napi\_async\_work** runs on their respective worker threads. Therefore, their execution sequence cannot be ensured. If tasks need to be executed in sequence, you are advised to use the **napi\_threadsafe\_function** APIs. For details, see [Thread Safety Development Using Node-API](../thread-safety-development-using-node-api/document.md).
