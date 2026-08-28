# Using hiTraceChain (C/C++)

#### Available APIs

The APIs for distributed call chain tracing are provided by the **HiTraceChain** module. For details, see [trace.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-trace-h).

The following table lists the APIs provided by HiTraceChain for implementing the basic distributed tracing functionality. The corresponding APIs are also available in ArkTS.

| API | Description |
| :-- | :-- |
| HiTraceId OH\_HiTrace\_BeginChain(const char \*name, int flags) | Starts call chain tracing and returns the created **HiTraceId**. |
| void OH\_HiTrace\_EndChain() | Stops call chain tracing. |
| HiTraceId OH\_HiTrace\_GetId() | Obtains the trace ID in TLS of the calling thread. |
| void OH\_HiTrace\_SetId(const HiTraceId \*id) | Sets the trace ID in TLS of the calling thread to **id**. |
| void OH\_HiTrace\_ClearId(void) | Clears the trace ID of the current thread. |
| HiTraceId OH\_HiTrace\_CreateSpan(void) | Creates a trace span. Specifically, create a **HiTraceId**, use the **chainId** and **spanId** in the Thread-Local Storage (TLS) of the current thread to initialize the **chainId** and **parentSpanId** of the **HiTraceId**, generate a new **spanId** for the **HiTraceId**, and return the **HiTraceId**. |
| bool OH\_HiTrace\_IsIdValid(const HiTraceId \*id) | 
Checks whether the **HiTraceId** is valid.

The value **true** indicates that **HiTraceId** is valid, and **false** indicates the opposite.

 |
| bool OH\_HiTrace\_IsFlagEnabled(const HiTraceId \*id, HiTrace\_Flag flag) | 

Checks whether the trace flag specified by **HiTraceId** is enabled.

The value **true** indicates that the specified trace flag is enabled, and **false** indicates the opposite.

 |
| void OH\_HiTrace\_EnableFlag(const HiTraceId \*id, HiTrace\_Flag flag) | Enables the trace flag specified in **HiTraceId**. |
| void OH\_HiTrace\_Tracepoint(HiTrace\_Communication\_Mode mode, HiTrace\_Tracepoint\_Type type, const HiTraceId \*id, const char \*fmt, ...) | Adds a trace point for the HiTraceMeter logging. |

The following table describes the APIs provided to extend **HiTraceId**. These APIs are available only in C/C++.

| API | Description |
| :-- | :-- |
| void OH\_HiTrace\_InitId(HiTraceId \*id) | Initializes a **HiTraceId**. |
| int OH\_HiTrace\_GetFlags(const HiTraceId \*id) | Obtains the trace flag set in **HiTraceId**. |
| void OH\_HiTrace\_SetFlags(HiTraceId \*id, int flags) | Sets the trace flag in **HiTraceId**. |
| uint64\_t OH\_HiTrace\_GetChainId(const HiTraceId \*id) | Obtains the trace chain ID in **HiTraceId**. |
| void OH\_HiTrace\_SetChainId(HiTraceId \*id, uint64\_t chainId) | Sets the trace chain ID in **HiTraceId**. |
| uint64\_t OH\_HiTrace\_GetSpanId(const HiTraceId \*id) | Obtains the span ID in **HiTraceId**. |
| void OH\_HiTrace\_SetSpanId(HiTraceId \*id, uint64\_t spanId) | Sets the span ID in **HiTraceId**. |
| uint64\_t OH\_HiTrace\_GetParentSpanId(const HiTraceId \*id) | Obtains the parent span ID in **HiTraceId**. |
| void OH\_HiTrace\_SetParentSpanId(HiTraceId \*id, uint64\_t parentSpanId) | Sets the parent span ID in **HiTraceId**. |
| int OH\_HiTrace\_IdToBytes(const HiTraceId\* id, uint8\_t\* pIdArray, int len) | Converts **HiTraceId** into a byte array for cache or communication. |
| void OH\_HiTrace\_IdFromBytes(HiTraceId \*id, const uint8\_t \*pIdArray, int len) | Creates a **HiTraceId** based on a byte array. |

