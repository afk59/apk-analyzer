# OhosImageSource

struct OhosImageSource {...}

#### Overview

The struct describes the input resource of an image source. Only one type of resource is accepted at a time. The image source is obtained by calling [OH\_ImageSource\_CreateFromUri](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromuri), [OH\_ImageSource\_CreateFromFd](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromfd), or [OH\_ImageSource\_CreateFromData](../../header-files/image-source-mdk-h/document.md#oh_imagesource_createfromdata).

**Since**: 10

**Deprecated from**: 11

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_source\_mdk.h](../../header-files/image-source-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* uri = nullptr | Pointer to the image source URI. Only a file URI or Base64 URI is accepted. |
| size\_t uriSize = 0 | Length of the image source URI. |
| int32\_t fd = - 1 | Descriptor of the image source. |
| uint8\_t\* buffer = nullptr | Pointer to the image source buffer. Only a formatted packet buffer or Base64 buffer is accepted. |
| size\_t bufferSize = 0 | Size of the image source buffer. |
