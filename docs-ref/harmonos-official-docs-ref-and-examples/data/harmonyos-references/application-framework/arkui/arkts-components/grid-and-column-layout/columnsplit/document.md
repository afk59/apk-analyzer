# ColumnSplit

The **ColumnSplit** component lays out child components vertically and inserts a horizontal divider between every two child components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/MkWA7IdRSzKRtwoJ8XH9Eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=330F3DA24D6AC83FDCC483077C0941518CA2C96F89E5AEC5FFAAB9B8AB8A4063)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Supported

This component limits the height of its child components through dividers. During initialization, the divider positions are calculated based on the height of its child components. After initialization, dynamic height modifications to child components do not affect divider positions. To adjust child component heights, drag the adjacent dividers.

After initialization, dynamic changes to the [margin](../../universal-attributes/layout-and-borders/sizing/document.md#margin), [border](../../universal-attributes/layout-and-borders/border-styling/document.md#border), or [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding) attributes may cause the size of the child components to exceed the allowable distance between adjacent dividers. In such cases, dividers cannot be dragged to adjust the height of the child components.

#### APIs

ColumnSplit()

Creates a vertical split layout container with dividers between child components.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/tJLcuPwDSPGMDVvdRp0oXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF8256B6972CFC211097936D0BC565471FF69FB5A94527201FCF8B48E5C711FA)

The default value of [shape clipping](../../universal-attributes/visual-effects/shape-clipping/document.md) of the **ColumnSplit** component is **true**.

#### \[h2\]resizeable

resizeable(value: boolean)

Sets whether the divider can be dragged.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the divider can be dragged. **true**: The divider can be dragged. **false**: The divider cannot be dragged.

Default value: **false**

Invalid values are treated as the default value.

 |

#### \[h2\]divider10+

divider(value: ColumnSplitDividerStyle | null)

Margin of the divider.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ColumnSplitDividerStyle](#columnsplitdividerstyle10) | null | Yes | 
Margin of the divider, that is, the distance between the divider and the child component.

Default value: **null**. When this parameter is set to null, the distance between the divider and the child component is 0 vp.

Invalid values are treated as the default value.

 |

#### ColumnSplitDividerStyle10+

Sets the distance between the child component and the upper and lower dividers.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| startMargin | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 
Distance between the child component and the upper divider.

Default value: **0**

Invalid values are treated as the default value. In this case, the attribute value obtained by the [getInspectorByKey()](../../universal-attributes/basic-attributes/component-id/document.md#getinspectorbykey9) API is **undefined**.

 |
| endMargin | [Dimension](../../common-definitions/basic-types/document.md#dimension10) | No | Yes | 

Distance between the child component and the lower divider.

Default value: **0**

Invalid values are treated as the default value. In this case, the attribute value obtained by the [getInspectorByKey()](../../universal-attributes/basic-attributes/component-id/document.md#getinspectorbykey9) API is **undefined**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/vY_16XxOQmySvBHD2FUBXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=15C0660E2BE784B3D9045CE668ACFD3C6BB50793054968993DAC543F1D0BBAA3)

Similar to [RowSplit](../rowsplit/document.md), the dividers of **ColumnSplit** adjust the height of adjacent child components. However, this adjustment is only applied to the extent that the resulting height stays within the height limits of the child components.

Universal attributes such as [clip](../../universal-attributes/visual-effects/shape-clipping/document.md#clip12) and [margin](../../universal-attributes/layout-and-borders/sizing/document.md#margin) are supported. If **clip** is not set, the default value **true** is used.

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

## Example 1: Setting the Resizable ColumnSplit Component

This example shows how to set the resizable **ColumnSplit** component and its effect.

// xxx.ets
@Entry
@Component
struct ColumnSplitExample {
  build() {
    Column(){
      Text('The dividing line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
      ColumnSplit() {
        Text('1').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('2').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('3').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('4').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('5').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
      }
      .borderWidth(1)
      .resizeable(true) // The divider can be dragged.
      .width('90%').height('60%')
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/VT7wACNETnWWW4Oblavpfg/en-us_image_0000002568765235.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E82376DF138B7D6BD501B5472516640CD0A1C2EA89ED97A005EF2153A6FCADAA)

## Example 2: Setting the ColumnSplit Component with Spacing

This example shows how to set the **ColumnSplit** component with spacing and its effect.

// xxx.ets
@Entry
@Component
struct ColumnSplitDividerExample {
  build() {
    Column() {
      Text('The dividing line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
      ColumnSplit() {
        Text('1').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('2').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('3').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('4').width('100%').height(50).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('5').width('100%').height(50).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
      }
      .borderWidth(1)
      .divider({ startMargin: 5, endMargin: 5 }) // Set the spacing.
      .width('90%')
      .height('60%')
    }.width('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/_udg7q_NQuOK7nyKMsqf7Q/en-us_image_0000002537765510.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BA987E3001C4CFFF66A81FC82E20331BAA923F4094F607CBFFA5455A811A32C)
