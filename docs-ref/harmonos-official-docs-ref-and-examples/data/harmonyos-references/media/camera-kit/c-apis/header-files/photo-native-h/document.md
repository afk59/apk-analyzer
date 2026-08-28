# photo\_native.h

#### Overview

The file declares the camera photo concepts.

**File to include**: <ohcamera/photo\_native.h>

**Library**: libohcamera.so

**System capability**: SystemCapability.Multimedia.Camera.Core

**Since**: 12

**Related module**: [OH\_Camera](../../modules/oh-camera/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_PhotoNative](../../structs/oh-photonative/document.md) | OH\_PhotoNative | Describes the photo object, which is a full-quality image object. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Camera\_ErrorCode OH\_PhotoNative\_GetMainImage(OH\_PhotoNative\* photo, OH\_ImageNative\*\* mainImage)](#oh_photonative_getmainimage) | Obtains a full-quality image. |
| [Camera\_ErrorCode OH\_PhotoNative\_Release(OH\_PhotoNative\* photo)](#oh_photonative_release) | Releases a full-quality image. |

#### Function Description

#### \[h2\]OH\_PhotoNative\_GetMainImage()

Camera\_ErrorCode OH\_PhotoNative\_GetMainImage(OH\_PhotoNative\* photo, OH\_ImageNative\*\* mainImage)

**Description**

Obtains a full-quality image.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PhotoNative](../../structs/oh-photonative/document.md)\* photo | Pointer to an OH\_PhotoNative instance. |
| [OH\_ImageNative](../../../../image-kit/c-apis/structs/oh-imagenative/document.md)\*\* mainImage | Double pointer to the full-quality image, which is an OH\_ImageNative instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |

#### \[h2\]OH\_PhotoNative\_Release()

Camera\_ErrorCode OH\_PhotoNative\_Release(OH\_PhotoNative\* photo)

**Description**

Releases a full-quality image.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PhotoNative](../../structs/oh-photonative/document.md)\* photo | Pointer to the OH\_PhotoNative instance to release. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Camera\_ErrorCode](../camera-h/document.md#camera_errorcode) | 
**CAMERA\_OK**: The operation is successful.

**CAMERA\_INVALID\_ARGUMENT**: A parameter is missing or the parameter type is incorrect.

 |
