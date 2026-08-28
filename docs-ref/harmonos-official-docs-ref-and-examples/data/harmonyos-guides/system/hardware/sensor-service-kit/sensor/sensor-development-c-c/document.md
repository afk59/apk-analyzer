# Sensor Development (C/C++)

#### When to Use

With the sensor module, a device can obtain sensor data. For example, the device can subscribe to data of the orientation sensor to detect its own orientation, and data of the pedometer sensor to learn the number of steps the user walks every day.

For details about the APIs, see [Sensor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-sensor).

#### Function Description

| Name | Description |
| :-- | :-- |
| OH\_Sensor\_GetInfos(Sensor\_Info \*\*infos, uint32\_t \*count) | Obtains information about all sensors on the device. |
| OH\_Sensor\_Subscribe(const Sensor\_SubscriptionId \*id, const Sensor\_SubscriptionAttribute \*attribute, const Sensor\_Subscriber \*subscriber) | 
Subscribes to sensor data. The system will report sensor data to the subscriber at the specified frequency.

To subscribe to data of acceleration sensors, request the **ohos.permission.ACCELEROMETER** permission.

To subscribe to data of gyroscope sensors, request the **ohos.permission.GYROSCOPE** permission.

To subscribe to data of pedometer-related sensors, request the **ohos.permission.ACTIVITY\_MOTION** permission.

To subscribe to data of health-related sensors, such as heart rate sensors, request the **ohos.permission.READ\_HEALTH\_DATA** permission. Otherwise, the subscription fails.

You do not need to request any permission to subscribe to data of other types of sensors.

 |
| OH\_Sensor\_Unsubscribe(const Sensor\_SubscriptionId \*id, const Sensor\_Subscriber \*subscriber) | 

Unsubscribes from sensor data.

To unsubscribe from data of acceleration sensors, request the **ohos.permission.ACCELEROMETER** permission.

To unsubscribe from data of gyroscope sensors, request the **ohos.permission.GYROSCOPE** permission.

To unsubscribe from data of pedometer-related sensors, request the **ohos.permission.ACTIVITY\_MOTION** permission.

To unsubscribe from data of health-related sensors, request the **ohos.permission.READ\_HEALTH\_DATA** permission. Otherwise, the unsubscription fails.

You do not need to request any permission to unsubscribe from data of other types of sensors.

 |
| OH\_Sensor\_CreateInfos(uint32\_t count) | Creates an array of instances with the given number. For details, see [Sensor\_Info](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-sensor-sensor-info). |
| OH\_Sensor\_DestroyInfos(Sensor\_Info \*\*sensors, uint32\_t count) | Destroys the array of instances and reclaims the memory. For details, see [Sensor\_Info](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-sensor-sensor-info). |
| OH\_SensorInfo\_GetName(Sensor\_Info \*sensor, char \*sensorName, uint32\_t \*length) | Obtains the sensor name. |
| OH\_SensorInfo\_GetVendorName(Sensor\_Info\* sensor, char \*vendorName, uint32\_t \*length) | Obtains the sensor's vendor name. |
| OH\_SensorInfo\_GetType(Sensor\_Info\* sensor, Sensor\_Type \*sensorType) | Obtains the sensor type. |
| OH\_SensorInfo\_GetResolution(Sensor\_Info\* sensor, float \*resolution) | Obtains the sensor resolution. |
| OH\_SensorInfo\_GetMinSamplingInterval(Sensor\_Info\* sensor, int64\_t \*minSamplingInterval) | Obtains the minimum data reporting interval of a sensor. |
| OH\_SensorInfo\_GetMaxSamplingInterval(Sensor\_Info\* sensor, int64\_t \*maxSamplingInterval) | Obtains the maximum data reporting interval of a sensor. |
| OH\_SensorEvent\_GetType(Sensor\_Event\* sensorEvent, Sensor\_Type \*sensorType) | Obtains the sensor type. |
| OH\_SensorEvent\_GetTimestamp(Sensor\_Event\* sensorEvent, int64\_t \*timestamp) | Obtains the timestamp of sensor data. |
| OH\_SensorEvent\_GetAccuracy(Sensor\_Event\* sensorEvent, Sensor\_Accuracy \*accuracy) | Obtains the accuracy of sensor data. |
| OH\_SensorEvent\_GetData(Sensor\_Event\* sensorEvent, float \*\*data, uint32\_t \*length) | 

