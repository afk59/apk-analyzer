# Print\_PrinterCapability

typedef struct {...} Print\_PrinterCapability

#### Overview

Defines a struct for the printer capabilities.

**Since**: 12

**Related module**: [OH\_Print](../../modules/oh-print/document.md)

**Header file**: [ohprint.h](../../header-files/ohprint-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Print\_ColorMode](../../header-files/ohprint-h/document.md#print_colormode) \*supportedColorModes | Array of supported color modes. |
| uint32\_t supportedColorModesCount | Number of supported color modes. |
| [Print\_DuplexMode](../../header-files/ohprint-h/document.md#print_duplexmode) \*supportedDuplexModes | Array of supported duplex modes. |
| uint32\_t supportedDuplexModesCount | Number of supported duplex modes. |
| [Print\_PageSize](../print-pagesize/document.md) \*supportedPageSizes | Array of supported page sizes. |
| uint32\_t supportedPageSizesCount | Number of supported page sizes. |
| char \*supportedMediaTypes | Array of supported print media types in JSON string format. |
| [Print\_Quality](../../header-files/ohprint-h/document.md#print_quality) \*supportedQualities | Array of supported print qualities. |
| uint32\_t supportedQualitiesCount | Number of supported print qualities. |
| char \*supportedPaperSources | Array of supported paper sources in JSON string format. |
| uint32\_t supportedCopies | Supported number of copies. |
| [Print\_Resolution](../print-resolution/document.md) \*supportedResolutions | Array of supported printer resolutions. |
| uint32\_t supportedResolutionsCount | Supported number of printer resolutions. |
| [Print\_OrientationMode](../../header-files/ohprint-h/document.md#print_orientationmode) \*supportedOrientations | Array of supported orientations. |
| uint32\_t supportedOrientationsCount | Supported number of orientations. |
| char \*advancedCapability | Advanced capabilities in JSON format. |
