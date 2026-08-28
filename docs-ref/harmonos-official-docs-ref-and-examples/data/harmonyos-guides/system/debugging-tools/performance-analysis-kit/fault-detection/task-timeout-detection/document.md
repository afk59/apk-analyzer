# Task Timeout Detection

#### Overview

Task timeout occurs when the execution duration of a service logic exceeds the expected duration.

Task timeout detection includes main thread timeout detection and task execution timeout detection. You can use HiCollie to customize the timeout threshold to proactively detect the service logic. The main thread timeout detection also has the default timeout threshold. For details, see [Using HiCollie to Detect Service Thread Stuck and Jank Events](../../service-thread-timeout-detection/using-hicollie-to-detect-service-thread-stuck-and-jank-events-c-c/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/NiwO3fSiRaSeOHaZSZb_9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3C4FC0693768AF1651637BE802C2D9D93DF2E32148A75A698758E62627A155D2)

Unlike task timeout detection, [application freeze detection](../application-freeze-detection/document.md) is a periodic detection logic provided by the system, which does not need to be perceived or adapted.

#### Main Thread Timeout Detection

## Detection Principles

The main thread event processing duration is checked. When the task duration exceeds the threshold, the log collection process is triggered, including stack collection and trace collection. The triggering conditions of the two collections are mutually exclusive. Only one collection is triggered upon a timeout.

Which of the collection processes is triggered depends on the processing duration of a single event in the main thread. The triggering conditions, log collection formats, and frequency restrictions are as follows:

| Collection Process | Triggering Condition | Log Collection Format | Prerequisites and Restrictions |
| :-- | :-- | :-- | :-- |
| Stack collection | 150 ms < Main thread processing duration < 450 ms | 
File name format: **MAIN\_THREAD\_JANK\_Second-level time\_PID.txt**.

For example, **MAIN\_THREAD\_JANK\_20240613211739\_40986.txt**.

 | 

\- The application is not detected within 10s after being started.

\- When [Developer options](../../../../../coding-and-debugging/debugging-your-app/developer-options/document.md#section0736139111917) is disabled, the main thread timeout event stack collection process can be triggered at most once a day within a lifecycle of an application.

\- When [Developer options](../../../../../coding-and-debugging/debugging-your-app/developer-options/document.md#section530763213432) is enabled, the main thread timeout event stack collection process can be triggered at most once an hour within a lifecycle of an application.

 |
| Trace collection | Main thread processing duration > 450 ms | 

File name format: **MAIN\_THREAD\_JANK\_unix timestamp\_PID.trace**.

For example, **MAIN\_THREAD\_JANK\_1762064185461\_40986.trace**.

 | 

\- To trigger trace collection, you can use the [nolog](../../performance-analysis-kit-terminology/document.md#nolog-version) version and disable [Developer options](../../../../../coding-and-debugging/debugging-your-app/developer-options/document.md#section530763213432).

\- Only one trace collection process can be triggered for the main thread timeout event within a day.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/vGu_tQrPQIy9LOAJxEOhMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D68E91AD21C99CBC5EF810636B5DE0936E19AC34426E14901EDC4DC1ABA723B3)

If the main thread processing duration is equal to 450 ms, no collection process is triggered.

When **Developer Options** is disabled, DevEco Studio may be unavailable. Therefore, you are advised to install the application before disabling **Developer Options**.

1.  Stack collection process:
    
    When the main thread processing times out (150 ms < main thread processing duration < 450 ms), a periodic detection task is started and executed every 150 ms. A stack file is generated only when the main thread processing duration exceeds 150 ms in at least one of the first two rounds of detection. The possible cases are as follows:
    
    (1) If a main thread timeout event (main thread processing duration > 150 ms) is detected during the first check, the stack collection starts and is performed every 150 ms for 10 times. The stack data is collected and an event is reported at the next interval. Then the check ends.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/e4envZ16RLCwVjmK_clxBg/en-us_image_0000002568684831.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90E76478763ED1FE7217096520D7C5D359FCA461249FA830441F2B7E28063D3C)
    
    (2) If a main thread timeout event (main thread processing duration > 150 ms) is detected during the second check, the stack collection starts and is performed every 150 ms for 10 times. The stack data is collected and an event is reported at the next interval. Then the check ends.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/MFxOZeIoTNyx6mrLAmFN5A/en-us_image_0000002568764841.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C171BD158F713B668F2531B704A99F957AA20D4FEA4D5646AF426F92636202A2)
    
    (3) If no main thread timeout event (main thread processing duration > 150 ms) is detected during the first two checks, the check ends.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/uJl8K6nPSGOHz9jsd-yfCw/en-us_image_0000002537765116.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02B622A42449B94FD48AB9A9459A7BC033C6AD0B1BD7BC698887B0B94CE7C474)
    
