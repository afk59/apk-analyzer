# OH\_NativeBuffer\_Config

typedef struct {...} OH\_NativeBuffer\_Config

#### Overview

The **OH\_NativeBuffer\_Config** struct describes the **OH\_NativeBuffer** attribute configuration, which is used when you apply for a new **OH\_NativeBuffer** instance or query the attributes of an existing instance.

**Since**: 9

**Related module**: [OH\_NativeBuffer](../../modules/oh-nativebuffer/document.md)

**Header file**: [native\_buffer.h](../../header-files/native-buffer-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t width | Width, in pixels. |
| int32\_t height | Height, in pixels. |
| int32\_t format | Pixel format. For details about the available options, see [OH\_NativeBuffer\_Format](../../header-files/buffer-common-h/document.md#oh_nativebuffer_format). |
| int32\_t usage | Usage of the buffer. For details about the available options, see [OH\_NativeBuffer\_Usage](../../header-files/native-buffer-h/document.md#oh_nativebuffer_usage). |
| int32\_t stride | 
Double pointer to the image processing instance created. Stride of the local window buffer, in bytes.

**Since**: 10

 |
