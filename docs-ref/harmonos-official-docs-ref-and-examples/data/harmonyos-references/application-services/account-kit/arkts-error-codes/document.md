# ArkTS Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/eXq4og6YSNCjr_TemCZp1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062501Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=060B5A632FAD2421F99C91874EB045201239B89DF5DF42209D0FF190A2329318)

This section describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../api-reference-overview/universal-error-codes/document.md).

#### 1001500001 App Certificate Fingerprint Verification Failure

**Message**

Failed to check the fingerprint of the app bundle.

**Description**

The certificate fingerprint of the app fails to be verified.

**Possible causes**

For details, please refer to [1001500001 Fingerprint Certificate Verification Failure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-1).

**Solution**

For details, please refer to [1001500001 Fingerprint Certificate Verification Failure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-1).

#### 1001500002 Repeated Request

**Message**

This error code is reported when a request is already being processed.

**Description**

Repeated request.

**Possible causes**

The user requests a page of Account Kit repeatedly.

**Solution**

No special processing is required.

#### 1001500003 Unsupported Scopes or Permissions

**Message**

The scopes or permissions are not supported.

**Description**

The scopes or permissions are not supported.

**Possible causes**

1\. The signed-in HUAWEI ID does not support the data requested by the authorized app.

2\. In scenarios such as real-name information retrieval/verification and face-based identity verification, a user signs in with a HUAWEI ID registered in the Chinese mainland but uses a Hong Kong, Macao, and Taiwan Travel Permit for real-name authentication.

3\. In scenarios such as real-name information verification and face-based identity verification, PCs/2-in-1 devices or devices without a functioning front camera do not support authorization based on the passed **verifyRealName** and **verifyFace** scopes.

4\. During the atomic service development, **profile** is passed to **scope** when [AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165) is called. However, **supportAtomicService** is not set to **true**.

5\. During atomic service development, the phone scope is passed for calling the [AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165) API.

6\. In scenarios including real-name information verification and face-based identity verification, the HUAWEI ID used for sign-in is a child account.

7\. The app on a wearable or TV requests scopes that are not supported.

**Solution**

1\. Guide users to switch to a HUAWEI ID registered in the Chinese mainland or register a new one for re-authentication. In one-tap sign-in scenarios, display alternative sign-in methods in your app.

2\. In scenarios such as real-name information retrieval/verification and face-based identity verification, guide the user to switch to a HUAWEI ID that has completed real-name authentication with a Chinese mainland ID card.

3\. In scenarios such as verifying real-name information and verifying the identity by face, use another device whose front camera is working properly to authorize the **verifyRealName** and **verifyFace** scopes.

4\. During the atomic service development, pass **profile** to **scope** when [AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165) is called. Additionally, set **supportAtomicService** to **true**.

5\. Atomic services cannot call this API to obtain mobile numbers, but the [quick mobile number verification button](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/scenario-fusion-button-getphonenumber) of Scenario Fusion Kit can be used for the atomic services to obtain mobile numbers.

6\. Guide users to switch to an adult HUAWEI ID registered in the Chinese mainland or register a new one, then re-trigger the API.

7\. Request the required information using another device that supports this API, or try an alternative method.

#### 1001500004 Function Not Supported by the Signed-In HUAWEI ID

**Message**

The account does not support this function.

**Description**

This function is unavailable for the HUAWEI ID already signed in.

**Possible causes**

1\. The signed-in HUAWEI ID is not registered in the Chinese mainland. As a result, the API for obtaining the mobile number consistency status cannot be called.

2\. The one-tap HUAWEI ID sign-in API using a child account is not supported on TVs.

**Solution**

1\. Guide users to switch to a HUAWEI ID registered in the Chinese mainland or register a new one, then re-trigger the API.

2\. Call the one-tap HUAWEI ID sign-in API for adult HUAWEI ID sign-in on TVs.

#### 1001500005 Function Restricted

**Message**

This function is restricted from being called.

**Description**

This function is restricted.

**Possible causes**

