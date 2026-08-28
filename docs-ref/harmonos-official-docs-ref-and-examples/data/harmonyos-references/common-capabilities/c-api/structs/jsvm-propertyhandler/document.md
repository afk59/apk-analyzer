# JSVM\_PropertyHandler

typedef struct {...} JSVM\_PropertyHandler

#### Overview

Defines the pointer to the callback function triggered when a class is called as a function, and the pointer collection of the callback function triggered when an instance object property is accessed.

**Since**: 18

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [JSVM\_PropertyHandlerCfg](../jsvm-propertyhandlerconfigurationstruct--00020177/document.md) propertyHandlerCfg | Callback triggered when an instance object property is accessed. |
| [JSVM\_Callback](../jsvm-callbackstruct--00020177/document.md) callAsFunctionCallback | Callback triggered when an instance object is called as a function. |
