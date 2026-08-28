# Click Feedback Effect

You can set the click feedback effect for a component to define its visual response when it is clicked.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/otK6VzNnRmmNNsjjzeQwpg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7A43000169F48E300F6E474E73F966DA73546C83F2703C86CC4DA35FF5193536)

The initial APIs of this module are supported since API version 10. Updates will be marked with a superscript to indicate their earliest API version.

#### clickEffect

clickEffect(value: ClickEffect | null): T

Sets the click feedback effect of the component.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [ClickEffect](#clickeffect) | null | Yes | 
Click feedback effect of the component.

**NOTE**

Use **null** to disable the click feedback effect.

Avoid using this feature in scenarios where the component size dynamically changes.

This attribute is not supported when the component cannot trigger universal events.

After the click feedback effect triggers scaling, the touch point may fall outside the control, making the component unresponsive to gesture events.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### clickEffect18+

clickEffect(effect: Optional<ClickEffect | null>): T

Sets the click feedback effect of the component. Compared with [clickEffect](#clickeffect), this API supports the **undefined** type.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| effect | [Optional](../../modifiers-and-custom-property/custom-property/document.md#optionalt)<[ClickEffect](#clickeffect) | null> | Yes | 
Click feedback effect of the component.

**NOTE**

Use **undefined** or **null** to disable the click feedback effect.

Avoid using this feature in scenarios where the component size dynamically changes.

This attribute is not supported when the component cannot trigger universal events.

After the click feedback effect triggers scaling, the touch point may fall outside the control, making the component unresponsive to gesture events.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### ClickEffect

Defines the click effect.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| level | [ClickEffectLevel](../../../common-definitions/enums/document.md#clickeffectlevel10) | No | No | 
Click feedback effect of the component.

Default value: **ClickEffectLevel.LIGHT**

**NOTE**

When **level** is **undefined** or **null**, **ClickEffect** uses the effect corresponding to **ClickEffectLevel.LIGHT** with a scaling ratio as described below.

 |
| scale | number | No | Yes | 

Custom scaling ratio for fine-tuning the click feedback effect.

**NOTE**

The default value varies depending on the value of **level**:

**ClickEffectLevel.LIGHT**: **0.90**

**ClickEffectLevel.MIDDLE** or **ClickEffectLevel.HEAVY**: **0.95**

**undefined** or **null** (treated as **ClickEffectLevel.LIGHT**): **0.90**

When **scale** is set to **undefined** or **null**, the default scaling ratio for the current **level** is used.

 |

#### Example

This example demonstrates the click feedback effects on different types of components.

// xxx.ets
@Entry
@Component
struct ToggleExample {
  build() {
    Column({ space: 10 }) {
      Text('type: Switch').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Switch, isOn: false })
          .clickEffect({ level: ClickEffectLevel.LIGHT })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Switch, isOn: true })
          .clickEffect({ level: ClickEffectLevel.LIGHT, scale: 0.5 })
          .selectedColor('#007DFF')
          .switchPointColor('#FFFFFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Checkbox').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Checkbox, isOn: false })
          .clickEffect({ level: ClickEffectLevel.MIDDLE })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })

        Toggle({ type: ToggleType.Checkbox, isOn: true })
          .clickEffect({ level: ClickEffectLevel.MIDDLE, scale: 0.5 })
          .size({ width: 20, height: 20 })
          .selectedColor('#007DFF')
          .onChange((isOn: boolean) => {
            console.info('Component status:' + isOn);
          })
      }

      Text('type: Button').fontSize(12).fontColor(0xcccccc).width('90%')
      Flex({ justifyContent: FlexAlign.SpaceEvenly, alignItems: ItemAlign.Center }) {
        Toggle({ type: ToggleType.Button, isOn: false }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .clickEffect({ level: ClickEffectLevel.HEAVY })
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })

        Toggle({ type: ToggleType.Button, isOn: true }) {
          Text('status button').fontColor('#182431').fontSize(12)
        }.width(106)
        .clickEffect({ level: ClickEffectLevel.HEAVY, scale: 0.5 })
        .selectedColor('rgba(0,125,255,0.20)')
        .onChange((isOn: boolean) => {
          console.info('Component status:' + isOn);
        })
      }
    }.width('100%').padding(24)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/bR2nLL6cQimfTaq8mk5tpQ/en-us_image_0000002537925376.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3411997FB50D8DB2406CD9A9713D8CBF45D26CC32DE31784B018EC520F3DA611)
