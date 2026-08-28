# Vibrator Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/tzSXss8DTGC8UFPZN_nfWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062412Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7AEE398736749D949BF95F47353A2B8F6423AA126FC5E083C2BF796DE76748B6)

This topic describes only module-specific error codes. For details about universal error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

#### 14600101 Device operation failed.

**Error Message**

Device operation failed.

**Description**

This error code is reported if the HDI service is abnormal or the device is occupied when the **startVibration** interface of the vibrator module is called.

**Possible Causes**

1.The HDI service is abnormal.

2.The device is occupied.

3.The system's haptic management switches are disabled when vibration is triggered.

**Solution**

1.Retry the operation at specified intervals or with exponentially increasing intervals. If the operation fails three consecutive times, stop retrying. You can also retrieve the vibrator list to verify device availability.

2.Set a higher priority for the vibrator.

3.Check whether the system's haptic switch is disabled or the three-state switch is in mute mode, and ensure that the usage field of the switch is correctly configured.
