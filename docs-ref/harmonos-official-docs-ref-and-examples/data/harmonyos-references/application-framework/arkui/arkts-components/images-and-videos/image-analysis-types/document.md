# Image Analysis Types

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/a17pyO8ATUGuD8eTbARU2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A90EC7C541B7E8872191BC535E4A3246A06E59E22B55590DAB11912F3FFB0EC9)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### PixelMap

type PixelMap = PixelMap

Represents an image pixel map for reading or writing image data and accessing image information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Multimedia.Image.Core

| Type | Description |
| :-- | :-- |
| [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Image pixel map class for reading or writing image data and accessing image information. |

#### ImageAnalyzerConfig12+

Provides AI image analyzer configuration.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| types | [ImageAnalyzerType\[\]](#imageanalyzertype12) | No | No | AI image analysis types. |

#### ImageAnalyzerType12+

Defines the AI image analysis type. If it is not set, subject recognition and text recognition are enabled by default.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SUBJECT | 0 | Subject recognition. |
| TEXT | 1 | Text recognition. |
| OBJECT\_LOOKUP | 2 | Object lookup. |

#### ImageAIOptions12+

Provides the AI image analysis options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| types | [ImageAnalyzerType\[\]](#imageanalyzertype12) | No | Yes | AI image analysis types. |
| aiController | [ImageAnalyzerController](#imageanalyzercontroller12) | No | Yes | AI image analysis controller. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/n-4TnmFUTkGrXMXYa8NjmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062243Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55ADECCE7F482E54C1CA32073BF8D520472D756600845998174AD728A83087A4)

The **types** parameter of this API has a higher priority than that of [ImageAnalyzerConfig](#imageanalyzerconfig12). This means that, if both parameters are set, the value set by this API takes precedence.

This API depends on device capabilities and must be used together with the [enableAnalyzer](../image/document.md#enableanalyzer11) API of the corresponding component (for example, the [Image](../image/document.md) component).

#### ImageAnalyzerController12+

Implements an AI image analysis controller, which provides control for image analysis features when bound to supported components.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]constructor12+

constructor()

A constructor used to create an **ImageAnalyzerController** instance.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]getImageAnalyzerSupportTypes12+

getImageAnalyzerSupportTypes(): ImageAnalyzerType\[\]

Obtains the analysis types supported by the corresponding component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| [ImageAnalyzerType\[\]](#imageanalyzertype12) | Analysis type supported by the corresponding component. |

#### ContentTransitionEffect21+

Defines the content transition effect.

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| IDENTITY | [ContentTransitionEffect](#contenttransitioneffect21) | Yes | No | Applies no transition effect during content switching. |
| OPACITY | [ContentTransitionEffect](#contenttransitioneffect21) | Yes | No | Applies a fade-in/fade-out transition animation during content switching. |
