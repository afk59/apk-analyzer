# OH\_NativeBuffer\_Plane

typedef struct {...} OH\_NativeBuffer\_Plane

#### Overview

This struct describes the plane information of an image.

**Since**: 12

**Related module**: [OH\_NativeBuffer](../../modules/oh-nativebuffer/document.md)

**Header file**: [native\_buffer.h](../../header-files/native-buffer-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t offset | Offset of the image plane, in bytes. |
| uint32\_t rowStride | Distance from the first value in an image row to the first value in the next row, in bytes. |
| uint32\_t columnStride | Distance from the first value in an image column to the first value in the next column, in bytes. |
