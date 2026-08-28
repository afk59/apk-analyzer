# DDK\_Ashmem

typedef struct DDK\_Ashmem {...} DDK\_Ashmem

#### Overview

Device memory map created by calling **OH\_DDK\_CreateAshmem**. A buffer using the device memory map can provide better performance.

**Since**: 12

**Related module**: [BaseDdk](../../modules/baseddk/document.md)

**Header file:** [ddk\_types.h](../../header-files/ddk-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t ashmemFd | File descriptor of the **Ashmem** object. |
| const uint8\_t\* address | Buffer address. |
| const uint32\_t size | Buffer size. |
| uint32\_t offset | Offset of the used buffer. The default value is **0**, indicating that there is no offset and the buffer starts from the specified address. |
| uint32\_t bufferLength | Length of the buffer. By default, the value is equal to that of **size**, indicating that the entire buffer is used. |
| uint32\_t transferredLength | Length of the transferred data. |
