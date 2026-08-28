# How do I set the dialog animation and mask animation separately?

**Symptom**

The dialog box and mask are combined. When a top-down animation is added to the dialog box, the mask also performs the same animation.

**Solution**

You can add the **.transition** attribute to the custom component in the dialog box to set its appearance mode. Before the component disappears, set the component to the hide status to trigger the **.transition** animation before closing the dialog box.

import { ComponentContent } from '@kit.ArkUI';

export interface SimpleDialogParams {
  title: string
  desc: string
  visible?: Visibility
}

@Builder
function SimpleDialogBuilder(params: SimpleDialogParams) {
  SimpleDialogUI({ params })
}

@Component
struct SimpleDialogUI {
  @Prop params: SimpleDialogParams | null = null;
  @State yOffset: number | string = '100%';
  @Prop visible: Visibility = Visibility.Visible;

  build() {
    Column() {
      Text(this.params?.title)
        .fontSize(18)
        .fontWeight(FontWeight.Bold)
        .textAlign(TextAlign.Center)
        .fontColor(Color.Black)
        .margin({ bottom: 16 })
        .width('100%')
      Text(this.params?.desc)
        .fontSize(14)
        .lineHeight(22)
        .fontColor(Color.Gray)
        .margin({ bottom: 16 })
        .width('100%')
    }
    .borderRadius({ topLeft: 16, topRight: 16 })
    .backgroundColor(Color.White)
    .width('100%')
    .alignItems(HorizontalAlign.Start)
    .visibility(this.params?.visible)
    .padding(20)
    .transition(TransitionEffect.translate({ y: '100%' }).animation({ duration: 200 }))
  }
}

@Entry
@Component
struct SetDialogAnimationAndMaskAnimationSeparately {
  @State message: string = 'Hello World';

  build() {
    RelativeContainer() {
      Text(this.message)
        .id('HelloWorld')
        .fontSize($r('app.float.page\_text\_font\_size'))
        .fontWeight(FontWeight.Bold)
        .alignRules({
          center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
          middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
        })
        .onClick(() => {
          const param =
            { title: 'Title title title', desc: 'Description description description description description description description description description description description description' } as SimpleDialogParams;
          const contentNode = new ComponentContent(this.getUIContext(), new WrappedBuilder(SimpleDialogBuilder), param);
          this.getUIContext().getPromptAction().openCustomDialog(contentNode, {
            autoCancel: true,
            maskColor: 'cc000000',
            maskRect: {
              x: 0,
              y: '-100%',
              width: '100%',
              height: '200%'
            },
            alignment: DialogAlignment.Bottom,
            transition: TransitionEffect.opacity(0).animation({ duration: 200 }),
            onWillDismiss: res => {
              contentNode.update({
                title: 'Title title title',
                desc: 'Description description description description description description description description description description description description',
                visible: Visibility.Hidden
              });
              res.dismiss();
            }
          });
        })
    }
    .width('100%')
    .height('100%')
  }
}
