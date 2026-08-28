# ArkWeb\_ProxyObjectWithResult

typedef struct {...} ArkWeb\_ProxyObjectWithResult

#### Overview

Defines a proxy object to be injected.

**Since**: 18

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Total

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* objName | Pointer to the object name to be injected. |
| const [ArkWeb\_ProxyMethodWithResult](../arkweb-proxymethodwithresult/document.md)\* methodList | Pointer to the method struct array of an object to be injected. |
| size\_t size | Length of the method struct array. |
