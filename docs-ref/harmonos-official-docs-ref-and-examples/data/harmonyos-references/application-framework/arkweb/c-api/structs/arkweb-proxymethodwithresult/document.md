# ArkWeb\_ProxyMethodWithResult

typedef struct {...} ArkWeb\_ProxyMethodWithResult

#### Overview

Defines a proxy method to be injected.

**Since**: 18

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Total

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* methodName | Pointer to the method name to be injected. |
| [ArkWeb\_OnJavaScriptProxyCallbackWithResult](../../header-files/arkweb-type-h/document.md#arkweb_onjavascriptproxycallbackwithresult) callback | Callback used when a proxy method is invoked. |
| void\* userData | Pointer to the user data used in a callback. |
