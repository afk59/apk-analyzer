# Obtaining the Avatar and Nickname

#### Use Case

Account Kit provides the service for an app to obtain a user's avatar and nickname. Once the user grants authorization for the app to access their avatar and nickname, their profile information can be quickly filled in. This section describes the capability of obtaining an avatar and nickname provided by Account Kit. Additionally, the [avatar selection button](../../../scenario-fusion-kit/scenario-specific-buttons/avatar-selection-button/document.md) provided by Scenario Fusion Kit can be used to obtain an avatar.

**Figure 1** Obtaining the avatar and nickname on a phone (subject to the actual display)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/i7kEDbCkTQWx_4fv2AaUFQ/en-us_image_0000002497223308.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4897D9981510227F343288878598B7D0972B92C2275F5B7D903758646F499EA6 "Click to enlarge")

**Figure 2** Obtaining the avatar and nickname on a wearable (subject to the actual display)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/T0px2Li8ThWtnR4bQoUy9w/en-us_image_0000002528943277.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=188691456660C7974E75B55D2D1F301D0DE40770C78AEAE132BB9A7A7344ACD3 "Click to enlarge")

#### Restrictions

The capability of obtaining the avatar and nickname is supported on phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.0(18), it is also supported on wearables. Starting from version 5.1.1(19), it is also supported on TVs.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/ySXRz5_wR_-7bh4QXdO_iQ/en-us_image_0000002528823305.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C2E0C8C40961BC387F17C9018FEB2655E755DCC4328F3BD068702872438BA9B5 "Click to enlarge")

The process is as follows:

1.  The app calls the authorization API, to which requested scopes are passed, to try obtaining a user's avatar and nickname.
2.  If the user has authorized the app, the user's avatar and nickname can be retrieved.
3.  If the user has not authorized the app, the authorization screen will be displayed. After the user grants authorization, the user's avatar and nickname can be retrieved.
4.  The app can download the avatar from the URL in the returned information.

#### API Description

The table below lists the key APIs for obtaining the avatar and nickname of a user. For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createAuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section610319714214)(): [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165)

 | 

Obtains the authorization request object. Pass the **profile** scope for obtaining the avatar and nickname and the **serviceauthcode** permission for obtaining an authorization code to the [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) object. Then, the avatar and nickname, as well as the authorization code can be obtained from the authorization result.

 |
| 

