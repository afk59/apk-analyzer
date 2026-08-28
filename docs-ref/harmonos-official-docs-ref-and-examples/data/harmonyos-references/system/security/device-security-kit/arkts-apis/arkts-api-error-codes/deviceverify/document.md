# DeviceVerify

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/g2Nnl4QUTmOqBSkegf4YGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062334Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DC5B407F10F56B770068008D1F3A49E5C9FB8CD8A70341F1FB87E59FF7047C6)

This section describes only module-specific client error codes and provides the cause analysis. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 201 Permission Verification Failed

**Description**

Permission verification failed.

**Possible causes**

Device Security Kit has not been enabled for the HAP.

**Solution**

1.  Enable **Device status detection** in AppGallery Connect. For details, please refer to [Enabling Device Security Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-deviceverify-activateservice).
2.  [Request a new debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugprofile-0000001914423102), and use it as the signature file of the project to try again.

#### 1003300005 Internal Error

**Description**

Internal error.

**Possible causes**

An exception occurred when other system APIs are called in the API execution process.

**Solution**

Try again first. If the retry fails, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.

#### 1003300006 An Exception Occurred When Accessing the Cloud Server

**Description**

An exception occurred when accessing the cloud server.

**Possible causes**

The device is not connected to the network or the network is unstable.

**Solution**

If the device is not connected to the network, connect to the network and try again. If it is already connected, the network may be unstable. Please try again.
