# How do I set click events for different positions in a custom span?

Custom spans are the smallest unit of components. When possible, set click events for separate custom spans, instead of for different positions within a single span. If implementation within a single span is required, you can determine the actual click position from **ClickEvent** in the click event callback and then provide differentiated responses based on the properties. The sample code snippet is as follows:

@Entry
@Component
struct Index {
  controller: RichEditorController = new RichEditorController();
  option: RichEditorOptions = { controller: this.controller };

  @Builder
  comment() {
    Row() {
      Text() {
        Span('123123123')
        ImageSpan($r('app.media.startIcon')).width(20).height(20)
        Span('ggggggggggggggggggggggxxxxxxxxxxxxxxxxxxxxxxx')
      }
      .maxLines(1)
      .wordBreak(WordBreak.BREAK\_ALL)
      .textOverflow({ overflow: TextOverflow.Ellipsis })
      .constraintSize({
        maxWidth: '90%'
      })

      Image($r('app.media.startIcon'))
        .width(25)
        .height(25)
        .onClick(() => {
          this.getUIContext().getPromptAction().showToast({
            message: 'Click to delete'
          })
        })
    }
    .width('100%')
    .align(Alignment.Center)
    .padding({
      top: 5,
      bottom: 5
    })
    .borderRadius(20)
    .backgroundColor(Color.Gray)
  }

  build() {
    Column() {
      Column() {
        RichEditor(this.option)
          .onReady(() => {
            this.controller.addBuilderSpan(() => this.comment())
          })
          .borderWidth(1)
          .borderColor(Color.Green)
          .width('100%')
          .height('30%')
      }
      .borderWidth(1)
      .borderColor(Color.Red)
      .width('100%')
      .height('70%')
    }
  }
}
