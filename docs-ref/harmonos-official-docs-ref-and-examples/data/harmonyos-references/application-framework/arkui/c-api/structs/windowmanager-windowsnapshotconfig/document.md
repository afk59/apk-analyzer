# WindowManager\_WindowSnapshotConfig

typedef struct {...} WindowManager\_WindowSnapshotConfig

#### Overview

Describes the configuration of the main window screenshot.

**Since**: 21

**Related module**: [WindowManager](../../modules/windowmanager/document.md)

**Header file**: [oh\_window\_comm.h](../../header-files/oh-window-comm-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| bool useCache | Whether the existing screenshot of the main window should be used. The default value is **true**. When it is set to **true**, the system uses the existing screenshot of the main window, or captures the latest screenshot if no existing screenshot is saved. When it is set to **false**, the system captures the latest screenshot of the main window. |
