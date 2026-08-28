# How do I set state-specific styles for a component?

You can use the **stateStyles** attribute to set styles of a component for different states (stateless, pressed, disabled, focused, or clicked). The code snippet is as follows:

@Component
struct PolymorphicStyle {
  @Styles
  pressedStyles() {
    .backgroundColor('#ED6F21')
    .borderRadius(10)
    .borderStyle(BorderStyle.Dashed)
    .borderWidth(2)
    .borderColor('#33000000')
    .width(120)
    .height(30)
    .opacity(1)
  }

  build() {
    Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center }) {
      Text('pressed')
        .backgroundColor('#0A59F7')
        .borderRadius(20)
        .borderStyle(BorderStyle.Dotted)
        .borderWidth(2)
        .borderColor(Color.Red)
        .width(100)
        .height(25)
        .opacity(1)
        .fontSize(14)
        .fontColor(Color.White)
        .stateStyles({
          pressed: this.pressedStyles
        })
        .margin({ bottom: 20 })
        .textAlign(TextAlign.Center)
    }
    .width(350)
    .height(300)
  }
}

**Reference**

[Polymorphic Style](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-polymorphic-style)
