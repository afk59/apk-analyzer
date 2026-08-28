# Using HiTraceMeter (C/C++)

#### Overview

HiTraceMeter provides APIs for system performance tracing. You can call the APIs at key code to track processes and check system and application performance.

#### Available APIs

The **HiTraceMeter** module provides APIs for performance tracing. For details, see [trace.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-trace-h).

| API | Description |
| :-- | :-- |
| void OH\_HiTrace\_StartTraceEx(HiTrace\_Output\_Level level, const char\* name, const char\* customArgs) | 
Starts a synchronous time slice trace with the trace output level specified.

**Note**: This API is supported since API version 19.

 |
| void OH\_HiTrace\_FinishTraceEx(HiTrace\_Output\_Level level) | 

Stops a synchronous time slice trace with the trace output level specified.

The value of **level** must be the same as that of **OH\_HiTrace\_StartTraceEx()**.

**Note**: This API is supported since API version 19.

 |
| void OH\_HiTrace\_StartAsyncTraceEx(HiTrace\_Output\_Level level, const char\* name, int32\_t taskId, const char\* customCategory, const char\* customArgs) | 

Starts an asynchronous time slice trace with the trace output level specified.

If multiple tracing tasks with the same name need to be performed at the same time, different task IDs must be specified through **taskId**. If the tracing tasks with the same name are not performed at the same time, the same task ID can be used.

**Note**: This API is supported since API version 19.

 |
| void OH\_HiTrace\_FinishAsyncTraceEx(HiTrace\_Output\_Level level, const char\* name, int32\_t taskId) | 

Stops an asynchronous time slice trace with the trace output level specified.

Stops a tracing task. The values of **name** and **taskId** must be the same as those in **OH\_HiTrace\_StartAsyncTraceEx()**.

**Note**: This API is supported since API version 19.

 |
| void OH\_HiTrace\_CountTraceEx(HiTrace\_Output\_Level level, const char\* name, int64\_t count) | 

Traces an integer with the trace output level specified.

**name** indicates the name of an integer variable to trace, and **count** indicates the integer value.

**Note**: This API is supported since API version 19.

 |
| bool OH\_HiTrace\_IsTraceEnabled(void) | 

Checks whether application trace capture is enabled.

When it is enabled, **true** is returned; when it is disabled or stopped, **false** is returned. In this case, calling the HiTraceMeter API does not take effect.

**Note**: This API is supported since API version 19.

 |
| int32\_t OH\_HiTrace\_RegisterTraceListener(OH\_HiTrace\_TraceEventListener callback) | 

Registers a callback to notify whether the application trace capture is enabled. This API uses a synchronous callback to return the result.

After the registration is successful, the callback is executed immediately. Subsequent callbacks are executed when the application trace capture status changes.

Note: This API is supported since API version 22.

 |
| int32\_t OH\_HiTrace\_UnregisterTraceListener(int32\_t index); | 

Deregisters the callback used to notify whether the application trace capture is enabled.

Note: This API is supported since API version 22.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/3Tn-6MkDQZS7k0CoW7b30g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062029Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=053924C8DDDBF323BDB8EC5AAEF24F9713C31F9C1C227A7AEE296C11E8BCDA30)

