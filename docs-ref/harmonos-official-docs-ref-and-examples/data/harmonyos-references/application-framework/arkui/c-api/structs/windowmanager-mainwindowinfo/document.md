# WindowManager\_MainWindowInfo

typedef struct {...} WindowManager\_MainWindowInfo

#### Overview

The struct describes the main window information.

**Since**: 21

**Related module**: [WindowManager](../../modules/windowmanager/document.md)

**Header file**: [oh\_window\_comm.h](../../header-files/oh-window-comm-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint64\_t displayId | ID of the display to which the main window belongs. |
| int32\_t windowId | ID of the main window. |
| bool showing | Foreground/Background status of the main window. **true** if the main window is in the foreground, **false** otherwise. |
| const char\* label | Pointer to the task name of the main window. |
