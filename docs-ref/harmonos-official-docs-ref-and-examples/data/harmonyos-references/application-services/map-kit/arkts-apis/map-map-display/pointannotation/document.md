# PointAnnotation

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### PointAnnotation

PointAnnotation, which inherits from [BasePriorityOverlay](../basepriorityoverlay/document.md). An instance of the PointAnnotation type will be returned when the [addPointAnnotation](../mapcomponentcontroller/document.md#section1899064804520) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

let pointAnnotationOptions: mapCommon.PointAnnotationParams = {
  position: {
    latitude: 32.120750,
    longitude: 118.788765
  },
  titles: \[{
    content: "Nanjing Confucius Temple",
  }\],
  // The icon must be stored in the **resources/rawfile** directory.
  icon: 'icon.png'
};
let pointAnnotation: map.PointAnnotation = await this.mapController.addPointAnnotation(pointAnnotationOptions);

#### \[h2\]getPosition

getPosition(): mapCommon.LatLng

Obtains the anchor coordinates of a PointAnnotation.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)

 | 

Anchor coordinates of a PointAnnotation.

 |

**Example**:

let position: mapCommon.LatLng = pointAnnotation.getPosition();

#### \[h2\]getTitleText

getTitleText(): mapCommon.Text

Obtains the attributes of a PointAnnotation's first title.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.Text](../../mapcommon-map-attribute-model/document.md#section132819018245)

 | 

Attributes of a PointAnnotation's first title.

 |

**Example**:

let titleText: mapCommon.Text = pointAnnotation.getTitleText();

#### \[h2\]setTitleText

setTitleText(text: mapCommon.Text): void

Sets the attributes of a PointAnnotation's first title (content excluded).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

text

 | 

[mapCommon.Text](../../mapcommon-map-attribute-model/document.md#section132819018245)

 | 

Yes

 | 

Attributes of a PointAnnotation's first title (content excluded).

NOTE:

Constraints: The values of **fontSize** and **strokeWidth** must be greater than or equal to 0.

 |

**Example**:

// Use a PointAnnotation as an example.
pointAnnotation.setTitleText({
  content: '',
  color: 0xff00ffff,
  fontSize: 15,
  strokeColor: 0xff00ff00,
  strokeWidth: 2,
  fontStyle: mapCommon.FontStyle.BOLD\_ITALIC
});

#### \[h2\]setTitleAnimation

setTitleAnimation(animation: FontSizeAnimation): void

Sets the title animation of a PointAnnotation.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Parameters**:

| 
Name

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

animation

 | 

[FontSizeAnimation](../fontsizeanimation/document.md)

 | 

Yes

 | 

Title animation of a PointAnnotation.

 |

**Example**:

let animation: map.FontSizeAnimation = new map.FontSizeAnimation(5, 25);
animation.setDuration(3000);
animation.on("start",() => {
  console.info('start Font Animation');
});
animation.on("end",() => {
  console.info('end Font Animation');
});
// Set the post-animation state.
animation.setFillMode(map.AnimationFillMode.BACKWARDS);
// Set the animation replay mode.
animation.setRepeatMode(map.AnimationRepeatMode.REVERSE);
// Set the animation interpolator.
animation.setInterpolator(Curve.Linear);
// Set the number of times the animation is replayed.
animation.setRepeatCount(100);
pointAnnotation.setTitleAnimation(animation);
pointAnnotation.startTitleAnimation();

#### \[h2\]startTitleAnimation

startTitleAnimation(): void

Starts the title animation of a PointAnnotation.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

pointAnnotation.startTitleAnimation();
