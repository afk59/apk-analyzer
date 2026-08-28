# SideBarContainer

The **SideBarContainer** component contains a sidebar and content area as its child components. The sidebar is the first child component and can be shown or hidden as needed. The content area is the second child component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/vxU02873TdeRwzrRFftAUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C76AF908891F12CC8455164A6D2FDD36EA3CF58838B77708914F0869B75BE56)

The APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Supported

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/kY9KG9ZCS8iNFOP5MLZRkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=187C79404AE9924325A944AA28A6E5A0AC4530DB934B33DF824A3F9D8E5932DB)

-   Allowed child component types: built-in and custom components, excluding rendering control types ([if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), and [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)).
-   This component must contain two child components.
-   If there are three or more child components, only the first and second child components are displayed. If there is only one child component, the sidebar is displayed, and the content area is blank.
-   The focus navigation is performed in the content area and then in the sidebar of the **SideBarContainer** component.

#### APIs

SideBarContainer( type?: SideBarContainerType )

Creates a sidebar container.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SideBarContainerType](#sidebarcontainertype) | No | 
Display type of the sidebar.

Default value: **SideBarContainerType.Embed**

 |

#### SideBarContainerType

Enumerates the types of sidebar containers.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Embed | 0 | 
The sidebar is embedded in the component and displayed side by side with the content area.

With the overall container size unchanged, displaying the sidebar reduces the content area, and hiding the sidebar expands the content area.

If the component size is less than the sum of [minContentWidth](#mincontentwidth10) and [minSideBarWidth](#minsidebarwidth), and **showSideBar** is not set, the sidebar is automatically hidden.

If **minSideBarWidth** or **minContentWidth** is not set, the default value will be used for calculation.

The user can bring out the sidebar in Overlay mode by clicking the control button.

 |
| Overlay | 1 | The sidebar is overlaid on top of the content area, without affecting the size of the content area. |
| AUTO10+ | 2 | 

The sidebar is displayed in Embed mode when the component size is greater than or equal to the sum of **minSideBarWidth** and **minContentWidth**

and in Overlay mode otherwise.

If **minSideBarWidth** or **minContentWidth** is not set, the default value will be used for calculation. If the calculation result is less than 600 vp, 600 vp will be used as the breakpoint value for mode switching.

 |

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

#### \[h2\]showSideBar

showSideBar(value: boolean)

Specifies whether to display the sidebar.

Since API version 10, this attribute supports two-way binding through [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display the sidebar.

**true**: The sidebar is displayed.

**false**: The sidebar is not displayed.

Default value: **true**

 |

#### \[h2\]controlButton

controlButton(value: ButtonStyle)

Sets the attributes of the sidebar control button.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ButtonStyle](#buttonstyle) | Yes | Attributes of the sidebar control button. |

#### \[h2\]showControlButton

showControlButton(value: boolean)

Specifies whether to display the sidebar control button.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to display the sidebar control button.

**true**: The sidebar control button is displayed.

**false**: The sidebar control button is not displayed.

Default value: **true**

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/KHfrhsEQSHm1Eu743PSeGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78F97353A48903C5CDC3011CC8029671ED81F037EAA33F0AB8F63EBD18963727)

The sidebar display or hiding animation is triggered when the sidebar is displayed or hidden by clicking the sidebar control button.

#### \[h2\]sideBarWidth

sideBarWidth(value: number)

Sets the width of the sidebar. If a value less than 0 is set, the default value is used. The value must comply with the width constraints. If it is not within the valid range, the valid value closest to the set one is used.

Since API version 18, this attribute supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Width of the sidebar.

Default value: **240vp**

Unit: vp

Value range: \[0, +∞).

**NOTE**

In API version 9 and earlier versions, the default value is **200vp**. In API version 10, the default value is **240vp**.

 |

#### \[h2\]sideBarWidth9+

sideBarWidth(value: Length)

Sets the width of the sidebar. If a value less than 0 is set, the default value is used. The value must comply with the width constraints. If it is not within the valid range, the valid value closest to the set one is used. Compared to [sideBarWidth](#sidebarwidth), this API supports percentage strings and other [pixel units](../../common-definitions/pixel-units/document.md) for the **value** parameter.

Since API version 18, this attribute supports two-way binding through [!!](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-new-binding).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Width of the sidebar.

Default value: **240vp**

Unit: vp

Value range: \[0, +∞).

**NOTE**

The default value is **200vp** in API version 9 and **240vp** in API version 10.

 |

#### \[h2\]minSideBarWidth

minSideBarWidth(value: number)

Sets the minimum width of the sidebar. If a value less than 0 is set, the default value is used. The value cannot exceed the width of the sidebar container. If the specified value exceeds the sidebar container width, the container width is used instead.

**minSideBarWidth**, whether it is specified or kept at the default value, takes precedence over **minWidth** of the sidebar child components.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Minimum width of the sidebar.

Default value: In API version 9 and earlier versions, the default value is **200vp**. In API version 10, the default value is **240vp**.

Value range: \[0, +∞).

 |

#### \[h2\]minSideBarWidth9+

minSideBarWidth(value: Length)

Sets the minimum width of the sidebar. If a value less than 0 is set, the default value is used. The value cannot exceed the width of the sidebar container. If the specified value exceeds the sidebar container width, the container width is used instead. Compared to [minSideBarWidth](#minsidebarwidth), this API supports percentage strings and other [pixel units](../../common-definitions/pixel-units/document.md) for the **value** parameter.

**minSideBarWidth**, whether it is specified or kept at the default value, takes precedence over **minWidth** of the sidebar child components.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Minimum width of the sidebar.

Default value: In API version 9 and earlier versions, the default value is **200vp**. In API version 10, the default value is **240vp**.

Value range: \[0, +∞).

 |

#### \[h2\]maxSideBarWidth

maxSideBarWidth(value: number)

Sets the maximum width of the sidebar. If a value less than 0 is set, the default value is used. The value cannot exceed the width of the sidebar container. If the specified value exceeds the sidebar container width, the container width is used instead.

**maxSideBarWidth**, whether it is specified or kept at the default value, takes precedence over **maxWidth** of the sidebar child components.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | 
Maximum width of the sidebar.

Default value: **280vp**

Unit: vp

Value range: \[0, +∞).

 |

#### \[h2\]maxSideBarWidth9+

maxSideBarWidth(value: Length)

Sets the maximum width of the sidebar. If a value less than 0 is set, the default value is used. The value cannot exceed the width of the sidebar container. If the specified value exceeds the sidebar container width, the container width is used instead. Compared with [maxSideBarWidth](#maxsidebarwidth), this API supports percentage strings and other [pixel units](../../common-definitions/pixel-units/document.md) for the **value** parameter.

**maxSideBarWidth**, whether it is specified or kept at the default value, takes precedence over **maxWidth** of the sidebar child components.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Length](../../common-definitions/basic-types/document.md#length) | Yes | 
Maximum width of the sidebar.

Default value: **280vp**

Unit: vp

Value range: \[0, +∞).

 |

#### \[h2\]autoHide9+

autoHide(value: boolean)

Specifies whether to automatically hide the sidebar when it is dragged to be smaller than the minimum width. The value is subject to the **minSideBarWidth** attribute method. If it is not set in **minSideBarWidth**, the default value is used.

Whether the sidebar should be hidden is determined when it is being dragged. When it is dragged to be smaller than the minimum width, the damping effect is required to trigger hiding (a distance out of range).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether to automatically hide the sidebar when it is dragged to be smaller than the minimum width.

**true**: The sidebar is automatically hidden.

**false**: The sidebar is not automatically hidden.

Default value: **true**

 |

#### \[h2\]sideBarPosition9+

sideBarPosition(value: SideBarPosition)

Sets the position of the sidebar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [SideBarPosition](#sidebarposition9) | Yes | 
Position of the sidebar.

Default value: **SideBarPosition.Start**

 |

#### \[h2\]divider10+

divider(value: DividerStyle | null)

Sets the divider style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [DividerStyle](#dividerstyle10) | null | Yes | 
Divider style.

\- **DividerStyle** (default): The divider is displayed.

\- **null** or **undefined**: No action is taken, and the divider style remains consistent with the default.

**NOTE**

In API version 11 and earlier versions, **null** results in the divider not being displayed.

 |

#### \[h2\]minContentWidth10+

minContentWidth(value: Dimension)

Sets the minimum content area width of the sidebar container.

If this attribute is set to a value less than 0, the default value **360vp** will be used. If this attribute is not set, the width of the content area can shrink to 0.

In Embed mode, when the component size is increased, only the content area is enlarged;

when the component size is decreased, the content area is shrunk until its width reaches the value defined by **minContentWidth**; if the component size is further decreased, while respecting the **minContentWidth** settings, the sidebar is shrunk

until its width reaches the value defined by **minSideBarWidth**; if the component size is further decreased, then:

-   If [autoHide](#autohide9) is set to **false**, while retaining the [minSideBarWidth](#minsidebarwidth) and **minContentWidth** settings, the content area has its content clipped.
-   If **autoHide** is set to **true**, the sidebar is hidden first, and then the content area is shrunk. After its width reaches the value defined by **minContentWidth**, the content area has its content clipped.

**minContentWidth** takes precedence over the [maxSideBarWidth](#maxsidebarwidth) and **sideBarWidth** attributes of the sidebar. If **minContentWidth** is not set, **minSideBarWidth** and **maxSideBarWidth** take precedence over its default value.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | Yes | 
Minimum content area width of the sidebar container.

Default value: **360vp**

Unit: vp

 |

#### ButtonStyle

Describes the style of the sidebar control button.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | Yes | 
Spacing between the sidebar control button and the left of the container.

Default value: **16vp**

Unit: vp

Value range: \[0, +∞).

 |
| top | number | No | Yes | 

Spacing between the sidebar control button and the top of the container.

Default value: **48vp**

Unit: vp

Value range: \[0, +∞).

 |
| width | number | No | Yes | 

Width of the sidebar control button.

Default value:

API version 9 and earlier versions: **32vp**

API version 10 and later versions: **24vp**

Unit: vp

Value range: \[0, +∞).

 |
| height | number | No | Yes | 

Height of the sidebar control button.

Default value:

API version 9 and earlier versions: **32vp**

API version 10 and later versions: **24vp**

Unit: vp

Value range: \[0, +∞).

 |
| icons | [ButtonIconOptions18+](#buttoniconoptions18) | No | Yes | 

Icons of the sidebar control button.

If the resource fails to be obtained or this attribute is not set, the default icon is used.

 |

#### ButtonIconOptions18+

Describes the icons of the sidebar control button.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/c7bC6ypQRaqh0gkLcnbuUg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FEFD90085657E3E624A9B2E07C1AAB2884B02873C6F31D9C5073EC5B4DFDD46C)

To standardize anonymous object definitions, the element definitions here have been revised in API version 18. While historical version information is preserved for anonymous objects, there may be cases where the outer element's @since version number is higher than inner elements'. This does not affect interface usability.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| shown8+ | string | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 
Icon of the control button when the sidebar is displayed.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| hidden8+ | string | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../common-definitions/basic-types/document.md#resource) | No | No | 

Icon of the control button when the sidebar is hidden.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| switching8+ | string | [PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | [Resource](../../common-definitions/basic-types/document.md#resource) | No | Yes | 

Icon of the control button when the sidebar is switching between the shown and hidden states.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |

#### SideBarPosition9+

Enumerates the positions of the sidebar.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| Start | 0 | The sidebar is on the left side of the container. |
| End | 1 | The sidebar is on the right side of the container. |

#### DividerStyle10+

Sets the divider style.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| strokeWidth | [Length](../../common-definitions/basic-types/document.md#length) | No | No | 
Stroke width of the divider.

Default value: **1vp**

Unit: vp

Value range: \[0, +∞).

**NOTE**

Percentage values are not supported. The priority of this attribute is lower than that of the universal attribute [height](../../universal-attributes/layout-and-borders/sizing/document.md#height). If the value of this attribute is greater than that of **height**, cropping is performed based on the **height** settings. Due to hardware limitations on some devices where 1 px dividers may not display properly after rounding, you are advised to use the **2px** value.

 |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the divider.

Default value: **#000000, 3%**

 |
| startMargin | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Distance between the divider and the top of the sidebar.

Default value: **0**

Unit: vp

Value range: \[0, +∞).

 |
| endMargin | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Distance between the divider and the bottom of the sidebar.

Default value: **0**

Unit: vp

Value range: \[0, +∞).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/nKqDeN5ZQXCBbKue8JN0dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D7AE2D75C564E4F6421FDE1B15E996C71095BB30A49F923B636C3CD8925F871)

The settings of the [universal size attributes](../../universal-attributes/layout-and-borders/sizing/document.md) **width** and **height** do not take effect for the sidebar child component.

The settings do not take effect for the sidebar content area either. By default, the sidebar content area takes up the remaining space of the sidebar container.

If the [showSideBar](#showsidebar) attribute is not set, the sidebar's visibility is subject to its size.

-   If the size is less than the sum of [minSideBarWidth](#minsidebarwidth) and [minContentWidth](#mincontentwidth10), the sidebar is not displayed by default.
-   If the size is greater than or equal to the sum of **minSideBarWidth** and **minContentWidth**, the sidebar is displayed by default.

#### Events

In addition to the [universal events](../../universal-events/document.md), the following events are supported.

#### \[h2\]onChange

onChange(callback: (value: boolean) => void)

Triggered when the status of the sidebar switches between shown and hidden.

This event is triggered when any of the following conditions is met:

1.  The value of the **showSideBar** attribute changes.
2.  The adaptation of the **showSideBar** attribute changes.
3.  [autoHide](#autohide9) is triggered upon divider dragging.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | **true**: The sidebar is shown. **false**: The sidebar is hidden. |

#### Example

This example demonstrates how to use the **SideBarContainer** component and implement the page layout.

// xxx.ets
@Entry
@Component
struct SideBarContainerExample {
  // Replace $r("app.media.icon") with the image resource file you use.
  normalIcon: Resource = $r("app.media.icon");
  selectedIcon: Resource = $r("app.media.icon");
  @State arr: number\[\] = \[1, 2, 3\];
  @State current: number = 1;

  build() {
    SideBarContainer(SideBarContainerType.Embed) {
      Column() {
        ForEach(this.arr, (item: number) => {
          Column({ space: 5 }) {
            Image(this.current === item ? this.selectedIcon : this.normalIcon).width(64).height(64)
            Text("Index0" + item)
              .fontSize(25)
              .fontColor(this.current === item ? '#0A59F7' : '#999')
              .fontFamily('source-sans-pro,cursive,sans-serif')
          }
          .onClick(() => {
            this.current = item;
          })
        }, (item: string) => item)
      }.width('100%')
      .justifyContent(FlexAlign.SpaceEvenly)
      .backgroundColor('#19000000')

      Column() {
        Text('SideBarContainer content text1').fontSize(25)
        Text('SideBarContainer content text2').fontSize(25)
      }
      .margin({ top: 50, left: 20, right: 30 })
    }
    .controlButton({
      icons: {
        // Replace $r('app.media.drawer') with the image resource file you use.
        hidden: $r('app.media.drawer'),
        shown: $r('app.media.drawer'),
        switching: $r('app.media.drawer')
      }
    })
    .sideBarWidth(150)
    .minSideBarWidth(50)
    .maxSideBarWidth(300)
    .minContentWidth(0)
    .onChange((value: boolean) => {
      console.info('status:' + value);
    })
    .divider({ strokeWidth: '1vp', color: Color.Gray, startMargin: '4vp', endMargin: '4vp' })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/ceqgiFotQfe5Kb2mEiRM7A/en-us_image_0000002568685227.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59790E8ABC6C0C46F8BC4E9DEAD01D5FD26C8DD2B65169D9E404EB25CAC9CB52)
