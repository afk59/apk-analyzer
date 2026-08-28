# OhosImageSourceProperty

struct OhosImageSourceProperty {...}

#### Overview

The struct describes the property string (in key-value format) of an image source. It is used in [OH\_ImageSource\_GetImageProperty](../../header-files/image-source-mdk-h/document.md#oh_imagesource_getimageproperty) and [OH\_ImageSource\_ModifyImageProperty](../../header-files/image-source-mdk-h/document.md#oh_imagesource_modifyimageproperty).

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_source\_mdk.h](../../header-files/image-source-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char\* value = nullptr | Pointer to the starting address of the property string. |
| size\_t size = 0 | Size of the property string. |
