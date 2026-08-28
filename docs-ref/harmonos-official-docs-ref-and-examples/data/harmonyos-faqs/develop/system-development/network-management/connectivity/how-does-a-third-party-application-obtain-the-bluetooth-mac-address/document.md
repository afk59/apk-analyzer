# How does a third-party application obtain the Bluetooth MAC address?

Call **connection.startBluetoothDiscovery()** to start Bluetooth scanning. You can then obtain the Bluetooth MAC address in the scanning result. Before using this API, you must have the **ohos.permission.ACCESS\_BLUETOOTH** permission. Refer to the code snippet below.

import { connection } from '@kit.ConnectivityKit';
import { BusinessError } from '@kit.BasicServicesKit';

function onReceiveEvent(data: Array<string>) { // data is a collection of Bluetooth device addresses
  console.info('bluetooth device find = '+ JSON.stringify(data));
}

try {
  connection.on('bluetoothDeviceFind', onReceiveEvent);
  connection.startBluetoothDiscovery();
} catch (err) {
  console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

**Reference**

[Bluetooth Device Discovery](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-bluetooth-connection#connectiononbluetoothdevicefind)
