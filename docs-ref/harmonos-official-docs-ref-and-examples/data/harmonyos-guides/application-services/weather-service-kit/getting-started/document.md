# Getting Started

Before you start integration, make [necessary preparations](../../../getting-prepared/application-development-preparations/document.md) (public key fingerprint included).

#### Enabling Weather Service Kit

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Pt7lYQ5hT_mzvJQBbEID0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062123Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72AF110414A883B9F287112224E14EDF76951083FF056234B5EE9BF71DE252D0)

Weather Service Kit is currently available only to system apps and cannot be accessed by external apps.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/).
2.  Click **Development and services**, find your project, and click the HarmonyOS app you created.
3.  Select Weather Service Kit on the **Manage open capabilities** tab page, and click **Save**.

#### Configuring the Profile

During API calling, Weather Service Kit will authenticate your profile. Therefore, after enabling Weather Service Kit, you need to apply for and configure the signing information in accordance with the instructions in [Configuring Signing Information](../../../getting-prepared/application-development-preparations/document.md#section42841246144813).

#### (Optional) Applying for Location Permissions

To obtain the weather data based on a user's current location, you need to call Location Kit to get the latitude and longitude information first. For details, please refer to [Applying for Permissions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-geolocationmanager#applying-for-permissions).
