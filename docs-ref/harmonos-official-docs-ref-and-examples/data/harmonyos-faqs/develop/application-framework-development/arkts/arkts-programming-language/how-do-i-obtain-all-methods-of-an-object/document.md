# How do I obtain all methods of an object?

You can use **Object.getOwnPropertyNames** to obtain the string arrays of all methods. To obtain the prototype of an object, the file must be a .ts file. Refer to the code snippet below.

1\. Define the class file **testClass.ts** for the methods to be obtained.

export class testClass {
  public test(): string {
    return "ArkUI Web Component";
  }

  public toString(): void {
    console.log('Web Component toString');
  }

  public FunToString(): void {
    console.log('Web Component toString');
  }
}

2\. Obtain the methods in the file.

import { testClass } from '../utils/testClass';

let protoType = testClass.prototype;
let methodsName: string\[\] = Object.getOwnPropertyNames(protoType);
console.info(methodsName.toString());

@Entry
@Component
struct GetObjectAllFun {
  @State message: string = 'Hello World';

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize(50)
          .fontWeight(FontWeight.Bold)
      }
      .width('100%')
    }
    .height('100%')
  }
}
