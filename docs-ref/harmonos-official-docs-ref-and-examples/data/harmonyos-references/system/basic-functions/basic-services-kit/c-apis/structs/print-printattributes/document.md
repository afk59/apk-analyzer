# Print\_PrintAttributes

typedef struct {...} Print\_PrintAttributes

#### Overview

Defines a struct for the print attributes.

**Since**: 13

**Related module**: [OH\_Print](../../modules/oh-print/document.md)

**Header file**: [ohprint.h](../../header-files/ohprint-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Print\_Range](../print-range/document.md) pageRange | Page range. |
| [Print\_PageSize](../print-pagesize/document.md) pageSize | Page size. |
| [Print\_Margin](../print-margin/document.md) pageMargin | Page margin. |
| uint32\_t copyNumber | Number of copies to print. |
| uint32\_t duplexMode | Duplex mode. |
| uint32\_t colorMode | Color mode. |
| bool isSequential | 
Whether pages are printed in sequential order.

The value **true** indicates that pages are printed in sequential order, and **false** indicates the opposite.

 |
| bool isLandscape | 

Whether pages are printed in landscape mode.

The value **true** indicates that pages are printed in landscape mode, and **false** indicates that pages are printed in portrait mode.

 |
| bool hasOption | 

Whether the printing has an option flag.

The value **true** indicates that the printing has an option flag, and **false** indicates the opposite.

 |
| char options\[256\] | Print options. |
