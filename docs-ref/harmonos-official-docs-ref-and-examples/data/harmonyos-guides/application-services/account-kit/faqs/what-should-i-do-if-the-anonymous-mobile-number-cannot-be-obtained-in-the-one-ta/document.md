# What Should I Do If the Anonymous Mobile Number Cannot Be Obtained in the One-Tap Sign-In Scenario?

Perform the following steps if the anonymous mobile number cannot be obtained in the one-tap sign-in scenario.

1.  If [code obfuscation](../../../../application-framework/arkts/arkts-compilation-toolchain/arkguard-for-source-code-obfuscation/using-arkguard-for-source-code-obfuscation/document.md) is enabled, add the **quickLoginAnonymousPhone** property to the trustlist to prevent it from being obfuscated in the release package. Add the following information to the **obfuscation-rules.txt** file of the module that contains the API for obtaining an anonymous mobile number:
    
    \# If property obfuscation is enabled, you need to add the quickLoginAnonymousPhone property to the trustlist to prevent it from being obfuscated.
    -enable-property-obfuscation
    -keep-property-name
    quickLoginAnonymousPhone
    
2.  Wearables and TVs (excluding version 5.1.1) do not support the function of obtaining a mobile number. In this case, error [1001500003](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-error-code#section116574197436) will be returned.
3.  Check whether a mobile number is bound to the HUAWEI ID. If not, show the sign-in screen that contains other sign-in options.
4.  The HUAWEI ID used for one-tap sign-in must be from the Chinese mainland.
5.  Check whether you have requested the one-tap HUAWEI ID sign-in scope on the [Development and services](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/myProject) page of AppGallery Connect. If you have not requested the scope, as shown in the figure below, error [1001502014](../1001502014-necessary-scopes-not-requested/document.md) will be returned.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/vOO0gkpfQ6qUEfkinhm-3g/en-us_image_0000002497063330.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B5FF8566D82BA13D23B5E747C9DA1FF9C3D2AA112205DCE80CB711C64CCEFEC "Click to enlarge")
    
6.  The **one-tap HUAWEI ID sign-in** scope is under review or has not taken effect. **The scope will take effect 24 hours after being approved. You can adjust the system time of the debugging device forward by 24 hours and try again.**
7.  After you have obtained the scope, make sure that you set **scope** to **quickLoginAnonymousPhone**. For details, please refer to [App-Side Development](../../sign-in/signing-in-with-huawei-id-through-just-one-tap-obtaining-the-mobile-number-union/document.md#section834212543125).
    
        // Create an authorization request and set parameters.
        const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
        // To obtain an anonymous mobile number, the quickLoginAnonymousPhone scope must be passed. Make sure that you have been granted this scope beforehand. Otherwise, error code 1001502014 will be returned.
        authRequest.scopes = \['quickLoginAnonymousPhone'\];
