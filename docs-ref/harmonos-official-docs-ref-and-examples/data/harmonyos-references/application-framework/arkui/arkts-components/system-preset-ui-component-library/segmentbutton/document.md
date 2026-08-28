# SegmentButton

**SegmentButton** is a versatile component that organizes related options into visually grouped buttons. It supports three variants: tab-style, capsule-style single-select, and capsule-style multi-select.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/GmFWddSmSSeXxunAk2XeLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99EA1850760833BFBA8D166D6861586E7F25E196F89098C42C381A2134B333DF)

This component is supported since API version 11. Updates will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { SegmentButton, SegmentButtonOptions, SegmentButtonItemOptionsArray } from '@kit.ArkUI';

#### Child Components

Not supported

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are not supported.

#### Events

The [universal events](../../universal-events/document.md) are not supported.

#### SegmentButton

SegmentButton({ options: SegmentButtonOptions, selectedIndexes: number\[\], onItemClicked: Callback<number>, maxFontScale: number | Resource })

**Decorator**: @Component

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Mandatory | Decorator | Description |
| :-- | :-- | :-- | :-- | :-- |
| options | [SegmentButtonOptions](#segmentbuttonoptions) | Yes | @ObjectLink | 
Options of the **SegmentButton** component.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedIndexes | number\[\] | Yes | @Link | 

Indexes of selected items of the **SegmentButton**. The index is zero-based and increments by 1.

**NOTE**

**selectedIndexes** is decorated with [@Link](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-link) to implement parent-child two-way synchronization. If no items are selected, an empty array **\[\]** can be passed in.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| onItemClicked13+ | Callback<number> | No | \- | 

Callback function triggered when a segment button option is tapped. The subscript of the tapped option is passed as a parameter.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| maxFontScale14+ | number | [Resource](../../common-definitions/basic-types/document.md#resource) | Yes | @Prop | 

Maximum font scale for the text in the **SegmentButton**.

Value range: \[1, 2\]

Values less than 1 are treated as 1, and values greater than 2 are treated as 2.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/sEB15BXjThy91JpJ7YHD9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8220B5C49CB5CDF7B97DE94B06CA975957E65D8367F00F4A1BDCD5591A8EAA2F)

The **SegmentButton** component does not support [universal attributes](../../universal-attributes/document.md). The component occupies the maximum available width within its content area and distributes this width evenly among its items. It adapts its height automatically to the content (text and images), the minimum height being 28 vp.

#### SegmentButtonOptions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/mKUjmfLrRu2aRYWeA9gjiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=14DE1489C34E3BC00BE8958C08ACD3D3914AADB178408CED54DEB337804FA35D)

The component does not support custom font type settings.

Provides initial data and custom properties for the **SegmentButton** component.

**Decorator Type**: @Observed

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | "tab" |"capsule" | No | No | 
Type of the **SegmentButton** component.

**NOTE**

**"tab"**: tab-style segmented buttons, designed for page or content section switching.

**"capsule"**: capsule-style segmented buttons, suitable for single or multiple selection scenarios.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| multiply | boolean | No | No | 

Whether multiple items can be selected.

**true**: Multiple items can be selected.

**false**: Multiple items cannot be selected. For the **SegmentButton** component consisting of tab-style buttons, only one item can be selected. In this case, setting **multiply** to **true** does not take effect.

If the value is **undefined**, the component does not support selection of multiple items.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| buttons | [SegmentButtonItemOptionsArray](#segmentbuttonitemoptionsarray) | No | No | 

Button information of the component, including the icon and text.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Text color of the unselected button.

If the value is **undefined**, the color is $r('sys.color.ohos\_id\_color\_text\_secondary').

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedFontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Text color of the selected button.

If the value is **undefined**, the color is $r('sys.color.ohos\_id\_color\_text\_primary') when type is set to **"tab"**.

When type is set to **"capsule"**, the color is $r('sys.color.ohos\_id\_color\_foreground\_contrary').

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fontSize | [DimensionNoPercentage](#dimensionnopercentage) | No | No | 

Font size of the unselected button. The value cannot be set in percentage.

If the value is **undefined**, the font size is $r('sys.float.ohos\_id\_text\_size\_body2').

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedFontSize | [DimensionNoPercentage](#dimensionnopercentage) | No | No | 

Font size of the selected button. The value cannot be set in percentage.

If the value is **undefined**, the font size is $r('sys.float.ohos\_id\_text\_size\_body2').

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | No | 

Font weight of the unselected button.

If the value is **undefined**, the font weight is **FontWeight.Regular**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedFontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | No | 

Font weight of the selected button.

If the value is **undefined**, the font weight is **FontWeight.Medium**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Background color of the component.

If the value is **undefined**, the background color is $r('sys.color.ohos\_id\_color\_button\_normal').

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedBackgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | No | 

Background color of the selected button.

When the value is **undefined** and **type** is **"tab"**, the background color is **$r('sys.color.segment\_button\_checked\_foreground\_color')**.

When **type** is **"capsule"**, the background color is **$r('sys.color.ohos\_id\_color\_emphasize')**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| imageSize | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | No | No | 

Image size of the component.

When the value is **undefined**, the image size is { width: 24, height: 24 }.

Unit: vp

**NOTE**

This attribute is effective only for buttons that contain icons.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| buttonPadding | [Padding](../../common-definitions/basic-types/document.md#padding) | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | No | 

Button padding of the component.

When the value is **undefined**, the button padding settings are as follows:

Icon button and text button: **{ top: 4, right: 8, bottom: 4, left: 8 }**.

Icon + text button: **{ top: 6, right: 8, bottom: 6, left: 8 }**.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| textPadding | [Padding](../../common-definitions/basic-types/document.md#padding) | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | No | 

Text padding of the component.

When the value is **undefined**, the text padding is 0.

Unit: vp

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| localizedButtonPadding12+ | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | Yes | 

Button padding of the component.

Default value:

Icon button and text button: **{ top: LengthMetrics.vp(4), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(4), start: LengthMetrics.vp(8) }**.

Icon + text button: \*\*{ top: LengthMetrics.vp(6), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(6), start: LengthMetrics.vp(8) \*\*}.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| localizedTextPadding12+ | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | Yes | 

Text padding.

Default value: **0**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| direction12+ | [Direction](../../common-definitions/enums/document.md#direction) | No | Yes | 

Layout direction of the component.

Default value: **Direction.Auto**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | No | 

Background blur style of the component.

If the value is **undefined**, it defaults to **BlurStyle.NONE**.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderRadiusMode20+ | [BorderRadiusMode](#borderradiusmode20) | No | Yes | 

Border radius mode, used to control the border radius calculation method.

Default value: **BorderRadiusMode.DEFAULT**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| backgroundBorderRadius20+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Container border radius.

**NOTE**

This attribute takes effect only when **borderRadiusMode** is set to **BorderRadiusMode.CUSTOM**.

For capsule-style multi-selection segmented buttons (with **type** being **"capsule"** and **multiply** being **true**), this attribute does not take effect and **itemBorderRadius** must be used to set the border radius.

The maximum value for the border radius is half of the component's width or height, and percentage values are not supported.

Default value: **$r('sys.float.segmentbutton\_container\_shape')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| itemBorderRadius20+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Individual button border radius.

**NOTE**

This attribute takes effect only when **borderRadiusMode** is set to **BorderRadiusMode.CUSTOM**.

For capsule-style multi-selection segmented buttons (with **type** being **"capsule"** and **multiply** being **true**), this attribute only affects end items.

The maximum value for the border radius is half of the component's width or height, and percentage values are not supported.

Default value: **$r('sys.float.segmentbutton\_selected\_background\_shape')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### \[h2\]constructor

constructor(options: TabSegmentButtonOptions | CapsuleSegmentButtonOptions)

Constructor.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TabSegmentButtonOptions](#tabsegmentbuttonoptions) | [CapsuleSegmentButtonOptions](#capsulesegmentbuttonoptions) | Yes | Configuration options for tab-style or capsule-style segmented buttons. |

#### \[h2\]tab

static tab(options: TabSegmentButtonConstructionOptions): SegmentButtonOptions

Creates a SegmentButtonOptions class to define tabs.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [TabSegmentButtonConstructionOptions](#tabsegmentbuttonconstructionoptions) | Yes | Configuration options for tab-style segmented buttons. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SegmentButtonOptions](#segmentbuttonoptions) | Options of the **SegmentButton** component. |

#### \[h2\]capsule

static capsule(options: CapsuleSegmentButtonConstructionOptions): SegmentButtonOptions

Creates a **SegmentButtonOptions** object specifically for capsule-style segmented buttons.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CapsuleSegmentButtonConstructionOptions](#capsulesegmentbuttonconstructionoptions) | Yes | Configuration options for capsule-style segmented buttons. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SegmentButtonOptions](#segmentbuttonoptions) | Options of the **SegmentButton** component. |

#### DimensionNoPercentage

type DimensionNoPercentage = PX | VP | FP | LPX | Resource

The percentage length union type is not supported.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| [PX](../../common-definitions/basic-types/document.md#px10) | Length in px. |
| [VP](../../common-definitions/basic-types/document.md#vp10) | Length in vp. |
| [FP](../../common-definitions/basic-types/document.md#fp10) | Length in fp. |
| [LPX](../../common-definitions/basic-types/document.md#lpx10) | Length in lpx. |
| [Resource](../../common-definitions/basic-types/document.md#resource) | Resource reference type, which is used to set the value of a component attribute. |

#### CommonSegmentButtonOptions

Defines the customizable attributes of a segment button component.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Font color of the unselected item.

Default value: **$r('sys.color.ohos\_id\_color\_text\_secondary')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedFontColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Font color of the selected item.

Default value:

The default value is **$r('sys.color.ohos\_id\_color\_text\_primary')** when **type** is **"tab"**

The default value is **$r('sys.color.ohos\_id\_color\_foreground\_contrary')** when **type** is **"capsule"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fontSize | [DimensionNoPercentage](#dimensionnopercentage) | No | Yes | 

Font size of the unselected item. It cannot be set in percentage.

Default value: **$r('sys.float.ohos\_id\_text\_size\_body2')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedFontSize | [DimensionNoPercentage](#dimensionnopercentage) | No | Yes | 

Font size of the selected item. It cannot be set in percentage.

Default value: **$r('sys.float.ohos\_id\_text\_size\_body2')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| fontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | Yes | 

Font weight of the unselected item.

Default value: **FontWeight.Regular**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedFontWeight | [FontWeight](../../common-definitions/enums/document.md#fontweight) | No | Yes | 

Font weight of the selected item.

Default value: FontWeight.Medium

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color.

Default value: **$r('sys.color.ohos\_id\_color\_button\_normal')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedBackgroundColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Background color of the button in the selected state.

Default value:

The default value is **$r('sys.color.segment\_button\_checked\_foreground\_color')** when **type** is **"tab"**.

The default value is **$r('sys.color.ohos\_id\_color\_emphasize')** when **type** is **"capsule"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| imageSize | [SizeOptions](../../common-definitions/basic-types/document.md#sizeoptions) | No | Yes | 

Defines the image size.

Default value: { width: 24, height: 24 }

Unit: vp

If the value is **undefined**, the default value is used.

**NOTE**

The imageSize attribute takes effect only for icon buttons and icon+text buttons.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| buttonPadding | [Padding](../../common-definitions/basic-types/document.md#padding) | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Button padding.

Default value:

For icon buttons and text buttons: { top: 4, right: 8, bottom: 4, left: 8 }

For icon+text buttons: { top: 6, right: 8, bottom: 6, left: 8 }

Unit: vp

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| textPadding | [Padding](../../common-definitions/basic-types/document.md#padding) | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Text padding.

Default value: **0**

Unit: vp

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| localizedButtonPadding12+ | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | Yes | 

Button padding.

Default value:

Icon button and text button: **{ top: LengthMetrics.vp(4), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(4), start: LengthMetrics.vp(8) }**.

Icon + text button: \*\*{ top: LengthMetrics.vp(6), end: LengthMetrics.vp(8), bottom: LengthMetrics.vp(6), start: LengthMetrics.vp(8) \*\*}.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| localizedTextPadding12+ | [LocalizedPadding](../../common-definitions/basic-types/document.md#localizedpadding12) | No | Yes | 

Text padding.

Default value: **0**

Unit: vp

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| direction12+ | [Direction](../../common-definitions/enums/document.md#direction) | No | Yes | 

Layout direction.

Default value: **Direction.Auto**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| backgroundBlurStyle | [BlurStyle](../../universal-attributes/basic-attributes/background/document.md#blurstyle9) | No | Yes | 

Background blur style applied between the content and the background.

Default value: **BlurStyle.NONE**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| borderRadiusMode20+ | [BorderRadiusMode](#borderradiusmode20) | No | Yes | 

Border radius mode, used to control the border radius calculation method.

Default value: **BorderRadiusMode.DEFAULT**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| backgroundBorderRadius20+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Container border radius.

**NOTE**

This attribute takes effect only when **borderRadiusMode** is set to **BorderRadiusMode.CUSTOM**.

For capsule-style multi-selection segmented buttons (with **type** being **"capsule"** and **multiply** being **true**), this attribute does not take effect and **itemBorderRadius** must be used to set the border radius.

The maximum value for the border radius is half of the component's width or height, and percentage values are not supported.

Default value: **$r('sys.float.segmentbutton\_container\_shape')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| itemBorderRadius20+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Individual button border radius.

**NOTE**

This attribute takes effect only when **borderRadiusMode** is set to **BorderRadiusMode.CUSTOM**.

For capsule-style multi-selection segmented buttons (with **type** being **"capsule"** and **multiply** being **true**), this attribute only affects end items.

The maximum value for the border radius is half of the component's width or height, and percentage values are not supported.

Default value: **$r('sys.float.segmentbutton\_selected\_background\_shape')**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### BorderRadiusMode20+

Enumerates the border radius modes for the **SegmentButton** component, which are used to control the border radius calculation method.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Default mode, where the framework automatically calculates the border radius. |
| CUSTOM | 1 | Custom mode, where the border radius is set by the developer. |

#### TabSegmentButtonConstructionOptions

Creates a SegmentButtonOptions object of the tab type.

Inherits from [CommonSegmentButtonOptions](#commonsegmentbuttonoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| buttons | [ItemRestriction](#itemrestriction)<[SegmentButtonTextItem](#segmentbuttontextitem)\> | No | No | Button information. |

#### CapsuleSegmentButtonConstructionOptions

Represents configuration options for creating a **SegmentButton** component consisting of capsule-style segmented buttons.

Inherits from [CommonSegmentButtonOptions](#commonsegmentbuttonoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| buttons | [SegmentButtonItemTuple](#segmentbuttonitemtuple) | No | No | Button information. |
| multiply | boolean | No | Yes | 
Whether multiple items can be selected.

Default value: **false**

If the value is **undefined**, the default value is used.

**true**: Multi-selection is allowed.

**false**: Multi-selection is not allowed.

 |

#### ItemRestriction

type ItemRestriction<T> = \[T, T, T?, T?, T?\]

Tuple type that stores button information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| \[T, T, T?, T?, T?\] | A tuple that contains two to five elements of the same type. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/Pyb-f4NVSViAdHKOtTU3aA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E0FEB7460EA08CD5782FCC418EABB8C6D554153AFB9EDCD5A5DD73948E61E900)

A **SegmentButton** component supports two to five buttons.

#### SegmentButtonItemTuple

type SegmentButtonItemTuple = ItemRestriction<SegmentButtonTextItem> | ItemRestriction<SegmentButtonIconItem> | ItemRestriction<SegmentButtonIconTextItem>

Represents the tuple union type used to store button information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| [ItemRestriction](#itemrestriction)<[SegmentButtonTextItem](#segmentbuttontextitem)\> | A tuple of text-only button information. |
| [ItemRestriction](#itemrestriction)<[SegmentButtonIconItem](#segmentbuttoniconitem)\> | A tuple of icon-only button information. |
| [ItemRestriction](#itemrestriction)<[SegmentButtonIconTextItem](#segmentbuttonicontextitem)\> | A tuple of icon and text button information. |

#### SegmentButtonItemArray

type SegmentButtonItemArray = Array<SegmentButtonTextItem> | Array<SegmentButtonIconItem> | Array<SegmentButtonIconTextItem>

Represents the array union type used to store button information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Type | Description |
| :-- | :-- |
| Array<[SegmentButtonTextItem](#segmentbuttontextitem)\> | An array of text-only button information. |
| Array<[SegmentButtonIconItem](#segmentbuttoniconitem)\> | An array of icon-only button information. |
| Array<[SegmentButtonIconTextItem](#segmentbuttonicontextitem)\> | An array of icon and text button information. |

#### SegmentButtonItemOptionsArray

Represents an array for storing button information.

**Decorator Type**: @Observed

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/PVfNxdEeTeCZrtDWibpNUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A17949CD4FF370D2F9C1813BCF7027E250F1D43E3F9CF9FF1F1560B17D48F7C)

The SegmentButtonItemOptionsArray can save only two to five button information elements.

#### \[h2\]constructor

constructor(elements: SegmentButtonItemTuple)

Constructor.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elements | [SegmentButtonItemTuple](#segmentbuttonitemtuple) | Yes | Button information. |

#### \[h2\]push

push(...items: SegmentButtonItemArray): number

Adds the specified elements to the end of this array and returns the new length of the array.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| items | [SegmentButtonItemArray](#segmentbuttonitemarray) | No | 
Elements to add to the end of the array.

Default value: array with 0 new button information items

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the array after the elements are added. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/aXHOgLP-QQiW-yhNTozUqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9775150AB92B230964BD4B9EC19557D7971B35DF25F44EDAE425258A35460C45)

A **SegmentButton** component array supports 2 to 5 buttons. If this limit is exceeded, the add operation will fail.

#### \[h2\]pop

pop(): SegmentButtonItemOptions | undefined

Removes the last element from this array and returns that element.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Return value**

| Type | Description |
| :-- | :-- |
| [SegmentButtonItemOptions](#segmentbuttonitemoptions) | undefined | Element removed from the array. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/KA60HhAVRs-tsFKSt7viMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B834652E3D83978EB7D6B1D3A8F9E29A5881230A00CB56A3BB42C439E8E28063)

A **SegmentButton** component array supports 2 to 5 buttons. If this limit is exceeded, this API will not take effect. If the number of buttons after removal falls outside this valid range, the removal operation will fail.

#### \[h2\]shift

shift(): SegmentButtonItemOptions | undefined

Removes the first element from this array and returns that element.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Return value**

| Type | Description |
| :-- | :-- |
| [SegmentButtonItemOptions](#segmentbuttonitemoptions) | undefined | Element removed from the array. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/8VnovnK-SZS10BdF9QlUag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F19C1A887A9719BE91656EEFBCCB7895B90522B9B81DF48CD14DC4E4DC856D5C)

A **SegmentButton** component array supports 2 to 5 buttons. If this limit is exceeded, this API will not take effect. If the number of buttons after removal falls outside this valid range, the removal operation will fail.

#### \[h2\]unshift

unshift(...items: SegmentButtonItemArray): number

Adds an element to the beginning of this array and returns the new length of the array.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| items | [SegmentButtonItemArray](#segmentbuttonitemarray) | No | 
Elements to add to the beginning of the array.

Default value: array with 0 new button information items

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the array after the elements are added. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/pUS2BCgXQ7-Z97T5rU5Ulg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC0DA77CB2F9D2530FBE12A516AF99CB774F411CA2086E4843396D6CC2E67838)

A maximum of two to five buttons can be saved in the segment button component array. If the number of segment button components exceeds the upper limit, the button information element fails to be added.

#### \[h2\]splice

splice(start: number, deleteCount: number, ...items: SegmentButtonItemOptions\[\]): SegmentButtonItemOptions\[\]

Changes the contents of this array by removing the specified number of elements from the specified position and adding new elements in place. This API returns an array containing the removed elements.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| start | number | Yes | Index of the position starting from which elements are to be removed. |
| deleteCount | number | Yes | Number of elements to remove. |
| items | [SegmentButtonItemOptions](#segmentbuttonitemoptions)\[\] | No | 
Element to be added to the array from start.

Default value: If no element is specified, the element is deleted from the array.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [SegmentButtonItemOptions](#segmentbuttonitemoptions)\[\] | An array containing the removed elements. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/V3chqwIhQ7iOJowS5nf7Eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C73940A483481A27D402F180E3659E6AE4CFA43DBC308076F395D660E3FA3F82)

The segment button component array saves information about only two to five buttons. If the number of segment button components exceeds the upper limit, the button information elements are not deleted or replaced.

#### \[h2\]create

static create(elements: SegmentButtonItemTuple): SegmentButtonItemOptionsArray

Creates a **SegmentButtonItemOptionsArray** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| elements | [SegmentButtonItemTuple](#segmentbuttonitemtuple) | Yes | Button information. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SegmentButtonItemOptionsArray](#segmentbuttonitemoptionsarray) | Created SegmentButtonItemOptionsArray object. |

#### TabSegmentButtonOptions

Provides configuration options for tab-style segmented buttons. Inherits from [TabSegmentButtonConstructionOptions](#tabsegmentbuttonconstructionoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | "tab" | No | No | Type of the segmented buttons, which is **"tab"** in this case. |

#### CapsuleSegmentButtonOptions

Provides configuration options for capsule-style segmented buttons. Inherits from [CapsuleSegmentButtonConstructionOptions](#capsulesegmentbuttonconstructionoptions).

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | "capsule" | No | No | Type of the segmented buttons, which is **"capsule"** in this case. |

#### SegmentButtonTextItem

Text button information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Button text.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| accessibilityLevel13+ | string | No | Yes | 

Accessibility level, which is used to set whether the current component can be recognized by accessibility services.

The options are as follows:

**"auto"**: The component can be recognized by accessibility services.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| accessibilityDescription13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility description, which is used to explain component operations to users. You can set detailed description text to help users understand the operation consequences. If a component has both text and accessibility description, the text is read first, and then the accessibility description is read.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |

#### SegmentButtonIconItem

Icon button information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Icon of the unselected item.

If the value is undefined, no icon is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| iconAccessibilityText13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the unselected item.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| selectedIcon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 

Icon of the selected item.

If the value is undefined, no icon is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedIconAccessibilityText13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the selected item.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| accessibilityLevel13+ | string | No | Yes | 

Accessibility level, which is used to set whether the current component can be recognized by accessibility services.

The options are as follows:

**"auto"**: The component can be recognized by accessibility services.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| accessibilityDescription13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility description. You can specify further explanation of the current component, for example, possible operation consequences, especially those that cannot be learned from component attributes and accessibility text. If a component contains both text information and the accessibility description, the text is read first and then the accessibility description, when the component is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/f6zfujxWT522xLwwrQUZ1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8823AC9036BC105C81EEA68CD58623630CBF50EBF9551897A2569C3BB2CBF736)

Both the **icon** and **selectedIcon** attributes must be set. Setting only one of them is invalid.

#### SegmentButtonIconTextItem

Icon and text button information.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Icon of the unselected item.

If the value is undefined, no icon is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| iconAccessibilityText13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the unselected item.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| selectedIcon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 

Icon of the selected item.

If the value is undefined, no icon is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedIconAccessibilityText13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the selected item.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 

Button text.

If the value is undefined, no text is displayed.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| accessibilityLevel13+ | string | No | Yes | 

Accessibility level, which is used to set whether the current component can be recognized by accessibility services.

The options are as follows:

**"auto"**: The component can be recognized by accessibility services.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| accessibilityDescription13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility description. You can specify further explanation of the current component, for example, possible operation consequences, especially those that cannot be learned from component attributes and accessibility text. If a component contains both text information and the accessibility description, the text is read first and then the accessibility description, when the component is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/RsNgbp4FRaqlmEIPfmyVXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F42947987F4622E6CF847F6B19BD89AB3964FF16CAF78E5E3C704010418FE4A)

Both the **icon** and **selectedIcon** attributes must be set. Setting only one of them is invalid.

#### SegmentButtonItemOptions

Button options in a segmented button.

**Decorator Type**: @Observed

#### \[h2\]Properties

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Icon of the unselected item.

Default value: The icon of the button in the unselected state is not displayed.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| iconAccessibilityText13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the unselected item.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| selectedIcon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon of the selected item.

Default value: no button icon in the selected state

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedIconAccessibilityText13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the selected item.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Button text.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| accessibilityLevel13+ | string | No | Yes | 

Accessibility level, which is used to set whether the current component can be recognized by accessibility services.

The options are as follows:

**"auto"**: The component can be recognized by accessibility services.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| accessibilityDescription13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility description. You can specify further explanation of the current component, for example, possible operation consequences, especially those that cannot be learned from component attributes and accessibility text. If a component contains both text information and the accessibility description, the text is read first and then the accessibility description, when the component is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |

#### \[h2\]constructor

constructor(options: SegmentButtonItemOptionsConstructorOptions)

Constructor.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SegmentButtonItemOptionsConstructorOptions](#segmentbuttonitemoptionsconstructoroptions) | Yes | Configuration options for a single segmented button, including the icon, text, and accessibility attributes. |

#### SegmentButtonItemOptionsConstructorOptions

Construct parameters for SegmentButtonItemOptions.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Device behavior differences**: On wearables, calling this API results in a runtime exception indicating that the API is undefined. On other devices, the API works correctly.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| icon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 
Icon of the unselected item.

Default value: The icon of the button in the unselected state is not displayed.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| iconAccessibilityText13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the unselected item.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| selectedIcon | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Icon of the selected item.

Default value: no button icon in the selected state

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| selectedIconAccessibilityText13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility text of the selected item.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| text | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Button text.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| accessibilityLevel13+ | string | No | Yes | 

Accessibility level, which is used to set whether the current component can be recognized by accessibility services.

The options are as follows:

**"auto"**: The component can be recognized by accessibility services.

**"yes"**: The component can be recognized by accessibility services.

**"no"**: The component cannot be recognized by accessibility services.

**"no-hide-descendants"**: Neither the component nor its child components can be recognized by accessibility services.

Default value: **"auto"**

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |
| accessibilityDescription13+ | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Accessibility description. You can specify further explanation of the current component, for example, possible operation consequences, especially those that cannot be learned from component attributes and accessibility text. If a component contains both text information and the accessibility description, the text is read first and then the accessibility description, when the component is selected.

The default value is an empty string.

If the value is **undefined**, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 13.

 |

#### Example

## Example 1: Setting the Type of the SegmentButton component

This example demonstrates how to create two different types of **SegmentButton** components by configuring **SegmentButtonOptions** with **tab** and **capsule** types.

import {
  ItemRestriction,
  SegmentButton,
  SegmentButtonItemTuple,
  SegmentButtonOptions,
  SegmentButtonTextItem
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: \[{ text: 'Tab 1' }, { text: 'Tab 2' }, {
      text: 'Tab 3'
    }\] as ItemRestriction<SegmentButtonTextItem>,
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[{ text: 'Single-selection 1' }, { text: 'Single-selection 2' }, { text: 'Single-selection 3' }\] as SegmentButtonItemTuple,
    multiply: false,
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[{ text: 'Multi-selection 1' }, { text: 'Multi-selection 2' }, { text: 'Multi-selection 3' }\] as SegmentButtonItemTuple,
    multiply: true
  });
  @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') }
    \] as SegmentButtonItemTuple,
    multiply: false,
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[
      { text: 'Icon 1', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 2', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 3', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 4', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 5', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') }
    \] as SegmentButtonItemTuple,
    multiply: true
  });
  @State tabSelectedIndexes: number\[\] = \[1\];
  @State singleSelectCapsuleSelectedIndexes: number\[\] = \[0\];
  @State multiplySelectCapsuleSelectedIndexes: number\[\] = \[0, 1\];
  @State singleSelectIconCapsuleSelectedIndexes: number\[\] = \[3\];
  @State multiplySelectIconTextCapsuleSelectedIndexes: number\[\] = \[1, 2\];

  build() {
    Row() {
      Column() {
        Column({ space: 25 }) {
          SegmentButton({
            options: this.tabOptions,
            selectedIndexes: $tabSelectedIndexes
          })
          SegmentButton({
            options: this.singleSelectCapsuleOptions,
            selectedIndexes: $singleSelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.multiplySelectCapsuleOptions,
            selectedIndexes: $multiplySelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconCapsuleOptions,
            selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconTextCapsuleOptions,
            selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
          })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/zoKjLHTFQQaJfGDjt4q82g/en-us_image_0000002568765711.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E96D8958778515E4EED989D0DB5E41427E6E25C847FA6780040A483F58C295BB)

## Example 2: Setting the Style of the SegmentButton component

This example demonstrates how to use **CommonSegmentButtonOptions** to customize the text and background style of the **SegmentButton** component.

import {
  ItemRestriction,
  SegmentButton,
  SegmentButtonItemTuple,
  SegmentButtonOptions,
  SegmentButtonTextItem
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: \[{ text: 'Tab 1' }, { text: 'Tab 2' }, {
      text: 'Tab 3'
    }\] as ItemRestriction<SegmentButtonTextItem>,
    backgroundColor: 'rgb(213,213,213)',
    selectedBackgroundColor: 'rgb(112,112,112)', // Configure CommonSegmentButtonOptions to implement the selected background color.
    textPadding: {
      top: 10,
      right: 10,
      bottom: 10,
      left: 10
    }, // Configure CommonSegmentButtonOptions to implement the text padding.
  });
  @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[{ text: 'Single-selection 1' }, { text: 'Single-selection 2' }, { text: 'Single-selection 3' }\] as SegmentButtonItemTuple,
    multiply: false,
    fontColor: 'rgb(0,74,175)', // Configure CommonSegmentButtonOptions to implement the text color.
    selectedFontColor: 'rgb(247,247,247)', // Configure CommonSegmentButtonOptions to implement the selected text color.
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK // Configure CommonSegmentButtonOptions to implement the background blur style.
  });
  @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[{ text: 'Multi-selection 1' }, { text: 'Multi-selection 2' }, { text: 'Multi-selection 3' }\] as SegmentButtonItemTuple,
    multiply: true,
    fontSize: 18,
    selectedFontSize: 18,
    fontWeight: FontWeight.Bolder, // Configure CommonSegmentButtonOptions to implement the text weight.
    selectedFontWeight: FontWeight.Lighter, // Configure CommonSegmentButtonOptions to implement the weight of the selected text.
  });
  @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') }
    \] as SegmentButtonItemTuple,
    multiply: false,
    imageSize: { width: 40, height: 40 },
    buttonPadding: {
      top: 6,
      right: 10,
      bottom: 6,
      left: 10
    },
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[
      { text: 'Icon 1', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 2', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 3', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 4', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 5', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') }
    \] as SegmentButtonItemTuple,
    multiply: true,
    imageSize: { width: 10, height: 10 },
  });
  @State tabSelectedIndexes: number\[\] = \[0\];
  @State singleSelectCapsuleSelectedIndexes: number\[\] = \[0\];
  @State multiplySelectCapsuleSelectedIndexes: number\[\] = \[0, 1\];
  @State singleSelectIconCapsuleSelectedIndexes: number\[\] = \[3\];
  @State multiplySelectIconTextCapsuleSelectedIndexes: number\[\] = \[1, 2\];

  build() {
    Row() {
      Column() {
        Column({ space: 20 }) {
          SegmentButton({ options: this.tabOptions, selectedIndexes: $tabSelectedIndexes })
          SegmentButton({
            options: this.singleSelectCapsuleOptions,
            selectedIndexes: $singleSelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.multiplySelectCapsuleOptions,
            selectedIndexes: $multiplySelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconCapsuleOptions,
            selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconTextCapsuleOptions,
            selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
          })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/GwRg9-gATDabbn6k_55HOw/en-us_image_0000002537765986.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75557E6E66F825285A10E92C002B99DE2BBE9540908D215CF2BDDA4073334334)

## Example 3: Performing Array Operations on the SegmentButton Component

This example shows how to perform operations such as adding and removing segmented buttons using array functions like **pop**, **shift**, and **unshift**.

import {
  SegmentButton,
  SegmentButtonOptions,
  SegmentButtonItemOptionsArray,
  SegmentButtonItemTuple,
  SegmentButtonItemOptions
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[{ text: '1' }, { text: '2' }, { text: '3' },
      { text: '4' }, { text: '5' }\] as SegmentButtonItemTuple,
    multiply: false,
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State capsuleSelectedIndexes: number\[\] = \[0\];

  build() {
    Row() {
      Column() {
        Column({ space: 10 }) {
          SegmentButton({
            options: this.singleSelectCapsuleOptions,
            selectedIndexes: $capsuleSelectedIndexes
          })
          Button('Delete First Item')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.shift()
            })
          Button('Delete Last Item')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.pop()
            })
          Button('Add to End')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.push({ text: 'push' })
            })
          Button('Add to Beginning')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.unshift(({ text: 'unshift' }))
            })
          Button('Replace Items 2 and 3 with splice1 and splice2')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons.splice(1, 2, new SegmentButtonItemOptions({
                text: 'splice1'
              }), new SegmentButtonItemOptions({ text: 'splice2' }))
            })
          Button('Change All Button Text')
            .onClick(() => {
              this.singleSelectCapsuleOptions.buttons =
                SegmentButtonItemOptionsArray.create(\[{ text: 'a' }, { text: 'b' },
                  { text: 'c' }, { text: 'd' }, { text: 'e' }\])
            })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/YEdxNyndSMKKfa6Su-b_0g/en-us_image_0000002537925926.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C2D531B5D6A28A5DBBFC21DBBA81F824E0FFDBBB09737283E892A73012FF864)

## Example 4: Implementing a Mirrored Layout

This example shows how to implement a mirrored layout for a **SegmentButton** component by configuring **direction**.

import { LengthMetrics, SegmentButton, SegmentButtonOptions } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: \[{ text: 'Tab 1' }, { text: 'Tab 2' }, {
      text: 'Tab 3'
    }\],
    direction: Direction.Rtl,
    backgroundColor: Color.Green,
    selectedBackgroundColor: Color.Orange,
    localizedTextPadding: {
      end: LengthMetrics.vp(10),
      start: LengthMetrics.vp(10)
    },
  });
  @State singleSelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[{ text: 'Single-selection 1' }, { text: 'Single-selection 2' }, { text: 'Single-selection 3' }\],
    multiply: false,
    direction: Direction.Rtl,
    fontColor: Color.Black,
    selectedFontColor: Color.Yellow,
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State multiplySelectCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[{ text: 'Multi-selection 1' }, { text: 'Multi-selection 2' }, { text: 'Multi-selection 3' }\],
    multiply: true,
    direction: Direction.Rtl,
    fontSize: 18,
    selectedFontSize: 18,
    fontWeight: FontWeight.Bolder,
    selectedFontWeight: FontWeight.Lighter,
  });
  @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') }
    \],
    multiply: false,
    direction: Direction.Rtl,
    imageSize: { width: 40, height: 40 },
    localizedButtonPadding: {
      end: LengthMetrics.vp(10),
      start: LengthMetrics.vp(10)
    },
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[
      { text: 'Icon 1', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 2', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 3', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 4', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') },
      { text: 'Icon 5', icon: $r('sys.media.ohos\_ic\_public\_email'), selectedIcon: $r('sys.media.ohos\_ic\_public\_clock') }
    \],
    multiply: true,
    direction: Direction.Rtl,
    imageSize: { width: 10, height: 10 },
  });
  @State tabSelectedIndexes: number\[\] = \[0\];
  @State singleSelectCapsuleSelectedIndexes: number\[\] = \[0\];
  @State multiplySelectCapsuleSelectedIndexes: number\[\] = \[0, 1\];
  @State singleSelectIconCapsuleSelectedIndexes: number\[\] = \[3\];
  @State multiplySelectIconTextCapsuleSelectedIndexes: number\[\] = \[1, 2\];

  build() {
    Row() {
      Column() {
        Column({ space: 20 }) {
          SegmentButton({ options: this.tabOptions, selectedIndexes: $tabSelectedIndexes })
          SegmentButton({
            options: this.singleSelectCapsuleOptions,
            selectedIndexes: $singleSelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.multiplySelectCapsuleOptions,
            selectedIndexes: $multiplySelectCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconCapsuleOptions,
            selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconTextCapsuleOptions,
            selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
          })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/mR5fdBbzR0W2_C1PXncH4w/en-us_image_0000002568685703.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8A697BC4ACD6E78B31E1711BB2EF1AAA9CC26FDE61A93096356597BE3260780)

## Example 5: Setting Accessibility

This example showcases how to implement accessibility features for the **SegmentButton** component by configuring attributes such as **accessibilityLevel** and **selectedIconAccessibilityText**.

import {
  ItemRestriction,
  SegmentButton,
  SegmentButtonItemTuple,
  SegmentButtonOptions,
  SegmentButtonTextItem,
  SegmentButtonItemOptions
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: \[{ text: 'Tab 1', accessibilityLevel: 'yes', accessibilityDescription: 'Tab 1 usage hints' },
      { text: 'Tab 2', accessibilityLevel: 'yes', accessibilityDescription: 'Tab 2 usage hints' },
      {
        text: 'Tab 3 ', accessibilityLevel: 'yes', accessibilityDescription: 'Tab 3 usage hints'
      }\] as ItemRestriction<SegmentButtonTextItem>,
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State iconCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[
      {
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        iconAccessibilityText: 'Unselected icon accessibility text',
        selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
        selectedIconAccessibilityText: 'Selected icon accessibility text',
        accessibilityLevel: 'yes',
        accessibilityDescription: 'SegmentButtonIconItem usage hints'
      },
      {
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        iconAccessibilityText: 'Unselected icon accessibility text',
        selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
        selectedIconAccessibilityText: 'Selected icon accessibility text',
        accessibilityLevel: 'yes',
        accessibilityDescription: 'SegmentButtonIconItem usage hints'
      },
      {
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        iconAccessibilityText: 'Unselected icon accessibility text',
        selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
        selectedIconAccessibilityText: 'Selected icon accessibility text',
        accessibilityLevel: 'yes',
        accessibilityDescription: 'SegmentButtonIconItem usage hints'
      },
      {
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        iconAccessibilityText: 'Unselected icon accessibility text',
        selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
        selectedIconAccessibilityText: 'Selected icon accessibility text',
        accessibilityLevel: 'yes',
        accessibilityDescription: 'SegmentButtonIconItem usage hints'
      }
    \] as SegmentButtonItemTuple,
    multiply: false,
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK
  });
  @State iconTextCapsuleOptions: SegmentButtonOptions = SegmentButtonOptions.capsule({
    buttons: \[
      {
        text: 'Icon 1',
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        iconAccessibilityText: 'Unselected icon accessibility text',
        selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
        selectedIconAccessibilityText: 'Selected icon accessibility text',
        accessibilityLevel: 'yes',
        accessibilityDescription: 'SegmentButtonIconTextItem usage hints'
      },
      {
        text: 'Icon 1',
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        iconAccessibilityText: 'Unselected icon accessibility text',
        selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
        selectedIconAccessibilityText: 'Selected icon accessibility text',
        accessibilityLevel: 'yes',
        accessibilityDescription: 'SegmentButtonIconTextItem usage hints'
      },
      {
        text: 'Icon 1',
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        iconAccessibilityText: 'Unselected icon accessibility text',
        selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
        selectedIconAccessibilityText: 'Selected icon accessibility text',
        accessibilityLevel: 'yes',
        accessibilityDescription: 'SegmentButtonIconTextItem usage hints'
      },
      {
        text: 'Icon 1',
        icon: $r('sys.media.ohos\_ic\_public\_email'),
        iconAccessibilityText: 'Unselected icon accessibility text',
        selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
        selectedIconAccessibilityText: 'Selected icon accessibility text',
        accessibilityLevel: 'yes',
        accessibilityDescription: 'SegmentButtonIconTextItem usage hints'
      }
    \] as SegmentButtonItemTuple,
    multiply: true
  });
  @State tabSelectedIndexes: number\[\] = \[1\];
  @State singleSelectIconCapsuleSelectedIndexes: number\[\] = \[3\];
  @State multiplySelectIconTextCapsuleSelectedIndexes: number\[\] = \[1, 2\];

  build() {
    Row() {
      Column() {
        Column({ space: 25 }) {
          SegmentButton({
            options: this.tabOptions,
            selectedIndexes: $tabSelectedIndexes
          })
          SegmentButton({
            options: this.iconCapsuleOptions,
            selectedIndexes: $singleSelectIconCapsuleSelectedIndexes
          })
          SegmentButton({
            options: this.iconTextCapsuleOptions,
            selectedIndexes: $multiplySelectIconTextCapsuleSelectedIndexes
          })
          Button('Replace Items 2 and 3 with splice1 and splice2')
            .onClick(() => {
              this.iconTextCapsuleOptions.buttons.splice(1, 2, new SegmentButtonItemOptions({
                text: 'splice1', accessibilityLevel: 'yes', accessibilityDescription: 'SegmentButtonItemOptions usage hints'
              }), new SegmentButtonItemOptions({
                text: 'splice2',
                icon: $r('sys.media.ohos\_ic\_public\_email'),
                iconAccessibilityText: 'Unselected icon accessibility text',
                selectedIcon: $r('sys.media.ohos\_ic\_public\_clock'),
                selectedIconAccessibilityText: 'Selected icon accessibility text',
                accessibilityLevel: 'yes',
                accessibilityDescription: 'SegmentButtonIconTextItem usage hints'
              }))
            })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}

## Example 6: Setting Custom Border Radius

This example demonstrates how to set a custom border radius for the **SegmentButton** component.

import {
  BorderRadiusMode,
  ItemRestriction,
  LengthMetrics,
  SegmentButton,
  SegmentButtonOptions,
  SegmentButtonTextItem
} from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State tabOptions: SegmentButtonOptions = SegmentButtonOptions.tab({
    buttons: \[{ text: 'Tab 1' }, { text: 'Tab 2' }, {
      text: 'Tab 3'
    }\] as ItemRestriction<SegmentButtonTextItem>,
    backgroundBlurStyle: BlurStyle.BACKGROUND\_THICK,
    borderRadiusMode: BorderRadiusMode.CUSTOM, // Customize the corner radius of the border.
    backgroundBorderRadius: LengthMetrics.vp(8),
    itemBorderRadius: LengthMetrics.vp(6)
  });
  @State tabSelectedIndexes: number\[\] = \[1\];

  build() {
    Row() {
      Column() {
        Column({ space: 25 }) {
          SegmentButton({
            options: this.tabOptions,
            selectedIndexes: $tabSelectedIndexes,
          })
        }.width('90%')
      }.width('100%')
    }.height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/Y8xICTGIR8uVhs2BFhowQg/en-us_image_0000002568765713.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062251Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86B855A45B2ACA6E069A7793AB2E317FDDF48F6799AD38BDA6500347533F2B51)
