# OH\_PixelmapNative

struct OH\_PixelmapNative

#### Overview

The OH\_PixelmapNative struct describes an uncompressed PixelMap format, which is encapsulated at the native layer after images are decoded.

To create an OH\_PixelmapNative object, call [OH\_PixelmapNative\_CreatePixelmap](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_createpixelmap). By default, BGRA\_8888 is used for data processing.

To release an OH\_PixelmapNative object, call [OH\_PixelmapNative\_Release](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_release).

The table below describes the content and operation mode of the OH\_PixelmapNative struct.

| Field Type | Field Name | Field Description | Operation Function | Function Description |
| :-- | :-- | :-- | :-- | :-- |
| uint8\_t | data | Image pixel data. | [OH\_PixelmapNative\_ReadPixels](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_readpixels) | Reads the pixels of a PixelMap and writes the result to an ArrayBuffer. |
| uint8\_t | data | Image pixel data. | [OH\_PixelmapNative\_WritePixels](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_writepixels) | Reads the pixel data in the buffer and writes the result to a PixelMap. |
| OH\_Pixelmap\_ImageInfo | imageInfo | Image information. | [OH\_PixelmapNative\_GetImageInfo](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_getimageinfo) | Obtains the image information of a PixelMap. |
| float | alphaRate | Opacity. | [OH\_PixelmapNative\_Opacity](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_opacity) | Sets the opacity rate to enable the PixelMap to achieve the corresponding opacity effect. |
| float, float | scaleX, scaleY | Scale ratios along the X axis and Y axis, respectively. | [OH\_PixelmapNative\_Scale](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_scale) | Scales a PixelMap based on a given width and height. |
| float, float | x, y | Distances to translate along the X axis and Y axis, respectively. | [OH\_PixelmapNative\_Translate](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_translate) | Translates a PixelMap based on given coordinates. |
| float | angle | Rotation angle. | [OH\_PixelmapNative\_Rotate](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_rotate) | Rotates a PixelMap based on a given angle. |
| bool, bool | shouldFlipHorizontally, shouldFlipVertically | Whether the PixelMap is flipped horizontally or vertically. | [OH\_PixelmapNative\_Flip](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_flip) | Flips a PixelMap based on a given angle. |
| Image\_Region | region | Cropping region. | [OH\_PixelmapNative\_Crop](../../header-files/pixelmap-native-h/document.md#oh_pixelmapnative_crop) | Crops a PixelMap based on a given size. |

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [pixelmap\_native.h](../../header-files/pixelmap-native-h/document.md)
