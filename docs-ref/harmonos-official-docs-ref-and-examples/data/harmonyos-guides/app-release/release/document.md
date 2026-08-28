# Release

HarmonyOS uses signature information such as the digital certificate and profile to ensure app/atomic service integrity. If your app/atomic service needs to be released in AppGallery Connect, it must pass signature verification. Therefore, you need to use the release certificate and release profile to sign the app/atomic service before releasing it.

#### Release Process

To release your app/atomic service to AppGallery Connect, package your app/atomic service into an App Pack (.app file). The process is shown below.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/Vn5YdyFETZWx2x_bI2s6rg/en-us_image_0000002532750607.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3A3C2FD426F61CADC2B15F2A593FD6E5FCE2A9BD5116C41D49F4F615943C1E8)

Read on to find out more about the process.

#### Preparing Signature Files

HarmonyOS uses digital certificates (.cer) and profiles (.p7b) to ensure app/atomic service integrity. Before requesting a digital certificate and a profile, you need to use DevEco Studio to generate a keystore file (in .p12 format) and a CSR file (in .csr format).

**Basic Concepts**

-   **Key**: classified into the public keys and private keys used in asymmetric encryption and stored in the keystore file in .p12 format. The public and private key pairs are used for digital signature and verification.
-   **Certificate signing request (CSR)**: contains the public key, public name, organization name, and organization unit in the key pair. It is used to apply for a digital certificate from AppGallery Connect.
-   **Digital certificate**: a .cer certificate issued by AppGallery Connect.
-   **Profile**: a .p7b file that contains a HarmonyOS app/atomic service's bundle name, digital certificate information, list of certificate permissions that can be requested by the app/atomic service, and list of devices where the app/atomic service can be debugged (if the app/atomic service type is Release, the device list will be empty). Each app/atomic service package must contain a profile.

## Generating a Key Store and CSR

1.  On the menu bar, choose **Build** > **Generate Key and CSR**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/47eWLq8ISeO9JGXQuoY5XQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4F476A62F69CC36179FDA83B0D43E714966E3B920B0DBD9047F2F1C60618FF9)
    
    If you have a local key, click **Skip** in the **Generate Key** window and use the local key to generate a CSR file.
    
2.  In **Key Store File**, click **Choose Existing** to select an existing key store (.p12 file that contains a key) or **New** to create one. The following describes how to create a key store.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/-ohIa9pyTW6wOWiaKomHMQ/en-us_image_0000002501070588.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAF12C892A6C670F3D2CC4D8B3BE274F2C3C15E590383AEBF4831125B31241B6 "Click to enlarge")
    
3.  In the **Create Key Store** dialog box, set the following parameters and click **OK**.
    
    -   **Key Store File**: Select the path for storing the key store and enter the .p12 file name.
    -   **Password**: Set the key store password, which must contain at least 8 characters that include two types of the following: uppercase letters, lowercase letters, digits, and special characters. Do not lose the password as it will be used later in configuring the signature.
    -   **Confirm Password**: Enter the key store password again.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/m6fif_vnRlCVBKpRn8Jr8Q/en-us_image_0000002501070586.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CDD5D26AF524B5F88CC774F4933272078D91155B2B49F4A81F39129BB0D334C "Click to enlarge")
    
