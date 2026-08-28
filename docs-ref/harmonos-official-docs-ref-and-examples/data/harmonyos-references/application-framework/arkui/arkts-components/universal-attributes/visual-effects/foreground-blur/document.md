# Foreground Blur

You can apply foreground blur effects to a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/H3aznjFjT8uQS4gSTaq0lw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE1D9E9B59D03FC62CEFB6F3EEDF335E7915E5C3EC40C8088143AC17C546AAD5)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### foregroundBlurStyle

foregroundBlurStyle(value: BlurStyle, options?: ForegroundBlurStyleOptions): T

Applies a foreground blur style to the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/FZI6IvlmSg2z0f7R-tA_uQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7327A7C63FC274E7DE4C5662F9ED81621E401D83E17DB050044F127714135FE1)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BlurStyle](../../basic-attributes/background/document.md#blurstyle9) | Yes | Settings of the foreground blur style. |
| options | [ForegroundBlurStyleOptions](#foregroundblurstyleoptions) | No | Defines the foreground blur options. For details about the default value, see [ForegroundBlurStyleOptions](#foregroundblurstyleoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### foregroundBlurStyle18+

foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions): T

Applies a foreground blur style to the component. Compared to [foregroundBlurStyle](#foregroundblurstyle), the **style** parameter supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[BlurStyle](../../basic-attributes/background/document.md#blurstyle9)\> | Yes | 
Settings of the foreground blur style.

If **style** is set to **undefined**, no blur is applied.

 |
| options | [ForegroundBlurStyleOptions](#foregroundblurstyleoptions) | No | Defines the foreground blur options. For details about the default value, see [ForegroundBlurStyleOptions](#foregroundblurstyleoptions). |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### foregroundBlurStyle19+

foregroundBlurStyle(style: Optional<BlurStyle>, options?: ForegroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T

Applies a foreground blur style to the component. Compared to [foregroundBlurStyle18+](#foregroundblurstyle18), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/YFE_mhm8QIKvUHVWdFgqwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=732FC0839F6CB2AE7B179C403AE397145D1B9F014B645316D31D4BD7AD7D9D8E)

**foregroundBlurStyle** is a real-time blurring API that performs rendering frame by frame, which incurs significant performance overhead. When both the blur content and blur radius remain unchanged, it is recommended that you use the static blur API [blur](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-effectkit-image-effects/document.md#blur). For best practices, see [Image Blurring Optimization – When to Use](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-fuzzy-scene-performance-optimization#section4945532519).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[BlurStyle](../../basic-attributes/background/document.md#blurstyle9)\> | Yes | 
Settings of the foreground blur style.

If **style** is set to **undefined**, no blur is applied.

 |
| options | [ForegroundBlurStyleOptions](#foregroundblurstyleoptions) | No | Foreground blur options. |
| sysOptions | [SystemAdaptiveOptions](../../basic-attributes/background/document.md#systemadaptiveoptions19) | No | 

System adaptive adjustment options.

Default value: **{ disableSystemAdaptation: false }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### ForegroundBlurStyleOptions

Inherits from [BlurStyleOptions](#blurstyleoptions) to define the foreground blur options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### BlurStyleOptions

Defines the foreground blur options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| colorMode | [ThemeColorMode](#themecolormode) | No | Yes | 
Color mode used for the foreground blur.

Default value: **ThemeColorMode.SYSTEM**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| adaptiveColor | [AdaptiveColor](#adaptivecolor) | No | Yes | 

Adaptive color mode.

Default value: **AdaptiveColor.DEFAULT**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| blurOptions11+ | [BlurOptions](#bluroptions11) | No | Yes | 

Grayscale blur parameters.

Default value: **grayscale: \[0,0\]**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| scale12+ | number | No | Yes | 

Foreground blur scale.

Default value: **1.0**

Value range: \[0.0, 1.0\]

**1.0** indicates the highest blur degree.

**0.0** indicates the lowest blur degree.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ThemeColorMode

Enumerates the color modes.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SYSTEM | 0 | System color mode. |
| LIGHT | 1 | Light color mode. |
| DARK | 2 | Dark color mode. |

#### AdaptiveColor

Enumerates the adaptive color modes used for the background blur effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Adaptive color mode is not used. The default color is used as the mask color. Using a mode other than **DEFAULT** can be more time-consuming. |
| AVERAGE | 1 | Adaptive color mode is used. The average color value of the color picking area is used as the mask color. |

#### BlurOptions11+

Grayscale blur parameters.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| grayscale | \[number, number\] | No | No | Grayscale blur, with two parameters in the value range of \[0, 127\]. The color gradation of the black and white in the image is adjusted to create different shades of gray. The first parameter indicates the brightness of the black color, and the second parameter indicates the darkness of the white color. A larger value indicates a more obvious adjustment effect (the black and white colors become grayer). The valid value range is 0–127. For example, if the value specified is (20,20), the RGB value \[0, 0, 0\] (black) is converted to \[20, 20, 20\], RGB value \[255, 255, 255\] (white) is converted to \[235, 235, 235\] (255-20), and the color pixels remain unchanged. |

#### Example

This example demonstrates how to apply content blur to an image using **foregroundBlurStyle**.

// xxx.ets
@Entry
@Component
struct ForegroundBlurStyleDemo {
  build() {
    Column() {
      Text('Thin Material').fontSize(30).fontColor(0xCCCCCC)
      // Replace $r("app.media.bg") with the image resource file you use.
      Image($r('app.media.bg'))
        .width(300)
        .height(350)
        .foregroundBlurStyle(BlurStyle.Thin,
          { colorMode: ThemeColorMode.LIGHT, adaptiveColor: AdaptiveColor.DEFAULT, scale: 1.0 })
    }
    .height('100%')
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/UoEQP1IZQr21qYD7wkw0Ig/en-us_image_0000002568765161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=990FAFC5A7C2F6BFE3A43947276F4A60802F5A7A222FE7623D2C490385093333)
