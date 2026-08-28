# OhosImageDecodingOps

struct OhosImageDecodingOps {...}

#### Overview

The struct describes the options for decoding an image source. It is used in [OH\_ImageSource\_CreatePixelMap](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createpixelmap) and [OH\_ImageSource\_CreatePixelMapList](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createpixelmaplist).

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_source\_mdk.h](../../header-files/image-source-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int8\_t editable | Whether the output PixelMap is editable. |
| int32\_t pixelFormat | Pixel format of the output PixelMap. |
| int32\_t fitDensity | Pixel density of the output PixelMap. |
| uint32\_t index | Index for decoding the image source. |
| uint32\_t sampleSize | Size of the sample. |
| uint32\_t rotate | Decoding rotation options. |
| struct [OhosImageSize](../ohosimagesize/document.md) size | Pixel width and height of the output PixelMap. |
| struct [OhosImageRegion](../ohosimageregion/document.md) region | Pixel range of the decoded image source. |
