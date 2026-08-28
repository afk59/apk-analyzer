# zoomOut

#### Module Import

import { map } from '@kit.MapKit';

#### zoomOut

zoomOut(): CameraUpdate

Zooms out on the map by 1 level.

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

[CameraUpdate](../cameraupdate/document.md)

 | 

Description of changes to the camera position.

 |

**Example**:

let cameraUpdate: map.CameraUpdate = map.zoomOut();
