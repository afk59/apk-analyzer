# Template-based Notifications on Wearable Devices

This API allows for template-based display of a notification on a wearable device after your phone app sends a notification to the wearable device. Meanwhile, the wearable device will vibrate or ring, depending on system settings. The following figure shows an example notification displayed on the wearable device.

This API does not require user authorization, but make sure that you have applied for the message notification permission for your app (by referring to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md)). Otherwise, the API calling will fail.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7c/v3/RGtFIb4uS2aGoEQGet6sYw/en-us_image_0000002190567617.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F9394BEAFF9C4BC46F3965B1C5BBD4047A88CB16FF69E3D339A5868449CBBC1F)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/hdid8-vdSee54JQDmXn-_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52EBB400B480875F7B31D2A125F7AF9B24B98BBCB0D2C22A4F7F7367FF6EFB13)

-   Template-based notifications can be displayed even if you don't have a counterpart app installed on the wearable device.
-   Ensure that the wearable device is connected to the Huawei Health app. Users can query the connection status on the **Devices** screen in the Huawei Health app. You can determine whether the device is connected by calling [getConnectedDevices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1828213119411). If the target device is not included in the returned device list, prompt the user to reconnect the device.
-   The wearable device vibrates or rings when the following conditions are met:
    1.  Vibration or ringing is enabled on the wearable device.
    2.  The wearable device is being worn.
    3.  Do Not Disturb is not enabled on the wearable device.
-   Notifications will pop up on its own on the wearable device when the following conditions are met:
    1.  The wearable device is being worn.
    2.  Do Not Disturb is not enabled on the wearable device.

#### Sending Notifications to the Wearable Device

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c6/v3/O4JJnF7kRZeBVse74aV6mA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E40AF865A5F5A47D829553291BCC5B149F772F9613E77D90A92E9775BBD45961)

To call this API, you need to apply for the message notification permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Call the [getNotifyClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section552416431386) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [NotifyClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section82221754103913) object.
4.  Define the configuration parameter class [NotificationOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section0751457344).
5.  Call the [notify](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section087562072313) method to send notifications from the phone app to the wearable device.
    
    // Step 3 Obtain the **NotifyClient** object.
    let notifyClient: wearEngine.NotifyClient = wearEngine.getNotifyClient(this.getUIContext().getHostContext());
    
    // Step 4 Construct the **NotificationOptions** object.
    let button1: wearEngine.NotificationButton = {
      buttonId: wearEngine.ButtonId.FIRST\_BUTTON,
      // The maximum length for the button content is 12 bytes.
      content: 'button\_1'
    }
    let type1Notification: wearEngine.Notification = {
      type: wearEngine.NotificationType.NOTIFICATION\_WITH\_ONE\_BUTTON,
      // The maximum length for the bundle name and title is 28 bytes.
      bundleName: 'bundleName',
      title: 'title',
      // The maximum length for the message content is 400 bytes.
      text: 'text',
      buttons: \[button1\]
    }
    let options: wearEngine.NotificationOptions = {
      notification: type1Notification,
      onAction: (feedback: wearEngine.NotificationFeedback) => {
        console.info(\`one button notify get feedback is ${feedback.action ? feedback.action : feedback.errorCode}\`);
      }
    }
    
    // Step 5 Send a template-based notification to the device.
    notifyClient.notify(targetDevice.randomId, options).then(result => {
      console.info(\`Succeeded in sending notification.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to send notification. Code is ${error.code}, message is ${error.message}\`);
    })
