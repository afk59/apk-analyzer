# image\_pixel\_map\_mdk.h

#### Overview

The file declares the APIs used to lock, access, and unlock a PixelMap.

**File to include**: <multimedia/image\_framework/image\_pixel\_map\_mdk.h>

**Library**: libpixelmap\_ndk.z.so

**System capability**: SystemCapability.Multimedia.Image.Core

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OhosPixelMapInfos](../../structs/ohospixelmapinfos/document.md) | OhosPixelMapInfos | Describes the information about a PixelMap. |
| [NativePixelMap\_](../../structs/nativepixelmap/document.md) | NativePixelMap | Describes the native PixelMap information. It defines the data type name of the PixelMap at the native layer. |
| [OhosPixelMapCreateOps](../../structs/ohospixelmapcreateops/document.md) | \- | Describes the options used for creating a PixelMap. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [anonymous enum](#pixelmap-alpha-types) | \- | Enumerates the PixelMap alpha types. |
| [anonymous enum](#pixelmap-editing-types) | \- | Enumerates the PixelMap editing types. |
| [OH\_PixelMap\_AntiAliasingLevel](#oh_pixelmap_antialiasinglevel) | OH\_PixelMap\_AntiAliasingLevel | Enumerates the anti-aliasing levels used for scaling PixelMaps. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_PixelMap\_CreatePixelMap(napi\_env env, OhosPixelMapCreateOps info, void\* buf, size\_t len, napi\_value\* res)](#oh_pixelmap_createpixelmap) | 
Creates a PixelMap object. Currently, only BGRA input streams are supported.

The buffer passed in by this API does not support the stride.

This function does not support the DMA memory.

 |
| [int32\_t OH\_PixelMap\_CreatePixelMapWithStride(napi\_env env, OhosPixelMapCreateOps info, void\* buf, size\_t len, int32\_t rowStride, napi\_value\* res)](#oh_pixelmap_createpixelmapwithstride) | 

Creates a PixelMap object.

Currently, only BGRA input streams are supported. For a PixelMap in RGBA format (with the size greater than 512\*512), DMA memory is used by default.

 |
| [int32\_t OH\_PixelMap\_CreateAlphaPixelMap(napi\_env env, napi\_value source, napi\_value\* alpha)](#oh_pixelmap_createalphapixelmap) | Creates a PixelMap object that contains only alpha channel information. |
| [NativePixelMap\* OH\_PixelMap\_InitNativePixelMap(napi\_env env, napi\_value source)](#oh_pixelmap_initnativepixelmap) | Initializes a NativePixelMap object. |
| [int32\_t OH\_PixelMap\_GetBytesNumberPerRow(const NativePixelMap\* native, int32\_t\* num)](#oh_pixelmap_getbytesnumberperrow) | Obtains the number of bytes per row of a NativePixelMap object. |
| [int32\_t OH\_PixelMap\_GetIsEditable(const NativePixelMap\* native, int32\_t\* editable)](#oh_pixelmap_getiseditable) | Checks whether a NativePixelMap object is editable. |
| [int32\_t OH\_PixelMap\_IsSupportAlpha(const NativePixelMap\* native, int32\_t\* alpha)](#oh_pixelmap_issupportalpha) | Checks whether a NativePixelMap object supports alpha channels. |
| [int32\_t OH\_PixelMap\_SetAlphaAble(const NativePixelMap\* native, int32\_t alpha)](#oh_pixelmap_setalphaable) | Sets an alpha channel for a NativePixelMap object. |
| [int32\_t OH\_PixelMap\_GetDensity(const NativePixelMap\* native, int32\_t\* density)](#oh_pixelmap_getdensity) | Obtains the pixel density of a NativePixelMap object. |
| [int32\_t OH\_PixelMap\_SetDensity(const NativePixelMap\* native, int32\_t density)](#oh_pixelmap_setdensity) | Sets the pixel density for a NativePixelMap object. |
| [int32\_t OH\_PixelMap\_SetOpacity(const NativePixelMap\* native, float opacity)](#oh_pixelmap_setopacity) | Sets the opacity for a NativePixelMap object. |
| [int32\_t OH\_PixelMap\_Scale(const NativePixelMap\* native, float x, float y)](#oh_pixelmap_scale) | 

Scales a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Scale](../pixelmap-native-h/document.md#oh_pixelmapnative_scale) since API version 12.

 |
| [int32\_t OH\_PixelMap\_ScaleWithAntiAliasing(const NativePixelMap\* native, float x, float y, OH\_PixelMap\_AntiAliasingLevel level)](#oh_pixelmap_scalewithantialiasing) | 

Scales a NativePixelMap object based on the specified anti-aliasing level, width, and height.

You are advised to use the new function [OH\_PixelmapNative\_ScaleWithAntiAliasing](../pixelmap-native-h/document.md#oh_pixelmapnative_scalewithantialiasing) since API version 12.

 |
| [int32\_t OH\_PixelMap\_Translate(const NativePixelMap\* native, float x, float y)](#oh_pixelmap_translate) | 

Translates a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Translate](../pixelmap-native-h/document.md#oh_pixelmapnative_translate) since API version 12.

 |
| [int32\_t OH\_PixelMap\_Rotate(const NativePixelMap\* native, float angle)](#oh_pixelmap_rotate) | 

Rotates a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Rotate](../pixelmap-native-h/document.md#oh_pixelmapnative_rotate) since API version 12.

 |
| [int32\_t OH\_PixelMap\_Flip(const NativePixelMap\* native, int32\_t x, int32\_t y)](#oh_pixelmap_flip) | 

Flips a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Flip](../pixelmap-native-h/document.md#oh_pixelmapnative_flip) since API version 12.

 |
| [int32\_t OH\_PixelMap\_Crop(const NativePixelMap\* native, int32\_t x, int32\_t y, int32\_t width, int32\_t height)](#oh_pixelmap_crop) | 

Crops a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Crop](../pixelmap-native-h/document.md#oh_pixelmapnative_crop) since API version 12.

 |
| [int32\_t OH\_PixelMap\_GetImageInfo(const NativePixelMap\* native, OhosPixelMapInfos \*info)](#oh_pixelmap_getimageinfo) | 

Obtains the image information of a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_GetImageInfo](../pixelmap-native-h/document.md#oh_pixelmapnative_getimageinfo) since API version 12.

 |
| [int32\_t OH\_PixelMap\_AccessPixels(const NativePixelMap\* native, void\*\* addr)](#oh_pixelmap_accesspixels) | Obtains the memory address of a NativePixelMap object and locks the memory. |
| [int32\_t OH\_PixelMap\_UnAccessPixels(const NativePixelMap\* native)](#oh_pixelmap_unaccesspixels) | Unlocks the memory of a NativePixelMap object. This function is used with [OH\_PixelMap\_AccessPixels](#oh_pixelmap_accesspixels) in pairs. |

#### Enum Description

#### \[h2\]PixelMap Alpha Types

enum anonymous enum

**Description**

Enumerates the PixelMap alpha types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OHOS\_PIXEL\_MAP\_ALPHA\_TYPE\_UNKNOWN = 0 | Unknown format. |
| OHOS\_PIXEL\_MAP\_ALPHA\_TYPE\_OPAQUE = 1 | Opaque format. |
| OHOS\_PIXEL\_MAP\_ALPHA\_TYPE\_PREMUL = 2 | Premultiplied format. |
| OHOS\_PIXEL\_MAP\_ALPHA\_TYPE\_UNPREMUL = 3 | Unpremultiplied format. |

#### \[h2\]PixelMap Editing Types

enum anonymous enum

**Description**

Enumerates the PixelMap editing types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OHOS\_PIXEL\_MAP\_READ\_ONLY = 0 | Read-only. |
| OHOS\_PIXEL\_MAP\_EDITABLE = 1 | Editable. |

#### \[h2\]OH\_PixelMap\_AntiAliasingLevel

enum OH\_PixelMap\_AntiAliasingLevel

**Description**

Enumerates the anti-aliasing levels used for scaling PixelMaps.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| OH\_PixelMap\_AntiAliasing\_NONE = 0 | Nearest neighbor interpolation. |
| OH\_PixelMap\_AntiAliasing\_LOW = 1 | Bilinear interpolation. |
| OH\_PixelMap\_AntiAliasing\_MEDIUM = 2 | Bilinear interpolation with mipmap enabled. You are advised to use this value when zooming out an image. |
| OH\_PixelMap\_AntiAliasing\_HIGH = 3 | Cubic interpolation. |

#### Function Description

#### \[h2\]OH\_PixelMap\_CreatePixelMap()

int32\_t OH\_PixelMap\_CreatePixelMap(napi\_env env, OhosPixelMapCreateOps info,void\* buf, size\_t len, napi\_value\* res)

**Description**

Creates a PixelMap object. Currently, only BGRA input streams are supported.

The buffer passed in by this API does not support the stride.

This function does not support the DMA memory.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| [OhosPixelMapCreateOps](../../structs/ohospixelmapcreateops/document.md) info | Options for setting the PixelMap object. |
| void\* buf | Pointer to the buffer of the image. |
| size\_t len | Image size. |
| napi\_value\* res | Pointer to the PixelMap object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: The decoder fails to be created.

**IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED**: The encoder fails to be created.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_INIT\_ABNORMAL**: The image fails to be initialized.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_ENCODE\_FAILED**: The image fails to be encoded.

**IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT**: Hardware decoding is not supported.

**IMAGE\_RESULT\_HW\_DECODE\_FAILED**: Hardware decoding fails.

**IMAGE\_RESULT\_INDEX\_INVALID**: IPC fails.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_CreatePixelMapWithStride()

int32\_t OH\_PixelMap\_CreatePixelMapWithStride(napi\_env env, OhosPixelMapCreateOps info,void\* buf, size\_t len, int32\_t rowStride, napi\_value\* res)

**Description**

Creates a PixelMap object.

Currently, only BGRA input streams are supported. For a PixelMap in RGBA format (with the size greater than 512\*512), DMA memory is used by default.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| [OhosPixelMapCreateOps](../../structs/ohospixelmapcreateops/document.md) info | Options for setting the PixelMap object. |
| void\* buf | Pointer to the buffer of the image. |
| size\_t len | Buffer size. |
| int32\_t rowStride | Row stride. The stride is the actual memory size occupied by each row of the image, in bytes. Stride = Width \*Number of bytes per pixel + Padding, where padding refers to the extra space added at the end of each row for memory alignment purposes. |
| napi\_value\* res | Pointer to the PixelMap object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The attribute is invalid or the image data is not supported.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

 |

#### \[h2\]OH\_PixelMap\_CreateAlphaPixelMap()

int32\_t OH\_PixelMap\_CreateAlphaPixelMap(napi\_env env, napi\_value source, napi\_value\* alpha)

**Description**

Creates a PixelMap object that contains only alpha channel information.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| napi\_value source | PixelMap object at the application layer. |
| napi\_value\* alpha | Pointer to the alpha channel. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_DECODE\_HEAD\_ABNORMAL**: An error occurs during decoding of the image header.

**IMAGE\_RESULT\_CREATE\_DECODER\_FAILED**: The decoder fails to be created.

**IMAGE\_RESULT\_CREATE\_ENCODER\_FAILED**: The encoder fails to be created.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_DECODE\_ABNORMAL**: Image decoding fails.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_INIT\_ABNORMAL**: The image fails to be initialized.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_ENCODE\_FAILED**: The image fails to be encoded.

**IMAGE\_RESULT\_HW\_DECODE\_UNSUPPORT**: Hardware decoding is not supported.

**IMAGE\_RESULT\_HW\_DECODE\_FAILED**: Hardware decoding fails.

**IMAGE\_RESULT\_INDEX\_INVALID**: IPC fails.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_InitNativePixelMap()

NativePixelMap\* OH\_PixelMap\_InitNativePixelMap(napi\_env env, napi\_value source)

**Description**

Initializes a NativePixelMap object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| napi\_value source | PixelMap object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [NativePixelMap](../../structs/nativepixelmap/document.md)\* | Pointer to the NativePixelMap object. If the operation fails, an error code is returned. |

#### \[h2\]OH\_PixelMap\_GetBytesNumberPerRow()

int32\_t OH\_PixelMap\_GetBytesNumberPerRow(const NativePixelMap\* native, int32\_t\* num)

**Description**

Obtains the number of bytes per row of a NativePixelMap object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| int32\_t\* num | Pointer to the number of bytes per row. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

 |

#### \[h2\]OH\_PixelMap\_GetIsEditable()

int32\_t OH\_PixelMap\_GetIsEditable(const NativePixelMap\* native, int32\_t\* editable)

**Description**

Checks whether a NativePixelMap object is editable.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| int32\_t\* editable | Pointer to the editing type of the NativePixelMap object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

 |

#### \[h2\]OH\_PixelMap\_IsSupportAlpha()

int32\_t OH\_PixelMap\_IsSupportAlpha(const NativePixelMap\* native, int32\_t\* alpha)

**Description**

Checks whether a NativePixelMap object supports alpha channels.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| int32\_t\* alpha | Pointer to the support for alpha channels. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

 |

#### \[h2\]OH\_PixelMap\_SetAlphaAble()

int32\_t OH\_PixelMap\_SetAlphaAble(const NativePixelMap\* native, int32\_t alpha)

**Description**

Sets an alpha channel for a NativePixelMap object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| int32\_t alpha | Alpha channel to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

 |

#### \[h2\]OH\_PixelMap\_GetDensity()

int32\_t OH\_PixelMap\_GetDensity(const NativePixelMap\* native, int32\_t\* density)

**Description**

Obtains the pixel density of a NativePixelMap object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| int32\_t\* density | Pointer to the pixel density. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

 |

#### \[h2\]OH\_PixelMap\_SetDensity()

int32\_t OH\_PixelMap\_SetDensity(const NativePixelMap\* native, int32\_t density)

**Description**

Sets the pixel density for a NativePixelMap object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| int32\_t density | Pixel density to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

 |

#### \[h2\]OH\_PixelMap\_SetOpacity()

int32\_t OH\_PixelMap\_SetOpacity(const NativePixelMap\* native, float opacity)

**Description**

Sets the opacity for a NativePixelMap object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| float opacity | Opacity to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

 |

#### \[h2\]OH\_PixelMap\_Scale()

int32\_t OH\_PixelMap\_Scale(const NativePixelMap\* native, float x, float y)

**Description**

Scales a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Scale](../pixelmap-native-h/document.md#oh_pixelmapnative_scale) since API version 12.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| float x | Scale ratio of the width. |
| float y | Scale ratio of the height. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_INIT\_ABNORMAL**: The image fails to be initialized.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_ScaleWithAntiAliasing()

int32\_t OH\_PixelMap\_ScaleWithAntiAliasing(const NativePixelMap\* native, float x, float y,OH\_PixelMap\_AntiAliasingLevel level)

**Description**

Scales a NativePixelMap object based on the specified anti-aliasing level, width, and height.

You are advised to use the new function [OH\_PixelmapNative\_ScaleWithAntiAliasing](../pixelmap-native-h/document.md#oh_pixelmapnative_scalewithantialiasing) since API version 12.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| float x | Scale ratio of the width. |
| float y | Scale ratio of the height. |
| [OH\_PixelMap\_AntiAliasingLevel](#oh_pixelmap_antialiasinglevel) level | Anti-aliasing level. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

 |

#### \[h2\]OH\_PixelMap\_Translate()

int32\_t OH\_PixelMap\_Translate(const NativePixelMap\* native, float x, float y)

**Description**

Translates a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Translate](../pixelmap-native-h/document.md#oh_pixelmapnative_translate) since API version 12.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| float x | Horizontal distance to translate. |
| float y | Vertical distance to translate. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_Rotate()

int32\_t OH\_PixelMap\_Rotate(const NativePixelMap\* native, float angle)

**Description**

Rotates a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Rotate](../pixelmap-native-h/document.md#oh_pixelmapnative_rotate) since API version 12.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| float angle | Angle to rotate. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_Flip()

int32\_t OH\_PixelMap\_Flip(const NativePixelMap\* native, int32\_t x, int32\_t y)

**Description**

Flips a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Flip](../pixelmap-native-h/document.md#oh_pixelmapnative_flip) since API version 12.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| int32\_t x | Whether to flip around the x axis. |
| int32\_t y | Whether to flip around the y axis. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_Crop()

int32\_t OH\_PixelMap\_Crop(const NativePixelMap\* native, int32\_t x, int32\_t y, int32\_t width, int32\_t height)

**Description**

Crops a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_Crop](../pixelmap-native-h/document.md#oh_pixelmapnative_crop) since API version 12.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| int32\_t x | X-coordinate of the upper left corner of the target image. |
| int32\_t y | Y-coordinate of the upper left corner of the target image. |
| int32\_t width | Width of the cropped region. |
| int32\_t height | Height of the cropped region. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_GetImageInfo()

int32\_t OH\_PixelMap\_GetImageInfo(const NativePixelMap\* native, OhosPixelMapInfos \*info)

**Description**

Obtains the image information of a NativePixelMap object.

You are advised to use the new function [OH\_PixelmapNative\_GetImageInfo](../pixelmap-native-h/document.md#oh_pixelmapnative_getimageinfo) since API version 12.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| [OhosPixelMapInfos](../../structs/ohospixelmapinfos/document.md) \*info | Pointer to the image information. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_AccessPixels()

int32\_t OH\_PixelMap\_AccessPixels(const NativePixelMap\* native, void\*\* addr)

**Description**

Obtains the memory address of a NativePixelMap object and locks the memory.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |
| void\*\* addr | Double pointer to the memory address. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |

#### \[h2\]OH\_PixelMap\_UnAccessPixels()

int32\_t OH\_PixelMap\_UnAccessPixels(const NativePixelMap\* native)

**Description**

Unlocks the memory of a NativePixelMap object. This function is used with [OH\_PixelMap\_AccessPixels](#oh_pixelmap_accesspixels) in pairs.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const [NativePixelMap](../../structs/nativepixelmap/document.md)\* native | Pointer to a NativePixelMap object. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Result code defined in [IRNdkErrCode](../image-mdk-common-h/document.md#irndkerrcode):

**IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**IMAGE\_RESULT\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_RESULT\_JNI\_ENV\_ABNORMAL**: The JNI environment is abnormal.

**IMAGE\_RESULT\_INVALID\_PARAMETER**: A parameter is invalid.

**IMAGE\_RESULT\_GET\_DATA\_ABNORMAL**: An error occurs during image data retrieval.

**IMAGE\_RESULT\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_RESULT\_CHECK\_FORMAT\_ERROR**: The format check fails.

**IMAGE\_RESULT\_THIRDPART\_SKIA\_ERROR**: Skia decoding fails.

**IMAGE\_RESULT\_DATA\_ABNORMAL**: The image input data is incorrect.

**IMAGE\_RESULT\_ERR\_SHAMEM\_NOT\_EXIST**: Sharing the memory fails.

**IMAGE\_RESULT\_ERR\_SHAMEM\_DATA\_ABNORMAL**: Data in the shared memory is incorrect.

**IMAGE\_RESULT\_MALLOC\_ABNORMAL**: An error occurs during memory allocation.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: The image data is not supported.

**IMAGE\_RESULT\_CROP**: Cropping fails.

**IMAGE\_RESULT\_UNKNOWN\_FORMAT**: The image format is unknown.

**IMAGE\_RESULT\_PLUGIN\_REGISTER\_FAILED**: The plugin fails to be registered.

**IMAGE\_RESULT\_PLUGIN\_CREATE\_FAILED**: The plugin fails to be created.

**IMAGE\_RESULT\_DATA\_UNSUPPORT**: A property is invalid.

**IMAGE\_RESULT\_ALPHA\_TYPE\_ERROR**: The alpha type is incorrect.

**IMAGE\_RESULT\_ALLOCATER\_TYPE\_ERROR**: The memory allocator type is incorrect.

 |
