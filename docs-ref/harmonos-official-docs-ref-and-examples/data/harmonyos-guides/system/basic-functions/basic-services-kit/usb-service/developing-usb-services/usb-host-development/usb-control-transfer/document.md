# USB Control Transfer

#### When to Use

The control transfer is used to obtain and set the device status, and control the device attribute status. You can determine whether the control transfer can read or write data based on the endpoint types supported by the device.

#### Preparing the Environment

## Environment Requirements

-   Development tool and configuration:
    
    DevEco Studio, as the driver development tool, allows you to develop, debug, and package drivers. [Download and install](https://developer.huawei.com/consumer/en/download/) DevEco Studio and verify basic operations to ensure that it can function properly. For details, see [Creating a Project](../../../../../../../environment-setup/creating-a-project/creating-a-project/document.md) in [DevEco Studio User Guide](../../../../../../../environment-setup/overview/document.md).
    
-   SDK version configuration:
    
    The ArkTs APIs for peripheral management can be used only when the SDK is of API version 16 or later.
    
-   HDC configuration:
    
    HarmonyOS Device Connector (hdc) is a command-line tool for debugging. It can be used to interact with real devices or the Emulators on Windows, Linux, and macOS. For details about the configuration, see [hdc](../../../../../../debugging-tools/performance-analysis-kit/command-line-tools/hdc/document.md).
    

## Environment Setup

-   Install [DevEco Studio](https://developer.huawei.com/consumer/en/download/) 4.1 or later on the PC.
-   Update the public SDK to API version 16 or later.
-   Install hdc on the PC. You can use it to interact with a real device or the Emulator on Windows, Linux, or macOS.
-   Use a USB cable to connect a device to the PC.

#### How to Develop

## Available APIs

| API | Description |
| :-- | :-- |
| usbControlTransfer(pipe: USBDevicePipe, requestparam: USBDeviceRequestParams, timeout?: number): Promise<number> | Performs control transfer. |

For details about the APIs of device management and transfer modes, see [@ohos.usbManager (USB Manager)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-usbmanager).

## Development Procedure

Connect a host to a device and use the **usbControlTransfer** API to transfer data. The following steps describe how to implement a control transfer:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/vRWJscN3Rx-NJbAVCsh-uA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39E28C8F16F6C8EAF9A364586A46FB7571567AFCB37BE38068335E44BD85F47C)

The following sample code shows only a basic process. You should execute the code in a specific method. When calling this method, you must comply with device protocols to ensure proper data transfer and device compatibility.

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
     Claim the corresponding interface from deviceList.
    interface1 must be one present in the device configuration.
    \*/
    usbManager.claimInterface(pipe, interface1, true);
    this.pipe\_ = pipe;
    this.interface\_ = interface1;
    console.info('open device success');
    this.logInfo\_ += '\\n\[INFO\] open device success';
    
5.  Perform data transfer.
    
    if (this.pipe\_ === undefined) {
      console.error('pipe\_ is null');
      this.logInfo\_ += '\\n\[ERROR\] pipe\_ is null';
      return;
    }
    let pipe: usbManager.USBDevicePipe = this.pipe\_;
    /\*
    Construct control transfer parameters.
    \*/
    let param: usbManager.USBDeviceRequestParams = {
      bmRequestType: 0x80, // 0x80 indicates a standard request for data transfer from the device to the host.
      bRequest: 0x06, // 0x06 indicates a request for the descriptor.
      wValue: 0x01 << 8 | 0, // The value is of two bytes. The high byte indicates the descriptor type. Here, 0x01 indicates the device descriptor. The low byte indicates the descriptor index. The value is set to 0 because it is not involved for the device descriptor.
      wIndex: 0, // Descriptor index. The value can be 0.
      wLength: 18, // Descriptor length. The value 18 indicates the length of a device descriptor. A maximum of 1024 characters are supported.
      data: new Uint8Array(18)
    };
    
    usbManager.usbControlTransfer(pipe, param).then((ret: number) => {
      console.info(\`usbControlTransfer = ${ret}\`);
      this.logInfo\_ += '\\n\[INFO\] usbControlTransfer = ' + JSON.stringify(ret);
    })
    
6.  Release the USB interface, and close the USB device pipe.
    
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
