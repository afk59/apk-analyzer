# Image\_PositionArea

typedef struct Image\_PositionArea {...} Image\_PositionArea

#### Overview

The struct describes the area of image pixels to be read from or written to.

**Since**: 22

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_common.h](../../header-files/image-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t \*pixels | Pointer to the image pixel data for reading or writing. Only pixel data in the BRGA\_8888 format is supported. |
| size\_t pixelsSize | Length of the pixel data, in bytes. |
| uint32\_t offset | Offset for reading or writing data, in bytes. |
| uint32\_t stride | Stride of the region, that is, the number of bytes occupied by each row of pixels. The value of **stride** must be greater than or equal to the value of **region.size.width** multiplied by 4. |
| [Image\_Region](../image-region/document.md) region | Area for reading or writing. The region's width plus the X coordinate must not exceed the original image's width, and the region's height plus the Y coordinate must not exceed the original image's height. |
