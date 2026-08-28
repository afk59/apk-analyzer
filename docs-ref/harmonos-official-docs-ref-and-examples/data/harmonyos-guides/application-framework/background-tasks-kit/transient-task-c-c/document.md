# Transient Task (C/C++)

#### When to Use

An application is suspended after it runs in the background for a short period of time. If the application needs to execute a short-time task in the background, for example, saving the status, it can request a transient task to extend the running time in the background.

#### Available APIs

The following table lists the common APIs. For details, see [transient\_task\_api.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-transient-task-api-h).

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_BackgroundTaskManager\_RequestSuspendDelay(const char \*reason, TransientTask\_Callback callback, TransientTask\_DelaySuspendInfo \*info)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-transient-task-api-h#oh_backgroundtaskmanager_requestsuspenddelay) | Requests a transient task. |
| [int32\_t OH\_BackgroundTaskManager\_GetRemainingDelayTime(int32\_t requestId, int32\_t \*delayTime)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-transient-task-api-h#oh_backgroundtaskmanager_getremainingdelaytime) | Obtains the remaining time of a transient task. |
| [int32\_t OH\_BackgroundTaskManager\_CancelSuspendDelay(int32\_t requestId)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-transient-task-api-h#oh_backgroundtaskmanager_cancelsuspenddelay) | Cancels a transient task. |
| [int32\_t OH\_BackgroundTaskManager\_GetTransientTaskInfo(TransientTask\_TransientTaskInfo \*transientTaskInfo)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-transient-task-api-h#oh_backgroundtaskmanager_gettransienttaskinfo) | Obtains all information about a transient task, including the remaining quota of the current day. |

#### How to Develop

## Encapsulating the Functions and Registering Modules in the napi\_init.cpp File

1.  Encapsulate the functions.
    
    #include "napi/native\_api.h"
    #include "transient\_task/transient\_task\_api.h"
    
    TransientTask\_DelaySuspendInfo delaySuspendInfo;
    const int32\_t TransientTask\_TIMER = 3;
    static void Callback(void)
    {
        // The transient task is about to end. The service cancels the transient task here.
        OH\_BackgroundTaskManager\_CancelSuspendDelay(delaySuspendInfo.requestId);
    }
    
    // Request a transient task.
    static napi\_value RequestSuspendDelay(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result;
        int32\_t res = OH\_BackgroundTaskManager\_RequestSuspendDelay("test", Callback, &delaySuspendInfo);
        if (res == 0) {
            napi\_create\_int32(env, delaySuspendInfo.requestId, &result);
        } else {
            napi\_create\_int32(env, -1, &result);
        }
        return result;
    }
    
    // Obtain the remaining time.
    static napi\_value GetRemainingDelayTime(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result;
        int32\_t delayTime = 0;
        int32\_t res = OH\_BackgroundTaskManager\_GetRemainingDelayTime(delaySuspendInfo.requestId, &delayTime);
        if (res == 0) {
            napi\_create\_int32(env, delayTime, &result);
        } else {
            napi\_create\_int32(env, -1, &result);
        }
        return result;
    }
    
    // Cancel the transient task.
    static napi\_value CancelSuspendDelay(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result;
        int32\_t res = OH\_BackgroundTaskManager\_CancelSuspendDelay(delaySuspendInfo.requestId);
        napi\_create\_int32(env, res, &result);
        return result;
    }
    
    // Obtain all transient task information.
    TransientTask\_TransientTaskInfo transientTaskInfo;
    
    static napi\_value GetTransientTaskInfo(napi\_env env, napi\_callback\_info info)
    {
        napi\_value result;
        napi\_create\_object(env, &result);
        int32\_t res = OH\_BackgroundTaskManager\_GetTransientTaskInfo(&transientTaskInfo);
        napi\_value napiRemainingQuota = nullptr;
        // The data is successfully obtained. The data is formatted and returned to the API.
        if (res == 0) {
            napi\_create\_int32(env, transientTaskInfo.remainingQuota, &napiRemainingQuota);
            napi\_set\_named\_property(env, result, "remainingQuota", napiRemainingQuota); // Format the total quota of the current day.
    
            napi\_value info {nullptr};
            napi\_create\_array(env, &info);
            uint32\_t count = 0;
            // Format all requested transient task information.
            for (int index = 0; index < TransientTask\_TIMER; index++) {
                if (transientTaskInfo.transientTasks\[index\].requestId == 0) {
                    continue;
                }
                
                napi\_value napiWork = nullptr;
                napi\_create\_object(env, &napiWork);
    
                napi\_value napiRequestId = nullptr;
                napi\_create\_int32(env, transientTaskInfo.transientTasks\[index\].requestId, &napiRequestId);
                napi\_set\_named\_property(env, napiWork, "requestId", napiRequestId);
    
                napi\_value napiActualDelayTime = nullptr;
                napi\_create\_int32(env, transientTaskInfo.transientTasks\[index\].actualDelayTime, &napiActualDelayTime);
                napi\_set\_named\_property(env, napiWork, "actualDelayTime", napiActualDelayTime);
    
                napi\_set\_element(env, info, count, napiWork);
                count++;
            }
            napi\_set\_named\_property(env, result, "transientTasks", info);
        } else {
            napi\_create\_int32(env, 0, &napiRemainingQuota);
            napi\_set\_named\_property(env, result, "remainingQuota", napiRemainingQuota);
            napi\_value info {nullptr};
            napi\_create\_array(env, &info);
            napi\_set\_named\_property(env, result, "transientTasks", info);
        }
        return result;
    }
    
2.  Register the functions.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"RequestSuspendDelay", nullptr, RequestSuspendDelay, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"GetRemainingDelayTime", nullptr, GetRemainingDelayTime, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"CancelSuspendDelay", nullptr, CancelSuspendDelay, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"GetTransientTaskInfo", nullptr, GetTransientTaskInfo, nullptr, nullptr, nullptr, napi\_default, nullptr },
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
3.  Register the module.
    
    static napi\_module demoModule = {
        .nm\_version = 1,
        .nm\_flags = 0,
        .nm\_filename = nullptr,
        .nm\_register\_func = Init,
        .nm\_modname = "entry",
        .nm\_priv = ((void\*)0),
        .reserved = { 0 },
    };
    
    extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
    {
        napi\_module\_register(&demoModule);
    }
    

## Declaring the Functions in the index.d.ts File

import backgroundTaskManager from '@kit.BackgroundTasksKit';

export const RequestSuspendDelay: () => number;
export const GetRemainingDelayTime: () => number;
export const CancelSuspendDelay: () => number;
export const GetTransientTaskInfo: () => backgroundTaskManager.TransientTaskInfo;

## Calling the Functions in the index.ets File

import testTransientTask from 'libentry.so';

@Entry
@Component
struct Index {
  @State message: string = '';
  // ...

  build() {
    Row() {
      Column() {
        // ...
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
        Button() {
          Text("RequestSuspendDelay").fontSize(20)
        }
        .id('request\_suspend\_delay')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.RequestSuspendDelay();
        })

        Button(){
          Text('GetRemainingDelayTime').fontSize(20)
        }
        .id('get\_remaining\_delay\_time')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.GetRemainingDelayTime();
        })

        Button(){
          Text('CancelSuspendDelay').fontSize(20)
        }
        .id('cancel\_suspend\_delay')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.CancelSuspendDelay();
        })

        Button(){
          Text('GetTransientTaskInfo').fontSize(20)
        }
        .id('get\_transient\_task\_info')
        .margin({ top: 10, bottom: 10 })
        .width(250)
        .height(40)
        .backgroundColor('#0D9FFB')
        .onClick(() => {
          this.GetTransientTaskInfo();
        })
      }
      .width('100%')
    }
    .height('100%')
  }

  RequestSuspendDelay() {
    let requestId = testTransientTask.RequestSuspendDelay();
    // ...
    console.info('The return requestId is ' + requestId);
  }

  GetRemainingDelayTime() {
    let time = testTransientTask.GetRemainingDelayTime();
    console.info('The time is ' + time);
  }

  CancelSuspendDelay() {
    let ret = testTransientTask.CancelSuspendDelay();
    console.info('The ret is ' + ret);
  }

  GetTransientTaskInfo() {
    let ret = testTransientTask.GetTransientTaskInfo();
    console.info('The ret is ' + JSON.stringify(ret));
  }
}

## Configuring the Library Dependency

Configure the CMakeLists.txt file. Add the required shared library, that is, libtransient\_task.so, to target\_link\_libraries in the CMakeLists.txt file automatically generated by the project.

target\_link\_libraries(entry PUBLIC libace\_napi.z.so libtransient\_task.so)

#### How to Test

1.  Connect to the device and run the program.
    
2.  Tap the Request transient task button. The console prints a log. The following is an example:
    
    The return requestId is 1
    
3.  Tap the Obtain remaining time button. The console prints a log. The following is an example:
    
    The return requestId is 18000
    
4.  Tap the Cancel transient task button. The console prints a log. The following is an example:
    
    The ret is 0
    
5.  Tap the Obtain all transient task information button. The console prints a log. The following is an example:
    
    The ret is {"remainingQuota":600000,"transientTasks":\[\]}
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/F-e5aDmpRKq5RxCSZv_3bQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061950Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B8780148CF5FE902F51413BC69C8C726E6A34E5BEC52FD68034BB5D19A35E0D)

If the Request transient task button is tapped for more than three consecutive times, the number of transient tasks exceeds the upper limit, and an error is reported. For more constraints, see [Transient Task (ArkTS)](../transient-task-arkts/document.md#constraints).
