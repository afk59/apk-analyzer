# JSVM\_ExtendedErrorInfo

typedef struct {...} JSVM\_ExtendedErrorInfo

#### Overview

Defines extended error information.

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* errorMessage | UTF-8-encoded string, which contains error messages. |
| void\* engineReserved | Detailed error message specific to a VM. This feature is not implemented for any VM yet. |
| uint32\_t engineErrorCode | Error code specific to a VM. This feature is not implemented for any VM yet. |
| JSVM\_Status errorCode | JSVM-API status code derived from the last error. |
