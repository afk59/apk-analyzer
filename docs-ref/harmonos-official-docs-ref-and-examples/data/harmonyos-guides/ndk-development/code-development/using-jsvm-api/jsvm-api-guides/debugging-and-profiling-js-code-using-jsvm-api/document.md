# Debugging and Profiling JS Code Using JSVM-API

#### Introduction

JSVM-API provide APIs for retrieving JavaScript virtual machine (JSVM) instances and performing memory analysis, profiling, and debugging, which facilitates code optimization and improves development efficiency.

#### Basic Concepts

-   JSVM: A JSVM is an environment for executing JavaScript (JS) code. It parses and executes JS code, manages memory, and provides interaction with other system resources. For example, you can use **OH\_JSVM\_GetVM** to retrieve JSVM instances in a specific environment. This is one of the basic JSVM management operations.
-   Debug: As an important activity in program development, debugging involves locating, analyzing, and rectifying code errors. For example, you can use **OH\_JSVM\_OpenInspector** to open inspector, a tool used to debug JS code, on a host and port and view the running status of an application on a real-time basis. You can use **OH\_JSVM\_CloseInspector** to close inspector.

#### Available APIs

| API | Description |
| :-- | :-- |
| OH\_JSVM\_GetVM | Obtains a VM instance. |
| OH\_JSVM\_GetHeapStatistics | Obtains heap statistics of a VM. |
| OH\_JSVM\_StartCpuProfiler | Creates and starts a CPU profiler instance. |
| OH\_JSVM\_StopCpuProfiler | Stops the CPU profiler and outputs the result to a stream. |
| OH\_JSVM\_TakeHeapSnapshot | Obtains a snapshot of the current heap and outputs it to a stream. |
| OH\_JSVM\_OpenInspector | Opens an inspector instance on the specified host and port for debugging JS code. |
| OH\_JSVM\_OpenInspectorWithName | Opens an inspector instance based on the PID and name. |
| OH\_JSVM\_CloseInspector | Closes all remaining inspector connections. |
| OH\_JSVM\_WaitForDebugger | Waits for the host to set up a socket connection with an inspector. After the connection is set up, the application continues to run. You can use **Runtime.runIfWaitingForDebugger** to run paused targets. |

#### Example

If you are just starting out with JSVM-API, see [JSVM-API Development Process](../../jsvm-api-development-process/document.md). The following demonstrates only the C++ code involved in the APIs.

## OH\_JSVM\_GetVM

Retrieves VM instances in an environment.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_GetVM.
static JSVM\_Value GetVM(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain a VM instance for subsequent VM-related operations or analysis.
    JSVM\_VM testVm;
    JSVM\_Status status = OH\_JSVM\_GetVM(env, &testVm);
    JSVM\_Value result = nullptr;
    if (status != JSVM\_OK || testVm == nullptr) {
        OH\_LOG\_ERROR(LOG\_APP, "JSVM OH\_JSVM\_GetVM: failed");
        OH\_JSVM\_GetBoolean(env, true, &result);
    } else {
        OH\_LOG\_INFO(LOG\_APP, "JSVM OH\_JSVM\_GetVM: success");
        OH\_JSVM\_GetBoolean(env, false, &result);
    }
    return result;
}
// Register the GetVM callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetVM},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getVM and associate it with a callback. This allows the GetVM callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getVM", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(getVM())JS";

Expected result:

JSVM OH\_JSVM\_GetVM: success

## OH\_JSVM\_GetHeapStatistics

Obtains heap statistics of a VM.

CPP code:

// hello.cpp
#include "napi/native\_api.h"
#include "ark\_runtime/jsvm.h"
#include <hilog/log.h>

