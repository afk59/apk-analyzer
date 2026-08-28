# Signing In with HUAWEI ID Through Just One Tap (Obtaining the Mobile Number, UnionID, and OpenID)

#### Overview

Account Kit, which is built on the [OAuth 2.0](https://oauth.net/2/) and [OpenID Connect](https://openid.net/connect/) protocols, enables an app to easily obtain HUAWEI ID users' identifiers and mobile numbers through one-tap sign-in, facilitating the establishment of a user system within the app.

**Advantages:**

-   Leveraging the security and convenience of HUAWEI IDs, users can sign in without entering account names and passwords, eliminating the need for complex security verifications. This streamlines the sign-in process and enhances the conversion rate.
-   System-verified mobile numbers are provided to link with existing app users.
-   A consistent sign-in experience is delivered across phones, tablets, PCs/2-in-1 devices, and TVs.

#### Use Case

If an app needs to obtain both the user's mobile number and UnionID to complete the sign-in process, Account Kit provides a one-tap HUAWEI ID sign-in button that can retrieve both pieces of information simultaneously. The app can embed this sign-in button directly into its own sign-in screen. When a user taps the button, the app can then fetch the user's mobile number and UnionID to implement the sign-in. If a device already has a HUAWEI ID signed in and the HUAWEI ID has been associated with a mobile number, one-tap sign-in to an app with the HUAWEI ID will obtain the mobile number even if the device does not have any SIM card.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/c51W_PJgRASA-yUC1PGvJw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E822EE6175CC85B78C5DAC2ADCFF9D219B728687F38DD4A8B70E97C326B261EF)

1.  One-tap sign-in with a child account:
    
    When a user tries to sign in with a child account, touching the one-tap HUAWEI ID sign-in button will trigger the parental verification process provided by Account Kit by default. (The verification page provided by Account Kit cannot be customized currently.) After the verification is complete, the user's identity and mobile number can be obtained. Currently, child accounts are not supported on TVs.
    
2.  About mobile number verification:
    
    Account Kit calls the system capability to obtain the mobile number of the SIM card in the device where a HUAWEI ID has signed in, and verifies the obtained mobile number against the mobile number bound to the HUAWEI ID. (Mobile data from a SIM card is not required as long as a network connection is available.) Upon a user touching the one-tap HUAWEI ID sign-in button, the app will verify HUAWEI ID SMS verification records of the bound mobile number. If a successful verification within the past 90 days is found, the bound mobile number will be returned. Otherwise, the app will initiate the default SMS verification process provided by Account Kit (using Account Kit's non-customizable verification screen) to ensure the returned mobile number is correctly verified.
    

#### Restrictions

1.  Ensure that your app meets the mobile number usage requirements in [Regulations on the Scope of Necessary Personal Information for Common Types of Mobile Internet Applications](https://appinchina.co/government-documents/notice-on-issuing-the-regulations-on-the-scope-of-necessary-personal-information-for-common-types-of-mobile-internet-applications/).
2.  To use the one-tap HUAWEI ID sign-in function, the user must first agree to the [HUAWEI ID User Authentication Agreement](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&amp;language=en-US). Upon a tap on the [HUAWEI ID User Authentication Agreement](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&amp;language=en-US) link, redirect the user to [https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=en-US](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&amp;language=en-US) in light mode and to [https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=en-US&bgmode=black](https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&amp;language=en-US&amp;bgmode=black) in dark mode.
3.  After obtaining the user's mobile number with their consent, use it appropriately based on specific service requirements and implement additional security measures as needed. For example, check whether the obtained mobile number was previously assigned.
4.  The one-tap HUAWEI ID sign-in function is available only to users in the Chinese mainland.
5.  Only the app server deployed in the Chinese mainland is allowed to request the mobile number bound to a HUAWEI ID.
6.  The one-tap HUAWEI ID sign-in capability is supported on phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.1(19), it is also supported on TVs.
7.  One-tap sign-in with a HUAWEI ID is available only to enterprise developers. For individual developers, only [sign-in with a HUAWEI ID](../signing-in-with-huawei-id-obtaining-the-unionid-and-openid/document.md) and [silent sign-in](../silently-signing-in/document.md) are supported.

#### Sign-In Process Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/OspkMyHKQUqeDri56B2tMw/en-us_image_0000002528823293.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CC96C6EE6C7B80899B9F5F805FC540FDF54C3EFECDFCFC472D8949C21547220 "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/2a0N72KqQqKeYU522Mzfmw/en-us_image_0000002528823283.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88A4333DE0DE51C848B8B1F4B2BE60341EFCEA696441BE2B1B9DB5C2E0553617 "Click to enlarge")

#### Sign-In UI Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/R3NS25NHRXiV_c1azIiyVw/en-us_image_0000002497223290.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC11BF8D8FB547958C7F353CCA94A3CCB3E644DC8D7B0381A1BF333C43F2F286 "Click to enlarge")

The sign-in process design and sign-in UI design related to the one-tap sign-in button must comply with the [rules specified here](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section41792374210). For the second design under **Sign-In Process Design**, implement the HUAWEI logo button according to **Style 3: logo-only buttons** in [Visual Specifications](https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section61791745172816). The designs that disobey the rules may result in app release failures or user experience issues. For details about the style of the one-tap sign-in button, please refer to [Style](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section19823216112610).

#### Scenario Design

The one-tap HUAWEI ID sign-in capability involves multiple scenarios and different processes, which you can implement based on your actual needs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bf/v3/n0aPscchQfWpPKKG8ajKmw/en-us_image_0000002528943259.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB2D332D9BC62F20A26D5F2C9ED71F0C6EC1DC8810F87330CC8D1498052ED63E "Click to enlarge")

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6c/v3/5DarP3GMReGjIYGJJ3Yebg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B6D9BA2DD202E3F5A7A5E3504CFA11ED3B87418FB5A938DF3E7AB5125BFD31A)

**Associating a UnionID/OpenID and mobile number with an app account could help implement functions such as [silent sign-in](../silently-signing-in/document.md), as well as [obtaining the user information](../../access-to-user-information-of-a-huawei-id/document.md) and [the risk level](../../access-to-user-information-of-a-huawei-id/obtaining-the-risk-level/obtaining-a-user-s-risk-level-through-one-tap-huawei-id-sign-in/document.md) of a HUAWEI ID, freeing the user from the sign-in process and fostering a secure and easy sign-in experience.**

#### Service Process

## First-Time Sign-in

If your app has not integrated HUAWEI ID sign-in before and there is no app account signed in via HUAWEI ID, implement one-tap HUAWEI ID sign-in as follows.

**Figure 1** One-tap HUAWEI ID sign-in process (for a user who has not signed in before)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/pEx5AJcSSI6HnnBmLkXtiQ/en-us_image_0000002497223298.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DD92EE3112C964F2295639E8327BDAB48C60B36B554E7586A80D0B57CB3844A1 "Click to enlarge")

The process is as follows:

