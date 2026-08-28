# BufferHandle

typedef struct {...} BufferHandle

#### Overview

Describes the buffer handle, which is used to transfer and obtain buffer information. The handle contains the file descriptor, size, format, usage, virtual address, shared memory key, physical address, and custom data of the buffer.

**Since**: 8

**Related module**: [NativeWindow](../../modules/nativewindow/document.md)

**Header file**: [buffer\_handle.h](../../header-files/buffer-handle-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t fd | File descriptor of the buffer. The value **\-1** means that the buffer is not supported. |
| int32\_t width | Width of the buffer memory, in pixels. |
| int32\_t stride | Stride of the buffer memory, in bytes. |
| int32\_t height | Height of the buffer memory, in pixels. |
| int32\_t size | Size of the buffer memory, in bytes. |
| int32\_t format | Format of the buffer memory. For details about the available options, see [OH\_NativeBuffer\_Format](../../header-files/buffer-common-h/document.md#oh_nativebuffer_format). |
| uint64\_t usage | Usage of the buffer memory, represented as bit flags. For details about the available options, see [OH\_NativeBuffer\_Format](../../header-files/buffer-common-h/document.md#oh_nativebuffer_format). |
| void\* virAddr | Virtual address of the buffer memory. |
| int32\_t key | Shared memory key of the buffer memory. |
| uint64\_t phyAddr | Physical address of the buffer memory. |
| uint32\_t reserveFds | Number of file descriptors for extra data. |
| uint32\_t reserveInts | Number of integer values for extra data. |
| int32\_t reserve\[0\] | Extra data. |
