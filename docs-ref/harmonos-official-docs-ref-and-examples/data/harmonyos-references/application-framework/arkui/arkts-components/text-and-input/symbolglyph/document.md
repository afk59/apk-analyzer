# SymbolGlyph

The **SymbolGlyph** component represents a symbol glyph.

For details about related resources, see [System Icons](https://developer.huawei.com/consumer/en/doc/design-guides/system-icons-0000001929854962).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/iQ_wcvhmRHKXHSXZ8GCL7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F2F4FE86F30C7EC43C1730698EA886E6605C2374F2B5A38E305E78A12F7A9CB)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Not supported

#### APIs

SymbolGlyph(value?: Resource)

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Resource of the **SymbolGlyph** component, for example, **$r('sys.symbol.ohos\_wifi')**. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/rD3RIsfxS0qc_qQxG9MkpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6FC688F780AFA835D9F0F842666617FA5E8844A4338EDBFA6C0888F8CF06DE4)

The resources referenced in **$r('sys.symbol.ohos\_wifi')** are preset in the system. The **SymbolGlyph** component supports only the preset symbol resources. If unsupported resources are referenced, an exception occurs.

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are supported. For text attributes, only the following attributes are supported.

#### \[h2\]fontColor

fontColor(value: Array<ResourceColor>)

Sets the color of the **SymbolGlyph** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/sqdFfke7SKuS86H6sSJUGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4D91CD7B15AF29488132014CB0971FCC2C7A880DDCBC9C2E9855AADA8F268C3)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Array<[ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Color of the **SymbolGlyph** component.

Default value: depending on the rendering strategy

 |

#### \[h2\]fontSize

fontSize(value: number | string | Resource)

Sets the size of the **SymbolGlyph** component. When using the string type, numeric string values with optional units, for example, **"10"** or **"10fp"**, are supported.

The display size of the symbol glyph is controlled by the **fontSize** setting. Once **width** or **height** is specified, other universal attributes will only affect the size of the component's placeholder, not the symbol glyph itself.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/I1e-YIyDRmqZ0oenzK3J9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=753F73F8CCD3F2B1D872259F766C1EE7DA60208505A3682ECAF032E1D2D80765)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | 
Size of the **SymbolGlyph** component.

Default value: **16fp**

Unit: [fp](../../common-definitions/pixel-units/document.md)

Percentage strings are not supported.

 |

#### \[h2\]fontWeight

fontWeight(value: number | FontWeight | string)

Sets the font weight of the **SymbolGlyph** component. For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a heavier font weight. The default value is **400**. For the string type, only strings of the number type are supported, for example, **"400"**, **"bold"**, **"bolder"**, **"lighter"**, **"regular"**, and **"medium"**, which correspond to the enumerated values in **FontWeight**.

The **sys.symbol.ohos\_lungs** icon does not support font weight setting.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/woC9AkfqQxetrjqXySGJlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAF32DE4128600F7AA1304E4127CDB34C2967479755FB7C0B1DDD6AD79F06842)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [FontWeight](../../common-definitions/enums/document.md#fontweight) | string | Yes | 
Font weight of the **SymbolGlyph** component.

Default value: **FontWeight.Normal**

 |

#### \[h2\]renderingStrategy

renderingStrategy(value: SymbolRenderingStrategy)

Sets the rendering strategy of the **SymbolGlyph** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/41LUVPHdSMyxAEzp1I0ZlQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E37FCF2118E0916BFACFF859B6CEA35F81D26CAA06C137F0BD239920BD82FF3)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SymbolRenderingStrategy](#symbolrenderingstrategy11) | Yes | 
Rendering strategy of the **SymbolGlyph** component.

Default value: **SymbolRenderingStrategy.SINGLE**

 |

The figure below shows the effects of different rendering strategies.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/Z-QydVmiQKKTiiTF9bN8Bg/en-us_image_0000002568685409.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E6533C8B104869AA74B88A3E1AE465CB8C651E421FB9039425794016BDB3B26)

#### \[h2\]effectStrategy

effectStrategy(value: SymbolEffectStrategy)