Obtains sensor data.

The data length and content depend on the sensor type. The format of the sensor data reported is as follows:

\- SENSOR\_TYPE\_ACCELEROMETER: data\[0\], data\[1\], and data\[2\], indicating the acceleration around the x, y, and z axes of a device, respectively, in m/s².

\- SENSOR\_TYPE\_GYROSCOPE: data\[0\], data\[1\], and data\[2\], indicating the angular velocity of rotation around the x, y, and z axes of a device, respectively, in rad/s.

\- SENSOR\_TYPE\_AMBIENT\_LIGHT: data\[0\], indicating the ambient light intensity, in lux. Since API version 12, two extra data records are returned, where **data\[1\]** indicates the color temperature (in kelvin), and **data\[2\]** indicates the infrared luminance (in cd/m²).

\- SENSOR\_TYPE\_MAGNETIC\_FIELD: data\[0\], data\[1\], and data\[2\], indicating the magnetic field strength around the x, y, and z axes of a device, respectively, in μT.

\- SENSOR\_TYPE\_BAROMETER: data\[0\], indicating the atmospheric pressure, in hPa.

\- SENSOR\_TYPE\_HALL: data\[0\], indicating the opening/closing state of the flip cover. The value **0** means that the flip cover is opened, and a value greater than 0 means that the flip cover is closed.

\- SENSOR\_TYPE\_PROXIMITY: data\[0\], indicates the approaching state. The value **0** means the two objects are close to each other, and a value greater than 0 means that they are far away from each other.

\- SENSOR\_TYPE\_ORIENTATION: data\[0\], data\[1\], and data\[2\], indicating the rotation angles of a device around the z, x, and y axes, respectively, in degree.

\- SENSOR\_TYPE\_GRAVITY: data\[0\], data\[1\], and data\[2\], indicating the gravitational acceleration around the x, y, and z axes of a device, respectively, in m/s².

\- SENSOR\_TYPE\_ROTATION\_VECTOR: data\[0\], data\[1\] and data\[2\], indicating the rotation angles of a device around the x, y, and z axes, respectively, in degree. data\[3\] indicates the rotation vector.

\- SENSOR\_TYPE\_PEDOMETER\_DETECTION: data\[0\], indicating the pedometer detection status. The value **1** means that the number of detected steps changes.

\- SENSOR\_TYPE\_PEDOMETER: data\[0\], indicating the number of steps a user has walked.

\- SENSOR\_TYPE\_HEART\_RATE: data\[0\], indicating the heart rate value.

 |
| OH\_Sensor\_CreateSubscriptionId(void) | Creates a **Sensor\_SubscriptionId** instance. |
| OH\_Sensor\_DestroySubscriptionId(Sensor\_SubscriptionId \*id) | Destroys a **Sensor\_SubscriptionId** instance and reclaims memory. |
| OH\_SensorSubscriptionId\_SetType(Sensor\_SubscriptionId\* id, const Sensor\_Type sensorType) | Sets the sensor type. |
| OH\_Sensor\_CreateSubscriptionAttribute(void) | Creates a **Sensor\_SubscriptionAttribute** instance. |
| OH\_Sensor\_DestroySubscriptionAttribute(Sensor\_SubscriptionAttribute \*attribute) | Destroys a **Sensor\_SubscriptionAttribute** instance and reclaims memory. |
| OH\_SensorSubscriptionAttribute\_SetSamplingInterval(Sensor\_SubscriptionAttribute\* attribute, const int64\_t samplingInterval) | Sets the interval for reporting sensor data. |
| OH\_Sensor\_CreateSubscriber(void) | Creates a **Sensor\_Subscriber** instance. |
| OH\_Sensor\_DestroySubscriber(Sensor\_Subscriber \*subscriber) | Destroys a **Sensor\_Subscriber** instance and reclaims memory. |
| OH\_SensorSubscriber\_SetCallback(Sensor\_Subscriber\* subscriber, const Sensor\_EventCallback callback) | Sets a callback function to report sensor data. |

