# Getting Started

Before using Car Kit capabilities, you need to configure the build mode, permissions, and capabilities.

#### Configuring the Build Mode

When packaging an app, click ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/NROxe_16QBS2RvXaicoxAQ/en-us_image_0000002418163981.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE5C2A5F42A4156E31F90CF7FBA6057CC8AFA1AE10CC7846CC018F02503E3F01) in the upper right corner of DevEco Studio, change the build mode to **release**, and click **Apply** in the lower right corner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/V_YAtOxITg-wVUAZQ0jisA/en-us_image_0000002384524882.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE5F8D9E34E0C18F8E3A4BF9E6598D13F4479B84DAD48EA71398F8B547E1B64C)

#### Configuring Permissions

Car Kit provides two types of APIs: navigation APIs and mobility connectivity APIs. You need to configure the corresponding permissions for using these APIs.

-   To use navigation APIs, you need to configure the **ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO** permission.
-   To use mobility connectivity APIs, you need to configure the **ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE** permission.

Configure required permissions in the app configuration file **module.json5** in **entry/src/main**. The sample code is as follows:

{
  "module": {
    "requestPermissions": \[
      {
        "name": "ohos.permission.ACCESS\_CAR\_DISTRIBUTED\_ENGINE"
      },
      {
        "name": "ohos.permission.ACCESS\_SERVICE\_NAVIGATION\_INFO"
      }
    \]
  }
}

#### Configuring Capabilities

Configure the navigation hop or HiCar capability in the **abilities** array of the app configuration file **module.json5** in **entry/src/main**. The procedure is as follows:

1.  Configure the actions of the navigation information service in [skills](../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/81XdfybrSpKGoee31Ynq0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062023Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFF67200880CB5BAAF5574B2CED2BFDCDF61165760EE7B2B611ACF1FCF360397)
    
    If your app has other skills, do not directly modify the existing configuration. Instead, supplement the configuration in the **skills** array.
    
    "skills": \[
      {
        "entities": \[
          "entity.system.default"
        \],
        "actions": \[
          "action.navigation.infoservice"
        \]
      },
      // Configuration of other skills.
      {
        // ...
      }
    \]
    
2.  Configure the navigation hop or HiCar capability in metadata. The sample code is as follows:
    
    {
      "module": {
        "abilities": \[
         {
            "name": "xxxx",
            "srcEntry": "xxxx",
            "description": "xxxx",
            "skills": \[
              {
                "entities": \[
                  "entity.system.home"
                \],
                "actions": \[
                  "action.system.home"
                \]
              },
              {
                "entities": \[
                  "entity.system.default"
                \],
                "actions": \[
                  "action.navigation.infoservice"
                \]
              }
            \],
            "metadata": \[
              {
                "name" : "carHopCapability",
                "value" : "carHopNavi,getOnCarNavi,insideCarNavi,getOffCarNavi"
              },
              {
                "name" : "hiCarCapability",
                "value" :"basicNavi,shortcutOper,multiScreenUI,mapUIOper,updateNaviStatus,searchPOI"
              }
            \]
          }
        \]
      }
    }
    

The options of **name** in metadata are **carHopCapability** and **hiCarCapability**.

-   If **name** is set to **carHopCapability**, the navigation hop capability is supported. The options of **value** are listed in the following table. Set it according to the service scenarios.
    
    | 
    Value
    
     | 
    
    Scenario
    
     |
    | :-- | :-- |
    | 
    
    carHopNavi
    
     | 
    
    Tap for navigation hop, which cannot coexist with "tap for address hop."
    
     |
    | 
    
    carHopAddress
    
     | 
    
    Tap for address hop, which cannot coexist with "tap for navigation hop."
    
     |
    | 
    
    getOnCarNavi
    
     | 
    
    Auto navigation hop upon vehicle entry.
    
     |
    | 
    
    insideCarNavi
    
     | 
    
    In-vehicle auto navigation hop.
    
     |
    | 
    
    getOffCarNavi
    
     | 
    
    Hop to walking navigation upon vehicle exit.
    
     |
    
-   If **name** is set to **hiCarCapability**, the HiCar capability is supported. The options of **value** are listed in the following table. Set it according to the service scenarios.
    
    | 
    Value
    
     | 
    
    Scenario
    
     |
    | :-- | :-- |
    | 
    
    basicNavi
    
     | 
    
    Basic navigation functions. The corresponding commands are as follows:
    
    1.  START\_NAVIGATION
    2.  STOP\_NAVIGATION
    
     |
    | 
    
    shortcutOper
    
     | 
    
    Shortcut operation functions. The corresponding commands are as follows:
    
    1.  GO\_HOME
    2.  GO\_TO\_COMPANY
    
     |
    | 
    
    multiScreenUI
    
     | 
    
    Multi-screen display functions. The corresponding commands are as follows:
    
    1.  START\_MAP\_LAYER
    2.  STOP\_MAP\_LAYER
    
     |
    | 
    
    mapUIOper
    
     | 
    
    Map UI control functions. The corresponding commands are as follows:
    
    1.  ZOOM\_IN\_MAP
    2.  ZOOM\_OUT\_MAP
    3.  CHANGE\_THEME
    
     |
    | 
    
    updateNaviStatus
    
     | 
    
    Map status and metadata update. The corresponding commands are as follows:
    
    1.  START\_UPDATE\_NAVIGATION\_STATUS
    2.  STOP\_UPDATE\_NAVIGATION\_STATUS
    
     |
    | 
    
    searchPOI
    
     | 
    
    Address search. The corresponding command is as follows:
    
    SEARCH\_POI
    
     |
    
    For more information about the commands, please refer to [CommandType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/car-navigationinfomgr#section1255014591510).
