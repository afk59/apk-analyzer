# ArkWeb\_JavaScriptValueAPI

typedef struct {...} ArkWeb\_JavaScriptValueAPI

#### Overview

Defines the JavaScriptValue API of ArkWeb. Before calling this API, you are advised to use [ARKWEB\_MEMBER\_MISSING](../../header-files/arkweb-type-h/document.md#macros) to check whether the function struct has the corresponding pointer to avoid crash caused by mismatch between the SDK and the device ROM.

**Since**: 18

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| size\_t size | Size of the struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [ArkWeb\_JavaScriptValuePtr (\*createJavaScriptValue)(ArkWeb\_JavaScriptValueType type, void\* data, size\_t dataLength)](#createjavascriptvalue) | Creates a JavaScript value to be returned to HTML. |

#### Member Function Description

#### \[h2\]createJavaScriptValue()

ArkWeb\_JavaScriptValuePtr (\*createJavaScriptValue)(ArkWeb\_JavaScriptValueType type, void\* data, size\_t dataLength)

**Description**

Creates a JavaScript value to be returned to HTML.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| ArkWeb\_JavaScriptValueType type | Type of the JavaScript value. |
| void\* data | Pointer to the JavaScript value data. |
| size\_t dataLength | Length of the JavaScript value data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ArkWeb\_JavaScriptValuePtr](../arkweb-javascriptvalue/document.md) | Created JavaScript value. |
