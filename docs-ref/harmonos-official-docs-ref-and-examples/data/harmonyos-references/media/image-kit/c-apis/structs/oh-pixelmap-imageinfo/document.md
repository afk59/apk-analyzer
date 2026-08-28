# OH\_Pixelmap\_ImageInfo

struct OH\_Pixelmap\_ImageInfo

#### Overview

The OH\_Pixelmap\_ImageInfo struct describes the image information encapsulated at the native layer. The struct stores the width, height, row stride, pixel format, and HDR of an image.

To create an OH\_Pixelmap\_ImageInfo object, call [OH\_PixelmapImageInfo\_Create](../../header-files/pixelmap-native-h/document.md#oh_pixelmapimageinfo_create).

To release an OH\_Pixelmap\_ImageInfo object, call [OH\_PixelmapImageInfo\_Release](../../header-files/pixelmap-native-h/document.md#oh_pixelmapimageinfo_release).

The table below describes the content and operation mode of the OH\_Pixelmap\_ImageInfo struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| uint32\_t | width | Image width. | [OH\_PixelmapImageInfo\_GetWidth](../../header-files/pixelmap-native-h/document.md#oh_pixelmapimageinfo_getwidth) | Obtains the image width. |
| uint32\_t | height | Image height. | [OH\_PixelmapImageInfo\_GetHeight](../../header-files/pixelmap-native-h/document.md#oh_pixelmapimageinfo_getheight) | Obtains the image height. |
| uint32\_t | rowStride | Row stride. | [OH\_PixelmapImageInfo\_GetRowStride](../../header-files/pixelmap-native-h/document.md#oh_pixelmapimageinfo_getrowstride) | Obtains the row stride. |
| int32\_t | pixelFormat | Pixel format. | [OH\_PixelmapImageInfo\_GetPixelFormat](../../header-files/pixelmap-native-h/document.md#oh_pixelmapimageinfo_getpixelformat) | Obtains the pixel format. |
| int32\_t | alphaType | Alpha type. | [OH\_PixelmapImageInfo\_GetAlphaType](../../header-files/pixelmap-native-h/document.md#oh_pixelmapimageinfo_getalphatype) | Obtains the alpha type. |
| bool | isHdr | Whether the image is an HDR image. | [OH\_PixelmapImageInfo\_GetDynamicRange](../../header-files/pixelmap-native-h/document.md#oh_pixelmapimageinfo_getdynamicrange) | Obtains information about whether the PixelMap is an HDR image. |

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [pixelmap\_native.h](../../header-files/pixelmap-native-h/document.md)
