# @system.sensor (Sensor)

The **Sensor** module provides APIs for querying the sensor list, subscribing to or unsubscribing from sensor data, and executing control commands.

The sensors are classified into the following categories based on their functions: motion, environment, orientation, light, body, and other categories (such as Hall effect sensors). Each category includes different sensor types. A sensor type may be a single hardware sensor or a composite of multiple hardware sensors.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/UwgnZaYySyq6U7OlWelEaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=743E7DE7E92C9F484C1314D8D1DCB10B560927AA9DC7B4F572E6AED794DEEB2B)

-   Module maintenance policy:
    -   For lite wearables, this module is constantly maintained and available.
    -   For other device types, this module is no longer maintained since API version 8, and you are advised to use the new [@ohos.sensor](../ohos-sensor-sensor/document.md) module.
-   The initial APIs of this module are supported since API version 3. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This module requires hardware support and can only be debugged on real devices.

#### Modules to Import

import { Sensor } from '@kit.SensorServiceKit';

#### Sensor.subscribeAccelerometer

subscribeAccelerometer(options: subscribeAccelerometerOptions): void

Subscribes to data changes of the acceleration sensor. If this API is called multiple times for the same application, the last call takes effect.

Except for lite wearables, you are advised to use [ACCELEROMETER](../ohos-sensor-sensor/document.md#accelerometer9) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.ACCELEROMETER (a system permission)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [subscribeAccelerometerOptions](#subscribeaccelerometeroptions) | Yes | Type of data to return. |

**Example**

import { Sensor, AccelerometerResponse, subscribeAccelerometerOptions } from '@kit.SensorServiceKit';

let accelerometerOptions: subscribeAccelerometerOptions = {
  interval: 'normal',
  success: (ret: AccelerometerResponse) => {
    console.info('Succeeded in subscribing. X-axis data: ' + ret.x);
    console.info('Succeeded in subscribing. Y-axis data: ' + ret.y);
    console.info('Succeeded in subscribing. Z-axis data: ' + ret.z);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.subscribeAccelerometer(accelerometerOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/VOPnUlQuRnKeVUuBntl2mw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D1A0C0AA82E5BDC35102A25E4FC431BA4773ED978777D12D1B3DDB193A45F83B)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeAccelerometer

unsubscribeAccelerometer(): void

Unsubscribes from data changes of the acceleration sensor.

Except for lite wearables, you are advised to use [ACCELEROMETER](../ohos-sensor-sensor/document.md#accelerometerdeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.ACCELEROMETER (a system permission)

**Example**

Sensor.unsubscribeAccelerometer();

#### Sensor.subscribeCompass

subscribeCompass(options: SubscribeCompassOptions): void

Subscribes to data changes of the compass sensor. If this API is called multiple times for the same application, the last call takes effect.

Except for lite wearables, you are advised to use [ORIENTATION](../ohos-sensor-sensor/document.md#orientationdeprecated) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeCompassOptions](#subscribecompassoptions) | Yes | Type of data to return. |

**Example**

import { Sensor, CompassResponse, SubscribeCompassOptions } from '@kit.SensorServiceKit';

let subscribeCompassOptions: SubscribeCompassOptions = {
  success: (ret: CompassResponse) => {
    console.info('Succeeded in subscribing. Get data direction:' + ret.direction);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.subscribeCompass(subscribeCompassOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/Q_DrzrWhSJKTn5LusX47Dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A89EC1EEED7F75DDD0A46B1D3C4110E6BD702DEDC2E5380B132D8CD16392E97)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeCompass

unsubscribeCompass(): void

Unsubscribes from data changes of the compass sensor.

Except for lite wearables, you are advised to use [ORIENTATION](../ohos-sensor-sensor/document.md#orientationdeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Example**

Sensor.unsubscribeCompass();

#### Sensor.subscribeProximity

subscribeProximity(options: SubscribeProximityOptions): void

Subscribes to data changes of the proximity sensor. If this API is called multiple times for the same application, the last call takes effect.

Except for lite wearables, you are advised to use [PROXIMITY](../ohos-sensor-sensor/document.md#proximitydeprecated) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeProximityOptions](#subscribeproximityoptions) | Yes | Type of data to return. |

**Example**

import { Sensor, ProximityResponse, SubscribeProximityOptions } from '@kit.SensorServiceKit';

let subscribeProximityOptions: SubscribeProximityOptions = {
  success: (ret: ProximityResponse) => {
    console.info('Succeeded in subscribing. Get data distance:' + ret.distance);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.subscribeProximity(subscribeProximityOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/6Eh9t9VkQQKZQ8pIYREVog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B08C8FABB521128B10FF5B36C871CAD3E03D7CF8CE065B2B0B16B3BEC07E5E65)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeProximity

unsubscribeProximity(): void

Unsubscribes from data changes of the proximity sensor.

Except for lite wearables, you are advised to use [PROXIMITY](../ohos-sensor-sensor/document.md#proximitydeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

**Example**

Sensor.unsubscribeProximity();

#### Sensor.subscribeLight

subscribeLight(options: SubscribeLightOptions): void

Subscribes to data changes of the ambient light sensor. If this API is called multiple times, the last call takes effect.

Except for lite wearables, you are advised to use [AMBIENT\_LIGHT](../ohos-sensor-sensor/document.md#ambient_lightdeprecated) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeLightOptions](#subscribelightoptions) | Yes | Type of data to return. |

**Example**

import { Sensor, LightResponse, SubscribeLightOptions } from '@kit.SensorServiceKit';

let subscribeLightOptions: SubscribeLightOptions = {
  success: (ret: LightResponse) => {
    console.info('Succeeded in subscribing. Get data intensity:' + ret.intensity);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.subscribeLight(subscribeLightOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/TE_R508fSjuSBb4WUnnTxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BAD9CF078FE41D9C4018FA2F34D340B4E43D4B37E7BD1E3B1994563162F87280)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeLight

unsubscribeLight(): void

Unsubscribes from data changes of the ambient light sensor.

Except for lite wearables, you are advised to use [AMBIENT\_LIGHT](../ohos-sensor-sensor/document.md#ambient_lightdeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

**Example**

Sensor.unsubscribeLight();

#### Sensor.subscribeStepCounter

subscribeStepCounter(options: SubscribeStepCounterOptions): void

Subscribes to data changes of the step counter sensor. If this API is called multiple times for the same application, the last call takes effect.

Except for lite wearables, you are advised to use [PEDOMETER](../ohos-sensor-sensor/document.md#pedometerdeprecated) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeStepCounterOptions](#subscribestepcounteroptions) | Yes | Type of data to return. |

**Example**

import { Sensor, StepCounterResponse, SubscribeStepCounterOptions } from '@kit.SensorServiceKit';

let subscribeStepCounterOptions: SubscribeStepCounterOptions = {
  success: (ret: StepCounterResponse) => {
    console.info('Succeeded in subscribing. Get step value:' + ret.steps);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.subscribeStepCounter(subscribeStepCounterOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/htlqJuZYSQK4ml4kx37Fqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A112C06F124ABF5072997486E3C696B869CDA3AD16B88194B6791FCAE8E84A1E)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeStepCounter

unsubscribeStepCounter(): void

Unsubscribes from data changes of the step counter sensor.

Except for lite wearables, you are advised to use [PEDOMETER](../ohos-sensor-sensor/document.md#pedometerdeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**Example**

Sensor.unsubscribeStepCounter();

#### Sensor.subscribeBarometer

subscribeBarometer(options: SubscribeBarometerOptions): void

Subscribes to data changes of the barometer sensor. If this API is called multiple times for the same application, the last call takes effect.

Except for lite wearables, you are advised to use [BAROMETER](../ohos-sensor-sensor/document.md#barometerdeprecated-1) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeBarometerOptions](#subscribebarometeroptions) | Yes | Type of data to return. |

**Example**

import { Sensor, BarometerResponse, SubscribeBarometerOptions } from '@kit.SensorServiceKit';

let subscribeBarometerOptions: SubscribeBarometerOptions = {
  success: (ret: BarometerResponse) => {
    console.info('Succeeded in subscribing. Get data value:' + ret.pressure);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.subscribeBarometer(subscribeBarometerOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/oJds1WBTQ427kVCxqYXIpA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=91A1ED2DA176D5AAC2DFBC6F0ABAD565A128B7A0F16D59E4D59AB112DB847A2B)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeBarometer

unsubscribeBarometer(): void

Unsubscribes from data changes of the barometer sensor.

Except for lite wearables, you are advised to use [BAROMETER](../ohos-sensor-sensor/document.md#barometerdeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Example**

Sensor.unsubscribeBarometer();

#### Sensor.subscribeHeartRate

subscribeHeartRate(options: SubscribeHeartRateOptions): void

Subscribes to data changes of the heart rate sensor. If this API is called multiple times for the same application, the last call takes effect.

Except for lite wearables, you are advised to use [HEART\_RATE](../ohos-sensor-sensor/document.md#heart_ratedeprecated) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.READ\_HEALTH\_DATA

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeHeartRateOptions](#subscribeheartrateoptions) | Yes | Type of data to return. |

**Example**

import { Sensor, HeartRateResponse, SubscribeHeartRateOptions } from '@kit.SensorServiceKit';

let subscribeHeartRateOptions: SubscribeHeartRateOptions = {
  success: (ret: HeartRateResponse) => {
    console.info('Succeeded in subscribing. Get heartRate value:' + ret.heartRate);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.subscribeHeartRate(subscribeHeartRateOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/ABEiHa-kRjaIQUTd_QZCUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=02735FAC32AE7253FDECB2180745607610E21CEDDAD9D17960671BFA62840B05)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeHeartRate

unsubscribeHeartRate(): void

Unsubscribes from data changes of the heart rate sensor.

Except for lite wearables, you are advised to use [HEART\_RATE](../ohos-sensor-sensor/document.md#heart_ratedeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.READ\_HEALTH\_DATA

**Example**

Sensor.unsubscribeHeartRate();

#### Sensor.subscribeOnBodyState

subscribeOnBodyState(options: SubscribeOnBodyStateOptions): void

Subscribes to wearing status changes of a wearable device. If this API is called multiple times for the same application, the last call takes effect.

Except for lite wearables, you are advised to use [WEAR\_DETECTION](../ohos-sensor-sensor/document.md#wear_detectiondeprecated) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeOnBodyStateOptions](#subscribeonbodystateoptions) | Yes | Type of data to return. |

**Example**

import { Sensor, OnBodyStateResponse, SubscribeOnBodyStateOptions } from '@kit.SensorServiceKit';

let subscribeOnBodyStateOptions: SubscribeOnBodyStateOptions = {
  success: (ret: OnBodyStateResponse) => {
    console.info('Succeeded in subscribing. Get on-body state value:' + ret.value);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.subscribeOnBodyState(subscribeOnBodyStateOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/0FA-m2PTRgyZbeYJBxQ3Og/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=442E0C0A1944FDA193F82AECD5B7ADFC66B065E4871E3D98E902F2768DFD73CE)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeOnBodyState

unsubscribeOnBodyState(): void

Unsubscribes from wearing status changes of a wearable device.

Except for lite wearables, you are advised to use [WEAR\_DETECTION](../ohos-sensor-sensor/document.md#wear_detectiondeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Example**

Sensor.unsubscribeOnBodyState();

#### Sensor.getOnBodyState

getOnBodyState(options: GetOnBodyStateOptions): void

Obtains the wearing state of a wearable device.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [GetOnBodyStateOptions](#getonbodystateoptions) | Yes | Callback invoked when obtaining the wearing state of the device that houses the sensor. |

**Example**

import { Sensor, OnBodyStateResponse, GetOnBodyStateOptions } from '@kit.SensorServiceKit';

let getOnBodyStateOptions: GetOnBodyStateOptions = {
  success: (ret: OnBodyStateResponse) => {
    console.info('Succeeded in subscribing. On body state: ' + ret.value);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  },
};
Sensor.getOnBodyState(getOnBodyStateOptions);

#### Sensor.subscribeDeviceOrientation6+

subscribeDeviceOrientation(options: SubscribeDeviceOrientationOptions): void

Subscribes to data changes of the device orientation sensor.

If this API is called multiple times for the same application, the last call takes effect. However, this API cannot be called multiple times in one click event.

Except for lite wearables, you are advised to use [ORIENTATION](../ohos-sensor-sensor/document.md#orientationdeprecated) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeDeviceOrientationOptions](#subscribedeviceorientationoptions6) | Yes | Type of data to return. |

**Example**

import { Sensor, DeviceOrientationResponse, SubscribeDeviceOrientationOptions } from '@kit.SensorServiceKit';

let subscribeDeviceOrientationOptions: SubscribeDeviceOrientationOptions = {
  interval: 'normal',
  success: (ret: DeviceOrientationResponse) => {
    console.info('Succeeded in subscribing. Alpha data: ' + ret.alpha);
    console.info('Succeeded in subscribing. Beta data: ' + ret.beta);
    console.info('Succeeded in subscribing. Gamma data: ' + ret.gamma);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  }
};
Sensor.subscribeDeviceOrientation(subscribeDeviceOrientationOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/wENGIqP_Rk6H2Qxa1qRvYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=973031B45EAB8DBBB2FE11B8F70DDC63D5F1AB99F449C9D1F64D56232B3346C9)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeDeviceOrientation6+

unsubscribeDeviceOrientation(): void

Unsubscribes from data changes of the device orientation sensor.

Except for lite wearables, you are advised to use [ORIENTATION](../ohos-sensor-sensor/document.md#orientationdeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

**Example**

Sensor.unsubscribeDeviceOrientation();

#### Sensor.subscribeGyroscope6+

subscribeGyroscope(options: SubscribeGyroscopeOptions): void

Subscribes to data changes of the gyroscope sensor.

If this API is called multiple times for the same application, the last call takes effect. However, this API cannot be called multiple times in one click event.

Except for lite wearables, you are advised to use [GYROSCOPE](../ohos-sensor-sensor/document.md#gyroscopedeprecated) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.GYROSCOPE (a system permission)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [SubscribeGyroscopeOptions](#subscribegyroscopeoptions6) | Yes | Type of data to return. |

**Example**

import { Sensor, GyroscopeResponse, SubscribeGyroscopeOptions } from '@kit.SensorServiceKit';

let subscribeGyroscopeOptions: SubscribeGyroscopeOptions = {
  interval: 'normal',
  success: (ret: GyroscopeResponse) => {
    console.info('Succeeded in subscribing. X-axis data: ' + ret.x);
    console.info('Succeeded in subscribing. Y-axis data: ' + ret.y);
    console.info('Succeeded in subscribing. Z-axis data: ' + ret.z);
  },
  fail: (data: string, code: number) => {
    console.error(\`Failed to subscription. Code: ${code}, data: ${data}\`);
  }
};
Sensor.subscribeGyroscope(subscribeGyroscopeOptions);

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/kGgDlGgURJSRedMpD3j59Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E331E4302902468B2FDAC6A842D2DE0E1169DD655FE686C55FFD9D731840B8A9)

To reduce performance overhead, you are advised to unsubscribe from the sensor data in the **onDestroy** callback.

#### Sensor.unsubscribeGyroscope6+

unsubscribeGyroscope(): void

Unsubscribes from data changes of the gyroscope sensor.

Except for lite wearables, you are advised to use [GYROSCOPE](../ohos-sensor-sensor/document.md#gyroscopedeprecated-2) since API Version 8.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.GYROSCOPE (a system permission)

**Example**

Sensor.unsubscribeGyroscope();

#### subscribeAccelerometerOptions

Defines the type of data to return for a subscription to data changes of the acceleration sensor.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.ACCELEROMETER

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| interval | string | Yes | 
Execution frequency of the callback for returning the acceleration sensor data.

The default value is **normal**. The options are as follows:

\- **game**: called at an interval of 20 ms, which is applicable to gaming scenarios.

\- **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios.

\- **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.

 |
| success | [AccelerometerResponse](#accelerometerresponse) | Yes | Callback invoked when the acceleration sensor data changes. |
| fail | Function | No | Callback invoked when an API call fails. |

#### AccelerometerResponse

Defines the callback invoked when the acceleration sensor data changes.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Required permissions**: ohos.permission.ACCELEROMETER

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Acceleration on the x-axis. |
| y | number | Yes | Acceleration on the y-axis. |
| z | number | Yes | Acceleration on the z-axis. |

#### SubscribeCompassOptions

Defines the type of data to return for a subscription to data changes of the compass sensor.

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | [CompassResponse](#compassresponse) | Yes | Callback invoked when the compass sensor data changes. |
| fail | Function | No | Callback invoked when an API call fails. |

#### CompassResponse

Defines a **CompassResponse** object.

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| direction | number | Yes | Direction of the device, in degrees. |

#### SubscribeProximityOptions

Defines the type of data to return for a subscription to data changes of the proximity sensor.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | [ProximityResponse](#proximityresponse) | Yes | Defines a **ProximityResponse** object. |
| fail | Function | No | Callback invoked when an API call fails. |

#### ProximityResponse

Callback invoked when the proximity sensor data changes.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| distance | number | Yes | Distance between a visible object and the device screen. |

#### SubscribeLightOptions

Defines the type of data to return for a subscription to data changes of the ambient light sensor.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | [LightResponse](#lightresponse) | Yes | Callback invoked when the ambient light sensor data changes. |
| fail | Function | No | Callback invoked when an API call fails. |

#### LightResponse

Defines a **LightResponse** object.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| intensity | number | Yes | Light intensity, in lux. |

#### SubscribeStepCounterOptions

Defines the type of data to return for a subscription to data changes of the step counter sensor.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | [StepCounterResponse](#stepcounterresponse) | Yes | Defines a **StepCounterResponse** object. |
| fail | Function | No | Callback invoked when an API call fails. |

#### StepCounterResponse

Callback invoked when the step counter sensor data changes.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| steps | number | Yes | Number of counted steps after the sensor is restarted. |

#### SubscribeBarometerOptions

Defines the type of data to return for a subscription to data changes of the barometer sensor.

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | [BarometerResponse](#barometerresponse) | Yes | Callback invoked when the barometer sensor data changes. |
| fail | Function | No | Callback invoked when an API call fails. |

#### BarometerResponse

Defines a **BarometerResponse** object.

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| pressure | number | Yes | Pressure, in pascal. |

#### SubscribeHeartRateOptions

Defines the type of data to return for a subscription to data changes of the heart rate sensor.

**Required permissions**: ohos.permission.READ\_HEALTH\_DATA

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | [HeartRateResponse](#heartrateresponse) | Yes | Callback invoked when the heart rate sensor data changes. This callback is invoked every five seconds. |
| fail | Function | No | Callback invoked when an API call fails. |

#### HeartRateResponse

Defines a **HeartRateResponse** object.

**Required permissions**: ohos.permission.READ\_HEALTH\_DATA

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| heartRate | number | Yes | Heart rate. |

#### SubscribeOnBodyStateOptions

Defines the callback invoked upon change in the wearing state of the device that houses the sensor.

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | [OnBodyStateResponse](#onbodystateresponse) | Yes | Callback invoked when the wearing state of the device that houses the sensor is successfully obtained. |
| fail | Function | No | Callback invoked when an API call fails. |

#### OnBodyStateResponse

Specifies whether the device that houses the sensor is worn.

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | boolean | Yes | Boolean value indicating whether the device is worn. The value **true** indicates that the device is worn, and the value **false** indicates the opposite. |

#### GetOnBodyStateOptions

Defines the callback for obtaining the wearing state of the device that houses the sensor.

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| success | [OnBodyStateResponse](#onbodystateresponse) | Yes | Callback upon a successful API call. |
| fail | Function | No | Callback invoked when an API call fails. |
| complete | Function | No | Callback invoked when the API call is complete. |

#### SubscribeDeviceOrientationOptions6+

Defines the type of data to return for a subscription to data changes of the device orientation sensor.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| interval | string | Yes | 
Interval at which the callback is invoked to return the device orientation sensor data.

The default value is **normal**. The options are as follows:

\- **game**: called at an interval of 20 ms, which is applicable to gaming scenarios.

\- **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios.

\- **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.

 |
| success | [DeviceOrientationResponse](#deviceorientationresponse6) | Yes | Callback invoked when the device orientation sensor data changes. |
| fail | Function | No | Callback invoked when an API call fails. |

#### DeviceOrientationResponse6+

Defines a **DeviceOrientationResponse** object.

**System capability**: SystemCapability.Sensors.Sensor.Lite

**Device behavior differences**: This API has no effect on lite wearables, but works properly on other devices.

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| alpha | number | Yes | Rotation angle around the Z axis when the X/Y axis of the device coincides with the X/Y axis of the earth. |
| beta | number | Yes | Rotation angle around the X axis when the Y/Z axis of the device coincides with the Y/Z axis of the earth. |
| gamma | number | Yes | Rotation angle around the Y axis when the X/Z axis of the device coincides with the X/Z axis of the earth. |

#### SubscribeGyroscopeOptions6+

Defines the type of data to return for a subscription to data changes of the gyroscope sensor.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| interval | string | Yes | 
Interval at which the callback is invoked to return the gyroscope sensor data.

The default value is **normal**. The options are as follows:

\- **game**: called at an interval of 20 ms, which is applicable to gaming scenarios.

\- **ui**: called at an interval of 60 ms, which is applicable to UI updating scenarios.

\- **normal**: called at an interval of 200 ms, which is applicable to power-saving scenarios.

 |
| success | [GyroscopeResponse](#gyroscoperesponse6) | Yes | Callback invoked when the gyroscope sensor data changes. |
| fail | Function | No | Callback invoked when an API call fails. |

#### GyroscopeResponse6+

Defines a **GyroscopeResponse** object.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor.Lite

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| x | number | Yes | Rotation angular velocity of the X axis. |
| y | number | Yes | Rotation angular velocity of the Y axis. |
| z | number | Yes | Rotation angular velocity of the Z axis. |
