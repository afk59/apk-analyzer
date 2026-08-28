# @ohos.geolocation (Geolocation)

The **geolocation** module provides a wide array of location services, including GNSS positioning, network positioning, geocoding, reverse geocoding, and geofencing.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0c/v3/SA_31a8DS86vPwvjtG9oBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9316945E94688DC5F854E522DBDB55D892882A39C8CC7D5AD7951E84AEB82A04)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

The APIs provided by this module are no longer maintained since API version 9. You are advised to use [geoLocationManager](../../ohos-geolocationmanager-geolocation-manager/document.md).

This module supports only the WGS-84 coordinate system.

#### Applying for Permissions

Before using basic location capabilities, check whether your application has been granted the permission to access the device location information. If not, your application needs to obtain the permission from the user as described below.

The system provides the following location permissions:

-   ohos.permission.LOCATION
    
-   ohos.permission.APPROXIMATELY\_LOCATION
    
-   ohos.permission.LOCATION\_IN\_BACKGROUND
    

If your application needs to access the device location information, it must first apply for required permissions. Specifically speaking:

API versions earlier than 9: Apply for **ohos.permission.LOCATION**.

API version 9 and later: Apply for **ohos.permission.APPROXIMATELY\_LOCATION**, or apply for **ohos.permission.APPROXIMATELY\_LOCATION** and **ohos.permission.LOCATION**. Note that **ohos.permission.LOCATION** cannot be applied for separately.

| API Version | Location Permission | Permission Application Result | Location Accuracy |
| :-- | :-- | :-- | :-- |
| Earlier than 9 | ohos.permission.LOCATION | Successful | Location accurate to meters. |
| 9 and later | ohos.permission.LOCATION | Failed | No location obtained. |
| 9 and later | ohos.permission.APPROXIMATELY\_LOCATION | Successful | Location accurate to 5 kilometers. |
| 9 and later | ohos.permission.APPROXIMATELY\_LOCATION and ohos.permission.LOCATION | Successful | Location accurate to meters. |

To access the device location information when running in the background, an application needs to request for a continuous task of the LOCATION type. In this way, the system continues to report device location information after your application moves to the background. For details about how to request for a continuous task, see [Continuous Task](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/continuous-task).

A user can grant the **ohos.permission.LOCATION\_IN\_BACKGROUND** permission for an application on the setting page. For details, see [ohos.permission.LOCATION\_IN\_BACKGROUND](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/permissions-for-all-user#ohospermissionlocation_in_background).

You can declare the required permission in your application's configuration file. For details, see [Requesting User Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/request-user-authorization).

#### Modules to Import

import geolocation from '@ohos.geolocation';

#### geolocation.on('locationChange')(deprecated)

on(type: 'locationChange', request: LocationRequest, callback: Callback<Location>): void

Registers a listener for location changes with a location request initiated. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/8T6YT9qtSji1RUkOapupzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=87A02DD99BA0093F53A87C0D00A88B4B4032C5FFF3DC706005D803BD7B8C2651)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.on('locationChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageronlocationchange) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **locationChange** indicates a location change event. |
| request | [LocationRequest](#locationrequestdeprecated) | Yes | Location request. |
| callback | Callback<[Location](#locationdeprecated)\> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
let locationChange = (location:geolocation.Location):void => {
    console.info('locationChanger: data: ' + JSON.stringify(location));
};
geolocation.on('locationChange', requestInfo, locationChange);

#### geolocation.off('locationChange')(deprecated)

off(type: 'locationChange', callback?: Callback<Location>): void

Unregisters the listener for location changes with the corresponding location request deleted.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/LR7x4OKGTT62l7w64FErmA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A5C17EC704494813982E449DD401AFA241FFE537E15E0C89706BD496FE2F68D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.off('locationChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerofflocationchange) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **locationChange** indicates a location change event. |
| callback | Callback<[Location](#locationdeprecated)\> | No | Callback to unregister. The callback must be the same as that passed by the **on** API. If this parameter is not specified, all callbacks of the specified event type are unregistered. |

**Example**

import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationRequest = {'priority': 0x203, 'scenario': 0x300, 'timeInterval': 0, 'distanceInterval': 0, 'maxAccuracy': 0};
let locationChange = (location:geolocation.Location):void => {
    console.info('locationChanger: data: ' + JSON.stringify(location));
};
geolocation.on('locationChange', requestInfo, locationChange);
geolocation.off('locationChange', locationChange);

#### geolocation.on('locationServiceState')(deprecated)

on(type: 'locationServiceState', callback: Callback<boolean>): void

Registers a listener for location service status change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/ecJCTiQXT2ujlz4ABWR-Lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3A06EB3179DD612ADFAB1D87AE18650ECDC909A091048866A2D65047ED80C745)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.on('locationEnabledChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageronlocationenabledchange) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **locationServiceState** indicates a location service status change event. |
| callback | Callback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the location service is enabled, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
let locationServiceState = (state:boolean):void => {
    console.info('locationServiceState: ' + JSON.stringify(state));
}
geolocation.on('locationServiceState', locationServiceState);

#### geolocation.off('locationServiceState')(deprecated)

off(type: 'locationServiceState', callback?: Callback<boolean>): void

Unregisters the listener for location service status change events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/nCzuGMHJTAyu9qggj78ZVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=879664DFA7F0BF36C16D7A43FFEFB7B95F64C05FD8ADAD9B812188DBE97AFD48)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.off('locationEnabledChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerofflocationenabledchange) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **locationServiceState** indicates a location service status change event. |
| callback | Callback<boolean> | No | Callback to unregister. The value **true** indicates that the location service is enabled, and the value **false** indicates the opposite. The callback must be the same as that passed by the **on** API. If this parameter is not specified, all callbacks of the specified event type are unregistered. |

**Example**

import geolocation from '@ohos.geolocation';
let locationServiceState = (state:boolean):void => {
    console.info('locationServiceState: state: ' + JSON.stringify(state));
}
geolocation.on('locationServiceState', locationServiceState);
geolocation.off('locationServiceState', locationServiceState);

#### geolocation.on('cachedGnssLocationsReporting')(deprecated)

on(type: 'cachedGnssLocationsReporting', request: CachedGnssLocationsRequest, callback: Callback<Array<Location>>): void

Registers a listener for cached GNSS location reports. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/p9fN7nnpQtuBrKNeAQY-rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D6601BCB6B27916E855342320600957B4AFD04C575A9C5B94BA5859687E92AD0)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.on('cachedGnssLocationsChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageroncachedgnsslocationschange).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **cachedGnssLocationsReporting** indicates reporting of cached GNSS locations. |
| request | [CachedGnssLocationsRequest](#cachedgnsslocationsrequestdeprecated) | Yes | Request for reporting cached GNSS location. |
| callback | Callback<Array<[Location](#locationdeprecated)\>> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
    console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
}
let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);

#### geolocation.off('cachedGnssLocationsReporting')(deprecated)

off(type: 'cachedGnssLocationsReporting', callback?: Callback<Array<Location>>): void

Unregisters the listener for cached GNSS location reports.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/6-Um3YYoR8OU_aUvCSetZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A0D00A25F4934B7A8552E0D178B9A7D42024446E33FDBAF504F6542268E98479)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.off('cachedGnssLocationsChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageroffcachedgnsslocationschange).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **cachedGnssLocationsReporting** indicates reporting of cached GNSS locations. |
| callback | Callback<Array<[Location](#locationdeprecated)\>> | No | Callback to unregister. The callback must be the same as that passed by the **on** API. If this parameter is not specified, all callbacks of the specified event type are unregistered. |

**Example**

import geolocation from '@ohos.geolocation';
let cachedLocationsCb = (locations:Array<geolocation.Location>):void => {
    console.info('cachedGnssLocationsReporting: locations: ' + JSON.stringify(locations));
}
let requestInfo:geolocation.CachedGnssLocationsRequest = {'reportingPeriodSec': 10, 'wakeUpCacheQueueFull': true};
geolocation.on('cachedGnssLocationsReporting', requestInfo, cachedLocationsCb);
geolocation.off('cachedGnssLocationsReporting');

#### geolocation.on('gnssStatusChange')(deprecated)

on(type: 'gnssStatusChange', callback: Callback<SatelliteStatusInfo>): void

Registers a listener for GNSS satellite status change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/eH5Ul7iSSyGVZadoJQCNSQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=138E2F2AAE692F291BFCAE53DDD7A0178405CCA9A3382D13A534F84E748AFC81)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.on('satelliteStatusChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageronsatellitestatuschange).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **gnssStatusChange** indicates a GNSS satellite status change. |
| callback | Callback<[SatelliteStatusInfo](#satellitestatusinfodeprecated)\> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo):void => {
    console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
}
geolocation.on('gnssStatusChange', gnssStatusCb);

#### geolocation.off('gnssStatusChange')(deprecated)

off(type: 'gnssStatusChange', callback?: Callback<SatelliteStatusInfo>): void

Unregisters the listener for GNSS satellite status change events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/dCsUhnznTgeaGcV2COPaVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E2803B211525EB94D7C8B203B7E42C96C358A5325D5DB2F07AD09D3FD36870F)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.off('satelliteStatusChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageroffsatellitestatuschange).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **gnssStatusChange** indicates a GNSS satellite status change. |
| callback | Callback<[SatelliteStatusInfo](#satellitestatusinfodeprecated)\> | No | Callback to unregister. The callback must be the same as that passed by the **on** API. If this parameter is not specified, all callbacks of the specified event type are unregistered. |

**Example**

import geolocation from '@ohos.geolocation';
let gnssStatusCb = (satelliteStatusInfo:geolocation.SatelliteStatusInfo) => {
    console.info('gnssStatusChange: ' + JSON.stringify(satelliteStatusInfo));
}
geolocation.on('gnssStatusChange', gnssStatusCb);
geolocation.off('gnssStatusChange', gnssStatusCb);

#### geolocation.on('nmeaMessageChange')(deprecated)

on(type: 'nmeaMessageChange', callback: Callback<string>): void

Registers a listener for GNSS NMEA message change events. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/9TXoEwXfSSy0VneWff4TXQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A50070595DF283B318407E46E8673144063DA455E1AE684705946C59A38A81B7)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.on('nmeaMessage')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageronnmeamessage).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **nmeaMessageChange** indicates a GNSS NMEA message change. |
| callback | Callback<string> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let nmeaCb = (str:string):void => {
    console.info('nmeaMessageChange: ' + JSON.stringify(str));
}
geolocation.on('nmeaMessageChange', nmeaCb );

#### geolocation.off('nmeaMessageChange')(deprecated)

off(type: 'nmeaMessageChange', callback?: Callback<string>): void

Unregisters the listener for GNSS NMEA message change events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/ZPSbcG7WRAKYmKrRelfKmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2FCC70B8EEF859D91A1033B2D1026C5CB91331AA6433986F47D063F691AE4084)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.off('nmeaMessage')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageroffnmeamessage).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **nmeaMessageChange** indicates a GNSS NMEA message change. |
| callback | Callback<string> | No | Callback to unregister. The callback must be the same as that passed by the **on** API. If this parameter is not specified, all callbacks of the specified event type are unregistered. |

**Example**

import geolocation from '@ohos.geolocation';
let nmeaCb = (str:string):void => {
    console.info('nmeaMessageChange: ' + JSON.stringify(str));
}
geolocation.on('nmeaMessageChange', nmeaCb);
geolocation.off('nmeaMessageChange', nmeaCb);

#### geolocation.on('fenceStatusChange')(deprecated)

on(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void

Registers a listener for status change events of the specified geofence. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/ARt2SepDQQaqMkvJLBPpjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B4576DA4D10693F1F018A3D62F0677BDC907BEF5CC918104792EAFD417CBDB3)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.on('gnssFenceStatusChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerongnssfencestatuschange).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geofence

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **fenceStatusChange** indicates a geofence status change. |
| request | [GeofenceRequest](#geofencerequestdeprecated) | Yes | Geofencing request. |
| want | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | Yes | **WantAgent** used to receive geofence (entrance or exit) events. |

**Example**

import geolocation from '@ohos.geolocation';
import wantAgent from '@ohos.app.ability.wantAgent';

let wantAgentInfo:wantAgent.WantAgentInfo = {
    wants: \[
        {
            bundleName: "com.example.myapplication",
            abilityName: "EntryAbility",
            action: "action1"
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\],
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let requestInfo:geolocation.GeofenceRequest = {'priority': 0x201, 'scenario': 0x301, "geofence": {"latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000}};
  geolocation.on('fenceStatusChange', requestInfo, wantAgentObj);
});

#### geolocation.off('fenceStatusChange')(deprecated)

off(type: 'fenceStatusChange', request: GeofenceRequest, want: WantAgent): void

Unregisters the listener for status change events of the specified geofence.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/8ZgSugP6TLKTLbBeQVujXg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=24A91AAFFD9D8EAD0142A3CCE45370159A16770553FC884C7CFFB29F16CF5080)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.off('gnssFenceStatusChange')](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanageroffgnssfencestatuschange).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geofence

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | Event type. The value **fenceStatusChange** indicates a geofence status change. |
| request | [GeofenceRequest](#geofencerequestdeprecated) | Yes | Geofencing request. |
| want | [WantAgent](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-wantagent-wantagent-module/document.md) | Yes | **WantAgent** used to receive geofence (entrance or exit) events. |

**Example**

import geolocation from '@ohos.geolocation';
import wantAgent from '@ohos.app.ability.wantAgent';

let wantAgentInfo:wantAgent.WantAgentInfo = {
    wants: \[
        {
            bundleName: "com.example.myapplication",
            abilityName: "EntryAbility",
            action: "action1",
        }
    \],
    operationType: wantAgent.OperationType.START\_ABILITY,
    requestCode: 0,
    wantAgentFlags: \[wantAgent.WantAgentFlags.UPDATE\_PRESENT\_FLAG\]
};

wantAgent.getWantAgent(wantAgentInfo).then((wantAgentObj) => {
  let requestInfo:geolocation.GeofenceRequest = {'priority': 0x201, 'scenario': 0x301, "geofence": {"latitude": 31.12, "longitude": 121.11, "radius": 100, "expiration": 10000}};
  geolocation.on('fenceStatusChange', requestInfo, wantAgentObj);
  geolocation.off('fenceStatusChange', requestInfo, wantAgentObj);
});

#### geolocation.getCurrentLocation(deprecated)

getCurrentLocation(request: CurrentLocationRequest, callback: AsyncCallback<Location>): void

Obtains the current position. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/TwK_YgeWT0S4CIVVzeyHeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAFF07D763CF9DC5E469167E392AF47A3E3EBD2820918C8F20E310123BE33445)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getCurrentLocation](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetcurrentlocation) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [CurrentLocationRequest](#currentlocationrequestdeprecated) | Yes | Location request. |
| callback | AsyncCallback<[Location](#locationdeprecated)\> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
import BusinessError from "@ohos.base"
let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location) => {
    if (err) {
        console.info('locationChanger: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChanger: location=' + JSON.stringify(location));
    }
};
geolocation.getCurrentLocation(requestInfo, locationChange);

#### geolocation.getCurrentLocation(deprecated)

getCurrentLocation(callback: AsyncCallback<Location>): void

Obtains the current position. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/EtpgCxWFRwWNBz9lRGRnww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39468C1E41DE34868809A768590149D8CEB6BCCA4BE99421CD8C1F4E08A80003)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getCurrentLocation](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetcurrentlocation) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Location](#locationdeprecated)\> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
import BusinessError from "@ohos.base"
let locationChange = (err:BusinessError.BusinessError, location:geolocation.Location):void => {
    if (err) {
        console.info('locationChanger: err=' + JSON.stringify(err));
    }
    if (location) {
        console.info('locationChanger: location=' + JSON.stringify(location));
    }
};
geolocation.getCurrentLocation(locationChange);

#### geolocation.getCurrentLocation(deprecated)

getCurrentLocation(request?: CurrentLocationRequest): Promise<Location>

Obtains the current position. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dc/v3/_51jcgXpStWpzOZf0xvD7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D016847398177E2DAAC782026CD0D8E160B6809A3B1FDBCEFCB02D6DAB5A3057)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getCurrentLocation](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetcurrentlocation-2) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [CurrentLocationRequest](#currentlocationrequestdeprecated) | No | Location request. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Location](#locationdeprecated)\> | Promise used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.CurrentLocationRequest = {'priority': 0x203, 'scenario': 0x300,'maxAccuracy': 0};
geolocation.getCurrentLocation(requestInfo).then((result) => {
    console.info('current location: ' + JSON.stringify(result));
});

#### geolocation.getLastLocation(deprecated)

getLastLocation(callback: AsyncCallback<Location>): void

Obtains the previous location. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5/v3/_j83_5AFS42y9P6vCv1VdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B252F7570F3BC443C891B741A00446ACDB42DB8C884822AD684E7E106FCD09C4)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getLastLocation](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetlastlocation) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Location](#locationdeprecated)\> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.getLastLocation((err, data) => {
    if (err) {
        console.info('getLastLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('getLastLocation: data=' + JSON.stringify(data));
    }
});

#### geolocation.getLastLocation(deprecated)

getLastLocation(): Promise<Location>

Obtains the previous location. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/hUHn1M1BS9S1l2BlqP0blQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA0DBDFAF714A026CD128397AAE7C220BAD6FE1434951205BB0210C9DBCD9ECA)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getLastLocation](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetlastlocation) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Location](#locationdeprecated)\> | Promise used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.getLastLocation().then((result) => {
    console.info('getLastLocation: result: ' + JSON.stringify(result));
});

#### geolocation.isLocationEnabled(deprecated)

isLocationEnabled(callback: AsyncCallback<boolean>): void

Checks whether the location service is enabled. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/MJicT6YlTLONF2b2Di0uzw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=840FC9DFB4326BED3732EEC4D31248CB93FA8DAF52BEA44021D654E91096C11D)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.isLocationEnabled](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerislocationenabled) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the location service is enabled, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.isLocationEnabled((err, data) => {
    if (err) {
        console.info('isLocationEnabled: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('isLocationEnabled: data=' + JSON.stringify(data));
    }
});

#### geolocation.isLocationEnabled(deprecated)

isLocationEnabled(): Promise<boolean>

Checks whether the location service is enabled. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/UjIepvnETOmaGhXVl9IdWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7224210D0F51D04D0BC8530E32928A87F7A4463489B1AC79E28309E664764EE)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.isLocationEnabled](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerislocationenabled) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the location service is enabled, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.isLocationEnabled().then((result) => {
    console.info('promise, isLocationEnabled: ' + JSON.stringify(result));
});

#### geolocation.requestEnableLocation(deprecated)

requestEnableLocation(callback: AsyncCallback<boolean>): void

Sends a request for enabling the location service. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1/v3/WzzLFL9JRbu5TZofniAYLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55440A224849105F0A6CD6CE42704A59CAFF03878DCEFEC7A725C85412CEB58F)

This API is supported since API version 7 and deprecated since API version 9. It is recommended that the application display a dialog box to request the user to go to **Settings** to enable the location function and specify the scenarios in which the location information will be used in the dialog box.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the location service is enabled, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.requestEnableLocation((err, data) => {
    if (err) {
        console.info('requestEnableLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('requestEnableLocation: data=' + JSON.stringify(data));
    }
});

#### geolocation.requestEnableLocation(deprecated)

requestEnableLocation(): Promise<boolean>

Sends a request for enabling the location service. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/Mb2-TYDvRuC4CSlZ1aDcnQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C086597E6F7AFF563A1A351CBD607A1F1739B7A0EB831B1D55528E37CA4A021C)

This API is supported since API version 7 and deprecated since API version 9. It is recommended that the application display a dialog box to request the user to go to **Settings** to enable the location function and specify the scenarios in which the location information will be used in the dialog box.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the location service is enabled, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.requestEnableLocation().then((result) => {
    console.info('promise, requestEnableLocation: ' + JSON.stringify(result));
});

#### geolocation.isGeoServiceAvailable(deprecated)

isGeoServiceAvailable(callback: AsyncCallback<boolean>): void

Checks whether the (reverse) geocoding service is available. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/sGLQAjmaT0ig6tfBhxO8bQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=918434A1873F019765AA85DF237707B657D290EC358C28A7BD1BB21291C2CF1B)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.isGeocoderAvailable](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerisgeocoderavailable) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the (reverse) geocoding service is available, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.isGeoServiceAvailable((err, data) => {
    if (err) {
        console.info('isGeoServiceAvailable: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('isGeoServiceAvailable: data=' + JSON.stringify(data));
    }
});

#### geolocation.isGeoServiceAvailable(deprecated)

isGeoServiceAvailable(): Promise<boolean>

Checks whether the (reverse) geocoding service is available. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/W2ZSqwxjQR2zIUNPMn_1oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6140FB0BC7611A5AAFDC7F13B9CC33ACDC69DE0CAD1E5BD837D3A1C795C697B2)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.isGeocoderAvailable](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerisgeocoderavailable) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the (reverse) geocoding service is available, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.isGeoServiceAvailable().then((result) => {
    console.info('promise, isGeoServiceAvailable: ' + JSON.stringify(result));
});

#### geolocation.getAddressesFromLocation(deprecated)

getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

Converts coordinates into geographic descriptions through reverse geocoding. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/tp5qnBfGTy2viXtZoB1NVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99A74FC6C6DD232BBE652457EFD4DA61DA865EFBEF770E05CD1422675C1E807A)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getAddressesFromLocation](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetaddressesfromlocation) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [ReverseGeoCodeRequest](#reversegeocoderequestdeprecated) | Yes | Reverse geocoding request. |
| callback | AsyncCallback<Array<[GeoAddress](#geoaddressdeprecated)\>> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let reverseGeocodeRequest:geolocation.ReverseGeoCodeRequest = {"latitude": 31.12, "longitude": 121.11, "maxItems": 1};
geolocation.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
    if (err) {
        console.info('getAddressesFromLocation: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('getAddressesFromLocation: data=' + JSON.stringify(data));
    }
});

#### geolocation.getAddressesFromLocation(deprecated)

getAddressesFromLocation(request: ReverseGeoCodeRequest): Promise<Array<GeoAddress>>

Converts coordinates into geographic descriptions through reverse geocoding. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/3F7ot0oZRIe-edNZRbE7uQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EF1DC658454C2FDC6A4C121B46F5ADF59C00A91EA75E3D1C3087B8C4D4E14332)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getAddressesFromLocation](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetaddressesfromlocation-1) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [ReverseGeoCodeRequest](#reversegeocoderequestdeprecated) | Yes | Reverse geocoding request. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[GeoAddress](#geoaddressdeprecated)\>> | Promise used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let reverseGeocodeRequest:geolocation.ReverseGeoCodeRequest = {"latitude": 31.12, "longitude": 121.11, "maxItems": 1};
geolocation.getAddressesFromLocation(reverseGeocodeRequest).then((data) => {
    console.info('getAddressesFromLocation: ' + JSON.stringify(data));
});

#### geolocation.getAddressesFromLocationName(deprecated)

getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void

Converts geographic descriptions into coordinates through geocoding. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/1gviwEhpSFCsVEySd-tUaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3520993CA1B5E70651EE50B23DCE93E01205AD3C616B90B2549A92351E1D47C)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getAddressesFromLocationName](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetaddressesfromlocationname) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [GeoCodeRequest](#geocoderequestdeprecated) | Yes | Geocoding request. |
| callback | AsyncCallback<Array<[GeoAddress](#geoaddressdeprecated)\>> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let geocodeRequest:geolocation.GeoCodeRequest = {"description": "No. xx, xx Road, Pudong District, Shanghai", "maxItems": 1};
geolocation.getAddressesFromLocationName(geocodeRequest, (err, data) => {
    if (err) {
        console.info('getAddressesFromLocationName: err=' + JSON.stringify(err));
    }
    if (data) {
        console.info('getAddressesFromLocationName: data=' + JSON.stringify(data));
    }
});

#### geolocation.getAddressesFromLocationName(deprecated)

getAddressesFromLocationName(request: GeoCodeRequest): Promise<Array<GeoAddress>>

Converts geographic descriptions into coordinates through geocoding. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/SED6Z8qRQzqysfSa7RhrHA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B858B9758C9B7B886088578AB21695F595049163CFDD13F4C79C9E07334F409)

This API is supported since API version 7 and deprecated since API version 9. You are advised to use [geoLocationManager.getAddressesFromLocationName](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetaddressesfromlocationname-1) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| request | [GeoCodeRequest](#geocoderequestdeprecated) | Yes | Geocoding request. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[GeoAddress](#geoaddressdeprecated)\>> | Promise used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
let geocodeRequest:geolocation.GeoCodeRequest = {"description": "No. xx, xx Road, Pudong District, Shanghai", "maxItems": 1};
geolocation.getAddressesFromLocationName(geocodeRequest).then((result) => {
    console.info('getAddressesFromLocationName: ' + JSON.stringify(result));
});

#### geolocation.getCachedGnssLocationsSize(deprecated)

getCachedGnssLocationsSize(callback: AsyncCallback<number>): void

Obtains the number of cached GNSS locations. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/XeoUAp4lTWqhBpRZ78WLBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF12AF9C8829103C9BB5C04EE6EEB69C692305E6011601CF3AF042303A616CE6)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.getCachedGnssLocationsSize](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetcachedgnsslocationssize).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<number> | Yes | Callback used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.getCachedGnssLocationsSize((err, size) => {
    if (err) {
        console.info('getCachedGnssLocationsSize: err=' + JSON.stringify(err));
    }
    if (size) {
        console.info('getCachedGnssLocationsSize: size=' + JSON.stringify(size));
    }
});

#### geolocation.getCachedGnssLocationsSize(deprecated)

getCachedGnssLocationsSize(): Promise<number>;

Obtains the number of cached GNSS locations. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/ciOhebJPTJODhamQnBOXjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42203A719C6BCF888B88C5FB9B01327FB24345F1A1B0645A59DC0606BCFEC4DB)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.getCachedGnssLocationsSize](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagergetcachedgnsslocationssize-1).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the result. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.getCachedGnssLocationsSize().then((result) => {
    console.info('promise, getCachedGnssLocationsSize: ' + JSON.stringify(result));
});

#### geolocation.flushCachedGnssLocations(deprecated)

flushCachedGnssLocations(callback: AsyncCallback<boolean>): void

Obtains all cached GNSS locations and clears the GNSS cache queue. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/h8ZlN7hrTHmZtCkxSHMePg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69E5C2A50E485C38198071581CBABEB9A36E947F8EC0241A9FADC9535ED79366)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.flushCachedGnssLocations](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerflushcachedgnsslocations).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.flushCachedGnssLocations((err, result) => {
    if (err) {
        console.info('flushCachedGnssLocations: err=' + JSON.stringify(err));
    }
    if (result) {
        console.info('flushCachedGnssLocations: result=' + JSON.stringify(result));
    }
});

#### geolocation.flushCachedGnssLocations(deprecated)

flushCachedGnssLocations(): Promise<boolean>

Obtains all cached GNSS locations and clears the GNSS cache queue. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/8VwJQcazRgSLIurWdm4Pnw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F0ADDAB3C5CE91F989C1814BAC01BD2F428782DA91BD121AED31675164673D2)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.flushCachedGnssLocations](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagerflushcachedgnsslocations-1).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
geolocation.flushCachedGnssLocations().then((result) => {
    console.info('promise, flushCachedGnssLocations: ' + JSON.stringify(result));
});

#### geolocation.sendCommand(deprecated)

sendCommand(command: LocationCommand, callback: AsyncCallback<boolean>): void

