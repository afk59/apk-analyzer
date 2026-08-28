# @ohos.sensor (Sensor)

The **Sensor** module provides APIs for obtaining the sensor list and subscribing to sensor data. It also provides some common sensor algorithms.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/VWZ9MwUIS82vsEVyYbp0Ig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9593916C88666C956D88AAD2B8ED3611F0E3B3E2CB56E3B08BF09F1FAC58BAAD)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version. Before subscribing to sensor data, call [getSingleSensor](#sensorgetsinglesensor9) to obtain the target sensor. For details about how to use the API, see [Sensor Development](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/sensor-guidelines#how-to-develop). If any error occurs, see the error code description of the API. When you subscribe to the sensor data, ensure that the **on** and **off** APIs are used in pairs.

#### Modules to Import

import { sensor } from '@kit.SensorServiceKit';

#### sensor.on

#### \[h2\]ACCELEROMETER9+

on(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>, options?: Options): void

Subscribes to data of the acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER**. |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | Yes | Callback used to report the sensor data, which is an **AccelerometerResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.ACCELEROMETER);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]FUSION\_PRESSURE22+

on(type: SensorId.FUSION\_PRESSURE, callback: Callback<FusionPressureResponse>, options?: Options): void

Subscribes to the fused pressure sensor data.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).FUSION\_PRESSURE | Yes | Sensor type. The value is fixed at SensorId.FUSION\_PRESSURE. |
| callback | Callback<[FusionPressureResponse](#fusionpressureresponse22)\> | Yes | Callback used to report the sensor data, which is a **FusionPressureResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.FUSION\_PRESSURE, (data: sensor.FusionPressureResponse) => {
    console.info('Succeeded in invoking on. fusionPressure: ' + data.fusionPressure);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.FUSION\_PRESSURE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ACCELEROMETER\_UNCALIBRATED9+

on(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void

Subscribes to data of the uncalibrated acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER\_UNCALIBRATED**. |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | Yes | Callback used to report the sensor data, which is an **AccelerometerUncalibratedResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.ACCELEROMETER\_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.ACCELEROMETER\_UNCALIBRATED);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]AMBIENT\_LIGHT9+

on(type: SensorId.AMBIENT\_LIGHT, callback: Callback<LightResponse>, options?: Options): void

Subscribes to data of the ambient light sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_LIGHT | Yes | Sensor type. The value is fixed at **SensorId.AMBIENT\_LIGHT**. |
| callback | Callback<[LightResponse](#lightresponse)\> | Yes | Callback used to report the sensor data, which is a **LightResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.AMBIENT\_LIGHT, (data: sensor.LightResponse) => {
    console.info('Succeeded in getting the ambient light intensity: ' + data.intensity);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.AMBIENT\_LIGHT);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]AMBIENT\_TEMPERATURE9+

on(type: SensorId.AMBIENT\_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>, options?: Options): void

Subscribes to data of the ambient temperature sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_TEMPERATURE | Yes | Sensor type. The value is fixed at **SensorId.AMBIENT\_TEMPERATURE**. |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | Yes | Callback used to report the sensor data, which is an **AmbientTemperatureResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.AMBIENT\_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
    console.info('Succeeded in invoking on. Temperature: ' + data.temperature);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.AMBIENT\_TEMPERATURE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]BAROMETER9+

on(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>, options?: Options): void

Subscribes to data of the barometer sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).BAROMETER | Yes | Sensor type. The value is fixed at **SensorId.BAROMETER**. |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | Yes | Callback used to report the sensor data, which is a **BarometerResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.BAROMETER, (data: sensor.BarometerResponse) => {
    console.info('Succeeded in invoking on. Atmospheric pressure: ' + data.pressure);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.BAROMETER);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GRAVITY9+

on(type: SensorId.GRAVITY, callback: Callback<GravityResponse>, options?: Options): void

Subscribes to data of the gravity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GRAVITY | Yes | Sensor type. The value is fixed at **SensorId.GRAVITY**. |
| callback | Callback<[GravityResponse](#gravityresponse)\> | Yes | Callback used to report the sensor data, which is a **GravityResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.GRAVITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GYROSCOPE9+

on(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options): void

Subscribes to data of the gyroscope sensor.

**Required permissions**: ohos.permission.GYROSCOPE

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE | Yes | Sensor type. The value is fixed at **SensorId.GYROSCOPE**. |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | Yes | Callback used to report the sensor data, which is a **GyroscopeResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.GYROSCOPE, (data: sensor.GyroscopeResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.GYROSCOPE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GYROSCOPE\_UNCALIBRATED9+

on(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>, options?: Options): void

Subscribes to data of the uncalibrated gyroscope sensor.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.GYROSCOPE\_UNCALIBRATED**. |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | Yes | Callback used to report the sensor data, which is a **GyroscopeUncalibratedResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.GYROSCOPE\_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.GYROSCOPE\_UNCALIBRATED);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HALL9+

on(type: SensorId.HALL, callback: Callback<HallResponse>, options?: Options): void

Subscribes to data of the Hall effect sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HALL | Yes | Sensor type. The value is fixed at **SensorId.HALL**. |
| callback | Callback<[HallResponse](#hallresponse)\> | Yes | Callback used to report the sensor data, which is a **HallResponse** object. |
| options | [Options](#options) | No | List of optional parameters. The default value is 200,000,000 ns. This parameter is used to set the data reporting frequency when Hall effect events are frequently triggered. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.HALL, (data: sensor.HallResponse) => {
    console.info('Succeeded in invoking on. Hall status: ' + data.status);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HALL);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HEART\_RATE9+

on(type: SensorId.HEART\_RATE, callback: Callback<HeartRateResponse>, options?: Options): void

Subscribes to data of the heart rate sensor.

**Required permissions**: ohos.permission.READ\_HEALTH\_DATA

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HEART\_RATE | Yes | Sensor type. The value is fixed at **SensorId.HEART\_RATE**. |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | Yes | Callback used to report the sensor data, which is a **HeartRateResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.HEART\_RATE, (data: sensor.HeartRateResponse) => {
    console.info('Succeeded in invoking on. Heart rate: ' + data.heartRate);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HEART\_RATE);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HUMIDITY9+

on(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>, options?: Options): void

Subscribes to data of the humidity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HUMIDITY | Yes | Sensor type. The value is fixed at **SensorId.HUMIDITY**. |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | Yes | Callback used to report the sensor data, which is a **HumidityResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.HUMIDITY, (data: sensor.HumidityResponse) => {
    console.info('Succeeded in invoking on. Humidity: ' + data.humidity);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.HUMIDITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]LINEAR\_ACCELEROMETER9+

on(type: SensorId.LINEAR\_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>, options?: Options): void

Subscribes to data of the linear acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).LINEAR\_ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.LINEAR\_ACCELEROMETER**. |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | Yes | Callback used to report the sensor data, which is a **LinearAccelerometerResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.LINEAR\_ACCELEROMETER, (data: sensor.LinearAccelerometerResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.LINEAR\_ACCELEROMETER);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]MAGNETIC\_FIELD9+

on(type: SensorId.MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>, options?: Options): void

Subscribes to data of the magnetic field sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC\_FIELD**. |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | Yes | Callback used to report the sensor data, which is a **MagneticFieldResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.MAGNETIC\_FIELD, (data: sensor.MagneticFieldResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.MAGNETIC\_FIELD);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED9+

on(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void

Subscribes to data of the uncalibrated magnetic field sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC\_FIELD\_UNCALIBRATED**. |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | Yes | Callback used to report the sensor data, which is a **MagneticFieldUncalibratedResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.MAGNETIC\_FIELD\_UNCALIBRATED);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ORIENTATION9+

on(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void

Subscribes to data of the orientation sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/wqDImKeRTy29VGbphuW1xw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E1896EB222543A35BE08511CF7CE435F9BC56C3B8BF3FB1D3AD62F6B7879CCCF)

Applications or services invoking this API can prompt users to use figure-8 calibration to improve the accuracy of the direction sensor. The sensor has a theoretical error of ±5 degrees, but the specific precision may vary depending on different driver implementations and algorithmic designs.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ORIENTATION | Yes | Sensor type. The value is fixed at **SensorId.ORIENTATION**. |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | Yes | Callback used to report the sensor data, which is a **OrientationResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
    console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
    console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
    console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.ORIENTATION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PEDOMETER9+

on(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>, options?: Options): void

Subscribes to data of the pedometer sensor. The step counter sensor's data reporting is subject to some delay, and the delay is determined by specific product implementations.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER**. |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | Yes | Callback used to report the sensor data, which is a **PedometerResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.PEDOMETER, (data: sensor.PedometerResponse) => {
    console.info('Succeeded in invoking on. Step count: ' + data.steps);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.PEDOMETER);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PEDOMETER\_DETECTION9+

on(type: SensorId.PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options): void

Subscribes to data of the pedometer detection sensor.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER\_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER\_DETECTION**. |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | Yes | Callback used to report the sensor data, which is a **PedometerDetectionResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.PEDOMETER\_DETECTION, (data: sensor.PedometerDetectionResponse) => {
    console.info('Succeeded in invoking on. Pedometer scalar: ' + data.scalar);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.PEDOMETER\_DETECTION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PROXIMITY9+

on(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>, options?: Options): void

Subscribes to data of the proximity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PROXIMITY | Yes | Sensor type. The value is fixed at **SensorId.PROXIMITY**. |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | Yes | Callback used to report the sensor data, which is a **ProximityResponse** object. |
| options | [Options](#options) | No | List of optional parameters. The default value is 200,000,000 ns. This parameter is used to set the data reporting frequency when proximity sensor events are frequently triggered. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.PROXIMITY, (data: sensor.ProximityResponse) => {
    console.info('Succeeded in invoking on. Distance: ' + data.distance);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.PROXIMITY);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ROTATION\_VECTOR9+

on(type: SensorId.ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>, options?: Options): void

Subscribes to data of the rotation vector sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ROTATION\_VECTOR | Yes | Sensor type. The value is fixed at **SensorId.ROTATION\_VECTOR**. |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | Yes | Callback used to report the sensor data, which is a **RotationVectorResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.ROTATION\_VECTOR, (data: sensor.RotationVectorResponse) => {
    console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking on. Scalar quantity: ' + data.w);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.ROTATION\_VECTOR);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]SIGNIFICANT\_MOTION9+

on(type: SensorId.SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options): void

Subscribes to the significant motion sensor data.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).SIGNIFICANT\_MOTION | Yes | Sensor type. The value is fixed at **SensorId.SIGNIFICANT\_MOTION**. |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | Yes | Callback used to report the sensor data, which is a **SignificantMotionResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.SIGNIFICANT\_MOTION, (data: sensor.SignificantMotionResponse) => {
    console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.SIGNIFICANT\_MOTION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]WEAR\_DETECTION9+

on(type: SensorId.WEAR\_DETECTION, callback: Callback<WearDetectionResponse>, options?: Options): void

Subscribes to data of the wear detection sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).WEAR\_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.WEAR\_DETECTION**. |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | Yes | Callback used to report the sensor data, which is a **WearDetectionResponse** object. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3.Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.WEAR\_DETECTION, (data: sensor.WearDetectionResponse) => {
    console.info('Succeeded in invoking on. Wear status: ' + data.value);
  }, { interval: 100000000 });
  setTimeout(() => {
    sensor.off(sensor.SensorId.WEAR\_DETECTION);
  }, 500);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]sensorStatusChange19+

on(type: 'sensorStatusChange', callback: Callback<SensorStatusEvent>): void

Enables listening for sensor status changes. This API asynchronously returns the result through a callback.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'sensorStatusChange' | Yes | Event type. The value **sensorStatusChange** indicates the sensor status change event. |
| callback | Callback<[SensorStatusEvent](#sensorstatusevent19)\> | Yes | Callback used to return the sensor status change event. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.on('sensorStatusChange', (data: sensor.SensorStatusEvent) => {
    console.info('sensorStatusChange : ' + JSON.stringify(data));
  });
  setTimeout(() => {
    sensor.off('sensorStatusChange');
  }, 5000);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.once9+

#### \[h2\]ACCELEROMETER9+

once(type: SensorId.ACCELEROMETER, callback: Callback<AccelerometerResponse>): void

Obtains data of the acceleration sensor once.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER**. |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | Yes | Callback used to report the sensor data, which is an **AccelerometerResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ACCELEROMETER\_UNCALIBRATED9+

once(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback: Callback<AccelerometerUncalibratedResponse>): void

Obtains data of the uncalibrated acceleration sensor once.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER\_UNCALIBRATED**. |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | Yes | Callback used to report the sensor data, which is an **AccelerometerUncalibratedResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.ACCELEROMETER\_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]AMBIENT\_LIGHT9+

once(type: SensorId.AMBIENT\_LIGHT, callback: Callback<LightResponse>): void

Obtains data of the ambient light sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_LIGHT | Yes | Sensor type. The value is fixed at **SensorId.AMBIENT\_LIGHT**. |
| callback | Callback<[LightResponse](#lightresponse)\> | Yes | Callback used to report the sensor data, which is a **LightResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.AMBIENT\_LIGHT, (data: sensor.LightResponse) => {
    console.info('Succeeded in invoking once. the ambient light intensity: ' + data.intensity);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]AMBIENT\_TEMPERATURE9+

once(type: SensorId.AMBIENT\_TEMPERATURE, callback: Callback<AmbientTemperatureResponse>): void

Obtains data of the temperature sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_TEMPERATURE | Yes | Sensor type. The value is fixed at **SensorId.AMBIENT\_TEMPERATURE**. |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | Yes | Callback used to report the sensor data, which is an **AmbientTemperatureResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.AMBIENT\_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
    console.info('Succeeded in invoking once. Temperature: ' + data.temperature);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]BAROMETER9+

once(type: SensorId.BAROMETER, callback: Callback<BarometerResponse>): void

