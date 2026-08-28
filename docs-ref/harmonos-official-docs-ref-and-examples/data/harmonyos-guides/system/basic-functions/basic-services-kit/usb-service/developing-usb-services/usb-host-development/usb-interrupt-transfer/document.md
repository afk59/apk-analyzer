# USB Interrupt Transfer

#### When to Use

The interrupt transfer is mainly used by the host to receive a data packet sent by a device. The endpoint mode of a device determines whether the interface supports interrupt reading or interrupt writing. This mode is applicable to the transfer of a small number of scattered and unpredictable data input by devices such as the mouse, keyboard, and joystick. In addition, the endpoints of these devices support only interrupt reading.

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
| usbSubmitTransfer(transfer: UsbDataTransferParams): void | Submits isochronous, bulk, or interrupt transfer in an asynchronous manner. |
| usbCancelTransfer(transfer: UsbDataTransferParams): void | Cancels the submitted asynchronous transfer. |

For details about the APIs of device management and transfer modes, see [@ohos.usbManager (USB Manager)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-usbmanager).

## How to Develop

Connect a host to a device and use the **usbSubmitTransfer** API to transfer data. The following steps describe how to implement an interrupt transfer:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/35/v3/SP9OpuPuS3WopA5L-_pjuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062020Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D28F2BB88A4EC58E52DCE3BB731A1C740D6A0DE6CBAD6FB1609BD6383FDA4272)

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
    
4.  Obtain the endpoint for reading data through interrupt transfer.
    
    if (this.deviceList\_ === undefined || this.deviceList\_.length === 0) {
      console.error('deviceList\_ is empty');
      this.logInfo\_ += '\\n\[ERROR\] deviceList\_ is empty';
      return;
    }
    let usbDevice: usbManager.USBDevice = this.deviceList\_\[0\];
    if (!usbManager.hasRight(usbDevice.name)) {
      console.error('permission denied');
      this.logInfo\_ += '\\n\[ERROR\] permission denied';
      return;
    }
    let devicePipe: usbManager.USBDevicePipe = usbManager.connectDevice(usbDevice);
    let usbConfigs: usbManager.USBConfiguration\[\] = usbDevice.configs;
    let usbInterfaces: usbManager.USBInterface\[\] = \[\];
    let usbInterface: usbManager.USBInterface | undefined = undefined;
    let usbEndpoints: usbManager.USBEndpoint\[\] = \[\];
    let usbEndpoint: usbManager.USBEndpoint | undefined = undefined;
    for (let i = 0; i < usbConfigs?.length; i++) {
      usbInterfaces = usbConfigs\[i\]?.interfaces;
      for (let j = 0; j < usbInterfaces?.length; j++) {
        usbEndpoints = usbInterfaces\[j\]?.endpoints;
        usbEndpoint = usbEndpoints?.find((value) => {
          return value.direction === 128 && value.type === usbManager.UsbEndpointTransferType.TRANSFER\_TYPE\_INTERRUPT;
        })
        if (usbEndpoint !== undefined) {
          usbInterface = usbInterfaces\[j\];
          break;
        }
      }
    }
    if (usbEndpoint === undefined) {
      console.error(\`get usbEndpoint error\`)
      this.logInfo\_ += '\\n\[ERROR\] get usbEndpoint error';
      return;
    }
    
5.  Connect to the device and register the communication interface.
    
    // Register a communication interface. If the registration is successful, 0 is returned; otherwise, other error codes are returned.
    let claimInterfaceResult: number = usbManager.claimInterface(devicePipe, usbInterface, true);
    if (claimInterfaceResult !== 0) {
      console.error(\`claimInterface error = ${claimInterfaceResult}\`)
      this.logInfo\_ += '\\n\[ERROR\] claimInterface error = ' + JSON.stringify(claimInterfaceResult);
      return;
    }
    
6.  Perform data transfer.
    
    let transferParams: usbManager.UsbDataTransferParams | undefined = undefined;
    try {
      // The communication interface is successfully registered and performs data transfer.
      transferParams = {
        devPipe: devicePipe,
        flags: usbManager.UsbTransferFlags.USB\_TRANSFER\_SHORT\_NOT\_OK,
        endpoint: usbEndpoint.address,
        type: usbManager.UsbEndpointTransferType.TRANSFER\_TYPE\_INTERRUPT,
        timeout: 2000,
        length: 10,
        callback: () => {
        },
        userData: new Uint8Array(10),
        buffer: new Uint8Array(10),
        isoPacketCount: 2,
      };
    
      transferParams.callback = (err: Error, callBackData: usbManager.SubmitTransferCallback) => {
        console.info(\`callBackData = ${callBackData}\`);
        this.logInfo\_ += '\\n\[INFO\] callBackData = ' + JSON.stringify(callBackData);
        console.info(\`transfer success,result = ${transferParams?.buffer}\`);
        this.logInfo\_ += '\\n\[INFO\] transfer success,result = ' + JSON.stringify(transferParams?.buffer);
      }
      usbManager.usbSubmitTransfer(transferParams);
      console.info('USB transfer request submitted.');
      this.logInfo\_ += '\\n\[INFO\] USB transfer request submitted.';
    } catch (error) {
      console.error(\`USB transfer failed: ${error}\`);
      this.logInfo\_ += '\\n\[ERROR\] USB transfer failed: ' + JSON.stringify(error);
    }
    
7.  Cancel the data transfer, releases the interface, and closes the USB device pipe.
    
    try {
      usbManager.usbCancelTransfer(transferParams);
      usbManager.releaseInterface(devicePipe, usbInterface);
      usbManager.closePipe(devicePipe);
    } catch (error) {
      console.error(\`release failed: ${error}\`);
      this.logInfo\_ += '\\n\[ERROR\] release failed: ' + JSON.stringify(error);
    }
    

## Verification

1.  Connect the host to a terminal device (such as a mouse or a keyboard) that supports interrupt transfer through a USB interface.
2.  Execute the preceding code.
3.  Search for the keyword **transfer success** in the log. If the keyword is found, the interrupt transfer interface is successfully called.