The vertical bar (|) is used as the separator in [user-mode trace format](../viewing-hitracemeter-logs/document.md#user-mode-trace-format). Therefore, the string parameters passed by the HiTraceMeter APIs must exclude this character to avoid trace parsing exceptions.

## API Category

HiTraceMeter APIs are classified into three types: synchronous timeslice tracing APIs, asynchronous timeslice tracing APIs, and integer tracing APIs. HiTraceMeter APIs are synchronous. The synchronous and asynchronous modes describe the traced services. The synchronous timeslice tracing APIs are used for synchronous services, and the asynchronous timeslice tracing APIs are used for asynchronous services. HiTraceMeter APIs can be used with [HiTraceChain](../../distributed-call-chain-tracing/using-hitracechain-c-c/document.md) to associate and analyze logging across devices, processes, or threads.

## Use Scenarios

-   Synchronous timeslice tracing APIs:
    
    The **OH\_HiTrace\_StartTraceEx()** and **OH\_HiTrace\_FinishTraceEx()** APIs must be used sequentially for logging during sequential execution. If they are not called in the correct order, the trace file will appear abnormal in visualization tools such as SmartPerf.
    
-   Asynchronous timeslice tracing APIs:
    
    The **OH\_HiTrace\_StartAsyncTraceEx()** API is called to start logging before an asynchronous operation is performed, and the **OH\_HiTrace\_FinishAsyncTraceEx()** API is called to end logging after the asynchronous operation is performed.
    
    During trace parsing, different asynchronous traces are identified by the **name** and **taskId** parameters. These two APIs must be used in sequence as a pair, with the same **name** and **taskId** passed.
    
    Different **name** and **taskId** values must be used for different asynchronous processes. However, the same **name** and **taskId** values can be used if asynchronous processes do not occur at the same time.
    
    If the API is called incorrectly, the trace file will appear abnormal in visualization tools such as SmartPerf.
    
-   Integer tracing APIs:
    
    The APIs are used to trace integer variables. The **OH\_HiTrace\_CountTraceEx()** API is called when integer values change. You can view the change in the lane diagram of SmartPerf. The values during the interval between the start of data collection and the first logging cannot be viewed.
    

## Parameter Description

| Name | Type | Description |
| :-- | :-- | :-- |
| level | enum | 
Trace output level. Trace data whose levels are lower than the system threshold will not be output.

The log version threshold is **HITRACE\_LEVEL\_INFO**, and the nolog version threshold is **HITRACE\_LEVEL\_COMMERCIAL**.

 |
| name | const char\* | Name of the task or integer variable to trace. |
| taskId | int32\_t | Task ID. If multiple tasks with the same **name** are executed at the same time, you must set different **taskId** when calling **OH\_HiTrace\_StartAsyncTraceEx()**. |
| count | int64\_t | Value of an integer variable. |
| customCategory | const char\* | 

Custom category name, which is used to collect asynchronous trace data of the same type.

If the category is not required, pass in an empty string.

 |
| customArgs | const char\* | 

Custom key-value pair. If there are multiple key-value pairs, separate them with commas (,), for example, **key1=value1,key2=value2**.

If this parameter is not required, pass in an empty string.

 |
| callback | void (\*)(bool) | Registered callback. |
| index | int32\_t | Callback index returned by **OH\_HiTrace\_RegisterTraceListener()**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/l-Kdt16ETZCV7MvtgM8AXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062029Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FB9E14856B9CC712D8115CC7DCDC2FB1030750E57A2EA62F7E68711B5CB09FD)

The maximum length of a [user-mode trace](../viewing-hitracemeter-logs/document.md#user-mode-trace-format) is 512 characters. Excess characters will be truncated. Therefore, it is recommended that the total length of the **name**, **customCategory**, and **customArgs** fields be less than or equal to 420 characters.

#### How to Develop

The following is an example of a native C++ application that uses the HiTraceMeter APIs.

## Step 1: Creating a Project

1.  Create a project in DevEco Studio and select **Native C++**. The project directory structure is as follows:
    
    ├── entry
    │   ├── src
    │       ├── main
    │       │   ├── cpp
    │       │   │   ├── CMakeLists.txt
    │       │   │   ├── napi\_init.cpp
    │       │   │   └── types
    │       │   │       └── libentry
    │       │   │           ├── Index.d.ts
    │       │   │           └── oh-package.json5
    │       │   ├── ets
    │       │   │   ├── entryability
    │       │   │   │   └── EntryAbility.ets
    │       │   │   ├── entrybackupability
    │       │   │   │   └── EntryBackupAbility.ets
    │       │   │   └── pages
    │       │   │       └── Index.ets
    
2.  In the **entry/src/main/cpp/CMakeLists.tx** file, add **libhitrace\_ndk.z.so** and **libhilog\_ndk.z.so**. The complete file content is as follows:
    
    \# the minimum version of CMake.
    cmake\_minimum\_required(VERSION 3.5.0)
    project(HiTraceChainTest03)
    
    set(NATIVERENDER\_ROOT\_PATH ${CMAKE\_CURRENT\_SOURCE\_DIR})
    
    if(DEFINED PACKAGE\_FIND\_FILE)
        include(${PACKAGE\_FIND\_FILE})
    endif()
    
    include\_directories(${NATIVERENDER\_ROOT\_PATH}
                        ${NATIVERENDER\_ROOT\_PATH}/include)
    
    add\_library(entry SHARED napi\_init.cpp)
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so libhitrace\_ndk.z.so libhilog\_ndk.z.so)
    