#### How to Develop

**std::thread** does not support automatic transfer of **HiTraceId**. The following example shows how to use distributed tracing in this scenario. For details about the common mechanisms that support and do not support HiTraceChain automatic transfer, see [Constraints](../introduction-to-hitracechain/document.md#constraints).

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
    
2.  In the **entry > src > main > cpp > CMakeLists.tx** file, add **libhitrace\_ndk.z.so** and **libhilog\_ndk.z.so**. The complete file content is as follows:
    
    \# Minimum version of CMake.
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
    
3.  In the **entry > src > main > cpp > napi\_init.cpp** file, use HiTraceChain to trace multi-thread tasks. The sample code is as follows:
    

#include <thread>

#include "hilog/log.h"
#include "hitrace/trace.h"
#include "napi/native\_api.h"

#undef LOG\_TAG
#define LOG\_TAG "testTag"

void Print2(HiTraceId id)
{
    // Set a HiTraceId for the thread.
    OH\_HiTrace\_SetId(&id);
    // Generate a spanId.
    id = OH\_HiTrace\_CreateSpan();
    // Set a HiTraceId with the spanId for the thread.
    OH\_HiTrace\_SetId(&id);
    OH\_LOG\_INFO(LogType::LOG\_APP, "Print2");
    // End the distributed tracing of the thread. This functionality is the same as that of OH\_HiTrace\_EndChain().
    OH\_HiTrace\_ClearId();
    OH\_LOG\_INFO(LogType::LOG\_APP, "Print2, HiTraceChain end");
}

void Print1(HiTraceId id)
{
    // Set a HiTraceId for the thread.
    OH\_HiTrace\_SetId(&id);
    // Generate a spanId.
    id = OH\_HiTrace\_CreateSpan();
    // Set a HiTraceId with the spanId for the thread.
    OH\_HiTrace\_SetId(&id);
    OH\_LOG\_INFO(LogType::LOG\_APP, "Print1");
    std::thread(Print2, OH\_HiTrace\_GetId()).detach();
    // End the distributed tracing of the thread.
    OH\_HiTrace\_EndChain();
    OH\_LOG\_INFO(LogType::LOG\_APP, "Print1, HiTraceChain end");
}

static napi\_value Add(napi\_env env, napi\_callback\_info info)
{
    // Start distributed tracing when the task starts.
    HiTraceId hiTraceId = OH\_HiTrace\_BeginChain("testTag: hiTraceChain begin", HiTrace\_Flag::HITRACE\_FLAG\_DEFAULT);
    // Check whether the generated hiTraceId is valid. If yes, a HiLog log is generated.
    if (OH\_HiTrace\_IsIdValid(&hiTraceId)) {
        OH\_LOG\_INFO(LogType::LOG\_APP, "HiTraceId is valid");
    }
    // Enable the HITRACE\_FLAG\_INCLUDE\_ASYNC flag, indicating that HiTraceId is automatically transferred in the asynchronous mechanism supported by the system.
    OH\_HiTrace\_EnableFlag(&hiTraceId, HiTrace\_Flag::HITRACE\_FLAG\_INCLUDE\_ASYNC);
    // Check whether the HITRACE\_FLAG\_INCLUDE\_ASYNC flag of HiTraceId is enabled. If yes, set the HiTraceId to the thread TLS.
    if (OH\_HiTrace\_IsFlagEnabled(&hiTraceId, HiTrace\_Flag::HITRACE\_FLAG\_INCLUDE\_ASYNC)) {
        OH\_HiTrace\_SetId(&hiTraceId);
        OH\_LOG\_INFO(LogType::LOG\_APP, "HITRACE\_FLAG\_INCLUDE\_ASYNC is enabled");
    }
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

    // Create a thread to execute the print task and transfer the HiTraceId of the thread.
    std::thread(Print1, OH\_HiTrace\_GetId()).detach();
    // Stop the distributed tracing when the task is complete.
    OH\_HiTrace\_EndChain();
    OH\_LOG\_INFO(LogType::LOG\_APP, "Add, HiTraceChain end");

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

In the **entry > src > main > ets > pages > Index.ets** file, call the **Add** method in the button click event. The sample code is as follows:

import { hilog } from '@kit.PerformanceAnalysisKit';
import testNapi from 'libentry.so';

const DOMAIN = 0x0000;

@Entry
@Component
struct Index {
  @State message: string = 'clickTime=0';
  @State clickTime: number = 0;

  build() {
    Row() {
      Column() {
        Button(this.message)
          .fontSize(20)
          .margin(5)
          .width(350)
          .height(60)
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            this.clickTime++;
            this.message = 'clickTime=' + this.clickTime;
            hilog.info(DOMAIN, 'testTag', 'Test NAPI 2 + 3 = %{public}d', testNapi.add(2, 3));
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}

1.  Click the **Run** button in DevEco Studio to run the project. Then, click **clickTime=0** on the device to trigger the service logic.
    
2.  In the **Log** window of DevEco Studio, view the distributed tracing information.
    
    -   If **clickTime=1** is displayed on the device screen, the button is clicked once and the service logic is triggered.
        
    -   All HiLog logs in this example use **testTag**. You can filter logs by the keyword **testTag** to view the HiLog logs printed by the service code.
        
        06-05 21:26:01.006   9944-9944     C02D33/com.exa...tion/HiTraceC  com.examp...lication  I     \[a92ab19ae90197d 0 0\]HiTraceBegin name:testTag: hiTraceChain begin flags:0x00.
        06-05 21:26:01.006   9944-9944     A00000/com.exa...ation/testTag  com.examp...lication  I     \[a92ab19ae90197d 0 0\]HiTraceId is valid
        06-05 21:26:01.006   9944-9944     A00000/com.exa...ation/testTag  com.examp...lication  I     \[a92ab19ae90197d 0 0\]HITRACE\_FLAG\_INCLUDE\_ASYNC is enabled
        06-05 21:26:01.007   9944-9944     A00000/com.exa...ation/testTag  com.examp...lication  I     Add, HiTraceChain end
        06-05 21:26:01.007   9944-9944     A00000/com.exa...ation/testTag  com.examp...lication  I     Test NAPI 2 + 3 = 5
        06-05 21:26:01.007   9944-13961    A00000/com.exa...ation/testTag  com.examp...lication  I     \[a92ab19ae90197d 2544fdb 0\]Print1
        06-05 21:26:01.007   9944-13961    A00000/com.exa...ation/testTag  com.examp...lication  I     Print1, HiTraceChain end
        06-05 21:26:01.008   9944-13962    A00000/com.exa...ation/testTag  com.examp...lication  I     \[a92ab19ae90197d 236699a 2544fdb\]Print2
        06-05 21:26:01.008   9944-13962    A00000/com.exa...ation/testTag  com.examp...lication  I     Print2, HiTraceChain end
        
    -   The **\[chainId spanId parentSpanId\]** information added before the HiLog log is **HiTraceId** information. For example, **\[a92ab19ae90197d 236699a 2544fdb\]** indicates that the trace chain ID (**chainId**) is **a92ab19ae90197d**, the span ID (**spanId**) is **236699a**, and the parent span ID (**parentSpanId**) is **2544fdb**.
        
    -   Transfer the **HiTraceId**, create a **spanId**, and set it to the child thread created by **std::thread**. The HiLog logs of the Print1 and Print2 services running in the child thread also carry the same trace ID **a92ab19ae90197d** as that of the main thread.
        
    -   After the distributed tracing is ended using **OH\_HiTrace\_EndChain()** or **OH\_HiTrace\_ClearId()**, the HiLog print information does not carry the **HiTraceId** information.
