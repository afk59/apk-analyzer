# ArkTS Component Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/On4XznyYRzewsyRkKrhjJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062519Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8703A0E1EC23BF9CF4F9F02C329BB3968524895B4F580430CCDE2ACA2695944)

For details about the error codes, please refer to the following references:

[Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md)

[Map Kit Error Codes](../../../map-kit/arkts-apis/arkts-api-error-codes/document.md)

[Ability Kit Error Codes](../../../../application-framework/ability-kit/error-codes/document.md)

[Account Kit Error Codes](../../../account-kit/arkts-error-codes/document.md)

[Live View Kit Error Codes](../../../live-view-kit/arkts-apis/arkts-api-error-codes/document.md)

[Push Kit Error Codes](../../../push-kit/arkts-apis/arkts-api-error-codes/document.md)

[ArkTS API Error Codes](../../../../application-framework/arkts/error-codes/utils-error-codes/document.md)

[REST API Error Codes](../../../account-kit/rest-apis/rest-api-error-codes/document.md)

#### 10004 System Internal Error

**Message**

Internal error.

**Description**

System internal error.

**Possible causes**

System internal error.

**Solution**

Ensure that the network connection is normal. If the problem persists and the error is reported for the service updates authorization code button, also ensure that you have [initiated an application for the corresponding service scenario](https://developer.huawei.com/consumer/en/doc/atomic-guides/push-as-timeline#section18702113217305).

#### 10006 Failed to Obtain Share Data

**Message**

Failed to get data.

**Description**

Failed to obtain shared data.

**Possible causes**

System internal error.

**Solution**

Ensure that the network environment is normal. If the problem persists, perform further analysis based on logs.

#### 10008 Caller Not an Atomic Service

**Message**

Not atomic service.

**Description**

The caller is not an atomic service.

**Possible causes**

The caller of the API is not an atomic service.

**Solution**

This API can be called only by atomic services.
