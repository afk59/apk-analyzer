# JSVM\_PropertyDescriptor

typedef struct {...} JSVM\_PropertyDescriptor

#### Overview

Defines property descriptor.

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* utf8name | Property key, which is an optional string in UTF-8 encoding. Either **utf8name** or **name** must be provided for a property. |
| [JSVM\_Value](../jsvm-value/document.md) name | Optional JSVM value, which points to the JavaScript string or symbol used as the property key. Either **utf8name** or **name** must be provided for a property. |
| [JSVM\_Callback](../jsvm-callbackstruct--00020177/document.md) method | Method represented using the **value** property of the property descriptor object. |
| [JSVM\_Callback](../jsvm-callbackstruct--00020177/document.md) getter | Callback used to obtain a property. |
| [JSVM\_Callback](../jsvm-callbackstruct--00020177/document.md) setter | Callback used to set a property. |
| [JSVM\_Value](../jsvm-value/document.md) value | Value retrieved by **getter** of the data property. |
| [JSVM\_PropertyAttributes](../../header-files/jsvm-types-h/document.md#jsvm_propertyattributes) attributes | Attributes associated with a specific property. |
