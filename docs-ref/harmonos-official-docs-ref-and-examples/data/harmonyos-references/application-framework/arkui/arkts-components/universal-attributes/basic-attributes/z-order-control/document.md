# Z-order Control

A component's z-order determines its stacking order relative to its sibling components within the same container.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/2eygqzdJSwa-WsPjymTfDw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E46BC0DEC926B37635890E3FC18F461627C9F44F15F0D29B95C9DDA12B68F6D)

The initial APIs of this module are supported since API version 7. Updates will be marked with a superscript to indicate their earliest API version.

#### zIndex

zIndex(value: number): T

Sets the stacking order of the component.

**Widget capability**: Since API version 9, this feature is supported in ArkTS widgets.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | number | Yes | Stacking order of the component relative to its sibling components in a container. The components with a larger **zIndex** value cover those with a smaller one. When dynamically changing zIndex does not involve adding or removing sibling nodes, the components are sorted stably based on their previous stack level. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

## Example 1: Setting the Component Stacking Order

This example demonstrates how to set the stacking order of components using **zIndex**.

// xxx.ets
@Entry
@Component
struct ZIndexExample {
  build() {
    Column() {
      Stack() {
        // Components in the Stack container overlap, with later-defined components are on top by default. Components with higher zIndex values appear in front of those with lower zIndex values.
        // Set the zIndex value of Text1 to 2.
        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)
        // Set the zIndex value of Text2 to 1.
        Text('2, default zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
        // Set the zIndex value of Text3 to 0.
        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}

Display of child components in the **Stack** container when **zIndex** is not set

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/qZnkwj8wS8WwD0wQTkZw1w/en-us_image_0000002537765396.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACE84A9D39CC81FD193CEA80AD0A90022E42FA5DF25BB1939D9A5F20C1C4E55F)

Display of child components in the **Stack** container when **zIndex** is set

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d2/v3/JSw8FpR3QIO84te5zuH8Vw/en-us_image_0000002537925336.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A7766B59250F276124DB7EECCC6E78585143C5F1F4758B78F5461A4ADC3835F)

## Example 2: Dynamically Modifying the zIndex Attribute

This example demonstrates dynamically modifying the **zIndex** attribute on a **Button** component.

// xxx.ets
@Entry
@Component
struct ZIndexExample {
  @State zIndex\_: number = 0

  build() {
    Column() {
      // Clicking the Button component changes the zIndex value. Components are sorted stably based on their previous stacking order.
      Button("change Text2 zIndex")
        .onClick(() => {
          this.zIndex\_ = (this.zIndex\_ + 1) % 3;
        })
      Stack() {
        // Set the zIndex value of Text1 to 1.
        Text('1, zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
        // Set the zIndex value of Text2 to the default value 0.
        Text('2, default zIndex(0), now zIndex:' + this.zIndex\_)
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(this.zIndex\_)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}

Effect without clicking the **Button** component to change **zIndex**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/xSroI5peQwq4laICwLNT8A/en-us_image_0000002568685113.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A29692D4AA36B9A45C9662140E886AA2DCF883CEB91A8C96CD797CE352839179)

Effect after clicking the **Button** component to dynamically change **zIndex** so that **Text1** and **Text2** have the same **zIndex** value

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/6otf70ieTouPdzq0Tpqz_Q/en-us_image_0000002568765123.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6032D20A50920C6E66F0CD253551E66DD136199C27698AD224513C63BEBDC227)

Effect after the **Button** component is clicked to dynamically change **zIndex** so that **Text2** has a higher **zIndex** value than **Text1**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/WTYlPjTiTlGe0abOV9lRhw/en-us_image_0000002537765398.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E6A9306616B0597FE719F02A389A8DA55324F730099CC7C6C5BE14AC82A409B)

## Example 3: Setting zIndex for Components in Different Containers

This example shows how to set **zIndex** for components in different containers. **Text1**, **Text2**, and **Text3** are placed in separate **Stack** containers. Although **Text3** has the smallest **zIndex** value, **Text1** and **Text2** cannot be displayed above **Text3**.

// xxx.ets
@Entry
@Component
struct ZIndexExample {
  build() {
    Stack() {
      Stack() {
        // Set the zIndex value of Text1 to 2.
        Text('1, zIndex(2)')
          .size({ width: '40%', height: '30%' }).backgroundColor(0xbbb2cb)
          .zIndex(2)
        // Set the zIndex value of Text2 to 1.
        Text('2, default zIndex(1)')
          .size({ width: '70%', height: '50%' }).backgroundColor(0xd2cab3).align(Alignment.TopStart)
          .zIndex(1)
      }.width('100%').height(200)

      Stack() {
        // zIndex cannot take effect across different container components. Text3 will be displayed on the top.
        // Set the zIndex value of Text3 to 0.
        Text('3, zIndex(0)')
          .size({ width: '90%', height: '80%' }).backgroundColor(0xc1cbac).align(Alignment.TopStart)
          .zIndex(0)
      }.width('100%').height(200)
    }.width('100%').height(200)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/-whTEVtyS3Kzpejnguw2aw/en-us_image_0000002537925338.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E75FE79AEA82EF8BCDCBC15143C02323FF9EC99E6CFB1ADF3D3DE7F6826BDF5)
