# ArkTS API Error Codes

For details about authorization-related error codes, please refer to [Account Kit ArkTS Error Codes](../../account-kit/arkts-error-codes/document.md).

| 
**Name**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

PACKAGE\_FINGERPRINT\_CHECK\_ERROR

 | 

[1001500001](../../account-kit/arkts-error-codes/document.md#section1581681312511)

 | 

The certificate fingerprint of the app fails to be verified.

 |
| 

DUPLICATE\_REQUEST\_REJECTED

 | 

[1001500002](../../account-kit/arkts-error-codes/document.md#section134761318124311)

 | 

Repeated request. No operation is needed to address this error code. Your app needs to implement tap control to prevent consecutive taps from initiating the same request.

 |
| 

ACCOUNT\_NOT\_LOGGED\_IN

 | 

[1001502001](../../account-kit/arkts-error-codes/document.md#section539558125020)

 | 

The HUAWEI ID is not signed in.

 |
| 

APP\_NOT\_AUTHORIZED

 | 

[1001502002](../../account-kit/arkts-error-codes/document.md#section1393125918588)

 | 

The app is not authorized.

 |
| 

PARAMETER\_INVALID

 | 

[1001502003](../../account-kit/arkts-error-codes/document.md#section289120911112)

 | 

Invalid parameters.

 |
| 

NETWORK\_ERROR

 | 

[1001502005](../../account-kit/arkts-error-codes/document.md#section1281526328)

 | 

Network error.

 |
| 

INTERNAL\_ERROR

 | 

[1001502009](../../account-kit/arkts-error-codes/document.md#section17561151616317)

 | 

Internal errors, such as Account Kit server errors.

 |
| 

USER\_CANCELED

 | 

[1001502012](../../account-kit/arkts-error-codes/document.md#section223413481361)

 | 

The user cancels authorization.

 |
| 

SCOPE\_OR\_PERMISSION\_NOT\_REQUESTED

 | 

[1001502014](../../account-kit/arkts-error-codes/document.md#section78953611814)

 | 

The app does not have the required scopes or permissions.

 |

#### 201 Authentication Failure

**Error message**

Permission verification failed.

**Description**

Authentication failed.

**Possible causes**

1\. The app fingerprint is incorrectly configured.

2\. Insufficient permission

3\. Some APIs can be called only by users in the trustlist.

4\. The number of test users has reached the upper limit.

**Solution**

1\. Ensure that the certificate fingerprint configured in AppGallery Connect for the app is correct by referring to [Adding the Public Key Fingerprint](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview#section1726913517284).

2\. Verify that required permissions have been granted by referring to [Managing User Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/health-add-permissions).

3\. The user's application for the beta version has been rejected. Complete the app acceptance process in the console by referring to [Applying for Formal Scopes](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/health-verification).

4\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 401 Invalid Parameters

**Error message**

Parameter error.Possible causes: 1. Mandatory parameters are left unspecified;2. Incorrect parameter types; 3.Parameter verification failed.

**Description**

Invalid parameters.

**Possible causes**

Invalid parameters.

**Solution**

1\. Check whether the mandatory parameters and value ranges are correct by referring to the documentation.

2\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 801 API Not Supported

**Error message**

Capability not supported. Failed to call the API due to limited device capabilities.

**Description**

The device does not support this API. Therefore, it cannot be called properly.

**Possible causes**

The device supports Syscap associated with the API but does not support the API itself.

**Solution**

Do not use this API on the device. Alternatively, implement conditional checks in the code to mitigate the effects of the application running across various devices, particularly under abnormal circumstances.

#### 1002700001 System Internal Error

**Error message**

System internal error.

**Description**

An internal system error occurs.

**Possible causes**

Unknown.

**Solution**

Resolve the issue for the specific scenario based on the actual error message. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1002700002 Database Error

**Error message**

Database processing error.

**Description**

Database error.

**Possible causes**

Unknown.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1002701001 Network Error

**Error message**

Network error. The network is unavailable.

**Description**

A network error occurs.

**Possible causes**

The network is not connected.

**Solution**

1\. Check the network configurations.

2\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1002702001 Not Signed In

**Error message**

Account error. The user has not logged in with HUAWEI ID.

**Description**

The account is not signed in.

**Possible causes**

The account is not signed in.

**Solution**

1\. Start the sign-in authorization process by referring to [Managing User Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/health-add-permissions), sign in to the account, and call the API again after the account is signed in.

2\. [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1002702002 Account Exception

**Error message**

Account error. Failed to obtain account information with HUAWEI ID.

**Description**

Account error.

**Possible causes**

Account error.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 1002703001 Privacy Agreement Not Agreed To

**Error message**

User privacy is not agreed.

**Description**

The user does not agree to the privacy agreement.

**Possible causes**

The user has never started the Huawei Health app.

**Solution**

Instruct the user to start the Huawei Health app by referring to [FAQs](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/health-faqs-5).

#### 1009104001 Linking Service Enabled

**Error message**

Sport service busy. Workout is already started by other application.

**Description**

The linking service is enabled.

**Possible causes**

The application or other applications have called **start** to enable the linking service.

**Solution**

1\. Check whether the linking service is repeatedly enabled in the service process.

2\. Capture exception handling scenarios where the linking service is enabled for other applications.

#### 1009104002 Workout Type Not Supported

**Error message**

Unsupported sport type.

**Description**

The workout type is not supported.

**Possible causes**

An unsupported workout type is passed.

**Solution**

Check the passed workout type. For details, please refer to [Exercise Record Type Constant](../arkts-apis/fitness-and-health-data-type-constants-and-model-definitions/exercisesequencehelper-exercise-record-type-constant/document.md).

#### 1009104003 Illegal Command

**Error message**

Illegal command.

**Description**

The command is illegal in the current state.

**Possible causes**

The API is called at a wrong time. The linking service has been enabled for other applications.

**Solution**

1\. Check the service process of the application.

2\. Capture exception handling scenarios where the linking service is enabled for other applications.

#### 1009104004 Permission Verification Error

**Error message**

Permission verification error. Application has no permission, such as Motion Permission.

**Description**

The application does not have the required permission, for example, the physical activity permission.

**Possible causes**

The application does not have the required permission.

**Solution**

Check whether the application has the required permission to call the API.

#### 1009104999 Universal Error Codes

**Error message**

System internal error.

**Description**

An unknown exception occurs.

**Possible causes**

Others.

**Solution**

Resolve the issue for the specific scenario based on the actual error message. If the error persists, [submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.

#### 14500101 Service Exception

**Error message**

Service exception.

**Description**

Service exception.

**Possible causes**

Unknown.

**Solution**

[Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/). Huawei will get back to you as soon as possible.
