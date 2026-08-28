# Does the Text component support setting font styles by segment?

Only one font style can be set for a single **Text** component. However, you can use multiple **Span** child components to display different styles within a single line of text. The code snippet is as follows:

@Entry
@Component
struct TestDemoPage {
  @State message: string = "Hello World";

  build() {
    Row() {
      Column() {
        Text() {
          // Using the Span subcomponent to implement segmented style settings
          Span('test text: ')
            .fontSize(20)
            .fontWeight(FontWeight.Bolder)
            .fontColor(Color.Black)
          Span(this.message)
            .fontSize(15)
            .fontColor(Color.Red)
        }
      }
      .width('100%')
    }
    .height('100%')
  }
}

**Reference**

[Text](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-basic-components-text)
