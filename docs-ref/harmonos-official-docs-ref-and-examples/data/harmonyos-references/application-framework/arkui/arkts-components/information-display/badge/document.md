# Badge

The **Badge** component is a container that can be attached to another component for notification and reminder purposes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/dKVu_xzbQHGDjP4ToJA2kw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BDA72364E38CDD685F7648C8FE4974C327811F5E8966A1E8448F409DD2D63D24)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

This component supports only one child component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/DDSdGvKmQeahzrHxE4z1oQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=986C46855A14BFA1C6006DEF6CA891653ACC576B9E5D5F6F9C2399B904F3AA71)

-   Allowed child component types: built-in and custom components, including rendering control types ([if/else](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-ifelse), [ForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-foreach), and [LazyForEach](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-rendering-control-lazyforeach)).
    
-   A custom component defaults to a width and height of 0. You must explicitly set its width and height; otherwise, the **Badge** component will not be displayed.
    
-   When there are multiple child components, only the last child component is displayed on the UI. However, the status update of other child components will still cause the badge and its child components to be re-rendered.
    
-   Child component layout is independent and does not automatically adjust to avoid overlapping with the badge.
    

#### APIs

#### \[h2\]Badge

Badge(value: BadgeParamWithNumber)

Creates a badge with the given numerical value.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BadgeParamWithNumber](#badgeparamwithnumber) | Yes | Options of the numeric badge. |

#### \[h2\]Badge

Badge(value: BadgeParamWithString)

Creates a badge with the given string.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

This component supports the scaling effect for visibility transition since API version 12.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [BadgeParamWithString](#badgeparamwithstring) | Yes | Options of the string-type badge. |

#### BadgeParam

Provides basic parameters for creating a badge.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| position | [BadgePosition](#badgeposition)|[Position10+](../../common-definitions/basic-types/document.md#position) | No | Yes | 
Position to display the badge relative to the parent component.

Default value: **BadgePosition.RightTop**

**NOTE**

With the **Position** type, percentage values are not supported. If an invalid value is set, the default value **(0,0)**, which indicates the upper left corner of the component, will be used.

With the **BadgePosition** type, the position is mirrored based on the [Direction](../../common-definitions/enums/document.md#direction) property.

 |
| style | [BadgeStyle](#badgestyle) | No | No | Style of the badge, including the font color, font size, badge color, and badge size. |

#### BadgeParamWithNumber

Inherits from [BadgeParam](#badgeparam) and has all attributes of **BadgeParam**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| count | number | No | No | 
Number of notifications.

**NOTE**

If the value is less than or equal to 0 and less than the value of **maxCount**, no badge is displayed.

Value range: \[-2147483648, 2147483647\]. If the value is out of the range, 4294967296 is added or subtracted so that the value is within the range. If the value is not an integer, it is rounded off to the nearest integer. For example, 5.5 is rounded off to 5.

 |
| maxCount | number | No | Yes | 

Maximum number of messages. If the number of messages exceeds the maximum, only **maxCount+** is displayed. For example, if **maxCount** is 99, **99+** is displayed.

Default value: **99**

Value range: \[-2147483648, 2147483647\]. If the value is out of the range, 4294967296 is added or subtracted so that the value is within the range. If the value is not an integer, it is rounded off to the nearest integer. For example, 5.5 is rounded off to 5.

 |

#### BadgeParamWithString

Inherits from [BadgeParam](#badgeparam) and has all attributes of **BadgeParam**.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | No | 
Text string of the badge content.

**NOTE**

The ResourceStr type is supported since API version 20.

 |

#### BadgePosition

Enumerates the display positions of a badge.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Value | Description |
| :-- | :-- | :-- |
| RightTop | \- | The badge is displayed in the upper right corner of the parent component. |
| Right | \- | The badge is vertically centered on the right of the parent component. |
| Left | \- | The badge is vertically centered on the left of the parent component. |

#### BadgeStyle

Describes the badge style. It includes the font color, font size, badge color, and badge size.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| color | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 
Font color.

Default value: **Color.White**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fontSize | number | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Font size. The value of this parameter is a string of the number type. The unit can be px, vp, fp, or lpx, for example, 10 or 10fp. If no unit is specified, fp is used by default.

Default value: **10vp**

The value must be greater than 0. If the value is **0**, the text is not displayed. If the value is less than 0, the default value is used.

**NOTE**

Percentage values are not supported. If a percentage value is set, the default value is used. The ResourceStr type is supported since API version 20.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| badgeSize | number | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Badge size. For the string type, numeric string values with optional units, for example, **"16"** or **"16fp"**, are supported.

Default value: **16**

Unit: vp

The value must be greater than 0. If the value is **0**, the badge is not displayed. If the value is less than 0, the default value is used.

**NOTE**

Percentage values are not supported. If a percentage value is set, the default value is used. The ResourceStr type is supported since API version 20.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| badgeColor | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Badge color.

Default value: **Color.Red**

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| fontWeight10+ | number |[FontWeight](../../common-definitions/enums/document.md#fontweight) | [ResourceStr](../../common-definitions/basic-types/document.md#resourcestr) | No | Yes | 

Font weight of the text. For the number type, the value ranges from 100 to 900, at an interval of 100. A larger value indicates a bolder font. For the number type, if the value is not within the range, the default value **400** is used. For the string type, only strings that represent a number, for example, **400**, and the following enumerated values of **FontWeight** are supported: **bold**, **bolder**, **lighter**, **regular**, and **medium**.

Default value: **FontWeight.Normal**

**NOTE**

Percentage values are not supported. If a percentage value is set, the default value is used. The ResourceStr type is supported since API version 20.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| borderColor10+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the background border.

Default value: **Color.Red**

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| borderWidth10+ | [Length](../../common-definitions/basic-types/document.md#length) | No | Yes | 

Width of the background border.

Default value: **1**

Unit: vp

**NOTE**

Percentage values are not supported. If a percentage value is set, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| outerBorderColor22+ | [ResourceColor](../../common-definitions/basic-types/document.md#resourcecolor) | No | Yes | 

Color of the background outer border.

Default value: **Color.White**

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| outerBorderWidth22+ | [LengthMetrics](../../../arkts-api/ui/arkui/graphics/document.md#lengthmetrics12) | No | Yes | 

Width of the background outer border.

Default value: **0**.

Unit: vp

Percentage values are not supported. If a percentage value is set, the default value is used.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |
| enableAutoAvoidance22+ | boolean | No | Yes | 

Whether to enable avoidance when the badge text is extended.

The value **true** means to enable avoidance, and **false** means the opposite.

Default value: **true**.

**NOTE**

1\. The avoidance effect is that the badge text is extended to the inside of the component.

2\. When the width of the outer border is greater than 0, the extension start point of the badge is the inner side of the outer border.

3\. When position is set to a specific coordinate value, the badge does not perform avoidance.

**Atomic service API**: This API can be used in atomic services since API version 22.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/2M8LExknQ82Lwkh3KGCt0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E6BF5514AF55636D667093B977584D101BCCC09A813AF64D8FF48AEC49C65DE)

When **borderWidth** is set to a value greater than 0 and **borderColor** is different from **badgeColor**, the badge is drawn before the border. Edge pixels are anti-aliased, which produces semi-transparent pixels. This causes the border in **badgeColor** to become visible at the four corners. To implement related scenarios, it is recommended that you use the [Text](../../text-and-input/text/document.md) component with its [outline](../../universal-attributes/visual-effects/outline-styling/document.md) attribute instead of the **Badge** component.

#### Attributes

The [universal attributes](../../universal-attributes/document.md) are supported.

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Setting the Badge Content

This example uses the **value** parameter of [BadgeParamWithNumber](#badgeparamwithnumber) and the **count** parameter of [BadgeParamWithString](#badgeparamwithstring) to display different effects when the **Badge** component receives an empty value, a character, or a number.

// xxx.ets
@Entry
@Component
struct BadgeExample {
  @Builder
  tabBuilder(index: number) {
    Column() {
      if (index === 2) {
        Badge({
          value: '',
          style: { badgeSize: 6, badgeColor: '#FA2A2D' }
        }) {
          Image('/common/public\_icon\_off.svg')
            .width(24)
            .height(24)
        }
        .width(24)
        .height(24)
        .margin({ bottom: 4 })
      } else {
        Image('/common/public\_icon\_off.svg')
          .width(24)
          .height(24)
          .margin({ bottom: 4 })
      }
      Text('Tab')
        .fontColor('#182431')
        .fontSize(10)
        .fontWeight(500)
        .lineHeight(14)
    }.width('100%').height('100%').justifyContent(FlexAlign.Center)
  }

  @Builder
  itemBuilder(value: string) {
    Row() {
      Image('common/public\_icon.svg').width(32).height(32).opacity(0.6)
      Text(value)
        .width(177)
        .height(21)
        .margin({ left: 15, right: 76 })
        .textAlign(TextAlign.Start)
        .fontColor('#182431')
        .fontWeight(500)
        .fontSize(16)
        .opacity(0.9)
      Image('common/public\_icon\_arrow\_right.svg').width(12).height(24).opacity(0.6)
    }.width('100%').padding({ left: 12, right: 12 }).height(56)
  }

  build() {
    Column() {
      // Badge of the red dot type
      Text('dotsBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
      Tabs() {
        TabContent()
          .tabBar(this.tabBuilder(0))
        TabContent()
          .tabBar(this.tabBuilder(1))
        TabContent()
          .tabBar(this.tabBuilder(2))
        TabContent()
          .tabBar(this.tabBuilder(3))
      }
      .width(360)
      .height(56)
      .backgroundColor('#F1F3F5')

      // Create a badge with the given string.
      Column() {
        Text('stringBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
        List({ space: 12 }) {
          ListItem() {
            Text('list1').fontSize(14).fontColor('#182431').margin({ left: 12 })
          }
          .width('100%')
          .height(56)
          .backgroundColor('#FFFFFF')
          .borderRadius(24)
          .align(Alignment.Start)

          ListItem() {
            Badge({
              value: 'New',
              position: BadgePosition.Right,
              style: { badgeSize: 16, badgeColor: '#FA2A2D' }
            }) {
              Text('list2').width(27).height(19).fontSize(14).fontColor('#182431')
            }.width(49.5).height(19)
            .margin({ left: 12 })
          }
          .width('100%')
          .height(56)
          .backgroundColor('#FFFFFF')
          .borderRadius(24)
          .align(Alignment.Start)
        }.width(336)

        // Create a badge with the given numerical value.
        Text('numberBadge').fontSize(18).fontColor('#182431').fontWeight(500).margin(24)
        List() {
          ListItem() {
            this.itemBuilder('list1')
          }

          ListItem() {
            Row() {
              Image('common/public\_icon.svg').width(32).height(32).opacity(0.6)
              Badge({
                count: 1,
                position: BadgePosition.Right,
                style: { badgeSize: 16, badgeColor: '#FA2A2D' }
              }) {
                Text('list2')
                  .width(177)
                  .height(21)
                  .textAlign(TextAlign.Start)
                  .fontColor('#182431')
                  .fontWeight(500)
                  .fontSize(16)
                  .opacity(0.9)
              }.width(240).height(21).margin({ left: 15, right: 11 })

              Image('common/public\_icon\_arrow\_right.svg').width(12).height(24).opacity(0.6)
            }.width('100%').padding({ left: 12, right: 12 }).height(56)
          }

          ListItem() {
            this.itemBuilder('list3')
          }

          ListItem() {
            this.itemBuilder('list4')
          }
        }
        .width(336)
        .height(232)
        .backgroundColor('#FFFFFF')
        .borderRadius(24)
        .padding({ top: 4, bottom: 4 })
        .divider({
          strokeWidth: 0.5,
          color: 'rgba(0,0,0,0.1)',
          startMargin: 60,
          endMargin: 12
        })
      }.width('100%').backgroundColor('#F1F3F5').padding({ bottom: 12 })
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/uImJCrqXSNKgSx5g35vicQ/en-us_image_0000002537925716.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AC39E87CE1D3E867C99282E3652910773B135512874747E9B9B4BFF0EEDC1F5)

## Example 2: Controlling the Badge Visibility with Numbers

This example shows how to use the **count** property to toggle the visibility of the **Badge** component. Specifically, when the **count** property is set to **0**, the badge is hidden; when it is set to **1**, the badge becomes visible.

// This example implements scaling when the badge visibility changes.
@Entry
@Component
struct Index {
  @State badgeCount: number = 1;

  build() {
    Column({ space: 40 }) {
      Badge({
        count: this.badgeCount,
        style: {},
        position: BadgePosition.RightTop,
      }) {
        Image($r('app.media.startIcon'))
          .width(50)
          .height(50)
      }
      .width(55)

      Button('count 0').onClick(() => {
        this.badgeCount = 0;
      })
      Button('count 1').onClick(() => {
        this.badgeCount = 1;
      })
    }
    .margin({ top: 20 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/_EhERjeqQkWNcZx7l3gK5w/en-us_image_0000002568685493.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE80533CE621725A09737E7EF5223A763FC5B1EB27279D3D18FC398CDEA0AFC4)

## Example 3: Setting the Outer Border and Text Extension Mode

Since API version 22, this example uses the **outerBorderColor** and **outerBorderWidth** attributes to set the outer border, and uses the **enableAutoAvoidance** attribute to set whether to avoid the badge text extension.

// This example implements the custom outer border and text extension direction of the Badge component.
import { LengthMetrics } from '@kit.ArkUI';

@Entry
@Component
struct Index {
  @State badgeValue: string = '1234';
  @State textAvoid:boolean\[\] = \[false, true\];
  @State textAvoidIndex: number = 0;
  @State textAvoidString: string \[\] = \["false", "true"\];
  build() {
    Column() {
      Badge({
        value: this.badgeValue,
        style: {
          badgeSize : 30,
          fontSize:20,
          outerBorderColor : Color.Pink,
          outerBorderWidth : LengthMetrics.vp(5),
          enableAutoAvoidance : this.textAvoid\[this.textAvoidIndex\]
        },
        position:BadgePosition.RightTop
      }) {
        // Replace $r('app.media.startIcon') with the image resource file you use.
        Image($r("app.media.startIcon"))
          .width(80)
          .height(80)
      }
      .direction(Direction.Ltr)
      .margin({ top: 20, bottom: 20 })
      Button("enableAutoAvoidance : " + this.textAvoidString\[this.textAvoidIndex\])
        .onClick(() => {
          this.textAvoidIndex = (this.textAvoidIndex + 1) % this.textAvoidString.length;
        })
    }
    .width('100%')
    .height('80%')
    .alignItems(HorizontalAlign.Center)
    .justifyContent(FlexAlign.Center)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9d/v3/My9e9alNS8eFCZzgJu3LtA/en-us_image_0000002568765503.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062244Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFE34136DC59CD51CC2DEBE3001F89E70B51E926CD71466CFF877A2681B1C281)
