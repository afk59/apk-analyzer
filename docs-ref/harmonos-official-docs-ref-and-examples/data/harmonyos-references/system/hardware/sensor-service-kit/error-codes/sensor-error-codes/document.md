# Sensor Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/maR2ttUrRJGSpvRCbohcBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAAB8C81CCD19969C6F982C5C626E5BAD70B257268B44D55D0EC5639918289FE)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 14500101 Service Exception

**Error Message**

Service exception.Possible causes:1. Sensor hdf service exception;2. Sensor service ipc exception;3.Sensor data channel exception.

**Description**

This error code is reported if the HDI service is abnormal when the **on**, **once**, or **off** API of the sensor module is called.

**Possible Causes**

The HDI service is abnormal.

**Solution**

1.  Retry the operation at a specified interval (for example, 1s) or at an exponential increase interval.
2.  If the operation fails for three consecutive times, stop the retry. You can also attempt to obtain the sensor list to check for device availability.

#### 14500102 Sensor Not Supported by the Device

**Error Message**

The sensor is not supported by the device.

**Description**

This error code is reported if the **GetSingleSensor** API is called to obtain a sensor that is not supported by the device.

**Possible Causes**

The device does not support the sensor because the underlying components are not adaptable to the sensor.

**Solution**

1.  Adapt the underlying components to the sensor.
