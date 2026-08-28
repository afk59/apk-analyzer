# How do I obtain the component rendering completion time?

You can use the APIs in **@kit.ArkUI.inspector** to obtain notifications of drawing completion callbacks. Create a **ComponentObserver** instance, register the draw event listener, record the start time in **aboutToAppear**, and listen for the drawing completion time in the listener. The difference in time is the component rendering time. The sample code is as follows:

import { inspector } from '@kit.ArkUI';

@Entry
@Component
struct GetComponentRenderTime {
  @State startTime: number = 0;
  private listener: inspector.ComponentObserver = this.getUIContext().getUIInspector().createComponentObserver('IMAGE\_ID');
  // Calculate rendering duration: currentTime - this.startTime
  private onDrawCompleteCallback = () => {
    // 2. Time when the image component finishes drawing
    console.info('onDrawComplete', new Date().getTime());
  };

  aboutToAppear() {
    // 1. Time when rendering starts
    this.startTime = new Date().getTime();
    console.info('aboutToAppear', this.startTime);

    // layout: Component layout completed
    // draw: Component drawing completed
    this.listener.on('draw', this.onDrawCompleteCallback);
  }

  aboutToDisappear() {
    // Unregister callback before destruction
    this.listener.off('draw', this.onDrawCompleteCallback);
  }

  build() {
    Column() {
      Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Start }) {
        Row({ space: 5 }) {
          Image($r('app.media.app\_icon'))
            .width(110)
            .height(110)
            .id('IMAGE\_ID')
        }
      }
    }
    .height(320)
    .width(360)
    .padding({
      right: 10,
      top: 10
    })
  }
}
