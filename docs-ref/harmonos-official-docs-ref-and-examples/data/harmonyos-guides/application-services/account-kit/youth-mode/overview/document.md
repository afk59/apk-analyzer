# Overview

The youth mode is designed to facilitate collaboration between your app and the device to provide network protection for minors. By integrating Account Kit's [youth mode capabilities](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection), your app can quickly and automatically follow the device's youth mode status, simplifying the setting process for parents and creating a safe and healthy online environment for minors.

#### Basic Concepts

-   Minors
    
    Minors in this section refer to citizens under the age of 18 in the Chinese mainland.
    
-   Restrictions after the youth mode is enabled
    1.  Usage time limit: For minors aged 16 or above but under 18, the default daily usage time is 2 hours. For those younger than 16, the default is 1 hour.
    2.  App installation restrictions: By default, only age-appropriate apps can be installed.
    3.  App access restrictions: By default, only apps that have [integrated the youth mode–related capabilities](#li09241991923) and have the **minors\_mode** value configured as **1** are permitted to open (game-type apps must also meet age-appropriate requirements). Parents can grant exemptions for specific apps to allow usage for the current session.
    4.  Content access restrictions: Apps integrated with the youth mode–related capabilities will follow the youth mode status on the device by default and display age-appropriate content within the apps.
    5.  Restrictions on other system functions: Certain functions of the device will be limited. This includes things like uninstalling or updating apps, signing out of the HUAWEI ID, and using USB debugging. For a full rundown of these restrictions, go to **Settings** > **Digital Balance**.
-   Age-appropriate apps
    
    An age-appropriate app, as defined by HUAWEI AppGallery, is one whose age rating is equal to or lower than the age of an underage user. Examples:
    
    1.  An app rated 12+ on HUAWEI AppGallery is considered suitable for a 13-year-old user, as they meet the age requirement.
    2.  If an app is rated 18+ on HUAWEI AppGallery and a minor is only 7 years old, then that app is considered unsuitable for their age.
    
-   Mobile guardian
    
    The **Mobile guardian** switch is provided under **Settings** > **HUAWEI ID** > **Family Sharing**. Once the **Mobile guardian** switch is turned on, the youth mode on the minor's device will be automatically disabled.
    

#### Youth Mode Capabilities

Below lists the capabilities of the on-device youth mode:

-   [Obtaining the youth mode status and age group information](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section11505356101217): Your app can obtain the device's youth mode status and enable or disable its own youth mode status accordingly. When enabling the device's youth mode, parents need to set the age information of the minor using the device. When the youth mode is enabled, your app can obtain the age group of the minor currently set in the device's minor mode, and provide content and services suitable for that age group to the minor. Currently, the age groups fall into:
    -   Under 3 years old
    -   3 years old or older but younger than 8 years old
    -   8 years old or older but younger than 12 years old
    -   12 years old or older but younger than 16 years old
    -   16 years old or older but younger than 18 years old
-   [Enabling the device's youth mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section198884228396): Your app can call this API to launch a system-level guide that walks users through enabling the youth mode on their device.
-   [Disabling the device's youth mode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section525913399571): Your app can call this API to launch a system-level guide that walks users through disabling the youth mode on their device.
-   [Verifying the parent's identity](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section145101029104312): To enable the device's minor mode, a parent sets a six-digit password. It acts as a key to control the youth mode status. While enabling the device's youth mode, you can decide on whether your app calls the API for verifying the parent's identity.

#### Scenarios

| 
Scenario

 | 

Description

 | 

Subscenario

 | 

How to Implement

 |
| :-- | :-- | :-- | :-- |
| 

[Following the Device's Youth Mode Status](../synchronization-of-the-device-s-youth-mode-status-to-an-app/following-the-device-s-youth-mode-status/document.md)

 | 

The app follows the device's youth mode status.

 | 

The app obtains the device's youth mode status.

 | 

The app obtains the device's youth mode status by [querying the status](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section11505356101217) or [subscribing to relevant common events](../synchronization-of-the-device-s-youth-mode-status-to-an-app/following-the-device-s-youth-mode-status/document.md#section1636450112718). The app's youth mode status must align with the device's.

 |
| 

[Enabling the Youth Mode Within an App](../synchronization-of-the-device-s-youth-mode-status-to-an-app/enabling-the-youth-mode-within-an-app/document.md)

 | 

Users enable the device's youth mode within the app.

 | 

A system-level guide is launched to walk users through enabling the device's youth mode.

 | 

The app calls the [leadToTurnOnMinorsMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section198884228396) API for enabling the device's youth mode. After the device's youth mode is enabled, the app also turns its youth mode on accordingly.

 |
| 

[(Recommended) Disabling the App's Youth Mode](../synchronization-of-the-device-s-youth-mode-status-to-an-app/disabling-the-youth-mode-within-an-app/recommended-disabling-the-app-s-youth-mode/document.md)

 | 

The app's youth mode can be disabled separately.

 | 

Users disable the youth mode of the app.

 | 

The app calls the [verifyMinorsProtectionCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section145101029104312) API for verifying the parental control password. If the verification is successful, the youth mode of the app is disabled. In addition, the flag indicating that the youth mode of the app is disabled separately is set to **true**.

 |
| 

The app finds that the device's youth mode is enabled or disabled through a query or a common event subscription.

 | 

If the device's youth mode is enabled, but the flag indicating that the youth mode of the app is disabled separately is set as **true**, the app will not enable its youth mode. If the device's youth mode is enabled, and the flag is set as **false**, the app will enable its youth mode.

If the device's youth mode is disabled, the flag indicating that the youth mode of the app is disabled separately will be set as **false** and the app will disable its youth mode.

 |
| 

[Disabling the Device's Youth Mode](../synchronization-of-the-device-s-youth-mode-status-to-an-app/disabling-the-youth-mode-within-an-app/disabling-the-device-s-youth-mode/document.md)

 | 

Users disable the device's youth mode within the app.

 | 

A system-level guide is launched to walk users through disabling the device's youth mode.

 | 

The app calls the [leadToTurnOffMinorsMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section525913399571) API for disabling the device's youth mode. After the device's youth mode is disabled, the app also turns its youth mode off accordingly.

 |
| 

[Adjusting Youth Mode Settings](../synchronization-of-the-device-s-youth-mode-status-to-an-app/adjusting-youth-mode-settings/document.md)

 | 

A parent adjusts the settings such as content preferences and usage time after successful identity verification.

 | 

The password verification screen is displayed to verify the parent's identity.

 | 

The app calls the [verifyMinorsProtectionCredential](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section145101029104312) API for verifying the parental control password.

 |

You are advised to build youth mode capabilities for your app by referring to [Following the Device's Youth Mode Status](../synchronization-of-the-device-s-youth-mode-status-to-an-app/following-the-device-s-youth-mode-status/document.md), [Enabling the Youth Mode Within an App](../synchronization-of-the-device-s-youth-mode-status-to-an-app/enabling-the-youth-mode-within-an-app/document.md), and also [(Recommended) Disabling the App's Youth Mode](../synchronization-of-the-device-s-youth-mode-status-to-an-app/disabling-the-youth-mode-within-an-app/recommended-disabling-the-app-s-youth-mode/document.md).

You can refer to the [sample code](https://gitcode.com/HarmonyOS_Samples/accountkit-samplecode-clientdemo-arkts) provided by Account Kit to implement the youth mode capability.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/YPT2ven1RSeQTGjuvoVr6A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2668F23D8D9D026A91D95B383019896C0C54110E127BDCD9128E185481A8AA9C)

1.  You can go to **Settings** > **Digital Balance** and tap **Enable Youth mode** to enable the youth mode.
2.  In accordance with the **Law of the People's Republic of China on the Protection of Minors**, **Cybersecurity Law of the People's Republic of China**, **Personal Information Protection Law of the People's Republic of China**, **Regulation on the Protection of Minors in Cyberspace**, **Guidelines for the Development of Minor Mode on the Mobile Internet**, and other applicable laws and regulations, to strengthen the protection of minors online, we offer a youth mode (also known as minor mode) to create a safe and healthy digital environment for minors.
3.  If your app follows the youth mode on the device, **it is recommended that it use the name "Youth mode" that is the same as that on the device** for easier understanding.
4.  If your app, which follows the youth mode on the device, automatically synchronizes the youth mode status to other devices, there may be a situation where the youth mode cannot be turned off on other devices. This is a user experience issue that the app needs to address.

#### Restrictions

1.  The youth mode is supported on phones, tablets, and PCs/2-in-1 devices. Starting from version 5.1.1(19), it is also supported on TVs.
2.  Enabling or disabling the youth mode is unsupported in the following scenarios:
    1.  The system version is earlier than HarmonyOS NEXT/5.0._x_.
    2.  The signed-in account is not registered in the Chinese mainland.
    3.  The private space has been activated on a device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/qCtUQLUeT02VyRDN8XSJiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CAE3A852E669702AEA3003D54B001F8E6EA9725209A4E73C061156641CA8D499)

For the preceding scenarios, you are advised to call the [canIUse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available) and [supportMinorsMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section233519244152) APIs to check whether the device environment supports the youth mode. A program crash error will occur if you call the youth mode-related APIs in an unsupported device environment.

1.  If both the [canIUse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available) and [supportMinorsMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section233519244152) APIs return **true**, the device supports the youth mode–related system capability. The app can associate itself with the youth mode–related system capability by implementing relevant functions described in this topic.
2.  If the [canIUse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available) or [supportMinorsMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-minorsprotection#section233519244152) API returns **false**, the device does not support the youth mode–related system capability or relevant capability associations. In this case, the app needs to build its own youth mode or cancel the entry to youth mode.

#### Integration Guidelines

When integrating the youth mode, follow the guidelines below:

1.  After the youth mode is integrated, you need to declare that the youth mode is supported in your app.
    1.  In the **module.json5** file of the **entry** module in the project, configure **meta-data** under the **module** property and set **minors\_mode** to **1**, indicating that the app supports the youth mode. If the **minors\_mode** field is not configured or its value is not **1**, the youth mode is unsupported. When the device's youth mode is enabled, apps that do not support the youth mode will be defaulted to an inactive state.
        
        "module": {
          "name": "_<name>_",
          "type": "entry",
          "description": "_<description>_",
          "mainElement": "_<mainElement>_",
          "deviceTypes": \[\],
          "pages": "_<pages>_",
          "abilities": \[\],
          "metadata": \[
            {
              "name": "minors\_mode",
              "value": "1"
            }
          \]**,**
          "extensionAbilities": \[\]
        }
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/93/v3/YlmiYgJ-QT-D-hIK6qOh_g/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE220ABBBECAA69FD62BC57AC86F8A107068839915EF9407060BDAE0BCB4091B)
        
        1.  If your app declares that it supports the youth mode, it is recommended that your app follow the device's youth mode status to provide age-appropriate content. For an app whose youth mode does not follow the device's, the app itself shall bear any related liabilities arising therefrom. You must ensure that the content provided by your app in youth mode complies with all relevant laws, regulations, and regulatory requirements. You shall be solely responsible for any liabilities arising from any non-compliance.
        2.  If you have modified your app's usage control rules under **Digital Balance**, the latest modified rules shall prevail.
        
2.  The app needs to proactively synchronize the device's youth mode status, except for the scenario where users manually disable the youth mode of the app.
3.  After enabling the youth mode by following the device's youth mode status, your app also obtains the age group information. Then, it needs to provide age-appropriate content and also block features that are inaccessible to the age group.
    
    Example: An app detects that the device's youth mode is enabled through a query or a common-event subscription and the age group is 3 years old or older but younger than 8 years old, and it then automatically enables its youth mode. The app will recommend age-appropriate content for this age group and block inappropriate features.
    

#### Sign-In Process Design

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/76/v3/CqmE4ju6TiGzasUCzAdUng/en-us_image_0000002528823311.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062055Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4277711D4289E9BEA993C17FC80665CD7487E4B833CB4C9C638283DC766D8A43 "Click to enlarge")

When the youth mode is enabled, it is recommended that the app's home screen follow the UX design suggested above to maintain a consistent user experience.
