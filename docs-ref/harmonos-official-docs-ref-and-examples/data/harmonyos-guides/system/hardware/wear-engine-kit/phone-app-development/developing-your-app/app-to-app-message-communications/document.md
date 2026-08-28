# App-to-App Message Communications

This API is used to establish the communications channel between your phone app and wearable app, to receive and send packet messages and files customized by your apps. This makes the interaction between the phone app and its wearable counterpart a full-fledged reality, providing the distributed scenarios and experience for your users. For example, a phone app sends an audio file to the wearable app, to play music on the wearable app; the phone app sends a pause command, to pause the music playback on the wearable device.

Before sending or receiving P2P messages, apply for the basic device information permission on HUAWEI Developers by referring to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md). Otherwise, the API calling will fail.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/vTuPpGy-To6cwz7AmZcyMQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11AE1C2FCD268817537F5A3513947DF3EA4AA35685DB250DEBD0223F1C13916A)

Before using this feature, ensure that the wearable device supports the app installation capability (by referring to [Selecting a Target Device](../selecting-a-target-device/document.md#section15715111213569)) and the app has been installed on the wearable device (by referring to [Wearable App Development](https://developer.huawei.com/consumer/en/doc/connectivity-Guides/watch-dev-0000001119195134)).

-   Both the phone app and wearable app must be launched.
-   If the phone app is launched while the wearable app is not, the phone app can launch the other one through [startRemoteApp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section169404201361).

#### Checking Whether the Wearable App Has Been Installed

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/DGbpeCxsQVWBuFrvohtlww/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=16F1C8907AF939C8D394D0291B2D54D4656F6D6F3CF8C4E07005674601CF8355)

To call this API, you need to apply for the basic device information permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).

