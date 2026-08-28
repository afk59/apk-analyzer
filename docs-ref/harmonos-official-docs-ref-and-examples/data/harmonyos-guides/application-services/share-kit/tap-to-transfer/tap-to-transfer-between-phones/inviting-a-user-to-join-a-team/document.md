# Inviting a User to Join a Team

#### Registering a Tap to Transfer Event Listener

Register a Tap to Transfer event listener on the page for inviting a user to join a team room.

**Figure 1** Example in landscape orientation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/36/v3/nD4chzvOSCKnJ-k5vuuDyQ/en-us_image_0000002513289553.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED457B39B38B916BA9AF2AA8179DB9AB6B09D4B001580B59FE0E438E7284C887 "Click to enlarge")

**Figure 2** Example in portrait orientation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/Mogto13OR-6cvoeaRcVakA/en-us_image_0000002513409521.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062122Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E85E99D227D30840B613A4BC93384D499690F787C234C4CC42B81628CE6F366E "Click to enlarge")

#### Registering the sendOnly Attribute

If two users use Tap to Transfer to invite each other to join their team rooms at the same time, the two users cannot join each other's team room.

To address this issue, Share Kit provides the **sendOnly** attribute. For details, please refer to the **sendOnly** attribute of [SendCapabilityRegistry](https://developer.huawei.com/consumer/en/doc/harmonyos-references/share-harmony-share#section7361949172719).

If the **sendOnly** attribute is enabled for both parties of Tap to Transfer, the sharing will be terminated and the users will be prompted to exit the current app on either device and try again. If the **sendOnly** attribute is not enabled for both parties, the sharing will be successful.

import { uniformTypeDescriptor as utd } from '@kit.ArkData';
import { systemShare, harmonyShare } from '@kit.ShareKit';
import { fileUri } from '@kit.CoreFileKit';

@Component
export default struct Index {
  aboutToAppear(): void {
    let capabilityRegistry: harmonyShare.SendCapabilityRegistry = {
      windowId: 999, // This is only an example. Replace it with the correct window ID.
      sendOnly: true, // Indicates that only data sending is supported. If the peer end also declares that only data sending is supported, the two-way sharing will fail.
    }
    harmonyShare.on('knockShare', capabilityRegistry, (sharableTarget: harmonyShare.SharableTarget) => {
      let uiContext: UIContext = this.getUIContext();
      let contextFaker: Context = uiContext.getHostContext() as Context;
      let filePath = contextFaker.filesDir + '/exampleKnock1.jpg'; // This is only an example. Replace it with the correct file path.
      let shareData: systemShare.SharedData = new systemShare.SharedData({
        utd: utd.UniformDataType.HYPERLINK,
        content: 'https://sharekitdemo.drcn.agconnect.link/ZB3p',
        // Generate a widget template based on **title**, **description**, and **thumbnailUri**.
        thumbnailUri: fileUri.getUriFromPath(filePath),
        title: 'Title on the Tap to Transfer widget.',
        description: 'Description on the Tap to Transfer widget.'
      });
      sharableTarget.share(shareData);
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

#### Setting a Preview Image for Inviting a User to a Team

For details about how to set a preview image, please refer to [Setting the Sharing Preview](../sharing-content/document.md#section1880197194811).

#### Processing the Team Joining Link

When started by Share Kit, the target app can obtain the **want** data passed through the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate) or [onNewWant](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#onnewwant) callback. In the **want** data, **want.uri** is the link in the team joining invitation. The target app can process the team invitation logic based on the parameters contained in the link.

The sample code is as follows:

import { AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  async onWindowStageCreate(windowStage: window.WindowStage): Promise<void> {
    try {
      windowStage.loadContent('pages/Index');
    } catch (error) {
      console.error(\`onWindowStageCreate error. Code: ${error?.code}, message: ${error?.message}\`);
    }
  }

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.log('EntryAbility onCreate invoked. uri: ', want.uri);
    // to do things.
  }

  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    console.log('EntryAbility onNewWant invoked. uri: ', want.uri);
    // to do things.
  }
}

#### Stopping Sharing in Unexpected Scenarios

If sharing cannot continue due to an exception when the Tap to Transfer callback is triggered, the host app can stop the sharing.

For details, please refer to [Stopping Sharing in Unexpected Scenarios](../sharing-content/document.md#section1142174216514).
