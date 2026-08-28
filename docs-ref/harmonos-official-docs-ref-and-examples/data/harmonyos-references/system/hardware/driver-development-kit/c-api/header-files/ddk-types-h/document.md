# ddk\_types.h

#### Overview

Provides BASE DDK types and declares the macros, enums, and data structures required by the BASE DDK APIs.

**Header file:** <ddk/ddk\_types.h>

**Library**: libddk\_base.z.so

**System capability**: SystemCapability.Driver.DDK.Extension

**Since**: 12

**Related module**: [Ddk](../../modules/baseddk/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DDK\_Ashmem](../../structs/ddk-ashmem/document.md) | DDK\_Ashmem | Device memory map created by calling **OH\_DDK\_CreateAshmem**. A buffer using the device memory map can provide better performance. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DDK\_RetCode](#ddk_retcode) | DDK\_RetCode | Enumerates error codes used in the BASE DDK. |

#### Enum Description

#### \[h2\]DDK\_RetCode

enum DDK\_RetCode

**Description**

Enumerates error codes used in the BASE DDK.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| DDK\_SUCCESS = 0 | Operation success. |
| DDK\_FAILURE = 28600001 | Operation failed. |
| DDK\_INVALID\_PARAMETER = 28600002 | Invalid parameter. |
| DDK\_INVALID\_OPERATION = 28600003 | Invalid operation. |
| DDK\_NULL\_PTR = 28600004 | Null pointer. |
