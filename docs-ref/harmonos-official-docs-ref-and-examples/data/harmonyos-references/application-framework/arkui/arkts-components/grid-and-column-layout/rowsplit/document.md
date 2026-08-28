# RowSplit

The **RowSplit** component lays out child components horizontally and inserts a vertical divider between every two child components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c1/v3/BVYxn4RRQRyp7Gi2U6IlTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8711496A24DED4162C61F7C8C89396275BA0CA0D9295258E59523DB80F2383A5)

This component is supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### Child Components

Supported

This component limits the width of its child components through dividers. During initialization, the divider positions are calculated based on the width of its child components. After initialization, dynamic width modifications to child components do not affect divider positions. To adjust child component widths, drag the adjacent dividers.

After initialization, dynamic changes to the [margin](../../universal-attributes/layout-and-borders/sizing/document.md#margin), [border](../../universal-attributes/layout-and-borders/border-styling/document.md#border), or [padding](../../universal-attributes/layout-and-borders/sizing/document.md#padding) attributes may cause the width of the child components to exceed the allowable distance between adjacent dividers. In such cases, dividers cannot be dragged to adjust the width of the child components.

#### APIs

RowSplit()

Creates a horizontal split layout container with dividers between child components.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

#### Attributes

In addition to the [universal attributes](../../universal-attributes/document.md), the following attributes are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/61/v3/aFoeAi6WTVmizdi1p4dUiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE4E0392D9C12326906F5C4DBC85A6F5DCBCB2D621C71347BF926644A98E043F)

The default value of [shape clipping](../../universal-attributes/visual-effects/shape-clipping/document.md) of the **RowSplit** component is **true**.

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/6jmnYoa2RjqcHttBqKZXEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=853A48DE3CA34EE6E7B0BCF557FC0995845C49190D69A420E48769AAF7EA39D7)

The divider of **RowSplit** can change the width of the left and right child components, but only to the extent that the resultant width falls within the maximum and minimum widths of the child components.

#### Events

The [universal events](../../universal-events/document.md) are supported.

#### Example

This example demonstrates the basic usage of **RowSplit**, which allows you to create draggable, horizontally laid-out child components.

// xxx.ets
@Entry
@Component
struct RowSplitExample {
  build() {
    Column() {
      Text('The second line can be dragged').fontSize(9).fontColor(0xCCCCCC).width('90%')
      RowSplit() {
        Text('1').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('2').width('10%').height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('3').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
        Text('4').width('10%').height(100).backgroundColor(0xD2B48C).textAlign(TextAlign.Center)
        Text('5').width('10%').height(100).backgroundColor(0xF5DEB3).textAlign(TextAlign.Center)
      }
      .resizeable(true) // Draggable.
      .width('90%').height(100)
    }.width('100%').margin({ top: 5 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/EmW_GAGxSGKIFm_6IGlWfQ/en-us_image_0000002537925450.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062238Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=317D0E23399BE1AE421BE2BF18B1C69A0BFC10FB47D0509A7DBE7A04B8FFB530)
