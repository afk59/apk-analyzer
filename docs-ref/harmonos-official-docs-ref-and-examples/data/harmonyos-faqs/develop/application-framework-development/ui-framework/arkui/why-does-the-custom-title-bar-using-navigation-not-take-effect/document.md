# Why does the custom title bar using Navigation not take effect?

**Symptom**

When using Navigation to customize the title bar layout, the **title** method is invalid.

**Solution**

The method passed into **builder** in NavigationCustomTitle needs to use the @LocalBuilder decorator. Due to the internal scope of the object, you need to use @LocalBuilder to ensure that **this** always points to the custom component itself. The @LocalBuilder decorator is used to ensure that the **builder** method is correctly bound to the **this** context in the **Navigation** component to avoid scope loss. The sample code is as follows:

@Entry
@Component
export struct MainPage {
  myTitle: NavigationCustomTitle = {
    builder: this.customTitleBuilder,
    height: TitleHeight.MainOnly
  };

  @LocalBuilder
  customTitleBuilder() {
    Row() {
      Text('Title1')
        .fontSize(12)
        .fontWeight(FontWeight.Bold)
        .margin({ left: 7, right: 7, top: 7 })

      Text('Title2')
        .fontSize(12)
        .fontWeight(FontWeight.Bold)
        .margin({ left: 7, right: 7, top: 7 })

      Text('Title3')
        .fontSize(12)
        .fontWeight(FontWeight.Bold)
        .margin({ left: 7, right: 7, top: 7 })
    }
  }

  build() {
    Navigation() {
      Column() {
        Text('hello world')
          .fontSize('24')
          .fontWeight(FontWeight.Bold)
          .fontFamily('HarmonyHeiTi-Bold')
          .textAlign(TextAlign.Center)
          .width('100%')
      }
      .height('100%')
      .width('100%')
      .background('#F1F3F5')
    }
    .title(this.myTitle)
  }
}