1.  Make preparations (steps 1 to 4):
    1.  After the user launches your app, the app calls [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) with **scope** set to **quickLoginAnonymousPhone** to request an anonymous mobile number. If the returned anonymous mobile number is empty, show other sign-in options.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/UPJErWfTSGCYswGkOFtnRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A9D834445C8F1B73F0AA35FF3DBDE16FDFF40D1F2E13C0050EFCB68AFBC6166)
        
        Implement a timeout mechanism for the process of obtaining an anonymous mobile number. Set a timeout interval for your app based on actual scenarios. A 5-second timeout interval is recommended to ensure a good user experience.
        
    2.  If the HUAWEI ID has not signed in and the app calls [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) to request authorization, [1001502001 User Has Not Signed In to HUAWEI ID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-error-code#section539558125020) will be returned. In this case, show other sign-in options.
2.  Show the one-tap sign-in screen (step 5):
    1.  Show the obtained anonymous mobile number on the screen, configure a privacy agreement, set the sign-in button type to **LoginType.QUICK\_LOGIN**, and show the one-tap sign-in screen that contains the [LoginWithHuaweiIDButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-huawei-id-button#section1624716107193) component. Implement risk control according to actual sign-in scenarios. Pass the risk level (obtained through the API for [obtaining the risk level through one-tap HUAWEI ID sign-in](../../access-to-user-information-of-a-huawei-id/obtaining-the-risk-level/obtaining-a-user-s-risk-level-through-one-tap-huawei-id-sign-in/document.md)) through a component parameter, and perform risk control on malicious accounts accordingly to improve the security level of your app.
3.  Tap the one-tap sign-in button to associate a user's credentials with their account within the app (steps 6 to 16):
    1.  After the user accepts the agreement and taps the one-tap HUAWEI ID sign-in button, the app will obtain data such as the authorization code from [HuaweiIDCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section1862534912215).
    2.  The app sends the obtained authorization code to the app server. Then, the app server uses the authorization code to call the [/oauth2/v6/quickLogin/getPhoneNumber](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-quicklogin-by-code#section2520125725115) API for obtaining a user's complete mobile number, UnionID, and OpenID.
    3.  The app associates the mobile number, UnionID, and OpenID with the user account to complete user sign-in.

## (Optional) Non-First-Time Sign-in

If the app has integrated HUAWEI ID sign-in, and there is an app account once signed in via HUAWEI ID (that is, the user is already associated with the app's system database according to the UnionID/OpenID), perform your development as follows.

**Figure 2** One-tap HUAWEI ID sign-in process (for a user who has signed in before)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/IfNS2ddfS62QPakay6Yt5Q/en-us_image_0000002497063300.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0423C7CA2B73A46A9C1EB08C83CDA58CBF984824D1C537BA8489AAB9FC05C32 "Click to enlarge")

The process is as follows:

1.  The app calls [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) to obtain the authorization code in [AuthorizationWithHuaweiIDResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section10418450161620).
2.  The app server uses the authorization code to call the [/oauth2/v6/quickLogin/getPhoneNumber](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-quicklogin-by-code#section2520125725115) API for obtaining a user's complete mobile number, UnionID, and OpenID. Using an authorization code to retrieve user information can effectively prevent security risks caused by data traversal, identity spoofing, replay attacks, and other forms of cyberattacks.
3.  After verifying the user ID (UnionID/OpenID) and the sign-in credential (**SessionId**), the app checks whether the user has been associated with the app's system database based on the UnionID/OpenID. If so, take appropriate measures based on risk control requirements, security considerations, and service scenarios. For example, display the associated HUAWEI ID, so the user can choose whether to sign in using the HUAWEI ID, or execute silent sign-in, freeing the user from the sign-in process.

#### API Description

The key APIs for the one-tap HUAWEI ID sign-in button are listed in the table below.

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createAuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section610319714214)(): [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165)

 | 

Obtains user authorization. Pass the **quickLoginAnonymousPhone** scope required for one-tap HUAWEI ID sign-in to [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165). Then, the user's anonymous mobile number and authorization code can be obtained from the authorization result.

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
| 

[LoginWithHuaweiIDButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-huawei-id-button#section1624716107193)

 | 

HUAWEI ID sign-in button component.

This component supports one-tap HUAWEI ID sign-in only in plain text style. You can adjust parameters such as the button size and rounded corners to adapt to the HarmonyOS app sign-in UI. Additionally, you can use **BUTTON\_CUSTOM** of [Style](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section19823216112610) to define the text color and background color of the button.

 |
| 

[onClickLoginWithHuaweiIDButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section1171153745914)(callback: AsyncCallback<[HuaweiIDCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section1862534912215)\>): [LoginWithHuaweiIDButtonController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section6921622144614)

 | 

Registers a callback triggered to return the result of one-tap HUAWEI ID sign-in.

 |
| 

[setAgreementStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section20291953195314)(agreementStatus: [AgreementStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section183397331373)): [LoginWithHuaweiIDButtonController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section6921622144614)

 | 

Sets the agreement signing status. Before the user agrees to the agreement, its status is set to **NOT\_ACCEPTED**. After the user agrees to the agreement, its status is set to **ACCEPTED** and then the user can sign in with HUAWEI ID.

 |
| 

[onClickEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section1892092034820)(callback: AsyncCallback<[ClickEvent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section967316103272)\>): [LoginWithHuaweiIDButtonController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section6921622144614)

 | 

Registers a callback triggered for a tap event related to the one-tap HUAWEI ID sign-in button.

 |
| 

[continueLogin](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section9921053045)(callback: AsyncCallback<void>): [LoginWithHuaweiIDButtonController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-component-manager#section6921622144614)

 | 

Callback triggered when a user taps the accept & sign-in button in the agreement dialog box.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/q5vPDT1VQg-0JLSm1ZX6cg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37109FC6608F2195CE11C860E100F6DD887D199C4750E4C6569DD446ECFA5A14)

The above APIs must be called within the lifecycle of a page or custom component.

#### Prerequisites

1.  Make [necessary preparations](../../getting-started/document.md).
    
    Configure signing information and add a fingerprint. Otherwise, error [1001500001](../../faqs/1001500001-fingerprint-certificate-verification-failure/document.md) will be returned, indicating that the app's certificate fingerprint fails the verification.
    
    If the scope for one-tap HUAWEI ID sign-in is not requested, error code [1001502014](../../faqs/1001502014-necessary-scopes-not-requested/document.md) will be returned.
    
2.  If [code obfuscation](../../../../application-framework/arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/using-arkguard-for-source-code-obfuscation/document.md) is enabled for your app, you need to configure the obfuscation trustlist for the **quickLoginAnonymousPhone** attribute obtained from the code of your app project to prevent the attribute from being obfuscated during compilation of the release package. Otherwise, an anonymous mobile number cannot be obtained. Add the following information to the **obfuscation-rules.txt** file of the module that contains the API for obtaining an anonymous mobile number:
    
    \# If property obfuscation is enabled, you need to add the **quickLoginAnonymousPhone** property to the trustlist to prevent it from being obfuscated.
    -enable-property-obfuscation
    -keep-property-name
    quickLoginAnonymousPhone
    

#### App-Side Development

## First-Time Sign-in

1.  Import modules.
    
    Import the [authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication) module of Account Kit and related common modules.
    
    import { authentication } from '@kit.AccountKit';
    import { util } from '@kit.ArkTS';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Obtain the anonymous mobile number.
    
    Call [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) of the [authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication) module to obtain the anonymous mobile number of a HUAWEI ID user. The anonymous mobile number will be displayed on the sign-in screen.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/8u-dxdzKTbWEaaDlW5RpFQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A38B19C83F388DF07F3C9CFA79B354BBEB0ECA43E2B77784D3B0ED0239BAC4B2)
    
    **forceAuthorization** must be set to **false**.
    
    Check which of the following responses you received and act accordingly based on the descriptions below.
    
    (1) If an ArkTS error code is returned, you can refer to the table below to handle different error codes.
    
    **Table 1** Errors involved in obtaining an anonymous mobile number
    | 
    Error Code
    
     | 
    
    Description
    
     | 
    
    Solution
    
     |
    | :-- | :-- | :-- |
    | 
    
    1001502001
    
     | 
    
    The user has not signed in with their HUAWEI ID.
    
     | 
    
    Show other ways to sign in.
    
     |
    | 
    
    1001502005
    
     | 
    
    Network error.
    
     | 
    
    Prompt the user to check the network status and try again.
    
     |
    | 
    
    1001502009
    
     | 
    
    Internal error.
    
     | 
    
    Show other ways to sign in.
    
     |
    | 
    
    1001502014
    
     | 
    
    The app does not have the required scopes or permissions.
    
     | 
    
    Resolve the issue according to the instructions in [1001502014 Necessary Scopes Not Requested](../../faqs/1001502014-necessary-scopes-not-requested/document.md).
    
     |
    | 
    
    1001500001
    
     | 
    
    The certificate fingerprint of the app fails to be verified.
    
     | 
    
    Resolve the issue according to the instructions in [1001500001 Fingerprint Certificate Verification Failure](../../faqs/1001500001-fingerprint-certificate-verification-failure/document.md).
    
     |
    | 
    
    1001500002
    
     | 
    
    Repeated request.
    
     | 
    
    No further action is needed.
    
     |
    | 
    
    1001500003
    
     | 
    
    The scopes or permissions are not supported.
    
     | 
    
    1\. The HUAWEI ID user is registered in a region outside of the Chinese mainland. In this case, the app should display alternative sign-in methods.
    
    2\. The one-tap HUAWEI ID sign-in capability is supported on TVs only in version 5.1.1(19). For other versions of an app on TVs, it should use [another HUAWEI ID sign-in method](../signing-in-with-huawei-id-obtaining-the-unionid-and-openid/document.md).
    
     |
    | 
    
    12300001
    
     | 
    
    System service error.
    
     | 
    
    Show other ways to sign in.
    
     |
    
    (2) If the obtained anonymous mobile number is empty, it indicates that there is no mobile number bound to the HUAWEI ID, the app has not requested the relevant scope, or the scope has not taken effect. In this case, the app needs to show the sign-in screen with other sign-in options.
    
    (3) If [code obfuscation](../../../../application-framework/arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/using-arkguard-for-source-code-obfuscation/document.md) is enabled, add the **quickLoginAnonymousPhone** property to the trustlist to prevent it from being obfuscated.
    
      getQuickLoginAnonymousPhone() {
        // Create an authorization request and set parameters.
        const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
        // To obtain an anonymous mobile number, the quickLoginAnonymousPhone scope must be passed. Make sure that you have been granted this scope beforehand. Otherwise, error code 1001502014 will be returned.
        authRequest.scopes = \['quickLoginAnonymousPhone'\];
        // Used to prevent cross-site request forgery.
        authRequest.state = util.generateRandomUUID();
        // In the one-tap HUAWEI ID sign-in scenario, this parameter must be set to false.
        authRequest.forceAuthorization = false;
        const controller = new authentication.AuthenticationController();
        try {
          controller.executeRequest(authRequest).then((response: authentication.AuthorizationWithHuaweiIDResponse) => {
          // The anonymous mobile number is obtained.
            const anonymousPhone = response.data?.extraInfo?.quickLoginAnonymousPhone as string;
            if (anonymousPhone) {
              hilog.info(0x0000, 'testTag', 'Succeeded in authentication.');
              const quickLoginAnonymousPhone: string = anonymousPhone;
              return;
            }
            hilog.info(0x0000, 'testTag', 'Succeeded in authentication. AnonymousPhone is empty.');
            // If no anonymous mobile number is obtained, the app needs to display other sign-in options.
          }).catch((error: BusinessError) => {
            this.dealAllError(error);
          })
        } catch (error) {
          this.dealAllError(error);
        }
      }
    
      // Handle the error.
      dealAllError(error: BusinessError): void {
        hilog.error(0x0000, 'testTag',
          \`Failed to get quickLoginAnonymousPhone, errorCode is ${error.code}, errorMessage is ${error.message}\`);
        // In sign-in scenarios involving UI interactions, it is advised to guide the user with the following error code prompts:
        if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
          // HUAWEI ID not signed in. The app needs to display other sign-in options.
        } else if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
          // Network error. Check the network status and try again, or show other sign-in options.
        } else if (error.code === ErrorCode.ERROR\_CODE\_INTERNAL\_ERROR) {
          // Sign-in fails. The app needs to display other sign-in options.
        } else if (error.code === ErrorCode.ERROR\_CODE\_SYSTEM\_SERVICE) {
          // System service error. The app needs to display other sign-in options.
        } else if (error.code === ErrorCode.ERROR\_CODE\_REQUEST\_REFUSE) {
          // Repeated request. No further action is needed.
        } else {
          // Sign-in fails. The app needs to display other sign-in options.
        }
      }
    
      export enum ErrorCode {
        // HUAWEI ID not signed in.
        ERROR\_CODE\_LOGIN\_OUT = 1001502001,
        // Network error.
        ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
        // Internal error.
        ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
        // System service exception.
        ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
        // Repeated request.
        ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
      }
    
3.  Show the screen for one-tap sign-in with a HUAWEI ID and obtain an authorization code.
    
    Assign the obtained anonymous mobile number to the **quickLoginAnonymousPhone** variable in the code for the **QuickLoginButtonComponent** component. Call [LoginWithHuaweiIDButton](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-huawei-id-button) to implement the sign-in UI of your app, and display the HUAWEI ID sign-in button and the _HUAWEI ID User Authentication Agreement_ link. (Implement redirection with a link provided by Account Kit. For details, please refer to point 2 in [Restrictions](#section2942427314).) After the user accepts the agreement and touches the one-tap HUAWEI ID sign-in button, an authorization code will be obtained. You can send the code to the app server to obtain user information (the complete mobile number, UnionID, and OpenID). Using an authorization code to retrieve user information can effectively prevent security risks caused by data traversal, identity spoofing, replay attacks, and other forms of cyberattacks.
    
    import { loginComponentManager, LoginWithHuaweiIDButton } from '@kit.AccountKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { connection } from '@kit.NetworkKit';
    
    @Component
    struct QuickLoginComponent {
      // Use the anonymous mobile number obtained in step 2 here.
      @State quickLoginAnonymousPhone: string = '';
    
      build() {
        if (this.quickLoginAnonymousPhone) {
          QuickLoginButtonComponent({
            quickLoginAnonymousPhone: this.quickLoginAnonymousPhone
          })
        } else {
          // If the obtained mobile number authorized by the user is empty, implement a sign-in screen with other sign-in options as needed.
        }
      }
    }
    
    @Component
    struct QuickLoginButtonComponent {
      logTag: string = 'QuickLoginButtonComponent';
      domainId: number = 0x0000;
      @State quickLoginAnonymousPhone: string = '';
      // Indicates whether the agreements are accepted.
      @State isSelected: boolean = false;
      // Link to the HUAWEI ID User Authentication Agreement. The link here is only an example. For maintainability and security reasons, it is recommended that the domain name be not hardcoded locally during actual development.
      private static USER\_AUTHENTICATION\_PROTOCOL: string =
        'https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&language=zh-CN';
      private static USER\_SERVICE\_TAG = 'User Service Agreement';
      private static PRIVACY\_TAG = 'Privacy Policy';
      private static USER\_AUTHENTICATION\_TAG = 'HUAWEI ID User Authentication Agreement';
      // Define the Privacy Policy, User Service Agreement, and HUAWEI ID User Authentication Agreement related to LoginWithHuaweiIDButton.
      privacyText: loginComponentManager.PrivacyText\[\] = \[{
        text: 'I have read and agree ',
        type: loginComponentManager.TextType.PLAIN\_TEXT
      }, {
        text: 'User Service Agreement, ',
        tag: QuickLoginButtonComponent.USER\_SERVICE\_TAG,
        type: loginComponentManager.TextType.RICH\_TEXT
      }, {
        text: 'Privacy Policy, ',
        tag: QuickLoginButtonComponent.PRIVACY\_TAG,
        type: loginComponentManager.TextType.RICH\_TEXT
      }, {
        text: 'and ',
        type: loginComponentManager.TextType.PLAIN\_TEXT
      }, {
        text: 'HUAWEI ID User Authentication Agreement',
        tag: QuickLoginButtonComponent.USER\_AUTHENTICATION\_TAG,
        type: loginComponentManager.TextType.RICH\_TEXT
      }, {
        text: '.',
        type: loginComponentManager.TextType.PLAIN\_TEXT
      }\];
      // Construct the controller of LoginWithHuaweiIDButton.
      controller: loginComponentManager.LoginWithHuaweiIDButtonController =
        new loginComponentManager.LoginWithHuaweiIDButtonController()
          /\*\*
           \* For an app with a custom sign-in UI, if the user does not accept the agreements, set the agreement status to NOT\_ACCEPTED.
           \* Set the agreement status to ACCEPTED once the user accepts the agreements. The one-tap HUAWEI ID sign-in function is available only when the agreement status is ACCEPTED.
           \*/
          .setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED)
          .onClickLoginWithHuaweiIDButton((error: BusinessError | undefined,
            response: loginComponentManager.HuaweiIDCredential) => {
            this.handleLoginWithHuaweiIDButton(error, response);
          })
          .onClickEvent((error: BusinessError, clickEvent: loginComponentManager.ClickEvent) => {
            if (error) {
              hilog.error(this.domainId, this.logTag,
                \`onClickEvent error. errCode is ${error?.code}, errMessage is ${error?.message}\`);
              return;
            }
            hilog.info(this.domainId, this.logTag, \`onClickEvent clickEvent: ${clickEvent}\`);
            // Set the button to a disabled state, and re-enable it once the service logic has completed.
            this.controller.setEnabled(false);
          });
      agreementDialog: CustomDialogController = new CustomDialogController({
        builder: AgreementDialog({
          privacyText: this.privacyText,
          cancel: () => {
            this.agreementDialog.close();
            this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED);
          },
          confirm: () => {
            this.agreementDialog.close();
            this.isSelected = true;
            this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
            // Call this method to complete accepting the agreements and signing in at the same time, with no need to tap the sign-in button again.
            this.controller.continueLogin((error: BusinessError) => {
              if (error) {
                hilog.error(this.domainId, this.logTag,
                  \`Failed to login with agreementDialog. errCode is ${error.code}, errMessage is ${error.message}\`);
              } else {
                hilog.info(this.domainId, this.logTag,
                  'Succeeded in clicking agreementDialog continueLogin.');
              }
            });
          },
          clickHyperlinkText: () => {
            this.agreementDialog.close();
            this.jumpToPrivacyWebView();
          }
        }),
        autoCancel: false,
        alignment: DialogAlignment.Center,
      });
    
      // Pass the data required for page rendering, such as the anonymous mobile number.
      aboutToAppear(): void {
      }
    
      // Toast message.
      showToast(resource: string) {
        try {
          this.getUIContext().getPromptAction().showToast({
            message: resource,
            duration: 2000
          });
        } catch (error) {
          const message = (error as BusinessError).message
          const code = (error as BusinessError).code
          hilog.error(this.domainId, this.logTag, \`showToast args  errCode is ${code}, errMessage is ${message}\`);
        }
      }
    
      // Redirect to the HUAWEI ID User Authentication Agreement page. This page needs to be configured in the main\_pages.json file of the project.
      jumpToPrivacyWebView() {
        try {
          // Configure the ohos.permission.GET\_NETWORK\_INFO permission in the module.json5 file.
          const checkNetConn = connection.hasDefaultNetSync();
          if (!checkNetConn) {
            this.showToast('Service or network exception. Try again later.');
            return;
          }
        } catch (error) {
          const message = error.message as string;
          const code = error.code as string;
          hilog.error(0x0000, 'testTag', \`Failed to hasDefaultNetSync, errCode is ${code}, errMessage is ${message}\`);
        }
        this.getUIContext().getRouter().pushUrl({
          // Configure the ohos.permission.INTERNET network permission in the module.json5 file.
          url: 'pages/WebPage',
          params: {
            isFromDialog: true,
            url: QuickLoginButtonComponent.USER\_AUTHENTICATION\_PROTOCOL,
          }
        }, (err) => {
          if (err) {
            hilog.error(this.domainId, this.logTag,
              \`Failed to jumpToPrivacyWebView, errCode is ${err.code}, errMessage is ${err.message}\`);
          }
        });
      }
    
      handleLoginWithHuaweiIDButton(error: BusinessError | undefined,
        response: loginComponentManager.HuaweiIDCredential) {
        if (error) {
          hilog.error(this.domainId, this.logTag,
            \`Failed to login with LoginWithHuaweiIDButton. errCode is ${error.code}, errMessage is ${error.message}\`);     
          if (error.code === ErrorCode.ERROR\_CODE\_NETWORK\_ERROR) {
            this.getUIContext().showAlertDialog(
              {
                message: "No Internet connection. Check your network settings.",
                offset: { dx: 0, dy: -12 },
                alignment: DialogAlignment.Bottom,
                autoCancel: false,
                confirm: {
                  value: "OK",
                  action: () => {
                  }
                }
              }
            );
          } else if (error.code === ErrorCode.ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED) {
            // If the agreements are not accepted, a dialog box that asks you to accept the agreements and sign in will be displayed. This callback way is recommended.
            this.agreementDialog.open();
          } else if (error.code === ErrorCode.ERROR\_CODE\_LOGIN\_OUT) {
            // Message displayed when no HUAWEI ID is signed in.
            this.showToast("HUAWEI ID not signed in. Try again.")
          } else if (error.code === ErrorCode.ERROR\_CODE\_NOT\_SUPPORTED) {
            // Message displayed when the scope or permission is not supported.
            this.showToast("Unsupported scope or permission.");
          } else if (error.code === ErrorCode.ERROR\_CODE\_PARAMETER\_ERROR) {
            // Parameter error message.
            this.showToast ("Parameter error.");
          } else if (error.code === ErrorCode.ERROR\_CODE\_USER\_CANCEL) {
            // Operation canceled by the user. No further handling required.
          } else {
            // Messages displayed upon other exceptions.
            this.showToast('Service or network exception. Try again later.');
          }
          this.controller.setEnabled(true);
          return;
        }
        try {
          if (this.isSelected) {
            if (response) {
              hilog.info(this.domainId, this.logTag, 'Succeeded in clicking LoginWithHuaweiIDButton.');
              // Use the information below as needed.
              const authCode = response.authorizationCode;
            }
          } else {
            this.agreementDialog.open();
          }
        } catch (err) {
          hilog.error(this.domainId, this.logTag,
            \`Failed to login with LoginWithHuaweiIDButton, errCode: ${err.code}, errMessage: ${err.message}\`);
          this.getUIContext().showAlertDialog(
            {
              message: 'Service or network exception. Try again later.',
              offset: { dx: 0, dy: -12 },
              alignment: DialogAlignment.Bottom,
              autoCancel: false,
              confirm: {
                value: 'OK',
                action: () => {
                }
              }
            }
          );
        } finally {
          this.controller.setEnabled(true);
        }
      }
    
      build() {
        Scroll() {
          Column() {
            Column() {
              Column() {
                // This is a sample icon. You can replace it with a real icon to ensure proper compilation and execution.
                Image($r('app.media.app\_icon'))
                  .width(48)
                  .height(48)
                  .draggable(false)
                  .copyOption(CopyOptions.None)
                  .onComplete(() => {
                    hilog.info(this.domainId, this.logTag, 'appIcon loading success.');
                  })
                  .onError(() => {
                    hilog.error(this.domainId, this.logTag, 'appIcon loading fail.');
                  })
    
                Text($r('app.string.app\_name'))
                  .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                  .fontWeight(FontWeight.Medium)
                  .fontWeight(FontWeight.Bold)
                  .maxFontSize($r('sys.float.ohos\_id\_text\_size\_headline8'))
                  .minFontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
                  .maxLines(1)
                  .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
                  .constraintSize({ maxWidth: '100%' })
                  .margin({
                    top: 12,
                  })
    
                Text('App description')
                  .fontSize($r('sys.float.ohos\_id\_text\_size\_body2'))
                  .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
                  .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
                  .fontWeight(FontWeight.Regular)
                  .constraintSize({ maxWidth: '100%' })
                  .margin({
                    top: 8,
                  })
              }.margin({
                top: 100
              })
    
              Column() {
                Text(this.quickLoginAnonymousPhone)
                  .fontSize(36)
                  .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
                  .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                  .fontWeight(FontWeight.Bold)
                  .lineHeight(48)
                  .textAlign(TextAlign.Center)
                  .maxLines(1)
                  .constraintSize({ maxWidth: '100%', minHeight: 48 })
    
                Text('Mobile number bound to a HUAWEI ID')
                  .fontSize($r('sys.float.ohos\_id\_text\_size\_body2'))
                  .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
                  .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
                  .fontWeight(FontWeight.Regular)
                  .lineHeight(19)
                  .textAlign(TextAlign.Center)
                  .maxLines(1)
                  .constraintSize({ maxWidth: '100%' })
                  .margin({
                    top: 8
                  })
              }.margin({
                top: 64
              })
    
              Column() {
                LoginWithHuaweiIDButton({
                  params: {
                    // Style supported by LoginWithHuaweiIDButton.
                    style: loginComponentManager.Style.BUTTON\_RED,
                    // Set the HUAWEI ID sign-in button to the loading state while the user is signing in.
                    extraStyle: {
                      buttonStyle: new loginComponentManager.ButtonStyle().loadingStyle({
                        show: true
                      })
                    },
                    // Rounded corner radius of LoginWithHuaweiIDButton.
                    borderRadius: 24,
                    // Sign-in type supported by LoginWithHuaweiIDButton.
                    loginType: loginComponentManager.LoginType.QUICK\_LOGIN,
                    // The button style of LoginWithHuaweiIDButton follows system settings.
                    supportDarkMode: true
                  },
                  controller: this.controller
                })
              }
              .height(40)
              .margin({
                top: 56
              })
    
              Column() {
                Button({
                  type: ButtonType.Capsule,
                  stateEffect: true
                }) {
                  Text('Other sign-in options')
                    .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
                    .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                    .fontWeight(FontWeight.Medium)
                    .fontSize($r('sys.float.ohos\_id\_text\_size\_button1'))
                    .focusable(true)
                    .focusOnTouch(true)
                    .textOverflow({ overflow: TextOverflow.Ellipsis })
                    .maxLines(1)
                    .padding({ left: 8, right: 8 })
                }
                .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
                .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                .fontWeight(FontWeight.Medium)
                .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
                .focusable(true)
                .focusOnTouch(true)
                .constraintSize({ minHeight: 40 })
                .width('100%')
                .onClick(() => {
                  hilog.info(this.domainId, this.logTag, 'click optionalLoginButton.');
                })
              }.margin({ top: 16 })
            }.width('100%')
    
            Row() {
              Row() {
                Checkbox({ name: 'privacyCheckbox', group: 'privacyCheckboxGroup' })
                  .width(24)
                  .height(24)
                  .focusable(true)
                  .focusOnTouch(true)
                  .margin({ top: 0 })
                  .select(this.isSelected)
                  .onChange((value: boolean) => {
                    if (value) {
                      this.isSelected = true;
                      this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.ACCEPTED);
                    } else {
                      this.isSelected = false;
                      this.controller.setAgreementStatus(loginComponentManager.AgreementStatus.NOT\_ACCEPTED);
                    }
                    hilog.info(this.domainId, this.logTag, \`agreementChecked: ${value}\`);
                  })
              }
    
              Row() {
                Text() {
                  ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
                    if (item?.type === loginComponentManager.TextType.PLAIN\_TEXT && item?.text) {
                      Span(item?.text)
                        .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
                        .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
                        .fontWeight(FontWeight.Regular)
                        .fontSize($r('sys.float.ohos\_id\_text\_size\_body3'))
                    } else if (item?.type === loginComponentManager.TextType.RICH\_TEXT && item?.text) {
                      Span(item?.text)
                        .fontColor($r('sys.color.ohos\_id\_color\_text\_primary\_activated'))
                        .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                        .fontWeight(FontWeight.Medium)
                        .fontSize($r('sys.float.ohos\_id\_text\_size\_body3'))
                        .onClick(() => {
                          // The app needs to implement the agreement redirection logic based on item.tag.
                          hilog.info(this.domainId, this.logTag, \`click privacy text tag: ${item.tag}\`);
                          // HUAWEI ID User Authentication Agreement
                          if (item.tag === QuickLoginButtonComponent.USER\_AUTHENTICATION\_TAG) {
                            this.jumpToPrivacyWebView();
                          }
                        })
                    }
                  }, (item: loginComponentManager.PrivacyText) => item.text.toString())
                }
                .width('100%')
              }
              .margin({ left: 12 })
              .layoutWeight(1)
              .constraintSize({ minHeight: 24 })
            }
            .alignItems(VerticalAlign.Top)
            .margin({
              top: 16,
              bottom: 16
            })
          }
          .justifyContent(FlexAlign.SpaceBetween)
          .constraintSize({ minHeight: '100%' })
          .margin({
            left: 16,
            right: 16
          })
        }
        .width('100%')
        .height('100%')
      }
    }
    
    @CustomDialog
    export struct AgreementDialog {
      logTag: string = 'AgreementDialog';
      domainId: number = 0x0000;
      dialogController?: CustomDialogController;
      cancel: () => void = () => {
      };
      confirm: () => void = () => {
      };
      clickHyperlinkText: () => void = () => {
      };
      privacyText: loginComponentManager.PrivacyText\[\] = \[\];
      private static USER\_AUTHENTICATION\_TAG = 'HUAWEI ID User Authentication Agreement';
    
      build() {
        Column() {
          Row() {
            Text('User Service Agreement and Privacy Policy')
              .id('loginPanel\_agreement\_dialog\_privacy\_title')
              .maxFontSize($r('sys.float.ohos\_id\_text\_size\_headline8'))
              .minFontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
              .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
              .fontWeight(FontWeight.Bold)
              .textAlign(TextAlign.Center)
              .textOverflow({ overflow: TextOverflow.Ellipsis })
              .maxLines(2)
          }
          .alignItems(VerticalAlign.Center)
          .constraintSize({ minHeight: 56, maxWidth: 400 })
          .margin({
            left: $r('sys.float.ohos\_id\_max\_padding\_start'),
            right: $r('sys.float.ohos\_id\_max\_padding\_start')
          })
    
          Row() {
            Text() {
              ForEach(this.privacyText, (item: loginComponentManager.PrivacyText) => {
                if (item?.type === loginComponentManager.TextType.PLAIN\_TEXT && item?.text) {
                  Span(item?.text)
                    .fontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
                    .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
                    .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_regular'))
                    .fontWeight(FontWeight.Regular)
                } else if (item?.type === loginComponentManager.TextType.RICH\_TEXT && item?.text) {
                  Span(item?.text)
                    .fontSize($r('sys.float.ohos\_id\_text\_size\_body1'))
                    .fontColor('#CE0E2D')
                    .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
                    .fontWeight(FontWeight.Medium)
                    .onClick(() => {
                      // The app needs to implement the agreement redirection logic based on item.tag.
                      hilog.info(this.domainId, this.logTag, \`click privacy text tag: ${item.tag}\`);
                      // HUAWEI ID User Authentication Agreement
                      if (item.tag === AgreementDialog.USER\_AUTHENTICATION\_TAG) {
                        hilog.info(this.domainId, this.logTag, 'AgreementDialog click.');
                        this.clickHyperlinkText();
                      }
                    })
                }
              }, (item: loginComponentManager.PrivacyText) => item.text.toString())
            }
            .width('100%')
            .textOverflow({ overflow: TextOverflow.Ellipsis })
            .maxLines(10)
            .textAlign(TextAlign.Start)
            .focusable(true)
            .focusOnTouch(true)
            .padding({ left: 24, right: 24 })
          }.width('100%')
    
          Flex({
            direction: FlexDirection.Row
          }) {
            Button('Cancel',
              { type: ButtonType.Capsule, stateEffect: true })
              .id('loginPanel\_agreement\_cancel\_btn')
              .fontColor($r('sys.color.ohos\_id\_color\_text\_primary'))
              .fontSize($r('sys.float.ohos\_id\_text\_size\_button1'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
              .backgroundColor(Color.Transparent)
              .fontWeight(FontWeight.Medium)
              .focusable(true)
              .focusOnTouch(true)
              .constraintSize({ minHeight: 40, maxWidth: 400 })
              .width('50%')
              .onClick(() => {
                hilog.info(this.domainId, this.logTag, 'AgreementDialog cancel.');
                this.cancel();
              })
    
            Button('Accept & sign in',
              { type: ButtonType.Capsule, stateEffect: true })
              .id('loginPanel\_agreement\_dialog\_huawei\_id\_login\_btn')
              .fontColor(Color.White)
              .backgroundColor('#CE0E2D')
              .fontSize($r('sys.float.ohos\_id\_text\_size\_button1'))
              .fontFamily($r('sys.string.ohos\_id\_text\_font\_family\_medium'))
              .fontWeight(FontWeight.Medium)
              .focusable(true)
              .focusOnTouch(true)
              .constraintSize({ minHeight: 40, maxWidth: 400 })
              .width('50%')
              .onClick(() => {
                hilog.info(this.domainId, this.logTag, 'AgreementDialog confirm.');
                this.confirm();
              })
          }
          .margin({
            top: 8,
            left: $r('sys.float.ohos\_id\_elements\_margin\_horizontal\_l'),
            right: $r('sys.float.ohos\_id\_elements\_margin\_horizontal\_l'),
            bottom: 16
          })
        }.backgroundColor($r('sys.color.ohos\_id\_color\_dialog\_default\_bg'))
        .padding({
          left: 16,
          right: 16
        })
      }
    }
    
    export enum ErrorCode {
      // HUAWEI ID not signed in.
      ERROR\_CODE\_LOGIN\_OUT = 1001502001,
      // This HUAWEI ID does not support one-tap sign-in due to some causes. For example, it is not registered in the Chinese mainland.
      ERROR\_CODE\_NOT\_SUPPORTED = 1001500003,
      // Network error.
      ERROR\_CODE\_NETWORK\_ERROR = 1001502005,
      // Internal error.
      ERROR\_CODE\_INTERNAL\_ERROR = 1001502009,
      // Authorization canceled by the user.
      ERROR\_CODE\_USER\_CANCEL = 1001502012,
      // System service exception.
      ERROR\_CODE\_SYSTEM\_SERVICE = 12300001,
      // The user does not accept the agreements.
      ERROR\_CODE\_AGREEMENT\_STATUS\_NOT\_ACCEPTED = 1005300001,
      // Parameter error.
      ERROR\_CODE\_PARAMETER\_ERROR = 401,
      // Repeated request.
      ERROR\_CODE\_REQUEST\_REFUSE = 1001500002
    }
    
    Here is the sample code of the page that shows the _HUAWEI ID User Authentication Agreement:_
    
    import { webview } from '@kit.ArkWeb';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Screen for showing the _HUAWEI ID User Authentication Agreement_.
    @Entry
    @Component
    struct WebPage {
      @State webUrl?: string = '';
      @State progress: number = 0;
      logTag: string = 'WebPage';
      domainId: number = 0x0000;
      controller: webview.WebviewController = new webview.WebviewController();
    
      build() {
        Column() {
          Column() {
            Button({ type: ButtonType.Normal }) {
              Image($r('sys.media.ohos\_ic\_compnent\_titlebar\_back'))
                .backgroundColor(Color.Transparent)
                .borderRadius(20)
                .width(24)
                .height(24)
                .draggable(false)
                .autoResize(false)
                .focusable(true)
                .fillColor($r('sys.color.ohos\_id\_color\_titlebar\_icon'))
                .matchTextDirection(true)
            }
            .alignSelf(ItemAlign.Start)
            .backgroundColor($r('sys.color.ohos\_id\_color\_button\_normal'))
            .borderRadius(20)
            .width(40)
            .height(40)
            .onClick(() => {
              this.getUIContext().getRouter().back();
            })
          }
          .height(56)
          .width('100%')
          .justifyContent(FlexAlign.Center)
          .margin({
            top: 36,
            left: 16
          })
    
          Progress({ value: this.progress, type: ProgressType.Linear })
            .width('100%')
            .visibility(this.progress <= 99 ? Visibility.Visible : Visibility.None)
    
          Web({ src: this.webUrl ?? '', controller: this.controller })
            .backgroundColor(Color.Transparent)
            .margin({ bottom: 60 })
            .onProgressChange((event) => {
              hilog.info(this.domainId, this.logTag,
                'onProgressChange: ', (event ? event.newProgress : -1));
              this.progress = event ? event.newProgress : 0;
            })
            .darkMode(WebDarkMode.Auto)
            .forceDarkAccess(true)
            .onLoadIntercept((event) => {
              hilog.info(this.domainId, this.logTag, 'onLoadIntercept');
              return false;
            })
            .onErrorReceive((event) => {
              if (event) {
                hilog.error(this.domainId, this.logTag, \`onErrorReceive,errorInfo: ${event?.error?.getErrorInfo()}\`);
              }
            })
        }
        .alignItems(HorizontalAlign.Start)
        .padding({ left: 12, right: 12, bottom: 60 })
        .width('100%')
        .height('100%')
      }
    
      aboutToAppear(): void {
        hilog.info(0x0000, 'testTag', 'aboutToAppear');
        const params = this.getUIContext().getRouter().getParams() as Record<string, string>;
        this.webUrl = params.url ?? '';
        hilog.info(0x0000, 'testTag', \`webUrl: ${this.webUrl}\`);
      }
    
      aboutToDisappear(): void {
        hilog.info(0x0000, 'testTag', 'aboutToDisappear');
        if (this.webUrl) {
            try {
                this.controller.stop();
              } catch (error) {
                hilog.error(0x0000, 'testTag',
                  \`ErrorCode: ${(error as BusinessError).code},  Message: ${(error as BusinessError).message}\`);
          }
        }
      }
    }
    

## (Optional) Non-First-Time Sign-in

For subsequent sign-ins, please refer to [Step 1](#li14938717193220) and [Step 2](#li146111330184515) of the first-time sign-in development process to obtain the authorization code from [AuthorizationWithHuaweiIDResponse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section10418450161620). For possible exceptions and troubleshooting methods, please refer to [Table 1](#table269794534618).

After successfully obtaining the authorization code, your app should send it to the app server to retrieve the user identifiers (UnionID and OpenID). This allows your app to check whether the user has already been associated with an in-app account.

(1) If so, the app, based on risk assessment, security considerations, and specific business requirements, can display the associated account and allow the user to choose whether to sign in with the HUAWEI ID or proceed with a silent sign-in. If not, client-side development ends.

(2) If not, continue with the development as described in [Step 3](#li8130114016451) of the first sign-in process.

## (Optional) Using DevEco Studio for Easy Development

1.  Open the page that requires the one-tap sign-in function and create a container (for example, **Column**) in **build()** of the page.
2.  On the DevEco Studio menu bar, go to **View** > **Tool Windows** > **Kit Assistant** or press **Alt+K** to open the **Kit Assistant** pane.
3.  In the navigation tree on the left, choose **AccountKit** > **QuickLoginButton** and drag it to the newly created container. That is, the code snippet is inserted at the current position.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/uXQd3BJpTwCHVSJDkhS9xA/en-us_image_0000002497223296.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E223668EE3AE418C986AA263941170C4F364607D73D779FA482EE73978906D0 "Click to enlarge")
    
    If the code snippet fails to be inserted, locate the fault according to the [instructions](../../../../coding-and-debugging/writing-code/quickly-inserting-scenario-based-code-snippets/document.md).
    
4.  In the **getQuickLoginAnonymousPhone** function of the automatically generated code snippet, execute the **executeRequest** function to obtain the response result.
    
    Check which of the following responses you received and act accordingly based on the descriptions below.
    
    -   The anonymous mobile number and authorization code have been obtained. You can pass the authorization code to the app server to retrieve user identifiers (UnionID and OpenID) and then check whether the user is associated with an in-app account.
        
        (1) If so, the app, based on risk assessment, security considerations, and specific business requirements, can display the associated account and allow the user to choose whether to sign in with the HUAWEI ID or proceed with a silent sign-in. If not, client-side development ends.
        
        (2) If not, check whether any of the following exceptions exists. If no exception is found, continue with your development by going to [Step 5](#li2579174225910).
        
    -   Possible exceptions:
        
        (1) Error code [1001502001](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-error-code#section539558125020) is returned, indicating that no HUAWEI ID is signed in.
        
        (2) Error code [1001500003](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-error-code#section116574197436) is returned, indicating that the HUAWEI ID user is registered in a region outside of the Chinese mainland.
        
        (3) The returned anonymous mobile number is empty as the HUAWEI ID has not been bound to the mobile number, the scope or permission has not been applied for, or the scope or permission has not taken effect.
        
        If any of the above exceptions occurs, your app should show other sign-in options.
        
    
5.  Implement the sign-in UI of the app and display the HUAWEI ID sign-in button and the _HUAWEI ID User Authentication Agreement_ link. (Implement redirection with a link provided by Account Kit. For details, please refer to point 2 in [Restrictions](#section2942427314).) After the user accepts the agreement and touches the HUAWEI ID sign-in button, an authorization code will be obtained. You can send the code to the app server to obtain user information (the complete mobile number, UnionID, and OpenID).

#### Server-Side Development

1.  The app server uses the client ID, client secret, and authorization code to call the [/oauth2/v6/quickLogin/getPhoneNumber](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-quicklogin-by-code#section2520125725115) API for obtaining the complete mobile number and UnionID of a HUAWEI ID user.
2.  The app checks whether the user has been associated with its system database based on the obtained complete mobile number or UnionID. If so, bind the obtained UnionID and mobile number to an existing account within the app (skip this step if the user has been bound). If not, create an account and bind the mobile number and UnionID to the account.

#### Development for App-App Server Interaction

## App-App Server Development

Service process:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/8-XsRMJBRN6EwnTsD5bk4w/en-us_image_0000002497223292.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=83C5523B6E1524142BEF1FDDBC52832DAA2FC21C65BAAC3F58BC44D2AF2C389A)

-   Preparations:

1.  [Complete the development of the one-tap sign-in function for your app](#section834212543125).
2.  Send relevant API requests from your app to your app server [using the fetch method](../../../../system/network/remote-communication-kit/network-communication-using-http/initiating-an-http-request-and-obtaining-a-response/sending-a-network-request-arkts/document.md#section71222326515). Here is the development procedure:
    1.  Your app calls the API of the app server to send the authorization code to the app server.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/27/v3/DylO-m0VS1acUywfYpuJmw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFB380C98858EB8B5C0EB8A0177B42B0936C73F385699912B2AA7F71747FF31E)
        
        You need to implement measures to ensure the security of the interaction between the app and the app server.
        
        import { rcp } from '@kit.RemoteCommunicationKit';
        import { hilog } from '@kit.PerformanceAnalysisKit';
        import { util } from '@kit.ArkTS';
        import { BusinessError } from '@kit.BasicServicesKit';
        
        // Sample code that demonstrates how the app calls an API.
        export function rcpRequest(authCode: string) {
          // Define the request header.
          const headers: rcp.RequestHeaders = {
            'accept': 'application/json'
          };
          // Define the parameters to be passed.
          const postMessage: Record<string, string> = {
            'authorizationCode': authCode
          };
          const securityConfig: rcp.SecurityConfiguration = {
            tlsOptions: {
              tlsVersion: 'TlsV1.3'
            }
          };
          // Assume that http://localhost:8080 is the app server address.
          const baseUrl = 'http://localhost:8080/login';
          // Define the request object.
          const req = new rcp.Request(baseUrl, 'POST', headers, postMessage);
          try {
          // Create a communication session object.
            const session = rcp.createSession({ requestConfiguration: { security: securityConfig } });
          // Initiate a request.
            session.fetch(req).then((response) => {
              hilog.info(0x0000, 'getRcpResult', 'Succeeded in getting result from server.');
              if (response.body) {
                const decoder = util.TextDecoder.create('utf-8');
                const result = JSON.parse(decoder.decodeToString(new Uint8Array(response.body))) as Record<string, Object>;
                // This is a code example. The actual implementation depends on the data structure returned by the app server.
                const phoneNumber: string = JSON.stringify(result\['phone'\] ?? '');
                if (phoneNumber) {
                // The app handles the relevant logic.
                }
              } else {
                hilog.error(0x0000, 'getRcpResult', 'Failed to get response body.');
              }
            }).catch((err: BusinessError) => {
              hilog.error(0x0000, 'getRcpResult', \`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
            });
          } catch (err) {
            hilog.error(0x0000, 'getRcpResult', \`err: err code is ${err.code}, err message is ${JSON.stringify(err)}\`);
          }
        }
        
    2.  The app server provides an API for receiving the authorization code obtained by the app.
        
        **java**
        import com.huawei.account.common.Response;
        import com.huawei.account.entity.PhoneNumberResp;
        import com.huawei.account.entity.LoginReq;
        import com.huawei.account.service.impl.LoginService;
        import lombok.RequiredArgsConstructor;
        import org.springframework.web.bind.annotation.RestController;
        import org.springframework.web.bind.annotation.PostMapping;
        import org.springframework.web.bind.annotation.RequestBody;
        
        @RestController
        @RequiredArgsConstructor
        public class QuickLoginController {
            private final LoginService loginService;
        
            @PostMapping("/login")
            public Response login(@RequestBody LoginReq requestBody) {
                PhoneNumberResp accountInfo = loginService.loginWithHuawei(requestBody.getAuthorizationCode());
                return new Response(200, "login success!", accountInfo);
            }
        }
        
        **python**
        from flask import Flask, request, jsonify
        
        from service.loginService import login\_with\_huawei
        
        app = Flask(\_\_name\_\_)
        
        @app.route('/login', methods=\['POST'\])
        def login():
            # Verification request parameters.
            request\_data = request.get\_json()
            if not request\_data or 'authorizationCode' not in request\_data:
                return jsonify({
                    'code': 400,
                    'message': 'invalid authorizationCode',
                    'data': None
                })
            authorization\_code = request\_data\['authorizationCode'\]
        
            # Call the service layer.
            user\_info = login\_with\_huawei(authorization\_code)
            if not user\_info:
                return jsonify({
                    'code': 401,
                    'message': 'Failed to authenticate with Huawei',
                    'data': None
                })
        
            # Successful response.
            return jsonify({
                'code': 200,
                'message': 'Login successful',
                'data': user\_info
            })
        
        
        if \_\_name\_\_ == '\_\_main\_\_':
            app.run(debug=True, port=8080)
        
        **go**
        package main
        
        import (
            loginService "./service"
            "encoding/json"
            "errors"
            "fmt"
            \_ "fmt"
            "io/ioutil"
            "log"
            "net/http"
            \_ "strconv"
        )
        
        type LoginRequest struct {
            AuthorizationCode string \`json:"authorizationCode"\`
        }
        
        type Response struct {
            UserInfo UserInfo \`json:"data"\`
            Code     int      \`json:"code"\`
            Message  string   \`json:"message"\`
        }
        
        type UserInfo struct {
            OpenID            string \`json:"openId"\`
            UnionID           string \`json:"unionId"\`
            LoginMobileNumber string \`json:"phoneNumber"\`
            LoginMobileValid  int    \`json:"phoneNumberValid"\`
            PurePhoneNumber   string \`json:"purePhoneNumber"\`
            PhoneCountryCode  string \`json:"phoneCountryCode"\`
        }
        
        type PhoneNumberErrRsp struct {
            ResultCode int    \`json:"resultCode"\`
            ResultDesc string \`json:"resultDesc"\`
        }
        
        func loginHandler(w http.ResponseWriter, r \*http.Request) {
           // Set the common JSON response header.
            w.Header().Set("Content-Type", "application/json")
           // 1. Parse the request body.
            var loginRequest LoginRequest
            if err := parseLoginRequest(r, &loginRequest); err != nil {
               sendErrorResponse(w, http.StatusBadRequest, "Invalid request format")
               return
            }
        ...// 2. Service call.
            resp, err := loginService.LoginWithHuawei(loginRequest.AuthorizationCode)
            if err != nil {
               log.Printf("Login service error: %v", err)
               sendErrorResponse(w, http.StatusInternalServerError, "Authentication failed")
               return
            }
            defer resp.Body.Close()
           // 3. Process the response.
            userInfo, err := processUserInfoResponse(resp)
            if err != nil {
               log.Printf("User info processing error: %v", err)
               sendErrorResponse(w, http.StatusInternalServerError, "Failed to process user data")
               return
            }
           // 4. Return a success response.
            sendSuccessResponse(w, userInfo)
        }
        
        func parseLoginRequest(r \*http.Request, dest \*LoginRequest) error {
            body, err := ioutil.ReadAll(r.Body)
            if err != nil {
               return fmt.Errorf("failed to read request body: %v", err)
            }
            defer r.Body.Close()
            if err := json.Unmarshal(body, dest); err != nil {
               return fmt.Errorf("invalid JSON format: %v", err)
            }
            if dest.AuthorizationCode == "" {
               return errors.New("missing authorization code")
            }
            return nil
        }
        
        func processUserInfoResponse(resp \*http.Response) (\*UserInfo, error) {
            if resp.StatusCode != http.StatusOK {
               return nil, fmt.Errorf("unexpected status code: %d", resp.StatusCode)
            }
            respBody, err := ioutil.ReadAll(resp.Body)
            var phoneNumberErrRsp PhoneNumberErrRsp
            err = json.Unmarshal(respBody, &phoneNumberErrRsp)
            if err != nil {
               return nil, fmt.Errorf("failed to unmarshal response body: %v", err)
            }
            if phoneNumberErrRsp.ResultCode != 0 {
               return nil, fmt.Errorf("api error %d: %s", phoneNumberErrRsp.ResultCode, phoneNumberErrRsp.ResultDesc)
            }
            var userInfo UserInfo
            err = json.Unmarshal(respBody, &userInfo)
            if err != nil {
               return nil, fmt.Errorf("failed to unmarshal response body: %v", err)
            }
        
            /\*
            Query user information in the database based on the designed service process. Example:
            1. Query a user by UnionID. If a match is found, return the user information.
            2. If no match is found, query by mobile number; if found, associate the user's in-app account with their HUAWEI ID's UnionID and return the user information.
            3. If neither UnionID nor mobile number matches, proceed to the registration flow.
            \*/
        
            return &userInfo, nil
        }
        
        func sendErrorResponse(w http.ResponseWriter, statusCode int, message string) {
            w.WriteHeader(statusCode)
            response := Response{
               Code:    statusCode,
               Message: message,
            }
            if err := json.NewEncoder(w).Encode(response); err != nil {
               log.Printf("Failed to encode error response: %v", err)
            }
        }
        
        func sendSuccessResponse(w http.ResponseWriter, userInfo \*UserInfo) {
            response := Response{
               Code:     http.StatusOK,
               Message:  "Login successful",
               UserInfo: \*userInfo,
            }
            if err := json.NewEncoder(w).Encode(response); err != nil {
               log.Printf("Failed to encode success response: %v", err)
               w.WriteHeader(http.StatusInternalServerError)
            }
        }
        
        func main() {
            http.HandleFunc("/login", loginHandler)
            log.Println("Server starting on :8080...")
            if err := http.ListenAndServe(":8080", nil); err != nil {
               log.Fatalf("Server failed: %v", err)
            }
        }
        
        **php**
        <?php
        
        require \_\_DIR\_\_ . '/../service/LoginService.php';
        
        // Initialize the router.
        $router = new Router();
        $router->addRoute('POST', '/login', function($request) {
            // Obtain POST data.
            $requestBody = json\_decode(file\_get\_contents('php://input'), true);
            if (isset($requestBody\['authorizationCode'\])) {
                // Call the service layer to verify sign-in.
                $userInfo = LoginService::loginWithHuawei($requestBody\['authorizationCode'\]);
                if (!isset($userInfo)) {
                    echo json\_encode(\[
                        'code' => 500,
                        'message' => 'login failed!'
                    \]);
                    return;
                }
        
                // Return a response.
                echo json\_encode(\[
                    'data' => $userInfo,
                    'code' => 200,
                    'message' => 'login success!'
                \]);
            } else {
                echo json\_encode(\['code' => 400, 'message' => 'Missing authorization code'\]);
            }
        });
        
        // Process the request.
        $router->dispatch($\_SERVER\['REQUEST\_METHOD'\], parse\_url($\_SERVER\['REQUEST\_URI'\], PHP\_URL\_PATH));
        class Router {
            private $routes = \[\];
        
            public function addRoute($method, $path, $handler) {
                $this->routes\[strtoupper($method)\]\[$path\] = $handler;
            }
        
            public function dispatch($method, $uri) {
                header('Content-Type: application/json');
                $method = strtoupper($method);
                // Exactly match a route.
                if (isset($this->routes\[$method\]\[$uri\])) {
                    $handler = $this->routes\[$method\]\[$uri\];
                    $handler($\_REQUEST);
                    return;
                }
        
                // Route not found.
                echo json\_encode(\[
                    'message' => 'Not Found',
                    'code' => 404
                \]);
            }
        }
        
    3.  After obtaining the authorization code, the app server interconnects with the Account Kit server and calls the [/oauth2/v6/quickLogin/getPhoneNumber](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-quicklogin-by-code#section2520125725115) API to obtain the complete mobile number, UnionID, and OpenID. For details, please refer to [Server-Side Development](#section286103315177).
    4.  Based on the obtained UnionID, OpenID, and complete mobile number, the app server checks whether the signing-in user is a new user and whether the user has been associated with an account within the app. (Develop this check mechanism based on your actual service needs.)
    5.  User information is saved to or updated on the app server. After necessary processing is complete, the app server returns the user information to the app.
        
        **java**
        import com.alibaba.fastjson2.JSONObject;
        import com.huawei.account.config.AGCProperties;
        import com.huawei.account.config.Constants;
        import com.huawei.account.entity.PhoneNumberReq;
        import com.huawei.account.entity.PhoneNumberResp;
        import com.huawei.account.util.HttpUtil;
        import lombok.RequiredArgsConstructor;
        import lombok.extern.slf4j.Slf4j;
        import org.springframework.stereotype.Service;
        
        @Slf4j
        @Service
        @RequiredArgsConstructor
        public class LoginService {
            private final HttpUtil httpService;
        
            private final AGCProperties agcProperties;
        
            public PhoneNumberResp loginWithHuawei(String authorizationCode) {
                PhoneNumberReq phoneNumberReq = new PhoneNumberReq();
                phoneNumberReq.setClientId(agcProperties.getClientId()); // Read the client ID from the previously configured settings.
                phoneNumberReq.setClientSecret(agcProperties.getClientSecret()); // Read the client secret from the previously configured settings.
                phoneNumberReq.setCode(authorizationCode);
                PhoneNumberResp phoneNumberResp = httpService.callHttpPost(Constants.QUICK\_LOGIN\_PHONE\_NUMBER\_URL, phoneNumberReq, PhoneNumberResp.class).getBody();
                log.info("/oauth2/v6/quickLogin/getPhoneNumber response body is: {}", JSONObject.toJSONString(phoneNumberResp));
        
                // Database-related logic:
                // Query a user by UnionID. If a match is found, return the user information.
                // If no match is found, query by mobile number; if found, associate the user's in-app account with their HUAWEI ID's UnionID and return the user information.
                // If neither UnionID nor mobile number matches, proceed to the registration flow.
        
                return phoneNumberResp;
            }
        }
        
        **python**
        import requests
        import json
        import os
        
        parent\_dir = os.path.dirname(os.path.dirname(os.path.abspath(\_\_file\_\_)))
        target\_file = os.path.join(parent\_dir, "config", "agc.json")
        with open(target\_file) as f:
            agc\_config = json.load(f)
        
        def login\_with\_huawei(authorization\_code):
            # Configuration.
            client\_id = agc\_config\["clientId"\] # Read the client ID from the previously configured settings.
            client\_secret = agc\_config\["clientSecret"\] # Read the client secret from the previously configured settings.
            phone\_number\_url = "https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber"
        
            #  Build a request body.
            token\_request\_body = {
                "clientId": client\_id,
                "clientSecret": client\_secret,
                "code": authorization\_code
            }
        
            # Send the request to obtain the one-tap sign-in user's mobile number.
            user\_info\_response = {}
            try:
                user\_info\_response = requests.post(phone\_number\_url, headers={'Content-Type': 'application/json'}, json=token\_request\_body)
                user\_info\_response.raise\_for\_status()  # If the request fails, the HTTPError exception will be thrown.
                user\_info = json.loads(user\_info\_response.content.decode('utf-8'))
            except requests.RequestException as e:
                user\_info = json.loads(user\_info\_response.content.decode('utf-8'))
                print(f"Error retrieving /oauth2/v6/quickLogin/getPhoneNumber: {e}")
                print(f"Error retrieving /oauth2/v6/quickLogin/getPhoneNumber: {user\_info}")
                return None
            if "resultCode" in user\_info:
                assert user\_info\["resultCode"\] == 0
        
            # Query user information in the database based on the designed service process. Example:
            # 1. Query a user by UnionID. If a match is found, return the user information.
            # 2. If no match is found, query by mobile number; if found, associate the user's in-app account with their HUAWEI ID's UnionID and return the user information.
            # 3. If neither UnionID nor mobile number matches, proceed to the registration flow.
        
            return user\_info
        
        **go**
        package service
        
        import (
            "bytes"
            "encoding/json"
            "fmt"
            "io/ioutil"
            "net"
            "net/http"
            "path/filepath"
            "sync"
            "time"
        )
        
        type Response struct {
            Data    interface{} \`json:"data"\`
            Code    int         \`json:"code"\`
            Message string      \`json:"message"\`
        }
        
        type PhoneNumberReq struct {
            ClientId     string \`json:"clientId"\`
            ClientSecret string \`json:"clientSecret"\`
            Code         string \`json:"code"\`
        }
        
        var httpClient = &http.Client{
            Transport: &http.Transport{
               DialContext: (&net.Dialer{
                  Timeout: 5 \* time.Second,
               }).DialContext,
               TLSHandshakeTimeout:   5 \* time.Second,
               ResponseHeaderTimeout: 10 \* time.Second,
            },
            Timeout: 30 \* time.Second,
        }
        
        var (
            config     \*Config
            configOnce sync.Once
            configErr  error
        )
        
        type Config struct {
            ClientID     string \`json:"clientId"\`
            ClientSecret string \`json:"clientSecret"\`
        }
        
        func LoadConfig() (\*Config, error) {
            configOnce.Do(func() {
               data, err := ioutil.ReadFile(filepath.Join("src", "config", "agc.json"))
               if err != nil {
                  configErr = err
                  return
               }
               var cfg Config
               if err := json.Unmarshal(data, &cfg); err != nil {
                  configErr = err
                  return
               }
               config = &cfg
            })
            return config, configErr
        }
        
        func LoginWithHuawei(authorizationCode string) (\*http.Response, error) {
            config, err := LoadConfig()
            if err != nil {
               return nil, err
            }
            // 1. Build a request body.
            reqBody := PhoneNumberReq{
               ClientId:     config.ClientID,
               ClientSecret: config.ClientSecret,
               Code:         authorizationCode,
            }
            // 2. Serialize the request body into JSON.
            jsonData, err := json.Marshal(reqBody)
            resp, err := httpClient.Post("https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber", "application/json", bytes.NewBuffer(jsonData))
            if err != nil {
               fmt.Errorf("failed to make POST request: %v, %v", config.ClientID, config.ClientSecret)
               return nil, fmt.Errorf("failed to make POST request: %v", err)
            }
            return resp, nil
        }
        
        **php**
        <?php
        
        class LoginService {
            public static function loginWithHuawei($authorizationCode) {
                $agcConfig = require \_\_DIR\_\_ . '/../config/agc.php';
                $requestBody = \[
                    'clientId' => $agcConfig\['clientId'\],
                    'clientSecret' => $agcConfig\['clientSecret'\],
                    'code' => $authorizationCode
                \];
        
                $ch = curl\_init();
                curl\_setopt\_array($ch,
                    \[
                        CURLOPT\_RETURNTRANSFER => true,
                        CURLOPT\_POST => true,
                        CURLOPT\_HTTPHEADER => \[
                            'Content-Type: application/json',
                            'Accept: application/json'
                        \],
                        CURLOPT\_SSL\_VERIFYPEER => false,
                        CURLOPT\_SSL\_VERIFYHOST => false,
                        CURLOPT\_URL => 'https://account-api.cloud.huawei.com/oauth2/v6/quickLogin/getPhoneNumber',
                        CURLOPT\_POSTFIELDS => json\_encode($requestBody)
                    \]);
        
                $response = curl\_exec($ch);
                if ($response === false) {
                    error\_log('cURL Error: ' . curl\_error($ch));
                    curl\_close($ch);
                    return null;
                }
        
                $userInfo = json\_decode($response, true);
                curl\_close($ch);
                if (!isset($data\['resultCode'\]) && $userInfo\['resultCode'\] != 0) {
                    error\_log('cURL Error: ' . curl\_error($ch));
                    curl\_close($ch);
                }
        
                /\*\*
                 \* Query user information in the database based on the designed service process. Example:
                 \* 1. Query a user by UnionID. If a match is found, return the user information.
                 \* 2. If no match is found, query by mobile number; if found, associate the user's in-app account with their HUAWEI ID's UnionID and return the user information.
                 \* 3. If neither UnionID nor mobile number matches, proceed to the registration flow.
                 \*/
        
                return $userInfo;
            }
        }
        

## Joint Commissioning Between the App and App Server

Prerequisites: You have completed necessary development work on the app and app server based on the sign-in scheme that you adopt. For details, please refer to [App-Side Development](#section834212543125), [Server-Side Development](#section286103315177), and [App-App Server Development](#section9343175722020).

1.  After obtaining the authorization code, the app sends it to the app server through the relevant API. The app server uses the authorization code to obtain the user's UnionID, OpenID, and the mobile number associated with their HUAWEI ID.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/YE9l7OLwSKOqORXO_RHvPg/en-us_image_0000002528943249.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=188E7F6D0CB95E3C10FC5E4A0BA7411F556850716470C928726AF82FB87D7812 "Click to enlarge")
    
2.  After successful sign-in via the mobile number, UnionID, or OpenID (according to relevant sign-in schemes) bound to a HUAWEI ID, the app server will return the user information to the app. The app can choose whether to persistently store the user information locally as needed, such as the sign-in status, account name, mobile number, and user ID.
3.  The user information is displayed on the home screen or personal information screen, as shown in the figure below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/F3cll7EaSJyoXM8QDdPEDQ/en-us_image_0000002528943251.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7568E0DA9AF6B124A0CBB0FDB68BB13ADB456CF2D21C81D0A4321DCE2552598B "Click to enlarge")

#### Verification After Development

## Suggestions on User Experience Guarantee Within an App That Has Integrated the One-Tap HUAWEI ID Sign-In Function

After the development is complete, check whether your app delivers a user experience that meets the expectation after the one-tap HUAWEI ID sign-in function is integrated based on the following criteria:

<table><tbody><tr><td class="cellrowborder" valign="top" width="12.458754124587541%"><p>No.</p></td><td class="cellrowborder" valign="top" width="19.518048195180484%"><p>Criterion</p></td><td class="cellrowborder" valign="top" width="10.46895310468953%"><p>Type</p></td><td class="cellrowborder" valign="top" width="57.55424457554245%"><p>Description</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.458754124587541%"><p>1</p></td><td class="cellrowborder" valign="top" width="19.518048195180484%"><p>HUAWEI ID sign-in design guidelines</p></td><td class="cellrowborder" valign="top" width="10.46895310468953%"><p>Rules that must be followed</p></td><td class="cellrowborder" valign="top" width="57.55424457554245%"><p>Your app should meet the rules specified in <strong><a href="https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344#section41792374210" target="_blank">HUAWEI ID Instant Login Button</a></strong> under <a href="https://developer.huawei.com/consumer/en/doc/design-guides/id-0000001880001344" target="_blank">HUAWEI ID Web Login Function</a> to create an easy-to-use, efficient, consistent, and secure sign-in experience.</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.458754124587541%"><p>2</p></td><td class="cellrowborder" valign="top" width="19.518048195180484%"><p>User interaction experience principles</p></td><td class="cellrowborder" valign="top" width="10.46895310468953%"><p>Recommendations</p></td><td class="cellrowborder" valign="top" width="57.55424457554245%"><p>(1) The user agreement, privacy agreement, and HUAWEI ID user authentication agreement are provided on the sign-in screen and can be tapped to view their details.</p><p>(2) When a user finishes viewing the details of an agreement and chooses to exit the agreement details screen, the app should show the screen that the user is viewing before going to the agreement details screen.</p><p>(3) The user can sign in only after accepting all the agreements. If the user directly taps the button for signing in via HUAWEI ID without accepting all the agreements, a clear reminder must be displayed to tell the user that they need to accept all the agreements first.</p><p>(4) After a tap on the sign-in button, the sign-in process will be complete as expected, and the avatar and nickname authorization screen can be displayed. Even a cancel operation is performed on the authorization screen, the user still successfully signs in. If an exception occurs, the relevant screen must be terminated in a timely manner, preventing the app from crashing.</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.458754124587541%"><p>3</p></td><td class="cellrowborder" valign="top" width="19.518048195180484%"><p>User experience principles for content on the sign-in screen</p></td><td class="cellrowborder" valign="top" width="10.46895310468953%"><p>Recommendations</p></td><td class="cellrowborder" valign="top" width="57.55424457554245%"><p>(1) The area of other ways to sign in is provided only when necessary.</p><p>(2) After a user signs in through the one-tap HUAWEI ID sign-in function, the anonymous mobile number displayed must be that obtained from HUAWEI ID, instead of any other sources.</p><p>(3) The agreements that are displayed to users must contain the <a href="https://privacy.consumer.huawei.com/legal/id/authentication-terms.htm?code=CN&amp;amp;language=en-US" target="_blank">HUAWEI ID User Authentication Agreement</a>, and must be clickable and loadable. When a user finishes viewing the details of an agreement and chooses to exit the agreement details screen, the app should show the screen that the user is viewing before going to the agreement details screen.</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.458754124587541%"><p>4</p></td><td class="cellrowborder" valign="top" width="19.518048195180484%"><p>User experience principles for exception handling</p></td><td class="cellrowborder" valign="top" width="10.46895310468953%"><p>Recommendations</p></td><td class="cellrowborder" valign="top" width="57.55424457554245%"><p>When troubleshooting, note that:</p><p>(1) Upon a sign-in exception (for example, the network is abnormal or the HUAWEI ID outside the Chinese mainland is used), do not transparently transmit the original information such as the error code to the user.</p><p>(2) If SMS verification is triggered during sign-in, after the verification is successful, the app should not display any other verification code input screen.</p></td></tr><tr><td class="cellrowborder" valign="top" width="12.458754124587541%"><p>5</p></td><td class="cellrowborder" valign="top" width="19.518048195180484%"><p>User experience principles related to app lifecycle changes</p></td><td class="cellrowborder" valign="top" width="10.46895310468953%"><p>Recommendations</p></td><td class="cellrowborder" valign="top" width="57.55424457554245%"><p>The user sign-in status must remain unchangeable before and after the app update.</p></td></tr></tbody></table>
