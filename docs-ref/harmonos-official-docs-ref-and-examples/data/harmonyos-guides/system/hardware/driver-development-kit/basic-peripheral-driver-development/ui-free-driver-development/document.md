# UI-free Driver Development

#### When to Use

Basic UI-free drivers are applicable to simple devices that do not require setting of driver capabilities via a UI, such as mouse devices and keyboards. These drivers are designed to ensure that these devices can be used immediately upon connection, enabling seamless plug-and-play functionality. You can use **DriverExtensionAbility** to develop such applications.

#### Basic Concepts

-   DriverExtensionAbility
    
    [DriverExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-driverextensionability) is an **ExtensionAbility** of the driver type that provides the driver-related extension framework. If the capabilities of a device can be expanded by inserting an external hardware module, you can install the driver of the hardware module through an application. You can bind a [DriverExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-driverextensionability) object to an application through **DriverExtensionManager** so that related transactions can be processed in the background based on the application request information.
    
    Each type of **ExtensionAbility** has its own context. The **DriverExtensionAbility** provides related capabilities through the [DriverExtensionContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-driverextensioncontext).
    

#### Environment Setup

Before you get started, make necessary preparations by following instructions in [Environment Preparation](../../setting-up-the-environment/document.md).

#### How to Develop

To implement a driver, create a DriverExtensionAbility in the DevEco Studio project. The procedure is as follows:

1.  Create an HarmonyOS project. For details, see [Creating a Project](../../../../../environment-setup/creating-a-project/creating-a-project/document.md). (If a project has been created in [UI-based Driver Development](../ui-based-driver-development/document.md), skip this step.)
    
2.  In the **ets** directory of the project, right-click **New** > **Directory** to create a directory named **driverextability**.
    
3.  In the **driverextability** directory, right-click and choose **New** > **ArkTS File** to create a file named **DriverExtAbility.ets**.
    
4.  Import the related kit, and define the request code.
    

import { DriverExtensionAbility } from '@kit.DriverDevelopmentKit';
import { Want } from '@kit.AbilityKit';
import { rpc } from '@kit.IPCKit';

const REQUEST\_CODE = 99; // Negotiate the request code with the peripheral client.

1.  Open the **DriverExtAbility.ets** file, import the [RPC module](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-rpc), and overload the **onRemoteMessageRequest()** method to receive messages from the application and return the processing result to the application. **REQUEST\_CODE** is used to verify the service request code sent by the application.
    

