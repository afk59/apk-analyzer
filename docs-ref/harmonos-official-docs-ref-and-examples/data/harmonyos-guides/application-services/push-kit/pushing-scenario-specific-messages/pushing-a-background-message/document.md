# Pushing a Background Message

#### Use Cases

Background messages are for scenarios where content updates are not frequent. They operate discreetly, without the usual notifications, ringtones, or app badge number changes. Upon receiving a background message, the device will transfer the message to the app if the app is currently running in the foreground. Otherwise, the message will be cached for later delivery after the app is launched.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/_AOW9IANSayZ96PKc7CTXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59A2AD8AB28BAA8CD492E01EA17AD81C07D4630B983FF64658831A8CD7B5E99B)

The device caches only the latest message for up to seven days by default.

#### Restrictions

The function of sending background messages supports phones, tablets, PCs, 2-in-1 devices, (since 5.1.0(18)) wearables, and (since 5.1.1(19)) TVs.

#### Frequency Control

**During the debugging phase**, the maximum number of test messages that can be pushed for each project every day is 1000. To send test messages, you need to set [testMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section418321011212) to **true**.

**After formal release**, the total number of messages that each app can push to a single device is subject to the limits specified in the [frequency control policy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-msg-freq-control#section993063213715). The total number of scenario-specific messages that can be pushed on a daily basis to each device cannot exceed 3000.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/9LFDdunNRu-DnFlkBaDm4g/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D1BAE6C56AE346B5D769F89AAE01FB8D8AF76FA6FA4C4DBA222DA49C42865BB)

-   Background messages are of a lower priority. To ensure delivery, it is advisable to limit background message frequency to no more than two per hour.
-   Factors such as the device battery level, system sleep, and user interactions can affect the timely delivery of background messages.

#### Development Procedure

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/cIGIIgH5SeWuHmOy-W4rIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062116Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1C9547A31FAE23E328FBB8795353BF3032D30D77995D5F9228794AF5D96D61E3)

You can choose a message cache policy based on your needs when the app process is not running in the foreground:

-   If you only need to cache the latest message on the device, you can perform step 2 to step 4.
-   If you want to cache more messages on the device, complete step 2 to step 4 to develop and adapt an on-device database and enable proxy-based data writing to the database. Push Kit will write background messages to the database. After your app process is running in the foreground, it will read messages from the database by itself.

1.  Complete operations in [Obtaining a Push Token](../../preparations/obtaining-a-push-token/document.md).
2.  (Optional) Create an on-device database (for example, **pushmessage.db**) by referring to [guide](../../../../application-framework/arkdata/application-data-persistence/persisting-rdb-store-data-arkts/document.md) and create a table (for example, **t\_push\_message**) in the following format.
    
    | 
    Field
    
     | 
    
    Type
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- |
    | 
    
    id
    
     | 
    
    INTEGER
    
     | 
    
    Auto-increment primary key.
    
     |
    | 
    
    message\_id
    
     | 
    
    TEXT
    
     | 
    
    Message ID.
    
     |
    | 
    
    push\_type
    
     | 
    
    TEXT
    
     | 
    
    Scenario type.
    
     |
    | 
    
    message\_action
    
     | 
    
    INTEGER
    
     | 
    
    Message action.
    
     |
    | 
    
    message
    
     | 
    
    TEXT
    
     | 
    
    Message body. The structure is as follows:
    
    {
      data: extraData in the message body.
    }
    
     |
    | 
    
    field1
    
     | 
    
    TEXT
    
     | 
    
    Extended field 1.
    
     |
    | 
    
    field2
    
     | 
    
    TEXT
    
     | 
    
    Extended field 2.
    
     |
    | 
    
    field3
    
     | 
    
    TEXT
    
     | 
    
    Extended field 3.
    
     |
    | 
    
    field4
    
     | 
    
    TEXT
    
     | 
    
    Extended field 4.
    
     |
    | 
    
    field5
    
     | 
    
    TEXT
    
     | 
    
    Extended field 5.
    
     |
    | 
    
    create\_time
    
     | 
    
    INTEGER
    
     | 
    
    Timestamp when a message is written into the database, in milliseconds.
    
     |
    
