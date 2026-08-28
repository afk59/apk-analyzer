# type\_def.h

#### Overview

The **type\_def.h** file declares the common types.

**File to include**: <ffrt/type\_def.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Variables

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| int | ffrt\_timer\_t | Handle to the timer. |
| int | ffrt\_qos\_t | QoS type. |
| using qos = int | \- | 
QoS type.

**Since**: 10

 |

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ffrt\_function\_header\_t](../../structs/ffrt-function-header-t/document.md) | ffrt\_function\_header\_t | Describes a task execution function. |
| [ffrt\_dependence\_t](../../structs/ffrt-dependence-t/document.md) | ffrt\_dependence\_t | Describes dependency data. |
| [ffrt\_deps\_t](../../structs/ffrt-deps-t/document.md) | ffrt\_deps\_t | Describes dependencies. |
| [ffrt\_task\_attr\_t](../../structs/ffrt-task-attr-t/document.md) | ffrt\_task\_attr\_t | Describes a task attribute. |
| [ffrt\_queue\_attr\_t](../../structs/ffrt-queue-attr-t/document.md) | ffrt\_queue\_attr\_t | Describes a serial queue attribute. |
| [ffrt\_condattr\_t](../../structs/ffrt-condattr-t/document.md) | ffrt\_condattr\_t | Describes a condition variable attribute. |
| [ffrt\_mutexattr\_t](../../structs/ffrt-mutexattr-t/document.md) | ffrt\_mutexattr\_t | Describes a mutex attribute. |
| [ffrt\_rwlockattr\_t](../../structs/ffrt-rwlockattr-t/document.md) | ffrt\_rwlockattr\_t | Describes a read-write lock attribute. |
| [ffrt\_mutex\_t](../../structs/ffrt-mutex-t/document.md) | ffrt\_mutex\_t | Describes a mutex. |
| [ffrt\_rwlock\_t](../../structs/ffrt-rwlock-t/document.md) | ffrt\_rwlock\_t | Describes a read-write lock. |
| [ffrt\_cond\_t](../../structs/ffrt-cond-t/document.md) | ffrt\_cond\_t | Describes a condition variable. |
| void\* | [ffrt\_task\_handle\_t](../../structs/ffrt-task-handle-t/document.md) | Defines the handle to a task. |
| [ffrt\_fiber\_t](../../structs/ffrt-fiber-t/document.md) | ffrt\_fiber\_t | Fiber structure. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ffrt\_queue\_priority\_t](#ffrt_queue_priority_t) | ffrt\_queue\_priority\_t | Enumerates the task priority types. |
| [ffrt\_qos\_default\_t](#ffrt_qos_default_t) | ffrt\_qos\_default\_t | Enumerates the task QoS types. |
| [ffrt\_storage\_size\_t](#ffrt_storage_size_t) | ffrt\_storage\_size\_t | Enumerates the storage sizes available for different types of structs. |
| [ffrt\_function\_kind\_t](#ffrt_function_kind_t) | ffrt\_function\_kind\_t | Enumerates the task types. |
| [ffrt\_dependence\_type\_t](#ffrt_dependence_type_t) | ffrt\_dependence\_type\_t | Enumerates the dependency types. |
| [ffrt\_error\_t](#ffrt_error_t) | ffrt\_error\_t | Enumerates the FFRT error codes. |
| [ffrt\_mutex\_type](#ffrt_mutex_type) | ffrt\_mutex\_type | Enumerates the mutex types. **ffrt\_mutex\_normal** indicates a normal mutex, **ffrt\_mutex\_recursive** indicates a recursive mutex, and **ffrt\_mutex\_default** indicates a default mutex. |
| [qos\_default](#qos_default) | \- | Enumerates the task QoS types. |

#### \[h2\]Function

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void(\*ffrt\_function\_t)(void\*)](#ffrt_function_t) | ffrt\_function\_t | Defines the type of the pointer to a task execution function. |
| [typedef void (\*ffrt\_poller\_cb)(void\* data, uint32\_t event)](#ffrt_poller_cb) | ffrt\_poller\_cb | Defines the poller callback function. |
| [typedef void (\*ffrt\_timer\_cb)(void\* data)](#ffrt_timer_cb) | ffrt\_timer\_cb | Defines the timer callback function. |

#### Enum Description

#### \[h2\]ffrt\_queue\_priority\_t

enum ffrt\_queue\_priority\_t

**Description**

Enumerates the task priority types.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| ffrt\_queue\_priority\_immediate = 0 | Immediate priority. |
| ffrt\_queue\_priority\_high | High priority. |
| ffrt\_queue\_priority\_low | Low priority. |
| ffrt\_queue\_priority\_idle | Lowest priority. |

#### \[h2\]ffrt\_qos\_default\_t

enum ffrt\_qos\_default\_t

**Description**

Enumerates the task QoS types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| ffrt\_qos\_inherit = -1 | Inherited task QoS. |
| ffrt\_qos\_background | Background task. |
| ffrt\_qos\_utility | Real-time utility. |
| ffrt\_qos\_default | Default type. |
| ffrt\_qos\_user\_initiated | User initiated. |

#### \[h2\]ffrt\_storage\_size\_t

enum ffrt\_storage\_size\_t

**Description**

Enumerates the storage sizes available for different types of structs.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| ffrt\_task\_attr\_storage\_size = 128 | Storage size for the task attribute struct. |
| ffrt\_auto\_managed\_function\_storage\_size = 64 + sizeof(ffrt\_function\_header\_t) | Storage size for the task execution function struct. |
| ffrt\_mutex\_storage\_size = 64 | Storage size for the mutex struct. |
| ffrt\_cond\_storage\_size = 64 | Storage size for the condition variable struct. |
| ffrt\_queue\_attr\_storage\_size = 128 | Storage size for the queue attribute struct. |
| ffrt\_rwlock\_storage\_size = 64 | 
Read-write lock.

**Since**: 18

 |
| ffrt\_fiber\_storage\_size | 

Fiber size across different platforms (in bytes). AArch64 architecture: 22 bytes; Arm architecture: 64 bytes; x86\_64 architecture: 8 bytes; other platforms: not supported.

**Since**: 20

 |

#### \[h2\]ffrt\_function\_kind\_t

enum ffrt\_function\_kind\_t

**Description**

Task type.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| ffrt\_function\_kind\_general | General task. |
| ffrt\_function\_kind\_queue | Queue task. |

#### \[h2\]ffrt\_dependence\_type\_t

enum ffrt\_dependence\_type\_t

**Description**

Enumerates the dependency types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| ffrt\_dependence\_data | Data dependency. |
| ffrt\_dependence\_task | Task dependency. |

#### \[h2\]ffrt\_error\_t

enum ffrt\_error\_t

**Description**

Enumerates the FFRT error codes.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| ffrt\_error = -1 | Failure. |
| ffrt\_success = 0 | Success. |
| ffrt\_error\_nomem = ENOMEM | Insufficient memory. |
| ffrt\_error\_timedout = ETIMEDOUT | Timeout. |
| ffrt\_error\_busy = EBUSY | Try again. |
| ffrt\_error\_inval = EINVAL | Invalid value. |

#### \[h2\]ffrt\_mutex\_type

enum ffrt\_mutex\_type

**Description**

Enumerates the mutex types. **ffrt\_mutex\_normal** indicates a normal mutex, **ffrt\_mutex\_recursive** indicates a recursive mutex, and **ffrt\_mutex\_default** indicates a default mutex.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| ffrt\_mutex\_normal = 0 | Normal mutex. |
| ffrt\_mutex\_recursive = 2 | Recursive mutex. |
| ffrt\_mutex\_default = ffrt\_mutex\_normal | Default mutex. |

#### \[h2\]qos\_default

enum qos\_default

**Description**

Enumerates the task QoS types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| qos\_inherit = ffrt\_qos\_inherit | Inherited task QoS. |
| qos\_background = ffrt\_qos\_background | Background task. |
| qos\_utility = ffrt\_qos\_utility | Real-time utility. |
| qos\_default = ffrt\_qos\_default | Default type. |
| qos\_user\_initiated = ffrt\_qos\_user\_initiated | User initiated. |

#### Function Description

#### \[h2\]ffrt\_function\_t()

typedef void(\*ffrt\_function\_t)(void\*)

**Description**

Defines the type of the pointer to a task execution function.

**Since**: 10

#### \[h2\]ffrt\_poller\_cb()

typedef void (\*ffrt\_poller\_cb)(void\* data, uint32\_t event)

**Description**

Defines the poller callback function.

**Since**: 12

#### \[h2\]ffrt\_timer\_cb()

typedef void (\*ffrt\_timer\_cb)(void\* data)

**Description**

Defines the timer callback function.

**Since**: 12