Obtains data of the barometer sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).BAROMETER | Yes | Sensor type. The value is fixed at **SensorId.BAROMETER**. |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | Yes | Callback used to report the sensor data, which is a **BarometerResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.BAROMETER, (data: sensor.BarometerResponse) => {
    console.info('Succeeded in invoking once. Atmospheric pressure: ' + data.pressure);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GRAVITY9+

once(type: SensorId.GRAVITY, callback: Callback<GravityResponse>): void

Obtains data of the gravity sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GRAVITY | Yes | Sensor type. The value is fixed at **SensorId.GRAVITY**. |
| callback | Callback<[GravityResponse](#gravityresponse)\> | Yes | Callback used to report the sensor data, which is a **GravityResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.GRAVITY, (data: sensor.GravityResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GYROSCOPE9+

once(type: SensorId.GYROSCOPE, callback: Callback<GyroscopeResponse>): void

Obtains data of the gyroscope sensor once.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE | Yes | Sensor type. The value is fixed at **SensorId.GYROSCOPE**. |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | Yes | Callback used to report the sensor data, which is a **GyroscopeResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.GYROSCOPE, (data: sensor.GyroscopeResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GYROSCOPE\_UNCALIBRATED9+

once(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback: Callback<GyroscopeUncalibratedResponse>): void

Obtains data of the uncalibrated gyroscope sensor once.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.GYROSCOPE\_UNCALIBRATED**. |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | Yes | Callback used to report the sensor data, which is a **GyroscopeUncalibratedResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.GYROSCOPE\_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HALL9+

once(type: SensorId.HALL, callback: Callback<HallResponse>): void

Obtains data of the Hall effect sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HALL | Yes | Sensor type. The value is fixed at **SensorId.HALL**. |
| callback | Callback<[HallResponse](#hallresponse)\> | Yes | Callback used to report the sensor data, which is a **HallResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.HALL, (data: sensor.HallResponse) => {
    console.info('Succeeded in invoking once. Status: ' + data.status);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HEART\_RATE9+

once(type: SensorId.HEART\_RATE, callback: Callback<HeartRateResponse>): void

Obtains data of the heart rate sensor once.

**Required permissions**: ohos.permission.READ\_HEALTH\_DATA

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HEART\_RATE | Yes | Sensor type. The value is fixed at **SensorId.HEART\_RATE**. |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | Yes | Callback used to report the sensor data, which is a **HeartRateResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.HEART\_RATE, (data: sensor.HeartRateResponse) => {
    console.info('Succeeded in invoking once. Heart rate: ' + data.heartRate);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HUMIDITY9+

once(type: SensorId.HUMIDITY, callback: Callback<HumidityResponse>): void

Obtains data of the humidity sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HUMIDITY | Yes | Sensor type. The value is fixed at **SensorId.HUMIDITY**. |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | Yes | Callback used to report the sensor data, which is a **HumidityResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.HUMIDITY, (data: sensor.HumidityResponse) => {
    console.info('Succeeded in invoking once. Humidity: ' + data.humidity);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]LINEAR\_ACCELEROMETER9+

once(type: SensorId.LINEAR\_ACCELEROMETER, callback: Callback<LinearAccelerometerResponse>): void

Obtains data of the linear acceleration sensor once.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).LINEAR\_ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.LINEAR\_ACCELEROMETER**. |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | Yes | Callback used to report the sensor data, which is a **LinearAccelerometerResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.LINEAR\_ACCELEROMETER, (data: sensor.LinearAccelerometerResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]MAGNETIC\_FIELD9+

once(type: SensorId.MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>): void

Obtains data of the magnetic field sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC\_FIELD**. |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | Yes | Callback used to report the sensor data, which is a **MagneticFieldResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.MAGNETIC\_FIELD, (data: sensor.MagneticFieldResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED9+

once(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback: Callback<MagneticFieldUncalibratedResponse>): void

Obtains data of the uncalibrated magnetic field sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC\_FIELD\_UNCALIBRATED**. |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | Yes | Callback used to report the sensor data, which is a **MagneticFieldUncalibratedResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ORIENTATION9+

once(type: SensorId.ORIENTATION, callback: Callback<OrientationResponse>): void

Obtains data of the orientation sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ORIENTATION | Yes | Sensor type. The value is fixed at **SensorId.ORIENTATION**. |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | Yes | Callback used to report the sensor data, which is a **OrientationResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.ORIENTATION, (data: sensor.OrientationResponse) => {
    console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
    console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
    console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PEDOMETER9+

once(type: SensorId.PEDOMETER, callback: Callback<PedometerResponse>): void

Obtains data of the pedometer sensor once. The step counter sensor's data reporting is subject to some delay, and the delay is determined by specific product implementations.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER**. |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | Yes | Callback used to report the sensor data, which is a **PedometerResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.PEDOMETER, (data: sensor.PedometerResponse) => {
    console.info('Succeeded in invoking once. Step count: ' + data.steps);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PEDOMETER\_DETECTION9+

once(type: SensorId.PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>): void

Obtains data of the pedometer sensor once.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER\_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER\_DETECTION**. |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | Yes | Callback used to report the sensor data, which is a **PedometerDetectionResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.PEDOMETER\_DETECTION, (data: sensor.PedometerDetectionResponse) => {
    console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PROXIMITY9+

once(type: SensorId.PROXIMITY, callback: Callback<ProximityResponse>): void

Obtains data of the proximity sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PROXIMITY | Yes | Sensor type. The value is fixed at **SensorId.PROXIMITY**. |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | Yes | Callback used to report the sensor data, which is a **ProximityResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.PROXIMITY, (data: sensor.ProximityResponse) => {
    console.info('Succeeded in invoking once. Distance: ' + data.distance);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ROTATION\_VECTOR9+

once(type: SensorId.ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>): void

Obtains data of the rotation vector sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ROTATION\_VECTOR | Yes | Sensor type. The value is fixed at **SensorId.ROTATION\_VECTOR**. |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | Yes | Callback used to report the sensor data, which is a **RotationVectorResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.ROTATION\_VECTOR, (data: sensor.RotationVectorResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. Scalar quantity: ' + data.w);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]SIGNIFICANT\_MOTION9+

once(type: SensorId.SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>): void

Obtains the significant motion sensor data once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).SIGNIFICANT\_MOTION | Yes | Sensor type. The value is fixed at **SensorId.SIGNIFICANT\_MOTION**. |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | Yes | Callback used to report the sensor data, which is a **SignificantMotionResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.SIGNIFICANT\_MOTION, (data: sensor.SignificantMotionResponse) => {
    console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]WEAR\_DETECTION9+

once(type: SensorId.WEAR\_DETECTION, callback: Callback<WearDetectionResponse>): void

Obtains data of the wear detection sensor once.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).WEAR\_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.WEAR\_DETECTION**. |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | Yes | Callback used to report the sensor data, which is a **WearDetectionResponse** object. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.once(sensor.SensorId.WEAR\_DETECTION, (data: sensor.WearDetectionResponse) => {
    console.info('Succeeded in invoking once. Wear status: ' + data.value);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke once. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.off

#### \[h2\]ACCELEROMETER9+

off(type: SensorId.ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void

Unsubscribes from data of the acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER**. |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.ACCELEROMETER, callback1);
  sensor.on(sensor.SensorId.ACCELEROMETER, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.ACCELEROMETER, callback1);
  // Unsubscribe from all callbacks of the SensorId.ACCELEROMETER type.
  sensor.off(sensor.SensorId.ACCELEROMETER);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ACCELEROMETER19+

off(type: SensorId.ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerResponse>): void

Unsubscribes from data of the acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.AccelerometerResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.ACCELEROMETER;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]ACCELEROMETER\_UNCALIBRATED9+

off(type: SensorId.ACCELEROMETER\_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>): void

Unsubscribes from data of the uncalibrated acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER\_UNCALIBRATED**. |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.ACCELEROMETER\_UNCALIBRATED, callback1);
  sensor.on(sensor.SensorId.ACCELEROMETER\_UNCALIBRATED, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.ACCELEROMETER\_UNCALIBRATED, callback1);
  // Unsubscribe from all callbacks of the SensorId.ACCELEROMETER\_UNCALIBRATED type.
  sensor.off(sensor.SensorId.ACCELEROMETER\_UNCALIBRATED);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]FUSION\_PRESSURE22+

off(type: SensorId.FUSION\_PRESSURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<FusionPressureResponse>): void

Unsubscribes from the fused pressure sensor data.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).FUSION\_PRESSURE | Yes | Sensor type. The value is fixed at SensorId.FUSION\_PRESSURE. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[FusionPressureResponse](#fusionpressureresponse22)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.FusionPressureResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.FUSION\_PRESSURE;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]ACCELEROMETER\_UNCALIBRATED19+

off(type: SensorId.ACCELEROMETER\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<AccelerometerUncalibratedResponse>): void

Unsubscribes from data of the uncalibrated acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ACCELEROMETER\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.ACCELEROMETER\_UNCALIBRATED**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.AccelerometerUncalibratedResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.ACCELEROMETER\_UNCALIBRATED;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]AMBIENT\_LIGHT9+

off(type: SensorId.AMBIENT\_LIGHT, callback?: Callback<LightResponse>): void

Unsubscribes from data of the ambient light sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_LIGHT | Yes | Sensor type. The value is fixed at **SensorId.AMBIENT\_LIGHT**. |
| callback | Callback<[LightResponse](#lightresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.AMBIENT\_LIGHT, callback1);
  sensor.on(sensor.SensorId.AMBIENT\_LIGHT, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.AMBIENT\_LIGHT, callback1);
  // Unsubscribe from all callbacks of the SensorId.AMBIENT\_LIGHT type.
  sensor.off(sensor.SensorId.AMBIENT\_LIGHT);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]AMBIENT\_LIGHT19+

off(type: SensorId.AMBIENT\_LIGHT, sensorInfoParam?: SensorInfoParam, callback?: Callback<LightResponse>): void

Unsubscribes from data of the ambient light sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_LIGHT | Yes | Sensor type. The value is fixed at **SensorId.AMBIENT\_LIGHT**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[LightResponse](#lightresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.LightResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.AMBIENT\_LIGHT;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]AMBIENT\_TEMPERATURE9+

off(type: SensorId.AMBIENT\_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>): void

Unsubscribes from data of the ambient temperature sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_TEMPERATURE | Yes | Sensor type. The value is fixed at **SensorId.AMBIENT\_TEMPERATURE**. |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.AMBIENT\_TEMPERATURE, callback1);
  sensor.on(sensor.SensorId.AMBIENT\_TEMPERATURE, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.AMBIENT\_TEMPERATURE, callback1);
  // Unsubscribe from all callbacks of the SensorId.AMBIENT\_TEMPERATURE type.
  sensor.off(sensor.SensorId.AMBIENT\_TEMPERATURE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]AMBIENT\_TEMPERATURE19+

off(type: SensorId.AMBIENT\_TEMPERATURE, sensorInfoParam?: SensorInfoParam, callback?: Callback<AmbientTemperatureResponse>): void

Unsubscribes from data of the ambient temperature sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).AMBIENT\_TEMPERATURE | Yes | Sensor type. The value is fixed at **SensorId.AMBIENT\_TEMPERATURE**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.AmbientTemperatureResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.AMBIENT\_TEMPERATURE;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]BAROMETER9+

off(type: SensorId.BAROMETER, callback?: Callback<BarometerResponse>): void

Unsubscribes from data of the barometer sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).BAROMETER | Yes | Sensor type. The value is fixed at **SensorId.BAROMETER**. |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
    console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
    console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
    sensor.on(sensor.SensorId.BAROMETER, callback1);
    sensor.on(sensor.SensorId.BAROMETER, callback2);
    // Unsubscribe from callback1.
    sensor.off(sensor.SensorId.BAROMETER, callback1);
    // Unsubscribe from all callbacks of the SensorId.BAROMETER type.
    sensor.off(sensor.SensorId.BAROMETER);
} catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]BAROMETER19+

off(type: SensorId.BAROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<BarometerResponse>): void

Unsubscribes from data of the barometer sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).BAROMETER | Yes | Sensor type. The value is fixed at **SensorId.BAROMETER**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.BarometerResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.BAROMETER;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]GRAVITY9+

off(type: SensorId.GRAVITY, callback?: Callback<GravityResponse>): void

Unsubscribes from data of the gravity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GRAVITY | Yes | Sensor type. The value is fixed at **SensorId.GRAVITY**. |
| callback | Callback<[GravityResponse](#gravityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.GRAVITY, callback1);
  sensor.on(sensor.SensorId.GRAVITY, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.GRAVITY, callback1);
  // Unsubscribe from all callbacks of the SensorId.GRAVITY type.
  sensor.off(sensor.SensorId.GRAVITY);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GRAVITY19+

off(type: SensorId.GRAVITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<GravityResponse>): void

Unsubscribes from data of the gravity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GRAVITY | Yes | Sensor type. The value is fixed at **SensorId.GRAVITY**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[GravityResponse](#gravityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.GravityResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.GRAVITY;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]GYROSCOPE9+

off(type: SensorId.GYROSCOPE, callback?: Callback<GyroscopeResponse>): void

Unsubscribes from data of the gyroscope sensor.

**Required permissions**: ohos.permission.GYROSCOPE

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE | Yes | Sensor type. The value is fixed at **SensorId.GYROSCOPE**. |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.GYROSCOPE, callback1);
  sensor.on(sensor.SensorId.GYROSCOPE, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.GYROSCOPE, callback1);
  // Unsubscribe from all callbacks of the SensorId.GYROSCOPE type.
  sensor.off(sensor.SensorId.GYROSCOPE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GYROSCOPE19+

off(type: SensorId.GYROSCOPE, sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeResponse>): void

Unsubscribes from data of the gyroscope sensor.

**Required permissions**: ohos.permission.GYROSCOPE

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE | Yes | Sensor type. The value is fixed at **SensorId.GYROSCOPE**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.GyroscopeResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.GYROSCOPE;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]GYROSCOPE\_UNCALIBRATED9+

off(type: SensorId.GYROSCOPE\_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void

Unsubscribes from data of the uncalibrated gyroscope sensor.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.GYROSCOPE\_UNCALIBRATED**. |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.GYROSCOPE\_UNCALIBRATED, callback1);
  sensor.on(sensor.SensorId.GYROSCOPE\_UNCALIBRATED, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.GYROSCOPE\_UNCALIBRATED, callback1);
  // Unsubscribe from all callbacks of the SensorId.GYROSCOPE\_UNCALIBRATED type.
  sensor.off(sensor.SensorId.GYROSCOPE\_UNCALIBRATED);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]GYROSCOPE\_UNCALIBRATED19+

off(type: SensorId.GYROSCOPE\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<GyroscopeUncalibratedResponse>): void

Unsubscribes from data of the uncalibrated gyroscope sensor.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).GYROSCOPE\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.GYROSCOPE\_UNCALIBRATED**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.GyroscopeUncalibratedResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.GYROSCOPE\_UNCALIBRATED;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]HALL9+

off(type: SensorId.HALL, callback?: Callback<HallResponse>): void

Unsubscribes from data of the Hall effect sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HALL | Yes | Sensor type. The value is fixed at **SensorId.HALL**. |
| callback | Callback<[HallResponse](#hallresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.HALL, callback1);
  sensor.on(sensor.SensorId.HALL, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.HALL, callback1);
  // Unsubscribe from all callbacks of the SensorId.HALL type.
  sensor.off(sensor.SensorId.HALL);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HALL19+

off(type: SensorId.HALL, sensorInfoParam?: SensorInfoParam, callback?: Callback<HallResponse>): void

Unsubscribes from data of the Hall effect sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HALL | Yes | Sensor type. The value is fixed at **SensorId.HALL**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[HallResponse](#hallresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.HallResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.HALL;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]HEART\_RATE9+

off(type: SensorId.HEART\_RATE, callback?: Callback<HeartRateResponse>): void

Unsubscribes from data of the heart rate sensor.

**Required permissions**: ohos.permission.READ\_HEALTH\_DATA

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HEART\_RATE | Yes | Sensor type. The value is fixed at **SensorId.HEART\_RATE**. |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.HEART\_RATE, callback1);
  sensor.on(sensor.SensorId.HEART\_RATE, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.HEART\_RATE, callback1);
  // Unsubscribe from all callbacks of the SensorId.HEART\_RATE type.
  sensor.off(sensor.SensorId.HEART\_RATE);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HEART\_RATE19+

off(type: SensorId.HEART\_RATE, sensorInfoParam?: SensorInfoParam, callback?: Callback<HeartRateResponse>): void

Unsubscribes from data of the heart rate sensor.

**Required permissions**: ohos.permission.READ\_HEALTH\_DATA

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HEART\_RATE | Yes | Sensor type. The value is fixed at **SensorId.HEART\_RATE**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.HeartRateResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.HEART\_RATE;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]HUMIDITY9+

off(type: SensorId.HUMIDITY, callback?: Callback<HumidityResponse>): void

Unsubscribes from data of the humidity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HUMIDITY | Yes | Sensor type. The value is fixed at **SensorId.HUMIDITY**. |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.HUMIDITY, callback1);
  sensor.on(sensor.SensorId.HUMIDITY, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.HUMIDITY, callback1);
  // Unsubscribe from all callbacks of the SensorId.HUMIDITY type.
  sensor.off(sensor.SensorId.HUMIDITY);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]HUMIDITY19+

off(type: SensorId.HUMIDITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<HumidityResponse>): void

Unsubscribes from data of the humidity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).HUMIDITY | Yes | Sensor type. The value is fixed at **SensorId.HUMIDITY**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.HumidityResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.HUMIDITY;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]LINEAR\_ACCELEROMETER9+

off(type: SensorId.LINEAR\_ACCELEROMETER, callback?: Callback<LinearAccelerometerResponse>): void

Unsubscribes from data of the linear acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).LINEAR\_ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.LINEAR\_ACCELERATION**. |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.LINEAR\_ACCELEROMETER, callback1);
  sensor.on(sensor.SensorId.LINEAR\_ACCELEROMETER, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.LINEAR\_ACCELEROMETER, callback1);
  // Unsubscribe from all callbacks of the SensorId.LINEAR\_ACCELEROMETER type.
  sensor.off(sensor.SensorId.LINEAR\_ACCELEROMETER);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]LINEAR\_ACCELEROMETER19+

off(type: SensorId.LINEAR\_ACCELEROMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<LinearAccelerometerResponse>): void

Unsubscribes from data of the linear acceleration sensor.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).LINEAR\_ACCELEROMETER | Yes | Sensor type. The value is fixed at **SensorId.LINEAR\_ACCELERATION**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.LinearAccelerometerResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.LINEAR\_ACCELEROMETER;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]MAGNETIC\_FIELD9+

off(type: SensorId.MAGNETIC\_FIELD, callback?: Callback<MagneticFieldResponse>): void

Unsubscribes from data of the magnetic field sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC\_FIELD**. |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.MAGNETIC\_FIELD, callback1);
  sensor.on(sensor.SensorId.MAGNETIC\_FIELD, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.MAGNETIC\_FIELD, callback1);
  // Unsubscribe from all callbacks of the SensorId.MAGNETIC\_FIELD type.
  sensor.off(sensor.SensorId.MAGNETIC\_FIELD);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]MAGNETIC\_FIELD19+

off(type: SensorId.MAGNETIC\_FIELD, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldResponse>): void

Unsubscribes from data of the magnetic field sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC\_FIELD**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.MagneticFieldResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.MAGNETIC\_FIELD;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED9+

off(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>): void

Unsubscribes from data of the uncalibrated magnetic field sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC\_FIELD\_UNCALIBRATED**. |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback1);
  sensor.on(sensor.SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, callback1);
  // Unsubscribe from all callbacks of the SensorId.MAGNETIC\_FIELD\_UNCALIBRATED type.
  sensor.off(sensor.SensorId.MAGNETIC\_FIELD\_UNCALIBRATED);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED19+

off(type: SensorId.MAGNETIC\_FIELD\_UNCALIBRATED, sensorInfoParam?: SensorInfoParam, callback?: Callback<MagneticFieldUncalibratedResponse>): void

Unsubscribes from data of the uncalibrated magnetic field sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).MAGNETIC\_FIELD\_UNCALIBRATED | Yes | Sensor type. The value is fixed at **SensorId.MAGNETIC\_FIELD\_UNCALIBRATED**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.MagneticFieldUncalibratedResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.MAGNETIC\_FIELD\_UNCALIBRATED;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]ORIENTATION9+

