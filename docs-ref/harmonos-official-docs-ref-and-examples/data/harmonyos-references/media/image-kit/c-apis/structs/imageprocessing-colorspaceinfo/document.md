# ImageProcessing\_ColorSpaceInfo

typedef struct ImageProcessing\_ColorSpaceInfo {...} ImageProcessing\_ColorSpaceInfo

#### Overview

The struct describes the color space information, which is used in Color Space Conversion (CSC) capability query.

**See also**

[OH\_ImageProcessing\_IsColorSpaceConversionSupported](../../header-files/image-processing-h/document.md#oh_imageprocessing_iscolorspaceconversionsupported), [OH\_ImageProcessing\_IsCompositionSupported](../../header-files/image-processing-h/document.md#oh_imageprocessing_iscompositionsupported), [OH\_ImageProcessing\_IsDecompositionSupported](../../header-files/image-processing-h/document.md#oh_imageprocessing_isdecompositionsupported)

**Since**: 13

**Related module**: [ImageProcessing](../../modules/imageprocessing/document.md)

**Header file**: [image\_processing\_types.h](../../header-files/image-processing-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t metadataType | Metadata type. For details, see [OH\_Pixelmap\_HdrMetadataKey](../../header-files/pixelmap-native-h/document.md#oh_pixelmap_hdrmetadatakey). |
| int32\_t colorSpace | Color space. For details, see [ColorSpaceName](../../../../../graphics/arkgraphics-2d/c-apis/header-files/native-color-space-manager-h/document.md#colorspacename). |
| int32\_t pixelFormat | Pixel format. For details, see [PIXEL\_FORMAT](../../header-files/pixelmap-native-h/document.md#pixel_format). |
