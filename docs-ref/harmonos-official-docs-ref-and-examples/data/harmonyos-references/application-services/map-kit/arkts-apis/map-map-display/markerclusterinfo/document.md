# MarkerClusterInfo

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MarkerClusterInfo

Information about a Marker on a ClusterOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

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

marker

 | 

[Marker](../marker/document.md)

 | 

No

 | 

No

 | 

Marker on a ClusterOverlay.

 |
| 

clusterItems

 | 

Array<[mapCommon.ClusterItem](../../mapcommon-map-attribute-model/document.md#section9436522104316)\>

 | 

No

 | 

No

 | 

Cluster item array.

 |

**Example**:

let clusterItem1: mapCommon.ClusterItem = {
  position: {
    latitude: 31.984,
    longitude: 118.766
  }
};
let clusterItem2: mapCommon.ClusterItem = {
  position: {
    latitude: 31.974,
    longitude: 118.75
  }
};
let array: Array<mapCommon.ClusterItem> = \[
  clusterItem1,
  clusterItem2
\];
let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 40, clusterItems: array };
let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);
let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", \`callback1 markerClusterInfo\`);
};
clusterOverlay.on("markerClusterClick", callback1);
