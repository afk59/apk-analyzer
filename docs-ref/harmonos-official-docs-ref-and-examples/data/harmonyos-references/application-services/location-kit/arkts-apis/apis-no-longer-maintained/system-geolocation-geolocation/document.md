# @system.geolocation (Geolocation)

The **geolocation** module provides only basic functions such as GNSS positioning and network positioning.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/Mi5a5sWSQYaRp3fpWT_zZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1D34374F34EA1BFD8E79418A0BA1D903076A3005893A93F56ABFD36E904E898)

-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs provided by this module are no longer maintained since API version 9. You are advised to use [geoLocationManager](../../ohos-geolocationmanager-geolocation-manager/document.md).

#### Modules to Import

import geolocation from '@system.geolocation';

#### Required Permissions

ohos.permission.LOCATION

#### geolocation.getLocation(deprecated)

getLocation(options?: GetLocationOption): void

Obtains the geographic location.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/V7h4sM10R36N_M3sCyluFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2B2F7F24E57E8E1A7FECDD917C948E84A21544CF8A791695D39722E1ECF49BB)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.getCurrentLocation](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetcurrentlocation).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GetLocationOption](#getlocationoptiondeprecated) | No | Options of a single location request. |

**JS example**:

<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    getLocation
  </text>
  <input type="button" value="Obtain Device Geographic Location" style="width: 240px; height: 50px;" onclick="getLocation"></input>
</div>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}

export default {
  getLocation() {
    geolocation.getLocation({
      success: function(data) {
        console.info('success get location data. latitude:' + data.latitude);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
      }
    });
  },
}

#### geolocation.getLocationType(deprecated)

getLocationType(options?: GetLocationTypeOption): void

Obtains the supported location types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/2iA9aT47ReOmyoyKnPOKCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B3328856352B3CF114CF1340B0A58776EAB9CF436E0DB5242C6DE25F5E38388)

This API is deprecated since API version 9. The location subsystem supports only two location types: GNSS positioning and network positioning. No APIs will be provided to query the supported location types.

**System capability**: SystemCapability.Location.Location.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GetLocationTypeOption](#getlocationtypeoptiondeprecated) | No | Callback used to return the result. |

**JS example**:

<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    getLocationType
  </text>
  <input type="button" value="Obtain Location Types Supported by Current Device" style="width: 240px; height: 50px;" onclick="getLocationType"></input>
</div>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}

export default {
  getLocationType() {
    geolocation.getLocationType({
      success: function(data) {
        console.info('success get location type:' + data.types\[0\]);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
       },
     });
  },
}

#### geolocation.subscribe(deprecated)

subscribe(options: SubscribeLocationOption): void

Listens to the geographic location. If this API is called multiple times, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/9Kzz4mEfR4Cl8k5qrV1ALg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B75C25B6374E8ABBC70B961D65F6C03F17B5AE34070C76E1B4C45E530DD61AB9)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.on('locationChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageronlocationchange).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeLocationOption](#subscribelocationoptiondeprecated) | Yes | Options for continuous location. |

**JS example**:

<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    subscribe
  </text>
  <input type="button" value="Subscribe to Device Geographic Location Information" style="width: 240px; height: 50px;" onclick="subscribe"></input>
</div>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}

export default {
  subscribe() {
    geolocation.subscribe({
      success: function(data) {
        console.info('get location. latitude:' + data.latitude);
      },
      fail: function(data, code) {
        console.info('fail to get location. code:' + code + ', data:' + data);
      },
    });
  },
}

#### geolocation.unsubscribe(deprecated)

unsubscribe(): void

Cancels listening to the geographic location.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/uW_3N8GKQj2UxwejTdbgoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09CF5BDAFFB11837DE31352FDACB8D6449B0AF5355D2AD98DB9C77A3FA1684B2)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.off('locationChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerofflocationchange).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Lite

**JS example**:

<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    unsubscribe
  </text>
  <input type="button" value="Unsubscribe from Device Geographic Location Information" style="width: 240px; height: 50px;" onclick="unsubscribe"></input>
</div>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}

export default {
  unsubscribe() {
    geolocation.unsubscribe();
  },
}

#### geolocation.getSupportedCoordTypes(deprecated)

getSupportedCoordTypes(): Array<string>

Obtains coordinate system types supported by the device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/_OQ4rY7xQPGEc8rKDy-YmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1AE4982C31B3A2AF9C92F646A641020935778AF8F14788F6850596D00983F5A)

This API is deprecated since API version 9. The location subsystem supports only the WGS-84 coordinate system. No APIs will be provided to query the supported coordinate system types.

**System capability**: SystemCapability.Location.Location.Lite

**Return value**

| Type | Not empty | Description |
| :-- | :-- | :-- |
| Array<string> | Yes | Coordinate system types, for example, **\[wgs84, gcj02\]**. |

**JS example**:

