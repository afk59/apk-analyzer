# How do I set a gradient background color for the Button component?

To set a gradient background color for a **Button** component, you must ensure that the default background color of the component is set to transparent. The code snippet is as follows:

@Entry
@Component
struct Index {
  build() {
    Button('test')
      .width(200)
      .height(50)
      .backgroundColor('#00000000')
      .linearGradient({
        angle: 90,
        colors: \[\[0xff0000, 0.0\], \[0x0000ff, 0.3\], \[0xffff00, 1.0\]\]
      })
  }
}

**Reference**

[Button](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button)
