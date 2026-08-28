# Print\_PrinterInfo

typedef struct {...} Print\_PrinterInfo

#### Overview

Defines a struct for the printer information.

**Since**: 12

**Related module**: [OH\_Print](../../modules/oh-print/document.md)

**Header file**: [ohprint.h](../../header-files/ohprint-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Print\_PrinterState](../../header-files/ohprint-h/document.md#print_printerstate) printerState | Printer state. |
| [Print\_PrinterCapability](../print-printercapability/document.md) capability | Printer capability. |
| [Print\_DefaultValue](../print-defaultvalue/document.md) defaultValue | Default property value of the printer. |
| bool isDefaultPrinter | Default printer. |
| char \*printerId | Printer ID. |
| char \*printerName | Printer name. |
| char \*description | Printer description. |
| char \*location | Printer location. |
| char \*makeAndModel | Brand and model of the printer. |
| char \*printerUri | Printer URI. |
| char \*detailInfo | Details in JSON format. |
