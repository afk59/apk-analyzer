# sleep.h

#### Overview

The **sleep.h** file declares the sleep and yield APIs in C.

**File to include**: <ffrt/sleep.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 10

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API int ffrt\_usleep(uint64\_t usec)](#ffrt_usleep) | Sets the fixed sleep time. |
| [FFRT\_C\_API void ffrt\_yield(void)](#ffrt_yield) | Passes control to other tasks so that they can be executed. |

#### Function Description

#### \[h2\]ffrt\_usleep()

FFRT\_C\_API int ffrt\_usleep(uint64\_t usec)

**Description**

Sets the fixed sleep time.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t usec | Sleep time, in microseconds. |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | 
Returns **ffrt\_success** if the sleep time is set;

returns **ffrt\_error** otherwise.

 |

#### \[h2\]ffrt\_yield()

FFRT\_C\_API void ffrt\_yield(void)

**Description**

Passes control to other tasks so that they can be executed.

**Since**: 10
