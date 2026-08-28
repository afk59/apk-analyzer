# Configuring a Debug Signature

DevEco Studio provides an [automatic signing](#section18815157237) solution for development and debugging to streamline your debug process. You can also generate a debug signature by [signing your app/atomic service manually](#section297715173233).

In DevEco Studio 6.0.0 Beta3 and earlier versions, automatic signing does not support association with a registered app. Since DevEco Studio 6.0.0 Beta5, the **Associate with registered application** option has been added to the **Signing Configs** tab.

-   Automatic signing for an app associated with a registered app: This applies to apps bound to an app registered in AppGallery Connect, allowing you to enable [open capabilities](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506#section1817619495251) directly in DevEco Studio.
-   Automatic signing for an app not associated with a registered app: This applies to apps not bound to any app in AppGallery Connect. Open capabilities cannot be enabled in DevEco Studio for such apps.

#### Use Cases for Automatic and Manual Signing

-   Automatic signing is applicable only for debugging apps. [Manual signing](#section297715173233) is required in the following debugging scenarios:
    1.  Cross-device debugging, cross-app interaction debugging, debugging without a network connection, or multi-user development with shared keys.
    2.  Debugging that involves permission request approval. For example:
        1.  When the [restricted permissions](../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md) that do not support automatic signing are used. (For details about the ACL permissions that can be requested through automatic signing, see [ACL Permissions Supported by Automatic Signing](#section5301916183411).)
        2.  When the permission requests (such as one-tap sign-in with HUAWEI ID) need to be reviewed by Huawei.
    3.  Debugging that involves fingerprint configuration for kits.
-   Manual signing is also required for release scenarios.

#### Signing Your App/Service Automatically

## Constraints

-   The feature of signing an app associated with a registered app is available only in the Chinese mainland.
-   Automatic signing for atomic services uses the mode "signing an app associated with a registered app in AppGallery Connect." Therefore, atomic services can be automatically signed only in the Chinese mainland.
-   To ensure successful automatic signing, verify that your local system time is synchronized with Beijing Time (UTC/GMT+08:00). Otherwise, signing will fail.

## Automatic Signing for an App Associated with a Registered App

**Procedure**

1.  Connect to a real device or an emulator. For details, see [Running Your App/Atomic Service on a Local Real Device](../running-your-app-on-a-local-real-device/document.md) or [Running Your App/Atomic Service on the Emulator](../running-your-app-on-the-emulator/document.md). The figure below shows the UI when DevEco Studio is connected to a device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/vp-SZHQKROKOUXmsJJmwRA/en-us_image_0000002501720796.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C670CB9154FC4209764A145FA5594DB269ED61FB66238B626079D3372E69F480)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/ZmvNuDU0Ry2W5y4C7vhd9A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=343A740B2AF7708F3E9E9BC1753CB318D37EEF22C81A363A7D5BC6C4BC94A975)
    
    If you use DevEco Studio to automatically sign your app/atomic service, the information about all the connected devices will be written into the certificate.
    
2.  Choose **File** > **Project Structure...** > **Project** > **Signing Configs** and select **Associate with registered application**. If you have not signed in, click **Sign In** first.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/86/v3/Dtjy3ql7S7Kw2oMApNZoMw/en-us_image_0000002501560966.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D295EB23EF40D79D882AB1DC8063739D835E0AA0B3B435F2119727192DACE688 "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/SE6m2zseQYSxTzRc8ILChg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=135A530D87B9535DA18052855268EDC796FDA7591005310F5933B4336A6ED403)
    
    -   You can select a team account from the **Team** drop-down list to switch accounts.
    -   Once signing starts, DevEco Studio searches for apps under the current team in AppGallery Connect that match the bundle name. If a matching app is found in AppGallery Connect, automatic signing proceeds. If no app is found or conflicts are detected, follow the on-screen instructions to make modifications and retry automatic signing. For details, see [FAQs](https://developer.huawei.com/consumer/en/doc/harmonyos-faqs/faqs-signature-service-18).
    
3.  Click **Enable open capabilities** to enable [open capabilities](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506#section1817619495251) in DevEco Studio. Currently, the following open capabilities are supported: [Push Kit](../../application-services/push-kit/about-this-kit/document.md), [DeviceVerify](../../system/security/device-security-kit/deviceverify/document.md), [Map Kit](../../application-services/map-kit/about-this-kit/document.md), and [SafetyDetect](../../system/security/device-security-kit/safetydetect/document.md). You can select any of them as required.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b0/v3/Dn_3IIAaSkmDeymS2QG3CA/en-us_image_0000002533480855.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=850349138918144F1B0E37BE5F6FE72EA81EE632D4AD4548DA3B5B2E59843672)
    
4.  (Optional) Add the ACL permission information to the configuration file. For details about ACL permissions, see [ACL Permissions Supported by Automatic Signing](#section5301916183411).
    
    In the **module.json5** or **config.json** file of the module that requires the permission, add the **requestPermissions** or **reqPermissions** field, including the permission names. The following example shows how to add the **ohos.permission.ACCESS\_DDK\_USB** permission to a project using the stage model.
    
    {
      "module": {
        ...
        "requestPermissions": \[{
          "name": "ohos.permission.ACCESS\_DDK\_USB",
        }\],
        ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/gvVmtBfBRt-FjjQwtya9NA/en-us_image_0000002533360809.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A84E060EA3D8446B3B6219A5FF5C69AF92EDB7B0238F474A8427EDE8F739E508)
    
    Click **OK** after modifying the configuration file. If the permission has been granted to the app in AppGallery Connect, the signing succeeds; if the permission has not been granted, the signing fails. In this case, click **submit a permission request in AppGallery Connect** or **Submit** in the **Notice** dialog box to go to AppGallery Connect to request it. Once granted, return to DevEco Studio and restart the signing process.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/MWsFK9tVSCa94hZoICGw6w/en-us_image_0000002501720798.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3320ECD04911A9DF8E1C6575482395AE710F2A718C4BEA9BF8F01CA07B75015A "Click to enlarge")
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/tXfXXwj5Tk-rbKt2smkIOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2B30BD34489FB20562203DC9A925E911065712921D786569236908E9194F9EF)
    
    -   Precautions:
        -   Restricted permissions are granted only in [special scenarios](../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md). Make sure your use case is among those scenarios before requesting the restricted permissions. For details about how to request these permissions, see [Requesting Restricted Permissions](../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
        -   When submitted for release, apps involving restricted permissions will be reviewed by AppGallery Connect based on the app's use case to determine whether they can use the corresponding restricted permissions. If the requirements are not met, the app will be rejected. For details about the review process, see [Releasing a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-0000002271695230).
    
    -   Profile certificate description:
        -   A temporary profile certificate with a short validity period can be obtained after an ACL permission request is submitted, but before it is approved. This allows the app to be signed. If the request is still not approved when the temporary certificate expires, a new temporary certificate must be requested and obtained again for signing.
        -   Once the ACL permission request is approved, an official profile certificate with a longer validity period can be acquired.
    
5.  After the signing is complete, the keystore file (.p12), certificate signing request file (.csr), digital certificate (.cer), and profile (.p7b) are generated locally. Hover over ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/YIsbgOFDR5GsQY38JjK8GA/en-us_image_0000002513741754.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88B00B85640C86E24122EE0FA92BD520F8B5669524216CA1BFDC874B8E7C1979) next to **Provisioning Profile: DevEco Managed Profile** to view details such as the certificate validity period, bundle name, ACL permissions, and open capabilities. Alternatively, open the project-level **build-profile.json5** file and view the signature information in **signingConfigs**.

## Automatic Signing for an App Not Associated with a Registered App

**Perform the following steps to sign a HarmonyOS project:**

1.  Connect to a real device or the Emulator. For details, see [Running Your App/Atomic Service on a Local Real Device](../running-your-app-on-a-local-real-device/document.md) or [Running Your App/Atomic Service on the Emulator](../running-your-app-on-the-emulator/document.md). The figure below shows the UI when DevEco Studio is connected to a device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/48/v3/Wmt0XL0nTtu-g76_coBucw/en-us_image_0000002501069962.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4329495C50B20DB22DB447D25DF8359F4B5B350A81A51D45CDCE6F5879A0458)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/pxMCeCjTSKKrEbXT_amPug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB54C73EBC86663FDBD3B49E04A47F85B3A4620AF03370A4275F6DE1A7D5DA71)
    
    If you use DevEco Studio to automatically sign your app/atomic service, the information about all the connected devices will be written into the certificate.
    
2.  Choose **File** > **Project Structure...** > **Project** > **Signing Configs** and select **Automatically generate signature**. When prompted, click **Sign In** to log in. Then the system will automatically sign your app/atomic service.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/O4VUMoF7RrSwXMBxJdoEBA/en-us_image_0000002533480857.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4F8AF28C83EC1D38821579ED37B834ED60FE8EB1C6D407CDA58E902B473A5096 "Click to enlarge")
    
3.  (Optional) Add the ACL permission information to the configuration file. For details about ACL permissions, see [ACL Permissions Supported by Automatic Signing](#section5301916183411). After modifying the configuration file, click **OK**.
    
    To declare required permissions, add the **requestPermissions** or **reqPermissions** field in your module's **module.json5** or **config.json** file. Here is an example for adding the **ohos.permission.ACCESS\_DDK\_USB** permission to a stage model project:
    
    {
      "module": {
        ...
        "requestPermissions": \[{
          "name": "ohos.permission.ACCESS\_DDK\_USB",
        }\],
        ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/evq0y8ZJQoqAGybI1UE0rA/en-us_image_0000002501069960.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0514DF983BE9F91C9B92231216469D602837192216C0BBCA2329E91F5131942)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/jAqc9o0SSh-dTPdiTZOutA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9AC49CA14E6F676A79A07586AC9A16B77C279E87026580E0736EAB86BDDF0DEA)
    
    -   Strict validation is not applied to the ACL permissions added in the configuration file during debug signing.
    -   When submitted for release, apps involving restricted permissions will be reviewed by AppGallery Connect based on their use cases to determine whether they can use the corresponding restricted permissions. If an app fails to meet the requirements, its release request will be rejected. Before configuring ACL permissions, ensure your app's use case aligns with the [scenarios for which restricted permissions are granted](../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md). Currently, only a limited number of apps qualifying for specific scenarios may use restricted permissions after approval. For details on how to request, see [Requesting Restricted Permissions](../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
    
4.  After the signing is complete, the keystore file (.p12), certificate signing request file (.csr), digital certificate (.cer), and profile (.p7b) are generated locally. Hover over ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/wTbgR10BRUONWaa5Z6GJug/en-us_image_0000002513901748.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=909A4C217B64CDDBE575654FA49ED9A9C9DF38FED035E904228FAD40026B269A) next to **Provisioning Profile: DevEco Managed Profile** to view details such as the certificate validity period, bundle name, ACL permissions, and open capabilities. Alternatively, open the project-level **build-profile.json5** file and view the signature information in **signingConfigs**.

**Perform the following steps to sign an OpenHarmony project:**

1.  Connect to a real device by following the instructions in [Running Your App on a Local Real Device](../running-your-app-on-a-local-real-device/document.md) or [Running Your App on the Emulator](../running-your-app-on-the-emulator/document.md). The figure below shows the UI when DevEco Studio is successfully connected to a device.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/-TkeFl61T--4KSCNShZIZQ/en-us_image_0000002513901680.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6C6E13238545531CBCBC71E3624B26C6997544C5C3FA5A1773BB750681A0578)
    
2.  Choose **File** > **Project Structure...** > **Project** > **Signing Configs**. If only **Automatically generate signature** is selected, an OpenHarmony signature is generated. If both **Support HarmonyOS** and **Automatically generate signature** are selected, a HarmonyOS signature is generated. If you have not signed in, click **Sign In** first.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/bqXoZ586RESohiS6oNmfWQ/en-us_image_0000002513743292.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F8B296AE013AF5CDCFCD249B645D50CC265C06E9D95FB35CC68747F1B2AF1215 "Click to enlarge")
    
    After the signing is complete, the page shown below is displayed. The keystore file (.p12), certificate signing request file (.csr), digital certificate (.cer), and profile (.p7b) are generated locally. You can view the digital certificate on the **Certificates, App IDs, and Profiles** tab page of AppGallery Connect.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/j1LTB3uvTw-9PFPZ-Q_A-g/en-us_image_0000002545421643.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AE4AE0775E6C95453B26EC5124544E197FAFB744A62AC2F686A6622A81823030)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/8srUV_OORsmj54oqY48RTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=746A29DFAD9E0B2D717EC6A8B38DDC5C39DCB340C13B32D660A2F58C2E4DDB92)
    
    -   You are advised to use the HarmonyOS signature when signing an OpenHarmony project. This is because the OpenHarmony signature is a release signature, and apps signed with a release signature do not support debugging features such as debug log printing. Additionally, using the OpenHarmony signature may affect app execution.
    -   If multiple devices are connected simultaneously during automatic signing, information of all connected devices will be written into the certificate file.
    

