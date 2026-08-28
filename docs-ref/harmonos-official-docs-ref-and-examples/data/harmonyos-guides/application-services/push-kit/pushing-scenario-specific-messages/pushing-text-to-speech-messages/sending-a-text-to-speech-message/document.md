# Sending a Text-to-Speech Message

#### Use Cases

When a user device receives a text-to-speech message sent by you:

-   If your app process is not running in the foreground, your app will start a subprocess, namely, an extended notification process. Push Kit will deliver the message content to the extended notification process, where you can complete service processing and return the customized message content. Push Kit will then display the customized notification. If you do not return the message content within 10 seconds, Push Kit will display the default notification content.
-   If your app process is running in the foreground, no notification will be displayed. You can obtain the text-to-speech message content in the app process and complete service processing.

#### Restrictions

The function of sending text-to-speech messages supports phones, tablets, PCs, 2-in-1 devices, and (since 5.1.0(18)) wearables.

#### Applying for Required Permissions

Your need to [apply for the text-to-speech message permission](../../../preparations/applying-for-scenario-specific-message-permissions/document.md#section159981112245) to push text-to-speech messages to your users.

#### Frequency Control

**During the debugging phase**, the maximum number of test messages that can be pushed for each project every day is 1000. To send test messages, you need to set [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212) to **true**.

**After formal release**, the total number of messages that each app can push to a single device is subject to the limits specified in the [frequency control policy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control#section993063213715). The total number of scenario-specific messages that can be pushed on a daily basis to each device cannot exceed 3000.

#### Development Procedure

1.  [Obtain a push token](../../../preparations/obtaining-a-push-token/document.md).
2.  To ensure that devices can receive messages properly, you are advised to call the [requestEnableNotification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerrequestenablenotification10-1)() method to prompt users to allow notifications before sending messages. For details, please refer to [Requesting Notification Authorization (Notification Kit)](../../../../notification-kit/requesting-notification-authorization/document.md).
3.  Call the REST API provided by Push Kit from your app server to push a text-to-speech message. For details, please refer to [Scenario-Specific Message API Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-intro). The following is a request example:
    
    // Request URL 
    POST "https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send"
     
    // Request Header 
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\* 
    **push-type: 2**
    
    // Request Body
    { 
      "payload": { 
        "extraData": "{\\"title\\":\\"replace title\\",\\"text\\":\\"replace text\\"}",
        "notification": { 
          "category": "PLAY\_VOICE",  
          "title": "Notification title",
          "body": "Notification body",
          "clickAction": { 
            "actionType": 0 
          },
          "notifyId": 12345
        }
      }, 
      "target": { 
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\] 
      }, 
      "pushOptions": { 
        "testMessage": true,
        "ttl": 86400
      } 
    }
    
    -   In the URL, **\[projectId\]** indicates the project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    -   **Authorization**: a character string in JWT format. Obtain the value by referring to [Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct#section20573634202313).
    -   **push-type**: The value **2** indicates the text-to-speech message type.
    -   **category**: message category used for self-classification. Currently, this parameter can be set to **PLAY\_VOICE**.
    -   **actionType**: The value **0** indicates that the home page of the app will be opened after a user taps the message.
    -   **token**: push token. Obtain the token by referring to [Obtaining a Push Token](../../../preparations/obtaining-a-push-token/document.md).
    -   **extraData**: extra data carried, which is a character string. For details, please refer to [ExtensionPayload (Text-to-Speech Message)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section161192514234). For details about how to obtain **extraData**, please refer to [Sample Code](https://gitcode.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/abilities/RemoteNotificationExtAbility.ets).
    -   **testMessage** (optional): indicates whether a message is a test message. The value **true** indicates a test message. In each project, a maximum of 1000 test messages can be sent every day. Each push can carry up to 10 tokens. For details, please refer to [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212).
    -   **ttl**: message cache duration. For details, please refer to [ttl](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212).
    -   **notifyId** (optional): custom message ID. If a message does not contain the ID or the ID is **\-1**, Push Kit will generate a unique ID for the message. Different notification messages can use the same notification ID, so that new messages can overwrite old messages. The ID must be a number in the range \[0, 2147483647\]. If the ID will be used for **message recall**, it **must be set**. For details, please refer to [notifyId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117).
    -   **image**: URL of the large icon on the right of a notification. This field is optional. The URL must use the HTTPS protocol.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/e_coribNQ4u5dhSTGiYZ2Q/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7538EFFFDD08470350EBFCB9820B0439C3EED52310323048B8A88D678EAF3F14)
        
        Do not push images that contain sensitive content.
        
    
4.  Implement the following logic: If your app is not in the foreground when a message is sent, Push Kit will deliver the notification content to the extended notification process and return the final notification content (including the title and body fields). Push Kit will then display the customized notification in the notification panel. The detailed procedure is as follows:
    
    Set **type** and **actions** for **RemoteNotificationExtAbility** in the **extensionAbilities** section of the **src/main/module.json5** file under your project. **There shall be only one ExtensionAbility for defining type and actions. If the uris parameter also exists, it should be left empty.** The following is a configuration example:
    
    "extensionAbilities": \[
      {
        "name": "RemoteNotificationExtAbility",
        **"type": "remoteNotification"**,
        "srcEntry": "./ets/entryability/RemoteNotificationExtAbility.ets",
        "description": "RemoteNotificationExtAbility test",
        "exported": false,
        "skills": \[
          // Add an independent **skill** object and set the **actions** parameter.
          {
            **"actions": \["action.hms.push.extension.remotenotification"\]**
          }
        \]
      }
    \]
    
    -   **type**: The value is always **remoteNotification**, indicating the ExtensionAbility type extended by the notification.
    -   **actions**: The value is always **action.hms.push.extension.remotenotification**, indicating that text-to-speech messages will be received.
    
    Create a component of the **ExtensionAbility** type in your project, which inherits from [RemoteNotificationExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-remote-notification-extension-ability), and override the [onReceiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-remote-notification-extension-ability#section455013322919)() method for data reception and service processing. The sample code is as follows:
    
    // File path: src/main/ets/entryability/RemoteNotificationExtAbility.ets
    import { pushCommon, RemoteNotificationExtensionAbility } from '@kit.PushKit';
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { resourceManager } from '@kit.LocalizationKit';
    import { common } from '@kit.AbilityKit';
    
    export default class RemoteNotificationExtAbility extends RemoteNotificationExtensionAbility {
      async onReceiveMessage(remoteNotificationInfo: pushCommon.RemoteNotificationInfo): Promise<pushCommon.RemoteNotificationContent> {
        hilog.info(0x0000, 'testTag', 'RemoteNotificationExtAbility onReceiveMessage, remoteNotificationInfo');
    
        // Read the pixel map object
        const resourceMgr: resourceManager.ResourceManager = (this.context as common.UIExtensionContext).resourceManager;
        let fileData: Uint8Array = new Uint8Array(0);
        try {
          fileData = await resourceMgr.getMediaContent($r('app.media.startIcon').id);
        } catch (e) {
          hilog.error(0x0000, 'testTag', 'Failed to get media content: %{public}d %{public}s', e.code, e.message);
        }
        const buffer = fileData.buffer;
        const imageSource: image.ImageSource = image.createImageSource(buffer as ArrayBuffer);
        const pixelMap: image.PixelMap = await imageSource.createPixelMap();
        if (pixelMap) {
          pixelMap.getImageInfo((err, imageInfo) => {
            if (imageInfo) {
              hilog.info(0x0000, 'testTag', \`imageInfo ${imageInfo.size.width} \* ${imageInfo.size.height}\`);
            }
          });
        }
    
        // You need to implement the logic of voice broadcast for your app yourself.
        this.textToSpeech();
    
        // Return the display message content.
        return {
          title: 'Default replace title.',
          text: 'Default replace text.',
          badgeNumber: 1,
          setBadgeNumber: 2,
          overlayIcon: pixelMap,
          wantAgent: {
            abilityName: 'DemoAbility',
            parameters: {
              key: 'Default value'
            }
          }
        }
      }
    
      textToSpeech(): void {
        // Perform the text-to-speech task.
      }
    
      onDestroy(): void {
        hilog.info(0x0000, 'testTag', 'RemoteNotificationExtAbility onDestroy.');
      }
    }
    
    -   The return value of the function will be used to replace the notification to be displayed on devices. **title** and **text** indicate the notification title and body to be displayed respectively.
    -   The **badgeNumber** field specifies the **increment** to be added to the current badge number. The **setBadgeNumber** field determines the **exact badge number** to be displayed. If both fields are present, **setBadgeNumber** takes precedence over **badgeNumber**. For details, please refer to [RemoteNotificationContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushcommon#section155703491918).
    -   The **overlayIcon** field specifies the superimposed icon of the displayed notification. For details, please refer to [RemoteNotificationContent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushcommon#section155703491918).
    -   The **wantAgent.abilityName** field indicates the **abilityName** to be replaced (for example, **DemoAbility**), corresponding to the landing page to be opened upon the button tap. You need to develop and adapt the **DemoAbility** by yourself. For details, please refer to [RemoteWantAgent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushcommon#section122049160211).
    -   The **wantAgent.parameters** field indicates the data to be transferred to the app. For details, please refer to [RemoteWantAgent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushcommon#section122049160211).
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ef/v3/9SQShkj8Rbee7XMJ235HGg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=73BF1B9124968153431F0D0ED1F0BFE22941F45A789A30171AD10393765792AC)
        
        You can implement voice broadcast using the **textToSpeech()** method in the sample code.
        
        You can implement voice broadcast by using the following capabilities offered by diverse kits:
        
        -   Text-to-speech service provided by [Core Speech Kit](../../../../../ai/core-speech-kit/text-to-speech/document.md)
        -   Media services provided by [Media Kit](../../../../../media/media-kit/about-this-kit/document.md)
        -   Audio Playback provided by [Audio Kit](../../../../../media/audio-kit/audio-playback/audio-playback-development/document.md)
        
    
5.  Implement the following logic: If your app is in the foreground when a message is sent, Push Kit will not display the notification on the notification panel. The detailed procedure is as follows:
    
    Set **actions** to **action.ohos.push.listener** in **skills** of the **abilities** section in the **src/main/module.json5** file at the module level. (This action can be defined for only one ability. **If the uris parameter also exists, it should be left empty.**) The following sample code uses **PushMessageAbility** as an example:
    
    {
      "name": "PushMessageAbility",
      "srcEntry": "./ets/abilities/PushMessageAbility.ets",
      "launchType": "singleton",
      "startWindowIcon": "$media:startIcon",
      "startWindowBackground": "$color:start\_window\_background",
      "exported": false,
      "skills": \[
        // Keep the existing **skill** object unchanged.
        {
          "actions": \[
            "com.app.action"
          \]
        },
        // Add an independent **skill** object and set the **actions** parameter.
        {
          "actions": \[
            **"action.ohos.push.listener"**
          \]
        }
      \]
    }
    
    In the **onCreate()** method of the existing **UIAbility** class in the client-side project, call the [receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911)() method and set [PushType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section5507492425) to **IM** to obtain text-to-speech messages when the app is running in the foreground. The following sample code uses **PushMessageAbility** as an example:
    
    // File path: src/main/ets/abilities/PushMessageAbility.ets
    import { UIAbility } from '@kit.AbilityKit';
    import { pushService } from '@kit.PushKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    /\*\*
     \* **PushMessageAbility** is used as an example for receiving notification messages when the app is running in the foreground.
     \*/
    export default class PushMessageAbility extends UIAbility {
      onCreate(): void {
        try {
          // The value of **receiveMessage** is always **IM**.
          pushService.receiveMessage('IM', this, (payload) => {
            try {
              // Obtain the data transmitted from the server.
              const data: string = payload.data;
              // TODO: Complete the service processing by yourself.
              hilog.info(0x0000, 'testTag', 'Succeeded in getting notification,data=%{public}s',
                JSON.stringify(JSON.parse(data)?.notification));
            } catch (e) {
              let errRes: BusinessError = e as BusinessError;
              hilog.error(0x0000, 'testTag', 'Failed to process data: %{public}d %{public}s',
                errRes.code, errRes.message);
            }
          });
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to get message: %{public}d %{public}s', e.code,
            e.message);
        }
      }
    }
