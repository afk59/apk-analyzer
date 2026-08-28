# Applying for Integrating Wear Engine

Before applying for Wear Engine, set up the development environment, and complete basic preparations such as creating a project and creating a HarmonyOS app, by referring to [Application Development Preparations](../../../../../../getting-prepared/application-development-preparations/document.md). Then proceed with the following development steps.

1.  Visit HUAWEI Developers, click **Console**, and then the **Wear Engine** card under **[Application service](https://developer.huawei.com/consumer/en/console/service/AppService)**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/XpI9zApdQIa9dlryrh_TTA/en-us_image_0000002155206400.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43898E53D1D724A991C1C581D3C8C61FB7AB72012F9C2E05A04AE0E6A3005BC5 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/vs8-V1c6QqedemGhwls_Rw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A95C1A4E3AAE37419924DCE3B7F2DF744E1EEB996511A9190A34B0AAEFEC6CB)
    
    If the **Wear Engine** card cannot be found, click **Customize console** in the upper right corner to add it.
    

2.  Click **Applying for the Wear Engine Service** and agree to the agreement. The screen for data permission application will then be displayed.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/OH1Z2UtWRDCl4y3Pm0dDjg/en-us_image_0000002155046640.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67B6EF64F6CCB0F3BB022159D822F3CF4C215D08D5618DE39B89FF728611C292 "Click to enlarge")
    
3.  Select **HarmonyOS App**, select a product, and select the required permissions. (Individual developers can only apply for basic device information and message notification permissions.)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/AxhgjF2xQ6a36Twu-xAYjA/en-us_image_0000002190453289.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C09A4152EC77B27CA283B6F90F8E70B3E4EF7361ECD59349341D18AE9F6704EF)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/S64wuLfrS2q0lBqCDpo7aw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=384AC39BCE3E25F0EE7BC98414A7AA86AA9C1C825F44B271347CD1E0747863C5)
    
    -   If your phone app needs to be compatible with phone apps that communicate with an older version of the wearable app, set the **compatible app name** and **compatible app package name** fields. Ensure that the app belongs to the same account as the current app.
    -   Human body sensor-related permissions are restricted and open for use by professional research institutions only. Do not apply for the permission unless you have confirmed with Huawei in advance.
    -   The device identifier permission is restricted and only open for use by professional partner research institutions. Do not apply for the permission unless you have confirmed with Huawei in advance.
    
    **Permissions and device capabilities**:
    
    **Basic device information** (permission)
    
    -   Wearable device status management
        -   Basic wearable information query: obtains the list of paired wearable devices, from which a user can select a target device, and supports querying available storage space on the selected device.
        -   Basic wearable status query: supports querying the battery level, subscribing to low-battery alerts, and querying or subscribing to the connection status, device mode, and charging status of a wearable device.
    -   Communications management
        -   Sending point-to-point messages/files: A phone app _XXX_ (app name) sends messages or files to a wearable app _XXX_ (app name).
        -   Receiving point-to-point messages/files: A phone app _XXX_ (app name) receives messages or files from a wearable app _XXX_ (app name).
    
    **Message notification** (permission)
    
    -   Message notification management
        -   Sending notifications to a wearable device: A phone app sends notifications to a wearable device, which are displayed using predefined templates. The notification title, content, and buttons can be customized.
    
    **Wearable user status [USER\_STATUS](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section09971113566)** (permission)
    
    -   Wearable device user status management
        -   Queries and subscribes to the user's wearing status, and subscribes to heart rate alerts.
    
    **Human body sensor [HEALTH\_SENSOR](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section09971113566)** (permission)
    
    -   Human body sensor
        -   Obtains the list of sensors on a wearable device.
        -   Reads ECG, PPG, and HR sensor data from a wearable device.
        -   Stops reading human body sensor data from a wearable device.
    
    **Motion sensor [MOTION\_SENSOR](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section09971113566)** (permission)
    
    -   Motion sensor
        -   Obtains the list of sensors on a wearable device.
        -   Reads ACC, GYRO, and MAG sensor data from a wearable device.
        -   Stops reading motion sensor data from a wearable device.
    
    **Device identifier [DEVICE\_IDENTIFIER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section09971113566)** (permission)
    
    -   Device identifier
        -   Obtains the serial number of a connected wearable device.
    
4.  Upload the data permission and data usage description, as well as the user authorization path description. Select whether to show the HUAWEI logo on the authorization screen, and then submit the application.
    
    **Data permission and usage description**
    
    -   Permission: Provide each requested data permission on a separate line.
    -   Data usage: Provide the requirements, scenarios, purposes, and methods of using the data permission.
    -   Data display path: Provide screenshots of the scenarios where you are going to use the permissions (optional).
    
    **User authorization path description**
    
    -   Provide screenshots of the user authorization screen and describe how users can access the screen.
    -   If your app allows users to modify the granted permissions, provide screenshots of the authorization modification screen and describe how users can access the screen (optional).
    
5.  Wait for approval.
    
    The approval process may take one to two weeks, depending on the requested permission types and the app release regions.
    
    An application won't be approved if the submitted materials do not meet the requirements. Once the application is approved, you can start to develop your app, and release your app once the development is complete.
    
    If your business scope changes and you need to modify the corresponding data permissions, click **Modify** and submit the application again.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/KrvH04CqRAGc_Cnudu_-LQ/en-us_image_0000002190567621.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32D418AEAF72D7112D3F021342D27E34AEFD17341028C2DAB6319546F47CCBBB "Click to enlarge")
