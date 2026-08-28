# image\_mdk.h

#### Overview

The file declares the APIs used to access the image rectangle, size, format, and component data.

**File to include**: <multimedia/image\_framework/image\_mdk.h>

**Library**: libimage\_ndk.z.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OhosImageRect](../../structs/ohosimagerect/document.md) | \- | Describes the information about an image rectangle. |
| [ImageNative\_](../../structs/imagenative/document.md) | ImageNative | Describes an image object at the native layer. |
| [OhosImageComponent](../../structs/ohosimagecomponent/document.md) | \- | Describes the information about an image component. |

#### \[h2\]Enums

| Name | Description |
| :-- | :-- |
| [Image Formats](#image-formats) | Enumerates the image formats. |
| [Image Color Channel Types](#image-color-channel-types) | Enumerates the image color channel types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [ImageNative\* OH\_Image\_InitImageNative(napi\_env env, napi\_value source)](#oh_image_initimagenative) | Converts an Image object at the JavaScript native layer into an ImageNative object. |
| [int32\_t OH\_Image\_ClipRect(const ImageNative\* native, struct OhosImageRect\* rect)](#oh_image_cliprect) | Obtains OhosImageRect of an ImageNative object. |
| [int32\_t OH\_Image\_Size(const ImageNative\* native, struct OhosImageSize\* size)](#oh_image_size) | Obtains OhosImageSize of an ImageNative object. |
| [int32\_t OH\_Image\_Format(const ImageNative\* native, int32\_t\* format)](#oh_image_format) | Obtains the format of an ImageNative object. |
| [int32\_t OH\_Image\_GetComponent(const ImageNative\* native, int32\_t componentType, struct OhosImageComponent\* componentNative)](#oh_image_getcomponent) | Obtains OhosImageComponent of an ImageNative object. |
| [int32\_t OH\_Image\_Release(ImageNative\* native)](#oh_image_release) | 
Releases an ImageNative object.

This function is not used to release an Image object at the JavaScript native API. It is used to release an ImageNative object parsed by calling [OH\_Image\_InitImageNative](#oh_image_initimagenative).

 |

#### Enum Description

#### \[h2\]Image Formats

enum anonymous enum

**Description**

Enumerates the image formats.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OHOS\_IMAGE\_FORMAT\_YCBCR\_422\_SP = 1000 | YCbCr422 semi-planar format. |
| OHOS\_IMAGE\_FORMAT\_JPEG = 2000 | JPEG encoding format. |

#### \[h2\]Image Color Channel Types

enum anonymous enum

**Description**

Enumerates the image color channel types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_Y = 1 | Luminance component. |
| OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_U = 2 | Chrominance component - blue projection. |
| OHOS\_IMAGE\_COMPONENT\_FORMAT\_YUV\_V = 3 | Chrominance component - red projection. |
| OHOS\_IMAGE\_COMPONENT\_FORMAT\_JPEG = 4 | JPEG. |

#### Function Description

#### \[h2\]OH\_Image\_InitImageNative()

ImageNative\* OH\_Image\_InitImageNative(napi\_env env, napi\_value source)

**Description**

Parses an ImageNative object from an Image object at the JavaScript native layer.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the JNI environment. |
| napi\_value source | Image object at the JavaScript native layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageNative](../../structs/imagenative/document.md)\* | Pointer to the ImageNative object. If the operation fails, a null pointer is returned. |

**See also**

[OH\_Image\_Release](#oh_image_release)

#### \[h2\]OH\_Image\_ClipRect()

int32\_t OH\_Image\_ClipRect(const ImageNative\* native, struct OhosImageRect\* rect)

**Description**

Obtains OhosImageRect of an ImageNative object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageNative](../../structs/imagenative/document.md)\* native | Pointer to an ImageNative object. |
| struct [OhosImageRect](../../structs/ohosimagerect/document.md)\* rect | Pointer to the OhosImageRect object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_Image\_Size()

int32\_t OH\_Image\_Size(const ImageNative\* native, struct OhosImageSize\* size)

**Description**

Obtains OhosImageSize of an ImageNative object.

If the ImageNative object stores the camera preview stream data (YUV image data), the width and height in **OhosImageSize** obtained correspond to those of the YUV image. If the ImageNative object stores the camera photo stream data (JPEG image data, which is already encoded), the width in **OhosImageSize** obtained is the JPEG data size, and the height is 1.

The type of data stored in the ImageNative object depends on whether the application passes the surface ID in the receiver to a previewOutput or captureOutput object of the camera. For details about the best practices of camera preview and photo capture, see [Secondary Processing of Preview Streams (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-camera-preview-imagereceiver) and [Photo Capture (C/C++)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/native-camera-shooting).

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageNative](../../structs/imagenative/document.md)\* native | Pointer to an ImageNative object. |
| struct [OhosImageSize](../../structs/ohosimagesize/document.md)\* size | Pointer to the OhosImageSize object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_Image\_Format()

int32\_t OH\_Image\_Format(const ImageNative\* native, int32\_t\* format)

**Description**

Obtains the format of an ImageNative object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageNative](../../structs/imagenative/document.md)\* native | Pointer to an ImageNative object. |
| int32\_t\* format | Pointer to the image format obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_Image\_GetComponent()

int32\_t OH\_Image\_GetComponent(const ImageNative\* native, int32\_t componentType, struct OhosImageComponent\* componentNative)

**Description**

Obtains OhosImageComponent of an ImageNative object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageNative](../../structs/imagenative/document.md)\* native | Pointer to an ImageNative object. |
| int32\_t componentType | Type of the component. |
| struct [OhosImageComponent](../../structs/ohosimagecomponent/document.md)\* componentNative | Pointer to the OhosImageComponent object obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_SURFACE\_GET\_PARAMETER\_FAILED**: Obtaining parameters from the surface fails.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_Image\_Release()

int32\_t OH\_Image\_Release(ImageNative\* native)

**Description**

Releases an ImageNative object.

This function is not used to release an Image object at the JavaScript native API. It is used to release an ImageNative object parsed by calling [OH\_Image\_InitImageNative](#oh_image_initimagenative).

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [ImageNative](../../structs/imagenative/document.md)\* native | Pointer to an ImageNative object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

 |

**See also**

[OH\_Image\_InitImageNative](#oh_image_initimagenative)
