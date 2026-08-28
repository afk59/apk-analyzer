# About This Kit

#### Use Case

Account Kit empowers your app with a simple, swift, and secure sign-in mechanism, enabling users to seamlessly sign in using their HUAWEI IDs. Upon user authorization, Account Kit grants your app access to user information, including the avatar, nickname, and mobile number, fostering a deeper understanding of your app's user base.

#### Functions

-   [Sign-In](../sign-in/document.md): Your app is empowered with a streamlined sign-in experience that allows users to effortlessly sign in using their HUAWEI IDs.
-   [Access to User Information of a HUAWEI ID](../access-to-user-information-of-a-huawei-id/document.md): A user's basic information can be obtained, including the avatar, nickname, mobile number, shipping address, invoice title, and risk level.
-   [Youth Mode](../youth-mode/document.md): The youth mode status and age group information can be retrieved for content rating. During the adjustment of youth mode–related settings, parental verification can be added, and also relevant APIs are provided for guiding users to enable or disable the youth mode. (Youth mode is also known as minor mode, which is intended for minors.)

#### Highlights

**One-tap sign-in**

With Account Kit's one-tap sign-in, apps can easily acquire users' authorization on their mobile numbers and streamline the sign-in process. This feature empowers apps to build their own user system or integrate with an existing one. Here are the advantages of this feature:

-   **Effortless sign-in**: achieves seamless sign-in with mobile number authorization simply after one tap, offering users a convenient and smooth sign-in experience.
-   **Seamless cross-device experience**: delivers consistent sign-in experiences across phones, tablets, and PCs/2-in-1 devices, ensuring the continuity of user data assets across devices.
-   **Enhanced efficiency**: eliminates the need for separate SDK integration, reducing development and operational costs for you.

**Youth mode**

Apps can seamlessly integrate with youth mode functionalities, enabling parents to easily activate this mode and foster a responsible digital environment for their children. More highlights of this feature are listed as follows:

-   **Easy parental control management**: supports centralized control over youth mode access. Simply enable the youth mode on the device, and apps will automatically synchronize this status, eliminating the need for repetitive operations within each app. This streamlined approach enhances user experience.
-   **Holistic child protection**: provides comprehensive protection for children through the seamless integration of apps and OS functionalities. This holistic approach encompasses a range of protective measures, including age-gated content access control, enhanced privacy control, and screen time management.

#### Sample Code

You can refer to the [sample code](https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-arkts) provided by Account Kit to implement functions such as [one-tap HUAWEI ID sign-in](../sign-in/signing-in-with-huawei-id-through-just-one-tap-obtaining-the-mobile-number-union/document.md) and [silent sign-in](../sign-in/silently-signing-in/document.md), as well as [obtaining the avatar and nickname](../access-to-user-information-of-a-huawei-id/obtaining-the-avatar-and-nickname/document.md), [verifying the mobile number in a quick manner](../access-to-user-information-of-a-huawei-id/obtaining-the-mobile-number/quick-verification/document.md), [obtaining the shipping address](../access-to-user-information-of-a-huawei-id/obtaining-the-shipping-address/document.md), [obtaining the invoice title](../access-to-user-information-of-a-huawei-id/obtaining-the-invoice-title/document.md), and [configuring youth mode status settings](../youth-mode/document.md).

#### Basic Concepts

-   **OpenID**: user ID at the app level, which uniquely identifies a HUAWEI ID in an app or atomic service. Different apps or atomic services, regardless of whether they belong to the same developer account, will obtain different OpenIDs for the same user.
-   **UnionID**: user ID at the developer level, which uniquely identifies a HUAWEI ID under a developer account. If a developer has multiple apps or atomic services, all apps or atomic services under the same developer account will obtain the same UnionID for a specific user.
-   **permission**: data or API permission, which can be used to indicate whether relevant data can be obtained or whether relevant APIs can be called.
-   **scopes**: list of scopes, which can be used to obtain user data. By specifying a scope, you can request different types of user data from Account Kit, for example, the avatar (**profile** scope required) and anonymous mobile number (**quickLoginAnonymousPhone** scope required).
-   **Authorization code**: authorization code. After the user signs in with a HUAWEI ID, you can obtain an authorization code by parsing the returned credential. The authorization code can be used to obtain an access token, refresh token, and ID token.
-   **Access token**: app-level credential used to access resources that are under permission control. With an access token, you can obtain user information by calling related APIs.
-   **ID token**: user identity credential that carries user information. It is provided by the [OpenID Connect](https://openid.net/specs/openid-connect-core-1_0.html) (OIDC) protocol, which extends OAuth 2.0. After a user successfully signs in with their HUAWEI ID, the returned credentials can be parsed to extract data such as the authorization code and ID token.

#### Restrictions

| 
Capabilities Provided by Account Kit

 | 

Supported Device Type

 |
| :-- | :-- |
| 

[Obtaining the Avatar and Nickname](../access-to-user-information-of-a-huawei-id/obtaining-the-avatar-and-nickname/document.md)

 | 

Phone, tablet, PC/2-in-1 device, wearable, and TV

 |
| 

[Obtaining the Mobile Number](../access-to-user-information-of-a-huawei-id/obtaining-the-mobile-number/document.md)

 | 

Phone, tablet, PC/2-in-1 device, wearable, and TV

 |
| 

[Obtaining the Shipping Address](../access-to-user-information-of-a-huawei-id/obtaining-the-shipping-address/document.md)

 | 

Phone, tablet, and PC/2-in-1 device

 |
| 

[Obtaining the Invoice Title](../access-to-user-information-of-a-huawei-id/obtaining-the-invoice-title/document.md)

 | 

Phone, tablet, and PC/2-in-1 device

 |
| 

[Obtaining the Risk Level](../access-to-user-information-of-a-huawei-id/obtaining-the-risk-level/document.md)

 | 

Phone, tablet, PC/2-in-1 device, wearable, and TV

 |
| 

[Youth Mode](../youth-mode/document.md)

 | 

Phone, tablet, PC/2-in-1 device, and TV

 |
| 

[ArkTS Components](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-arkts-component)

 | 

Phone, tablet, PC/2-in-1 device, and TV

 |

## Supported Countries/Regions

For details, please refer to [Supported Countries/Regions](../appendix/supported-countries-regions/document.md).
