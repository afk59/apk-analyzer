# Applying for Wallet Kit

Before you start integration, make [necessary preparations](../../../getting-prepared/application-development-preparations/document.md) (public key fingerprint included).

1.  Sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) and click **My projects**.
2.  Click the desired project, go to **Project settings** > **Manage open capabilities**, and enable **Wallet Kit** so that the car key management console can send HTTP/HTTPS requests to the HUAWEI Wallet server. When Wallet Kit is disabled, your app server cannot access the HUAWEI Wallet server.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/nFv9zojDSzaSXzQUIEeRbw/en-us_image_0000002218521725.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B959BE182EF5EE71EF98CE7904B85C2171CAFEEECBFDEC4F3697443D30057C56 "Click to enlarge")
    
3.  On the **Project settings** page, go to **Earn** > **Wallet Kit** and click **Apply for Wallet Kit**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/3NQRSOBaTgWm6RFJmNhLqg/en-us_image_0000002182921474.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E80AC41C14AA16A8DE33237AB81A3ADB2954D32D91CFB49F95119691D1ADB6CB "Click to enlarge")
    
4.  Set the Wallet Kit parameters. The parameters may vary depending on the service scenario.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/ua87jUeDSNqHVURpJUS41w/en-us_image_0000002218367285.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA2F1F66EDB47274C69299935A177E1EB1CAC113F82DE18657549B7183C010AC "Click to enlarge")
    
    | 
    Wallet Kit Service Parameter
    
     | 
    
    Value
    
     |
    | :-- | :-- |
    | 
    
    Service Type
    
     | 
    
    Service type, which covers cards, coupons, tickets, and keys. Currently, you can only choose from transportation card and car key.
    
     |
    | 
    
    Service Project
    
     | 
    
    The options available depend on the value selected for **Service Type**. For example, when **Service Type** is set to **card**, the options of **Service Project** include **loyaltycardw**, **OverseaGiftCard**, and **OverseaAllpowerful**.
    
     |
    | 
    
    Service Name
    
     | 
    
    It is used to distinguish one service from another when all services that you have applied for are displayed on the Wallet Kit service list page.
    
     |
    | 
    
    Service ID
    
     | 
    
    It is used by the HUAWEI Wallet server to distinguish one service from another. It must be unique.
    
     |
    | 
    
    Callback address
    
     | 
    
    Address you provide for Wallet Kit to send a callback notification when a user successfully claims or deletes a pass.
    
    If you do not need Wallet Kit to send a callback notification in such scenarios, you can leave this parameter empty.
    
     |
    | 
    
    User public key
    
     | 
    
    The public key will be used by the HUAWEI Wallet server to authenticate your identity. You need to generate a public key using the following method, and copy and paste it here.
    
     |
    
    **How to generate a public key**:
    
    (1) Configure the node execution environment, use the text editor to create a file, copy the following code to the file, and save the file as **generateKeyPair.js**.
    
    const crypto = require('crypto');
    // Generate a key pair.
    const { publicKey, privateKey } = crypto.generateKeyPairSync('rsa', {
      modulusLength: 4096, // Key length, which must be greater than or equal to 4096 characters.
      publicKeyEncoding: {
        type: 'spki', // Public key encoding format.
        format: 'pem' // Public key output format.
      },
      privateKeyEncoding: {
        type: 'pkcs8', // Private key encoding format.
        format: 'pem' // Private key output format.
      }
    });
    console.info('Generated public key:');
    console.info(publicKey);
    console.info('Generated private key:');
    console.info(privateKey);
    
    (2) Open the command-line interface (CLI) and run the **node generateKeyPair.js** command.
    
    (3) Copy the generated public and private keys and save them.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3b/v3/0qrFGGwsRqaPgNZDhn8maQ/en-us_image_0000002183081170.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=79E6B69E71FB8633283BB21427BE54AEE946BB20A52717AB11CC2A9A7F98DCF3 "Click to enlarge")
    
5.  Click **Next**. On the **Configuring NFC Parameters** page, set the NFC parameters. The parameters may vary depending on the service scenario.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/NaPCc__DSX6TE0tBv7sAMg/en-us_image_0000002182921478.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F1A5DB8E961F1E95F8D51E216708022276DC585EEFED725F7C44A04E9165E6FB "Click to enlarge")
    
    | 
    NFC Parameter
    
     | 
    
    Value
    
     |
    | :-- | :-- |
    | 
    
    Whether to support synchronization across mobile devices
    
     | 
    
    Indicates whether users can share the claimed passes across different devices under the same account. Select **NO** by default.
    
     |
    | 
    
    Whether to enable the NFC capability
    
     | 
    
    For keys, all-in-one cards, access cards, transportation cards, health insurance cards, exit-entry permit for traveling to and from Hong Kong (China) and Macao (China), and passports, select **YES** and set **Application ID (AID)** and **File parameter definition**. For other passes, you can select **NO**.
    
     |
    | 
    
    Application ID (AID)
    
     | 
    
    Click **Get AID** to create an app ID. The value is a hexadecimal number with up to 32 digits (recommended: 32 digits). It is recommended that the value start with **A000000048575041590100**.
    
     |
    | 
    
    External authentication key
    
     | 
    
    Key for external authentication during offline pass reading and writing. The value is a hexadecimal number with up to 32 bits (recommended: 32 digits).
    
     |
    | 
    
    File parameter definition
    
     | 
    
    Key information, which is used to control the read and write permissions of a specified file section. The value is a hexadecimal number with up to 32 bits (recommended: 32 digits).
    
     |
    
6.  Click **Next**. On the displayed Wallet Kit service list page, you can view, edit, or delete a service.
