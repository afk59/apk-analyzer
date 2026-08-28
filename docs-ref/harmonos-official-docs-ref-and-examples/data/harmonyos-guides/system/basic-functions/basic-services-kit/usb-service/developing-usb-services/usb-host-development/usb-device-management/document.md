# USB Device Management

#### When to Use

When a USB device is inserted, you can use **usbManager** to obtain basic information about the USB device, such as the device type and supported functions. The host communicates with the USB device through the encapsulated pipe. In HarmonyOS, the USB management service is the core component that manages the connection and communication with USB devices. With the USB management service, applications can detect the USB connection and disconnection, manage permission requests and device configurations of USB devices, and perform data transfer and device control.

#### Environment Preparation

## Environment Requirements

-   Development tool and configuration:
    
    DevEco Studio, as the driver development tool, allows you to develop, debug, and package drivers. [Download and install](https://developer.huawei.com/consumer/en/download/) DevEco Studio and verify basic operations to ensure that it can function properly. For details, see [Creating a Project](../../../../../../../environment-setup/creating-a-project/creating-a-project/document.md) in [DevEco Studio User Guide](../../../../../../../environment-setup/overview/document.md).
    
-   SDK version configuration:
    
    The ArkTs APIs for peripheral management can be used only when the SDK is of API version 16 or later.
    
-   HDC configuration:
    
    HarmonyOS Device Connector (hdc) is a command-line tool for debugging. It can be used to interact with real devices or the Emulator on Windows, Linux, and macOS. For details about the configuration, see [hdc](../../../../../../debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).
    

## Environment Setup

-   Install [DevEco Studio](https://developer.huawei.com/consumer/en/download/) 4.1 or later on the PC.
-   Update the public SDK to API version 16 or later.
-   Install hdc on the PC. You can use it to interact with a real device or the Emulator on Windows, Linux, or macOS.
-   Use a USB cable to connect a device to the PC.

#### How to Develop

## Available APIs

USB device management provides the following functions: querying the USB device list, controlling USB device permissions, and setting USB device configurations.

The following table lists the USB APIs currently available. For details, see [@ohos.usbManager (USB Manager)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-usbmanager).

**Table 1** Open USB APIs

| API | Description |
| :-- | :-- |
| hasRight(deviceName: string): boolean | Checks whether the USB has the device access permissions. |
| requestRight(deviceName: string): Promise<boolean> | Requests the temporary permission for the application to access the USB device. This API uses a promise to return the result. |
| removeRight(deviceName: string): boolean | Removes the device access permissions of the application. |
| connectDevice(device: USBDevice): Readonly<USBDevicePipe> | Connects to the USB device based on the device information returned by **getDevices()**. |
| getDevices(): Array<Readonly<USBDevice>> | Obtains the list of USB devices connected to the host. If no device is connected, an empty list is returned. |
| setConfiguration(pipe: USBDevicePipe, config: USBConfiguration): number | Sets the USB device configuration. |
| setInterface(pipe: USBDevicePipe, iface: USBInterface): number | Sets a USB interface. |
| claimInterface(pipe: USBDevicePipe, iface: USBInterface, force ?: boolean): number | Claims a USB interface. |
| closePipe(pipe: USBDevicePipe): number | Closes a USB device pipe. |
| releaseInterface(pipe: USBDevicePipe, iface: USBInterface): number | Releases a USB interface. |
| getFileDescriptor(pipe: USBDevicePipe): number | Obtains the file descriptor of a USB device. |
| getRawDescriptor(pipe: USBDevicePipe): Uint8Array | Obtains the raw USB descriptor. |

## How to Develop

A USB device can be used as a host to connect to a device for management. The procedure is as follows:

1.  Import modules.
    
    // Import the usbManager module.
    import { usbManager } from '@kit.BasicServicesKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { JSON } from '@kit.ArkTS';
    
2.  Obtain the USB device list.
    
    // Obtain the USB device list.
    let deviceList: usbManager.USBDevice\[\] = usbManager.getDevices();
    console.info(\`deviceList: ${deviceList}\`);
    this.logInfo\_ += '\\n\[INFO\] deviceList: ' + JSON.stringify(deviceList);
    if (deviceList === undefined || deviceList.length === 0) {
      console.error('deviceList is empty');
      this.logInfo\_ += '\\n\[ERROR\] deviceList is empty';
      return;
    }
    /\*
    Example deviceList structure:
    \[
      {
        name: '1-1',
        serial: '',
        manufacturerName: '',
        productName: '',
        version: '',
        vendorId: 7531,
        productId: 2,
        clazz: 9,
        subClass: 0,
        protocol: 1,
        devAddress: 1,
        busNum: 1,
        configs: \[
          {
            id: 1,
            attributes: 224,
            isRemoteWakeup: true,
            isSelfPowered: true,
            maxPower: 0,
            name: '1-1',
            interfaces: \[
              {
                id: 0,
                protocol: 0,
                clazz: 9,
                subClass: 0,
                alternateSetting: 0,
                name: '1-1',
                endpoints: \[
                  {
                    address: 129,
                    attributes: 3,
                    interval: 12,
                    maxPacketSize: 4,
                    direction: 128,
                    number: 1,
                    type: 3,
                    interfaceId: 0,
                  }
                \]
              }
            \]
          }
        \]
      }
    \]
    \*/
    this.deviceList\_ = deviceList;
    
3.  Obtain the device operation permissions.
    
    if (this.deviceList\_ === undefined || this.deviceList\_.length === 0) {
      console.error('deviceList is empty');
      this.logInfo\_ += '\\n\[ERROR\] deviceList is empty';
      return;
    }
    let deviceList: usbManager.USBDevice\[\] = this.deviceList\_;
    let deviceName: string = deviceList\[0\].name;
    // Request the permissions to operate a specified device.
    usbManager.requestRight(deviceName).then((hasRight: boolean) => {
      console.info('usb device request right result: ' + hasRight);
      this.logInfo\_ += '\\n\[INFO\] usb device request right result: ' + JSON.stringify(hasRight);
    }).catch((error: BusinessError) => {
      console.error(\`usb device request right failed : ${error}\`);
      this.logInfo\_ += '\\n\[ERROR\] usb device request right failed: ' + JSON.stringify(error);
    });
    
4.  Open the device.
    
    if (this.deviceList\_ === undefined || this.deviceList\_.length === 0) {
      console.error('deviceList\_ is empty');
      this.logInfo\_ += '\\n\[ERROR\] deviceList is empty';
      return;
    }
    let deviceList: usbManager.USBDevice\[\] = this.deviceList\_;
    if (!usbManager.hasRight(deviceList\[0\]?.name)) {
      console.error('permission denied');
      this.logInfo\_ += '\\n\[ERROR\] permission denied';
      return;
    }
    // Open the device, and obtain the USB device pipe for data transfer.
    let pipe: usbManager.USBDevicePipe = usbManager.connectDevice(deviceList\[0\]);
    if (!deviceList?.\[0\]?.configs?.\[0\]?.interfaces?.\[0\]) {
      console.error('invalid interface');
      this.logInfo\_ += '\\n\[ERROR\] invalid interface';
      return;
    }
    let interface1: usbManager.USBInterface = deviceList?.\[0\]?.configs?.\[0\]?.interfaces?.\[0\];
    /\*
     Claim the corresponding interface from \*\*deviceList\*\*.
    interface1 must be one present in the device configuration.
    \*/
    usbManager.claimInterface(pipe, interface1, true);
    this.pipe\_ = pipe;
    this.interface\_ = interface1;
    console.info('open device success');
    this.logInfo\_ += '\\n\[INFO\] open device success';
    
5.  Release the USB interface, and close the USB device.
    
    if (this.pipe\_ === undefined || this.interface\_ === undefined) {
      console.error('pipe\_ or interface\_ is null');
      this.logInfo\_ += '\\n\[ERROR\] pipe\_ or interface\_ is null';
      return;
    }
    let pipe: usbManager.USBDevicePipe = this.pipe\_;
    let interface1: usbManager.USBInterface = this.interface\_;
    usbManager.releaseInterface(pipe, interface1);
    usbManager.closePipe(pipe);
    this.pipe\_ = undefined;
    this.interface\_ = undefined;
    console.info('close device success');
    this.logInfo\_ += '\\n\[INFO\] close device success';
