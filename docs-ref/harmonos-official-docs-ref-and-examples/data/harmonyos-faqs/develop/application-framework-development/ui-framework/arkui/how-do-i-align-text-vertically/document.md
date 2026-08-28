# How do I align text vertically?

You can set the width of the **Text** component to be the same as the font size to achieve the purpose. The code snippet is as follows:

@Entry
@Component
struct Index {
  private message: string = 'This document is suitable for beginners in application development. By building a simple application with page jump/return function, quickly understand the main files of the project directory and familiarize yourself with the application development process.';
  build() {
    Column() {
      Text(this.message)
        .fontSize(13)
        .width(13)
    }
  }
}
