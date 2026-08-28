# Sharing Links

#### Sharing a Link of App Linking to Go to a Specified In-app Page

When an app is shared through a link of App Linking, the target user can tap the link on the target device to directly go to the specified in-app page. For details, please refer to [Using App Linking for App-to-App Redirection](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5f/v3/I42kk_kOT5S-iVU9w7fZdg/en-us_image_0000002513289551.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062121Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=30961086A8AA45B1F1F0D8C1EB12AA5AF89E58F9DFE9D8DF64D15B8E89667F95 "Click to enlarge")

## Development Procedure

1.  Enable the App Linking service, complete relevant configuration, and test a link of App Linking. For details about how to perform the test, please refer to [Testing a Link of App Linking](https://developer.huawei.com/consumer/en/doc/AppGallery-connect-Guides/agc-applinking-debug-0000001059139667).
2.  Add the association configuration to the [skills](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills) section in the app configuration file (**src/main/module.json5**). For details, please refer to [Configuring a Website Domain Name](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section1101111611317).
3.  Use App Linking to initiate a system sharing request.
    
    import { systemShare } from '@kit.ShareKit';
    import { uniformTypeDescriptor as utd } from '@kit.ArkData';
    import { common } from '@kit.AbilityKit';
    import { image } from '@kit.ImageKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Component
    export default struct Index {
      private async share() {
        // Generate an app icon thumbnail.
        let uiContext: UIContext = this.getUIContext();
        let contextFaker: Context = uiContext.getHostContext() as Context;
        let thumbnailPath = contextFaker.filesDir + '/exampleImage.jpg'; // This is only an example. Replace it with the correct file path.
        let imageSource: image.ImageSource = image.createImageSource(thumbnailPath);
        let imagePacker: image.ImagePacker = image.createImagePacker();
        let buffer: ArrayBuffer = await imagePacker.packToData(imageSource, {
          // The value of **format** can only be **image/jpeg**, **image/webp**, or **image/png**.
          format: 'image/jpeg',
          // Quality of the output image in JPEG encoding. The value ranges from 0 to 100.
          // You are advised to compress the image to a reasonable size. An oversized image will fail to be shared.
          quality: 30
        });
        // Construct **ShareData**. You need to configure a valid data record.
        let shareData: systemShare.SharedData = new systemShare.SharedData({
          utd: utd.UniformDataType.HYPERLINK,
          // The link of App Linking is only an example.
          content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
          title: 'App name', // If this parameter is not passed, the link will be displayed.
          description: 'App description', // If this parameter is not passed, the description will not be displayed.
          thumbnail: new Uint8Array(buffer) // You are advised to pass the app icon. If no app icon is passed, the default HTML icon will be displayed.
        });
        // Display the sharing panel.
        let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
        let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
        controller.show(context, {
          previewMode: systemShare.SharePreviewMode.DEFAULT,
          selectionMode: systemShare.SelectionMode.SINGLE
        }).then(() => {
          console.info('ShareController show success.');
        }).catch((error: BusinessError) => {
          console.error(\`ShareController show error. code: ${error.code}, message: ${error.message}\`);
        });
      }
    
      build() {
        Button('Share')
          .onClick(() => this.share())
      }
    }
    
4.  The target app processes the link of App Linking. For details, please refer to [Implementing App Redirection Required for the Caller App](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup#section93961521541).
    
    import { common, OpenLinkOptions } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    @Entry
    @Component
    struct Index {
      build() {
        Button('start link', { type: ButtonType.Capsule, stateEffect: true })
          .width('87%')
          .height('5%')
          .margin({ bottom: '12vp' })
          .onClick(() => {
            let uiContext: UIContext = this.getUIContext();
            let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
            let link: string = "https://www.example.com/programs?action=showall";
            let openLinkOptions: OpenLinkOptions = {
              appLinkingOnly: false
            };
            context.openLink(link, openLinkOptions)
              .then(() => {
                console.info('openlink success.');
              })
              .catch((error: BusinessError) => {
                console.error(\`openlink failed. code: ${error.code}, message: ${error.message}\`);
              });
          })
      }
    }
    
    For details about the complete sample code, please refer to [Sample Code - Sharing a Link of App Linking to Go to a Specified In-app Page](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/AppLinkingScenario.ets).
    

#### Sharing a Common Link to Be Opened Using a Browser

Common link sharing can link a web page to a target device or app.

-   When receiving the link, the target device will open the link using the browser.
-   When receiving the link, the target app can conveniently process the link content. For example, a user can share a link with a MeeTime friend.

## Development Procedure

1.  Import required modules.
    
    import { systemShare } from '@kit.ShareKit';
    import { uniformTypeDescriptor as utd } from '@kit.ArkData';
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Construct the data to be shared.
    
    // Construct **ShareData**. You need to configure a valid data record.
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.HYPERLINK,
      content: 'https://www.vmall.com/index.html?cid=128688', // This is only an example. Replace it with your link to be shared.
      title: 'VMALL',
      description: 'Huawei phone',
      // thumbnail: new Uint8Array() // You are advised to pass a suitable thumbnail. If no thumbnail is passed, the default HTML icon will be displayed.
    });
    
3.  Add a record.
    
    shareData.addRecord({
      utd: utd.UniformDataType.HYPERLINK,
      content: 'https://www.vmall.com/index.html?cid=128688', // This is only an example. Replace it with your link to be shared.
      title: 'Test URL',
      description: 'Test description',
    });
    
4.  Start the sharing panel.
    
    // Display the sharing panel.
    let controller: systemShare.ShareController = new systemShare.ShareController(shareData);
    let uiContext: UIContext = this.getUIContext();
    let context: common.UIAbilityContext = uiContext.getHostContext() as common.UIAbilityContext;
    controller.show(context, {
      selectionMode: systemShare.SelectionMode.SINGLE,
      previewMode: systemShare.SharePreviewMode.DEFAULT,
    }).then(() => {
      console.info('ShareController show success.');
    }).catch((error: BusinessError) => {
      console.error(\`ShareController show error. code: ${error.code}, message: ${error.message}\`);
    });
    
    For details about the complete sample code, please refer to [Sample Code - Sharing a Common Link to Be Opened Using a Browser](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/scenario/LinkScenario.ets).
