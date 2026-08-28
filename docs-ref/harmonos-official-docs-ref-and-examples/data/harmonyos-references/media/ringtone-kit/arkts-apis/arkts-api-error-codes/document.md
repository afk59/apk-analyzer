# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/sce0Tq6KRIy-3KUrDguNFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062444Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFE2943F4B275F9FE4C0A28C16161325B2BC4FFEA4C843205C52A681BD04E4BB)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 401 Invalid Parameter

**Message**

Invalid parameter.

**Description**

Invalid parameter.

**Possible causes**

Invalid parameter.

**Solution**

1\. Check whether the mandatory parameters and value ranges are correct by referring to the documentation.

2\. Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1011600001 Operation Canceled by User

**Message**

User canceled.

**Description**

After the user opens the dialog box, the user cancels the dialog box when the ringtone setting is not complete.

**Possible causes**

User operation error.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1011600002 The File Does Not Exist

**Message**

The media file is not found.

**Description**

No file exists in the input file path.

**Possible causes**

The [ringtone.startRingtoneSetting](../ringtone-ringtone-service/document.md#section5949453189) API is called before a file is created.

**Solution**

Ensure that the corresponding file is passed to the file path and try again, or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1011600003 Dialog Box Display Error

**Message**

Failed to show the dialog box.

**Description**

This error code is reported when a system error occurs.

**Possible causes**

An unknown error occurred.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1011600004 Failed to Call the System API

**Message**

Failed to call the system API.

**Description**

This error code is reported when a system error occurs.

**Possible causes**

An unknown error occurred.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).

#### 1011699999 System Internal Error

**Message**

System exception.

**Description**

This error code is reported when a system error occurs.

**Possible causes**

An unknown error occurred.

**Solution**

Try again or [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/).
