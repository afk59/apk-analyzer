# How do I implement a QR code with an image?

Stack an **Image** component on top of a **QRCode** component using a stack layout. You should adjust the image size to avoid affecting the recognition of the QR code. The sample code is as follows:

@Entry
@Component
struct QRCodeWithImage {
  private value: string = 'hello world';

  build() {
    Stack() {
      QRCode(this.value)
        .width(200)
        .height(200)
      Image($r('app.media.app\_icon'))
        .height(50)
        .width(50)
    }
    .height('100%')
    .width('100%')
  }
}
