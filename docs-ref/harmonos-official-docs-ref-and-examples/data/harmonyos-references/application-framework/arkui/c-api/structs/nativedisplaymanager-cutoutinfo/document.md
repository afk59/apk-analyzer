# NativeDisplayManager\_CutoutInfo

typedef struct {...} NativeDisplayManager\_CutoutInfo

#### Overview

The struct describes the unusable area of a display, including punch hole, notch, and curved area of a waterfall display.

**Since**: 12

**Related module**: [OH\_DisplayManager](../../modules/oh-displaymanager/document.md)

**Header file**: [oh\_display\_info.h](../../header-files/oh-display-info-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Struct | Description |
| :-- | :-- |
| int32\_t boundingRectsLength | Number of unusable areas (bounding rectangles) designed for punch holes and notches. |
| [NativeDisplayManager\_Rect](../nativedisplaymanager-rect/document.md)\* boundingRects | Unusable areas (bounding rectangles) designed for punch holes and notches. |
| [NativeDisplayManager\_WaterfallDisplayAreaRects](../nativedisplaymanager-waterfalldisplayarearects/document.md) waterfallDisplayAreaRects | Curved area on a waterfall display. |
