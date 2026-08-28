# What should I do if the debug signature configuration is abnormal?

#### The error message "Bundle name \*\*\* does not exist." is displayed.

**Possible Causes**

The uploaded application or atomic service does not exist in AppGallery Connect. As a result, the verification fails.

**Solution**

Method 1:

1.  In the error message dialog box, click **Add App ID**. In the displayed DevEco Studio window, add basic information of the application or atomic service, and click **OK**.
    
    -   **Project**: project name. You can input a new project name or select an existing project from the drop-down list.
    -   **App type**: application type, which is HarmonyOS application or atomic service.
    -   **App name**: application name displayed on the details page in Huawei AppGallery.
    -   **App package name**: application bundle name. This field is mandatory only when **App type** is the HarmonyOS application. The field value must be the same as the bundle name of the project and cannot be changed.
    -   **App category**: application category.
    
    For details about the requirements on the application or atomic service name and bundle name, see [Procedure](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506#section1772711713288), [Creating an Atomic Service](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-atomic-service-0000002247795706).
    
2.  After the application or atomic service is added, sign it.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/c1LX9VjDTnG8EtU3Sx949g/en-us_image_0000002428044174.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11DCD49EA4F9F8CD8C8391F840B5D480B6BC4EC40F1C247B0B1F14300B75C953 "Click to enlarge")

Method 2:

1.  Go to AppGallery Connect and create an application or atomic service. The bundle name must be the same as that of the application created in DevEco Studio. For details about the creation process, see [Procedure](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506#section1772711713288), [Creating an Atomic Service](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-atomic-service-0000002247795706).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/TOHH66CCQXGMhOsLTShqvQ/en-us_image_0000002461722685.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE19517B730C0250F76F4D2E0B2A94D29BCF6D5E090EE86B83F4F2C9BED90B2F "Click to enlarge")
    
2.  After the creation is complete, return to the DevEco Studio page and sign it again.

#### The error message "Bundle name \*\*\* is already in use. Choose a different name, or use the team account that owns it." is displayed.

**Possible Causes**

Scenario 1: The application name and its bundle name must be unique in the Huawei AppGallery. But the bundle name of the application to create is used by another application.

Scenario 2: The application name is used by another team.

**Solution**

Method 1: Change the bundle name. Follow the instructions to add the application and sign it.

Method 2:

1.  Join the target team. For details, see [Adding a Member Account](https://developer.huawei.com/consumer/en/doc/app/agc-help-manageaccount-0000002306610129#section151241455193313).
2.  After joining the team, change **Team** to the target team.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/IgrgRstCSKyn3aXJN5-tpQ/en-us_image_0000002428203990.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92D49AF22278EF8DDAA324A6FB70B498C19AD7DBA7BAF1EA86FA3349718F31F9 "Click to enlarge")
    

#### The error message "Failed to find the capabilities.Check the following configurations: Networkconnection,HTTP Proxy,etc." is displayed.

**Possible Causes and Solution**

Scenario 1: The network connectivity is abnormal. Check and configure the network before signing. For details about how to configure the network, see [Setting Up the Proxy](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-environment-config#section10369436568).

Scenario 2: The application does not have the open capability management and ACL settings. You need to create the application again and then sign it. To check the settings and create an application, perform the following operations.

1.  Go to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/) and click **Development and services**, and select the project to which the application belongs.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/rvla-xLFSo-aQM2L1iRIHQ/en-us_image_0000002440458356.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062622Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=650BEE3D7AE61B0FBCC311F3EDA72AB84C28D67ABD975B3A0C6D72A91BB9F0BF "Click to enlarge")
    
2.  Select the application and check the open capability management and ACL settings. If these settings do not exist, re-create a HarmonyOS application and add an app ID. For details, see **Creating an App ID for a HarmonyOS App**.

**Reference**

[Procedure](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506#section1772711713288)

#### The message "Failed to verify the bundle name. Check your network connection or try again after configuring a proxy." is displayed.

**Possible Causes and Solution**

Scenario 1: The network connectivity is abnormal. Check and configure the network before signing. For details about how to configure the network, see [Setting Up the Proxy](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/ide-environment-config#section10369436568).

Scenario 2: Log out of DevEco Studio, log in again, and then sign it.
