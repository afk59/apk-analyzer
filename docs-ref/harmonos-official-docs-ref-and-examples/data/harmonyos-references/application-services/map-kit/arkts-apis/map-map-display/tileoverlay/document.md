# TileOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### TileOverlay

TileOverlay, which inherits from [BaseOverlay](../baseoverlay/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/rsjathQ2QKuLGR1MShfS-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062513Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1D41841A4B8CE8FCFEFAED05FC2662BD48B4DA90955CCE349C620DAAF36F687)

It is recommended that a maximum of 10 TileOverlays be added and the tile resolution be 256 x 256.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Example**:

let params: mapCommon.TileOverlayParams = {
  // Set the URL of the TileOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
  tileUrl: "https://xxx/xxx?x={x}&y={y}&z={z}",
  transparency: 0,
  fadeIn: false
};
let tileOverlay: map.TileOverlay = this.mapController?.addTileOverlay(params);

#### \[h2\]clearTileCache

clearTileCache(): void

Clears the cache of a TileOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

**Example**:

tileOverlay.clearTileCache();

#### \[h2\]setFadeIn

setFadeIn(fadeIn: boolean): void

Sets whether to enable TileOverlay fade-in.

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

fadeIn

 | 

boolean

 | 

Yes

 | 

Indicates whether to enable TileOverlay fade-in.

-   **true**: yes
-   **false**: no

 |

**Example**:

tileOverlay.setFadeIn(false);

#### \[h2\]setTransparency

setTransparency(transparency: number): void

Sets the transparency of a TileOverlay.

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

transparency

 | 

number

 | 

Yes

 | 

Transparency of a TileOverlay. The value ranges from 0 to 1. The value **1** indicates completely transparent, and the value **0** indicates completely opaque.

 |

**Example**:

tileOverlay.setTransparency(0.5);

#### \[h2\]getFadeIn

getFadeIn(): boolean

Checks whether TileOverlay fade-in is enabled.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

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

Indicates whether TileOverlay fade-in is enabled.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isFadeIn: boolean = tileOverlay.getFadeIn();

#### \[h2\]getTransparency

getTransparency(): number

Obtains the transparency of a TileOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.3(15).

**System capability**: SystemCapability.Map.Core

**Start version**: 5.0.3(15)

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

Transparency of a TileOverlay.

 |

**Example**:

let transparency: number = tileOverlay.getTransparency();

#### \[h2\]clearDiskCache

clearDiskCache(): Promise<void>

Clears the disk cache, which will also clear the memory cache. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

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

tileOverlay.clearDiskCache();
