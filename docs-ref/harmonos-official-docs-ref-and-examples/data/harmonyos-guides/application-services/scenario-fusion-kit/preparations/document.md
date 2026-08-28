# Preparations

Before you start integrating Scenario Fusion Kit, make [necessary preparations](../../../getting-prepared/application-development-preparations/document.md) (public key fingerprint configuration included).

#### Applying for Permissions

You need to request required permissions according to your actual needs by complying with the [Basic Principles for Using Permissions](../../../system/security/application-access-control/application-permission-management/application-permission-management-overview/document.md#basic-principles-for-using-permissions). You need to [declare permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) as required.

| 
Permission

 | 

Scenario

 |
| :-- | :-- |
| 

ohos.permission.GET\_WIFI\_INFO

 | 

Request this permission to obtain Wi-Fi information in scenario-specific API calls. (The permission is not required for 5.0.1(13) and later versions.)

 |
| 

ohos.permission.ACCESS\_BLUETOOTH

 | 

Request this permission to obtain Bluetooth status information in scenario-specific API calls. (The permission is not required for 5.0.1(13) and later versions.)

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/9i8dfHfuRRKXhdisaZH0vw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062118Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23A294AF92BF52A2CFEFB5C4E64D3FD096022D75F095B29EB4EDE8E6B1149FA0)

To obtain the user program access control permission, you need to configure [program access control management](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9) first.
