# mutex.h

#### Overview

The **mutex.h** file declares the mutex APIs in C.

**File to include**: <ffrt/mutex.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API int ffrt\_mutexattr\_init(ffrt\_mutexattr\_t\* attr)](#ffrt_mutexattr_init) | Initializes the mutex attribute. |
| [FFRT\_C\_API int ffrt\_mutexattr\_settype(ffrt\_mutexattr\_t\* attr, int type)](#ffrt_mutexattr_settype) | Sets the mutex attribute type. |
| [FFRT\_C\_API int ffrt\_mutexattr\_gettype(ffrt\_mutexattr\_t\* attr, int\* type)](#ffrt_mutexattr_gettype) | Obtains the mutex type. |
| [FFRT\_C\_API int ffrt\_mutexattr\_destroy(ffrt\_mutexattr\_t\* attr)](#ffrt_mutexattr_destroy) | Destroys the mutex attribute. This API needs to be called by users. |
| [FFRT\_C\_API int ffrt\_mutex\_init(ffrt\_mutex\_t\* mutex, const ffrt\_mutexattr\_t\* attr)](#ffrt_mutex_init) | Initializes a mutex. |
| [FFRT\_C\_API int ffrt\_mutex\_lock(ffrt\_mutex\_t\* mutex)](#ffrt_mutex_lock) | Locks a mutex. |
| [FFRT\_C\_API int ffrt\_mutex\_unlock(ffrt\_mutex\_t\* mutex)](#ffrt_mutex_unlock) | Unlocks a mutex. |
| [FFRT\_C\_API int ffrt\_mutex\_trylock(ffrt\_mutex\_t\* mutex)](#ffrt_mutex_trylock) | Attempts to lock a mutex. |
| [FFRT\_C\_API int ffrt\_mutex\_destroy(ffrt\_mutex\_t\* mutex)](#ffrt_mutex_destroy) | Destroys a mutex. |

#### Function Description

#### \[h2\]ffrt\_mutexattr\_init()

FFRT\_C\_API int ffrt\_mutexattr\_init(ffrt\_mutexattr\_t\* attr)

**Description**

Initializes the mutex attribute.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutexattr\_t](../../structs/ffrt-mutexattr-t/document.md)\* attr | Pointer to the mutex attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex attribute is initialized;

returns **ffrt\_error\_inval** otherwise.

 |

#### \[h2\]ffrt\_mutexattr\_settype()

FFRT\_C\_API int ffrt\_mutexattr\_settype(ffrt\_mutexattr\_t\* attr, int type)

**Description**

Sets the mutex attribute type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutexattr\_t](../../structs/ffrt-mutexattr-t/document.md)\* attr | Pointer to the mutex attribute. |
| int type | Mutex type. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex attribute type is set;

returns **ffrt\_error\_inval** if the pointer to the mutex attribute is null

or the mutex is not of the **ffrt\_mutex\_normal** or **ffrt\_mutex\_recursive** type.

 |

#### \[h2\]ffrt\_mutexattr\_gettype()

FFRT\_C\_API int ffrt\_mutexattr\_gettype(ffrt\_mutexattr\_t\* attr, int\* type)

**Description**

Obtains the mutex type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutexattr\_t](../../structs/ffrt-mutexattr-t/document.md)\* attr | Pointer to the mutex attribute. |
| int\* type | Pointer to the mutex type. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex type is obtained;

returns **ffrt\_error\_inval** if the pointer to the mutex attribute or mutex type is null.

 |

#### \[h2\]ffrt\_mutexattr\_destroy()

FFRT\_C\_API int ffrt\_mutexattr\_destroy(ffrt\_mutexattr\_t\* attr)

**Description**

Destroys the mutex attribute. This API needs to be called by users.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutexattr\_t](../../structs/ffrt-mutexattr-t/document.md)\* attr | Pointer to the mutex attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex attribute is destroyed;

returns **ffrt\_error\_inval** otherwise.

 |

#### \[h2\]ffrt\_mutex\_init()

FFRT\_C\_API int ffrt\_mutex\_init(ffrt\_mutex\_t\* mutex, const ffrt\_mutexattr\_t\* attr)

**Description**

Initializes a mutex.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutex\_t](../../structs/ffrt-mutex-t/document.md)\* mutex | Pointer to the mutex. |
| [const ffrt\_mutexattr\_t](../../structs/ffrt-mutexattr-t/document.md)\* attr | Pointer to the mutex attribute. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex is initialized;

returns **ffrt\_error\_inval** otherwise.

 |

#### \[h2\]ffrt\_mutex\_lock()

FFRT\_C\_API int ffrt\_mutex\_lock(ffrt\_mutex\_t\* mutex)

**Description**

Locks a mutex.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutex\_t](../../structs/ffrt-mutex-t/document.md)\* mutex | Pointer to the mutex. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex is locked;

returns **ffrt\_error\_inval** or blocks the calling thread otherwise.

 |

#### \[h2\]ffrt\_mutex\_unlock()

FFRT\_C\_API int ffrt\_mutex\_unlock(ffrt\_mutex\_t\* mutex)

**Description**

Unlocks a mutex.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutex\_t](../../structs/ffrt-mutex-t/document.md)\* mutex | Pointer to the mutex. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex is unlocked;

returns **ffrt\_error\_inval** otherwise.

 |

#### \[h2\]ffrt\_mutex\_trylock()

FFRT\_C\_API int ffrt\_mutex\_trylock(ffrt\_mutex\_t\* mutex)

**Description**

Attempts to lock a mutex.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutex\_t](../../structs/ffrt-mutex-t/document.md)\* mutex | Pointer to the mutex. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex is locked;

returns **ffrt\_error\_inval** or **ffrt\_error\_busy** otherwise.

 |

#### \[h2\]ffrt\_mutex\_destroy()

FFRT\_C\_API int ffrt\_mutex\_destroy(ffrt\_mutex\_t\* mutex)

**Description**

Destroys a mutex.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_mutex\_t](../../structs/ffrt-mutex-t/document.md)\* mutex | Pointer to the mutex. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the mutex is destroyed successfully;

returns **ffrt\_error\_inval** otherwise.

 |
