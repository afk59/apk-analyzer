# OhosImageSourceUpdateData

struct OhosImageSourceUpdateData {...}

#### Overview

The struct describes the update data option of the image source. It is obtained by calling [OH\_ImageSource\_UpdateData](../../header-files/image-source-mdk-h/document.md#oh_imagesource_updatedata).

**Since**: 10

**Related module**: [Image](../../modules/image/document.md)

**Header file**: [image\_source\_mdk.h](../../header-files/image-source-mdk-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t\* buffer = nullptr | Pointer to the buffer for storing the update data. |
| size\_t bufferSize = 0 | Size of the buffer. |
| uint32\_t offset = 0 | Offset of the update data in the buffer. |
| uint32\_t updateLength = 0 | Length of the update data in the buffer. |
| int8\_t isCompleted = 0 | Whether the image source data update is completed. |
