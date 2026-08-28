# ScenePostProcessSettings

The module provides image post-processing methods (for example, tone mapping) in 3D graphics.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/bglQe9krRvyiEboJDOKBxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062456Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=351E782DAB1FF4C347ECECA6C8D219FB1B3B267065779A7FFA21839B431C221D)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { ToneMappingType, ToneMappingSettings, BloomSettings, PostProcessSettings } from '@kit.ArkGraphics3D';

#### ToneMappingType

Enumerates the tone mapping types.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Value | Description |
| :-- | :-- | :-- |
| ACES | 0 | Academy Color Encoding System (ACES). |
| ACES\_2020 | 1 | ACES\_2020. |
| FILMIC | 2 | Filmic. |

#### ToneMappingSettings

Describes the tone mapping settings.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [ToneMappingType](#tonemappingtype) | No | Yes | Tone mapping type. The default value is undefined. |
| exposure | number | No | Yes | Exposure. The value must be greater than 0. The default value is undefined. |

#### BloomSettings18+

Describes the settings for bloom effects. It is unavailable when [RenderingPipelineType](../scenetype/document.md#renderingpipelinetype21) is set to **FORWARD\_LIGHTWEIGHT**.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| thresholdHard | number | No | Yes | Hard threshold. The value is a non-negative number. The default value is **1.0**. |
| thresholdSoft | number | No | Yes | Soft threshold. The value is a non-negative number. The default value is **2.0**. |
| scaleFactor | number | No | Yes | Scale factor. The value must be greater than 0. The default value is **1.0**. |
| scatter | number | No | Yes | Scatter amount. The value must be greater than 0. The default value is **1.0**. |

#### VignetteSettings22+

Describes the settings for vignette effects.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| roundness | number | No | Yes | Extent of the effect. The value ranges from 0 to 1. The value **1** means a global effect. The default is **sqrt(0.5)**. |
| intensity | number | No | Yes | Strength of the effect. The default value is **0.4**. |

#### ColorFringeSettings22+

Describes the settings for color fringing. It is unavailable when [RenderingPipelineType](../scenetype/document.md#renderingpipelinetype21) is set to **FORWARD\_LIGHTWEIGHT**.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| intensity | number | No | Yes | Strength of the effect. The value ranges from 0 to 1. The default value is **0.2**. |

#### PostProcessSettings

Describes the post-processing settings.

**System capability**: SystemCapability.ArkUi.Graphics3D

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| toneMapping | [ToneMappingSettings](#tonemappingsettings) | No | Yes | Tone mapping settings. The default value is undefined. |
| bloom18+ | [BloomSettings](#bloomsettings18) | No | Yes | Bloom settings. The default value is undefined. |
| vignette22+ | [VignetteSettings](#vignettesettings22) | No | Yes | Vignette settings. The default value is undefined. |
| colorFringe22+ | [ColorFringeSettings](#colorfringesettings22) | No | Yes | Color fringing settings. The default value is undefined. |
