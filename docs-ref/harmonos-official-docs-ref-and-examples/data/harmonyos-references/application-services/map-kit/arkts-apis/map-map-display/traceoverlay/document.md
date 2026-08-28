# TraceOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### TraceOverlay

TraceOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

// Parameters of Marker 1.
let markerOptions1: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.99227173519985,
    longitude: 118.7622219990476
  },
  // The icon must be stored in the **resources/base/media** directory.
  icon: $r("app.media.track\_setting\_sport\_map\_marker\_22"),
  anchorU: 0.5,
  anchorV: 1,
  visible: true
};
// Add Marker 1.
let markerBoy1 = await this.mapController.addMarker(markerOptions1);
let boyImages1: map.PlayImageAnimation = new map.PlayImageAnimation();
boyImages1.setDuration(1000);
let resourceArray: Array<Resource> = new Array();
resourceArray.push($r("app.media.side\_0"));
resourceArray.push($r("app.media.side\_1"));
resourceArray.push($r("app.media.side\_2"));
resourceArray.push($r("app.media.side\_3"));
resourceArray.push($r("app.media.side\_4"));
resourceArray.push($r("app.media.side\_5"));
resourceArray.push($r("app.media.side\_6"));
resourceArray.push($r("app.media.side\_7"));
resourceArray.push($r("app.media.side\_8"));
resourceArray.push($r("app.media.side\_9"));
resourceArray.push($r("app.media.side\_10"));
resourceArray.push($r("app.media.side\_11"));
resourceArray.push($r("app.media.side\_12"));
resourceArray.push($r("app.media.side\_13"));
resourceArray.push($r("app.media.side\_14"));
resourceArray.push($r("app.media.side\_15"));
resourceArray.push($r("app.media.side\_16"));
resourceArray.push($r("app.media.side\_17"));
resourceArray.push($r("app.media.side\_18"));
resourceArray.push($r("app.media.side\_19"));
resourceArray.push($r("app.media.side\_20"));
await boyImages1.addImages(resourceArray);
boyImages1.setRepeatCount(-1);

// Add an animation for Marker 1.
markerBoy1.setAnimation(boyImages1);
markerBoy1.startAnimation();

// Parameters of Marker 2.
let markerOptions2: mapCommon.MarkerOptions = {
  position: {
    latitude: 31.99227173519985,
    longitude: 118.7622219990476
  },
  // The icon must be stored in the **resources/base/media** directory.
  icon: $r("app.media.track\_setting\_sport\_map\_marker\_22"),
  anchorU: 0.5,
  anchorV: 1,
  visible: false
};
// Add Marker 2.
let markerBoy2 = await this.mapController.addMarker(markerOptions2);
let boyImages2: map.PlayImageAnimation = new map.PlayImageAnimation();
boyImages2.setDuration(1000);
let resourceArray2: Array<Resource> = new Array();
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_000"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_001"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_002"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_003"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_004"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_005"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_006"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_007"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_008"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_009"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_010"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_011"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_012"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_013"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_014"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_015"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_016"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_017"));
resourceArray2.push($r("app.media.behavior\_front\_cycling\_boy\_018"));
await boyImages2.addImages(resourceArray2);
boyImages2.setRepeatCount(-1);
// Add an animation for Marker 2.
markerBoy2.setAnimation(boyImages2);
markerBoy2.startAnimation();

let points: Array<mapCommon.LatLng> = new Array();
points.push({ latitude: 31.99685233070878, longitude: 118.75846023442728 });
points.push({ latitude: 31.99671325810786, longitude: 118.75846738985165 });
points.push({ latitude: 31.99659191076709, longitude: 118.7585347621686 });
points.push({ latitude: 31.99648202537233, longitude: 118.7586266510386 });
points.push({ latitude: 31.99637707201552, longitude: 118.75872004590596 });
points.push({ latitude: 31.996278207010903, longitude: 118.75880449946251 });
points.push({ latitude: 31.996187481969695, longitude: 118.7588781960278 });
points.push({ latitude: 31.996092248919354, longitude: 118.75895330554488 });
points.push({ latitude: 31.995962740450565, longitude: 118.75904721407304 });
points.push({ latitude: 31.995792921394, longitude: 118.75916904998051 });
points.push({ latitude: 31.995601885713416, longitude: 118.7593235241019 });
points.push({ latitude: 31.995398221178277, longitude: 118.75949998588176 });
points.push({ latitude: 31.995185902197715, longitude: 118.7596871082939 });
points.push({ latitude: 31.994983473052656, longitude: 118.75987334062296 });
points.push({ latitude: 31.99482433699269, longitude: 118.76002095184032 });
points.push({ latitude: 31.994709073721708, longitude: 118.76012902920532 });
points.push({ latitude: 31.99460732100702, longitude: 118.76023892576234 });
points.push({ latitude: 31.99449284962087, longitude: 118.7603694232856 });
points.push({ latitude: 31.99435358179254, longitude: 118.76053622438056 });
points.push({ latitude: 31.99420771148339, longitude: 118.76072790126692 });
points.push({ latitude: 31.994075194901523, longitude: 118.7609100960977 });
points.push({ latitude: 31.993952686158877, longitude: 118.7610741329013 });
points.push({ latitude: 31.993840180644217, longitude: 118.7612193418965 });
points.push({ latitude: 31.993733787150244, longitude: 118.76135383115654 });
points.push({ latitude: 31.993617206525155, longitude: 118.76150529647698 });

// Input parameters of the TraceOverlay.
let traceOptions: mapCommon.TraceOverlayParams = {
  // Trajectory points.
  points: points,
  // TraceOverlay animation duration.
  animationDuration: 5000,
  // Whether the camera follows the animation path.
  isMapMoving: true,
  // TraceOverlay color.
  color: 0xAAFFAA00,
  // TraceOverlay width.
  width: 20,
  // TraceOverlay animation callback (using the trajectory point index).
  animationCallback: (pointIndex) => {
    // Change to cycling.
    if (pointIndex === 10) {
      markerBoy1.setVisible(false);
      markerBoy2.setVisible(true);
    }
  }
};
let markers: Array<map.Marker> = new Array();
markers.push(markerBoy1, markerBoy2);
// Add a trajectory point animation.
let traceOverlay: map.TraceOverlay = await this.mapController.addTraceOverlay(traceOptions, markers);

#### \[h2\]getId

getId(): string

Obtains the ID of a TraceOverlay.

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

string

 | 

TraceOverlay ID.

 |

**Example**:

let id: string = traceOverlay.getId();

#### \[h2\]remove

remove(): void

Deletes a TraceOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

traceOverlay.remove();

#### \[h2\]pause

pause(): void

Pauses TraceOverlay playback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

traceOverlay.pause();

#### \[h2\]resume

resume(): void

Resumes TraceOverlay playback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.0(12)

**Example**:

traceOverlay.resume();
