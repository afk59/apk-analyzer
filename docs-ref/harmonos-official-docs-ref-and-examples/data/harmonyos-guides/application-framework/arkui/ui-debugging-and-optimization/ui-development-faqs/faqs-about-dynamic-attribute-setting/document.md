# FAQs About Dynamic Attribute Setting

This topic addresses common issues related to dynamic attribute setting.

#### JS Crash Occurs When AttributeModifier Is Used to Set Dynamic Attributes for a Component

**Symptom**

A [JS crash](../../../../../system/debugging-tools/performance-analysis-kit/fault-detection/crash-detection/js-crash-process-crash-detection/document.md) occurs after **AttributeModifier** is used to [set dynamic attributes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-attribute-modifier) for a component.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/dKUQeQALQxCkUca0gIwAJg/en-us_image_0000002568684703.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC997E09E226F23545BBAFD549773945104917C528473D1E78C78A3D87A7AB67)

**Solution**

Go to the error log as prompted, view the error cause, and rectify the fault. For details, see the code example below.

**Code Example**

In this example, a button is bound to **AttributeModifier** to demonstrate the scenario where an exception is thrown when an unsupported attribute is set. After the code is executed, a JS crash error is reported. In this example, deleting the code related to **reuseId** will allow the application to run normally.

// xxx.ets
// Set the custom AttributeModifier for the Button component attributes.
class MyButtonModifier implements AttributeModifier<ButtonAttribute> {

  applyNormalAttribute(instance: ButtonAttribute): void {
    instance.reuseId('String') // Deleting this line will allow the application to run normally.
    instance.backgroundColor(Color.Red)
  }
}

@Entry
@Component
struct attributeDemo {
  @State modifier: MyButtonModifier = new MyButtonModifier();

  build() {
    Row() {
      Column() {
        Button('Button')
          .attributeModifier(this.modifier)
      }
      .width('100%')
    }
    .height('100%')
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/f-4xHypnSjq6WflO0hBxqQ/en-us_image_0000002568764713.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061945Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8405E204A1256C5E15F7726102A5AAFA6D25906ADD76C6CCBD7F63EA0275A91)
