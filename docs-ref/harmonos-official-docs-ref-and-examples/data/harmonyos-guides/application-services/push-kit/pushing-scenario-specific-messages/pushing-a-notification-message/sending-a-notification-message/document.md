# Sending a Notification Message

#### Use Cases

A notification message is directly sent by Push Kit and displayed in the notification panel, on the lock screen, or as a banner. Users can tap the message to launch the corresponding app. You can perform operations in [Configuring the Notification Message Layout](#section5164103925811) to engage more users.

#### Restrictions

The function of sending notification messages supports phones, tablets, PCs, 2-in-1 devices, (since 5.1.0(18)) wearables, and (since 5.1.1(19)) TVs.

#### Applying for Required Permissions

Push Kit classifies notification messages into the following categories based on the message content: **service and communication**, and **news and marketing**. For the two types, self-classification needs to be enabled and configured separately.

The two types of notification messages are different in terms of the **notification mode, display position, and frequency control rules**. For more information about permission application, please refer to [Message Self-Classification](../../../preparations/applying-for-scenario-specific-message-permissions/document.md#section16708911111611).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/C0A3Fr97SNSkdRK6EgePHQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=842929F41CFC6C2D0F60AA9C0F580E975B8CC297FD4E8348594F8EECC0486A37)

-   **If you have not applied for the message self-classification permission, messages pushed by your app are categorized as news and marketing messages by default ([category](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) set to MARKETING)**. If you need to send only MARKETING messages, you do not need to apply for the message self-classification permission.
-   The maximum number of news and marketing messages that can be pushed by an app to each device on a daily basis is either **2** or **5**, depending on your app category. For details, please refer to [Notification Message Frequency Control Rules](../../../preparations/applying-for-scenario-specific-message-permissions/document.md#section1128516504398). If your upper limit is reached, send test messages or apply for the self-classification permission. For details, please refer to [Message Frequency Control](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control).

#### Frequency Control

**During the debugging phase**, the maximum number of test messages that can be pushed for each project every day is 1000. To send test messages, you need to set [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212) to **true**.

**After formal release**, the total number of messages that each app can push to a single device is subject to the limits specified in the [frequency control policy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control#section993063213715). The total number of scenario-specific messages that can be pushed on a daily basis to each device cannot exceed 3000.

Different frequency control policies are applied for service and communication messages, and news and marketing messages. For details, please refer to [Notification Message Frequency Control Rules](../../../preparations/applying-for-scenario-specific-message-permissions/document.md#section1128516504398).

#### Development Procedure

1.  [Obtain a push token](../../../preparations/obtaining-a-push-token/document.md).
2.  To ensure that devices can receive messages properly, you need to call the [requestEnableNotification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerrequestenablenotification10-1)() method to prompt users to allow notifications before sending messages. The sample code is as follows:
    
    // File path: src/main/ets/entryability/EntryAbility.ets
    import { BusinessError } from '@kit.BasicServicesKit';
    import { UIAbility } from '@kit.AbilityKit';
    import { window } from '@kit.ArkUI';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { notificationManager } from '@kit.NotificationKit';
    
    export default class EntryAbility extends UIAbility {
      onWindowStageCreate(windowStage: window.WindowStage) {
        hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
        windowStage.loadContent('pages/Index', (err, data) => {
          if (err.code) {
            hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
            return;
          }
          hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
          notificationManager.requestEnableNotification(this.context).then(() => {
            hilog.info(0x0000, 'testTag', \`\[ANS\] requestEnableNotification success\`);
          }).catch((err: BusinessError) => {
            hilog.error(0x0000, 'testTag', \`\[ANS\] requestEnableNotification failed, code is ${err.code}, message is ${err.message}\`);
          });
        });
      }
    }
    
3.  Configure the **skills** section to ensure proper redirection upon tapping the message. For details, please refer to [Actions to Be Triggered upon Message Tapping](#section697519219136).
4.  Call the REST API of the Push Kit server from your app server to push notification messages. If you have not [enabled the required permission](#section15809122792917) or the permission you have enabled does not match the [category](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field contained in the request body of your [REST API call to push scenario-specific messages](../../../device-cloud-debugging/pushing-scenario-specific-messages/document.md), notification messages are classified into **news and marketing messages** by default. In this case, you are subject to the [restriction](../../../preparations/applying-for-scenario-specific-message-permissions/document.md#section1128516504398) that each app can push up to 2 or 5 (depending on the app category) messages to each device on a daily basis.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/Sk0HSxWyQ1-q4nzMoi5XAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5449274B8E044A139E4B9AA9BDA97A83229A5A2B93F64A2B9C9CAD8B61C40FC6)
    
    -   This sample code demonstrates only some message fields in REST APIs. For details about server-side development, please refer to [Device-Cloud Debugging](../../../device-cloud-debugging/document.md).
    
    -   Use the API request URL of the V3 version (**https://push-api.cloud.huawei.com/****v3****/_\[projectId\]_/messages:send**) to push messages.
        
        If the API request URL version is V3 (https://push-api.cloud.huawei.com/v3/\[projectId\]/messages:send), the message can be pushed to HarmonyOS Next/5.x and later versions. If the request URL version is V2 (https://push-api.cloud.huawei.com/v2/\[projectId\]/messages:send), the message can be pushed only to HarmonyOS 3.x/4.x.
        
    
    The following is an example request (change the value of **category** to the actual message type):
    
    // Request URL
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
    
    // Request Header
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
    push-type: 0
    
    // Request Body
    {
      "payload": {
        **"notification": {**
          "category": "xxxxxx", // Change it to the actual notification message type.
          "title": "Common notification title",
          "body": "Common notification body",
          "clickAction": {
            "actionType": 0
          },
          // Indicates whether to display the notification when the app is running in the foreground. This parameter is valid only for notifications whose **push-type** is **0**.
          "foregroundShow": true,
          "notifyId": 12345
        **}**
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
    -   **push-type**: The value **0** indicates alert message. In this example, the message is a notification message.
    -   **category**: category of a notification message. In this example, **MARKETING** indicates news and marketing messages. You can check [more categories](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117).
    -   **actionType**: action triggered upon message tapping. The value **0** indicates that [the home page of the app will be opened after a user taps the message](#section1792616175914). The value **1** indicates that [a specified in-app page will be opened after a user taps a message](#section8794131614597).
    -   **token**: push token. [Obtain the push token](../../../preparations/obtaining-a-push-token/document.md) in advance.
    -   **testMessage** (optional): indicates whether a message is a test message. The value **true** indicates a test message. In each project, a maximum of 1000 test messages can be sent every day. Each push can carry up to 10 tokens. For details, please refer to [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212).
    -   **ttl**: message cache duration. For details, please refer to [ttl](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212).
    -   **notifyId** (optional): custom message ID. If a message does not contain the ID or the ID is **\-1**, Push Kit will generate a unique ID for the message. Different notification messages can use the same notification ID, so that new messages can overwrite old messages. The ID must be a number in the range \[0, 2147483647\]. If the ID will be used for **message recall**, it **must be set**. For details, please refer to [notifyId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117).
    -   **foregroundShow** (optional): Indicates whether notification messages are displayed in the notification panel when the app is running in the foreground. The value **true** indicates that notification messages are displayed regardless of whether the app is running in the foreground or background. The value **false** indicates that notification messages are displayed in the notification panel only when the app is tunning in the background. The default value is **true**. If **foregroundShow** is set to **true**, [receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911) is not triggered.
    
5.  Send a push request. For details about the response, please refer to [Response Parameters](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-response). Then check whether the device has received the notification message. If not, locate the problem by referring to [FAQs](../../../faqs/why-does-the-target-device-fail-to-receive-a-push-message-after-the-push-api-is-/document.md).

#### Actions to Be Triggered upon Message Tapping

## Opening the App Home Page upon Message Tapping

1.  Check the [skills](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills) configuration in **src/main/module.json5** at the module level. Ensure that **uris is not set** for the skill that specifies the **app home page** (skill that contains the configurations **entity.system.home** and **ohos.want.action.home**); otherwise, **devices will fail to receive messages**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/Gj3oh544T_uEjBRBTlLIfA/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4EA641C4720B08CE77839CF0F56E946C6F34D3E1DBC3A7313827272AF7DB2BAF)
    
    The **skills** section in the **module.json5** file can contain multiple **skill** objects. Each object corresponds to one capability.
    
    To configure push message redirection and other redirection capabilities (like NFC or browser redirection), you must create separate **skill** objects within **skills** to map the respective capabilities.
    
    The following is an example of configuring the **skills** section for opening the app home page for upon message tapping:
    
    {
      "module": {
        // ...
        "abilities": \[
          {
            "name": "TestAbility",
            "srcEntry": "./ets/abilities/TestAbility.ets",
            "exported": false,
            "startWindowIcon": "$media:startIcon",
            "startWindowBackground": "$color:start\_window\_background",
            "skills": \[
              // This skill specifies the app home page. Do not set **uris** for it.
              {
                "entities": \[
                  "entity.system.home"
                \],
                "actions": \[
                  // The configuration **action.system.home** is for versions earlier than API 19 and has been discarded.
                  "ohos.want.action.home"
                \]
              },
              // Configurations of other skills.
              {}
            \]
          }
        \]
      }
    }
    
2.  Set **actionType** to **0** when sending a message.
    
    // Request URL
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
    
    // Request Header
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
    **push-type: 0**
    
    // Request Body
    {
      "payload": {
        **"notification": {**
          "category": "MARKETING",
          "title": "Common notification title",
          "body": "Common notification body",
          **"clickAction": {**
            **"actionType": 0,**
            **"data": {"testKey": "testValue"}**
          **}**
        **}**
      },
      "target": {
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
      },
      "pushOptions": {
        "testMessage": true
      }
    }
    
    -   **actionType**: action triggered by a message tap. The value **0** indicates that the home page (page where the entry ability, usually **EntryAbility**, is located) is opened.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/_DP8yYPuRIOppjlOePPHgA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=010D3251A5CA17B351911F49C773B327C42A1E20A139B58A0EF973E2132E2AAD)
        
        In the [request body](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct) of a scenario-specific message, if the API request URL version is V3 (https://push-api.cloud.huawei.com/v3/\[projectId\]/messages:send), the message can be pushed to HarmonyOS Next/5.x and later versions. If the API request URL version is V2 (https://push-api.cloud.huawei.com/v2/\[projectId\]/messages:send), the message can be pushed only to HarmonyOS 3.x/4.x.
        
    

## Opening an In-app Page upon Message Tapping

1.  Set **actions** or **uris** in [skills](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills) of the target ability in **src/main/module.json5** at the module level using either of the following methods:
    
    Method 1: Add an **independent skill object** in [skills](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills). For the object, set the **actions** parameter to open an in-app page upon message tapping. The following is an example:
    
    {
      "name": "TestAbility",
      "srcEntry": "./ets/abilities/TestAbility.ets",
      "exported": false,
      "startWindowIcon": "$media:startIcon",
      "startWindowBackground": "$color:start\_window\_background",
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
            "com.test.action"
          \]
        }
      \]
    }
    
    Method 2: Add an **independent skill object** to [skills](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills). For the object, set the **uris** parameter to open an in-app page upon message tapping. (**Note that, both the actions and uris parameters need to be set, with the actions parameter set to an empty string.**) The following is an example:
    
    {
      "name": "TestAbility",
      "srcEntry": "./ets/abilities/TestAbility.ets",
      "exported": false,
      "startWindowIcon": "$media:startIcon",
      "startWindowBackground": "$color:start\_window\_background",
      "skills": \[
        // Keep the existing **skill** object unchanged.
        {
          "actions": \[
            "com.app.action"
          \]
        },
        // Add an independent **skill** object, and set the **uris** and **actions** parameters for it. The **actions** parameter must be set to an empty string.
        {
          "actions": \[""\],
          "uris": \[
            {
              "scheme": "https",
              "host": "www.xxx.com",
              "port": "8080",
              "path": "push/test"
            }
          \]
        }
      \]
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/72/v3/mto-EguSSW2RZmnLl5lVLQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6CA2CD147EFA5AE42636D82EB57FE46644F0029FB6B5F1BCF1A15981223369BB)
    
    The **skills** section in the **module.json5** file can contain multiple **skill** objects. Each object corresponds to one capability.
    
    To configure push message redirection and other redirection capabilities (like NFC or browser redirection), you must create separate **skill** objects within **skills** to map the respective capabilities.
    
2.  Set **actionType** under [clickAction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section152462191216) to **1** when sending a message.
    
    // Request URL
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
    
    // Request Header
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
    **push-type: 0**
    
    // Request Body
    {
      "payload": {
        **"notification": {**
          "category": "MARKETING",
          "title": "Common notification title",
          "body": "Common notification body",
          **"clickAction": {**
            **"actionType": 1,**
            **"action": "com.test.action",**
            **"uri": "https://www.xxx.com:8080/push/test",**
            **"data": {"testKey": "testValue"}**
          **}**
        **}**
      },
      "target": {
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
      },
      "pushOptions": {
        "testMessage": true
      }
    }
    
    -   **actionType**: action triggered by a message tap. The value **1** indicates that an in-app page is opened. When this field is set to **1**, set at least one of **uri** and **action**. If both of them are set, the app page specified by **action** is opened first. If no app page is matched for both **action** and **uri**, the app home page is opened upon message tapping.
    -   **action**: a set of values that can be used to receive [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-ability-want). These values can be customized.
    -   **uri**: a set of values that match **uris** in [Want](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-ability-want). For details, please refer to [skills](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#skills).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/V3yvHP-vQ8eazpDcrrQVyQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1FAC0B3A0559B9581BDACA2D5D5E434EA3EE28B3C5640FB009C311DC57CB5509)
    
    -   In the [request body](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct) of a scenario-specific message, if the API request URL version is V3 (https://push-api.cloud.huawei.com/v3/\[projectId\]/messages:send), the message can be pushed to HarmonyOS Next/5.x and later versions. If the API request URL version is V2 (https://push-api.cloud.huawei.com/v2/\[projectId\]/messages:send), the message can be pushed only to HarmonyOS 3.x/4.x.
    
    -   If no app page is matched for both **action** and **uri**, the app home page is opened upon message tapping.
    

## Transmitting Data

When calling the REST API of the Push Kit server to push a notification message, your app server can pass the **data** field in the API call request, so the passed data can be transmitted to your app client when a user taps the message.

1.  Call the REST API to push a message and pass the **data** field under [clickAction](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section152462191216) in the request body. The following is an example:
    
    {
      "payload": {
        **"notification": {**
          "category": "MARKETING",
          "title": "Common notification title",
          "body": "Common notification body",
          **"clickAction": {**
            **"actionType": 0,**
            **"data": {"testKey": "testValue"}** // The **data** field is passed.
          **}**
        **}**
      },
      "target": {
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
      },
      "pushOptions": {
        "testMessage": true
      }
    }
    
    -   **data**: data in JSON format, carried when a message is tapped.
    
2.  Override the following code in the [onCreate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#oncreate)() method of the target page (**TestAbility** used as an example) to enter this lifecycle callback from a [cold start](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/starting-uiability-within-the-same-application/document.md#cold-starting-uiability):
    
    // File path: src/main/ets/abilities/TestAbility.ets
    import { UIAbility, Want } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    export default class TestAbility extends UIAbility {
      onCreate(want: Want): void {
        // Obtain data transferred in the message.
        const data = want.parameters;
        const value = want.parameters?.\["testKey"\]; // value: "testValue"
        hilog.info(0x0000, 'testTag', 'Succeeded in getting message data, value is %{public}s', value);
        // Process data based on the service scenario.
      }
    }
    
    Override the following code in the [onNewWant](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-uiability#onnewwant)() method to enter this lifecycle callback from a [hot start](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/starting-uiability-within-the-same-application/document.md#hot-starting-uiability):
    
    // File path: src/main/ets/abilities/TestAbility.ets
    import { UIAbility, Want } from '@kit.AbilityKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    export default class TestAbility extends UIAbility {
      onNewWant(want: Want): void {
        // Obtain data transferred in the message.
        const data = want.parameters;
        const value = want.parameters?.\["testKey"\]; // value: "testValue"
        hilog.info(0x0000, 'testTag', 'Succeeded in getting message data, value is %{public}s', value);
        // Process data based on the service scenario.
      }
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/pBX81rJIT_WXFepZPVVPAQ/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC25D065914CEAC3833BD6691619E3C9D0E25AC43A1D3B1BE86967FEC59BC94F)
    
    The **onNewWant()** method is available only in singleton mode.
    

#### Configuring the Notification Message Layout

Push Kit offers a variety of notification message layouts that you can customize to attract users and increase your app's daily active users.

## Common Notification Format

When you send a notification, the [notification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) parameter must contain the **title** and **body** fields to define the title and body displayed in the notification panel respectively. A maximum of three lines of content can be displayed. An overload text will be truncated by an ellipsis (...).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/S847duhkQMWnN6o5GWyHLw/en-us_image_0000002368545992.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1E24FB5865E3AA7CBDF4AF5361CE3618385EB133F778F922D0DC70C78B97F63A "Click to enlarge")

Message body example:

{
  "payload": {
    "notification": {
      "category": "MARKETING",
      **"title": "Push Kit",**
      **"body": "Push Kit is a messaging service provided for you to establish a cloud-to-device messaging channel. By integrating Push Kit, you can send messages to your apps on user devices in real time. This helps you maintain closer ties with users and increase user awareness of and engagement with your apps.",**
      "clickAction": {
        "actionType": 0
      }
    }
  },
  "target": {
    "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
  },
  "pushOptions": {
    "testMessage": true
  }
}

## Notification Badge

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/DNKvhNV8QCOkoomUuCIxiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B64D93B9C8A4B59CF7A6B161B42DAD831C1F0BCF93E0F518A12E1442B21282D4)

Wearables and TVs do not support this notification format.

You can include the [badge](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section266310382145) field when sending a notification to set the numerical badge to be displayed on your app icon, informing users of new messages.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3/v3/o64_pxe0R52Fkb3S7m7NDg/en-us_image_0000002402305737.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9C064FD2F579F9EADD441E41AF7BDC7F72090F614E63B80C206C9B9241E06E73 "Click to enlarge")

Message body example:

{
  "payload": {
    "notification": {
      "category": "MARKETING",
      "title": "Notification title",
      "body": "Notification body",
      **"badge":{**
        **"addNum": 1**,
        **"setNum": 99**
      **},**
      "clickAction": {
        "actionType": 0
      }
    }
  },
  "target": {
    "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
  },
  "pushOptions": {
    "testMessage": true
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/52/v3/QrV4R1ZfRZSvlIbRvBUH0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A846239D21F621743C92DBFF7CB22C129B1B9A957E8AEECD69BEC65AB043A7BE)

-   **addNum**: increment of the badge number, but not the actual number to be displayed.
-   **setNum**: actual number to be displayed on the badge. The priority of **setNum** is higher than that of **addNum**.
-   Launching an app, tapping a message, or cleaning up notifications will not decrease the badge number. You can call the [setBadgeNumber](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagersetbadgenumber10)() method to change the badge number. Before doing so, please [import the module](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#modules-to-import) first.
-   When **badgeNumber** in the **setBadgeNumber()** method is set to **0**, the badge number can be cleaned up.

## Large Notification Icon

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/x4i2RBK-S3GxZM6mVqqjrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=07B48EDA5B17099958CDCFBF541A714CE2B092B3B18E686F8BF8FC89C9D0B09F)

Wearables do not support this notification format.

**Do not push images that contain sensitive content.**

You can include the [image](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) field when sending a notification to display a large icon to notify users.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8e/v3/T5Wl3Qh9QK20ilPnKhCV7w/en-us_image_0000002368546012.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=046CBAC1E82B27519D335988BB8572085A18F6DAA7C24F6238A5BBC352511870 "Click to enlarge")

Message body example:

{
  "payload": {
    "notification": {
      "category": "MARKETING",
      "title": "Push Kit",
      "body": "is a messaging service",
      **"image": "https://\*\*\*.png"**, // The supported image formats are PNG, JPG, JPEG, and BMP. It is recommended that the image width x height be less than 128 x 128 pixels. Images larger than 49,152 pixels will not be displayed.
      "clickAction": {
        "actionType": 0
      }
    }
  },
  "target": {
    "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
  },
  "pushOptions": {
    "testMessage": true
  }
}

## Multi-Line Text Format

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/2B_8GoQvQlOfNQ33rz7Apw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=81B616E20ADB960436B6F66B6FE2CBD17DA72BA2C134BE6DCAC27004677450CF)

Wearables do not support this notification format.

You can include the **inboxContent** and **style** fields in [notification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) to set the multi-line text format when sending a message. A maximum of three separate lines of content can be displayed. For each line, overlong text will be truncated by an ellipsis (...).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/xC3kpVRySOiEDo3Z35-KBQ/en-us_image_0000002368546008.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DE22D75C9024BDDF7E7643DE9686F839D9B8BEBE20F00BF3D9F2913E9052CC82 "Click to enlarge")

Message body example:

{
  "payload": {
    "notification": {
      "category": "MARKETING",
      "title": "Personalized message display",
      "body": "Notification body",
      **"style": 3,**
      **"inboxContent"****: \[**
          **"1. Message styles",** 
          **"2. Message reminder and display modes",** 
          **"3. Support notification message localization"**
          **\],**
      "clickAction": {
        "actionType": 0
      }
    }
  },
  "target": {
    "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
  },
  "pushOptions": {
    "testMessage": true
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/R1GOoLpaTbSuCqQk06uWqQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AEB18D1D837CA99B3027E57B64A04B369AA83E72477CC29AF3DEE22B32A0C9EA)

-   To use the multi-line text format, set the **style** field to **3**.
-   If you send multiple notifications and they get collapsed, the title and body shown before the multi-line text expansion use the values of the **title** and **body** fields respectively.
-   When a user expands a multi-line text message or only one multi-line text message exists, the title and body displayed use the values of the **title** and **inboxContent** fields respectively.

#### Developing Account Authentication for Notification Messages

Push Kit enables targeted messaging by authenticating user accounts. This feature allows you to send notifications to specific accounts on a device based on their unique account attributes.

For example, on a Huawei mobile phone, if a user switches from account A to account B within a specific app, notifications sent to account A will not be displayed on the device to prevent account B from seeing account A's notifications.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/R9pgdk9eQ_y3-kC5Ybkeiw/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E92CF686EB982F5EFCB3589B15ED0712E671C964B54E9638C2EBEECAEF612CC8)

-   After the push token is changed, the corresponding account is automatically unbound from your app.
-   A maximum of 10 app accounts can be bound.

Push Kit supports two account types: HUAWEI ID and account in the app's own account system.

-   **HUAWEI ID**
    
    In this case, **profileId** is the unique anonymous identifier mapped to a HUAWEI ID in the app.
    
    You can call the [bindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section20575105524912)() API for account binding when:
    
    -   A user authorizes to sign in to your app using their HUAWEI ID.
    -   A user switches from another account to the current HUAWEI ID.
    
    You can call the [unbindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section915174525214)() API to unbind an account when:
    
    -   A user signs out of their HUAWEI ID in your app.
    
    Example: After a user selects HUAWEI ID for sign-in and successfully signs in to account A, your app calls the [bindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section20575105524912)() API of Push Kit to bind the **profileId** of account A to the push token on the current device. If a notification sent by the app server contains the **profileId** of account A, the notification is displayed only when account A signs in. If a notification does not contain any **profileId**, the notification is displayed regardless of which account has signed in.
    
-   **App account in the app's own account system**
    
    In this case, **profileId** is the unique anonymous identifier mapped to an account in the app's own account system.
    
    You can call the [bindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section20575105524912)() API for account binding when:
    
    -   A user signs in to their account in your app.
    -   A user switches from another account to the current account.
    
    You can call the [unbindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section915174525214)() API to unbind an account when:
    
    -   A user signs out of their account in your app.
    
    Example: After a user successfully signs in to account A in the app's own account system, the app calls the [bindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section20575105524912)() API of Push Kit to bind the **profileId** of the account to the push token on the current device. If a notification sent by the app server contains the **profileId** of account A, the notification is displayed only when account A signs in. If a notification does not contain any **profileId**, the notification is displayed regardless of which account has signed in.
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/4BkMwp-LRpSIlnfviMztMA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C3739FE877D1EA337374629E67417B3DC9971F52F1E1F18557EA62DE2E74FD99)

If [unbindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section915174525214)() is not called when an account signs out, or [bindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section20575105524912)() is not called when the user switches to another account, messages sent to the previous account will still be displayed.

1.  [Obtain a push token](../../../preparations/obtaining-a-push-token/document.md).
2.  To ensure that devices can receive messages properly, you are advised to call the [requestEnableNotification](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-notificationmanager#notificationmanagerrequestenablenotification10-1)() method to prompt users to allow notifications before sending messages. For details, please refer to [Requesting Notification Authorization (Notification Kit)](../../../../notification-kit/requesting-notification-authorization/document.md).
3.  Generate a non-null and unique **profileId** for the account to be bound. (You are not advised to use the actual account ID as **profileId**. Generate an anonymous identifier that can uniquely map to the account ID. There is no restriction on the generation algorithm.) Call the [bindAppProfileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section20575105524912)() method to bind the user to the app on the current device. The sample code is as follows:
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { pushCommon, pushService } from '@kit.PushKit';
    import { BusinessError } from '@kit.BasicServicesKit';
     
    // Define the profileId to be bound. You are advised to use an anonymous identifier generated based on the account ID.
    const profileId = '111\*\*\*222';
    // Bind the app account.
    pushService.bindAppProfileId(pushCommon.AppProfileType.PROFILE\_TYPE\_APPLICATION\_ACCOUNT, profileId).then(() => {
      hilog.info(0x0000, 'testTag', 'Succeeded in binding app profile id');
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'Failed to bind app profile id: %{public}d %{public}s', err.code, err.message);
    });
    
4.  Report the push token and the generated **profileId** to your app server so that the server can push messages to the device.
5.  The app server calls the REST API to push a notification message. The sample code is as follows:
    
    // Request URL
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
    
    // Request Header
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
    push-type: 0
    
    // Request Body
    {
      "payload": {
        **"notification": {**
          "category": "MARKETING",
          "title": "Common notification title",
          "body": "Common notification body",
          **"profileId": "111\*\*\*222"**,
          "clickAction": {
            "actionType": 0
          }
        **}**
      },
      "target": {
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
      },
      "pushOptions": {
        "testMessage": true
      }
    }
    
    -   In the URL, **\[projectId\]** indicates the project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    -   **Authorization**: a character string in JWT format. Obtain the value by referring to [Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct#section20573634202313).
    -   **push-type**: The value **0** indicates the notification message scenario.
    -   **actionType**: The value **0** indicates that the home page of the app will be opened after a user taps the message.
    -   **token**: push token. [Obtain the push token](../../../preparations/obtaining-a-push-token/document.md) in advance.
    -   **profileId**: anonymous identifier of an account in the app's account system. For details, please refer to [profileId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117).
    
    After a message is sent successfully, Push Kit verifies the [AppProfileType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushcommon#section411410371767) (HUAWEI ID or app account) used during account binding.
    
    -   If a HUAWEI ID is bound, Push Kit checks whether the **profileId** carried in the message is the same as the **profileId** bound to the app, and then checks whether the current signed-in HUAWEI ID is the same as that signed in during account binding. The message is displayed only when both conditions are met.
    -   If an account in the app's own account system is bound, Push Kit checks whether the **profileId** carried in the message is the same as the **profileId** bound to the app. If so, the message is displayed.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/Q0QB7u9ISg2onm7TgJBUhA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D03165325DA7F9514569CCD8FA742C04A6AED5B73AAB8DB32C661939923BAA84)
        
        In the [request body](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct) of a scenario-specific message, if the API request URL version is V3 (https://push-api.cloud.huawei.com/v3/\[projectId\]/messages:send), the message can be pushed to HarmonyOS Next/5.x and later versions. If the API request URL version is V2 (https://push-api.cloud.huawei.com/v2/\[projectId\]/messages:send), the message can be pushed only to HarmonyOS 3.x/4.x.
        
    

#### Processing Notification Messages When the App is Running in the Foreground

To display notification messages when the app is running in the background and only receive notification messages and complete service handling when the app is running in the foreground, you need to configure both the server and client as follows:

1.  Pass the [foregroundShow](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117) parameter in the REST API call request body and set it to **false**, so that notification messages are not displayed when the app is running in the foreground. (The default value of **foregroundShow** is **true**, indicating that notification messages are displayed no matter whether the app is running in the foreground or background.)
    
    {
      "payload": {
        **"notification": {**
          "category": "MARKETING",
          "title": "Common notification title",
          "body": "Common notification body",
          "clickAction": {
            "actionType": 0
          },
          "foregroundShow": false  // If this parameter is set to **false**, notifications are not displayed when the app is running in the foreground.
        **}**
      },
      "target": {
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
      },
      "pushOptions": {
        "testMessage": true
      }
    }
    
2.  Set **actions** to **action.ohos.push.listener** in **skills** of the ability configuration (**PushMessageAbility** used as an example here) in the **src/main/module.json5** file at the module level of the client-side project. (**This action can be defined for only one ability.**)
    
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
    
3.  In the **onCreate()** method of the existing **UIAbility** class with the **actions** parameter set (for details, see step 2) in the client-side project, call the [receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911)() method and set [PushType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section5507492425) to **DEFAULT** to obtain notification messages when the app is running in the foreground. The following sample code uses **PushMessageAbility** as an example:
    
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
          // The value of **receiveMessage** is always **DEFAULT**.
          pushService.receiveMessage('DEFAULT', this, (payload) => {
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
    

#### Implementing Custom Ringtones for Notification Messages

When a device receives a notification message, the default system notification ringtone is played. To implement custom ringtones, pass the **[sound](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117)** field in the REST API call request. This function is not supported for messages with **category** set to **MARKETING**. This function requires configurations on both the server and client sides. The steps are as follows:

1.  Place the custom ringtone file in the **/resources/rawfile** directory of the **client-side** project (for example, the value **alert.mp3** corresponds to the **/resources/rawfile/alert.mp3** file of the app on the device). Then recompile and reinstall the app package.
2.  Call the REST API on the **server side** to push a message and pass the **sound** field in the request body. The following is an example:
    
    // Request URL
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
    
    // Request Header
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
    push-type: 0
    
    // Request Body
    {
      "payload": {
        "notification": {
          "category": "TRAVEL", // Change it to the actual notification message type.
          "title": "Common notification title",
          "body": "Common notification body",
          "clickAction": {
            "actionType": 0
          },
          "notifyId": 12345,
          "sound": "alert.mp3",  // When **category** is set to **MARKETING**, this function is not supported.
          "soundDuration": 10  // This parameter must be used together with the **sound** parameter.
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
    
    -   **sound**: custom notification ringtone. This field is optional. The ringtone file specified here must be stored in the **/resources/rawfile** path of the app. For example, the value **alert.mp3** corresponds to the **/resources/rawfile/alert.mp3** file of the app on the device. For details, please refer to [sound](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117). When **category** is set to **MARKETING**, this function is not supported.
    -   **soundDuration** (optional): duration of the custom ringtone, in seconds. The value must be a number within the range \[1, 60\]. The **soundDuration** parameter must be used together with the **sound** parameter The custom ringtone specified by the **sound** parameter will be played until the duration reaches the value of **soundDuration**. If the duration of the custom ringtone is shorter than the value of **soundDuration**, it will loop until the specified time is reached. For details, please refer to [soundDuration](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section17371529101117).
