# How do I enable the background to change with the text size?

You can enable the component to automatically adjust its width based on the length of the text. The code snippet is as follows:

@Entry
@Component
struct Index {
  @State message: string = 'Hello World';

  build() {
    Column() {
      Row() {
        Text(this.message)
      }
      .backgroundImage($r('app.media.startIcon'))
      .backgroundImageSize({
        width: '100%',
        height: '100%'
      })
      .height(100)
      .border({
        width: 3,
        color: Color.Pink
      })

      TextInput()
        .onChange((value: string) => {
          this.message = value;
        })
    }
  }
}
