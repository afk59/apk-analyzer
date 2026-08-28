# UI-based Driver Development

#### When to Use

UI-based basic drivers are applicable to a wide variety of composite devices. When developing these drivers, you may set the corresponding unique driver capabilities through the UI, or display the information retrieved from the devices on the UI. Examples of such devices include mice with side buttons, handwriting tablets, and ID card readers.

#### Environment Setup

Before you get started, make necessary preparations by following instructions in [Environment Preparation](../../setting-up-the-environment/document.md).

#### Available APIs

The following table describes the basic peripheral management capabilities. For details, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-driver-devicemanager).

**Table 1** APIs for basic peripheral management

| Name | Description |
| :-- | :-- |
| queryDevices(busType?: number): Array<Readonly<Device>> | Queries the peripheral list. |
| bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>; | Binds a peripheral. This API uses a promise to return the result. It is supported since API version 18. |
| unbindDriverWithDeviceId(deviceId: number): Promise<number> | Unbinds a peripheral device. This API uses a promise to return the result. It is supported since API version 18. |

#### How to Develop

You can use the APIs to query and bind peripheral devices so as to use the customized driver capabilities of the peripherals.

The following sample code is a demo that illustrates how to develop both the client and server and implement IPC.

1.  Create a project following instructions in [Creating a Project](../../../../../environment-setup/creating-a-project/creating-a-project/document.md).
    
    **NOTE**
    
    To develop a driver client, select the **Empty Ability** template.
    
    To develop the driver server, select the **Native C++** template.
    
    To develop both the driver client and server, select the **Native C++** template.
    
2.  Import the related kit, and declare the product ID, vendor ID, and code of the USB device to be bound.
    
    **NOTE**
    
    Write following sample code in the **entry/src/main/ets/pages/Index.ets** file.
    

import { hilog } from '@kit.PerformanceAnalysisKit';
import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

const REQUEST\_CODE: number = 99; // Custom communication code, which is for reference only.
const productId: number = 4258; // Declare the product ID of the connected USB device.
const vendorId: number = 4817; // Declare the vendor ID of the connected USB device.
const DOMAIN = 0x0000;

1.  Define the **message** variable and remote object variable for communication with the driver.
    
    **NOTE**
    
    The following APIs are defined in **struct Index{}**.
    

  @State message: string = 'Hello';
  private remote: rpc.IRemoteObject | null = null;

1.  Define the **queryDevices** API, and use it to obtain the device ID of the peripheral.
    

  private async queryTargetDeviceId(): Promise<number> {
    try {
      const devices: deviceManager.Device\[\] = deviceManager.queryDevices(deviceManager.BusType.USB);
      const index = devices.findIndex((item: deviceManager.Device) => {
        let usbDevice = item as deviceManager.USBDevice;
        // If the product ID and vendor ID of the peripheral are unknown, you can view the information about the connected USB device in the log.
        hilog.info(DOMAIN, 'testTag', \`usbDevice.productId = ${usbDevice.productId}, usbDevice.vendorId = ${usbDevice.vendorId}\`);
        return usbDevice.productId === productId && usbDevice.vendorId === vendorId;
      });
      hilog.info(DOMAIN, 'testTag', \`queryTargetDeviceId index = ${index}, deviceId = ${devices\[index\].deviceId}\`);
      if (index < 0) {
        hilog.error(DOMAIN, 'testTag', 'can not find device');
        return -1;
      }
      return devices\[index\].deviceId;
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', \`queryDevice failed, err: ${JSON.stringify(error)}\`);
    }
    return -1;
  }

1.  Define the **bindDriverWithDeviceId** API, and use it to obtain the remote object.
    

  private async getDriverRemote(deviceId: number): Promise<rpc.IRemoteObject | null> {
    try {
      let remoteDeviceDriver: deviceManager.RemoteDeviceDriver = await deviceManager.bindDeviceDriver(deviceId,
        (err: BusinessError, id: number) => {
          hilog.info(DOMAIN, 'testTag', \`device\[${id}\] id disconnect, err: ${JSON.stringify(err)}\`);
        });
      return remoteDeviceDriver.remote;
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', \`bindDriverWithDeviceId failed, err: ${JSON.stringify(error)}\`);
    }
    return null;
  }

1.  Defines the **sendMessageRequest** API, and use it to perform IPC with the remote object.
    

  private async communicateWithRemote(): Promise<void> {
    const deviceId: number = await this.queryTargetDeviceId();
    hilog.info(DOMAIN, 'testTag', \`queryTargetDeviceId, deviceId=${deviceId}\`);
    if (deviceId < 0) {
      hilog.error(DOMAIN, 'testTag', 'can not find target device');
      return;
    }
    this.remote = await this.getDriverRemote(deviceId);
    if (this.remote === null) {
      hilog.error(DOMAIN, 'testTag', \`getDriverRemote failed\`);
      return;
    }

    let option = new rpc.MessageOption();
    let data = new rpc.MessageSequence();
    let reply = new rpc.MessageSequence();

    // Send "Hello" to the driver.
    hilog.info(DOMAIN, 'testTag', \`communicateWithRemote, message=${this.message}\`);
    data.writeString(this.message);

    try {
      await this.remote.sendMessageRequest(REQUEST\_CODE, data, reply, option);
      // Obtain the "Hello world" information returned by the driver.
      this.message = reply.readString();
      hilog.info(DOMAIN, 'testTag', \`sendMessageRequest, message: ${this.message}\`);
    } catch (error) {
      hilog.error(DOMAIN, 'testTag', \`sendMessageRequest failed, err: ${JSON.stringify(error)}\`);
    }
  }

1.  Render the UI. For details about UI development, see [UI Development](../../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/document.md).
    

  build() {
    Row() {
      Column() {
        Text(this.message)
          .fontSize($r('app.float.page\_text\_font\_size'))
          .fontWeight(FontWeight.Bold)
          .onClick(() => {
            // Click Hello to communicate with the remote object. The message "Hello World" is displayed.
            this.communicateWithRemote();
          })
      }
      .width('100%')
    }
    .height('100%')
  }

1.  Develop peripheral drivers by following instructions in [UI-free Driver Development](../ui-free-driver-development/document.md).

#### Application Signing

**NOTE**

Configure the permission before enabling automatic signing.

You need to configure a signature file for your application to run on a device. Besides, to develop a peripheral driver client, you need to declare the **ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER** and **ohos.permission.ACCESS\_DDK\_DRIVERS** permissions for the peripheral.

-   ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER
    
    To obtain authorization on this access permission, [declare it](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) in the **requestPermissions** field in the **module.json5** file.
    
-   ohos.permission.ACCESS\_DDK\_DRIVERS
    
    1.  [Declare the required permissions](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) in the **requestPermissions** field in the **module.json5** file.
    2.  Modify the **acls** field in the **HarmonyAppProvision** configuration file to request permissions via ACL. For details, see [Requesting Restricted Permissions](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/requesting-restricted-permissions/document.md).
    3.  When you choose **Certificates, App IDs, and Profiles** > **Profiles** in [AppGallery Connect](https://developer.huawei.com/consumer/cn/service/josp/agc/index.html) to request a profile, select the restricted permission **ohos.permission.ACCESS\_DDK\_DRIVERS** and enter the bundle name of the server your client needs to connect to. If there are multiple servers, separate their bundle names with a comma.

After completing the permission configuration, sign the application by following the instructions in [Automatic Signing](../../../../../coding-and-debugging/configuring-a-debug-signature/document.md).