2.  Trace collection process
    
    When the main thread processing times out (main thread processing duration > 450 ms), the API for enabling trace collection is invoked to check every 150 ms for 20 times whether the duration exceeds 150 ms. The possible cases are as follows:
    
    (1) If no main thread timeout event (main thread processing duration > 150 ms) is detected during the 20 checks, no trace file is generated, and the check ends.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/r_u4wxSHRtuhkHe_r_ZjBA/en-us_image_0000002537925056.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=143BB3A75389E02737925BBAFDDAF2257F2742F52F5AEFE97292DE35395C650E)
    
    (2) If a main thread timeout event (main thread processing duration > 150 ms) is detected during any of the 20 checks, a trace file is generated, and an event is reported. Then the check ends.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5e/v3/46oRSc2QR8Cm5vaTXzDJIg/en-us_image_0000002568684833.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9756C42FE50953A1CC0632D1BC099310661BA5C0587977AB374EC39311524B33)
    

## Obtaining Logs

Main thread jank event logs are stored in the application sandbox directory. You can obtain the logs in any of the following ways:

**Subscribing to Main Thread Jank Events using HiAppEvent APIs**

HiAppEvent provides APIs for subscribing to faults. For details, see [Introduction to HiAppEvent](../../event-subscription/introduction-to-hiappevent/document.md). You can subscribe to the main thread timeout event by referring to [Subscribing to Main Thread Jank Events (ArkTS)](../../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/main-thread-jank-events/subscribing-to-main-thread-jank-events-arkts/document.md) or [Subscribing to Main Thread Jank Events (C/C++)](../../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/main-thread-jank-events/subscribing-to-main-thread-jank-events-c-c/document.md), and read the fault log file using the [external\_log](../../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/main-thread-jank-events/main-thread-jank-event-overview/document.md#event-fields) field in the event.

## Log Specifications

1.  Log aging specifications of main thread timeout detection
    
    Generally, the size of a stack file is 7 KB to 10 KB, and the size of a trace file is 1 MB to 5 MB. The **watchdog** directory in the application sandbox can store a maximum of 10 MB data. If the total file size exceeds 10 MB, the directory aging mechanism is automatically triggered to delete a maximum of 100 files based on the file name sequence. The path to **watchdog** is **/data/storage/el2/log/watchdog/**.
    
2.  Stack specifications of main thread timeout detection
    
    Currently, stack capturing supports only the ARM64 architecture. The stack capture result contains both native frames and JS frames parsed.
    
    An example of the stack capture result is as follows:
    
    9 #00 pc 0000757c /system/bin/appspawn(55679d09bcdea35bb1e0d4e1d9a3e58f)
        9 #01 pc 000731c0 /system/lib/ld-musl-aarch64.so.1(add9e521e4eaf5cb009d4260f3b69ccd)
            9 #02 pc 000090a9 /system/bin/appspawn(main+396)(55679d09bcdea35bb1e0d4e1d9a3e58f)
                9 #03 pc 0000ab5d /system/bin/appspawn(AppSpawnRun+100)(55679d09bcdea35bb1e0d4e1d9a3e58f)
                    9 #04 pc 0000e7f1 /system/lib/chipset-pub-sdk/libbegetutil.z.so(RunLoop\_+200)(52ace27d827ad482439bf32cc75bb17b)
                    ......
                                            9 #21 pc 00107aec /system/lib/ld-musl-aarch64.so.1(\_\_pthread\_cond\_timedwait+628)(add9e521e4eaf5cb009d4260f3b69ccd)
    1 #00 pc 00032e67 /system/lib/platformsdk/libmmi-util.z.so(OHOS::MMI::UDSSocket::OnReadPackets(OHOS::MMI::CircleStreamBuffer&, std::\_\_h::function<void (OHOS::MMI::NetPacket&)>)+158)(99e56bc765f9208f7b7ba8b268886a59)
        1 #01 pc 0000312e5 /system/lib/platformsdk/libmmi-client.z.so(OHOS::MMI::ClientMsgHandler::OnMsgHandler(OHOS::MMI::UDSClient const&, OHOS::MMI::NetPacket&)+340)(66ac85e964777ae89f0c26c339093cd1)
            1 #02 pc 0003016b /system/lib/platformsdk/libmmi-client.z.so(OHOS::MMI::ClientMsgHandler::OnPointerEvent(OHOS::MMI::UDSClient const&, OHOS::MMI::NetPacket&)+1222)(66ac85e964777ae89f0c26c339093cd1)
                1 #03 pc 0003b96b /system/lib/platformsdk/libmmi-client.z.so(OHOS::MMI::InputManagerImpl::OnPointerEvent(std::\_\_h::shared\_ptr<OHOS::MMI::PointerEvent>)+1370)(66ac85e964777ae89f0c26c339093cd1)
                    1 #04 pc 00095903 /system/lib/platformsdk/libwm.z.so(OHOS::Rosen::InputEventListener::OnInputEvent(std::\_\_h::shared\_ptr<OHOS::MMI::PointerEvent>) const+478)(9c40c5f416d6f830435126998fbcad42)
                    ......
                                            1 #21 pc 003f5c55 /system/lib/platformsdk/libark\_jsruntime.so(4e6a2651ec80a7f639233f414d6486fe)
                                                1 #22 at anonymous (/entry/build/default/cache/default/default@CompileArkTS/esmodule/debug/entry/src/main/ets/pages/Index.js:67:17)
                                                    1 #23 at wait2 (/entry/build/default/cache/default/default@CompileArkTS/esmodule/debug/entry/src/main/ets/pages/Index.js:16:12)
                                                    ......
    
    Each stack capture records 16 KB call stack information of the main thread for stack unwinding. Therefore, each stack capture result contains a maximum of 16 KB invocation information of the process for 10 times. The captured data is displayed in a tree view, with repeated stack frames aggregated and different call layers distinguished by line indentation. If the stack fails to be captured (for example, the main thread is blocked in the kernel or signals are masked), the content of the **/proc/self/wchan** file is output.
    
    In the result, each row indicates a piece of stack information. The meaning of a row of stack frame information can be interpreted as follows:
    
    Native frame:
    
    9 #02 pc 000090a9 /system/bin/appspawn(main+396)(55679d09bcdea35bb1e0d4e1d9a3e58f)
    ^  ^       ^               ^              ^                   ^
    1  2       3               4              5                   6
    
    1 indicates the number of times that the frame is sampled.
    2 indicates the invoking level of the frame. The line indentation size corresponds to this level. The number of sampling times of all frames at the same level cannot be greater than 10. The number of sampling times of #00 is 10 (set the sampling times).
    3 indicates the Program Counter (PC) value of the native frame.
    4 indicates the path of the called file.
    5 indicates the name of the called function and the code line offset.
    6 indicates the MD5 value of the .so file.
    
    JS frame:
    
    1 #23 at wait2 (/entry/build/default/cache/default/XXX/entry/src/main/ets/pages/Index.js:16:12)
    ^  ^    ^               ^
    1  2    3               4
    
    1 indicates the number of times that the frame is sampled. The maximum value is the sampling times.
    2 indicates the invoking level of the frame, which is the same as that of the native frame.
    3 indicates the name of the called function, which is \*\*wait2\*\*.
    4 indicates the path, file, row number, and column number of the called function.
    
3.  Trace specifications of main thread timeout detection
    
    The size of the trace file is 1 MB to 5 MB. You can visually analyze the trace file using [SmartPerf](https://gitcode.com/openharmony/developtools_smartperf_host). You can download the tool from [developtools\_smartperf\_host Release](https://gitcode.com/openharmony/developtools_smartperf_host/releases).
    
    For details about the trace file, see [Loading Trace Files on the Web Client](https://gitcode.com/openharmony/developtools_smartperf_host/blob/master/smartperf_host/ide/src/doc/md/quickstart_systemtrace.md).
    

#### Task Execution Timeout Detection

## Detection Principles

**Overview**: Task timeout occurs when the service logic execution time exceeds the expected time.

**Principles**: If the service logic execution time exceeds the specified timeout threshold, the task execution times out.

The following figure shows the detection principles.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/YZLrSNfESCif3hXt0vuC0w/en-us_image_0000002568764843.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062027Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69D881B6733E46FE56D6825C0D8DFADE6E483AB797BED17469573E4F01BE3AA1)

## Obtaining Logs

You can obtain task execution timeout logs in any of the following ways:

**Subscribing to Task Execution Timeout Events using HiAppEvent APIs**

HiAppEvent provides APIs for subscribing to faults. For details, see [Introduction to HiAppEvent](../../event-subscription/introduction-to-hiappevent/document.md). You can subscribe to the task execution timeout event by referring to [Subscribing to Task Execution Timeout Events (ArkTS)](../../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/task-execution-timeout-events/subscribing-to-task-execution-timeout-events-arkts/document.md) or [Subscribing to Task Execution Timeout Events (C/C++)](../../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/task-execution-timeout-events/subscribing-to-task-execution-timeout-events-c-c/document.md), and read the fault log file using the [external\_log](../../event-subscription/using-hiappevent-to-subscribe-to-events/system-events/task-execution-timeout-events/task-execution-timeout-event-overview/document.md#event-fields) field in the event.

## Log Specifications

The log specifications of task execution timeout events are the same as those of application freeze events. For details, see [Application Freeze Log Specifications](../application-freeze-detection/document.md#log-specifications).
