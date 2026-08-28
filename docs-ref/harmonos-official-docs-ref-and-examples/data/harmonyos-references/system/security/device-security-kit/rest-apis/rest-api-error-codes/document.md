# REST API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/78lOhe-zR76sQjR2EgFaNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062335Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1EA99344B66BF3E24F0098CD7429C69C920B3421065026375D21387878B8EF8A)

This section describes only cloud service-specific error codes and provides the cause analysis.

#### InvalidBundleName

**Message**

{
     "errorCodes": "InvalidBundleName" 
}

**Description**

The package name is missing or invalid.

**Possible causes**

1\. The request header does not contain **bundleName**.

2\. The value of **bundleName** in the request header is different from the package name of the app that calls the **getDeviceToken** API.

**Solution**

1\. Verify that the request header contains **bundleName**.

2\. Verify that the value of **bundleName** in the request header is the same as the package name of the app that calls the **getDeviceToken** API.

#### InvalidDeviceToken

**Message**

{
     "errorCodes": "InvalidDeviceToken" 
}

**Description**

The device token is missing or invalid.

**Possible causes**

The **deviceToken** parameter is missing from the request or contains special characters.

**Solution**

Verify that the **deviceToken** parameter exists in the request and does not contain special characters.

#### DeviceTokenExpired

**Message**

{
     "errorCodes": "DeviceTokenExpired" 
}

**Description**

The device token has expired.

**Possible causes**

The device token has expired.

**Solution**

A device token is valid for 1 hour. Generate a new token and try again.

#### InvalidTimeStamp

**Message**

{
     "errorCodes": "InvalidTimeStamp" 
}

**Description**

The timestamp is missing or invalid.

**Possible causes**

The **timeStamp** parameter is missing from the request, or is invalid (not of the Long type).

**Solution**

Verify that the **timeStamp** parameter exists in the request and is valid.

#### NotFound

**Message**

{
     "errorCodes": "NotFound" 
}

**Description**

No marking record about the device is found. (The device is authenticated successfully but not marked.)

**Possible causes**

The marking does not exist on the server.

**Solution**

1\. Update the device marking status, and then query the marking again.

2\. Change the value of **mode** to **1** or **2**, and try again.

#### InvalidMode

**Message**

{
     "errorCodes": "InvalidMode" 
}

**Description**

The mode is invalid.

**Possible causes**

The value of **mode** in the request is incorrect. For details about the enumerated values of **mode**, see the parameter description in the API reference.

**Solution**

Verify that the value of **mode** in the request is correct and complies with the API specifications.

#### InvalidBits

**Message**

{
     "errorCodes": "InvalidBits" 
}

**Description**

The bit value is missing or invalid.

**Possible causes**

The bit value is missing from the request or is not of the Boolean type.

**Solution**

Verify that the bit value exists in the request and is of the Boolean type (**true** or **false**).

#### InternalServerError

**Message**

{
     "errorCodes": "InternalServerError" 
}

**Description**

Internal server error.

**Possible causes**

An error occurred in internal server processing.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) for assistance.
