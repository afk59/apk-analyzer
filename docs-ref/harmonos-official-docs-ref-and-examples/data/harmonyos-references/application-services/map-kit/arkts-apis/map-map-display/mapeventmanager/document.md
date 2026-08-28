# MapEventManager

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MapEventManager

Map event listening manager.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

let mapEventManager: map.MapEventManager = this.mapController.getEventManager();

#### \[h2\]on('cameraChange')

on(type: 'cameraChange', callback: Callback<mapCommon.LatLng>): void

Listens for map camera status changes. This API can use multiple asynchronous callbacks to return the result. The callbacks are not triggered during animation. Instead, they are triggered when the animation ends.

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

**'cameraChange'**: listens for map camera status change events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810). This callback is used to listen for map camera status change events. The callback is not triggered during animation. Instead, it is triggered when the animation ends.

 |

**Example**:

let callback1 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", \`callback1 position = ${position.longitude}\`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", \`callback2 position = ${position.longitude}\`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", \`callback3 position = ${position.longitude}\`);
};
mapEventManager.on("cameraChange", callback1);
mapEventManager.on("cameraChange", callback2);
mapEventManager.on("cameraChange", callback3);

#### \[h2\]off('cameraChange')

off(type: 'cameraChange', callback?: Callback<mapCommon.LatLng>): void

Cancels listening for map camera status change events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraChange'**: listens for map camera status change events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810) to cancel listening for map camera status change events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", \`callback1 position\`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", \`callback2 position\`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("cameraChange", \`callback3 position\`);
};
mapEventManager.on("cameraChange", callback1);
mapEventManager.on("cameraChange", callback2);
mapEventManager.on("cameraChange", callback3);
// Cancel only the event response of the **callback1** object. When a **cameraChange** event occurs, **callback2** and **callback3** will be called.
mapEventManager.off('cameraChange', callback1);
// Cancel all **cameraChange** event responses.
mapEventManager.off('cameraChange');

#### \[h2\]on('cameraIdle')

on(type: 'cameraIdle', callback: Callback<void>): void

Listens for camera movement end events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraIdle'**: listens for camera movement end events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no result. This callback is used to listen for camera movement end events.

 |

**Example**:

let callback1 = () => {
  console.info("cameraIdle", \`callback1\`);
};
let callback2 = () => {
  console.info("cameraIdle", \`callback2\`);
};
let callback3 = () => {
  console.info("cameraIdle", \`callback3\`);
};
mapEventManager.on("cameraIdle", callback1);
mapEventManager.on("cameraIdle", callback2);
mapEventManager.on("cameraIdle", callback3);

#### \[h2\]off('cameraIdle')

off(type: 'cameraIdle', callback?: Callback<void>): void

Cancels listening for camera movement end events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraIdle'**: listens for camera movement end events.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no result. This callback is used to cancel listening for camera movement end events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = () => {
  console.info("cameraIdle", \`callback1\`);
};
let callback2 = () => {
  console.info("cameraIdle", \`callback2\`);
};
let callback3 = () => {
  console.info("cameraIdle", \`callback3\`);
};
mapEventManager.on("cameraIdle", callback1);
mapEventManager.on("cameraIdle", callback2);
mapEventManager.on("cameraIdle", callback3);
// Cancel only the event response of the **callback1** object. When a **cameraIdle** event occurs, **callback2** and **callback3** will be called.
mapEventManager.off('cameraIdle', callback1);
// Cancel all **cameraIdle** event responses.
mapEventManager.off('cameraIdle');

#### \[h2\]on('cameraMoveCancel')

on(type: 'cameraMoveCancel', callback: Callback<void>): void

Listens for camera movement cancellation events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraMoveCancel'**: listens for camera movement cancellation events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no result. This callback is used to listen for map camera movement cancellation events.

 |

**Example**:

let callback1 = () => {
  console.info("cameraMoveCancel", \`callback1\`);
};
let callback2 = () => {
  console.info("cameraMoveCancel", \`callback2\`);
};
let callback3 = () => {
  console.info("cameraMoveCancel", \`callback3\`);
};
mapEventManager.on("cameraMoveCancel", callback1);
mapEventManager.on("cameraMoveCancel", callback2);
mapEventManager.on("cameraMoveCancel", callback3);

#### \[h2\]off('cameraMoveCancel')

off(type: 'cameraMoveCancel', callback?: Callback<void>): void

Cancels listening for camera movement cancellation events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraMoveCancel'**: listens for camera movement cancellation events.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no result. This callback is used to cancel listening for map camera movement cancellation events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = () => {
  console.info("cameraMoveCancel", \`callback1\`);
};
let callback2 = () => {
  console.info("cameraMoveCancel", \`callback2\`);
};
let callback3 = () => {
  console.info("cameraMoveCancel", \`callback3\`);
};
mapEventManager.on("cameraMoveCancel", callback1);
mapEventManager.on("cameraMoveCancel", callback2);
mapEventManager.on("cameraMoveCancel", callback3);
// Cancel only the event response of the **callback1** object. When a **cameraMoveCancel** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('cameraMoveCancel', callback1);
// Cancel all **cameraMoveCancel** event responses.
mapEventManager.off('cameraMoveCancel');

#### \[h2\]on('cameraMove')

on(type: 'cameraMove', callback: Callback<void>): void

Listens for camera movement events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraMove'**: listens for camera movement events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no result. This callback is used to listen for camera movement events.

 |

**Example**:

let callback1 = () => {
  console.info("cameraMove", \`callback1\`);
};
let callback2 = () => {
  console.info("cameraMove", \`callback2\`);
};
let callback3 = () => {
  console.info("cameraMove", \`callback3\`);
};
mapEventManager.on("cameraMove", callback1);
mapEventManager.on("cameraMove", callback2);
mapEventManager.on("cameraMove", callback3);

#### \[h2\]off('cameraMove')

off(type: 'cameraMove', callback?: Callback<void>): void

Cancels listening for camera movement events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraMove'**: listens for camera movement events.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no result. This callback is used to cancel listening for camera movement events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = () => {
  console.info("cameraMove", \`callback1\`);
};
let callback2 = () => {
  console.info("cameraMove", \`callback2\`);
};
let callback3 = () => {
  console.info("cameraMove", \`callback3\`);
};
mapEventManager.on("cameraMove", callback1);
mapEventManager.on("cameraMove", callback2);
mapEventManager.on("cameraMove", callback3);
// Cancel only the event response of the **callback1** object. When a **cameraMove** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('cameraMove', callback1);
// Cancel all **cameraMove** event responses.
mapEventManager.off('cameraMove');

#### \[h2\]on('cameraMoveStart')

on(type: 'cameraMoveStart', callback: Callback<number>): void

Listens for camera movement start events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraMoveStart'**: listens for camera movement start events.

 |
| 

callback

 | 

Callback<number>

 | 

Yes

 | 

Callback function, which returns **number**. This callback is used to listen for camera movement start events.

**number** indicates the reason why the camera moves.

-   **1**: A user makes a gesture on the map.
-   **2**: The default animation is triggered by user interaction.
-   **3**: You start an animation.

 |

**Example**:

let callback1 = (reason: number) => {
  console.info("cameraMoveStart", \`callback1 reason = ${reason}\`);
};
let callback2 = (reason: number) => {
  console.info("cameraMoveStart", \`callback2 reason = ${reason}\`);
};
let callback3 = (reason: number) => {
  console.info("cameraMoveStart", \`callback3 reason = ${reason}\`);
};
mapEventManager.on("cameraMoveStart", callback1);
mapEventManager.on("cameraMoveStart", callback2);
mapEventManager.on("cameraMoveStart", callback3);

#### \[h2\]off('cameraMoveStart')

off(type: 'cameraMoveStart', callback?: Callback<number>): void

Cancels listening for camera movement start events. This API can use multiple asynchronous callbacks to return the result.

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

**'cameraMoveStart'**: listens for camera movement start events.

 |
| 

callback

 | 

Callback<number>

 | 

No

 | 

Callback used to cancel listening for camera movement start events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

**number** indicates the reason why the camera moves.

-   **1**: A user makes a gesture on the map.
-   **2**: The default animation is triggered by user interaction.
-   **3**: You start an animation.

 |

**Example**:

let callback1 = (reason: number) => {
  console.info("cameraMoveStart", \`callback1\`);
};
let callback2 = (reason: number) => {
  console.info("cameraMoveStart", \`callback2\`);
};
let callback3 = (reason: number) => {
  console.info("cameraMoveStart", \`callback3\`);
};
mapEventManager.on("cameraMoveStart", callback1);
mapEventManager.on("cameraMoveStart", callback2);
mapEventManager.on("cameraMoveStart", callback3);

// Cancel only the event response of the **callback1** object. When a **cameraMoveStart** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('cameraMoveStart', callback1);
// Cancel all **cameraMoveStart** event responses.
mapEventManager.off('cameraMoveStart');

#### \[h2\]on('mapClick')

on(type: 'mapClick', callback: Callback<mapCommon.LatLng>): void

Listens for map tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'mapClick'**: listens for map tap events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810). This callback is used to listen for map tap events.

 |

**Example**:

let callback1 = (position: mapCommon.LatLng) => {
  console.info("mapClick", \`callback1 position = ${position.longitude}\`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("mapClick", \`callback2 position = ${position.longitude}\`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("mapClick", \`callback3 position = ${position.longitude}\`);
};
mapEventManager.on("mapClick", callback1);
mapEventManager.on("mapClick", callback2);
mapEventManager.on("mapClick", callback3);

#### \[h2\]off('mapClick')

off(type: 'mapClick', callback?: Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>): void

Cancels listening for map tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'mapClick'**: listens for map tap events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810). This callback is used to cancel listening for map tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (position: mapCommon.LatLng) => {
  console.info("mapClick", \`callback1 position\`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("mapClick", \`callback2 position\`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("mapClick", \`callback3 position\`);
};
mapEventManager.on("mapClick", callback1);
mapEventManager.on("mapClick", callback2);
mapEventManager.on("mapClick", callback3);

// Cancel only the event response of the **callback1** object. When a **mapClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('mapClick', callback1);
// Cancel all **mapClick** event responses.
mapEventManager.off('mapClick');

#### \[h2\]on('mapLoad')

on(type: 'mapLoad', callback: Callback<void>): void

Listens for map load events. This API can use multiple asynchronous callbacks to return the result.

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

**'mapLoad'**: listens for map load events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no result. This callback is used to listen for map load events.

 |

**Example**:

let callback1 = () => {
  console.info("mapLoad", \`callback1\`);
};
let callback2 = () => {
  console.info("mapLoad", \`callback2\`);
};
let callback3 = () => {
  console.info("mapLoad", \`callback3\`);
};
mapEventManager.on("mapLoad", callback1);
mapEventManager.on("mapLoad", callback2);
mapEventManager.on("mapLoad", callback3);

#### \[h2\]off('mapLoad')

off(type: 'mapLoad', callback?: Callback<void>): void

Cancels listening for map load events. This API can use multiple asynchronous callbacks to return the result.

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

**'mapLoad'**: listens for map load events.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no result. This callback is used to cancel listening for map load events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = () => {
  console.info("mapLoad", \`callback1\`);
};
let callback2 = () => {
  console.info("mapLoad", \`callback2\`);
};
let callback3 = () => {
  console.info("mapLoad", \`callback3\`);
};
mapEventManager.on("mapLoad", callback1);
mapEventManager.on("mapLoad", callback2);
mapEventManager.on("mapLoad", callback3);

// Cancel only the event response of the **callback1** object. When a **mapLoad** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('mapLoad', callback1);
// Cancel all **mapLoad** event responses.
mapEventManager.off('mapLoad');

#### \[h2\]on('mapLongClick')

on(type: 'mapLongClick', callback: Callback<mapCommon.LatLng>): void

Listens for map long-press events. This API can use multiple asynchronous callbacks to return the result.

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

**'mapLongClick'**: listens for map long-press events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810). This callback is used to listen for map long-press events.

 |

**Example**:

let callback1 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", \`callback1 position = ${position.longitude}\`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", \`callback2 position = ${position.longitude}\`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", \`callback3 position = ${position.longitude}\`);
};
mapEventManager.on("mapLongClick", callback1);
mapEventManager.on("mapLongClick", callback2);
mapEventManager.on("mapLongClick", callback3);

#### \[h2\]off('mapLongClick')

off(type: 'mapLongClick', callback?: Callback<mapCommon.LatLng>): void

Cancels listening for map long-press events. This API can use multiple asynchronous callbacks to return the result.

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

**'mapLongClick'**: listens for map long-press events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810). This callback is used to cancel listening for map long-press events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", \`callback1 position\`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", \`callback2 position\`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("mapLongClick", \`callback3 position\`);
};
mapEventManager.on("mapLongClick", callback1);
mapEventManager.on("mapLongClick", callback2);
mapEventManager.on("mapLongClick", callback3);

// Cancel only the event response of the **callback1** object. When a **mapLongClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('mapLongClick', callback1);
// Cancel all **mapLongClick** event responses.
mapEventManager.off('mapLongClick');

#### \[h2\]on('myLocationButtonClick')

on(type: 'myLocationButtonClick', callback: Callback<void>): void

Listens for **my-location** icon tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'myLocationButtonClick'**: listens for **my-location** icon tap events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no result. This callback is used to listen for **my-location** icon tap events.

 |

**Example**:

let callback1 = () => {
  console.info("myLocationButtonClick", \`callback1\`);
};
let callback2 = () => {
  console.info("myLocationButtonClick", \`callback2\`);
};
let callback3 = () => {
  console.info("myLocationButtonClick", \`callback3\`);
};
mapEventManager.on("myLocationButtonClick", callback1);
mapEventManager.on("myLocationButtonClick", callback2);
mapEventManager.on("myLocationButtonClick", callback3);

#### \[h2\]off('myLocationButtonClick')

off(type: 'myLocationButtonClick', callback?: Callback<void>): void

Cancels listening for **my-location** icon tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'myLocationButtonClick'**: listens for **my-location** icon tap events.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no result. This callback is used to cancel listening for **my-location** icon tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = () => {
  console.info("myLocationButtonClick", \`callback1\`);
};
let callback2 = () => {
  console.info("myLocationButtonClick", \`callback2\`);
};
let callback3 = () => {
  console.info("myLocationButtonClick", \`callback3\`);
};
mapEventManager.on("myLocationButtonClick", callback1);
mapEventManager.on("myLocationButtonClick", callback2);
mapEventManager.on("myLocationButtonClick", callback3);

// Cancel only the event response of the **callback1** object. When a **myLocationButtonClick** event occurs, **callback2** and **callback3** will be called.
mapEventManager.off('myLocationButtonClick', callback1);
// Cancel all **myLocationButtonClick** event responses.
mapEventManager.off('myLocationButtonClick');

#### \[h2\]on('myLocationClick')

on(type: 'myLocationClick', callback: Callback<mapCommon.LatLng>): void

Listens for **my-location** tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'myLocationClick'**: listens for **my-location** tap events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

Yes

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810). This callback is used to listen for **my-location** tap events.

 |

**Example**:

let callback1 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", \`callback1 position = ${position.longitude}\`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", \`callback2 position = ${position.longitude}\`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", \`callback3 position = ${position.longitude}\`);
};
mapEventManager.on("myLocationClick", callback1);
mapEventManager.on("myLocationClick", callback2);
mapEventManager.on("myLocationClick", callback3);

#### \[h2\]off('myLocationClick')

off(type: 'myLocationClick', callback?: Callback<mapCommon.LatLng>): void

Cancels listening for **my-location** tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'myLocationClick'**: listens for **my-location** tap events.

 |
| 

callback

 | 

Callback<[mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810)\>

 | 

No

 | 

Callback function, which returns [mapCommon.LatLng](../../mapcommon-map-attribute-model/document.md#section20691173773810). This callback is used to cancel listening for **my-location** tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", \`callback1 position\`);
};
let callback2 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", \`callback2 position\`);
};
let callback3 = (position: mapCommon.LatLng) => {
  console.info("myLocationClick", \`callback3 position\`);
};
mapEventManager.on("myLocationClick", callback1);
mapEventManager.on("myLocationClick", callback2);
mapEventManager.on("myLocationClick", callback3);

// Cancel only the event response of the **callback1** object. When a **myLocationClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('myLocationClick', callback1);
// Cancel all **myLocationClick** event responses.
mapEventManager.off('myLocationClick');

#### \[h2\]on('poiClick')

on(type: 'poiClick', callback: Callback<mapCommon.Poi>): void

Listens for POI tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'poiClick'**: listens for POI tap events.

 |
| 

callback

 | 

Callback<[mapCommon.Poi](../../mapcommon-map-attribute-model/document.md#section1155919456273)\>

 | 

Yes

 | 

Callback function, which returns [mapCommon.Poi](../../mapcommon-map-attribute-model/document.md#section1155919456273). This callback is used to listen for POI tap events.

 |

**Example**:

let callback1 = (poi: mapCommon.Poi) => {
  console.info("poiClick", \`callback1 poi = ${poi.id}\`);
};
let callback2 = (poi: mapCommon.Poi) => {
  console.info("poiClick", \`callback2 poi = ${poi.id}\`);
};
let callback3 = (poi: mapCommon.Poi) => {
  console.info("poiClick", \`callback3 poi = ${poi.id}\`);
};
mapEventManager.on("poiClick", callback1);
mapEventManager.on("poiClick", callback2);
mapEventManager.on("poiClick", callback3);

#### \[h2\]off('poiClick')

off(type: 'poiClick', callback?: Callback<mapCommon.Poi>): void

Cancels listening for POI tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'poiClick'**: listens for POI tap events.

 |
| 

callback

 | 

Callback<[mapCommon.Poi](../../mapcommon-map-attribute-model/document.md#section1155919456273)\>

 | 

No

 | 

Callback function, which returns [mapCommon.Poi](../../mapcommon-map-attribute-model/document.md#section1155919456273). This callback is used to cancel listening for POI tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (poi: mapCommon.Poi) => {
  console.info("poiClick", \`callback1 poi\`);
};
let callback2 = (poi: mapCommon.Poi) => {
  console.info("poiClick", \`callback2 poi\`);
};
let callback3 = (poi: mapCommon.Poi) => {
  console.info("poiClick", \`callback3 poi\`);
};
mapEventManager.on("poiClick", callback1);
mapEventManager.on("poiClick", callback2);
mapEventManager.on("poiClick", callback3);

// Cancel only the event response of the **callback1** object. When a **poiClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('poiClick', callback1);
// Cancel all **poiClick** event responses.
mapEventManager.off('poiClick');

#### \[h2\]on('markerClick')

on(type: 'markerClick', callback: Callback<Marker>): void

Listens for Marker tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'markerClick'**: listens for Marker tap events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to listen for Marker tap events.

 |

**Example**:

let callback1 = (marker: map.Marker) => {
  console.info("markerClick", \`callback1 marker = ${marker.getId()}\`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerClick", \`callback2 marker = ${marker.getId()}\`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerClick", \`callback3 marker = ${marker.getId()}\`);
};
mapEventManager.on("markerClick", callback1);
mapEventManager.on("markerClick", callback2);
mapEventManager.on("markerClick", callback3);

#### \[h2\]off('markerClick')

off(type: 'markerClick', callback?: Callback<Marker>): void

Cancels listening for Marker tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'markerClick'**: listens for Marker tap events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

No

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to cancel listening for Marker tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (marker: map.Marker) => {
  console.info("markerClick", \`callback1 marker\`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerClick", \`callback2 marker\`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerClick", \`callback3 marker\`);
};
mapEventManager.on("markerClick", callback1);
mapEventManager.on("markerClick", callback2);
mapEventManager.on("markerClick", callback3);

// Cancel only the event response of the **callback1** object. When a **markerClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('markerClick', callback1);
// Cancel all **markerClick** event responses.
mapEventManager.off('markerClick');

#### \[h2\]on('markerDragStart')

on(type: 'markerDragStart', callback: Callback<Marker>): void

Listens for Marker drag start events. This API can use multiple asynchronous callbacks to return the result.

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

**'markerDragStart'**: listens for Marker drag start events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to listen for Marker drag start events.

 |

**Example**:

let callback1 = (marker: map.Marker) => {
  console.info("markerDragStart", \`callback1 marker = ${marker.getId()}\`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDragStart", \`callback2 marker = ${marker.getId()}\`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDragStart", \`callback3 marker = ${marker.getId()}\`);
};
mapEventManager.on("markerDragStart", callback1);
mapEventManager.on("markerDragStart", callback2);
mapEventManager.on("markerDragStart", callback3);

#### \[h2\]off('markerDragStart')

off(type: 'markerDragStart', callback?: Callback<Marker>): void

Cancels listening for Marker drag start events. This API can use multiple asynchronous callbacks to return the result.

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

**'markerDragStart'**: listens for Marker drag start events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

No

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to cancel listening for Marker drag start events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (marker: map.Marker) => {
  console.info("markerDragStart", \`callback1 marker\`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDragStart", \`callback2 marker\`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDragStart", \`callback3 marker\`);
};
mapEventManager.on("markerDragStart", callback1);
mapEventManager.on("markerDragStart", callback2);
mapEventManager.on("markerDragStart", callback3);

// Cancel only the event response of the **callback1** object. When a **markerDragStart** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('markerDragStart', callback1);
// Cancel all **markerDragStart** event responses.
mapEventManager.off('markerDragStart');

#### \[h2\]on('markerDrag')

on(type: 'markerDrag', callback: Callback<Marker>): void

Listens for Marker drag events. This API can use multiple asynchronous callbacks to return the result.

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

**'markerDrag'**: listens for Marker drag events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to listen for Marker drag events.

 |

**Example**:

let callback1 = (marker: map.Marker) => {
  console.info("markerDrag", \`callback1 marker = ${marker.getId()}\`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDrag", \`callback2 marker = ${marker.getId()}\`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDrag", \`callback3 marker = ${marker.getId()}\`);
};
mapEventManager.on("markerDrag", callback1);
mapEventManager.on("markerDrag", callback2);
mapEventManager.on("markerDrag", callback3);

#### \[h2\]off('markerDrag')

off(type: 'markerDrag', callback?: Callback<Marker>): void

Cancels listening for Marker drag events. This API can use multiple asynchronous callbacks to return the result.

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

**'markerDrag'**: listens for Marker drag events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

No

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to cancel listening for Marker drag events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (marker: map.Marker) => {
  console.info("markerDrag", \`callback1 marker\`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDrag", \`callback2 marker\`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDrag", \`callback3 marker\`);
};
mapEventManager.on("markerDrag", callback1);
mapEventManager.on("markerDrag", callback2);
mapEventManager.on("markerDrag", callback3);

// Cancel only the event response of the **callback1** object. When a **markerDrag** event occurs, **callback2** and **callback3** will be called.
mapEventManager.off('markerDrag', callback1);
// Cancel all **markerDrag** event responses.
mapEventManager.off('markerDrag');

#### \[h2\]on('markerDragEnd')

on(type: 'markerDragEnd', callback: Callback<Marker>): void

Listens for Marker drag end events. This API can use multiple asynchronous callbacks to return the result.

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

**'markerDragEnd'**: listens for Marker drag end events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to listen for Marker drag end events.

 |

**Example**:

let callback1 = (marker: map.Marker) => {
  console.info("markerDragEnd", \`callback1 marker = ${marker.getId()}\`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDragEnd", \`callback2 marker = ${marker.getId()}\`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDragEnd", \`callback3 marker = ${marker.getId()}\`);
};
mapEventManager.on("markerDragEnd", callback1);
mapEventManager.on("markerDragEnd", callback2);
mapEventManager.on("markerDragEnd", callback3);

#### \[h2\]off('markerDragEnd')

off(type: 'markerDragEnd', callback?: Callback<Marker>): void

Cancels listening for Marker drag end events. This API can use multiple asynchronous callbacks to return the result.

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

**'markerDragEnd'**: listens for Marker drag end events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

No

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to cancel listening for Marker drag end events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (marker: map.Marker) => {
  console.info("markerDragEnd", \`callback1 marker\`);
};
let callback2 = (marker: map.Marker) => {
  console.info("markerDragEnd", \`callback2 marker\`);
};
let callback3 = (marker: map.Marker) => {
  console.info("markerDragEnd", \`callback3 marker\`);
};
mapEventManager.on("markerDragEnd", callback1);
mapEventManager.on("markerDragEnd", callback2);
mapEventManager.on("markerDragEnd", callback3);

// Cancel only the event response of the **callback1** object. When a **markerDragEnd** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('markerDragEnd', callback1);
// Cancel all **markerDragEnd** event responses.
mapEventManager.off('markerDragEnd');

#### \[h2\]on('circleClick')

on(type: 'circleClick', callback: Callback<MapCircle>): void

Listens for MapCircle tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'circleClick'**: listens for MapCircle tap events.

 |
| 

callback

 | 

Callback<[MapCircle](../mapcircle/document.md)\>

 | 

Yes

 | 

Callback function, which returns [MapCircle](../mapcircle/document.md). This callback is used to listen for MapCircle tap events.

 |

**Example**:

let callback1 = (circle: map.MapCircle) => {
  console.info("circleClick", \`callback1 circle = ${circle.getId()}\`);
};
let callback2 = (circle: map.MapCircle) => {
  console.info("circleClick", \`callback2 circle = ${circle.getId()}\`);
};
let callback3 = (circle: map.MapCircle) => {
  console.info("circleClick", \`callback3 circle = ${circle.getId()}\`);
};
mapEventManager.on("circleClick", callback1);
mapEventManager.on("circleClick", callback2);
mapEventManager.on("circleClick", callback3);

#### \[h2\]off('circleClick')

off(type: 'circleClick', callback?: Callback<MapCircle>): void

Cancels listening for MapCircle tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'circleClick'**: listens for MapCircle tap events.

 |
| 

callback

 | 

Callback<[MapCircle](../mapcircle/document.md)\>

 | 

No

 | 

Callback function, which returns [MapCircle](../mapcircle/document.md). This callback is used to cancel listening for MapCircle tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (circle: map.MapCircle) => {
  console.info("circleClick", \`callback1 circle\`);
};
let callback2 = (circle: map.MapCircle) => {
  console.info("circleClick", \`callback2 circle\`);
};
let callback3 = (circle: map.MapCircle) => {
  console.info("circleClick", \`callback3 circle\`);
};
mapEventManager.on("circleClick", callback1);
mapEventManager.on("circleClick", callback2);
mapEventManager.on("circleClick", callback3);

// Cancel only the event response of the **callback1** object. When a **circleClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('circleClick', callback1);
// Cancel all **circleClick** event responses.
mapEventManager.off('circleClick');

#### \[h2\]on('polylineClick')

on(type: 'polylineClick', callback: Callback<MapPolyline>): void

Listens for MapPolyline tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'polylineClick'**: listens for MapPolyline tap events.

 |
| 

callback

 | 

Callback<[MapPolyline](../mappolyline/document.md)\>

 | 

Yes

 | 

Callback function, which returns [MapPolyline](../mappolyline/document.md). This callback is used to listen for MapPolyline tap events.

 |

**Example**:

let callback1 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", \`callback1 polyline = ${polyline.getId()}\`);
};
let callback2 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", \`callback2 polyline = ${polyline.getId()}\`);
};
let callback3 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", \`callback3 polyline = ${polyline.getId()}\`);
};
mapEventManager.on("polylineClick", callback1);
mapEventManager.on("polylineClick", callback2);
mapEventManager.on("polylineClick", callback3);

#### \[h2\]off('polylineClick')

off(type: 'polylineClick', callback?: Callback<MapPolyline>): void

Cancels listening for MapPolyline tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'polylineClick'**: listens for MapPolyline tap events.

 |
| 

callback

 | 

Callback<[MapPolyline](../mappolyline/document.md)\>

 | 

No

 | 

Callback function, which returns [MapPolyline](../mappolyline/document.md). This callback is used to cancel listening for MapPolyline tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", \`callback1 polyline\`);
};
let callback2 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", \`callback2 polyline\`);
};
let callback3 = (polyline: map.MapPolyline) => {
  console.info("polylineClick", \`callback3 polyline\`);
};
mapEventManager.on("polylineClick", callback1);
mapEventManager.on("polylineClick", callback2);
mapEventManager.on("polylineClick", callback3);

// Cancel only the event response of the **callback1** object. When a **polylineClick** event occurs, **callback2** and **callback3** will be called.
mapEventManager.off('polylineClick', callback1);
// Cancel all **polylineClick** event responses.
mapEventManager.off('polylineClick');

#### \[h2\]on('polygonClick')

on(type: 'polygonClick', callback: Callback<MapPolygon>): void

Listens for MapPolygon tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'polygonClick'**: listens for MapPolygon tap events.

 |
| 

callback

 | 

Callback<[MapPolygon](../mappolygon/document.md)\>

 | 

Yes

 | 

Callback function, which returns [MapPolygon](../mappolygon/document.md). This callback is used to listen for MapPolygon tap events.

 |

**Example**:

let callback1 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", \`callback1 polygon = ${polygon.getId()}\`);
};
let callback2 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", \`callback2 polygon = ${polygon.getId()}\`);
};
let callback3 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", \`callback3 polygon = ${polygon.getId()}\`);
};
mapEventManager.on("polygonClick", callback1);
mapEventManager.on("polygonClick", callback2);
mapEventManager.on("polygonClick", callback3);

#### \[h2\]off('polygonClick')

off(type: 'polygonClick', callback?: Callback<MapPolygon>): void

Cancels listening for MapPolygon tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'polygonClick'**: listens for MapPolygon tap events.

 |
| 

callback

 | 

Callback<[MapPolygon](../mappolygon/document.md)\>

 | 

No

 | 

Callback function, which returns [MapPolygon](../mappolygon/document.md). This callback is used to cancel listening for MapPolygon tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", \`callback1 polygon\`);
};
let callback2 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", \`callback2 polygon\`);
};
let callback3 = (polygon: map.MapPolygon) => {
  console.info("polygonClick", \`callback3 polygon\`);
};
mapEventManager.on("polygonClick", callback1);
mapEventManager.on("polygonClick", callback2);
mapEventManager.on("polygonClick", callback3);

// Cancel only the event response of the **callback1** object. When a **polygonClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('polygonClick', callback1);
// Cancel all **polygonClick** event responses.
mapEventManager.off('polygonClick');

#### \[h2\]on('infoWindowClick')

on(type: 'infoWindowClick', callback: Callback<Marker>): void

Listens for information window tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'infoWindowClick'**: listens for information window tap events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to listen for information window tap events.

 |

**Example**:

let callback1 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", \`callback1 infoWindow = ${infoWindow.getId()}\`);
};
let callback2 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", \`callback2 infoWindow = ${infoWindow.getId()}\`);
};
let callback3 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", \`callback3 infoWindow = ${infoWindow.getId()}\`);
};
mapEventManager.on("infoWindowClick", callback1);
mapEventManager.on("infoWindowClick", callback2);
mapEventManager.on("infoWindowClick", callback3);

#### \[h2\]off('infoWindowClick')

off(type: 'infoWindowClick', callback?: Callback<[Marker](../marker/document.md)\>): void

Cancels listening for information window tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'infoWindowClick'**: listens for information window tap events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

No

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to cancel listening for information window tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", \`callback1 infoWindow\`);
};
let callback2 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", \`callback2 infoWindow\`);
};
let callback3 = (infoWindow: map.Marker) => {
  console.info("infoWindowClick", \`callback3 infoWindow\`);
};
mapEventManager.on("infoWindowClick", callback1);
mapEventManager.on("infoWindowClick", callback2);
mapEventManager.on("infoWindowClick", callback3);

// Cancel only the event response of the **callback1** object. When an **infoWindowClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('infoWindowClick', callback1);
// Cancel all **infoWindowClick** event responses.
mapEventManager.off('infoWindowClick');

#### \[h2\]on('infoWindowClose')

on(type: 'infoWindowClose', callback: Callback<Marker>): void

Listens for information window close events. This API can use multiple asynchronous callbacks to return the result.

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

**'infoWindowClose'**: listens for information window close events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to listen for information window close events.

 |

**Example**:

let callback1 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", \`callback1 infoWindowClose = ${infoWindow.getId()}\`);
};
let callback2 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", \`callback2 infoWindowClose = ${infoWindow.getId()}\`);
};
let callback3 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", \`callback3 infoWindowClose = ${infoWindow.getId()}\`);
};
mapEventManager.on("infoWindowClose", callback1);
mapEventManager.on("infoWindowClose", callback2);
mapEventManager.on("infoWindowClose", callback3);

#### \[h2\]off('infoWindowClose')

off(type: 'infoWindowClose', callback?: Callback<Marker>): void

Cancels listening for information window close events. This API can use multiple asynchronous callbacks to return the result.

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

**'infoWindowClose'**: listens for information window close events.

 |
| 

callback

 | 

Callback<[Marker](../marker/document.md)\>

 | 

No

 | 

Callback function, which returns [Marker](../marker/document.md). This callback is used to cancel listening for information window close events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", \`callback1 infoWindowClose\`);
};
let callback2 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", \`callback2 infoWindowClose\`);
};
let callback3 = (infoWindow: map.Marker) => {
  console.info("infoWindowClose", \`callback3 infoWindowClose\`);
};
mapEventManager.on("infoWindowClose", callback1);
mapEventManager.on("infoWindowClose", callback2);
mapEventManager.on("infoWindowClose", callback3);

// Cancel only the event response of the **callback1** object. When an **infoWindowClose** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('infoWindowClose', callback1);
// Cancel all **infoWindowClose** event responses.
mapEventManager.off('infoWindowClose');

#### \[h2\]on('pointAnnotationClick')

on(type: 'pointAnnotationClick', callback: Callback<PointAnnotation>): void

Listens for PointAnnotation tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'pointAnnotationClick'**: listens for PointAnnotation tap events.

 |
| 

callback

 | 

Callback<[PointAnnotation](../pointannotation/document.md)\>

 | 

Yes

 | 

Callback function, which returns [PointAnnotation](../pointannotation/document.md). This callback is used to listen for PointAnnotation tap events.

 |

**Example**:

let callback1 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", \`callback1 pointAnnotation = ${pointAnnotation.getId()}\`);
};
let callback2 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", \`callback2 pointAnnotation = ${pointAnnotation.getId()}\`);
};
let callback3 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", \`callback3 pointAnnotation = ${pointAnnotation.getId()}\`);
};
mapEventManager.on("pointAnnotationClick", callback1);
mapEventManager.on("pointAnnotationClick", callback2);
mapEventManager.on("pointAnnotationClick", callback3);

#### \[h2\]off('pointAnnotationClick')

off(type: 'pointAnnotationClick', callback?: Callback<PointAnnotation>): void

Cancels listening for PointAnnotation tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'pointAnnotationClick'**: listens for PointAnnotation tap events.

 |
| 

callback

 | 

Callback<[PointAnnotation](../pointannotation/document.md)\>

 | 

No

 | 

Callback function, which returns [PointAnnotation](../pointannotation/document.md). This callback is used to cancel listening for PointAnnotation tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", \`callback1 pointAnnotation\`);
};
let callback2 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", \`callback2 pointAnnotation\`);
};
let callback3 = (pointAnnotation: map.PointAnnotation) => {
  console.info("pointAnnotationClick", \`callback3 pointAnnotation\`);
};
mapEventManager.on("pointAnnotationClick", callback1);
mapEventManager.on("pointAnnotationClick", callback2);
mapEventManager.on("pointAnnotationClick", callback3);

// Cancel only the event response of the **callback1** object. When a **pointAnnotationClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('pointAnnotationClick', callback1);
// Cancel all **pointAnnotationClick** event responses.
mapEventManager.off('pointAnnotationClick');

#### \[h2\]on('bubbleClick')

on(type: 'bubbleClick', callback: Callback<Bubble>): void

Listens for Bubble tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'bubbleClick'**: listens for Bubble tap events.

 |
| 

callback

 | 

Callback<[Bubble](../bubble/document.md)\>

 | 

Yes

 | 

Callback function, which returns [Bubble](../bubble/document.md). This callback is used to listen for Bubble tap events.

 |

**Example**:

let callback1 = (bubble: map.Bubble) => {
  console.info("bubbleClick", \`callback1 bubble = ${bubble.getId()}\`);
};
let callback2 = (bubble: map.Bubble) => {
  console.info("bubbleClick", \`callback2 bubble = ${bubble.getId()}\`);
};
let callback3 = (bubble: map.Bubble) => {
  console.info("bubbleClick", \`callback3 bubble = ${bubble.getId()}\`);
};
mapEventManager.on("bubbleClick", callback1);
mapEventManager.on("bubbleClick", callback2);
mapEventManager.on("bubbleClick", callback3);

#### \[h2\]off('bubbleClick')

off(type: 'bubbleClick', callback?: Callback<Bubble>): void

Cancels listening for Bubble tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'bubbleClick'**: listens for Bubble tap events.

 |
| 

callback

 | 

Callback<[Bubble](../bubble/document.md)\>

 | 

No

 | 

Callback function, which returns [Bubble](../bubble/document.md). This callback is used to cancel listening for Bubble tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (bubble: map.Bubble) => {
  console.info("bubbleClick", \`callback1 bubble\`);
};
let callback2 = (bubble: map.Bubble) => {
  console.info("bubbleClick", \`callback2 bubble\`);
};
let callback3 = (bubble: map.Bubble) => {
  console.info("bubbleClick", \`callback3 bubble\`);
};
mapEventManager.on("bubbleClick", callback1);
mapEventManager.on("bubbleClick", callback2);
mapEventManager.on("bubbleClick", callback3);

// Cancel only the event response of the **callback1** object. When a **bubbleClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('bubbleClick', callback1);
// Cancel all **bubbleClick** event responses.
mapEventManager.off('bubbleClick');

#### \[h2\]on('imageOverlayClick')

on(type: 'imageOverlayClick', callback: Callback<ImageOverlay>): void

Listens for ImageOverlay tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'imageOverlayClick'**: listens for ImageOverlay tap events.

 |
| 

callback

 | 

Callback<[ImageOverlay](../imageoverlay/document.md)\>

 | 

Yes

 | 

Callback function, which returns [ImageOverlay](../imageoverlay/document.md). This callback is used to listen for ImageOverlay tap events.

 |

**Example**:

let callback1 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", \`callback1 imageOverlay = ${imageOverlay.getId()}\`);
};
let callback2 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", \`callback2 imageOverlay = ${imageOverlay.getId()}\`);
};
let callback3 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", \`callback3 imageOverlay = ${imageOverlay.getId()}\`);
};
mapEventManager.on("imageOverlayClick", callback1);
mapEventManager.on("imageOverlayClick", callback2);
mapEventManager.on("imageOverlayClick", callback3);

#### \[h2\]off('imageOverlayClick')

off(type: 'imageOverlayClick', callback?: Callback<ImageOverlay>): void

Cancels listening for ImageOverlay tap events. This API can use multiple asynchronous callbacks to return the result.

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

**'imageOverlayClick'**: listens for ImageOverlay tap events.

 |
| 

callback

 | 

Callback<[ImageOverlay](../imageoverlay/document.md)\>

 | 

No

 | 

Callback function, which returns [ImageOverlay](../imageoverlay/document.md). This callback is used to cancel listening for ImageOverlay tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

let callback1 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", \`callback1 imageOverlay\`);
};
let callback2 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", \`callback2 imageOverlay\`);
};
let callback3 = (imageOverlay: map.ImageOverlay) => {
  console.info("imageOverlayClick", \`callback3 imageOverlay\`);
};
mapEventManager.on("imageOverlayClick", callback1);
mapEventManager.on("imageOverlayClick", callback2);
mapEventManager.on("imageOverlayClick", callback3);

// Cancel only the event response of the **callback1** object. When an **imageOverlayClick** event occurs, **callback2** and **callback3** will be called. 
mapEventManager.off('imageOverlayClick', callback1);
// Cancel all **imageOverlayClick** event responses.
mapEventManager.off('imageOverlayClick');

#### \[h2\]on('error')

on(type: 'error', callback: ErrorCallback): void

Listens for error events. This API can use multiple asynchronous callbacks to return the result.

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

**'error'**: listens for error events.

 |
| 

callback

 | 

[ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)

 | 

Yes

 | 

Callback function, which returns [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback). This callback is used to listen for error events.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let callback1 = (error: BusinessError) => {
  console.error("error", \`callback1 code: ${error.code}, message: ${error.message}\`);
};
let callback2 = (error: BusinessError) => {
  console.error("error", \`callback2 code: ${error.code}, message: ${error.message}\`);
};
let callback3 = (error: BusinessError) => {
  console.error("error", \`callback3 code: ${error.code}, message: ${error.message}\`);
};
mapEventManager.on("error", callback1);
mapEventManager.on("error", callback2);
mapEventManager.on("error", callback3);

#### \[h2\]off('error')

off(type: 'error', callback?: ErrorCallback): void

Cancels listening for error events. This API can use multiple asynchronous callbacks to return the result.

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

**'error'**: listens for error events.

 |
| 

callback

 | 

[ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback)

 | 

No

 | 

Callback function, which returns [ErrorCallback](../../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#errorcallback). This callback is used to cancel listening for error events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';

let callback1 = (error: BusinessError) => {
  console.info("error", \`callback1\`);
};
let callback2 = (error: BusinessError) => {
  console.info("error", \`callback2\`);
};
let callback3 = (error: BusinessError) => {
  console.info("error", \`callback3\`);
};
mapEventManager.on("error", callback1);
mapEventManager.on("error", callback2);
mapEventManager.on("error", callback3);

// Cancel only the event response of the **callback1** object. When an **error** event occurs, **callback2** and **callback3** will be called.
mapEventManager.off('error', callback1);
// Cancel all **error** event responses.
mapEventManager.off('error');

#### \[h2\]on('indoorMapEnter')

on(type: 'indoorMapEnter', callback: Callback<IndoorMapInfo>): void

Listens for indoor map access events.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.1.1(19)

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

**'indoorMapEnter'**: listens for indoor map access events.

 |
| 

callback

 | 

Callback<[IndoorMapInfo](../indoormapinfo/document.md)\>

 | 

Yes

 | 

Callback function, which returns [IndoorMapInfo](../indoormapinfo/document.md). This callback is used to listen for indoor map access events.

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

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let callback = (indoorMapInfo: map.IndoorMapInfo) => {
  console.info("indoorMapEnter", \`callback indoorMapInfo\`);
};
mapEventManager.on("indoorMapEnter", callback);

#### \[h2\]off('indoorMapEnter')

off(type: 'indoorMapEnter', callback?: Callback<IndoorMapInfo>): void

Cancels listening for indoor map access events.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.1.1(19)

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

**'indoorMapEnter'**: listens for indoor map access events.

 |
| 

callback

 | 

Callback<[IndoorMapInfo](../indoormapinfo/document.md)\>

 | 

No

 | 

Callback function, which returns [IndoorMapInfo](../indoormapinfo/document.md). This callback is used to cancel listening for indoor map access events.

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

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let callback = (indoorMapInfo: map.IndoorMapInfo) => {
  console.info("indoorMapEnter", \`callback\`);
};
mapEventManager.on("indoorMapEnter", callback);

// Cancel the event response of the **callback** object.
mapEventManager.off('indoorMapEnter', callback);

#### \[h2\]on('indoorMapExit')

on(type: 'indoorMapExit', callback: Callback<void>): void

Listens for indoor map exit events.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.1.1(19)

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

**'indoorMapExit'**: listens for indoor map exit events.

 |
| 

callback

 | 

Callback<void>

 | 

Yes

 | 

Callback function that returns no result. This callback is used to listen for indoor map exit events.

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

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let callback = () => {
  console.info("indoorMapExit", \`callback\`);
};
mapEventManager.on("indoorMapExit", callback);

#### \[h2\]off('indoorMapExit')

off(type: 'indoorMapExit', callback?: Callback<void>): void

Cancels listening for indoor map exit events.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.1.1(19)

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

**'indoorMapExit'**: listens for indoor map exit events.

 |
| 

callback

 | 

Callback<void>

 | 

No

 | 

Callback function that returns no result. This callback is used to cancel listening for indoor map exit events.

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

801

 | 

Capability not supported. Failed to call the API due to limited device capabilities.

 |

**Example**:

let callback = () => {
  console.info("indoorMapExit", \`callback\`);
};
mapEventManager.on("indoorMapExit", callback);

// Cancel the event response of the **callback** object.
mapEventManager.off('indoorMapExit', callback);

#### \[h2\]on('massPointOverlayClick')

on(type: 'massPointOverlayClick', callback: MassPointOverlayCallback): void

Listens for MassPointOverlay tap events.

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

type

 | 

string

 | 

Yes

 | 

**'massPointOverlayClick'**: listens for MassPointOverlay tap events.

 |
| 

callback

 | 

[MassPointOverlayCallback](../masspointoverlaycallback/document.md)

 | 

Yes

 | 

Callback function that returns no result. This callback is used to listen for MassPointOverlay tap events.

 |

**Example**:

// Initialize the listening event manager of the map component.
let mapEventManager = this.mapController.getEventManager();
let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
  console.info(\`overlayId:${overlay.getId()},item :${JSON.stringify(item)}\`);
}
// Start listening for MassPointOverlay tap events.
mapEventManager.on('massPointOverlayClick', massCallback);

#### \[h2\]off('massPointOverlayClick')

off(type: 'massPointOverlayClick', callback?: MassPointOverlayCallback): void

Cancels listening for MassPointOverlay tap events.

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

type

 | 

string

 | 

Yes

 | 

**'massPointOverlayClick'**: listens for MassPointOverlay tap events.

 |
| 

callback

 | 

[MassPointOverlayCallback](../masspointoverlaycallback/document.md)

 | 

No

 | 

Callback function that returns no result. This callback is used to cancel listening for MassPointOverlay tap events.

-   If **callback** is null, cancel all callbacks.
-   If **callback** is not null, cancel the specified callback.

 |

**Example**:

// Initialize the listening event manager of the map component.
let mapEventManager = this.mapController.getEventManager();
let massCallback: map.MassPointOverlayCallback = (overlay, item) => {
  console.info(\`overlayId:${overlay.getId()},item :${JSON.stringify(item)}\`);
}
// Start listening for MassPointOverlay tap events.
mapEventManager.on('massPointOverlayClick', massCallback);
// Stop specific listening for MassPointOverlay tap events by passing the corresponding callback.
mapEventManager.off('massPointOverlayClick', massCallback);
// Stop all listening for MassPointOverlay tap events. No callback needs to be passed.
mapEventManager.off('massPointOverlayClick');
