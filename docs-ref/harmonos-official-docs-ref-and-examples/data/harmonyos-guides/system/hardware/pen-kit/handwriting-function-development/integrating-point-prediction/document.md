# Integrating Point Prediction

After point prediction is integrated, you can reduce the latency during drawing and writing in your app and improve stylus writing experience.

#### Use Case

Obtain a touch event on the custom screen of the app, and call the point prediction API to obtain the location information of the next predicted point.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/BT0N__gGRb2W7_9-7JPuzA/en-us_image_0000002535422313.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF41EB5B766F731B5EA7872CA936AFB2AD1C8766EF037779F738595BA1E85C56 "Click to enlarge")

#### API Description

| 
Class

 | 

API

 | 

Description

 |
| :-- | :-- | :-- |
| 

[PointPredictor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-pointpredictor)

 | 

[getPredictionPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-pointpredictor#section158711315171)(event: [TouchEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-events-touch#touchevent)): [TouchPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-types#touchpoint11)

 | 

Obtains a prediction point.

 |

#### Development Procedure

1\. Import required modules.

import { PointPredictor } from '@kit.Penkit';

2\. Obtain the touch event information of the current screen and call the API to calculate the prediction point information.

@Entry
@Component
struct PointPredictorDemo {
  @State actualXCoordinate: number = 0
  @State actualYCoordinate: number = 0
  @State predictorXCoordinate: Dimension = 0
  @State predictorYCoordinate: Dimension = 0
  pointPredictor: PointPredictor = new PointPredictor();

  aboutToAppear() {
    console.info('getPredictionPoint aboutToAppear')
  }

  aboutToDisappear() {
    console.info('getPredictionPoint aboutToDisappear')
  }

  build() {
    Stack({ alignContent: Alignment.TopEnd }) {
      this.Canvas() // Canvas.
    }.height('100%').width('100%')
  }

  // Canvas.
  @Builder
  Canvas() {
    Column() {
      Text ("Actual point coordinates: X: " + this.actualXCoordinate + " Y: " + this.actualYCoordinate) .textAlign(TextAlign.Start)
      Text ("Predicted point coordinates: X: " + this.predictorXCoordinate + " Y: " + this.predictorYCoordinate)
        .textAlign(TextAlign.Start)
    }.position({ x: 0, y: 0 })
    .alignItems(HorizontalAlign.Start)

    Stack()
      .width('100%')
      .height('100%')
      .onTouch((event: TouchEvent) => {
        switch (event.type) {
          case TouchType.Down: // Create a drawing path when the screen is touched.
            break;
          case TouchType.Move: // Use the prediction algorithm to perform prediction and obtain the prediction point.
            let point = this.pointPredictor?.getPredictionPoint(event)
            this.actualXCoordinate = event.touches\[0\]?.x
            this.actualYCoordinate = event.touches\[0\]?.y
            this.predictorXCoordinate = point?.x
            this.predictorYCoordinate = point?.y
            console.info ("pointPredictor actual point coordinates x:" + event.touches\[0\]?.x + " y:" + event.touches\[0\]?.y)
            console.info ("pointPredictor predicted point coordinates x:" + point?.x + " y:" + point?.y)
            break;
          case TouchType.Up:
            break;
        }
      })
  }
}
