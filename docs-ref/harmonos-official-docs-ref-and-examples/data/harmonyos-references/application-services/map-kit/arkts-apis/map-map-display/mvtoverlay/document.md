# MvtOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MvtOverlay

MvtOverlay object. An instance of the MvtOverlay type will be returned when the [addMvtOverlay](../mapcomponentcontroller/document.md#section10177450104116) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called. This API inherits from [BaseOverlay](../baseoverlay/document.md).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.0(20)

**Example**:

let params: mapCommon.MvtOverlayParams = {
  source: {
    // Set the URL of the MvtOverlay, which must start with **http** or **https** and contain placeholders {x}, {y}, and {z}.
    tileUrl: 'http://xxx/tiles/{z}/{x}/{y}.pbf',
    minZoom: 2,
    maxZoom: 15
  },
  layers: \[{
    id: 'layer-map',
    type: mapCommon.MvtLayerType.FILL,
    // MvtOverlay name.
    sourceLayer: 'XX',
    paint: {
      fillColor: {
        operator: mapCommon.Operator.GET,
        args: 'fill'
      },
      fillOpacity: {
        operator: mapCommon.Operator.GET,
        args: 'fill-opacity'
      }
    }
  }\]
};
let mvtOverlay = this.mapController?.addMvtOverlay(params);

#### \[h2\]addLayers

addLayers(layers: mapCommon.MvtLayer\[\]): void

Adds vector layers.

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

layers

 | 

[mapCommon.MvtLayer](../../mapcommon-map-attribute-model/document.md#section14599124818)\[\]

 | 

Yes

 | 

Vector layers. It is recommended that the number of vector layers be less than 2000 to ensure smoothness of the MvtOverlay.

 |

**Example**:

let renderLayers: Array<mapCommon.MvtLayer> = \[\]
let staticLayerIds = \[-12, -8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44\];
for (let index = 0; index < staticLayerIds.length; index++) {
  let layer: mapCommon.MvtLayer = {
    id: index.toString(),
    type: mapCommon.MvtLayerType.FILL,
    sourceLayer: staticLayerIds\[index\].toString(),
    paint: {
      fillColor: {
        operator: mapCommon.Operator.GET,
        args: 'fill'
      },
      fillOpacity: {
        operator: mapCommon.Operator.GET,
        args: 'fill-opacity'
      }
    }
  }
  renderLayers.push(layer)
};

mvtOverlay.addLayers(renderLayers);

#### \[h2\]removeLayers

removeLayers(layerIds: string\[\]): void

Deletes specified layers.

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

layerIds

 | 

string\[\]

 | 

Yes

 | 

IDs of the layers to be deleted.

 |

**Example**:

let layerIds = \['111'\];
mvtOverlay.removeLayers(layerIds);

#### \[h2\]changeLayers

changeLayers(addedLayers: mapCommon.MvtLayer\[\], removedLayerIds: string\[\]): void

Adds vector layers and deletes layers by layer ID.

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

addedLayers

 | 

[mapCommon.MvtLayer](../../mapcommon-map-attribute-model/document.md#section14599124818)\[\]

 | 

Yes

 | 

Vector layers.

 |
| 

removedLayerIds

 | 

string\[\]

 | 

Yes

 | 

IDs of the layers to be deleted.

 |

**Example**:

let renderLayers: Array<mapCommon.MvtLayer> = \[\];
let staticLayerIds = \[-12, -8, -4, 0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44\];
for (let index = 0; index < staticLayerIds.length; index++) {
  let layer: mapCommon.MvtLayer = {
    id: index.toString(),
    type: mapCommon.MvtLayerType.FILL,
    sourceLayer: staticLayerIds\[index\].toString(),
    paint: {
      fillColor: {
        operator: mapCommon.Operator.GET,
        args: 'fill'
      },
      fillOpacity: {
        operator: mapCommon.Operator.GET,
        args: 'fill-opacity'
      }
    }
  }
  renderLayers.push(layer)
}
let layerIds = \['111'\];

mvtOverlay.changeLayers(renderLayers, layerIds);

#### \[h2\]setBlur

setBlur(blurIntensity: number | Record<number, number>): void

Sets the blur intensity of the MvtOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.2(22)

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

blurIntensity

 | 

number | Record<number, number>

 | 

Yes

 | 

Blur intensity of the MvtOverlay. This parameter does not take effect for the 3D globe view.

The blur intensity ranges from 0 to 20. The decimal part is rounded down. The default value is **0**. If an invalid value is passed, the default value will be used.

If the **blurIntensity** value is a number, the same intensity is used for all zoom levels.

If the **blurIntensity** value is key-value pairs, the key indicates the zoom level and the value indicates the blur intensity. The valid level range is \[2, 20\]. For a level value outside of this range, the nearest boundary value will be used. For example, the value **{ 5: 5, 10: 8, 18: 15 }** indicates that the blur intensity is 0 (no blur) for levels 2–4, 5 for levels 5–9, 8 for levels 10–17, and 15 for levels 18–20.

 |

**Example**:

mvtOverlay.setBlur(8);

#### \[h2\]getBlur

getBlur(): number | Record<number, number>

Obtains the blur intensity of the MvtOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

**System capability**: SystemCapability.Map.Core.EnhancedOverlay

**Start version**: 6.0.2(22)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number | Record<number, number>

 | 

Blur intensity of the MvtOverlay.

 |

**Example**:

let blur: number | Record<number, number> = mvtOverlay.getBlur()
