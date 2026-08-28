# Overview

In the APIs of Account Kit, credentials are essential for calling various APIs. They play a critical role in identity verification, permission validation, data security, and others.

#### Use Cases

-   **Obtaining a user-level credential**
    
    After user sign-in and authorization, your app can obtain a user-level access token using the authorization code. This token enables access to restricted Account Kit APIs, such as the API for [obtaining the avatar and nickname from user information](../../obtaining-user-information/obtaining-user-information-avatar-and-nickname/document.md) and API for [obtaining the risk level](../../obtaining-user-information/obtaining-the-risk-level/document.md).
    
-   **Refreshing a user-level credential**
    
    An access token refresh mechanism is provided, allowing your app to periodically refresh the access token to avoid interruptions in API calls.
    
-   **Parsing a credential**
    
    A credential parsing capability is provided, allowing your app to obtain key information such as client ID, user identity, and validity period.
    
-   **Revoking authorization for a user-level credential**
    
    This API can be used when the user proactively revokes authorization or when your app needs to terminate associated services.
    
-   **Obtaining an app-level credential**
    
    The access token (app-level credential) obtained through the client ID and client secret of the app can be used to call the app-level permission control API. (For example, [obtain a UnionID through an OpenID](../../extended-capabilities/obtaining-the-unionid-through-the-openid/document.md).)
