# hidebug.h

#### Overview

Defines the APIs for debugging.

**File to include**: <hidebug/hidebug.h>

**Library**: libohhidebug.so

**System capability**: SystemCapability.HiviewDFX.HiProfiler.HiDebug

**Since**: 12

**Related module**: [HiDebug](../../modules/hidebug/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [double OH\_HiDebug\_GetSystemCpuUsage()](#oh_hidebug_getsystemcpuusage) | \- | Obtains the CPU usage of the system. Note that this API involves cross-process communication and takes a long time. Therefore, you are advised not to call this API in the main thread. |
| [double OH\_HiDebug\_GetAppCpuUsage()](#oh_hidebug_getappcpuusage) | \- | Obtains the CPU usage of an application. Note that this API involves cross-process communication and takes a long time. Therefore, you are advised not to call this API in the main thread. |
| [HiDebug\_ThreadCpuUsagePtr OH\_HiDebug\_GetAppThreadCpuUsage()](#oh_hidebug_getappthreadcpuusage) | \- | Obtains the CPU usage of all threads of an application. Note that this API involves cross-process communication and takes a long time. Therefore, you are advised not to call this API in the main thread. |
| [void OH\_HiDebug\_FreeThreadCpuUsage(HiDebug\_ThreadCpuUsagePtr \*threadCpuUsage)](#oh_hidebug_freethreadcpuusage) | \- | Releases the **HiDebug\_ThreadCpuUsagePtr**. |
| [void OH\_HiDebug\_GetSystemMemInfo(HiDebug\_SystemMemInfo \*systemMemInfo)](#oh_hidebug_getsystemmeminfo) | \- | Obtains system memory information. |
| [void OH\_HiDebug\_GetAppNativeMemInfo(HiDebug\_NativeMemInfo \*nativeMemInfo)](#oh_hidebug_getappnativememinfo) | \- | Obtains the memory information of an application process. Note that this API needs to read the **/proc/{pid}/smaps\_rollup** node information, which takes a long time. Therefore, you are advised not to call this API in the main thread. |
| [void OH\_HiDebug\_GetAppNativeMemInfoWithCache(HiDebug\_NativeMemInfo \*nativeMemInfo, bool forceRefresh)](#oh_hidebug_getappnativememinfowithcache) | \- | Obtains the memory information of an application process. This API has a cache mechanism to improve its performance. The cache value is valid for 5 minutes. Note that this API needs to read the **/proc/{pid}/smaps\_rollup** node information, which takes a long time. Therefore, you are advised not to call this API in the main thread. |
| [void OH\_HiDebug\_GetAppMemoryLimit(HiDebug\_MemoryLimit \*memoryLimit)](#oh_hidebug_getappmemorylimit) | \- | Obtains the memory limit of an application process. |
| [HiDebug\_ErrorCode OH\_HiDebug\_StartAppTraceCapture(HiDebug\_TraceFlag flag, uint64\_t tags, uint32\_t limitSize, char\* fileName, uint32\_t length)](#oh_hidebug_startapptracecapture) | \- | Starts application trace collection. |
| [HiDebug\_ErrorCode OH\_HiDebug\_StopAppTraceCapture()](#oh_hidebug_stopapptracecapture) | \- | Stops application trace collection. |
| [HiDebug\_ErrorCode OH\_HiDebug\_GetGraphicsMemory(uint32\_t \*value)](#oh_hidebug_getgraphicsmemory) | \- | Obtains the size of the GPU memory. Note that this API involves multiple cross-process communications and may take more than 1 second. Therefore, you are advised not to call this API in the main thread. |
| [int OH\_HiDebug\_BacktraceFromFp(HiDebug\_Backtrace\_Object object, void\* startFp, void\*\* pcArray, int size)](#oh_hidebug_backtracefromfp) | \- | Performs stack back-tracing based on the given fp address. This function is async-signal-safe. |
| [typedef void (\*OH\_HiDebug\_SymbolicAddressCallback)(void\* pc, void\* arg, const HiDebug\_StackFrame\* frame)](#oh_hidebug_symbolicaddresscallback) | OH\_HiDebug\_SymbolicAddressCallback | 
If the [OH\_HiDebug\_SymbolicAddress](#oh_hidebug_symbolicaddress) API is successfully called, the parsed stack information is returned to the caller through this function.

Note: This API involves multiple I/O operations and takes a long time. Therefore, you are advised not to call this API in the main thread.

 |
| [HiDebug\_ErrorCode OH\_HiDebug\_SymbolicAddress(HiDebug\_Backtrace\_Object object, void\* pc, void\* arg, OH\_HiDebug\_SymbolicAddressCallback callback)](#oh_hidebug_symbolicaddress) | \- | 

Obtains detailed symbol information based on the specified PC address. This function is not asyn-signal-safe.

Note: This API involves multiple I/O operations and takes a long time. Therefore, you are advised not to call this API in the main thread.

 |
| [HiDebug\_Backtrace\_Object OH\_HiDebug\_CreateBacktraceObject(void)](#oh_hidebug_createbacktraceobject) | \- | 

Creates an object for stack backtracing and parsing. This function is not asyn-signal-safe.

Note: This API involves multiple I/O operations and takes a long time. Therefore, you are advised not to call this API in the main thread.

 |
| [void OH\_HiDebug\_DestroyBacktraceObject(HiDebug\_Backtrace\_Object object)](#oh_hidebug_destroybacktraceobject) | \- | Destroys the object created by [OH\_HiDebug\_CreateBacktraceObject](#oh_hidebug_createbacktraceobject) to release the resources applied for during stack back-tracing and parsing. This function is not asyn-signal-safe. |
| [HiDebug\_ErrorCode OH\_HiDebug\_SetMallocDispatchTable(struct HiDebug\_MallocDispatch \*dispatchTable)](#oh_hidebug_setmallocdispatchtable) | \- | 

Sets the **MallocDispatch** table in the basic C library to temporarily replace the original memory operation functions (such as **malloc**, **free**, **calloc**, **realloc**, **mmap**, and **munmap**) with the custom memory operation functions. The **MallocDispatch** table is a struct that encapsulates memory operation functions such as **malloc**, **calloc**, **realloc**, and **free** in the basic C library. **HiDebug\_MallocDispatch** is only a part of the **MallocDispatch** struct.

Note: Do not directly call memory operation functions such as **malloc**, **free**, **calloc**, **realloc**, **mmap**, and **munmap** in the **libc** standard library in the custom memory operation functions. Otherwise, a deadlock occurs. Do not use hilog to print logs in the custom **malloc** method. Otherwise, a deadlock occurs.

 |
| [HiDebug\_MallocDispatch\* OH\_HiDebug\_GetDefaultMallocDispatchTable(void)](#oh_hidebug_getdefaultmallocdispatchtable) | \- | Obtains the default MallocDispatch table of the system C library. You can call [OH\_HiDebug\_RestoreMallocDispatchTable](#oh_hidebug_restoremallocdispatchtable) to restore the table. |
| [void OH\_HiDebug\_RestoreMallocDispatchTable(void)](#oh_hidebug_restoremallocdispatchtable) | \- | Restores the MallocDispatch table of the system C library. |
| [HiDebug\_ErrorCode OH\_HiDebug\_GetGraphicsMemorySummary(uint32\_t interval, HiDebug\_GraphicsMemorySummary \*summary)](#oh_hidebug_getgraphicsmemorysummary) | \- | Obtains the detailed GPU memory usage of an application. |
| [typedef void (\*OH\_HiDebug\_ThreadLiteSamplingCallback)(const char\* stacks)](#oh_hidebug_threadlitesamplingcallback) | OH\_HiDebug\_ThreadLiteSamplingCallback | Triggered for the lightweight Perf sampling stack content. Note: The sampling data is valid only during the execution of this callback. If you need to use the data outside the function, deep copy the sampling stack content. |
| [HiDebug\_ErrorCode OH\_HiDebug\_RequestThreadLiteSampling(HiDebug\_ProcessSamplerConfig\* config, OH\_HiDebug\_ThreadLiteSamplingCallback stacksCallback)](#oh_hidebug_requestthreadlitesampling) | \- | Performs Perf sampling on the specified threads and returns the sampling stack content after the call is complete. Note: After this function is called, the current thread is blocked until the sampling process ends. The system strictly limits the number of times that this API is called. If the number of times that this API is called exceeds the upper limit, the error code [HIDEBUG\_RESOURCE\_UNAVAILABLE](../hidebug-type-h/document.md#hidebug_errorcode) is returned. |

#### Function Description

#### \[h2\]OH\_HiDebug\_GetSystemCpuUsage()

double OH\_HiDebug\_GetSystemCpuUsage()

**Description**

Obtains the CPU usage of the system. Note that this API involves cross-process communication and takes a long time. Therefore, you are advised not to call this API in the main thread.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| double | Returns the system CPU usage if the operation is successful. Returns **0** if the operation fails. |

#### \[h2\]OH\_HiDebug\_GetAppCpuUsage()

double OH\_HiDebug\_GetAppCpuUsage()

**Description**

Obtains the CPU usage of an application. Note that this API involves cross-process communication and takes a long time. Therefore, you are advised not to call this API in the main thread.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| double | Application CPU usage obtained if the operation is successful. If **0** is returned, the CPU usage of the current application is too low. |

#### \[h2\]OH\_HiDebug\_GetAppThreadCpuUsage()

HiDebug\_ThreadCpuUsagePtr OH\_HiDebug\_GetAppThreadCpuUsage()

**Description**

Obtains the CPU usage of all threads of an application. Note that this API involves cross-process communication and takes a long time. Therefore, you are advised not to call this API in the main thread.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_ThreadCpuUsagePtr](../../structs/hidebug-threadcpuusage/document.md) | 
CPU usage of all threads. For details, see [HiDebug\_ThreadCpuUsagePtr](../../structs/hidebug-threadcpuusage/document.md).

If null is returned, the thread data may not be obtained.

 |

#### \[h2\]OH\_HiDebug\_FreeThreadCpuUsage()

void OH\_HiDebug\_FreeThreadCpuUsage(HiDebug\_ThreadCpuUsagePtr \*threadCpuUsage)

**Description**

Releases the **HiDebug\_ThreadCpuUsagePtr**.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_ThreadCpuUsagePtr](../../structs/hidebug-threadcpuusage/document.md) \*threadCpuUsage | Pointer to the available CPU buffer of all threads of the application. For details, see [HiDebug\_ThreadCpuUsagePtr](../../structs/hidebug-threadcpuusage/document.md). The input parameter is obtained by **OH\_HiDebug\_GetAppThreadCpuUsage()**. |

#### \[h2\]OH\_HiDebug\_GetSystemMemInfo()

void OH\_HiDebug\_GetSystemMemInfo(HiDebug\_SystemMemInfo \*systemMemInfo)

**Description**

Obtains system memory information.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_SystemMemInfo](../../structs/hidebug-systemmeminfo/document.md) \*systemMemInfo | Pointer to [HiDebug\_SystemMemInfo](../../structs/hidebug-systemmeminfo/document.md). If the struct data is empty after the function is called, the calling fails. |

#### \[h2\]OH\_HiDebug\_GetAppNativeMemInfo()

void OH\_HiDebug\_GetAppNativeMemInfo(HiDebug\_NativeMemInfo \*nativeMemInfo)

**Description**

Obtains the memory information of an application process. Note that this API needs to read the **/proc/{pid}/smaps\_rollup** node information, which takes a long time. Therefore, you are advised not to call this API in the main thread.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_NativeMemInfo](../../structs/hidebug-nativememinfo/document.md) \*nativeMemInfo | Pointer to [HiDebug\_NativeMemInfo](../../structs/hidebug-nativememinfo/document.md). If the struct data is empty after the function is called, the calling fails. |

#### \[h2\]OH\_HiDebug\_GetAppNativeMemInfoWithCache()

void OH\_HiDebug\_GetAppNativeMemInfoWithCache(HiDebug\_NativeMemInfo \*nativeMemInfo, bool forceRefresh)

**Description**

Obtains the memory information of an application process. This API has a cache mechanism to improve its performance. The cache value is valid for 5 minutes. Note that this API needs to read the **/proc/{pid}/smaps\_rollup** node information, which takes a long time. Therefore, you are advised not to call this API in the main thread.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_NativeMemInfo](../../structs/hidebug-nativememinfo/document.md) \*nativeMemInfo | Pointer to [HiDebug\_NativeMemInfo](../../structs/hidebug-nativememinfo/document.md). If the struct data is empty after the function is called, the calling fails. |
| bool forceRefresh | 
Whether to ignore the cache validity and forcibly update the cache value.

The value **true** means to directly obtain the current memory data and update the cache value.

The value **false** means to directly return the cache value if the cache is valid and obtain the current memory data and update the cache value if the cache is invalid.

 |

#### \[h2\]OH\_HiDebug\_GetAppMemoryLimit()

void OH\_HiDebug\_GetAppMemoryLimit(HiDebug\_MemoryLimit \*memoryLimit)

**Description**

Obtains the memory limit of an application process.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_MemoryLimit](../../structs/hidebug-memorylimit/document.md) \*memoryLimit | Pointer to [HiDebug\_MemoryLimit](../../structs/hidebug-memorylimit/document.md). If the struct data is empty after the function is called, the calling fails. |

#### \[h2\]OH\_HiDebug\_StartAppTraceCapture()

HiDebug\_ErrorCode OH\_HiDebug\_StartAppTraceCapture(HiDebug\_TraceFlag flag, uint64\_t tags, uint32\_t limitSize, char\* fileName, uint32\_t length)

**Description**

Starts application trace collection.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_TraceFlag](../hidebug-type-h/document.md#hidebug_traceflag) flag | Type of the thread (the main thread or all threads of the application) to trace. |
| uint64\_t tags | Modules or subsystems to trace. |
| uint32\_t limitSize | Maximum size of the trace file (in bytes), which is 500 MB. |
| char\* fileName | Buffer for the output trace file. |
| uint32\_t length | Length of the buffer for the output trace file. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode) | 
**0** - The operation is successful.

[HIDEBUG\_INVALID\_ARGUMENT](../hidebug-type-h/document.md#hidebug_errorcode) 401 - The **fileName** parameter is a null pointer, the input **length** parameter is too small, or the **limitSize** parameter is less than or equal to 0.

**11400102** - A trace is already started.

**11400103** - You do not have the permission to start the trace function.

**11400104** - An internal system error occurs.

 |

#### \[h2\]OH\_HiDebug\_StopAppTraceCapture()

HiDebug\_ErrorCode OH\_HiDebug\_StopAppTraceCapture()

**Description**

Stops application trace collection.

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode) | 
**0** - The operation is successful.

**11400104** - An internal system error occurs.

**11400105** - No trace collection is running.

 |

#### \[h2\]OH\_HiDebug\_GetGraphicsMemory()

HiDebug\_ErrorCode OH\_HiDebug\_GetGraphicsMemory(uint32\_t \*value)

**Description**

Obtains the size of the GPU memory. Note that this API involves multiple cross-process communications and may take more than 1 second. Therefore, you are advised not to call this API in the main thread.

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t \*value | Pointer to the variable that stores the size (in KB) of the obtained GPU memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode) | 
**0** - The API is obtained successfully.

**401** - The parameter is a null pointer, which is invalid.

**11400104** - An internal system error occurs.

 |

#### \[h2\]OH\_HiDebug\_BacktraceFromFp()

int OH\_HiDebug\_BacktraceFromFp(HiDebug\_Backtrace\_Object object, void\* startFp, void\*\* pcArray, int size)

**Description**

Performs stack back-tracing based on the given fp address. This function is async-signal-safe.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_Backtrace\_Object](../../structs/hidebug-backtrace-object/document.md) object | Object obtained by the [OH\_HiDebug\_CreateBacktraceObject](#oh_hidebug_createbacktraceobject) API for stack backtracing. |
| void\* startFp | Start frame pointer for stack backtracing. |
| void\*\* pcArray | Array of PC addresses obtained from stack backtracing. |
| int size | Length of the PC address array obtained by stack backtracing. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Number of stack frames that are successfully backtraced and written to **pcArray**. If 0 is returned, stack backtracing may fail. |

#### \[h2\]OH\_HiDebug\_SymbolicAddressCallback()

typedef void (\*OH\_HiDebug\_SymbolicAddressCallback)(void\* pc, void\* arg, const HiDebug\_StackFrame\* frame)

**Description**

If the [OH\_HiDebug\_SymbolicAddress](#oh_hidebug_symbolicaddress) API is successfully called, the parsed stack information is returned to the caller through this function. Note: This API involves multiple I/O operations and takes a long time. Therefore, you are advised not to call this API in the main thread.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| void\* pc | PC address transferred to the [OH\_HiDebug\_SymbolicAddress](#oh_hidebug_symbolicaddress) API for parsing. |
| void\* arg | arg value of the [OH\_HiDebug\_SymbolicAddress](#oh_hidebug_symbolicaddress) API. |
| [const HiDebug\_StackFrame](../../structs/hidebug-stackframe/document.md)\* frame | Pointer to [HiDebug\_StackFrame](../../structs/hidebug-stackframe/document.md), which is obtained by parsing the PC address passed to the [OH\_HiDebug\_SymbolicAddress](#oh_hidebug_symbolicaddress) API. What the pointer points to is valid only in the function scope. |

#### \[h2\]OH\_HiDebug\_SymbolicAddress()

HiDebug\_ErrorCode OH\_HiDebug\_SymbolicAddress(HiDebug\_Backtrace\_Object object, void\* pc, void\* arg, OH\_HiDebug\_SymbolicAddressCallback callback)

**Description**

Obtains detailed symbol information based on the specified PC address. This function is not asyn-signal-safe.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/xv6KCrz3TWay_mYV26ElvA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062415Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABF77784752767CD60EA46263CA738ED62880503FEB51B058DD74BE81F68E02A)

This API involves multiple I/O operations and takes a long time. Therefore, you are advised not to call this API in the main thread.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_Backtrace\_Object](../../structs/hidebug-backtrace-object/document.md) object | Object created by the [OH\_HiDebug\_CreateBacktraceObject](#oh_hidebug_createbacktraceobject) API. |
| void\* pc | PC address obtained through the [OH\_HiDebug\_BacktraceFromFp](#oh_hidebug_backtracefromfp) API. |
| void\* arg | Reserved custom parameter. After the symbol is successfully parsed, this parameter is passed to [OH\_HiDebug\_SymbolicAddressCallback](#oh_hidebug_symbolicaddresscallback). |
| [OH\_HiDebug\_SymbolicAddressCallback](#oh_hidebug_symbolicaddresscallback) callback | Callback used to return the parsed stack information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode) | 
For details, see [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode).

[HIDEBUG\_SUCCESS](../hidebug-type-h/document.md#hidebug_errorcode): The detailed stack information is successfully obtained, and the callback input by the function is called.

[HIDEBUG\_INVALID\_ARGUMENT](../hidebug-type-h/document.md#hidebug_errorcode): Invalid parameter.

[HIDEBUG\_INVALID\_SYMBOLIC\_PC\_ADDRESS](../hidebug-type-h/document.md#hidebug_errorcode): Failed to find the corresponding symbol based on the input PC address.

 |

#### \[h2\]OH\_HiDebug\_CreateBacktraceObject()

HiDebug\_Backtrace\_Object OH\_HiDebug\_CreateBacktraceObject(void)

**Description**

Creates an object for stack backtracing and parsing. This function is not asyn-signal-safe.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/96putwrvR8SxkvQxcyY-pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062415Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6526175846A6CCFF43A06B7CCB0D89ACFAC371E13B4FFF77C133EC097EBA36E4)

This API involves multiple I/O operations and takes a long time. Therefore, you are advised not to call this API in the main thread.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_Backtrace\_Object](../../structs/hidebug-backtrace-object/document.md) | Pointer to the created object. If the object fails to be created, NULL is returned. |

#### \[h2\]OH\_HiDebug\_DestroyBacktraceObject()

void OH\_HiDebug\_DestroyBacktraceObject(HiDebug\_Backtrace\_Object object)

**Description**

Destroys the object created by [OH\_HiDebug\_CreateBacktraceObject](#oh_hidebug_createbacktraceobject) to release the resources applied for during stack backtracing and parsing. This function is not asyn-signal-safe.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_Backtrace\_Object](../../structs/hidebug-backtrace-object/document.md) object | Object to destroy. |

#### \[h2\]OH\_HiDebug\_SetMallocDispatchTable()

HiDebug\_ErrorCode OH\_HiDebug\_SetMallocDispatchTable(struct HiDebug\_MallocDispatch \*dispatchTable)

**Description**

Sets the **MallocDispatch** table in the basic C library to temporarily replace the original memory operation functions (such as **malloc**, **free**, **calloc**, **realloc**, **mmap**, and **munmap**) with the custom memory operation functions. The **MallocDispatch** table is a struct that encapsulates memory operation functions such as **malloc**, **calloc**, **realloc**, and **free** in the basic C library. **HiDebug\_MallocDispatch** is only a part of the **MallocDispatch** struct.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/CMlLmgg-QmuFbOleFeB8HA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062415Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A68073207437E4CFA66216B2C5B39E290A22CB1DE3632FAB46858F1B74139B75)

Do not directly call memory operation functions such as **malloc**, **free**, **calloc**, **realloc**, **mmap**, and **munmap** in the **libc** standard library in the custom memory operation functions. Otherwise, a deadlock occurs.

Do not use hilog to print logs in the custom **malloc** method. Otherwise, a deadlock occurs.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct HiDebug\_MallocDispatch](../../structs/hidebug-mallocdispatch/document.md) \*dispatchTable | Pointer to the [HiDebug\_MallocDispatch](../../structs/hidebug-mallocdispatch/document.md) struct that contains the custom memory operation functions. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode) | 
For details, see [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode).

[HIDEBUG\_SUCCESS](../hidebug-type-h/document.md#hidebug_errorcode): The custom memory operation function is set successfully.

[HIDEBUG\_INVALID\_ARGUMENT](../hidebug-type-h/document.md#hidebug_errorcode): Invalid parameter.

 |

#### \[h2\]OH\_HiDebug\_GetDefaultMallocDispatchTable()

HiDebug\_MallocDispatch\* OH\_HiDebug\_GetDefaultMallocDispatchTable(void)

**Description**

Obtains the default MallocDispatch table of the system C library. You can call [OH\_HiDebug\_RestoreMallocDispatchTable](#oh_hidebug_restoremallocdispatchtable) to restore the table.

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_MallocDispatch\*](../../structs/hidebug-mallocdispatch/document.md) | Pointer to the default [HiDebug\_MallocDispatch](../../structs/hidebug-mallocdispatch/document.md) struct of the current C library. |

#### \[h2\]OH\_HiDebug\_RestoreMallocDispatchTable()

void OH\_HiDebug\_RestoreMallocDispatchTable(void)

**Description**

Restores the MallocDispatch table of the system C library.

**Since**: 20

#### \[h2\]OH\_HiDebug\_GetGraphicsMemorySummary()

HiDebug\_ErrorCode OH\_HiDebug\_GetGraphicsMemorySummary(uint32\_t interval, HiDebug\_GraphicsMemorySummary \*summary)

**Description**

Obtains the detailed GPU memory usage of an application.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t interval | 
Interval that the cached GPU memory data exists, in seconds. If the duration exceeds the value of interval, the API obtains the latest data and updates the buffer. Otherwise, the API directly returns the cached data.

The value range of interval is \[2, 3600\]. If the passed-in interval is out of the range, **300** is used as the default value.

 |
| [HiDebug\_GraphicsMemorySummary](../../structs/hidebug-graphicsmemorysummary/document.md) \*summary | Pointer to [HiDebug\_GraphicsMemorySummary](../../structs/hidebug-graphicsmemorysummary/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode) | 
For details, see [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode).

**HIDEBUG\_SUCCESS**: The GPU memory information of the application is obtained successfully.

**HIDEBUG\_INVALID\_ARGUMENT**: Invalid parameter.

**HIDEBUG\_TRACE\_ABNORMAL**: Internal system error.

 |

#### \[h2\]OH\_HiDebug\_ThreadLiteSamplingCallback()

typedef void (\*OH\_HiDebug\_ThreadLiteSamplingCallback)(const char\* stacks)

**Description**

Triggered for the lightweight Perf sampling stack content. Note: The sampling data is valid only during the execution of this callback. If you need to use the data outside the function, deep copy the sampling stack content.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* stacks | Content of the sampling call stack. |

#### \[h2\]OH\_HiDebug\_RequestThreadLiteSampling()

HiDebug\_ErrorCode OH\_HiDebug\_RequestThreadLiteSampling(HiDebug\_ProcessSamplerConfig\* config, OH\_HiDebug\_ThreadLiteSamplingCallback stacksCallback)

**Description**

Performs Perf sampling on the specified threads and returns the sampling stack content after the call is complete. Note: After this function is called, the current thread is blocked until the sampling process ends. The system strictly limits the number of times that this API is called. If the number of times that this API is called exceeds the upper limit, the error code [HIDEBUG\_RESOURCE\_UNAVAILABLE](../hidebug-type-h/document.md#hidebug_errorcode) is returned.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiDebug\_ProcessSamplerConfig](../../structs/hidebug-processsamplerconfig/document.md)\* config | Pointer to the [HiDebug\_ProcessSamplerConfig](../../structs/hidebug-processsamplerconfig/document.md) struct. |
| [OH\_HiDebug\_ThreadLiteSamplingCallback](#oh_hidebug_threadlitesamplingcallback) stacksCallback | Callback used to return the sampling result when the sampling is complete. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiDebug\_ErrorCode](../hidebug-type-h/document.md#hidebug_errorcode) | 
Result code.

**HIDEBUG\_SUCCESS**: Sampling successful.

**HIDEBUG\_INVALID\_ARGUMENT**: Invalid parameter.

**HIDEBUG\_NOT\_SUPPORTED**: Perf sampling not supported.

**HIDEBUG\_UNDER\_SAMPLING**: A sampling task is in progress.

**HIDEBUG\_RESOURCE\_UNAVAILABLE**: Sampling resources are insufficient or the upper call limit is reached.

 |