3.  In the **entry/src/main/cpp/napi\_init.cpp** file, call the HiTraceMeter NDK\_C API in the **Add** function to trace performance. The sample code is as follows:
    

#include <cstdio>
#include <cstring>

#include "hilog/log.h"
#include "hitrace/trace.h"
#include "napi/native\_api.h"

#undef LOG\_TAG
#define LOG\_TAG "traceTest"

static napi\_value Add(napi\_env env, napi\_callback\_info info)
{
    // Start the first asynchronous tracing task.
    HiTrace\_Output\_Level level = HITRACE\_LEVEL\_COMMERCIAL;
    constexpr int64\_t taskIdOne = 1001;
    OH\_HiTrace\_StartAsyncTraceEx(level, "myTestAsyncTrace", taskIdOne, "categoryTest", "key=value");
    // Start the counting task.
    int64\_t traceCount = 0;
    traceCount++;
    OH\_HiTrace\_CountTraceEx(level, "myTestCountTrace", traceCount);
    // Keep the service process running.
    OH\_LOG\_INFO(LogType::LOG\_APP, "myTraceTest running, taskId: 1001");
    // Start the second asynchronous tracing task with the same name while the first task is still running. The tasks are running concurrently and therefore their taskId must be different.
    constexpr int64\_t taskIdTwo = 1002;
    OH\_HiTrace\_StartAsyncTraceEx(level, "myTestAsyncTrace", taskIdTwo, "categoryTest", "key=value");
    // Start the counting task.
    traceCount++;
    OH\_HiTrace\_CountTraceEx(level, "myTestCountTrace", traceCount);
    // Keep the service process running.
    OH\_LOG\_INFO(LogType::LOG\_APP, "myTraceTest running, taskId: 1002");

    // Stop the asynchronous tracing task whose taskId is 1001.
    OH\_HiTrace\_FinishAsyncTraceEx(level, "myTestAsyncTrace", taskIdOne);
    // Stop the asynchronous tracing task whose taskId is 1002.
    OH\_HiTrace\_FinishAsyncTraceEx(level, "myTestAsyncTrace", taskIdTwo);

    // Start a synchronous tracing task.
    OH\_HiTrace\_StartTraceEx(level, "myTestSyncTrace", "key=value");
    // Keep the service process running.
    OH\_LOG\_INFO(LogType::LOG\_APP, "myTraceTest running, synchronizing trace");
    // Stop the synchronous tracing task.
    OH\_HiTrace\_FinishTraceEx(level);

    // If the process of generating the parameters passed by the HiTraceMeter API is complex, you can use isTraceEnabled to determine whether trace capture is enabled.
    // Avoid performance loss when application trace capture is not enabled.
    constexpr int64\_t taskIdThree = 1003;
    constexpr int loopTime = 10;
    if (OH\_HiTrace\_IsTraceEnabled()) {
        char customArgs\[128\] = "key0=value0";
        for (int index = 1; index < loopTime; index++) {
            char buffer\[16\];
            snprintf(buffer, sizeof(buffer), ",key%d=value%d", index, index);
            strncat(customArgs, buffer, sizeof(customArgs) - strlen(customArgs) - 1);
        }
        OH\_HiTrace\_StartAsyncTraceEx(level, "myTestAsyncTrace", taskIdThree, "categoryTest", customArgs);
        OH\_LOG\_INFO(LogType::LOG\_APP, "myTraceTest running, taskId: 1003");
        OH\_HiTrace\_FinishAsyncTraceEx(level, "myTestAsyncTrace", taskIdThree);
    } else {
        OH\_LOG\_INFO(LogType::LOG\_APP, "myTraceTest running, trace is not enabled");
    }

    size\_t requireArgc = 2;
    size\_t argc = 2;
    napi\_value args\[2\] = {nullptr};

    napi\_get\_cb\_info(env, info, &argc, args, nullptr, nullptr);

    napi\_valuetype valuetype0;
    napi\_typeof(env, args\[0\], &valuetype0);

    napi\_valuetype valuetype1;
    napi\_typeof(env, args\[1\], &valuetype1);

    double value0;
    napi\_get\_value\_double(env, args\[0\], &value0);

    double value1;
    napi\_get\_value\_double(env, args\[1\], &value1);

    napi\_value sum;
    napi\_create\_double(env, value0 + value1, &sum);

    return sum;
}

