# Print\_PrintDocCallback

typedef struct {...} Print\_PrintDocCallback

#### Overview

Defines a struct for the print job state callback.

**Since**: 13

**Related module**: [OH\_Print](../../modules/oh-print/document.md)

**Header file**: [ohprint.h](../../header-files/ohprint-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Print\_OnStartLayoutWrite](../../header-files/ohprint-h/document.md#print_onstartlayoutwrite) startLayoutWriteCb | Callback to be invoked when the file write-back starts. |
| [Print\_OnJobStateChanged](../../header-files/ohprint-h/document.md#print_onjobstatechanged) jobStateChangedCb | Callback to be invoked when the print job state changes. |
