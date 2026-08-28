# MassPointOverlay

#### Module Import

import { map, mapCommon } from '@kit.MapKit';

#### MassPointOverlay

MassPointOverlay object. An instance of the MassPointOverlay type will be returned when the [addMassPointOverlay](../mapcomponentcontroller/document.md#section18441352614) method in the map.[MapComponentController](../mapcomponentcontroller/document.md) class is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Example**:

let items: mapCommon.MassPointItem\[\] = \[\];
for (let i = 0; i < 1000; i++) {
  // Save mass points to **items**.
  items.push({
    itemId: 'test' + i,
    position: {
      longitude: 118.11111 + Math.random() \* 1 - 0.5,
      latitude: 32.11111 + Math.random() \* 1 - 0.5,
    },
    snippet: 'test' + i,
    title: 'test' + i
  })
}
let params: mapCommon.MassPointOverlayParams = {
  id: 'test',
  items: items,
  // The icon is stored in **resources/rawfile**. Set **icon** to the relative path of the icon file in the **rawfile** folder.
  icon: 'icon/maps\_blue\_dot.png',
}
let massPointOverlay = await this.mapController?.addMassPointOverlay(params);

#### \[h2\]getId

getId(): string

Obtains the ID of a MassPointOverlay.

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

string

 | 

MassPointOverlay ID.

 |

**Example**:

let Id = massPointOverlay.getId();

#### \[h2\]setItems

setItems(items: mapCommon.MassPointItem\[\]): void

Sets the mass point list.

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

items

 | 

[mapCommon.MassPointItem](../../mapcommon-map-attribute-model/document.md#section17837254174411)\[\]

 | 

Yes

 | 

Mass point list (it is recommended that the number of mass points be less than 100,000).

 |

**Example**:

let items: mapCommon.MassPointItem\[\] = \[
  {
    itemId: '1',
    position: { latitude: 32.11111, longitude: 118.11111 },
  },
  {
    itemId: '2',
    position: { latitude: 32.22222, longitude: 118.22222 },
  }
\];
massPointOverlay.setItems(items);

#### \[h2\]getItems

getItems(): mapCommon.MassPointItem\[\]

Obtains the mass point list.

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

[mapCommon.MassPointItem](../../mapcommon-map-attribute-model/document.md#section17837254174411)\[\]

 | 

Mass point list.

 |

**Example**:

let MassPointItem: mapCommon.MassPointItem\[\] = this.massPointOverlay.getItems();

#### \[h2\]setAnchorU

setAnchorU(anchorU: number): void

Sets the horizontal position of an icon anchor.

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

anchorU

 | 

number

 | 

Yes

 | 

Horizontal position of an icon anchor. The value ranges from 0 to 1.

 |

**Example**:

massPointOverlay.setAnchorU(0.6);

#### \[h2\]getAnchorU

getAnchorU(): number

Obtains the horizontal position of an icon anchor.

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

number

 | 

Horizontal position of an icon anchor.

 |

**Example**:

let AnchorU: number = this.massPointOverlay.getAnchorU();

#### \[h2\]setAnchorV

setAnchorV(anchorV: number): void

Sets the vertical position of an icon anchor.

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

anchorV

 | 

number

 | 

Yes

 | 

Vertical position of an icon anchor. The value ranges from 0 to 1.

 |

**Example**:

massPointOverlay.setAnchorV(0.6);

#### \[h2\]getAnchorV

getAnchorV(): number

Obtains the vertical position of an icon anchor.

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

number

 | 

Vertical position of an icon anchor.

 |

**Example**:

let AnchorV: number = this.massPointOverlay.getAnchorV();

#### \[h2\]setVisible

setVisible(visible: boolean): void

Sets whether a MassPointOverlay is visible.

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

visible

 | 

boolean

 | 

Yes

 | 

Indicates whether a MassPointOverlay is visible.

-   **true**: yes
-   **false**: no

 |

**Example**:

massPointOverlay.setVisible(true);

#### \[h2\]isVisible

isVisible(): boolean

Checks whether a MassPointOverlay is visible.

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

boolean

 | 

Indicates whether a MassPointOverlay is visible.

-   **true**: yes
-   **false**: no

 |

**Example**:

let isVisible: boolean = massPointOverlay.isVisible();

#### \[h2\]remove

remove(): void

Deletes a MassPointOverlay.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.0(20).

**System capability**: SystemCapability.Map.Core

**Start version**: 6.0.0(20)

**Example**:

massPointOverlay.remove();
