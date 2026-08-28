# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/2jfOPZtNT2WKPNWJXfqjIg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062521Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C3E9D43EDE6EE7F0ABE344453E9E5F1D17C7E73C11176374761905BB3BB83C1)

This topic describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 1011900001 Weather Service Not Enabled

**Message**

Capability is not configured.

**Description**

The weather service has not been enabled.

**Possible causes**

1\. The weather service has not been enabled.

2\. The app signature is incorrectly configured.

**Solution**

1\. Ensure that the user has enabled the weather service.

2\. Ensure that the app signature is correctly configured by referring to [Releasing a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-0000002271695230).

3\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1011900002 Weather Data Missing

**Message**

The requested longitude and latitude grid point lacks data.

**Description**

No weather data is available.

**Possible causes**

The longitude and latitude information provided does not correspond to a place in the land area.

**Solution**

1\. Check whether the longitude and latitude data corresponds to a place in the land area by using a search engine.

2\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1011900003 Network Error

**Message**

Network error.

**Description**

A network error occurs.

**Possible causes**

The network is not connected.

**Solution**

1\. Check the network configurations.

2\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1011900004 Internal System Error

**Message**

System error.

**Description**

An internal system error occurs.

**Possible causes**

Unknown.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.