4.  On the **Generate Key and CSR** page, set the following parameters and click **Next**.
    
    -   **Alias**: (mandatory) alias of the key. Do not lose the alias as it will be used later in configuring the signature.
    -   **Password**: (mandatory) password of the key, which is automatically filled in and the same as the keystore password.
    -   **Validity(years)**: (optional) certificate validity period. A validity period of 25 years or longer is recommended to cover the entire lifecycle of your app/atomic service.
    -   **First and last name**: (optional) common name, which can be the app name or your name. The value must be greater than 0 and less than 64 characters in length, and cannot contain double quotation marks ("), backslashes (\\), or backquotes (\`).
    -   **Organizational unit**: (optional) organizational unit, which can be the department name or, for individual developers, your name. The value must be greater than 0 and less than 64 characters in length, and cannot contain double quotation marks ("), backslashes (\\), or backquotes (\`).
    -   **Organization**: (optional) organization name, which can be the full name of your company or your name. The value must be greater than 0 and less than 64 characters in length, and cannot contain double quotation marks ("), backslashes (\\), or backquotes (\`).
    -   **City or locality**: (optional) city or region. The value must be greater than 0 and less than 64 characters in length, and cannot contain double quotation marks ("), backslashes (\\), or backquotes (\`).
    -   **State or province**: (optional) state or province. The value must be greater than 0 and less than 64 characters in length, and must not contain double quotation marks ("), backslashes (\\), or backquotes (\`).
    -   **Country code(XX)**: (optional) [country/region code](https://developer.huawei.com/consumer/en/doc/app/agc-help-connect-api-appendix-countrycode-0000002236201362).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/QJoVOteQQqi85WSZc01LRQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C33A6F0F1A402C01622580D9757FF68861FB0316150134BF416E972A381A6782)
    
    The values for **First and last name**, **Organizational unit**, **Organization**, **City or locality**, and **State or province** must be greater than 0 and less than 64 characters in length and must not contain double quotation marks ("), backslashes (\\), or backquotes (\`).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/B5MmNPzcQJ2n7WFyC7VoRg/en-us_image_0000002501070590.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43F692FE373F00D77D8F9F3799496DA0A0E09F4F8B8894AAE05464CB0EB29D7B)
    
5.  On the **Generate Key and CSR** page, set the CSR directory, including the file name.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/UwcIFJ_VSlKIDQmUbSOAGQ/en-us_image_0000002500910744.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AFA877F2B28D12698A13ACC109AAE816F098003CFB754CF93E4DBB63DDC966A3 "Click to enlarge")
    
6.  Click **OK**. You can then obtain the generated keystore file (.p12) and CSR file (.csr) from the storage path.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/PYndB-3bTTSiD4JPiOhs4Q/en-us_image_0000002532670657.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC5093718035F3EB99CD50E62B1457326F9C379941DE56A1631C8560FF387BF2)
    

## Requesting a Release Certificate and a Release Profile

1.  Create a HarmonyOS app or atomic service in AppGallery Connect. For details, see [Creating a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506) and [Creating an Atomic Service](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-atomic-service-0000002247795706).
2.  Request a release certificate and a profile and download them in AppGallery Connect. For details, see [Requesting a Release Certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-cert-0000002283336729) and [Requesting a Release Profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090).
3.  With the obtained release certificate and profile, sign your app in DevEco Studio as instructed in [Configuring Signature Information](#section280162182818).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0f/v3/FsvM7ZDuSCiEH8Z26G8VCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F76B67626CF133FA88ADE35B002A82FB742AD7C91EFB0126B9F281CDEFA29DE)
    
    -   If you are requesting a release certificate and profile for an atomic service, set **FA** to **Yes** on the **New app** page.
    -   The release certificate and profile are for manual signing to package an app for release, but cannot be used to run or debug a project.
    

#### Configuring Signature Information

With the keystore file (.p12), certificate file (.cer), and profile file (.p7b) – the latter two files are obtained from AppGallery Connect, you can start configuring the signature information for your app/atomic service in DevEco Studio.

Choose **File** > **Project Structure** > **Project** > **Signing Configs** > **default**, and deselect **Automatically generate signature** and **Associate with registered application**.

Configure the paths to the key (.p12), profile (.p7b), and digital certificate (.cer) files.

-   **Store File**: Select a key store file in .p12 format.
-   **Store Password**: Enter the key store password.
-   **Key Alias**: Enter the alias of the key.
-   **Key Password**: Enter the password of the key.
-   **Sign Alg**: Specify the signing algorithm, which has a fixed value of **SHA256withECDSA**.
-   **Profile File**: Select the obtained release profile in .p7b format.
-   **Certpath File**: Select the obtained release certificate in .cer format.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/qhmy2pYxT66v3ut8ad9mkA/en-us_image_0000002500910746.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4853BAE9EA439AE5537DDDF6021F8D193A27BA6EA9D62EB30A9E7DCA0179C95 "Click to enlarge")

After setting the signature information, click **OK** to save the settings. Then build your app as instructed in [Building the App](#section1992513343374).

#### (Conditionally Mandatory) Updating to a Public Key Fingerprint

If your app needs to use one or more of the following open capabilities, you must update its fingerprint to match the release certificate fingerprint in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html#/) before releasing the app. For details, see [Configuring a Public Key Fingerprint](https://developer.huawei.com/consumer/en/doc/app/agc-help-cert-fingerprint-0000002278002933).

-   Account Kit
-   Game Service Kit
-   Health Service Kit
-   IAP Kit
-   Map Kit
-   Payment Kit
-   Wallet Kit

#### Building the App

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/0KZF-RTRRWCTNZCxN1Moww/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8920F482A809E7FBF9D849CD2B63A4B65966793D753F272F80ADAFA03A6EF042)

For an app to be released, the app package type must be **Release**.

Before packaging, make sure your project directory does not contain any unwanted HAPs. Once packaging starts, DevEco Studio will pack all HAPs in your project directory into an App Pack.

1.  Choose **Build** > **Build Hap(s)/APP(s)** > **Build APP(s)** and wait until the process is complete.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/uekUuy6xTBeoBLOLB6cgEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=831D243F809442D5DD616046CD36F13A5E958647635766234835F4027AFF43A9)
    
    The default [Build Mode](../../building-an-app/customizing-your-build/customizing-build-options/introduction/document.md#section192461528194916) is **release** for an App Pack and **debug** for a HAP/HSP/HAR package.
    
    That is, when **Build APP(s)** is selected, the App Pack is of the **release** type by default.
    
2.  Choose **build** > **outputs** > **app** > **release** in the project directory to obtain the digitally signed App Pack.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1a/v3/S6rrCcwgTQyFvRwEEnnt-Q/en-us_image_0000002532750609.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=129B1543062722C6EBF1EE4213004BCD9D59045F9C019DB7801C28719EF1BD0C)
    

#### Uploading an App Package

Since DevEco Studio 5.0.5.200, you can upload an app package in DevEco Studio after you have [created the app](https://developer.huawei.com/consumer/en/doc/app/agc-help-create-app-0000002247955506).

## Constraints

-   Currently, this feature is available only in the Chinese mainland.
-   This feature will upload your app package to AppGallery Connect. To keep your information safe, do not upload any sensitive personal data (including passwords, source code, private keys, debug installation packages, and service logs).
-   This feature is only available for apps in the release build mode. Ensure that a release signature has been configured for the app package.
-   You can also [upload app packages via AppGallery Connect](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-upload-pkg-0000002277983368).

## Procedure

1.  On the menu bar, choose **Build** > **Upload Product**. If you have not signed in to DevEco Studio, click **Sign in** to sign in with your Huawei developer account.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/oMN-CSSkS0apeOQzVtgQbg/en-us_image_0000002532670659.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5FE7C3CE3FC9165EE1CE341C76686FC669A800FF608207596485B2A5332EAE0 "Click to enlarge")
    
2.  When you are back to the app package upload page in DevEco Studio after a successful sign-in, verify the product information, select the type of the app package to upload, and click **OK**.
    
    -   If the app package to upload is used only for test purposes, select **Generate app package and upload it to AppGallery Connect for test**.
    -   If the app package to upload is used for official release, select **Generate app package and upload it to AppGallery Connect for test and publish**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/YdEQcvU6SVCok94tPMLybg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E517FF5387281AF611ED4D2D521DBED1A812278DBC39E89F62181AC33650C555)
    
    -   To upload a symbol table, select **Upload your app's symbols**.
    -   You can click the ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/BroDPvL9Q3e2kB8ZDaHfzA/en-us_image_0000002500910748.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79422A4824AFAA44661100F60048D8DDD39FC2B966CB7E12351301377AAE0A69) icon in the upper-right corner of the editing area to view and switch the uploaded product.
    -   To change the bundle name and version number of the app package, modify the **bundleName** and **versionName** fields in the **app.json5** file. The bundle name must be the one that has been registered on AppGallery, actually exists, and belongs to your current developer account.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/4KaSERsHShG4O0OIXei0BQ/en-us_image_0000002532670655.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1A112B4F11D2152A49EC0392376F5E0FCE0388A591D88BC4F7B096CC262C7FEA)
    
3.  After the upload is complete, the cloud test result is displayed. Click **View Full Result in AppGallery Connect** to view the upload record and test result in AppGallery Connect. For details, see [Uploading Your Package](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-upload-pkg-0000002277983368). To close the upload page, click **Close**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/hEBfFP29QHiUhg_hwHgwTQ/en-us_image_0000002532750611.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062159Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=23FF312A3CE2C349EA4EBE8AB8B8DCACA9F1CA861D9A09AFF528FA69C3D9D656)
    

#### Releasing an .app File to AppGallery

Release the app/atomic service package (.app file) on AppGallery. For details, see [Releasing a HarmonyOS App](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-app-0000002271695230) or [Releasing an Atomic Service](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-atomic-0000002327731065).
