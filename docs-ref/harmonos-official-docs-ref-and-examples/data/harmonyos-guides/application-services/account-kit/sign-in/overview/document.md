# Overview

Account Kit provides multiple sign-in methods, including [one-tap sign-in with a HUAWEI ID](../signing-in-with-huawei-id-through-just-one-tap-obtaining-the-mobile-number-union/document.md), [sign-in with a HUAWEI ID (mobile number not obtained)](../signing-in-with-huawei-id-obtaining-the-unionid-and-openid/document.md), and [silent sign-in](../silently-signing-in/document.md). One-tap sign-in with a HUAWEI ID is **available only to enterprise developers**. Sign-in with a HUAWEI ID and silent sign-in are **available to both enterprise and individual developers**. You can choose to implement one or more sign-in methods as needed.

#### Basic Concepts

HUAWEI ID user identifiers include UnionID and OpenID. For details about the formats of the identifiers, please refer to [Formats of OpenID and UnionID](../../faqs/formats-of-openid-and-unionid/document.md). The table below lists their definitions and use cases.

| 
Item

 | 

UnionID

 | 

OpenID

 |
| :-- | :-- | :-- |
| 

Definition

 | 

UnionID is a unique identifier for a HUAWEI ID user under a developer account. If a developer has multiple HarmonyOS apps, these apps will obtain the same UnionID for a specific user.

 | 

OpenID is a unique identifier for a HUAWEI ID user within a HarmonyOS app. Different HarmonyOS apps, regardless of whether they belong to the same developer account, will obtain different OpenIDs for the same user.

 |
| 

Use case

 | 

To uniquely identify a user under the same developer account, **UnionID is recommended.**

 | 

To uniquely identify a user within the same app, you can use OpenID.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2e/v3/F3Sno25NRTeEdRqlbfQvKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DD8E697E9CDB17ADA35DEF327CDBB68D0C109BFF9A74B89B01B4F6E9D70E4A2)

When developing HarmonyOS apps, you need to consider whether the data of the same user can be exchanged between non-HarmonyOS apps and HarmonyOS apps. If you used OpenID to associate user data within non-HarmonyOS apps before, it is recommended that you switch to UnionID to ensure that your users can inherit their data from earlier versions after using HarmonyOS apps. For details, please refer to [Obtaining the UnionID Through the OpenID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-unionid).

#### Use Case

-   **Obtaining the mobile number and UnionID for sign-in, that is, one-tap sign-in with a HUAWEI ID**

This capability is recommended when an app needs to obtain both the mobile number and the UnionID. With just one tap, the app can obtain the **mobile number** and **UnionID** of a user. After obtaining the two items from the user, the app can **use them to associate users with its own account system**. This capability is available only to enterprise developers. For individual developers, only sign-in with a HUAWEI ID (mobile number not obtained) and silent sign-in are supported.

-   **Signing in with a HUAWEI ID**

Use this method if only the UnionID needs to be obtained. **Your app can use the UnionID to associate users with its own account system.**

-   **Silently signing in**

In scenarios such as app reinstallation or device change, the app can use the silent sign-in method provided by Account Kit to obtain the user's UnionID without requiring the user to tap the sign-in/sign-up button.

-   **Subscribing to HUAWEI ID sign-in/sign-out events**

When an app needs to sign the user in or out along with the status of a HUAWEI ID on a device, the app can subscribe to HUAWEI ID sign-in and sign-out events.
