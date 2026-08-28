# Image Effect

Image effects include blur, shadow, spherical effect, and much more.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/f4DFGlRFStaFgsmUZDHaDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EF7A9D0E0E6D4E5F8D59C0B401A869640D227383A1688840B523E3B68742E19)

The feature is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### blur

blur(value: number, options?: BlurOptions): T

Applies a foreground blur effect to the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Foreground blur effect to apply to the component. The input parameter is the blur radius. The larger the radius is, the more blurred the content is. If the value is **0**, the content is not blurred. |
| options11+ | [BlurOptions](../foreground-blur/document.md#bluroptions11) | No | Grayscale parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### blur18+

blur(blurRadius: Optional<number>, options?: BlurOptions): T

Applies a foreground blur effect to the component. Compared to [blur](#blur), the **blurRadius** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| blurRadius | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Foreground blur effect to apply to the component. The input parameter is the blur radius. The larger the radius is, the more blurred the content is. If the value is **0**, the content is not blurred.

If **blurRadius** is set to **undefined**, the previous value is retained.

 |
| options | [BlurOptions](../foreground-blur/document.md#bluroptions11) | No | Grayscale parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### blur19+

blur(blurRadius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T

Applies a foreground blur effect to the component. Compared to [blur18+](#blur18), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments.

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| blurRadius | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Foreground blur effect to apply to the component. The input parameter is the blur radius. The larger the radius is, the more blurred the content is. If the value is **0**, the content is not blurred.

If **blurRadius** is set to **undefined**, the previous value is retained.

 |
| options | [BlurOptions](../foreground-blur/document.md#bluroptions11) | No | Grayscale parameters. |
| sysOptions | [SystemAdaptiveOptions](../../basic-attributes/background/document.md#systemadaptiveoptions19) | No | 

System adaptive adjustment options.

Default value: **{ disableSystemAdaptation: false }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### shadow

shadow(value: ShadowOptions | ShadowStyle): T

Applies a shadow effect to the component.

**Widget capability**: Since API version 9, this API is supported in ArkTS widgets. Yet, the [ShadowStyle](#shadowstyle10) type is not supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ShadowOptions](#shadowoptions) | [ShadowStyle](#shadowstyle10)10+ | Yes | 
Shadow of the component.

When the value type is **ShadowOptions**, the blur radius, shadow color, and offset along the x-axis and y-axis can be specified.

When the value type is **ShadowStyle**, the shadow style can be specified.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### shadow18+

shadow(options: Optional<ShadowOptions | ShadowStyle>): T

Applies a shadow effect to the component. Compared to [shadow](#shadow), the **options** parameter supports the **undefined** type.

**Widget capability**: Since API version 18, this API is supported in ArkTS widgets. Yet, the [ShadowStyle](#shadowstyle10) type is not supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[ShadowOptions](#shadowoptions) | [ShadowStyle](#shadowstyle10)\> | Yes | 
Shadow of the component.

When the value type is **ShadowOptions**, the blur radius, shadow color, and offset along the x-axis and y-axis can be specified.

When the value type is **ShadowStyle**, the shadow style can be specified.

If **options** is **undefined**, the component reverts to its original effect with no shadow.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### grayscale

grayscale(value: number): T

Applies a grayscale effect to the component. The grayscale rendering of the upper layer will overlay that of lower-layer child components. If this API is not used, there will be no change by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Grayscale conversion ratio of the component. If the value is **1.0**, the component is completely converted to grayscale. If the value is **0.0**, the component remains unchanged. Between **0** and **1**, the value applies a linear multiplier on the grayscale effect.

Value range: \[0.0, 1.0\]

**NOTE**

A value less than **0.0** evaluates to the value **0.0**. A value greater than **1.0** evaluates to the value **1.0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### grayscale18+

grayscale(grayscale: Optional<number>): T

Applies a grayscale effect to the component. The grayscale rendering of the upper layer will overlay that of lower-layer child components. If this API is not used, there will be no change by default. Compared to [grayscale](#grayscale), the **grayscale** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| grayscale | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Grayscale conversion ratio of the component. If the value is **1.0**, the component is completely converted to grayscale. If the value is **0.0**, the component remains unchanged. Between **0** and **1**, the value applies a linear multiplier on the grayscale effect.

Value range: \[0.0, 1.0\]

**NOTE**

A value less than **0.0** evaluates to the value **0.0**. A value greater than **1.0** evaluates to the value **1.0**.

If **grayscale** is set to **undefined**, the default value **0.0** is used, which means the component reverts to its original effect with no grayscale.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### brightness

brightness(value: number): T

Applies a brightness effect to the component. If this API is not used, there will be no change by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Brightness effect of the component. **1**: No brightness adjustment. Less than 1.0: decreases brightness. 0 or less: Complete black. Greater than 1: increases brightness. 2 or greater: complete white.

Value range: \[0, +∞)

Recommended value range: \[0, 2\]

**NOTE**

A value less than 0 evaluates to the value **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### brightness18+

brightness(brightness: Optional<number>): T

Applies a brightness effect to the component. If this API is not used, there will be no change by default. Compared with [brightness](#brightness), this API supports the **undefined** type for the **brightness** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| brightness | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Brightness effect of the component. **1**: No brightness adjustment. Less than 1.0: decreases brightness. 0 or less: Complete black. Greater than 1: increases brightness. 2 or greater: complete white.

Value range: \[0, +∞)

Recommended value range: \[0, 2\]

**NOTE**

A value less than 0 evaluates to the value **0**.

If **brightness** is **undefined**, the brightness level is reset to **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### saturate

saturate(value: number): T

Applies a saturation effect to the component. If this API is not used, there will be no change by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Saturation of the component. The saturation is the ratio of the chromatic component to the achromatic component (gray) in a color. If the value is **1**, the original image is displayed. If the value is greater than **1**, a higher percentage of the chromatic component indicates a higher saturation. If the value is less than **1**, a higher percentage of the achromatic component indicates a lower saturation.

Recommended value range: \[0, 50)

**NOTE**

A value less than 0 evaluates to the value **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### saturate18+

saturate(saturate: Optional<number>): T

Applies a saturation effect to the component. If this API is not used, there will be no change by default. Compared to [saturate](#saturate), the **saturate** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| saturate | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Saturation of the component. The saturation is the ratio of the chromatic component to the achromatic component (gray) in a color. If the value is **1**, the original image is displayed. If the value is greater than **1**, a higher percentage of the chromatic component indicates a higher saturation. If the value is less than **1**, a higher percentage of the achromatic component indicates a lower saturation.

Recommended value range: \[0, 50)

**NOTE**

A value less than 0 evaluates to the value **0**.

If **saturate** is **undefined**, the saturation effect is reset to **1.0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### contrast

contrast(value: number): T

Applies a contrast effect to the component. If this API is not used, there will be no change by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Contrast of the component. The input parameter is a contrast value. If the value is **1**, the source image is displayed. If the value is greater than 1, a larger value indicates a higher contrast and a clearer image. If the value is less than 1, a smaller value indicates a lower contrast is. If the value is **0**, the image becomes all gray.

Recommended value range: \[0, 10)

**NOTE**

A value less than 0 evaluates to the value **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### contrast18+

contrast(contrast: Optional<number>): T

Applies a contrast effect to the component. If this API is not used, there will be no change by default. Compared to [contrast](#contrast), the **contrast** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| contrast | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Contrast of the component. The input parameter is a contrast value. If the value is **1**, the source image is displayed. If the value is greater than 1, a larger value indicates a higher contrast and a clearer image. If the value is less than 1, a smaller value indicates a lower contrast is. If the value is **0**, the image becomes all gray.

Recommended value range: \[0, 10)

**NOTE**

A value less than 0 evaluates to the value **0**.

If **contrast** is **undefined**, the contrast effect is reset to **1.0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### invert

invert(value: number | InvertOptions): T

Inverts an image.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | [InvertOptions](#invertoptions11)11+ | Yes | 
How an image is inverted.

When the input parameter is a number: If the value is **1**, the component is completely inverted. If the value is **0**, the component remains unchanged.

Value range: \[0, 1\].

A value less than 0 evaluates to the value **0**. A value larger than 1 is treated as **1**.

If the value is of the InvertOptions type, the grayscale value of the background color is compared with the threshold range. If the grayscale value is greater than the upper bound of the threshold range, the **high** value is used. If the grayscale value is less than the lower bound of the threshold range, the **low** value is used. If the grayscale value is within the threshold range, the background color changes linearly from high to low.

**NOTE**

The number and InvertOptions parameter types produce different inversion effects. When you switch parameter types, previous effects persist and both effects coexist. Use consistent parameter types for predictable results.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### invert18+

invert(options: Optional<number | InvertOptions>): T

Inverts an image. Compared with [invert](#invert), this API supports the **undefined** type for the **options** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number | [InvertOptions](#invertoptions11)11+\> | Yes | 
How an image is inverted.

When the input parameter is a number: If the value is **1**, the component is completely inverted. If the value is **0**, the component remains unchanged.

Value range: \[0, 1\].

A value less than 0 evaluates to the value **0**. A value larger than 1 is treated as **1**.

If the value is of the InvertOptions type, the grayscale value of the background color is compared with the threshold range. If the grayscale value is greater than the upper bound of the threshold range, the **high** value is used. If the grayscale value is less than the lower bound of the threshold range, the **low** value is used. If the grayscale value is within the threshold range, the background color changes linearly from high to low.

If **options** is **undefined**, the component reverts to its original effect.

**NOTE**

The number and InvertOptions parameter types produce different inversion effects. When you switch parameter types, previous effects persist and both effects coexist. Use consistent parameter types for predictable results.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### sepia

sepia(value: number): T

Converts the image to a sepia tone, reducing color intensity to create a warm, vintage image style.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Intensity of the sepia filter. A value of 1 results in a completely sepia image, values less than or equal to 0 leave the image unchanged, and values greater than 1 increase the color shift, making the image brighter and more yellow or red, though this is not a standard sepia effect.

Value range: \[0, +∞). Recommended value range: (0, 1\].

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### sepia18+

sepia(sepia: Optional<number>): T

Converts the image to a sepia tone, reducing color intensity to create a warm, vintage image style. Compared to [sepia](#sepia), this API supports the **undefined** type for the **sepia** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| sepia | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Intensity of the sepia filter. A value of 1 results in a completely sepia image, values less than or equal to 0 leave the image unchanged, and values greater than 1 increase the color shift, making the image brighter and more yellow or red, though this is not a standard sepia effect.

If **sepia** is **undefined**, the component reverts to its original effect.

Value range: \[0, +∞). Recommended value range: (0, 1\].

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### hueRotate

hueRotate(value: number | string): T

Rotates the hue of the component. If this API is not used, there will be no change by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | string | Yes | 
Hue rotation angle of the component.

Value range: (-∞, +∞)

**NOTE**

A rotation of 360 degrees leaves the color unchanged. A rotation of 180 degrees and then -180 degrees also leaves the color unchanged. When the data type is number, the value **90** is equivalent to **'90deg'**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### hueRotate18+

hueRotate(rotation: Optional<number | string>): T

Rotates the hue of the component. If this API is not used, there will be no change by default. Compared to [hueRotate](#huerotate), the **rotation** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotation | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number | string> | Yes | 
Hue rotation angle of the component.

Value range: (-∞, +∞)

For the string type, the value must be a numeric string.

**NOTE**

A rotation of 360 degrees leaves the color unchanged. A rotation of 180 degrees and then -180 degrees also leaves the color unchanged. When the data type is number, the value **90** is equivalent to **'90deg'**.

If **sepia** is **undefined**, the component reverts to its original effect with no hue rotation.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### colorBlend

colorBlend(value: Color | string | Resource): T

Applies a color blend effect to the component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Color](../../../common-definitions/enums/document.md#color) | string | [Resource](../../../common-definitions/basic-types/document.md#resource) | Yes | Color to blend with the component. The value can be a string, for example, **'0x000000'** or **'rgba(0,0,0,1)'**. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### colorBlend18+

colorBlend(color: Optional<Color | string | Resource>): T

Applies a color blend effect to the component. Compared with [colorBlend](#colorblend), this API supports the **undefined** type for the **color** parameter.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Atomic service API**: This API can be used in atomic services since API version 18.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[Color](../../../common-definitions/enums/document.md#color) | string | [Resource](../../../common-definitions/basic-types/document.md#resource)\> | Yes | 
Color to blend with the component. The value can be a string, for example, **'0x000000'** or **'rgba(0,0,0,1)'**.

If **color** is **undefined**, the component reverts to its original effect with no color blending.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### linearGradientBlur12+

linearGradientBlur(value: number, options: LinearGradientBlurOptions): T

Applies a linear gradient foreground blur effect to the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Blur radius. A larger value indicates a higher blur degree. If the value is 0, the content is not blurred.

Value range: \[0, 1000\]

 |
| options | [LinearGradientBlurOptions](#lineargradientbluroptions12) | Yes | 

Linear gradient blur effect.

The linear gradient blur effect is defined by [fractionStops](#lineargradientbluroptions12) and [direction](#lineargradientbluroptions12).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### linearGradientBlur18+

linearGradientBlur(blurRadius: Optional<number>, options: Optional<LinearGradientBlurOptions>): T

Applies a linear gradient foreground blur effect to the component. Compared with [linearGradientBlur12+](#lineargradientblur12), this API supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| blurRadius | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Blur radius. A larger value indicates a higher blur degree. If the value is 0, the content is not blurred.

Value range: \[0, 1000\]

If **blurRadius** is **undefined**, the gradient blur effect reverts to **0**.

 |
| options | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[LinearGradientBlurOptions](#lineargradientbluroptions12)\> | Yes | 

Linear gradient blur effect.

If **options** is **undefined**, the gradient blur effect reverts to **0**.

The linear gradient blur effect is defined by [fractionStops](#lineargradientbluroptions12) and [direction](#lineargradientbluroptions12).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### renderGroup10+

renderGroup(value: boolean): T

Sets whether to form a render group. A render group means that the subtree composed of the current component and its child components is first rendered on an offscreen canvas and then composited with the parent component. Setting a render group allows the system to cache the rendering result, improving performance. However, if components within the render group are frequently updated, cache invalidation may lead to performance degradation. Additionally, when a render group is set and the current component's opacity is not **1**, the rendering effect may differ.

If this attribute is not set, no render group is formed by default.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the current component and its child components form a render group.

**false**: no. Rendering is performed directly without offscreen rendering.

**true**: yes. The current component and its child components are rendered offscreen first and then composited with the parent component.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### renderGroup18+

renderGroup(isGroup: Optional<boolean>): T

Sets whether to form a render group. A render group means that the subtree composed of the current component and its child components is first rendered on an offscreen canvas and then composited with the parent component. Setting a render group allows the system to cache the rendering result, improving performance. However, if components within the render group are frequently updated, cache invalidation may lead to performance degradation. Additionally, when a render group is set and the current component's opacity is not **1**, the rendering effect may differ.

Compared with [renderGroup10+](#rendergroup10), this API supports the **undefined** type for the **isGroup** parameter.

If this attribute is not set, no render group is formed by default.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| isGroup | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether the current component and its child components form a render group.

**false**: no. Rendering is performed directly without offscreen rendering.

**true**: yes. The current component and its child components are rendered offscreen first and then composited with the parent component.

If **isGroup** is set to **undefined**, no render group is formed.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### blendMode11+

blendMode(value: BlendMode, type?: BlendApplyType): T

Defines how the component's content (including the content of it child components) is blended with the existing content on the canvas (possibly offscreen canvas) below.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BlendMode](#blendmode11) | Yes | 
Blend mode.

Default value: **BlendMode.NONE**

**NOTE**

When **BlendMode.NONE** is used, the blend effect is **BlendMode.SRC\_OVER** by default, and **BlendApplyType** does not take effect.

 |
| type | [BlendApplyType](#blendapplytype11) | No | 

Whether the blend mode is implemented offscreen.

Default value: **BlendApplyType.FAST**

**NOTE**

1\. **BlendApplyType.FAST**: The blend mode is not implemented offscreen.

2\. **BlendApplyType.OFFSCREEN**: An offscreen canvas of the size of the current component is created. The content of the current component (including child components) is then drawn onto the offscreen canvas, and blended with the existing content on the canvas below using the specified blend mode. This approach may cause issues with screen capture for APIs such as [linearGradientBlur12+](#lineargradientblur12), [backgroundEffect](../../basic-attributes/background/document.md#backgroundeffect11), [brightness](#brightness), and [blur](#blur).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### blendMode18+

blendMode(mode: Optional<BlendMode>, type?: BlendApplyType): T

Defines how the component's content (including the content of it child components) is blended with the existing content on the canvas (possibly offscreen canvas) below. Compared to [blendMode11+](#blendmode11), the **mode** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[BlendMode](#blendmode11)\> | Yes | 
Blend mode.

Default value: **BlendMode.NONE**

If **mode** is **undefined**, the component reverts to its original effect of not enabling offscreen rendering as a whole before blending with the parent component.

**NOTE**

When **BlendMode.NONE** is used, the blend effect is **BlendMode.SRC\_OVER** by default, and **BlendApplyType** does not take effect.

 |
| type | [BlendApplyType](#blendapplytype11) | No | 

Whether the blend mode is implemented offscreen.

Default value: **BlendApplyType.FAST**

**NOTE**

1\. **BlendApplyType.FAST**: The blend mode is not implemented offscreen.

2\. **BlendApplyType.OFFSCREEN**: An offscreen canvas of the size of the current component is created. The content of the current component (including child components) is then drawn onto the offscreen canvas, and blended with the existing content on the canvas below using the specified blend mode. This approach may cause issues with screen capture for APIs such as [linearGradientBlur12+](#lineargradientblur12), [backgroundEffect](../../basic-attributes/background/document.md#backgroundeffect11), [brightness](#brightness), and [blur](#blur).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### BlendApplyType11+

Defines how to apply the specified blend mode to the content of a view.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FAST | 0 | The content of the view is blended in sequence on the target image. |
| OFFSCREEN | 1 | The content of the component and its child components are drawn on the offscreen canvas, and then blended with the existing content on the canvas. |

#### useShadowBatching11+

useShadowBatching(value: boolean): T

Sets whether to render child node shadows at the same layer, enabling shadow overlap within the same layer.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to render child node shadows at the same layer.

Default value: **false**

**true**: Child node shadows are rendered at the same layer without overlapping.

**false**: Child node shadows are rendered separately, with later shadows overlapping earlier ones.

**NOTE**

1\. This feature is disabled by default. When child nodes have large shadow radius and overlapping areas, later-rendered shadows cover earlier ones. Enabling this feature renders all child shadows simultaneously without overlap.

2\. Avoid nesting **useShadowBatching**. When used in nested mode, **useShadowBatching** takes effect for the current child node only and cannot be recursively used.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### useShadowBatching18+

useShadowBatching(use: Optional<boolean>): T

Sets whether to render child node shadows at the same layer, enabling shadow overlap within the same layer. Compared with [useShadowBatching11+](#useshadowbatching11), this API supports the **undefined** type for the **use** parameter.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| use | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to render child node shadows at the same layer.

Default value: **false**

**true**: Child node shadows are rendered at the same layer without overlapping.

**false**: Child node shadows are rendered separately, with later shadows overlapping earlier ones.

**NOTE**

1\. This feature is disabled by default. When child nodes have large shadow radius and overlapping areas, later-rendered shadows cover earlier ones. Enabling this feature renders all child shadows simultaneously without overlap.

2\. Avoid nesting **useShadowBatching**. When used in nested mode, **useShadowBatching** takes effect for the current child node only and cannot be recursively used.

If **use** is **undefined**, the component reverts to its original effect of not using shadow overlapping.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### sphericalEffect12+

sphericalEffect(value: number): T

Applies a spherical effect to the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Spherical degree of the component.

The value ranges from 0 to 1.

**NOTE**

1\. If the value is **0**, the component remains unchanged. If the value is 1, the component is completely spherical. Between **0** and **1**, a larger value indicates a higher spherical degree.

A value less than 0 is handled as the value **0**. A value greater than 1 is handled as the value **1**.

2\. The component's shadow and outer stroke do not support spherical effects.

3\. If the value is greater than 0, the component is frozen, and its content is drawn to the transparent offscreen buffer. To update the component attributes, set the value to **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### sphericalEffect18+

sphericalEffect(effect: Optional<number>): T

Applies a spherical effect to the component. Compared to [sphericalEffect12+](#sphericaleffect12), the **effect** parameter supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effect | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Spherical degree of the component.

The value ranges from 0 to 1.

**NOTE**

1\. If the value is **0**, the component remains unchanged. If the value is 1, the component is completely spherical. Between **0** and **1**, a larger value indicates a higher spherical degree.

A value less than 0 is handled as the value **0**. A value greater than 1 is handled as the value **1**.

2\. The component's shadow and outer stroke do not support spherical effects.

3\. If **effect** is set to a positive number, the component is frozen, and its content is drawn to the transparent offscreen buffer. To update the component attributes, set **effect** to **0**.

If **effect** is **undefined**, the spherical degree reverts to **0**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### lightUpEffect12+

lightUpEffect(value: number): T

Applies a light up effect to the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Light up degree of the component.

The value ranges from 0 to 1.

If the value is **0**, the component is dark. If the value is **1**, the component is fully illuminated. Between **0** and **1**, a larger value indicates higher luminance. A value less than 0 is handled as the value **0**. A value greater than 1 is handled as the value **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### lightUpEffect18+

lightUpEffect(degree: Optional<number>): T

Applies a light up effect to the component. Compared to [lightUpEffect12+](#lightupeffect12), the **degree** parameter supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| degree | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<number> | Yes | 
Light up degree of the component.

The value ranges from 0 to 1.

If the value is **0**, the component is dark. If the value is **1**, the component is fully illuminated. Between **0** and **1**, a larger value indicates higher luminance. A value less than 0 is handled as the value **0**. A value greater than 1 is handled as the value **1**.

If **degree** is **undefined**, the light up degree reverts to **1**.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### pixelStretchEffect12+

pixelStretchEffect(options: PixelStretchEffectOptions): T

Applies a pixel stretch effect to the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [PixelStretchEffectOptions](#pixelstretcheffectoptions10) | Yes | 
Pixel stretch effect options.

The value includes the length by which a pixel is stretched toward the four edges.

**NOTE**

1\. If the length is a positive value, the original image is stretched, and the image size increases. The edge pixels grow by the set length toward the top, bottom, left, and right edges.

2\. If the length is a negative value, the original image shrinks as follows, but the image size remains unchanged:

Shrinking mode:

(1) The image shrinks from the four edges by the absolute value of length set through **options**.

(2) The image is stretched back to the original size with edge pixels.

3\. Constraints on **options**:

(1) The length values for the four edges must be all positive or all negative. That is, the four edges are stretched or shrink at the same time in the same direction.

(2) The length values must all be a percentage or a specific value. Combined use of the percentage and specific value is not allowed.

If the input value is invalid, the image is displayed as {0, 0, 0, 0}, that is, the image remains unchanged.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### pixelStretchEffect18+

pixelStretchEffect(options: Optional<PixelStretchEffectOptions>): T

Applies a pixel stretch effect to the component. Compared to [pixelStretchEffect12+](#pixelstretcheffect12), the **options** parameter supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[PixelStretchEffectOptions](#pixelstretcheffectoptions10)\> | Yes | 
Pixel stretch effect options.

The value includes the length by which a pixel is stretched toward the four edges.

**NOTE**

1\. If the length is a positive value, the original image is stretched, and the image size increases. The edge pixels grow by the set length toward the top, bottom, left, and right edges.

2\. If the length is a negative value, the original image shrinks as follows, but the image size remains unchanged:

Shrinking mode:

(1) The image shrinks from the four edges by the absolute value of length set through **options**.

(2) The image is stretched back to the original size with edge pixels.

3\. Constraints on **options**:

(1) The length values for the four edges must be all positive or all negative. That is, the four edges are stretched or shrink at the same time in the same direction.

(2) The length values must all be a percentage or a specific value. Combined use of the percentage and specific value is not allowed.

If the input value is invalid, the image is displayed as {0, 0, 0, 0}, that is, the image remains unchanged.

If **options** is **undefined**, the component reverts to its original effect with no pixel stretch.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### PixelStretchEffectOptions10+

Describes the pixel stretch effect options.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 
Length by which a pixel is stretched towards the left edge of the image.

Default value: **0vp**

 |
| right | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Length by which a pixel is stretched towards the right edge of the image.

Default value: **0vp**

 |
| top | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Length by which a pixel is stretched towards the top edge of the image.

Default value: **0vp**

 |
| bottom | [Length](../../../common-definitions/basic-types/document.md#length) | No | Yes | 

Length by which a pixel is stretched towards the right edge of the image.

Default value: **0vp**

 |

#### systemBarEffect12+

systemBarEffect(): T

Applies a system bar effect to the component, which means to invert colors based on the background and add a blur.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### ShadowType10+

Shadow type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| COLOR | 0 | Color. |
| BLUR | 1 | Blur. |

#### ShadowOptions

Provides the shadow attributes, including the blur radius, color, and offset along the x-axis and y-axis.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| radius | number | [Resource](../../../common-definitions/basic-types/document.md#resource) | No | No | 
Blur radius of the shadow.

Value range: \[0, +∞)

Unit: px

**NOTE**

A value less than 0 evaluates to the value **0**.

To use a value in the unit of vp, you can use [vp2px](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert the value.

If **radius** is of the Resource type, its value must be of the number type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| type10+ | [ShadowType](#shadowtype10) | No | Yes | 

Shadow type.

Default value: **COLOR**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| color | [Color](../../../common-definitions/enums/document.md#color) | string | [Resource](../../../common-definitions/basic-types/document.md#resource)| [ColoringStrategy11+](../../../common-definitions/enums/document.md#coloringstrategy10) | No | Yes | 

Color of the shadow.

The default color is black.

**NOTE**

Since API version 11, this API supports **ColoringStrategy**, which cannot be used with ArkTS widgets or the [textShadow](../../../text-and-input/text/document.md#textshadow10) attribute.

With **ColoringStrategy**, the average color or primary color can be obtained, and the obtained color is applied to the shadow drawing area.

The **'average'** string can be used to trigger the mode for obtaining the average color, and the **'primary'** string for obtaining the primary color.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| offsetX | number | [Resource](../../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Offset of the shadow along the x-axis.

Default value: **0**

Unit: px

**NOTE**

To use a value in the unit of vp, you can use [vp2px](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert the value.

If **offsetX** is of the Resource type, its value must be of the number type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| offsetY | number | [Resource](../../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Offset of the shadow along the y-axis.

Default value: **0**

Unit: px

**NOTE**

To use a value in the unit of vp, you can use [vp2px](../../../../arkts-api/ui/ohos-arkui-uicontext-uicontext/class-uicontext/document.md#vp2px12) to convert the value.

If **offsetY** is of the Resource type, its value must be of the number type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| fill11+ | boolean | No | Yes | 

Whether to fill the inside of the component with shadow. **true**: Fill the inside of the component with shadow.

**false**: Do not fill the inside of the component with shadow.

Default value: **false**.

**NOTE**

This attribute does not take effect in [textShadow](../../../text-and-input/text/document.md#textshadow10).

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### ShadowStyle10+

Defines the shadow effect of a component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| OUTER\_DEFAULT\_XS | 0 | Mini shadow. |
| OUTER\_DEFAULT\_SM | 1 | Small shadow. |
| OUTER\_DEFAULT\_MD | 2 | Medium shadow. |
| OUTER\_DEFAULT\_LG | 3 | Large shadow. |
| OUTER\_FLOATING\_SM | 4 | Floating small shadow. |
| OUTER\_FLOATING\_MD | 5 | Floating medium shadow. |

#### BlendMode11+

Blend mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/4V1Sa2qESwKeSaADfHnaeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=35F1D6B90158894CF231E18199D0B21875BBBFF8D5FA11DDDCD8A86A70FB8E60)

In the **blendMode** enums, **s** indicates the source pixel, **d** indicates the target pixel, **sa** indicates the opacity of the source pixel, **da** indicates the opacity of the target pixel, **r** indicates the pixel after blending, and **ra** indicates the opacity of the pixel after blending.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0 | The top image is superimposed on the bottom image without any blending. |
| CLEAR | 1 | The target pixels covered by the source pixels are erased by being turned to completely transparent. |
| SRC | 2 | r = s: Only the source pixels are displayed. |
| DST | 3 | r = d: Only the target pixels are displayed. |
| SRC\_OVER | 4 | r = s + (1 - sa) \* d: The source pixels are blended based on opacity and cover the target pixels. |
| DST\_OVER | 5 | r = d + (1 - da) \* s: The target pixels are blended based on opacity and cover on the source pixels. |
| SRC\_IN | 6 | r = s \* da: Only the part of the source pixels that overlap with the target pixels is displayed. |
| DST\_IN | 7 | r = d \* sa: Only the part of the target pixels that overlap with the source pixels is displayed. |
| SRC\_OUT | 8 | r = s \* (1 - da): Only the part of the source pixels that do not overlap with the target pixels is displayed. |
| DST\_OUT | 9 | r = d \* (1 - sa): Only the part of the target pixels that do not overlap with the source pixels is displayed. |
| SRC\_ATOP | 10 | r = s \* da + d \* (1 - sa): The part of the source pixels that overlap with the target pixels is displayed and the part of the target pixels that do not overlap with the source pixels are displayed. |
| DST\_ATOP | 11 | r = d \* sa + s \* (1 - da): The part of the target pixels that overlap with the source pixels and the part of the source pixels that do not overlap with the target pixels are displayed. |
| XOR | 12 | r = s \* (1 - da) + d \* (1 - sa). The pixel is not displayed where the source pixel overlaps the target pixel, and the source pixel and target pixel are displayed where the source pixel does not overlap the target pixel. |
| PLUS | 13 | r = min(s + d, 1): New pixels resulting from adding the source pixels to the target pixels are displayed. |
| MODULATE | 14 | r = s \* d: New pixels resulting from multiplying the source pixels with the target pixels are displayed. |
| SCREEN | 15 | r = s + d - s \* d: Pixels are blended by adding the source pixels to the target pixels and subtracting the product of their multiplication. |
| OVERLAY | 16 | The MULTIPLY or SCREEN mode is used based on the target pixels. |
| DARKEN | 17 | rc = s + d - max(s \* da, d \* sa), ra = kSrcOver: When two colors overlap, whichever is darker is used. |
| LIGHTEN | 18 | rc = s + d - min(s \* da, d \* sa), ra = kSrcOver: The darker of the pixels (source and target) is used. |
| COLOR\_DODGE | 19 | The colors of the target pixels are lightened to reflect the source pixels. |
| COLOR\_BURN | 20 | The colors of the target pixels are darkened to reflect the source pixels. |
| HARD\_LIGHT | 21 | The MULTIPLY or SCREEN mode is used, depending on the source pixels. |
| SOFT\_LIGHT | 22 | The LIGHTEN or DARKEN mode is used, depending on the source pixels. |
| DIFFERENCE | 23 | rc = s + d - 2 \* (min(s \* da, d \* sa)), ra = kSrcOver: The final pixel is the result of subtracting the darker of the two pixels (source and target) from the lighter one. |
| EXCLUSION | 24 | rc = s + d - two(s \* d), ra = kSrcOver: The final pixel is similar to **DIFFERENCE**, but with less contrast. |
| MULTIPLY | 25 | r = s \* (1 - da) + d \* (1 - sa) + s \* d: The final pixel is the result of multiplying the source pixel by the target pixel. |
| HUE | 26 | The resultant image is created with the luminance and saturation of the source image and the hue of the target image. |
| SATURATION | 27 | The resultant image is created with the luminance and hue of the target image and the saturation of the source image. |
| COLOR | 28 | The resultant image is created with the saturation and hue of the source image and the luminance of the target image. |
| LUMINOSITY | 29 | The resultant image is created with the saturation and hue of the target image and the luminance of the source image. |

#### LinearGradientBlurOptions12+

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fractionStops | [FractionStop](#fractionstop12)\[\] | No | No | Gradient blur stops. The value is a set of binary arrays, each of which indicates \[blur degree, blur position\] and consists of numbers ranging from 0 to 1 (those less than 0 are treated as **0**, and those greater than 1 are treated as **1**). The blur positions in the arrays must be in strict ascending order. Noncompliance will be logged. For the blur settings to take effect, the number of binary arrays must be greater than or equal to 2. |
| direction | [GradientDirection](../../../common-definitions/enums/document.md#gradientdirection) | No | No | 
Gradient blur direction.

Default value:

GradientDirection.Bottom

 |

#### FractionStop12+

type FractionStop = \[ number, number \]

Defines a gradient blur stop.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Type | Description |
| :-- | :-- |
| \[ number, number \] | 
The first number indicates the opacity value. The value **1** indicates fully opaque, and **0** indicates fully transparent.

Value range: \[0, 1\].

The second number indicates the position in gradient . The value **1** indicates the end position, and **0** indicates the start position.

Value range: \[0, 1\].

 |

#### InvertOptions11+

Describes the options for inverting the foreground color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| low | number | No | No | 
Value when the background color is greater than the grayscale threshold.

Value range: \[0, 1\].

 |
| high | number | No | No | 

Value when the background color is less than the grayscale threshold.

Value range: \[0, 1\].

 |
| threshold | number | No | No | 

Grayscale threshold.

Value range: \[0, 1\].

 |
| thresholdRange | number | No | No | 

Threshold value range.

Value range: \[0, 1\].

**NOTE**

This range defines the upper and lower bounds of the grayscale threshold. The grayscale value changes linearly from high to low within the range.

 |

#### BackgroundImageOptions18+

Defines the background image options.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/ddjXl1uAS5qdCItRDRbItQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A89AA74431E0C2B767D57F31837ADECAC3B7C38E80279A83029E238F0A5B46C1)

Synchronously loading background images can lead to potential performance issues. For details, see [Image](../../../images-and-videos/image/document.md#image-1).

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| syncLoad | boolean | No | Yes | 
Whether to load the image synchronously. By default, the image is loaded asynchronously. During synchronous loading, the UI thread is blocked and the placeholder image is not displayed.

Default value: **false**

**false**: Asynchronously load the image.

**true**: Synchronously load the image.

 |
| repeat | [ImageRepeat](../../../common-definitions/enums/document.md#imagerepeat) | No | Yes | Repeat pattern of the background image. Default value: **ImageRepeat.NoRepeat**. |

#### freeze12+

freeze(value: boolean): T

Sets whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/P99W0X-YTfCSjC7zgXQ5dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78D20E64F5914A6AF512997CAC964DE5AF8F131C481727A17A439F1980BBDFF0)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes. If the opacity of the component is not 1, the drawing effect may vary depending on the value.

Default value: **false**

**true**: Freeze the component.

**false**: Do not freeze the component.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### freeze18+

freeze(freeze: Optional<boolean>): T

Sets whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes. Compared with [freeze](#freeze12), this API supports the **undefined** type for the **freeze** parameter.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/twwvz1ErTvWLTXHfoMj1UA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=633D7F94435B74CE1C60E034DAEFD6DB631B24A7634347D623325C7231ACB3B8)

This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| freeze | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<boolean> | Yes | 
Whether to freeze the component. When frozen, the component and its children are cached for repeated drawing after offscreen rendering, without updating internal attributes. If the opacity of the component is not 1, the drawing effect may vary depending on the value.

Default value: **false**

**true**: Freeze the component.

**false**: Do not freeze the component.

If **freeze** is set to **undefined**, the previous value is retained.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

## Example 1: Setting Different Image Attributes

This example applies different image effects.

// xxx.ets
@Entry
@Component
struct ImageEffectsExample {
  build() {
    Column({ space: 5 }) {
      // Apply the shadow effect.
      Text('shadow').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image'))
        .width('90%')
        .height(30)
        .shadow({
          radius: 10,
          color: Color.Green,
          offsetX: 20,
          offsetY: 20
        })

      // Add the internal shadow effect.
      Text('shadow').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image'))
        .width('90%')
        .height(30)
        .shadow({
          radius: 5,
          color: Color.Green,
          offsetX: 20,
          offsetY: 20,
          fill: true
        }).opacity(0.5)

      // Apply the grayscale effect. The grayscale value ranges from 0 to 1. The closer the grayscale value is to 1, the more obvious the grayscale effect is.
      Text('grayscale').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).grayscale(0.3)
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).grayscale(0.8)

      // Apply the brightness effect. The value 1 indicates no effects. If the value is less than 1, the brightness decreases. If the value is greater than 1, the brightness increases.
      Text('brightness').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).brightness(1.2)

      // Apply the saturation effect. If the value is 1, the source image is displayed.
      Text('saturate').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).saturate(2.0)
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).saturate(0.7)

      // Apply the contrast effect. If the value is 1, the source image is displayed. If the value is greater than 1, a larger value indicates a higher contrast and a clearer image. If the value is less than 1, a smaller value indicates a lower contrast is.
      Text('contrast').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).contrast(2.0)
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).contrast(0.8)

      // Invert the image.
      Text('invert').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).invert(0.2)
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).invert(0.8)

      // Apply the color blend effect.
      Text('colorBlend').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).colorBlend(Color.Green)
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).colorBlend(Color.Blue)

      // Convert the image color to sepia.
      Text('sepia').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).sepia(0.8)

      // Apply the hue rotation effect.
      Text('hueRotate').fontSize(15).fontColor(0xCCCCCC).width('90%')
      // Replace $r("app.media.image") with the image resource file you use.
      Image($r('app.media.image')).width('90%').height(30).hueRotate(90)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/rTzromutTWuE42byy7gK_g/en-us_image_0000002568765147.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00ACB13DB4A4D4ABE38AD296AA5D1C11E1BFFB56EDFC3F2735311BA6858017E7)

## Example 2: Applying a Linear Gradient Blur Effect

This example demonstrates how to apply a linear gradient blur effect on a component using [linearGradientBlur](#lineargradientblur12).

// xxx.ets
@Entry
@Component
struct ImageExample1 {
  // Replace $r('app.media.testlinearGradientBlurOrigin') with the resource file you use.
  private\_resource1: Resource = $r('app.media.testlinearGradientBlurOrigin')
  @State image\_src: Resource = this.private\_resource1

  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Image(this.image\_src)
            .blur(0) // Set the blur effect of the image to none (no blur applied).
            .linearGradientBlur(60,
              { fractionStops: \[\[0, 0\], \[0, 0.33\], \[1, 0.66\], \[1, 1\]\], direction: GradientDirection.Bottom })
        }
      }
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/Cbnpb2YxSqG6oXMyZHyBDw/en-us_image_0000002537765422.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36F19302D2E5083977780D98AFD318F85C2F190E2A99862753E2D0B5DB90DF2D)

## Example 3: Setting Offscreen Rendering Effect

This example demonstrates how to use [renderGroup](#rendergroup10) to set whether the component is rendered entirely offscreen and then composited with its parent component.

// xxx.ets
@Component
struct Component1 {
  @Prop renderGroupValue: boolean;

  build() {
    Row() {
      Row() {
        Row()
          .backgroundColor(Color.Black)
          .width(100)
          .height(100)
          .opacity(1)
      }
      .backgroundColor(Color.White)
      .width(150)
      .height(150)
      .justifyContent(FlexAlign.Center)
      .opacity(0.6)
      .renderGroup(this.renderGroupValue)
    }
    .backgroundColor(Color.Black)
    .width(200)
    .height(200)
    .justifyContent(FlexAlign.Center)
    .opacity(1)
  }
}

@Entry
@Component
struct RenderGroupExample {
  build() {
    Column() {
      Component1({ renderGroupValue: true })
        .margin(20)
      Component1({ renderGroupValue: false })
        .margin(20)
    }
    .width("100%")
    .height("100%")
    .alignItems(HorizontalAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/mcb7hGBGTTKkAvicrbIQJA/en-us_image_0000002537925362.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A529A48022EE6535BC7E1C22EC51923F12C6A85256F0182619D028D0A689440)

## Example 4: Blending the Current Component Content with Canvas Content

This example demonstrates how to blend the current component content with the canvas content below using [blendMode](#blendmode11).

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Text("blendMode")
        .fontSize(20)
        .fontWeight(FontWeight.Bold)
        .fontColor('#ffff0101')
      Row() {
        Circle()
          .width(200)
          .height(200)
          .fill(Color.Green)
          .position({ x: 50, y: 50 })
        Circle()
          .width(200)
          .height(200)
          .fill(Color.Blue)
          .position({ x: 150, y: 50 })
      }
      .blendMode(BlendMode.OVERLAY, BlendApplyType.OFFSCREEN)
      .alignItems(VerticalAlign.Center)
      .height(300)
      .width('100%')
    }
    .height('100%')
    .width('100%')
    // Replace $r("app.media.image") with the image resource file you use.
    .backgroundImage($r('app.media.image'))
    .backgroundImageSize(ImageSize.Cover)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/PC3VGbhhTmqxk1-y73FUNg/en-us_image_0000002568685139.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E05AB759C67DAB1FDA96BCDB1A36FB3334BD053283BED1041A3987322157FE40)

## Example 5: Inverting the Foreground Color

This example demonstrates how to achieve intelligent foreground color inversion using [InvertOptions](#invertoptions11).

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Stack() {
      Column()
      Stack() {
        // Replace $r("app.media.r") with the image resource file you use.
        // In this example, the images are arranged from left to right, and the color is from light to dark.
        Image($r('app.media.r')).width('100%')
        Column() {
          Column().width("100%").height(30).invert({
            low: 0,
            high: 1,
            threshold: 0.5,
            thresholdRange: 0.2
          })
          Column().width("100%").height(30).invert({
            low: 0.2,
            high: 0.5,
            threshold: 0.3,
            thresholdRange: 0.2
          })
        }
      }
      .width('100%')
      .height('100%')
    }
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/CsrqhO0QRDWrPfAlink1Xg/en-us_image_0000002568765149.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5424284BC6EEC3851E45F0A6C4A09B6FED02FC04AA94103F77E1532B5BB0751F)

## Example 6: Setting Non-Overlapping Same-Layer Shadows

This example demonstrates how to implement non-overlapping shadow effect within the same layer using [useShadowBatching](#useshadowbatching11) in combination with [shadow](#shadow).

// xxx.ets
@Entry
@Component
struct UseShadowBatchingExample {
  build() {
    Column() {
      Column({ space: 10 }) {
        Stack() {

        }
        .width('90%')
        .height(50)
        .margin({ top: 5 })
        .backgroundColor(0xFFE4C4)
        .shadow({
          radius: 120,
          color: Color.Green,
          offsetX: 0,
          offsetY: 0
        })
        .align(Alignment.TopStart)
        .shadow({
          radius: 120,
          color: Color.Green,
          offsetX: 0,
          offsetY: 0
        })

        Stack() {

        }
        .width('90%')
        .height(50)
        .margin({ top: 5 })
        .backgroundColor(0xFFE4C4)
        .align(Alignment.TopStart)
        .shadow({
          radius: 120,
          color: Color.Red,
          offsetX: 0,
          offsetY: 0
        })
        .width('90%')
        .backgroundColor(Color.White)

        Column() {
          Text()
            .fontWeight(FontWeight.Bold)
            .fontSize(20)
            .fontColor(Color.White)
        }
        .justifyContent(FlexAlign.Center)
        .width(150)
        .height(150)
        .borderRadius(10)
        .backgroundColor(0xf56c6c)
        .shadow({
          radius: 300,
          color: Color.Yellow,
          offsetX: 0,
          offsetY: 0
        })

        Column() {
          Text()
            .fontWeight(FontWeight.Bold)
            .fontSize(20)
            .fontColor(Color.White)
        }
        .justifyContent(FlexAlign.Center)
        .width(150)
        .height(150)
        .backgroundColor(0x67C23A)
        .borderRadius(10)
        .translate({ y: -50 })
        .shadow({
          radius: 220,
          color: Color.Blue,
          offsetX: 0,
          offsetY: 0
        })
      }
      .useShadowBatching(true)
    }
    .width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/MGyJo38wQSOn9ktWh_VqVA/en-us_image_0000002537765424.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=906DC362438235EF54201B5C9EA1593B2F8F2DA029E71094C8FB52874CB5CEA9)

## Example 7: Applying a Spherical Effect to a Component

This example demonstrates how to apply a spherical effect to a component using [sphericalEffect](#sphericaleffect12).

// xxx.ets
@Entry
@Component
struct SphericalEffectExample {
  build() {
    Stack() {
      TextInput({ placeholder: "Enter a percentage (\[0%, 100%\])." })
        .width('50%')
        .height(35)
        .type(InputType.Number)
        .enterKeyType(EnterKeyType.Done)
        .caretColor(Color.Red)
        .placeholderColor(Color.Blue)
        .placeholderFont({
          size: 20,
          style: FontStyle.Italic,
          weight: FontWeight.Bold
        })
        .sphericalEffect(0.5)
    }.alignContent(Alignment.Center).width("100%").height("100%")
  }
}

Below is how the component looks with the spherical effect applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/pcnnIb89RRSgcjvtImtp3A/en-us_image_0000002537925364.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=179829B23C9B048EB5E555EC715DECE7F6763F81DC754FA7EC6F65C9922C7C92)

Below is how the component looks without the spherical effect applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/Q4fT6fTUR-Gnn9wxGFDhEw/en-us_image_0000002568685141.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A8004F41E0D402FC21FC7B8FC04855CDA95C1286AD6637883884ED9E0E0413D)

## Example 8: Applying a Light Up Effect to a Component

This example demonstrates how to apply a light up effect to a component using [lightUpEffect](#lightupeffect12).

// xxx.ets
@Entry
@Component
struct LightUpExample {
  build() {
    Stack() {
      Text('This is the text content with letterSpacing 0.')
        .letterSpacing(0)
        .fontSize(12)
        .border({ width: 1 })
        .padding(10)
        .width('50%')
        .lightUpEffect(0.6)
    }.alignContent(Alignment.Center).width("100%").height("100%")
  }
}

Below is how the component looks with the light up effect applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/QjHV2mnnQEGIOkJUSv-UoQ/en-us_image_0000002568765151.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C6BD550336AB3BD1EEA25B58963D95FAEB630EA50709D33132DD53DF775A3F43)

Below is how the component looks with **lightUpEffect** set to **0.2**:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Byjuj8knRpaTVXNTyEmm1g/en-us_image_0000002537765426.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=729DC4105F5E87D551DFD5435D0E3E18FBABD08E37F02F49F62D8EDEE1F35340)

Below is how the component looks without the light up effect applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/5DT6AUJYSRa_MnziIONbgw/en-us_image_0000002537925366.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDFAD8E7F57E139D9964AD59F59DFD79FD7B7D3A5B69393EEF5F0FAB3E1C8928)

## Example 9: Applying a Pixel Stretch Effect to a Component

This example demonstrates how to apply a pixel stretch effect to a component using [pixelStretchEffect](#pixelstretcheffect12).

// xxx.ets
@Entry
@Component
struct PixelStretchExample {
  build() {
    Stack() {
      Text('This is the text content with letterSpacing 0.')
        .letterSpacing(0)
        .fontSize(12)
        .border({ width: 1 })
        .padding(10)
        .clip(false)
        .width('50%')
        .pixelStretchEffect({
          top: 10,
          left: 10,
          right: 10,
          bottom: 10
        })
    }.alignContent(Alignment.Center).width("100%").height("100%")
  }
}

Below is how the component looks with the pixel stretch effect applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/ZGv2_oVcQ3Ww7Aah8SdDaw/en-us_image_0000002568685143.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D675258D122C59888EC72888A63A1F6D263BD2562DA53718CBAB7AC5A306EC0)

Below is how the component looks without the pixel stretch effect applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/7vBQstJbTbeIRU_59OtAvg/en-us_image_0000002568765153.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83616E8F69D6D935CB8C523A429931A3D8C6AF901E7F70173833459518699DEE)

## Example 10: Applying a System Bar Effect to a Component

This example demonstrates how to apply a system bar effect to a component using [systemBarEffect](#systembareffect12).

// xxx.ets
@Entry
@Component
struct Index {
  build() {
    Column() {
      Stack() {
        // Replace $r("app.media.testImage") with the image resource file you use.
        Image($r('app.media.testImage')).width('100%').height('100%')
        Column()
          .width(150)
          .height(10)
          .systemBarEffect()
          .border({ radius: 5 })
          .margin({ bottom: 80 })
      }.alignContent(Alignment.Center)
    }
  }
}

Below is how the component looks with the system bar effect applied.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/exhdeX1wQKW7Bn3fLZ1gRQ/en-us_image_0000002537765428.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062234Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68695C02F520010F7173D3C3B279E2614B3637802F737B411FF935D8C158514C)
