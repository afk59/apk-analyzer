# FlowFieldOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### FlowFieldOverlay

FlowFieldOverlay object. An instance of the FlowFieldOverlay type will be returned when the [addFlowFieldOverlay](../mapcomponentcontroller/document.md#section7516202017439) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called. This API inherits from [BaseOverlay](../baseoverlay/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

**Example**:

let params: mapCommon.FlowFieldOverlayParams = {
  // The value of **data** must be in JSON format that complies with the GRIB2 specification. Set **data** by referring to [Flow Field Data Format Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/map-flow-field#section138174613135).
  data: 'xxx'
};
let fieldOverlay = await mapController.addFlowFieldOverlay(params);

#### \[h2\]setStyle

setStyle(style: mapCommon.ParticleStyle): void

Sets the particle style.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

**Parameters**:

| 
**Name**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

style

 | 

[mapCommon.ParticleStyle](../../mapcommon-map-attribute-model/document.md#section1666151282917)

 | 

Yes

 | 

Particle style.

 |

**Example**:

let style: mapCommon.ParticleStyle = {
  count: 200,
  color: 0xff009575,
  maxSpeed: 60,
  speedFactor: 0.3
};
fieldOverlay.setStyle(style);

#### \[h2\]getStyle

getStyle(): mapCommon.ParticleStyle

Obtains the particle style.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[mapCommon.ParticleStyle](../../mapcommon-map-attribute-model/document.md#section1666151282917)

 | 

Particle style.

 |

**Example**:

let style: mapCommon.ParticleStyle = fieldOverlay.getStyle();
