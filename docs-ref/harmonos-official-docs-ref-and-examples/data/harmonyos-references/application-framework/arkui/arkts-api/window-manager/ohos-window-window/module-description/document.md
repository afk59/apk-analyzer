# Module Description

The module provides basic window management capabilities, such as creating and destroying the current window, setting properties for the current window, and managing and scheduling windows.

This module provides the following common window-related functionalities:

-   [Window](../interface-window/document.md): window instance, which is the basic unit managed by the window manager.
-   [WindowStage](../interface-windowstage/document.md): window manager that manages windows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/fR8AW9FRSdygKNQ4UFKmoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062230Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97F6D24AAD2AE07C366A95BE6A5F31A492E866257B09FE1D1E89C22225E08CCB)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   For the system capability SystemCapability.Window.SessionManager, use [canIUse()](../../../../../../common-capabilities/arkts-api/syscap/document.md#caniuse) to check whether the device supports this system capability and the corresponding APIs.
    

#### Modules to Import

import { window } from '@kit.ArkUI';
