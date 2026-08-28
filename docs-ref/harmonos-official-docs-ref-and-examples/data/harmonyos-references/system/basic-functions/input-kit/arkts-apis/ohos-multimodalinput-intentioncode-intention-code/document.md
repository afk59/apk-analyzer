# @ohos.multimodalInput.intentionCode (Intention Code)

The **intentionCode** module maps the original events of the keyboard to intention codes for normalized interaction. For example, if the mapped event of the space bar on the keyboard is **INTENTION\_SELECT**, the intent is to select an item.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/PwTfF4NnTQKWBl4izvQ8Bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062403Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CF7549A4FD20EE6B02E421AE019615668CC8DF703BECF23148BBB5661B97A52)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { IntentionCode } from '@kit.InputKit';

#### IntentionCode

Enumerates intention codes.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.MultimodalInput.Input.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| INTENTION\_UNKNOWN | \-1 | Unknown intent |
| INTENTION\_UP | 1 | Up |
| INTENTION\_DOWN | 2 | Down |
| INTENTION\_LEFT | 3 | Left |
| INTENTION\_RIGHT | 4 | Right |
| INTENTION\_SELECT | 5 | Select |
| INTENTION\_ESCAPE | 6 | Escape |
| INTENTION\_BACK | 7 | Back |
| INTENTION\_FORWARD | 8 | Forward |
| INTENTION\_MENU | 9 | Menu |
| INTENTION\_PAGE\_UP | 11 | Page up |
| INTENTION\_PAGE\_DOWN | 12 | Page down |
| INTENTION\_ZOOM\_OUT | 13 | Zoom out |
| INTENTION\_ZOOM\_IN | 14 | Zoom in |
