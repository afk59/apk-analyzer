# ArkWeb\_JavaScriptObject

typedef struct {...} ArkWeb\_JavaScriptObject

#### Overview

Defines a JavaScript object.

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const uint8\_t\* buffer | Pointer to the injected JavaScript code. |
| size\_t size | Length of the JavaScript code. |
| [ArkWeb\_OnJavaScriptCallback](../../header-files/arkweb-type-h/document.md#arkweb_onjavascriptcallback) callback | Callback used when JavaScript execution is complete. |
| void\* userData | Pointer to the user data used in a callback. |
