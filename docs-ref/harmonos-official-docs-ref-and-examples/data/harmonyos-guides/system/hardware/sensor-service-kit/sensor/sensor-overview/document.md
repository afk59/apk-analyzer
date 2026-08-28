# Sensor Overview

#### Sensor Types

Sensors are an abstraction of underlying sensor hardware. Your application can access the underlying sensor hardware via the sensors. Using the [@ohos.sensor (Sensor)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-sensor) APIs, you can query sensors on your device, subscribe to sensor data, customize algorithms based on sensor data, and develop various sensor-based applications, such as compass, motion-controlled games, and fitness and health applications.

| Sensor Types | Name | Description | Usage |
| :-- | :-- | :-- | :-- |
| ACCELEROMETER | Acceleration sensor | Measures the acceleration (including the gravity acceleration) applied to a device on three physical axes (X, Y, and Z), in the unit of m/s2. | Detecting the motion status |
| ACCELEROMETER\_UNCALIBRATED | Uncalibrated acceleration sensor | Measures the uncalibrated acceleration (including the gravity acceleration) applied to a device on three physical axes (X, Y, and Z), in the unit of m/s2. | Measuring the acceleration bias estimation |
| LINEAR\_ACCELEROMETER | Linear acceleration sensor | Measures the linear acceleration (excluding the gravity acceleration) applied to a device on three physical axes (X, Y, and Z), in the unit of m/s2. | Detecting the linear acceleration in each axis |
| GRAVITY | Gravity sensor | Measures the gravity acceleration applied to a device on three physical axes (X, Y, and Z), in the unit of m/s2. | Measuring the gravity |
| GYROSCOPE | Gyroscope sensor | Measures the rotation angular velocity of a device on three physical axes (X, Y, and Z), in the unit of rad/s. | Measuring the rotation angular velocity |
| GYROSCOPE\_UNCALIBRATED | Uncalibrated gyroscope sensor | Measures the uncalibrated rotation angular velocity of a device on three physical axes (X, Y, and Z), in the unit of rad/s. | Measuring the bias estimation of the rotation angular velocity |
| SIGNIFICANT\_MOTION | Significant motion sensor | Checks whether a device has a significant motion on three physical axes (X, Y, and Z). The value **0** means that the device does not have a significant motion, and **1** means the opposite. | Detecting significant motions of a device |
| PEDOMETER\_DETECTION | Pedometer detection sensor | Detects whether a user takes a step. The value can be **0** (the user does not take a step) or **1** (the user takes a step). | Detecting whether a user takes a step |
| PEDOMETER | Pedometer sensor | Records the number of steps a user has walked. | Providing the number of steps a user has walked |
| AMBIENT\_TEMPERATURE | Ambient temperature sensor | Measures the ambient temperature, in the unit of degree Celsius (°C). | Measuring the ambient temperature |
| MAGNETIC\_FIELD | Magnetic field sensor | Measures the magnetic field on three physical axes (X, Y, and Z), in the unit of μT. | Creating a compass |
| MAGNETIC\_FIELD\_UNCALIBRATED | Uncalibrated magnetic field sensor | Measures the uncalibrated magnetic field on three physical axes (X, Y, and Z), in the unit of μT. | Measuring the magnetic field bias estimation |
| HUMIDITY | Humidity sensor | Measures the ambient relative humidity, in a percentage (%). | Monitoring the dew point, absolute humidity, and relative humidity |
| BAROMETER | Barometer sensor | Measures the barometric pressure, in the unit of hPa or mbar. | Measuring the barometric pressure |
| ORIENTATION | Orientation sensor | Measures the rotation angles of a device on three physical axes (Z, X, and Y), in the unit of rad. | Measuring the three orientation angles of the screen |
| ROTATION\_VECTOR | Rotation vector sensor | Measures the rotation vector of a device. It is a composite sensor that generates data from the acceleration sensor, magnetic field sensor, and gyroscope sensor. | Detecting the orientation of a device in the East, North, Up (ENU) Cartesian coordinate system |
| PROXIMITY | Proximity sensor | Measures the distance between a visible object and the device screen. | Measuring the distance between a person and the device during a call |
| AMBIENT\_LIGHT | Ambient light sensor | Measures the ambient light intensity of a device, in the unit of lux. | Automatically adjusting the screen brightness and checking whether the screen is covered on the top |
| HEART\_RATE | Heart rate sensor | Measures the heart rate of a user. | Providing users' heart rate data |
| WEAR\_DETECTION | Wear detection sensor | Checks whether a user is wearing a wearable device. | Detecting wearables |
| HALL | Hall effect sensor | Detects a magnetic field around a device. | Smart cover mode of the device |