#### Signing Your App/Atomic Service Manually

HarmonyOS uses digital certificates (.cer) and profiles (.p7b) to ensure app/atomic service integrity. First, you need to use DevEco Studio or CertificateTool to generate a key (stored in a .p12 keystore file) and a certificate signing request (.csr file). Then, request a debug digital certificate and a profile file. Finally, configure the key (.p12), digital certificate (.cer), and profile (.p7b) files in your project.

**Basic Concepts**

-   **Key**: a public and private key pair saved in a .p12 keystore file, used in asymmetric encryption for digital signature and verification.
-   **Certificate signing request (CSR)**: a .csr file that contains the public key, common name, organization name, and organizational unit in the key pair. It is used to request a digital certificate from AppGallery Connect.
-   **Digital certificate**: a .cer certificate issued by AppGallery Connect.
-   **Profile**: a .p7b file that contains a HarmonyOS app/atomic service's bundle name, digital certificate information, list of certificate permissions that can be requested by the app/atomic service, and list of devices where the app/atomic service can be debugged (if the app/atomic service type is Release, the device list will be empty). Each app/atomic service package must contain a profile.

## Generating a Key and CSR

1.  On the menu bar, choose **Build** > **Generate Key and CSR**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/WYFAqMNQScWmGKKKH1eiVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DE65BB98A936113DF16F6DB4D9FD822A8873ED436FF874B93B924DECEFE19A8)
    
    If you have a local key, click **Skip** in the **Generate Key** window and use the local key to generate a CSR.
    
