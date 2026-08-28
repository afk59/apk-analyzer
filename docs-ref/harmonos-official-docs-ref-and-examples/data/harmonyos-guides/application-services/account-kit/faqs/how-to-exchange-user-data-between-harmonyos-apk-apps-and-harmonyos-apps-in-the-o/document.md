# How to exchange user data between HarmonyOS APK apps and HarmonyOS apps in the one-tap sign-in scenario?

Devices are upgraded from HarmonyOS 3.x/4.x to HarmonyOS NEXT 5.0.x or later.

1.  For a HarmonyOS APK app that uses OpenID to associate user data, switch to use UnionID for user data association after the app changes to a HarmonyOS NEXT app. For details, please refer to [Obtaining the UnionID Through the OpenID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/account-api-get-unionid).
2.  For a HarmonyOS APK app that uses UnionID to associate user data, after the app changes to a HarmonyOS NEXT 5.0.x app and in the scenario where a mobile number is obtained for one-tap sign-in using a HUAWEI ID, the UnionID and mobile number need to be associated with user information. In this way, data can be exchanged between the one-tap sign-in using the HUAWEI ID and the sign-in using the mobile number. Check [Scenario Design](../../sign-in/signing-in-with-huawei-id-through-just-one-tap-obtaining-the-mobile-number-union/document.md#section4654113502814) for the detailed process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/-44V6N_TQgapM8kRyq2fUA/en-us_image_0000002497063310.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062056Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4BE235B532BE5DDE55341A073561099297DE2242A042F4C78894A1F46846AB44 "Click to enlarge")
