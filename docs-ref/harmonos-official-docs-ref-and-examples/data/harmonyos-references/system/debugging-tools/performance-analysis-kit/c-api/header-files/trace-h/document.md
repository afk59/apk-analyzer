# trace.h

#### Overview

Defines APIs of the **HiTraceMeter** and **HiTraceChain** modules for performance tracing and distributed tracing.

The vertical bar (|) is used as the separator in user-mode trace format. Therefore, the string parameters passed by the HiTraceMeter APIs must exclude this character to avoid trace parsing exceptions.

The maximum length of a user-mode trace is 512 characters. Excess characters will be truncated.

**File to include**: <hitrace/trace.h>

**Library**: libhitrace\_ndk.z.so

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 10

**Related module**: [HiTrace](../../modules/hitrace/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) | HiTraceId | Defines a **HiTraceId** instance. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [HiTraceId\_Valid](#hitraceid_valid) | HiTraceId\_Valid | Enumerates whether a **HiTraceId** instance is valid. |
| [HiTrace\_Version](#hitrace_version) | HiTrace\_Version | Enumerates the HiTrace versions. |
| [HiTrace\_Flag](#hitrace_flag) | HiTrace\_Flag | Enumerates the HiTrace flags. |
| [HiTrace\_Tracepoint\_Type](#hitrace_tracepoint_type) | HiTrace\_Tracepoint\_Type | Enumerates the trace point types. |
| [HiTrace\_Communication\_Mode](#hitrace_communication_mode) | HiTrace\_Communication\_Mode | Enumerates the trace communication types. |
| [HiTrace\_Output\_Level](#hitrace_output_level) | HiTrace\_Output\_Level | Enumerates the HiTrace output levels. The trace output level lower than the threshold does not take effect. The log version threshold is **HITRACE\_LEVEL\_INFO**, and the nolog version threshold is **HITRACE\_LEVEL\_COMMERCIAL**. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_HiTrace\_TraceEventListener)(bool traceStatus)](#oh_hitrace_traceeventlistener) | OH\_HiTrace\_TraceEventListener | Defines a callback to listen for whether the trace capture is enabled. |
| [HiTraceId OH\_HiTrace\_BeginChain(const char \*name, int flags)](#oh_hitrace_beginchain) | \- | 
Starts tracing.

If the current thread's TLS does not contain a valid HiTrace ID, this function generates one, stores it in TLS, and returns it.

If the current thread's TLS already contains a valid HiTrace ID, this function does not start tracing and returns an invalid HiTrace ID with all property values being 0.

 |
| [void OH\_HiTrace\_EndChain()](#oh_hitrace_endchain) | \- | 

Stops tracing.

Stops tracing and sets the HiTrace ID in the TLS of the current thread to invalid.

 |
| [HiTraceId OH\_HiTrace\_GetId()](#oh_hitrace_getid) | \- | 

Obtains the HiTrace ID in the TLS of the current thread.

 |
| [void OH\_HiTrace\_SetId(const HiTraceId \*id)](#oh_hitrace_setid) | \- | 

Sets the given HiTrace ID to the TLS of the current thread. If the given HiTrace ID is invalid, no operation is performed.

 |
| [void OH\_HiTrace\_ClearId(void)](#oh_hitrace_clearid) | \- | 

Clears the HiTrace ID in the current thread's TLS.

 |
| [HiTraceId OH\_HiTrace\_CreateSpan(void)](#oh_hitrace_createspan) | \- | 

Creates a trace span.

Specifically, create a **HiTraceId**, use the **chainId** and **spanId** in the TLS of the current thread to initialize the **chainId** and **parentSpanId** of the **HiTraceId**, generate a new **spanId** for the **HiTraceId**, and return the **HiTraceId**.

 |
| [void OH\_HiTrace\_Tracepoint(HiTrace\_Communication\_Mode mode, HiTrace\_Tracepoint\_Type type, const HiTraceId \*id, const char \*fmt, ...)](#oh_hitrace_tracepoint) | \- | 

Adds a trace point for the HiTraceMeter logging.

When **type** is set to **HITRACE\_TP\_CS** and **HITRACE\_TP\_SR**, the HiTraceMeter tracing starts. When **type** is set to **HITRACE\_TP\_CR** and **HITRACE\_TP\_SS**, the HiTraceMeter tracing ends. When **type** is set to **HITRACE\_TP\_GENERAL**, the HiTraceMeter tracing does not start.

The tracing points of **HITRACE\_TP\_CS** and **HITRACE\_TP\_CR** must be used in pairs; the tracing points of **HITRACE\_TP\_SR** and **HITRACE\_TP\_SS** must be used in pairs. Otherwise, the start and end trace points of HiTraceMeter cannot match each other.

 |
| [void OH\_HiTrace\_InitId(HiTraceId \*id)](#oh_hitrace_initid) | \- | Initializes a **HiTraceId**. |
| [void OH\_HiTrace\_IdFromBytes(HiTraceId \*id, const uint8\_t \*pIdArray, int len)](#oh_hitrace_idfrombytes) | \- | Creates a **HiTraceId** based on a byte array. |
| [bool OH\_HiTrace\_IsIdValid(const HiTraceId \*id)](#oh_hitrace_isidvalid) | \- | Checks whether the **HiTraceId** is valid. |
| [bool OH\_HiTrace\_IsFlagEnabled(const HiTraceId \*id, HiTrace\_Flag flag)](#oh_hitrace_isflagenabled) | \- | Checks whether the trace flag is enabled for the **HiTraceId**. |
| [void OH\_HiTrace\_EnableFlag(const HiTraceId \*id, HiTrace\_Flag flag)](#oh_hitrace_enableflag) | \- | Enables the trace flag specified in **HiTraceId**. |
| [int OH\_HiTrace\_GetFlags(const HiTraceId \*id)](#oh_hitrace_getflags) | \- | Obtains the trace flag set in **HiTraceId**. |
| [void OH\_HiTrace\_SetFlags(HiTraceId \*id, int flags)](#oh_hitrace_setflags) | \- | Sets the trace flag to [HiTraceId](../../structs/hitraceid/document.md). |
| [uint64\_t OH\_HiTrace\_GetChainId(const HiTraceId \*id)](#oh_hitrace_getchainid) | \- | Obtains the trace chain ID in **HiTraceId**. |
| [void OH\_HiTrace\_SetChainId(HiTraceId \*id, uint64\_t chainId)](#oh_hitrace_setchainid) | \- | Sets the trace chain ID in **HiTraceId**. |
| [uint64\_t OH\_HiTrace\_GetSpanId(const HiTraceId \*id)](#oh_hitrace_getspanid) | \- | Obtains the span ID in **HiTraceId**. |
| [void OH\_HiTrace\_SetSpanId(HiTraceId \*id, uint64\_t spanId)](#oh_hitrace_setspanid) | \- | Sets the span ID in **HiTraceId**. |
| [uint64\_t OH\_HiTrace\_GetParentSpanId(const HiTraceId \*id)](#oh_hitrace_getparentspanid) | \- | Obtains the parent span ID in **HiTraceId**. |
| [void OH\_HiTrace\_SetParentSpanId(HiTraceId \*id, uint64\_t parentSpanId)](#oh_hitrace_setparentspanid) | \- | Sets the **ParentSpanId** in a **HiTraceId** instance. |
| [int OH\_HiTrace\_IdToBytes(const HiTraceId\* id, uint8\_t\* pIdArray, int len)](#oh_hitrace_idtobytes) | \- | Converts **HiTraceId** into a byte array for cache or communication. |
| [void OH\_HiTrace\_StartTrace(const char \*name)](#oh_hitrace_starttrace) | \- | 

Marks the start of a synchronous trace.

This API is used with **OH\_HiTrace\_FinishTrace()** in pairs.

The two APIs can be nested. The stack data structure is used for matching during trace parsing.

Since API version 19, you are advised to use the **OH\_HiTrace\_StartTraceEx()** API to specify the trace output level.

 |
| [void OH\_HiTrace\_FinishTrace(void)](#oh_hitrace_finishtrace) | \- | 

Marks the end of a synchronous trace.

This API must be used with **OH\_HiTrace\_StartTrace()** in pairs. During trace parsing, the system matches it with the latest **OH\_HiTrace\_StartTrace()** API in the service process.

Since API version 19, you are advised to use the **OH\_HiTrace\_FinishTraceEx()** API to specify the trace output level.

 |
| [void OH\_HiTrace\_StartAsyncTrace(const char \*name, int32\_t taskId)](#oh_hitrace_startasynctrace) | \- | 

Marks the start of an asynchronous trace.

This API is used to start tracing before an asynchronous operation. The start and end of an asynchronous trace do not occur in sequence. Therefore, a unique task ID is required to identify them.

It must be used with **OH\_HiTrace\_FinishAsyncTrace()** in pairs. The start and end identified by the same name and task ID constitute an asynchronous trace task.

If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be performed multiple times concurrently, different task IDs must be specified.

If the trace tasks with the same name are not performed at the same time, the same **taskId** can be used.

Since API version 19, you are advised to use the **OH\_HiTrace\_StartAsyncTraceEx()** API to specify the trace output level and category.

 |
| [void OH\_HiTrace\_FinishAsyncTrace(const char \*name, int32\_t taskId)](#oh_hitrace_finishasynctrace) | \- | 

Marks the end of an asynchronous trace.

This API is called in the callback function after an asynchronous trace is complete.

It is used with **OH\_HiTrace\_StartAsyncTrace()** in pairs. Its name and task ID must be the same as those of **OH\_HiTrace\_StartAsyncTrace()**.

Since API version 19, you are advised to use the **OH\_HiTrace\_FinishAsyncTraceEx()** API to specify the trace output level.

 |
| [void OH\_HiTrace\_CountTrace(const char \*name, int64\_t count)](#oh_hitrace_counttrace) | \- | 

Traces the value change of an integer variable based on its name.

This API can be executed for multiple times to trace the value change of a given integer variable at different time points.

Since API version 19, you are advised to use the **OH\_HiTrace\_CountTraceEx()** API to specify the trace output level.

 |
| [void OH\_HiTrace\_StartTraceEx(HiTrace\_Output\_Level level, const char \*name, const char \*customArgs)](#oh_hitrace_starttraceex) | \- | 

Marks the start of a synchronous trace task with the trace output level specified.

This API is used with **OH\_HiTrace\_FinishTraceEx()** in pairs.

The two APIs can be nested. The stack data structure is used for matching during trace parsing.

 |
| [void OH\_HiTrace\_FinishTraceEx(HiTrace\_Output\_Level level)](#oh_hitrace_finishtraceex) | \- | 

Marks the end of a synchronous trace task with the trace output level specified.

It must be used with **OH\_HiTrace\_StartTraceEx()** in pairs. Its level must be the same as those of **OH\_HiTrace\_StartTraceEx()**.

During trace data parsing, the system matches it with the **OH\_HiTrace\_StartTraceEx()** API recently invoked in the service process.

 |
| [void OH\_HiTrace\_StartAsyncTraceEx(HiTrace\_Output\_Level level, const char \*name, int32\_t taskId, const char \*customCategory, const char \*customArgs)](#oh_hitrace_startasynctraceex) | \- | 

Marks the start of an asynchronous trace task with the trace output level specified.

This API is used to start tracing before an asynchronous operation. The start and end of an asynchronous trace do not occur in sequence. Therefore, a unique task ID is required to identify them.

It is used with **OH\_HiTrace\_FinishAsyncTraceEx()** in pairs. The start and end identified by the same name and task ID constitute an asynchronous trace task.

If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be performed multiple times concurrently, different task IDs must be specified.

If the trace tasks with the same name are not performed at the same time, the same **taskId** can be used.

Task IDs of different processes does not interfere with each other.

 |
| [void OH\_HiTrace\_FinishAsyncTraceEx(HiTrace\_Output\_Level level, const char \*name, int32\_t taskId)](#oh_hitrace_finishasynctraceex) | \- | 

Marks the end of an asynchronous trace task with the trace output level specified.

This API is used to stop tracing after an asynchronous operation is complete, for example, in a callback function.

It is used with **OH\_HiTrace\_StartAsyncTraceEx()** in pairs. Its level, name and task ID must be the same as those of **OH\_HiTrace\_StartAsyncTraceEx()**.

 |
| [void OH\_HiTrace\_CountTraceEx(HiTrace\_Output\_Level level, const char \*name, int64\_t count)](#oh_hitrace_counttraceex) | \- | Marks an integer variable trace task with the trace output level specified. |
| [bool OH\_HiTrace\_IsTraceEnabled(void)](#oh_hitrace_istraceenabled) | \- | Checks whether trace capture is enabled for an application. |
| [int32\_t OH\_HiTrace\_RegisterTraceListener(OH\_HiTrace\_TraceEventListener callback)](#oh_hitrace_registertracelistener) | \- | 

Registers a callback to notify whether the application trace capture is enabled. This API uses a synchronous callback to return the result.

After the registration is successful, the callback is executed immediately. Subsequent callbacks are executed when the application trace capture status changes.

Callbacks are stored in the application process. A maximum of 10 callbacks can be registered in a process.

If the callback contains time-consuming operations, the registration or unregistration will be blocked (waiting for the callback execution to complete) when the callback is executed.

Therefore, you are advised not to register or unregister callbacks containing time-consuming operations in the main thread of the application to avoid application freeze.

 |
| [int32\_t OH\_HiTrace\_UnregisterTraceListener(int32\_t index)](#oh_hitrace_unregistertracelistener) | \- | 

Unregisters the callback used to notify whether the application trace capture is enabled.

You can use this function to unregister the callback function associated with the callback index returned by [OH\_HiTrace\_RegisterTraceListener](#oh_hitrace_registertracelistener).

 |

#### Enum Description

#### \[h2\]HiTraceId\_Valid

enum HiTraceId\_Valid

**Description**

Enumerates whether a **HiTraceId** instance is valid.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HITRACE\_ID\_INVALID = 0 | 
Invalid **HiTraceId**.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_ID\_VALID = 1 | 

Valid **HiTraceId**.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |

#### \[h2\]HiTrace\_Version

enum HiTrace\_Version

**Description**

Enumerates the HiTrace versions.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HITRACE\_VER\_1 = 0 | 
Version 1.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |

#### \[h2\]HiTrace\_Flag

enum HiTrace\_Flag

**Description**

Enumerates the HiTrace flags.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HITRACE\_FLAG\_DEFAULT = 0 | 
Default flag.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_FLAG\_INCLUDE\_ASYNC = 1 << 0 | 

Asynchronous call flag.

When this flag is set, both synchronous and asynchronous calls are traced. By default, only synchronous calls are traced.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_FLAG\_DONOT\_CREATE\_SPAN = 1 << 1 | 

No span flag.

When this flag is set, no span information is created. By default, span information is created.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_FLAG\_TP\_INFO = 1 << 2 | 

Trace point flag.

When this flag is set in the debugging scenario, the HiLog logs of the trace point are printed upon calling the **OH\_HiTrace\_Tracepoint()** API. By default, the HiLog logs are not printed.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_FLAG\_NO\_BE\_INFO = 1 << 3 | 

No begin and end flag.

When this flag is set in the debugging scenario, the HiLog logs about the begin and end of tracing are printed when the **OH\_HiTrace\_BeginChain()** and **OH\_HiTrace\_EndChain()** APIs are called. By default, the HiLog logs about the begin and end of tracing are not printed.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_FLAG\_DONOT\_ENABLE\_LOG = 1 << 4 | 

Log association flag.

When this flag is set, the **HiTraceId** information is not added to the HiLog logs. By default, the **HiTraceId** information is added to the HiLog logs.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_FLAG\_FAULT\_TRIGGER = 1 << 5 | 

Failure trigger flag. This is a reserved flag.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_FLAG\_D2D\_TP\_INFO = 1 << 6 | 

Device-to-device trace point flag. It is a subset of **HITRACE\_FLAG\_TP\_INFO** and is used in debugging scenarios.

When the **HITRACE\_FLAG\_TP\_INFO** flag is set, the **HITRACE\_FLAG\_D2D\_TP\_INFO** flag does not take effect.

When **HITRACE\_FLAG\_TP\_INFO** is not set and **HITRACE\_FLAG\_D2D\_TP\_INFO** is set, the HiLog logs of the trace point are printed only when the **mode** parameter is set to **HITRACE\_CM\_DEVICE** upon calling **OH\_HiTrace\_Tracepoint()**.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |

#### \[h2\]HiTrace\_Tracepoint\_Type

enum HiTrace\_Tracepoint\_Type

**Description**

Enumerates the trace point types.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HITRACE\_TP\_CS = 0 | 
CS trace point.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_TP\_CR = 1 | 

CR trace point.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_TP\_SS = 2 | 

SS trace point.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_TP\_SR = 3 | 

SR trace point.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_TP\_GENERAL = 4 | 

General type, which identifies the trace points except **HITRACE\_TP\_CS**, **HITRACE\_TP\_CR**, **HITRACE\_TP\_SS**, and **HITRACE\_TP\_SR**.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |

#### \[h2\]HiTrace\_Communication\_Mode

enum HiTrace\_Communication\_Mode

**Description**

Enumerates the trace communication types.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HITRACE\_CM\_DEFAULT = 0 | 
Default communication.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_CM\_THREAD = 1 | 

Inter-thread communication.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_CM\_PROCESS = 2 | 

Inter-process communication (IPC).

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |
| HITRACE\_CM\_DEVICE = 3 | 

Inter-device communication.

**Since**: 12

**System capability**: SystemCapability.HiviewDFX.HiTrace

 |

#### \[h2\]HiTrace\_Output\_Level

enum HiTrace\_Output\_Level

**Description**

Enumerates the HiTrace output levels. The trace output level lower than the threshold does not take effect. The log version threshold is **HITRACE\_LEVEL\_INFO**, and the nolog version threshold is **HITRACE\_LEVEL\_COMMERCIAL**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 19

| Enum Item | Description |
| :-- | :-- |
| HITRACE\_LEVEL\_DEBUG = 0 | 
Level used only for debugging, which has the lowest priority.

**Since**: 19

 |
| HITRACE\_LEVEL\_INFO = 1 | 

Level for the log version.

**Since**: 19

 |
| HITRACE\_LEVEL\_CRITICAL = 2 | 

Level for the log version, which has a higher priority than **INFO**.

**Since**: 19

 |
| HITRACE\_LEVEL\_COMMERCIAL = 3 | 

Level for the nolog version, which has the highest priority.

**Since**: 19

 |
| HITRACE\_LEVEL\_MAX = HITRACE\_LEVEL\_COMMERCIAL | 

The maximum output level.

**Since**: 19

 |

#### Function Description

#### \[h2\]OH\_HiTrace\_TraceEventListener()

typedef void (\*OH\_HiTrace\_TraceEventListener)(bool traceStatus)

**Description**

Defines a callback to listen for whether the trace capture is enabled.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| bool traceStatus | 
Whether the trace capture is enabled for the current application.

The value **true** indicates that the trace capture is enabled, and **false** indicates the opposite.

 |

#### \[h2\]OH\_HiTrace\_BeginChain()

HiTraceId OH\_HiTrace\_BeginChain(const char \*name, int flags)

**Description**

Starts tracing.

If the current thread's TLS does not contain a valid HiTrace ID, this function generates one, stores it in TLS, and returns it.

If the current thread's TLS already contains a valid HiTrace ID, this function does not start tracing and returns an invalid HiTrace ID with all property values being 0.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Name of the traced service. |
| int flags | Trace flags. For details, see [HiTrace\_Flag](#hitrace_flag). |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) | The [HiTraceId](../../structs/hitraceid/document.md) struct. |

#### \[h2\]OH\_HiTrace\_EndChain()

void OH\_HiTrace\_EndChain()

**Description**

Stops tracing.

Stops tracing and sets the HiTrace ID in the TLS of the current thread to invalid.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

#### \[h2\]OH\_HiTrace\_GetId()

HiTraceId OH\_HiTrace\_GetId()

**Description**

Obtains the HiTrace ID in the TLS of the current thread.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) | The [HiTraceId](../../structs/hitraceid/document.md) struct. |

#### \[h2\]OH\_HiTrace\_SetId()

void OH\_HiTrace\_SetId(const HiTraceId \*id)

**Description**

Sets the given HiTrace ID to the TLS of the current thread. If the given HiTrace ID is invalid, no operation is performed.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to set. |

#### \[h2\]OH\_HiTrace\_ClearId()

void OH\_HiTrace\_ClearId(void)

**Description**

Clears the HiTrace ID in the current thread's TLS.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

#### \[h2\]OH\_HiTrace\_CreateSpan()

HiTraceId OH\_HiTrace\_CreateSpan(void)

**Description**

Creates a trace span.

Specifically, create a **HiTraceId**, use the **chainId** and **spanId** in the TLS of the current thread to initialize the **chainId** and **parentSpanId** of the **HiTraceId**, generate a new **spanId** for the **HiTraceId**, and return the **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) | The [HiTraceId](../../structs/hitraceid/document.md) struct. |

#### \[h2\]OH\_HiTrace\_Tracepoint()

void OH\_HiTrace\_Tracepoint(HiTrace\_Communication\_Mode mode, HiTrace\_Tracepoint\_Type type, const HiTraceId \*id, const char \*fmt, ...)

**Description**

Adds a trace point for the HiTraceMeter logging.

When **type** is set to **HITRACE\_TP\_CS** and **HITRACE\_TP\_SR**, the HiTraceMeter tracing starts. When **type** is set to **HITRACE\_TP\_CR** and **HITRACE\_TP\_SS**, the HiTraceMeter tracing ends. When **type** is set to **HITRACE\_TP\_GENERAL**, the HiTraceMeter tracing does not start.

The tracing points of **HITRACE\_TP\_CS** and **HITRACE\_TP\_CR** must be used in pairs; the tracing points of **HITRACE\_TP\_SR** and **HITRACE\_TP\_SS** must be used in pairs. Otherwise, the start and end trace points of HiTraceMeter cannot match each other.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTrace\_Communication\_Mode](#hitrace_communication_mode) mode | Trace communication mode. For details, see [HiTrace\_Communication\_Mode](#hitrace_communication_mode). |
| [HiTrace\_Tracepoint\_Type](#hitrace_tracepoint_type) type | Trace information type. For details, see [HiTrace\_Tracepoint\_Type](#hitrace_tracepoint_type). |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) for implementing trace points. |
| const char \*fmt | Formatted string of the trace description information passed by the HiTraceMeter logging. |

#### \[h2\]OH\_HiTrace\_InitId()

void OH\_HiTrace\_InitId(HiTraceId \*id)

**Description**

Initializes a **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to initialize. |

#### \[h2\]OH\_HiTrace\_IdFromBytes()

void OH\_HiTrace\_IdFromBytes(HiTraceId \*id, const uint8\_t \*pIdArray, int len)

**Description**

Creates a **HiTraceId** based on a byte array.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to create. |
| const uint8\_t \*pIdArray | Byte array. |
| int len | Length of the byte array. |

#### \[h2\]OH\_HiTrace\_IsIdValid()

bool OH\_HiTrace\_IsIdValid(const HiTraceId \*id)

**Description**

Checks whether the **HiTraceId** is valid.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to check. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | The value **true** indicates that [HiTraceId](../../structs/hitraceid/document.md) is valid, and **false** indicates the opposite. |

#### \[h2\]OH\_HiTrace\_IsFlagEnabled()

bool OH\_HiTrace\_IsFlagEnabled(const HiTraceId \*id, HiTrace\_Flag flag)

**Description**

Checks whether the trace flag is enabled for the **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to check. |
| [HiTrace\_Flag](#hitrace_flag) flag | Trace flag. For details, see [HiTrace\_Flag](#hitrace_flag). |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | The value **true** indicates that the flag is enabled for the [HiTraceId](../../structs/hitraceid/document.md), and **false** indicates the opposite. |

#### \[h2\]OH\_HiTrace\_EnableFlag()

void OH\_HiTrace\_EnableFlag(const HiTraceId \*id, HiTrace\_Flag flag)

**Description**

Enables the trace flag specified in **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) for which the trace flag is enabled. |
| [HiTrace\_Flag](#hitrace_flag) flag | Trace flag. For details, see [HiTrace\_Flag](#hitrace_flag). |

#### \[h2\]OH\_HiTrace\_GetFlags()

int OH\_HiTrace\_GetFlags(const HiTraceId \*id)

**Description**

Obtains the trace flag set in **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) for which the trace flag is obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Trace flag set in [HiTraceId](../../structs/hitraceid/document.md). |

#### \[h2\]OH\_HiTrace\_SetFlags()

void OH\_HiTrace\_SetFlags(HiTraceId \*id, int flags)

**Description**

Sets the trace flag to [HiTraceId](../../structs/hitraceid/document.md).

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to which the trace flag is set. |
| int flags | Trace flag. For details, see [HiTrace\_Flag](#hitrace_flag). |

#### \[h2\]OH\_HiTrace\_GetChainId()

uint64\_t OH\_HiTrace\_GetChainId(const HiTraceId \*id)

**Description**

Obtains the trace chain ID in **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) for which the trace chain ID is obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Trace chain ID. |

#### \[h2\]OH\_HiTrace\_SetChainId()

void OH\_HiTrace\_SetChainId(HiTraceId \*id, uint64\_t chainId)

**Description**

Sets the trace chain ID in **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to which the trace chain ID is to be set. |
| uint64\_t chainId | Trace chain ID to set. |

#### \[h2\]OH\_HiTrace\_GetSpanId()

uint64\_t OH\_HiTrace\_GetSpanId(const HiTraceId \*id)

**Description**

Obtains the span ID in **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) for which span ID is obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Span ID set in [HiTraceId](../../structs/hitraceid/document.md). |

#### \[h2\]OH\_HiTrace\_SetSpanId()

void OH\_HiTrace\_SetSpanId(HiTraceId \*id, uint64\_t spanId)

**Description**

Sets the span ID in **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to which the span ID is set. |
| uint64\_t spanId | Span ID to set. |

#### \[h2\]OH\_HiTrace\_GetParentSpanId()

uint64\_t OH\_HiTrace\_GetParentSpanId(const HiTraceId \*id)

**Description**

Obtains the parent span ID in **HiTraceId**.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) for which the parent span ID is obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint64\_t | Parent span ID set in [HiTraceId](../../structs/hitraceid/document.md). |

#### \[h2\]OH\_HiTrace\_SetParentSpanId()

void OH\_HiTrace\_SetParentSpanId(HiTraceId \*id, uint64\_t parentSpanId)

**Description**

Sets the **ParentSpanId** in a **HiTraceId** instance.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTraceId](../../structs/hitraceid/document.md) \*id | [HiTraceId](../../structs/hitraceid/document.md) to which the parent span ID is set. |
| uint64\_t parentSpanId | Parent span ID to set. |

#### \[h2\]OH\_HiTrace\_IdToBytes()

int OH\_HiTrace\_IdToBytes(const HiTraceId\* id, uint8\_t\* pIdArray, int len)

**Description**

Converts **HiTraceId** into a byte array for cache or communication.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [const HiTraceId](../../structs/hitraceid/document.md)\* id | [HiTraceId](../../structs/hitraceid/document.md) to convert. |
| uint8\_t\* pIdArray | Byte array. |
| int len | Length of the byte array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns the length of the byte array after conversion. |

#### \[h2\]OH\_HiTrace\_StartTrace()

void OH\_HiTrace\_StartTrace(const char \*name)

**Description**

Marks the start of a synchronous trace.

This API is used with **OH\_HiTrace\_FinishTrace()** in pairs.

The two APIs can be nested. The stack data structure is used for matching during trace parsing.

Since API version 19, you are advised to use the **OH\_HiTrace\_StartTraceEx()** API to specify the trace output level.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Name of a synchronous trace. |

#### \[h2\]OH\_HiTrace\_FinishTrace()

void OH\_HiTrace\_FinishTrace(void)

**Description**

Marks the end of a synchronous trace.

This API must be used with **OH\_HiTrace\_StartTrace()** in pairs. During trace parsing, the system matches it with the latest **OH\_HiTrace\_StartTrace()** API in the service process.

Since API version 19, you are advised to use the **OH\_HiTrace\_FinishTraceEx()** API to specify the trace output level.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 10

#### \[h2\]OH\_HiTrace\_StartAsyncTrace()

void OH\_HiTrace\_StartAsyncTrace(const char \*name, int32\_t taskId)

**Description**

Marks the start of an asynchronous trace.

This API is used to start tracing before an asynchronous operation. The start and end of an asynchronous trace do not occur in sequence. Therefore, a unique task ID is required to identify them.

It must be used with **OH\_HiTrace\_FinishAsyncTrace()** in pairs. The start and end identified by the same name and task ID constitute an asynchronous trace task.

If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be performed multiple times concurrently, different task IDs must be specified.

If the trace tasks with the same name are not performed at the same time, the same **taskId** can be used.

Since API version 19, you are advised to use the **OH\_HiTrace\_StartAsyncTraceEx()** API to specify the trace output level and category.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Name of the asynchronous trace. |
| int32\_t taskId | ID of the asynchronous trace. The start and end of an asynchronous trace do not occur in sequence. Therefore, the start and end of an asynchronous trace need to be matched based on the task name and the unique task ID together. |

#### \[h2\]OH\_HiTrace\_FinishAsyncTrace()

void OH\_HiTrace\_FinishAsyncTrace(const char \*name, int32\_t taskId)

**Description**

Marks the end of an asynchronous trace.

This API is called in the callback function after an asynchronous trace is complete.

It is used with **OH\_HiTrace\_StartAsyncTrace()** in pairs. Its name and task ID must be the same as those of **OH\_HiTrace\_StartAsyncTrace()**.

Since API version 19, you are advised to use the **OH\_HiTrace\_FinishAsyncTraceEx()** API to specify the trace output level.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Name of the asynchronous trace. |
| int32\_t taskId | ID of the asynchronous trace. The start and end of an asynchronous trace do not occur in sequence. Therefore, the start and end of an asynchronous trace need to be matched based on the task name and the unique task ID together. |

#### \[h2\]OH\_HiTrace\_CountTrace()

void OH\_HiTrace\_CountTrace(const char \*name, int64\_t count)

**Description**

Traces the value change of an integer variable based on its name.

This API can be executed for multiple times to trace the value change of a given integer variable at different time points.

Since API version 19, you are advised to use the **OH\_HiTrace\_CountTraceEx()** API to specify the trace output level.

**System capability**: SystemCapability.HiviewDFX.HiTrace

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Name of the integer variable. It does not need to be the same as the real variable name. |
| int64\_t count | Integer value. |

#### \[h2\]OH\_HiTrace\_StartTraceEx()

void OH\_HiTrace\_StartTraceEx(HiTrace\_Output\_Level level, const char \*name, const char \*customArgs)

**Description**

Marks the start of a synchronous trace task with the trace output level specified.

This API is used with **OH\_HiTrace\_FinishTraceEx()** in pairs.

The two APIs can be nested. The stack data structure is used for matching during trace parsing.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTrace\_Output\_Level](#hitrace_output_level) level | Trace output level. |
| const char \*name | Name of a synchronous trace. |
| const char \*customArgs | Key-value pair. Use commas (,) to separate multiple key-value pairs, for example, **"key1=value1,key2=value2"**. |

#### \[h2\]OH\_HiTrace\_FinishTraceEx()

void OH\_HiTrace\_FinishTraceEx(HiTrace\_Output\_Level level)

**Description**

Marks the end of a synchronous trace task with the trace output level specified.

It must be used with **OH\_HiTrace\_StartTraceEx()** in pairs. Its level must be the same as those of **OH\_HiTrace\_StartTraceEx()**.

During trace data parsing, the system matches it with the **OH\_HiTrace\_StartTraceEx()** API recently invoked in the service process.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTrace\_Output\_Level](#hitrace_output_level) level | Trace output level. |

#### \[h2\]OH\_HiTrace\_StartAsyncTraceEx()

void OH\_HiTrace\_StartAsyncTraceEx(HiTrace\_Output\_Level level, const char \*name, int32\_t taskId, const char \*customCategory, const char \*customArgs)

**Description**

Marks the start of an asynchronous trace task with the trace output level specified.

This API is used to start tracing before an asynchronous operation. The start and end of an asynchronous trace do not occur in sequence. Therefore, a unique task ID is required to identify them.

It is used with **OH\_HiTrace\_FinishAsyncTraceEx()** in pairs. The start and end identified by the same name and task ID constitute an asynchronous trace task.

If multiple trace tasks with the same name need to be performed at the same time or a trace task needs to be performed multiple times concurrently, different task IDs must be specified.

If the trace tasks with the same name are not performed at the same time, the same **taskId** can be used.

Task IDs of different processes does not interfere with each other.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTrace\_Output\_Level](#hitrace_output_level) level | Trace output level. |
| const char \*name | Name of the asynchronous trace. |
| int32\_t taskId | ID of the asynchronous trace. |
| const char \*customCategory | Custom category name, which is used to collect asynchronous trace data of the same type. |
| const char \*customArgs | Key-value pair. Use commas (,) to separate multiple key-value pairs, for example, **"key1=value1,key2=value2"**. |

#### \[h2\]OH\_HiTrace\_FinishAsyncTraceEx()

void OH\_HiTrace\_FinishAsyncTraceEx(HiTrace\_Output\_Level level, const char \*name, int32\_t taskId)

**Description**

Marks the end of an asynchronous trace task with the trace output level specified.

This API is used to stop tracing after an asynchronous operation is complete, for example, in a callback function.

It is used with **OH\_HiTrace\_StartAsyncTraceEx()** in pairs. Its level, name and task ID must be the same as those of **OH\_HiTrace\_StartAsyncTraceEx()**.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTrace\_Output\_Level](#hitrace_output_level) level | Trace output level. |
| const char \*name | Name of the asynchronous trace. |
| int32\_t taskId | ID of the asynchronous trace. |

#### \[h2\]OH\_HiTrace\_CountTraceEx()

void OH\_HiTrace\_CountTraceEx(HiTrace\_Output\_Level level, const char \*name, int64\_t count)

**Description**

Marks an integer variable trace task with the trace output level specified.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiTrace\_Output\_Level](#hitrace_output_level) level | Trace output level. |
| const char \*name | Name of the integer variable. It does not need to be the same as the actual variable name. |
| int64\_t count | Integer value. |

#### \[h2\]OH\_HiTrace\_IsTraceEnabled()

bool OH\_HiTrace\_IsTraceEnabled(void)

**Description**

Checks whether trace capture is enabled for an application.

**Since**: 19

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
When it is enabled, **true** is returned;

when it is disabled or stopped, **false** is returned. In this case, calling the HiTraceMeter API does not take effect.

 |

#### \[h2\]OH\_HiTrace\_RegisterTraceListener()

int32\_t OH\_HiTrace\_RegisterTraceListener(OH\_HiTrace\_TraceEventListener callback)

**Description**

Registers a callback to notify whether the application trace capture is enabled. This API uses a synchronous callback to return the result.

After the registration is successful, the callback is executed immediately. Subsequent callbacks are executed when the application trace capture status changes.

Callbacks are stored in the application process. A maximum of 10 callbacks can be registered in a process.

If the callback contains time-consuming operations, the registration or unregistration will be blocked (waiting for the callback execution to complete) when the callback is executed.

Therefore, you are advised not to register or unregister callbacks containing time-consuming operations in the main thread of the application to avoid application freeze.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_HiTrace\_TraceEventListener](#oh_hitrace_traceeventlistener) callback | Registered callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Callback registration status.

\>= **0**: The registration is successful. The callback index for unregistration is returned. The index ranges from 0 to 9.

**\-1**: The maximum number of callbacks has been reached.

**\-2**: Invalid parameter. The parameter is not of the **TraceEventListener** type.

 |

#### \[h2\]OH\_HiTrace\_UnregisterTraceListener()

int32\_t OH\_HiTrace\_UnregisterTraceListener(int32\_t index)

**Description**

Unregisters the callback used to notify whether the application trace capture is enabled.

You can use this function to unregister the callback function associated with the callback index returned by [OH\_HiTrace\_RegisterTraceListener](#oh_hitrace_registertracelistener).

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t index | Index of the registered callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Callback unregistration status.

**0**: Unregistration succeeded.

**\-1**: The callback corresponding to the index is not registered.

**\-2**: Invalid index. The index value is not within the range of 0 to 9.

 |
