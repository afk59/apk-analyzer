# @ohos.inputMethod.Panel (Input Method Panel)

The **inputMethod.Panel** module provides APIs for managing the attributes of the input method panel.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/sob2Ny9NRXWMEKVWTOBxYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062323Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=135EF7C1168F60B6D90909D602129D1A36D380C4B1AB61B406D4752E24B91503)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { PanelInfo, PanelType, PanelFlag } from '@kit.IMEKit';

#### PanelInfo

Defines the attributes of the input method panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [PanelType](#paneltype) | No | No | Type of the input method panel. |
| flag | [PanelFlag](#panelflag) | No | Yes | 
State type of the input method panel.

\- The default value is **FLAG\_FIXED**.

\- Currently, this parameter is used to describe the state type of the soft keyboard.

 |

#### PanelType

Enumerates the types of the input method panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| SOFT\_KEYBOARD | 0 | Soft keyboard. |
| STATUS\_BAR | 1 | Status bar. |

#### PanelFlag

Enumerates the state types of the input method panel.

**System capability**: SystemCapability.MiscServices.InputMethodFramework

| Name | Value | Description |
| :-- | :-- | :-- |
| FLAG\_FIXED | 0 | Fixed state type. |
| FLAG\_FLOATING | 1 | Floating state type. |
| FLAG\_CANDIDATE | 2 | 
Candidate state type.

\- When in the candidate state type, the input method panel is a window displaying candidates based on user input.

\- The input method service does not proactively control the visibility of the candidate panel. You need to control the visibility on your own.

 |
