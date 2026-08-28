# Enabling Push Kit

Before enabling Push Kit, create a project and an app by referring to [Application Development Preparations](../../../../getting-prepared/application-development-preparations/document.md).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/bVZQ0cUuQZacTvGTE0_C0w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A35E3F251E8D6FE0D4B952DB808C79693CED4E275BEB959B7AF9A396C1FEE11D)

Since HarmonyOS NEXT Developer Beta2, you no longer need to configure the public key fingerprint and client ID.

#### Procedure

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/kv9GjxA1Tmm_T--Kr63Eww/en-us_image_0000002402225641.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4968E6997D27C637A382FBDDEA79F78B00A031C229EAEE070D4C4B93B504F0F "Click to enlarge")
    
2.  Find and click the desired project in the project list, and click the app for which you need to set Push Kit parameters.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/3salS5RjQ1WPee7inApP6g/en-us_image_0000002368546048.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D9048BEBF639FE4662B45C4C07169E6E03757B334E13F8A97E5E4D8AE5292E7B "Click to enlarge")
    
3.  Go to **Grow** > **Push Kit** and click **Enable now**. In the dialog box that is displayed, click **OK**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/0eybzjQ_SkCqjz3Nn8idlQ/en-us_image_0000002402305797.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=126879E85D48887C49C658F8ED9DE4802175305B5DA8E6667D5E78A694A8D74D "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/h4SjDDu0Spq-N7xxo_pPjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=62B33C40A71C720144173860B293F828CF1A79E5E9438E0AAAF855C9FC7001B7)
    
    Push Kit is enabled at the project level. If you have enabled Push Kit earlier for a project, the kit is available for all apps in this project, including those added later.
    
4.  If you have not set a data processing location, click **OK** in the dialog box displayed. Then set the data processing location as prompted and click **OK**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/koo6b_R4Rc6S-pVjaOadVA/en-us_image_0000002368705944.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F45D4C847BBA5FCCB279043E710E76C33F1A25909F903CCC363444C90B5E8F6 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/DA9cmS7OSL-rbs8RPN7PtA/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D1A9EED5FC92740A6A9E346CCB6D179F503A2EB07B31EFFA5920AAE21FA2F5F)
    
    For details about the countries/regions where Push Kit is supported on wearables, please refer to [Supported Countries/Regions](../../appendixes/supported-countries-regions/document.md). You can set the data processing location based on the supported countries/regions. For other devices, Push Kit is available only in the Chinese mainland, and the data processing location is fixed to China.
    
5.  Sign your app in either of the following ways during debugging. Note that, in development and debugging scenarios, DevEco Studio 6.0.0 Beta5 and later versions provide a more efficient automatic signing solution for you to choose.
    
    -   Manual signing: During app debugging, you **must** apply for a debug certificate, [register a debug device](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-device-0000002283189937), enable Push Kit under **Grow** > **Push Kit**, apply for a **new** debug profile file, and complete [manual signing](../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233) for your app.
    -   Automatic signing (new): In DevEco Studio, click **Enable open capabilities**. In the **Permission Management** dialog box that is displayed, select **Push Kit** and click **OK**. Then DevEco Studio will automatically sign your app. For details, please refer to [Signing Your App/Service Automatically](../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section18815157237).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/5t-PUZ6aR32dsYJu0W4BJw/en-us_image_0000002441281984.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F4DACACE6C7FE12A7C44CBEA30B9ECC7EE8212C0ED8C8B024F606D48679839C "Click to enlarge")
        
        Wait for 5 to 10 minutes, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), and go to **Project settings** > **Manage open capabilities**. You will find that Push Kit has been selected. At the same time, Push Kit is also automatically enabled under **Grow** > **Push Kit**.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/dlkXh63-QaqnMaqkV3CdCg/en-us_image_0000002539415667.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=651ED3744E170A888948CACBFA61B1DD8FC97347C7BFB6DA0CCC8907151E2C13 "Click to enlarge")
        
    
6.  During app release, apply for a release certificate, ensure that Push Kit is enabled under **Grow** > **Push Kit**, apply for a new release profile file, and complete manual signing. For details about app signing for app release, please refer to [Configuring Signature Information](../../../../app-release/release/document.md#section280162182818).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/SWeudy_3R4aQ0vrJaRA2KQ/en-us_image_0000002539414419.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0568F33EA6F32693812ACB719DFF27B166280E91A26CC9F80FED09751C394085 "Click to enlarge")
    
7.  Go to **Grow** > **Push Kit** > **Settings**. Select the desired app for which you need to apply for the self-classification permission, and click **Apply** next to **Self-classification**. For details, please refer to the [application procedure](../applying-for-scenario-specific-message-permissions/document.md#section16708911111611).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/PbdWKf3fR-WJDh1x5VBzMw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F54DE4684D6E1E640ABD3948BDF98ADCD6229018878EA5F33658C3E019B0ED5)
    
    You are advised to apply for the **self-classification permission** and send notifications by category. **Otherwise, Push Kit classifies these messages as news and marketing messages by default.** In this case, your app is subject to the restriction that it can push up to **2** or **5** messages to each device on a daily basis.
    
8.  (Optional) Enable or disable the [message receipt](../../device-cloud-debugging/optional-developing-the-message-receipt/document.md) function at the project and app levels on the **Settings** page.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/CrshehPRQsaI_ttoPd3TyA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDFD2B0EAC1FC787C07B300EAD33EC64CB41570C4B611D399980503DABCF530D)
    
    -   If the message receipt has been enabled at the project level but not for a specific app, this app will use the project-level message receipt.
    -   If the message receipt has been enabled at the project level and also for a specific app, this app will use the message receipt enabled for itself.
    

#### (Optional) Setting the Data Processing Location

To set or change the data processing location, perform the following steps:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/o2fg5hLQSFqWvntKloDiYw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1E46AABCAFD1D1138EAF654CFF0CB985EC4E4B491C3F665332BF23C3888DA37)

If the data processing location is different from your server location, or is different from the location of a user that the app serves, push messages will fail to be sent.

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
2.  Click the project for which you want to set the data processing location.
3.  Go to **Project settings** > **Data processing location**, and click **Edit**.
4.  Set a data processing location as required.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/KIbg81IATV-3kucSfbqtfw/en-us_image_0000002472644830.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DB45B9165582134DD657096B6FA12A5DA7A77B9D4E931BEC7CA1119336B70B19 "Click to enlarge")
    
5.  Click **Save**.
