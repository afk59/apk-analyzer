# OhosPixelMapInfo

struct OhosPixelMapInfo {...}

#### Overview

The struct describes the information about a PixelMap.

**Since**: 8

**Deprecated from**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_pixel\_map\_napi.h](../../header-files/image-pixel-map-napi-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t width | Image width, in pixels. |
| uint32\_t height | Image height, in pixels. |
| uint32\_t rowSize | 
Number of bytes that each row of the image occupies in the memory.

In the case of DMA, the formula is as follows: Image width \* Number of bytes of each pixel + Number of padding bytes at the end of each row. In the case of other types of memory, the formula is as follows: Image width \* Number of bytes of each pixel.

 |
| int32\_t pixelFormat | 

Pixel format. The options are as follows:

**0**: Unknown format.

**2**: RGB\_565.

**3**: RGBA\_8888.

**4**: BGRA\_8888.

**5**: RGB\_888.

**6**: ALPHA\_8.

**7**: RGBA\_F16.

**8**: NV21.

**9**: NV12.

 |
