# Does $r support nested resource access?

Currently, $r does not support nesting. The second parameter needs to be assigned the corresponding string value of the application resource obtained through **ResourceManager**. The sample code is as follows:

@Entry
@Component
struct Page16 {
  context = this.getUIContext();

  build() {
    Row() {
      Column() {
        Text($r('app.string.EntryAbility1\_label2',
          this.context.getHostContext()!.resourceManager.getStringSync($r('app.string.EntryAbility\_label'))))// path: resources\\base\\element\\string.json
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}

**Reference**

[ResourceManager](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#resourcemanager)