class StubTest extends rpc.RemoteObject {
  // Receive a message from the application and return the processing result to the client.
  onRemoteMessageRequest(code: number, data: rpc.MessageSequence, reply: rpc.MessageSequence,
    option: rpc.MessageOption) {
    if (code === REQUEST\_CODE) {
      // Receive the data sent from the application.
      // When the application calls data.writeString() multiple times to write data, the driver can receive the corresponding data by calling data.readString() for multiple times.
      let optFir: string = data.readString();
      // The driver returns the data processing result to the application.
      // In the example, Hello is received and Hello World is returned to the application.
      reply.writeString(optFir + \` World\`);
    }
    return true;
  }
}

1.  In the **DriverExtAbility.ets** file, import the dependency package [DriverExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-driverextensionability), which provides the **onInit()**, **onRelease()**, **onConnect()**, and **onDisconnect()** lifecycle callbacks. Then, customize a class to inherit from [DriverExtensionAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-driverextensionability) and override the lifecycle callbacks as required.
    

export default class DriverExtAbility extends DriverExtensionAbility {
  onInit(want: Want) {
    console.info('testTag', \`onInit, want: ${want.abilityName}\`);
  }

  onRelease() {
    console.info('testTag', \`onRelease\`);
  }

  onConnect(want: Want) {
    console.info('testTag', \`onConnect, want: ${want.abilityName}\`);
    return new StubTest('test');
  }

  onDisconnect(want: Want) {
    console.info('testTag', \`onDisconnect, want: ${want.abilityName}\`);
  }

  onDump(params: Array<string>) {
    console.info('testTag', \`onDump, params:\` + JSON.stringify(params));
    return \['params'\];
  }
}

1.  Register **DriverExtensionAbility** in the [**module.json5** file](../../../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) of the module in the project. Set **type** to **driver** and **srcEntry** to the code path of **DriverExtensionAbility**.
    

{
  "module": {
    "name": "entry",
    "type": "entry",
    "description": "$string:module\_desc",
    "mainElement": "EntryAbility",
    "deviceTypes": \[
      "default",
      "tablet",
      "2in1"
    \],
    "requestPermissions": \[
      {
        "name": "ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER" // Peripheral-specific permission, which is mandatory.
      }
    \],
    "deliveryWithInstall": true,
    "installationFree": false,
    "pages": "$profile:main\_pages",
    "abilities": \[
      {
        "name": "EntryAbility",
        "srcEntry": "./ets/entryability/EntryAbility.ets",
        "description": "$string:EntryAbility\_desc",
        "icon": "$media:layered\_image",
        "label": "$string:EntryAbility\_label",
        "startWindowIcon": "$media:startIcon",
        "startWindowBackground": "$color:start\_window\_background",
        "exported": true,
        "skills": \[
          {
            "entities": \[
              "entity.system.home"
            \],
            "actions": \[
              "ohos.want.action.home"
            \]
          }
        \]
      }
    \],
    "extensionAbilities": \[
      {
        "name": "DriverExtAbility",
        "icon": "$media:startIcon",
        "description": "driver",
        "type": "driver",
        "exported": true,
        "srcEntry": "./ets/driverextability/DriverExtAbility.ets",
        "metadata": \[
          {
            "name": "bus", // Bus, which is mandatory.
            "value": "USB"
          },
          {
            "name": "desc", // Driver description, which is optional.
            "value": "the sample of driverExtensionAbility"
          },
          {
            "name": "vendor", // Driver vendor name, which is optional.
            "value": "string"
          },
          {
            "name": "vid," // List of USB vendor IDs. Enter a hex value. Here, the value is the hex value of 4817.
            "value": "0x12D1"
          },
          {
            "name": "pid," // List of USB product IDs. Enter a hex value. Here, the value is the hex value of 4258.
            "value": "0x10A2"
          },
          {
            "name": "launchOnBind," // Whether to enable delayed driver startup. This parameter is optional. The value \*\*true\*\* indicates delayed startup, and the value \*\*false\*\* indicates immediate startup. The value is \*\*false\*\* by default if the specified value is incorrect or the value is left unspecified.
            "value": "true"
          },
          {
            "name": "ohos.permission.ACCESS\_DDK\_ALLOWED," // Whether to allow DDK access. This parameter is optional. The value \*\*true\*\* indicates that DDK access is allowed, and the value \*\*false\*\* indicates the opposite. The default value is \*\*false\*\*.
            "value": "true"
          }
        \]
      }
    \]
  }
}

1.  After completing development of the client and driver sample code, import the HAP to the device by following instructions in [Running Your App/Atomic Service on a Local Real Device](../../../../../coding-and-debugging/running-your-app-on-a-local-real-device/document.md), and run **Hello** in the HAP to check whether **Hello world** is displayed. If yes, the IPC communication is ready for use.

#### Driver Development

Currently, **DriverExtensionAbility** provides four capabilities: HID DDK, USB DDK, USB Serial DDK, and SCSI peripheral DDK, which are used to develop dedicated drivers for extended peripherals. Choose either mode depending on your need:

-   [HID DDK Development](../../dedicated-peripheral-driver-development/hid-ddk-development/document.md)
-   [USB DDK Development](../../dedicated-peripheral-driver-development/usb-ddk-development/document.md)
-   [USB Serial DDK Development](../../dedicated-peripheral-driver-development/usb-serial-ddk-development/document.md)
-   [SCSI Peripheral DDK Development](../../dedicated-peripheral-driver-development/scsi-peripheral-ddk-development/document.md)

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
