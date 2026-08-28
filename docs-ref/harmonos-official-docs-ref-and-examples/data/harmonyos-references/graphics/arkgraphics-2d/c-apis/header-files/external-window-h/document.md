# external\_window.h

#### Overview

This file declares the functions for obtaining and using **NativeWindow**.

**File to include**: <native\_window/external\_window.h>

**Library**: libnative\_window.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Related module**: [NativeWindow](../../modules/nativewindow/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Region](../../structs/region/document.md) | Region | Describes the rectangle (dirty region) where the content is to be updated in the local **OHNativeWindow**. |
| [Rect](../../structs/rect/document.md) | \- | If **rects** is a null pointer, the buffer size is the same as the size of the dirty region by default. |
| [OHHDRMetaData](../../structs/ohhdrmetadata/document.md) | OHHDRMetaData | Describes the HDR metadata. |
| [OHExtDataHandle](../../structs/ohextdatahandle/document.md) | OHExtDataHandle | Describes the extended data handle. |
| [OHIPCParcel](../../structs/ohipcparcel/document.md) | OHIPCParcel | Provides access to **OHIPCParcel**, which is an IPC parcelable object. |
| [NativeWindow](../../structs/nativewindow/document.md) | OHNativeWindow | Provides access to **OHNativeWindow**. |
| [NativeWindowBuffer](../../structs/nativewindowbuffer/document.md) | OHNativeWindowBuffer | Provides access to **OHNativeWindowBuffer**. |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) | OH\_NativeBuffer | Provides access to **OH\_NativeBuffer**. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NativeWindowOperation](#nativewindowoperation) | NativeWindowOperation | Defines an enum for the operation codes in the **OH\_NativeWindow\_NativeWindowHandleOpt** function. |
| [OHScalingMode](#ohscalingmode) | OHScalingMode | Enumerates the scaling modes. |
| [OHScalingModeV2](#ohscalingmodev2) | OHScalingModeV2 | Defines an enum for the rendering scaling modes. |
| [OHHDRMetadataKey](#ohhdrmetadatakey) | OHHDRMetadataKey | Enumerates the HDR metadata keys. |
| [OHSurfaceSource](#ohsurfacesource) | OHSurfaceSource | Defines an enum for the sources of content displayed in the local window. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OHNativeWindow\* OH\_NativeWindow\_CreateNativeWindow(void\* pSurface)](#oh_nativewindow_createnativewindow) | 
Creates an **OHNativeWindow** instance. A new **OHNativeWindow** instance is created each time this function is called.

Note: If this API is unavailable, you can use **OH\_NativeImage\_AcquireNativeWindow** or XComponent as a substitute.

 |
| [void OH\_NativeWindow\_DestroyNativeWindow(OHNativeWindow\* window)](#oh_nativewindow_destroynativewindow) | 

Decreases the reference count of an **OHNativeWindow** instance by 1 and when the reference count reaches 0, destroys the instance.

This function is not thread-safe.

 |
| [OHNativeWindowBuffer\* OH\_NativeWindow\_CreateNativeWindowBufferFromSurfaceBuffer(void\* pSurfaceBuffer)](#oh_nativewindow_createnativewindowbufferfromsurfacebuffer) | 

Creates an **OHNativeWindowBuffer** instance. A new **OHNativeWindowBuffer** instance is created each time this function is called.

Note: If this function is unavailable, you can use **OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer** as a substitute.

 |
| [OHNativeWindowBuffer\* OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer(OH\_NativeBuffer\* nativeBuffer)](#oh_nativewindow_createnativewindowbufferfromnativebuffer) | 

Creates an **OHNativeWindowBuffer** instance. A new **OHNativeWindowBuffer** instance is created each time this function is called.

This function must be used in pair with [OH\_NativeWindow\_DestroyNativeWindowBuffer](#oh_nativewindow_destroynativewindowbuffer). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [void OH\_NativeWindow\_DestroyNativeWindowBuffer(OHNativeWindowBuffer\* buffer)](#oh_nativewindow_destroynativewindowbuffer) | 

Decreases the reference count of an **OHNativeWindowBuffer** instance by 1 and when the reference count reaches 0, destroys the instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_NativeWindowRequestBuffer(OHNativeWindow \*window,OHNativeWindowBuffer \*\*buffer, int \*fenceFd)](#oh_nativewindow_nativewindowrequestbuffer) | 

Requests an **OHNativeWindowBuffer** through an **OHNativeWindow** instance for content production.

Before calling this function, you must call [SET\_BUFFER\_GEOMETRY](#nativewindowoperation) to set the width and height of **OHNativeWindow**.

This function must be used in pair with [OH\_NativeWindow\_NativeWindowFlushBuffer](#oh_nativewindow_nativewindowflushbuffer). Otherwise, memory leak occurs.

When **fenceFd** is used up, you must close it.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_NativeWindowFlushBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer,int fenceFd, Region region)](#oh_nativewindow_nativewindowflushbuffer) | 

Flushes the **OHNativeWindowBuffer** filled with the produced content to the buffer queue through an **OHNativeWindow** instance for content consumption.

The system will close **fenceFd**. You do not need to close it.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_GetLastFlushedBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer,int \*fenceFd, float matrix\[16\])](#oh_nativewindow_getlastflushedbuffer) | Obtains the **OHNativeWindowBuffer** that was flushed to the buffer queue last time through an **OHNativeWindow** instance. |
| [int32\_t OH\_NativeWindow\_NativeWindowAbortBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)](#oh_nativewindow_nativewindowabortbuffer) | 

Returns the **OHNativeWindowBuffer** to the buffer queue through an **OHNativeWindow** instance, without filling in any content. The **OHNativeWindowBuffer** can be used for a new request.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_NativeWindowHandleOpt(OHNativeWindow \*window, int code, ...)](#oh_nativewindow_nativewindowhandleopt) | 

Sets or obtains the attributes of an **OHNativeWindow** instance, including the width, height, and content format.

This function is not thread-safe.

 |
| [BufferHandle \*OH\_NativeWindow\_GetBufferHandleFromNative(OHNativeWindowBuffer \*buffer)](#oh_nativewindow_getbufferhandlefromnative) | 

Obtains the pointer to a **BufferHandle** of an **OHNativeWindowBuffer** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_NativeObjectReference(void \*obj)](#oh_nativewindow_nativeobjectreference) | 

Adds the reference count of a native object.

This function must be used in pair with [OH\_NativeWindow\_NativeObjectUnreference](#oh_nativewindow_nativeobjectunreference). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_NativeObjectUnreference(void \*obj)](#oh_nativewindow_nativeobjectunreference) | 

Decreases the reference count of a native object by 1 and when the reference count reaches 0, destroys this object.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_GetNativeObjectMagic(void \*obj)](#oh_nativewindow_getnativeobjectmagic) | 

Obtains the magic ID of a native object.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_NativeWindowSetScalingMode(OHNativeWindow \*window, uint32\_t sequence,OHScalingMode scalingMode)](#oh_nativewindow_nativewindowsetscalingmode) | Sets a scaling mode for an **OHNativeWindow**. |
| [int32\_t OH\_NativeWindow\_NativeWindowSetMetaData(OHNativeWindow \*window, uint32\_t sequence, int32\_t size,const OHHDRMetaData \*metaData)](#oh_nativewindow_nativewindowsetmetadata) | Sets metadata for an **OHNativeWindow**. |
| [int32\_t OH\_NativeWindow\_NativeWindowSetMetaDataSet(OHNativeWindow \*window, uint32\_t sequence, OHHDRMetadataKey key,int32\_t size, const uint8\_t \*metaData)](#oh_nativewindow_nativewindowsetmetadataset) | Sets a metadata set for an **OHNativeWindow**. |
| [int32\_t OH\_NativeWindow\_NativeWindowSetTunnelHandle(OHNativeWindow \*window, const OHExtDataHandle \*handle)](#oh_nativewindow_nativewindowsettunnelhandle) | Sets a tunnel handle to an **OHNativeWindow**. |
| [int32\_t OH\_NativeWindow\_NativeWindowAttachBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)](#oh_nativewindow_nativewindowattachbuffer) | 

Attaches an **OHNativeWindowBuffer** to an **OHNativeWindow** instance.

This function must be used in pair with [OH\_NativeWindow\_NativeWindowDetachBuffer](#oh_nativewindow_nativewindowdetachbuffer). Otherwise, memory management disorder may occur.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_NativeWindowDetachBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)](#oh_nativewindow_nativewindowdetachbuffer) | 

Detaches an **OHNativeWindowBuffer** from an **OHNativeWindow** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_GetSurfaceId(OHNativeWindow \*window, uint64\_t \*surfaceId)](#oh_nativewindow_getsurfaceid) | 

Obtains a surface ID through an **OHNativeWindow**.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_CreateNativeWindowFromSurfaceId(uint64\_t surfaceId, OHNativeWindow \*\*window)](#oh_nativewindow_createnativewindowfromsurfaceid) | 

Creates an **OHNativeWindow** instance based on a surface ID.

This function must be used in pair with [OH\_NativeWindow\_DestroyNativeWindow](#oh_nativewindow_destroynativewindow). Otherwise, memory leak occurs.

If **OHNativeWindow** instances are released concurrently, call [OH\_NativeWindow\_NativeObjectReference](#oh_nativewindow_nativeobjectreference) and [OH\_NativeWindow\_NativeObjectUnreference](#oh_nativewindow_nativeobjectunreference) to increase and decrease the reference count of **OHNativeWindow**.

The surface obtained by using the surface ID must be created in the current process, but not in a different process.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_NativeWindowSetScalingModeV2(OHNativeWindow\* window, OHScalingModeV2 scalingMode)](#oh_nativewindow_nativewindowsetscalingmodev2) | 

Sets a rendering scaling mode for an **OHNativeWindow** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_GetLastFlushedBufferV2(OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer,int \*fenceFd, float matrix\[16\])](#oh_nativewindow_getlastflushedbufferv2) | 

Obtains the **OHNativeWindowBuffer** that was flushed to the buffer queue last time through an **OHNativeWindow** instance. The difference between this function and **OH\_NativeWindow\_GetLastFlushedBuffer** lies in the matrix.

This function must be used in pair with [OH\_NativeWindow\_NativeObjectUnreference](#oh_nativewindow_nativeobjectunreference). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [void OH\_NativeWindow\_SetBufferHold(OHNativeWindow \*window)](#oh_nativewindow_setbufferhold) | Enables the single-frame buffering mechanism, which caches a frame buffer in advance and delays the display of the frame to smooth the frame rate fluctuation. |
| [int32\_t OH\_NativeWindow\_WriteToParcel(OHNativeWindow \*window, OHIPCParcel \*parcel)](#oh_nativewindow_writetoparcel) | 

Writes an **OHNativeWindow** instance to an **OHIPCParcel** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_ReadFromParcel(OHIPCParcel \*parcel, OHNativeWindow \*\*window)](#oh_nativewindow_readfromparcel) | 

Reads an **OHNativeWindow** instance from an **OHIPCParcel** instance.

This function creates an **OHNativeWindow** instance. After it is used, you need to use this function in pair with [OH\_NativeWindow\_DestroyNativeWindow](#oh_nativewindow_destroynativewindow). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_SetColorSpace(OHNativeWindow \*window, OH\_NativeBuffer\_ColorSpace colorSpace)](#oh_nativewindow_setcolorspace) | 

Sets the color space for an **OHNativeWindow** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_GetColorSpace(OHNativeWindow \*window, OH\_NativeBuffer\_ColorSpace \*colorSpace)](#oh_nativewindow_getcolorspace) | 

Obtains the color space of an **OHNativeWindow** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_SetMetadataValue(OHNativeWindow \*window, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t size, uint8\_t \*metadata)](#oh_nativewindow_setmetadatavalue) | 

Sets a metadata value for an **OHNativeWindow** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_GetMetadataValue(OHNativeWindow \*window, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t \*size, uint8\_t \*\*metadata)](#oh_nativewindow_getmetadatavalue) | 

Obtains the metadata value of an **OHNativeWindow** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_CleanCache(OHNativeWindow \*window)](#oh_nativewindow_cleancache) | 

Clears the **OHNativeWindowBuffer** cache in **OHNativeWindow**.

Ensure that **OHNativeWindowBuffer** has been successfully allocated by calling [OH\_NativeWindow\_NativeWindowRequestBuffer](#oh_nativewindow_nativewindowrequestbuffer).

This function is not thread-safe.

 |
| [int32\_t OH\_NativeWindow\_PreAllocBuffers(OHNativeWindow \*window, uint32\_t allocBufferCnt)](#oh_nativewindow_preallocbuffers) | 

Request multiple **OHNativeWindowBuffer** blocks in advance through the **OHNativeWindow** object for content production.

Before calling this function, you need to set the width and height of **OHNativeWindow** through [OH\_NativeWindow\_NativeWindowHandleOpt](#oh_nativewindow_nativewindowhandleopt).

This function is not thread-safe.

 |

#### Enum Description

#### \[h2\]NativeWindowOperation

enum NativeWindowOperation

**Description**

Defines an enum for the operation codes in the **OH\_NativeWindow\_NativeWindowHandleOpt** function.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

| Enum | Description |
| :-- | :-- |
| SET\_BUFFER\_GEOMETRY | 
Sets the geometry of the local window buffer.

Variable arguments in the function: \[Input\] int32\_t width and \[Input\] int32\_t height.

Note: The order of width and height for setting is different from that for obtaining. Exercise caution when using this API.

 |
| GET\_BUFFER\_GEOMETRY | 

Obtains the geometry of the local window buffer.

Variable arguments in the function: \[Output\] int32\_t \*height and \[Output\] int32\_t \*width.

Note: The order of width and height for obtaining is different from that for setting. Exercise caution when using this API.

 |
| GET\_FORMAT | 

Obtains the format of the local window buffer.

Variable arguments in the function: \[Output\] int32\_t \*format. For details about the available options, see [OH\_NativeBuffer\_Format](../buffer-common-h/document.md#oh_nativebuffer_format).

 |
| SET\_FORMAT | 

Sets the format of the local window buffer.

Variable arguments in the function: \[Input\] int32\_t format. For details about the available options, see [OH\_NativeBuffer\_Format](../buffer-common-h/document.md#oh_nativebuffer_format).

 |
| GET\_USAGE | 

Obtains the read/write mode of the local window.

Variable arguments in the function: \[Output\] uint64\_t \*usage. For details about the available options, see [OH\_NativeBuffer\_Usage](../native-buffer-h/document.md#oh_nativebuffer_usage).

 |
| SET\_USAGE | 

Sets the usage mode for the local window buffer.

Variable argument in the function: \[Input\] uint64\_t usage.

For details about the available options, see [OH\_NativeBuffer\_Usage](../native-buffer-h/document.md#oh_nativebuffer_usage).

 |
| SET\_STRIDE | 

Sets the stride of the local window buffer.

Variable argument in the function: \[Input\] int32\_t stride.

**Deprecated from**: 16

 |
| GET\_STRIDE | 

Obtains the stride of the local window buffer.

Variable argument in the function: \[Output\] int32\_t \*stride.

**Deprecated from**: 16

**Substitute**: Use [OH\_NativeWindow\_GetBufferHandleFromNative](#oh_nativewindow_getbufferhandlefromnative) to obtain a [BufferHandle](../../structs/bufferhandle/document.md) instance, and obtain the stride from this instance.

 |
| SET\_SWAP\_INTERVAL | 

Sets the swap interval of the local window buffer.

Variable argument in the function: \[Input\] int32\_t interval.

 |
| GET\_SWAP\_INTERVAL | 

Obtains the swap interval of the local window buffer.

Variable argument in the function: \[Output\] int32\_t \*interval.

 |
| SET\_TIMEOUT | 

Sets the timeout duration for requesting the local window buffer, in ms.

Default value: 3,000 ms.

Variable argument in the function: \[Input\] int32\_t timeout.

 |
| GET\_TIMEOUT | 

Obtains the timeout duration for requesting the local window buffer, in ms.

Default value: 3,000 ms.

Variable argument in the function: \[Output\] int32\_t \*timeout.

 |
| SET\_COLOR\_GAMUT | 

Sets the color gamut of the local window buffer.

Variable argument in the function: \[Input\] int32\_t colorGamut.

For details about the available options, see [OH\_NativeBuffer\_ColorGamut](../native-buffer-h/document.md#oh_nativebuffer_colorgamut).

 |
| GET\_COLOR\_GAMUT | 

Obtains the color gamut of the local window buffer.

Variable arguments in the function: \[Output\] int32\_t \*colorGamut. For details about the available options, see [OH\_NativeBuffer\_ColorGamut](../native-buffer-h/document.md#oh_nativebuffer_colorgamut).

 |
| SET\_TRANSFORM | 

Sets the transform of the local window buffer.

Variable argument in the function: \[Input\] int32\_t transform.

For details about the available options, see [OH\_NativeBuffer\_TransformType](../buffer-common-h/document.md#oh_nativebuffer_transformtype).

 |
| GET\_TRANSFORM | 

Obtains the transform of the local window buffer.

Variable argument in the function: \[Output\] int32\_t \*transform.

For details about the available options, see [OH\_NativeBuffer\_TransformType](../buffer-common-h/document.md#oh_nativebuffer_transformtype).

 |
| SET\_UI\_TIMESTAMP | 

Sets the UI timestamp for the local window buffer.

Variable argument in the function: \[Input\] uint64\_t uiTimestamp.

 |
| GET\_BUFFERQUEUE\_SIZE | 

Obtains the memory queue size.

Variable argument in the function: \[Output\] int32\_t \*size.

**Since**: 12

 |
| SET\_SOURCE\_TYPE | 

Sets the source of content displayed in the local window.

Variable argument in the function: \[Input\] int32\_t sourceType. For details about the available options, see [OHSurfaceSource](#ohsurfacesource).

**Since**: 12

 |
| GET\_SOURCE\_TYPE | 

Obtains the source of content displayed in the local window.

Variable argument in the function: \[Output\] int32\_t \*sourceType. For details about the available options, see [OHSurfaceSource](#ohsurfacesource).

**Since**: 12

 |
| SET\_APP\_FRAMEWORK\_TYPE | 

Sets the application framework name of the local window.

Variable argument in the function: \[Input\] char\* frameworkType. A maximum of 64 bytes are supported.

**Since**: 12

 |
| GET\_APP\_FRAMEWORK\_TYPE | 

Obtains the application framework name of the local window.

Variable argument in the function: \[Output\] char\*\* frameworkType.

**Since**: 12

 |
| SET\_HDR\_WHITE\_POINT\_BRIGHTNESS | 

Sets the brightness of HDR white points.

Variable arguments in the function: \[Input\] float brightness. The value range is \[0.0f, 1.0f\].

**Since**: 12

 |
| SET\_SDR\_WHITE\_POINT\_BRIGHTNESS | 

Sets the brightness of SDR white points.

Variable arguments in the function: \[Input\] float brightness. The value range is \[0.0f, 1.0f\].

**Since**: 12

 |
| SET\_DESIRED\_PRESENT\_TIMESTAMP = 24 | 

Sets a timestamp indicating when the local window buffer is expected to show on the screen.

The timestamp takes effect only when **RenderService** is the consumer of the local window and after [OH\_NativeWindow\_NativeWindowFlushBuffer](#oh_nativewindow_nativewindowflushbuffer) is called.

The next buffer added to the queue by the producer is consumed by **RenderService** and displayed on the screen only after the expected on-screen time arrives.

If there are multiple buffers in the queue from various producers, all of them have set **desiredPresentTimestamp**, and the desired time arrives, the buffer that was enqueued earliest will be pushed back into the queue by the consumer.

If the expected on-screen time exceeds the time provided by the consumer by over 1 second, the expected timestamp is ignored.

Variable argument in the function: \[Input\] int64\_t desiredPresentTimestamp. The value must be greater than 0 and should be generated by the standard library std::chrono::steady\_clock, in nanoseconds.

**Since**: 13

 |

#### \[h2\]OHScalingMode

enum OHScalingMode

**Description**

Enumerates the scaling modes.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 9

**Deprecated from**: 10

**Substitute API**: [OHScalingModeV2](#ohscalingmodev2)

| Enum | Description |
| :-- | :-- |
| OH\_SCALING\_MODE\_FREEZE = 0 | The window content cannot be updated before the buffer of the window size is received. |
| OH\_SCALING\_MODE\_SCALE\_TO\_WINDOW | The buffer is scaled in two dimensions to match the window size. |
| OH\_SCALING\_MODE\_SCALE\_CROP | The buffer is scaled uniformly so that its smaller size can match the window size. |
| OH\_SCALING\_MODE\_NO\_SCALE\_CROP | The window is cropped to the size of the buffer's cropping rectangle. Pixels outside the cropping rectangle are considered completely transparent. |

#### \[h2\]OHScalingModeV2

enum OHScalingModeV2

**Description**

Defines an enum for the rendering scaling modes.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

| Enum | Description |
| :-- | :-- |
| OH\_SCALING\_MODE\_FREEZE\_V2 = 0 | Freezes the window. The window content is not updated until a buffer with the same size as the window is received. |
| OH\_SCALING\_MODE\_SCALE\_TO\_WINDOW\_V2 | Scales the buffer to match the window size. |
| OH\_SCALING\_MODE\_SCALE\_CROP\_V2 | Scales the buffer at the original aspect ratio to enable the smaller side of the buffer to match the window, while making the excess part transparent. |
| OH\_SCALING\_MODE\_NO\_SCALE\_CROP\_V2 | Crops the buffer by window size. Pixels outside the cropping rectangle are considered completely transparent. |
| OH\_SCALING\_MODE\_SCALE\_FIT\_V2 | 
Scales the buffer at the original aspect ratio to fully display the buffer content, while filling the unfilled area of the window with the background color.

This mode is not available for the the Emulator.

 |

#### \[h2\]OHHDRMetadataKey

enum OHHDRMetadataKey

**Description**

Enumerates the HDR metadata keys.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 9

**Deprecated from**: 10

| Enum | Description |
| :-- | :-- |
| OH\_METAKEY\_RED\_PRIMARY\_X = 0 | X coordinate of the red primary color. |
| OH\_METAKEY\_RED\_PRIMARY\_Y = 1, | Y coordinate of the red primary color. |
| OH\_METAKEY\_GREEN\_PRIMARY\_X = 2, | X coordinate of the green primary color. |
| OH\_METAKEY\_GREEN\_PRIMARY\_Y = 3, | Y coordinate of the green primary color. |
| OH\_METAKEY\_BLUE\_PRIMARY\_X = 4, | X coordinate of the blue primary color. |
| OH\_METAKEY\_BLUE\_PRIMARY\_Y = 5, | Y coordinate of the blue primary color. |
| OH\_METAKEY\_WHITE\_PRIMARY\_X = 6, | X coordinate of the white point. |
| OH\_METAKEY\_WHITE\_PRIMARY\_Y = 7, | Y coordinate of the white point. |
| OH\_METAKEY\_MAX\_LUMINANCE = 8, | Maximum luminance. |
| OH\_METAKEY\_MIN\_LUMINANCE = 9, | Minimum luminance. |
| OH\_METAKEY\_MAX\_CONTENT\_LIGHT\_LEVEL = 10, | Maximum content light level (MaxCLL). |
| OH\_METAKEY\_MAX\_FRAME\_AVERAGE\_LIGHT\_LEVEL = 11, | Maximum frame average light level. |
| OH\_METAKEY\_HDR10\_PLUS = 12, | HDR10 Plus. |
| OH\_METAKEY\_HDR\_VIVID = 13, | Vivid. |

#### \[h2\]OHSurfaceSource

enum OHSurfaceSource

**Description**

Defines an enum for the sources of content displayed in the local window.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

| Enum | Description |
| :-- | :-- |
| OH\_SURFACE\_SOURCE\_DEFAULT = 0 | Default source. |
| OH\_SURFACE\_SOURCE\_UI | The window content comes from UIs. |
| OH\_SURFACE\_SOURCE\_GAME | The window content comes from games. |
| OH\_SURFACE\_SOURCE\_CAMERA | The window content comes from cameras. |
| OH\_SURFACE\_SOURCE\_VIDEO | The window content comes from videos. |

#### Function Description

#### \[h2\]OH\_NativeWindow\_CreateNativeWindow()

OHNativeWindow\* OH\_NativeWindow\_CreateNativeWindow(void\* pSurface)

**Description**

Creates an **OHNativeWindow** instance. A new **OHNativeWindow** instance is created each time this function is called.

Note: If this API is unavailable, you can use [OH\_NativeImage\_AcquireNativeWindow](../native-image-h/document.md#oh_nativeimage_acquirenativewindow) or XComponent as a substitute.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Deprecated from**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| void\* pSurface | Pointer to a **ProduceSurface**. The type is **sptr<OHOS::Surface>**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md)\* | Returns the pointer to the **OHNativeWindow** instance created. |

#### \[h2\]OH\_NativeWindow\_DestroyNativeWindow()

void OH\_NativeWindow\_DestroyNativeWindow(OHNativeWindow\* window)

**Description**

Decreases the reference count of an **OHNativeWindow** instance by 1 and when the reference count reaches 0, destroys the instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md)\* window | Pointer to an **OHNativeWindow** instance. |

#### \[h2\]OH\_NativeWindow\_CreateNativeWindowBufferFromSurfaceBuffer()

OHNativeWindowBuffer\* OH\_NativeWindow\_CreateNativeWindowBufferFromSurfaceBuffer(void\* pSurfaceBuffer)

**Description**

Creates an **OHNativeWindowBuffer** instance. A new **OHNativeWindowBuffer** instance is created each time this function is called.

Note: If this API is unavailable, you can use [OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer](#oh_nativewindow_createnativewindowbufferfromnativebuffer) as a substitute.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Deprecated from**: 12

**Substitute**: [OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer](#oh_nativewindow_createnativewindowbufferfromnativebuffer)

**Parameters**

| Name | Description |
| :-- | :-- |
| void\* pSurfaceBuffer | Pointer to a **ProduceSurfaceBuffer**. The type is **sptrOHOS::SurfaceBuffer**. |

**Returns**

| Type | Description |
| :-- | :-- |
| OHNativeWindowBuffer\* | Returns the pointer to the **OHNativeWindowBuffer** instance created. |

#### \[h2\]OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer()

OHNativeWindowBuffer\* OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer(OH\_NativeBuffer\* nativeBuffer)

**Description**

Creates an **OHNativeWindowBuffer** instance. A new **OHNativeWindowBuffer** instance is created each time this function is called.

This function must be used in pair with [OH\_NativeWindow\_DestroyNativeWindowBuffer](#oh_nativewindow_destroynativewindowbuffer). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_NativeBuffer\* nativeBuffer | Pointer to an **OH\_NativeBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OHNativeWindowBuffer\* | Returns the pointer to the **OHNativeWindowBuffer** instance created. |

#### \[h2\]OH\_NativeWindow\_DestroyNativeWindowBuffer()

void OH\_NativeWindow\_DestroyNativeWindowBuffer(OHNativeWindowBuffer\* buffer)

**Description**

Decreases the reference count of an **OHNativeWindowBuffer** instance by 1 and when the reference count reaches 0, destroys the instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md)\* buffer | Pointer to an **OHNativeWindowBuffer** instance. |

#### \[h2\]OH\_NativeWindow\_NativeWindowRequestBuffer()

int32\_t OH\_NativeWindow\_NativeWindowRequestBuffer(OHNativeWindow \*window,OHNativeWindowBuffer \*\*buffer, int \*fenceFd)

**Description**

Requests an **OHNativeWindowBuffer** through an **OHNativeWindow** instance for content production.

Before calling this function, you must call [SET\_BUFFER\_GEOMETRY](#nativewindowoperation) to set the width and height of **OHNativeWindow**.

This function must be used in pair with [OH\_NativeWindow\_NativeWindowFlushBuffer](#oh_nativewindow_nativewindowflushbuffer). Otherwise, memory leak occurs.

When **fenceFd** is used up, you must close it.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*\*buffer | 
Double pointer to an **OHNativeWindowBuffer** instance.

You can obtain the **BufferHandle** struct by calling **OH\_NativeWindow\_GetBufferHandleFromNative** to access the buffer memory.

 |
| int \*fenceFd | 

File descriptor handle, used for GPU/CPU sync. The returns are as follows:

\- ≥0: The buffer is being used by the GPU. You need to wait until the file descriptor is ready.

\- **\-1**: The buffer can be used directly.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_NativeWindowFlushBuffer()

int32\_t OH\_NativeWindow\_NativeWindowFlushBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer,int fenceFd, Region region)

**Description**

Flushes the **OHNativeWindowBuffer** filled with the produced content to the buffer queue through an **OHNativeWindow** instance for content consumption.

The system will close **fenceFd**. You do not need to close it.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*buffer | Pointer to an **OHNativeWindowBuffer** instance. |
| int fenceFd | 
File descriptor handle, which is used for timing synchronization. The options are as follows:

\- **\-1**: The CPU rendering is complete, and no timing synchronization is required.

\- ≥0: The handle is converted from a GPU synchronization object (for example, **eglDupNativeFenceFDANDROID** of EGL). The peer end needs to synchronize timing through fenceFd.

 |
| [Region](../../structs/region/document.md) region | Region struct, which indicates a dirty region where content is updated. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_GetLastFlushedBuffer()

int32\_t OH\_NativeWindow\_GetLastFlushedBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer,int \*fenceFd, float matrix\[16\])

**Description**

Obtains the **OHNativeWindowBuffer** that was flushed to the buffer queue last time through an **OHNativeWindow** instance.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 11

**Deprecated from**: 12

**Substitute**: [OH\_NativeWindow\_GetLastFlushedBufferV2](#oh_nativewindow_getlastflushedbufferv2)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*\*buffer | Double pointer to an **OHNativeWindowBuffer** instance. |
| int \*fenceFd | Pointer to a file descriptor. |
| matrix | Retrieved 4 × 4 transformation matrix. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_NativeWindowAbortBuffer()

int32\_t OH\_NativeWindow\_NativeWindowAbortBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)

**Description**

Returns the **OHNativeWindowBuffer** to the buffer queue through an **OHNativeWindow** instance, without filling in any content. The **OHNativeWindowBuffer** can be used for a new request.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*buffer | Pointer to an **OHNativeWindowBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_NativeWindowHandleOpt()

int32\_t OH\_NativeWindow\_NativeWindowHandleOpt(OHNativeWindow \*window, int code, ...)

**Description**

Sets or obtains the attributes of an **OHNativeWindow** instance, including the width, height, and content format.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| int code | Operation code. For details, see [NativeWindowOperation](#nativewindowoperation). |
| ... | Variable argument, which must be the same as the data type corresponding to the operation code. The number of input parameters must be the same as that of the operation code. Otherwise, undefined behavior may occur. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_GetBufferHandleFromNative()

BufferHandle \*OH\_NativeWindow\_GetBufferHandleFromNative(OHNativeWindowBuffer \*buffer)

**Description**

Obtains the pointer to a **BufferHandle** of an **OHNativeWindowBuffer** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*buffer | Pointer to an **OHNativeWindowBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [BufferHandle](../../structs/bufferhandle/document.md) | Returns the pointer to the [BufferHandle](../../structs/bufferhandle/document.md) instance obtained. |

#### \[h2\]OH\_NativeWindow\_NativeObjectReference()

int32\_t OH\_NativeWindow\_NativeObjectReference(void \*obj)

**Description**

Adds the reference count of a native object.

This function must be used in pair with [OH\_NativeWindow\_NativeObjectUnreference](#oh_nativewindow_nativeobjectunreference). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*obj | Pointer to an **OHNativeWindow** or **OHNativeWindowBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_NativeObjectUnreference()

int32\_t OH\_NativeWindow\_NativeObjectUnreference(void \*obj)

**Description**

Decreases the reference count of a native object by 1 and when the reference count reaches 0, destroys this object.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*obj | Pointer to an **OHNativeWindow** or **OHNativeWindowBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_GetNativeObjectMagic()

int32\_t OH\_NativeWindow\_GetNativeObjectMagic(void \*obj)

**Description**

Obtains the magic ID of a native object.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 8

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*obj | Pointer to an **OHNativeWindow** or **OHNativeWindowBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns the magic ID, which is unique for each native object. |

#### \[h2\]OH\_NativeWindow\_NativeWindowSetScalingMode()

int32\_t OH\_NativeWindow\_NativeWindowSetScalingMode(OHNativeWindow \*window, uint32\_t sequence,OHScalingMode scalingMode)

**Description**

Sets a scaling mode for an **OHNativeWindow**.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 9

**Deprecated from**: 10

**Substitute**: [OH\_NativeWindow\_NativeWindowSetScalingModeV2](#oh_nativewindow_nativewindowsetscalingmodev2)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| uint32\_t sequence | Sequence of the producer buffer. |
| [OHScalingMode](#ohscalingmode) scalingMode | Scaling mode to set. For details, see [OHScalingMode](#ohscalingmode). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** if the operation is successful. |

#### \[h2\]OH\_NativeWindow\_NativeWindowSetMetaData()

int32\_t OH\_NativeWindow\_NativeWindowSetMetaData(OHNativeWindow \*window, uint32\_t sequence, int32\_t size,const OHHDRMetaData \*metaData)

**Description**

Sets metadata for an **OHNativeWindow**.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 9

**Deprecated from**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| uint32\_t sequence | Sequence of the producer buffer. |
| int32\_t size | Size of the **OHHDRMetaData** array. |
| metaData | Pointer to the **OHHDRMetaData** array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** if the operation is successful. |

#### \[h2\]OH\_NativeWindow\_NativeWindowSetMetaDataSet()

int32\_t OH\_NativeWindow\_NativeWindowSetMetaDataSet(OHNativeWindow \*window, uint32\_t sequence, OHHDRMetadataKey key,int32\_t size, const uint8\_t \*metaData)

**Description**

Sets a metadata set for an **OHNativeWindow**.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 9

**Deprecated from**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| uint32\_t sequence | Sequence of the producer buffer. |
| [OHHDRMetadataKey](#ohhdrmetadatakey) key | Metadata key. For details, see [OHHDRMetadataKey](#ohhdrmetadatakey). |
| int32\_t size | Size of the uint8\_t vector. |
| metaDate | Pointer to the uint8\_t vector. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** if the operation is successful. |

#### \[h2\]OH\_NativeWindow\_NativeWindowSetTunnelHandle()

int32\_t OH\_NativeWindow\_NativeWindowSetTunnelHandle(OHNativeWindow \*window, const OHExtDataHandle \*handle)

**Description**

Sets a tunnel handle to an **OHNativeWindow**.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 9

**Deprecated from**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| const [OHExtDataHandle](../../structs/ohextdatahandle/document.md) \*handle | Pointer to an **OHExtDataHandle** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **0** if the operation is successful. |

#### \[h2\]OH\_NativeWindow\_NativeWindowAttachBuffer()

int32\_t OH\_NativeWindow\_NativeWindowAttachBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)

**Description**

Attaches an **OHNativeWindowBuffer** to an **OHNativeWindow** instance.

This function must be used in pair with [OH\_NativeWindow\_NativeWindowDetachBuffer](#oh_nativewindow_nativewindowdetachbuffer). Otherwise, memory management disorder may occur.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*buffer | Pointer to an **OHNativeWindowBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_NativeWindowDetachBuffer()

int32\_t OH\_NativeWindow\_NativeWindowDetachBuffer(OHNativeWindow \*window, OHNativeWindowBuffer \*buffer)

**Description**

Detaches an **OHNativeWindowBuffer** from an **OHNativeWindow** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*buffer | Pointer to an **OHNativeWindowBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_GetSurfaceId()

int32\_t OH\_NativeWindow\_GetSurfaceId(OHNativeWindow \*window, uint64\_t \*surfaceId)

**Description**

Obtains a surface ID through an **OHNativeWindow**.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| uint64\_t \*surfaceId | Pointer to the surface ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_CreateNativeWindowFromSurfaceId()

int32\_t OH\_NativeWindow\_CreateNativeWindowFromSurfaceId(uint64\_t surfaceId, OHNativeWindow \*\*window)

**Description**

Creates an **OHNativeWindow** instance based on a surface ID.

This function must be used in pair with [OH\_NativeWindow\_DestroyNativeWindow](#oh_nativewindow_destroynativewindow). Otherwise, memory leak occurs.

If **OHNativeWindow** instances are released concurrently, call [OH\_NativeWindow\_NativeObjectReference](#oh_nativewindow_nativeobjectreference) and [OH\_NativeWindow\_NativeObjectUnreference](#oh_nativewindow_nativeobjectunreference) to increase and decrease the reference count of **OHNativeWindow**.

The surface obtained by using the surface ID must be created in the current process, but not in a different process.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| uint64\_t surfaceId | Surface ID. |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*\*window | Double pointer to an **OHNativeWindow** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_NativeWindowSetScalingModeV2()

int32\_t OH\_NativeWindow\_NativeWindowSetScalingModeV2(OHNativeWindow\* window, OHScalingModeV2 scalingMode)

**Description**

Sets a rendering scaling mode for an **OHNativeWindow** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md)\* window | Pointer to an **OHNativeWindow** instance. |
| [OHScalingModeV2](#ohscalingmodev2) scalingMode | Scaling mode. For details about the available options, see **OHScalingModeV2**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_GetLastFlushedBufferV2()

int32\_t OH\_NativeWindow\_GetLastFlushedBufferV2(OHNativeWindow \*window, OHNativeWindowBuffer \*\*buffer,int \*fenceFd, float matrix\[16\])

**Description**

Obtains the **OHNativeWindowBuffer** that was flushed to the buffer queue last time through an **OHNativeWindow** instance. The difference between this function and **OH\_NativeWindow\_GetLastFlushedBuffer** lies in the matrix.

This function must be used in pair with [OH\_NativeWindow\_NativeObjectUnreference](#oh_nativewindow_nativeobjectunreference). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an **OHNativeWindow** instance. |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*\*buffer | Double pointer to an **OHNativeWindowBuffer** instance. |
| int \*fenceFd | Pointer to a file descriptor. |
| matrix | Retrieved 4 × 4 transformation matrix. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_SetBufferHold()

void OH\_NativeWindow\_SetBufferHold(OHNativeWindow \*window)

**Description**

Enables the single-frame buffering mechanism, which caches a frame buffer in advance and delays the display of the frame to smooth the frame rate fluctuation.

After this function is enabled, the system caches a frame buffer, and the frame is displayed one display cycle later. If a long frame or uneven frame interval occurs during subsequent rendering, the cached frame can be used to fill the blank to reduce image freezing.

You are advised to call this function before the rendering peak to establish buffer protection. The buffer takes effect only once. After the buffer is consumed, it automatically becomes invalid. If continuous protection is required, call this function again.

This function is applicable to scenarios that require high frame rate stability, such as games, animations, and complex UI rendering. However, it introduces a frame display delay (for example, 16.6 ms in the 60 Hz refresh rate). Therefore, this function is not recommended in high-interaction real-time scenarios.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an [OHNativeWindow](../../structs/nativewindow/document.md) instance. |

#### \[h2\]OH\_NativeWindow\_WriteToParcel()

int32\_t OH\_NativeWindow\_WriteToParcel(OHNativeWindow \*window, OHIPCParcel \*parcel)

**Description**

Writes an **OHNativeWindow** instance to an **OHIPCParcel** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an [OHNativeWindow](../../structs/nativewindow/document.md) instance. |
| [OHIPCParcel](../../structs/ohipcparcel/document.md) \*parcel | Pointer to an [OHIPCParcel](../../structs/ohipcparcel/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_ReadFromParcel()

int32\_t OH\_NativeWindow\_ReadFromParcel(OHIPCParcel \*parcel, OHNativeWindow \*\*window)

**Description**

Reads an **OHNativeWindow** instance from an **OHIPCParcel** instance.

This function creates an **OHNativeWindow** instance. After it is used, you need to use this function in pair with [OH\_NativeWindow\_DestroyNativeWindow](#oh_nativewindow_destroynativewindow). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHIPCParcel](../../structs/ohipcparcel/document.md) \*parcel | Pointer to an [OHIPCParcel](../../structs/ohipcparcel/document.md) instance. |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*\*window | Double pointer to an [OHNativeWindow](../../structs/nativewindow/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_SetColorSpace()

int32\_t OH\_NativeWindow\_SetColorSpace(OHNativeWindow \*window, OH\_NativeBuffer\_ColorSpace colorSpace)

**Description**

Sets the color space for an **OHNativeWindow** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an [OHNativeWindow](../../structs/nativewindow/document.md) instance. |
| [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace) colorSpace | Pointer to the color space. For details about the available options, see [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_GetColorSpace()

int32\_t OH\_NativeWindow\_GetColorSpace(OHNativeWindow \*window, OH\_NativeBuffer\_ColorSpace \*colorSpace)

**Description**

Obtains the color space of an **OHNativeWindow** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an [OHNativeWindow](../../structs/nativewindow/document.md) instance. |
| [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace) \*colorSpace | Pointer to the color space. For details about the available options, see [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_SetMetadataValue()

int32\_t OH\_NativeWindow\_SetMetadataValue(OHNativeWindow \*window, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t size, uint8\_t \*metadata)

**Description**

Sets a metadata value for an **OHNativeWindow** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an [OHNativeWindow](../../structs/nativewindow/document.md) instance. |
| [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey) metadataKey | Metadata type of the window. The value is obtained from [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey). |
| int32\_t size | Size of the uint8\_t vector. For details about the value range, see [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey). |
| metaDate | Pointer to the uint8\_t vector. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_GetMetadataValue()

int32\_t OH\_NativeWindow\_GetMetadataValue(OHNativeWindow \*window, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t \*size, uint8\_t \*\*metadata)

**Description**

Obtains the metadata value of an **OHNativeWindow** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an [OHNativeWindow](../../structs/nativewindow/document.md) instance. |
| [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey) metadataKey | Metadata type of the window. The value is obtained from [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey). |
| int32\_t \*size | Size of the uint8\_t vector. For details about the value range, see [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey). |
| metaDate | Double pointer to the uint8\_t vector. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_CleanCache()

int32\_t OH\_NativeWindow\_CleanCache(OHNativeWindow \*window)

**Description**

Clears the **OHNativeWindowBuffer** cache in **OHNativeWindow**.

Ensure that **OHNativeWindowBuffer** has been successfully allocated by calling [OH\_NativeWindow\_NativeWindowRequestBuffer](#oh_nativewindow_nativewindowrequestbuffer).

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to an [OHNativeWindow](../../structs/nativewindow/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeWindow\_PreAllocBuffers()

int32\_t OH\_NativeWindow\_PreAllocBuffers(OHNativeWindow \*window, uint32\_t allocBufferCnt)

**Description**

Request multiple **OHNativeWindowBuffer** blocks in advance through the **OHNativeWindow** object for content production.

Before calling this function, you need to set the width and height of **OHNativeWindow** through [OH\_NativeWindow\_NativeWindowHandleOpt](#oh_nativewindow_nativewindowhandleopt).

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeWindow

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindow](../../structs/nativewindow/document.md) \*window | Pointer to the **OHNativeWindow** struct instance. |
| uint32\_t allocBufferCnt | Number of buffers to be requested in advance. If the value of **allocBufferCnt** is greater than that of **bufferQueueSize**, only **bufferQueueSize** buffers can be requested in advance. **bufferQueueSize** can be obtained by calling [OH\_NativeWindow\_NativeWindowHandleOpt](#oh_nativewindow_nativewindowhandleopt). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |
