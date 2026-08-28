# OhosImageSourceSupportedFormat

struct OhosImageSourceSupportedFormat {...}

#### Overview

The struct describes the format string supported by an image source. It is used in [OhosImageSourceSupportedFormatList](../ohosimagesourcesupportedformatlist/document.md) and [OH\_ImageSource\_GetSupportedFormats](../../header-files/image-source-mdk-h/document.md#oh_imagesource_getsupportedformats).

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_source\_mdk.h](../../header-files/image-source-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* format = nullptr | Pointer to the starting address of the format string. |
| size\_t size = 0 | Size of the format string. |
