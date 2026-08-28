# Overview

When an app needs to acquire a user's mobile number, it can use the relevant capability of Account Kit to request user authorization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/OAfg4F90QpSmVC2MkuxT5w/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A61648058FDB81713DCF2E4A593882E7C86BDE5E71F0C79EE9D83538017F7B5D)

If a user has signed in with an in-app account and the account has been bound to the UnionID of the user's HUAWEI ID, the app, when obtaining user information such as the mobile number, can determine whether to check the consistency between the UnionID bound to the in-app account and that of the HUAWEI ID.

Below describes the quick verification method provided by Account Kit.

| 
Method

 | 

Description

 |
| :-- | :-- |
| 

[Quick verification](../quick-verification/document.md)

 | 

Verifies a mobile number that a user associates with their HUAWEI ID or newly adds. **The verification is not necessarily in real time and requires user authorization only for the first time.**

 |

#### Restrictions

1.  Ensure that your app meets the mobile number usage requirements in [Regulations on the Scope of Necessary Personal Information for Common Types of Mobile Internet Applications](https://appinchina.co/government-documents/notice-on-issuing-the-regulations-on-the-scope-of-necessary-personal-information-for-common-types-of-mobile-internet-applications/). (Huawei does not assume any responsibility for the content on third-party websites.)
2.  The mobile number bound to a child account cannot be obtained through quick verification.
3.  The capability of obtaining the mobile number is supported on phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.0(18), it is also supported on wearables. Starting from version 5.1.1(19), it is also supported on TVs.