off(type: SensorId.ORIENTATION, callback?: Callback<OrientationResponse>): void

Unsubscribes from data of the orientation sensor.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ORIENTATION | Yes | Sensor type. The value is fixed at **SensorId.ORIENTATION**. |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.ORIENTATION, callback1);
  sensor.on(sensor.SensorId.ORIENTATION, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.ORIENTATION, callback1);
  // Unsubscribe from all callbacks of the SensorId.ORIENTATION type.
  sensor.off(sensor.SensorId.ORIENTATION);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ORIENTATION19+

off(type: SensorId.ORIENTATION, sensorInfoParam?: SensorInfoParam, callback?: Callback<OrientationResponse>): void

Unsubscribes from data of the orientation sensor.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ORIENTATION | Yes | Sensor type. The value is fixed at **SensorId.ORIENTATION**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.OrientationResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.ORIENTATION;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]PEDOMETER9+

off(type: SensorId.PEDOMETER, callback?: Callback<PedometerResponse>): void

Unsubscribes from data of the pedometer sensor.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER**. |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.PEDOMETER, callback1);
  sensor.on(sensor.SensorId.PEDOMETER, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.PEDOMETER, callback1);
  // Unsubscribe from all callbacks of the SensorId.PEDOMETER type.
  sensor.off(sensor.SensorId.PEDOMETER);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PEDOMETER19+

off(type: SensorId.PEDOMETER, sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerResponse>): void

Unsubscribes from data of the pedometer sensor.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.PedometerResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.PEDOMETER;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]PEDOMETER\_DETECTION9+

off(type: SensorId.PEDOMETER\_DETECTION, callback?: Callback<PedometerDetectionResponse>): void

Unsubscribes from data of the pedometer detection sensor.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER\_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER\_DETECTION**. |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.PEDOMETER\_DETECTION, callback1);
  sensor.on(sensor.SensorId.PEDOMETER\_DETECTION, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.PEDOMETER\_DETECTION, callback1);
  // Unsubscribe from all callbacks of the SensorId.PEDOMETER\_DETECTION type.
  sensor.off(sensor.SensorId.PEDOMETER\_DETECTION);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PEDOMETER\_DETECTION19+

off(type: SensorId.PEDOMETER\_DETECTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<PedometerDetectionResponse>): void

Unsubscribes from data of the pedometer detection sensor.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PEDOMETER\_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.PEDOMETER\_DETECTION**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.PedometerDetectionResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.PEDOMETER\_DETECTION;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]PROXIMITY9+

off(type: SensorId.PROXIMITY, callback?: Callback<ProximityResponse>): void

Unsubscribes from data of the proximity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PROXIMITY | Yes | Sensor type. The value is fixed at **SensorId.PROXIMITY**. |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.PROXIMITY, callback1);
  sensor.on(sensor.SensorId.PROXIMITY, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.PROXIMITY, callback1);
  // Unsubscribe from all callbacks of the SensorId.PROXIMITY type.
  sensor.off(sensor.SensorId.PROXIMITY);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]PROXIMITY19+

off(type: SensorId.PROXIMITY, sensorInfoParam?: SensorInfoParam, callback?: Callback<ProximityResponse>): void

Unsubscribes from data of the proximity sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).PROXIMITY | Yes | Sensor type. The value is fixed at **SensorId.PROXIMITY**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.ProximityResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.PROXIMITY;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]ROTATION\_VECTOR9+

off(type: SensorId.ROTATION\_VECTOR, callback?: Callback<RotationVectorResponse>): void

Unsubscribes from data of the rotation vector sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ROTATION\_VECTOR | Yes | Sensor type. The value is fixed at **SensorId.ROTATION\_VECTOR**. |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.ROTATION\_VECTOR, callback1);
  sensor.on(sensor.SensorId.ROTATION\_VECTOR, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.ROTATION\_VECTOR, callback1);
  // Unsubscribe from all callbacks of the SensorId.ROTATION\_VECTOR type.
  sensor.off(sensor.SensorId.ROTATION\_VECTOR);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]ROTATION\_VECTOR19+

off(type: SensorId.ROTATION\_VECTOR, sensorInfoParam?: SensorInfoParam, callback?: Callback<RotationVectorResponse>): void

Unsubscribes from data of the rotation vector sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).ROTATION\_VECTOR | Yes | Sensor type. The value is fixed at **SensorId.ROTATION\_VECTOR**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.RotationVectorResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.ROTATION\_VECTOR;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]SIGNIFICANT\_MOTION9+

off(type: SensorId.SIGNIFICANT\_MOTION, callback?: Callback<SignificantMotionResponse>): void

Unsubscribes from valid motion sensor data.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).SIGNIFICANT\_MOTION | Yes | Sensor type. The value is fixed at **SensorId.SIGNIFICANT\_MOTION**. |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.SIGNIFICANT\_MOTION, callback1);
  sensor.on(sensor.SensorId.SIGNIFICANT\_MOTION, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.SIGNIFICANT\_MOTION, callback1);
  // Unsubscribe from all callbacks of the SensorId.SIGNIFICANT\_MOTION type.
  sensor.off(sensor.SensorId.SIGNIFICANT\_MOTION);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]SIGNIFICANT\_MOTION19+

off(type: SensorId.SIGNIFICANT\_MOTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<SignificantMotionResponse>): void

Unsubscribes from valid motion sensor data.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).SIGNIFICANT\_MOTION | Yes | Sensor type. The value is fixed at **SensorId.SIGNIFICANT\_MOTION**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.SignificantMotionResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.SIGNIFICANT\_MOTION;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]WEAR\_DETECTION9+

off(type: SensorId.WEAR\_DETECTION, callback?: Callback<WearDetectionResponse>): void

Unsubscribes from data of the wear detection sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).WEAR\_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.WEAR\_DETECTION**. |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

function callback1(data: object) {
  console.info('Succeeded in getting callback1 data: ' + JSON.stringify(data));
}

function callback2(data: object) {
  console.info('Succeeded in getting callback2 data: ' + JSON.stringify(data));
}

