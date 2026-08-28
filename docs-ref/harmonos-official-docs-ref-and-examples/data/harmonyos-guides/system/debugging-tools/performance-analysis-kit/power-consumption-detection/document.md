# Power Consumption Detection

#### Overview

Power consumption detection detects high CPU load events by event subscription.

For details about how to use the HiAppEvent APIs to subscribe to high CPU load events, see the following topic. Currently, only the ArkTS APIs are provided.

-   [Event Subscription (ArkTS)](../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/high-cpu-load-events/event-subscription-arkts/document.md)

#### Principles

The system periodically collects the running time of third-party applications on the CPU and collects statistics on the average CPU load within the previous 5 minutes every 5 minutes under specific conditions (such as switching between the foreground and background). If the load exceeds the specified threshold, the HiAppEvent warning event is triggered.

The load in the high CPU load event triggered by the application is the running time normalized based on the number of CPU cores. For example, if an application process runs on a 10-core CPU for 5 minutes within 5 minutes, the average load is calculated as follows: 5 (running time on the CPU)/5 (statistics period, in minutes)/10 (number of cores) = 10%.

#### Constraints

The threshold for triggering high CPU load exceptions is the default value and cannot be customized for a single application.

High CPU load thresholds:

When the average CPU load of a foreground application is greater than 30% within 5 minutes, a high CPU load event is triggered.

When the average CPU load of a background application is greater than 10% within 5 minutes, a high CPU load event is triggered.

When the average load of a single thread in 1 minute is greater than 70%, a high thread load event is triggered.

#### Log Specifications

After obtaining the system event data processing log in the last step of event subscription development (for details, see [Event Subscription (ArkTS)](../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/high-cpu-load-events/event-subscription-arkts/document.md)), you can obtain the fault log file based on the file path recorded in **external\_log**. Example:

<HiAppEvent> eventInfo={"domain":"OS","name":"CPU\_USAGE\_HIGH","eventType":1,"params":{"begin\_time":1749128563568,"bundle\_name":"com.example.powerdemon","bundle\_version":"1.0.0","end\_time":1749128863573,"external\_log":\["/data/storage/el2/log/hiappevent/CPU\_USAGE\_HIGH\_1749128939012\_0.log","/data/storage/el2/log/hiappevent/CPU\_USAGE\_HIGH\_1749128939015\_0.log"\],"fault\_type":2,"foreground":true,"log\_over\_limit":false,"threads":\[{"name":"WorkerThread","tid":20743,"usage":8.30084},{"name":"WorkerThread","tid":20741,"usage":8.29501}

**external\_log** records the path of the fault log file, from which you can obtain the fault log file.

The fault log format of the high CPU load event triggered in the foreground and background is as follows:

Result: 0 ( no error )
Timestamp:2025-06-05 21:07:54.000
Pid:57531         <- Process ID
Uid:20020188      <- Thread ID
Process name:com.example.powerdemon       <- Process name
Tid:57531, Name:mple.powerdemon           <- Thread name
#00 pc 0000000000156a74 /system/lib/ld-musl-aarch64.so.1(epoll\_wait+80)(f77c0346c0084ebbadf721ea319f5f77)      <- Error stack information
#01 pc 00000000000192bc /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EpollIoWaiter::WaitFor(std::\_\_h::unique\_lock<std::\_\_h::mutex>&, long)+232)(4f4eb5c696148d35cce6d2e07f75f1ea)
#02 pc 0000000000021660 /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EventQueue::WaitUntilLocked(std::\_\_h::chrono::time\_point<std::\_\_h::chrono::steady\_clock, std::\_\_h::chrono::duration<long long, std::\_\_h::ratio<1l, 1000000000l>>> const&, std::\_\_h::unique\_lock<std::\_\_h::mutex>&)+140)(4f4eb5c696148d35cce6d2e07f75f1ea)
#03 pc 0000000000022fdc /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EventQueueBase::GetEvent()+216)(4f4eb5c696148d35cce6d2e07f75f1ea)
#04 pc 000000000002cf60 /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::(anonymous namespace)::EventRunnerImpl::Run()+928)(4f4eb5c696148d35cce6d2e07f75f1ea)
#05 pc 00000000000302f0 /system/lib64/chipset-pub-sdk/libeventhandler.z.so(OHOS::AppExecFwk::EventRunner::Run()+528)(4f4eb5c696148d35cce6d2e07f75f1ea)

For high thread load events, the fault log is a stack contains both native frames and JS frames parsed, which is captured once a day for a single application.

Native frame:

59 #07 pc 0000000000015adc /system/lib64/module/libworker.z.so(74be9232848e55d7c5da62a978ef624b)
59 #08 pc 000000000007dd38 /system/lib64/platformsdk/libace\_napi.z.so(napi\_call\_function+216)(7d9559571526f9f5efb838da8f2ea2ac)
59 #09 pc 00000000003b10f0 /system/lib64/platformsdk/libark\_jsruntime.so(panda::FunctionRef::CallForNapi(panda::ecmascript::EcmaVM const\*, panda::JSValueRef\*, panda::JSValueRef\* const\*, int)+564)(81e7710dc27ae7c5f6000ede7e911f20)
...

| 
Number of Sampling Times

 | 

Frame Call Level (Matched by Line Indentation)

 | 

PC Value

 | 

Called File Path

 | 

Name and Code Line Offset of the Called Function

 | 

MD5 Value of the .so File

 |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 

59

 | 

#09

 | 

00000000003b10f0

 | 

/system/lib64/platformsdk/libark\_jsruntime.so

 | 

panda::FunctionRef::CallForNapi(panda::ecmascript::EcmaVM const\*, panda::JSValueRef\*, panda::JSValueRef\* const\*, int)+564

 | 

81e7710dc27ae7c5f6000ede7e911f20

 |

JS frame:

59 #11 at anonymous (entry/build/default/cache/default/default@CompileArkTS/esmodule/release/entry/src/main/ets/workers/Worker.ts:12:12)
59 #12 at eatCpu (entry/build/default/cache/default/default@CompileArkTS/esmodule/release/entry/src/main/ets/workers/Worker.ts:26:26)
...

| 
Number of Sampling Times

 | 

Frame Call Level (Matched by Line Indentation)

 | 

Called Function Name

 | 

File Path and Row and Column Numbers of the Called Function

 |
| :-- | :-- | :-- | :-- |
| 

59

 | 

#11

 | 

anonymous

 | 

entry/build/default/cache/default/default@CompileArkTS/esmodule/release/entry/src/main/ets/workers/Worker.ts:12:12

 |