<div class="container">
  <text class="title" style="font-size: {{fontSize}}; color: {{fontColor}};">
    getSupportedCoordTypes
  </text>
  <input type="button" value="Obtain Coordinate System Types Supported by Device" style="width: 240px; height: 50px;" onclick="getSupportedCoordTypes"></input>
</div>

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  left: 0px;
  top: 0px;
  width: 454px;
  height: 454px;
}

.title {
  font-size: 100px;
  text-align: center;
  width: 200px;
  height: 100px;
}

.button {
  font-size: 30px;
  text-align: center;
  width: 200px;
  height: 100px;
}

export default {
  getSupportedCoordTypes() {
    var types = geolocation.getSupportedCoordTypes();
    console.info('getSupportedCoordTypes:' types);
  },
}

#### GetLocationOption(deprecated)

Options of a single location request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/F0JfBiwgTw-Jfb53DUbh9g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=958B6AACE7834F413BA3DD0AE68477FA6CE2B3A91647D616EF38CA05F1EAB99B)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.CurrentLocationRequest](../../ohos-geolocationmanager-geolocation-manager/document.md#currentlocationrequest).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeout | number | No | 
Timeout duration, in ms. The default value is **30000**.

The timeout duration is necessary in case the request to obtain the geographic location is rejected for the lack of the required permission, weak positioning signal, or incorrect location settings. After the timeout duration expires, the fail function will be called.

The value is a 32-digit positive integer. If the specified value is less than or equal to **0**, the default value will be used.

 |
| coordType | string | No | Coordinate system type. Available types can be obtained by **getSupportedCoordTypes**. The default type is **wgs84**. |
| success | (data: [GeolocationResponse](#geolocationresponsedeprecated)) => void | No | Called when API call is successful. |
| fail | (data: string, code: number) => void | No | Called when API call has failed. **data** indicates the error information, and **code** indicates the error code. |
| complete | () => void | No | Called when API call is complete. |

**Return value of fail()**

| Error Code | Description |
| :-- | :-- |
| 601 | Failed to obtain the required permission because the user rejected the request. |
| 602 | Permission not declared. |
| 800 | Operation times out due to a poor network condition or GNSS unavailability. |
| 801 | System location disabled. |
| 802 | API called again while the previous execution result is not returned yet. |

#### GeolocationResponse(deprecated)

Defines the location information, including the longitude, latitude, and location precision.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/Yx8LoVE1Sf6S2F6mVg7FXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6168980ACFA3BF6AB3706A868E7B06DB8A166D6183E39C9E399723C375995436)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.Location](../../ohos-geolocationmanager-geolocation-manager/document.md#location).

**System capability**: SystemCapability.Location.Location.Lite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| longitude | number | No | No | Longitude. |
| latitude | number | No | No | Latitude. |
| altitude | number | No | No | Altitude. |
| accuracy | number | No | No | Location accuracy. |
| time | number | No | No | Time when the location is obtained. |

#### GetLocationTypeOption(deprecated)

Defines the location type option, which holds the callback function used to return the query result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/XfXfhrvvQJqayDAO3P-BsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1785CDCB7E80B756A40A41F9779FECD7BE37D279C8660ECFC887666FF76A17AF)

This API is deprecated since API version 9.

**System capability**: SystemCapability.Location.Location.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | (data: [GetLocationTypeResponse](#getlocationtyperesponsedeprecated)) => void | No | Called when API call is successful. |
| fail | (data: string, code: number) => void | No | Called when API call has failed. |
| complete | () => void | No | Called when API call is complete. |

#### GetLocationTypeResponse(deprecated)

Defines the list of location types supported by the current device

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/C7r_5iT7Spev77L5ZOUNTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=321E14AD977BC9ADB093CDE19F111A74BD07FA30FCC190A41FFAC2C644FD972F)

This API is deprecated since API version 9.

**System capability**: SystemCapability.Location.Location.Lite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| types | Array<string> | No | No | Available location types, \['gps', 'network'\] |

#### SubscribeLocationOption(deprecated)

Defines the options for continuous location.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/tOCUeIEWTnifvkYYJWWbHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=33178BB1FA5A124F3290C631D81DFEF35C63976F2F0C8631E6749DCCB9C9B0E6)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.CurrentLocationRequest](../../ohos-geolocationmanager-geolocation-manager/document.md#currentlocationrequest).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| coordType | string | No | Coordinate system type. Available types can be obtained by **getSupportedCoordTypes**. The default type is **wgs84**. |
| success | (data: [GeolocationResponse](#geolocationresponsedeprecated)) => void | Yes | Called when the geographic location changes. |
| fail | (data: string, code: number) => void | No | Called when API call has failed. |

**Return value of fail()**

| Error Code | Description |
| :-- | :-- |
| 601 | Failed to obtain the required permission because the user rejected the request. |
| 602 | Permission not declared. |
| 801 | System location disabled. |
