# Configuring an App

Before integrating the digital product service, you need to configure **bundleName** and the identity information of your app.

#### Configuring bundleName

The value of **bundleName** in the **AppScope/app.json5** file of your project must be the same as the package name specified during [app creation](../../../../../getting-prepared/application-development-preparations/document.md#section13566816173114) in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html).

Here is a configuration example:

{
  "app": {
    // Set **bundleName** to the package name specified during app creation in AppGallery Connect.
    "bundleName": "com.huawei.\*\*\*.\*\*\*.demo",
    // ...
  }
}

#### Configuring App Identity Information

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), choose **Development and services**, locate your target project, and click the name of the target app to access the **Project settings** page. On the **General information** tab page, find the client ID under **App information**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/6wqbiZNWRBSullQaQopqoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E66454C20E8DCE7A725366E8634C4A3467CEE23ADC27B30349DB56F7C5989744)
    
    -   The app ID in the following figure will be used in the request to call server-side APIs.
    -   If **compatibleSdkVersion** of your app is 14 or later, the tasks of [adding a public key fingerprint](../../../../../getting-prepared/application-development-preparations/document.md#section1726913517284) and **configuring app identity information** are not required for IAP Kit integration.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/_TVlAmZ_TqykuVJ18NDd9A/en-us_image_0000002371652969.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062058Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62E7F31E891EA949DC3A853F8820BA074898848DAC4F3A8B852E55F191FA2D64 "Click to enlarge")
    
2.  Add the **client\_id** attribute configuration to the **module** block of the **entry/src/main/module.json5** file under the project to authenticate the app identity for APIs of the digital product service.
    
    **"module"**:{
      "type": "\*\*\*",
      "name": "\*\*\*",
      "description": "\*\*\*",
      "mainElement": "\*\*\*",
      "deviceTypes": \[\*\*\*\],
      // ...
      "metadata": \[
      {
        "name": "client\_id",
        "value": "\*\*\*"
      },
      // ...
      \]
    }