// Use try catch to capture possible exceptions.
try {
  sensor.on(sensor.SensorId.WEAR\_DETECTION, callback1);
  sensor.on(sensor.SensorId.WEAR\_DETECTION, callback2);
  // Unsubscribe from callback1.
  sensor.off(sensor.SensorId.WEAR\_DETECTION, callback1);
  // Unsubscribe from all callbacks of the SensorId.WEAR\_DETECTION type.
  sensor.off(sensor.SensorId.WEAR\_DETECTION);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke off. Code: ${e.code}, message: ${e.message}\`);
}

#### \[h2\]WEAR\_DETECTION19+

off(type: SensorId.WEAR\_DETECTION, sensorInfoParam?: SensorInfoParam, callback?: Callback<WearDetectionResponse>): void

Unsubscribes from data of the wear detection sensor.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9).WEAR\_DETECTION | Yes | Sensor type. The value is fixed at **SensorId.WEAR\_DETECTION**. |
| sensorInfoParam | [SensorInfoParam](#sensorinfoparam19) | No | Sensor parameters, including **deviceId** and **sensorIndex**. |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

enum Ret { OK, Failed = -1 }

// Sensor callback
const sensorCallback = (response: sensor.WearDetectionResponse) => {
  console.info(\`callback response: ${JSON.stringify(response)}\`);
}
// Sensor type
const sensorType = sensor.SensorId.WEAR\_DETECTION;
const sensorInfoParam: sensor.SensorInfoParam = { deviceId: -1, sensorIndex: 0 };

function sensorSubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    // Query all sensors.
    const sensorList: sensor.Sensor\[\] = sensor.getSensorListSync();
    if (!sensorList.length) {
      return Ret.Failed;
    }
    // Obtain the target sensor based on the actual service logic.
    const targetSensor = sensorList
      // Filter all sensors with deviceId 1 and sensorId 2 as required. This example is for reference only. You need to adjust the filtering logic accordingly.
      .filter((sensor: sensor.Sensor) => sensor.deviceId === 1 && sensor.sensorId === 2)
      // Select the sensor with sensorIndex 0 among all sensors of the same type.
      .find((sensor: sensor.Sensor) => sensor.sensorIndex === 0);
    if (!targetSensor) {
      return Ret.Failed;
    }
    sensorInfoParam.deviceId = targetSensor.deviceId;
    sensorInfoParam.sensorIndex = targetSensor.sensorIndex;
    // Subscribe to sensor events.
    sensor.on(sensorType, sensorCallback, { sensorInfoParam });
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.on. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

function sensorUnsubscribe(): Ret {
  let ret: Ret = Ret.OK;
  // Use try catch to capture possible exceptions.
  try {
    sensor.off(sensorType, sensorInfoParam, sensorCallback);
  } catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to invoke sensor.off. Code: ${e.code}, message: ${e.message}\`);
    ret = Ret.Failed;
  }
  return ret;
}

#### \[h2\]sensorStatusChange19+

off(type: 'sensorStatusChange', callback?: Callback<SensorStatusEvent>): void

Disables listening for sensor status changes.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'sensorStatusChange' | Yes | Event type. The value **sensorStatusChange** indicates the sensor status change event. |
| callback | Callback<[SensorStatusEvent](#sensorstatusevent19)\> | No | Callback passed to **sensor.on**. If this parameter is left unspecified, listening will be disabled for all callbacks. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  const statusChangeCallback = (data: sensor.SensorStatusEvent) => {
    console.info('sensorStatusChange : ' + JSON.stringify(data));
  }
  const statusChangeCallback2 = (data: sensor.SensorStatusEvent) => {
    console.info('sensorStatusChange2 : ' + JSON.stringify(data));
  }
  // Register two callback listeners for device online events.
  sensor.on('sensorStatusChange', statusChangeCallback);
  sensor.on('sensorStatusChange', statusChangeCallback2);
  
  // Unregister the first listener after 3 seconds.
  setTimeout(() => {
    sensor.off('sensorStatusChange', statusChangeCallback);
  }, 3000);
  // Unregister the other listener after 5 seconds.
  setTimeout(() => {
    sensor.off('sensorStatusChange');
  }, 5000);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to invoke on. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getSensorListByDeviceSync19+

getSensorListByDeviceSync(deviceId?: number): Array<Sensor>

Obtains the information about all sensors on the device.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | No | Device ID. The default value is **\-1**, indicating the local device. You can use [getSensorList](#sensorgetsensorlist9) or [sensorStatusChange](#sensorstatuschange19) to obtain the device ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Sensor](#sensor9)\> | Sensor attribute list. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const deviceId = 1;
  // The first deviceId is optional. By default, it is set to the ID of the local device.
  const sensorList: sensor.Sensor\[\] = sensor.getSensorListByDeviceSync(deviceId);
  console.info(\`sensorList length: ${sensorList.length}\`);
  console.info(\`sensorList: ${JSON.stringify(sensorList)}\`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get sensorList. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getSingleSensorByDeviceSync19+

getSingleSensorByDeviceSync(type: SensorId, deviceId?: number): Array<Sensor>

Obtains information about the sensor of a specific type.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9) | Yes | Sensor type. |
| deviceId | number | No | Device ID. The default value is **\-1**, indicating the local device. You can use [getSensorList](#sensorgetsensorlist9) or [sensorStatusChange](#sensorstatuschange19) to obtain the device ID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Sensor](#sensor9)\> | Sensor attribute list. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  const deviceId = 1;
  // The second deviceId is optional.
  const sensorList: sensor.Sensor\[\] = sensor.getSingleSensorByDeviceSync(sensor.SensorId.ACCELEROMETER, deviceId);
  console.info(\`sensorList length: ${sensorList.length}\`);
  console.info(\`sensorList Json: ${JSON.stringify(sensorList)}\`);
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get sensorList. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getGeomagneticInfo9+

getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void

Obtains the geomagnetic field of a geographic location at a certain time. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locationOptions | [LocationOptions](#locationoptions) | Yes | Geographic location, including the longitude, latitude, and altitude. |
| timeMillis | number | Yes | Time when the magnetic declination is obtained. The value is a Unix timestamp, in ms. |
| callback | AsyncCallback<[GeomagneticResponse](#geomagneticresponse)\> | Yes | Callback used to return the geomagnetic field. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.getGeomagneticInfo({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000,
      (err: BusinessError, data: sensor.GeomagneticResponse) => {
    if (err) {
      console.error(\`Failed to get geomagneticInfo. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info("Succeeded in getting geomagneticInfo x" + data.x);
    console.info("Succeeded in getting geomagneticInfo y" + data.y);
    console.info("Succeeded in getting geomagneticInfo z" + data.z);
    console.info("Succeeded in getting geomagneticInfo geomagneticDip" + data.geomagneticDip);
    console.info("Succeeded in getting geomagneticInfo deflectionAngle" + data.deflectionAngle);
    console.info("Succeeded in getting geomagneticInfo levelIntensity" + data.levelIntensity);
    console.info("Succeeded in getting geomagneticInfo totalIntensity" + data.totalIntensity);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getGeomagneticInfo9+

getGeomagneticInfo(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>

Obtains the geomagnetic field of a geographic location at a certain time. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locationOptions | [LocationOptions](#locationoptions) | Yes | Geographic location, including the longitude, latitude, and altitude. |
| timeMillis | number | Yes | Time when the magnetic declination is obtained. The value is a Unix timestamp, in ms. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GeomagneticResponse](#geomagneticresponse)\> | Promise used to return the geomagnetic field. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  const promise = sensor.getGeomagneticInfo({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000);
  promise.then((data: sensor.GeomagneticResponse) => {
    console.info("Succeeded in getting geomagneticInfo x" + data.x);
    console.info("Succeeded in getting geomagneticInfo y" + data.y);
    console.info("Succeeded in getting geomagneticInfo z" + data.z);
    console.info("Succeeded in getting geomagneticInfo geomagneticDip" + data.geomagneticDip);
    console.info("Succeeded in getting geomagneticInfo deflectionAngle" + data.deflectionAngle);
    console.info("Succeeded in getting geomagneticInfo levelIntensity" + data.levelIntensity);
    console.info("Succeeded in getting geomagneticInfo totalIntensity" + data.totalIntensity);
  }, (err: BusinessError) => {
    console.error(\`Failed to get geomagneticInfo. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get geomagneticInfo. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getDeviceAltitude9+

getDeviceAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void

Obtains the altitude based on the atmospheric pressure. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| seaPressure | number | Yes | Sea-level atmospheric pressure, in hPa. |
| currentPressure | number | Yes | Specified atmospheric pressure, in hPa. |
| callback | AsyncCallback<number> | Yes | Callback used to return the altitude, in meters. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let seaPressure = 1013.2;
  let currentPressure = 1500.0;
  sensor.getDeviceAltitude(seaPressure, currentPressure, (err: BusinessError, data: number) => {
    if (err) {
      console.error(\`Failed to get altitude. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting altitude: ' + data);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get altitude. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getDeviceAltitude9+

getDeviceAltitude(seaPressure: number, currentPressure: number): Promise<number>

Obtains the altitude based on the atmospheric pressure. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| seaPressure | number | Yes | Sea-level atmospheric pressure, in hPa. |
| currentPressure | number | Yes | Specified atmospheric pressure, in hPa. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the altitude, in meters. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let seaPressure = 1013.2;
  let currentPressure = 1500.0;
  const promise = sensor.getDeviceAltitude(seaPressure, currentPressure);
  promise.then((data: number) => {
    console.info('Succeeded in getting sensor\_getDeviceAltitude\_Promise', data);
  }, (err: BusinessError) => {
    console.error(\`Failed to get altitude. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get altitude. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getInclination9+

getInclination(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void

Obtains the magnetic dip based on the inclination matrix. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inclinationMatrix | Array<number> | Yes | Inclination matrix. |
| callback | AsyncCallback<number> | Yes | Callback used to return the magnetic dip, in radians. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // inclinationMatrix can be 3\*3 or 4\*4.
  let inclinationMatrix = \[
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  \]
  sensor.getInclination(inclinationMatrix, (err: BusinessError, data: number) => {
    if (err) {
      console.error(\`Failed to get inclination. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting inclination: ' + data);
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get inclination. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getInclination9+

getInclination(inclinationMatrix: Array<number>): Promise<number>

Obtains the magnetic dip based on the inclination matrix. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inclinationMatrix | Array<number> | Yes | Inclination matrix. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the magnetic dip, in radians. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // inclinationMatrix can be 3\*3 or 4\*4.
  let inclinationMatrix = \[
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  \]
  const promise = sensor.getInclination(inclinationMatrix);
  promise.then((data: number) => {
    console.info('Succeeded in getting inclination: ' + data);
  }, (err: BusinessError) => {
    console.error(\`Failed to get inclination. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get inclination. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getAngleVariation9+

getAngleVariation(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

Obtains the angle change between two rotation matrices. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| currentRotationMatrix | Array<number> | Yes | Current rotation matrix. |
| preRotationMatrix | Array<number> | Yes | The other rotation matrix. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the angle change around the z, x, and y axes. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // The rotation matrix can be 3\*3 or 4\*4.
  let currentRotationMatrix = \[
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  \];
  let preRotationMatrix = \[
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  \];
  sensor.getAngleVariation(currentRotationMatrix, preRotationMatrix, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(\`Failed to get angle variation. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    if (data.length < 3) {
      console.error("Failed to get angle variation, length" + data.length);
      return;
    }
    console.info("Z: " + data\[0\]);
    console.info("X: " + data\[1\]);
    console.info("Y: " + data\[2\]);
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get angle variation. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getAngleVariation9+

getAngleVariation(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>): Promise<Array<number>>

Obtains the angle change between two rotation matrices. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| currentRotationMatrix | Array<number> | Yes | Current rotation matrix. |
| preRotationMatrix | Array<number> | Yes | The other rotation matrix. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the angle change around the z, x, and y axes. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  // The rotation matrix can be 3\*3 or 4\*4.
  let currentRotationMatrix = \[
    1, 0, 0,
    0, 1, 0,
    0, 0, 1
  \];
  let preRotationMatrix = \[
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  \];
  const promise = sensor.getAngleVariation(currentRotationMatrix, preRotationMatrix);
  promise.then((data: Array<number>) => {
    if (data.length < 3) {
      console.error("Failed to get angle variation, length" + data.length);
      return;
    }
    console.info("Z: " + data\[0\]);
    console.info("X: " + data\[1\]);
    console.info("Y: " + data\[2\]);
  }, (err: BusinessError) => {
    console.error(\`Failed to get angle variation. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get angle variation. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getRotationMatrix9+

getRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

Obtains the rotation matrix from a rotation vector. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | Yes | Rotation vector. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the rotation matrix. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let rotationVector = \[0.20046076, 0.21907, 0.73978853, 0.60376877\];
  sensor.getRotationMatrix(rotationVector, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(\`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data\[' + i + '\]: ' + data\[i\]);
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getRotationMatrix9+

getRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>

Obtains the rotation matrix from a rotation vector. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | Yes | Rotation vector. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the rotation matrix. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let rotationVector = \[0.20046076, 0.21907, 0.73978853, 0.60376877\];
  const promise = sensor.getRotationMatrix(rotationVector);
  promise.then((data: Array<number>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data\[' + i + '\]: ' + data\[i\]);
    }
  }, (err: BusinessError) => {
    console.error(\`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.transformRotationMatrix9+

transformRotationMatrix(inRotationVector: Array<number>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<number>>): void

Transforms a rotation vector based on the coordinate system. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inRotationVector | Array<number> | Yes | Rotation vector. |
| coordinates | [CoordinatesOptions](#coordinatesoptions) | Yes | Rotation vector to transform. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the rotation vector after being transformed. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let rotationMatrix = \[
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  \];
  sensor.transformRotationMatrix(rotationMatrix, { x: 1, y: 3 }, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(\`Failed to transform rotationMatrix. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data\[' + i + '\] = ' + data\[i\]);
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to transform rotationMatrix. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.transformRotationMatrix9+

transformRotationMatrix(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>

Transforms a rotation vector based on the coordinate system. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inRotationVector | Array<number> | Yes | Rotation vector. |
| coordinates | [CoordinatesOptions](#coordinatesoptions) | Yes | Rotation vector to transform. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the rotation vector after being transformed. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let rotationMatrix = \[
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  \];
  const promise = sensor.transformRotationMatrix(rotationMatrix, { x: 1, y: 3 });
  promise.then((data: Array<number>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data\[' + i + '\]: ' + data\[i\]);
    }
  }, (err: BusinessError) => {
    console.error(\`Failed to transform rotationMatrix. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to transform rotationMatrix. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getQuaternion9+

getQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

Obtains the quaternion from a rotation vector. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | Yes | Rotation vector. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the quaternion. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let rotationVector = \[0.20046076, 0.21907, 0.73978853, 0.60376877\];
  sensor.getQuaternion(rotationVector, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(\`Failed to get quaternion. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data\[' + i + '\]: ' + data\[i\]);
    }
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get quaternion. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getQuaternion9+

getQuaternion(rotationVector: Array<number>): Promise<Array<number>>

Obtains the quaternion from a rotation vector. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | Yes | Rotation vector. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the quaternion. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
    let rotationVector = \[0.20046076, 0.21907, 0.73978853, 0.60376877\];
    const promise = sensor.getQuaternion(rotationVector);
    promise.then((data: Array<number>) => {
        for (let i = 0; i < data.length; i++) {
            console.info('Succeeded in getting data\[' + i + '\]: ' + data\[i\]);
        }
    }, (err: BusinessError) => {
        console.error(\`Failed to get quaternion. Code: ${err.code}, message: ${err.message}\`);
    });
} catch (error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to get quaternion. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getOrientation9+

getOrientation(rotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

Obtains the device direction based on the rotation matrix. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationMatrix | Array<number> | Yes | Rotation matrix. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the rotation angle around the z, x, and y axes. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let preRotationMatrix = \[
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  \];
  sensor.getOrientation(preRotationMatrix, (err: BusinessError, data: Array<number>) => {
    if (err) {
      console.error(\`Failed to get orientation. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    if (data.length < 3) {
      console.error("Failed to get orientation, length" + data.length);
    }
    console.info("Succeeded in getting data. Z: " + data\[0\]);
    console.info("Succeeded in getting data. X: " + data\[1\]);
    console.info("Succeeded in getting data. Y: " + data\[2\]);
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get orientation. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getOrientation9+

getOrientation(rotationMatrix: Array<number>): Promise<Array<number>>

Obtains the device direction based on the rotation matrix. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationMatrix | Array<number> | Yes | Rotation matrix. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the rotation angle around the z, x, and y axes. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let preRotationMatrix = \[
    1, 0, 0,
    0, 0.87, -0.50,
    0, 0.50, 0.87
  \];
  const promise = sensor.getOrientation(preRotationMatrix);
  promise.then((data: Array<number>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data\[' + i + '\]: ' + data\[i\]);
    }
  }, (err: BusinessError) => {
    console.error(\`Failed to getOrientation. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to getOrientation Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getRotationMatrix9+

getRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void

Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gravity | Array<number> | Yes | Gravity vector. |
| geomagnetic | Array<number> | Yes | Geomagnetic vector. |
| callback | AsyncCallback<[RotationMatrixResponse](#rotationmatrixresponse)\> | Yes | Callback used to return the rotation matrix. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let gravity = \[-0.27775216, 0.5351276, 9.788099\];
  let geomagnetic = \[210.87253, -78.6096, -111.44444\];
  sensor.getRotationMatrix(gravity, geomagnetic, (err: BusinessError, data: sensor.RotationMatrixResponse) => {
    if (err) {
      console.error(\`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting rotationMatrix' + JSON.stringify(data));
  })
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getRotationMatrix9+

getRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>): Promise<RotationMatrixResponse>

Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gravity | Array<number> | Yes | Gravity vector. |
| geomagnetic | Array<number> | Yes | Geomagnetic vector. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RotationMatrixResponse](#rotationmatrixresponse)\> | Promise used to return the rotation matrix. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let gravity = \[-0.27775216, 0.5351276, 9.788099\];
  let geomagnetic = \[210.87253, -78.6096, -111.44444\];
  const promise = sensor.getRotationMatrix(gravity, geomagnetic);
  promise.then((data: sensor.RotationMatrixResponse) => {
    console.info('Succeeded in getting rotationMatrix' + JSON.stringify(data));
  }, (err: BusinessError) => {
    console.error(\`Failed to get rotationMatrix. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get rotationMatrix. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getSensorList9+

getSensorList(callback: AsyncCallback<Array<Sensor>>): void

Obtains information about all sensors on the device. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[Sensor](#sensor9)\>> | Yes | Callback used to return the sensor list. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.getSensorList((err: BusinessError, data: Array<sensor.Sensor>) => {
    if (err) {
      console.error(\`Failed to get sensorList. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data\[' + i + '\]: ' + JSON.stringify(data\[i\]));
    }
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get sensorList. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getSensorList9+

getSensorList(): Promise<Array<Sensor>>

Obtains information about all sensors on the device. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[Sensor](#sensor9)\>> | Promise used to return the sensor list. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.getSensorList().then((data: Array<sensor.Sensor>) => {
    for (let i = 0; i < data.length; i++) {
      console.info('Succeeded in getting data\[' + i + '\]: ' + JSON.stringify(data\[i\]));
    }
  }, (err: BusinessError) => {
    console.error(\`Failed to get sensorList. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get sensorList. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getSensorListSync12+

getSensorListSync(): Array<Sensor>

Obtains information about all sensors on the device. This API returns the result synchronously.

**System capability**: SystemCapability.Sensors.Sensor

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[Sensor](#sensor9)\> | List of sensor attributes. |

**Error codes**

For details about the following error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let ret = sensor.getSensorListSync()
  for (let i = 0; i < ret.length; i++) {
    console.info('Succeeded in getting sensor: ' + JSON.stringify(ret\[i\]));
  }
} catch(error) {
    let e: BusinessError = error as BusinessError;
    console.error(\`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getSingleSensor9+

getSingleSensor(type: SensorId, callback: AsyncCallback<Sensor>): void

Obtains information about the sensor of a specific type. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9) | Yes | Sensor type. |
| callback | AsyncCallback<[Sensor](#sensor9)\> | Yes | Callback used to return the sensor information. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.getSingleSensor(sensor.SensorId.ACCELEROMETER, (err: BusinessError, data: sensor.Sensor) => {
    if (err) {
      console.error(\`Failed to get singleSensor. Code: ${err.code}, message: ${err.message}\`);
      return;
    }
    console.info('Succeeded in getting sensor: ' + JSON.stringify(data));
    sensor.on(sensor.SensorId.ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
      console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
      console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
      console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
    }, { interval: 100000000 });
    setTimeout(() => {
      sensor.off(sensor.SensorId.ACCELEROMETER);
    }, 500);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get singleSensor. Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getSingleSensor9+

getSingleSensor(type: SensorId): Promise<Sensor>

Obtains information about the sensor of a specific type. This API uses a promise to return the result.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9) | Yes | Sensor type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Sensor](#sensor9)\> | Promise used to return the sensor information. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  sensor.getSingleSensor(sensor.SensorId.ACCELEROMETER).then((data: sensor.Sensor) => {
    console.info('Succeeded in getting sensor: ' + JSON.stringify(data));
  }, (err: BusinessError) => {
    console.error(\`Failed to get singleSensor . Code: ${err.code}, message: ${err.message}\`);
  });
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}\`);
}

#### sensor.getSingleSensorSync12+

getSingleSensorSync(type: SensorId): Sensor

Obtains information about the sensor of a specific type. This API returns the result synchronously.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorId](#sensorid9) | Yes | Sensor type. |

**Return value**

| Type | Description |
| :-- | :-- |
| Sensor | Sensor information. |

**Error codes**

For details about the error codes, see [Sensor Error Codes](../../error-codes/sensor-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md). Error codes and error information are reported as exceptions. You need to use **try catch** to capture the exceptions that may occur during an API call.

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error.Possible causes:1. Mandatory parameters are left unspecified;2. Incorrect parameter types;3. Parameter verification failed. |
| 14500101 | Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception. |
| 14500102 | The sensor is not supported by the device. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use try catch to capture possible exceptions.
try {
  let ret = sensor.getSingleSensorSync(sensor.SensorId.ACCELEROMETER);
  console.info('Succeeded in getting sensor: ' + JSON.stringify(ret));
} catch (error) {
  let e: BusinessError = error as BusinessError;
  console.error(\`Failed to get singleSensor . Code: ${e.code}, message: ${e.message}\`);
}

#### SensorId9+

Enumerates the sensor types.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Value | Description |
| :-- | :-- | :-- |
| ACCELEROMETER | 1 | 
Acceleration sensor.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GYROSCOPE | 2 | 

Gyroscope sensor.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| AMBIENT\_LIGHT | 5 | Ambient light sensor. |
| MAGNETIC\_FIELD | 6 | Magnetic field sensor. |
| BAROMETER | 8 | Barometer sensor. |
| HALL | 10 | Hall effect sensor. |
| PROXIMITY | 12 | Proximity sensor. |
| HUMIDITY | 13 | Humidity sensor. |
| ORIENTATION | 256 | 

Orientation sensor.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| GRAVITY | 257 | Gravity sensor. |
| LINEAR\_ACCELEROMETER | 258 | Linear acceleration sensor. |
| ROTATION\_VECTOR | 259 | Rotation vector sensor. |
| AMBIENT\_TEMPERATURE | 260 | Ambient temperature sensor. |
| MAGNETIC\_FIELD\_UNCALIBRATED | 261 | Uncalibrated magnetic field sensor. |
| GYROSCOPE\_UNCALIBRATED | 263 | Uncalibrated gyroscope sensor. |
| SIGNIFICANT\_MOTION | 264 | Significant motion sensor. |
| PEDOMETER\_DETECTION | 265 | Pedometer detection sensor. |
| PEDOMETER | 266 | Pedometer sensor. |
| HEART\_RATE | 278 | Heart rate sensor. |
| WEAR\_DETECTION | 280 | Wear detection sensor. |
| ACCELEROMETER\_UNCALIBRATED | 281 | Uncalibrated acceleration sensor. |
| FUSION\_PRESSURE22+ | 283 | 

Fused pressure sensor.

This sensor is available only on smart watches.

 |

#### SensorInfoParam19+

Defines sensor parameters, including **deviceId** and **sensorIndex**.

**System capability**: SystemCapability.Sensors.Sensor

**Atomic service API**: This API can be used in atomic services since API version 19.

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId | number | No | Yes | 
Device ID. The default value is -1, indicating the local device. You can use [getSensorList](#sensorgetsensorlist9) or [sensorStatusChange](#sensorstatuschange19) to obtain the device ID.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |
| sensorIndex | number | No | Yes | 

Sensor index. The default value is **0**, indicating the default sensor on the device. You can use [getSensorList](#sensorgetsensorlist9) or [sensorStatusChange](#sensorstatuschange19) to obtain the sensor index.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### SensorStatusEvent19+

Defines a device status change event.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timestamp | number | No | No | Timestamp when an event occurs. |
| sensorId | number | No | No | Sensor ID. |
| sensorIndex | number | No | No | Sensor index. |
| isSensorOnline | boolean | No | No | Sensor status. The value **true** indicates that the sensor is online, and the value **false** indicates the opposite. |
| deviceId | number | No | No | Device ID. |
| deviceName | string | No | No | Device name. |

#### SensorAccuracy11+

Enumerates the accuracy levels of sensor data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Value | Description |
| :-- | :-- | :-- |
| ACCURACY\_UNRELIABLE | 0 | The sensor data is unreliable. |
| ACCURACY\_LOW | 1 | The sensor data is at a low accuracy level. |
| ACCURACY\_MEDIUM | 2 | The sensor data is at a medium accuracy level. |
| ACCURACY\_HIGH | 3 | The sensor data is at a high accuracy level. |

#### Response

Describes the timestamp of the sensor data.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| timestamp | number | No | No | Timestamp when the sensor reports data. Time from device startup to data reporting, in nanoseconds. |
| accuracy11+ | [SensorAccuracy](#sensoraccuracy11)11+ | No | No | Accuracy of the sensor data. |

#### Sensor9+

Describes the sensor information.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sensorName | string | No | No | Sensor name. |
| vendorName | string | No | No | Vendor of the sensor. |
| firmwareVersion | string | No | No | Firmware version of the sensor. |
| hardwareVersion | string | No | No | Hardware version of the sensor. |
| sensorId | number | No | No | Sensor type ID. |
| maxRange | number | No | No | Maximum measurement range of the sensor. |
| minSamplePeriod | number | No | No | Minimum sampling period. |
| maxSamplePeriod | number | No | No | Maximum sampling period. |
| precision | number | No | No | Precision of the sensor. |
| power | number | No | No | Estimated sensor power, in mA. |
| sensorIndex19+ | number | No | Yes | Sensor index. |
| deviceId19+ | number | No | Yes | Device ID. |
| deviceName19+ | string | No | Yes | Device name. |
| isLocalSensor19+ | boolean | No | Yes | Whether the sensor is a local sensor. The value **true** indicates a local sensor, and the value **false** indicates the opposite. |

#### AccelerometerResponse

Describes the acceleration sensor data. It extends from [Response](#response).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Acceleration along the x-axis of the device, in m/s². The value is equal to the reported physical quantity. |
| y | number | No | No | Acceleration along the y-axis of the device, in m/s². The value is equal to the reported physical quantity. |
| z | number | No | No | Acceleration along the z-axis of the device, in m/s². The value is equal to the reported physical quantity. |

#### LinearAccelerometerResponse

Describes the linear acceleration sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Linear acceleration along the x-axis of the device, in m/s². |
| y | number | No | No | Linear acceleration along the y-axis of the device, in m/s². |
| z | number | No | No | Linear acceleration along the z-axis of the device, in m/s². |

#### AccelerometerUncalibratedResponse

Describes the uncalibrated acceleration sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Uncalibrated acceleration along the x-axis of the device, in m/s². |
| y | number | No | No | Uncalibrated acceleration along the y-axis of the device, in m/s². |
| z | number | No | No | Uncalibrated acceleration along the z-axis of the device, in m/s². |
| biasX | number | No | No | Uncalibrated acceleration bias along the x-axis of the device, in m/s². |
| biasY | number | No | No | Uncalibrated acceleration bias along the y-axis of the device, in m/s². |
| biasZ | number | No | No | Uncalibrated acceleration bias along the z-axis of the device, in m/s². |

#### FusionPressureResponse22+

Describes the fusion pressure sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fusionPressure | number | No | No | Pressure percentage on the fused pressure sensor, in percentage (%) |

#### GravityResponse

Describes the gravity sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Gravitational acceleration along the x-axis of the device, in m/s². |
| y | number | No | No | Gravitational acceleration along the y-axis of the device, in m/s². |
| z | number | No | No | Gravitational acceleration along the z-axis of the device, in m/s². |

#### OrientationResponse

Describes the orientation sensor data. It extends from [Response](#response).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| alpha | number | No | No | Rotation angle of the device around the z-axis, in degrees. The value ranges from 0 to 360. |
| beta | number | No | No | Rotation angle of the device around the x-axis, in degrees. The value ranges from 0 to ±180. |
| gamma | number | No | No | Rotation angle of the device around the y-axis, in degrees. The value ranges from 0 to ±90. |

#### RotationVectorResponse

Describes the rotation vector sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | X-component of the rotation vector. |
| y | number | No | No | Y-component of the rotation vector. |
| z | number | No | No | Z-component of the rotation vector. |
| w | number | No | No | Scalar, which describes the rotation status of the device relative to a reference direction, in radians |

#### GyroscopeResponse

Describes the gyroscope sensor data. It extends from [Response](#response).

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Angular velocity of rotation around the x-axis of the device, in rad/s. The value is equal to the reported physical quantity. |
| y | number | No | No | Angular velocity of rotation around the y-axis of the device, in rad/s. The value is equal to the reported physical quantity. |
| z | number | No | No | Angular velocity of rotation around the z-axis of the device, in rad/s. The value is equal to the reported physical quantity. |

#### GyroscopeUncalibratedResponse

Describes the uncalibrated gyroscope sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Uncalibrated angular velocity of rotation around the x-axis of the device, in rad/s. |
| y | number | No | No | Uncalibrated angular velocity of rotation around the y-axis of the device, in rad/s. |
| z | number | No | No | Uncalibrated angular velocity of rotation around the z-axis of the device, in rad/s. |
| biasX | number | No | No | Uncalibrated angular velocity bias of rotation around the x-axis of the device, in rad/s. |
| biasY | number | No | No | Uncalibrated angular velocity bias of rotation around the y-axis of the device, in rad/s. |
| biasZ | number | No | No | Uncalibrated angular velocity bias of rotation around the z-axis of the device, in rad/s. |

#### SignificantMotionResponse

Describes the significant motion sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scalar | number | No | No | Intensity of a motion. This parameter specifies whether a device has a significant motion on three physical axes (X, Y, and Z). The value **1** is reported when the device has a significant motion. |

#### ProximityResponse

Describes the proximity sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| distance | number | No | No | Proximity between the visible object and the device monitor. The value **0** means the two are close to each other, and a value greater than 0 means that they are far away from each other. |

#### LightResponse

Describes the ambient light sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| intensity | number | No | No | Illumination, in lux. |
| colorTemperature12+ | number | No | Yes | Color temperature, in Kelvin. This parameter is optional. If this parameter is not supported, a fixed value (customized by the sensor) is returned. If this parameter is supported, a normal value is returned. |
| infraredLuminance12+ | number | No | Yes | Infrared luminance, in cd/m². This parameter is optional. If this parameter is not supported, a fixed value (customized by the sensor) is returned. If this parameter is supported, a normal value is returned. |

#### HallResponse

Describes the Hall effect sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| status | number | No | No | Hall effect sensor status. This parameter specifies whether a magnetic field exists around a device. The value **0** means that a magnetic field does not exist, and a value greater than **0** means the opposite. |

#### MagneticFieldResponse

Describes the magnetic field sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Magnetic field strength on the x-axis, in μT. |
| y | number | No | No | Magnetic field strength on the y-axis, in μT. |
| z | number | No | No | Magnetic field strength on the z-axis, in μT. |

#### MagneticFieldUncalibratedResponse

Describes the uncalibrated magnetic field sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | Uncalibrated magnetic field strength on the x-axis, in μT. |
| y | number | No | No | Uncalibrated magnetic field strength on the y-axis, in μT. |
| z | number | No | No | Uncalibrated magnetic field strength on the z-axis, in μT. |
| biasX | number | No | No | Bias of the uncalibrated magnetic field strength on the x-axis, in μT. |
| biasY | number | No | No | Bias of the uncalibrated magnetic field strength on the y-axis, in μT. |
| biasZ | number | No | No | Bias of the uncalibrated magnetic field strength on the z-axis, in μT. |

#### PedometerResponse

Describes the pedometer sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| steps | number | No | No | Number of steps a user has walked. |

#### HumidityResponse

Describes the humidity sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| humidity | number | No | No | Ambient relative humidity, in a percentage (%). |

#### PedometerDetectionResponse

Describes the pedometer detection sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| scalar | number | No | No | Pedometer detection. This parameter specifies whether a user takes a step. The value **0** means that the user does not take a step, and **1** means that the user takes a step. |

#### AmbientTemperatureResponse

Describes the ambient temperature sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| temperature | number | No | No | Ambient temperature, in degree Celsius. |

#### BarometerResponse

Describes the barometer sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pressure | number | No | No | Atmospheric pressure, in units of hPa. |

#### HeartRateResponse

Describes the heart rate sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| heartRate | number | No | No | Heart rate, in beats per minute (bpm). |

#### WearDetectionResponse

Describes the wear detection sensor data. It extends from [Response](#response).

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| value | number | No | No | Whether the device is being worn. The value **1** means that the device is being worn, and **0** means the opposite. |

#### Options

Describes the sensor data reporting frequency.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| interval | number|[SensorFrequency](#sensorfrequency11)11+ | No | Yes | Frequency at which a sensor reports data. The default value is 200,000,000 ns. The maximum and minimum values of this parameter are determined by the reporting frequency supported by the hardware. If the configured frequency is greater than the maximum value, the maximum value is used for data reporting. If the configured frequency is less than the minimum value, the minimum value is used for data reporting. |
| sensorInfoParam19+ | [SensorInfoParam](#sensorinfoparam19) | No | Yes | 
Sensor parameters, including **deviceId** and **sensorIndex**.

**Atomic service API**: This API can be used in atomic services since API version 19.

 |

#### SensorFrequency11+

type SensorFrequency = 'game' | 'ui' | 'normal'

Defines the reporting frequency mode of the sensor.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Sensors.Sensor

| Type | Description |
| :-- | :-- |
| 'game' | Game mode, which specifies a sensor data reporting frequency of 20,000,000 ns. This parameter takes effect only when the frequency is within the frequency range supported by the hardware. |
| 'ui' | UI mode, which specifies a sensor data reporting frequency of 60,000,000 ns. This parameter takes effect only when the frequency is within the frequency range supported by the hardware. |
| 'normal' | Normal mode, which specifies a sensor data reporting frequency of 200,000,000 ns. This parameter takes effect only when the frequency is within the frequency range supported by the hardware. |

#### RotationMatrixResponse

Describes the response for setting the rotation matrix.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| rotation | Array<number> | No | No | Rotation matrix. |
| inclination | Array<number> | No | No | Inclination matrix. |

#### CoordinatesOptions

Describes the coordinate options.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | X coordinate direction. |
| y | number | No | No | Y coordinate direction. |

#### GeomagneticResponse

Describes a geomagnetic response object.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| x | number | No | No | North component of the geomagnetic field. |
| y | number | No | No | East component of the geomagnetic field. |
| z | number | No | No | Vertical component of the geomagnetic field. |
| geomagneticDip | number | No | No | Magnetic dip, also called magnetic inclination, which is the angle measured from the horizontal plane to the magnetic field vector. |
| deflectionAngle | number | No | No | Magnetic declination, which is the angle between true north (geographic north) and the magnetic north (the horizontal component of the field). |
| levelIntensity | number | No | No | Horizontal intensity of the magnetic field vector field. |
| totalIntensity | number | No | No | Total intensity of the magnetic field vector. |

#### LocationOptions

Describes the geographical location.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| latitude | number | No | No | Latitude. |
| longitude | number | No | No | Longitude. |
| altitude | number | No | No | Altitude. |

#### sensor.on(deprecated)

#### \[h2\]ACCELEROMETER(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback: Callback<AccelerometerResponse>,options?: Options): void

Subscribes to data changes of the acceleration sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/yI8hbo_gQjmyc2KScWoEww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98373A9E4A9B54F3303705D6D442A58D2B2D41EA3A5F23A9681152E56D8AACDC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.ACCELEROMETER](#accelerometer9)9+ instead.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_ACCELEROMETER**. |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | Yes | Callback used to return the acceleration sensor data. The reported data type in the callback is **AccelerometerResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
},
  { interval: 100000000 }
);

#### \[h2\]LINEAR\_ACCELERATION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION,callback:Callback<LinearAccelerometerResponse>, options?: Options): void

Subscribes to data changes of the linear acceleration sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/ygSUBdzXQNG6O_nckpKmTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2586F15CB5806E4BEDC1F45E875A97C1CC13AD72CC4F1B2EF1B75D5BA197D66A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.LINEAR\_ACCELEROMETER](#linear_accelerometer9)9+ instead.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION**. |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | Yes | Callback used to return the linear acceleration sensor data. The reported data type in the callback is **LinearAccelerometerResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

#### \[h2\]ACCELEROMETER\_UNCALIBRATED(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED,callback: Callback<AccelerometerUncalibratedResponse>, options?: Options): void

Subscribes to data changes of the uncalibrated acceleration sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/2GXqgIzLT4u5uWNI4ydE8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC74C08C5CB29FD3054C95082C2BFECACB1DCF80A6E87F1C34819020384B7FF3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.ACCELEROMETER\_UNCALIBRATED](#accelerometer_uncalibrated9)9+ instead.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED**. |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | Yes | Callback used to return the uncalibrated acceleration sensor data. The reported data type in the callback is **AccelerometerUncalibratedResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
},
  { interval: 100000000 }
);

#### \[h2\]GRAVITY(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback: Callback<GravityResponse>,options?: Options): void

Subscribes to data changes of the gravity sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/CeNi8ELcTfuYmGz4XqRXGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=64549E8599FC6E38ED8DA71EBB3A1FB7C4FEC6109F28D8D71F2272E0A162E7F4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.GRAVITY](#gravity9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_GRAVITY**. |
| callback | Callback<[GravityResponse](#gravityresponse)\> | Yes | Callback used to return the gravity sensor data. The reported data type in the callback is **GravityResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_GRAVITY, (data: sensor.GravityResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
},
  { interval: 100000000 }
);

#### \[h2\]GYROSCOPE(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback: Callback<GyroscopeResponse>, options?: Options): void

Subscribes to data changes of the gyroscope sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/HOojuQsAQZWeCiRidITDAw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=356B698964F1A4EC8228EA2BACBA07DB03DD0EBF7F31B89C4FFDDD2437814A1A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.GYROSCOPE](#gyroscope9)9+ instead.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_GYROSCOPE**. |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | Yes | Callback used to return the gyroscope sensor data. The reported data type in the callback is **GyroscopeResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, (data: sensor.GyroscopeResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
},
  { interval: 100000000 }
);

#### \[h2\]GYROSCOPE\_UNCALIBRATED(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED,callback:Callback<GyroscopeUncalibratedResponse>, options?: Options): void

Subscribes to data changes of the uncalibrated gyroscope sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/POeAr3oeS0O5O5U_SWF_1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1EB469E92465F7F393CBDF7AC7D87F626CDE32BDF53A78FD4F6848F141FE3ED)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.GYROSCOPE\_UNCALIBRATED](#gyroscope_uncalibrated9)9+ instead.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED**. |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | Yes | Callback used to return the uncalibrated gyroscope sensor data. The reported data type in the callback is **GyroscopeUncalibratedResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
},
  { interval: 100000000 }
);

#### \[h2\]SIGNIFICANT\_MOTION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, callback: Callback<SignificantMotionResponse>, options?: Options): void

Subscribes to data changes of the significant motion sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/TnD-0biARqOF-VWAgfn0iA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C275A063BE96617C9CE04842F5AFC3E252D6DA8169632610AFFD57A11274150)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.SIGNIFICANT\_MOTION](#significant_motion9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION**. |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | Yes | Callback used to return the significant motion sensor data. The reported data type in the callback is **SignificantMotionResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, (data: sensor.SignificantMotionResponse) => {
  console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
},
  { interval: 100000000 }
);

#### \[h2\]PEDOMETER\_DETECTION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, callback: Callback<PedometerDetectionResponse>, options?: Options): void

Subscribes to data changes of the pedometer detection sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/jOfPKNeEQ4-cMnnMBZidoA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92689C31BB4686CD12DFB1BE62AB0862F1FCB3C9BF5F2208E30F84B817F2737E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.PEDOMETER\_DETECTION](#pedometer_detection9)9+ instead.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION**. |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | Yes | Callback used to return the pedometer detection sensor data. The reported data type in the callback is **PedometerDetectionResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, (data: sensor.PedometerDetectionResponse) => {
  console.info('Succeeded in invoking on. Scalar data: ' + data.scalar);
},
  { interval: 100000000 }
);

#### \[h2\]PEDOMETER(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback: Callback<PedometerResponse>, options?: Options): void

Subscribes to data changes of the pedometer sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/JemRuOp3QbKu4rEqM8MB1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8EAD36D9431F2D308726F035F27B94283DC1B7AAC93E025E3CB6F6B8FC3B8327)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.PEDOMETER](#pedometer9)9+ instead.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_PEDOMETER**. |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | Yes | Callback used to return the pedometer sensor data. The reported data type in the callback is **PedometerResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, (data: sensor.PedometerResponse) => {
  console.info('Succeeded in invoking on. Steps: ' + data.steps);
},
  { interval: 100000000 }
);

#### \[h2\]AMBIENT\_TEMPERATURE(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE,callback:Callback<AmbientTemperatureResponse>, options?: Options): void

Subscribes to data changes of the ambient temperature sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/EuMCHKraREyZWbL4v69MNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D029F12B02A119658E90C90C5D1A39B8E8D56453D49946E3CA6FB964C10443BB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.AMBIENT\_TEMPERATURE](#ambient_temperature9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE**. |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | Yes | Callback used to return the ambient temperature sensor data. The reported data type in the callback is **AmbientTemperatureResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
  console.info('Succeeded in invoking on. Temperature: ' + data.temperature);
},
  { interval: 100000000 }
);

#### \[h2\]MAGNETIC\_FIELD(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>,options?: Options): void

Subscribes to data changes of the magnetic field sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/E-SGIml5SsWjjo7aNjWZ8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2694F5E9C15C97354D8E9ACF93411240DB89BBF55D87022D1C3C0A23AD830E6C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.MAGNETIC\_FIELD](#magnetic_field9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD**. |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | Yes | Callback used to return the magnetic field sensor data. The reported data type in the callback is **MagneticFieldResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, (data: sensor.MagneticFieldResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
},
  { interval: 100000000 }
);

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED,callback: Callback<MagneticFieldUncalibratedResponse>, options?: Options): void

Subscribes to data changes of the uncalibrated magnetic field sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/-iRCEqY1Ti6O9cfMsOLjNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EF1F5B2F262B32139E41AA71CCB7CDD875E0B15F865B9FD91534539CAE7EE38)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.MAGNETIC\_FIELD\_UNCALIBRATED](#magnetic_field_uncalibrated9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED**. |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | Yes | Callback used to return the uncalibrated magnetic field sensor data. The reported data type in the callback is **MagneticFieldUncalibratedResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking on. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking on. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking on. Z-coordinate bias: ' + data.biasZ);
},
  { interval: 100000000 }
);

#### \[h2\]PROXIMITY(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback: Callback<ProximityResponse>,options?: Options): void

Subscribes to data changes of the proximity sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/74/v3/DRi7FBzfQim34kP6vdcryQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18D5E0C342A4CCA629E639DB2F186E122287CE9EF48C67343630EC9443C21263)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.PROXIMITY](#proximity9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_PROXIMITY**. |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | Yes | Callback used to return the proximity sensor data. The reported data type in the callback is **ProximityResponse**. |
| options | [Options](#options) | No | List of optional parameters. The default value is 200,000,000 ns. This parameter is used to set the data reporting frequency when proximity sensor events are frequently triggered. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, (data: sensor.ProximityResponse) => {
  console.info('Succeeded in invoking on. Distance: ' + data.distance);
},
  { interval: 100000000 }
);

#### \[h2\]HUMIDITY(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback: Callback<HumidityResponse>,options?: Options): void

Subscribes to data changes of the humidity sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/efIf-NDwSoG5elwymRpPkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9814B973A859AAA1DFB0842621D1C25A81BE216D032B282B6C27C61BA978AA78)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.HUMIDITY](#humidity9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_HUMIDITY**. |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | Yes | Callback used to return the humidity sensor data. The reported data type in the callback is **HumidityResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, (data: sensor.HumidityResponse) => {
  console.info('Succeeded in invoking on. Humidity: ' + data.humidity);
},
  { interval: 100000000 }
);

#### \[h2\]BAROMETER(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback: Callback<BarometerResponse>,options?: Options): void

Subscribes to data changes of the barometer sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/dkOllsYWSjWZi1hU_3ZWog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D385F068CE26A7670E5B656176CCD87455A586BF5926038ABE87236D1FA694B4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.BAROMETER](#barometer9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_BAROMETER**. |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | Yes | Callback used to return the barometer sensor data. The reported data type in the callback is **BarometerResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_BAROMETER, (data: sensor.BarometerResponse) => {
  console.info('Succeeded in invoking on. Atmospheric pressure: ' + data.pressure);
},
  { interval: 100000000 }
);

#### \[h2\]HALL(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback: Callback<HallResponse>, options?: Options): void

Subscribes to data changes of the Hall effect sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/P8sTwAMDQ5O4ifXa3ZZLOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BD61A51E16C3C2A183F6A63F86619B1070E0BB2A7A2C36F21781EA0EED48FF4)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.HALL](#hall9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_HALL**. |
| callback | Callback<[HallResponse](#hallresponse)\> | Yes | Callback used to return the Hall effect sensor data. The reported data type in the callback is **HallResponse**. |
| options | [Options](#options) | No | List of optional parameters. The default value is 200,000,000 ns. This parameter is used to set the data reporting frequency when Hall effect events are frequently triggered. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_HALL, (data: sensor.HallResponse) => {
  console.info('Succeeded in invoking on. Status: ' + data.status);
},
  { interval: 100000000 }
);

#### \[h2\]AMBIENT\_LIGHT(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback: Callback<LightResponse>, options?: Options): void

Subscribes to data changes of the ambient light sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/_PSlsDwrSC6-50GS60adiA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5351EBD7876E85E2A30195C94A0D94F710603D807D51C103B116EE514C90E913)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.AMBIENT\_LIGHT](#ambient_light9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT**. |
| callback | Callback<[LightResponse](#lightresponse)\> | Yes | Callback used to return the ambient light sensor data. The reported data type in the callback is **LightResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, (data: sensor.LightResponse) => {
  console.info('Succeeded in invoking on. Illumination: ' + data.intensity);
},
  { interval: 100000000 }
);

#### \[h2\]ORIENTATION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback: Callback<OrientationResponse>, options?: Options): void

Subscribes to data changes of the orientation sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/ch56uW2jQgSD1h5v6xOHlg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21475F1CEF75D5F4A56A655F3BA47B504B964DCFA9F058CA121F8956DE88335A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.ORIENTATION](#orientation9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_ORIENTATION**. |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | Yes | Callback used to return the orientation sensor data. The reported data type in the callback is **OrientationResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, (data: sensor.OrientationResponse) => {
  console.info('Succeeded in the device rotating at an angle around the X axis: ' + data.beta);
  console.info('Succeeded in the device rotating at an angle around the Y axis: ' + data.gamma);
  console.info('Succeeded in the device rotating at an angle around the Z axis: ' + data.alpha);
},
  { interval: 100000000 }
);

#### \[h2\]HEART\_RATE(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback: Callback<HeartRateResponse>, options?: Options): void

Subscribes to data changes of the heart rate sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/4CnN64hFS9ChgO3e8L8mWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A1EA6DA1D0685D81F93F7479276E8034362E212D8D2ABBD63BE1E0A745DC4EF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.HEART\_RATE](#heart_rate9)9+ instead.

**Required permissions**: ohos.permission.HEALTH\_DATA

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_HEART\_RATE**. |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | Yes | Callback used to return the heart rate sensor data. The reported data type in the callback is **HeartRateResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

#### \[h2\]ROTATION\_VECTOR(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR,callback: Callback<RotationVectorResponse>,options?: Options): void

Subscribes to data changes of the rotation vector sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/yVhRTSXTRN2W94AxRjmy_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=69B65879DD66DAFBA15A49E48E5DAE8CA0472F64BA605A932825E21081B19B88)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.ROTATION\_VECTOR](#rotation_vector9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_ROTATION\_VECTOR**. |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | Yes | Callback used to return the rotation vector sensor data. The reported data type in the callback is **RotationVectorResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, (data: sensor.RotationVectorResponse) => {
  console.info('Succeeded in invoking on. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking on. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking on. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking on. Scalar quantity: ' + data.w);
},
  { interval: 100000000 }
);

#### \[h2\]WEAR\_DETECTION(deprecated)

on(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback: Callback<WearDetectionResponse>,options?: Options): void

Subscribes to data changes of the wear detection sensor. If this API is called multiple times for the same application, the last call takes effect.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/Zz5miM84QoSbQSwW4989Rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56C2B276CBE9052804819B08E51C70451E18075092DBEBC3B2C7FF3A0C607BF2)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.on.WEAR\_DETECTION](#wear_detection9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_WEAR\_DETECTION**. |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | Yes | Callback used to return the wear detection sensor data. The reported data type in the callback is **WearDetectionResponse**. |
| options | [Options](#options) | No | List of optional parameters. This parameter is used to set the data reporting frequency. The default value is 200,000,000 ns. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.on(sensor.SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, (data: sensor.WearDetectionResponse) => {
  console.info('Succeeded in invoking on. Wear status: ' + data.value);
},
  { interval: 100000000 }
);

#### sensor.once(deprecated)

#### \[h2\]ACCELEROMETER(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback: Callback<AccelerometerResponse>): void

Subscribes to only one data change of the acceleration sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/knjXfBHuRJWgNlXWxeRqDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A960CEC78817228DDBE728D9B303B1ACF84609F407FE60FF6117552A4927DC03)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.ACCELEROMETER](#accelerometer9-1)9+ instead.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_ACCELEROMETER**. |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | Yes | One-shot callback used to return the acceleration sensor data. The reported data type in the callback is **AccelerometerResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, (data: sensor.AccelerometerResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
});

#### \[h2\]LINEAR\_ACCELERATION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION,callback:Callback<LinearAccelerometerResponse>): void

Subscribes to only one data change of the linear acceleration sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/nHNCIuEIS6WVlmAl7LSVMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B478EC8A7ECC76A6641CE326C992CE9DE754D6F3B9642CB35F88E3F4D8CC122)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.LINEAR\_ACCELEROMETER](#linear_accelerometer9-1)9+ instead.

**Required permissions**: ohos.permission.ACCELERATION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION**. |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | Yes | One-shot callback used to return the linear acceleration sensor data. The reported data type in the callback is **LinearAccelerometerResponse**. |

#### \[h2\]ACCELEROMETER\_UNCALIBRATED(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED,callback: Callback<AccelerometerUncalibratedResponse>): void

Subscribes to only one data change of the uncalibrated acceleration sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/cuwZDPgqQl-XbJ62lhJfrg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA0C3A9BD55EFE07E9FED5A19E92EB9FE69C19925D24D0956D216352D658EB18)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.ACCELEROMETER\_UNCALIBRATED](#accelerometer_uncalibrated9-1)9+ instead.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED**. |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | Yes | One-shot callback used to return the uncalibrated acceleration sensor data. The reported data type in the callback is **AccelerometerUncalibratedResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED, (data: sensor.AccelerometerUncalibratedResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
});

#### \[h2\]GRAVITY(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback: Callback<GravityResponse>): void

Subscribes to only one data change of the gravity sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/6VSvDxB8Qb2WCe5cIzXs1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD3DB4A287BB62EBA9DBDC816AECB359807B67B4F34CCBD18E8875D56416DE0C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.GRAVITY](#gravity9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_GRAVITY**. |
| callback | Callback<[GravityResponse](#gravityresponse)\> | Yes | One-shot callback used to return the gravity sensor data. The reported data type in the callback is **GravityResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_GRAVITY, (data: sensor.GravityResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  });

#### \[h2\]GYROSCOPE(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback: Callback<GyroscopeResponse>): void

Subscribes to only one data change of the gyroscope sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/7N95lrW3RMW5eXOTzvb8NQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=90C7396B78254F150F7A7069FA3DE804F84B20CDCA119B285D4CE89F1230659C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.GYROSCOPE](#gyroscope9-1)9+ instead.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_GYROSCOPE**. |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | Yes | One-shot callback used to return the gyroscope sensor data. The reported data type in the callback is **GyroscopeResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, (data: sensor.GyroscopeResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
});

#### \[h2\]GYROSCOPE\_UNCALIBRATED(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED,callback: Callback<GyroscopeUncalibratedResponse>): void

Subscribes to only one data change of the uncalibrated gyroscope sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/YATA3odSTSGkjsdSuVbLGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC5709735018E6576BAA1553D48C776E645AD748C9549C17CC455E47FE8B43E6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.GYROSCOPE\_UNCALIBRATED](#gyroscope_uncalibrated9-1)9+ instead.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED**. |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | Yes | One-shot callback used to return the uncalibrated gyroscope sensor data. The reported data type in the callback is **GyroscopeUncalibratedResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED, (data: sensor.GyroscopeUncalibratedResponse) => {
    console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
    console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
    console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
    console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
    console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
    console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
});

#### \[h2\]SIGNIFICANT\_MOTION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION,callback: Callback<SignificantMotionResponse>): void

Subscribes to only one data change of the significant motion sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/RBE3hxDKQDGS_MXfQ-LPeQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=65720A25C0E4CDF08C730D80B54E17D3308285E3BDC1CE403866138BB219C25C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.SIGNIFICANT\_MOTION](#significant_motion9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION**. |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | Yes | One-shot callback used to return the significant motion sensor data. The reported data type in the callback is **SignificantMotionResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, (data: sensor.SignificantMotionResponse) => {
  console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
});

#### \[h2\]PEDOMETER\_DETECTION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION,callback: Callback<PedometerDetectionResponse>): void

Subscribes to only one data change of the pedometer detection sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/O-PhdesiSYqO4973_k-vDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44C1E7668B16A4808249FAF7300DEF3765EF721381B22CA53E8FC11DD9D3AFAD)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.PEDOMETER\_DETECTION](#pedometer_detection9-1)9+ instead.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION**. |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | Yes | One-shot callback used to return the pedometer detection sensor data. The reported data type in the callback is **PedometerDetectionResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, (data: sensor.PedometerDetectionResponse) => {
  console.info('Succeeded in invoking once. Scalar data: ' + data.scalar);
});

#### \[h2\]PEDOMETER(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback: Callback<PedometerResponse>): void

Subscribes to only one data change of the pedometer sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/nCrq4RkMQS6vWkHTXtlD6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5AAA2C273F50CC5B8EB11F0B6A3699407D9E3538AD23EC358E0BF1EFAC4ECC73)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.PEDOMETER](#pedometer9-1)9+ instead.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_PEDOMETER**. |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | Yes | One-shot callback used to return the pedometer sensor data. The reported data type in the callback is **PedometerResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, (data: sensor.PedometerResponse) => {
  console.info('Succeeded in invoking once. Steps: ' + data.steps);
});

#### \[h2\]AMBIENT\_TEMPERATURE(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE,callback: Callback<AmbientTemperatureResponse>): void

Subscribes to only one data change of the ambient temperature sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/19HoOgB1TvmgNzaDUPx9fA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A920CF4C0A1B0CB1E46BFFBE34A13159EFC4FCC23493AA26A34783B32746C3AC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.AMBIENT\_TEMPERATURE](#ambient_temperature9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE**. |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | Yes | One-shot callback used to return the ambient temperature sensor data. The reported data type in the callback is **AmbientTemperatureResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE, (data: sensor.AmbientTemperatureResponse) => {
  console.info('Succeeded in invoking once. Temperature: ' + data.temperature);
});

#### \[h2\]MAGNETIC\_FIELD(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback: Callback<MagneticFieldResponse>): void

Subscribes to only one data change of the magnetic field sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/qgYYNkooTYaYn9j_dXPb6w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58CA10B22836D2CF284129E9337584D132A78CDFF883A2A9BFB465E79905A4C3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.MAGNETIC\_FIELD](#magnetic_field9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD**. |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | Yes | One-shot callback used to return the magnetic field sensor data. The reported data type in the callback is **MagneticFieldResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, (data: sensor.MagneticFieldResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
});

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED,callback: Callback<MagneticFieldUncalibratedResponse>): void

Subscribes to only one data change of the uncalibrated magnetic field sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/pdOt8lSLTc-HB8c_Qgyblw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=873A3B6E4E42C0E080222AD6A8617EB454A2A59665788720EDEF685BDB9A5D95)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.MAGNETIC\_FIELD\_UNCALIBRATED](#magnetic_field_uncalibrated9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED**. |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | Yes | One-shot callback used to return the uncalibrated magnetic field sensor data. The reported data type in the callback is **MagneticFieldUncalibratedResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED, (data: sensor.MagneticFieldUncalibratedResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking once. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking once. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking once. Z-coordinate bias: ' + data.biasZ);
});

#### \[h2\]PROXIMITY(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback: Callback<ProximityResponse>): void

Subscribes to only one data change of the proximity sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/6jcBjgltTparQMLZ_tTjuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D36EFDE3947A48ED11FC13A827DB7A0282EF6323440CF95796DD731331B091D2)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.PROXIMITY](#proximity9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_PROXIMITY**. |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | Yes | One-shot callback used to return the proximity sensor data. The reported data type in the callback is **ProximityResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, (data: sensor.ProximityResponse) => {
  console.info('Succeeded in invoking once. Distance: ' + data.distance);
}
);

#### \[h2\]HUMIDITY(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback: Callback<HumidityResponse>): void

Subscribes to only one data change of the humidity sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/AezOZ-OJSJSBeGNGHIPH0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C237A87367DAFE55636F0AF7E3C14E3FBE2A2C2231BE6DCFE07F22EAB9676C1E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.HUMIDITY](#humidity9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_HUMIDITY**. |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | Yes | One-shot callback used to return the humidity sensor data. The reported data type in the callback is **HumidityResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, (data: sensor.HumidityResponse) => {
  console.info('Succeeded in invoking once. Humidity: ' + data.humidity);
});

#### \[h2\]BAROMETER(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback: Callback<BarometerResponse>): void

Subscribes to only one data change of the barometer sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/brbmm_wxQQOaD1Xx3UK3AA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C6C07A8E41DD2E23F13AA0507B0F08607767BD2B40654F6EF48F3B934373781)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.BAROMETER](#barometer9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_BAROMETER**. |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | Yes | One-shot callback used to return the barometer sensor data. The reported data type in the callback is **BarometerResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_BAROMETER, (data: sensor.BarometerResponse) => {
  console.info('Succeeded in invoking once. Atmospheric pressure: ' + data.pressure);
});

#### \[h2\]HALL(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback: Callback<HallResponse>): void

Subscribes to only one data change of the Hall effect sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/GVSd3qziSDmwLpA55hwH2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77CB403FB64C5E9C2D26B990B302A86837B7A9553F710989F1D9081FC63984F8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.HALL](#hall9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_HALL**. |
| callback | Callback<[HallResponse](#hallresponse)\> | Yes | One-shot callback used to return the Hall effect sensor data. The reported data type in the callback is **HallResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_HALL, (data: sensor.HallResponse) => {
  console.info('Succeeded in invoking once. Status: ' + data.status);
});

#### \[h2\]AMBIENT\_LIGHT(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback: Callback<LightResponse>): void

Subscribes to only one data change of the ambient light sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/SKOdCK-DSkK3G0_w-1ZFmg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B25D5AAA6E80C4BCD702F2051E37D4FA079B75C74C3F02E943AAFA0678539DE0)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.AMBIENT\_LIGHT](#ambient_light9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT**. |
| callback | Callback<[LightResponse](#lightresponse)\> | Yes | One-shot callback used to return the ambient light sensor data. The reported data type in the callback is **LightResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, (data: sensor.LightResponse) => {
  console.info('Succeeded in invoking once. invoking once. Illumination: ' + data.intensity);
});

#### \[h2\]ORIENTATION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback: Callback<OrientationResponse>): void

Subscribes to only one data change of the orientation sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/33pjgMwXSIK64hmXaKMQRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFB0C01678EBE3EF61B1CDB98F062E4B3B4083637C0BE2219CBFCD3AA86329CA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.ORIENTATION](#orientation9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_ORIENTATION**. |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | Yes | One-shot callback used to return the orientation sensor data. The reported data type in the callback is **OrientationResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, (data: sensor.OrientationResponse) => {
  console.info('Succeeded in invoking the device rotating at an angle around the X axis: ' + data.beta);
  console.info('Succeeded in invoking the device rotating at an angle around the Y axis: ' + data.gamma);
  console.info('Succeeded in invoking the device rotating at an angle around the Z axis: ' + data.alpha);
});

#### \[h2\]ROTATION\_VECTOR(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, callback: Callback<RotationVectorResponse>): void

Subscribes to only one data change of the rotation vector sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/I1ufvT1AQ3qcPa9FBHw-VA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6F5CBA23B74291B5DBA21741D8ECBD8458E34C42C77E9A8D3AFD7B927F7DA07)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.ROTATION\_VECTOR](#rotation_vector9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_ROTATION\_VECTOR**. |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | Yes | One-shot callback used to return the rotation vector sensor data. The reported data type in the callback is **RotationVectorResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, (data: sensor.RotationVectorResponse) => {
  console.info('Succeeded in invoking once. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking once. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking once. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking once. Scalar quantity: ' + data.w);
});

#### \[h2\]HEART\_RATE(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback: Callback<HeartRateResponse>): void

Subscribes to only one data change of the heart rate sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/5b9bMs-EQYuXDznL5VWAbA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B85D56BCF6F351E7E2D2687BFA380258C2CB98F0AC14936628980AB442DEE496)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.HEART\_RATE](#heart_rate9-1)9+ instead.

**Required permissions**: ohos.permission.HEART\_RATE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_HEART\_RATE**. |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | Yes | One-shot callback used to return the heart rate sensor data. The reported data type in the callback is **HeartRateResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, (data: sensor.HeartRateResponse) => {
  console.info("Succeeded in invoking once. Heart rate: " + data.heartRate);
});

#### \[h2\]WEAR\_DETECTION(deprecated)

once(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback: Callback<WearDetectionResponse>): void

Subscribes to only one data change of the wear detection sensor.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/83VQbfJrSiCz1zkS-OrVDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4AB694F5CC135107761E88DE7080C3F7C8C589DA56294279DDE128ACC955AD13)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.once.WEAR\_DETECTION](#wear_detection9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | Yes | Type of the sensor to subscribe to, which is **SENSOR\_TYPE\_ID\_WEAR\_DETECTION**. |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | Yes | One-shot callback used to return the wear detection sensor data. The reported data type in the callback is **WearDetectionResponse**. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

sensor.once(sensor.SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, (data: sensor.WearDetectionResponse) => {
  console.info("Succeeded in invoking once. Wear status: " + data.value);
});

#### sensor.off(deprecated)

#### \[h2\]ACCELEROMETER(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback?: Callback<AccelerometerResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/YKYN3GX3TrO4SuI7GjKSQw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A681918AD85CCB201532C5162591424351034AF28A18FB40020A7EBFB7817A5F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.ACCELEROMETER9+](#accelerometer9-2) instead.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_ACCELEROMETER**. |
| callback | Callback<[AccelerometerResponse](#accelerometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.AccelerometerResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER, callback);

#### \[h2\]ACCELEROMETER\_UNCALIBRATED(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED, callback?: Callback<AccelerometerUncalibratedResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/dk2PCMqXTJm3pG75X6PdfQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55DB9D82F1B28B29876ACC44244E76E2F137F350E7A9E2D324A8C374C58FA0E8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.ACCELEROMETER\_UNCALIBRATED](#accelerometer_uncalibrated9-2)9+ instead.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED**. |
| callback | Callback<[AccelerometerUncalibratedResponse](#accelerometeruncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.AccelerometerUncalibratedResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking off. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking off. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking off. Z-coordinate bias: ' + data.biasZ);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED, callback);

#### \[h2\]AMBIENT\_LIGHT(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback?: Callback<LightResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/MbKomUwoRda1p6t9xewo8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF729D356AB820DBAD5735FF23CA618473DFA924BD18308A515CC297BBD50CCB)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.AMBIENT\_LIGHT](#ambient_light9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT**. |
| callback | Callback<[LightResponse](#lightresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.LightResponse) {
  console.info('Succeeded in invoking off. Illumination: ' + data.intensity);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT, callback);

#### \[h2\]AMBIENT\_TEMPERATURE(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE, callback?: Callback<AmbientTemperatureResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/UcKMUdlKTNy2GcEQHvqHlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B1544320B99A2E9A65A73E5DF7918D0E4D9DD1A2636CCC15E490D8E8B1651C3B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.AMBIENT\_TEMPERATURE](#ambient_temperature9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE**. |
| callback | Callback<[AmbientTemperatureResponse](#ambienttemperatureresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.AmbientTemperatureResponse) {
  console.info('Succeeded in invoking off. Temperature: ' + data.temperature);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE, callback);

#### \[h2\]BAROMETER(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback?: Callback<BarometerResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/pcmtKh8DQvC5ayN5VmtloA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BECB8DE44D95D46BA87A3D3D9E51674E4E61CF80013C5BEF9A3F9AC09F31ED56)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.BAROMETER](#barometer9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_BAROMETER | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_BAROMETER**. |
| callback | Callback<[BarometerResponse](#barometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.BarometerResponse) {
  console.info('Succeeded in invoking off. Atmospheric pressure: ' + data.pressure);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_BAROMETER, callback);

#### \[h2\]GRAVITY(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback?: Callback<GravityResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/53/v3/E8blBk6UR_SpgYz-WL-NHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=761B91D58AD99C32916A0ABD6F7C23017A34AF9355C67C481E9ACC5C78B6DDD8)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.GRAVITY](#gravity9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GRAVITY | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_GRAVITY**. |
| callback | Callback<[GravityResponse](#gravityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GravityResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_GRAVITY, callback);

#### \[h2\]GYROSCOPE(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback?: Callback<GyroscopeResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/8Zfge8QcThyIsSMt4boL8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5A24645DA42D2A48D7D0DCFF465ADBCA1B1D14C60035186AB17B78255723B3D7)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.GYROSCOPE](#gyroscope9-2)9+ instead.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_GYROSCOPE**. |
| callback | Callback<[GyroscopeResponse](#gyroscoperesponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GyroscopeResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE, callback);

#### \[h2\]GYROSCOPE\_UNCALIBRATED(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED, callback?: Callback<GyroscopeUncalibratedResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/3qsC59ftQFWyI4BAIfknsQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5CA130AE5F905E2C8565F4754FE94034E4242632B7DBBE9A41E8F246D0A2EC9E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.GYROSCOPE\_UNCALIBRATED](#gyroscope_uncalibrated9-2)9+ instead.

**Required permissions**: ohos.permission.GYROSCOPE

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED**. |
| callback | Callback<[GyroscopeUncalibratedResponse](#gyroscopeuncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.GyroscopeUncalibratedResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED, callback);

#### \[h2\]HALL(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_HALL, callback?: Callback<HallResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/3mzOogeIS4e2oiO3lZ_tCA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F7E90F2DC548206135BF57AF8D3393ABEA901037C86F3526FF34E5DB06B783D6)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.HALL](#hall9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HALL | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_HALL**. |
| callback | Callback<[HallResponse](#hallresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HallResponse) {
  console.info('Succeeded in invoking off. Status: ' + data.status);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_HALL, callback);

#### \[h2\]HEART\_RATE(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback?: Callback<HeartRateResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/Mi1VW0lgS-Opw0szpr2u5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EBC3367BFD5EA7E4BAC1E1F25C98EC462CC4884C75E4FD1A716D0604DF7B37A)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.HEART\_RATE](#heart_rate9-2)9+ instead.

**Required permissions**: ohos.permission.HEALTH\_DATA

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HEART\_RATE | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_HEART\_RATE**. |
| callback | Callback<[HeartRateResponse](#heartrateresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HeartRateResponse) {
  console.info('Succeeded in invoking off. Heart rate: ' + data.heartRate);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_HEART\_RATE, callback);

#### \[h2\]HUMIDITY(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback?: Callback<HumidityResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/z0wsQhsBRs6yarnv-j4VJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E2480CCF26A8C796F1901AB5AF0493419B590F4F16E65FD67F3A011EFD2F478)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.HUMIDITY](#humidity9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_HUMIDITY | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_HUMIDITY**. |
| callback | Callback<[HumidityResponse](#humidityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.HumidityResponse) {
  console.info('Succeeded in invoking off. Humidity: ' + data.humidity);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_HUMIDITY, callback);

#### \[h2\]LINEAR\_ACCELERATION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION, callback?: Callback<LinearAccelerometerResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/yAka5MeZTPC-gXsUPppncw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=559456C6A0DB9604AFFE70887B22021476753F894B066FE1FCBEB7EAB5E9766E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.LINEAR\_ACCELEROMETER](#linear_accelerometer9-2)9+ instead.

**Required permissions**: ohos.permission.ACCELEROMETER

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION**. |
| callback | Callback<[LinearAccelerometerResponse](#linearaccelerometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.LinearAccelerometerResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION, callback);

#### \[h2\]MAGNETIC\_FIELD(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback?: Callback<MagneticFieldResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/ZzkjHfKaRlimOq6nWTVwcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DEB58B5BE849F8478B959BA963FD30053F04A505E75A1456838F36D23EC94214)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.MAGNETIC\_FIELD](#magnetic_field9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD**. |
| callback | Callback<[MagneticFieldResponse](#magneticfieldresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.MagneticFieldResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD, callback);

#### \[h2\]MAGNETIC\_FIELD\_UNCALIBRATED(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED, callback?: Callback<MagneticFieldUncalibratedResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/3yAGtwM_QieS2CMRMG9neA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF3F069B8AB7D8147D293D866B82A1F360F371E20BDEF7B2BC856AD21D703CFF)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.MAGNETIC\_FIELD\_UNCALIBRATED](#magnetic_field_uncalibrated9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED**. |
| callback | Callback<[MagneticFieldUncalibratedResponse](#magneticfielduncalibratedresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.MagneticFieldUncalibratedResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking off. X-coordinate bias: ' + data.biasX);
  console.info('Succeeded in invoking off. Y-coordinate bias: ' + data.biasY);
  console.info('Succeeded in invoking off. Z-coordinate bias: ' + data.biasZ);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED, callback);

#### \[h2\]ORIENTATION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback?: Callback<OrientationResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/18/v3/FoXTqxRORx6xxRqcuv_WUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2A59A4D646AFE377AA6B4495EDDC8F418353A69D5F3DD4AA16275C10D233CFAA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.ORIENTATION](#orientation9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ORIENTATION | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_ORIENTATION**. |
| callback | Callback<[OrientationResponse](#orientationresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.OrientationResponse) {
  console.info('Succeeded in invoking off. The device rotates at an angle around the X axis: ' + data.beta);
  console.info('Succeeded in invoking off. The device rotates at an angle around the Y axis: ' + data.gamma);
  console.info('Succeeded in invoking off. The device rotates at an angle around the Z axis: ' + data.alpha);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_ORIENTATION, callback);

#### \[h2\]PEDOMETER(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback?: Callback<PedometerResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/KWpYeApNTImBTuD54KnkSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F5431ABF5786D1811B8FF44803B1E6AE808256C137587DFA9248CEB6E9E8F54)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.PEDOMETER](#pedometer9-2)9+ instead.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_PEDOMETER**. |
| callback | Callback<[PedometerResponse](#pedometerresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.PedometerResponse) {
  console.info('Succeeded in invoking off. Steps: ' + data.steps);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_PEDOMETER, callback);

#### \[h2\]PEDOMETER\_DETECTION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, callback?: Callback<PedometerDetectionResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/sd-ez5fNSUy0_qArcWw_Xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1130512E4C73EEE08374AD66DBAF989687EB207C31D9719D94BAE602B7DCFC0E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.PEDOMETER\_DETECTION](#pedometer_detection9-2)9+ instead.

**Required permissions**: ohos.permission.ACTIVITY\_MOTION

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION**. |
| callback | Callback<[PedometerDetectionResponse](#pedometerdetectionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.PedometerDetectionResponse) {
  console.info('Succeeded in invoking off. Scalar data: ' + data.scalar);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION, callback);

#### \[h2\]PROXIMITY(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback?: Callback<ProximityResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/1LVTRFCdT-ubtS7AZ0G4rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD121BFF555B78C807AFDF8FF4282FCBD4D6C8E3F3D8F3B4C981998EE6614238)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.PROXIMITY](#proximity9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_PROXIMITY | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_PROXIMITY**. |
| callback | Callback<[ProximityResponse](#proximityresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.ProximityResponse) {
  console.info('Succeeded in invoking off. Distance: ' + data.distance);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_PROXIMITY, callback);

#### \[h2\]ROTATION\_VECTOR(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, callback?: Callback<RotationVectorResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/GPRM_CKzQH6Sqo2SlFeD3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=103EA64C4FA15EA819655D9E016EF5B794D1E3268F2B8F236501A65889BEFA6F)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.ROTATION\_VECTOR](#rotation_vector9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_ROTATION\_VECTOR**. |
| callback | Callback<[RotationVectorResponse](#rotationvectorresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.RotationVectorResponse) {
  console.info('Succeeded in invoking off. X-coordinate component: ' + data.x);
  console.info('Succeeded in invoking off. Y-coordinate component: ' + data.y);
  console.info('Succeeded in invoking off. Z-coordinate component: ' + data.z);
  console.info('Succeeded in invoking off. Scalar quantity: ' + data.w);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_ROTATION\_VECTOR, callback);

#### \[h2\]SIGNIFICANT\_MOTION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, callback?: Callback<SignificantMotionResponse>): void

Unsubscribes from valid motion sensor data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/ttgws74MRo2VbORAT2ksZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61E2C713A9B49C3FCCF52573AF49B976095CBE4C7ED60B38E356BF3619ED9AD2)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.SIGNIFICANT\_MOTION](#significant_motion9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION**. |
| callback | Callback<[SignificantMotionResponse](#significantmotionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function callback(data: sensor.SignificantMotionResponse) {
  console.info('Succeeded in invoking off. Scalar data: ' + data.scalar);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION, callback);

#### \[h2\]WEAR\_DETECTION(deprecated)

off(type: SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, callback?: Callback<WearDetectionResponse>): void

Unsubscribes from sensor data changes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/90/v3/Re6MoL4lRymydZk9IUpVow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10FE55E593F80F73B5B989515D5AECCD60A9B4513BD110B15226AEC3D0820CD9)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.off.WEAR\_DETECTION](#wear_detection9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | [SensorType](#sensortypedeprecated).SENSOR\_TYPE\_ID\_WEAR\_DETECTION | Yes | Type of the sensor to unsubscribe from, which is **SENSOR\_TYPE\_ID\_WEAR\_DETECTION**. |
| callback | Callback<[WearDetectionResponse](#weardetectionresponse)\> | No | Callback used for unsubscription. If this parameter is not specified, all callbacks of the specified sensor type are unsubscribed from. |

**Example**

import { sensor } from '@kit.SensorServiceKit';

function accCallback(data: sensor.WearDetectionResponse) {
  console.info('Succeeded in invoking off. Wear status: ' + data.value);
}

sensor.off(sensor.SensorType.SENSOR\_TYPE\_ID\_WEAR\_DETECTION, accCallback);

#### sensor.transformCoordinateSystem(deprecated)

transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions, callback: AsyncCallback<Array<number>>): void

Rotates a rotation vector so that it can represent the coordinate system in different ways. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/70g5OWR-T0esngguSirVLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5657E0D6365A159A803F1F3C312CE8EB72AE1662DD3D8BEF64E97CEC3A7B19EC)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.transformRotationMatrix](#sensortransformrotationmatrix9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inRotationVector | Array<number> | Yes | Rotation vector. |
| coordinates | [CoordinatesOptions](#coordinatesoptions) | Yes | Direction of the coordinate system. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the rotation vector after being rotated. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.transformCoordinateSystem(\[1, 0, 0, 0, 1, 0, 0, 0, 1\], { x: 2, y: 3 },
                                 (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(\`Failed to operate. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info("Succeeded in starting Operation. Data obtained: " + data);
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting transformCoordinateSystem data\[ " + i + "\] = " + data\[i\]);
  }
})

#### sensor.transformCoordinateSystem(deprecated)

transformCoordinateSystem(inRotationVector: Array<number>, coordinates: CoordinatesOptions): Promise<Array<number>>

Rotates a rotation vector so that it can represent the coordinate system in different ways. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/o7xCixnuRTWlfmEbNGSLgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2C8B1C6ED9ABE88884C42B7A85365B6A17DDCC4768B0E1D25F503C4A441C088)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.transformRotationMatrix](#sensortransformrotationmatrix9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inRotationVector | Array<number> | Yes | Rotation vector. |
| coordinates | [CoordinatesOptions](#coordinatesoptions) | Yes | Direction of the coordinate system. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the rotation vector after being rotated. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.transformCoordinateSystem(\[1, 0, 0, 0, 1, 0, 0, 0, 1\], { x: 2, y: 3 });
promise.then((data: Array<number>) => {
  console.info("Succeeded in starting Operation");
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting transformCoordinateSystem data\[ " + i + "\] = " + data\[i\]);
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to operate.\`);
})

#### sensor.getGeomagneticField(deprecated)

getGeomagneticField(locationOptions: LocationOptions, timeMillis: number, callback: AsyncCallback<GeomagneticResponse>): void

Obtains the geomagnetic field of a geographic location. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ar3I3PwOSvaEnZeVcxvX-A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DD12A56017261D4FF05D936575A72B7A9A312CDA1704E6946CC5728EC12892E)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getGeomagneticInfo](#sensorgetgeomagneticinfo9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locationOptions | [LocationOptions](#locationoptions) | Yes | Geographic location. |
| timeMillis | number | Yes | Time for obtaining the magnetic declination, in milliseconds. |
| callback | AsyncCallback<[GeomagneticResponse](#geomagneticresponse)\> | Yes | Callback used to return the geomagnetic field. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getGeomagneticField({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000,
                           (err: BusinessError, data: sensor.GeomagneticResponse) => {
  if (err) {
    console.error(\`Failed to operate. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info('Succeeded in getting sensor\_getGeomagneticField\_callback x: ' + data.x + ',y: ' + data.y + ',z: ' +
  data.z + ',geomagneticDip: ' + data.geomagneticDip + ',deflectionAngle: ' + data.deflectionAngle +
  ',levelIntensity: ' + data.levelIntensity + ',totalIntensity: ' + data.totalIntensity);
});

#### sensor.getGeomagneticField(deprecated)

getGeomagneticField(locationOptions: LocationOptions, timeMillis: number): Promise<GeomagneticResponse>

Obtains the geomagnetic field of a geographic location. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/DVzcnHFDTzeXUtySV8zrzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C85B124C7EBCAC0A84E0AB314B1CF938D97F0A72241CD2A2C94E03F02B6E5D2)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getGeomagneticInfo](#sensorgetgeomagneticinfo9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| locationOptions | [LocationOptions](#locationoptions) | Yes | Geographic location. |
| timeMillis | number | Yes | Time for obtaining the magnetic declination, in milliseconds. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[GeomagneticResponse](#geomagneticresponse)\> | Promise used to return the geomagnetic field. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getGeomagneticField({ latitude: 80, longitude: 0, altitude: 0 }, 1580486400000);
promise.then((data: sensor.GeomagneticResponse) => {
  console.info('Succeeded in getting sensor\_getGeomagneticField\_promise x: ' + data.x + ',y: ' + data.y + ',z: ' +
  data.z + ',geomagneticDip: ' + data.geomagneticDip + ',deflectionAngle: ' + data.deflectionAngle +
  ',levelIntensity: ' + data.levelIntensity + ',totalIntensity: ' + data.totalIntensity);
}).catch((reason: BusinessError) => {
  console.error(\`Failed to operate.\`);
})

#### sensor.getAltitude(deprecated)

getAltitude(seaPressure: number, currentPressure: number, callback: AsyncCallback<number>): void

Obtains the altitude at which the device is located based on the sea-level atmospheric pressure and the current atmospheric pressure. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/94qO51POREu5Vkc6ITgICg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27BFA43DF167E0D0E18FBEA8CA7F0F68B6A42B8997F9BEF83E0DD480F488D8E9)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getDeviceAltitude](#sensorgetdevicealtitude9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| seaPressure | number | Yes | Sea-level atmospheric pressure, in hPa. |
| currentPressure | number | Yes | Atmospheric pressure at the altitude where the device is located, in hPa. |
| callback | AsyncCallback<number> | Yes | Callback used to return the altitude, in meters. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getAltitude(0, 200, (err: BusinessError, data: number) => {
  if (err) {
    console.error(\`Failed to operate. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info("Succeeded in getting getAltitude interface get data: " + data);
});

#### sensor.getAltitude(deprecated)

getAltitude(seaPressure: number, currentPressure: number): Promise<number>

Obtains the altitude at which the device is located based on the sea-level atmospheric pressure and the current atmospheric pressure. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/9lEB7x77QM-IghnwboC7Qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A64DD5A54CAE1DE8066A84B479F5F7A86331C72E0A7B7DA86B8A0A9FE146E137)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getDeviceAltitude](#sensorgetdevicealtitude9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| seaPressure | number | Yes | Sea-level atmospheric pressure, in hPa. |
| currentPressure | number | Yes | Atmospheric pressure at the altitude where the device is located, in hPa. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the altitude, in meters. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getAltitude(0, 200);
promise.then((data: number) => {
  console.info('Succeeded in getting sensor\_getAltitude\_Promise success', data);
}).catch((err: BusinessError) => {
  console.error(\`Failed to operate.\`);
})

#### sensor.getGeomagneticDip(deprecated)

getGeomagneticDip(inclinationMatrix: Array<number>, callback: AsyncCallback<number>): void

Obtains the magnetic dip based on the inclination matrix. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/NQhCnJ9EQseoeSWh_KPuxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=10A3C19952A1F4D2E7FCC4E9BB3D7CD25EC38FCB11699048D269C7A78B649B5D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getInclination](#sensorgetinclination9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inclinationMatrix | Array<number> | Yes | Inclination matrix. |
| callback | AsyncCallback<number> | Yes | Callback used to return the magnetic dip, in radians. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getGeomagneticDip(\[1, 0, 0, 0, 1, 0, 0, 0, 1\], (err: BusinessError, data: number) => {
  if (err) {
    console.error(\`Failed to register data. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info("Succeeded in getting getGeomagneticDip interface get data: " + data);
})

#### sensor.getGeomagneticDip(deprecated)

getGeomagneticDip(inclinationMatrix: Array<number>): Promise<number>

Obtains the magnetic dip based on the inclination matrix. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/T8Oh7q-qQSqrvdeCXyN_vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DB834459BB792934CA679FCFDC50157D27C52610C6A253A79B0B05229585CE7)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getInclination](#sensorgetinclination9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inclinationMatrix | Array<number> | Yes | Inclination matrix. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the magnetic dip, in radians. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getGeomagneticDip(\[1, 0, 0, 0, 1, 0, 0, 0, 1\]);
promise.then((data: number) => {
  console.info('Succeeded in get GeomagneticDip\_promise', data);
}).catch((err: BusinessError) => {
  console.error(\`Failed to operate.\`);
})

#### sensor. getAngleModify(deprecated)

getAngleModify(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

Obtains the angle change between two rotation matrices. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/iDfhB7raQNqD9s-pbrWq_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F5BE981C793D68CA5B2F68E68A2AEAE21F5801FCBE771494D0D0F8C8876220D)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getAngleVariation](#sensorgetanglevariation9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| currentRotationMatrix | Array<number> | Yes | Current rotation matrix. |
| preRotationMatrix | Array<number> | Yes | The other rotation matrix. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the angle change around the z, x, and y axes. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getAngleModify(\[1, 0, 0, 0, 1, 0, 0, 0, 1\], \[1, 0, 0, 0, 0.87, -0.50, 0, 0.50, 0.87\],
                      (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(\`Failed to register data. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  for (let i = 0; i < data.length; i++) {
    console.info("data\[" + i + "\]: " + data\[i\]);
  }
})

#### sensor. getAngleModify(deprecated)

getAngleModify(currentRotationMatrix: Array<number>, preRotationMatrix: Array<number>): Promise<Array<number>>

Obtains the angle change between two rotation matrices. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/Dzixl6GiTM6rObxAENjEsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B741EDDDCA226A4CE6D63D62C6DBDD50AE7D25ED4A91949E883F63971E352E0B)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getAngleVariation](#sensorgetanglevariation9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| currentRotationMatrix | Array<number> | Yes | Current rotation matrix. |
| preRotationMatrix | Array<number> | Yes | The other rotation matrix. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the angle change around the z, x, and y axes. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getAngleModify(\[1, 0, 0, 0, 1, 0, 0, 0, 1\], \[1, 0, 0, 0, 0.87, -0.50, 0, 0.50, 0.87\]);
promise.then((data: Array<number>) => {
  console.info('Succeeded in getting AngleModify\_promise.');
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting data\[" + i + "\]: " + data\[i\]);
  }
}).catch((reason: BusinessError) => {
  let e: BusinessError = reason as BusinessError;
  console.info("Succeeded in getting promise::catch", e);
})

#### sensor.createRotationMatrix(deprecated)

createRotationMatrix(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

Converts a rotation vector into a rotation matrix. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/vqzBubELTnSquZs8tX-MLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F724F159BEA482EF57F4CA4BE4ADB07A1E90E5187C6270BF9F0471E8C5F0BA3)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getRotationMatrix](#sensorgetrotationmatrix9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | Yes | Rotation vector to convert. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the rotation matrix. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.createRotationMatrix(\[0.20046076, 0.21907, 0.73978853, 0.60376877\],
                            (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(\`Failed to register data. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting data\[" + i + "\]: " + data\[i\]);
  }
})

#### sensor.createRotationMatrix(deprecated)

createRotationMatrix(rotationVector: Array<number>): Promise<Array<number>>

Converts a rotation vector into a rotation matrix. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/1vZgyi7GQj-p9VJTBLM0cA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EE924E44735EB10B7D545F42B71259BC9A13C56B19EFD9C720E5CC3E00DF249)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getRotationMatrix](#sensorgetrotationmatrix9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | Yes | Rotation vector to convert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the rotation matrix. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.createRotationMatrix(\[0.20046076, 0.21907, 0.73978853, 0.60376877\]);
promise.then((data: Array<number>) => {
  console.info('Succeeded in getting createRotationMatrix\_promise');
  for (let i = 0; i < data.length; i++) {
    console.info("data\[" + i + "\]: " + data\[i\]);
  }
}).catch((reason: BusinessError) => {
  console.info("Succeeded in getting promise::catch", reason);
})

#### sensor.createQuaternion(deprecated)

createQuaternion(rotationVector: Array<number>, callback: AsyncCallback<Array<number>>): void

Converts a rotation vector into a quaternion. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/0qO9-INUQAmvwZCFlj6hwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD31EB1E9C31C4497F4AE42E902E5068F7D53F3C2DAC9DFB4929AB79A5977357)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getQuaternion](#sensorgetquaternion9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | Yes | Rotation vector to convert. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the quaternion. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.createQuaternion(\[0.20046076, 0.21907, 0.73978853, 0.60376877\],
                        (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(\`Failed to register data. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  for (let i = 0; i < data.length; i++) {
    console.info("Succeeded in getting data\[" + i + "\]: " + data\[i\]);
  }
})

#### sensor.createQuaternion(deprecated)

createQuaternion(rotationVector: Array<number>): Promise<Array<number>>

Converts a rotation vector into a quaternion. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/lHepnaLCTj2lpZo4vtlo2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A66AB3893F180AA86E2DDB21629B3CB7D6104CF4EE02674E31B4957C7FDA2CE)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getQuaternion](#sensorgetquaternion9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationVector | Array<number> | Yes | Rotation vector to convert. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the quaternion. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.createQuaternion(\[0.20046076, 0.21907, 0.73978853, 0.60376877\]);
promise.then((data: Array<number>) => {
  console.info('Succeeded in getting createQuaternion\_promise');
  for (let i = 0; i < data.length; i++) {
    console.info("data\[" + i + "\]: " + data\[i\]);
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to get promise.\`);
})

#### sensor.getDirection(deprecated)

getDirection(rotationMatrix: Array<number>, callback: AsyncCallback<Array<number>>): void

Obtains the device direction based on the rotation matrix. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/S6q-eed-TcaOqP-MuwUCCQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=97F4AC2C7A01EE2D19107340E1E5A4A31F37471E56932C82A9BB3E920B4F315C)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getOrientation](#sensorgetorientation9)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationMatrix | Array<number> | Yes | Rotation matrix. |
| callback | AsyncCallback<Array<number>> | Yes | Callback used to return the rotation angle around the z, x, and y axes. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.getDirection(\[1, 0, 0, 0, 1, 0, 0, 0, 1\], (err: BusinessError, data: Array<number>) => {
  if (err) {
    console.error(\`Failed to register data. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info("Succeeded in getting getDirection interface get data: " + data);
  for (let i = 1; i < data.length; i++) {
    console.info("Succeeded in getting sensor\_getDirection\_callback" + data\[i\]);
  }
})

#### sensor.getDirection(deprecated)

getDirection(rotationMatrix: Array<number>): Promise<Array<number>>

Obtains the device direction based on the rotation matrix. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/-dxBFMBzRxu7iUrk-nzqQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1B362F9573298830C69A3757612970FE2FA99D8BBA3900C3C4D05001502E6FBA)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getOrientation](#sensorgetorientation9-1)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| rotationMatrix | Array<number> | Yes | Rotation matrix. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the rotation angle around the z, x, and y axes. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.getDirection(\[1, 0, 0, 0, 1, 0, 0, 0, 1\]);
promise.then((data: Array<number>) => {
  console.info('Succeeded in getting sensor\_getAltitude\_Promise', data);
  for (let i = 1; i < data.length; i++) {
    console.info("Succeeded in getting sensor\_getDirection\_promise" + data\[i\]);
  }
}).catch((err: BusinessError) => {
  console.error(\`Failed to get promise.\`);
})

#### sensor.createRotationMatrix(deprecated)

createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>, callback: AsyncCallback<RotationMatrixResponse>): void

Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/E92gt_fAQuWRXSTUaoHp_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B59956832BDC58B6E71F920A6C266BE5FFA40A6B3976C0BE90ED75D93843F54)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getRotationMatrix](#sensorgetrotationmatrix9-2)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gravity | Array<number> | Yes | Gravity vector. |
| geomagnetic | Array<number> | Yes | Geomagnetic vector. |
| callback | AsyncCallback<[RotationMatrixResponse](#rotationmatrixresponse)\> | Yes | Callback used to return the rotation matrix. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

sensor.createRotationMatrix(\[-0.27775216, 0.5351276, 9.788099\], \[210.87253, -78.6096, -111.44444\],
                            (err: BusinessError, data: sensor.RotationMatrixResponse) => {
  if (err) {
    console.error(\`Failed to get create rotationMatrix. Code: ${err.code}, message: ${err.message}\`);
    return;
  }
  console.info(JSON.stringify(data));
})

#### sensor.createRotationMatrix(deprecated)

createRotationMatrix(gravity: Array<number>, geomagnetic: Array<number>): Promise<RotationMatrixResponse>

Obtains the rotation matrix based on a gravity vector and geomagnetic vector. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/YwfPDsEKS-a-TgC35d9sCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B4038FB081A8B038E76ACDBEA9EE04402776AF3609C7CE56995A12F01520EC5)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [sensor.getRotationMatrix](#sensorgetrotationmatrix9-3)9+ instead.

**System capability**: SystemCapability.Sensors.Sensor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| gravity | Array<number> | Yes | Gravity vector. |
| geomagnetic | Array<number> | Yes | Geomagnetic vector. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RotationMatrixResponse](#rotationmatrixresponse)\> | Promise used to return the rotation matrix. |

**Example**

import { sensor } from '@kit.SensorServiceKit';
import { BusinessError } from '@kit.BasicServicesKit';

const promise = sensor.createRotationMatrix(\[-0.27775216, 0.5351276, 9.788099\], \[210.87253, -78.6096, -111.44444\]);
promise.then((data: sensor.RotationMatrixResponse) => {
  console.info(JSON.stringify(data));
}).catch((err: BusinessError) => {
  console.error(\`Failed to get promise.\`);
})

#### SensorType(deprecated)

Enumerates the sensor types.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/3i45ZAD6S4GQDqaNpV80MQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9FB57621044338FBE0134DB13B1FA586704A87111460380056A23D609FFBE914)

This API is supported since API version 8 and deprecated since API version 9. You are advised to use [SensorId](#sensorid9) instead.

**System capability**: SystemCapability.Sensors.Sensor

| Name | Value | Description |
| :-- | :-- | :-- |
| SENSOR\_TYPE\_ID\_ACCELEROMETER | 1 | Acceleration sensor. |
| SENSOR\_TYPE\_ID\_GYROSCOPE | 2 | Gyroscope sensor. |
| SENSOR\_TYPE\_ID\_AMBIENT\_LIGHT | 5 | Ambient light sensor. |
| SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD | 6 | Magnetic field sensor. |
| SENSOR\_TYPE\_ID\_BAROMETER | 8 | Barometer sensor. |
| SENSOR\_TYPE\_ID\_HALL | 10 | Hall effect sensor. |
| SENSOR\_TYPE\_ID\_PROXIMITY | 12 | Proximity sensor. |
| SENSOR\_TYPE\_ID\_HUMIDITY | 13 | Humidity sensor. |
| SENSOR\_TYPE\_ID\_ORIENTATION | 256 | Orientation sensor. |
| SENSOR\_TYPE\_ID\_GRAVITY | 257 | Gravity sensor. |
| SENSOR\_TYPE\_ID\_LINEAR\_ACCELERATION | 258 | Linear acceleration sensor. |
| SENSOR\_TYPE\_ID\_ROTATION\_VECTOR | 259 | Rotation vector sensor. |
| SENSOR\_TYPE\_ID\_AMBIENT\_TEMPERATURE | 260 | Ambient temperature sensor. |
| SENSOR\_TYPE\_ID\_MAGNETIC\_FIELD\_UNCALIBRATED | 261 | Uncalibrated magnetic field sensor. |
| SENSOR\_TYPE\_ID\_GYROSCOPE\_UNCALIBRATED | 263 | Uncalibrated gyroscope sensor. |
| SENSOR\_TYPE\_ID\_SIGNIFICANT\_MOTION | 264 | Significant motion sensor. |
| SENSOR\_TYPE\_ID\_PEDOMETER\_DETECTION | 265 | Pedometer detection sensor. |
| SENSOR\_TYPE\_ID\_PEDOMETER | 266 | Pedometer sensor. |
| SENSOR\_TYPE\_ID\_HEART\_RATE | 278 | Heart rate sensor. |
| SENSOR\_TYPE\_ID\_WEAR\_DETECTION | 280 | Wear detection sensor. |
| SENSOR\_TYPE\_ID\_ACCELEROMETER\_UNCALIBRATED | 281 | Uncalibrated acceleration sensor. |