The [getMobileNumberConsistency](../arkts-api/authentication-unified-authentication-service/document.md#section571965992211) API for obtaining the mobile number consistency status has been called for more than 50 times within 24 hours.

**Solution**

1\. The app controls the number of times that the API for obtaining the mobile number consistency status is called to no more than 50 within 24 hours.

2\. If this error code is displayed during debugging, restart your device to rectify the error.

#### 1001502001 User Has Not Signed In to HUAWEI ID

**Message**

The user has not logged in with HUAWEI ID.

**Description**

The user has not signed in with their HUAWEI ID.

**Possible causes**

1\. The user has not signed in with their HUAWEI ID.

2\. A wearable in an unsigned-in state attempts to sign in to the HUAWEI ID by calling [LoginWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section42261825935), [AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165), or another related API.

**Solution**

1\. Call [LoginWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section42261825935) and set **forceLogin** to **true** to open the sign-in screen or guide the user to sign in with a HUAWEI ID in system settings.

2\. Ensure that for wearables, the user signs in with their HUAWEI ID in system settings or the HUAWEI Health app.

#### 1001502002 App Not Authorized

**Message**

The application is not authorized.

**Description**

The app is not authorized.

**Possible causes**

1\. When the [AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165) API is called and **forceAuthorization** is set to **false**, the user has not granted authorization to the app.

2\. The **idValue** passed in [ConsistencyRequest](../arkts-api/authentication-unified-authentication-service/document.md#section168131411512) when the [getMobileNumberConsistency](../arkts-api/authentication-unified-authentication-service/document.md#section571965992211) API is called is incorrect, or the user has revoked the authorization on the app.

3\. The passed **idValue** in [StateRequest](../arkts-api/authentication-unified-authentication-service/document.md#section9615740103819) when the [getHuaweiIDState](../arkts-api/authentication-unified-authentication-service/document.md#section102884586336) API is called is incorrect, or the user has revoked the authorization on the app.

**Solution**

1\. To guide the user to authorize the app, call [AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165) and set **forceAuthorization** to **true** to open the authorization screen for the user.

2\. Pass in correct **idValue** by referring to [ConsistencyRequest](../arkts-api/authentication-unified-authentication-service/document.md#section168131411512) or request the user to grant authorization again.

3\. Pass in correct **idValue** by referring to [StateRequest](../arkts-api/authentication-unified-authentication-service/document.md#section9615740103819) or request the user to grant authorization again.

#### 1001502003 Invalid Input Parameter Value

**Message**

Invalid input parameter value.

**Description**

The input parameter value is invalid.

**Possible causes**

1\. The input parameters are invalid. For example, neither **scope** nor **permission** is passed when the [AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165) API is called.

2\. The **client\_id** parameter is not set or incorrectly set.

3\. In the one-tap sign-in scenario, the passed anonymous mobile number may be incorrect or the authorization API ([AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165)) is not called to obtain the anonymous mobile number.

4\. Manual signing is not used.

5\. The current profile does not contain the app ID. You need to request a new profile.

**Solution**

1\. Ensure that input parameters are correctly passed.

2\. Ensure that the client ID in the **module.json5** file of the module whose **module type** is **entry** is correctly set by referring to [Configuring the Client ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

3\. If the fault is caused by cause 3, pass the anonymous mobile number obtained through the authorization API [AuthorizationWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section12940173017165).

4\. Configure signing information. For details, please refer to [Configuring Signing Information and Fingerprint](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-sign-fingerprints).

5\. Request a new profile in AppGallery Connect and sign your app again. During the debugging phase, [request a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278) and manually re-sign your app. During the release phase, [request a release profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090) and manually re-sign the app.

#### 1001502005 Network Error

**Message**

Network error.

**Description**

A network error occurs.

**Possible causes**

The device is not connected to the network.

**Solution**

Check the network connection.

#### 1001502009 Internal Error

**Message**

Internal error.

**Description**

Internal error.

**Possible causes**

Internal errors, such as Account Kit server errors.

**Solution**

1\. Restart your device.

2\. If the error persists, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>). Huawei will get back to you as soon as possible.

#### 1001502012 Authorization Revoked

**Message**

The user canceled the authorization.

**Description**

The user revokes authorization.

**Possible causes**

The user revokes authorization.

**Solution**

No special handling is required because the user revokes authorization.

#### 1001502014 App Does Not Have Required Scopes or Permissions

**Message**

The app does not have the required scopes or permissions.

**Description**

The app does not have the required scopes or permissions.

**Possible causes**

For details, please refer to [1001502014 Necessary Scopes Not Requested](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-2).

**Solution**

For details, please refer to [1001502014 Necessary Scopes Not Requested](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-faq-2).

#### 1001600001 Network Unavailable

**Message**

The network is unavailable.

**Description**

The network is unavailable.

**Possible causes**

The network is not properly connected.

**Solution**

Ensure that the network is properly connected.

#### 1001600002 Account Not Signed In

**Message**

The user has not logged in with HUAWEI ID.

**Description**

The user has not signed in with their HUAWEI ID.

**Possible causes**

The user has not signed in with their HUAWEI ID.

**Solution**

Call [LoginWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section42261825935) and set **forceLogin** to **true** to open the sign-in screen or guide the user to sign in with a HUAWEI ID in system settings.

#### 1001600003 App Certificate Fingerprint Verification Failure

**Message**

Failed to check the fingerprint of the application bundle.

**Description**

The certificate fingerprint of the app fails to be verified.

**Possible causes**

1\. **client\_id** has an incorrect value. (For example, it is set to the client ID of the project).

2\. The certificate fingerprint of the app is not configured or is incorrect.

**Solution**

1\. Ensure that the client ID in the **module.json5** file of the module whose **module type** is **entry** is correctly set by referring to [Configuring the Client ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

2\. Ensure that the [certificate fingerprint configured](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview#section1726913517284) in AppGallery Connect for the app is correct.

#### 1001600004 App Does Not Have Required Permissions

**Message**

The application does not have the required permissions.

**Description**

The app does not have the required permissions.

**Possible causes**

The permissions of the corresponding API are not applied for.

**Solution**

Request required permissions.

#### 1001600005 Operation Canceled by User

**Message**

The user canceled the current operation.

**Description**

The user canceled the current operation.

**Possible causes**

The user canceled the current operation.

**Solution**

No special processing is required.

#### 1001600006 Verification Factor Unavailable

**Message**

The requested verification factors are unavailable on the device.

**Description**

The verification factor is not supported on the device.

**Possible causes**

Verification elements, such as the mobile number, security mobile number, email address, and security email address, are not configured for secondary verification.

**Solution**

Instruct the user to go to **Personal info** or **Account security** under **Settings** > **HUAWEI ID** to configure verification elements.

#### 1001600007 Internal Error

**Message**

Internal error.

**Description**

Internal error.

**Possible causes**

Internal errors, such as Account Kit server errors.

**Solution**

1\. Restart your device.

2\. If the error persists, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>). Huawei will get back to you as soon as possible.

#### 1008100001 Internal Error

**Message**

Internal error.

**Description**

Internal error.

**Possible causes**

Internal errors, such as Account Kit server errors.

**Solution**

1\. Restart your device.

2\. If the error persists, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>). Huawei will get back to you as soon as possible.

#### 1008100002 Network Unavailable

**Message**

The network is unavailable.

**Description**

The network is unavailable.

**Possible causes**

The network is not properly connected.

**Solution**

Ensure that the network is properly connected.

#### 1008100003 Account Not Signed In

**Message**

The user has not signed in with HUAWEI ID.

**Description**

The user has not signed in with their HUAWEI ID.

**Possible causes**

The user has not signed in with their HUAWEI ID.

**Solution**

Call [LoginWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section42261825935) and set **forceLogin** to **true** to open the sign-in screen or guide the user to sign in with a HUAWEI ID in system settings.

#### 1008100004 App Certificate Fingerprint Verification Failure

**Message**

Failed to check the fingerprint of the app bundle.

**Description**

The certificate fingerprint of the app fails to be verified.

**Possible causes**

1\. **client\_id** has an incorrect value. (For example, it is set to the client ID of the project).

2\. The certificate fingerprint of the app is not configured or is incorrect.

**Solution**

1\. Ensure that the client ID in the **module.json5** file of the module whose **module type** is **entry** is correctly set by referring to [Configuring the Client ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

2\. Ensure that the [certificate fingerprint configured](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview#section1726913517284) in AppGallery Connect for the app is correct.

#### 1008100005 App Does Not Have Required Permissions

**Message**

The app does not have the required permissions.

**Description**

The app does not have the required permissions.

**Possible causes**

The permissions of the corresponding API are not applied for.

**Solution**

Ensure that you have requested the permissions of the corresponding API. For details, please refer to [Prerequisites](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-choose-address-dev#section1061219267293).

#### 1008100006 User Exits Shipping Address Management Service Without Completing Current Operation

**Message**

The user quits the shipping address management service without finishing.

**Description**

A user exits the shipping address management service without completing the current operation.

**Possible causes**

The user closes the shipping address management screen without completing the shipping address selection.

**Solution**

No special processing is required.

#### 1008100007 Shipping Address Management Service Unavailable for Current HUAWEI ID

**Message**

The shipping address management service does not support the HUAWEI ID that is already signed in.

**Description**

The shipping address management service is unavailable for the HUAWEI ID signed in.

**Possible causes**

The shipping address management service is unavailable for the HUAWEI ID signed in, for example, a HUAWEI ID registered outside the Chinese mainland.

**Solution**

Guide users to switch to a HUAWEI ID registered in the Chinese mainland or register a new one, or use other methods to obtain the shipping address.

#### 1010060001 User Canceled Invoice Service

**Message**

The operation was canceled by the user.

**Description**

The user cancels the invoice service.

**Possible causes**

The user cancels the operation before it is complete.

**Solution**

No special processing is required.

#### 1010060002 System Internal Error

**Message**

System internal error.

**Description**

Internal system error.

**Possible causes**

Internal errors, such as Account Kit server errors.

**Solution**

1\. Restart your device.

2\. If the error persists, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>). Huawei will get back to you as soon as possible.

#### 1010060003 App Certificate Fingerprint Verification Failure

**Message**

Failed to check the fingerprint of the app bundle.

**Description**

The certificate fingerprint of the app fails to be verified.

**Possible causes**

1\. **client\_id** has an incorrect value. (For example, it is set to the client ID of the project).

2\. The certificate fingerprint of the app is not configured or is incorrect.

**Solution**

1\. Ensure that the client ID in the **module.json5** file of the module whose **module type** is **entry** is correctly set by referring to [Configuring the Client ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

2\. Ensure that the [certificate fingerprint configured](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview#section1726913517284) in AppGallery Connect for the app is correct.

#### 1010060004 Calls Too Frequent

**Message**

Too frequent API calls.

**Description**

API calls are too frequent.

**Possible causes**

The API call interval is too short.

**Solution**

Control the API call frequency.

#### 1010060005 Network Connection Error

**Message**

Network connection error.

**Description**

Network connection error.

**Possible causes**

The network is not properly connected.

**Solution**

Ensure that the network is properly connected.

#### 1010060006 Account Not Signed In

**Message**

The HUAWEI ID is not signed in.

**Description**

The user has not signed in with their HUAWEI ID.

**Possible causes**

The user has not signed in with their HUAWEI ID.

**Solution**

Call [LoginWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section42261825935) and set **forceLogin** to **true** to open the sign-in screen or guide the user to sign in with a HUAWEI ID in system settings.

#### 1010060007 Invoice Title Already Exists

**Message**

Failed to create an invoice title because the title already exists.

**Description**

This error code is reported when the invoice title to be created already exists.

**Possible causes**

The invoice title already exists.

**Solution**

No special processing is required.

#### 1010060008 Invoice Service Unavailable for Current HUAWEI ID

**Message**

The invoice service does not support the logged HUAWEI ID.

**Description**

The invoice service is unavailable for the HUAWEI ID signed in.

**Possible causes**

The HUAWEI ID may be registered outside the Chinese mainland.

**Solution**

Guide users to switch to a HUAWEI ID registered in the Chinese mainland or register a new one, or use other methods to obtain the invoice title.

#### 1005300001 The User Does Not Accept Agreements

**Message**

The user did not accept the agreement.

**Description**

The user does not accept the agreements.

**Possible causes**

When the HUAWEI ID sign-in component is used, the agreement status is not set to ACCEPTED.

**Solution**

The user needs to manually accept the agreements.

#### 1005300002 One-Tap HUAWEI ID Sign-in Button Not Tapped by User

**Message**

The user did not click the HUAWEI ID login button.

**Description**

The user does not tap the one-tap HUAWEI ID sign-in button.

**Possible causes**

The developer bypasses the one-tap HUAWEI ID sign-in button and directly calls the **continueLogin** API.

**Solution**

The **continueLogin** API is called only when the user taps the one-tap HUAWEI ID sign-in button and taps the button for accepting agreements and signing in from the displayed dialog box.

#### 1009900002 Youth Mode Not Enabled

**Message**

The minors mode is not enabled.

**Description**

The youth mode is not enabled.

**Possible causes**

The password verification request is called when the youth mode is not enabled.

**Solution**

[Enable the youth mode](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-app-turn-on-minorsprotection).

#### 1009900003 Operation Canceled by User

**Message**

The user canceled the operation.

**Description**

The user canceled the operation.

**Possible causes**

A user taps a screen close button.

**Solution**

Process the logic for the user to cancel the current operation.

#### 1009900005 Youth Mode Already Enabled

**Message**

The minors mode is already on.

**Description**

The youth mode is already enabled.

**Possible causes**

The youth mode enabling API is repeatedly called when the youth mode has been enabled.

**Solution**

Call [getMinorsProtectionInfoSync](../arkts-api/minorsprotection-youth-mode/document.md#section11505356101217)() or [getMinorsProtectionInfo](../arkts-api/minorsprotection-youth-mode/document.md#section82313184131)() to check the status of the youth mode. If the youth mode is disabled, call the API to enable it.

#### 1009900006 Youth Mode Already Disabled

**Message**

The minors mode is already off.

**Description**

The youth mode is already disabled.

**Possible causes**

The youth mode disabling API is repeatedly called when the youth mode has been disabled.

**Solution**

Call [getMinorsProtectionInfoSync](../arkts-api/minorsprotection-youth-mode/document.md#section11505356101217)() or [getMinorsProtectionInfo](../arkts-api/minorsprotection-youth-mode/document.md#section82313184131)() to check the status of the youth mode. If the youth mode is enabled, call the API to disable it.

#### 1009900007 Unsupported Account

**Message**

Unsupported HUAWEI ID.

**Description**

The account is not supported.

**Possible causes**

The HUAWEI ID may be registered outside the Chinese mainland.

**Solution**

Guide users to sign in with a HUAWEI ID registered in the Chinese mainland.

#### 1009900011 Service Unavailable

**Message**

Service not available.

**Description**

Service unavailable.

**Possible causes**

The device enters the private space mode.

**Solution**

Prompt the user to disable the private space mode by going to **Settings** > **Privacy** > **PrivateSpace**, or build your own youth mode as needed.

#### 1002500001 Network Unavailable

**Message**

The network is unavailable.

**Description**

The network is unavailable.

**Possible causes**

The network is not properly connected.

**Solution**

Ensure that the network is properly connected.

#### 1002500002 Account Not Signed In

**Message**

The user has not logged in with HUAWEI ID.

**Description**

The user has not signed in with their HUAWEI ID.

**Possible causes**

The user has not signed in with their HUAWEI ID.

**Solution**

Call [LoginWithHuaweiIDRequest](../arkts-api/authentication-unified-authentication-service/document.md#section42261825935) and set **forceLogin** to **true** to open the sign-in screen or guide the user to sign in with a HUAWEI ID in system settings.

#### 1002500003 App Certificate Fingerprint Verification Failure

**Message**

Failed to check the fingerprint of the application bundle.

**Description**

The certificate fingerprint of the app fails to be verified.

**Possible causes**

1\. **client\_id** has an incorrect value. (For example, it is set to the client ID of the project).

2\. The certificate fingerprint of the app is not configured or is incorrect.

**Solution**

1\. Ensure that the client ID in the **module.json5** file of the module whose **module type** is **entry** is correctly set by referring to [Configuring the Client ID](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/account-client-id).

2\. Ensure that the [certificate fingerprint configured](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-dev-overview#section1726913517284) in AppGallery Connect for the app is correct.

#### 1002500004 App Does Not Have Required Permissions

**Message**

The application does not have the required permissions.

**Description**

The app does not have the required permissions.

**Possible causes**

The permissions of the corresponding API are not applied for.

**Solution**

Check whether the permissions of the corresponding API have been applied for. For details about how to apply for the permissions, please refer to the development prerequisites in the corresponding scenario.

#### 1002500005 Verification Canceled by User

**Message**

The user canceled the verification of the HUAWEI ID.

**Description**

The user canceled the verification operation.

**Possible causes**

The user canceled the verification operation.

**Solution**

No special processing is required.

#### 1002500006 Internal Error

**Message**

Internal error.

**Description**

Internal error.

**Possible causes**

An error occurs on the Account Kit server, an API that is not supported by the current device is called, or other internal errors occur.

**Solution**

1\. Restart your device.

2\. Ensure that the current device supports the API. You are advised to use [canIUse](../../../api-reference-overview/systemcapability/document.md#checking-whether-an-api-is-available) to check whether the current device supports an API before calling it.

3\. If the error persists, [submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>). Huawei will get back to you as soon as possible.

#### 1002500008 Real-Name Information Verification Not Supported for HUAWEI ID

**Message**

Real-name verification is not supported for the HUAWEI ID.

**Description**

The HUAWEI ID does not support real-name information verification.

**Possible causes**

The HUAWEI ID used is not registered in the Chinese mainland.

**Solution**

Guide users to sign in with a HUAWEI ID registered in the Chinese mainland and try again.

#### 1002500009 Real-Name Channel Verification Failed

**Message**

Real-name channel verification failed.

**Description**

Failed to verify the real-name channel.

**Possible causes**

1\. The real-name channel ID passed is incorrect.

2\. An error occurred during real-name channel verification.

**Solution**

1\. Ensure that the real-name channel ID is correct.

2\. [Submit a ticket online](<https://developer.huawei.com/consumer/en/support/feedback/#/add/101704353566310877?level2=101704353626565886&amp;level3=101704354306240980&amp;keyWord=Account Kit>). Huawei will get back to you as soon as possible.

#### 1002500011 Unmatched Face in Proof of Identify

**Message**

Your face does not match your facial image as proof of identity.

**Description**

The user's face does not match the facial image used as proof of identity.

**Possible causes**

The user's face does not match the facial image used as proof of identity.

**Solution**

Instruct the user to verify the face again.

#### 1002500012 No Real-Name Information Found

**Message**

No real-name information is found for the HUAWEI ID.

**Description**

No real-name information is found.

**Possible causes**

The account is not verified by real-name information.

**Solution**

Instruct the user to go to the **Real-name authentication** menu under **Settings** > **HUAWEI ID** > **Personal info** to complete identity verification.

#### 1002500013 Unmatched Name and ID Card Number

**Message**

Your name and ID number do not match.

**Description**

The name does not match the ID card number.

**Possible causes**

1\. The user input is incorrect.

2\. The user may have changed the household register recently, or reported the loss of the ID card and issued a new card. However, the new identity information has not been synchronized with that of the Ministry of Public Security.

**Solution**

1\. Enter the name and ID card number again and try again.

2\. If the fault is caused by cause 2, try again later.

#### 1002500014 Too Many Attempts for Real-Name Information Verification

**Message**

Too many real-name verification attempts.

**Description**

Too many real-name information verification attempts.

**Possible causes**

Too many real-name information verification attempts.

**Solution**

Try again 24 hours later.

#### 1002500015 Invalid Parameter verificationToken

**Message**

The verificationToken parameter is incorrectly set.

**Description**

The **verificationToken** parameter is invalid.

**Possible causes**

The **verificationToken** parameter is invalid.

**Solution**

Obtain the correct value of **verificationToken** and try again.

#### 1002500016 API Not Supported on Device

**Message**

This device does not support this API.

**Description**

The device does not support this API.

**Possible causes**

The device's front camera is unavailable in the scenario of verifying the identity by face.

**Solution**

Rectify the front camera fault or replace the device with one that has a functioning front camera, and try again.
