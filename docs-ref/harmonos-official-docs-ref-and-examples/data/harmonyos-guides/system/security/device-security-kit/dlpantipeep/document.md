# DlpAntiPeep

#### Use Cases

This feature enables apps to protect user privacy based on the peeping status. For example, display a system-level overlay to mask the window, disable personalized recommendations, and hide sensitive information such as browsing records, payment records, and favorites records when the phone is not used by the device owner. The system intelligently identifies the person who consistently unlocks the phone using facial recognition as the device owner for screen privacy protection.

#### Development Prerequisites

-   Facial recognition has been enabled on the device.
-   The global screen privacy switch has been enabled under **Settings** > **Privacy & security** > **Screen Privacy** on the device. Then the screen privacy function has been enabled for the specific app after successful facial recognition.

#### Restrictions

All of the following conditions must be met:

1\. This feature requires that the **Screen Privacy** option be available on the device. You can check it by going to **Settings** > **Privacy & security** > **Screen Privacy** on the device.

2\. The HarmonyOS version must be HarmonyOS 6.0.0 Beta1 or later.

3\. The DevEco Studio version must be DevEco Studio 6.0.0 Beta1 or later.

4\. The HarmonyOS SDK version must be HarmonyOS 6.0.0 Beta1 SDK or later.

5\. The screen privacy function uses intelligent detection to assess your surrounding environment via sensors and provide risk alerts. Key factors include whether your face is within a certain distance from the device, whether your face is blocked, and whether the ambient lighting is sufficient. If the distance is too close or too far, the face is blocked, or the environment is dimly lit, recognition errors may occur, potentially resulting in missed or false alerts. If you suspect the intelligent detection is inaccurate, you can try adjusting your position and lighting, re-unlock the phone using facial recognition, and then re-enable the feature to help safeguard your privacy.

#### Service Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/LoFlgedORtCTPk7V4XFoiw/en-us_image_0000002515108411.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CDB6F4F3E5BDA4181A8C01F1C3596A81BEB7AB818A50B1C06DC24112853F40E "Click to enlarge")

The process is as follows:

1.  A user enables the screen privacy function for the current app under **Settings** > **Privacy & security** > **Screen Privacy**.
2.  The app calls the **isDlpAntiPeepSwitchOn()** API to query whether screen privacy has been enabled.
3.  The app calls the **on()** API to subscribe to the screen privacy notification. If only the owner is looking at the screen, the non-peeping state is returned. If the owner and a non-owner are looking at the screen at the same time, the peeping state is returned. As long as the owner is not looking at the screen, the non-peeping state is returned regardless of whether a non-owner views the screen accidentally or with the owner's authorization.
4.  The app calls the **getDlpAntiPeepInfo()** API to query the peeping status.
5.  The app calls the **setAntiPeepMaskLayer(windowId: number)** API to display a system-level overlay.
6.  The app calls the **passDlpAntiPeepInfo()** API to set the peeping status to non-peeping. Then the non-peeping state will be returned until the phone is locked or the app exits.
7.  The app calls the **off()** API to unsubscribe from the screen privacy notification.

#### API Description

The following table lists the APIs related to screen privacy. For more information about the APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/devicesecurity-dlpantipeep-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

isDlpAntiPeepSwitchOn(): Promise<boolean>

 | 

Checks whether screen privacy has been enabled.

 |
| 

on(type: 'dlpAntiPeep', callback: Callback<DlpAntiPeepStatus>): void

 | 

Subscribes to the screen privacy notification.

 |
| 

off(type: 'dlpAntiPeep', callback?: Callback<DlpAntiPeepStatus>): void

 | 

Unsubscribes from the screen privacy notification.

 |
| 

getDlpAntiPeepInfo(): DlpAntiPeepStatus

 | 

Obtains the peeping status of the current app.

 |
| 

passDlpAntiPeepInfo(): void

 | 

Sets the peeping status to non-peeping. Then the non-peeping state will be returned until the phone is locked or the app exits.

 |
| 

setAntiPeepMaskLayer(windowId: number): Promise<void>

 | 

Displays a system-level overlay to mask the window.

 |

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b9/v3/dCAVuXlOTpKFMSbWedJQJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062008Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A404AFF860FAA2CCCF7E59F38C2BBA2347162D754040DB790DF720B33AD08B65)

