# Pushing an In-App Call Message

#### Use Cases

In-app call messages empower your app with VoIP call capabilities. Push Kit processes a VoIP call message differently when the device screen is locked or unlocked:

-   When the device screen is locked, a user can tap the answer or reject button on the lock screen. In this situation, only voice calls are supported.
-   When the device screen is unlocked, a banner notification is displayed to inform the user of the incoming video or voice call. In this situation, both the voice and video calls are supported.

When a user answers a video call, the calling page in your app is displayed. After the call is connected, it can be ended proactively or passively.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/R2KTcEY7SK-SMtBShE5N1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=153A6F321AE8023BA7AECB0CAAC65760075666AE12AAE6A7A3E54E2C51F1BFFE)

-   For details about in-app call message problems, please refer to the [FAQs](../../faqs/incoming-call-banner-error-of-an-in-app-call-message/document.md).
-   For VoIP call messages, you are advised to set **pushOptions.[ttl](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212)** to a duration within **30 to 60 seconds**.

#### Restrictions

Currently, in-app call messages support only phones and tablets.

#### Applying for Required Permissions

Your need to [apply for the in-app call message permission](../../preparations/applying-for-scenario-specific-message-permissions/document.md#section7291115452410) to push in-app call messages to your users.

#### Frequency Control

**During the debugging phase**, the maximum number of test messages that can be pushed for each project every day is 1000. To send test messages, you need to set [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212) to **true**.

**After formal release**, the total number of messages that each app can push to a single device is subject to the limits specified in the [frequency control policy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control#section993063213715). The total number of scenario-specific messages that can be pushed on a daily basis to each device cannot exceed 3000.

#### Development Procedure

1.  [Obtain a push token](../../preparations/obtaining-a-push-token/document.md).
2.  Create a component of the **UIAbility** type in your project, for example, **VoIPUIAbility.ets** (under the **src/main/ets/entryability** directory of the project). The component will process the main process of in-app call messages. Override the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate)(), [onWindowStageCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#onwindowstagecreate)(), and [onDestroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#ondestroy)() methods. The sample code is as follows:
    
    // File path: src/main/ets/entryability/VoIPUIAbility.ets
    import { UIAbility } from '@kit.AbilityKit';
    import { pushService } from '@kit.PushKit';
    import { window } from '@kit.ArkUI';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { VoipCallService } from '../service/VoipCallService';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    export default class VoIPUIAbility extends UIAbility {
      onCreate(): void {
        hilog.info(0x0000, 'testTag', \`VoIPUIAbility onCreate\`);
    
        try {
          pushService.receiveMessage('VoIP', this, async (data) => {
            // Process the message. You are advised to add a try-catch block for the callback.
            try {
              await VoipCallService.processVoIPMainMsg(data.data, this.context);
            } catch (error) {
              hilog.error(0x0000, 'testTag', 'Failed to process VoIP message: %{public}d %{public}s',
                error.code,
                error.message);
            }
          });
        } catch (e) {
          hilog.error(0x0000, 'testTag', \`Failed to register VOIP, error: ${e.code}, ${e.message}.\`);
        }
      }
    
      onWindowStageCreate(windowStage: window.WindowStage): void {
        hilog.info(0x0000, 'testTag', \`VoIPUIAbility onWindowStageCreate\`);
    
        windowStage.loadContent('pages/CalleePage').catch((err: BusinessError) => {
          hilog.error(0x0000, 'testTag', \`Failed to load content, error: ${err.code}, ${err.message}.\`);
        });
      }
    
      onDestroy(): void {
        hilog.info(0x0000, 'testTag', 'VoIPUIAbility onDestroy');
      }
    }
    
    **VoipCallService.ets** (in the **src/main/ets/service** directory of the project) is used to process an in-app call. The sample code is as follows:
    
    // File path: src/main/ets/service/VoipCallService.ets
    import { voipCall } from '@kit.CallServiceKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { common } from '@kit.AbilityKit';
    import { image } from '@kit.ImageKit';
    import { resourceManager } from '@kit.LocalizationKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    export interface VoipScene {
      scene: string;
    }
    
    export interface Content {
      data: string;
      header: string;
      callId: string;
    }
    
    export class VoipCallService {
      private static callId: string | undefined;
    
      public static async processVoIPMainMsg(data: string,
        context: common.UIAbilityContext): Promise<void> {
        hilog.info(0x0000, 'testTag', \`Process VoIP message: ${data}\`);
    
        let content: Content = JSON.parse(data);
        let scene: VoipScene = JSON.parse(content.data);
        let callId: string = content.callId;
        if (!callId) {
          hilog.error(0x0000, 'testTag', \`CallId is null\`);
        }
        VoipCallService.callId = callId;
    
        try {
          // Subscribe to **voipCallUiEvent**.
          voipCall.on('voipCallUiEvent', async (event) => {
            hilog.info(0x0000, 'testTag', \`Process voip call ui event: ${JSON.stringify(event)}.\`);
    
            await VoipCallService.processVoipCallEvent(event.voipCallUiEvent);
          });
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to register event: %{public}d %{public}s', e.code, e.message);
        }
    
        const resourceMgr: resourceManager.ResourceManager = context.resourceManager;
        // **example.png** indicates the user avatar. The value is the corresponding file name under **/resources/rawfile**.
        let fileData: Uint8Array = new Uint8Array(0);
        try {
          fileData = await resourceMgr.getRawFileContent('example.png');
        } catch (e) {
          hilog.error(0x0000, 'testTag', 'Failed to get raw file: %{public}d %{public}s', e.code, e.message);
        }
        const buffer = fileData.buffer;
        const imageSource: image.ImageSource = image.createImageSource(buffer);
        const pixelMap: image.PixelMap = await imageSource.createPixelMap();
        if (pixelMap) {
          pixelMap.getImageInfo((err, imageInfo) => {
            if (imageInfo) {
              hilog.info(0x0000, 'testTag',
                \`User profile imageInfo: ${imageInfo.size.width} \* ${imageInfo.size.height}.\`);
            }
          });
        }
    
        // Define the parameters for reporting an incoming call. Note that the **voipCallType.scene** field is defined by yourself to specify the call scenario type. Ensure that the options of this field defined on the device side are consistent with those used for pushing messages from the server side.
        let call: voipCall.VoipCallAttribute = {
          callId: callId,
          voipCallType: scene?.scene === 'video' ? voipCall.VoipCallType.VOIP\_CALL\_VIDEO :
          voipCall.VoipCallType.VOIP\_CALL\_VOICE,
          userName: 'push',
          userProfile: pixelMap,
          abilityName: 'VoIPUIAbility',
          voipCallState: voipCall.VoipCallState.VOIP\_CALL\_STATE\_RINGING
        };
    
        try {
          // Report the incoming call.
          let error = await voipCall.reportIncomingCall(call);
          hilog.info(0x0000, 'testTag', \`ReportIncomingCall result: ${error}.\`);
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to report incoming call: %{public}d %{public}s', e.code, e.message);
        }
    
        // ...Trigger vibration and play a ringtone in the app.
      }
    
      public static async processVoipCallEvent(event: voipCall.VoipCallUiEvent) {
        try {
          switch (event) {
            case voipCall.VoipCallUiEvent.VOIP\_CALL\_EVENT\_VOICE\_ANSWER:
            case voipCall.VoipCallUiEvent.VOIP\_CALL\_EVENT\_VIDEO\_ANSWER:
              // Immediately report the answered state to Call Service Kit.
              await voipCall.reportCallStateChange(VoipCallService.callId,
                voipCall.VoipCallState.VOIP\_CALL\_STATE\_ANSWERED);
    
              // Implement call answering in the app.
    
              // After implementing call answering in the app, report the active state to Call Service Kit.
              await voipCall.reportCallStateChange(VoipCallService.callId,
                voipCall.VoipCallState.VOIP\_CALL\_STATE\_ACTIVE);
              break;
            case voipCall.VoipCallUiEvent.VOIP\_CALL\_EVENT\_REJECT:
            case voipCall.VoipCallUiEvent.VOIP\_CALL\_EVENT\_HANGUP:
              // ...Implement call hang-up in the app.
    
              // Report the call status to Call Service Kit.
              await voipCall.reportCallStateChange(VoipCallService.callId,
                voipCall.VoipCallState.VOIP\_CALL\_STATE\_DISCONNECTED);
              break;
            default: {
              break;
            }
          }
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to report call state change: %{public}d %{public}s', e.code, e.message);
        }
      }
    
      public static close(): void {
        hilog.info(0x0000, 'testTag', \`Close VoIP\`);
    
        VoipCallService.processVoipCallEvent(voipCall.VoipCallUiEvent.VOIP\_CALL\_EVENT\_HANGUP);
        try {
          voipCall.off('voipCallUiEvent');
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to unregister event: %{public}d %{public}s', e.code, e.message);
        }
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/gkkz6K9uQG6PbCuYSF8pfQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4007A1B363D224EED786569D6CAB28624B34CEFE7A1FD9DBAD59478C60806244)
    
    You need to add the **example.png** file to the **src/main/resources/rawfile** directory of the project to specify the avatar displayed upon an incoming call.
    
    -   **UIAbility.onCreate** is a synchronous API and does not support asynchronous callback. You need to register [pushService.receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911)() at the lifecycle entry of the **onCreate** method and ensure that no asynchronous method awaits execution before the registration.
    -   Receive the in-app call message in [receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911)(). Your app client is advised to connect to the app server in advance so that the call can be directly connected when the user answers the call and call the [voipCall.on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section7587131203319)() API to register the call status listening callback. After the user answers or rejects the call, the registered call status listening callback will return the call status.
    -   When an in-app call is incoming, call the [voipCall.reportIncomingCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section13177019143216)() API within 10 seconds to report the call status. When receiving the call status, the system displays the notification banner. The **callId** parameter passed in the [voipCall.reportIncomingCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section13177019143216)() API must be the same as the **callId** returned by **receiveMessage()**.
    -   If the in-app call connection fails to be established, call [voipCall.reportIncomingCallError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section155796451716)() to report the connection failure. If an app running in the foreground first receives an incoming in-app call through its own network connection and calls the [voipCall.reportIncomingCall](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section13177019143216)() API to report the incoming call before it receives the in-app call message pushed by Push Kit, the app needs to call the [voipCall.reportIncomingCallError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section155796451716)() API to report the [busy line](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section157617591167).
    -   An in-app call generally has three callback statues: answered, rejected, and ended.
        -   Answered: Your app needs to call the [voipCall.reportCallStateChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section491515915329)() API to report the call activation status after the connection is set up.
        -   Rejected: After the connection to the server is disconnected, your app needs to call the [voipCall.reportCallStateChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section491515915329)() API to report the call rejection status.
        -   Ended: If a carrier call is incoming during an in-app call, the carrier call answering screen is launched. If the user taps the answer button, a callback of the in-app call ended status is triggered. In this case, you need to disconnect your app client from your server in the callback method and call the [voipCall.reportCallStateChange](https://developer.huawei.com/consumer/en/doc/harmonyos-references/call-voipcall#section491515915329)() API to report the call ended status.
    -   For details about the in-app call callback status, please refer to [Call Service Kit](../../../call-service-kit/about-this-kit/document.md).
    -   After reporting the incoming call, your app can call the [vibrator.startVibration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-vibrator#vibratorstartvibration9-1) API to trigger device vibration. For details, please refer to [Sensor Service Kit](../../../../system/hardware/sensor-service-kit/about-this-kit/document.md). You can use the AVPlayer to play your app's ringtone. You are advised to set the audio stream to ringtone by setting **usage** to **STREAM\_USAGE\_RINGTONE**. When a call comes in, the ringtone starts to play and the music playback pauses. In addition, you can use AudioSession to manage the audio focus. This ensures that the audio focus is maintained throughout the call answering. For details, please refer to [Audio Kit](../../../../media/audio-kit/about-this-kit/document.md).
    -   If your app is in Overhead state (Level = 4: device overheating or heavy load) during a voice or video call, please reduce the bitrate and frame rate, or disable the video stream and proceed with audio only. For details, please refer to the [getLevel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resourceschedule-systemload#systemloadgetlevel)() API provided by Basic Services Kit.
    
3.  Add the video call answering screen **CalleePage.ets** to the **src/main/ets/pages** directory of the project. The sample code is as follows:
    
    // File path: src/main/ets/pages/CalleePage.ets
    import CallComponent from '../component/CallComponent';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    @Entry
    @Component
    struct CalleePage {
      @StorageLink('close') @Watch('close') end: boolean | undefined = undefined;
    
      aboutToAppear() {
        hilog.info(0x0000, 'testTag', \`CalleePage aboutToAppear\`);
    
        this.end = false;
      }
    
      private close() {
        if (this.end) {
          hilog.info(0x0000, 'testTag', \`CalleePage close\`);
    
          this.getUIContext().getRouter().back(); // This is only an example (going back). Set the routing based on your needs.
        }
      }
    
      aboutToDisappear() {
        hilog.info(0x0000, 'testTag', \`CalleePage aboutToDisappear\`);
      }
    
      build() {
        Column() {
          CallComponent({})
        }
      }
    }
    
    The sample code of **CallComponent.ets** (in the **src/main/ets/component** directory of the project) is as follows:
    
    // File path: src/main/ets/component/CallComponent.ets
    import { VoipCallService } from '../service/VoipCallService';
    import { voipCall } from '@kit.CallServiceKit';
    
    @Component
    export default struct CallComponent {
      @StorageLink('close') end: boolean | undefined = undefined;
    
      build() {
        Flex({ direction: FlexDirection.Column, justifyContent: FlexAlign.SpaceBetween }) {
          Row() {
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
    
          Row({ space: 30 }) {
    
            Column() {
              Button()
                .width(80)
                .height(80)
                .backgroundColor(Color.Green)
                .onClick(() => {
                  VoipCallService.processVoipCallEvent(voipCall.VoipCallUiEvent.VOIP\_CALL\_EVENT\_VIDEO\_ANSWER);
                })
    
              Text('Answer').fontColor(Color.White).padding({ top: 5 })
            }
    
            Column() {
              Button()
                .width(80)
                .height(80)
                .backgroundColor(Color.Red)
                .onClick(() => {
                  this.end = true;
                  VoipCallService.close();
                })
    
              Text('Hang Up').fontColor(Color.White).padding({ top: 5 })
            }
    
          }
          .width('100%')
          .justifyContent(FlexAlign.Center)
        }
        .padding('30 10')
        .backgroundColor(Color.Black)
      }
    }
    
    Add page indexes to **src/main/resources/base/profile/main\_pages.json** at the project level. The sample code is as follows:
    
    {
      "src": \[
        "pages/Index",
        "pages/CalleePage"
      \]
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/bmNj7Fb7RT6UUvNGP56xRQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C8D7335C0FA8FC5CD3B344E71D9EDE0FA7023753DB5D18C6FE50C8BB2C6D43AE)
    
    The page effect implemented by the sample code is for reference only.
    
4.  Configure **actions** for **VoIPUIAbility** in the **abilities** section of the **src/main/module.json5** file of the project.
    
    "abilities": \[ 
      { 
        "name": "VoIPUIAbility", 
        "srcEntry": "./ets/entryability/VoIPUIAbility.ets", 
        "launchType": "singleton",
        "description": "VoIPUIAbility test", 
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": false, 
        "skills": \[ 
          // Keep the existing **skill** object unchanged.
          // Add an independent **skill** object and set the **actions** parameter.
          { 
            **"actions": \["action.ohos.push.listener"\]**
          }
        \]
      } 
    \]
    
    -   **actions**: Set this parameter to **action.ohos.push.listener**. This action can be defined for only one ability. If the **uris** parameter also exists, it should be left empty.
    
5.  Call the REST API provided by Push Kit from your app server to send an in-app call message. For details, please refer to [Scenario-Specific Message API Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-intro).

## Sending an In-App Call Message

1.  Call the REST API provided by Push Kit from your app server to send an in-app call message. The following is a request example:
    
    // Request URL    
    POST https://push-api.cloud.huawei.com/v3/\[projectId\]/messages:send 
    
    // Request Header   
    Content-Type: application/json   
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*   
    push-type: 10 
    
    // Request Body
    {   
      "pushOptions": { 
        "ttl": 30 
      }, 
      "payload": {   
        "extraData": "{\\"scene\\": \\"voice\\"}" 
      },   
      "target": {   
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*aZW"\]   
      } 
    }
    
    -   In the URL, **\[projectId\]** indicates the project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    -   **Authorization**: a character string in JWT format. Obtain the value by referring to [Generating a JWT Based on a Service Account](../../device-cloud-debugging/generating-a-jwt-based-on-a-service-account/document.md).
    -   **push-type**: The value **10** indicates in-app call message.
    -   **token**: push token. [Obtain the push token](../../preparations/obtaining-a-push-token/document.md) in advance.
    -   **extraData**: extra data carried, which is a character string. For details, please refer to the description of the **extraData** parameter in [VoIPCallPayload (In-App Call Message)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section146341550144011). For details about how to obtain **extraData**, please refer to the [sample code](https://gitee.com/harmonyos_samples/push-kit-sample-code-clientdemo-arkts/blob/master/entry/src/main/ets/service/VoipCallService.ets).
    -   **ttl**: message cache duration. You are advised to set the duration to 30 to 60 seconds. For details, please refer to pushOptions.[ttl](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212).
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d9/v3/p50SkhV1RmSrNsrQhKiDDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=219BF02C7282F83A755EFFC4319DB3FE0320AC11C7216FC1C070EEB5554842A9)

-   In-app call messages can only be used to wake up an app client during a voice/video call and notify users of the incoming call. Do not use this type of messages to end a call or communicate with the app client directly. Your app server should communicate with your app client through its own network connection. Compared with pushing messages, it is faster to use the existing network connection between the app server and app client for communication. If the connection to Push Kit is poor, push messages may fail to reach the app client.
-   You are advised to use Push Kit to send in-app call messages and then send call requests through the existing network connection between the app server and app client, regardless of whether the app client is running in the foreground. This ensures that calls can reach the app client properly.

## Missed Call Notification

1.  If you need to send a missed call notification to the called party in a call, your app server can call the REST API to [send a notification message](../pushing-a-notification-message/sending-a-notification-message/document.md). The following uses notification messages as an example:
    
    // Request URL    
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send 
       
    // Request Header   
    Content-Type: application/json   
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*   
    **push-type: 0** 
       
    // Request Body
    {   
      "pushOptions": { 
        **"ttl":**86400
      }, 
      "payload": {   
        "notification": { 
          "category": "MISS\_CALL",  
          "title": "Notification title",
          "body": "Notification body",
          "clickAction": { 
            "actionType": 0 
          },
          "appMessageId": "12345"
        }
       },   
       "target": {   
         "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*aZW"\]   
       } 
     }
    
    -   **push-type**: The value **0** indicates the notification message scenario.
    -   **category**: message category used for self-classification. Set this parameter to **MISS\_CALL**. For details, please refer to the [parameter description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117). Before pushing messages, ensure that you have applied for the required [notification self-classification permission](../../preparations/applying-for-scenario-specific-message-permissions/document.md#section16708911111611).
    -   **appMessageId**: unique ID of an app message. When the called party ends a call directly, the VoIP app of the called party can send a missed call notification. If the VoIP app is running in the foreground, the app can use [Notification Kit](../../../notification-kit/about-this-kit/document.md) to send the missed call notification; if the VoIP app is running in the background, the app can use Push Kit to send the missed call notification. Whether an app is running in the foreground or background sometimes cannot be accurately determined, and two missed call notifications may be sent in this case. You are advised to use the same **appMessageId** for Notification Kit and Push Kit to send missed call notifications. The notifications will then be automatically deduplicated by ID.
    -   For details about other parameters, please refer to [AlertPayload (Notification Message)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section1152516418157).
