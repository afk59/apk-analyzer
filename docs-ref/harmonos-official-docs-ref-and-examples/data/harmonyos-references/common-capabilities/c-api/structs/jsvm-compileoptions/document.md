# JSVM\_CompileOptions

typedef struct {...} JSVM\_CompileOptions

#### Overview

Defines a struct that represents the type of the elements in **options** of [OH\_JSVM\_CompileScriptWithOptions](../../header-files/jsvm-h/document.md#oh_jsvm_compilescriptwithoptions).

**Since**: 12

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [JSVM\_CompileOptionId](../../header-files/jsvm-types-h/document.md#jsvm_compileoptionid) id | Compilation option ID. |
| content | Union of the compilation option value corresponding to the ID. |
| content.ptr | Pointer to the compilation option value. |
| content.num | Used to store the compilation option value of the integer type. |
| content.boolean | Used to store the compilation option value of the Boolean type. |
