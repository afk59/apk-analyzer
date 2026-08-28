# Configuring App Identity Information

#### bundleName Setting

The value of **bundleName** in the **AppScope/app.json5** file of the project must be the same as the package name specified during [app creation](../../../../getting-prepared/application-development-preparations/document.md#section13566816173114).

Here is a configuration example:

{
  "app": {
   // Set **bundleName** to the package name specified during app creation in AppGallery Connect.
    "bundleName": "com.huawei.\*\*\*.\*\*\*.demo",
    // ...
  }
}

#### App Identity Setting

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), choose **Development and services**, locate your target project, and click the name of the app to access the **Project settings** page. On the **General information** tab page, find the client ID under **App information**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/zySVfdMaRWqYnAXrMjze5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=012B7380206DAC91136C262B4F9DF1452BB88D82F99F781ACBAEDE669559426D)
    
    -   The app ID in the following figure will be used in the request to call APIs of the IAP server.
    -   If **compatibleSdkVersion** of your app is 14 or later, the tasks of [adding a public key fingerprint](../../../../getting-prepared/application-development-preparations/document.md#section1726913517284) and **configuring app identity information** are not required for IAP Kit integration.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/Q80Gm_UgRxmClOQt9GyFDw/en-us_image_0000002447011469.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062109Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C196C5A6966F2E1C48C5624D5DAFD174046B3D6779E81D6BD1489D0A214C17F "Click to enlarge")
    
2.  Add the **client\_id** attribute configuration to the **module** block in the **entry/src/main/module.json5** file under the project to authenticate the app identity for IAP Kit API calls.
    
    {
      "module":{
        "type": "\*\*\*",
        "name": "\*\*\*",
        "description": "\*\*\*",
        "mainElement": "\*\*\*",
        "deviceTypes": \[\*\*\*\],
        // ...
        "metadata": \[
          {
            "name": "**client\_id**",
            "value": "\*\*\*"
          }
          // ...
        \]
      }
    }
