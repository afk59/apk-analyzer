# Quick Verification

#### Use Case

If an app does not have high requirements on the timeliness of the obtained mobile number, it can utilize Account Kit's mobile number authorization and quick verification capabilities to initiate a mobile number authorization request to the user. Upon obtaining user authorization, the app obtains the mobile phone number and proceeds to provide services for the user. This section describes the functions of mobile number authorization and quick verification provided by Account Kit. Additionally, the [quick mobile number verification button](../../../../scenario-fusion-kit/scenario-specific-buttons/mobile-number-quick-verification-button/document.md) provided by Scenario Fusion Kit can be used to quickly verify a mobile number.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/DYrObQ2hTZ68dfWD-55Iuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7D8E23BE8A2134DBC0447A1E9E523EADFC3E972B1AE7F6C8626EB58C1B8F1B5)

The quick verification method verifies a mobile number that a user associates with their HUAWEI ID or newly adds. **The verification is not necessarily in real time and requires user authorization only for the first time.**

**Figure 1** Quick mobile number verification on a phone (subject to the actual display)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/fIjTnFvqSYqYYjiPt7E6qA/en-us_image_0000002528943253.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5A8D497B8163C53CFB39D71D99DD636FE4D1BD26DB7C6A72B738B4DEF6245EE "Click to enlarge")

**Figure 2** Quick mobile number verification on a wearable (subject to the actual display)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/3sRAj71OSAi8Ovv_ne5f5g/en-us_image_0000002497063302.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F683D68A1A3224BB25BD1B3C5C324E1DEFC88AC9E5F3D80523CEDC33C346FE4A "Click to enlarge")

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/v0gRDKSARpipgRRMgch3Ag/en-us_image_0000002528943255.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D0FEDF1681D4F69700D22AB87ADA344D16CA3172069EA5250F219F3D9D8DDD8 "Click to enlarge")

The process is as follows:

1.  The app calls the authorization API by passing the necessary scope and permission. If user authorization is already obtained, an authorization code will be directly returned. If user authorization is not obtained, the authorization screen will be displayed. After user authorization, an authorization code will be returned.
2.  The app sends the authorization code to its server. Then, the app server uses the client ID, client secret, and authorization code to obtain an access token from the Account Kit server, and uses the access token to request user information.
3.  The app obtains the mobile number, UnionID, and OpenID from the user information.

#### API Description

The table below lists the key APIs for quick mobile number verification. For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createAuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section610319714214)(): [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165)

 | 

Obtains user authorization. Pass the **phone** scope for obtaining the mobile number and the **serviceauthcode** permission for obtaining an authorization code to [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165). Then, the app will obtain an authorization code.

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

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/2mkRCk4JTyuZ_wcp4_NW7g/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD784317282F86D33515FBC0CF9CCC527A4346C18EF909555C1D9CCB8F7D8397)

The above APIs must be called within the lifecycle of a page or custom component.

#### Prerequisites

1\. Make [necessary preparations](../../../getting-started/document.md).

-   Configure signing information and add a fingerprint. Otherwise, error [1001500001](../../../faqs/1001500001-fingerprint-certificate-verification-failure/document.md) will be returned, indicating that the app's certificate fingerprint fails the verification.
-   Apply for the scope for obtaining a user's mobile number. Otherwise, error [1001502014](../../../faqs/1001502014-necessary-scopes-not-requested/document.md) will be returned, indicating that necessary scopes or permissions are not requested.

2\. Make sure that a HUAWEI ID has signed in. If not, show the sign-in screen.

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
    // To obtain the user's mobile number, pass the scope as follows. Ensure that you have obtained the scope. Otherwise, error code 1001502014 will be returned.
    authRequest.scopes = \['phone'\];
    // To obtain an authorization code, set the permission as follows.
    authRequest.permissions = \['serviceauthcode'\];
    // Specify whether user authorization is required. If the value is true and the user has not signed in or granted authorization, the sign-in or authorization screen will be displayed.
    authRequest.forceAuthorization = true;
    // Used to prevent cross-site request forgery.
    authRequest.state = util.generateRandomUUID();
    
3.  Call the [executeRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section3975181884311) method of the [AuthenticationController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section620452019185) object to execute the authorization request, process the authorization result, parse the authorization result to obtain the authorization code, and send the authorization code to the app server for processing.
    
    // Execute the request.
    try {
      // The following provides only code snippets. Use it in the custom component instance to obtain the **UIContext** object as the input parameter of the function.
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
        const authorizationCode = authorizationWithHuaweiIDCredential?.authorizationCode;
        // Process the authorization code.
      }).catch((err: BusinessError) => {
        dealAllError(err);
      });
    } catch (error) {
      dealAllError(error);
    }
    
    // Handle the error.
    function dealAllError(error: BusinessError): void {
      hilog.error(0x0000, 'testTag', \`Failed to obtain userInfo. Code: ${error.code}, message: ${error.message}\`);
      // When the app attempts to obtain the mobile number for quick verification and UI interaction is required, you are advised to guide users using the corresponding error code prompts.
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
        // Failed to sign in. Try another way.
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
    

## Server-Side Development

1.  The app server calls the [API for obtaining user-level credentials](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-user-token#section1085901313579) with the client ID, client secret, and authorization code to request an access token and a refresh token from the Account Kit server.
2.  The app server uses the access token to call the [API for obtaining user information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-get-phone#section2520125725115), and retrieves the user's mobile number, UnionID, and OpenID from the obtained user information.
    
    **Processing after an access token has expired:**
    
    An access token is valid for only 60 minutes. When an access token has expired or is about to expire (as indicated by the returned [REST API error code](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-get-nickname-and-avatar#section15782984912)), request a new access token from the Account Kit server using a refresh token (valid for 180 days) through the API for [refreshing a user-level credential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-refresh-token#section1085901313579).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/faqUVzqqSSO48uyufc_MUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF6E39A0213A008D90B7B18C0322C88C365ABE726636B8D94179454454A2CCCC)
    
    1.  When the access token has expired, if your app does not use the refresh token to request a new access token from the Account Kit server, the authorization of the signed-in HUAWEI ID will become invalid. As a result, functions that rely on the expired access token will be unavailable.
    2.  If the access token becomes invalid abnormally (for example, the password is changed, the HUAWEI ID is signed out, or a device is removed from the list of devices already signed in with the HUAWEI ID), the app can call the authorization API again to request user authorization for obtaining an authorization code, and use it to get a new access token from the Account Kit server.
    
    **Processing after a refresh token has expired:**
    
    A refresh token is valid for 180 days. When a refresh token has expired (as indicated by the returned [REST API error code](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-obtain-refresh-token#section1394417423453)), the app server needs to instruct the app to call the authorization API again to request user authorization.
