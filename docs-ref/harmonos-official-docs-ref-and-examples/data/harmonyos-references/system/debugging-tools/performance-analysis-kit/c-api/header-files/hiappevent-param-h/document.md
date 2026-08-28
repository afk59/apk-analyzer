# hiappevent\_param.h

#### Overview

Defines the names of all predefined event parameters. In addition to custom events associated with specific applications, you can use predefined events for logging.

**File to include**: <hiappevent/hiappevent\_param.h>

**Library**: libhiappevent\_ndk.z.so

**System capability**: SystemCapability.HiviewDFX.HiAppEvent

**Since**: 8

**Related module**: [HiAppEvent](../../modules/hiappevent/document.md)

#### Summary

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| [PARAM\_USER\_ID](#param_user_id) "user\_id" | 
User ID.

**Since**: 8

 |
| [PARAM\_DISTRIBUTED\_SERVICE\_NAME](#param_distributed_service_name) "ds\_name" | 

Distributed service name.

**Since**: 8

 |
| [PARAM\_DISTRIBUTED\_SERVICE\_INSTANCE\_ID](#param_distributed_service_instance_id) "ds\_instance\_id" | 

Distributed service instance ID.

**Since**: 8

 |
| [MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE](#main_thread_jank_param_log_type) "log\_type" | 

Type of the log collected by the main thread jank event detection. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL](#main_thread_jank_param_sample_interval) "sample\_interval" | 

Sampling interval of the main thread jank event detection. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_IGNORE\_STARTUP\_TIME](#main_thread_jank_param_ignore_startup_time) "ignore\_startup\_time" | 

Main thread jank event detection time ignored during application startup. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT](#main_thread_jank_param_sample_count) "sample\_count" | 

Number of stack samplings of the main thread timeout detection. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_REPORT\_TIMES\_PER\_APP](#main_thread_jank_param_report_times_per_app) "report\_times\_per\_app" | 

Number of sampling reporting times of the main thread jank event detection within a single lifecycle of an application PID, which can only be set once in a lifecycle. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

 |
| [MAIN\_THREAD\_JANK\_PARAM\_AUTO\_STOP\_SAMPLING](#main_thread_jank_param_auto_stop_sampling) "auto\_stop\_sampling" | 

Whether to stop sampling the main thread stack when the main thread jank event ends. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

 |

#### Macro Description

#### \[h2\]PARAM\_USER\_ID

#define PARAM\_USER\_ID "user\_id"

**Description**

User ID.

**Since**: 8

#### \[h2\]PARAM\_DISTRIBUTED\_SERVICE\_NAME

#define PARAM\_DISTRIBUTED\_SERVICE\_NAME "ds\_name"

**Description**

Distributed service name.

**Since**: 8

#### \[h2\]PARAM\_DISTRIBUTED\_SERVICE\_INSTANCE\_ID

#define PARAM\_DISTRIBUTED\_SERVICE\_INSTANCE\_ID "ds\_instance\_id"

**Description**

Distributed service instance ID.

**Since**: 8

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE

#define MAIN\_THREAD\_JANK\_PARAM\_LOG\_TYPE "log\_type"

**Description**

Type of the log collected by the main thread jank event detection. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL

#define MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_INTERVAL "sample\_interval"

**Description**

Sampling interval of the main thread jank event detection. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_IGNORE\_STARTUP\_TIME

#define MAIN\_THREAD\_JANK\_PARAM\_IGNORE\_STARTUP\_TIME "ignore\_startup\_time"

**Description**

Main thread jank event detection time ignored during application startup. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT

#define MAIN\_THREAD\_JANK\_PARAM\_SAMPLE\_COUNT "sample\_count"

**Description**

Number of stack samplings of the main thread timeout detection. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_REPORT\_TIMES\_PER\_APP

#define MAIN\_THREAD\_JANK\_PARAM\_REPORT\_TIMES\_PER\_APP "report\_times\_per\_app"

**Description**

Number of sampling reporting times of the main thread jank event detection within a single lifecycle of an application PID, which can only be set once in a lifecycle. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22

#### \[h2\]MAIN\_THREAD\_JANK\_PARAM\_AUTO\_STOP\_SAMPLING

#define MAIN\_THREAD\_JANK\_PARAM\_AUTO\_STOP\_SAMPLING "auto\_stop\_sampling"

**Description**

Whether to stop sampling the main thread stack. This macro is used for **MAIN\_THREAD\_JANK\_V2** events.

**Since**: 22
