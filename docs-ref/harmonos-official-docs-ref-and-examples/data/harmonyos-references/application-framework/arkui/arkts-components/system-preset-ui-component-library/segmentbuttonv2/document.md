# SegmentButtonV2

**SegmentButtonV2** is a versatile component that organizes related options into visually grouped buttons. It supports three variants: tab-style, capsule-style single-select, and capsule-style multi-select.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/rE_W2vI6TjWf6kh9hHCp5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5649B50A2AD40FBB7825BCF4F4B4E860226BAC6DA1153B9651ABF278B418C6A1)

This component is supported since API version 18. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { TabSegmentButtonV2, CapsuleSegmentButtonV2, MultiCapsuleSegmentButtonV2, SegmentButtonV2Items } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### TabSegmentButtonV2

TabSegmentButtonV2({
  items: SegmentButtonV2Items,
  selectedIndex: number,
  $selectedIndex?: OnSelectedIndexChange,
  onItemClicked?: Callback<number>,
  itemMinFontScale?: number | Resource,
  itemMaxFontScale?: number | Resource,
  itemSpace?: LengthMetrics,
  itemFontSize?: LengthMetrics,
  itemSelectedFontSize?: LengthMetrics,
  itemFontColor?: ColorMetrics,
  itemSelectedFontColor?: ColorMetrics,
  itemFontWeight?: FontWeight,
  itemSelectedFontWeight?: FontWeight,
  itemBorderRadius?: LengthMetrics,
  itemSelectedBackgroundColor?: ColorMetrics,
  itemIconSize?: SizeT<LengthMetrics>,
  itemIconFillColor?: ColorMetrics,
  itemSelectedIconFillColor?: ColorMetrics,
  itemSymbolFontSize?: LengthMetrics,
  itemSymbolFontColor?: ColorMetrics,
  itemSelectedSymbolFontColor?: ColorMetrics,
  itemMinHeight?: LengthMetrics,
  itemPadding?: LocalizedPadding,
  itemShadow?: ShadowOptions | ShadowStyle,
  buttonBackgroundColor?: ColorMetrics,
  buttonBackgroundBlurStyle?: BlurStyle,
  buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions,
  buttonBackgroundEffect?: BackgroundEffectOptions,
  buttonBorderRadius?: LengthMetrics,
  buttonMinHeight?: LengthMetrics,
  buttonPadding?: LengthMetrics,
  languageDirection?: Direction
})

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| items | [SegmentButtonV2Items](#segmentbuttonv2items) | Yes | 
@Require

@Param

 | 

Items of the segmented button.

If the value is **undefined**, the option information is not displayed.

This property is read-only.

 |
| selectedIndex | number | Yes | 

@Require

@Param

 | 

Index of the selected segmented button item. The index is zero-based and increments by 1.

If the value is undefined, no item is selected. If the value is a non-positive value, the default value **0** is used.

This property is read-only.

 |
| $selectedIndex | [OnSelectedIndexChange](#onselectedindexchange) | No | @Event | Callback invoked when the selected item changes. |
| onItemClicked | Callback<number> | No | @Event | Callback invoked when a segmented button item is clicked. |
| buttonBackgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Background color of the segmented button.

Default value: **$r('sys.color.segment\_button\_v2\_tab\_button\_background')**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| buttonBackgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | @Param | 

Background blur style of the segmented button.

Default value: **undefined**

This property is read-only.

 |
| buttonBackgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | @Param | 

Background blur style options of the segmented button.

Default value: **undefined**

This property is read-only.

 |
| buttonBackgroundEffect | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | @Param | 

Background blur effect options of the segmented button.

Default value: **undefined**

This property is read-only.

 |
| buttonBorderRadius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Background border radius of the segmented button.

Value range: \[0, +∞)

Default value: **$r('sys.float.segment\_button\_v2\_background\_corner\_radius')**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| buttonMinHeight | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Minimum height of the segmented button.

Value range: \[0, +∞)

Default value: **$r('sys.float.segment\_button\_v2\_singleline\_background\_height')** for text-only buttons and icon-only buttons, and **$r('sys.float.segment\_button\_v2\_doubleline\_background\_height')** for buttons with both an icon and text.

If the value is out of the range, the default value is used.

This property is read-only.

 |
| buttonPadding | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Padding of the segmented button.

Value range: \[0, +∞)

Default value: **$r('sys.float.padding\_level1')**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemSelectedBackgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Background color of the selected segmented button item.

Default value: **$r('sys.color.segment\_button\_v2\_tab\_selected\_item\_background')**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| itemMinHeight | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Minimum height of the segmented button item.

Value range: \[0, +∞)

Default value:

**$r('sys.float.segment\_button\_v2\_singleline\_selected\_height')** for text-only buttons and icon-only buttons, and **$r('sys.float.segment\_button\_v2\_doubleline\_selected\_height')** for buttons with both an icon and text.

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemPadding | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | @Param | 

Padding of the segmented button item.

Default value: **{top: LengthMetrics.resource ($r('sys.float.padding\_level2')), bottom: LengthMetrics.resource ($r('sys.float.padding\_level2')), start: LengthMetrics.resource($r('sys.float.padding\_level4')), end: LengthMetrics.resource($r('sys.float.padding\_level4'))}**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| itemShadow | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | @Param | 

Shadow of the segmented button item.

Default value: **ShadowStyle.OUTER\_DEFAULT\_XS**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemSpace | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Space between segmented button items.

Value range: \[0, +∞)

Default value: **LengthMetrics.vp(0)**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

This property is read-only.

 |
| itemMinFontScale | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | @Param | 

Minimum font scale factor of the segmented button item text.

Value range: \[0, 1\]

Default value: **0**.

**NOTE**

A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**. Abnormal values are ineffective by default.

This property is read-only.

 |
| itemMaxFontScale | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | @Param | 

Maximum font scale factor of the segmented button item text.

Value range: \[1, 2\]

Default value: **1**

**NOTE**

A value less than 1 is treated as **1**. A value greater than 2 is treated as **2**. Abnormal values are ineffective by default.

This property is read-only.

 |
| itemFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Font size of unselected segmented button items.

Value range: \[0, +∞)

Default value: **14fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **textModifier** is set for **items**, **itemFontSize** has no effect.

This property is read-only.

 |
| itemSelectedFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Font size of the selected segmented button item.

Value range: \[0, +∞)

Default value: **14fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **textModifier** is set for **items**, **itemSelectedFontSize** has no effect.

This property is read-only.

 |
| itemFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Font color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **textModifier** is set for **items**, **itemFontColor** has no effect.

This property is read-only.

 |
| itemSelectedFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Font color of the selected segmented button item.

Default value: **$r('sys.color.font\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **textModifier** is set for **items**, **itemSelectedFontColor** has no effect.

This property is read-only.

 |
| itemFontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | @Param | 

Font weight of unselected segmented button items.

Default value: **FontWeight.Medium**

If the value is out of the range, the default value is used.

**NOTE**

When **fontWeight** of **textModifier** is set for **items**, **itemFontWeight** has no effect.

This property is read-only.

 |
| itemSelectedFontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | @Param | 

Font weight of the selected segmented button item.

Default value: **FontWeight.Medium**

If the value is out of the range, the default value is used.

**NOTE**

When **fontWeight** of **textModifier** is set for **items**, **itemSelectedFontWeight** has no effect.

This property is read-only.

 |
| itemBorderRadius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Border radius of segmented button items.

Value range: \[0, +∞)

Default value: **$r('sys.float.segment\_button\_v2\_selected\_corner\_radius')**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemIconSize | [SizeT](../../../arkts-api/ui/arkui/graphics/document.md#sizett12)<[LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)\> | No | @Param | 

Image-type icon size of segmented button items.

Value range: \[0, +∞)

Default value: **{ width: LengthMetrics.vp(24), height: LengthMetrics.vp(24) }**

If the value is out of the range, the default value is used.

**NOTE**

When **width** and **height** of **iconModifier** are set for **items**, **itemIconSize** has no effect.

This property is read-only.

 |
| itemIconFillColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Icon color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fillColor** of **iconModifier** is set for **items**, **itemIconFillColor** has no effect.

This property is read-only.

 |
| itemSelectedIconFillColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Icon color of the selected segmented button item.

Default value: **$r('sys.color.font\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fillColor** of **iconModifier** is set for **items**, **itemSelectedIconFillColor** has no effect.

This property is read-only.

 |
| itemSymbolFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

HM Symbol icon size of segmented button items.

Value range: \[0, +∞)

Default value: **20fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **symbolModifier** is set for **items**, **itemSymbolFontSize** has no effect.

This property is read-only.

 |
| itemSymbolFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

HM Symbol icon color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **symbolModifier** is set for **items**, **itemSymbolFontColor** has no effect.

This property is read-only.

 |
| itemSelectedSymbolFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

HM Symbol icon color of the selected segmented button item.

Default value: **$r('sys.color.font\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **symbolModifier** is set for **items**, **itemSelectedSymbolFontColor** has no effect.

This property is read-only.

 |
| languageDirection | [Direction](../../common-definitions/enums/document.md#direction) | No | @Param | 

Language direction of the segmented button.

Default value: **Direction.Auto**

If the value is out of the range, the default value is used.

This property is read-only.

 |

#### CapsuleSegmentButtonV2

CapsuleSegmentButtonV2({
  items: SegmentButtonV2Items,
  selectedIndex: number,
  $selectedIndex?: OnSelectedIndexChange,
  onItemClicked?: Callback<number>,
  itemMinFontScale?: number | Resource,
  itemMaxFontScale?: number | Resource,
  itemSpace?: LengthMetrics,
  itemFontSize?: LengthMetrics,
  itemSelectedFontSize?: LengthMetrics,
  itemFontColor?: ColorMetrics,
  itemSelectedFontColor?: ColorMetrics,
  itemFontWeight?: FontWeight,
  itemSelectedFontWeight?: FontWeight,
  itemBorderRadius?: LengthMetrics,
  itemSelectedBackgroundColor?: ColorMetrics,
  itemIconSize?: SizeT<LengthMetrics>,
  itemIconFillColor?: ColorMetrics,
  itemSelectedIconFillColor?: ColorMetrics,
  itemSymbolFontSize?: LengthMetrics,
  itemSymbolFontColor?: ColorMetrics,
  itemSelectedSymbolFontColor?: ColorMetrics,
  itemMinHeight?: LengthMetrics,
  itemPadding?: LocalizedPadding,
  itemShadow?: ShadowOptions | ShadowStyle,
  buttonBackgroundColor?: ColorMetrics,
  buttonBackgroundBlurStyle?: BlurStyle,
  buttonBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions,
  buttonBackgroundEffect?: BackgroundEffectOptions,
  buttonBorderRadius?: LengthMetrics,
  buttonMinHeight?: LengthMetrics,
  buttonPadding?: LengthMetrics,
  languageDirection?: Direction
})

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| items | [SegmentButtonV2Items](#segmentbuttonv2items) | Yes | 
@Require

@Param

 | 

Items of the segmented button.

If the value is **undefined**, the option information is not displayed.

This property is read-only.

 |
| selectedIndex | number | Yes | 

@Require

@Param

 | 

Index of the selected segmented button item. The index is zero-based and increments by 1.

If the value is undefined, no item is selected. If the value is a non-positive value, the default value **0** is used.

This property is read-only.

 |
| $selectedIndex | [OnSelectedIndexChange](#onselectedindexchange) | No | @Event | Callback invoked when the selected item changes. |
| onItemClicked | Callback<number> | No | @Event | Callback invoked when a segmented button item is clicked. |
| buttonBackgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Background color of the segmented button.

Default value: **$r('sys.color.segment\_button\_v2\_tab\_button\_background')**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| buttonBackgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | @Param | 

Background blur style of the segmented button.

Default value: **undefined**

This property is read-only.

 |
| buttonBackgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | @Param | 

Background blur style options of the segmented button.

Default value: **undefined**

This property is read-only.

 |
| buttonBackgroundEffect | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | @Param | 

Background blur effect options of the segmented button.

Default value: **undefined**

This property is read-only.

 |
| buttonBorderRadius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Background border radius of the segmented button.

Value range: \[0, +∞)

Default value: **$r('sys.float.segment\_button\_v2\_background\_corner\_radius')**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| buttonMinHeight | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Minimum height of the segmented button.

Value range: \[0, +∞)

Default value: **$r('sys.float.segment\_button\_v2\_singleline\_background\_height')** for text-only buttons and icon-only buttons, and **$r('sys.float.segment\_button\_v2\_doubleline\_background\_height')** for buttons with both an icon and text.

If the value is out of the range, the default value is used.

This property is read-only.

 |
| buttonPadding | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Padding of the segmented button.

Value range: \[0, +∞)

Default value: **$r('sys.float.padding\_level1')**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemSelectedBackgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Background color of the selected segmented button item.

Default value: **$r('sys.color.comp\_background\_emphasize')**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| itemMinHeight | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Minimum height of the segmented button item.

Value range: \[0, +∞)

Default value:

**$r('sys.float.segment\_button\_v2\_singleline\_selected\_height')** for text-only buttons and icon-only buttons, and **$r('sys.float.segment\_button\_v2\_doubleline\_selected\_height')** for buttons with both an icon and text.

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemPadding | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | @Param | 

Padding of the segmented button item.

Default value: **{top: LengthMetrics.resource ($r('sys.float.padding\_level2')), bottom: LengthMetrics.resource ($r('sys.float.padding\_level2')), start: LengthMetrics.resource($r('sys.float.padding\_level4')), end: LengthMetrics.resource($r('sys.float.padding\_level4'))}**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| itemShadow | [ShadowOptions](../../universal-attributes/visual-effects/image-effect/document.md#shadowoptions) | [ShadowStyle](../../universal-attributes/visual-effects/image-effect/document.md#shadowstyle10) | No | @Param | 

Shadow of the segmented button item.

Default value: **ShadowStyle.OUTER\_DEFAULT\_XS**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemSpace | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Space between segmented button items.

Value range: \[0, +∞)

Default value: **LengthMetrics.vp(0)**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

This property is read-only.

 |
| itemMinFontScale | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | @Param | 

Minimum font scale factor of the segmented button item text.

Value range: \[0, 1\]

Default value: **0**

**NOTE**

A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**. Abnormal values are ineffective by default.

This property is read-only.

 |
| itemMaxFontScale | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | @Param | 

Maximum font scale factor of the segmented button item text.

Value range: \[1, 2\]

Default value: **1**

**NOTE**

A value less than 1 is treated as **1**. A value greater than 2 is treated as **2**. Abnormal values are ineffective by default.

This property is read-only.

 |
| itemFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Font size of unselected segmented button items.

Value range: \[0, +∞)

Default value: **14fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **textModifier** is set for **items**, **itemFontSize** has no effect.

This property is read-only.

 |
| itemSelectedFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Font size of the selected segmented button item.

Value range: \[0, +∞)

Default value: **14fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **textModifier** is set for **items**, **itemSelectedFontSize** has no effect.

This property is read-only.

 |
| itemFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Font color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **textModifier** is set for **items**, **itemFontColor** has no effect.

This property is read-only.

 |
| itemSelectedFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Font color of the selected segmented button item.

Default value: **$r('sys.color.font\_on\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **textModifier** is set for **items**, **itemSelectedFontColor** has no effect.

This property is read-only.

 |
| itemFontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | @Param | 

Font weight of unselected segmented button items.

Default value: **FontWeight.Medium**

If the value is out of the range, the default value is used.

**NOTE**

When **fontWeight** of **textModifier** is set for **items**, **itemFontWeight** has no effect.

This property is read-only.

 |
| itemSelectedFontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | @Param | 

Font weight of the selected segmented button item.

Default value: **FontWeight.Medium**

If the value is out of the range, the default value is used.

**NOTE**

When **fontWeight** of **textModifier** is set for **items**, **itemSelectedFontWeight** has no effect.

This property is read-only.

 |
| itemBorderRadius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Border radius of segmented button items.

Value range: \[0, +∞)

Default value: **$r('sys.float.segment\_button\_v2\_selected\_corner\_radius')**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemIconSize | [SizeT](../../../arkts-api/ui/arkui/graphics/document.md#sizett12)<[LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)\> | No | @Param | 

Image-type icon size of segmented button items.

Value range: \[0, +∞)

Default value: **{ width: LengthMetrics.vp(24), height: LengthMetrics.vp(24) }**

If the value is out of the range, the default value is used.

**NOTE**

When **width** and **height** of **iconModifier** are set for **items**, **itemIconSize** has no effect.

This property is read-only.

 |
| itemIconFillColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Icon color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fillColor** of **iconModifier** is set for **items**, **itemIconFillColor** has no effect.

This property is read-only.

 |
| itemSelectedIconFillColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Icon color of the selected segmented button item.

Default value: **$r('sys.color.font\_on\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fillColor** of **iconModifier** is set for **items**, **itemSelectedIconFillColor** has no effect.

This property is read-only.

 |
| itemSymbolFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

HM Symbol icon size of segmented button items.

Value range: \[0, +∞)

Default value: **20fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **symbolModifier** is set for **items**, **itemSymbolFontSize** has no effect.

This property is read-only.

 |
| itemSymbolFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

HM Symbol icon color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **symbolModifier** is set for **items**, **itemSymbolFontColor** has no effect.

This property is read-only.

 |
| itemSelectedSymbolFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

HM Symbol icon color of the selected segmented button item.

Default value: **$r('sys.color.font\_on\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **symbolModifier** is set for **items**, **itemSelectedSymbolFontColor** has no effect.

This property is read-only.

 |
| languageDirection | [Direction](../../common-definitions/enums/document.md#direction) | No | @Param | 

Language direction of the segmented button.

Default value: **Direction.Auto**

If the value is out of the range, the default value is used.

This property is read-only.

 |

#### MultiCapsuleSegmentButtonV2

MultiCapsuleSegmentButtonV2({
  items: SegmentButtonV2Items,
  selectedIndexes: number\[\],
  $selectedIndexes: OnSelectedIndexesChange,
  onItemClicked?: Callback<number>,
  itemMinFontScale?: number | Resource,
  itemMaxFontScale?: number | Resource,
  itemSpace?: LengthMetrics,
  itemFontColor?: ColorMetrics,
  itemSelectedFontColor?: ColorMetrics,
  itemFontSize?: LengthMetrics,
  itemSelectedFontSize?: LengthMetrics,
  itemFontWeight?: FontWeight,
  itemSelectedFontWeight?: FontWeight,
  itemBorderRadius?: LengthMetrics,
  itemBackgroundColor?: ColorMetrics,
  itemBackgroundEffect?: BackgroundEffectOptions,
  itemBackgroundBlurStyle?: BlurStyle,
  itemBackgroundBlurStyleOptions?: BackgroundBlurStyleOptions,
  itemSelectedBackgroundColor?: ColorMetrics,
  itemIconSize?: SizeT<LengthMetrics>,
  itemIconFillColor?: ColorMetrics,
  itemSelectedIconFillColor?: ColorMetrics,
  itemSymbolFontSize?: LengthMetrics,
  itemSymbolFontColor?: ColorMetrics,
  itemSelectedSymbolFontColor?: ColorMetrics,
  itemMinHeight?: LengthMetrics,
  itemPadding?: LocalizedPadding,
  languageDirection?: Direction
})

**Decorator**: @ComponentV2

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| items | [SegmentButtonV2Items](#segmentbuttonv2items) | Yes | 
@Require

@Param

 | 

Items of the segmented button.

If the value is **undefined**, the option information is not displayed.

This property is read-only.

 |
| selectedIndexes | number\[\] | Yes | 

@Require

@Param

 | 

Array of indexes of the selected segmented button items. The index is zero-based and increments by 1.

If the value is **undefined**, no item is selected.

**NOTE**

Only valid button indexes are supported. An empty array \[\] indicates no selection.

This property is read-only.

 |
| $selectedIndexes | [OnSelectedIndexesChange](#onselectedindexeschange) | Yes | @Event | Callback invoked when the selected item changes. |
| onItemClicked | Callback<number> | No | @Event | Callback invoked when a segmented button item is clicked. |
| itemBackgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Background color of unselected segmented button items.

Default value: **$r('sys.color.segment\_button\_v2\_multi\_capsule\_button\_background')**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| itemBackgroundEffect | [BackgroundEffectOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundeffectoptions11) | No | @Param | 

Background effect of segmented button items.

Default value: **undefined**

This property is read-only.

 |
| itemBackgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | @Param | 

Background blur style of segmented button items.

Default value: **undefined**

This property is read-only.

 |
| itemBackgroundBlurStyleOptions | [BackgroundBlurStyleOptions](../../universal-attributes/basic-attributes/background/document.md#backgroundblurstyleoptions10) | No | @Param | 

Background blur style options of segmented button items.

Default value: **undefined**

This property is read-only.

 |
| itemSelectedBackgroundColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Background color of the selected segmented button item.

Default value: **$r('sys.color.comp\_background\_emphasize')**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| itemMinHeight | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Minimum height of the segmented button item.

Value range: \[0, +∞)

Default value:

**$r('sys.float.segment\_button\_v2\_singleline\_selected\_height')** for text-only buttons and icon-only buttons, and **$r('sys.float.segment\_button\_v2\_doubleline\_selected\_height')** for buttons with both an icon and text.

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemPadding | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | @Param | 

Padding of the segmented button item.

Default value: **{top: LengthMetrics.resource ($r('sys.float.padding\_level2')), bottom: LengthMetrics.resource ($r('sys.float.padding\_level2')), start: LengthMetrics.resource($r('sys.float.padding\_level4')), end: LengthMetrics.resource($r('sys.float.padding\_level4'))}**

If the value is **undefined**, the default value is used.

This property is read-only.

 |
| itemSpace | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Space between segmented button items.

Value range: \[0, +∞)

Default value: **LengthMetrics.vp(1)**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

This property is read-only.

 |
| itemMinFontScale | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | @Param | 

Minimum font scale factor of the segmented button item text.

Value range: \[0, 1\]

Default value: **0**

**NOTE**

A value less than 0 is treated as **0**. A value greater than 1 is treated as **1**. Abnormal values are ineffective by default.

This property is read-only.

 |
| itemMaxFontScale | number | [Resource](../../common-definitions/basic-types/document.md#resource) | No | @Param | 

Maximum font scale factor of the segmented button item text.

Value range: \[1, 2\]

Default value: **1**

**NOTE**

A value less than 1 is treated as **1**. A value greater than 2 is treated as **2**. Abnormal values are ineffective by default.

This property is read-only.

 |
| itemSelectedFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Font size of the selected segmented button item.

Value range: \[0, +∞)

Default value: **14fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **textModifier** is set for **items**, **itemSelectedFontSize** has no effect.

This property is read-only.

 |
| itemFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Font color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **textModifier** is set for **items**, **itemFontColor** has no effect.

This property is read-only.

 |
| itemFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Font size of unselected segmented button items.

Value range: \[0, +∞)

Default value: **14fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **textModifier** is set for **items**, **itemFontSize** has no effect.

This property is read-only.

 |
| itemSelectedFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Font color of the selected segmented button item.

Default value: **$r('sys.color.font\_on\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **textModifier** is set for **items**, **itemSelectedFontColor** has no effect.

This property is read-only.

 |
| itemFontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | @Param | 

Font weight of unselected segmented button items.

Default value: **FontWeight.Medium**

If the value is out of the range, the default value is used.

**NOTE**

When **fontWeight** of **textModifier** is set for **items**, **itemFontWeight** has no effect.

This property is read-only.

 |
| itemSelectedFontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | @Param | 

Font weight of the selected segmented button item.

Default value: **FontWeight.Medium**

If the value is out of the range, the default value is used.

**NOTE**

When **fontWeight** of **textModifier** is set for **items**, **itemSelectedFontWeight** has no effect.

This property is read-only.

 |
| itemBorderRadius | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

Border radius of segmented button items.

Value range: \[0, +∞)

Default value: **$r('sys.float.segment\_button\_v2\_multi\_corner\_radius')**

If the value is out of the range, the default value is used.

This property is read-only.

 |
| itemIconSize | [SizeT](../../../arkts-api/ui/arkui/graphics/document.md#sizett12)<[LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12)\> | No | @Param | 

Image-type icon size of segmented button items.

Value range: \[0, +∞)

Default value: **{ width: LengthMetrics.vp(24), height: LengthMetrics.vp(24) }**

If the value is out of the range, the default value is used.

**NOTE**

When **width** and **height** of **iconModifier** are set for **items**, **itemIconSize** has no effect.

This property is read-only.

 |
| itemIconFillColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Icon color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fillColor** of **iconModifier** is set for **items**, **itemIconFillColor** has no effect.

This property is read-only.

 |
| itemSelectedIconFillColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

Icon color of the selected segmented button item.

Default value: **$r('sys.color.font\_on\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fillColor** of **iconModifier** is set for **items**, **itemSelectedIconFillColor** has no effect.

This property is read-only.

 |
| itemSymbolFontSize | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | @Param | 

HM Symbol icon size of segmented button items.

Value range: \[0, +∞)

Default value: **20fp**

**NOTE**

Percentage values are not supported. If an invalid value is set, the default value is used.

When **fontSize** of **symbolModifier** is set for **items**, **itemSymbolFontSize** has no effect.

This property is read-only.

 |
| itemSymbolFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

HM Symbol icon color of unselected segmented button items.

Default value: **$r('sys.color.font\_secondary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **symbolModifier** is set for **items**, **itemSymbolFontColor** has no effect.

This property is read-only.

 |
| itemSelectedSymbolFontColor | [ColorMetrics](../../../arkts-api/ui/arkui/graphics/document.md#colormetrics12) | No | @Param | 

HM Symbol icon color of the selected segmented button item.

Default value: **$r('sys.color.font\_on\_primary')**

If the value is **undefined**, the default value is used.

**NOTE**

When **fontColor** of **symbolModifier** is set for **items**, **itemSelectedSymbolFontColor** has no effect.

This property is read-only.

 |
| languageDirection | [Direction](../../common-definitions/enums/document.md#direction) | No | @Param | 

Language direction of the segmented button.

Default value: **Direction.Auto**

If the value is out of the range, the default value is used.

This property is read-only.

 |

#### SegmentButtonV2Items

Represents items of the **SegmentButtonV2** component.

This parameter is inherited from Array<[SegmentButtonV2Item](#segmentbuttonv2item)\>.

**Decorator type**: @ObservedV2

#### \[h2\]constructor

constructor(items: SegmentButtonV2ItemOptions\[\])

Constructs a **SegmentButtonV2ItemOptions** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| items | [SegmentButtonV2ItemOptions](#segmentbuttonv2itemoptions)\[\] | Yes | Options of the item of the **SegmentButtonV2** component. |

#### \[h2\]hasHybrid

get hasHybrid():boolean

Checks whether the component supports mixed icon and text items.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the component supports mixed icon and text items.

The value **true** indicates that there is an item with both an icon and text; the value **false** indicates the opposite.

 |

#### SegmentButtonV2Item

**Decorator type**: @ObservedV2

#### \[h2\]Properties

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Text of the segmented button item.

Default value: **undefined**

Decorator type: @Trace

 |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Image icon of the segmented button item.

Default value: **undefined**

Decorator type: @Trace

 |
| symbol | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

HM Symbol icon of the segmented button item.

Default value: **undefined**

Decorator type: @Trace

 |
| enabled | boolean | No | No | 

Whether the segmented button item is enabled.

Default value: **true**.

**true**: enabled. **false**: disabled.

If the value is **undefined**, the default value is used.

Decorator type: @Trace

 |
| textModifier | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md) | No | Yes | 

Text modifier for the segmented button item.

Default value: **undefined**

Decorator type: @Trace

 |
| iconModifier | [ImageModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md) | No | Yes | 

Image icon modifier for the segmented button item.

Default value: **undefined**

Decorator type: @Trace

 |
| symbolModifier | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/symbol-glyph-modifier/document.md#symbolglyphmodifier) | No | Yes | 

HM Symbol icon modifier for the segmented button item.

Default value: **undefined**

Decorator type: @Trace

 |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

[Accessibility text](../../universal-attributes/accessibility/document.md#accessibilitytext) of the segmented button item.

Default value: **""**

If the value is **undefined**, the default value is used.

Decorator type: @Trace

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

[Accessibility description](../../universal-attributes/accessibility/document.md#accessibilitydescription) of the segmented button item.

Default value: **""**

If the value is **undefined**, the default value is used.

Decorator type: @Trace

 |
| accessibilityLevel | string | No | Yes | 

[Accessibility level](../../universal-attributes/accessibility/document.md#accessibilitylevel) of the segmented button item.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

Decorator type: @Trace

 |

**Description**

1.  If both **symbol** and **icon** are configured, **symbol** takes precedence.
2.  If both **symbol** and **symbolModifier** are configured with HM Symbol resources, the resources specified by **symbolModifier** take precedence.

#### \[h2\]constructor

constructor(options: SegmentButtonV2ItemOptions)

Constructs a **SegmentButtonV2ItemOptions** instance.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SegmentButtonV2ItemOptions](#segmentbuttonv2itemoptions) | Yes | Options of the item of the **SegmentButtonV2** component. |

#### \[h2\]isHybrid

get isHybrid():boolean

Checks whether the segmented button item contains both text and icon configurations.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | 
Whether the item contains both text and icon configurations.

**true**: The item has both text and icon configurations. **false**: The item does not have both text and icon configured.

 |

#### SegmentButtonV2ItemOptions

Defines segmented button item options.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Text of the segmented button item.

Default value: **undefined**

 |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon of the segmented button item.

Default value: **undefined**

 |
| symbol | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

HM Symbol icon of the segmented button item.

Default value: **undefined**

 |
| enabled | boolean | No | Yes | 

Whether the segmented button item is enabled.

Default value: **true**

The value **true** means that the item is enabled, and **false** means the opposite.

If the value is **undefined**, the default value is used.

 |
| textModifier | [TextModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md) | No | Yes | 

Text modifier for the segmented button item.

Default value: **undefined**

 |
| iconModifier | [ImageModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md) | No | Yes | 

Icon modifier for the segmented button item.

Default value: **undefined**

 |
| symbolModifier | [SymbolGlyphModifier](../../universal-attributes/modifiers-and-custom-property/attribute-modifier/document.md) | No | Yes | 

HM Symbol icon modifier for the segmented button item.

Default value: **undefined**

 |
| accessibilityText | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

[Accessibility text](../../universal-attributes/accessibility/document.md#accessibilitytext) of the segmented button item.

Default value: **""**

If the value is **undefined**, the default value is used.

 |
| accessibilityDescription | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

[Accessibility description](../../universal-attributes/accessibility/document.md#accessibilitydescription) of the segmented button item.

Default value: **""**

If the value is **undefined**, the default value is used.

 |
| accessibilityLevel | string | No | Yes | 

[Accessibility level](../../universal-attributes/accessibility/document.md#accessibilitylevel) of the segmented button item.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

 |

**Description**

1.  If both **symbol** and **icon** are configured, **symbol** takes precedence.
2.  If both **symbol** and **symbolModifier** are configured with HM Symbol resources, the resources specified by **symbolModifier** take precedence.

#### OnSelectedIndexChange

type OnSelectedIndexChange = (selectedIndex: number) => void

Defines a callback invoked when the selected segmented button item changes.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectedIndex | number | Yes | Index of the selected segmented button item. |

#### OnSelectedIndexesChange

type OnSelectedIndexesChange = (selectedIndexes: number\[\]) => void

Defines a callback invoked when the selected segmented button items change.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| selectedIndexes | number\[\] | Yes | Indexes of selected segmented button items. |

#### Example

## Example 1: Using the TabSegmentButtonV2

This example describes how to use the **TabSegmentButtonV2** component.

import { SegmentButtonV2Items, TabSegmentButtonV2 } from '@kit.ArkUI';

@Entry
@ComponentV2
struct TabSegmentButtonV2Example {
  @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Phone'},
    { text: 'Tablet' },
    { text: '2-in-1' },
    { text: 'Wearable' },
  \]);
  @Local textSelectedIndex: number = 0;
  @Local imageItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { icon: $r('sys.media.ohos\_ic\_public\_device\_phone') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_pad') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_matebook') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_watch') },
  \]);
  @Local imageSelectedIndex: number = 0;
  @Local symbolItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { symbol: $r('sys.symbol.phone') },
    { symbol: $r('sys.symbol.pad') },
    { symbol: $r('sys.symbol.matebook') },
    { symbol: $r('sys.symbol.watch') },
  \]);
  @Local symbolSelectedIndex: number = 0;
  @Local hybridItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Phone', symbol: $r('sys.symbol.phone') },
    { text: 'Tablet', symbol: $r('sys.symbol.pad') },
    { text: '2-in-1', symbol: $r('sys.symbol.matebook') },
    { text: 'Wearable', symbol: $r('sys.symbol.watch') },
  \]);
  @Local hybridSelectedIndex: number = 0;
  @Local freeItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Year' },
    { text: 'Month' },
    { text: 'Week' },
    { text: 'Day' },
    { icon: $r('sys.media.ohos\_ic\_public\_search\_filled') },
  \]);
  @Local freeSelectedIndex: number = 0;

  build() {
    Scroll() {
      Column({ space: 12 }) {
        VCard({ title: 'Text Button' }) {
          TabSegmentButtonV2({
            items: this.textItems,
            selectedIndex: this.textSelectedIndex!!,
          })
        }

        VCard({ title: 'Image Button' }) {
          TabSegmentButtonV2({
            items: this.imageItems,
            selectedIndex: this.imageSelectedIndex!!,
          })
        }

        VCard({ title: 'Symbol Button' }) {
          TabSegmentButtonV2({
            items: this.symbolItems,
            selectedIndex: this.symbolSelectedIndex!!,
          })
        }

        VCard({ title: 'Text and Icon Button' }) {
          TabSegmentButtonV2({
            items: this.hybridItems,
            selectedIndex: this.hybridSelectedIndex!!,
          })
        }

        VCard({ title: 'Custom Button' }) {
          TabSegmentButtonV2({
            items: this.freeItems,
            selectedIndex: this.freeSelectedIndex!!,
          })
        }
        
        Button (\`Usage instructions for the isHybrid API, ${this.textItems\[0\].isHybrid}\`) // false is displayed for text-only items.
          .width('70%')

        Button (\`Usage instructions for the isHybrid API, ${this.hybridItems\[0\].isHybrid}\`) // true is displayed for items with both text and an icon.
          .width('70%')

        Button ('Usage instructions for the hasHybrid API, ${this.textItems.hasHybrid}\`) // false is displayed when a segmented button does not support items with both text and an icon.
          .width('70%')

        Button ('Usage instructions for the hasHybrid API, ${this.hybridItems.hasHybrid}\`) // true is displayed when a segmented button supports items with both text and an icon.
          .width('70%')
      }
      .constraintSize({ minHeight: '100%' })
      .justifyContent(FlexAlign.Start)
      .padding(16)
    }
    .backgroundColor('#f1f3f5')
    .width('100%')
    .height('100%')
  }
}

@Builder
function Noop() {
}

@Component
export struct VCard {
  @Prop
  title: ResourceStr;
  @BuilderParam
  content: () => void = Noop;

  build() {
    Column({ space: 8 }) {
      if (this.title) {
        Text(this.title)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .constraintSize({ maxWidth: '80%' })
      }
      this.content()
    }
    .backgroundColor(Color.White)
    .borderRadius(8)
    .padding(8)
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/que2Yq5dSn6pGURF7vOklQ/en-us_image_0000002537765988.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7FF1BECA62C0DB27DDF2E84172F73C2952504F705CE55A1829596CA7F289B60F)

## Example 2: Using the CapsuleSegmentButtonV2

This example describes how to use the **CapsuleSegmentButtonV2** component.

import { CapsuleSegmentButtonV2, SegmentButtonV2Items } from '@kit.ArkUI';

@Entry
@ComponentV2
struct CapsuleSegmentButtonV2Example {
  @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Phone'},
    { text: 'Tablet' },
    { text: '2-in-1' },
    { text: 'Wearable' },
  \]);
  @Local textSelectedIndex: number = 0;
  @Local imageItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { icon: $r('sys.media.ohos\_ic\_public\_device\_phone') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_pad') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_matebook') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_watch') },
  \]);
  @Local imageSelectedIndex: number = 0;
  @Local symbolItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { symbol: $r('sys.symbol.phone') },
    { symbol: $r('sys.symbol.pad') },
    { symbol: $r('sys.symbol.matebook') },
    { symbol: $r('sys.symbol.watch') },
  \]);
  @Local symbolSelectedIndex: number = 0;
  @Local hybridItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Phone', symbol: $r('sys.symbol.phone') },
    { text: 'Tablet', symbol: $r('sys.symbol.pad') },
    { text: '2-in-1', symbol: $r('sys.symbol.matebook') },
    { text: 'Wearable', symbol: $r('sys.symbol.watch') },
  \]);
  @Local hybridSelectedIndex: number = 0;
  @Local freeItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Year' },
    { text: 'Month' },
    { text: 'Week' },
    { text: 'Day' },
    { icon: $r('sys.media.ohos\_ic\_public\_search\_filled') },
  \]);
  @Local freeSelectedIndex: number = 0;

  build() {
    Scroll() {
      Column({ space: 12 }) {
        VCard({ title: 'Text Button' }) {
          CapsuleSegmentButtonV2({
            items: this.textItems,
            selectedIndex: this.textSelectedIndex!!,
          })
        }

        VCard({ title: 'Image Button' }) {
          CapsuleSegmentButtonV2({
            items: this.imageItems,
            selectedIndex: this.imageSelectedIndex!!,
          })
        }

        VCard({ title: 'Symbol Button' }) {
          CapsuleSegmentButtonV2({
            items: this.symbolItems,
            selectedIndex: this.symbolSelectedIndex!!,
          })
        }

        VCard({ title: 'Text and Icon Button' }) {
          CapsuleSegmentButtonV2({
            items: this.hybridItems,
            selectedIndex: this.hybridSelectedIndex!!,
          })
        }

        VCard({ title: 'Custom Button' }) {
          CapsuleSegmentButtonV2({
            items: this.freeItems,
            selectedIndex: this.freeSelectedIndex!!,
          })
        }
      }
      .constraintSize({ minHeight: '100%' })
      .justifyContent(FlexAlign.Start)
      .padding(16)
    }
    .backgroundColor('#f1f3f5')
    .width('100%')
    .height('100%')
  }
}

@Builder
function Noop() {
}

@Component
export struct VCard {
  @Prop
  title: ResourceStr;
  @BuilderParam
  content: () => void = Noop;

  build() {
    Column({ space: 8 }) {
      if (this.title) {
        Text(this.title)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .constraintSize({ maxWidth: '80%' })
      }
      this.content()
    }
    .backgroundColor(Color.White)
    .borderRadius(8)
    .padding(8)
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4d/v3/6HmQQhUFRbum3pL2vAf6Nw/en-us_image_0000002537925928.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD2979FBB440D3145B58721742B0B5D2B0ACD28730E5F6FD0887A80BD9CD55DE)

## Example 3: Using the MultiCapsuleSegmentButtonV2

This example describes how to use the **MultiCapsuleSegmentButtonV2** component.

import { MultiCapsuleSegmentButtonV2, SegmentButtonV2Items } from '@kit.ArkUI';

@Entry
@ComponentV2
struct MultiCapsuleSegmentButtonV2Example {
  @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Phone'},
    { text: 'Tablet' },
    { text: '2-in-1' },
    { text: 'Wearable' },
  \]);
  @Local textSelectedIndexes: number\[\] = \[0\];
  @Local imageItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { icon: $r('sys.media.ohos\_ic\_public\_device\_phone') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_pad') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_matebook') },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_watch') },
  \]);
  @Local imageSelectedIndexes: number\[\] = \[0\];
  @Local symbolItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { symbol: $r('sys.symbol.phone') },
    { symbol: $r('sys.symbol.pad') },
    { symbol: $r('sys.symbol.matebook') },
    { symbol: $r('sys.symbol.watch') },
  \]);
  @Local symbolSelectedIndexes: number\[\] = \[0\];
  @Local hybridItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Phone', symbol: $r('sys.symbol.phone') },
    { text: 'Tablet', symbol: $r('sys.symbol.pad') },
    { text: '2-in-1', symbol: $r('sys.symbol.matebook') },
    { text: 'Wearable', symbol: $r('sys.symbol.watch') },
  \]);
  @Local hybridSelectedIndexes: number\[\] = \[0\];
  @Local freeItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Year' },
    { text: 'Month' },
    { text: 'Week' },
    { text: 'Day' },
    { icon: $r('sys.media.ohos\_ic\_public\_search\_filled') },
  \]);
  @Local freeSelectedIndexes: number\[\] = \[0\];

  build() {
    Scroll() {
      Column({ space: 12 }) {
        VCard({ title: 'Text Button' }) {
          MultiCapsuleSegmentButtonV2({
            items: this.textItems,
            selectedIndexes: this.textSelectedIndexes!!,
          })
        }

        VCard({ title: 'Image Button' }) {
          MultiCapsuleSegmentButtonV2({
            items: this.imageItems,
            selectedIndexes: this.imageSelectedIndexes!!,
          })
        }

        VCard({ title: 'Symbol Button' }) {
          MultiCapsuleSegmentButtonV2({
            items: this.symbolItems,
            selectedIndexes: this.symbolSelectedIndexes!!,
          })
        }

        VCard({ title: 'Text and Icon Button' }) {
          MultiCapsuleSegmentButtonV2({
            items: this.hybridItems,
            selectedIndexes: this.hybridSelectedIndexes!!,
          })
        }

        VCard({ title: 'Custom Button' }) {
          MultiCapsuleSegmentButtonV2({
            items: this.freeItems,
            selectedIndexes: this.freeSelectedIndexes!!,
          })
        }
      }
      .constraintSize({ minHeight: '100%' })
      .justifyContent(FlexAlign.Start)
      .padding(16)
    }
    .backgroundColor('#f1f3f5')
    .width('100%')
    .height('100%')
  }
}

@Builder
function Noop() {
}

@Component
export struct VCard {
  @Prop
  title: ResourceStr;
  @BuilderParam
  content: () => void = Noop;

  build() {
    Column({ space: 8 }) {
      if (this.title) {
        Text(this.title)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .constraintSize({ maxWidth: '80%' })
      }
      this.content()
    }
    .backgroundColor(Color.White)
    .borderRadius(8)
    .padding(8)
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/8ki2K-G5TBii7kQLFIKp3g/en-us_image_0000002568685705.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69AB347EC09FCB1525DDD190A67CCD93AB4079567686B4683F6412F54B6E48E0)

## Example 4: Implementing Basic Usage of the Segmented Button Modifier

This example shows the basic usage of the modifiers for **TabSegmentButtonV2**, **CapsuleSegmentButtonV2**, and **MultiCapsuleSegmentButtonV2** components.

import {
  SegmentButtonV2Items,
  TabSegmentButtonV2,
  CapsuleSegmentButtonV2,
  MultiCapsuleSegmentButtonV2,
  TextModifier,
  ImageModifier,
  SymbolGlyphModifier
} from '@kit.ArkUI';

@Entry
@ComponentV2
struct SegmentButtonV2Example {
  @Local textItems: SegmentButtonV2Items = new SegmentButtonV2Items(\[
    { text: 'Phone', textModifier: new TextModifier().fontSize(20) },
    { text: 'Tablet' },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_phone'), iconModifier: new ImageModifier().height(17).width(17) },
    { icon: $r('sys.media.ohos\_ic\_public\_device\_pad') },
    { symbol: $r('sys.symbol.phone'), symbolModifier: new SymbolGlyphModifier().fontColor(\[Color.Pink\]) },
    { symbolModifier: new SymbolGlyphModifier($r('sys.symbol.pad')).fontColor(\[Color.Orange\]) },
    { symbol: $r('sys.symbol.matebook') },
  \]);
  @Local textSelectedIndex: number = 0;
  @Local freeSelectedIndex: number\[\] = \[0\];

  build() {
    Column() {
      VCard({ title: 'TabSegmentButtonV2' }) {
        TabSegmentButtonV2({
          items: this.textItems,
          selectedIndex: this.textSelectedIndex!!,
        })
      }

      VCard({ title: 'CapsuleSegmentButtonV2' }) {
        CapsuleSegmentButtonV2({
          items: this.textItems,
          selectedIndex: this.textSelectedIndex!!,
        })
      }

      VCard({ title: 'MultiCapsuleSegmentButtonV2' }) {
        MultiCapsuleSegmentButtonV2({
          items: this.textItems,
          selectedIndexes: this.freeSelectedIndex!!,
        })
      }

    }
    .constraintSize({ minHeight: '100%' })
    .justifyContent(FlexAlign.Start)
    .padding(16)

  }
}

@Builder
function Noop() {
}

@Component
export struct VCard {
  @Prop
  title: ResourceStr;
  @BuilderParam
  content: () => void = Noop;

  build() {
    Column({ space: 8 }) {
      if (this.title) {
        Text(this.title)
          .maxLines(1)
          .textOverflow({ overflow: TextOverflow.Ellipsis })
          .constraintSize({ maxWidth: '80%' })
      }
      this.content()
    }
    .backgroundColor(Color.White)
    .borderRadius(8)
    .padding(8)
    .width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/2OocGBAJQGKzIfETN2Is1A/en-us_image_0000002568765715.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6050C3EA337C0F84D3AC9761AB48435C301A8C01B682E9C6C633298B7B22EA4)
