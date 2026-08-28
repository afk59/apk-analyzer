# Requesting Scopes

Create an app in AppGallery Connect and create an app project on DevEco Studio. For details, please refer to [Application Development Preparations](../../../../getting-prepared/application-development-preparations/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/KLymXPeURi6GwFpHoeaBLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FF5033BA803B5DD23B6F6309A5DACD71823CB3D33CB48DDC92234C647EF54935)

If your app needs the scopes for one-tap sign-in via HUAWEI ID, for obtaining the mobile number, and for obtaining the shipping address, request the scopes by following the instructions below. Otherwise, you can skip this topic.

#### Self-Check Before Request

Before submitting a scope request, review **Table 1** to understand what the scope supports and how it is intended to be used. Then, go through **Tables 2, 3, and 4** to verify that your information such as the **app type, device type, and developer type** meet the request criteria. Requests that do not meet the criteria will be declined.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/TGyXSkMhQhSKq6Hs8Orjfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D27498B170F433A0E727F63ED19A8054A7F3808B777A96A2455DDBCD07551E4C)

The scopes for one-tap sign-in via HUAWEI ID, for obtaining a mobile number, and for obtaining a shipping address are available only to enterprise developers. For individual developers, only [sign-in with a HUAWEI ID (mobile number not obtained)](../../sign-in/signing-in-with-huawei-id-obtaining-the-unionid-and-openid/document.md) and [silent sign-in](../../sign-in/silently-signing-in/document.md) are supported.

**Table 1** Scope description
| 
Scope

 | 

Description

 | 

Supported App

 | 

Supported Developer Type

 | 

Supported Device Type

 |
| :-- | :-- | :-- | :-- | :-- |
| 

HUAWEI ID instant login

 | 

Allows an app to obtain a user's **UnionID**, **OpenID**, and **mobile number** associated with their HUAWEI ID.

 | 

Apps that do not fall under gaming or banking

 | 

Enterprise developer

 | 

Phone, tablet, PC/2-in-1 device, and TV

 |
| 

Obtain user's mobile number

 | 

Allows an app to obtain either the **mobile number** bound to a user's HUAWEI ID or **an alternative mobile number** chosen by the user.

 | 

Gaming app

 | 

Enterprise developer

 | 

Phone, tablet, PC/2-in-1 device, wearable, and TV

 |
| 

Obtain shipping address

 | 

Allows an app to obtain a user's **shipping address**, which can be used for receiving or shipping goods.

 | 

All

 | 

Enterprise developer

 | 

Phone, tablet, and PC/2-in-1 device

 |

**Table 2** Self-check before requesting the scope for one-tap sign-in with HUAWEI ID
| 
No.

 | 

Item

 |
| :-- | :-- |
| 

1

 | 

You must be an enterprise developer.

 |
| 

2

 | 

The app type must be HarmonyOS NEXT app. (This scope will not be approved for HarmonyOS apps.)

 |
| 

3

 | 

The scope is not available to gaming or banking apps currently.

 |
| 

4

 | 

If the app is not released on AppGallery, specify the reason.

 |
| 

5

 | 

If the app has any recent violations, the request will be denied, or if the scope is already granted, it may be revoked.

 |
| 

6

 | 

If you are found to have misused the scope, Huawei reserves the right to revoke it.

 |

**Table 3** Self-check before requesting the scope for obtaining a user's mobile number
| 
No.

 | 

Item

 |
| :-- | :-- |
| 

1

 | 

You must be an enterprise developer.

 |
| 

2

 | 

The scope is only available to gaming apps.

 |
| 

3

 | 

If the app is not released on AppGallery, specify the reason.

 |
| 

4

 | 

If the app has any recent violations, the request will be denied, or if the scope is already granted, it may be revoked.

 |
| 

5

 | 

If you are found to have misused the scope, Huawei reserves the right to revoke it.

 |

**Table 4** Self-check before requesting the scope for obtaining a user's shipping address
| 
No.

 | 

Item

 |
| :-- | :-- |
| 

1

 | 

You must be an enterprise developer.

 |
| 

2

 | 

If the app is not released on AppGallery, specify the reason.

 |
| 

3

 | 

If the app has any recent violations, the request will be denied, or if the scope is already granted, it may be revoked.

 |
| 

4

 | 

If you are found to have misused the scope, Huawei reserves the right to revoke it.

 |

#### Procedure

1.  Go to [Development and services](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/myProject) in AppGallery Connect, select the target project, and select the HarmonyOS app for which you want to apply for a scope.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/5X-CzC3jQVmheQo43XT_-w/en-us_image_0000002497063296.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=083F5416666E95957AF2006C057EFCA4ED01DE0BC99BC18334BEA2576E252B39 "Click to enlarge")
    
2.  Under **Project settings** > **Manage open capabilities**, select the desired scope, and click **Request**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/UQ1TKTLoQPSEb8x5yss-0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28A1C5A12A73E74615AA3EE0DC72CB344464CFF75D8FB66ACC89F0AEF965A96F)
    
    Currently, the **Request** button is available only to enterprise developers.
    
    The figure is for reference only. Permissions displayed may vary by app type. Please refer to the actual page for accurate information.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/DeH8jzW3QvCcTRAdayo8Cg/en-us_image_0000002528823279.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1D9AC42758F4C6ACAA703325BB9042E471FB41C3F79765058F11279CF2745F7A "Click to enlarge")
    
