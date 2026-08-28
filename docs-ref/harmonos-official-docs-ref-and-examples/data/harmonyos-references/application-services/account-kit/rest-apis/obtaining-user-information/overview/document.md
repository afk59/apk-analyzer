# Overview

Account Kit provides streamlined user identity verification and user data access capabilities. By leveraging the features of Account Kit, you can guide users through entering and managing relevant information to complete the authorization process. Then you can request a credential and call the relevant API of Account Kit server with the credential to obtain required information.

#### Use Cases

-   **Obtaining the mobile number and UnionID/OpenID associated with a HUAWEI ID through one-tap sign-in**
    
    You can quickly obtain the user's UnionID/OpenID and mobile number through a HUAWEI ID, enabling sign-in with minimal efforts while **maintaining association with the app's own account system**. For details, please refer to [Obtaining the UnionID/OpenID and Mobile Number Bound to a HUAWEI ID with One-Tap Sign-In](../obtaining-the-unionid-openid-and-mobile-number-bound-to-a-huawei-id-with-one-tap/document.md).
    
-   **Obtaining user information associated with a HUAWEI ID – avatar and nickname**
    
    After the user grants authorization for the app to obtain the avatar and nickname information, the app server calls the Account Kit server's relevant API to complete the personal information. For details, please refer to [Obtaining User information: Avatar and Nickname](../obtaining-user-information-avatar-and-nickname/document.md).
    
-   **Obtaining user information associated with a HUAWEI ID – mobile number**
    
    After a user grants authorization for the app to obtain their mobile number, the app server calls the Account Kit server's relevant API to quickly complete the user's profile information. For details, please refer to [Obtaining User Information: Mobile Number](../obtaining-user-information-mobile-number/document.md).
    
-   **Obtaining a user's risk level after sign-in**
    
    If the app needs to retrieve a user's risk level after the user signs in, the app server can call the corresponding API provided by the Account Kit server. For details, please refer to [Obtaining the Risk Level](../obtaining-the-risk-level/document.md).
