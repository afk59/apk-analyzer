# How to simulate a touch event?

Simulating a touch event refers to simulating the touch operation on UI through code in the program. It is usually used in automatic tests or scenarios where UI restrictions need to be bypassed. To simulate the [TapGesture](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-gestures-tapgesture) event, you can use **onTouch** to trigger a touch event in the area outside the button, and use the **BuilderNode** method to pass the **touchEvent**.

import { NodeController, BuilderNode, FrameNode, UIContext } from '@kit.ArkUI';

class Params {
  text: string = 'this is a text';
}

@Builder
function ButtonBuilder(params: Params) {
  Column() {
    Button(\`button \` + params.text)
      .backgroundColor(Color.Orange)
      .width('100%')
      .gesture(
        TapGesture()
          .onAction((event: GestureEvent) => {
            console.info('TapGesture');
          })
      )
  }
  .width('100%')
  .height(300)
  .padding({
    left: 16,
    right: 16
  })
  .justifyContent(FlexAlign.Center)
  .backgroundColor(Color.Gray)
}

class MyNodeController extends NodeController {
  private rootNode: BuilderNode<\[Params\]> | null = null;
  private wrapBuilder: WrappedBuilder<\[Params\]> = wrapBuilder(ButtonBuilder);

  makeNode(uiContext: UIContext): FrameNode | null {
    this.rootNode = new BuilderNode(uiContext);
    this.rootNode.build(this.wrapBuilder, { text: 'this is a string' });
    return this.rootNode.getFrameNode();
  }

  // Coordinate Conversion Example
  postTouchEvent(event: TouchEvent, uiContext: UIContext): boolean {
    if (this.rootNode == null) {
      return false;
    }
    let node: FrameNode | null = this.rootNode.getFrameNode();
    if (node == null) {
      return false;
    }
    let offsetX: number | null | undefined = node?.getPositionToParent().x;
    let offsetY: number | null | undefined = node?.getPositionToParent().y;
    let changedTouchLen = event.changedTouches.length;
    for (let i = 0; i < changedTouchLen; i++) {
      if (offsetX != null && offsetY != null && offsetX != undefined && offsetY != undefined) {
        event.changedTouches\[i\].x = uiContext.vp2px(offsetX + event.changedTouches\[i\].x);
        event.changedTouches\[i\].y = uiContext.vp2px(offsetY + event.changedTouches\[i\].y);
      }
    }
    let result = this.rootNode.postTouchEvent(event);
    console.info('result:' + result);
    return result;
  }
}

@Entry
@Component
struct MyComponent {
  private nodeController: MyNodeController = new MyNodeController();

  build() {
    Column() {
      NodeContainer(this.nodeController)
        .height(300)
        .width('100%')

      Column()
        .width(500)
        .height(300)
        .backgroundColor('#0A59F7')
        .onTouch((event) => {
          if (event != undefined) {
            let uiContext = this.getUIContext();
            // Dispatch event events to the FrameNode created by the nodeController by touching them with fingers
            this.nodeController.postTouchEvent(event, uiContext);
          }
        })
    }
  }
}
