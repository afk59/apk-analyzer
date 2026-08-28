# ClusterOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### ClusterOverlay

ClusterOverlay class.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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
    longitude:118.75
  }
};
let array: Array<mapCommon.ClusterItem> = \[
  clusterItem1,
  clusterItem2
\];
let clusterOverlayParams: mapCommon.ClusterOverlayParams = { distance: 40, clusterItems: array };
let clusterOverlay: map.ClusterOverlay = await this.mapController.addClusterOverlay(clusterOverlayParams);

#### \[h2\]on('clusterClick')

on(type: 'clusterClick', callback: Callback<Array<mapCommon.ClusterItem>>): void

Listens for ClusterOverlay tap events. This API returns the result asynchronously through a callback.

You are advised to use [ClusterOverlay.on(type: 'click')](#section8306133712135).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

**'clusterClick'**: listens for events triggered when cluster items of a ClusterOverlay are tapped.

 |
| 

callback

 | 

Callback<Array<[mapCommon.ClusterItem](../../mapcommon-map-attribute-model/document.md#section9436522104316)\>>

 | 

Yes

 | 

Callback function, which returns Array<[mapCommon.ClusterItem](../../mapcommon-map-attribute-model/document.md#section9436522104316)\>.

 |

**Example**:

clusterOverlay.on("clusterClick", (clusterItems) => {
  console.info(\`callback: ${clusterItems.length}\`);
});

#### \[h2\]off('clusterClick')

off(type: 'clusterClick', callback?: Callback<void>): void

Cancels listening for ClusterOverlay tap events. This API returns the result asynchronously through a callback.

You are advised to use [ClusterOverlay.off(type: 'click')](#section13314133751318).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

**'clusterClick'**: listens for events triggered when cluster items of a ClusterOverlay are tapped.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no value.

 |

**Example**:

clusterOverlay.off("clusterClick", () => {
  console.info("callback off");
});

#### \[h2\]on('click')

on(type: 'click', callback: Callback<Array<mapCommon.ClusterItem>>): void

Listens for cluster item tap events. This API can use multiple asynchronous callbacks to return the result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

**'click'**: Listens for cluster item tap events.

 |
| 

callback

 | 

Callback<Array<[mapCommon.ClusterItem](../../mapcommon-map-attribute-model/document.md#section9436522104316)\>>

 | 

Yes

 | 

Callback function, which returns Array<[mapCommon.ClusterItem](../../mapcommon-map-attribute-model/document.md#section9436522104316)\>. This callback is used to listen for cluster item tap events.

 |

**Example**:

let callback1 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", \`callback1 clusterItem length: ${clusterItem.length}\`);
};
let callback2 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", \`callback2 clusterItem length: ${clusterItem.length}\`);
};
let callback3 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", \`callback3 clusterItem length: ${clusterItem.length}\`);
};
clusterOverlay.on("click", callback1);
clusterOverlay.on("click", callback2);
clusterOverlay.on("click", callback3);

#### \[h2\]off('click')

off(type: 'click', callback?: Callback<Array<mapCommon.ClusterItem>>): void

Cancels listening for cluster item tap events. This API can use multiple asynchronous callbacks to return the result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

**'click'**: Listens for cluster item tap events.

 |
| 

callback

 | 

Callback<Array<[mapCommon.ClusterItem](../../mapcommon-map-attribute-model/document.md#section9436522104316)\>>

 | 

No

 | 

Callback function, which returns Array<[mapCommon.ClusterItem](../../mapcommon-map-attribute-model/document.md#section9436522104316)\>. This callback is used to cancel listening for cluster item tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", \`callback1 clusterItem\`);
};
let callback2 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", \`callback2 clusterItem\`);
};
let callback3 = (clusterItem: Array<mapCommon.ClusterItem>) => {
  console.info("click", \`callback3 clusterItem\`);
};
clusterOverlay.on("click", callback1);
clusterOverlay.on("click", callback2);
clusterOverlay.on("click", callback3);

// Cancel only the event response of the **callback1** object. When a **click** event occurs, **callback2** and **callback3** will be called. 
clusterOverlay.off('click', callback1);
// Cancel all **click** event responses.
clusterOverlay.off('click');

#### \[h2\]on('markerClusterClick')

on(type: 'markerClusterClick', callback: Callback<MarkerClusterInfo>): void

Listens for tap events that occur on markers of a ClusterOverlay. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

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

type

 | 

string

 | 

Yes

 | 

**'markerClusterClick'**: listens for tap events that occur on markers of a ClusterOverlay.

 |
| 

callback

 | 

Callback<[MarkerClusterInfo](../markerclusterinfo/document.md)\>

 | 

Yes

 | 

Callback function, which returns Callback<[MarkerClusterInfo](../markerclusterinfo/document.md)\>. This callback is used to listen for tap events that occur on markers of a ClusterOverlay.

**MarkerClusterInfo** includes:

-   **marker**: Marker on a ClusterOverlay.
-   **clusterItems**: Cluster item array.

 |

**Example**:

let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", \`callback1 markerClusterInfo\`);
};
let callback2 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", \`callback2 markerClusterInfo\`);
};
let callback3 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", \`callback3 markerClusterInfo\`);
};
clusterOverlay.on("markerClusterClick", callback1);
clusterOverlay.on("markerClusterClick", callback2);
clusterOverlay.on("markerClusterClick", callback3);

#### \[h2\]off('markerClusterClick')

off(type: 'markerClusterClick', callback?: Callback<MarkerClusterInfo>): void

Cancels listening for tap events that occur on markers of a ClusterOverlay. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

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

type

 | 

string

 | 

Yes

 | 

**'markerClusterClick'**: listens for tap events that occur on markers of a ClusterOverlay.

 |
| 

callback

 | 

Callback<[MarkerClusterInfo](../markerclusterinfo/document.md)\>

 | 

No

 | 

Callback function, which returns Callback<[MarkerClusterInfo](../markerclusterinfo/document.md)\>. This callback is used to cancel listening for tap events that occur on markers of a ClusterOverlay.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

**MarkerClusterInfo** includes:

-   **marker**: Marker on a ClusterOverlay.
-   **clusterItems**: Cluster item array.

 |

**Example**:

let callback1 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", \`callback1 markerClusterInfo\`);
};
let callback2 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", \`callback2 markerClusterInfo\`);
};
let callback3 = (markerClusterInfo: map.MarkerClusterInfo) => {
  console.info("markerClusterClick", \`callback3 markerClusterInfo\`);
};
clusterOverlay.on("markerClusterClick", callback1);
clusterOverlay.on("markerClusterClick", callback2);
clusterOverlay.on("markerClusterClick", callback3);
// Cancel only the event response of the **callback1** object. When a **markerClusterClick** event occurs, **callback2** and **callback3** will be called.
clusterOverlay.off('markerClusterClick', callback1);
// Cancel all **markerClusterClick** event responses.
clusterOverlay.off('markerClusterClick');

#### \[h2\]addItem

addItem(item: mapCommon.ClusterItem): Promise<void>

Adds a cluster item. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

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

item

 | 

mapCommon.[ClusterItem](../../mapcommon-map-attribute-model/document.md#section9436522104316)

 | 

Yes

 | 

Cluster item.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Example**:

let clusterItem: mapCommon.ClusterItem = {
  position: {
    latitude: 31.98,
    longitude: 118.766
  }
};
await clusterOverlay.addItem(clusterItem);

#### \[h2\]remove

remove(): Promise<void>

Removes a ClusterOverlay. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Example**:

await clusterOverlay.remove();
