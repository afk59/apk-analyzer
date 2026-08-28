# Integrating Instant Shape

After Instant Shape is integrated, the point information of users' strokes will be passed. They can hold their stylus/finger on the screen for a certain period of time when a continuous drawing path ends and turn it into a regular shape.

#### Use Case

Implement the Instant Shape feature in the app. The effect is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/gMlAwkP2TQuGpkBda7fjKg/en-us_image_0000002503542526.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062024Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73CDE3ADDF46D6419B89AC2E3C745398963349930D98F70570685889BB42E2EB "Click to enlarge")

1.  This capability can obtain and store recognized image information.
2.  This capability can read information from a stored image.

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

[InstantShapeGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator)

 | 

[processTouchEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator#section759192934316)

 | 

Processes a touch event.

 |
| 

[InstantShapeGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator)

 | 

[getPathFromString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator#section613810527439)

 | 

Extracts shape information from a given shape string.

 |
| 

[InstantShapeGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator)

 | 

[notifyAreaChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator#section660833016157)

 | 

Notifies of the component size change.

 |
| 

[InstantShapeGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator)

 | 

[setPauseTime](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator#section74801151101719)

 | 

Sets the pause duration for triggering recognition, in ms.

 |
| 

[InstantShapeGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator)

 | 

[release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator#section8613112012)

 | 

Destroys the recognition tool.

 |
| 

[InstantShapeGenerator](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator)

 | 

[onShapeRecognized](https://developer.huawei.com/consumer/en/doc/harmonyos-references/pen-instantsshapegenerator#section0716101115205)

 | 

Registers a callback for the recognition.

 |

#### Development Procedure

1\. Import required modules.

import { InstantShapeGenerator, ShapeInfo } from '@kit.Penkit';

2\. Construct the Instant Shape capability. The following uses a component as an example:

@Entry
@Component
struct InstantShapeDemo {
  private instantShapeGenerator: InstantShapeGenerator = new InstantShapeGenerator();
  private points: DrawPathPointModel\[\] = \[\];
  // Draw a path.
  private drawPath = new Path2D();
  private shapePath = new Path2D();
  private mShapeSuccess = false;
  private settings: RenderingContextSettings = new RenderingContextSettings(true);
  private context: CanvasRenderingContext2D = new CanvasRenderingContext2D(this.settings);
  // Obtain the recognition result using the callback.
  private shapeInfoCallback = (shapeInfo: ShapeInfo) => {
    this.shapePath = shapeInfo.shapePath;
    this.mShapeSuccess = true;
    this.context.beginPath();
    this.context.reset();
    this.drawCurrentPathModel(this.shapePath);
  }

  aboutToAppear() {
    console.info('InstantShapeGenerator aboutToAppear');
    // Set the pause time for triggering recognition.
    this.instantShapeGenerator?.setPauseTime(280);
    // Register a callback for the recognition.
    this.instantShapeGenerator?.onShapeRecognized(this.shapeInfoCallback);
  }

  aboutToDisappear() {
    console.info('InstantShapeGenerator aboutToDisappear')
    this.instantShapeGenerator?.release();
  }

  build() {
    Stack({ alignContent: Alignment.TopEnd }) {
      Canvas(this.context)
        .width('100%')
        .height('100%')
        .onAreaChange((oldValue: Area, newValue: Area) => {
          // Notify of the component size change. The size of the shape (for example, the radius of the circle) changes according to the dimensions of the component.
          this.instantShapeGenerator?.notifyAreaChange(Number(newValue.width), Number(newValue.height));
        }).onTouch((event: TouchEvent) => {
        // Process a touch event.
        this.instantShapeGenerator?.processTouchEvent(event);
        switch (event.type) {
          case TouchType.Down:
            this.moveStart(event.touches\[0\]?.x, event.touches\[0\]?.y);
            break;
          case TouchType.Move:
            this.moveUpdate(event.touches\[0\]?.x, event.touches\[0\]?.y);
            break;
          case TouchType.Up:
            this.moveEnd();
            break;
        }
      })
    }.height('100%').width('100%')
  }

  moveStart(x: number, y: number) {
    this.points.push({ x: x, y: y })
    this.drawPath.moveTo(x, y);
    this.drawCurrentPathModel(this.drawPath);
    this.mShapeSuccess = false;
  }

  moveUpdate(x: number, y: number) {
    let lastPoint = this.points\[this.points.length - 1\];
    this.points.push({ x: x, y: y });
    this.drawPath.quadraticCurveTo((x + lastPoint?.x) / 2, (y + lastPoint?.y) / 2, x, y);
    if (!this.mShapeSuccess) {
      this.drawCurrentPathModel(this.drawPath);
    }
  }

  moveEnd() {
    this.points = \[\];
    this.drawPath = new Path2D();
    this.shapePath = new Path2D();
  }

  private drawCurrentPathModel(path: Path2D) {
    this.context.globalCompositeOperation = 'source-over';
    this.context.lineWidth = 8;
    this.context.strokeStyle = "#ED1B1B";
    this.context.lineJoin = 'round';
    this.context.stroke(path);
  }
}

export class DrawPathPointModel {
  x: number = 0;
  y: number = 0;
}
