# WindowManager\_WindowProperties

typedef struct {...} WindowManager\_WindowProperties

#### Overview

The struct describes the window properties.

**Since**: 15

**Related module**: [WindowManager](../../modules/windowmanager/document.md)

**Header file**: [oh\_window\_comm.h](../../header-files/oh-window-comm-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [WindowManager\_Rect](../windowmanager-rect/document.md) windowRect | Position and size of the window. |
| [WindowManager\_Rect](../windowmanager-rect/document.md) drawableRect | Size of the drawable area within the window. |
| [WindowManager\_WindowType](../../header-files/oh-window-comm-h/document.md#windowmanager_windowtype) type | Window type. |
| bool isFullScreen | Whether the window is in full-screen mode. The default value is **false**. **true** if in full-screen mode, **false** otherwise. |
| bool isLayoutFullScreen | Whether the window layout is immersive. The default value is **false**. **true** if immersive, **false** otherwise. |
| bool focusable | Whether the window is focusable. The default value is **true**. **true** if focusable, **false** otherwise. |
| bool touchable | Whether the window is touchable. The default value is **true**. **true** if touchable, **false** otherwise. |
| float brightness | Screen brightness of the window. The value is a floating-point number in the range \[0.0, 1.0\] or is set to **\-1.0**, where **1.0** indicates the brightest, and **\-1.0** is the default brightness. |
| bool isKeepScreenOn | Whether the screen is steady on. The default value is **false**. **true** if steady on, **false** otherwise. |
| bool isPrivacyMode | Whether privacy mode is enabled for the window. The default value is **false**. **true** if enabled, **false** otherwise. |
| bool isTransparent | Whether the window is transparent. The default value is **false**. **true** if transparent, **false** otherwise. |
| uint32\_t id | Window ID. The default value is **0**, and the value is an integer. |
| uint32\_t displayId | ID of the screen where the window is located. By default, the ID of the primary screen is returned. The value is an integer. |
