# How do I obtain object values by key?

ArkTS does not support field access through indexes. To use indexes, consider **Record<key, value>**. Refer to the code snippet below.

class Student {
  data: Record<string, string> = { 'name': 'aaa', 'age': 'bbb' };
}

@Entry
@Component
struct KeyObject {
  build() {
    Column() {
      Button('click')
        .onClick(() => {
          let student = new Student();
          console.info(\`${student.data\['name'\]}\`);
        })
    }
    .justifyContent(FlexAlign.Center)
    .alignItems(HorizontalAlign.Center)
    .width('100%')
    .height('100%')
  }
}