2.  For **Key store file**, click **Choose Existing** to select an existing .p12 keystore file or **New** to create one. The following describes how to create a keystore file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/w_W6xjNrR3GAKWqh5KXMWQ/en-us_image_0000002501069970.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B360EBEE3F5F82DB5ACC38327186E4646CBFC64D779EFC175450079CF37DDFEF)
    
3.  In the **Create Key Store** dialog box, set the following parameters and click **OK**.
    
    -   **Key store File**: Select the path for storing the keystore and enter the .p12 file name.
    -   **Password**: Set the keystore password, which must contain at least 8 characters that include two types of the following: uppercase letters, lowercase letters, digits, and special characters. Make a note of the password. You will need it when configuring the signature.
    -   **Confirm password**: Enter the keystore password again.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/LCj29LwwS-mWCIC7Fadrsw/en-us_image_0000002532749997.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B670E4565B2B14DB4E1997BE9909F7987B634B28F740E167B34BA1B9044A8C2)
    
4.  On the **Generate Key and CSR** page, set the following parameters and click **Next**.
    
    -   **Alias**: (mandatory) alias of the key. Remember the alias as it will be required for subsequent signing configuration.
    -   **Password**: (mandatory) password of the key, which is automatically filled in and the same as the keystore password.
    
    -   **Validity(years)**: (optional) certificate validity period. A validity period of 25 years or longer is recommended to cover the entire lifecycle of your app/atomic service.
    -   **First and last name**: (optional) common name, which can be the app name or your name.
    -   **Organizational unit**: (optional) organizational unit, which can be the department name or, for individual developers, your name.
    -   **Organization**: (optional) organization name, which can be the full name of your company or your name.
    -   **City or locality**: (optional) city or region.
    -   **State or province**: (optional) state or province.
    -   **Country code(XX)**: (optional) [country/region code](https://developer.huawei.com/consumer/en/doc/app/agc-help-connect-api-appendix-countrycode-0000002236201362).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/ArozV9r6Q8O55iRB51AFkA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D07BFA6055ACFDD78D78757B1AACACDB9BF3D4347A9C5FCD73D841E925FA78E)
    
    The values for **First and last name**, **Organizational unit**, **Organization**, **City or locality**, and **State or province** must be greater than 0 and less than 64 characters in length and must not contain double quotation marks ("), backslashes (\\), or backquotes (\`).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/kXwyQpNmRRCAqLedK8_yaw/en-us_image_0000002501069968.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=811D8B92DA77C4C8E268ACCF3640E00F1A220168DA1D2A53734D2D91366566EA)
    
5.  On the **Generate Key and CSR** page, set the CSR directory, including the file name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/6po3poi4S3yl_Anm6sBgvg/en-us_image_0000002532670063.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7A33191B51A046EE0F0D134059C74D008046F5CCED68710F8026A1BF7378BC4)
    
6.  Click **Finish**. You can then obtain the generated keystore file (.p12), CSR (.csr), and **material** folder (which stores materials related to the signing solution, such as passwords and certificates) from the storage path.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/nxvyBiNIT1ikz3hwteKDwQ/en-us_image_0000002532750001.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E998A5838A702D287F3D0DEADC11FEB516B328D075BB78A04B099D4B623F698)
    

