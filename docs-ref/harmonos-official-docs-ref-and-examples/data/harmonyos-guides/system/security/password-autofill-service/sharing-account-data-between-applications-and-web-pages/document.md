# Sharing Account Data Between Applications and Web Pages

#### Introduction

Password Vault supports saving and autofill of account passwords in applications and web pages. To improve password management experience, it offers the capability of sharing account data between applications and web pages.

With this capability, the account data saved in the current application or web page is preferentially recommended when password autofill is triggered. If no account data is saved in the current application or web page, the account of the associated web page or application is recommended.

When a password is selected, the passwords of the associated websites or applications are also displayed as suggested passwords.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/Uo8Wi71qQn-3p8KN7dPg0g/en-us_image_0000002185570538.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21BC4001C4F9B97D367C09E25144B9EABF6BC6C8E557BA0DABB41176C80692E7)

#### Scenarios

This capability can be used when both the application and web page have account and password login scenarios and the Password Vault capability has been implemented. The account data of the application or web page saved can be directly used for accessing the associated web page or application.

#### How to Access

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/0Iz5kaidS7mMidbgKRWlBA/en-us_image_0000002185410878.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=009E16629D407B3F6CC401C755A3CB1F6E2892EE4912C0DDA014DB1C49642DE2)

After an application and a web page are associated by App Linking, Password Vault can identify the application or web page based on the binding relationship.

To implement password sharing between an application and a web page, do as follows:

1.  Implement autofill for the application and web page.
    
    For details, see [Quick Adaptation](../accessing-password-vault-for-an-application/quick-adaptation/document.md) and [Adding Password Vault for Web Pages](../adding-password-vault-for-web-pages/document.md).
    
2.  Associate the application and web page by App Linking.
    
    [Enable App Linking in AGC](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section189581229144811) > [Associate the application on the website](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section6903241628) > [Configure the website domain name](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section1101111611317)