3.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
4.  Call the [isRemoteAppInstalled](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section28747514219) method to check whether the specified app has been installed.
    
    // Define the device-side app bundle name as **remoteBundleName**.
    let remoteBundleName: string = '';
    
    // Step 3: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 4: Check whether the specified app has been installed on the device.
    p2pClient.isRemoteAppInstalled(targetDevice.randomId, remoteBundleName).then((isInstall) => {
      console.info(\`Succeeded in checking remote app install, result is ${isInstall}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to check remote app install. Code is ${error.code}, message is ${error.message}.\`);
    })
    

#### Obtaining the Wearable App's Version Number

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/ieEzoKq_TNun-oj7xG3zUg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=919D958E63CAD9EE7E229CE362E87E5C4D32909F3F615C89B3B0B94B29B5464C)

To call this API, you need to apply for the basic device information permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).

3.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
4.  Call the [getRemoteAppVersion](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1737133513289) method to obtain the app version number of a specified device.
    
    // Define the device-side app bundle name as **remoteBundleName**.
    let remoteBundleName: string = '';
    
    // Step 3: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 4: Obtain the app version number of a specified device.
    p2pClient.getRemoteAppVersion(targetDevice.randomId, remoteBundleName).then((version) => {
      console.info(\`Succeeded in getting remote app version, version is ${version}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to check get remote app version. Code is ${error.code}, message is ${error.message}.\`);
    })
    

#### Launching the Device-side App with the Phone-side App

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/PMzyBcrARtq1H-GhVQ--2g/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7EDA0051C5A68E9715E7289CE99A9202C4C1290E7271D020947B4C5C90B7999)

To call this API, you need to apply for the basic device information permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

Before sending a P2P message, you can use the [startRemoteApp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section169404201361) method to launch the device-side app.

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
4.  Call the [startRemoteApp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section169404201361) method to specify the device-side app bundle name to be launched. The default value of [transformLocalBundleName](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section169404201361) is **false**. If **true** is passed, Wear Engine will convert the local bundle name and fingerprint to match those stored on the cloud for compatible apps. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).
    
    // Define the device-side app bundle name as **remoteBundleName**.
    let remoteBundleName: string = '';
    
    // Step 3: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
      
    // Step 4: Launch the specified device-side app (**transformLocalBundleName** defaults to **false**).
    p2pClient.startRemoteApp(targetDevice.randomId, remoteBundleName).then((p2pResult) => {
      console.info(\`Succeeded in starting remote app, result is ${p2pResult.code}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to start remote app. Code is ${error.code}, message is ${error.message}.\`);
    })
    

#### Sending P2P Messages or Files to Your Wearable App

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/PNgp6FMfTUC_LDpqDb91CA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=63BC6A842883D0950BA7B799D5D20725552928B99A757604A545DA99357C634C)

To call this API, you need to apply for the basic device information permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

The maximum size of a message is 4096 bytes. If the size of a message exceeds the limit, the message can be divided into several packets or files (with each no larger than 100 MB) for sending.

If the phone app is able to send messages and files, the wearable app need to support receiving these messages and files.

## Sending P2P Messages

To use the utility class to construct the message body, import the required module first.

import { util } from '@kit.ArkTS';

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Construct the device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).
4.  Construct the [P2pMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section188531948121319) to be sent.

5.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
6.  Call the [sendMessage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10826949193413) method to send short messages from your phone app to the wearable app. Register a listener for the wearable device, and the wearable app will be able to receive messages from the phone.
    
    // Step 3: Construct device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      // Set the device-side app information, including the bundle name and fingerprint.
      bundleName: '',
      fingerprint: ''
    }
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    
    // Set the message content to be sent, with a maximum length of 4096 bytes.
    let messageContent: string = 'this is message';
    
    //Step 4: Construct the message structure.
    let textEncoder: util.TextEncoder = new util.TextEncoder;
    let message: wearEngine.P2pMessage = {
      content: textEncoder.encodeInto(messageContent)
    }
    
    // Step 5: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 6: Send the message.
    p2pClient.sendMessage(targetDevice.randomId, appParam, message).then((p2pResult) => {
      console.info(\`Succeeded in sending message, result is ${p2pResult.code}.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to send message. Code is ${error.code}, message is ${error.message}.\`);
    })
    

## Sending Files

Import the module below before you open the file descriptor.

import { fileIo } from '@kit.CoreFileKit';

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Construct the device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).

4.  Construct the [P2pFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1223384152) to be sent based on **filePath**.
5.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
6.  Call the [transferFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section16802133114448) method and send a file using your phone app to the wearable app.
    
    // Step 3: Construct device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      // Set the device-side app information, including the bundle name and fingerprint.
      bundleName: '',
      fingerprint: ''
    }
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    
    // Step 4: Construct the file to be sent.
    let p2pfile: wearEngine.P2pFile = {
      // Set the file path to be sent, which should not contain '..'.
      file: fileIo.openSync('')
    }
    
    // Step 5: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 6: Send the specified file to the device.
    p2pClient.transferFile(targetDevice.randomId, appParam, p2pfile, (error: BusinessError, p2pResult: wearEngine.P2pResult) => {
      // Callback processing logic.
      if (error) {
        console.error(\`Failed to transfer file. Code is ${error.code}, message is ${error.message}.\`);
        return;
      }
      if (p2pResult.code) {
        if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION\_SUCCESS) {
          console.info(\`Succeeded in transferring file, the result is ${p2pResult.code}.\`);
        } else {
          console.info(\`Failed to transfer file, the error code is ${p2pResult.code}.\`);
          return;
        }
      }
      if (p2pResult.progress) {
        console.info(\`Succeeded in transferring file, the progress is ${p2pResult.progress}.\`);
      }
    });
    
    fileIo.close(p2pfile.file);
    

## Canceling the File Sending Task

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Construct the device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).

4.  Construct the [P2pFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1223384152) to be canceled for sending based on **filePath**.
5.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
6.  Call the [cancelFileTransfer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section67354131415) method to cancel the file transfer from your phone app to the wearable app.
    
    // Step 3: Construct device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      // Set the device-side app information, including the bundle name and fingerprint.
      bundleName: '',
      fingerprint: ''
    }
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    
    // Step 4: Construct the file to be sent.
    let p2pfile: wearEngine.P2pFile = {
      // Set the file path to be sent, which should not contain '..'.
      file: fileIo.openSync('')
    }
    
    // Step 5: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Send the specified file to the device.
    p2pClient.transferFile(targetDevice.randomId, appParam, p2pfile, () => {
      // Execution logic of the callback function.
    })
    
    // Step 6: Cancel the file sending.
    p2pClient.cancelFileTransfer(targetDevice.randomId, appParam, p2pfile).then((p2pResult) => {
      if (p2pResult.code === wearEngine.P2pResultCode.COMMUNICATION\_SUCCESS) {
        console.info(\`Succeeded in cancelling transfer file, the result is ${p2pResult.code}.\`);
      }
    }).catch((error: BusinessError) => {
      console.error(\`Failed to cancel transfer file. Code is ${error.code}, message is ${error.message}.\`);
    })
    
    fileIo.close(p2pfile.file);
    

#### Subscribing to and Receiving Messages Sent by the Wearable App

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/g6qkx61xTQKtkcz5ZHa5UQ/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062026Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6212C9A9E51EDA33FFDECD0213D416CEFD2C04D13B64EE9638B283A5EE11364)

To call this API, you need to apply for the basic device information permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
4.  Construct the device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).
5.  Construct the [Callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#callback) function for message receiving from the device.
6.  Call the [registerMessageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section893873771918) method to subscribe to message receiving events.
    
    // Step 3: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 4: Construct device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    
    // Step 5: Construct a callback function.
    let callback = (p2pMessage: wearEngine.P2pMessage) => {
      console.info(\`Succeeded in receiving message, the message is ${p2pMessage.content}.\`);
    }
    
    // Step 6: Subscribe to message receiving events.
    p2pClient.registerMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in registering message receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to register message receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
    

7.  Call the [unregisterMessageReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section13676139154415) method for the phone app to cancel message reception from the wearable app. The callback function passed should be the one used during subscription.
    
    p2pClient.unregisterMessageReceiver(targetDevice.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in unregistering message receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to unregister message receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
    

#### Subscribing to and Receiving Files Sent by the Wearable App

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices by referring to [Selecting a Target Device](../selecting-a-target-device/document.md).
3.  Call the [getP2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section15604103515412) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [P2pClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section10175450143316) object.
4.  Construct the device-side app parameter [P2pAppParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section7874153142020).
5.  Construct the [callback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-base#callback) function for file receiving from the peer device.
6.  Call the [registerFileReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1899163313713) method to subscribe to file receiving events.
    
    // Step 3: Obtain the **P2pClient** object.
    let p2pClient: wearEngine.P2pClient = wearEngine.getP2pClient(this.getUIContext().getHostContext());
    
    // Step 4: Construct device-side app parameters.
    let appInfo: wearEngine.AppInfo = {
      bundleName: '',
      fingerprint: ''
    }
    // Define the device-side app parameter class as **appParam**.
    let appParam: wearEngine.P2pAppParam = {
      remoteApp: appInfo
      // The default value of **transformLocalAppInfo** is **false**, indicating that the bundle name and fingerprint are not converted.
    }
    
    // Step 5: Construct a callback function.
    let callback = (p2pMessage: wearEngine.P2pFile) => {
      console.info(\`Succeeded in receiving file.\`);
    }
    
    // Step 6: Subscribe to file receiving events.
    p2pClient.registerFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in registering file receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to register file receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
    

7.  Call the [unregisterFileReceiver](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section146072474497) method for the phone app to cancel file reception from the wearable app. The callback function passed should be the one used during subscription.
    
    p2pClient.unregisterFileReceiver(targetDevice.randomId, appParam, callback).then(() => {
      console.info(\`Succeeded in unregistering file receiver.\`);
    }).catch((error: BusinessError) => {
      console.error(\`Failed to unregister file receiver. Code is ${error.code}, message is ${error.message}.\`);
    })
