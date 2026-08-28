# Querying Connected Wearable Devices

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/41/v3/iU6bs8h6R1ipmS0BRpddGA/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062025Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B294C5FFE90CEDC3528E63D0BC339D85278EB6C0C1C7AC8277B05B7C11BCB381)

To call this API, you need to apply for the basic device information permission on HUAWEI Developers. For details, please refer to [Applying for Integrating Wear Engine](../../getting-started/applying-for-integrating-wear-engine/document.md).

Wear Engine provides the API for querying the list of connected wearable devices (which are connected to the Huawei Health app on the phone and support Wear Engine).

You are advised to implement this API before calling other APIs of Wear Engine.

1.  Call the [getDeviceClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1892394201117) method in [wearEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api) to obtain the [DeviceClient](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section126321419369) object.
2.  Call the [getConnectedDevices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section1828213119411) method to query the list of connected wearable devices.
    
    // Before using Wear Engine, import the **wearEngine** and related modules.
    import { wearEngine } from '@kit.WearEngine';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Step 1: Obtain the **DeviceClient** object.
    // **this.getUIContext().getHostContext()** indicates the **Context** object of the app.
    let deviceClient: wearEngine.DeviceClient = wearEngine.getDeviceClient(this.getUIContext().getHostContext());
    // Create a device list to store the returned device data.
    let deviceList: wearEngine.Device\[\] = \[\];
    
    // Step 2: Call the **getConnectedDevices** method to query whether the user has a connected wearable device.
    deviceClient.getConnectedDevices().then(devices => {
      // Process the returned device list.
      deviceList = devices ;
      console.info(\`Succeeded in getting deviceList, deviceList number is ${deviceList.length}\`);
    }).catch((error: BusinessError) => {
      // Process the exception captured when the calling fails.
      console.error(\`Failed to get deviceList. Code is ${error.code}, message is ${error.message}\`);
    })
