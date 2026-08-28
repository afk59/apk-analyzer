# hicollie.h

#### Overview

HiCollie provides APIs for checking service thread stuck and jank events and reporting stuck events.

**File to include**: <hicollie/hicollie.h>

**Library**: libohhicollie.so

**System capability**: SystemCapability.HiviewDFX.HiCollie

**Since**: 12

**Related module**: [HiCollie](../../modules/hicollie/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [HiCollie\_DetectionParam](../../structs/hicollie-detectionparam/document.md) | HiCollie\_DetectionParam | Defines the parameters of the jank event detection. Note that this struct is supported since API 12. |
| [HiCollie\_SetTimerParam](../../structs/hicollie-settimerparam/document.md) | HiCollie\_SetTimerParam | Defines the input parameters of the **OH\_HiCollie\_SetTimer** function. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [HiCollie\_ErrorCode](#hicollie_errorcode) | HiCollie\_ErrorCode | Enumerates the error codes used in the HiCollie module. |
| [HiCollie\_Flag](#hicollie_flag) | HiCollie\_Flag | Enumerates the actions to be performed when a function times out. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_HiCollie\_Task)(void)](#oh_hicollie_task) | OH\_HiCollie\_Task | 
Checks whether a service thread is stuck.

This function is called by HiCollie every 3 seconds in a service thread.

For example, this function can be used to send a message to a service thread and set a flag after the service thread receives the message. Then the flag is checked to determine whether the service thread is stuck.

 |
| [typedef void (\*OH\_HiCollie\_BeginFunc)(const char\* eventName)](#oh_hicollie_beginfunc) | OH\_HiCollie\_BeginFunc | 

Records the begin time when a service thread processes an event. This function is used in the jank event detection.

HiCollie checks the execution time of the event. If the duration exceeds the preset threshold, a jank event is reported.

This function is inserted before each event is processed.

 |
| [typedef void (\*OH\_HiCollie\_EndFunc)(const char\* eventName)](#oh_hicollie_endfunc) | OH\_HiCollie\_EndFunc | 

Checks whether a service thread is janky when processing an event. This function is used in the jank event detection.

HiCollie checks the execution time of the event. If the duration exceeds the preset threshold, a jank event is reported.

This function is inserted after each event is processed.

 |
| [HiCollie\_ErrorCode OH\_HiCollie\_Init\_StuckDetection(OH\_HiCollie\_Task task)](#oh_hicollie_init_stuckdetection) | \- | 

Registers a callback used to periodically detect service thread stuck events.

By default, the **BUSSINESS\_THREAD\_BLOCK\_3S** event is reported when the thread is blocked for 3s and the **BUSSINESS\_THREAD\_BLOCK\_6S** event is reported when the thread is blocked for 6s.

Note: Use this API in non-main threads.

 |
| [HiCollie\_ErrorCode OH\_HiCollie\_Init\_StuckDetectionWithTimeout(OH\_HiCollie\_Task task, uint32\_t stuckTimeout)](#oh_hicollie_init_stuckdetectionwithtimeout) | \- | 

Registers a callback used to periodically detect service thread stuck events.

You can set the interval for the stuck event detection. The value range is \[3, 15\], in seconds.

Note: Use this API in non-main threads.

 |
| [HiCollie\_ErrorCode OH\_HiCollie\_Init\_JankDetection(OH\_HiCollie\_BeginFunc\* beginFunc, OH\_HiCollie\_EndFunc\* endFunc, HiCollie\_DetectionParam param)](#oh_hicollie_init_jankdetection) | \- | 

Registers a callback used to detect service thread jank events.

To monitor service thread jank events, you can implement two callbacks as instrumentation functions, placing them before and after the service thread event.

Note: Use this API in non-main threads.

 |
| [HiCollie\_ErrorCode OH\_HiCollie\_Report(bool\* isSixSecond)](#oh_hicollie_report) | \- | 

Reports a service thread stuck event and generates logs to help locate application stuck issues.

Call **OH\_HiCollie\_Init\_StuckDetection()** or **OH\_HiCollie\_Init\_StuckDetectionWithTimeout()** to initialize the detection task.

If the task times out, call **OH\_HiCollie\_Report()** to report the stuck event based on the service logic.

Note: Use this API in non-main threads.

 |
| [typedef void (\*OH\_HiCollie\_Callback)(void\*)](#oh_hicollie_callback) | OH\_HiCollie\_Callback | Triggered when [OH\_HiCollie\_CancelTimer](#oh_hicollie_canceltimer) is not called within the custom task timeout period after [OH\_HiCollie\_SetTimer](#oh_hicollie_settimer) is called. |
| [HiCollie\_ErrorCode OH\_HiCollie\_SetTimer(HiCollie\_SetTimerParam param, int \*id)](#oh_hicollie_settimer) | \- | 

Registers a timer to check whether the execution time of a function or code block exceeds the custom time.

This API is used together with the **OH\_HiCollie\_CancelTimer** API.

 |
| [void OH\_HiCollie\_CancelTimer(int id)](#oh_hicollie_canceltimer) | \- | 

Cancels a timer based on the ID.

This API is used together with the **OH\_HiCollie\_SetTimer** API. It must be used after the function or code block is executed.

If a timer is not canceled within the custom time, a callback function is executed to generate fault logs for the specified timeout event.

 |

#### Enum Description

#### \[h2\]HiCollie\_ErrorCode

enum HiCollie\_ErrorCode

**Description**

Enumerates the error codes used in the HiCollie module.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| HICOLLIE\_SUCCESS = 0 | The operation is successful. |
| HICOLLIE\_INVALID\_ARGUMENT = 401 | The parameter is invalid. |
| HICOLLIE\_WRONG\_THREAD\_CONTEXT = 29800001 | The called thread is incorrect. |
| HICOLLIE\_REMOTE\_FAILED = 29800002 | The remote call fails. |
| HICOLLIE\_INVALID\_TIMER\_NAME = 29800003 | 
The timer name is invalid.

**Since**: 18

 |
| HICOLLIE\_INVALID\_TIMEOUT\_VALUE = 29800004 | 

The function execution timeout value is invalid.

**Since**: 18

 |
| HICOLLIE\_WRONG\_PROCESS\_CONTEXT = 29800005 | 

The process to be accessed is incorrect.

**Since**: 18

 |
| HICOLLIE\_WRONG\_TIMER\_ID\_OUTPUT\_PARAM = 29800006 | 

The pointer used to save the returned timer ID is null.

**Since**: 18

 |

#### \[h2\]HiCollie\_Flag

enum HiCollie\_Flag

**Description**

Enumerates the actions to be performed when a function times out.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| HICOLLIE\_FLAG\_DEFAULT = (~0) | Generates logs and recovers the function. This is the default action. |
| HICOLLIE\_FLAG\_NOOP = (0) | Executes only the callback. |
| HICOLLIE\_FLAG\_LOG = (1 << 0) | Generates logs. |
| HICOLLIE\_FLAG\_RECOVERY = (1 << 1) | Recovers the function. |

#### Function Description

#### \[h2\]OH\_HiCollie\_Task()

typedef void (\*OH\_HiCollie\_Task)(void)

**Description**

Checks whether a service thread is stuck.

This function is called by HiCollie every 3 seconds in a service thread.

For example, this function can be used to send a message to a service thread and set a flag after the service thread receives the message. Then the flag is checked to determine whether the service thread is stuck.

**Since**: 12

#### \[h2\]OH\_HiCollie\_BeginFunc()

typedef void (\*OH\_HiCollie\_BeginFunc)(const char\* eventName)

**Description**

Records the begin time when a service thread processes an event. This function is used in the jank event detection.

HiCollie checks the execution time of the event. If the duration exceeds the preset threshold, a jank event is reported.

This function is inserted before each event is processed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* eventName | Name of the service thread event. |

#### \[h2\]OH\_HiCollie\_EndFunc()

typedef void (\*OH\_HiCollie\_EndFunc)(const char\* eventName)

**Description**

Checks whether a service thread is janky when processing an event. This function is used in the jank event detection.

HiCollie checks the execution time of the event. If the duration exceeds the preset threshold, a jank event is reported.

This function is inserted after each event is processed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* eventName | Name of the service thread event. |

#### \[h2\]OH\_HiCollie\_Init\_StuckDetection()

HiCollie\_ErrorCode OH\_HiCollie\_Init\_StuckDetection(OH\_HiCollie\_Task task)

**Description**

Registers a callback used to periodically detect service thread stuck events.

By default, the **BUSSINESS\_THREAD\_BLOCK\_3S** event is reported when the thread is blocked for 3s and the **BUSSINESS\_THREAD\_BLOCK\_6S** event is reported when the thread is blocked for 6s.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_HiCollie\_Task](#oh_hicollie_task) task | A periodic detection task that is executed every 3 seconds to check whether a service thread is stuck. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiCollie\_ErrorCode](#hicollie_errorcode) | 
[HICOLLIE\_SUCCESS](#hicollie_errorcode) 0 - Operation successful.

[HICOLLIE\_WRONG\_THREAD\_CONTEXT](#hicollie_errorcode) 29800001 - Incorrect calling thread. This function should be called in a non-main thread.

For details, see [HiCollie\_ErrorCode](#hicollie_errorcode).

 |

#### \[h2\]OH\_HiCollie\_Init\_StuckDetectionWithTimeout()

HiCollie\_ErrorCode OH\_HiCollie\_Init\_StuckDetectionWithTimeout(OH\_HiCollie\_Task task, uint32\_t stuckTimeout)

**Description**

Registers a callback used to periodically detect service thread stuck events.

You can set the interval for the stuck event detection. The value range is \[3, 15\], in seconds.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_HiCollie\_Task](#oh_hicollie_task) task | Periodic detection task that is executed every **stuckTimeout** time to check whether a service thread is stuck. |
| uint32\_t stuckTimeout | 
Threshold for reporting a service thread stuck event, in seconds. When the task execution time exceeds the value of **stuckTimeout**, a stuck warning event is reported. When the task execution time exceeds twice the value of **stuckTimeout**, a stuck event is reported.

The maximum value is **15s** and the minimum value is **3s**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiCollie\_ErrorCode](#hicollie_errorcode) | 
[HICOLLIE\_SUCCESS](#hicollie_errorcode) 0 - Operation successful.

[HICOLLIE\_INVALID\_ARGUMENT](#hicollie_errorcode) 401 - Invalid detection time.

[HICOLLIE\_WRONG\_THREAD\_CONTEXT](#hicollie_errorcode) 29800001 - Incorrect calling thread. This function should be called in a non-main thread.

For details, see [HiCollie\_ErrorCode](#hicollie_errorcode).

 |

#### \[h2\]OH\_HiCollie\_Init\_JankDetection()

HiCollie\_ErrorCode OH\_HiCollie\_Init\_JankDetection(OH\_HiCollie\_BeginFunc\* beginFunc, OH\_HiCollie\_EndFunc\* endFunc, HiCollie\_DetectionParam param)

**Description**

Registers a callback used to detect service thread jank events.

To monitor service thread jank events, you can implement two callbacks as instrumentation functions, placing them before and after the service thread event.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_HiCollie\_BeginFunc](#oh_hicollie_beginfunc)\* beginFunc | Function used before the service thread event detection. |
| [OH\_HiCollie\_EndFunc](#oh_hicollie_endfunc)\* endFunc | Function used after the service thread event detection. |
| [HiCollie\_DetectionParam](../../structs/hicollie-detectionparam/document.md) param | Extended parameter for future use. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiCollie\_ErrorCode](#hicollie_errorcode) | 
[HICOLLIE\_SUCCESS](#hicollie_errorcode) 0 - Operation successful.

[HICOLLIE\_INVALID\_ARGUMENT](#hicollie_errorcode) 401 - The begin and end functions are not both set or both unset; they must either both have valid values or both be empty.

[HICOLLIE\_WRONG\_THREAD\_CONTEXT](#hicollie_errorcode) 29800001 - Incorrect calling thread. This function should be called in a non-main thread.

For details, see [HiCollie\_ErrorCode](#hicollie_errorcode).

 |

#### \[h2\]OH\_HiCollie\_Report()

HiCollie\_ErrorCode OH\_HiCollie\_Report(bool\* isSixSecond)

**Description**

Reports a service thread stuck event and generates logs to help locate application stuck issues.

Call **OH\_HiCollie\_Init\_StuckDetection()** or **OH\_HiCollie\_Init\_StuckDetectionWithTimeout()** to initialize the detection task.

If the task times out, call **OH\_HiCollie\_Report()** to report the stuck event based on the service logic.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| bool\* isSixSecond | Pointer to a Boolean value. If the service thread is stuck for 6s, the value is **true**. If the service thread is stuck for 3s, the value is **false**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiCollie\_ErrorCode](#hicollie_errorcode) | 
[HICOLLIE\_SUCCESS](#hicollie_errorcode) 0 - Operation successful.

[HICOLLIE\_INVALID\_ARGUMENT](#hicollie_errorcode) 401 - The begin and end functions are not both set or both unset; they must either both have valid values or both be empty.

[HICOLLIE\_WRONG\_THREAD\_CONTEXT](#hicollie_errorcode) 29800001 - Incorrect calling thread. This function should be called in a non-main thread.

[HICOLLIE\_REMOTE\_FAILED](#hicollie_errorcode) 29800002 - Remote call error. The IPC remote service fails to be called.

For details, see [HiCollie\_ErrorCode](#hicollie_errorcode).

 |

#### \[h2\]OH\_HiCollie\_Callback()

typedef void (\*OH\_HiCollie\_Callback)(void\*)

**Description**

Triggered when [OH\_HiCollie\_CancelTimer](#oh_hicollie_canceltimer) is not called within the custom task timeout period after [OH\_HiCollie\_SetTimer](#oh_hicollie_settimer) is called.

**Since**: 18

#### \[h2\]OH\_HiCollie\_SetTimer()

HiCollie\_ErrorCode OH\_HiCollie\_SetTimer(HiCollie\_SetTimerParam param, int \*id)

**Description**

Registers a timer to check whether the execution time of a function or code block exceeds the custom time.

This API is used together with the **OH\_HiCollie\_CancelTimer** API.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [HiCollie\_SetTimerParam](../../structs/hicollie-settimerparam/document.md) param | Input parameters. |
| int \*id | Pointer to the returned timer ID, which should not be NULL. |

**Returns**

| Type | Description |
| :-- | :-- |
| [HiCollie\_ErrorCode](#hicollie_errorcode) | 
[HICOLLIE\_SUCCESS](#hicollie_errorcode) 0 - Operation successful.

[HICOLLIE\_INVALID\_TIMER\_NAME](#hicollie_errorcode) 29800003 - Invalid timer name. The timer name cannot be NULL or an empty string.

[HICOLLIE\_INVALID\_TIMEOUT\_VALUE](#hicollie_errorcode) 29800004 - Invalid timeout value.

[HICOLLIE\_WRONG\_PROCESS\_CONTEXT](#hicollie_errorcode) 29800005 - Invalid process context for detection. This function cannot be called in the **appspawn** and **nativespawn** processes.

[HICOLLIE\_WRONG\_TIMER\_ID\_OUTPUT\_PARAM](#hicollie_errorcode) 29800006 - The pointer used to save the returned timer ID is NULL.

For details, see [HiCollie\_ErrorCode](#hicollie_errorcode).

 |

#### \[h2\]OH\_HiCollie\_CancelTimer()

void OH\_HiCollie\_CancelTimer(int id)

**Description**

Cancels a timer based on the ID.

This API is used together with the **OH\_HiCollie\_SetTimer** API. It must be used after the function or code block is executed.

If a timer is not canceled within the custom time, a callback function is executed to generate fault logs for the specified timeout event.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| int id | Timer ID updated after the [OH\_HiCollie\_SetTimer](#oh_hicollie_settimer) function is executed. |
