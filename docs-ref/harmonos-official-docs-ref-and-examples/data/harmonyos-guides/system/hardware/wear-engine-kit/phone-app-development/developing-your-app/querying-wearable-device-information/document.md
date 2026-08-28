# Querying Wearable Device Information

// Before using Wear Engine, import the **wearEngine** and related modules.
import { wearEngine } from '@kit.WearEngine';
import { BusinessError } from '@kit.BasicServicesKit';

#### Querying Whether the Wearable Device Supports Certain Wear Engine Capabilities

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/Tuvf6A2eSFa_5yJrV2wKkg/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=03E25565E398D8F7256DC97A3170954F85B9B6C3E16DED4E64E0C6BAC2A094F5)

To call this API, you need to apply for the basic device information permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

Call the [isWearEngineCapabilitySupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section116382923217) method in the [Device](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section385118379447) object to query whether the wearable device supports certain Wear Engine capabilities.

1.  Call the [getDeviceClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1892394201117) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [DeviceClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section126321419369) object.
    
    let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
    
2.  Call the [getConnectedDevices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1828213119411) method to obtain the connected device list.
    
    let deviceList: wearEngine.Device\[\] = \[\];
    deviceClient.getConnectedDevices().then(devices => {
      // Store the list of connected devices.
      deviceList = devices;
      console.info(\`Succeeded in getting deviceList, devices number is ${deviceList.length}\`);
    }).catch((error: BusinessError) => {
      // Process the exception captured when the calling fails.
      console.error(\`Failed to get deviceList. Code is ${error.code}, message is ${error.message}\`);
    })
    
3.  Select the target device from the device list.
4.  Call [isWearEngineCapabilitySupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section116382923217) in the [Device](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section385118379447) object to query whether this device supports the passed Wear Engine capability (**true**: supported; **false**: not supported). The following uses the P2P capability as an example.
    
    if (deviceList.length > 0) {
      // Step 3 Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
      let targetDevice: wearEngine.Device = deviceList\[0\];
    
      // Step 4 Call the method to check whether certain Wear Engine capability is supported (the P2P capability is used as an example).
      targetDevice.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.P2P\_COMMUNICATION).then((isSupportP2P) => {
        console.info(\`Succeeded in checking p2p capability, result is ${isSupportP2P}\`);
      }).catch((error: BusinessError) => {
        console.error(\`Failed to check p2p capability. Code is ${error.code}, message is ${error.message}\`);
      })
    }
    

#### Querying Whether the Wearable Device Supports Certain Device Capabilities

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/Od2dtLEIREy_Fd-7mSwA7Q/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FAD7769051B4F26642F52A458E91D6A8D8C90827BCECB19412149B18E697102)

To call this API, you need to apply for the basic device information permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

Call the [isDeviceCapabilitySupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section196921253123213) method in the [Device](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section385118379447) object to query whether the wearable device supports certain Device capabilities.

1.  Call the [getDeviceClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1892394201117) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [DeviceClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section126321419369) object.
    
    let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
    
2.  Call the [getConnectedDevices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1828213119411) method to obtain the connected device list.
    
    let deviceList: wearEngine.Device\[\] = \[\];
    deviceClient.getConnectedDevices().then(devices => {
      // Store the list of connected devices.
      deviceList = devices;
      console.info(\`Succeeded in getting deviceList, devices number is ${deviceList.length}\`);
    }).catch((error: BusinessError) => {
      // Process the exception captured when the calling fails.
      console.error(\`Failed to get deviceList. Code is ${error.code}, message is ${error.message}\`);
    })
    
3.  Select the target device from the device list.
4.  Call [isDeviceCapabilitySupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section196921253123213) in the [Device](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section385118379447) object to query whether this device supports the passed device capability (**true**: supported; **false**: not supported).
    
    if (deviceList.length > 0) {
      // Step 3 Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
      let targetDevice: wearEngine.Device = deviceList\[0\];
    
      // Step 4 Call the device method to query whether a certain device capability is supported (the app installation capability is used as an example).
      targetDevice.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION).then((isSupportInstall) => {
        console.info(\`Succeeded in checking install app capability, result is ${isSupportInstall}\`);
      }).catch((error: BusinessError) => {
        console.error(\`Failed to check install app capability. Code is ${error.code}, message is ${error.message}\`);
      })
    }
    

#### Querying the Device SN

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/hXP3dOgxRE67huII2rp6ww/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=203344F44676F842BB1983BA5FF4D6DEE46AED72D1CC01926A7AFB411B8D7C36)

To call this API, you need to apply for the device identifier permission (restricted) on HUAWEI Developers and obtain user authorization. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

Call the [getSerialNumber](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section164908590339) method in the [Device](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section385118379447) object to query the SN of the wearable device.

1.  Call the [getDeviceClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1892394201117) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [DeviceClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section126321419369) object.
    
    let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
    
2.  Call the [getConnectedDevices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1828213119411) method to obtain the connected device list.
    
    let deviceList: wearEngine.Device\[\] = \[\];
    deviceClient.getConnectedDevices().then(devices => {
      // Store the list of connected devices.
      deviceList = devices;
      console.info(\`Succeeded in getting deviceList, devices number is ${deviceList.length}\`);
    }).catch((error: BusinessError) => {
      // Process the exception captured when the calling fails.
      console.error(\`Failed to get deviceList. Code is ${error.code}, message is ${error.message}\`);
    })
    
3.  Select the target device from the device list.
4.  Call the [getSerialNumber](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section164908590339) method in the [Device](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section385118379447) object to query the SN of the wearable device.
    
    if (deviceList.length > 0) {
      // Step 3 Select the target device from the obtained device list and define it as **device**. (Assume that there are connected devices in the array and the first one is the target device.)
      let targetDevice: wearEngine.Device = deviceList\[0\];
    
      //Step 4 Call the device method to query the SN.
      targetDevice.getSerialNumber().then((sn) => {
        console.info(\`Succeeded in getting device SN, result is ${sn}\`);
      }).catch((error: BusinessError) => {
        console.error(\`Failed to get device SN. Code is ${error.code}, message is ${error.message}\`);
      })
    }
