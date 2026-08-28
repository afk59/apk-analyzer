# OH\_NativeBuffer\_Planes

typedef struct {...} OH\_NativeBuffer\_Planes

#### Overview

This struct describes the plane information of images in an **OH\_NativeBuffer** instance.

**Since**: 12

**Related module**: [OH\_NativeBuffer](../../modules/oh-nativebuffer/document.md)

**Header file**: [native\_buffer.h](../../header-files/native-buffer-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t planeCount | Number of planes. |
| [OH\_NativeBuffer\_Plane](../oh-nativebuffer-plane/document.md) planes\[4\] | Array holding the plane information of each image. |
