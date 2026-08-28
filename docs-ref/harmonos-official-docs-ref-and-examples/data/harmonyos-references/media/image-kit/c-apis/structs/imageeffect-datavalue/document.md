# ImageEffect\_DataValue

typedef union ImageEffect\_DataValue {...} ImageEffect\_DataValue

#### Overview

The union describes the data values.

**Since**: 12

**Related module**: [ImageEffect](../../modules/imageeffect/document.md)

**Header file**: [image\_effect\_filter.h](../../header-files/image-effect-filter-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t int32Value | Integer value, corresponding to [EFFECT\_DATA\_TYPE\_INT32](../../header-files/image-effect-filter-h/document.md#imageeffect_datatype). |
| float floatValue | Single-precision floating-point value, corresponding to [EFFECT\_DATA\_TYPE\_FLOAT](../../header-files/image-effect-filter-h/document.md#imageeffect_datatype). |
| double doubleValue | Double-precision floating-point value, corresponding to [EFFECT\_DATA\_TYPE\_DOUBLE](../../header-files/image-effect-filter-h/document.md#imageeffect_datatype). |
| char charValue | Byte value, corresponding to [EFFECT\_DATA\_TYPE\_CHAR](../../header-files/image-effect-filter-h/document.md#imageeffect_datatype). |
| long longValue | Long integer, corresponding to [EFFECT\_DATA\_TYPE\_LONG](../../header-files/image-effect-filter-h/document.md#imageeffect_datatype). |
| bool boolValue | Boolean value, corresponding to [EFFECT\_DATA\_TYPE\_BOOL](../../header-files/image-effect-filter-h/document.md#imageeffect_datatype). |
| void\* ptrValue | Pointer value, corresponding to [EFFECT\_DATA\_TYPE\_PTR](../../header-files/image-effect-filter-h/document.md#imageeffect_datatype). |