3.  On the **New request** page, specify required information, including the request reason.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/-gLIKLIZRe-spZOtjH0flg/en-us_image_0000002528823275.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB566EBE742E3ECB0D78C2CC8981C193A4938EA4B3E8C2BD076722DFF1C8CC9F "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/HHIqv0ngTiWU7rPyiAv6dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6BD1788B707EC95FDD586AF34A0F9B26206D4FB41F97FB7D486767172EE6E63)
    
    Template for filling in the request reason:
    
    -   **App introduction**: Specify the app type. For example, "XXX is a \[type\] app."
    -   **Usage scenario**: Describe how a scope will be used. For example, "In \[scenario\], the app requires access to \[capability\]." Refer to **Table 5** for [scenario types](#table869613911529). If your use case does not fall under the listed types, please describe it based on actual usage.
    -   **Request purpose**: Explain the intended use of a scope. For example, "After using \[feature\], users perform \[action\] to receive \[service\]."
    
    **Table 5** Scenario types
    | 
    **Scenario Type**
    
     | 
    
    **Scenario Description**
    
     |
    | :-- | :-- |
    | 
    
    Online ride-hailing
    
     | 
    
    Available services include online taxi booking service and on-call cruising taxi service.
    
     |
    | 
    
    Instant communications
    
     | 
    
    Available services include online instant communications with text, image, audio, and video.
    
     |
    | 
    
    Online community
    
     | 
    
    Available services include topic discussions, information sharing, and follow interactions on blogs/forums and in communities.
    
     |
    | 
    
    Online payment
    
     | 
    
    Available services include online payment, withdrawal, and transfer.
    
     |
    | 
    
    Online shopping
    
     | 
    
    Available services include purchase of goods.
    
     |
    | 
    
    Food delivery
    
     | 
    
    Available services include food purchase and delivery.
    
     |
    | 
    
    Mail and express
    
     | 
    
    Available services include delivery services for letters, parcels, printed matter, and other items.
    
     |
    | 
    
    Transportation ticketing
    
     | 
    
    Available services include transportation–related ticketing and itinerary management, such as ticket purchase, rescheduling, refunds.
    
     |
    | 
    
    Dating and matchmaking
    
     | 
    
    Available services include online dating and matchmaking.
    
     |
    | 
    
    Job search and recruitment
    
     | 
    
    Available services include the exchange of job search and recruitment information.
    
     |
    | 
    
    Online lending
    
     | 
    
    Available services include personal loan services provided through online platforms for consumption, daily business operations, and other purposes.
    
     |
    | 
    
    Real estate rental and sales
    
     | 
    
    Available services include listing personal real estate information and renting or selling houses.
    
     |
    | 
    
    Used car trading
    
     | 
    
    Available services include the exchange of used car trading information.
    
     |
    | 
    
    Online medical consultation and appointment booking
    
     | 
    
    Available services include online medical consultations and appointment bookings.
    
     |
    | 
    
    Travel services
    
     | 
    
    Available services include the publication and booking of travel products.
    
     |
    | 
    
    Hotel services
    
     | 
    
    Available services include hotel reservations.
    
     |
    | 
    
    Online games
    
     | 
    
    Available services include online game products and services.
    
     |
    | 
    
    Education and learning services
    
     | 
    
    Available services include online tutoring, online classes, and other educational resources.
    
     |
    | 
    
    Local life services
    
     | 
    
    Available services include daily life services such as house cleaning/maintenance/decorating and second-hand goods trading.
    
     |
    | 
    
    Vehicle services
    
     | 
    
    Available services include shared bicycles, shared cars, car rentals, and other vehicle–related services.
    
     |
    | 
    
    Investment and financial management
    
     | 
    
    Available services include stocks, futures, funds, bonds, and other investment and financial services.
    
     |
    | 
    
    Mobile banking
    
     | 
    
    Available services include bank account management, information inquiry, transfer, and remittance through mobile devices such as smartphones.
    
     |
    | 
    
    Email and cloud storage
    
     | 
    
    Available services include email and cloud storage.
    
     |
    | 
    
    Remote conferencing
    
     | 
    
    Available services include audio or video conferencing via the Internet.
    
     |
    | 
    
    Performance ticketing
    
     | 
    
    Available services include ticket purchasing for performances.
    
     |
    
4.  Once the request is submitted, you are automatically taken to the interaction center, where you will see a message stating the request is awaiting review.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/ypQd9twoSNylNoZiX8lEVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FFF35B4372FA92061C91A129DA453F6B760BF862B757B117BC8B0455449C3C6)
    
    The review result will be sent to the [interaction center](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/interactive) through an internal message within five working days.
    
5.  The scopes will take effect within 25 hours after being approved.
    
    **(Optional)** You can change the value of **versionCode** in **app.json5** of your project to validate the scopes.
    
    **Figure 1** Before  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/hp8aUujuRAO5k4kTIkyIUw/en-us_image_0000002497223276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=45B08E80DED3D7CC348DBD1FEDFD38CEE7A9B52868FBB3CDFDED5D630BD68EC0 "Click to enlarge")
    
    **Figure 2** After  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/iHKzdB-UTLmNOAAk0MVjMQ/en-us_image_0000002497223284.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31C6704D6EF0CD03441728A9DA61A9C89219865791B68A4DB835FFCF037CA891)