// Define OH\_JSVM\_GetHeapStatistics.
void PrintHeapStatistics(JSVM\_HeapStatistics result)
{
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap totalHeapSize: %{public}zu", result.totalHeapSize);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap totalHeapSizeExecutable: %{public}zu", result.totalHeapSizeExecutable);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap totalPhysicalSize: %{public}zu", result.totalPhysicalSize);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap totalAvailableSize: %{public}zu", result.totalAvailableSize);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap usedHeapSize: %{public}zu", result.usedHeapSize);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap heapSizeLimit: %{public}zu", result.heapSizeLimit);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap mallocedMemory: %{public}zu", result.mallocedMemory);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap externalMemory: %{public}zu", result.externalMemory);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap peakMallocedMemory: %{public}zu", result.peakMallocedMemory);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap numberOfNativeContexts: %{public}zu", result.numberOfNativeContexts);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap numberOfDetachedContexts: %{public}zu", result.numberOfDetachedContexts);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap totalGlobalHandlesSize: %{public}zu", result.totalGlobalHandlesSize);
    OH\_LOG\_INFO(LOG\_APP, "JSVM API heap usedGlobalHandlesSize: %{public}zu", result.usedGlobalHandlesSize);
}

static JSVM\_Value GetHeapStatistics(JSVM\_Env env, JSVM\_CallbackInfo info)
{
    // Obtain the VM instance.
    JSVM\_VM testVm;
    OH\_JSVM\_GetVM(env, &testVm);
    // Obtain the heap statistics of the VM.
    JSVM\_HeapStatistics result;
    OH\_JSVM\_GetHeapStatistics(testVm, &result);
    // Print VM heap statistics.
    PrintHeapStatistics(result);
    // Return the number of local contexts in the VM heap statistics.
    JSVM\_Value nativeContextsCnt = nullptr;
    OH\_JSVM\_CreateInt64(env, result.numberOfNativeContexts, &nativeContextsCnt);
    return nativeContextsCnt;
}
// Register the GetHeapStatistics callback.
static JSVM\_CallbackStruct param\[\] = {
    {.data = nullptr, .callback = GetHeapStatistics},
};
static JSVM\_CallbackStruct \*method = param;
// Set a property descriptor named getHeapStatistics and associate it with a callback. This allows the GetHeapStatistics callback to be called from JS.
static JSVM\_PropertyDescriptor descriptor\[\] = {
    {"getHeapStatistics", nullptr, method++, nullptr, nullptr, nullptr, JSVM\_DEFAULT},
};

JS example:

const char \*srcCallNative = R"JS(getHeapStatistics())JS";

Expected output (heap statistics of a VM, which change in real time):

JSVM API heap totalHeapSize: 1597440
JSVM API heap totalHeapSizeExecutable: 0
JSVM API heap totalPhysicalSize: 1323008
JSVM API heap totalAvailableSize: 1519203688
JSVM API heap usedHeapSize: 178256
JSVM API heap heapSizeLimit: 1518338048
JSVM API heap mallocedMemory: 32848
JSVM API heap externalMemory: 0
JSVM API heap peakMallocedMemory: 40960
JSVM API heap numberOfNativeContexts: 1
JSVM API heap numberOfDetachedContexts: 0
JSVM API heap totalGlobalHandlesSize: 8192
JSVM API heap usedGlobalHandlesSize: 32

For details about the sample code of the previous APIs, see:

[JSVM-API Debugging](../../typical-jsvm-api-use-cases/jsvm-api-debugging/document.md)

## OH\_JSVM\_StartCpuProfiler

Creates and starts a CPU profiler instance.

## OH\_JSVM\_StopCpuProfiler

Stops the CPU profiler and output the result to a stream.

## OH\_JSVM\_TakeHeapSnapshot

Obtains the current heap snapshot and outputs it to the stream.

## OH\_JSVM\_OpenInspector

Opens an inspector instance on a specified host and port for debugging JS code.

## OH\_JSVM\_CloseInspector

Closes all remaining inspector connections.

## OH\_JSVM\_WaitForDebugger

Waits for the host to set up a socket connection with the inspector. After the connection is set up, the program continues to run and sends the **Runtime.runIfWaitingForDebugger** command.
