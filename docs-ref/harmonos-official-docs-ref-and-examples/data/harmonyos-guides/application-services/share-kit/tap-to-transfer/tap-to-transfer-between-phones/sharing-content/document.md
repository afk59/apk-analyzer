# Sharing Content

#### Registering a Tap to Transfer Event Listener

When a user accesses a page or scenario that supports Tap to Transfer, provide proper guidance and prompts to effectively improve the user's willingness to share.

The following figures show how to provide the guidance:

-   Display the message "Tap against a phone with HarmonyOS 5 or later to share".
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d1/v3/uZ9pSW7lTjeizRcZFfNppA/en-us_image_0000002481169676.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20515C2F00ACF9F89EB9E6073309C9BF2C6F6498FF1E95F5A38A52F88E9A5420 "Click to enlarge")
    

-   Display an animated image, suggesting the Tap to Transfer function.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/hhU8V9dNTzi9kM0pmS6UTA/en-us_image_0000002481169670.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C4822D361B4BB234D3CF408084F70FD1FC480392FE6305BC864D290CB380333 "Click to enlarge")
    
    Share Kit provides unified animated image resource files for apps to integrate.
    
    -   Click [here](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/tree/master/entry/src/main/resources/rawfile) to download all files in the **knock\_share\_guide** directory and place the files in **entry/src/main/resources/rawfile** of the app.
    -   For details about the sample code, click [here](https://gitcode.com/harmonyos_samples/share-kit_-sample-code_-clientdemo_-arkts/blob/master/entry/src/main/ets/components/subpages/KnockShareTips.ets).

#### Setting the Sharing Preview

When integrating the Tap to Transfer function, you need to use proper widget templates for different types of shared data.

## Setting the Widget Style

To ensure the Tap to Transfer user experience, Share Kit provides three sharing widget templates for phones to choose when initiating Tap to Transfer.

| 
Template Type

 | 

Description

 | 

Display Effect

 |
| :-- | :-- | :-- |
| 

Image-only template

 | 

This template contains only a preview image.

It is recommended for scenarios such as file and image sharing, which do not require a title or description.

-   Usage
    
    When constructing the data to be shared, transfer only the **thumbnailUri** parameter.
    
-   Layout requirements
    
    Preview image: The minimum aspect ratio is 1:4. The excess part will be cropped.
    

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/qRSLH6xoSM6kv_yhurS7QA/en-us_image_0000002481329630.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E01D0EBEC742D9063093A260FD5AC883A05415F51436C7FC742404464ADDBD4 "Click to enlarge")

 |
| 

Immersive large widget template

 | 

This template contains a preview image, title, description, and app icon.

This template is recommended for link sharing.

-   Usage
    
    Both of the following conditions must be met:
    
    -   When constructing the data to be shared, transfer the **title**, **description**, and **thumbnailUri** parameters.
    -   **The aspect ratio of a preview image is less than 1:1.**
    

-   Layout requirements
    1.  Preview image: The minimum aspect ratio is 1:4. The excess part will be cropped.
    2.  Title: A maximum of two lines can be displayed. Excess text will be truncated with an ellipsis (...). If a title contains important information at the end, you need to keep the title length around 40 characters.
    3.  Description: Only one line can be displayed. Excess text will be truncated with an ellipsis (...).
    4.  App icon: You do not need to configure this. The system obtains the app icon and displays it at the bottom of the widget by default.

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/Jhx6HCy0QWKKuEZWxa7rzQ/en-us_image_0000002513289525.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8D08BEA0A69CEF22F8AC5171438E90EC59A2526A00D2DFFACD5603E02022CBF "Click to enlarge")

 |
| 

Two-part white widget template with image above

 | 

This template contains a preview image, title, description, and app icon. This template is recommended for link sharing.

-   Usage
    
    Both of the following conditions must be met:
    
    1.  When constructing the data to be shared, transfer the **title**, **description**, and **thumbnailUri** parameters.
    2.  **The aspect ratio of a preview image is greater than 1:1.**
    
-   Layout requirements
    1.  Preview image: The preview image is displayed only in the upper part of the widget and does not cover the entire widget.
    2.  Title: A maximum of two lines can be displayed. Excess text will be truncated with an ellipsis (...). If a title contains important information at the end, you need to keep the title length around 40 characters.
    3.  Description: Only one line can be displayed. Excess text will be truncated with an ellipsis (...).
    4.  App icon: You do not need to configure this. The system obtains the app icon and displays it at the bottom of the widget by default.

 | 

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/PrHslB7JRpanEHGk4OqbLQ/en-us_image_0000002481169672.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B61AA506B140BB579C426ED2C5D90799A5FE865951BD1A4E0EDAAE93F9721AC3 "Click to enlarge")

 |

## Setting a Proper Preview Image