The coordinate system of directional sensors is related to the device's component mounting orientation, and is basically based on the device's natural screen direction. (The natural screen direction may vary according to device models.)

Take a common bar phone for example: hold it vertically in front of you, with the screen directly facing you.

X-axis: the axis from left to right along the short edge of the screen.

Y-axis: the axis from bottom to top along the long edge of the screen.

Z-axis: axis perpendicular to the screen, pointing outward from the screen toward the user.

You can combine the device's natural screen direction and the current screen direction to determine how to interpret and use these raw data to meet your service demands. For example, a motion-sensing racing game requires the player to tilt the device to control the direction. Regardless of whether the player plays it in portrait or landscape mode, the X-axis and Y-axis data provided by the sensor is always relative to the natural screen direction. You need to determine whether to use the X-axis or Y-axis data to control the racing car's left and right steering based on the current screen direction and the application's UI display requirements, thereby ensuring a consistent user experience.

For the orientation sensor, you are advised to call the [Display](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#display) API of the DMS to obtain the screen orientation before starting development.

#### Working Principles

The following modules work cooperatively to implement sensors: Sensor API, Sensor Framework, Sensor Service, and HDF layer.

**Figure 1** How the sensor works

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/0Gg1WmPLReaWw5B6xSVf-A/en-us_image_0000002568684825.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F5895B8A2E849C1BC564CC6440D24D4FFE0480C6A93CFFBC2E013F306D7BAB7)

-   Sensor API: provides APIs for performing basic operations on sensors, including querying the sensor list, subscribing to or unsubscribing from sensor data, and executing control commands. This module makes application development simpler.
    
-   Sensor Framework: manages sensor data subscription, creates and destroys data channels, subscribes to or unsubscribes from sensor data, and implements communication with the Sensor Service module.
    
-   Sensor Service: interacts with the HD\_IDL module to receive, parse, and distribute data, manages foreground and background policies and sensors of a device, and controls sensor permissions.
    
-   HDF layer: selects proper policies based on the hardware first in first out (FIFO) and frequency, and adapts to different devices.
    

#### Constraints

1.  To obtain data of the following sensors, you must request the required permissions.
    
    | Sensor | Permission | Sensitivity | Permission Description |
    | :-- | :-- | :-- | :-- |
    | Acceleration sensor, uncalibrated acceleration sensor, and linear acceleration sensor | ohos.permission.ACCELEROMETER | system\_grant | The permission allows an application to read data from acceleration sensors, uncalibrated acceleration sensors, and linear acceleration sensors. |
    | Gyroscope sensor and uncalibrated gyroscope sensor | ohos.permission.GYROSCOPE | system\_grant | The permission allows an application to read data from gyroscope sensors and uncalibrated gyroscope sensors. |
    | Pedometer sensor | ohos.permission.ACTIVITY\_MOTION | user\_grant | The permission allows an application to read an end user's motion status, for example, to determine whether the user is in motion or to record the number of steps that the user has walked. |
    | Heart rate sensor | ohos.permission.READ\_HEALTH\_DATA | user\_grant | The permission allows an application to obtain an end user's health data, such as heart rate data. |
    
2.  The APIs for subscribing to and unsubscribing from sensor data work in pairs. If you do not need sensor data, call the unsubscription API to stop sensor data reporting.
