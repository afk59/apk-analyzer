# BaseOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### BaseOverlay

Base class of overlays. Overlays such as [Marker](../marker/document.md), [MapPolyline](../mappolyline/document.md), [MapPolygon](../mappolygon/document.md), [MapCircle](../mapcircle/document.md), [MapArc](../maparc/document.md), [ImageOverlay](../imageoverlay/document.md), and [BasePriorityOverlay](../basepriorityoverlay/document.md) inherit from this base class.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

| 
Return Type

 | 

Method

 |
| :-- | :-- |
| 

string

 | 

[getId](#section7073612370)()

Obtains the ID of an overlay.

 |
| 

number

 | 

[getZIndex](#section15225105915396)()

Obtains the z-index of an overlay.

 |
| 

Object

 | 

[getTag](#section19301111714013)()

Obtains the tag of an overlay.

 |
| 

boolean

 | 

[isVisible](#section186444914423)()

Checks whether an overlay is visible.

 |
| 

void

 | 

[remove](#section39155506439)()

Removes an overlay from the map.

 |
| 

void

 | 

[setZIndex](#section394129124411)(zIndex: number)

Sets the z-index of an overlay.

 |
| 

void

 | 

[setTag](#section15199510114518)(tag: Object)

Sets the tag of an overlay.

 |
| 

void

 | 

[setVisible](#section132033103450)(visible: boolean)

Sets whether an overlay is visible.

 |

#### \[h2\]getId

getId(): string

Obtains the ID of an overlay.

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

string

 | 

ID of an overlay.

 |

**Example**:

// Use a Marker as an example.
let markerOptions: mapCommon.MarkerOptions = {
  position: {
    latitude: 39.9,
    longitude: 116.4
  }
};
let marker: map.Marker = await this.mapController.addMarker(markerOptions);
let id: string = marker.getId();

#### \[h2\]getZIndex

getZIndex(): number

Obtains the z-index of an overlay.

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

number

 | 

Z-index of an overlay. The z-index indicates the stacking order of an overlay. An overlay with a larger z-index covers that with a smaller z-index. Overlays with the same z-index cover each other by the order in which they are added. If the z-index is not set during overlay initialization, the default value **0** will be used. If an invalid value is passed, the default value will be used.

 |

**Example**:

// Use a Marker as an example.
let zIndex: number = marker.getZIndex();

#### \[h2\]getTag

getTag(): Object

Obtains the tag of an overlay.

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

Object

 | 

Tag of an overlay.

 |

**Example**:

// Use a Marker as an example.
let tag: Object = marker.getTag();

#### \[h2\]isVisible

isVisible(): boolean

Checks whether an overlay is visible.

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

boolean

 | 

Indicates whether an overlay is visible.

-   **true**: yes
-   **false**: no

 |

**Example**:

// Use a Marker as an example.
let isVisible: boolean = marker.isVisible();

#### \[h2\]remove

remove(): void

Removes an overlay from the map.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

**Example**:

// Use a Marker as an example.
marker.remove();

#### \[h2\]setZIndex

setZIndex(zIndex: number): void

Sets the z-index of an overlay.

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

zIndex

 | 

number

 | 

Yes

 | 

Z-index of an overlay. The z-index indicates the stacking order of an overlay. An overlay with a larger z-index covers that with a smaller z-index. Overlays with the same z-index cover each other by the order in which they are added. If the z-index is not set during overlay initialization, the default value **0** will be used. If an invalid value is passed, the default value will be used.

 |

**Example**:

// Use a Marker as an example.
marker.setZIndex(3);

#### \[h2\]setTag

setTag(tag: Object): void

Sets the tag of an overlay. The tag can be any object. If you change the parameter value to **null**, the original tag will be cleared. When you no longer need a tag, call **setTag(null)** or **setTag(undefined)** to clear it to prevent memory leakage from occurring on the app.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Map.Core

**Start version**: 4.1.0(11)

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

tag

 | 

Object

 | 

Yes

 | 

Tag of an overlay.

 |

**Example**:

// Use a Marker as an example.
let tag = "tag-1";
marker.setTag(tag);

#### \[h2\]setVisible

setVisible(visible: boolean): void

Sets whether an overlay is visible. By default, an overlay is visible.

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

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether an overlay is visible.

-   **true**: yes
-   **false**: no

The default value is **true**.

 |

**Example**:

// Use a Marker as an example.
marker.setVisible(true);
