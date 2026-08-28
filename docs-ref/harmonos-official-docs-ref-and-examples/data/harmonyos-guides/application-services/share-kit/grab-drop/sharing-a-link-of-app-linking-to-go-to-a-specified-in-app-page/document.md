# Sharing a Link of App Linking to Go to a Specified In-app Page

This section describes how to develop the function of going to a specified in-app page through Grab & drop. Your host app must integrate App Linking to deliver a smooth end-to-end user experience. For details, please refer to [Using App Linking for App-to-App Redirection](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup).

#### Precautions

1.  When a user accesses a page with a shareable item, use the [harmonyShare.on('gesturesShare')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-harmony-share#section79507713161) method to register a Grab & drop event listener.
2.  When a user leaves a page with a shareable item (including the scenario where **the user switches the app to the background**), use the [harmonyShare.off('gesturesShare')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-harmony-share#section3951197151616) method to unregister the Grab & drop event listener.

#### Development Procedure

1.  Import required modules.
    
    import { uniformTypeDescriptor as utd } from '@kit.ArkData';
    import { systemShare, harmonyShare } from '@kit.ShareKit';
    import { fileUri } from '@kit.CoreFileKit';
    
2.  Define the methods for registering and unregistering a Grab & drop event listener. (When receiving a Grab & drop event callback, it is advised to call the [sharableTarget.share()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-harmony-share#section1862171812120) method to initiate sharing within 3 seconds. Otherwise, the sharing may fail.)
    
    private immersiveCallback = (sharableTarget: harmonyShare.SharableTarget) => {
      let uiContext: UIContext = this.getUIContext();
      let contextFaker: Context = uiContext.getHostContext() as Context;
      let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // This is only an example. Replace it with the correct file path.
      let shareData: systemShare.SharedData = new systemShare.SharedData({
        utd: utd.UniformDataType.HYPERLINK,
        content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
        thumbnailUri: fileUri.getUriFromPath(filePath),
        title: 'Title on the Grab & drop widget.',
        description: 'Description on the Grab & drop widget.'
      });
      sharableTarget.share(shareData);
    }
    
    private immersiveListening() {
      harmonyShare.on('gesturesShare', this.immersiveCallback);
    }
    
    private immersiveDisablingListening() {
      harmonyShare.off('gesturesShare', this.immersiveCallback);
    }
    
3.  When a user accesses a page with a shareable item, register a Grab & drop event listener. When the user leaves the page with a shareable item (including the scenario where **the user switches the app to the background**), unregister the Grab & drop event listener.
    
    // Entry component code snippet.
    onPageHide(): void {
      let uiContext: UIContext = this.getUIContext();
      let context: Context = uiContext.getHostContext() as Context;
      context.eventHub.emit('onBackGround');
    }
    
    aboutToAppear(): void {
      this.immersiveListening();
      let uiContext: UIContext = this.getUIContext();
      let context: Context = uiContext.getHostContext() as Context;
      context.eventHub.on('onBackGround', this.onBackGround);
    }
    
    aboutToDisappear(): void {
      this.immersiveDisablingListening();
      let uiContext: UIContext = this.getUIContext();
      let context: Context = uiContext.getHostContext() as Context;
      context.eventHub.off('onBackGround', this.onBackGround);
    }
    
    private onBackGround = () => {
      this.immersiveDisablingListening();
    }
