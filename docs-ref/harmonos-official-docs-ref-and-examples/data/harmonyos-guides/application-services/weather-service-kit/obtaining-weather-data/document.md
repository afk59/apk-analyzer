# Obtaining Weather Data

Weather Service Kit can obtain weather data, such as real-time weather data and alert data, based on the longitude and latitude data you provide.

#### Restrictions

This kit supports phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.0(18), wearables are also supported.

#### (Optional) Obtaining Longitude and Latitude Information

To query the weather data of the current location, you need to [apply for location permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#applying-for-permissions) and obtain the latitude and longitude information of the current location. Specific steps are as follows:

1.  Import required modules.
    
    import { geoLocationManager } from '@kit.LocationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call [getCurrentLocation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#geolocationmanagergetcurrentlocation-2) to obtain the longitude and latitude information.
    
    geoLocationManager.getCurrentLocation().then((result) => {
      console.info('current location latitude: ' + result.latitude);
      console.info('current location longitude: ' + result.longitude);
    }).catch((err: BusinessError ) => {
      console.error(\`getCurrentLocation failed. Code: ${err.code}, message: ${err.message}\`);
    });
    

#### Querying Weather Data

After you provide the longitude and latitude data (accurate to two decimal places), Weather Service Kit returns the gridded weather data.

1.  Import required modules.
    
    import { weatherService } from '@kit.WeatherServiceKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Build a request object.
    
    -   **location**: Provide the [current location data](#section546501255) or the longitude and latitude of the place to be queried.
    -   **limitedDatasets**: optional. Pass an array to request limited datasets. For details about the value range, refer to weatherService.[Dataset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/weather-service-weatherservice#section83091727192814).
    
    let request: weatherService.WeatherRequest = {
      location: {
        latitude: 22.62,
        longitude: 114.07
      },
      limitedDatasets: \[weatherService.Dataset.CURRENT, weatherService.Dataset.ALERTS\]
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/x6Gw7laXQLKCzR-zGmTkEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062123Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA5A3D53E1DDEF7FA86507D1B63E05E19DE0BA8C6CE34484D39A64E4AF431A29)
    
    If **limitedDatasets** is not set or is empty, all data supported by Weather Service Kit is returned by default. You can set **limitedDatasets** based on the weather data your need, so that the API request latency is greatly reduced.
    
3.  Request data.
    
    try {
      let weather = await weatherService.getWeather(request);
      if (weather.current) {
        console.info('getWeather current temperature: ' + weather.current.temperature);
      }
      if (weather.alerts?.length) {
        console.info('getWeather alert: ' + weather.alerts\[0\].title);
      }
    } catch (err) {
      err = err as BusinessError;
      console.error(\`getWeather failed. Code: ${err.code}, message: ${err.message}\`);
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/4GrSw9RwREqgtN2gTmXSSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062123Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AE0A9A3B2575A6D396633D44F043BCBB4FCD8AE6EDE42995098CB2C8E718011)
    
    The use of the **getWeather** API depends on the context of the current ability. If you request weather data in an environment where the context cannot be obtained through the [getHostContext()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#gethostcontext12) API, for example, in the **Worker** or **TaskPool** child thread environment, use the [weatherService.getWeatherWithContext(context, request)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/weather-service-weatherservice#section25641843201511) method and provide the context information of the ability.
