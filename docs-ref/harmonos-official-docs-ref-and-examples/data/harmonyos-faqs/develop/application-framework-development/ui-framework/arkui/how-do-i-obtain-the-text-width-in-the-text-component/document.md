# How do I obtain the text width in the Text component?

Use the **measureText()** method in the **@ohos.measure** module to measure the width of the given single-line text. The code snippet is as follows:

@Entry
@Component
struct IndexTest {
  @State textWidth: number = this.getUIContext().getMeasureUtils().measureText({
    textContent: "Hello World",
    fontSize: '50px'
  })

  build() {
    Row() {
      Column() {
        Text(\`The width of 'Hello World': ${this.textWidth}\`)
      }
      .width('100%')
    }
    .height('100%')
  }
}

**Reference**

[@ohos.measure (Text Measurement)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-measure)