#### How to Develop

The following uses the acceleration sensor as an example to describe the development procedure.

1.  Create a native C++ project.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/RPb-VirVRdSbAtOArw0amw/en-us_image_0000002568764837.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D3550B7FFD5487A64E189AFFF734B3572AA4B52517C7FC77E49866A47BD0E47)
    
2.  Configure the acceleration sensor permission. For details, see [Declaring Permissions](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
    
    "requestPermissions": \[
      {
        "name": "ohos.permission.ACCELEROMETER"
      }
    \]
    
3.  Add the dynamic dependency libraries into the **CMakeLists.txt** file.
    
    target\_link\_libraries(entry PUBLIC libace\_napi.z.so)
    target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC libohsensor.so)
    
4.  Write the **oh\_sensor\_capi.cpp** file to import related modules.
    
    #include "sensors/oh\_sensor.h"
    #include "napi/native\_api.h"
    #include "hilog/log.h"
    #include <thread>
    
5.  Define constants.
    
    const int SENSOR\_LOG\_DOMAIN = 0xD002700;
    const char \*TAG = "\[Sensor\]";
    constexpr Sensor\_Type SENSOR\_ID { SENSOR\_TYPE\_ACCELEROMETER };
    constexpr uint32\_t SENSOR\_NAME\_LENGTH\_MAX = 64;
    constexpr int64\_t SENSOR\_SAMPLE\_PERIOD = 200000000;
    constexpr int32\_t SLEEP\_TIME\_MS = 1000;
    constexpr int64\_t INVALID\_VALUE = -1;
    constexpr float INVALID\_RESOLUTION = -1.0F;
    Sensor\_Subscriber \*g\_user = nullptr;
    
6.  Define a callback function to receive sensor data.
    
    // Define the callback.
    void SensorDataCallbackImpl(Sensor\_Event \*event)
    {
        if (event == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "event is null");
            return;
        }
        int64\_t timestamp = INVALID\_VALUE;
        // Obtain the timestamp of sensor data.
        int32\_t ret = OH\_SensorEvent\_GetTimestamp(event, &timestamp);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get timestamp is failed");
            return;
        }
        Sensor\_Type sensorType;
        // Obtain the sensor type.
        ret = OH\_SensorEvent\_GetType(event, &sensorType);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor type is failed");
            return;
        }
        Sensor\_Accuracy accuracy = SENSOR\_ACCURACY\_UNRELIABLE;
        // Obtain the accuracy of sensor data.
        ret = OH\_SensorEvent\_GetAccuracy(event, &accuracy);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor accuracy is failed");
            return;
        }
        float \*data = nullptr;
        uint32\_t length = 0;
        // Obtain sensor data.
        ret = OH\_SensorEvent\_GetData(event, &data, &length);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor data is failed");
            return;
        }
        if (data == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "sensor data is null");
            return;
        }
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, SENSOR\_LOG\_DOMAIN, TAG,
            "sensorType:%{public}d, dataLen:%{public}d, accuracy:%{public}d", sensorType, length, accuracy);
        for (uint32\_t i = 0; i < length; ++i) {
            OH\_LOG\_Print(LOG\_APP, LOG\_INFO, SENSOR\_LOG\_DOMAIN, TAG, "data\[%{public}d\]:%{public}f", i, data\[i\]);
        }
    }
    
