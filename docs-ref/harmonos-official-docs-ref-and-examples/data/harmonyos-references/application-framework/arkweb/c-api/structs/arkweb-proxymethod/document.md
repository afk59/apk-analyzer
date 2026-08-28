# ArkWeb\_ProxyMethod

typedef struct {...} ArkWeb\_ProxyMethod

#### Overview

Defines a proxy method to be injected.

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* methodName | Pointer to the method name to be injected. |
| [ArkWeb\_OnJavaScriptProxyCallback](../../header-files/arkweb-type-h/document.md#arkweb_onjavascriptproxycallback) callback | Callback used when a proxy method is executed. |
| void\* userData | Pointer to the user data used in a callback. |
