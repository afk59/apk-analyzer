# oh\_sensor.h

#### Overview

The **oh\_sensor.h** file declares the APIs for operating sensors, including obtaining sensor information and subscribing to and unsubscribing from sensor data.

**File to include**: <sensors/oh\_sensor.h>

**Library**: libohsensor.so

**System capability**: SystemCapability.Sensors.Sensor

**Since**: 11

**Related module**: [Sensor](../../modules/sensor/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Sensor\_Result OH\_Sensor\_GetInfos(Sensor\_Info \*\*infos, uint32\_t \*count)](#oh_sensor_getinfos) | Obtains information about all sensors on the device. |
| [Sensor\_Result OH\_Sensor\_Subscribe(const Sensor\_SubscriptionId \*id, const Sensor\_SubscriptionAttribute \*attribute, const Sensor\_Subscriber \*subscriber)](#oh_sensor_subscribe) | Subscribes to sensor data. The system will report sensor data to the subscriber at the specified frequency. To subscribe to data of acceleration sensors, request the **ohos.permission.ACCELEROMETER** permission. To subscribe to data of gyroscope sensors, request the **ohos.permission.GYROSCOPE** permission. To subscribe to data of pedometer-related sensors, request the **ohos.permission.ACTIVITY\_MOTION** permission. To subscribe to data of health-related sensors, such as heart rate sensors, request the **ohos.permission.READ\_HEALTH\_DATA** permission. Otherwise, the subscription fails. You do not need to request any permission to subscribe to data of other types of sensors. |
| [Sensor\_Result OH\_Sensor\_Unsubscribe(const Sensor\_SubscriptionId \*id, const Sensor\_Subscriber \*subscriber)](#oh_sensor_unsubscribe) | Unsubscribes from sensor data. To unsubscribe from data of acceleration sensors, request the **ohos.permission.ACCELEROMETER** permission. To unsubscribe from data of gyroscope sensors, request the **ohos.permission.GYROSCOPE** permission. To unsubscribe from data of pedometer-related sensors, request the **ohos.permission.ACTIVITY\_MOTION** permission. To unsubscribe from data of health-related sensors, request the **ohos.permission.READ\_HEALTH\_DATA** permission. Otherwise, the unsubscription fails. You do not need to request any permission to unsubscribe from data of other types of sensors. |

#### Function Description

#### \[h2\]OH\_Sensor\_GetInfos()

Sensor\_Result OH\_Sensor\_GetInfos(Sensor\_Info \*\*infos, uint32\_t \*count)

**Description**

Obtains information about all sensors on the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md) \*\*infos | Double pointer to the information about all sensors on the device. For details, see [Sensor\_Info](../../structs/sensor-info/document.md). |
| uint32\_t \*count | Pointer to the number of sensors on the device. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Sensor\_Result](../oh-sensor-type-h/document.md#sensor_result) | 
**SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](../oh-sensor-type-h/document.md#sensor_result) otherwise. The error code can be:

\- [SENSOR\_PARAMETER\_ERROR](../oh-sensor-type-h/document.md#sensor_result) if the parameter verification fails. For example, the parameter is invalid or the parameter type is incorrect.

\- [SENSOR\_SERVICE\_EXCEPTION](../oh-sensor-type-h/document.md#sensor_result) if the sensor service is abnormal.

 |

#### \[h2\]OH\_Sensor\_Subscribe()

Sensor\_Result OH\_Sensor\_Subscribe(const Sensor\_SubscriptionId \*id, const Sensor\_SubscriptionAttribute \*attribute, const Sensor\_Subscriber \*subscriber)

**Description**

Subscribes to sensor data. The system will report sensor data to the subscriber at the specified frequency. To subscribe to data of acceleration sensors, request the **ohos.permission.ACCELEROMETER** permission. To subscribe to data of gyroscope sensors, request the **ohos.permission.GYROSCOPE** permission. To subscribe to data of pedometer-related sensors, request the **ohos.permission.ACTIVITY\_MOTION** permission. To subscribe to data of health-related sensors, such as heart rate sensors, request the **ohos.permission.READ\_HEALTH\_DATA** permission. Otherwise, the subscription fails. You do not need to request any permission to subscribe to data of other types of sensors.

**Required permissions:** ohos.permission.ACCELEROMETER or ohos.permission.GYROSCOPE or

ohos.permission.ACTIVITY\_MOTION or ohos.permission.READ\_HEALTH\_DATA

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) \*id | Pointer to the sensor subscription ID. For details, see [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md). |
| [const Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) \*attribute | Pointer to the subscription attribute, which is used to specify the data reporting frequency. For details, see [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md). |
| [const Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) \*subscriber | Pointer to the subscriber information, which is used by the callback function to report sensor data. For details, see [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Sensor\_Result](../oh-sensor-type-h/document.md#sensor_result) | 
**SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](../oh-sensor-type-h/document.md#sensor_result) otherwise. The error code can be:

\- [SENSOR\_PERMISSION\_DENIED](../oh-sensor-type-h/document.md#sensor_result) if the permission verification fails.

\- [SENSOR\_PARAMETER\_ERROR](../oh-sensor-type-h/document.md#sensor_result) if the parameter verification fails. For example, the parameter is invalid or the parameter type is incorrect.

\- [SENSOR\_SERVICE\_EXCEPTION](../oh-sensor-type-h/document.md#sensor_result) if the sensor service is abnormal.

 |

#### \[h2\]OH\_Sensor\_Unsubscribe()

Sensor\_Result OH\_Sensor\_Unsubscribe(const Sensor\_SubscriptionId \*id, const Sensor\_Subscriber \*subscriber)

**Description**

Unsubscribes from sensor data. To unsubscribe from data of acceleration sensors, request the **ohos.permission.ACCELEROMETER** permission. To unsubscribe from data of gyroscope sensors, request the **ohos.permission.GYROSCOPE** permission. To unsubscribe from data of pedometer-related sensors, request the **ohos.permission.ACTIVITY\_MOTION** permission. To unsubscribe from data of health-related sensors, request the **ohos.permission.READ\_HEALTH\_DATA** permission. Otherwise, the unsubscription fails. You do not need to request any permission to unsubscribe from data of other types of sensors.

**Required permissions:** ohos.permission.ACCELEROMETER or ohos.permission.GYROSCOPE or

ohos.permission.ACTIVITY\_MOTION or ohos.permission.READ\_HEALTH\_DATA

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [const Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) \*id | Pointer to the sensor subscription ID. For details, see [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md). |
| [const Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) \*subscriber | Pointer to the subscriber information, which is used by the callback function to report sensor data. For details, see [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Sensor\_Result](../oh-sensor-type-h/document.md#sensor_result) | 
**SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](../oh-sensor-type-h/document.md#sensor_result) otherwise. The error code can be:

\- [SENSOR\_PERMISSION\_DENIED](../oh-sensor-type-h/document.md#sensor_result) if the permission verification fails.

\- [SENSOR\_PARAMETER\_ERROR](../oh-sensor-type-h/document.md#sensor_result) if the parameter verification fails. For example, the parameter is invalid or the parameter type is incorrect.

\- [SENSOR\_SERVICE\_EXCEPTION](../oh-sensor-type-h/document.md#sensor_result) if the sensor service is abnormal.

 |
