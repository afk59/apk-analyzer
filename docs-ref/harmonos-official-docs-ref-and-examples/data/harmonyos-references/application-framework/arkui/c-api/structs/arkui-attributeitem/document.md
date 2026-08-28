# ArkUI\_AttributeItem

typedef struct {...} ArkUI\_AttributeItem

#### Overview

Defines the general input parameter structure of the [setAttribute](../arkui-nativenodeapi-1/document.md#setattribute) function. Individual attribute-setting API can use appropriate member variables within it to store parameter data of specific types.

**Since**: 12

**Related module**: [ArkUI\_NativeModule](../../modules/arkui-nativemodule/document.md)

**Header file**: [native\_node.h](../../header-files/native-node-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const [ArkUI\_NumberValue](../arkui-numbervalue/document.md)\* value | Numeric array, used to store parameters of the numeric array type. |
| int32\_t size | Size of the numeric array. Used in conjunction with the **value** variable, it indicates the length of the **value** array. |
| const char\* string | String, used to store parameters of the string type. |
| void\* object | Object pointer, used to store parameters of the object type. |