The preview image quality directly affects the display effect of the Tap to Transfer widget. Preview images that are too large or too small can lead to experience issues such as slow loading or blurriness. You are advised to set proper preview images according to the recommended aspect ratios and resolutions in the table below.

| 
Preview Image Source

 | 

Recommended Aspect Ratio

 | 

Recommended Resolution (Pixels)

 |
| :-- | :-- | :-- |
| 

Poster created by an app

 | 

3:4

 | 

Minimum resolution: 600 x 800

Maximum resolution: 3000 x 4000

 |
| 

Image uploaded by a user

 | 

No restrictions

 | 

Minimum resolution: no restrictions

Maximum resolution: 3000 x 4000

 |

## Using the Preview Image Update Capability

When an app uses a cloud-hosted image as the preview image, the image may fail to be downloaded to the local device promptly when the Tap to Transfer callback is triggered, resulting in the sharing failure.

To address this issue, Share Kit provides the capability of delayed update of preview images.

1.  When receiving the callback triggered by the Tap to Transfer event, the source device can send just the core data content to establish a connection.
2.  Share Kit provides the default preview image for widget display.
3.  After the cloud-hosted image is downloaded, call the [sharableTarget.updateShareData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-harmony-share#section18386290710) API to update the preview image information.

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { fileUri } from '@kit.CoreFileKit';

@Component
export default struct Index {
  aboutToAppear(): void {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: 999, // This is only an example. Replace it with the correct window ID.
    }
    harmonyShare.on('knockShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
      let shareData: systemShare.SharedData = new systemShare.SharedData({
        utd: utd.UniformDataType.HYPERLINK,
        content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
        // Generate a widget template based on **title**, **description**, and **thumbnailUri**. For details, please refer to the "Setting the Widget Style" section.
        title: 'Title on the Tap to Transfer widget.',
        description: 'Description on the Tap to Transfer widget.'
      });
      // If the cloud-hosted preview image cannot be downloaded in a timely manner, send the data first.
      sharableTarget.share(shareData);

      setTimeout(() => {
        // Update the preview image once the download is complete.
        let uiContext: UIContext = this.getUIContext();
        let contextFaker: Context = uiContext.getHostContext() as Context;
        let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // This is only an example. Replace it with the correct file path.
        sharableTarget.updateShareData({
          thumbnailUri: fileUri.getUriFromPath(filePath)
        });
      }, 5000);
    });
  }

  aboutToDisappear(): void {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: 999, // This is only an example. Replace it with the correct window ID.
    }
    // Unregister the knockShare event listener.
    harmonyShare.off('knockShare', capabilityRegistry);
  }

  build() {
  }
}

## Security Policies

To enhance information security of the sender and receiver, the Tap to Transfer feature displays the HUAWEI ID or device identifier of the other device during content sharing in HarmonyOS NEXT 5.0.0.123 SP16 and later versions, helping users verify the identity of the sender/receiver. The specific rules are as follows.

| 
Device

 | 

HUAWEI ID Signed In on the Other Device

 | 

HUAWEI ID Not Signed In on the Other Device

 |
| :-- | :-- | :-- |
| 

Sender of the Tap to Transfer feature

 | 

If a HUAWEI ID is signed in on the receiver, the nickname and avatar of this HUAWEI ID will be displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/eChTadWQSuyvq4QaouOmRw/en-us_image_0000002481169674.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16F5765BAC05F6B998E58823C88BF126BD1743D89771EFC2D7C6137C2E794C34 "Click to enlarge")

 | 

If no HUAWEI ID is signed in on the receiver, the receiver device information will be displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/M9XFWyx0RFiM_LfSDYR6nA/en-us_image_0000002513289533.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A556162267943F1E1927FDDD88A8FCB0DE973010E6001C3E2D674EBE54F5AA38 "Click to enlarge")

 |
| 

Receiver of the Tap to Transfer feature

 | 

If a HUAWEI ID is signed in on the sender, the nickname and avatar of this HUAWEI ID will be displayed.

NOTE:

If the sender runs an OS earlier than HarmonyOS NEXT 5.0.0.123 SP16, no information will be displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/RTX0v0BnQ5izjaGEVrZrNw/en-us_image_0000002481169664.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9504CAAC72B71F4C54208DB9FA763277073FBD946BF922512C04DCC9B59F8FE1 "Click to enlarge")

 | 

If no HUAWEI ID is signed in on the sender, the sender device information will be displayed.

NOTE:

If the sender runs an OS earlier than HarmonyOS NEXT 5.0.0.123 SP16, no information will be displayed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/vx6Dv_KfSwWmeJYfP6KJKA/en-us_image_0000002481329624.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CB5822D7B1A885BBB48A4C1A55082474BE54D6F222651F513863EE9F4967550 "Click to enlarge")

 |

