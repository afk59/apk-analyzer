# Enabling Cloud Storage

You need to enable Cloud Storage before using it. If you have enabled it, skip this step.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
2.  Click the project for which you need to enable Cloud Storage.
3.  Go to **Serverless** > **Cloud Storage**. On the **Cloud Storage** page, click **Enable now**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/3Cxd1_3WQ1mjxbZkZc8b8A/en-us_image_0000002522848223.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CAD35CD67D0158B29E39C7256E3ECBAFB3ED903D425279D9DCD7F40843EA824)
    
4.  On the page displayed, set **Storage instance** and **Default data processing location**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/um36hhIgSXuXOgqVDdVSoQ/en-us_image_0000002474174501.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B103633E9601C8EC3E577017A849D436ACF2BD6C479155BCAAD082721CDB5580)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    Storage instance
    
     | 
    
    Storage instance name, which must:
    
    -   Contain only lowercase letters, digits, and hyphens (-).
    -   Start and end with a digit or letter.
    -   Contain 3 to 57 characters.
    -   Not be an IP address.
    -   Not contain two or more consecutive hyphens (-).
    -   Be globally unique and cannot be changed after being created.
    
     |
    | 
    
    Default data processing location
    
     | 
    
    Currently, you can [enable multiple data processing locations](https://developer.huawei.com/consumer/en/doc/app/agc-help-data-location-0000002277923065#section154810363471) for Cloud Storage. You do not need to set this parameter if you have already set a data processing location for the project.
    
     |
    
5.  Click **Next** and view the default security rule.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/97/v3/AJ8suDsaRkO9aFPSHnVEaw/en-us_image_0000002440774516.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6D7B2997764B4EF0941C09AE752D22A68FF410EC7B7D43A2B74B9AC02FFC1313)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/Ra3I2xLRQyatLUjDdSp5oQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FB8AB62E328AFE88C494D77032E336F0AFF8C77C67AD884F8B1485D873B0C745)
    
    The default security rule allows authenticated users to perform all read and write operations. The security rule cannot be modified when you enable the service. After enabling the service, you can design a more appropriate [security rule](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-cloudstorage-securityrules-overview-0000001054966859) to protect your user data.
    
6.  Click **Finish**.
    
    After the service is enabled, AppGallery Connect will create a default storage instance for you, and its name is in the format _Storage instance name configured in step [4](#en-us_topic_0000001275330014_li191317012303)_\-_Five random digits and letters_, for example, **bucket001-2wezr**.
    
7.  If you have enabled multiple data processing locations, you can switch among these locations to facilitate management.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/A-HO5SC5QNCZ9_PKDPrtPw/en-us_image_0000002517637939.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062101Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BFDA167D2ED56673AA62809A863FA3C6CFD87645BCDB3182C19E9481254013A2)
