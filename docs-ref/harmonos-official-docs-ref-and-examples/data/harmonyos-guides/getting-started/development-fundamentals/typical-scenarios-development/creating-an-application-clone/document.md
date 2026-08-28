# Creating an Application Clone

App clone allows multiple instances of the same application to be installed on one device, enabling simultaneous login and independent operation for multiple accounts. When users log in with two different accounts to a social media or a game application simultaneously, they do not have to switch accounts, reducing frequent logins.

After an application is cloned, multiple applications with the same icon are displayed on the home screen. An application with a lower corner mark is a cloned application.

Relationship between the main application and the cloned application:

-   These two applications share the same program. For example, when the main application is updated, the cloned one is synchronously updated, including icon, label, and new features.
-   Both applications are independent of each other in terms of feature enabling, related configurations, and data.
-   When the main application is uninstalled, all cloned applications will also be uninstalled. However, uninstalling a cloned application does not affect the main application.

The following figure shows the effect of cloned applications.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/QLytUC9rSeiBWwFnP8DQnA/en-us_image_0000002537924274.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7D726E6E40F9F319118D39D439C2B4AF43F56C9EF7ACD5D1F98E8034610C568)

#### Constraints

The input method application cannot create an application clone.

#### How to Develop

1.  Configure the application clone.
    
    Configure the [multiAppMode](../../application-configuration-files-in-stage-model/app-json5-configuration-file/document.md#multiappmode) field in the **AppScope/application.json5** configuration file in the project. The code snippet is as follows:
    
    {
      "app": {
        // ...
        "multiAppMode": {
          "multiAppModeType": "appClone",
          "maxCount": 2
        }
      }
    }
    
2.  Clone an application.
    
    -   Build and package the configured project and install it on the device.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/XbcT42EfQEeANYNyE1I_5w/en-us_image_0000002568684051.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31D2D3C44C000062AE296752CA67FBB2519841B92B2B0FE41442F930E2E1B852)
        
    -   Choose **Settings** > **System** > **App Clone**, and tap **Create**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/wrdobjZ2RdKcEgbg98jRtA/en-us_image_0000002568764061.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2AD9039F70B07EBCCCCD7582B665FD39D9FD7E8CE320CF974A6BC08205EEC3C8)
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Nz4k6MtjR4ubhvnow1SZwA/en-us_image_0000002537764336.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2933B055E3A869FD7AD88A8791ED9DC38C2F8A8DB2D90F01991533F38CC17CBA)
        
    -   Return to the home screen and check whether the application is cloned.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/67/v3/lmYaEp_4TJ2dinppikvDvw/en-us_image_0000002537924274.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061912Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04FE5F2316CDB4F991D186B2818BBD1A5DFE33554A494C4979750B7B134B7160)
        
        The three cloned applications in the figure are independent of each other in terms of process, running, data, and notification.
