# oh\_sensor\_type.h

#### Overview

Declares the common sensor attributes.

**Reference file**: <sensors/oh\_sensor\_type.h>

**Library**: libohsensor.so

**System capability**: SystemCapability.Sensors.Sensor

**Since**: 11

**Related module**: [Sensor](../../modules/sensor/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md) | Sensor\_Info | Defines a struct for the sensor information. |
| [Sensor\_Event](../../structs/sensor-event/document.md) | Sensor\_Event | Defines a struct for the sensor data information. |
| [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) | Sensor\_SubscriptionId | Defines a struct for the sensor subscription ID, which uniquely identifies a sensor. |
| [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) | Sensor\_SubscriptionAttribute | Defines a struct for the sensor subscription attribute. |
| [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) | Sensor\_Subscriber | Defines a struct for the sensor subscriber information. |

#### \[h2\]Enumeration

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Sensor\_Type](#sensor_type) | Sensor\_Type | Enumerates the sensor types. |
| [Sensor\_Result](#sensor_result) | Sensor\_Result | Enumerates the sensor result codes. |
| [Sensor\_Accuracy](#sensor_accuracy) | Sensor\_Accuracy | Enumerates the accuracy levels of data reported by a sensor. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Sensor\_Info \*\*OH\_Sensor\_CreateInfos(uint32\_t count)](#oh_sensor_createinfos) | \- | Creates an instance array using a given number. For details, see [Sensor\_Info](../../structs/sensor-info/document.md). |
| [int32\_t OH\_Sensor\_DestroyInfos(Sensor\_Info \*\*sensors, uint32\_t count)](#oh_sensor_destroyinfos) | \- | Destroys the instance array and reclaims the memory. For details, see [Sensor\_Info](../../structs/sensor-info/document.md). |
| [int32\_t OH\_SensorInfo\_GetName(Sensor\_Info\* sensor, char \*sensorName, uint32\_t \*length)](#oh_sensorinfo_getname) | \- | Obtains the sensor name. |
| [int32\_t OH\_SensorInfo\_GetVendorName(Sensor\_Info\* sensor, char \*vendorName, uint32\_t \*length)](#oh_sensorinfo_getvendorname) | \- | Obtains the sensor's vendor name. |
| [int32\_t OH\_SensorInfo\_GetType(Sensor\_Info\* sensor, Sensor\_Type \*sensorType)](#oh_sensorinfo_gettype) | \- | Obtains the sensor type. |
| [int32\_t OH\_SensorInfo\_GetResolution(Sensor\_Info\* sensor, float \*resolution)](#oh_sensorinfo_getresolution) | \- | Obtains the sensor resolution. |
| [int32\_t OH\_SensorInfo\_GetMinSamplingInterval(Sensor\_Info\* sensor, int64\_t \*minSamplingInterval)](#oh_sensorinfo_getminsamplinginterval) | \- | Obtains the minimum data reporting interval of a sensor. |
| [int32\_t OH\_SensorInfo\_GetMaxSamplingInterval(Sensor\_Info\* sensor, int64\_t \*maxSamplingInterval)](#oh_sensorinfo_getmaxsamplinginterval) | \- | Obtains the maximum data reporting interval of a sensor. |
| [int32\_t OH\_SensorEvent\_GetType(Sensor\_Event\* sensorEvent, Sensor\_Type \*sensorType)](#oh_sensorevent_gettype) | \- | Obtains the sensor type. |
| [int32\_t OH\_SensorEvent\_GetTimestamp(Sensor\_Event\* sensorEvent, int64\_t \*timestamp)](#oh_sensorevent_gettimestamp) | \- | Obtains the timestamp of sensor data. |
| [int32\_t OH\_SensorEvent\_GetAccuracy(Sensor\_Event\* sensorEvent, Sensor\_Accuracy \*accuracy)](#oh_sensorevent_getaccuracy) | \- | Obtains the accuracy of sensor data. |
| [int32\_t OH\_SensorEvent\_GetData(Sensor\_Event\* sensorEvent, float \*\*data, uint32\_t \*length)](#oh_sensorevent_getdata) | \- | 
Obtains sensor data. The data length and content depend on the sensor type. The format of the sensor data reported is as follows:

\- SENSOR\_TYPE\_ACCELEROMETER: data\[0\], data\[1\], and data\[2\], indicating the acceleration around the x, y, and z axes of a device, respectively, in m/s². - SENSOR\_TYPE\_GYROSCOPE: data\[0\], data\[1\], and data\[2\], indicating the angular velocity of rotation around the x, y, and z axes of a device, respectively, in rad/s.

\- SENSOR\_TYPE\_AMBIENT\_LIGHT: data\[0\], indicating the ambient light intensity, in lux. Two additional data values are returned since API version 12. data\[1\] indicates the color temperature, in kelvin, and data\[2\] indicates the infrared luminance, in cd/m².

\- SENSOR\_TYPE\_MAGNETIC\_FIELD: data\[0\], data\[1\], and data\[2\], indicating the magnetic field strength around the x, y, and z axes of a device, respectively, in μT.

\- SENSOR\_TYPE\_BAROMETER: data\[0\], indicating the atmospheric pressure, in hPa.

\- SENSOR\_TYPE\_HALL: data\[0\], indicating the opening/closing state of the flip cover. The value **0** means that the flip cover is opened, and a value greater than 0 means that the flip cover is closed.

\- SENSOR\_TYPE\_PROXIMITY: data\[0\], indicates the approaching state. The value **0** means the two objects are close to each other, and a value greater than 0 means that they are far away from each other.

\- SENSOR\_TYPE\_ORIENTATION: data\[0\], data\[1\], and data\[2\], indicating the rotation angles of a device around the z, x, and y axes, respectively, in degree.

\- SENSOR\_TYPE\_GRAVITY: data\[0\], data\[1\], and data\[2\], indicating the gravitational acceleration around the x, y, and z axes of a device, respectively, in m/s2.

\- SENSOR\_TYPE\_ROTATION\_VECTOR: data\[0\], data\[1\] and data\[2\], indicating the rotation angles of a device around the x, y, and z axes, respectively, in degree. data\[3\] indicates the rotation vector.

\- SENSOR\_TYPE\_PEDOMETER\_DETECTION: data\[0\], indicating the pedometer detection status. The value **1** means that the number of detected steps changes.

\- SENSOR\_TYPE\_PEDOMETER: data\[0\], indicating the number of steps a user has walked.

\- SENSOR\_TYPE\_HEART\_RATE: data\[0\], indicating the heart rate value.

\- SENSOR\_TYPE\_LINEAR\_ACCELERATION: data\[0\], data\[1\], and data\[2\], indicating the linear acceleration of the device on the x, y, and z axes, respectively, in m/s2. This field is supported since API version 13.

\- SENSOR\_TYPE\_GAME\_ROTATION\_VECTOR: data\[0\], data\[1\], and data\[2\], indicating the rotation angles of the device around the x, y, and z axes, respectively, in degree; data\[3\], indicating the rotation vector. This field is supported since API version 13.

 |
| [Sensor\_SubscriptionId \*OH\_Sensor\_CreateSubscriptionId(void)](#oh_sensor_createsubscriptionid) | \- | Creates a [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) instance. |
| [int32\_t OH\_Sensor\_DestroySubscriptionId(Sensor\_SubscriptionId \*id)](#oh_sensor_destroysubscriptionid) | \- | Destroys a [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) instance and reclaims the memory. |
| [int32\_t OH\_SensorSubscriptionId\_GetType(Sensor\_SubscriptionId\* id, Sensor\_Type \*sensorType)](#oh_sensorsubscriptionid_gettype) | \- | Obtains the sensor type. |
| [int32\_t OH\_SensorSubscriptionId\_SetType(Sensor\_SubscriptionId\* id, const Sensor\_Type sensorType)](#oh_sensorsubscriptionid_settype) | \- | Sets the sensor type. |
| [Sensor\_SubscriptionAttribute \*OH\_Sensor\_CreateSubscriptionAttribute(void)](#oh_sensor_createsubscriptionattribute) | \- | Creates a [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) instance. |
| [int32\_t OH\_Sensor\_DestroySubscriptionAttribute(Sensor\_SubscriptionAttribute \*attribute)](#oh_sensor_destroysubscriptionattribute) | \- | Destroys a [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) instance and reclaims the memory. |
| [int32\_t OH\_SensorSubscriptionAttribute\_SetSamplingInterval(Sensor\_SubscriptionAttribute\* attribute, const int64\_t samplingInterval)](#oh_sensorsubscriptionattribute_setsamplinginterval) | \- | Sets the sensor data reporting interval. |
| [int32\_t OH\_SensorSubscriptionAttribute\_GetSamplingInterval(Sensor\_SubscriptionAttribute\* attribute, int64\_t \*samplingInterval)](#oh_sensorsubscriptionattribute_getsamplinginterval) | \- | Obtains the sensor data reporting interval. |
| [typedef void (\*Sensor\_EventCallback)(Sensor\_Event \*event)](#sensor_eventcallback) | Sensor\_EventCallback | Defines the callback function used to report sensor data. |
| [Sensor\_Subscriber \*OH\_Sensor\_CreateSubscriber(void)](#oh_sensor_createsubscriber) | \- | Creates a [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) instance. |
| [int32\_t OH\_Sensor\_DestroySubscriber(Sensor\_Subscriber \*subscriber)](#oh_sensor_destroysubscriber) | \- | Destroys a [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) instance and reclaims the memory. |
| [int32\_t OH\_SensorSubscriber\_SetCallback(Sensor\_Subscriber\* subscriber, const Sensor\_EventCallback callback)](#oh_sensorsubscriber_setcallback) | \- | Sets a callback function to report sensor data. |
| [int32\_t OH\_SensorSubscriber\_GetCallback(Sensor\_Subscriber\* subscriber, Sensor\_EventCallback \*callback)](#oh_sensorsubscriber_getcallback) | \- | Obtains the callback function used to report sensor data. |

#### Enum Description

#### \[h2\]Sensor\_Type

enum Sensor\_Type

**Description**

Enumerates the sensor types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| SENSOR\_TYPE\_ACCELEROMETER = 1 | 
Acceleration sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_GYROSCOPE = 2 | 

Gyroscope sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_AMBIENT\_LIGHT = 5 | 

Ambient light sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_MAGNETIC\_FIELD = 6 | 

Magnetic field sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_BAROMETER = 8 | 

Barometer sensor

**Since**: 11

 |
| SENSOR\_TYPE\_HALL = 10 | 

Hall effect sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_PROXIMITY = 12 | 

Proximity sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_ORIENTATION = 256 | 

Orientation sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_GRAVITY = 257 | 

Gravity sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_LINEAR\_ACCELERATION = 258 | 

Linear acceleration sensor.

**Since**: 13

 |
| SENSOR\_TYPE\_ROTATION\_VECTOR = 259 | 

Rotation vector sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_GAME\_ROTATION\_VECTOR = 262 | 

Game rotation vector sensor

**Since**: 13

 |
| SENSOR\_TYPE\_PEDOMETER\_DETECTION = 265 | 

Pedometer detection sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_PEDOMETER = 266 | 

Pedometer sensor.

**Since**: 11

 |
| SENSOR\_TYPE\_HEART\_RATE = 278 | 

Heart rate sensor.

**Since**: 11

 |

#### \[h2\]Sensor\_Result

enum Sensor\_Result

**Description**

Enumerates the sensor result codes.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| SENSOR\_SUCCESS = 0 | 
Operation success.

**Since**: 11

 |
| SENSOR\_PERMISSION\_DENIED = 201 | 

Permission verification failed.

**Since**: 11

 |
| SENSOR\_PARAMETER\_ERROR = 401 | 

An error occurs during parameter verification. For example, a mandatory parameter is not passed in, or the parameter type passed in is incorrect.

**Since**: 11

 |
| SENSOR\_SERVICE\_EXCEPTION = 14500101 | 

The sensor service is abnormal.

**Since**: 11

 |

#### \[h2\]Sensor\_Accuracy

enum Sensor\_Accuracy

**Description**

Enumerates the accuracy levels of data reported by a sensor.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| SENSOR\_ACCURACY\_UNRELIABLE = 0 | 
The sensor data is unreliable. It is possible that the sensor does not contact with the device to measure.

**Since**: 11

 |
| SENSOR\_ACCURACY\_LOW = 1 | 

The sensor data is at a low accuracy level. The data must be calibrated based on the environment before being used.

**Since**: 11

 |
| SENSOR\_ACCURACY\_MEDIUM = 2 | 

The sensor data is at a medium accuracy level. You are advised to calibrate the data based on the environment before using it.

**Since**: 11

 |
| SENSOR\_ACCURACY\_HIGH = 3 | 

The sensor data is at a high accuracy level. The data can be used directly.

**Since**: 11

 |

#### Function Description

#### \[h2\]OH\_Sensor\_CreateInfos()

Sensor\_Info \*\*OH\_Sensor\_CreateInfos(uint32\_t count)

**Description**

Creates an instance array using a given number. For details, see [Sensor\_Info](../../structs/sensor-info/document.md).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| uint32\_t count | Number of instances to be created. For details, see [Sensor\_Info](../../structs/sensor-info/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Sensor\_Info \*\*](../../structs/sensor-info/document.md) | Double pointer to the [Sensor\_Info](../../structs/sensor-info/document.md) instance array if the operation is successful; NULL otherwise. |

#### \[h2\]OH\_Sensor\_DestroyInfos()

int32\_t OH\_Sensor\_DestroyInfos(Sensor\_Info \*\*sensors, uint32\_t count)

**Description**

Destroys the sensor instance array and reclaims the memory. For details, see [Sensor\_Info](../../structs/sensor-info/document.md).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md) \*\*sensors | Double pointer to the [Sensor\_Info](../../structs/sensor-info/document.md) instance array. |
| uint32\_t count | Number of [Sensor\_Info](../../structs/sensor-info/document.md) instances to be destroyed. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorInfo\_GetName()

int32\_t OH\_SensorInfo\_GetName(Sensor\_Info\* sensor, char \*sensorName, uint32\_t \*length)

**Description**

Obtains the sensor name.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md)\* sensor | Pointer to the sensor information. |
| char \*sensorName | Pointer to the sensor data. |
| uint32\_t \*length | Pointer to the length, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorInfo\_GetVendorName()

int32\_t OH\_SensorInfo\_GetVendorName(Sensor\_Info\* sensor, char \*vendorName, uint32\_t \*length)

**Description**

Obtains the sensor's vendor name.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md)\* sensor | Pointer to the sensor information. |
| char \*vendorName | Pointer to the vendor name. |
| uint32\_t \*length | Pointer to the length, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorInfo\_GetType()

int32\_t OH\_SensorInfo\_GetType(Sensor\_Info\* sensor, Sensor\_Type \*sensorType)

**Description**

Obtains the sensor type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md)\* sensor | Pointer to the sensor information. |
| [Sensor\_Type](#sensor_type) \*sensorType | Pointer to the sensor type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorInfo\_GetResolution()

int32\_t OH\_SensorInfo\_GetResolution(Sensor\_Info\* sensor, float \*resolution)

**Description**

Obtains the sensor resolution.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md)\* sensor | Pointer to the sensor information. |
| float \*resolution | Pointer to the sensor resolution [Sensor\_Accuracy](#sensor_accuracy). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorInfo\_GetMinSamplingInterval()

int32\_t OH\_SensorInfo\_GetMinSamplingInterval(Sensor\_Info\* sensor, int64\_t \*minSamplingInterval)

**Description**

Obtains the minimum data reporting interval of a sensor.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md)\* sensor | Pointer to the sensor information. |
| int64\_t \*minSamplingInterval | Pointer to the minimum data reporting interval, in nanoseconds. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorInfo\_GetMaxSamplingInterval()

int32\_t OH\_SensorInfo\_GetMaxSamplingInterval(Sensor\_Info\* sensor, int64\_t \*maxSamplingInterval)

**Description**

Obtains the maximum data reporting interval of a sensor.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Info](../../structs/sensor-info/document.md)\* sensor | Pointer to the sensor information. |
| int64\_t \*maxSamplingInterval | Pointer to the maximum data reporting interval, in nanoseconds. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorEvent\_GetType()

int32\_t OH\_SensorEvent\_GetType(Sensor\_Event\* sensorEvent, Sensor\_Type \*sensorType)

**Description**

Obtains the sensor type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Event](../../structs/sensor-event/document.md)\* sensorEvent | Pointer to the sensor data information. |
| [Sensor\_Type](#sensor_type) \*sensorType | Pointer to the sensor type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorEvent\_GetTimestamp()

int32\_t OH\_SensorEvent\_GetTimestamp(Sensor\_Event\* sensorEvent, int64\_t \*timestamp)

**Description**

Obtains the timestamp of sensor data.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Event](../../structs/sensor-event/document.md)\* sensorEvent | Pointer to the sensor data information. |
| int64\_t \*timestamp | Pointer to the timestamp. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorEvent\_GetAccuracy()

int32\_t OH\_SensorEvent\_GetAccuracy(Sensor\_Event\* sensorEvent, Sensor\_Accuracy \*accuracy)

**Description**

Obtains the accuracy of sensor data.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Event](../../structs/sensor-event/document.md)\* sensorEvent | Pointer to the sensor data information. |
| [Sensor\_Accuracy](#sensor_accuracy) \*accuracy | Pointer to the accuracy. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorEvent\_GetData()

int32\_t OH\_SensorEvent\_GetData(Sensor\_Event\* sensorEvent, float \*\*data, uint32\_t \*length)

**Description**

Obtains sensor data. The data length and content depend on the sensor type. The format of the sensor data reported is as follows:

\- SENSOR\_TYPE\_ACCELEROMETER: data\[0\], data\[1\], and data\[2\], indicating the acceleration around the x, y, and z axes of a device, respectively, in m/s². - SENSOR\_TYPE\_GYROSCOPE: data\[0\], data\[1\], and data\[2\], indicating the angular velocity of rotation around the x, y, and z axes of a device, respectively, in rad/s.

\- SENSOR\_TYPE\_AMBIENT\_LIGHT: data\[0\], indicating the ambient light intensity, in lux. Two additional data values are returned since API version 12. data\[1\] indicates the color temperature, in kelvin, and data\[2\] indicates the infrared luminance, in cd/m².

\- SENSOR\_TYPE\_MAGNETIC\_FIELD: data\[0\], data\[1\], and data\[2\], indicating the magnetic field strength around the x, y, and z axes of a device, respectively, in μT.

\- SENSOR\_TYPE\_BAROMETER: data\[0\], indicating the atmospheric pressure, in hPa.

\- SENSOR\_TYPE\_HALL: data\[0\], indicating the opening/closing state of the flip cover. The value **0** means that the flip cover is opened, and a value greater than 0 means that the flip cover is closed.

\- SENSOR\_TYPE\_PROXIMITY: data\[0\], indicates the approaching state. The value **0** means the two objects are close to each other, and a value greater than 0 means that they are far away from each other.

\- SENSOR\_TYPE\_ORIENTATION: data\[0\], data\[1\], and data\[2\], indicating the rotation angles of a device around the z, x, and y axes, respectively, in degree.

\- SENSOR\_TYPE\_GRAVITY: data\[0\], data\[1\], and data\[2\], indicating the gravitational acceleration around the x, y, and z axes of a device, respectively, in m/s2.

\- SENSOR\_TYPE\_ROTATION\_VECTOR: data\[0\], data\[1\] and data\[2\], indicating the rotation angles of a device around the x, y, and z axes, respectively, in degree. data\[3\] indicates the rotation vector.

\- SENSOR\_TYPE\_PEDOMETER\_DETECTION: data\[0\], indicating the pedometer detection status. The value **1** means that the number of detected steps changes.

\- SENSOR\_TYPE\_PEDOMETER: data\[0\], indicating the number of steps a user has walked.

\- SENSOR\_TYPE\_HEART\_RATE: data\[0\], indicating the heart rate value.

\- SENSOR\_TYPE\_LINEAR\_ACCELERATION: data\[0\], data\[1\], and data\[2\], indicating the linear acceleration of the device on the x, y, and z axes, respectively, in m/s2. This field is supported since API version 13.

\- SENSOR\_TYPE\_GAME\_ROTATION\_VECTOR: data\[0\], data\[1\], and data\[2\], indicating the rotation angles of the device around the x, y, and z axes, respectively, in degree; data\[3\], indicating the rotation vector. This field is supported since API version 13.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Event](../../structs/sensor-event/document.md)\* sensorEvent | Pointer to the sensor data information. |
| float \*\*data | Double pointer to the sensor data. |
| uint32\_t \*length | Pointer to the array length. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_Sensor\_CreateSubscriptionId()

Sensor\_SubscriptionId \*OH\_Sensor\_CreateSubscriptionId(void)

**Description**

Creates a [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) instance.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [Sensor\_SubscriptionId \*](../../structs/sensor-subscriptionid/document.md) | Pointer to the [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) instance if the operation is successful; **NULL** otherwise. |

#### \[h2\]OH\_Sensor\_DestroySubscriptionId()

int32\_t OH\_Sensor\_DestroySubscriptionId(Sensor\_SubscriptionId \*id)

**Description**

Destroys a [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) instance and reclaims the memory.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) \*id | Pointer to the [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorSubscriptionId\_GetType()

int32\_t OH\_SensorSubscriptionId\_GetType(Sensor\_SubscriptionId\* id, Sensor\_Type \*sensorType)

**Description**

Obtains the sensor type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md)\* id | Pointer to the sensor subscription ID. |
| [Sensor\_Type](#sensor_type) \*sensorType | Pointer to the sensor type. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorSubscriptionId\_SetType()

int32\_t OH\_SensorSubscriptionId\_SetType(Sensor\_SubscriptionId\* id, const Sensor\_Type sensorType)

**Description**

Sets the sensor type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_SubscriptionId](../../structs/sensor-subscriptionid/document.md)\* id | Pointer to the sensor subscription ID. |
| [const Sensor\_Type](#sensor_type) sensorType | Sensor type to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_Sensor\_CreateSubscriptionAttribute()

Sensor\_SubscriptionAttribute \*OH\_Sensor\_CreateSubscriptionAttribute(void)

**Description**

Creates a [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) instance.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [Sensor\_SubscriptionAttribute \*](../../structs/sensor-subscriptionattribute/document.md) | Pointer to the [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) instance if the operation is successful; **NULL** otherwise. |

#### \[h2\]OH\_Sensor\_DestroySubscriptionAttribute()

int32\_t OH\_Sensor\_DestroySubscriptionAttribute(Sensor\_SubscriptionAttribute \*attribute)

**Description**

Destroys a [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) instance and reclaims the memory.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) \*attribute | Pointer to the [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorSubscriptionAttribute\_SetSamplingInterval()

int32\_t OH\_SensorSubscriptionAttribute\_SetSamplingInterval(Sensor\_SubscriptionAttribute\* attribute, const int64\_t samplingInterval)

**Description**

Sets the sensor data reporting interval.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md)\* attribute | Pointer to the sensor subscription attribute. |
| const int64\_t samplingInterval | Data reporting interval to set, in nanoseconds. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorSubscriptionAttribute\_GetSamplingInterval()

int32\_t OH\_SensorSubscriptionAttribute\_GetSamplingInterval(Sensor\_SubscriptionAttribute\* attribute, int64\_t \*samplingInterval)

**Description**

Obtains the sensor data reporting interval.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_SubscriptionAttribute](../../structs/sensor-subscriptionattribute/document.md)\* attribute | Pointer to the sensor subscription attribute. |
| int64\_t \*samplingInterval | Pointer to the data reporting interval, in nanoseconds. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]Sensor\_EventCallback()

typedef void (\*Sensor\_EventCallback)(Sensor\_Event \*event)

**Description**

Defines the callback function used to report sensor data.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Event](../../structs/sensor-event/document.md)\* event | Pointer to the sensor data information. |

#### \[h2\]OH\_Sensor\_CreateSubscriber()

Sensor\_Subscriber \*OH\_Sensor\_CreateSubscriber(void)

**Description**

Creates a [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) instance.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [Sensor\_Subscriber \*](../../structs/sensor-subscriber/document.md) | Pointer to the [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) instance if the operation is successful; **NULL** otherwise. |

#### \[h2\]OH\_Sensor\_DestroySubscriber()

int32\_t OH\_Sensor\_DestroySubscriber(Sensor\_Subscriber \*subscriber)

**Description**

Destroys a [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) instance and reclaims the memory.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) \*subscriber | Pointer to the [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorSubscriber\_SetCallback()

int32\_t OH\_SensorSubscriber\_SetCallback(Sensor\_Subscriber\* subscriber, const Sensor\_EventCallback callback)

**Description**

Sets a callback function to report sensor data.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md)\* subscriber | Pointer to the sensor subscriber information. |
| [const Sensor\_EventCallback](#sensor_eventcallback) callback | Sets the callback function. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |

#### \[h2\]OH\_SensorSubscriber\_GetCallback()

int32\_t OH\_SensorSubscriber\_GetCallback(Sensor\_Subscriber\* subscriber, Sensor\_EventCallback \*callback)

**Description**

Obtains the callback function used to report sensor data.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [Sensor\_Subscriber](../../structs/sensor-subscriber/document.md)\* subscriber | Pointer to the sensor subscriber information. |
| [Sensor\_EventCallback](#sensor_eventcallback) \*callback | Pointer to the callback function. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | **SENSOR\_SUCCESS** if the operation is successful; an error code defined in [Sensor\_Result](#sensor_result) otherwise. |
