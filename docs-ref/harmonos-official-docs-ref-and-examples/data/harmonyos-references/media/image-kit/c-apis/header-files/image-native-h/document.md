# image\_native.h

#### Overview

The file declares the cropping rectangle, size, and component data of an image.

**File to include**: <multimedia/image\_framework/image/image\_native.h>

**Library**: libohimage.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) | OH\_ImageNative | Describes the alias for an image object at the native layer. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Image\_ErrorCode OH\_ImageNative\_GetImageSize(OH\_ImageNative \*image, Image\_Size \*size)](#oh_imagenative_getimagesize) | Obtains the [Image\_Size](../../structs/image-size/document.md) information of an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. |
| [Image\_ErrorCode OH\_ImageNative\_GetComponentTypes(OH\_ImageNative \*image, uint32\_t \*\*types, size\_t \*typeSize)](#oh_imagenative_getcomponenttypes) | Obtains the component types of an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. |
| [Image\_ErrorCode OH\_ImageNative\_GetByteBuffer(OH\_ImageNative \*image, uint32\_t componentType, OH\_NativeBuffer \*\*nativeBuffer)](#oh_imagenative_getbytebuffer) | Obtains the buffer corresponding to a component type in an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. |
| [Image\_ErrorCode OH\_ImageNative\_GetBufferSize(OH\_ImageNative \*image, uint32\_t componentType, size\_t \*size)](#oh_imagenative_getbuffersize) | Obtains the size of the buffer corresponding to a component type in an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. |
| [Image\_ErrorCode OH\_ImageNative\_GetRowStride(OH\_ImageNative \*image, uint32\_t componentType, int32\_t \*rowStride)](#oh_imagenative_getrowstride) | Obtains the row stride corresponding to a component type in an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. |
| [Image\_ErrorCode OH\_ImageNative\_GetPixelStride(OH\_ImageNative \*image, uint32\_t componentType, int32\_t \*pixelStride)](#oh_imagenative_getpixelstride) | Obtains the pixel stride corresponding to a component type in an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. |
| [Image\_ErrorCode OH\_ImageNative\_GetTimestamp(OH\_ImageNative \*image, int64\_t \*timestamp)](#oh_imagenative_gettimestamp) | Obtains the timestamp of an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. |
| [Image\_ErrorCode OH\_ImageNative\_Release(OH\_ImageNative \*image)](#oh_imagenative_release) | Releases an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. |

#### Function Description

#### \[h2\]OH\_ImageNative\_GetImageSize()

Image\_ErrorCode OH\_ImageNative\_GetImageSize(OH\_ImageNative \*image, Image\_Size \*size)

**Description**

Obtains the [Image\_Size](../../structs/image-size/document.md) information of an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object.

If the OH\_ImageNative object stores the camera preview stream data (YUV image data), the width and height in **Image\_Size** obtained correspond to those of the YUV image. If the OH\_ImageNative object stores the camera photo stream data (JPEG image data, which is already encoded), the width in **Image\_Size** obtained is the JPEG data size, and the height is 1.

The type of data stored in the OH\_ImageNative object depends on whether the application passes the surface ID in the receiver to a previewOutput or captureOutput object of the camera. For details about the best practices of camera preview and photo capture, see [Secondary Processing of Preview Streams (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-camera-preview-imagereceiver) and [Photo Capture (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-camera-shooting).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) \*image | Pointer to an OH\_ImageNative object. |
| [Image\_Size](../../structs/image-size/document.md) \*size | Pointer to the Image\_Size object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_ImageNative\_GetComponentTypes()

Image\_ErrorCode OH\_ImageNative\_GetComponentTypes(OH\_ImageNative \*image,uint32\_t \*\*types, size\_t \*typeSize)

**Description**

Obtains the component types of an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) \*image | Pointer to an OH\_ImageNative object. |
| uint32\_t \*\*types | Pointer to the component type list object obtained. Since the number of components is uncertain, this API needs to be called twice: first, set **types** to **NULL** to obtain the number of components (**typeSize**); second, allocate corresponding memory for **types** based on **typeSize** and then obtain the component type list. |
| size\_t \*typeSize | Pointer to the number of component types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageNative\_GetByteBuffer()

Image\_ErrorCode OH\_ImageNative\_GetByteBuffer(OH\_ImageNative \*image,uint32\_t componentType, OH\_NativeBuffer \*\*nativeBuffer)

**Description**

Obtains the buffer corresponding to a component type in an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) \*image | Pointer to an OH\_ImageNative object. |
| uint32\_t componentType | Component type. The value is obtained using the [OH\_ImageNative\_GetComponentTypes](#oh_imagenative_getcomponenttypes) API. |
| [OH\_NativeBuffer](../../../../../graphics/arkgraphics-2d/c-apis/structs/oh-nativebuffer/document.md) \*\*nativeBuffer | Double pointer to the buffer, which is an OH\_NativeBuffer object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageNative\_GetBufferSize()

Image\_ErrorCode OH\_ImageNative\_GetBufferSize(OH\_ImageNative \*image,uint32\_t componentType, size\_t \*size)

**Description**

Obtains the size of the buffer corresponding to a component type in an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) \*image | Pointer to an OH\_ImageNative object. |
| uint32\_t componentType | Component type. The value is obtained using the [OH\_ImageNative\_GetComponentTypes](#oh_imagenative_getcomponenttypes) API. |
| size\_t \*size | Pointer to the size of the buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageNative\_GetRowStride()

Image\_ErrorCode OH\_ImageNative\_GetRowStride(OH\_ImageNative \*image,uint32\_t componentType, int32\_t \*rowStride)

**Description**

Obtains the row stride corresponding to a component type in an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object.

Camera preview stream data must be read based on the stride. For details, see [Secondary Processing of Preview Streams (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-camera-preview-imagereceiver).

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) \*image | Pointer to an OH\_ImageNative object. |
| uint32\_t componentType | Component type. The value is obtained using the [OH\_ImageNative\_GetComponentTypes](#oh_imagenative_getcomponenttypes) API. |
| int32\_t \*rowStride | Pointer to the row stride obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageNative\_GetPixelStride()

Image\_ErrorCode OH\_ImageNative\_GetPixelStride(OH\_ImageNative \*image,uint32\_t componentType, int32\_t \*pixelStride)

**Description**

Obtains the pixel stride corresponding to a component type in an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) \*image | Pointer to an OH\_ImageNative object. |
| uint32\_t componentType | Component type. The value is obtained using the [OH\_ImageNative\_GetComponentTypes](#oh_imagenative_getcomponenttypes) API. |
| int32\_t \*pixelStride | Pointer to the pixel stride obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageNative\_GetTimestamp()

Image\_ErrorCode OH\_ImageNative\_GetTimestamp(OH\_ImageNative \*image, int64\_t \*timestamp)

**Description**

Obtains the timestamp of an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object. Timestamps, measured in nanoseconds, are usually monotonically increasing.

The specific meaning and baseline of these timestamps are determined by the image producer, which is the camera in the camera preview and photo scenarios. As a result, images from different producers may carry timestamps with distinct meanings and baselines, making direct comparison between them infeasible.

To obtain the generation time of a photo, you can use [OH\_ImageSourceNative\_GetImageProperty](../image-source-native-h/document.md#oh_imagesourcenative_getimageproperty) to read the related Exif information.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) \*image | Pointer to an OH\_ImageNative object. |
| int64\_t \*timestamp | Pointer to the timestamp. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImageNative\_Release()

Image\_ErrorCode OH\_ImageNative\_Release(OH\_ImageNative \*image)

**Description**

Releases an [OH\_ImageNative](../../structs/oh-imagenative/document.md) object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageNative](../../structs/oh-imagenative/document.md) \*image | Pointer to an OH\_ImageNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |
