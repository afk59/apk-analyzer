# Geocoding and Reverse Geocoding (ArkTS)

#### Scenario

Describing a location using coordinates is accurate, but neither intuitive nor user-friendly. To address this issue, the system provides your application the geocoding and reverse geocoding capabilities:

-   Geocoding: converts geographic descriptions into specific coordinates.
    
-   Reverse geocoding: converts coordinates into geographic descriptions.
    

The geocoding information describes a location using several attributes, including the country, administrative region, street, house number, and address, etc.

#### Available APIs

The following table lists the APIs used for mutual conversion between coordinates and geographic descriptions. For details, see [Location Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager).

| API | Description |
| :-- | :-- |
| [isGeocoderAvailable(): boolean](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanagerisgeocoderavailable) | Checks whether the geocoding and reverse geocoding services are available. |
| [getAddressesFromLocation(request: ReverseGeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanagergetaddressesfromlocation) | Converts coordinates into geographic descriptions through reverse geocoding. This API uses an asynchronous callback to return the result. |
| [getAddressesFromLocationName(request: GeoCodeRequest, callback: AsyncCallback<Array<GeoAddress>>): void](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanagergetaddressesfromlocationname) | Converts geographic descriptions into coordinates through geocoding. This API uses an asynchronous callback to return the result. |

#### How to Develop

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/GK-8x5RDR4KYz4oAsM8w2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=350CAB7CE1990EC09595601071B3096E2B78942822E748DF1FEFDCA67F0E6914)

The geocoding and reverse geocoding services need to access backend services to obtain information. Therefore, before performing the following steps, ensure that your device is connected to the network.

1.  Import the **geoLocationManager** module. All geocoding and reverse geocoding APIs are provided by this module.
    
    import { geoLocationManager } from '@kit.LocationKit';
    
2.  Check whether the geocoding and reverse geocoding services are available.
    
    -   Call **isGeocoderAvailable** to check whether the geocoding and reverse geocoding services are available. If yes, go to step 3. If the services are unavailable, the device does not have the geocoding and reverse geocoding capabilities. Do not use related APIs.
        
        import { geoLocationManager } from '@kit.LocationKit';
        try {
            let isAvailable = geoLocationManager.isGeocoderAvailable();
        } catch (err) {
            console.error("errCode:" + JSON.stringify(err));
        }
        
3.  Obtain the geocoding conversion result.
    
    -   Call **getAddressesFromLocation** to convert coordinates into geographical location information. Your application can obtain the list of [GeoAddress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#geoaddress) objects that match the specified coordinates and then read location information from it.
        
        let reverseGeocodeRequest:geoLocationManager.ReverseGeoCodeRequest = {"latitude": 31.12, "longitude": 121.11, "maxItems": 1};
        try {
            geoLocationManager.getAddressesFromLocation(reverseGeocodeRequest, (err, data) => {
                if (err) {
                    console.error('getAddressesFromLocation err: ' + JSON.stringify(err));
                } else {
                    console.info('getAddressesFromLocation data: ' + JSON.stringify(data));
                }
            });
        } catch (err) {
            console.error("errCode:" + JSON.stringify(err));
        }
        
    -   Call **getAddressesFromLocationName** to convert the location description into coordinates.
        
        let geocodeRequest:geoLocationManager.GeoCodeRequest = {"description": "No. xx, xx Road, Pudong District, Shanghai", "maxItems": 1};
        try {
            geoLocationManager.getAddressesFromLocationName(geocodeRequest, (err, data) => {
                if (err) {
                    console.error('getAddressesFromLocationName err: ' + JSON.stringify(err));
                } else {
                    console.info('getAddressesFromLocationName data: ' + JSON.stringify(data));
                }
            });
        } catch (err) {
            console.error("errCode:" + JSON.stringify(err));
        }
        
        Your application can obtain the list of [GeoAddress](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#geoaddress) objects that match the specified location description and then read coordinates from it.
        
        If the location description contains duplicate location names, you can call [GeoCodeRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#geocoderequest) to specify a longitude and latitude range to narrow down the scope.
