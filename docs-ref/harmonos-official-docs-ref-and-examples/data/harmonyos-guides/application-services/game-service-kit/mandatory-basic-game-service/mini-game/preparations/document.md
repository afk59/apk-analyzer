# Preparations

#### Creating a Mini Game

To release a mini game on AppGallery, you need to create an atomic service of the mini game type in AppGallery Connect. Relevant parameters need to be set as follows:

-   **App type**: Select **Atomic service**.
-   **Level-1 app category**: Select **Mini game**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Ro6hb8VwRWm7Vir_Fp_zLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30D1211D428C5E8689ED06D0E5F2B57F8E5ED2CDB94F4611F7A91DB924AA1D90)

It is recommended that the name of the game package for official release not contain words such as **test** and **dev**.

#### Applying for Identity Verification by the National Press and Publication Administration

According to the _Notice by the National Press and Publication Administration of Further Imposing Strict Administrative Measures to Prevent Minors from Becoming Addicted to Online Games_, all game publishing and operating enterprises were required to complete interconnection with the [online game anti-addiction identity verification system](https://wlc.nppa.gov.cn/fcm_company/index.html#/login?redirect=/) before June 1, 2021, with **bizID** (game record filing identification code) obtained. A game's **bizID** needs to be configured in AppGallery Connect for Huawei to connect to the National Press and Publication Administration's identity verification system and enable mandatory identity verification. No additional development is required from developers.

#### Applying for Filing

Refer to the [App Filing FAQs](https://developer.huawei.com/consumer/cn/doc/App/50130#h2-1710150107897-0), [Quick Game Development](https://developer.huawei.com/consumer/cn/doc/quickApp-Guides/quickgame-filing-guide-0000001806139508), and [Filing for Mini Games Developed Within China](https://developer.huawei.com/consumer/cn/doc/games-guides/quickgame-filing-chinese-preparation-0000001979934858) to complete the mini game filing, and ensure that the filing information is stored properly.

#### Applying for the JSVM Permission and Storage Space Management Open Capabilities

To release a mini game, you must apply for the JSVM permission and storage space management open capabilities.

#### Generating a Signing Certificate

The signature information, including the digital certificate and profile, can ensure the integrity of your mini game.

-   Debugging phase: [Sign your app manually](../../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233), [request a debug certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-cert-0000002283256797), and [request a debug profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-debug-profile-0000002248181278).
-   Release phase: [Sign your app manually](../../../../../coding-and-debugging/configuring-a-debug-signature/document.md#section297715173233), [request a release certificate](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-cert-0000002283336729), and [request a release profile](https://developer.huawei.com/consumer/en/doc/app/agc-help-release-profile-0000002248341090).

#### Configuring a Signing Certificate Fingerprint

AppGallery Connect automatically generates a public key for the certificate and calculates the SHA-256 fingerprint. You need to obtain and configure the SHA-256 fingerprint in AppGallery Connect. Each game can have a maximum of four signing certificate fingerprints. For details, please refer to [Configuring a Public Key Fingerprint](https://developer.huawei.com/consumer/en/doc/app/agc-help-cert-fingerprint-0000002278002933).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/om0-D-suSW-R69EIbhrUbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCDAAD1E6C210C475E3B4F2C413EDB3EA1C77C58AB7CD53CC45B77DDAFA26472)

Add the fingerprint of the debug certificate in the debugging phase and add the fingerprint of the release certificate in the release phase.

#### Configuring the App ID, Client ID, and Permissions

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), choose **Development and services**, select your project and mini game, and obtain the app ID and client ID under **App information**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/31UpwzSoSTiHo-_rhV1RsA/en-us_image_0000002474311100.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE726E35E993F4DBAA76BD2CECF5A9D7B4E6265D323B13A07DA2C403B750BE86)
    
2.  In the **module.json5** file of the **entry** module in the project, add **metadata**, configure **client\_id** and **app\_id** in **metadata**, and add **requestPermissions** to configure the ACL permission and open capabilities. The sample code is as follows:
    
    "module": {
      "name": "entry",
      "type": "xxx",
      "description": "xxxx",
      "mainElement": "xxxx",
      "deviceTypes": \[\],
      "pages": "xxxx",
      "abilities": \[\],
      "metadata": \[ // Configure the following information:
        {
          "name": "client\_id",
          "value": "xxxxxx" // Set it to the client ID obtained in the preceding step.
        },
        {
          "name": "app\_id",
          "value": "xxxxxx" // Set it to the app ID obtained in the preceding step.
        }
      \],
      "requestPermissions": \[ // Configure the JSVM permission and storage space management open capabilities.
        {
          "name": "ohos.permission.kernel.ALLOW\_EXECUTABLE\_FORT\_MEMORY"
        },
        {
          "name": "ohos.permission.atomicService.MANAGE\_STORAGE"
        }
      \]
    }
    

#### Configuring the App ID Mapping

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), choose **Development and services**, select your project and mini game, choose **Build** > **Game Service** from the navigation pane on the left, and click **New Configuration**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/uwL6I4RHQlGvMWeyvrNZMQ/en-us_image_0000002506391133.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7B33522B871572699FAA52270D153481634F6280D54EAE27DEAED39989D9A96)
    
2.  In the **Adding configuration information** dialog box, set the parameters and click **Next step**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/UJeiyiaRTEGTEs_yPa8XMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4053B08DF5B3E48DDBD47D8EEC643F8184A9285B2E97650844FB0EDB775FF427)
    
    Ensure that the mapping between the game (in HAP format) and the quick game (in RPK format) is correctly configured. If you select a game of an incorrect type, you will be prompted to reselect a correct game.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/8T7qI1gkQdqs6cXeNjHGyw/en-us_image_0000002474151176.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F5CD6F551EBD618CF3A7D1B22523A311B213357F2FD3BA9E170AEAE5F9629D9)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    HarmonyOS 5.0 and above game
    
     | 
    
    Select the mini game (in HAP format) to be released.
    
     |
    | 
    
    HarmonyOS 4 and below game
    
     | 
    
    Select the corresponding quick game (in RPK format) that has been released or is in draft state.
    
     |
    
3.  (Optional) Enter the callback address of your server and click **OK** to submit the app ID mapping for approval.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/7rvxE7PgQE64IlMzFmD1wg/en-us_image_0000002474151172.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4627C242C5BB2990368BD618974CEAC017F64B60FCDE34B29A007CFC1720A678)
    
4.  Any exceptions (for example, the release status does not meet the requirements) will be indicated in red text in the dialog box shown below. You are advised to click **Cancel** and reconfigure the app ID mapping. If you ignore the exceptions and click **OK** to continue submitting, your app ID mapping configuration may be rejected.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/qB5zXYjwT1-gcAA9g5afaA/en-us_image_0000002506391131.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0AB95901948235B1A749913920016DFF4C3F71C01ACF3A761019873CC8CC9C98)
    
5.  After you submit your request, it will take 1–3 working days for Huawei staff to complete the review. If you want to reconfigure the app ID mapping after it has taken effect, submit a request for deleting the mapping first.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/1ZNR6-TuSAapFnlUwqz4ig/en-us_image_0000002506391137.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AC5C0C9BB7A2D68CC3085C317CA88F2E98B9C096435078A9136E1E7EA1D5EC00)
    
    The review result of the app ID mapping configuration or deletion request will be sent to you through the interaction center or email.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/u8yew_mZSd685Zsjgh15mA/en-us_image_0000002474311098.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062104Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C322F136BAE0FEABA578E50A18351EEAB845192CAAECF4A6882F276C805D2BC2)
