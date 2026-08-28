# How do I use a custom decorator in ArkTS?

ArkTS supports the TS decorator syntax earlier than TS5.0 (such as TS4.x and earlier versions). For details about the definition and runtime behavior of the decorators, see the [TS official documents](https://www.typescriptlang.org/docs/handbook/decorators.html).

If a decorator is defined in an .ets file, it must comply with the [TypeScript to ArkTS Cookbook](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/typescript-to-arkts-migration-guide). For example, it cannot use **any**.

Refer to the code snippet below.

function MyDescriptor(target: Object, key: string, descriptor: PropertyDescriptor) {
  const originalMethod: Function = descriptor.value
  descriptor.value = (...args: Object\[\]) => {
    // Get the name, input parameters, and return value of the decorated method
    console.log(\`Calling ${target.constructor?.name} method ${key} with argument: ${args}\`)
    const result: Object = originalMethod(...args)
    console.log(\`Method ${key} returned: ${result}\`)
    return result
  }
  return descriptor
}

@Entry
@Component
export struct MyDescriptorCom {
  @State message: string = 'Hello World';

  @MyDescriptor
  demoFunc(str: string) {
    return str
  }

  aboutToAppear(): void {
    this.demoFunc('DemoTest')
  }

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

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/wLbb_6ZPTzmZ4Iv7h7Yxgg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062541Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAD906B802F612461CDD546C1EC5217C32BB0359D9A73D13A32DD4462E32081F)

Due to the ArkTS runtime limitations, multiple custom decorators cannot be used at the same time.