#### Sending the Shared Data

Link-based redirection to a specified app can be implemented in either of the following modes: [Using App Linking for App-to-App Redirection](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/app-linking-startup) and [Using Deep Linking for Application Redirection](../../../../../application-framework/ability-kit/stage-model-development/inter-application-redirection/starting-a-specified-application/using-deep-linking-for-application-redirection/document.md).

To implement redirection to a specified app, the UTD type must be set to **general.hyperlink** to ensure that Share Kit processes the link correctly.

## App Linking

When App Linking is used for redirection, users can access the content of the link regardless of whether the app is installed.

With the capability provided by [App Linking Kit](../../../../app-linking-kit/about-this-kit/document.md), users can be redirected to AppGallery if the specified app is not installed, improving user experience.

-   If the app has been installed, App Linking can directly launch the app.
-   If the app has not been installed, App Linking opens the web page of the link using the system browser by default. With the App Linking Kit's capability of direct access to AppGallery, users can be directly redirected to AppGallery if the specified app is not installed. For details, please refer to [Direct Access to AppGallery](../../../../app-linking-kit/redirecting-to-an-app-download-page-through-direct-access-to-appgallery/document.md). With the [Deferred Link](../../../../app-linking-kit/redirecting-to-an-app-details-page-with-the-deferred-link-capability/document.md) capability, even if an app is not installed when Tap to Transfer is triggered, the app can still obtain the shared link after being downloaded and launched. This enhances user experience and boosts the link conversion rate.

The sample code is as follows:

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { harmonyShare, systemShare } from '@kit.ShareKit';
import { fileUri } from '@kit.CoreFileKit';

@Component
export struct HarmonyShareScenes {
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

  build() {
  }

  private onBackGround = () => {
    this.immersiveDisablingListening();
  }

  private immersiveCallback = (sharableTarget: harmonyShare.SharableTarget) => {
    let uiContext: UIContext = this.getUIContext();
    let contextFaker: Context = uiContext.getHostContext() as Context;
    let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // This is only an example. Replace it with the correct file path.
    let shareData: systemShare.SharedData = new systemShare.SharedData({
      utd: utd.UniformDataType.HYPERLINK,
      content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
      // Generate a widget template based on **title**, **description**, and **thumbnailUri**. For details, please refer to the "Setting the Widget Style" section.
      thumbnailUri: fileUri.getUriFromPath(filePath),
      title: 'Title on the Tap to Transfer widget.',
      description: 'Description on the Tap to Transfer widget.'
    });
    sharableTarget.share(shareData);
  }

  private immersiveListening() {
    harmonyShare.on('knockShare', this.immersiveCallback);
  }

  private immersiveDisablingListening() {
    harmonyShare.off('knockShare', this.immersiveCallback);
  }
}

## Deep Linking

When Deep Linking is used for redirection, the system searches only the installed apps on the local device for the target app. If no match is found, a message is displayed, indicating "No available opening mode".

#### Stopping Sharing in Unexpected Scenarios

When a user goes to the page to be shared, the host app calls [harmonyShare.on('knockShare')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-harmony-share#section1215414133214) to register a Tap to Transfer event listener. When the host app receives the Tap to Transfer event callback from Share Kit, the sharing may fail to be initiated due to certain reasons. To ensure user experience, the host app needs to stop sharing promptly to avoid long-time waiting.

The handling varies depending on the actual scenario.

## No Shareable Content on the Current Page

Since version 6.0.2 (22), if the content on the current page cannot be shared using Tap to Transfer, you can call [sharableTarget.clarifyNonShare()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-harmony-share#section8129205594811) to terminate the sharing and guide the user to a shareable page to try again.

The display effect is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/aPdzJwL-S-q8qhCRgYnThA/en-us_image_0000002515305857.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C954481EA3077C0A2B6D7B5C1ADEFA22CF9D3BDF60A3FBB7C629DC15D32F5E9 "Click to enlarge")

The sample code is as follows:

import { harmonyShare } from '@kit.ShareKit';

aboutToAppear(): void {
  harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
    sharableTarget.clarifyNonShare({ message: 'Try again on a page that supports Tap to Transfer.' });
  });
}

## Other Exceptions Such as Content Download Failure

Since version 5.0.3(15), if sharing cannot be initiated due to network or service reasons, you can call [sharableTarget.reject()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-harmony-share#section063111381379) to terminate the sharing and notify the user of the termination reason.

The sample code is as follows:

import { harmonyShare } from '@kit.ShareKit';

aboutToAppear(): void {
  harmonyShare.on('knockShare', (sharableTarget: harmonyShare.SharableTarget) => {
    sharableTarget.reject(harmonyShare.SharableErrorCode.DOWNLOAD\_ERROR);
  });
}
