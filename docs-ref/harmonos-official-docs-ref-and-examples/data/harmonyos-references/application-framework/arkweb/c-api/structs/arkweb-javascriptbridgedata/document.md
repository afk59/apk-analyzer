# ArkWeb\_JavaScriptBridgeData

typedef struct {...} ArkWeb\_JavaScriptBridgeData

#### Overview

Defines the JavaScript Bridge data.

**Since**: 12

**Related module**: [Web](../../modules/web/document.md)

**Header file**: [arkweb\_type.h](../../header-files/arkweb-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const uint8\_t\* buffer | Pointer to the data to be transferred. Only the String and ArrayBuffer types can be transferred from the frontend. Other types will be serialized by JSON and then transferred as the String type. |
| size\_t size | Length of the data to be transferred. |
