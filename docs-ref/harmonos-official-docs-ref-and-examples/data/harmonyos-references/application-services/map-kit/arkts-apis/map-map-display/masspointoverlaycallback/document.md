# MassPointOverlayCallback

#### MassPointOverlayCallback

type MassPointOverlayCallback = (massPointOverlay: MassPointOverlay, massPointItem: mapCommon.MassPointItem) => void

Callback function that returns no result. This callback is used to listen for MassPointOverlay tap events.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

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

massPointOverlay

 | 

[MassPointOverlay](../masspointoverlay/document.md)

 | 

Yes

 | 

MassPointOverlay object.

 |
| 

massPointItem

 | 

[mapCommon.MassPointItem](../../mapcommon-map-attribute-model/document.md#section17837254174411)

 | 

Yes

 | 

Mass point list.

 |
