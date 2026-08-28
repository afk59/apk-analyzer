# How do I keep the layout unchanged after the soft keyboard pops up?

You can achieve this purpose using the [expandSafeArea](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea) attribute. This attribute allows components to extend into the safe area, ensuring that the overall page layout remains unchanged. When **type** is set to **SafeAreaType.KEYBOARD**, it takes effect by default, meaning the component will not avoid the keyboard, and the layout remains stable even when the keyboard appears. The code snippet is as follows:

// xxx.ets
@Entry
@Component
struct TextInputExample {
  scroller: Scroller = new Scroller();
  @State text: string = '';

  build() {
    Scroll(this.scroller) {
      Column({ space: 20 }) {
        TextInput({ placeholder: 'Please enter the content.' })
          .expandSafeArea(\[SafeAreaType.KEYBOARD\])
          .type(InputType.Password)
          .margin({ top: 200 })
        TextInput({ placeholder: 'Please enter the content.' })
          .expandSafeArea(\[SafeAreaType.KEYBOARD\])
          .margin({ top: 200 })
        Text(\`UserName:${this.text}\`)
          .expandSafeArea(\[SafeAreaType.KEYBOARD\])
          .width('80%')
          .margin({ top: 200 })
        TextInput({ placeholder: 'Please enter a user name.', text: this.text })
          .expandSafeArea(\[SafeAreaType.KEYBOARD\])
          .margin({ top: 200 })
          .onChange((value: string) => {
            this.text = value;
          })
      }
      .width('100%')
    }
    .scrollBar(BarState.Off)
  }
}
