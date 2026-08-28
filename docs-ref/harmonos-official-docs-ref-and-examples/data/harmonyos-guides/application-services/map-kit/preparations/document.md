# Preparations

[Enable Map Kit](#section16133115441516) first, make [necessary preparations](../../../getting-prepared/application-development-preparations/document.md), and then proceed with the subsequent development activities.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/9rvyE83FRX-TxXj_iPKYGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5F1E6E8762B0A9065B0D741FAEACC58A849E1DC77D28DBEE3BC94FDDDC1BDF7)

-   Starting from HarmonyOS 5.0.2(14), you do not need to configure the public key fingerprint and client ID.
-   You can enable Map Kit via DevEco Studio 6.0.0 Beta5 or later versions.

#### Enabling Map Kit

Map Kit can be enabled:

-   Via DevEco Studio
-   In AppGallery Connect

Method 1: Enabling Map Kit via DevEco Studio

1.  Sign in to DevEco Studio.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/14/v3/ShMZth02QSiOGh0VS68baA/en-us_image_0000002485160148.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CE44073A162BF43BD2DCC6DC6CD8AF70906F36709C37820C14ED99CEAB1BAEF)
    
2.  Choose **File** > **Project Structure**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/hwRctSOLTw2EjZszP1uyzg/en-us_image_0000002517200113.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C20C8E88079163635F3FB50A01EEBBF8C5291C09339CFBA441C2067932AFFD65)
    
3.  On the **Signing Configs** page, click **Enable open capabilities**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/pr79940ES7OB6NJhcI3gaw/en-us_image_0000002485160156.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=527D8EED9BA26A8A0971FEE88197E4F3520C9028E1856B0525EB8F2625FC678D "Click to enlarge")
    
4.  Select **Map Kit** and click **OK**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/p1YkQvmUTHyt6QtRmRvjNg/en-us_image_0000002517280091.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6214496CC625423CF2782FC763378D6E9F725A8A1CC4CA7ED5E5A036E0C3070A "Click to enlarge")
    
5.  Click **Apply** to apply the Map Kit configuration and then click **OK**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/zU0OanCeTFeqV1_5bb-gcg/en-us_image_0000002485000182.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EC33E73857E2E762DA9BFF1F343549508E534EB13269C3899D84C5A5D31E9519 "Click to enlarge")
    

Method 2: Enabling Map Kit in AppGallery Connect

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **Development and services**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ae/v3/MOHnuLZKTJavf9dPZTkf8w/en-us_image_0000002517280103.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76524BA1CB33B6BDB45C9FE3CD93E02ACE053B47D447EE2645E51DE205A0F837 "Click to enlarge")
    
2.  Find your project and click the app for which you want to enable Map Kit.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/nZxyFEdbQze33P7ctKJl7g/en-us_image_0000002485160154.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8408017F411E62CE35BA6B36C2C9D9B3D1A9111A294BB391090578CCA37D6722 "Click to enlarge")
    
3.  Go to the **Manage open capabilities** page, select **Map Kit** and click **Save**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/A_Kr8ZhQTcaE8w9WneAnCQ/en-us_image_0000002485160160.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BC9355A2B4B7552675317FE9CB6B895F62172A7144DCD400AC38C36C9A3ADCE1 "Click to enlarge")
    
4.  Complete signing after Map Kit is enabled.
    -   During app debugging, you must [request a debug certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-debugcert-0000001914263178), [register a device](https://developer.huawei.com/consumer/en/doc/app/agc-help-add-device-0000002283189937), [request a new debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278) after Map Kit is enabled, and [sign your app manually](../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233).
    -   During app release, you must [request a release certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-cert-0000002283336729), [request a new release profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090) after Map Kit is enabled, and [configure signature information](../../../app-release/release/document.md#section280162182818).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/88/v3/bb1Hqv4uRA2BB6MDS9IZGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062111Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CD4E59FEB2ED055F9E20FBDB2FEB830FBB705E076A9ACA6DB08428CE9377496)
        
        If you want to use the original profile, ensure that Map Kit has been enabled before you request this profile.
