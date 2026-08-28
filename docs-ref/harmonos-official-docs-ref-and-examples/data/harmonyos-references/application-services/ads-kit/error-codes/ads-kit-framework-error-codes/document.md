# Ads Kit Framework Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/iVID7HfuSgWRNZuWVRZr7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5BE4577B85B4E46D4CF94BF6E34DDACA2FFF37EDAE66B1C7A11ADF287491EBAC)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

#### 21800001 System Error

**Message**

System internal error.

**Description**

An internal system error occurs. For example, the JavaScript object of the **Web** component fails to be registered or deleted.

**Possible causes**

Failed to connect to Ads Kit.

**Solution**

1\. Restart the device and try again.

2\. If the error persists, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354358694993&amp;keyWord=Ads Kit>). Huawei will get back to you as soon as possible.

#### 21800003 Ad Loading Failed

**Message**

Failed to load the ad request.

**Description**

Ad loading failed.

**Possible causes**

1\. The network is abnormal.

2\. The ad request parameters are incorrect.

3\. The server does not have any suitable ads to display.

**Solution**

1\. Check the network status.

2\. Check whether the ad request parameters meet the requirements based on the API reference.

3\. If the error persists, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354358694993&amp;keyWord=Ads Kit>). Huawei will get back to you as soon as possible.

#### 21800004 Ad Display Failed

**Message**

Failed to display the ad.

**Description**

Failed to display the ad.

**Possible causes**

The network is abnormal.

**Solution**

Check the network status.

#### 21800005 Failed to Parse Ad Data

**Message**

Failed to parse the ad response.

**Description**

Failed to parse ad data.

**Possible causes**

Ad response data lacks key attributes or contains structural errors.

**Solution**

Check the ad response data.