## Requesting a Debug Certificate

Request and download a debug certificate in AppGallery Connect. For details, see [Requesting a Debug Certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-cert-0000002283256797).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/3u2sVXpYSv2aHEUuFpy_Qg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60AC35ADCB0FC8BB8DC75645F1AF2BA9EB1FCCD0C7DF6A02286F8B94F1EA9ECB)

If you haven't registered the app in AppGallery Connect, complete registration before proceeding. For details, see [Creating a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506).

## Requesting a Debug Profile File and Adding Permission Information

1.  (Optional) Request ACL permissions (if required) in AppGallery Connect. Then, add the permission information in the configuration file in DevEco Studio.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/DYEszBIbTperXmxfQM3cWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5133093F23C0B8C74FCF618709A95F5A249932C4BD24FD62898E42989F27EC1D)
    
    -   Requests for ACL permissions are supported only in the Chinese mainland.
    -   If your app requires the use of restricted permissions for special scenarios, request them at this step; otherwise, the app will be rejected during review. For details about the scenarios where the restricted permissions can be used, see [Restricted Permissions](../../system/security/application-access-control/application-permission-management/application-permissions/restricted-permissions/document.md).
    -   Ensure that the information about the scenarios and functionalities you provided for requesting the restricted permissions is accurate. If the usage of restricted permissions within your app exceeds the scope you requested, or the scenarios and functionalities that use the permissions are beyond the scope specified when you requested the permissions, your app's release will be affected.
    
    To declare required permissions, add the **requestPermissions** or **reqPermissions** field in your module's **module.json5** or **config.json** file. Here is an example for adding the **ohos.permission.ACCESS\_DDK\_USB** permission to a stage model project:
    
    {
      "module": {
        ...
        "requestPermissions": \[{
          "name": "ohos.permission.ACCESS\_DDK\_USB",
        }\],
        ...
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/h8deEdVlTtOYDSU4Re4mhw/en-us_image_0000002501069978.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B3A6D51A62D0B88BDCD64009D9739C933C17A3DBD7903FA3660BE72D10FA73D5)
    
2.  Request and download the profile in AppGallery Connect. For details, see [Requesting a Debug Profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278).

## Configuring Signature Information

1.  [Connect DevEco Studio to a real device](../running-your-app-on-a-local-real-device/document.md).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/73/v3/BOU191LkTJOUko5FVyti7A/en-us_image_0000002545625825.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=32CA494EAA1DDE3AC77CA6048551CFAB2BB97324FC335A5664BDEF78A8F2E7DA)
    
