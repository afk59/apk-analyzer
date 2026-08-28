# Polymorphic Style

You can set state-specific styles for components.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/fvm6aZbDSAaytK6C6191Nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DED4B7A43375A4E97DB524A7A3C48EEC7B9FA140A8B089EB50AD34FF304110B5)

-   The initial APIs of this module are supported since API version 8. Updates will be marked with a superscript to indicate their earliest API version.
    
-   Since API version 11, you can also dynamically set component attributes through [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md).
    
-   Polymorphic styles only support [universal attributes](../document.md). If a polymorphic style does not take effect, the attribute you are modifying might be a private attribute of the component, for example, **fontColor** or [backgroundColor](../basic-attributes/background/document.md#backgroundcolor18) of the [TextInput](../../text-and-input/textinput/document.md) component. In this case, you can use **attributeModifier** to dynamically set these component-specific attributes.
    
-   Currently, the implementation of polymorphic styles relies on the refresh mechanism of custom component nodes. Since the builder does not have an independent custom parent node and cannot directly trigger refresh, polymorphic styles cannot be applied directly within the builder. The recommended solution is to encapsulate the polymorphic styles into a custom component and place this component within the @Builder to indirectly achieve the polymorphic style effect. For details about the sample code, see [Example 3: Setting Polymorphic Styles for the Builder Component](#example-3-setting-polymorphic-styles-for-the-builder-component).
    
-   Polymorphic styles for the focused state are only applied when [focus activation](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-events-focus-event#basic-concepts) is enabled.
    

#### stateStyles

stateStyles(value: StateStyles): T

Sets the state-specific styles for the component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/unSiZGRMQSeejiXT8z9Y5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=645A51C90406D4B7A559F36600DBA3B486EDFC7EE20ABE400515811428EF4AA0)

This API cannot be called within [attributeModifier](../modifiers-and-custom-property/attribute-modifier/document.md#attributemodifier).

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | [StateStyles](#statestyles-1) | Yes | State-specific styles for the component. |

**Return value**

| Type | Description |
| :-- | :-- |
| T | Current component. |

#### StateStyles

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.ArkUI.ArkUI.Full

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| normal | any | No | Yes | 
Style of the component when being stateless.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| pressed | any | No | Yes | 

Style of the component in the pressed state.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| disabled | any | No | Yes | 

Style of the component in the disabled state.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| focused | any | No | Yes | 

Style of the component in the focused state.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| clicked | any | No | Yes | 

Style of the component in the clicked state.

**Widget capability**: This API can be used in ArkTS widgets since API version 9.

 |
| selected10+ | object | No | Yes | 

Style of the component in the selected state.

**Widget capability**: This API can be used in ArkTS widgets since API version 10.

 |

**Notes about the selected state:**

-   The selected state style depends on the value of the component's selected attribute. You can change the attribute value through a [click event](../../universal-events/interaction-response-events/click-event/document.md) or [$$](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-two-way-sync).
    
-   The table below lists the components that support the selected state style and their selected attributes or parameters.
    
    | Component | Selected Parameter/Attribute | Initial API Version |
    | :-- | :-- | :-- |
    | [Checkbox](../../buttons-and-selections/checkbox/document.md) | select | 10 |
    | [CheckboxGroup](../../buttons-and-selections/checkboxgroup/document.md) | selectAll | 10 |
    | [Radio](../../buttons-and-selections/radio/document.md) | checked | 10 |
    | [Toggle](../../buttons-and-selections/toggle/document.md) | isOn | 10 |
    | [ListItem](../../scroll-and-swipe/listitem/document.md) | selected | 10 |
    | [GridItem](../../scroll-and-swipe/griditem/document.md) | selected | 10 |
    | [MenuItem](../../menus/menuitem/document.md) | selected | 10 |
    

**Notes about pressed and clicked states**

-   When both **clicked** and **pressed** are used on the same component, only the last registered state takes effect.

#### Example

## Example 1: Setting Polymorphic Styles for the Text Component

This example demonstrates the style changes of the **Text** component when its state is pressed or disabled.

// xxx.ets
@Entry
@Component
struct StyleExample {
  @State isEnable: boolean = true

  @Styles
  pressedStyles(): void {
    .backgroundColor("#ED6F21")
    .borderRadius(10)
    .borderStyle(BorderStyle.Dashed)
    .borderWidth(2)
    .borderColor("#33000000")
    .width(120)
    .height(30)
    .opacity(1)
  }

  @Styles
  disabledStyles(): void {
    .backgroundColor("#E5E5E5")
    .borderRadius(10)
    .borderStyle(BorderStyle.Solid)
    .borderWidth(2)
    .borderColor("#2a4c1919")
    .width(90)
    .height(25)
    .opacity(1)
  }

  @Styles
  normalStyles(): void {
    .backgroundColor("#0A59F7")
    .borderRadius(10)
    .borderStyle(BorderStyle.Solid)
    .borderWidth(2)
    .borderColor("#33000000")
    .width(100)
    .height(25)
    .opacity(1)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Text("normal")
        .fontSize(14)
        .fontColor(Color.White)
        .opacity(0.5)
        // stateStyles sets the style of the component in its normal state.
        .stateStyles({
          normal: this.normalStyles,
        })
        .margin({ bottom: 20 })
        .textAlign(TextAlign.Center)
      Text("pressed")
        .backgroundColor("#0A59F7")
        .borderRadius(20)
        .borderStyle(BorderStyle.Dotted)
        .borderWidth(2)
        .borderColor(Color.Red)
        .width(100)
        .height(25)
        .opacity(1)
        .fontSize(14)
        .fontColor(Color.White)
        // stateStyles sets the style of the component in its pressed state.
        .stateStyles({
          pressed: this.pressedStyles,
        })
        .margin({ bottom: 20 })
        .textAlign(TextAlign.Center)
      Text(this.isEnable == true ? "effective" : "disabled")
        .backgroundColor("#0A59F7")
        .borderRadius(20)
        .borderStyle(BorderStyle.Solid)
        .borderWidth(2)
        .borderColor(Color.Gray)
        .width(100)
        .height(25)
        .opacity(1)
        .fontSize(14)
        .fontColor(Color.White)
        .enabled(this.isEnable)
        // stateStyles sets the style of the component in its disabled state.
        .stateStyles({
          disabled: this.disabledStyles,
        })
        .textAlign(TextAlign.Center)
      Text("control disabled")
        .onClick(() => {
          this.isEnable = !this.isEnable
          console.info(\`${this.isEnable}\`)
        })
    }
    .width(350).height(300)
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/M19zmMhERJ22JK54CIGRdw/en-us_image_0000002568685173.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=676BEEBBFBCC2686EE8EF4EB36B69CB7F8A2C94D27D312EB2F1E6B2AF94E610F)

## Example 2: Setting Polymorphic Styles for the Radio Component

This example demonstrates the style changes of the **Radio** component when its state is selected.

// xxx.ets
@Entry
@Component
struct Index {
  @State value: boolean = false
  @State value2: boolean = false

  @Styles
  normalStyles(): void{
    .backgroundColor("#E5E5E1")
  }

  @Styles
  selectStyles(): void{
    .backgroundColor("#ED6F21")
    .borderWidth(2)
  }

  build() {
    Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.Center, alignItems: ItemAlign.Center }) {
      Column() {
        Text('Radio1')
          .fontSize(25)
        Radio({ value: 'Radio1', group: 'radioGroup1' })
          .checked(this.value)
          .height(50)
          .width(50)
          .borderWidth(0)
          .borderRadius(30)
          .onClick(() => {
            this.value = !this.value
          })
          .stateStyles({
            normal: this.normalStyles,
            selected: this.selectStyles,
          })
      }
      .margin(30)

      Column() {
        Text('Radio2')
          .fontSize(25)
        Radio({ value: 'Radio2', group: 'radioGroup2' })
          .checked($$this.value2)
          .height(50)
          .width(50)
          .borderWidth(0)
          .borderRadius(30)
          .stateStyles({
            normal: this.normalStyles,
            selected: this.selectStyles,
          })
      }
      .margin(30)
    }.padding({ top: 30 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/asPQpghmRvW6EZUvcQYa1w/en-us_image_0000002568765183.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4B0CE8566D126D56EA0E8B3C620E8E0535F24935F93E732C510A6DE89AFCFBC)

## Example 3: Setting Polymorphic Styles for the Builder Component

This example demonstrates the style changes of the **Builder** component when it is in pressed state.

import { ComponentContent } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

@Component
struct Child {
  build() {
    Row()
      .zIndex(10)
      .width(200)
      .height(200)
      .stateStyles({
        normal: {
          .backgroundColor(Color.Blue)
        },
        pressed: {
          .backgroundColor(Color.Black)
        }
      })
  }
}

@Builder
function buildText() {
  Child()
}

@Entry
@Component
struct Index {
  private contentNode: ComponentContent<Object> =
    new ComponentContent(this.getUIContext(), wrapBuilder(buildText));

  build() {
    Column() {
      Button().margin({ top: 200 }).onClick((event: ClickEvent) => {
        this.getUIContext()
          .getPromptAction()
          .openCustomDialog(this.contentNode)
          .then(() => {
            console.info('OpenCustomDialog complete.')
          })
          .catch((error: BusinessError) => {
            let message = (error as BusinessError).message;
            let code = (error as BusinessError).code;
            console.error(\`OpenCustomDialog args error code is ${code}, message is ${message}\`);
          })
      })
    }
    .width('100%')
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f/v3/KirQCKLrTpeZLlzvF_6svw/en-us_image_0000002537765458.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062235Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=697A1217168FB866B99160D05D569BC1E28929802BE75ABAEEA0096CA4082E12)
