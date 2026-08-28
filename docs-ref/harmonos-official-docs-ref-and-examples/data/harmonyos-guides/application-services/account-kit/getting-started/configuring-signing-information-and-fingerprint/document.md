# Configuring Signing Information and Fingerprint

Refer to [Application Development Preparations](../../../../getting-prepared/application-development-preparations/document.md) to complete the following operations:

1.  Create an app in AppGallery Connect and create an app project on DevEco Studio.
2.  Configure signing information. **(The youth mode–related APIs support automatic signing, and other APIs support only manual signing.)**
3.  Add a public key fingerprint.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/MECYxXOnR3WkZLNJoHQvTQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EC1A7F7C84A77A38E0B0E1FFFC363C32DF8D2F4CAB4988BAD51D170D86781E8)
    
    For the **release phase**, refer to the [Release Process](../../../../app-release/release/document.md#section6406135115814) section to reconfigure the signature information and (mandatory) add the public key fingerprint.
    

-   Check whether a public key fingerprint needs to be configured. If the app integrates only youth mode–related services or if **compatibleSdkVersion** is 20 or later, configuration of the public key fingerprint is not required. In all other scenarios, it must be configured.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/o-E52FTQRX64ITOoEWB-Gw/en-us_image_0000002528943261.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=213634E3B981D0F3B533920012F4C39A320B302C4A5F1819D24ACF1459CCA1BF)
    
-   Check whether the public key fingerprint is successfully configured. Go to [Development and services](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/myProject), select the corresponding project and app, and check the public key fingerprint.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/de/v3/aw0ro1dZRZa48V0yb7wc6A/en-us_image_0000002497063306.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F71B8A258C676969BE39CC59E9200EF8EFBF87CCFE7F95A5200BA60454E2A53 "Click to enlarge")
    
-   The public key fingerprint will take effect within 25 hours after being added.
    
    **(Optional)** Ten minutes after configuring the public key fingerprint, you can change the value of **versionCode** in the project's **app.json5** file to validate the fingerprint.
    
    **Figure 1** Before  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/56/v3/fgKZzm3kRRWKeP3leU6vdw/en-us_image_0000002528823285.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1D9EF89D7D4B682553DD24DF72328FA6BD9A7B2DC4753486012390A960BB8BA)
    
    **Figure 2** After  
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/S9I7LTktQhC1zRGfgDufBg/en-us_image_0000002497223294.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062054Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C1C66FF43E916B06941D7788B8851DA115C05DEAF96DA2BCC93CEE3C8773CF52)
