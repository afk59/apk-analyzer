# Enabling a Car Key

To enable a car key, a user needs to add a car key and activate it. The following figure shows the entire interaction process. For details about the relevant APIs, please refer to [ArkTS API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-arkts).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/11/v3/Rjz_tBmlRguSfQzWw63PWg/en-us_image_0000002182921494.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C4091444C89F3CE3B0A29B6A1123363953314CAC7AA7D56943BEE8D0E424527)

1.  The car owner app calls the [queryPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section375194074718) API to check whether the car key is enabled on the device.
2.  If the [queryPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section375194074718) API returns [1010220501 No Card Found](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-error-code#section5732174019224), the car owner app calls the [canAddPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section20458166124611) API to check whether the device supports adding the specific car key.
3.  If the [queryPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section375194074718) or [canAddPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section20458166124611) API returns [1010200003 Environment of HUAWEI Wallet Is Not Ready](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-error-code#section205478194408), the car owner app calls the [initWalletEnvironment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section139341726154718) API to initialize HUAWEI Wallet and prompt the user to agree to the agreement for car key enabling or sign in to their account.
4.  The car owner app calls the [queryPassDeviceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section5251175451917) API to query the device type and specify the target device ID to enhance security.
5.  After presetting the template, the car owner app server applies for a key card and JWE data. For details, please refer to [Conducting Development for the Car Owner App Server](#section5585115171117).
6.  When a user initiates a card enabling request, the user is redirected to HUAWEI Wallet and the [addPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section596313613472) API carrying the encoded JWE data generated in the preceding step is called to enable the car key in HUAWEI Wallet.
7.  During card activation, the HUAWEI Wallet server needs to interact with the DK management service to authenticate the device (exchange certificate information with the car key management console), obtain the token for requesting applet personal data from the car key management console, request applet personal data, and write data to the data security chipset. For details, please refer to [Activating the Card on the Car Owner App Server](#section19676155018507).
8.  The car owner app can call the [viewPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section18261142114710) API to show the car key details page to the user in HUAWEI Wallet.

#### Development Procedure

1.  Make the car owner app call the [queryPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section375194074718) API to check whether a car key is enabled on the device based on the service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md) and the unique pass ID defined in [Applying for a Key Card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = '';
    // Unique pass ID defined in [Applying for a Key Card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
    private serialNumber: string = ''; 
    
    async queryPass() {
      let passStr = JSON.stringify({
        passType: this.passType,
        serialNumber: this.serialNumber
      });
      this.walletPassClient.queryPass(passStr).then((result: string) => {
        console.info(\`Succeeded in querying pass, result: ${result}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to query pass, code:${err.code}, message:${err.message}\`);
      })
    }
    
2.  If the [queryPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section375194074718) API returns [1010220501 No Card Found](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-error-code#section5732174019224), make the car owner app call the [canAddPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section20458166124611) API to check whether the device supports adding the specific car key.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = ''; 
    // Target device type. The value **phone** indicates mobile phone.
    private targetDeviceType: string = ''; 
    
    async canAddPass() {
      let passStr = JSON.stringify({
        passType: this.passType,
        targetDeviceType: this.targetDeviceType
      });
      this.walletPassClient.canAddPass(passStr).then((result: string) => {
        console.info(\`Succeeded in checking addPass, result:${result}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to check addPass, code:${err.code}, message:${err.message}\`);
      })
    }
    
3.  If the [queryPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section375194074718) or [canAddPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section20458166124611) API returns [1010200003 Environment of HUAWEI Wallet Is Not Ready](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-error-code#section205478194408), make the car owner app call the [initWalletEnvironment](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section139341726154718) API to initialize HUAWEI Wallet and prompt the user to agree to the agreement for car key enabling or sign in to their account.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // Target device type. The value **phone** indicates mobile phone.
    private targetDeviceType: string = ''; 
    
    async initWalletEnvironment() {
      let passStr = JSON.stringify({
        targetDeviceType: this.targetDeviceType
      });
      this.walletPassClient.initWalletEnvironment(passStr).then(() => {
        console.info(\`Succeeded in initiating walletEnvironment\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to initiate walletEnvironment, code:${err.code}, message:${err.message}\`);
      })
    }
    
4.  Make the car owner app call the [queryPassDeviceInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section5251175451917) API to query the device type and specify the target device ID.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = ''; 
    // Target device type. The value **phone** indicates mobile phone.
    private targetDeviceType: string = ''; 
    
    async queryPassDeviceInfo() {
      let passStr = JSON.stringify({
        passType: this.passType,
        targetDeviceType: this.targetDeviceType
      });
      this.walletPassClient.queryPassDeviceInfo(passStr).then((result: string) => {
        console.info(\`Succeeded in querying passDeviceInfo, result:${result}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to query passDeviceInfo, code:${err.code}, message:${err.message}\`);
      })
    }
    
5.  Make the car owner app server apply for a key card and JWE data after presetting the template. For details, please refer to [Conducting Development for the Car Owner App Server](#section5585115171117).
6.  When a user initiates a card enabling request, the user is redirected to HUAWEI Wallet and the [addPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section596313613472) API carrying the encoded JWE data generated in the preceding step is called to enable the car key in HUAWEI Wallet.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // JWE data generated by referring to [Conducting Development for the Car Owner App Server](#section5585115171117).
    private jweContent: string = ''; 
    
    async addPass() {
      let passStr = JSON.stringify({
        jweContent: this.jweContent
      });
      this.walletPassClient.addPass(passStr).then((result: string) => {
        console.info(\`Succeeded in adding pass, result:${result}\`);
      }).catch((err: BusinessError) => {
        console.error(\`Failed to add pass, code:${err.code}, message:${err.message}\`);
      })
    }
    
7.  During card activation, make the HUAWEI Wallet server interact with the DK management service to authenticate the device (exchange certificate information with the car key management console), obtain the token for requesting applet personal data from the car key management console, request applet personal data, and write data to the data security chipset. For details, please refer to [Activating the Card on the Car Owner App Server](#section19676155018507).
8.  Make the car owner app call the [viewPass](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-walletpass#section18261142114710) API to show the car key details page to the user in HUAWEI Wallet.
    
    import { common } from '@kit.AbilityKit';
    import { walletPass } from '@kit.WalletKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    private walletPassClient: walletPass.WalletPassClient = new walletPass.WalletPassClient(this.getUIContext().getHostContext() as common.UIAbilityContext);
    // Service ID registered in [Applying for Wallet Kit](../../applying-for-wallet-kit/document.md).
    private passType: string = '';  
    // Unique pass ID defined in [Applying for a Key Card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
    private serialNumber: string = '';  
    
    async viewPass() {
      let passStr = JSON.stringify({
        passType: this.passType,
        serialNumber: this.serialNumber
      });
      try {
        await this.walletPassClient.viewPass(passStr);
        console.info(\`Succeeded in viewing pass\`);
      } catch (err) {
        console.error(\`Failed to view pass, code:${err.code}, message:${err.message}\`);
      }
    }
    

#### Conducting Development for the Car Owner App Server

1.  Download the sample code for [Wallet Kit - Card Enabling on the Server](https://gitee.com/harmonyos_samples/wallet-kit-sample-code-severdemo-java) and open the code using Intellij IDEA. If you do not have Intellij IDEA, download its latest version first. The directory structure of the sample code is as follows. Pay attention to the files enclosed in red boxes.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/B_AhLO_tTLWYTTOMOjErbQ/en-us_image_0000002182921482.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC58CE41F4425B5EB1EB3A954858A6B34E306747ECE8BAA0DF06342F44596EB9)
    
2.  Open the **resources/release.config.properties** file and set the parameters based on the actual app data.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/tn2O106CSUOnLHBSf2gP7w/en-us_image_0000002218367281.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37439FDEFE82288EBA369F48A24E7088C1A18ACC83994F18FB6B8BC5FCFF8AFD)
    
    | 
    Parameter
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    gw.appid
    
     | 
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/81oY29AWQ5e_ST5LyEJNjg/en-us_image_0000002183081166.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE02F0715336CF19214F72F95C570AB6F5199EC40F0870EBF7CDF2D3EB5A6375 "Click to enlarge")
    
    Set **gw.appid** and **gw.appid.secret** to the values of **Client ID** and **Client Secret** obtained in [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html) respectively.
    
     |
    | 
    
    gw.appid.secret
    
     |
    | 
    
    walletServerBaseUrl
    
     | 
    
    Set it to **https://wallet-passentrust-drcn.cloud.huawei.com.cn/hmspass**.
    
     |
    | 
    
    servicePrivateKey
    
     | 
    
    Set it to the private key generated in step 4 of [4](../../applying-for-wallet-kit/document.md#li69221528123212).
    
     |
    
3.  Open the **resources/data/StdCarKeyModel.json** file and set the parameters based on the actual app data. For details, please refer to the request parameters in [Preset Templates](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section37263211548).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/1SsZOMWqQuye1c_idB-LJw/en-us_image_0000002218367301.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0E0370B681AE2E13A3AEEF196B22E2FA3A902EF3128ACD8A1ADBEF8A53C8538)
    
4.  Open the **stdcarkey/StdCarKeyModelTest.java** file and execute the **createStdCarKeyModel** method. The following information is displayed on the console. For details, please refer to the response parameters in [Preset Templates](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section37263211548).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/3netM19zQESah49LiD_Tmg/en-us_image_0000002218521737.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A9D6CC49D8EA55207486DEE293AA05082D737498CFE36151E90A1910C35699E1 "Click to enlarge")
    
5.  Open the **resources/data/StdCarKeyInstance.json** file and set the parameters based on the actual app data. For details, please refer to the request parameters in [Applying for a Key Card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
6.  Open the **stdcarkey/StdCarKeyInstanceTest.java** file and execute the **addStdCarKeyInstance** method. The following information is displayed on the console. For details, please refer to the response parameters in [Applying for a Key Card](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-carkey#section129511211195).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/7NbXGOrgSpmcw2mntGUGSg/en-us_image_0000002183081158.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E73BAABEA70CAC198BBA6DF3863F7BF03B47C2EADEDAAD49C9568C3DF7D33E5 "Click to enlarge")
    

#### Activating the Card on the Car Owner App Server

1.  Download the sample code for [Wallet Kit - Card Activation on the Server](https://gitee.com/harmonyos_samples/wallet-kit-sample-code-severdemo-nfc-java) and open the code using Intellij IDEA. Complete the project configuration, and set **SERVER\_PUBLIC\_KEY** and **SERVER\_SECRET\_KEY** in the **Constants** class to the public key and private key generated in step 4 of [4](../../applying-for-wallet-kit/document.md#li69221528123212) respectively. Open the **PassesController** class.
2.  Use the **register** method in the **PassesController** class to authenticate the device. For details, please refer to [Device Authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-public#section113578586311).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/XDoOktv0SQCPxG_EpVEHBg/en-us_image_0000002218521733.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89527823AC57649CD5D56D30B278B0C2F016E297A941D09705FC130C77C36E4B "Click to enlarge")
    
3.  Use the **requestToken** method in the **PassesController** class to obtain the personal data token. For details, please refer to [Obtaining a Personal Data Token](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-public#section257714144308).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/NauC5Qc9Q2SwzPRwPyKVpA/en-us_image_0000002183081178.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EFA1612F7434282F924A78603181CA915C3B24398613A1E9DC6DB6FCA9C33EDE "Click to enlarge")
    
4.  Use the **getPersonalInfo** method in the **PassesController** class to obtain personal data. For details, please refer to [Obtaining Personal Data](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wallet-rest-api-public#section178319716389). Focus on the **getDevicePassData** method in **dealWithPersonalizeDataRequest** and the **generatePassData** method in **ICCECarKeyDevicePassUnit**. Generate data according to the API description of the **getPersonalizeData** method.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/bSqPAeYjTYO1rwCkTnMLJQ/en-us_image_0000002218521741.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACCB53FDE804F0ED3484817173CCDF97E35204417E596770C499B8055C5BE1F0 "Click to enlarge")