7.  Obtain information about all sensors on the device.
    
    static int32\_t GetSensorInfo(Sensor\_Info \*sensorInfoTemp)
    {
        char sensorName\[SENSOR\_NAME\_LENGTH\_MAX\] = {};
        uint32\_t length = SENSOR\_NAME\_LENGTH\_MAX;
        // Obtain the sensor name.
        int32\_t ret = OH\_SensorInfo\_GetName(sensorInfoTemp, sensorName, &length);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor name is failed");
            return ret;
        }
        char vendorName\[SENSOR\_NAME\_LENGTH\_MAX\] = {};
        length = SENSOR\_NAME\_LENGTH\_MAX;
        // Obtain the sensor's vendor name.
        ret = OH\_SensorInfo\_GetVendorName(sensorInfoTemp, vendorName, &length);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor vender name is failed");
            return ret;
        }
        Sensor\_Type sensorType;
        // Obtain the sensor type.
        ret = OH\_SensorInfo\_GetType(sensorInfoTemp, &sensorType);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor type is failed");
            return ret;
        }
        float resolution = INVALID\_RESOLUTION;
        // Obtain the sensor resolution.
        ret = OH\_SensorInfo\_GetResolution(sensorInfoTemp, &resolution);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor resolution is failed");
            return ret;
        }
        int64\_t minSamplePeriod = INVALID\_VALUE;
        // Obtain the minimum data reporting interval of a sensor.
        ret = OH\_SensorInfo\_GetMinSamplingInterval(sensorInfoTemp, &minSamplePeriod);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor min sampling interval is failed");
            return ret;
        }
        int64\_t maxSamplePeriod = INVALID\_VALUE;
        // Obtain the maximum data reporting interval of a sensor.
        ret = OH\_SensorInfo\_GetMaxSamplingInterval(sensorInfoTemp, &maxSamplePeriod);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor max sampling interval is failed");
        }
        return ret;
    }
    
    static napi\_value GetSensorInfos(napi\_env env, napi\_callback\_info info)
    {
        uint32\_t count = 0;
        // Obtain the number of all sensors on the device.
        int32\_t ret = OH\_Sensor\_GetInfos(nullptr, &count);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor count is failed");
            return nullptr;
        }
        // Create an array of instances with the given number.
        Sensor\_Info \*\*sensors = OH\_Sensor\_CreateInfos(count);
        if (sensors == nullptr) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "create sensorInfo array is failed");
            return nullptr;
        }
        // Obtain information about all sensors on the device.
        ret = OH\_Sensor\_GetInfos(sensors, &count);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get all sensor info is failed");
            return nullptr;
        }
        for (uint32\_t i = 0; i < count; ++i) {
            Sensor\_Info \*sensorInfoTemp = sensors\[i\];
            ret = GetSensorInfo(sensorInfoTemp);
            if (ret != SENSOR\_SUCCESS) {
                OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "get sensor info failed");
                return nullptr;
            }
        }
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, SENSOR\_LOG\_DOMAIN, TAG, "GetSensorInfos successful");
        // Destroy the instance array and reclaim memory.
        ret = OH\_Sensor\_DestroyInfos(sensors, count);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "destroy sensor info is failed");
            return nullptr;
        }
        return nullptr;
    }
    
