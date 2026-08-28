# @ohos.graphics.hdrCapability (HDR Capability)

The hdrCapability module provides enums related to the High Dynamic Range (HDR) capability.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/DclehJkTQKeSFqh3aQ-RuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062448Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE1DE4444B911834392002088C69D85C0D1083F90A2D18016C94DB6240EC186D)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { hdrCapability } from '@kit.ArkGraphics2D';

#### HDRFormat

Enumerates the HDR formats.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Graphic.Graphic2D.ColorManager.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | Unsupported HDR type. |
| VIDEO\_HLG | 1 | Videos in Hybrid Log-Gamma (HLG) format. |
| VIDEO\_HDR10 | 2 | Videos in HDR10 format. |
| VIDEO\_HDR\_VIVID | 3 | Videos in HDR\_VIVID format. |
| IMAGE\_HDR\_VIVID\_DUAL | 4 | Images in HDR\_VIVID format, stored in dual JPEG format. |
| IMAGE\_HDR\_VIVID\_SINGLE | 5 | Images in HDR\_VIVID format, stored in single HEIF format. |
| IMAGE\_HDR\_ISO\_DUAL | 6 | Images in HDR\_ISO format, stored in dual JPEG format. |
| IMAGE\_HDR\_ISO\_SINGLE | 7 | Images in HDR\_ISO format, stored in single HEIF format. |
