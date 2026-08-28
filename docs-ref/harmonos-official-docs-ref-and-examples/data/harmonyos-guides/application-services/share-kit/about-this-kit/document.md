# About This Kit

Share Kit provides cross-app and cross-device sharing of text, images, and videos.

To share content to another app or device through Share Kit, an app needs to send configuration about the content to be shared and its preview style to Share Kit. Share Kit then processes the sharing request based on the scenario:

-   If the content is to be shared to another app, Share Kit constructs a sharing panel based on the shared data type and quantity of shared items to provide users with content preview, recommended sharing contacts, associated apps, and relevant operations. Users can quickly select the target app to share content or choose the desired operation.
-   If the content is to be shared to another device, Share Kit constructs a preview page based on the shared data type and quantity of shared items for cross-device sharing.

To receive the shared content, the target app needs to be displayed on the sharing panel. You need to develop the data processing ability and declare it in the target app's configuration file based on the configuration requirements. Social apps can provide contact information through the API of [Intents Kit](../../../ai/intents-kit/about-this-kit/document.md) so that a user can share content to a specified contact.

The [Sample Code](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts) provided by Share Kit showcases the integration mode, examples of text/image sharing, example of Tap to Transfer, and widget templates. You can refer to the sample code to develop your app.

**Figure 1** Sharing panel on a phone

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/mN60IuklQJqVOZ5w6ME9eA/en-us_image_0000002513409519.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=307ADE12533A3E625BC3A4701509B0534B5F84129767E1C95ECDC2D602DABF4E "Click to enlarge")

**Figure 2** Tap to Transfer through Huawei Share across phones

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/48ud-gWaRMO3zvR8Mu0WKw/en-us_image_0000002481169682.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=41FAF3F6773AA89204CBE50F405CC411FC11F453D8684D7659999481BC7A70DB "Click to enlarge")

**Figure 3** Tap to Transfer between a phone and a PC/2-in-1 device

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/oM92KfWUT1-nbmg7OPWGIQ/en-us_image_0000002481329646.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=43E70C00B7BF2BC58B8266D89FB560E0FFC2312BE8BFE986801C0F9A0F34CF0A "Click to enlarge")

#### Basic Concepts

-   Host app
    
    App that initiates the sharing. The host app calls the sharing API to configure information such as the content to be shared and preview style and displays the sharing panel.
    
-   Target app
    
    App that receives the shared content. You need to develop the data processing ability in the target app and declare the ability according to the target app integration guide, so that the package management service can identify the ability supported by the app.
    
-   Content area
    
    Displays the title, preview, and selection of the shared content.
    
-   Recommendation area
    
    Integrates Share Kit and [Intents Kit](../../../ai/intents-kit/about-this-kit/document.md) and uses algorithms to efficiently and accurately recommend devices and target app users that can process the shared content.
    
-   Sharing mode area
    
    Obtains target apps that support the shared content through the package management service of HarmonyOS. The following redirection methods are supported:
    
    1\. Redirects to the **UIAbility** component in the target app.
    
    2\. Redirects to the **ExtensionAbility** component provided by the target app (hereinafter referred to as the sharing details page).
    
    The target app developer needs to configure the description of the **UIAbility** and **ExtensionAbility** components in the [module.json5 configuration file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) to declare the supported types of shared data.
    
-   Operation area
    
    Provides content-related operations, such as copying, saving, saving as, and printing.
    

#### Mechanism

**Figure 4** Mechanism of content sharing

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/ob3eHVMBRWeoySeIjmVqmw/en-us_image_0000002481169686.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4A8AC87A6F17CEB1030FD93635108F160071A1EA58BE1A76E70E5D0D3BB6E05 "Click to enlarge")

| 
App Type

 | 

Logic

 |
| :-- | :-- |
| 

Host app

 | 

You need to provide a sharing entry for the content to be shared in the host app. When a user taps **Share**, the host app needs to send configuration about the shared content to Share Kit and starts the sharing panel.

-   [Initiating Content Sharing Through the Sharing Panel](../system-share/content-sharing-initiation-by-a-host-app/initiating-content-sharing-through-the-sharing-panel/document.md)
-   [Tap to Transfer](../tap-to-transfer/document.md)

 |
| 

Target app

 | 

1.  You need to develop a data processing component in the target app. The following sharing methods are available:
    -   [Processing the Shared Content Inside a Target App](../system-share/shared-content-processing-by-a-target-app/processing-the-shared-content-inside-a-target-app/document.md)
    -   [Processing the Shared Content on the Sharing Details Page](../system-share/shared-content-processing-by-a-target-app/processing-the-shared-content-on-the-sharing-details-page/document.md)
2.  (Optional) Social apps can provide contact information in recent sharings to [Intents Kit](../../../ai/intents-kit/about-this-kit/document.md) based on the [Intents Kit](../../../ai/intents-kit/about-this-kit/document.md) integration specifications. Share Kit obtains recommendation information from [Intents Kit](../../../ai/intents-kit/about-this-kit/document.md). When a user selects a recommended contact, Share Kit sends the contact information to the target app together with the shared content. The target app then directly sends the content to the specified user based on the contact information.

 |

#### Restrictions

-   Restrictions on devices
    
    | 
    Capability
    
     | 
    
    Device Type
    
     |
    | :-- | :-- |
    | 
    
    Phone
    
     | 
    
    Tablet
    
     | 
    
    PC/2-in-1 Device
    
     | 
    
    TV
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    System Share
    
     | 
    
    Supported
    
     | 
    
    Supported
    
     | 
    
    Supported
    
     | 
    
    Partially supported (Only sharing to nearby devices is supported. System operations and sharing to other apps are not supported.)
    
     |
    | 
    
    Tap to Transfer
    
     | 
    
    Supported
    
     | 
    
    Not supported
    
     | 
    
    Supported
    
     | 
    
    Not supported
    
     |
    | 
    
    Grab & drop
    
     | 
    
    Supported
    
     | 
    
    Supported
    
     | 
    
    Supported
    
     | 
    
    Not supported
    
     |
    
-   Restrictions on usage
    -   The data types defined by the host app and target app must comply with the Uniform Type Descriptor ([UTD](../../../application-framework/arkdata/unified-data-definition/utds-arkts/document.md)) specifications provided by the Unified Data Management Framework ([UDMF](../../../application-framework/arkdata/unified-data-definition/unified-data-definition-overview/document.md)). The supported content types must be configured in the target app configuration file. If all image types are supported, declare **general.image**.
    -   The total size of the [description about shared data](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-system-share#section816451553012) configured in the host app cannot exceed 200 KB, and the total number of shared items cannot exceed 500.

#### Emulator Support

Share Kit supports the Emulator, but there are some differences in feature support between real devices and the Emulator.