Sends an extended command to the location subsystem. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/n1B3v5sATtCy-A9fIo3PFQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC0C1E127173A4E7AD342FD3375FB585CF2EEB9E6FEFD484592B7715387D6D78)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.sendCommand](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagersendcommand).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| command | [LocationCommand](#locationcommanddeprecated) | Yes | Extended command (string) to be sent. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationCommand = {'scenario': 0x301, 'command': "command\_1"};
geolocation.sendCommand(requestInfo, (err, result) => {
    if (err) {
        console.info('sendCommand: err=' + JSON.stringify(err));
    }
    if (result) {
        console.info('sendCommand: result=' + JSON.stringify(result));
    }
});

#### geolocation.sendCommand(deprecated)

sendCommand(command: LocationCommand): Promise<boolean>

Sends an extended command to the location subsystem. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/43/v3/MJ6PQhwuS5a_btpfxFaZ_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B5EFFDEB28C0D12560B1D9E55BEED7773F73C4449759C649B56D634D3EC07A6)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.sendCommand](../../ohos-geolocationmanager-geolocation-manager/document.md#geolocationmanagersendcommand).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| command | [LocationCommand](#locationcommanddeprecated) | Yes | Extended command (string) to be sent. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import geolocation from '@ohos.geolocation';
let requestInfo:geolocation.LocationCommand = {'scenario': 0x301, 'command': "command\_1"};
geolocation.sendCommand(requestInfo).then((result) => {
    console.info('promise, sendCommand: ' + JSON.stringify(result));
});

#### ReverseGeoCodeRequest(deprecated)

Defines a reverse geocoding request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/1kdptDskQVuq0b-JgtcLWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6878CBE25AF334A6796D805FB82CA9C00C7076EA545B2EA5C79B5A26D6537FF)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.ReverseGeoCodeRequest](../../ohos-geolocationmanager-geolocation-manager/document.md#reversegeocoderequest).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| locale | string | No | Yes | Language used for the location description. **zh** indicates Chinese, and **en** indicates English. |
| latitude | number | No | No | Latitude information. A positive value indicates north latitude, and a negative value indicates south latitude. The value ranges from **\-90** to **90**. |
| longitude | number | No | No | Longitude information. A positive value indicates east longitude , and a negative value indicates west longitude. The value ranges from **\-180** to **180**. |
| maxItems | number | No | Yes | Maximum number of location records to be returned. The value must be greater than or equal to **0**. A value smaller than **10** is recommended. |

#### GeoCodeRequest(deprecated)

Defines a geocoding request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/cYVuRuarTeaSuXNjniBpmw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E44A9566E0EE9867FE64A07FC3BCF08AE4A094CD22A7F9A4C769D03CB05BB724)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.GeoCodeRequest](../../ohos-geolocationmanager-geolocation-manager/document.md#geocoderequest).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| locale | string | No | Yes | Language used for the location description. **zh** indicates Chinese, and **en** indicates English. |
| description | string | No | No | Location description, for example, **No. xx, xx Road, Pudong New District, Shanghai**. |
| maxItems | number | No | Yes | Maximum number of location records to be returned. The value must be greater than or equal to **0**. A value smaller than **10** is recommended. |
| minLatitude | number | No | Yes | Minimum latitude. This parameter is used with **minLongitude**, **maxLatitude**, and **maxLongitude** to specify the latitude and longitude ranges. The value ranges from **\-90** to **90**. |
| minLongitude | number | No | Yes | Minimum longitude. The value ranges from **\-180** to **180**. |
| maxLatitude | number | No | Yes | Maximum latitude. The value ranges from **\-90** to **90**. |
| maxLongitude | number | No | Yes | Maximum longitude. The value ranges from **\-180** to **180**. |

#### GeoAddress(deprecated)

Geocoding address information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/Svl_hmnNQySzAaye33CCww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25294C225719F5A7AE427A40AF02EFCFED093250EB6DF058ADCA3AE818CBC34E)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.GeoAddress](../../ohos-geolocationmanager-geolocation-manager/document.md#geoaddress).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geocoder

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| latitude7+ | number | No | Yes | Latitude information. A positive value indicates north latitude, and a negative value indicates south latitude. The value ranges from **\-90** to **90**. |
| longitude7+ | number | No | Yes | Longitude information. A positive value indicates east longitude , and a negative value indicates west longitude. The value ranges from **\-180** to **180**. |
| locale7+ | string | No | Yes | Language used for the location description. **zh** indicates Chinese, and **en** indicates English. |
| placeName7+ | string | No | Yes | Landmark of the location. |
| countryCode7+ | string | No | Yes | Country code. |
| countryName7+ | string | No | Yes | Country name. |
| administrativeArea7+ | string | No | Yes | Administrative region name. |
| subAdministrativeArea7+ | string | No | Yes | Sub-administrative region name. |
| locality7+ | string | No | Yes | Locality information. |
| subLocality7+ | string | No | Yes | Sub-locality information. |
| roadName7+ | string | No | Yes | Road name. |
| subRoadName7+ | string | No | Yes | Auxiliary road information. |
| premises7+ | string | No | Yes | House information. |
| postalCode7+ | string | No | Yes | Postal code. |
| phoneNumber7+ | string | No | Yes | Phone number. |
| addressUrl7+ | string | No | Yes | Website URL. |
| descriptions7+ | Array<string> | No | Yes | Additional descriptions. |
| descriptionsSize7+ | number | No | Yes | Total number of additional descriptions. The value must be greater than or equal to **0**. A value smaller than **10** is recommended. |

#### LocationRequest(deprecated)

Defines a location request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/g6WQw52FSQy_XqvP85Ad8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F77A9B2BA523CF16B64EE1B5E90ECC8C5B9AC0DCE201A3759881CD78C1A2264C)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.LocationRequest](../../ohos-geolocationmanager-geolocation-manager/document.md#locationrequest).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| priority | [LocationRequestPriority](#locationrequestprioritydeprecated) | No | Yes | Priority of the location request. For details about the value range, see [LocationRequestPriority](#locationrequestprioritydeprecated). |
| scenario | [LocationRequestScenario](#locationrequestscenariodeprecated) | No | Yes | Scenario of the location request. For details about the value range, see [LocationRequestScenario](#locationrequestscenariodeprecated). |
| timeInterval | number | No | Yes | Time interval at which location information is reported, in seconds. The value must be greater than **0**. |
| distanceInterval | number | No | Yes | Distance interval at which location information is reported. The value must be greater than **0**, in meters. |
| maxAccuracy | number | No | Yes | 
Location accuracy, in meters.

This parameter is valid only when the precise location function is enabled (both the **ohos.permission.APPROXIMATELY\_LOCATION** and **ohos.permission.LOCATION** permissions are granted), and is invalid when the approximate location function is enabled (only the **ohos.permission.APPROXIMATELY\_LOCATION** permission is enabled).

The specified value must be greater than or equal to **0**. The default value is **0**.

If **scenario** is set to **NAVIGATION**, **TRAJECTORY\_TRACKING**, or **CAR\_HAILING** or **priority** is set to **ACCURACY**, you are advised to set **maxAccuracy** to a value greater than **10**.

If scenario is set to **DAILY\_LIFE\_SERVICE** or **NO\_POWER** or **priority** is set to **LOW\_POWER** or **FIRST\_FIX**, you are advised to set **maxAccuracy** to a value greater than **100**.

 |

#### CurrentLocationRequest(deprecated)

Defines a location request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/5kA8cp5MQT-vpwAJgp9_VA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FC015E7DD0D35E9391CCDDBEB8F036AA1C6FC679D03F0E800E7BB088A9D4E88A)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.CurrentLocationRequest](../../ohos-geolocationmanager-geolocation-manager/document.md#currentlocationrequest).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| priority | [LocationRequestPriority](#locationrequestprioritydeprecated) | No | Yes | Priority of the location request. For details about the value range, see [LocationRequestPriority](#locationrequestprioritydeprecated). |
| scenario | [LocationRequestScenario](#locationrequestscenariodeprecated) | No | Yes | Scenario of the location request. For details about the value range, see [LocationRequestScenario](#locationrequestscenariodeprecated). |
| maxAccuracy | number | No | Yes | 
Location accuracy, in meters.

This parameter is valid only when the precise location function is enabled (both the **ohos.permission.APPROXIMATELY\_LOCATION** and **ohos.permission.LOCATION** permissions are granted), and is invalid when the approximate location function is enabled (only the **ohos.permission.APPROXIMATELY\_LOCATION** permission is enabled).

The specified value must be greater than or equal to **0**. The default value is **0**.

If **scenario** is set to **NAVIGATION**, **TRAJECTORY\_TRACKING**, or **CAR\_HAILING** or **priority** is set to **ACCURACY**, you are advised to set **maxAccuracy** to a value greater than **10**.

If scenario is set to **DAILY\_LIFE\_SERVICE** or **NO\_POWER** or **priority** is set to **LOW\_POWER** or **FIRST\_FIX**, you are advised to set **maxAccuracy** to a value greater than **100**.

 |
| timeoutMs | number | No | Yes | Timeout duration, in milliseconds. The minimum value is **1000**. The value must be greater than or equal to **1000**. |

#### SatelliteStatusInfo(deprecated)

Defines the satellite status information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/vsQnbfwFRWyG7dtQwU4DrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B8A84A05CBD37C707471B90CEF89A6DA3AFFE41ACF5A2314AEFBA37657B758D)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.SatelliteStatusInfo](../../ohos-geolocationmanager-geolocation-manager/document.md#satellitestatusinfo).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| satellitesNumber | number | No | No | Number of satellites. The value must be greater than or equal to **0**. |
| satelliteIds | Array<number> | No | No | Array of satellite IDs. The value must be greater than or equal to **0**. |
| carrierToNoiseDensitys | Array<number> | No | No | Carrier-to-noise density ratio, that is, **cn0**. The value must be greater than **0**. |
| altitudes | Array<number> | No | No | Satellite altitude angle information. The value ranges from **\-90** to **90**, in degrees. |
| azimuths | Array<number> | No | No | Azimuth information. The value ranges from **0** to **360**, in degrees. |
| carrierFrequencies | Array<number> | No | No | Carrier frequency. The value must be greater than or equal to **0**, in Hz. |

#### CachedGnssLocationsRequest(deprecated)

Represents a request for reporting cached GNSS locations.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/8iKEr2GDRqemNlAoeeqXLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BAE49660611BFE083F4EE25A8A13F1C02C3FA604EF0A15C128BB21DD401FE39)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.CachedGnssLocationsRequest](../../ohos-geolocationmanager-geolocation-manager/document.md#cachedgnsslocationsrequest).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Gnss

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| reportingPeriodSec | number | No | No | Interval for reporting the cached GNSS locations, in milliseconds. The value must be greater than **0**. |
| wakeUpCacheQueueFull | boolean | No | No | 
**true**: reports the cached GNSS locations to the application when the cache queue is full.

**false**: discards the cached GNSS locations when the cache queue is full.

 |

#### Geofence(deprecated)

Defines a GNSS geofence. Currently, only circular geofences are supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/p32cFNTiRWKk_b1XRWaGVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31E0FCD7CBDB43E388F63A7F76076C99A2CCA6D186625708067E40D42394C2A9)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.Geofence](../../ohos-geolocationmanager-geolocation-manager/document.md#geofence).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geofence

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| latitude | number | No | No | Latitude information. The value ranges from **\-90** to **90**. |
| longitude | number | No | No | Longitude information. The value ranges from **\-180** to **180**. |
| radius | number | No | No | Radius of a circular geofence. The value must be greater than **0**, in meters. |
| expiration | number | No | No | Expiration period of a geofence, in milliseconds. The value must be greater than **0**. |

#### GeofenceRequest(deprecated)

Defines a geofence request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/Ed2ve0KMTEWya7BgaLpwYA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E6F3FB7E6FC5FBB6F1FCF967218A82A85EBAE6D21F4A51049A73B1B0CAAA8BB)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.GeofenceRequest](../../ohos-geolocationmanager-geolocation-manager/document.md#geofencerequest).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Geofence

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| priority | [LocationRequestPriority](#locationrequestprioritydeprecated) | No | No | Priority of the location information. |
| scenario | [LocationRequestScenario](#locationrequestscenariodeprecated) | No | No | Location scenario. |
| geofence | [Geofence](#geofencedeprecated) | No | No | Geofence information. |

#### LocationCommand(deprecated)

Defines a location command.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/QCnkD1mdRG-nC4a70ex2-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=273FB50CE02331FC6AD34097BA0FBA92CA4221C69B56DCC78ADCC1D4F567C4C2)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use [geoLocationManager.LocationCommand](../../ohos-geolocationmanager-geolocation-manager/document.md#locationcommand).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scenario | [LocationRequestScenario](#locationrequestscenariodeprecated) | No | No | Location scenario. |
| command | string | No | No | Extended command, in the string format. |

#### Location(deprecated)

Defines location information.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/AZFNPKSfSkaWYs_W9_HViw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=425A110A53A67D3B660581FA29363A310D91C6E6BB09F2514019CA9E8436D31A)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.Location](../../ohos-geolocationmanager-geolocation-manager/document.md#location).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| latitude7+ | number | No | No | Latitude information. A positive value indicates north latitude, and a negative value indicates south latitude. The value ranges from **\-90** to **90**. |
| longitude7+ | number | No | No | Longitude information. A positive value indicates east longitude , and a negative value indicates west longitude. The value ranges from **\-180** to **180**. |
| altitude7+ | number | No | No | Location altitude, in meters. |
| accuracy7+ | number | No | No | Location accuracy, in meters. |
| speed7+ | number | No | No | Speed, in m/s. |
| timeStamp7+ | number | No | No | Location timestamp in the UTC format. |
| direction7+ | number | No | No | Direction information. The value ranges from **0** to **360**, in degrees. |
| timeSinceBoot7+ | number | No | No | Location timestamp since boot. |
| additions7+ | Array<string> | No | Yes | Additional description. |
| additionSize7+ | number | No | Yes | Number of additional descriptions. The value must be greater than or equal to **0**. |

#### LocationPrivacyType(deprecated)

Defines the privacy statement type.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/iAAUgpThTEu41C_dnifT5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A8198BC35D107C42AEFDFDAB9A22ABBC824F720953F35E8C487B33B61D782691)

This API is supported since API version 8.

This API is deprecated since API version 9. You are advised to use **geoLocationManager.LocationPrivacyType**, which is available only for system applications.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| OTHERS | 0 | Other scenarios. Reserved field. |
| STARTUP | 1 | Privacy statement displayed in the startup wizard. |
| CORE\_LOCATION | 2 | Privacy statement displayed when enabling the location service. |

#### LocationRequestPriority(deprecated)

Sets the priority of a location request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/ckFnWseGRdG76ZQIwgUxtg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D00184014E0C307AC2BAD46E8C291675B5D251517EAAD482421F915EF1F88379)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.LocationRequestPriority](../../ohos-geolocationmanager-geolocation-manager/document.md#locationrequestpriority).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSET | 0x200 | 
Priority unspecified.

If this option is used, [LocationRequestPriority](#locationrequestprioritydeprecated) is invalid.

 |
| ACCURACY | 0x201 | 

Location accuracy preferred.

This policy mainly uses the GNSS positioning technology. In an open area, the technology can achieve the meter-level location accuracy, depending on the hardware performance of the device. However, in a shielded environment, the location accuracy may significantly decrease.

 |
| LOW\_POWER | 0x202 | 

Power efficiency preferred.

This policy mainly uses the base station positioning, WLAN positioning, and Bluetooth positioning technologies to obtain device location in both indoor and outdoor scenarios. The location accuracy depends on the distribution of surrounding base stations, visible WLANs, and Bluetooth devices and therefore may fluctuate greatly. This policy is recommended and can reduce power consumption when your application does not require high location accuracy or when base stations, visible WLANs, and Bluetooth devices are densely distributed.

 |
| FIRST\_FIX | 0x203 | 

Fast location preferred. Use this option if you want to obtain a location as fast as possible.

This policy uses the GNSS positioning, base station positioning, WLAN positioning, and Bluetooth positioning technologies simultaneously to obtain the device location in both the indoor and outdoor scenarios. When all positioning technologies provide a location result, the system provides the most accurate location result for your application. It can lead to significant hardware resource consumption and power consumption.

 |

#### LocationRequestScenario(deprecated)

Defines the location scenario in a location request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/bHEb_v4MR7CzZEvjHNfxoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E22268AAE4F1E3528212E3C7C40C96252B204286915443123C5EE1148FA3C067)

This API is deprecated since API version 9. You are advised to use [geoLocationManager.LocationRequestScenario](../../ohos-geolocationmanager-geolocation-manager/document.md#locationrequestscenario).

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| UNSET | 0x300 | 
Scenario unspecified.

If this option is used, [LocationRequestScenario](#locationrequestscenariodeprecated) is invalid.

 |
| NAVIGATION | 0x301 | 

Navigation scenario.

This option is applicable when your application needs to obtain the real-time location of a mobile device outdoors, such as navigation for driving or walking.

In this scenario, GNSS positioning is used to provide location services to ensure the optimal location accuracy of the system.

The location result is reported at a minimum interval of 1 second by default.

 |
| TRAJECTORY\_TRACKING | 0x302 | 

Trajectory tracking scenario.

This option is applicable when your application needs to record user trajectories, for example, the track recording function of sports applications. In this scenario, the GNSS positioning technology is mainly used to ensure the location accuracy.

The location result is reported at a minimum interval of 1 second by default.

 |
| CAR\_HAILING | 0x303 | 

Ride hailing scenario.

This option is applicable when your application needs to obtain the current location of a user who is hailing a taxi.

The location result is reported at a minimum interval of 1 second by default.

 |
| DAILY\_LIFE\_SERVICE | 0x304 | 

Daily life service scenario.

This option is applicable when your application only needs the approximate user location for recommendations and push notifications in scenarios such as when the user is browsing news, shopping online, and ordering food.

The location result is reported at a minimum interval of 1 second by default.

 |
| NO\_POWER | 0x305 | 

Power efficiency scenario.

This option is applicable when your application does not proactively start the location service. When responding to another application requesting the same location service, the system marks a copy of the location result to your application. In this way, your application will not consume extra power for obtaining the user location.

 |

#### GeoLocationErrorCode(deprecated)

Enumerates error codes of the location service.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/q-PKs8zkQYiKwDlzpnSxJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062510Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F270A7D1C51C81E1BA814ABF132280FDA1FCF13AE2BBB2A10DEEC2A17BE85BCE)

This API is deprecated since API version 9. You are advised to use [Location Kit Error Codes](../../../error-codes/location-kit-error-codes/document.md) instead.

**Required permissions**: ohos.permission.LOCATION

**System capability**: SystemCapability.Location.Location.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| INPUT\_PARAMS\_ERROR7+ | 101 | Incorrect input parameters. |
| REVERSE\_GEOCODE\_ERROR7+ | 102 | Failed to call the reverse geocoding API. |
| GEOCODE\_ERROR7+ | 103 | Failed to call the geocoding API. |
| LOCATOR\_ERROR7+ | 104 | Failed to obtain the location. |
| LOCATION\_SWITCH\_ERROR7+ | 105 | Failed to change the location service switch. |
| LAST\_KNOWN\_LOCATION\_ERROR7+ | 106 | Failed to obtain the previous location. |
| LOCATION\_REQUEST\_TIMEOUT\_ERROR7+ | 107 | Failed to obtain the location within the specified time. |
