# What should I do if the avatar and nickname cannot be obtained?

1.  Make sure that the **profile** scope is properly passed in the call to the [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) API for obtaining **authorizationCode**.
    
    import { authentication } from '@kit.AccountKit';
    
    // Create an authorization request and set parameters.
    const authRequest = new authentication.HuaweiIDProvider().createAuthorizationWithHuaweiIDRequest();
    // To obtain the avatar and nickname, pass the following scope:
    **authRequest.scopes = \['profile'\]****;**
    // For server-side development, pass the following permission to obtain **authorizationCode**:
    authRequest.permissions = \['serviceauthcode'\];
    
2.  Make sure that the authorization code and ID token obtained through the [AuthorizationWithHuaweiIDRequest](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-authentication#section12940173017165) API are valid.
3.  Make sure that the [API for obtaining the avatar and nickname](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-user-info-get-nickname-and-avatar) is called from the Huawei's Account Kit server.
