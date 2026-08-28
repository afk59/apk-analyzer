# USB Bulk Transfer

#### When to Use

Bulk transfer is used to transfer and receive a large amount of data without bandwidth or interval requirements, for example, file or image transfer. Devices such as printers and scanners support this type of transfer.

#### Preparing the Environment

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

| API | Description |
| :-- | :-- |
| bulkTransfer(pipe: USBDevicePipe, endpoint: USBEndpoint, buffer: Uint8Array, timeout ?: number): Promise<number> | Performs bulk transfer. |

For details about the APIs of device management and transfer modes, see [@ohos.usbManager (USB Manager)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-usbmanager).

## Development Procedure

Connect a host to a device and use the **bulkTransfer** API to transfer data. The following steps describe how to implement a bulk transfer:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/99MYW8hrRZOczubSFKD3oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E52BA7B63A4CCC271E8E35FFE00B0DD04AC39CB9CFE57029E54B7CF7430D67DD)

The following sample code shows only a basic process. You should execute the code in a specific method. When calling this method, you must comply with device protocols to ensure proper data transfer and device compatibility.

1.  Import modules.
    
    // Import the usbManager module.
    import { usbManager } from '@kit.BasicServicesKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { JSON } from '@kit.ArkTS';
    
2.  Obtain the USB device list.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/02/v3/FvRvdk3PRDK1srhloTyQ_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13E8355E074D4C68F4C3A321B45AF0CE7E0F6B445DF83A9922C5C83AA3CE41C7)
    
    Bulk transfer can be performed only on the endpoint whose [transfer type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-usbmanager#usbendpointtransfertype18) is **2**. If an incorrect endpoint type is used, an I/O error is returned.
    
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
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/mD1_yoyPTZ-EmdO7a0mrZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C85362C8AAA3405BB24FDB5C00ED847D257E78998D31270E6CC61A8888E921EB)
    
    Before data transfer, you are advised to obtain the **type** of the **endpoint** to which the **interface** belongs and determine whether the **interface** supports the required transfer type.
    
    If the transfer API fails to be called, check whether the device interface supports [alternateSetting](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-usbmanager#usbinterface). If it is supported, you can call [usbManager.setInterface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-usbmanager#usbmanagersetinterface) to reset the **interface** before data transfer to match the endpoint with the transfer type, ensuring normal communications.
    
    if (this.pipe\_ === undefined || this.interface\_ === undefined) {
      console.error('pipe\_ or interface\_ is null');
      this.logInfo\_ += '\\n\[ERROR\] pipe\_ or interface\_ is null';
      return;
    }
    let pipe: usbManager.USBDevicePipe = this.pipe\_;
    let interface1: usbManager.USBInterface = this.interface\_;
    /\*
    Read data. Select the corresponding RX endpoint from deviceList for data transfer.
    (endpoint.direction == 0x80); dataUint8Array indicates the data to read. The data type is Uint8Array.
    \*/
    let inEndpoint: usbManager.USBEndpoint = interface1.endpoints?.\[1\];
    let outEndpoint: usbManager.USBEndpoint = interface1.endpoints?.\[0\];
    let dataUint8Array: Uint8Array = new Uint8Array(1024);
    if (inEndpoint !== undefined && inEndpoint.direction === 0x80) {
      usbManager.bulkTransfer(pipe, inEndpoint, dataUint8Array, 15000).then((dataLength: number) => {
        if (dataLength >= 0) {
          console.info(\`usb readData result Length : ${dataLength}\`);
          this.logInfo\_ += '\\n\[INFO\] usb readData result Length: ' + JSON.stringify(dataLength);
        } else {
          console.error('usb readData failed');
          this.logInfo\_ += '\\n\[ERROR\] usb readData failed';
        }
      }).catch((error: BusinessError) => {
        console.error(\`usb readData error : ${error}\`);
        this.logInfo\_ += '\\n\[ERROR\] usb readData error: ' + JSON.stringify(error);
      });
    }
    
    // Send data. Select the corresponding TX endpoint from deviceList for data transfer. (endpoint.direction == 0)
    if (outEndpoint !== undefined && outEndpoint.direction === 0) {
      usbManager.bulkTransfer(pipe, outEndpoint, dataUint8Array, 15000).then((dataLength: number) => {
        if (dataLength >= 0) {
          console.info(\`usb writeData result write length : ${dataLength}\`);
          this.logInfo\_ += '\\n\[INFO\] usb writeData result write length: ' + JSON.stringify(dataLength);
        } else {
          console.error('usb writeData failed');
          this.logInfo\_ += '\\n\[ERROR\] usb writeData failed';
        }
      }).catch((error: BusinessError) => {
        console.error(\`usb writeData error : ${error}\`);
        this.logInfo\_ += '\\n\[ERROR\] usb writeData error: ' + JSON.stringify(error);
      });
    }
    
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
