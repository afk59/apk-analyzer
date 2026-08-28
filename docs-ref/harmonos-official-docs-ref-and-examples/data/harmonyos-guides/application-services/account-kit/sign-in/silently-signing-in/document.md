# Silently Signing In

#### Use Case

In scenarios such as app reinstallation or device change, if the signed-in HUAWEI ID is the same as before, the app can use the silent sign-in method provided by Account Kit to obtain the user's UnionID and OpenID without requiring the user to tap the sign-in button.

#### Restrictions

The silent sign-in capability is supported on phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.0(18), it is also supported on wearables. Starting from version 5.1.1(19), it is also supported on TVs.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/f-i60GJUTNiTMplg3NrUXA/en-us_image_0000002528823277.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E33E8B2F7BB36488A2245BF9CB6BD7CF053D61311E53C4B1B8A619EAD8820493 "Click to enlarge")

The process is as follows:

1.  Call the sign-in API (steps 1 to 3):
    1.  In the case that the user previously signed in using a HUAWEI ID, and later either reinstalls the app after uninstalling it or launches the app on another device, the app calls the sign-in API with **forceLogin** set to **false**.
    2.  If the HUAWEI ID has signed in and the API is successfully called, the app will obtain the sign-in result including the authorization code. Note that if the HUAWEI ID has not signed in, error [1001502001](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-error-code#section539558125020) will be returned. Handle it as needed.
2.  Associate the user with an app account (steps 4 to 13):
    1.  The app server uses the authorization code to obtain an access token, and then calls the API for [parsing credentials](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-token-info#section2520125725115) with the access token to obtain user information. Using an authorization code to retrieve user information can effectively prevent security risks caused by data traversal, identity spoofing, replay attacks, and other forms of cyberattacks.
    2.  The app server sends the sign-in credential (**SessionId**) and UnionID/OpenID to the app. The app then checks whether the user has signed in with a HUAWEI ID based on the UnionID/OpenID.
    3.  The app verifies the UnionID/OpenID and the sign-in credential (**SessionId**) to ensure security, and completes silent sign-in.

#### API Description

The table below lists the key APIs for silent sign-in. For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createLoginWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section7843123616411)(): [LoginWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section42261825935)

 | 

Creates a HUAWEI ID sign-in request. The **forceLogin** parameter in [LoginWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section42261825935) specifies whether to forcibly show the HUAWEI ID sign-in screen when a user does not have their HUAWEI ID signed in on the device. In the silent sign-in scenario, set this parameter to **false**.

 |
| 

[constructor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section9716526428)(context?: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-common#context))

 | 

Creates a sign-in request controller.

 |
| 

[executeRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section3975181884311)(request: [AuthenticationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section3118182610348)): Promise<[AuthenticationResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section2697164193515)\>

 | 

Executes the sign-in request using a promise.

 |

#### Prerequisites

Before coding, make sure that you have [configured the signing information and fingerprint](../../getting-started/configuring-signing-information-and-fingerprint/document.md) and also [set the client ID](../../getting-started/configuring-the-client-id/document.md). No additional scope or permission needs to be requested for the scenario described in this topic.

#### App-Side Development

1.  Import the [authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication) module and related common modules.
    
    import { authentication } from '@kit.AccountKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { util } from '@kit.ArkTS';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create a sign-in request and set parameters.
    
    // Create a sign-in request and set parameters.
    const loginRequest = new authentication.HuaweiIDProvider().createLoginWithHuaweiIDRequest();
    // false indicates silent sign-in.
    loginRequest.forceLogin = false;
    // Used to prevent cross-site request forgery.
    loginRequest.state = util.generateRandomUUID();
    
3.  Call the [executeRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section3975181884311) method of the [AuthenticationController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section620452019185) object to execute the sign-in request, and process the sign-in result to obtain the authorization code and ID token. Then, send the authorization code to the app server. For details, please refer to steps **a** and **b** in [Development for App-App Server Interaction](../signing-in-with-huawei-id-through-just-one-tap-obtaining-the-mobile-number-union/document.md#section4355919132013). The app can obtain the public key provided by the Account Kit server from the public website and verify the signature and necessary information in the ID token to prove that they are not tampered with. For details about how to parse the ID token, please refer to [Parsing and Verification](../../faqs/when-and-how-can-i-use-the-id-token/document.md#section6924154019588).
    
    // Execute the sign-in request.
    try {
      const controller = new authentication.AuthenticationController();
      controller.executeRequest(loginRequest).then((response: authentication.LoginWithHuaweiIDResponse) => {
        const loginWithHuaweiIDResponse = response as authentication.LoginWithHuaweiIDResponse;
        const state = loginWithHuaweiIDResponse.state;
        if (state && loginRequest.state !== state) {
          hilog.error(0x0000, 'testTag', \`Failed to login. The state is different, response state: ${state}\`);
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in logging in.');
        const loginWithHuaweiIDCredential = loginWithHuaweiIDResponse?.data;
        const code = loginWithHuaweiIDCredential?.authorizationCode;
        // Process the authorization code.
      }).catch((error: BusinessError) => {
        dealAllError(error);
      })
    } catch (error) {
      dealAllError(error);
    }
    
    // Handle the error.
    function dealAllError(error: BusinessError): void {
      hilog.error(0x0000, 'testTag', \`Failed to login. Code: ${error.code}, message: ${error.message}\`);
      // In sign-in scenarios involving UI interactions, it is advised to guide the user with the following error code prompts:
      if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
        // HUAWEI ID not signed in. Use a HUAWEI ID to sign in and try again, or sign in to the app in another way.
      } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
        // A network exception occurs. Check the current network status and try again, or sign in to the app in another way.
      } else if (error.code === ErrorCode.ERROR\_CODE\_INTERNAL\_ERROR) {
        // Failed to sign in. Try another way.
      } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
        // Authorization canceled by the user.
      } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
        // System service exception. Try again later or sign in to the app in another way.
      } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
        // Repeated request. No further action is needed.
      } else {
        // Failed to sign in. Try another way.
      }
    }
    
    export enum ErrorCode {
      // HUAWEI ID not signed in.
      ERROR\_CODE\_LOGIN\_OUT = 1001502001,
      // Network error.
      ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
      // Internal error.
      ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
      // Authorization canceled by the user.
      ERROR\_CODE\_USER\_CANCEL = 1001502012,
      // System service exception.
      ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
      // Repeated request.
      ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
    }
    

#### Server-Side Development

1.  The app server calls the [API for obtaining user-level credentials](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-user-token#section1085901313579) with the client ID, client secret, and authorization code to request an access token and a refresh token from the Account Kit server.
2.  Use the access token to call the API for [Prototype](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-token-info#section2520125725115) to obtain the UnionID of a user.
    
    **Processing after an access token has expired:**
    
    An access token is valid for only 60 minutes. When an access token has expired or is about to expire (as indicated by the returned [REST API error code](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-token-info#section1737691991515)), request a new access token from the Account Kit server using a refresh token (valid for 180 days) through the API for [refreshing a user-level credential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-refresh-token#section1085901313579).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/jLoBUvLJSyO01miOzYRCtA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9040633DE7EB3C7616BEE8302D38095CE8BC0A674320E2C595BCBF1FCD3B803A)
    
    1.  When the access token has expired, if your app does not use the refresh token to request a new access token from the Account Kit server, the authorization of the signed-in HUAWEI ID will become invalid. As a result, functions that rely on the expired access token will be unavailable.
    2.  If the access token becomes invalid abnormally (for example, the password is changed, the HUAWEI ID is signed out, or a device is removed from the list of devices already signed in with the HUAWEI ID), the app can call the authorization API again to request user authorization for obtaining an authorization code, and use it to get a new access token from the Account Kit server.
    
    **Processing after a refresh token has expired:**
    
    A refresh token is valid for 180 days. When a refresh token has expired (as indicated by the returned [REST API error code](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-refresh-token#section1394417423453)), the app server needs to instruct the app to call the authorization API again to request user authorization.
    
3.  The app checks whether the user has been bound to its own account system based on the obtained UnionID. If so, user sign-in is complete; if not, create a new app account, bind the UnionID to the app account, and then complete user sign-in.