-   When preparing for the development, you need to apply for the **ohos.permission.DLP\_GET\_HIDE\_STATUS** permission to obtain the screen peeping status of the current app.
-   Only enterprise apps in the trustlist can apply for this permission. For details about how to apply for this permission, please refer to [Requesting Restricted Permissions](../../application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
-   You need to inform users about the purpose, methods, and scope of data usage.

1.  Import the DlpAntiPeep module and related public modules.
    
    import { dlpAntiPeep } from '@kit.DeviceSecurityKit';
    import { window } from '@kit.ArkUI';
    import { common } from '@kit.AbilityKit';
    
2.  Call the query API to check whether screen privacy is enabled for the current app. If screen privacy is enabled, call the screen privacy notification subscription API and obtain the peeping status.
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Dlp anti peep start';
    
      async callback(dlpAntiPeepStatus: dlpAntiPeep.DlpAntiPeepStatus) {
        if (dlpAntiPeepStatus == dlpAntiPeep.DlpAntiPeepStatus.PASS) {
          console.info(\`DlpAntiPeepStatus is PASS.\`);
        } else if (dlpAntiPeepStatus == dlpAntiPeep.DlpAntiPeepStatus.HIDE) { // Indicates that someone is peeping at the screen. The app can perform privacy protection operations.
          console.info(\`DlpAntiPeepStatus is HIDE.\`);
          await this.setMaskLayer();
        }
      }
    
      private async setMaskLayer(): Promise<void> {
        let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
        let windowClass: window.Window;
        try {
          windowClass = await window.getLastWindow(context);
        } catch(err) {
          console.error('error', err.code, err.message);
          return;
        }
        let windowId: number;
        try {
          windowId = windowClass.getWindowProperties().id;
        } catch (err) {
          console.error('Failed to get window properties:', err);
          return;
        }
        try {
          await dlpAntiPeep.setAntiPeepMaskLayer(windowId); // Use the obtained window ID to set the privacy protection overlay.
        } catch (error) {
          console.error(\`setAntiPeepMaskLayer failed. error code is ${JSON.stringify(error)}\`);
        }
      }
    
      async testAntiPeep() {
        let isOpen: boolean;
        try {
          isOpen = await dlpAntiPeep.isDlpAntiPeepSwitchOn();
        } catch (err) {
          console.error('isDlpAntiPeepSwitchOn failed:', err);
          return;
        }
        if (isOpen) {
          console.info(\`isDlpAntiPeepSwitchOn is true.\`); // Indicates that the screen privacy function of the current app is enabled.
        } else {
          console.info(\`isDlpAntiPeepSwitchOn is false.\`);// Indicates that the screen privacy function of the current app is disabled.
          return;
        }
        try {
          dlpAntiPeep.on('dlpAntiPeep', this.callback); // Subscribe to the screen privacy notification.
          let result = dlpAntiPeep.getDlpAntiPeepInfo(); // Call the API to obtain the peeping status of the current app.
         if (result === dlpAntiPeep.DlpAntiPeepStatus.HIDE) { // Indicates that someone is peeping at the screen. The app can perform privacy protection operations.
            console.info(\`getDlpAntiPeepInfo is HIDE.\`);
            await this.setMaskLayer(); // Display the overlay.
          } else if (result === dlpAntiPeep.DlpAntiPeepStatus.PASS) {
            console.info(\`getDlpAntiPeepInfo is PASS.\`);
          }
          dlpAntiPeep.passDlpAntiPeepInfo(); // Sets the peeping status to non-peeping. So no peeping alert will be displayed.
          dlpAntiPeep.off('dlpAntiPeep', this.callback); // Unsubscribe from the screen privacy notification. No more such notifications will be sent.
        } catch (err) {
          console.error('error', err.code, err.message);
        }
      }
    
      build() {
        Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center}) {
          Button() {
            Text('Dlp\_anti\_peep\_test')
              .fontSize(30)
              .fontWeight(FontWeight.Bold)
          }.type(ButtonType.Capsule)
          .margin({
            top: 30
          })
          .width('80%')
          .height('10%')
          .backgroundColor(Color.White)
          .onClick(() => {
            this.testAntiPeep();
          })
        }
      }
    }
