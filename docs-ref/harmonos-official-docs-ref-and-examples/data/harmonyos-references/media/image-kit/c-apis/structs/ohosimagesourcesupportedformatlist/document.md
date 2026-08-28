# OhosImageSourceSupportedFormatList

struct OhosImageSourceSupportedFormatList {...}

#### Overview

The struct defines the format string list supported by an image source. It is obtained by calling [OH\_ImageSource\_GetSupportedFormats](../../header-files/image-source-mdk-h/document.md#oh_imagesource_getsupportedformats).

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_source\_mdk.h](../../header-files/image-source-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| struct [OhosImageSourceSupportedFormat](../ohosimagesourcesupportedformat/document.md)\*\* supportedFormatList = nullptr | Double pointer to the starting address of the format string list. |
| size\_t size = 0 | Size of the format string list. |
