# condition\_variable.h

#### Overview

The **condition\_variable.h** file declares the condition variable APIs in C.

**File to include**: <ffrt/condition\_variable.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API int ffrt\_cond\_init(ffrt\_cond\_t\* cond, const ffrt\_condattr\_t\* attr)](#ffrt_cond_init) | Initializes a condition variable. |
| [FFRT\_C\_API int ffrt\_cond\_signal(ffrt\_cond\_t\* cond)](#ffrt_cond_signal) | Unblocks at least one of the threads that are blocked on a condition variable. |
| [FFRT\_C\_API int ffrt\_cond\_broadcast(ffrt\_cond\_t\* cond)](#ffrt_cond_broadcast) | Unblocks all threads currently blocked on a condition variable. |
| [FFRT\_C\_API int ffrt\_cond\_wait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex)](#ffrt_cond_wait) | Blocks the calling thread on a condition variable. |
| [FFRT\_C\_API int ffrt\_cond\_timedwait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex, const struct timespec\* time\_point)](#ffrt_cond_timedwait) | Blocks the calling thread on a condition variable for a given duration. If **ffrt\_cond\_signal** or **ffrt\_cond\_broadcast** is not called to unblock the thread when the maximum wait time is reached, the thread is automatically unblocked. |
| [FFRT\_C\_API int ffrt\_cond\_destroy(ffrt\_cond\_t\* cond)](#ffrt_cond_destroy) | Destroys a condition variable. |

#### Function Description

#### \[h2\]ffrt\_cond\_init()

FFRT\_C\_API int ffrt\_cond\_init(ffrt\_cond\_t\* cond, const ffrt\_condattr\_t\* attr)

**Description**

Initializes a condition variable.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_cond\_t](../../structs/ffrt-cond-t/document.md)\* cond | Pointer to the condition variable. |
| [const ffrt\_condattr\_t](../../structs/ffrt-condattr-t/document.md)\* attr | Pointer to the condition variable attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the condition variable is initialized; returns **ffrt\_error\_inval** otherwise. |

#### \[h2\]ffrt\_cond\_signal()

FFRT\_C\_API int ffrt\_cond\_signal(ffrt\_cond\_t\* cond)

**Description**

Unblocks at least one of the threads that are blocked on a condition variable.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_cond\_t](../../structs/ffrt-cond-t/document.md)\* cond | Pointer to the condition variable. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if at least one of the threads is unblocked; returns **ffrt\_error\_inval** otherwise. |

#### \[h2\]ffrt\_cond\_broadcast()

FFRT\_C\_API int ffrt\_cond\_broadcast(ffrt\_cond\_t\* cond)

**Description**

Unblocks all threads currently blocked on a condition variable.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_cond\_t](../../structs/ffrt-cond-t/document.md)\* cond | Pointer to the condition variable. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if all threads are unblocked successfully; returns **ffrt\_error\_inval** otherwise. |

#### \[h2\]ffrt\_cond\_wait()

FFRT\_C\_API int ffrt\_cond\_wait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex)

**Description**

Blocks the calling thread on a condition variable.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_cond\_t](../../structs/ffrt-cond-t/document.md)\* cond | Pointer to the condition variable. |
| [ffrt\_mutex\_t](../../structs/ffrt-mutex-t/document.md)\* mutex | Pointer to the mutex. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the thread is unblocked after being blocked; returns **ffrt\_error\_inval** otherwise. |

#### \[h2\]ffrt\_cond\_timedwait()

FFRT\_C\_API int ffrt\_cond\_timedwait(ffrt\_cond\_t\* cond, ffrt\_mutex\_t\* mutex, const struct timespec\* time\_point)

**Description**

Blocks the calling thread on a condition variable for a given duration. If **ffrt\_cond\_signal** or **ffrt\_cond\_broadcast** is not called to unblock the thread when the maximum wait time is reached, the thread is automatically unblocked.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_cond\_t](../../structs/ffrt-cond-t/document.md)\* cond | Pointer to the condition variable. |
| [ffrt\_mutex\_t](../../structs/ffrt-mutex-t/document.md)\* mutex | Pointer to the mutex. |
| const struct timespec\* time\_point | Pointer to the maximum duration that the thread is blocked. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the thread is unblocked after being blocked; returns **ffrt\_error\_timedout** if the wait times out; returns **ffrt\_error\_inval** if the wait fails. |

#### \[h2\]ffrt\_cond\_destroy()

FFRT\_C\_API int ffrt\_cond\_destroy(ffrt\_cond\_t\* cond)

**Description**

Destroys a condition variable.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_cond\_t](../../structs/ffrt-cond-t/document.md)\* cond | Pointer to the condition variable. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the condition variable is destroyed successfully; returns **ffrt\_error\_inval** otherwise. |