EXTERN\_C\_START
static napi\_value Init(napi\_env env, napi\_value exports)
{
    napi\_property\_descriptor desc\[\] = {
        { "add", nullptr, Add, nullptr, nullptr, nullptr, napi\_default, nullptr }
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
    .nm\_modname = "entry",
    .nm\_priv = ((void\*)0),
    .reserved = { 0 },
};

extern "C" \_\_attribute\_\_((constructor)) void RegisterEntryModule(void)
{
    napi\_module\_register(&demoModule);
}

## Step 2: Collecting and Viewing Trace Information

1.  Run the following command in DevEco Studio Terminal to enable trace capture:
    
    PS D:\\xxx\\xxx> hdc shell
    $ hitrace --trace\_begin app
    
2.  Click the **Run** button in DevEco Studio to run the project. Then, click "Hello world" to execute the service logic that contains HiTraceMeter logging. Run the following command to capture trace data and filter the trace data using the keyword **myTest** (the name field prefix passed by the logging API is **myTest** in this example).
    
    $ hitrace --trace\_dump | grep myTest
    
    The sample trace data is as follows:
    
    <...>-49837   (-------) \[002\] .... 349137.708093: tracing\_mark\_write: S|49837|H:myTestAsyncTrace|1001|M62|categoryTest|key=value
    <...>-49837   (-------) \[002\] .... 349137.708103: tracing\_mark\_write: C|49837|H:myTestCountTrace|1|M62
    <...>-49837   (-------) \[002\] .... 349137.708201: tracing\_mark\_write: S|49837|H:myTestAsyncTrace|1002|M62|categoryTest|key=value
    <...>-49837   (-------) \[002\] .... 349137.708209: tracing\_mark\_write: C|49837|H:myTestCountTrace|2|M62
    <...>-49837   (-------) \[002\] .... 349137.708239: tracing\_mark\_write: F|49837|H:myTestAsyncTrace|1001|M62
    <...>-49837   (-------) \[002\] .... 349137.708246: tracing\_mark\_write: F|49837|H:myTestAsyncTrace|1002|M62
    <...>-49837   (-------) \[002\] .... 349137.708252: tracing\_mark\_write: B|49837|H:myTestSyncTrace|M62|key=value
    <...>-49837   (-------) \[002\] .... 349137.708301: tracing\_mark\_write: S|49837|H:myTestAsyncTrace|1003|M62|categoryTest|key0=value0,key1=value1,key2=value2,key3=value3,key4=value4,key5=value5,key6=value6,key7=value7,key8=value8,key9=value9
    <...>-49837   (-------) \[002\] .... 349137.708323: tracing\_mark\_write: F|49837|H:myTestAsyncTrace|1003|M62
    

## Step 3: Stoping Trace Capture

1.  Run the following command to stop the application trace capture:
    
    $ hitrace --trace\_finish
    
2.  Click "Hello World" on the application screen again. The trace capture of the application is disabled, and the **OH\_HiTrace\_IsTraceEnabled()** API returns **false**. In the **Log** window of the DevEco Studio, input the keyword **not enabled** for filtering and the following log is displayed.
    
    myTraceTest running, trace is not enabled
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/BO7iFRC0ThSR3QC5wj73kg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062029Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3739272C76061708121709044EF6CEE223152F98DE31B77AC58D6CFEFE87D685)
    
    In the log version, after the **hitrace --trace\_finish** command is used to stop capture, the snapshot mode is automatically started and trace capture is enabled. In this case, the **OH\_HiTrace\_IsTraceEnabled()** API returns **true**, and the preceding log is not printed.
