# Image\_Region

struct Image\_Region {...}

#### Overview

The struct describes the region of an image to decode.

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

**Header file**: [image\_common.h](../../header-files/image-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t x | X coordinate of the region. It cannot be greater than the width of the original image. |
| uint32\_t y | Y coordinate of the region. It cannot be greater than the height of the original image. |
| uint32\_t width | Width of the output image, in px. |
| uint32\_t height | Height of the output image, in px. |
