# Region

typedef struct {...} Region

#### Overview

The **Region** struct describes the rectangle (dirty region) where the content is to be updated in the local **OHNativeWindow**.

**Since**: 8

**Related module**: [NativeWindow](../../modules/nativewindow/document.md)

**Header file**: [external\_window.h](../../header-files/external-window-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| \* rects | If **rects** is a null pointer, the buffer size is the same as the size of the dirty region by default. |
| int32\_t rectNumber | If **rectNumber** is **0**, the buffer size is the same as the size of the dirty region by default. |
