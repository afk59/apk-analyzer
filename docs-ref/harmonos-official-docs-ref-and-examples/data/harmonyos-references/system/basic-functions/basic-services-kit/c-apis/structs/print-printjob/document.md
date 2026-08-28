# Print\_PrintJob

typedef struct {...} Print\_PrintJob

#### Overview

Defines a struct for the print job.

**Since**: 12

**Related module**: [OH\_Print](../../modules/oh-print/document.md)

**Header file**: [ohprint.h](../../header-files/ohprint-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char \*jobName | Job name. |
| uint32\_t \*fdList | Array of file descriptors to be printed. |
| uint32\_t fdListCount | Number of file descriptors to be printed. |
| char \*printerId | Printer ID. |
| uint32\_t copyNumber | Number of copies to print. |
| char \*paperSource | Paper source. |
| char \*mediaType | Media type. |
| char \*pageSizeId | Page size ID. |
| [Print\_ColorMode](../../header-files/ohprint-h/document.md#print_colormode) colorMode | Color mode. |
| [Print\_DuplexMode](../../header-files/ohprint-h/document.md#print_duplexmode) duplexMode | Duplex mode. |
| [Print\_Resolution](../print-resolution/document.md) resolution | Print resolution, in dpi. |
| [Print\_Margin](../print-margin/document.md) printMargin | Page margin. |
| bool borderless | Whether to print without margins. |
| [Print\_OrientationMode](../../header-files/ohprint-h/document.md#print_orientationmode) orientationMode | Orientation mode. |
| [Print\_Quality](../../header-files/ohprint-h/document.md#print_quality) printQuality | Print quality. |
| [Print\_DocumentFormat](../../header-files/ohprint-h/document.md#print_documentformat) documentFormat | Document format. |
| char \*advancedOptions | 
Advanced options in JSON format.

The supported keys are as follows:

\- **isReverse**: Boolean type, indicating whether to print in reverse order.

\- **isCollate**: Boolean type, indicating whether to print copies one by one.

 |
