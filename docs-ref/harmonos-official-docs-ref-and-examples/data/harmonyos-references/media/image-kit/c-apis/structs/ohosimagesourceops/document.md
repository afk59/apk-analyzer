# OhosImageSourceOps

struct OhosImageSourceOps {...}

#### Overview

The struct describes the image source options. It is used in [OH\_ImageSource\_CreateFromUri](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromuri), [OH\_ImageSource\_CreateFromFd](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromfd), [OH\_ImageSource\_CreateFromData](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromdata), and [OH\_ImageSource\_CreateIncremental](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createincremental).

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_source\_mdk.h](../../header-files/image-source-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t density | Pixel density of the image source. |
| int32\_t pixelFormat | Pixel format of the image source. It is usually used to describe the YUV buffer. |
| struct [OhosImageSize](../ohosimagesize/document.md) size | Pixel width and height of the image source. |
