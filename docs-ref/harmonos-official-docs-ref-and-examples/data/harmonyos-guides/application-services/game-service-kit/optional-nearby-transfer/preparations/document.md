# Preparations

#### Creating a Game

To release a game on HUAWEI AppGallery or use services provided by AppGallery Connect, you must create a game app in AppGallery Connect. For details, please refer to [Creating a Project](https://developer.huawei.com/consumer/en/doc/distribution/app/agc-help-createproject-0000001100334664) and [Creating a HarmonyOS App or Atomic Service](https://developer.huawei.com/consumer/en/doc/app/agc-help-createharmonyapp-0000001945392297). Relevant parameters need to be set as follows:

-   **App type**: Select **HarmonyOS app**.
-   **Level-1 app category**: Select **Game**.

#### Requesting the Nearby Transfer Open Capability

For security purposes, the nearby transfer capability is now permission-restricted. To use associated APIs, you must submit a request for enabling nearby transfer. The capability will be available only after the request is approved.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/) and click **Development and services**. Find your project in the project list, and click the game for which you want to request nearby transfer.
2.  Go to **Project settings** > **Manage open capabilities**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/GZlEROdLT72zQJoswxTU0g/en-us_image_0000002535032789.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A6765923BBA2EAAD38102673F84DF74BD8A64BA597BC82050DA011B9CF885A9E)
    
3.  Search for **Game Nearby Transfer** and click **Request** next to this capability.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/eMOHbA9-QOW02Dy3jg_M9Q/en-us_image_0000002502227874.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=257457224F9B1F4CDB98C6BCF8BFF3AFB9CDCB9CA0B0EB8F9EA4BE67FB3DA7A2)
    
4.  In the **New request--Game Nearby Transfer** dialog box that is displayed, enter the request information and click **Submit**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/JaYVZP6lT6GXREO3-V3X0w/en-us_image_0000002502387724.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C6DBF1237D2B71101CEE74D74E09339908D8469F24A0AEDB25106BC9D4920ED)
    
    | 
    Parameter
    
     | 
    
    Mandatory
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- |
    | 
    
    Request reason
    
     | 
    
    Yes
    
     | 
    
    Reason for requesting nearby transfer. Enter the information as prompted, with up to 512 characters.
    
     |
    | 
    
    Attachment
    
     | 
    
    No
    
     | 
    
    Only one attachment is allowed, with a maximum file size of 500 MB. The attachment can be a Word file, Excel file, image, video, or compressed package.
    
     |
    
5.  Back on the **Manage open capabilities** tab page, **Requesting** is displayed for **Game Nearby Transfer**. You will receive the request result in one to three working days.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/LQPuS44vTiagoAqmA55D-w/en-us_image_0000002502227880.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=71C6AA23CAEF0B2DA2D4607F8B82A8AD34FAEF0B03355B5D352EB8598C324835)
    
6.  Once your request is approved, you will receive a notification in the interaction center, the nearby transfer capability switch will be automatically enabled, and **Requesting** will change to a disabled **Request** button, indicating that nearby transfer has been successfully enabled for your app.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/cC7pCnsSR1-vrvyYRWfqLw/en-us_image_0000002534107701.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A15796130D7FA7F50D3D5B31E9AE436E82F76188E0BE26A461528BE952C4E2A)
    

#### Generating a Signing Certificate

The signature information, including the digital certificate and profile, can ensure the integrity of your game. Configure it by referring to [Configuring Signing Information](../../../../getting-prepared/application-development-preparations/document.md#section42841246144813).

#### Configuring the App ID and Required Permissions

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), choose **Development and services**, find your desired app, and click it to access the **Project settings** page. On the **General information** tab page, find the app ID under **App information**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/msWg7RMXQwGRX_m2mMOTRA/en-us_image_0000002474311090.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062105Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F0EE3C86F01744BFF5A0336808ADA51ADC945BA6166E5A267A1FE90E129DE30)
    
2.  In the **module.json5** file of the **entry** module in the project, add **metadata**, configure **app\_id**, add **requestPermissions**, and configure the following permissions:
    
    "module": {
      "name": "entry",
      "type": "entry",
      "description": "xxxx",
      "mainElement": "xxxx",
      "deviceTypes": \[
        "phone"
      \],
      "deliveryWithInstall": true,
      "pages": "$profile:main\_pages",
      "abilities": \[\],
      "metadata": \[ // Configure the following information:
        {
          "name": "app\_id",
          "value": "xxxxxx" // Set it to the app ID obtained in the preceding step.
        }
      \],
      "requestPermissions": \[ // Configure permissions.
         {
           "name": "ohos.permission.INTERNET" // Permission to access the Internet.
         },
         {
           "name": "ohos.permission.GET\_NETWORK\_INFO"  // Permission that allows the app to obtain network information.
         },
         {
           "name": "ohos.permission.SET\_NETWORK\_INFO" // Permission that allows the app to configure network information.
         },
         {
           "name": "ohos.permission.DISTRIBUTED\_DATASYNC", // Permission that allows data exchange among devices.
           "reason": "$string:distributed\_permission",
           "usedScene": {
             "abilities": \[
               "EntryAbility"
             \],
             "when": "inuse"
           }
         }
       \]
    }
