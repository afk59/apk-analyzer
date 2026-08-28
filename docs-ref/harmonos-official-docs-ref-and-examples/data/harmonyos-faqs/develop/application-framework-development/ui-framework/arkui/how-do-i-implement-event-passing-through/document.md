# How do I implement event passing through?

**Question**

There are two sibling components, Component A and Component B, in a **Stack** container, with Component A being covered by Component B. When users click Component B, how can the click event be passed through to Component A to trigger Component A's **onClick** callback without triggering Component B's **onClick** callback?

**Answer**

Set the **hitTestBehavior** attribute of Component B to **HitTestMode.None**. The sample code is as follows:

@Entry
@Component
struct StackExample {
  build() {
    Stack({ alignContent: Alignment.Bottom }) {
      Text('A')
        .width('90%')
        .height('100%')
        .backgroundColor(0xd2cab3)
        .align(Alignment.Top)
        .onClick(() => {
          console.log('TextA click')
        })
      Text('B')
        .width('70%')
        .height('60%')
        .backgroundColor(0xc1cbac)
        .align(Alignment.Top)
        .hitTestBehavior(HitTestMode.None)
        .onClick(() => {
          console.log('TextB click')
        })
    }
    .width('100%')
    .height(150)
    .margin({ top: 5 })
  }
}

**Reference**

[Hit Test Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-hit-test-behavior)