[constructor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section9716526428)(context?: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-common#context))

 | 

Creates an authorization request controller.

 |
| 

[executeRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section3975181884311)(request: [AuthenticationRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section3118182610348)): Promise<[AuthenticationResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section2697164193515)\>

 | 

Executes the authorization request using a promise.

The avatar and nickname can be parsed from the [AuthorizationWithHuaweiIDResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section10418450161620) subclass of [AuthenticationResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section2697164193515). For details about the parsing method, please refer to the sample code in [App-Side Development](#section154801110677).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/ByF55am7T7G9atGRQZlTJg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0349136B4B3CF644E34C669A68AFD1976A5CA201DA68417CAB60824A4CF0654F)

1\. The above APIs must be called within the lifecycle of a page or custom component.

2\. If no nickname is set, the mobile number or email address bound to the HUAWEI ID will be returned anonymously by default.

#### Prerequisites

Before coding, make sure that you have [configured the signing information and fingerprint](../../getting-started/configuring-signing-information-and-fingerprint/document.md) and also [set the client ID](../../getting-started/configuring-the-client-id/document.md). No additional scope or permission needs to be requested for the scenario described in this topic.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/af/v3/HRsyjBvGTdS2cMRV342SJA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F9C048A623D6866C70157FAC853D2E5D3B21FCC4DA3B86712206295A48F80E8)

Error [1001500001 App Certificate Fingerprint Verification Failure](../../faqs/1001500001-fingerprint-certificate-verification-failure/document.md) will be returned if the public key fingerprint is not configured correctly.

#### Development Procedure

## App-Side Development

1.  Import the [authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication) module and related common modules.
    
    import { authentication } from '@kit.AccountKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { util } from '@kit.ArkTS';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create an authorization request and set parameters.
    
    // Create an authorization request and set parameters.
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    // To obtain the avatar and nickname, pass the following scope:
    authRequest.scopes = \['profile'\];
    // For server-side development, pass the following permission to obtain authorizationCode:
    authRequest.permissions = \['serviceauthcode'\];
    // Specify whether user authorization is required. If the value is true and the user has not signed in or granted authorization, the sign-in or authorization screen will be displayed.
    authRequest.forceAuthorization = true;
    // Used to prevent cross-site request forgery.
    authRequest.state = util.generateRandomUUID();
    
3.  Call the [executeRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section3975181884311) method of the [AuthenticationController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section620452019185) object to execute the authorization request and process the authorization result to obtain the avatar, nickname, and authorization code from the authorization result.
    
    // Execute the authorization request.
    try {
      // The following provides only code snippets. Use it in the custom component instance to obtain the UIContext object as the input parameter of the function.
      const controller = new authentication.AuthenticationController(this.getUIContext().getHostContext());
      controller.executeRequest(authRequest).then((data) => {
        const authorizationWithHuaweiIDResponse = data as authentication.AuthorizationWithHuaweiIDResponse;
        const state = authorizationWithHuaweiIDResponse.state;
        if (state && authRequest.state !== state) {
          hilog.error(0x0000, 'testTag', \`Failed to authorize. The state is different, response state: ${state}\`);
          return;
        }
        hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
        const authorizationWithHuaweiIDCredential = authorizationWithHuaweiIDResponse?.data;
        const avatarUri = authorizationWithHuaweiIDCredential?.avatarUri;
        const nickName = authorizationWithHuaweiIDCredential?.nickName;
        // Process avatarUri and nickName.
        const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
        // In the server-side development scenario that involves the retrieval of user avatars and nicknames, you need to process the authorization code.
      }).catch((err: BusinessError) => {
        dealAllError(err);
      });
    } catch (error) {
      dealAllError(error);
    }
    
    // Handle the error.
    function dealAllError(error: BusinessError): void {
      hilog.error(0x0000, 'testTag', \`Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}\`);
      // When the app attempts to obtain user avatars and nicknames and UI interaction is required, you are advised to guide users using the corresponding error code prompts.
      if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
        // Not signed in with a HUAWEI ID. Sign in with a HUAWEI ID and try again.
      } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
        // Network error. Check your network connection and try again.
      } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
        // Authorization canceled by the user.
      } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
        // System error. Try again later.
      } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
        // Repeated request. No further action is needed.
      } else {
        // Failed to obtain your information. Please try again later.
      }
    }
    
    export enum ErrorCode {
      // HUAWEI ID not signed in.
      ERROR\_CODE\_LOGIN\_OUT = 1001502001,
      // Network error.
      ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
      // Authorization canceled by the user.
      ERROR\_CODE\_USER\_CANCEL = 1001502012,
      // System service exception.
      ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
      // Repeated request.
      ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
    }
    

## (Optional) Server-Side Development

You can determine whether to make server-side development according to your service requirements.

1.  The app server calls the [API for obtaining user-level credentials](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-user-token#section1085901313579) with the client ID, client secret, and authorization code to request an access token and a refresh token from the Account Kit server.
2.  The app server calls the API [for obtaining user information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-get-nickname-and-avatar#section2520125725115) with the access token, and retrieves the user's avatar and nickname from the obtained user information.
    
    **Processing after an access token has expired:**
    
    An access token is valid for only 60 minutes. When an access token has expired or is about to expire (as indicated by the returned [REST API error code](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-get-nickname-and-avatar#section15782984912)), request a new access token from the Account Kit server using a refresh token (valid for 180 days) through the API for [refreshing a user-level credential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-refresh-token#section1085901313579).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d0/v3/w6tNpr-JQp6D3P7Xa6VOXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0BE29C506AA0A868E2A1D8A50232A05A138FF8469C6AE629D3009CDEAFCB860E)
    
    1.  When the access token has expired, if your app does not use the refresh token to request a new access token from the Account Kit server, the authorization of the signed-in HUAWEI ID will become invalid. As a result, functions that rely on the expired access token will be unavailable.
    2.  If the access token becomes invalid abnormally (for example, the password is changed, the HUAWEI ID is signed out, or a device is removed from the list of devices already signed in with the HUAWEI ID), the app can call the authorization API again to request user authorization for obtaining an authorization code, and use it to get a new access token from the Account Kit server.
    
    **Processing after a refresh token has expired:**
    
    A refresh token is valid for 180 days. When a refresh token has expired (as indicated by the returned [REST API error code](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-refresh-token#section1394417423453)), the app server needs to instruct the app to call the authorization API again to request user authorization.
