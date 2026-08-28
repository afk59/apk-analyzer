# OhosImageSourceInfo

struct OhosImageSourceInfo {...}

#### Overview

The struct describes the image source information, which is obtained by calling [OH\_ImageSource\_GetImageInfo](../../header-files/image-source-mdk-h/document.md#oh_imagesource_getimageinfo).

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_source\_mdk.h](../../header-files/image-source-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t pixelFormat | Pixel format of the image source. It is set by calling [OH\_ImageSource\_CreateFromUri](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromuri), [OH\_ImageSource\_CreateFromFd](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromfd), or [OH\_ImageSource\_CreateFromData](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromdata). |
| int32\_t colorSpace | Color space of the image source. |
| int32\_t alphaType | Alpha type of the image source. |
| int32\_t density | Image density of the image source. It is set by calling [OH\_ImageSource\_CreateFromUri](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromuri), [OH\_ImageSource\_CreateFromFd](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromfd), or [OH\_ImageSource\_CreateFromData](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromdata). |
| struct [OhosImageSize](../ohosimagesize/document.md) size | Pixel width and height of the image source. |
