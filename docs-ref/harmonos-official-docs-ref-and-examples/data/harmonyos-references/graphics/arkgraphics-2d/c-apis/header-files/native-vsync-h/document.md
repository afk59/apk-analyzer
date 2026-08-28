# native\_vsync.h

#### Purpose

This file declares the functions for obtaining and using native virtual synchronization (VSync).

**File to include**: <native\_vsync/native\_vsync.h>

**Library**: libnative\_vsync.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 9

**Related module**: [NativeVsync](../../modules/nativevsync/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeVSync\_ExpectedRateRange](../../structs/oh-nativevsync-expectedraterange/document.md) | OH\_NativeVSync\_ExpectedRateRange | Provides the expected frame rate range. |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md) | OH\_NativeVSync | Provides the declaration of an **OH\_NativeVSync** struct. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_NativeVSync\_FrameCallback)(long long timestamp, void \*data)](#oh_nativevsync_framecallback) | OH\_NativeVSync\_FrameCallback | Defines the pointer to a VSync callback function. |
| [OH\_NativeVSync\* OH\_NativeVSync\_Create(const char\* name, unsigned int length)](#oh_nativevsync_create) | \- | 
Creates an **OH\_NativeVSync** instance. A new **OH\_NativeVSync** instance is created each time this function is called.

This API must be used in pair with [OH\_NativeVSync\_Destroy](#oh_nativevsync_destroy). Otherwise, memory leak occurs.

 |
| [OH\_NativeVSync\* OH\_NativeVSync\_Create\_ForAssociatedWindow(uint64\_t windowID, const char\* name, unsigned int length)](#oh_nativevsync_create_forassociatedwindow) | \- | 

Creates an **OH\_NativeVSync** instance to bind with a window. A new **OH\_NativeVSync** instance is created each time this API is called.

The actual VSync period of the **OH\_NativeVSync** instance created by calling this function may be different from the system's VSync period. The system adjusts the actual VSync period based on the window status.

 |
| [void OH\_NativeVSync\_Destroy(OH\_NativeVSync\* nativeVsync)](#oh_nativevsync_destroy) | \- | 

Destroys an **OH\_NativeVSync** instance.

Once the **OH\_NativeVSync** pointer is destroyed, it should not be used, as this can result in dangling pointer problems. Pay special attention to the management of the **OH\_NativeVSync** pointer in multithreaded scenarios.

 |
| [int OH\_NativeVSync\_RequestFrame(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_FrameCallback callback, void\* data)](#oh_nativevsync_requestframe) | \- | 

Requests the next VSync signal. When the signal arrives, a callback function is invoked.

If this function is called for multiple times in the same frame, only the last callback function is invoked.

If this function and the [OH\_NativeVSync\_RequestFrameWithMultiCallback](#oh_nativevsync_requestframewithmulticallback) function are called in the same frame, the current function call does not take effect.

 |
| [int OH\_NativeVSync\_RequestFrameWithMultiCallback(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_FrameCallback callback, void\* data)](#oh_nativevsync_requestframewithmulticallback) | \- | 

Requests the next VSync signal. When the signal arrives, a callback function is invoked.

If this function is called for multiple times in the same frame, every callback function is invoked.

 |
| [int OH\_NativeVSync\_GetPeriod(OH\_NativeVSync\* nativeVsync, long long\* period)](#oh_nativevsync_getperiod) | \- | 

Obtains the VSync period.

The VSync period is refreshed only when the **OH\_NativeVSync\_FrameCallback** callback is received following a request for a VSync signal via **OH\_NativeVSync\_RequestFrame**.

To obtain the VSync period for the first time using this function, you need to call **OH\_NativeVSync\_RequestFrame** to request a VSync signal. Once the **OH\_NativeVSync\_FrameCallback** callback is received, the vsync period can be obtained.

 |
| [int OH\_NativeVSync\_DVSyncSwitch(OH\_NativeVSync\* nativeVsync, bool enable)](#oh_nativevsync_dvsyncswitch) | \- | 

Enables DVSync to improve the smoothness of self-drawing animations.

DVSync, short for Decoupled VSync, is a frame timing management policy that is decoupled from the hardware's VSync.

DVSync drives the early rendering of upcoming animation frames by sending VSync signals with future timestamps. These frames are stored in a frame buffer queue. This helps DVSync reduce potential frame drops and therefore enhances the smoothness of animations.

DVSync requires free self-drawing frame buffers to store these pre-rendered animation frames. Therefore, you must ensure that at least one free frame buffer is available. Otherwise, do not enable DVSync.

After DVSync is enabled, you must correctly respond to the early VSync signals and request the subsequent VSync after the animation frame associated with the previous VSync is complete. In addition, the self-drawing frames must carry timestamps that align with VSync.

After the animation ends, disable DVSync.

On a platform that does not support DVSync or if another application has enabled DVSync, the attempt to enable it will not take effect, and the application still receives normal VSync signals.

 |
| [int OH\_NativeVSync\_SetExpectedFrameRateRange(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_ExpectedRateRange\* range)](#oh_nativevsync_setexpectedframeraterange) | \- | Sets the expected VSync frame rate and its range. |

#### Function Description

#### \[h2\]OH\_NativeVSync\_FrameCallback()

typedef void (\*OH\_NativeVSync\_FrameCallback)(long long timestamp, void \*data)

**Description**

Defines the pointer to a VSync callback function.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| long long timestamp | System timestamp obtained by VSync using **CLOCK\_MONOTONIC**, in nanoseconds. |
| void \*data | Pointer to user-defined data. |

#### \[h2\]OH\_NativeVSync\_Create()

OH\_NativeVSync\* OH\_NativeVSync\_Create(const char\* name, unsigned int length)

**Description**

Creates an **OH\_NativeVSync** instance. A new **OH\_NativeVSync** instance is created each time this function is called.

This API must be used in pair with [OH\_NativeVSync\_Destroy](#oh_nativevsync_destroy). Otherwise, memory leak occurs.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const char\* name | Pointer to the name that associates with the **OH\_NativeVSync** instance. |
| unsigned int length | Length of the name (number of characters). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md)\* | Returns the pointer to an **OH\_NativeVSync** instance. |

#### \[h2\]OH\_NativeVSync\_Create\_ForAssociatedWindow()

OH\_NativeVSync\* OH\_NativeVSync\_Create\_ForAssociatedWindow(uint64\_t windowID, const char\* name, unsigned int length)

**Description**

Creates an **OH\_NativeVSync** instance to bind with a window. A new **OH\_NativeVSync** instance is created each time this API is called.

The actual VSync period of the **OH\_NativeVSync** instance created by calling this function may be different from the system's VSync period. The system adjusts the actual VSync period based on the window status.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t windowID | Window ID, which is the index identifier of the window child process and can be obtained through [OH\_NativeWindow\_GetSurfaceId](../external-window-h/document.md#oh_nativewindow_getsurfaceid). |
| const char\* name | Pointer to the name that associates with the **OH\_NativeVSync** instance. |
| unsigned int length | Length of the name (number of characters). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md)\* | Returns the pointer to an **OH\_NativeVSync** instance. |

#### \[h2\]OH\_NativeVSync\_Destroy()

void OH\_NativeVSync\_Destroy(OH\_NativeVSync\* nativeVsync)

**Description**

Destroys an **OH\_NativeVSync** instance.

Once the **OH\_NativeVSync** pointer is destroyed, it should not be used, as this can result in dangling pointer problems. Pay special attention to the management of the **OH\_NativeVSync** pointer in multithreaded scenarios.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md)\* nativeVsync | Pointer to an **OH\_NativeVSync** instance. |

#### \[h2\]OH\_NativeVSync\_RequestFrame()

int OH\_NativeVSync\_RequestFrame(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_FrameCallback callback, void\* data)

**Description**

Requests the next VSync signal. When the signal arrives, a callback function is invoked.

If this function is called for multiple times in the same frame, only the last callback function is invoked.

If this function and the [OH\_NativeVSync\_RequestFrameWithMultiCallback](#oh_nativevsync_requestframewithmulticallback) function are called in the same frame, the current function call does not take effect.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md)\* nativeVsync | Pointer to an **OH\_NativeVSync** instance. |
| [OH\_NativeVSync\_FrameCallback](#oh_nativevsync_framecallback) callback | Function pointer of the **OH\_NativeVSync\_FrameCallback** type. This function pointer will be called when the next VSync signal arrives. |
| void\* data | Pointer to the user-defined data struct. The type is void. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeVSync\_RequestFrameWithMultiCallback()

int OH\_NativeVSync\_RequestFrameWithMultiCallback(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_FrameCallback callback, void\* data)

**Description**

Requests the next VSync signal. When the signal arrives, a callback function is invoked.

If this function is called for multiple times in the same frame, every callback function is invoked.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md)\* nativeVsync | Pointer to an **OH\_NativeVSync** instance. |
| [OH\_NativeVSync\_FrameCallback](#oh_nativevsync_framecallback) callback | Function pointer of the **OH\_NativeVSync\_FrameCallback** type. This function pointer will be called when the next VSync signal arrives. |
| void\* data | Pointer to the user-defined data struct. The type is void. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeVSync\_GetPeriod()

int OH\_NativeVSync\_GetPeriod(OH\_NativeVSync\* nativeVsync, long long\* period)

**Description**

Obtains the VSync period.

The VSync period is refreshed only when the **OH\_NativeVSync\_FrameCallback** callback is received following a request for a VSync signal via **OH\_NativeVSync\_RequestFrame**.

To obtain the VSync period for the first time using this function, you need to call **OH\_NativeVSync\_RequestFrame** to request a VSync signal. Once the **OH\_NativeVSync\_FrameCallback** callback is received, the vsync period can be obtained.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md)\* nativeVsync | Pointer to an **OH\_NativeVSync** instance. |
| long long\* period | Pointer to the VSync period. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeVSync\_DVSyncSwitch()

int OH\_NativeVSync\_DVSyncSwitch(OH\_NativeVSync\* nativeVsync, bool enable)

**Description**

Enables DVSync to improve the smoothness of self-drawing animations.

DVSync, short for Decoupled VSync, is a frame timing management policy that is decoupled from the hardware's VSync.

DVSync drives the early rendering of upcoming animation frames by sending VSync signals with future timestamps. These frames are stored in a frame buffer queue. This helps DVSync reduce potential frame drops and therefore enhances the smoothness of animations.

DVSync requires free self-drawing frame buffers to store these pre-rendered animation frames. Therefore, you must ensure that at least one free frame buffer is available. Otherwise, do not enable DVSync.

After DVSync is enabled, you must correctly respond to the early VSync signals and request the subsequent VSync after the animation frame associated with the previous VSync is complete. In addition, the self-drawing frames must carry timestamps that align with VSync.

After the animation ends, disable DVSync.

On a platform that does not support DVSync or if another application has enabled DVSync, the attempt to enable it will not take effect, and the application still receives normal VSync signals.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 14

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md)\* nativeVsync | Pointer to an **OH\_NativeVSync** instance. |
| bool enable | Whether to enable DVSync. The value **true** means to enable DVSync, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeVSync\_SetExpectedFrameRateRange()

int OH\_NativeVSync\_SetExpectedFrameRateRange(OH\_NativeVSync\* nativeVsync, OH\_NativeVSync\_ExpectedRateRange\* range)

**Description**

Sets the expected frame rate and its range. The actual frame rate may be different from the expected frame rate due to system power consumption, performance, and hardware specifications.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeVsync

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeVSync](../../structs/oh-nativevsync/document.md)\* nativeVsync | Pointer to an [OH\_NativeVSync](../../structs/oh-nativevsync/document.md) instance. |
| [OH\_NativeVSync\_ExpectedRateRange](../../structs/oh-nativevsync-expectedraterange/document.md)\* range | 
Pointer to an [OH\_NativeVSync\_ExpectedRateRange](../../structs/oh-nativevsync-expectedraterange/document.md) instance.

Valid expected frame rate range: 0 <= Minimum value <= Expected frame rate <= Maximum value <= 144.

The value **0** means that the expected frame rate is canceled.

You need to manage the lifecycle of this pointer.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **0** if successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |
