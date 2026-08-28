# Color Inversion

You can specify whether to enable the color inversion feature for a component. This feature automatically inverts or modifies color values during color mode (dark/light) transitions. You can disable the color inversion algorithm to maintain original color behavior during color mode transitions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/fq-CLjG-TPallboNUvQtYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E7470BB9406A35D7C2279F6F38C99534A56F6474E992474D94E1075B56E2CEC)

The initial APIs of this module are supported since API version 21. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### allowForceDark

allowForceDark(value: boolean): T

Sets whether to enable color inversion for the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/zNie9KJ2RXygVpgtxaR88w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F22D2A1F2E17E9606A8D63B257E99BF4C448780D5B6E26C10F4829C6B33D824)

When a component has color inversion disabled, both the component and all its child components will ignore color inversion capabilities, regardless of the settings on parent or ancestor components.

**Atomic service API**: This API can be used in atomic services since API version 21.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | Whether to enable color inversion. **true** to enable, **false** otherwise. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### Example

// Components with allowForceDark(false) will ignore color inversion capabilities.
@Entry
@Component
struct ComponentPage {
  build() {
    Column() {
      Column() {
        Text("Hello World")
          .fontSize(20)
          .fontColor(Color.Blue)
          .onClick(() => {
            console.info(\`Text is clicked\`);
          })
      }
      .allowForceDark(false) // Disable color inversion for Column and its child Text component, ignoring the color inversion settings of the parent component Column.

      Row() {
        Button('BUTTON')
          .backgroundColor(Color.Grey)
          .allowForceDark(true)
          .onClick(() => {
            console.info(\`Button is clicked\`);
          })
      }
      .allowForceDark(false) // Disable color inversion for Row and its child Button component, ignoring the color inversion settings of the parent component Column.
    }
    .allowForceDark(true)
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/1zHLzmo3Q5y5bTIIz-It4Q/en-us_image_0000002568765125.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062233Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD47FC1EC91EC876523C348E9D5006C80971E03A5167738248AC8CF1BF386703)
