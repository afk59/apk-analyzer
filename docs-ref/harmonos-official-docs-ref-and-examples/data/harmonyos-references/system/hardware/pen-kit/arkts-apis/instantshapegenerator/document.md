# InstantShapeGenerator

Main entrance for accessing functions of Instant Shape.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

#### Module Import

import { InstantShapeGenerator, ShapeInfo } from '@kit.Penkit';

This module provides the classes or APIs described in the following table to implement the function of Instant Shape.

| 
Name

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

ShapeInfo

 | 

[ShapeInfo](#section579673518478)

 | 

Object of the recognized result using Instant Shape, including the basic information about the recognized shape.

 |

The module provides the following methods.

| 
Method

 | 

Description

 |
| :-- | :-- |
| 

[processTouchEvent](#section759192934316)

 | 

Processes a touch event.

 |
| 

[getPathFromString](#section613810527439)

 | 

Extracts shape information from a given shape string.

 |
| 

[notifyAreaChange](#section660833016157)

 | 

Notifies of the size change.

 |
| 

[setPauseTime](#section74801151101719)

 | 

Sets the pause duration for triggering recognition, in ms.

 |
| 

[release](#section8613112012)

 | 

Destroys the recognition tool.

 |
| 

[onShapeRecognized](#section0716101115205)

 | 

Registers a callback for the recognition.

 |

#### ShapeInfo

Object of the recognized result using Instant Shape, including the basic information about the recognized shape.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters:**

| 
**Name**

 | 

**Type**

 | 

Read-Only

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

shapePath

 | 

[Path2D](../../../../../application-framework/arkui/arkts-components/canvas-drawing/path2d/document.md)

 | 

No

 | 

No

 | 

Shape object.

 |
| 

shapeString

 | 

string

 | 

No

 | 

No

 | 

Shape information, which can be saved.

 |
| 

shapeType

 | 

number

 | 

No

 | 

No

 | 

Shape type.

-   **0**: unknown type (recognition failure)
-   **1**: straight line
-   **2**: circle (ellipse)
-   **3**: broken line
-   **6**: rectangle
-   **7**: parallelogram
-   **9**: rhombus
-   **10**: isosceles triangle
-   **11**: equilateral triangle
-   **12**: pentagram
-   **13**: pentagon
-   **14**: parabola
-   **15**: straight line with an arrow pointing to the start point
-   **16**: straight line with an arrow pointing to the end point
-   **17**: straight line with arrows pointing to both points
-   **18**: parabola with an arrow pointing to the start point
-   **19**: parabola with an arrow pointing to the end point
-   **20**: parabola with arrows pointing to both points

 |

**Example**:

private shapeInfo : ShapeInfo = {
shapePath: '',
shapeString: '',
shapeType: 0
}

#### processTouchEvent

processTouchEvent(event: TouchEvent): void

Processes a touch event.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

event

 | 

[TouchEvent](../../../../../application-framework/arkui/arkts-components/universal-events/basic-input-events/touch-event/document.md#touchevent)

 | 

Yes

 | 

Current touch event.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010410001

 | 

internal recognition engine has been released.

 |

**Example**:

instantShapeGenerator: InstantShapeGenerator = new InstantShapeGenerator();
// Canvas.
@Builder
Canvas() {
  Stack()
    .width('100%')
    .height('100%')
    .onTouch((event: TouchEvent) => {
      this.instantShapeGenerator?.processTouchEvent(event);
    })
}

#### getPathFromString

getPathFromString(shapeString: string, penSize: number): Path2D

Extracts shape information from a given shape string and uses the information to generate a **Path2D** object.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

shapeString

 | 

string

 | 

Yes

 | 

Shape string. No value range restriction is specified.

 |
| 

penSize

 | 

number

 | 

Yes

 | 

Pen width used to draw the result shape. Some shapes, such as arrows, vary according to this value. Unit: 1/1000 of the canvas width.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Path2D](../../../../../application-framework/arkui/arkts-components/canvas-drawing/path2d/document.md)

 | 

**Path2D** object generated based on shape information.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010410001

 | 

internal recognition engine has been released.

 |

**Example**:

// Obtain the recognition result using the callback.
private shapeInfoCallback(shapeInfo: ShapeInfo) {
  this.drawPath = this.instantShapeGenerator?.getPathFromString(shapeInfo.shapeString, this.penWidth);
}

#### notifyAreaChange

notifyAreaChange(width: number, height: number): void

Notifies of the component size change. The shape size (such as the radius of a circle) varies according to the component size.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

width

 | 

number

 | 

Yes

 | 

Width of the component after the change. Unit: 1/1000 of the canvas width.

 |
| 

height

 | 

number

 | 

Yes

 | 

Height of the component after the change. Unit: 1/1000 of the canvas width.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010410001

 | 

internal recognition engine has been released.

 |

**Example**:

// Canvas.
@Builder Canvas() {
  Stack()
    .width('100%')
    .height('100%')
    .onAreaChange((oldValue, newValue) => {
    this.instantShapeGenerator?.notifyAreaChange(Number(newValue.width), Number(newValue.height));
  })
}

#### setPauseTime

setPauseTime(time: number): void

Sets the pause time for triggering recognition.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

time

 | 

number

 | 

Yes

 | 

Pause time for triggering recognition.

The unit is ms.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1010410001

 | 

internal recognition engine has been released.

 |

**Example**:

aboutToAppear() {
  console.info('InstantShapeGenerator aboutToAppear')
  this.instantShapeGenerator?.setPauseTime(280);
}

#### release

release(): void

Destroys the Instant Shape tool.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Stylus.Handwrite

**Start version**: 5.0.0(12)

**Example**:

aboutToDisappear(){
  console.info('InstantShapeGenerator aboutToDisappear')
  this.instantShapeGenerator?.release();
}

#### onShapeRecognized

onShapeRecognized(callback: Callback<ShapeInfo>): InstantShapeGenerator

Registers a callback for the recognition.

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

callback

 | 

Callback<[ShapeInfo](#section579673518478)\>

 | 

Yes

 | 

Callback triggered when the shape recognition is complete.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[InstantShapeGenerator](#)

 | 

Instance of the Instant Shape function class.

 |

**Example**:

// Obtain the recognition result using the callback.
private shapeInfoCallback(shapeInfo: ShapeInfo) {
  this.shapeInfo = shapeInfo;
}

aboutToAppear() {
  console.info('InstantShapeGenerator aboutToAppear')
  this.instantShapeGenerator?.onShapeRecognized(this.shapeInfoCallback)
}
