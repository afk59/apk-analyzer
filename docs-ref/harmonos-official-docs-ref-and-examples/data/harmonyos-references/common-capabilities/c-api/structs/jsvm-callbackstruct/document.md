# JSVM\_CallbackStruct

typedef struct {...} JSVM\_CallbackStruct

#### Overview

Defines the pointer to the data of the native callbacks provided by the user. These functions are exposed to JavaScript via JSVM-API.

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| void\* data | Data of the native callbacks provided by the user. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [JSVM\_Value(JSVM\_CDECL\* callback)(JSVM\_Env env,JSVM\_CallbackInfo info)](#callback) | Defines a pointer to the native callback provided by users. |

#### Member Function Description

#### \[h2\]callback()

JSVM\_Value(JSVM\_CDECL\* callback)(JSVM\_Env env,JSVM\_CallbackInfo info)

**Description**

Defines a pointer to the native callback provided by users.
