# Scan\_PictureScanProgress

#### Overview

Defines the progress of scanning a picture by the scanner.

**Since**: 12

**Related module**: [OH\_Scan](../../modules/oh-scan/document.md)

**Header file**: [ohscan.h](../../header-files/ohscan-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int32\_t progress | Progress of scanning a picture, ranging from 0 to 100. |
| int32\_t fd | Scanner file handle. |
| bool isFinal | Whether the picture is the last one to be scanned. The value **true** indicates that the picture is the last one to be scanned, and **false** indicates the opposite. |