8.  Subscribe to and unsubscribe from sensor data.
    
    static napi\_value Subscriber(napi\_env env, napi\_callback\_info info)
    {
        // Create a Sensor\_Subscriber instance.
        g\_user = OH\_Sensor\_CreateSubscriber();
        // Set the callback used to return sensor data.
        int32\_t ret = OH\_SensorSubscriber\_SetCallback(g\_user, SensorDataCallbackImpl);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "OH\_SensorSubscriber\_SetCallback failed");
            return nullptr;
        }
        // Create a Sensor\_SubscriptionId instance.
        Sensor\_SubscriptionId \*id = OH\_Sensor\_CreateSubscriptionId();
        // Set the sensor type. For example, if you use SENSOR\_TYPE\_ACCELEROMETER, you need to request the ohos.permission.ACCELEROMETER permission.
        // Configure the required permission as instructed in step 2 in the Sensor Development.
        ret = OH\_SensorSubscriptionId\_SetType(id, SENSOR\_ID);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "OH\_SensorSubscriptionId\_SetType failed");
            return nullptr;
        }
        // Create a Sensor\_SubscriptionAttribute instance.
        Sensor\_SubscriptionAttribute \*attr = OH\_Sensor\_CreateSubscriptionAttribute();
        // Set the sensor data reporting interval.
        ret = OH\_SensorSubscriptionAttribute\_SetSamplingInterval(attr, SENSOR\_SAMPLE\_PERIOD);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG,
                "OH\_SensorSubscriptionAttribute\_SetSamplingInterval failed");
            return nullptr;
        }
        // Subscribe to sensor data.
        ret = OH\_Sensor\_Subscribe(id, attr, g\_user);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "OH\_Sensor\_Subscribe failed");
            return nullptr;
        }
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, SENSOR\_LOG\_DOMAIN, TAG, "OH\_Sensor\_Subscribe successful");
        std::this\_thread::sleep\_for(std::chrono::milliseconds(SLEEP\_TIME\_MS));
        // Unsubscribe from sensor data.
        ret = OH\_Sensor\_Unsubscribe(id, g\_user);
        if (ret != SENSOR\_SUCCESS) {
            OH\_LOG\_Print(LOG\_APP, LOG\_ERROR, SENSOR\_LOG\_DOMAIN, TAG, "OH\_Sensor\_Unsubscribe failed");
            return nullptr;
        }
        OH\_LOG\_Print(LOG\_APP, LOG\_INFO, SENSOR\_LOG\_DOMAIN, TAG, "OH\_Sensor\_Unsubscribe successful");
        if (id != nullptr) {
            // Destroy the Sensor\_SubscriptionId instance.
            OH\_Sensor\_DestroySubscriptionId(id);
        }
        if (attr != nullptr) {
            // Destroy the Sensor\_SubscriptionAttribute instance.
            OH\_Sensor\_DestroySubscriptionAttribute(attr);
        }
        if (g\_user != nullptr) {
            // Destroy the Sensor\_Subscriber instance and reclaim memory.
            OH\_Sensor\_DestroySubscriber(g\_user);
            g\_user = nullptr;
        }
        return nullptr;
    }
    
9.  Add related APIs to the **Init** function.
    
    EXTERN\_C\_START
    static napi\_value Init(napi\_env env, napi\_value exports)
    {
        napi\_property\_descriptor desc\[\] = {
            {"getSensorInfos", nullptr, GetSensorInfos, nullptr, nullptr, nullptr, napi\_default, nullptr},
            {"subscriber", nullptr, Subscriber, nullptr, nullptr, nullptr, napi\_default, nullptr}
        };
        napi\_define\_properties(env, exports, sizeof(desc) / sizeof(desc\[0\]), desc);
        return exports;
    }
    EXTERN\_C\_END
    
10.  Introduce the NAPI APIs to the **index.d.ts** file in **types/libentry**.
     
     export const getSensorInfos: () => object;
     export const subscriber: () => object;
     
11.  Write the application entry call code.
     
     import { BusinessError } from '@kit.BasicServicesKit';
     import { hilog } from '@kit.PerformanceAnalysisKit';
     import sensorCapi from 'libentry.so';
     
     const DOMAIN = 0xD002700;
     // ...
               try {
                 sensorCapi.getSensorInfos();
                 // ...
               } catch (error) {
                 let e: BusinessError = error as BusinessError;
                 hilog.error(DOMAIN, 'testTag', \`Failed to invoke getSensorInfos. Code: ${e.code}, message: ${e.message}\`);
               }
               // ...
               try {
                 sensorCapi.subscriber();
                 // ...
               } catch (error) {
                 let e: BusinessError = error as BusinessError;
                 hilog.error(DOMAIN, 'testTag', \`Failed to invoke getSensorInfos. Code: ${e.code}, message: ${e.message}\`);
               }
