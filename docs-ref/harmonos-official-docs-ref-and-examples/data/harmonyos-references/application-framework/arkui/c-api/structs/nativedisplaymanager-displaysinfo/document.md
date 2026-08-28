# NativeDisplayManager\_DisplaysInfo

typedef struct {...} NativeDisplayManager\_DisplaysInfo

#### Overview

The struct describes the information about displays of a device with multiple screens.

**Since**: 14

**Related module**: [OH\_DisplayManager](../../modules/oh-displaymanager/document.md)

**Header file**: [oh\_display\_info.h](../../header-files/oh-display-info-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t displaysLength | Number of displays of a device with multiple screens. |
| [NativeDisplayManager\_DisplayInfo](../nativedisplaymanager-displayinfo/document.md)\* displaysInfo | An array of NativeDisplayManager\_DisplayInfo structs, each containing information about a display. |
