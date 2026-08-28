# How do I use iconfont?

To use iconfont, you need to obtain the corresponding TTF file of the font library first, and then register it through the **font.registerFont** API. After that, you can use the corresponding Unicode characters for icons on the **Text** component. The code snippet is as follows:

import { Font } from '@kit.ArkUI'
@Entry
@Component
struct UseIconFont {
  // Assuming 0000 is the Unicode for the specified icon, developers actually need to obtain Unicode from the ttf file of the registered iconFont
  @State unicode: string = '\\u0000';
  aboutToAppear(): void {
    let font: Font = this.getUIContext().getFont();
    font.registerFont({
      familyName: 'iconfont',
      familySrc: 'xxx.ttf'
    })
  }
  build() {
    Row() {
      Column() {
        Text(this.unicode)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
          .fontFamily('iconfont')
      }
      .width('100%')
    }
    .height('100%')
  }
}

**Reference**

[registerFont](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-font#registerfont)
