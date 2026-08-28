# PointPredictor

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

#### Module Import

import { PointPredictor } from '@kit.Penkit';

The module provides the following methods.

| 
Method

 | 

Description

 |
| :-- | :-- |
| 

[getPredictionPoint](#section158711315171)

 | 

Obtains the prediction point information.

 |

#### getPredictionPoint

getPredictionPoint(event: TouchEvent): TouchPoint

Obtains the prediction point information.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

event

 | 

[TouchEvent](../../../../../application-framework/arkui/arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent)

 | 

Yes

 | 

Information about the current touch event.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[TouchPoint](../../../../../application-framework/arkui/arkts-components/common-definitions/basic-types/document.md#touchpoint11)

 | 

Prediction point information.

 |

**Example**:

import { PointPredictor } from '@kit.Penkit';

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
