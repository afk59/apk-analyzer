# App-to-App Message Communications

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/vkLjdrYfSvW9aWlZFCUPhQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F78D2D0D953880F7AA763E3BD06FDFF5010A87D545CBB370B707E5AE1EF9B1ED)

-   Before using this function, ensure that you have your app installed on the peer device. (For details, refer to [Phone App Development](../../phone-app-development/document.md).)
-   Both the app on the peer device and the app on the wearable device must be launched.

#### Checking Whether the App Has Been Installed on the Peer Device

1.  Select the peer device to communicate with from the list of connected devices by referring to [Querying Connected Peer Devices](../querying-connected-peer-devices/document.md).

2.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
3.  Call the [isRemoteAppInstalled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section28747514219) method to check whether the specified app has been installed on the peer device.
    
    // Define the peer-device-side app bundle name as **remoteBundleName**.
    let remoteBundleName: string = '';
    
    // Step 2: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 3: Check whether the specified app has been installed on the peer device.
    p2pClient.isRemoteAppInstalled(targetDevice.randomId, remoteBundleName).then((isInstall) => {
      console.info(\`Succeeded in checking remote app install, result is ${isInstall}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.\`);
    })
    

#### Sending P2P Messages or Files to the Peer-Device-Side App

The maximum size of a message is 4096 bytes. If the size of a message exceeds the limit, the message can be divided into several packets or files (with each no larger than 100 MB) for sending.

If the wearable app is able to send messages and files, the peer-device-side app needs to support receiving these messages and files.

## Sending P2P Messages

To use the utility class to construct the message body, import the required module first.

import { util } from '@kit.ArkTS';

1.  Select the peer device to communicate with from the list of connected devices by referring to [Querying Connected Peer Devices](../querying-connected-peer-devices/document.md).
2.  Construct the peer-device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).
3.  Construct the [P2pMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section188531948121319) to be sent.

4.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
5.  Call the [sendMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10826949193413) method to send short messages from the wearable app to the peer-device-side app. Register a listener for the peer device, and the peer-device-side app will be able to receive messages from the wearable app.
    
    // Step 2: Construct the peer-device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      // Set the peer-device-side app information, including the bundle name and fingerprint.
      bundleName: '',
      fingerprint: ''
    }
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
    }
    
    // Set the message content to be sent, with a maximum length of 4096 bytes.
    let messageContent: string = 'this is message';
    
    //Step 3: Construct the message structure.
    let textEncoder: util.TextEncoder = new util.TextEncoder;
    let message: wearEngine.P2pMessage = {
      content: textEncoder.encodeInto(messageContent)
    }
    
    // Step 4: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 5: Send the message.
    p2pClient.sendMessage(targetDevice.randomId, appParam, message).then((p2pResult) => {
      console.info(\`Succeeded in sending message, result is ${p2pResult.code}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to send message. Code is ${error.code}, message is ${error.message}.\`);
    })
    

## Sending Files

To open the file descriptor before sending a file, import the module below first.

import { fileIo } from '@kit.CoreFileKit';

1.  Select the peer device to communicate with from the list of connected devices by referring to [Querying Connected Peer Devices](../querying-connected-peer-devices/document.md).
2.  Construct the peer-device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).

3.  Construct the [P2pFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1223384152) to be sent based on **filePath**.
4.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
5.  Call the [transferFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section16802133114448) method to send a file from the wearable app to the peer-device-side app.
    
    // Step 2: Construct the peer-device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      // Set the peer-device-side app information, including the bundle name and fingerprint.
      bundleName: '',
      fingerprint: ''
    }
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
    }
    
    // Step 3: Construct the file to be sent.
    let p2pfile: wearEngine.P2pFile = {
      // Set the file path to be sent, which should not contain '..'.
      file: fileIo.openSync('')
    }
    
    // Step 4: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 5: Send the specified file to the peer device.
    p2pClient.transferFile(targetDevice.randomId, appParam, p2pfile, (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
      // Callback processing logic.
      if (error) {
        console.error(\`Failed to transfer file. Code is ${error.code}, message is ${error.message}.\`);
        return;
      }
      if (p2pResult.code) {
        if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION\_SUCCESS) {
          console.info(\`Succeeded in transferring file, the result is ${p2pResult.code}.\`);
        }
        console.info(\`Failed to transfer file, the error code is ${p2pResult.code}.\`);
      }
      if (p2pResult.progress) {
        console.info(\`Succeeded in transfering file, the progress is ${p2pResult.progress}.\`);
      }
    });
    
    fileIo.close(p2pfile.file);
    

#### Subscribing to and Receiving Messages Sent by the Peer-Device-Side App

1.  Select the peer device to communicate with from the list of connected devices by referring to [Querying Connected Peer Devices](../querying-connected-peer-devices/document.md).
2.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
3.  Construct the peer-device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).
4.  Construct the [Callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#callback) function for message receiving from the peer device.
5.  Call the [registerMessageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section893873771918) method to subscribe to message receiving events.
    
    // Step 2: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 3: Construct the peer-device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the peer-device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
    }
    
    // Step 4: Construct a callback function.
    let callback = (p2pMessage: wearEngine.P2pMessage) => {
      console.info(\`Succeeded in receiving message, the message is ${p2pMessage.content}.\`);
    }
    
    // Step 5: Subscribe to message receiving events.
    p2pClient.registerMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in registering message receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
    

6.  Call the [unregisterMessageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section13676139154415) method for the wearable app to cancel message reception from the peer-device-side app. The callback function passed should be the one used during subscription.
    
    p2pClient.unregisterMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in unregistering message receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
    

#### Subscribing to and Receiving Files Sent by the Peer-Device-Side App

1.  Select the peer device to communicate with from the list of connected devices by referring to [Querying Connected Peer Devices](../querying-connected-peer-devices/document.md).
2.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
3.  Construct the device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).
4.  Construct the [Callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#callback) function for file receiving from the peer device.
5.  Call the [registerFileReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1899163313713) method to subscribe to file receiving events.
    
    // Step 2: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 3: Construct the peer-device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the peer-device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
    }
    
    // Step 4: Construct a callback function.
    let callback = (p2pMessage: wearEngine.P2pFile) => {
      console.info(\`Succeeded in receiving file.\`);
    }
    
    // Step 5: Subscribe to file receiving events.
    p2pClient.registerFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in registering file receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
    

6.  Call the [unregisterFileReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section146072474497) method for the wearable app to cancel file reception from the peer-device-side app. The callback function passed should be the one used during subscription.
    
    p2pClient.unregisterFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in unregistering file receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
    

#### Launching the Wearable App with the Peer-Device-Side App Using the **startRemoteApp** Method

Configure the page to be launched on the wearable device, for the peer-device-side app to call the **startRemoteApp** method to launch the wearable app.

1.  Create the **HiWearMainAbility.ets** file, which should be inherited from **UIAbility**. Rewrite the **onWindowStageCreate** function to configure the page to be redirected to.
    
    // Ensure to inherit **UIAbility**.
    import hilog from '@ohos.hilog';
    import UIAbility from '@ohos.app.ability.UIAbility';
    import window from '@ohos.window';
    
    /\*\*
     \* The peer-device-side app calls the **startRemoteApp** method to launch **HiWearMainAbility** of the wearable app.
     \*/
    export default class HiWearMainAbility extends UIAbility {
      onWindowStageCreate(windowStage: window.WindowStage): void {
        hilog.info(0x0000, 'HiWearMainAbility', '%{public}s', 'Ability onWindowStageCreate');
    
    // Configure the page to be redirected to as **XXXPage**.
        windowStage.loadContent("pages/XXXPage", (err, data) => {
          if (err.code) {
            hilog.error(0x0000, 'HiWearMainAbility', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
            return;
          }
          hilog.info(0x0000, 'HiWearMainAbility', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
        });
      }
    }
    
2.  Configure **HiWearMainAbility** in **abilities** of **module.json5**. For details, refer to [abilities](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md#abilities).
    
    -   Set **name** to **HiWearMainAbility**.
    -   Set **srcEntry** as the path of the **HiWearMainAbility.ets** file.
    -   Specify **startWindowIcon** as the index of the icon resource file on the **UIAbility** startup page.
    -   Specify **startWindowBackground** as the index of the background color resource file on the **UIAbility** startup page.
        
        "module": {
          "name": "xxxx",
          "type": "entry",
          "description": "xxxx",
          "mainElement": "xxxx",
          "deviceTypes": \[\],
          "pages": "xxxx",
          "abilities": \[
        	{
        	"name": "HiWearMainAbility",
        	"srcEntry": "xxxx",
        	"startWindowIcon": "xxxx", // Index of the icon resource file on the **UIAbility** startup page.
        	"startWindowBackground": "xxxx" // Index of the background color resource file on the **UIAbility** startup page.
          }\],
          "metadata": \[\]
          }
        
    
3.  Configure the following in **metadata** of **module.json5**: the peer-device-side app bundle name, the name of the ability to be started, and whether to wait for the wearable app to complete subscribing to message or file receiving.
    
    -   When configuring the peer-device-side app bundle name: Set **name** to **wearEngineRemoteAppNameList** and **value** to the peer-device-side app bundle name. If there are multiple app bundle names, separate them with commas (,). The maximum size of the value is 4 KB.
    -   When configuring the name of the ability to be started: Set **name** to **wearEngineUIAbilityName** and **value** to the name of the UIAbility to be started. If the parameters are not set, HiWearMainAbility is started by default.
    -   When configuring **AwaitRegisterReceiver**: Set **name** to **wearEngineAwaitRegisterReceiver** and **value** to **true** or **false**. The value **true** means to wait for the wearable app to complete subscribing to message or file receiving, and **false** means the opposite.
        
        "module": {
          "name": "xxxx",
          "type": "entry",
          "description": "xxxx",
          "mainElement": "xxxx",
          "deviceTypes": \[\],
          "pages": "xxxx",
          "abilities": \[\],
          "metadata": \[ // Configure the following information:
              {
                "name": "wearEngineRemoteAppNameList",
                "value": "xxxx1,xxxx2,xxxx3"
              },
              {
                "name": "wearEngineUIAbilityName",
                "value": "xxxx"
              },
              {
                "name": "wearEngineAwaitRegisterReceiver",
                "value": "true"
              }
          \]}
