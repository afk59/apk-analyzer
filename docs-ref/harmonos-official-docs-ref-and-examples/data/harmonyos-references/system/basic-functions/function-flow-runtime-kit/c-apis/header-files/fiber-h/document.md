# fiber.h

#### Overview

A fiber is a lightweight user mode thread that enables efficient task scheduling and context switching within the user space. The **fiber.h** file declares the related APIs in C.

**File to include**: <ffrt/fiber.h>

**Library**: libffrt.z.so

**System capability**: SystemCapability.Resourceschedule.Ffrt.Core

**Since**: 20

**Related module**: [FFRT](../../modules/ffrt/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [FFRT\_C\_API int ffrt\_fiber\_init(ffrt\_fiber\_t\* fiber, void(\*func)(void\*), void\* arg, void\* stack, size\_t stack\_size)](#ffrt_fiber_init) | Initializes a fiber. The initialized fiber instance can store contexts. |
| [FFRT\_C\_API void ffrt\_fiber\_switch(ffrt\_fiber\_t\* from, ffrt\_fiber\_t\* to)](#ffrt_fiber_switch) | Switches between fibers. The thread that calls this function suspends the current task, saves the context to the **from** fiber, and restores the context of the **to** fiber. |

#### Function Description

#### \[h2\]ffrt\_fiber\_init()

FFRT\_C\_API int ffrt\_fiber\_init(ffrt\_fiber\_t\* fiber, void(\*func)(void\*), void\* arg, void\* stack, size\_t stack\_size)

**Description**

Initializes a fiber. The initialized fiber instance can store contexts.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| fiber | Pointer to the fiber to be initialized. For details, see [ffrt\_fiber\_t](../../structs/ffrt-fiber-t/document.md). |
| func | Method to be executed after fiber switching. |
| void\* arg | Pointer to the argument of the method. |
| void\* stack | Pointer to the fiber stack memory. |
| size\_t stack\_size | Fiber stack size. For details, see [ffrt\_storage\_size\_t](../type-def-h/document.md#ffrt_storage_size_t). |

**Returns**

| Type | Description |
| :-- | :-- |
| FFRT\_C\_API int | If the initialization is successful, **ffrt\_success** is returned. Otherwise, **ffrt\_error** is returned. |

#### \[h2\]ffrt\_fiber\_switch()

FFRT\_C\_API void ffrt\_fiber\_switch(ffrt\_fiber\_t\* from, ffrt\_fiber\_t\* to)

**Description**

Switches between fibers. The thread that calls this function suspends the current task, saves the context to the **from** fiber, and restores the context of the **to** fiber.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [ffrt\_fiber\_t](../../structs/ffrt-fiber-t/document.md)\* from | Pointer to the fiber to be saved. |
| [ffrt\_fiber\_t](../../structs/ffrt-fiber-t/document.md)\* to | Pointer to the fiber to be restored. |
