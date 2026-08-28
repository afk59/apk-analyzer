# Click Control

Click control attributes are used to set whether a component can respond to finger interactions such as click and touch events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/TwexgDE7QEWPrHX1Qbk2vQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FA643335E4315055BA239968962A68E1F59430AECBFFA68B7E6D94C63A6A180)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### touchable(deprecated)

touchable(value: boolean): T

Whether the component can respond to finger interactions such as click and touch events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/6v-fIG57QuSUOEX8SmBLAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D22482610F94217E28C75B43ED8D161A09D8FB7E56F50E03DF904867A9957CDA)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [hitTestBehavior](../../universal-attributes/interaction-properties/touch-interactions/hit-test-control/document.md#hittestbehavior) instead.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | 
Whether the component can respond to finger interactions such as click and touch events.

**true** (default): The component can respond to finger interactions. **false**: The component cannot respond to finger interactions.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

// xxx.ets
@Entry
@Component
struct TouchAbleExample {
  @State text1: string = ''
  @State text2: string = ''

  build() {
    Stack() {
      Rect()
        .fill(Color.Gray).width(150).height(150)
        .onClick(() => {
          console.info(this.text1 = 'Rect Clicked')
        })
        .overlay(this.text1, { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
      Ellipse()
        .fill(Color.Pink).width(150).height(80)
        .touchable(false) // When the Ellipse area is touched, the message "Ellipse Clicked" is not displayed.
        .onClick(() => {
          console.info(this.text2 = 'Ellipse Clicked')
        })
        .overlay(this.text2, { align: Alignment.Bottom, offset: { x: 0, y: 20 } })
    }.margin(100)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/T9tqszQTTzKMFyxP5QXqTg/en-us_image_0000002568685745.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062253Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A03EF6E70C0A257F13604441D9EC38A81CAE351D84F64AEC81C36673806A07D6)
