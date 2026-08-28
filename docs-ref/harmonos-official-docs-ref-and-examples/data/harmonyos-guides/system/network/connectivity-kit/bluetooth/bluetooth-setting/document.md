# Bluetooth Setting

#### Introduction

This topic walks you through how to implement basic Bluetooth settings, including enabling and disabling Bluetooth and obtaining the Bluetooth status. Before using Bluetooth-dependent functions, ensure that Bluetooth is enabled.

#### How to Develop

## Applying for Required Permissions

Apply for the **ohos.permission.ACCESS\_BLUETOOTH** permission. For details about how to configure and apply for permissions, see [Declaring Permissions](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) and [Requesting User Authorization](../../../../security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).

## Importing Required Modules

Import the **access** and **BusinessError** modules.

import { access } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

## Subscribing to Bluetooth Status Change Events

You can subscribe to the Bluetooth status change events to obtain the real-time Bluetooth status. When Bluetooth is enabled or disabled, the Bluetooth status changes. [STATE\_ON](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-access#bluetoothstate) indicates that Bluetooth is enabled while [STATE\_OFF](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-access#bluetoothstate) indicates the opposite. An application can use Bluetooth-dependent functions only if Bluetooth is enabled.

// Define the callback for Bluetooth status change events.
function onReceiveEvent(data: access.BluetoothState) {
  let btStateMessage = '';
  switch (data) {
    case access.BluetoothState.STATE\_OFF:
      // Bluetooth is disabled.
      btStateMessage += 'STATE\_OFF';
      break;
    case access.BluetoothState.STATE\_TURNING\_ON:
      btStateMessage += 'STATE\_TURNING\_ON';
      break;
    case access.BluetoothState.STATE\_ON:
      // Bluetooth is enabled. In this case, the application can use Bluetooth-dependent functions.
      btStateMessage += 'STATE\_ON';
      break;
    case access.BluetoothState.STATE\_TURNING\_OFF:
      btStateMessage += 'STATE\_TURNING\_OFF';
      break;
    case access.BluetoothState.STATE\_BLE\_TURNING\_ON:
      btStateMessage += 'STATE\_BLE\_TURNING\_ON';
      break;
    case access.BluetoothState.STATE\_BLE\_ON:
      btStateMessage += 'STATE\_BLE\_ON';
      break;
    case access.BluetoothState.STATE\_BLE\_TURNING\_OFF:
      btStateMessage += 'STATE\_BLE\_TURNING\_OFF';
      break;
    default:
      btStateMessage += 'unknown state';
      break;
  }
  console.info('bluetooth state: ' + btStateMessage);
}

try {
    // Subscribe to scan result reporting events.
    access.on('stateChange', onReceiveEvent);
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

## Enabling Bluetooth

If the Bluetooth switch is turned off, Bluetooth needs to be enabled manually when Bluetooth is required. You can subscribe to the Bluetooth status change events to determine whether Bluetooth is successfully enabled.

When you enable Bluetooth, a dialog box is displayed, as shown in Figure 1. By tapping **Enable**, you agree to enable Bluetooth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/Jl9xZ61WRsWG9rRCggdP8w/en-us_image_0000002537925030.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062014Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=706330380768F996368E775875D064040F50205268F5C2B08B119187E15D45EA)

**Figure 1** Enabling Bluetooth

try {
    // Obtain the current Bluetooth status.
    let state = access.getState();
    if (state == access.BluetoothState.STATE\_OFF) {
        // Enable Bluetooth if it is disabled.
        access.enableBluetooth();
    }
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

## Disabling Bluetooth

You can disable Bluetooth if access to Bluetooth-dependent functions is no longer needed. You can subscribe to the Bluetooth status change events to determine whether Bluetooth is successfully disabled.

When you disable Bluetooth, a dialog box is displayed, as shown in Figure 2. By tapping **Disable**, you agree to disable Bluetooth.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/LJ9XlSpeSxy87N8c5b00KA/en-us_image_0000002568684807.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062014Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A47318BED669FF0AD8E607F56530A91B717E8FD08B185831EC8CA5A0CFFF9514)

**Figure 2** Disabling Bluetooth

try {
   // Obtain the current Bluetooth status.
   let state = access.getState();
   if (state == access.BluetoothState.STATE\_ON) {
     // Disable Bluetooth if it is enabled.
     access.disableBluetooth();
  }
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### Development Example

import { access } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

export class AdapterManager {
  // Define the callback for Bluetooth status change events.
  onReceiveEvent = (data: access.BluetoothState) => {
    let btStateMessage = '';
    switch (data) {
      case access.BluetoothState.STATE\_OFF:
        // Bluetooth is disabled.
        btStateMessage += 'STATE\_OFF';
        break;
      case access.BluetoothState.STATE\_TURNING\_ON:
        btStateMessage += 'STATE\_TURNING\_ON';
        break;
      case access.BluetoothState.STATE\_ON:
        // Bluetooth is enabled. In this case, the application can use Bluetooth-dependent functions.
        btStateMessage += 'STATE\_ON';
        break;
      case access.BluetoothState.STATE\_TURNING\_OFF:
        btStateMessage += 'STATE\_TURNING\_OFF';
        break;
      case access.BluetoothState.STATE\_BLE\_TURNING\_ON:
        btStateMessage += 'STATE\_BLE\_TURNING\_ON';
        break;
      case access.BluetoothState.STATE\_BLE\_ON:
        btStateMessage += 'STATE\_BLE\_ON';
        break;
      case access.BluetoothState.STATE\_BLE\_TURNING\_OFF:
        btStateMessage += 'STATE\_BLE\_TURNING\_OFF';
        break;
      default:
        btStateMessage += 'unknown state';
        break;
    }
    console.info('bluetooth state: ' + btStateMessage);
  };

  // Enable Bluetooth.
  public openBluetooth() {
    try {
      access.on('stateChange', this.onReceiveEvent);
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
    try {
      // Obtain the current Bluetooth status.
      let state = access.getState();
      if (state == access.BluetoothState.STATE\_OFF) {
        // Enable Bluetooth if it is disabled.
        access.enableBluetooth();
      }
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
  }

  // Disable Bluetooth.
  public closeBluetooth() {
    try {
      // Obtain the current Bluetooth status.
      let state = access.getState();
      if (state == access.BluetoothState.STATE\_ON) {
        // Disable Bluetooth if it is enabled.
        access.disableBluetooth();
      }
    } catch (err) {
      console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
    }
  }
}

let adapterManager = new AdapterManager();
export default adapterManager as AdapterManager;
