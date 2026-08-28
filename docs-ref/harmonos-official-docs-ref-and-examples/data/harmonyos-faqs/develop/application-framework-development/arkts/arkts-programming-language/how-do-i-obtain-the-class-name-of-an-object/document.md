# How do I obtain the class name of an object?

You can obtain the instance of a class, and then obtain the class name through the **name** property of the constructor.

Refer to the code snippet below.

class TestClass {
  a: string = 'A';
  b: string = 'B';
}

let testClassObj: TestClass = new TestClass();

@Entry
@Component
struct Index {
  build() {
    Row() {
      Column() {
        Button('get Class Name')
          .onClick(() => {
            console.log('TestClass Name:', testClassObj.constructor.name);
          })
      }
      .width('100%')
    }
    .height('100%')
  }
}
