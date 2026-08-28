# IndoorMapInfo

#### Module Import

import { map } from '@kit.MapKit';

#### IndoorMapInfo

Indoor map information. An instance of the IndoorMapInfo type is returned when the [on](../mapeventmanager/document.md#section76731728143918)(type: 'indoorMapEnter', callback: Callback<[IndoorMapInfo](#)\>) API is called.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.1.1(19).

**System capability**: SystemCapability.Map.Core

**Device behavior differences**: For version 19 or later, this API is supported on phones, tablets, and 2-in-1 devices but returns error code 801 on other devices.

**Start version**: 5.1.1(19)

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

buildingId

 | 

string

 | 

No

 | 

No

 | 

Building ID.

 |
| 

floorNames

 | 

string\[\]

 | 

No

 | 

No

 | 

Building floor name array.

 |
| 

floorOrders

 | 

number\[\]

 | 

No

 | 

No

 | 

Building floor sequence array.

 |
| 

currentFloorName

 | 

string

 | 

No

 | 

No

 | 

Name of the current floor.

 |

**Example**:

mapEventManager.on('indoorMapEnter', (indoorMapInfo: map.IndoorMapInfo)=>{
  console.info('indoorMapinfo: ' , indoorMapInfo);
})
