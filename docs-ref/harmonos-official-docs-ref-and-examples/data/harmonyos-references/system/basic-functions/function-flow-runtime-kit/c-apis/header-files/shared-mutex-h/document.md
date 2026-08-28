# shared\_mutex.h

#### Overview

The **shared\_mutex.h** file declares read-write lock APIs in C.

**File to include**: <ffrt/shared\_mutex.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 18

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API int ffrt\_rwlock\_init(ffrt\_rwlock\_t\* rwlock, const ffrt\_rwlockattr\_t\* attr)](#ffrt_rwlock_init) | Initializes a read-write lock. |
| [FFRT\_C\_API int ffrt\_rwlock\_wrlock(ffrt\_rwlock\_t\* rwlock)](#ffrt_rwlock_wrlock) | Obtains a write lock. |
| [FFRT\_C\_API int ffrt\_rwlock\_trywrlock(ffrt\_rwlock\_t\* rwlock)](#ffrt_rwlock_trywrlock) | Attempts to obtain a write lock. |
| [FFRT\_C\_API int ffrt\_rwlock\_rdlock(ffrt\_rwlock\_t\* rwlock)](#ffrt_rwlock_rdlock) | Obtains a read lock. |
| [FFRT\_C\_API int ffrt\_rwlock\_tryrdlock(ffrt\_rwlock\_t\* rwlock)](#ffrt_rwlock_tryrdlock) | Attempts to obtain a read lock. |
| [FFRT\_C\_API int ffrt\_rwlock\_unlock(ffrt\_rwlock\_t\* rwlock)](#ffrt_rwlock_unlock) | Releases the read-write lock. |
| [FFRT\_C\_API int ffrt\_rwlock\_destroy(ffrt\_rwlock\_t\* rwlock)](#ffrt_rwlock_destroy) | Destroys the read-write lock. |

#### Function Description

#### \[h2\]ffrt\_rwlock\_init()

FFRT\_C\_API int ffrt\_rwlock\_init(ffrt\_rwlock\_t\* rwlock, const ffrt\_rwlockattr\_t\* attr)

**Description**

Initializes a read-write lock.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_rwlock\_t](../../structs/ffrt-rwlock-t/document.md)\* rwlock | Pointer to the read-write lock. |
| [const ffrt\_rwlockattr\_t](../../structs/ffrt-rwlockattr-t/document.md)\* attr | Pointer to the **rwlock** property. Only the default value (null) is supported. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | If rwlock is not empty and attr is empty, the initialization is successful, and **ffrt\_success** is returned. Otherwise, the rwlock fails to be initialized, and **ffrt\_error\_inval** is returned. |

#### \[h2\]ffrt\_rwlock\_wrlock()

FFRT\_C\_API int ffrt\_rwlock\_wrlock(ffrt\_rwlock\_t\* rwlock)

**Description**

Obtains a write lock.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_rwlock\_t](../../structs/ffrt-rwlock-t/document.md)\* rwlock | Pointer to the read-write lock. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the write lock is successfully obtained; returns **ffrt\_error\_inval** or blocks the task otherwise. |

#### \[h2\]ffrt\_rwlock\_trywrlock()

FFRT\_C\_API int ffrt\_rwlock\_trywrlock(ffrt\_rwlock\_t\* rwlock)

**Description**

Attempts to obtain a write lock.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_rwlock\_t](../../structs/ffrt-rwlock-t/document.md)\* rwlock | Pointer to the read-write lock. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the write lock is successfully obtained; returns **ffrt\_error\_inval** or **ffrt\_error\_busy** otherwise. |

#### \[h2\]ffrt\_rwlock\_rdlock()

FFRT\_C\_API int ffrt\_rwlock\_rdlock(ffrt\_rwlock\_t\* rwlock)

**Description**

Obtains a read lock.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_rwlock\_t](../../structs/ffrt-rwlock-t/document.md)\* rwlock | Pointer to the read-write lock. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the read lock is successfully obtained; returns **ffrt\_error\_inval** or blocks the task otherwise. |

#### \[h2\]ffrt\_rwlock\_tryrdlock()

FFRT\_C\_API int ffrt\_rwlock\_tryrdlock(ffrt\_rwlock\_t\* rwlock)

**Description**

Attempts to obtain a read lock.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_rwlock\_t](../../structs/ffrt-rwlock-t/document.md)\* rwlock | Pointer to the read-write lock. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the read lock is successfully obtained; returns **ffrt\_error\_inval** or **ffrt\_error\_busy** otherwise. |

#### \[h2\]ffrt\_rwlock\_unlock()

FFRT\_C\_API int ffrt\_rwlock\_unlock(ffrt\_rwlock\_t\* rwlock)

**Description**

Releases the read-write lock.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_rwlock\_t](../../structs/ffrt-rwlock-t/document.md)\* rwlock | Pointer to the read-write lock. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the read-write lock is successfully released; returns **ffrt\_error\_inval** otherwise. |

#### \[h2\]ffrt\_rwlock\_destroy()

FFRT\_C\_API int ffrt\_rwlock\_destroy(ffrt\_rwlock\_t\* rwlock)

**Description**

Destroys the read-write lock.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_rwlock\_t](../../structs/ffrt-rwlock-t/document.md)\* rwlock | Pointer to the read-write lock. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | Returns **ffrt\_success** if the read-write lock is destroyed successfully; returns **ffrt\_error\_inval** otherwise. |
