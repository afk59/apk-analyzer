# How do I control the fixed height of a sheet transition?

You can use the **options** parameter of **bindSheet()** to set a specific height for the sheet. The code snippet is as follows:

@Entry
@Component
struct SheetTransitionExample {
  @State isShow: boolean = false;
  @State sheetHeight: number = 300;

  @Builder
  myBuilder() {
    Column() {
      Button('change height')
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.sheetHeight = 500;
        })

      Button('Set Illegal height')
        .margin(10)
        .fontSize(20)
        .onClick(() => {
          this.sheetHeight = 0;
        })
    }
    .width('100%')
    .height('100%')
  }

  build() {
    Column() {
      Button('transition modal 1')
        .onClick(() => {
          this.isShow = true;
        })
        .fontSize(20)
        .margin(10)
        .bindSheet(this.isShow, this.myBuilder(), { height: this.sheetHeight, backgroundColor: Color.Green })
    }
    .justifyContent(FlexAlign.Center)
    .width('100%')
    .height('100%')
  }
}

**Reference**

[Sheet Transition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-sheet-transition)
