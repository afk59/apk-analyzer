# Background

You can set the background for a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/iwm3vyq2TGKzXt00qRytgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BC3E9C19108D8AC4DAC1139B684D7D91B15D712137BD63EAB7273E1549B1AB2)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### background10+

background(content: CustomBuilder | ResourceColor, options?: BackgroundOptions): T

Sets the background of the component. Since API version 20, this API supports the [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) type for the **content** parameter and allows the background to extend into the parent component's safe area.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/wyuGmlgQRuKWQD4xoHI0Yg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC9D3B7DCE3842FD3801D7898D6CB33D2F331E34359EDF91B3ECE21A598418A8)

-   Events related to node mounting and unmounting, such as [onAppear](../../../universal-events/component-change-events/show-hide-event/document.md#onappear) and [onDisAppear](../../../universal-events/component-change-events/show-hide-event/document.md#ondisappear), are not supported.
    
-   This API can be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier) since API version 20 only if the input parameter type of **content** is ResourceColor.
    

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| content | [CustomBuilder](../../../common-definitions/basic-types/document.md#custombuilder8) | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Custom background. |
| options | [BackgroundOptions](#backgroundoptions20) | No | 
Custom background options.

**NOTE**

In versions earlier than API version 20, **options** is defined as follows:

{

align?: [Alignment](../../../common-definitions/enums/document.md#alignment)

}

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/y2bqBfMKT3i6apSHtgKKjA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A56C5C9481472DB7AD43DB0249E555768523CF844EFD2261679DAD226FFD0395)

-   The custom background takes some time to render and cannot respond to events during this rendering period. This property cannot be nested.
-   CustomBuilder backgrounds cannot be previewed in the DevEco Studio Previewer.
-   Dynamic background update is supported since API version 20.
-   If **background**, **backgroundColor**, and **backgroundImage** are set at the same time, all three will take effect, with the stacking order following the rules below:
    -   If **background** is of the **ResourceColor** type or the **ignoresLayoutSafeAreaEdges** property is set, **background** is at the bottom layer.
    -   In other cases, **background** is at the top layer.

#### BackgroundOptions20+

Provides background options.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| align10+ | [Alignment](../../../common-definitions/enums/document.md#alignment) | No | Yes | 
Alignment mode between the custom background and the component. This property takes effect only for backgrounds of the **CustomBuilder** type. If **ignoresLayoutSafeAreaEdges** is set, alignment applies to the expanded safe area.

Default value: **Alignment.Center**.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ignoresLayoutSafeAreaEdges | Array<[LayoutSafeAreaEdge](../../layout-and-borders/safe-area/document.md#layoutsafeareaedge12)\> | No | Yes | 

Safe areas to which the background will be extended, including the status bar, navigation bar, and [safeAreaPadding](../../layout-and-borders/sizing/document.md#safeareapadding14).

Default value:

\- CustomBuilder background: \[\], no extension.

\- ResourceColor background: \[LayoutSafeAreaEdge.ALL\] (expands all directions).

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/5_64-hVIQRi44zor0bINuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB1DEE405B58F3182EDB56378FC15C41C6537CF6D17672153D31BA911EE12C99)

The default value of **clip** of the **Shape**, **RowSplit**, **ColumnSplit**, **SideBarContainer**, **Stepper**, **List**, **Grid**, **WaterFlow**, **Scroll**, **Refresh**, **Swiper**, and **Tabs** components is **true**, and the background extension of the child component is clipped.

#### backgroundColor

backgroundColor(value: ResourceColor): T

Sets the background color of the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | Yes | Background color of the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundColor18+

backgroundColor(color: Optional<ResourceColor>): T

Sets the background color of the component. Compared to [backgroundColor](#backgroundcolor), the **color** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | Optional<[ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor)\> | Yes | 
Background color of the component.

If **color** is **undefined**, the background color reverts to the default transparent color.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/YlRjd-8zR5KwLrjOUukklw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48DFC3DF99B44B0BDDF5F4D2BF90D82C19C0B9043EF6447EAC53393A0DD58CE0)

If the background color is specified through **inactiveColor** in [backgroundBlurStyle](#backgroundblurstyle9), avoid setting the background color again using **backgroundColor**.

#### backgroundColor20+

backgroundColor(color: Optional<ResourceColor | ColorMetrics>): T

Sets the background color of the component. Compared with [backgroundColor](#backgroundcolor18), this API supports the [ColorMetrics](../../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) type for the **color** parameter.

**Widget capability**: This API can be used in ArkTS widgets since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| color | Optional<[ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | [ColorMetrics](../../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12)\> | Yes | 
Background color of the component.

If **color** is **undefined**, the background color reverts to the default transparent color.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundImage

backgroundImage(src: ResourceStr | PixelMap, repeat?: ImageRepeat): T

Sets the background image of the component.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [ResourceStr](../../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap12+](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Image address, which can be the address of an online or local image, a Base64 encoded string, or a pixel map. SVG and GIF images are not supported. |
| repeat | [ImageRepeat](../../../common-definitions/enums/document.md#imagerepeat) | No | Whether the background image is repeated. By default, the background image is not repeated. If the set image has a transparent background and **backgroundColor** is set, the image is overlaid on the background color. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundImage18+

backgroundImage(src: ResourceStr | PixelMap, options?: BackgroundImageOptions): T

Sets the background image of the component. Compared with [backgroundImage](#backgroundimage), this API allows you to specify synchronous or asynchronous loading modes for images.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/Xwkq-6epQQOS4HRvS8isrw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8B100A3AB1BC9E640F7375DFB5E52B020A4B46B2206924796DA926D5CF7DFCA)

This API cannot be called within [attributeModifier](../../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | [ResourceStr](../../../common-definitions/basic-types/document.md#resourcestr) | [PixelMap](../../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | Yes | Image address, which can be the address of an online or local image, a Base64 encoded string, or a pixel map. SVG, GIF, and WebP formats are not supported. |
| options | [BackgroundImageOptions](../../visual-effects/image-effect/document.md#backgroundimageoptions18) | No | Background image options. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundImageSize

backgroundImageSize(value: SizeOptions | ImageSize): T

Sets the width and height of the background image for the component. If **backgroundImageSize** is not set, the [ImageSize.Auto](../../../common-definitions/enums/document.md#imagesize) effect is applied.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SizeOptions](../../../common-definitions/basic-types/document.md#sizeoptions) | [ImageSize](../../../common-definitions/enums/document.md#imagesize) | Yes | 
Width and height of the background image. By default, the original image aspect ratio remains unchanged.

The value range of **width** and **height** is \[0, +∞).

**ImageSize** is used to control the scaling display mode, such as keeping the aspect ratio and filling the boundary.

**NOTE**

If both **width** and **height** are set to values less than or equal to 0, they are treated as 0. If either **width** or **height** is unset or set to a value less than or equal to 0, the other one is adjusted based on the original aspect ratio of the image.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundImagePosition

backgroundImagePosition(value: Position | Alignment): T

Sets the position of the component background image. If **backgroundImagePosition** is not set, the component background image is positioned at the upper left corner of the component by default.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Position](../../../common-definitions/basic-types/document.md#position) | [Alignment](../../../common-definitions/enums/document.md#alignment) | Yes | 
Position of the background image in the component, that is, the coordinates relative to the upper left corner of the component.

When **x** and **y** are set in percentage, the offset is calculated based on the width and height of the component.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### BlurStyle9+

Enumerates blur styles.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Thin | \- | 
Thin material.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Regular | \- | 

Regular material.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| Thick | \- | 

Thick material.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BACKGROUND\_THIN10+ | 3 | 

Material that creates the minimum depth of field effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BACKGROUND\_REGULAR10+ | 4 | 

Material that creates a medium shallow depth of field effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BACKGROUND\_THICK10+ | 5 | 

Material that creates a high shallow depth of field effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BACKGROUND\_ULTRA\_THICK10+ | 6 | 

Material that creates the maximum depth of field effect.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| NONE10+ | 7 | 

No blur.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| COMPONENT\_ULTRA\_THIN11+ | 8 | 

Component ultra-thin material.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| COMPONENT\_THIN11+ | 9 | 

Component thin material.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| COMPONENT\_REGULAR11+ | 10 | 

Component regular material.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| COMPONENT\_THICK11+ | 11 | 

Component thick material.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| COMPONENT\_ULTRA\_THICK11+ | 12 | 

Component ultra-thick material.

**Widget capability**: This API can be used in ArkTS widgets since API version 11.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### SystemAdaptiveOptions19+

Provides parameters for system adaptive adjustments. By default, the system performs adaptive adjustments based on chip performance.

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| disableSystemAdaptation | boolean | No | Yes | 
Whether to disable system adaptive adjustment. Whenever possible, do not include this parameter. This parameter only affects low-computing-power devices, the definition of which is determined by the device manufacturer. On low-computing-power devices, the system automatically decides whether to adjust effects (such as blur) to lower-computing-power alternatives based on conditions including computing power and load. To disable this feature, set this parameter to **true**.

Default value: **false**

 |

#### backgroundBlurStyle9+

backgroundBlurStyle(value: BlurStyle, options?: BackgroundBlurStyleOptions): T

Defines the background material blur style. It encapsulates various blur radius, mask color, mask opacity, saturation, and brightness values through enum values.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BlurStyle](#blurstyle9) | Yes | Settings of the background blur style, including the blur radius, mask color, mask opacity, saturation, and brightness. |
| options | [BackgroundBlurStyleOptions](#backgroundblurstyleoptions10) | No | 
Background blur options.

This parameter cannot be used in ArkTS widgets.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundBlurStyle18+

backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions): T

Defines the background material blur style. It encapsulates various blur radius, mask color, mask opacity, saturation, and brightness values through enum values. Compared to [backgroundBlurStyle9+](#backgroundblurstyle9), the **style** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | Optional<[BlurStyle](#blurstyle9)\> | Yes | 
Settings of the background blur style, including the blur radius, mask color, mask opacity, saturation, and brightness.

If **style** is **undefined**, the background blur reverts to its default state (that is, no blur).

 |
| options | [BackgroundBlurStyleOptions](#backgroundblurstyleoptions10) | No | 

Background blur options.

This parameter cannot be used in ArkTS widgets.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c/v3/_tI7R8SoSACIePhDTUnrpw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=70BD92F051678440E2FC0BF0C9076762E8D1B44E8E368B56E2AD4484DC0BCAF9)

If the background color is specified through **inactiveColor** in **backgroundBlurStyle**, avoid setting the background color again using [backgroundColor](#backgroundcolor).

#### backgroundBlurStyle19+

backgroundBlurStyle(style: Optional<BlurStyle>, options?: BackgroundBlurStyleOptions, sysOptions?: SystemAdaptiveOptions): T

Defines the background material blur style. It encapsulates various blur radius, mask color, mask opacity, saturation, and brightness values through enum values. Compared with [backgroundBlurStyle18+](#backgroundblurstyle18), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments.

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| style | Optional<[BlurStyle](#blurstyle9)\> | Yes | 
Settings of the background blur style, including the blur radius, mask color, mask opacity, saturation, and brightness.

If **style** is **undefined**, the background blur reverts to its default state (that is, no blur).

 |
| options | [BackgroundBlurStyleOptions](#backgroundblurstyleoptions10) | No | 

Background blur options.

This parameter cannot be used in ArkTS widgets.

 |
| sysOptions | [SystemAdaptiveOptions](#systemadaptiveoptions19) | No | 

System adaptive adjustment options.

Default value: **{ disableSystemAdaptation: false }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/R5yPNC6fRRibQdE1pZT9Rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D79C35EF5B174991BDA4439F6F93B00D70524A7A3E4E522606AB83D7D4FF328C)

If the background color is specified through **inactiveColor** in **backgroundBlurStyle**, avoid setting the background color again using [backgroundColor](#backgroundcolor).

#### backdropBlur

backdropBlur(value: number, options?: BlurOptions): T

Applies a background blur effect to the component. You can customize the blur radius and grayscale parameters.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Background blur effect to apply to the component. The input parameter is the blur radius. The larger the radius is, the more blurred the background is. If the value is **0**, the background is not blurred. |
| options11+ | [BlurOptions](../../visual-effects/foreground-blur/document.md#bluroptions11) | No | Grayscale parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backdropBlur18+

backdropBlur(radius: Optional<number>, options?: BlurOptions): T

Applies a background blur effect to the component. You can customize the blur radius and grayscale parameters. Compared to [backdropBlur](#backdropblur), the **radius** parameter supports the **undefined** type.

**Widget capability**: This API can be used in ArkTS widgets since API version 18.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| radius | Optional<number> | Yes | 
Background blur effect to apply to the component. The input parameter is the blur radius. The larger the radius is, the more blurred the background is. If the value is **0**, the background is not blurred.

If **radius** is **undefined**, the background blur reverts to its default state (that is, no blur).

 |
| options | [BlurOptions](../../visual-effects/foreground-blur/document.md#bluroptions11) | No | Grayscale parameters. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/NlWgp8oTQmuHRGz272lNOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA1B184ED633111F6DA23B6E969341547B5806BA9BB3065C881BCE12EAB688CA)

The **blur** and **backdropBlur** APIs provide real-time blurring by rendering each frame, which can be performance-intensive. For static blur effects where content and radius remain unchanged, you are advised to use the static [blur](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-effectkit-image-effects/document.md#blur) API to reduce the load.

#### backdropBlur19+

backdropBlur(radius: Optional<number>, options?: BlurOptions, sysOptions?: SystemAdaptiveOptions): T

Applies a background blur effect to the component. You can customize the blur radius and grayscale parameters. Compared with [backdropBlur18+](#backdropblur18), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments.

**Widget capability**: This API can be used in ArkTS widgets since API version 19.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| radius | Optional<number> | Yes | 
Background blur effect to apply to the component. The input parameter is the blur radius. The larger the radius is, the more blurred the background is. If the value is **0**, the background is not blurred.

If **radius** is **undefined**, the background blur reverts to its default state (that is, no blur).

 |
| options | [BlurOptions](../../visual-effects/foreground-blur/document.md#bluroptions11) | No | Grayscale parameters. |
| sysOptions | [SystemAdaptiveOptions](#systemadaptiveoptions19) | No | 

System adaptive adjustment options.

Default value: **{ disableSystemAdaptation: false }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/4kizTIFoRUmsoX7MRizTgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D17F44D4EC2FDC5FD561F8B6F7BBC70450AD996B5A691EBED8D0BB155981AB47)

**backgroundBlurStyle**, **blur**, and **backdropBlur** perform real-time rendering per frame, resulting in high performance overhead. When both the blur content and blur radius remain unchanged, it is recommended that you use the static blur API [blur](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-effectkit-image-effects/document.md#blur). For best practices, see [Image Blurring Optimization – When to Use](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-fuzzy-scene-performance-optimization#section4945532519).

#### backgroundEffect11+

backgroundEffect(options: BackgroundEffectOptions): T

Sets the background effect of the component, including the blur radius, brightness, saturation, and color.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [BackgroundEffectOptions](#backgroundeffectoptions11) | Yes | Background effect of the component, including the blur radius, brightness, saturation, and color. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundEffect18+

backgroundEffect(options: Optional<BackgroundEffectOptions>): T

Sets the background effect of the component, including the blur radius, brightness, saturation, and color. Compared to [backgroundEffect11+](#backgroundeffect11), the **options** parameter supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | Optional<[BackgroundEffectOptions](#backgroundeffectoptions11)\> | Yes | 
Background effect of the component, including the blur radius, brightness, saturation, and color.

If **options** is **undefined**, the background reverts to its default state with no effect.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundEffect19+

backgroundEffect(options: Optional<BackgroundEffectOptions>, sysOptions?: SystemAdaptiveOptions): T

Sets the background effect of the component, including the blur radius, brightness, saturation, and color. Compared with [backgroundEffect18+](#backgroundeffect18), this API adds the **sysOptions** parameter, which allows for system adaptive adjustments.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/3drK94RhS8Wx7WTQdad9og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80F3B3D25CF6F5D6E0D94A6C79DC8C7B36B8D205FA7969AC04B7ECC70B2489C8)

**backgroundEffect** performs real-time rendering per frame, resulting in high performance overhead. When the background blur effect remains unchanged, it is recommended that you use the static blur API [blur](../../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-effectkit-image-effects/document.md#blur). For best practices, see [Image Blurring Optimization – When to Use](https://developer.huawei.com/consumer/en/doc/best-practices/bpta-fuzzy-scene-performance-optimization#section4945532519).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | Optional<[BackgroundEffectOptions](#backgroundeffectoptions11)\> | Yes | 
Background effect of the component, including the blur radius, brightness, saturation, and color.

If **options** is **undefined**, the background reverts to its default state with no effect.

 |
| sysOptions | [SystemAdaptiveOptions](#systemadaptiveoptions19) | No | 

System adaptive adjustment options.

Default value: **{ disableSystemAdaptation: false }**

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### BackgroundEffectOptions11+

Describes the background effect.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| radius | number | No | No | 
Blur radius.

Value range: \[0, +∞)

Default value: **0**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| saturation | number | No | Yes | 

Saturation.

Value range: \[0, +∞)

Default value: **1** Recommended value range: \[0, 50\]

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| brightness | number | No | Yes | 

Brightness.

Value range: \[0, +∞)

Default value: **1** Recommended value range: \[0, 2\]

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| color | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color.

Default value: transparent

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| adaptiveColor | [AdaptiveColor](../../visual-effects/foreground-blur/document.md#adaptivecolor) | No | Yes | 

Adaptive color mode used for the background blur effect. Default value: **DEFAULT** When set to **AVERAGE**, the adaptive color mode takes effect only when the color has transparency.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| blurOptions | [BlurOptions](../../visual-effects/foreground-blur/document.md#bluroptions11) | No | Yes | 

Grayscale blur.

Default value: **\[0, 0\]**

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| policy14+ | [BlurStyleActivePolicy](#blurstyleactivepolicy14) | No | Yes | 

Blur activation policy.

Default value: **BlurStyleActivePolicy.ALWAYS\_ACTIVE**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| inactiveColor14+ | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color when the blur effect does not take effect. This parameter must be used together with the **policy** parameter. When **policy** is set to a value that disables the blur effect, the blur effect on the components is removed. If **inactiveColor** is specified, it is applied as the component background color.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### backgroundImageResizable12+

backgroundImageResizable(value: ResizableOptions): T

Sets the resizable background image options.

When **ResizableOptions** is set to a valid value, the **repeat** parameter in [backgroundImage](#backgroundimage) does not take effect.

When the sum of the values of **top** and **bottom** is greater than the source image height, or the sum of the values of **left** and **right** is greater than the source image width, the **ResizableOptions** attribute does not take effect.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ResizableOptions](../../../images-and-videos/image/document.md#resizableoptions11) | Yes | Resizable image options. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### BackgroundBlurStyleOptions10+

Inherits from [BlurStyleOptions](../../visual-effects/foreground-blur/document.md#blurstyleoptions).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| policy14+ | [BlurStyleActivePolicy](#blurstyleactivepolicy14) | No | Yes | 
Blur activation policy.

Default value: **BlurStyleActivePolicy.ALWAYS\_ACTIVE**

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| inactiveColor14+ | [ResourceColor](../../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color when the blur effect does not take effect. This parameter must be used together with the **policy** parameter. When **policy** is set to a value that disables the blur effect, the blur effect on the components is removed. If **inactiveColor** is specified, it is applied as the component background color.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### BlurStyleActivePolicy14+

Enumerates the activation policies for the background blur effect.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| FOLLOWS\_WINDOW\_ACTIVE\_STATE | 0 | The blur effect changes according to the window's focus state; it is inactive when the window is not in focus and active when the window is in focus. |
| ALWAYS\_ACTIVE | 1 | The blur effect is always active. |
| ALWAYS\_INACTIVE | 2 | The blur effect is always inactive. |

#### backgroundBrightness12+

backgroundBrightness(params: BackgroundBrightnessOptions): T

Sets the background brightness of the component.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| params | [BackgroundBrightnessOptions](#backgroundbrightnessoptions12) | Yes | Parameters for setting the background brightness. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### backgroundBrightness18+

backgroundBrightness(options: Optional<BackgroundBrightnessOptions>): T

Sets the background brightness of the component. Compared to [backgroundBrightness12+](#backgroundbrightness12), the **options** parameter supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | Optional<[BackgroundBrightnessOptions](#backgroundbrightnessoptions12)\> | Yes | 
Parameters for setting the background brightness.

If **options** is **undefined**, the background reverts to its default state with no brightness effect.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### BackgroundBrightnessOptions12+

Provides background brightness options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rate | number | No | No | 
Brightness change rate. A higher rate means that brightness decreases more quickly. If **rate** is set to **0**, **lightUpDegree** will not take effect, meaning no brightening effect will occur.

Default value: **0.0**

Value range: (0.0, +∞)

 |
| lightUpDegree | number | No | No | 

Light up degree. A greater degree indicates a greater increase in brightness.

Default value: **0.0**

Value range: \[-1.0, 1.0\]

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/M2jXKLsqSE2Vy0JneexERg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20C0264F2A2F96BC702339F5781AE5FB7692148ED9B8E1EEE65B52E9B9C9C61B)

The brightness (gray scale value) of each pixel in the component background content is calculated using the following formula:

Y = (0.299R + 0.587G + 0.114B) / 255.0, where **R**, **G**, and **B** represent red, green, and blue channel values of the pixel, respectively, and **Y** is the gray scale value. This formula normalizes the gray scale value to a range of 0 to 1.

The formula for calculating the increase in brightness for each pixel is as follows: ΔY = -rate \* Y + lightUpDegree. For example, when rate = 0.5 and lightUpDegree = 0.5, for a pixel with a gray scale value of 0.2, the increase in brightness is -0.5 \* 0.2 + 0.5 = 0.4. For a pixel with a gray scale value of 1, the increase in brightness is -0.5 \* 1 + 0.5 = 0.

#### Example

## Example 1: Setting Basic Background Styles

This example shows how to configure basic background styles by setting **backgroundColor**, **backgroundImage**, **backgroundImageSize**, and **backgroundImagePosition**.

// xxx.ets
@Entry
@Component
struct BackgroundExample {
  build() {
    Column({ space: 5 }) {
      Text('background color').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Row().width('90%').height(50).backgroundColor(0xE5E5E5).border({ width: 1 })

      Text('background image repeat along X').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Row()
      // Replace $r('app.media.image') with the image resource file you use.
        .backgroundImage($r('app.media.image'), ImageRepeat.X)
        .backgroundImageSize({ width: '250px', height: '140px' })
        .width('90%')
        .height(70)
        .border({ width: 1 })

      Text('background image repeat along Y').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Row()
      // Replace $r('app.media.image') with the image resource file you use.
        .backgroundImage($r('app.media.image'), ImageRepeat.Y)
        .backgroundImageSize({ width: '500px', height: '120px' })
        .width('90%')
        .height(100)
        .border({ width: 1 })

      Text('background image size').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Row()
        .width('90%')
        .height(150)
        // Replace $r('app.media.image') with the image resource file you use.
        .backgroundImage($r('app.media.image'), ImageRepeat.NoRepeat)
        .backgroundImageSize({ width: 1000, height: 500 })
        .border({ width: 1 })

      Text('background fill the box(Cover)').fontSize(9).width('90%').fontColor(0xCCCCCC)
      // Occupy all the space of the container, without ensuring that the image is completely displayed.
      Row()
        .width(200)
        .height(50)
        // Replace $r('app.media.image') with the image resource file you use.
        .backgroundImage($r('app.media.image'), ImageRepeat.NoRepeat)
        .backgroundImageSize(ImageSize.Cover)
        .border({ width: 1 })

      Text('background fill the box(Contain)').fontSize(9).width('90%').fontColor(0xCCCCCC)
      // Maximize the image while ensuring that it can be completely displayed.
      Row()
        .width(200)
        .height(50)
        // Replace $r('app.media.image') with the image resource file you use.
        .backgroundImage($r('app.media.image'), ImageRepeat.NoRepeat)
        .backgroundImageSize(ImageSize.Contain)
        .border({ width: 1 })

      Text('background image position').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Row()
        .width(100)
        .height(50)
        // Replace $r('app.media.image') with the image resource file you use.
        .backgroundImage($r('app.media.image'), ImageRepeat.NoRepeat)
        .backgroundImageSize({ width: 1000, height: 560 })
        .backgroundImagePosition({ x: -500, y: -300 })
        .border({ width: 1 })
    }
    .width('100%').height('100%').padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/ZL4Ko4GpQhCPXuwRnnIusQ/en-us_image_0000002568685105.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC37E3CC09F56EA7AD67EED458333F4E63CAAC9355D9B0B693FEB2C22AD147A4)

## Example 2: Setting the Background Blur Style

This example sets the background blur style using **backgroundBlurStyle**.

// xxx.ets
@Entry
@Component
struct BackgroundBlurStyleDemo {
  build() {
    Column() {
      Row() {
        Text("Thin Material")
      }
      .width('50%')
      .height('50%')
      .backgroundBlurStyle(BlurStyle.Thin,
        { colorMode: ThemeColorMode.LIGHT, adaptiveColor: AdaptiveColor.DEFAULT, scale: 1.0 })
      .position({ x: '15%', y: '30%' })
    }
    .height('100%')
    .width('100%')
    // Replace $r('app.media.bg') with the image resource file you use.
    .backgroundImage($r('app.media.bg'))
    .backgroundImageSize(ImageSize.Cover)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/FeiHIELJRqSqLKrTMcj-4w/en-us_image_0000002568765115.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FAF60022140477086B70E521038212F56D3713A2592505E0CB84312E3258E368)

## Example 3: Setting the Component Background

This example shows how to set the component background using **background**.

// xxx.ets
@Entry
@Component
struct BackgroundExample {
  @Builder
  renderBackground() {
    Column() {
      Progress({ value: 50 })
    }
  }

  build() {
    Column() {
      Text("content")
        .width(100)
        .height(40)
        .fontColor("#FFF")
        .position({ x: 50, y: 80 })
        .textAlign(TextAlign.Center)
        .backgroundColor(Color.Green)
    }
    .width(200).height(200)
    .background(this.renderBackground)
    .backgroundColor(Color.Gray)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/S69xDgD_SdewawLtG1c8vQ/en-us_image_0000002537765390.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=133B8A6DF1DB422AA6779983EC0856977A810D27B848EC90C35B6E5DA9864A9E)

## Example 4: Setting Component Background Brightness

This example sets the component background brightness using **backgroundBrightness**.

// xxx.ets
@Entry
@Component
struct BackgroundBrightnessDemo {
  build() {
    Column() {
      Row() {
        Text("BackgroundBrightness")
      }
      .width(200)
      .height(100)
      .position({ x: 100, y: 100 })
      .backgroundBlurStyle(BlurStyle.Thin, { colorMode: ThemeColorMode.LIGHT, adaptiveColor: AdaptiveColor.DEFAULT})
      .backgroundBrightness({rate:0.5,lightUpDegree:0.5}) // Background brightness
    }
    .width('100%')
    .height('100%')
    // Replace $r('app.media.image') with the image resource file you use.
    .backgroundImage($r('app.media.image'))
    .backgroundImageSize(ImageSize.Cover)
  }
}

The following figures show how the component looks with the background brightness set.

When **rate** and **lightUpDegree** are both set to **0.5**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/QWs92sYoSNuubMs0VoNoJQ/en-us_image_0000002537925330.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=988247B6A37D933C5F83A569DC5BDC92C1B26A1C49713165FB2CD07E5517A77D)

When **rate** is set to **0.5** and **lightUpDegree** **\-0.1**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/tCoBUtzNRTeIkYo1l9sflA/en-us_image_0000002568685107.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48813C3304BB14246B038A1DEF34BE2F9A07ED91B098CCECFE00FA5E245A6C64)

The following figure shows how the component looks without the background brightness set.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/XMRsigk_TdC0O3UihEaxng/en-us_image_0000002568765117.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DA3DA7DAA674569CAD355934E5509F36B2D3613EC3BAC78D4DF3EBF6E68BF3A)

## Example 5: Setting Blur Effects

This example shows how to use **blur** to apply a foreground blur effect and **backdropBlur** to apply a background blur effect.

// xxx.ets
@Entry
@Component
struct BlurEffectsExample {
  build() {
    Column({ space: 10 }) {
      // Blur the font.
      Text('font').fontSize(15).fontColor(0xCCCCCC).width('90%')
      Flex({ alignItems: ItemAlign.Center }) {
        Text('original').margin(10)
        Text('blur')
          .blur(5).margin(10)
        Text('blur')
          .blur(10, undefined).margin(10) // Set the foreground blur radius to 5 and disable system adaptive adjustment.
        Text('blur')
          .blur(15).margin(10)
      }.width('90%').height(40)
      .backgroundColor(0xF9CF93)

      // Blur the background.
      Text('backdropBlur').fontSize(15).fontColor(0xCCCCCC).width('90%')
      Text()
        .width('90%')
        .height(40)
        .fontSize(16)
        .backdropBlur(3)
        // Replace $r('app.media.image') with the image resource file you use.
        .backgroundImage($r('app.media.image'))
        .backgroundImageSize({ width: 1200, height: 160 })
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/nFAZyxUoQVyqW0jE6JKK5w/en-us_image_0000002537765392.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FA6006035F2679FBCCE679A549978A348DFE6AC39950171DF2256B586782112)

## Example 6: Setting Text Blur Effects

This example demonstrates how to use [blendMode](../../visual-effects/image-effect/document.md#blendmode11) and backgroundEffect to implement the text blur effect.

If unwanted lines appear, make sure the sizes of the two owning components of **blendMode** are the same. If the issue persists, the component bounds may have fallen on the floating-point coordinates. In this case, set the universal attribute [pixelRound](../../layout-and-borders/component-level-pixel-rounding/document.md#pixelround) to align the component bounds on both sides of the unwanted lines with the integer pixel coordinates.

// xxx.ets
@Entry
@Component
struct Index {
  @State shColor: Color = Color.White;
  @State sizeDate: number = 20;
  @State rVal: number = 255;
  @State gVal: number = 255;
  @State bVal: number = 255;
  @State aVal: number = 0.1;
  @State rad: number = 40;
  @State satVal: number = 0.8;
  @State briVal: number = 1.5;
  build() {
    Stack() {
      // Replace $r('app.media.image') with the image resource file you use.
      Image($r('app.media.image'))
      Column() {
        Column({ space: 0 }) {
          Column() {
            Text('11')
              .fontSize(144)
              .fontWeight(FontWeight.Bold)
              .fontColor('rgba(255,255,255,1)')
              .fontFamily('HarmonyOS-Sans-Digit')
              .maxLines(1)
              .lineHeight(120 \* 1.25)
              .height(120 \* 1.25)
              .letterSpacing(4 \* 1.25)
            Text('42')
              .fontSize(144)
              .fontWeight(FontWeight.Bold)
              .fontColor('rgba(255,255,255,1)')
              .fontFamily('HarmonyOS-Sans-Digit')
              .maxLines(1)
              .lineHeight(120 \* 1.25)
              .height(120 \* 1.25)
              .letterSpacing(4 \* 1.25)
              .shadow({
                color: 'rgba(0,0,0,0)',
                radius: 20,
                offsetX: 0,
                offsetY: 0
              })
            Row() {
              Text('October 16')
                .fontSize(this.sizeDate)
                .height(22)
                .fontWeight('medium')
                .fontColor('rgba(255,255,255,1)')
              Text('Monday')
                .fontSize(this.sizeDate)
                .height(22)
                .fontWeight('medium')
                .fontColor('rgba(255,255,255,1)')
            }
          }
          // Use offscreen rendering for blendMode. In DST\_IN mode, only the overlapping area of the current component and the underlying canvas is displayed.
          .blendMode(BlendMode.DST\_IN, BlendApplyType.OFFSCREEN)
          .pixelRound({
            start: PixelRoundCalcPolicy.FORCE\_FLOOR ,
            top: PixelRoundCalcPolicy.FORCE\_FLOOR ,
            end: PixelRoundCalcPolicy.FORCE\_CEIL,
            bottom: PixelRoundCalcPolicy.FORCE\_CEIL
          })
        }
        // Use offscreen rendering for blendMode. In SRC\_OVER mode, the content of the current component is displayed over the underlying canvas.
        .blendMode(BlendMode.SRC\_OVER, BlendApplyType.OFFSCREEN)
        // backgroundEffect configures the rounded corners, saturation, brightness, and dynamic RGBA color of the component background.
        .backgroundEffect({
          radius: this.rad,
          saturation: this.satVal,
          brightness: this.briVal,
          color: this.getVolumeDialogWindowColor()
        })
        .justifyContent(FlexAlign.Center)
        .pixelRound({
          start: PixelRoundCalcPolicy.FORCE\_FLOOR ,
          top: PixelRoundCalcPolicy.FORCE\_FLOOR ,
          end: PixelRoundCalcPolicy.FORCE\_CEIL,
          bottom: PixelRoundCalcPolicy.FORCE\_CEIL
        })
      }
    }
  }
  getVolumeDialogWindowColor(): ResourceColor | string {
    return \`rgba(${this.rVal.toFixed(0)}, ${this.gVal.toFixed(0)}, ${this.bVal.toFixed(0)}, ${this.aVal.toFixed(0)})\`;
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/nACB1bDHRXe4hjJhNCTMRA/en-us_image_0000002537925332.jpeg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F11653917E17E0EB865BF8452DD794690D83B866972DF83D91CF32DB1EAFD29)

## Example 7: Comparing Blur Effects

This example compares three different blur effects: **backgroundEffect**, **backDropBlur**, and **backgroundBlurStyle**.

// xxx.ets
@Entry
@Component
struct BackGroundBlur {
  private imageSize: number = 150;

  build() {
    Column({ space: 5 }) {
      // Use backgroundBlurStyle with an enum value to set blur parameters.
      Stack() {
        // Replace $r('app.media.test') with the image resource file you use.
        Image($r('app.media.test'))
          .width(this.imageSize)
          .height(this.imageSize)
        Column()
          .width(this.imageSize)
          .height(this.imageSize)
          .backgroundBlurStyle(BlurStyle.Thin)
      }

      // backgroundEffect allows for custom settings for blur radius, brightness, saturation, and more.
      Stack() {
        // Replace $r('app.media.test') with the image resource file you use.
        Image($r('app.media.test'))
          .width(this.imageSize)
          .height(this.imageSize)
        Column()
          .width(this.imageSize)
          .height(this.imageSize)
          .backgroundEffect({ radius: 20, brightness: 0.6, saturation: 15 })
      }

      // backdropBlur only sets blur radius and grayscale parameters.
      Stack() {
        // Replace $r('app.media.test') with the image resource file you use.
        Image($r('app.media.test'))
          .width(this.imageSize)
          .height(this.imageSize)
        Column()
          .width(this.imageSize)
          .height(this.imageSize)
          .backdropBlur(20, { grayscale: \[30, 50\] })
      }
    }
    .width('100%')
    .padding({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/hVCbzbaiT46yzk23xfwobQ/en-us_image_0000002568685109.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=826EE4CB44047E327775B3ADFD6BCE72659254F1DECA01DDA3F63583A22541FE)

## Example 8: Applying a P3 Color Gamut Background Effect

This example demonstrates how to apply a P3 color gamut background effect using [backgroundColor](#backgroundcolor20), available since API version 20.

// xxx.ets
// To set the P3 color gamut, use the setColorSpace API in ets/entryability/EntryAbility.ets to set the current window to a wide color gamut.
import { ColorMetrics } from '@kit.ArkUI';

@Entry
@Component
struct P3BackgroundDemo {
  @State p3Color: ColorMetrics = ColorMetrics.colorWithSpace(ColorSpace.DISPLAY\_P3, 0, 0.3, 0.8, 1);

  build() {
    Column({ space: 5 }) {
      Text('background color with colorMetrics').fontSize(9).width('90%').fontColor(0xCCCCCC)
      Row().width('90%').height(50).backgroundColor(this.p3Color)
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/hUEfNX9YRo6SzUL3Kjx7-g/en-us_image_0000002568765119.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EBFD641B2061BCC2CD0104D107B4D05DA5039C4732087D635F094C324E55FCA)

## Example 9: Setting Component Background Extension

This example shows how to use [background](#background10) to extend the component's background to the parent component's safe area, supported since API version 20.

import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct BackgroundExtension {
  @Builder
  myImages() {
    Column() {
      Image($r('app.media.startIcon'))
        .width('100%')
        .height('100%')
    }
  }

  build() {
    Column({space: 10}) {
      Stack() {
        // A background of the CustomBuilder type with the ignoresLayoutSafeAreaEdges property set extends to the parent component's safe area.
        Column()
          .size({ width: '100%', height: '100%' })
          .border({ width: 1, color: Color.Red })
          .background(
            this.myImages(),
            { align: Alignment.Center , ignoresLayoutSafeAreaEdges: \[ LayoutSafeAreaEdge.START, LayoutSafeAreaEdge.TOP \] }
          )
      }
      .size({ width: 300, height: 300 })
      .backgroundColor('#004aaf')
      .safeAreaPadding(LengthMetrics.vp(50))

      Stack() {
        // A background of the ResourceColor type without the ignoresLayoutSafeAreaEdges property set extends to the parent component's safe area by default.
        Column()
          .size({ width: '100%', height: '100%' })
          .border({ width: 1, color: Color.Red })
          .background('#d5d5d5', { align: Alignment.Center })
      }
      .size({ width: 300, height: 300 })
      .backgroundColor('#707070')
      .safeAreaPadding(LengthMetrics.vp(50))
    }
    .margin(10)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/EK_Q7yRGTYGkFZQCYYIGjQ/en-us_image_0000002537765394.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BBF6037A73F8F28CA05A938CAEC127D9C80A4699E69C7FD6767D95B5BD6ECFA1)
