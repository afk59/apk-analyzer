# OH\_AVScreenCaptureHighlightConfig

typedef struct OH\_AVScreenCaptureHighlightConfig {...} OH\_AVScreenCaptureHighlightConfig

#### Overview

The struct describes the style of the highlight border shown during screen capture, including its shape, thickness, and color.

**Since**: 22

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

**Header file**: [native\_avscreen\_capture\_base.h](../../header-files/native-avscreen-capture-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_ScreenCaptureHighlightMode](../../header-files/native-avscreen-capture-base-h/document.md#oh_screencapturehighlightmode) mode | Shape of the highlight border. If this variable is not set, a full rectangle is used by default. |
| uint32\_t lineThickness | Thickness of the border line. If this variable is not set, the border is invisible by default. The valid value range is 1 vp to 8 vp. |
| uint32\_t lineColor | Color of the border line. The default value is black. Valid values are in RGB (0-0xffffff) or non-transparent ARGB (0xff000000-0xffffffff) format. |
