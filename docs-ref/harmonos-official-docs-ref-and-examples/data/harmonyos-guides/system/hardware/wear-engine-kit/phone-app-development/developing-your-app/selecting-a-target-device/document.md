# Selecting a Target Device

If the list of connected devices contains more than one device, you need to select the target device as needed.

#### Selecting a Device Type

The [DeviceCategory](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section145591125155713) field in the [Device](https://developer.huawei.com/consumer/en/doc/harmonyos-references/wearengine_api#section385118379447) class indicates the device type, and you can use this field to select the target device.

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices based on the device type.
    
    // Declare the target device.
    let targetDevice: wearEngine.Device;
    for (let index = 0; index < deviceList.length; index++) {
      // Select devices of the watch type.
      if (deviceList\[index\].category === wearEngine.DeviceCategory.WATCH) {
        targetDevice = deviceList\[index\];
        break;
      }
      if (index === deviceList.length - 1) {
        // An error is thrown if the target device does not exist.
        throw new Error('cannot find target device');
      }
    }
    // An error is thrown if **targetDevice** is **undefined**.
    if (!targetDevice) {
        throw new Error('The value of targetDevice is undefined');
    }
    

#### Selecting Devices Supporting Certain Capabilities

Query the capabilities supported by the obtained devices by referring to [Querying Wearable Device Information](../querying-wearable-device-information/document.md).

## Selecting the Target Device Supporting Certain Wear Engine Capabilities

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices based on the supported Wear Engine capabilities.
    
    async function fun() {
    // Declare the target device.
      let targetDevice: wearEngine.Device;
      for (let index = 0; index < deviceList.length; index++) {
        // Select devices of the watch type.
        if (await device.isWearEngineCapabilitySupported(wearEngine.WearEngineCapability.MONITOR)) {
          targetDevice = deviceList\[index\];
          break;
        }
        if (index === deviceList.length - 1) {
        // An error is thrown if the target device does not exist.
          throw new Error('cannot find target device');
        }
      }
      // An error is thrown if **targetDevice** is **undefined**.
      if (!targetDevice) {
        throw new Error('The value of targetDevice is undefined.');
      }
    }
    

## Selecting the Target Device Supporting Certain Device Capabilities

1.  Obtain the list of connected wearable devices by referring to [Querying Connected Wearable Devices](../querying-connected-wearable-devices/document.md).
2.  Select the device to communicate with from the list of connected devices based on the supported device capabilities.
    
    async function fun() {
    // Declare the target device.
      let targetDevice: wearEngine.Device;
      for (let index = 0; index < deviceList.length; index++) {
        // Select devices of the watch type.
        if (await device.isDeviceCapabilitySupported(wearEngine.DeviceCapability.APP\_INSTALLATION)) {
          targetDevice = deviceList\[index\];
          break;
        }
        if (index === deviceList.length - 1) {
        // An error is thrown if the target device does not exist.
          throw new Error('cannot find target device');
        }
      }
      // An error is thrown if **targetDevice** is **undefined**.
      if (!targetDevice) {
        throw new Error('The value of targetDevice is undefined.');
      }
    }