3.  (Optional) Create the **PushMessage.json** file under **src/main/resources/base/profile/** at the module level. The file content is as follows:
    
    {
      "path": "pushmessage/t\_push\_message",
      "type": "rdb",
      "scope": "application"
    }
    
    -   **path**: path of the table created in step 2, in the format **\[_Database name_\]/\[_Table name_\]**, for example, **pushmessage/t\_push\_message**.
    -   **type**: The value is always **rdb**, indicating a relational database.
    -   **scope**: database level. The options are **application** (app level) and **module** (HAP module level).
    
4.  (Optional) Add the following **proxyData** configuration to the **src/main/module.json5** file under the module-level directory of your project:
    
    {
      "module": {
        "proxyData":\[{
          "uri": "datashareproxy://{bundleName}/PushMessage",
          "requiredWritePermission": "ohos.permission.WRITE\_PRIVACY\_PUSH\_DATA",
          "metadata":{
            "name": "dataProperties",
            "resource": "$profile:PushMessage"
          }
        }\]
      }
    }
    
    -   **uri**: The value is in format **datashareproxy://_{bundleName}_/PushMessage**. You need to replace _{bundleName}_ with the package name of your app. **PushMessage** is a fixed value and cannot be changed.
    -   **requiredWritePermission**: The value is always **ohos.permission.WRITE\_PRIVACY\_PUSH\_DATA**, which allows Push Kit to write background message data to the database.
    -   **metadata**: extended configuration. The value of **name** is fixed to **dataProperties**. The value of **resource** must be in the format **$profile:_File name_**. The file name should be **PushMessage**.
    
5.  In the **onCreate()** method of the existing **UIAbility** class in your project, call the [receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911)() method to receive notification messages. The following sample code uses **PushMessageAbility** as an example: Note that you can only use **UIAbility** to receive background messages.
    
    import { UIAbility } from '@kit.AbilityKit';
    import { pushService, pushCommon } from '@kit.PushKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    /\*\*
     \* PushMessageAbility is used as an example for receiving background messages.
     \*/
    export default class PushMessageAbility extends UIAbility {
      onCreate(): void {
        try {
          pushService.receiveMessage('BACKGROUND', this, (data: pushCommon.PushPayload) => {
            // Process the message. You are advised to add a try-catch block for the callback.
            try {
              hilog.info(0x0000, 'testTag', 'Receive background message');
            } catch (e) {
              let errRes: BusinessError = e as BusinessError;
              hilog.error(0x0000, 'testTag', 'Failed to process data: %{public}d %{public}s', errRes.code, errRes.message);
            }
          });
        } catch (err) {
          let e: BusinessError = err as BusinessError;
          hilog.error(0x0000, 'testTag', 'Failed to get background message: %{public}d %{public}s', e.code, e.message);
        }
      }
    }
    
6.  Set **actions** to **action.ohos.push.listener** in **skills** in the **abilities** section of the **src/main/module.json5** file at the project level. (This action can be defined for only one ability. **If the uris parameter also exists, it should be left empty.**)
    
    "abilities": \[
      {
        "name": "PushMessageAbility",
        "srcEntry": "./ets/abilities/PushMessageAbility.ets",
        "launchType": "singleton",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": false,
        "skills": \[
          {
            "actions": \[
              "action.ohos.push.listener"
            \]
          }
        \]
      }
    \]
    
7.  Call the REST API provided by Push Kit from your app server to send a background message. For details, please refer to [Scenario-Specific Message API Description](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-intro). The following is a request example:
    
    // Request URL
    POST https://push-api.cloud.huawei.com/v3/**\[projectId\]**/messages:send
    
    // Request Header
    Content-Type: application/json
    Authorization: Bearer eyJr\*\*\*\*\*OiIx---\*\*\*\*.eyJh\*\*\*\*\*iJodHR--\*\*\*.QRod\*\*\*\*\*4Gp---\*\*\*\*
    **push-type: 6**
    
    // Request Body
    {
      "payload": {
        "extraData": "Extra data carried",
        "proxyData": "ENABLE"
      },
      "target": {
        "token": \["MAMzLg\*\*\*\*\*\*\*\*\*\*lPW"\]
      }
    }
    
    -   In the URL, **\[projectId\]** indicates the project ID. To obtain the project ID, sign in to [AppGallery Connect](https://developer.huawei.com/consumer/en/service/josp/agc/index.html), click **Development and services**, click the desired project, and go to the **Project settings** page.
    -   **Authorization**: a character string in JWT format. Obtain the value by referring to [Authorization](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-struct#section20573634202313).
    -   **push-type**: The value **6** indicates the background message type.
    -   **token**: push token. Obtain the token by referring to [Obtaining a Push Token](../../preparations/obtaining-a-push-token/document.md).
    -   **extraData**: extra data carried, which is a character string. For details, please refer to [extraData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section056120245274).
    -   **proxyData** (optional): indicates whether to enable the data proxy to silently write data to the app cache when the process does not exist. Currently, the value can only be **ENABLE** to enable the proxy. If you do not want to enable the proxy to write data, do not set this parameter in the message body. For details, please refer to [proxyData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section056120245274).
    
    When the app process is running in the foreground, the app is directly launched to transfer message data. You can call the [receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911)() method to obtain message data.
    
    When the app process is not running in the foreground and [proxyData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section056120245274) is set to **ENABLE**, Push Kit writes background message data to the database. You are advised to migrate the data from the database to your own service database once your app process is launched in the foreground to **prevent unlimited database growth**. When the app process is not running in the foreground and [proxyData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-scenariozed-api-request-param#section056120245274) is not set, messages are cached. **(If multiple messages are sent, only the latest message is cached.)** Once the app process is later launched in the foreground, call the [getToken](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section562973524818)() API so Push Kit will send the cached message again. You can call the [receiveMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/push-pushservice#section125883044911)() method to obtain the message data.
