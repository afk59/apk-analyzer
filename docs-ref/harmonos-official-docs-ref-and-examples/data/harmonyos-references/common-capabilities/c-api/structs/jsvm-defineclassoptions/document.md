# JSVM\_DefineClassOptions

typedef struct {...} JSVM\_DefineClassOptions

#### Overview

Defines the options of a class.

**Since**: 18

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [JSVM\_DefineClassOptionsId](../../header-files/jsvm-types-h/document.md#jsvm_defineclassoptionsid) id | Option ID of a class. |
| content | Union of the option value of a class corresponding to the ID. |
| content.ptr | Pointer to the class option value. |
| content.num | Used to store the class option value of the integer type. |
| content.boolean | Used to store the class option value of the Boolean type. |