2.  Choose **File** > **Project Structure** > **Project** > **Signing Configs**, deselect **Automatically generate signature** and **Associate with registered application**, and configure the key (.p12 file), profile (.p7b file), and digital certificate (.cer file). After the configuration is complete, click **Apply**.
    
    -   **Store file**: Select the .p12 keystore file generated in [Generating a Key and CSR](#section462703710326).
    -   **Store password**: Enter the key store password, which must match the keystore password entered when [generating a key and CSR](#section462703710326).
    -   **Key alias**: Enter the alias of the key, which must match the alias entered when [generating a key and CSR](#section462703710326).
    -   **Key password**: Enter the key password, which must match the store password entered when [generating a key and CSR](#section462703710326).
    -   **Sign alg**: Specify the signing algorithm, which has a fixed value of **SHA256withECDSA**.
    -   **Profile file**: Select the .p7b profile file generated in [Requesting a Debug Profile File and Adding Permission Information](#section89479413571).
    -   **Certpath file**: Select the .cer debug certificate generated in [Requesting a Debug Certificate](#section081822416419).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/hVoazewEQpyoBbH99sDv0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB61C14F2B00146AAE3BF917DF3800DD0E8D0C5A4F2A25367BA48F6725AF5341)
    
    -   The **Store file**, **Profile file**, and **Certpath file** fields support relative paths, starting from the root directory of the project.
    -   The keystore file, keystore password, key alias, key password, profile file, and certificate file must form a matching set to ensure successful signing. If a failure occurs, check the error message, modify your configuration accordingly, and retry the signing process.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/2Tc-QVtqSGe_MvseBPhnWg/en-us_image_0000002501069980.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5EF649032C5F74F448310AE43B20B690EFCA7E1EBDA309046983C579FF96EEDA "Click to enlarge")
    
    After configuration, hover over ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/7JN2Z5B_Raa8X01t4s2NVA/en-us_image_0000002532670047.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5ECCE6FE25B948C239C60FAE9C8E6A0D1EF7D3D68C7E59D1D011A574B5FE15D8) next to **Provisioning Profile: DevEco Manage Profile** to view details such as the certificate validity period, bundle name, common name (enterprise name), ACL permissions, and open capabilities.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/ZarP2W2jQImTszJk_8DOwg/en-us_image_0000002532749995.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E9FB5181DBF476426B9476F376264EDDCE1B344D91141CF6FE7B04C94FA6BAB "Click to enlarge")
    
3.  In the project-level **build-profile.json5** file, review the signature configuration under **signingConfigs**. Click **Run** in the upper-right corner to run the app/atomic service.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/v-hMMzL_SziuAs4-YRvyXw/en-us_image_0000002545537119.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062149Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=690BF080608AE1AA5E02FF6B1B3398AD662C3ABA679A50C87C21833C83AA59A7)
    

#### Appendix

## ACL Permissions Supported by Automatic Signing

The following lists the ACL permissions supported by automatic signing. Once [automatic signing](#section18815157237) is enabled, DevEco Studio verifies that all declared ACL permissions are included in the following list. If validated, it automatically requests the corresponding profile from AppGallery Connect for signing and packaging, eliminating cumbersome manual steps.

**6.0.2 Beta****1**

New permissions

-   ohos.permission.SUBSCRIBE\_NOTIFICATION
-   ohos.permission.ACCESS\_USER\_FULL\_DISK
-   ohos.permission.CUSTOM\_SCREEN\_RECORDING
-   ohos.permission.GET\_IP\_MAC\_INFO

**6.0.1 Release** **(6.0.1.260)**

New permissions

-   ohos.permission.SET\_SYSTEMSHARE\_APPLAUNCHTRUSTLIST
-   ohos.permission.HOOK\_KEY\_EVENT
-   ohos.permission.WEB\_NATIVE\_MESSAGING

**6.0.0 Beta3**

New permissions

-   ohos.permission.CUSTOMIZE\_SAVE\_BUTTON
-   ohos.permission.GET\_ABILITY\_INFO
-   ohos.permission.LINKTURBO
-   ohos.permission.GET\_WIFI\_LOCAL\_MAC
-   ohos.permission.GET\_ETHERNET\_LOCAL\_MAC
-   ohos.permission.USE\_FLOAT\_BALL
-   ohos.permission.READ\_LOCAL\_DEVICE\_NAME
-   ohos.permission.ACCESS\_NET\_TRACE\_INFO
-   ohos.permission.KEEP\_BACKGROUND\_RUNNING\_SYSTEM
-   ohos.permission.atomicService.MANAGE\_STORAGE
-   ohos.permission.MANAGE\_SCREEN\_TIME\_GUARD

**5.1.0 Release**

New permissions

-   ohos.permission.ACCESS\_DDK\_USB\_SERIAL
-   ohos.permission.ACCESS\_DDK\_SCSI\_PERIPHERAL
-   ohos.permission.USE\_FRAUD\_APP\_PICKER

**5.0.5 Release**

New permissions

-   ohos.permission.kernel.DISABLE\_GOTPLT\_RO\_PROTECTION
-   ohos.permission.MANAGE\_APN\_SETTING

**5.0.3 Release**

New permissions

-   ohos.permission.READ\_WRITE\_USB\_DEV
-   ohos.permission.USE\_FRAUD\_CALL\_LOG\_PICKER
-   ohos.permission.USE\_FRAUD\_MESSAGES\_PICKER
-   ohos.permission.ACCESS\_DISK\_PHY\_INFO
-   ohos.permission.SET\_PAC\_URL
-   ohos.permission.PERSONAL\_MANAGE\_RESTRICTIONS
-   ohos.permission.START\_PROVISIONING\_MESSAGE
-   ohos.permission.PRELOAD\_FILE
-   ohos.permission.kernel.ALLOW\_WRITABLE\_CODE\_MEMORY
-   ohos.permission.kernel.DISABLE\_CODE\_MEMORY\_PROTECTION
-   ohos.permission.kernel.ALLOW\_EXECUTABLE\_FORT\_MEMORY
-   ohos.permission.GET\_WIFI\_PEERS\_MAC
-   ohos.permission.READ\_WRITE\_DESKTOP\_DIRECTORY
-   ohos.permission.MANAGE\_PASTEBOARD\_APP\_SHARE\_OPTION
-   ohos.permission.MANAGE\_UDMF\_APP\_SHARE\_OPTION
-   ohos.permission.READ\_WRITE\_USER\_FILE

**5.0.0 Release**

Supported permissions

-   ohos.permission.READ\_CONTACTS
-   ohos.permission.WRITE\_CONTACTS
-   ohos.permission.READ\_AUDIO
-   ohos.permission.WRITE\_AUDIO
-   ohos.permission.READ\_IMAGEVIDEO
-   ohos.permission.READ\_PASTEBOARD
-   ohos.permission.WRITE\_IMAGEVIDEO
-   ohos.permission.ACCESS\_DDK\_USB
-   ohos.permission.ACCESS\_DDK\_HID
-   ohos.permission.SYSTEM\_FLOAT\_WINDOW
-   ohos.permission.FILE\_ACCESS\_PERSIST
-   ohos.permission.INPUT\_MONITORING
-   ohos.permission.INTERCEPT\_INPUT\_EVENT
-   ohos.permission.SHORT\_TERM\_WRITE\_IMAGEVIDEO
