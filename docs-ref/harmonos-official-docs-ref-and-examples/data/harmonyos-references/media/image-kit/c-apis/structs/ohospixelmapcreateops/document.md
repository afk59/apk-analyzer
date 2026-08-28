# OhosPixelMapCreateOps

struct OhosPixelMapCreateOps {...}

#### Overview

The struct describes the options used for creating a PixelMap.

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_pixel\_map\_mdk.h](../../header-files/image-pixel-map-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t width | Image width, in pixels. |
| uint32\_t height | Image height, in pixels. |
| int32\_t pixelFormat | 
Image format. The options are as follows:

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
| uint32\_t editable | Editing type of the image. The value **true** means that the image pixel can be edited, and **false** means the opposite. |
| uint32\_t alphaType | 

Alpha type of the image. The options are as follows:

**0**: Unknown alpha type.

**1**: There is no alpha or the image is opaque.

**2**: Premultiplied format.

**3**: Non-premultiplied format.

 |
| uint32\_t scaleMode | 

Scale mode of the image. The options are as follows:

**1**: The image is scaled in such a way that it fits the dimensions of the target and centered in the target.

**0**: The image size is reduced to fit the dimensions of the target.

 |
