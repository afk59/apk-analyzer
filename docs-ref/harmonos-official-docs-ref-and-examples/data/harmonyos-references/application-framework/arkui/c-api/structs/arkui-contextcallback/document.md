# ArkUI\_ContextCallback

typedef struct {...} ArkUI\_ContextCallback

#### Overview

Defines the event callback type.

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_type.h](../../header-files/native-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| void\* userData | Custom type. The data of the custom type is passed as a parameter during callback. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [void (\*callback)(void\* userData)](#callback) | Event callback. |

#### Member Function Description

#### \[h2\]callback()

void (\*callback)(void\* userData)

**Description**

Event callback.
