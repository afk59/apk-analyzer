# How do I set the image resolution?

You can use the [sourceSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-image#sourcesize) attribute to set the image resolution. In the sample code below, the image resolution is scaled from 1280 x 960 to 40 x 40.

@Entry
@Component
struct Index {
  build() {
    Column() {
      Row({ space: 50 }) {
        Image($r('app.media.example'))
          .sourceSize({
            width: 40,
            height: 40
          })
          .objectFit(ImageFit.ScaleDown)
          .aspectRatio(1)
          .width('25%')
          .border({ width: 1 })
          .overlay('width:40 height:40', { align: Alignment.Bottom, offset: { x: 0, y: 40 } })
      }
    }
  }
}
