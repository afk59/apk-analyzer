# How do I apply a linear gradient blur effect to images?

You can use the universal style attribute **linearGradientBlur** to apply a linear gradient blur effect. The code snippet is as follows:

@Entry
@Component
struct ImageExample1 {
  privateResource1: Resource = $r('app.media.icon');
  @State imageSrc: Resource = this.privateResource1;

  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Image(this.imageSrc)
            .linearGradientBlur(60, {
              fractionStops: \[\[0, 0\], \[0, 0.33\], \[1, 0.66\], \[1, 1\]\],
              direction: GradientDirection.Bottom
            })
        }
      }
    }
  }
}

**Reference**

[linearGradientBlur](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/ts-universal-attributes-image-effect#lineargradientblur12)
