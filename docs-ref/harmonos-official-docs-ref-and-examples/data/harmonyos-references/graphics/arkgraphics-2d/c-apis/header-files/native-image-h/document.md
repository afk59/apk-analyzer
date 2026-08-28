# native\_image.h

#### Overview

This file declares the functions for obtaining and using **NativeImage**.

**File to include**: <native\_image/native\_image.h>

**Library**: libnative\_image.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Related module**: [OH\_NativeImage](../../modules/oh-nativeimage/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_OnFrameAvailableListener](../../structs/oh-onframeavailablelistener/document.md) | OH\_OnFrameAvailableListener | Defines an **OH\_NativeImage** listener, which is registered through [OH\_NativeImage\_SetOnFrameAvailableListener](#oh_nativeimage_setonframeavailablelistener). The listener triggers a callback when a frame is available. |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md) | OH\_NativeImage | Provides the declaration of an **OH\_NativeImage** struct. |
| [NativeWindow](../../structs/nativewindow/document.md) | OHNativeWindow | Provides the capability of accessing the **NativeWindow**. |
| [NativeWindowBuffer](../../structs/nativewindowbuffer/document.md) | OHNativeWindowBuffer | Provides the declaration of a **NativeWindowBuffer** struct. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_OnFrameAvailable)(void \*context)](#oh_onframeavailable) | OH\_OnFrameAvailable | Callback function triggered when a frame is available. |
| [OH\_NativeImage\* OH\_NativeImage\_Create(uint32\_t textureId, uint32\_t textureTarget)](#oh_nativeimage_create) | \- | 
Creates an **OH\_NativeImage** instance to be associated with the specified OpenGL ES texture ID and target.

This function must be used in pair with [OH\_NativeImage\_Destroy](#oh_nativeimage_destroy). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [OHNativeWindow\* OH\_NativeImage\_AcquireNativeWindow(OH\_NativeImage\* image)](#oh_nativeimage_acquirenativewindow) | \- | 

Obtains an **OHNativeWindow** instance associated with an **OH\_NativeImage** instance.

This function is not thread-safe.

When **OH\_NativeImage** is being destructed, the corresponding **OHNativeWindow** instance is released. If the **OHNativeWindow** pointer is obtained by using this function, set the pointer to null when releasing the **OH\_NativeImage** instance, so as to prevent subsequent wild pointers.

 |
| [int32\_t OH\_NativeImage\_AttachContext(OH\_NativeImage\* image, uint32\_t textureId)](#oh_nativeimage_attachcontext) | \- | 

Attaches an **OH\_NativeImage** instance to the current OpenGL ES context. The OpenGL ES texture will be bound to an **GL\_TEXTURE\_EXTERNAL\_OES** instance and updated through the **OH\_NativeImage** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_DetachContext(OH\_NativeImage\* image)](#oh_nativeimage_detachcontext) | \- | 

Detaches an **OH\_NativeImage** instance from the current OpenGL ES context.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_UpdateSurfaceImage(OH\_NativeImage\* image)](#oh_nativeimage_updatesurfaceimage) | \- | 

Updates the OpenGL ES texture associated with the latest frame through an **OH\_NativeImage** instance.

This function must be called in a thread of the OpenGL ES context.

This function must be called after the [OH\_OnFrameAvailableListener](../../structs/oh-onframeavailablelistener/document.md) callback is received.

This function is not thread-safe.

 |
| [int64\_t OH\_NativeImage\_GetTimestamp(OH\_NativeImage\* image)](#oh_nativeimage_gettimestamp) | \- | 

Obtains the timestamp of the texture image that recently called the **OH\_NativeImage\_UpdateSurfaceImage** function.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_GetTransformMatrix(OH\_NativeImage\* image, float matrix\[16\])](#oh_nativeimage_gettransformmatrix) | \- | Obtains the transformation matrix of the texture image that recently called the **OH\_NativeImage\_UpdateSurfaceImage** function. |
| [int32\_t OH\_NativeImage\_GetSurfaceId(OH\_NativeImage\* image, uint64\_t\* surfaceId)](#oh_nativeimage_getsurfaceid) | \- | 

Obtains the surface ID of an **OH\_NativeImage** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_SetOnFrameAvailableListener(OH\_NativeImage\* image, OH\_OnFrameAvailableListener listener)](#oh_nativeimage_setonframeavailablelistener) | \- | 

Registers a listener to listen for frame availability events.

Do not call other functions of this module in the callback.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_UnsetOnFrameAvailableListener(OH\_NativeImage\* image)](#oh_nativeimage_unsetonframeavailablelistener) | \- | 

Deregisters the listener used to listen for frame availability events.

This function is not thread-safe.

 |
| [void OH\_NativeImage\_Destroy(OH\_NativeImage\*\* image)](#oh_nativeimage_destroy) | \- | 

Destroys an **OH\_NativeImage** instance created by calling **OH\_NativeImage\_Create**. After the instance is destroyed, the pointer to the **OH\_NativeImage** instance is assigned **NULL**.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_GetTransformMatrixV2(OH\_NativeImage\* image, float matrix\[16\])](#oh_nativeimage_gettransformmatrixv2) | \- | 

Obtains, based on the rotation angle set by the producer, the transform matrix of the texture image that recently called the **OH\_NativeImage\_UpdateSurfaceImage** function.

The matrix is updated only after [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage) is called.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_GetBufferMatrix(OH\_NativeImage\* image, float matrix\[16\])](#oh_nativeimage_getbuffermatrix) | \- | 

Obtains the transformation matrix calculated based on the rotation angle set by the producer and the actual valid content area of the buffer.

This function returns a transformation matrix that is determined by the buffer's rotation angle and actual valid content area during the consumption of the buffer by [OH\_NativeImage](../../structs/oh-nativeimage/document.md), specifically when calling [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage) or [OH\_NativeImage\_AcquireNativeWindowBuffer](#oh_nativeimage_acquirenativewindowbuffer).

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_AcquireNativeWindowBuffer(OH\_NativeImage\* image,OHNativeWindowBuffer\*\* nativeWindowBuffer, int\* fenceFd)](#oh_nativeimage_acquirenativewindowbuffer) | \- | 

Obtain an **OHNativeWindowBuffer** instance through the **OH\_NativeImage** instance on the consumer side.

This function cannot be used in together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function creates an **OHNativeWindowBuffer**.

When using the **OHNativeWindowBuffer**, call [OH\_NativeWindow\_NativeObjectReference](../external-window-h/document.md#oh_nativewindow_nativeobjectreference) to increase its reference count by one.

When finishing using the **OHNativeWindowBuffer**, call [OH\_NativeWindow\_NativeObjectUnreference](../external-window-h/document.md#oh_nativewindow_nativeobjectunreference) to decrease the reference count by one.

This function must be used in pair with [OH\_NativeImage\_ReleaseNativeWindowBuffer](#oh_nativeimage_releasenativewindowbuffer). Otherwise, memory leak occurs.

When **fenceFd** is used up, you must close it.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_ReleaseNativeWindowBuffer(OH\_NativeImage\* image,OHNativeWindowBuffer\* nativeWindowBuffer, int fenceFd)](#oh_nativeimage_releasenativewindowbuffer) | \- | 

Release the **OHNativeWindowBuffer** instance through the **OH\_NativeImage** instance.

The system will close **fenceFd**. You do not need to close it.

This function is not thread-safe.

 |
| [OH\_NativeImage\* OH\_ConsumerSurface\_Create(void)](#oh_consumersurface_create) | \- | 

Creates an **OH\_NativeImage** instance as the consumer of the surface.

This function is used only for memory cycling of the surface consumer. Memory rendering is not proactively performed in the created **OH\_NativeImage** instance.

This function cannot be used in together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function must be used in together with [OH\_NativeImage\_AcquireNativeWindowBuffer](#oh_nativeimage_acquirenativewindowbuffer) and [OH\_NativeImage\_ReleaseNativeWindowBuffer](#oh_nativeimage_releasenativewindowbuffer).

This function must be used in pair with [OH\_NativeImage\_Destroy](#oh_nativeimage_destroy). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [int32\_t OH\_ConsumerSurface\_SetDefaultUsage(OH\_NativeImage\* image, uint64\_t usage)](#oh_consumersurface_setdefaultusage) | \- | 

Sets the default read/write mode.

This function is not thread-safe.

 |
| [int32\_t OH\_ConsumerSurface\_SetDefaultSize(OH\_NativeImage\* image, int32\_t width, int32\_t height)](#oh_consumersurface_setdefaultsize) | \- | 

Sets the default size of a geometric shape.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_SetDropBufferMode(OH\_NativeImage\* image, bool isOpen)](#oh_nativeimage_setdropbuffermode) | \- | 

Sets the frame-dropping mode for rendering of an **OH\_NativeImage** instance.

In frame-dropping mode, most buffers produced by the producer are discarded, and only the latest buffer is rendered promptly.

This mode does not guarantee high frame rates.

It is recommended that you can call this function immediately after [OH\_NativeImage\_Create](#oh_nativeimage_create).

This function takes effect only when it is used together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function is not thread-safe.

 |
| [OH\_NativeImage\* OH\_NativeImage\_CreateWithSingleBufferMode(uint32\_t textureId, uint32\_t textureTarget, bool singleBufferMode)](#oh_nativeimage_createwithsinglebuffermode) | \- | 

Creates an **OH\_NativeImage** instance with the texture ID. The instance is associated with the texture ID and texture target of OpenGL ES, and determines whether to set the single-buffer mode.

This function must be used in pair with [OH\_NativeImage\_Destroy](#oh_nativeimage_destroy). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [OH\_NativeImage\* OH\_ConsumerSurface\_CreateWithSingleBufferMode(bool singleBufferMode)](#oh_consumersurface_createwithsinglebuffermode) | \- | 

Creates an [OH\_NativeImage](../../structs/oh-nativeimage/document.md) instance as the consumer of the surface and determines whether to set the single-buffer mode.

This function is used only for memory rotation of the surface consumer. The created [OH\_NativeImage](../../structs/oh-nativeimage/document.md) does not perform memory rendering.

This function cannot be used in together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function must be used in pair with [OH\_NativeImage\_Destroy](#oh_nativeimage_destroy). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_ReleaseTextImage(OH\_NativeImage\* image)](#oh_nativeimage_releasetextimage) | \- | 

Unbinds **SurfaceBuffer** from the texture and restores the texture to the unused state.

In single-buffer mode, this function is called to release the texture. Otherwise, the producer cannot request a buffer next time.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_GetColorSpace(OH\_NativeImage\* image, OH\_NativeBuffer\_ColorSpace\* colorSpace)](#oh_nativeimage_getcolorspace) | \- | 

Obtains the color space of the texture image that is most recently passed to [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function is not thread-safe.

 |
| [int32\_t OH\_NativeImage\_AcquireLatestNativeWindowBuffer(OH\_NativeImage\* image, OHNativeWindowBuffer\*\* nativeWindowBuffer, int\* fenceFd)](#oh_nativeimage_acquirelatestnativewindowbuffer) | \- | 

Obtains the **OHNativeWindowBuffer** recently produced by the producer through the **OH\_NativeImage** of the consumer, and discards other buffers.

The consumer can receive the callback of all available buffers (including discarded buffers) through the callback registered by [OH\_OnFrameAvailableListener](../../structs/oh-onframeavailablelistener/document.md).

This function cannot be used in together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function is not thread-safe.

 |

#### Function Description

#### \[h2\]OH\_OnFrameAvailable()

typedef void (\*OH\_OnFrameAvailable)(void \*context)

**Description**

Callback function triggered when a frame is available.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*context | User-defined context information, which is returned when the callback is triggered. |

#### \[h2\]OH\_NativeImage\_Create()

OH\_NativeImage\* OH\_NativeImage\_Create(uint32\_t textureId, uint32\_t textureTarget)

**Description**

Creates an **OH\_NativeImage** instance to be associated with the specified OpenGL ES texture ID and target.

This function must be used in pair with [OH\_NativeImage\_Destroy](#oh_nativeimage_destroy). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t textureId | OpenGL ES texture ID. |
| uint32\_t textureTarget | OpenGL ES texture target. The value can be **GL\_TEXTURE\_2D** or **GL\_TEXTURE\_EXTERNAL\_OES**. For details, see [How do I choose between the texture types GL\_TEXTURE\_2D and GL\_TEXTURE\_EXTERNAL\_OES?](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-12). |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_NativeImage\* | Returns a pointer to the **OH\_NativeImage** instance if the creation is successful; returns **NULL** otherwise. |

#### \[h2\]OH\_NativeImage\_AcquireNativeWindow()

OHNativeWindow\* OH\_NativeImage\_AcquireNativeWindow(OH\_NativeImage\* image)

**Description**

Obtains an **OHNativeWindow** instance associated with an **OH\_NativeImage** instance.

This function is not thread-safe.

When **OH\_NativeImage** is being destructed, the corresponding **OHNativeWindow** instance is released. If the **OHNativeWindow** pointer is obtained by using this function, set the pointer to null when releasing the **OH\_NativeImage** instance, so as to prevent subsequent wild pointers.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md)\* | Returns a pointer to the **OHNativeWindow** instance if the operation is successful; returns **NULL** otherwise. |

#### \[h2\]OH\_NativeImage\_AttachContext()

int32\_t OH\_NativeImage\_AttachContext(OH\_NativeImage\* image, uint32\_t textureId)

**Description**

Attaches an **OH\_NativeImage** instance to the current OpenGL ES context. The OpenGL ES texture will be bound to an **GL\_TEXTURE\_EXTERNAL\_OES** instance and updated through the **OH\_NativeImage** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| uint32\_t textureId | ID of the OpenGL ES texture to which the **OH\_NativeImage** instance is to be attached. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeImage\_DetachContext()

int32\_t OH\_NativeImage\_DetachContext(OH\_NativeImage\* image)

**Description**

Detaches an **OH\_NativeImage** instance from the current OpenGL ES context.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeImage\_UpdateSurfaceImage()

int32\_t OH\_NativeImage\_UpdateSurfaceImage(OH\_NativeImage\* image)

**Description**

Updates the OpenGL ES texture associated with the latest frame through an **OH\_NativeImage** instance.

This function must be called in a thread of the OpenGL ES context.

This function must be called after the [OH\_OnFrameAvailableListener](../../structs/oh-onframeavailablelistener/document.md) callback is received.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeImage\_GetTimestamp()

int64\_t OH\_NativeImage\_GetTimestamp(OH\_NativeImage\* image)

**Description**

Obtains the timestamp of the texture image that recently called the **OH\_NativeImage\_UpdateSurfaceImage** function.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int64\_t | Returns the timestamp of the texture image. |

#### \[h2\]OH\_NativeImage\_GetTransformMatrix()

int32\_t OH\_NativeImage\_GetTransformMatrix(OH\_NativeImage\* image, float matrix\[16\])

**Description**

Obtains the transformation matrix of the texture image that recently called the **OH\_NativeImage\_UpdateSurfaceImage** function.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Deprecated from**: 12

**Substitute**: [OH\_NativeImage\_GetTransformMatrixV2](#oh_nativeimage_gettransformmatrixv2)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| matrix | Buffer used to store the 4 × 4 transformation matrix obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeImage\_GetSurfaceId()

int32\_t OH\_NativeImage\_GetSurfaceId(OH\_NativeImage\* image, uint64\_t\* surfaceId)

**Description**

Obtains the surface ID of an **OH\_NativeImage** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| uint64\_t\* surfaceId | Pointer to the surface ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeImage\_SetOnFrameAvailableListener()

int32\_t OH\_NativeImage\_SetOnFrameAvailableListener(OH\_NativeImage\* image, OH\_OnFrameAvailableListener listener)

**Description**

Registers a listener to listen for frame availability events.

Do not call other functions of this module in the callback.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| [OH\_OnFrameAvailableListener](../../structs/oh-onframeavailablelistener/document.md) listener | Listener to register. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeImage\_UnsetOnFrameAvailableListener()

int32\_t OH\_NativeImage\_UnsetOnFrameAvailableListener(OH\_NativeImage\* image)

**Description**

Deregisters the listener used to listen for frame availability events.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeImage\_Destroy()

void OH\_NativeImage\_Destroy(OH\_NativeImage\*\* image)

**Description**

Destroys an **OH\_NativeImage** instance created by calling **OH\_NativeImage\_Create**. After the instance is destroyed, the pointer to the **OH\_NativeImage** instance is assigned **NULL**.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\*\* image | Pointer to an **OH\_NativeImage** instance. |

#### \[h2\]OH\_NativeImage\_GetTransformMatrixV2()

int32\_t OH\_NativeImage\_GetTransformMatrixV2(OH\_NativeImage\* image, float matrix\[16\])

**Description**

Obtains, based on the rotation angle set by the producer, the transform matrix of the texture image that recently called the **OH\_NativeImage\_UpdateSurfaceImage** function.

The matrix is updated only after [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage) is called.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| matrix | Buffer used to store the 4 × 4 transformation matrix obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** (error code: 40001000) if **image** is a null pointer.

Returns **NATIVE\_ERROR\_UNKNOWN** (error code: 50002000), indicating an unknown error. In this case, check the logs.

 |

#### \[h2\]OH\_NativeImage\_GetBufferMatrix()

int32\_t OH\_NativeImage\_GetBufferMatrix(OH\_NativeImage\* image, float matrix\[16\])

**Description**

Obtains the transformation matrix calculated based on the rotation angle set by the producer and the actual valid content area of the buffer.

This function returns a transformation matrix that is determined by the buffer's rotation angle and actual valid content area during the consumption of the buffer by [OH\_NativeImage](../../structs/oh-nativeimage/document.md), specifically when calling [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage) or [OH\_NativeImage\_AcquireNativeWindowBuffer](#oh_nativeimage_acquirenativewindowbuffer).

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 15

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an [OH\_NativeImage](../../structs/oh-nativeimage/document.md) instance. |
| matrix | Buffer used to store the 4 × 4 transformation matrix obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** (error code: 40001000) if **image** is a null pointer.

Returns **NATIVE\_ERROR\_MEM\_OPERATION\_ERROR** (error code: 30001000) if the transformation matrix fails to be obtained due to a memory manipulation error.

 |

#### \[h2\]OH\_NativeImage\_AcquireNativeWindowBuffer()

int32\_t OH\_NativeImage\_AcquireNativeWindowBuffer(OH\_NativeImage\* image,OHNativeWindowBuffer\*\* nativeWindowBuffer, int\* fenceFd)

**Description**

Obtain an **OHNativeWindowBuffer** instance through the **OH\_NativeImage** instance on the consumer side. This function cannot be used in together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function creates an **OHNativeWindowBuffer**. When using the **OHNativeWindowBuffer**, call [OH\_NativeWindow\_NativeObjectReference](../external-window-h/document.md#oh_nativewindow_nativeobjectreference) to increase its reference count by one. When finishing using the **OHNativeWindowBuffer**, call [OH\_NativeWindow\_NativeObjectUnreference](../external-window-h/document.md#oh_nativewindow_nativeobjectunreference) to decrease the reference count by one.

This function must be used in pair with [OH\_NativeImage\_ReleaseNativeWindowBuffer](#oh_nativeimage_releasenativewindowbuffer). Otherwise, memory leak occurs.

When **fenceFd** is used up, you must close it.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md)\*\* nativeWindowBuffer | Double pointer to the **OHNativeWindowBuffer** instance obtained. |
| int\* fenceFd | Pointer to the file descriptor handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** if **image**, **nativeWindowBuffer**, or **fenceFd** is a null pointer.

Returns **NATIVE\_ERROR\_NO\_BUFFER** if no buffer is available for consumption.

 |

#### \[h2\]OH\_NativeImage\_ReleaseNativeWindowBuffer()

int32\_t OH\_NativeImage\_ReleaseNativeWindowBuffer(OH\_NativeImage\* image,OHNativeWindowBuffer\* nativeWindowBuffer, int fenceFd)

**Description**

Release the **OHNativeWindowBuffer** instance through the **OH\_NativeImage** instance.

The system will close **fenceFd**. You do not need to close it.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md)\* nativeWindowBuffer | Pointer to an **OHNativeWindowBuffer** instance. |
| int fenceFd | File descriptor handle, which is used for concurrent synchronization control. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** if **image** or **nativeWindowBuffer** is a null pointer.

Returns **NATIVE\_ERROR\_BUFFER\_STATE\_INVALID** if the status of **nativeWindowBuffer** is invalid.

Returns **NATIVE\_ERROR\_BUFFER\_NOT\_IN\_CACHE** if **nativeWindowBuffer** is not in the cache.

 |

#### \[h2\]OH\_ConsumerSurface\_Create()

OH\_NativeImage\* OH\_ConsumerSurface\_Create(void)

**Description**

Creates an **OH\_NativeImage** instance as the consumer of the surface.

This function is used only for memory cycling of the surface consumer. Memory rendering is not proactively performed in the created **OH\_NativeImage** instance.

This function cannot be used in together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function must be used in together with [OH\_NativeImage\_AcquireNativeWindowBuffer](#oh_nativeimage_acquirenativewindowbuffer) and [OH\_NativeImage\_ReleaseNativeWindowBuffer](#oh_nativeimage_releasenativewindowbuffer).

This function must be used in pair with [OH\_NativeImage\_Destroy](#oh_nativeimage_destroy). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* | Returns a pointer to the **OH\_NativeImage** instance if the operation is successful; returns **NULL** otherwise. |

#### \[h2\]OH\_ConsumerSurface\_SetDefaultUsage()

int32\_t OH\_ConsumerSurface\_SetDefaultUsage(OH\_NativeImage\* image, uint64\_t usage)

**Description**

Sets the default read/write mode.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| uint64\_t usage | Read/write mode. For details about the enumerated values, see [OH\_NativeBuffer\_Usage](../native-buffer-h/document.md#oh_nativebuffer_usage). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** if **image** is a null pointer.

 |

#### \[h2\]OH\_ConsumerSurface\_SetDefaultSize()

int32\_t OH\_ConsumerSurface\_SetDefaultSize(OH\_NativeImage\* image, int32\_t width, int32\_t height)

**Description**

Sets the default size of a geometric shape.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| int32\_t width | Width of the geometric shape. The value is greater than 0, in pixels. |
| int32\_t height | Height of the geometric shape. The value is greater than 0, in pixels. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** if **image** is a null pointer or **width** or **height** is less than 0.

 |

#### \[h2\]OH\_NativeImage\_SetDropBufferMode()

int32\_t OH\_NativeImage\_SetDropBufferMode(OH\_NativeImage\* image, bool isOpen)

**Description**

Sets the frame-dropping mode for rendering of an **OH\_NativeImage** instance.

In frame-dropping mode, most buffers produced by the producer are discarded, and only the latest buffer is rendered promptly.

This mode does not guarantee high frame rates.

It is recommended that you can call this function immediately after [OH\_NativeImage\_Create](#oh_nativeimage_create).

This function takes effect only when it is used together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function is not thread-safe.

The number of listener callbacks set by [OH\_NativeImage\_SetOnFrameAvailableListener](#oh_nativeimage_setonframeavailablelistener) does not decrease because the frame loss mode is set.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 17

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| bool isOpen | Whether to set the frame-dropping mode. The value **true** means to set the frame-dropping mode, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** if **image** is a null pointer.

 |

#### \[h2\]OH\_NativeImage\_CreateWithSingleBufferMode()

OH\_NativeImage\* OH\_NativeImage\_CreateWithSingleBufferMode(uint32\_t textureId, uint32\_t textureTarget, bool singleBufferMode)

**Description**

Creates an **OH\_NativeImage** instance with the texture ID. The instance is associated with the texture ID and texture target of OpenGL ES, and determines whether to set the single-buffer mode.

This function must be used in pair with [OH\_NativeImage\_Destroy](#oh_nativeimage_destroy). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t textureId | OpenGL ES texture ID. |
| uint32\_t textureTarget | OpenGL ES texture target. For details, see [How do I choose between the texture types GL\_TEXTURE\_2D and GL\_TEXTURE\_EXTERNAL\_OES?](https://developer.huawei.com/consumer/cn/doc/harmonyos-faqs/faqs-arkgraphics-2d-12). |
| bool singleBufferMode | Whether to set the single-buffer mode. **true**: yes; **false**: no. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeImage\*](../../structs/oh-nativeimage/document.md) | Returns a pointer to the **OH\_NativeImage** instance if the creation is successful; returns **NULL** otherwise. |

#### \[h2\]OH\_ConsumerSurface\_CreateWithSingleBufferMode()

OH\_NativeImage\* OH\_ConsumerSurface\_CreateWithSingleBufferMode(bool singleBufferMode)

**Description**

Creates an [OH\_NativeImage](../../structs/oh-nativeimage/document.md) instance as the consumer of the surface and determines whether to set the single-buffer mode.

This function is used only for memory rotation of the surface consumer. The created [OH\_NativeImage](../../structs/oh-nativeimage/document.md) does not perform memory rendering.

This function cannot be used in together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function must be used in pair with [OH\_NativeImage\_Destroy](#oh_nativeimage_destroy). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| bool singleBufferMode | Whether to set the single-buffer mode. **true**: yes; **false**: no. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeImage\*](../../structs/oh-nativeimage/document.md) | Returns the pointer to the [OH\_NativeImage](../../structs/oh-nativeimage/document.md) instance if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_NativeImage\_ReleaseTextImage()

int32\_t OH\_NativeImage\_ReleaseTextImage(OH\_NativeImage\* image)

**Description**

Unbinds **SurfaceBuffer** from the texture and restores the texture to the unused state.

In single-buffer mode, this function is called to release the texture. Otherwise, the producer cannot request a buffer next time.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an [OH\_NativeImage](../../structs/oh-nativeimage/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** if **image** is a null pointer.

 |

#### \[h2\]OH\_NativeImage\_GetColorSpace()

int32\_t OH\_NativeImage\_GetColorSpace(OH\_NativeImage\* image, OH\_NativeBuffer\_ColorSpace\* colorSpace)

**Description**

Obtains the color space of the texture image that is most recently passed to [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an [OH\_NativeImage](../../structs/oh-nativeimage/document.md) instance. |
| OH\_NativeBuffer\_ColorSpace\* colorSpace | Pointer to the color space set in [OH\_NativeImage](../../structs/oh-nativeimage/document.md). For details about the available options, see [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** if **image** or **colorSpace** is a null pointer.

 |

#### \[h2\]OH\_NativeImage\_AcquireLatestNativeWindowBuffer()

int32\_t OH\_NativeImage\_AcquireLatestNativeWindowBuffer(OH\_NativeImage\* image, OHNativeWindowBuffer\*\* nativeWindowBuffer, int\* fenceFd)

**Description**

Obtains the **OHNativeWindowBuffer** recently produced by the producer through the **OH\_NativeImage** of the consumer, and discards other buffers.

The consumer can receive the callback of all available buffers (including discarded buffers) through the callback registered by [OH\_OnFrameAvailableListener](../../structs/oh-onframeavailablelistener/document.md).

This function cannot be used in together with [OH\_NativeImage\_UpdateSurfaceImage](#oh_nativeimage_updatesurfaceimage).

This function creates an **OHNativeWindowBuffer**. When using the **OHNativeWindowBuffer**, call [OH\_NativeWindow\_NativeObjectReference](../external-window-h/document.md#oh_nativewindow_nativeobjectreference) to increase its reference count by one.

When finishing using the **OHNativeWindowBuffer**, call [OH\_NativeWindow\_NativeObjectUnreference](../external-window-h/document.md#oh_nativewindow_nativeobjectunreference) to decrease the reference count by one.

This function must be used in pair with [OH\_NativeImage\_ReleaseNativeWindowBuffer](#oh_nativeimage_releasenativewindowbuffer). Otherwise, memory leak occurs.

When **fenceFd** is used up, you must close it.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeImage

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeImage](../../structs/oh-nativeimage/document.md)\* image | Pointer to an **OH\_NativeImage** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md)\*\* nativeWindowBuffer | Pointer to the second-level **OHNativeWindowBuffer**. |
| int\* fenceFd | Pointer to the file descriptor handle. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Returns **NATIVE\_ERROR\_OK** if the operation is successful.

Returns **NATIVE\_ERROR\_INVALID\_ARGUMENTS** if **image**, **nativeWindowBuffer**, or **fenceFd** is a null pointer.

Returns **NATIVE\_ERROR\_NO\_BUFFER** if no buffer is available for consumption.

 |