Sets the effect strategy of the **SymbolGlyph** component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/Xu6HZrJoSuyr_s8RZw7mVw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=953D30445170336F1BD921AB1B5F0A303769380AF4E7B786A120C2177EBAF6FF)

This API can be called within [attributeModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 12.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SymbolEffectStrategy](#symboleffectstrategy11) | Yes | 
Effect strategy of the **SymbolGlyph** component.

Default value: **SymbolEffectStrategy.NONE**

 |

#### \[h2\]symbolEffect12+

symbolEffect(symbolEffect: SymbolEffect, isActive?: boolean)

Sets the symbol effect and effect state for the **SymbolGlyph** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| symbolEffect | [SymbolEffect](#symboleffect12) | Yes | 
Symbol effect of the **SymbolGlyph** component.

Default value: [SymbolEffect](#symboleffect12)

 |
| isActive | boolean | No | 

Whether the effect is active.

**true**: playing. **false**: not playing.

Default value: **false**.

 |

#### \[h2\]symbolEffect12+

symbolEffect(symbolEffect: SymbolEffect, triggerValue?: number)

Sets the symbol effect and effect trigger for the **SymbolGlyph** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| symbolEffect | [SymbolEffect](#symboleffect12) | Yes | 
Symbol effect of the **SymbolGlyph** component.

Default value: [SymbolEffect](#symboleffect12)

 |
| triggerValue | number | No | 

Value that, when changed, initiates the animation of the **SymbolGlyph** component.

To prevent the motion effect from triggering initially, set it to **\-1**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/R5lb5Z9mSSmPOX8lSmz3ZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBCCF2CF00E87B9403BFC4A34FAFCCBC9FB1131F103AE3C8F1EA4B636DE1E4C7)

When configuring the symbol effect, use the **effectStrategy** attribute or a single **symbolEffect** attribute. Mixing multiple effect attributes is not allowed.

#### \[h2\]minFontScale18+

minFontScale(scale: Optional<number | Resource>)

Sets the minimum font scale factor for the **SymbolGlyph** component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number | [Resource](../../common-definitions/basic-types/document.md#resource)\> | Yes | 
Minimum font scale factor for the **SymbolGlyph** component.

Value range: \[0, 1\]

The value **0** results in the minimum scaling.

**NOTE**

A value less than 0 is handled as 0. A value greater than 1 is handled as 1. Abnormal values are ineffective by default.

 |

#### \[h2\]maxFontScale18+

maxFontScale(scale: Optional<number | Resource>)

Sets the maximum font scale factor for the **SymbolGlyph** component.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scale | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<number | [Resource](../../common-definitions/basic-types/document.md#resource)\> | Yes | 
Maximum font scale factor for the **SymbolGlyph** component.

Value range: \[1, +∞)

**NOTE**

A value less than 1 is handled as **1**. Abnormal values are ineffective by default.

 |

#### \[h2\]shaderStyle20+

shaderStyle(shader: Array<ShaderStyle | undefined> | ShaderStyle)

Applies a gradient or solid color shader effect to the **SymbolGlyph** component.

This API supports [RadialGradientStyle](../text-component-common-apis/document.md#radialgradientstyle20), [LinearGradientStyle](../text-component-common-apis/document.md#lineargradientstyle20), and [ColorShaderStyle](../text-component-common-apis/document.md#colorshaderstyle20). When set, **shaderStyle** takes precedence over [fontColor](../symbolspan/document.md#fontcolor) and any AI-based styling. To apply a simple solid color, using [fontColor](../symbolspan/document.md#fontcolor) is recommended.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| shader | Array<[ShaderStyle](../text-component-common-apis/document.md#shaderstyle20) | undefined> | [ShaderStyle](../text-component-common-apis/document.md#shaderstyle20) | Yes | 
Shader effect.

Input types and behavior:

Single **ShaderStyle** object: applies the specified effect to all layers. Array of **ShaderStyle** objects: applies the specified effect to the corresponding layer. Array of **undefined**: applies the default **SymbolGlyph** color to the corresponding layer. Layers unset retain their default color.

Based on the input, the system applies a radial gradient ([RadialGradientStyle](../text-component-common-apis/document.md#radialgradientstyle20)), linear gradient ([LinearGradientStyle](../text-component-common-apis/document.md#lineargradientstyle20)), or solid color ([ColorShaderStyle](../text-component-common-apis/document.md#colorshaderstyle20)) to the **SymbolGlyph** component.

**NOTE**

Unit: [vp](../../common-definitions/pixel-units/document.md)

Specify the center point and radius using percentages. If a non-percentage value (e.g., **10px**) is provided, it will be interpreted as 1000%.

You are advised to specify the radius using percentages.

Percentages are relative to the icon's size. The recommended value range is \[0, 1).

 |

#### \[h2\]symbolShadow20+

symbolShadow(shadow: Optional<ShadowOptions>)

Sets the shadow effect of the **SymbolGlyph** component.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| shadow | [Optional](../../universal-attributes/modifiers-and-custom-property/custom-property/document.md#optionalt)<[ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions)\> | Yes | 
Shadow effect of the **SymbolGlyph** component.

Unit: [vp](../../common-definitions/pixel-units/document.md)

Default value: {

radius: 0,

color: Color.Black

offsetX: 0,

offsetY: 0

}

The **fill** and **type** attributes, as well as the enumerated values of **ColoringStrategy** within the \*\*color \*\*attribute, are not supported.

 |

#### ScaleSymbolEffect12+

Inherits from **SymbolEffect**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | Yes | 
Effect scope.

Default value: **EffectScope.LAYER**

 |
| direction | [EffectDirection](#effectdirection12) | No | Yes | 

Effect direction.

Default value: **EffectDirection.DOWN**

 |

#### \[h2\]constructor12+

constructor(scope?: EffectScope, direction?: EffectDirection)

A constructor used to create a **ScaleSymbolEffect** instance, which comes with a scaling animation effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | 
Effect scope.

Default value: **EffectScope.LAYER**

 |
| direction | [EffectDirection](#effectdirection12) | No | 

Effect direction.

Default value: **EffectDirection.DOWN**

 |

#### HierarchicalSymbolEffect12+

Inherits from **SymbolEffect**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fillStyle | [EffectFillStyle](#effectfillstyle12) | No | Yes | 
Effect fill style.

Default value: **EffectFillStyle.CUMULATIVE**

 |

#### \[h2\]constructor12+

constructor(fillStyle?: EffectFillStyle)

A constructor used to create a **HierarchicalSymbolEffect** instance, which comes with a hierarchical animation effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fillStyle | [EffectFillStyle](#effectfillstyle12) | No | 
Effect fill style.

Default value: **EffectFillStyle.CUMULATIVE**

 |

#### AppearSymbolEffect12+

Inherits from **SymbolEffect**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | Yes | 
Effect scope.

Default value: **EffectScope.LAYER**

 |

#### \[h2\]constructor12+

constructor(scope?: EffectScope)

A constructor used to create an **AppearSymbolEffect** instance, which comes with an appear animation effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | 
Effect scope.

Default value: **EffectScope.LAYER**

 |

#### DisappearSymbolEffect12+

Inherits from **SymbolEffect**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | Yes | 
Effect scope.

Default value: **EffectScope.LAYER**

 |

#### \[h2\]constructor12+

constructor(scope?: EffectScope)

A constructor used to create a **DisappearSymbolEffect** instance, which comes with a disappear animation effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | 
Effect scope.

Default value: **EffectScope.LAYER**

 |

#### BounceSymbolEffect12+

Inherits from **SymbolEffect**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

## Attributes

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | Yes | 
Effect scope.

Default value: **EffectScope.LAYER**

 |
| direction | [EffectDirection](#effectdirection12) | No | Yes | 

Effect direction.

Default value: **EffectDirection.DOWN**

 |

#### \[h2\]constructor12+

constructor(scope?: EffectScope, direction?: EffectDirection)

A constructor used to create a **BounceSymbolEffect** instance, which comes with a bounce animation effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | 
Effect scope.

Default value: **EffectScope.LAYER**

 |
| direction | [EffectDirection](#effectdirection12) | No | 

Effect direction.

Default value: **EffectDirection.DOWN**

 |

#### ReplaceSymbolEffect12+

Inherits from **SymbolEffect**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### \[h2\]Attributes

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | Yes | 
Effect scope.

Default value: **EffectScope.LAYER**

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| replaceType20+ | [ReplaceEffectType](#replaceeffecttype20) | No | Yes | 

Replacement effect type.

Default value: **ReplaceEffectType.SEQUENTIAL**.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### \[h2\]constructor12+

constructor(scope?: EffectScope)

A constructor used to create a **ReplaceSymbolEffect** instance, which comes with a replace animation effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | 
Effect scope.

Default value: **EffectScope.LAYER**

 |

#### \[h2\]constructor20+

constructor(scope?: EffectScope, replaceType?: ReplaceEffectType)

A constructor used to create a **ReplaceSymbolEffect** instance, which comes with a replace animation effect. The replace effect type can be specified.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scope | [EffectScope](#effectscope12) | No | 
Effect scope.

Default value: **EffectScope.LAYER**

 |
| replaceType | [ReplaceEffectType](#replaceeffecttype20) | No | 

Replacement effect type.

Default value: **ReplaceEffectType.SEQUENTIAL**

 |

#### SymbolEffectStrategy11+

Enumerates symbol effect types. Once applied, the symbol effect becomes active instantly, eliminating the need for triggering.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | No effect (default value). |
| SCALE | 1 | Scale effect as a whole. |
| HIERARCHICAL | 2 | Hierarchical effect. |

#### SymbolRenderingStrategy11+

Enumerates the rendering modes.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SINGLE | 0 | 
Single-color mode (default value).

The default color is black.

You can set one or multiple colors, but only the first color will be applied.

 |
| MULTIPLE\_COLOR | 1 | 

Multi-color mode.

A maximum of three colors can be set. If only one color is set, it updates the color of the first layer, leaving other colors at their default values.

The sequence of color settings matches the layering order of the symbol; any colors beyond the number of symbol layers will not take effect.

Only color values are accepted. Opacity settings do not take effect.

 |
| MULTIPLE\_OPACITY | 2 | 

Layered mode.

The default color is black. You can set one or multiple colors, but only the first color will be applied.

Opacity is predefined for the layers: 100% for the first layer, 50% for the second layer, and 20% for the third layer.

 |

#### SymbolEffect12+

Defines the **SymbolEffect** class.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### PulseSymbolEffect12+

Inherits from **SymbolEffect**.

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### EffectDirection12+

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| DOWN | 0 | The symbol scales down and then returns to its original size. |
| UP | 1 | The symbol scales up and then returns to its original size. |

#### EffectScope12+

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| LAYER | 0 | Layered mode. |
| WHOLE | 1 | Whole mode. |

#### EffectFillStyle12+

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| CUMULATIVE | 0 | Cumulative style. |
| ITERATIVE | 1 | Iterative style. |

#### ReplaceEffectType20+

Enumerates symbol replacement effect types.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| SEQUENTIAL | 0 | Sequential replacement: The current symbol disappears before a new symbol appears. This is the default symbol replacement effect type. |
| CROSS\_FADE | 1 | Cross-fade transition effect: The current symbol fades out while a new symbol fades in simultaneously. |
| SLASH\_OVERLAY | 2 | Slash overlay effect: The current symbol is replaced with a symbol featuring diagonal slash, typically indicating disabled state. |

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Setting Rendering and Effect Strategies

This example demonstrates different rendering and effect strategies using [renderingStrategy](#renderingstrategy) and [effectStrategy](#effectstrategy), available since API version 11.

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Row() {
        Column() {
          Text("Light")
          SymbolGlyph($r('sys.symbol.ohos\_trash'))
            .fontWeight(FontWeight.Lighter)
            .fontSize(96)
        }

        Column() {
          Text("Normal")
          SymbolGlyph($r('sys.symbol.ohos\_trash'))
            .fontWeight(FontWeight.Normal)
            .fontSize(96)
        }

        Column() {
          Text("Bold")
          SymbolGlyph($r('sys.symbol.ohos\_trash'))
            .fontWeight(FontWeight.Bold)
            .fontSize(96)
        }
      }

      Row() {
        Column() {
          Text("Single-color mode")
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.SINGLE)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }

        Column() {
          Text("Multi-color mode")
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_COLOR)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }

        Column() {
          Text ("Layered mode")
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_OPACITY)
            .fontColor(\[Color.Black, Color.Green, Color.White\])
        }
      }

      Row() {
        Column() {
          Text("No effect")
          SymbolGlyph($r('sys.symbol.ohos\_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.NONE)
        }

        Column() {
          Text("Overall scale effect")
          SymbolGlyph($r('sys.symbol.ohos\_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.SCALE)
        }

        Column() {
          Text("Hierarchical effect")
          SymbolGlyph($r('sys.symbol.ohos\_wifi'))
            .fontSize(96)
            .effectStrategy(SymbolEffectStrategy.HIERARCHICAL)
        }
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/A7MfjmGnRty4BNyXTJsJaw/en-us_image_0000002537925634.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B55BDBE6AE5401F1721469CDEA4B1A8519314FEB44FE119F2E67D85C6971A9E)

## Example 2: Setting Symbol and Shadow Effects

This example demonstrates various symbol effects using the [symbolEffect](#symboleffect12) attribute (available since API version 12) and shadow effects with [symbolShadow](#symbolshadow20) (available since API version 20).

// xxx.ets
@Entry
@Component
struct Index {
  @State isActive: boolean = true;
  @State triggerValueReplace: number = 0;
  @State triggerValueReplace1: number = 0;
  @State triggerValueReplace2: number = 0;
  @State renderMode: number = 1;

  replaceFlag: boolean = true;
  replaceFlag1: boolean = true;
  replaceFlag2: boolean = true;

  options: ShadowOptions = {
    radius: 10.0,
    color: Color.Blue,
    offsetX: 10,
    offsetY: 10,
  };

  build() {
    Column() {
      Row() {
        Column() {
          Text("Variable color effect")
          SymbolGlyph($r('sys.symbol.ohos\_wifi'))
            .fontSize(96)
            .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
          Button(this.isActive ? 'Stop' : 'Play')
            .onClick(() => {
              this.isActive = !this.isActive;
            })
        }
        .margin({ right: 20 })
        Column() {
          Text("Replacement effect")
          SymbolGlyph(this.replaceFlag ? $r('sys.symbol.checkmark\_circle') : $r('sys.symbol.repeat\_1'))
            .fontSize(96)
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE), this.triggerValueReplace)
          Button('Trigger')
            .onClick(() => {
              this.replaceFlag = !this.replaceFlag;
              this.triggerValueReplace = this.triggerValueReplace + 1;
            })
        }
        .margin({ right: 20 })
      }

      Row() {
        Column() {
          Text("Slash overlay")
          SymbolGlyph(this.replaceFlag1 ? $r('sys.symbol.eye\_slash') : $r('sys.symbol.eye'))
            .fontSize(96)
            .renderingStrategy(this.renderMode)
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.LAYER, ReplaceEffectType.SLASH\_OVERLAY), this.triggerValueReplace1)
          Button('Trigger')
            .onClick(() => {
              this.replaceFlag1 = !this.replaceFlag1;
              this.triggerValueReplace1 = this.triggerValueReplace1 + 1;
            })
        }
        .margin({ right: 20 })
        Column() {
          Text("Cross-fade transition")
          SymbolGlyph(this.replaceFlag2 ? $r('sys.symbol.checkmark\_circle') : $r('sys.symbol.repeat\_1'))
            .fontSize(96)
            .symbolEffect(new ReplaceSymbolEffect(EffectScope.WHOLE, ReplaceEffectType.CROSS\_FADE), this.triggerValueReplace2)
          Button('Trigger')
            .onClick(() => {
              this.replaceFlag2 = !this.replaceFlag2;
              this.triggerValueReplace2 = this.triggerValueReplace2 + 1;
            })
        }
        .margin({ right: 20 })
        Column() {
          Text("Shadow effect")
          SymbolGlyph($r('sys.symbol.ohos\_wifi'))
            .fontSize(96)
            .symbolEffect(new HierarchicalSymbolEffect(EffectFillStyle.ITERATIVE), this.isActive)
            .symbolShadow(this.options)
          Button(this.isActive ? 'Stop' : 'Play')
            .onClick(() => {
              this.isActive = !this.isActive;
            })
        }
        .margin({ right: 20 })
      }
    }
    .margin({
      left: 45,
      top: 50
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/BU1-6jKgRdCjR-UiZIdCWw/en-us_image_0000002568685411.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=664F709AB7DBD13F33E1AB0081CD784E07538218E1E5C55140461D62C60A6A02)

## Example 3: Setting Gradient Color Effects

This example demonstrates how to apply gradient colors to **SymbolGlyph** components using the [shaderStyle](#shaderstyle20) API, available since API version 20.

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  linearGradientOptions1: LinearGradientOptions = {
    angle: 45,
    colors: \[\[Color.Red, 0.0\], \[Color.Blue, 0.3\], \[Color.Green, 0.5\]\]
  };

  linearGradientOptions2: LinearGradientOptions = {
    direction: GradientDirection.LeftTop,
    colors: \[\[Color.Red, 0.0\], \[Color.Blue, 0.3\], \[Color.Green, 0.5\]\],
    repeating: true,
  };

  radialGradientOptions: RadialGradientOptions = {
    center: \["50%", "50%"\],
    radius: "20%",
    colors: \[\[Color.Red, 0.0\], \[Color.Blue, 0.3\], \[Color.Green, 0.5\]\],
    repeating: true,
  };

  build() {
    Column() {
      Row() {
        Column() {
          Text('Linear gradient with 45° angle')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .shaderStyle(\[new LinearGradientStyle(this.linearGradientOptions1)\])
        }
        .margin({ right: 20 })
        Column() {
          Text('Linear gradient from LeftTop')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .shaderStyle(\[new LinearGradientStyle(this.linearGradientOptions2)\])
        }
        .margin({ right: 20 })
      }

      Row() {
        Column() {
          Text('Radial gradient')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .shaderStyle(\[new RadialGradientStyle(this.radialGradientOptions)\])
        }
        .margin({ right: 20 })
        Column() {
          Text('Solid color')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .shaderStyle(\[new ColorShaderStyle(Color.Red)\])
        }
        .margin({ right: 20 })
        Column() {
          Text('Linear and radial gradient')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .shaderStyle(\[
              new LinearGradientStyle(this.linearGradientOptions2),
              new LinearGradientStyle(this.linearGradientOptions2),
              new RadialGradientStyle(this.radialGradientOptions)
            \])
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_OPACITY)
        }
        .margin({ right: 20 })
      }

      Row() {
        Column() {
          Text('Single-layer array gradient')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .shaderStyle(\[
              new LinearGradientStyle(this.linearGradientOptions2),
            \])
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_OPACITY)
        }.margin({ right: 20 })

        Column() {
          Text('Non-array covers all')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .shaderStyle(new RadialGradientStyle(this.radialGradientOptions))
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_OPACITY)
        }.margin({ right: 20 })

        Column() {
          Text('First layer is default')
            .fontSize(18)
            .fontColor(0xCCCCCC)
            .textAlign(TextAlign.Center)
          SymbolGlyph($r('sys.symbol.ohos\_folder\_badge\_plus'))
            .fontSize(96)
            .shaderStyle(\[
              undefined,
              new LinearGradientStyle(this.linearGradientOptions2),
            \])
            .renderingStrategy(SymbolRenderingStrategy.MULTIPLE\_OPACITY)
        }.margin({ right: 20 })
      }
    }
    .margin({
      left: 20,
      top: 50
    })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/5rg4t92YRNyCEr_3vuwmLg/en-us_image_0000002568765421.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062242Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB8492963595F1227ABCC44719AA8A11BA364B54EE4837215E5F7CA3DED3293A)
