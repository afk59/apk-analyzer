# JSVM\_VMInfo

typedef struct {...} JSVM\_VMInfo

#### Overview

Defines the JavaScript VM information.

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t apiVersion | The latest API version supported by the VM. |
| const char\* engine | Name of the engine that implements the VM. |
| const char\* version | VM version. |
| uint32\_t cachedDataVersionTag | Cache data version tag. |
