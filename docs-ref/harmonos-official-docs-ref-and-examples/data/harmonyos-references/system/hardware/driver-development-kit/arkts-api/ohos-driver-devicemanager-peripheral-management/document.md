# @ohos.driver.deviceManager (Peripheral Management)

The **deviceManager** module provides APIs for managing peripheral devices, including querying the peripheral device list and binding or unbinding a peripheral device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/Y3z2C0IASTmXiqP_Q993FA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F08347E66D0B29DDD1B5DABFB8F1F56164E1E1FE94162E22BC82DDBBD2999BF2)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { deviceManager } from '@kit.DriverDevelopmentKit';

#### deviceManager.queryDevices

queryDevices(busType?: number): Array<Readonly<Device>>

Queries the list of peripheral devices. If the device has no peripheral device connected, an empty list is returned.

**Required permissions**: ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| busType | number | No | Bus type of the peripheral device to query. If this parameter is left blank, all types of peripheral devices are queried. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<Readonly<[Device](#device)\>> | List of peripheral devices obtained. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 22900001 | ExternalDeviceManager service exception or busType parameter error. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';

try {
  let devices : Array<deviceManager.Device> = deviceManager.queryDevices(deviceManager.BusType.USB);
  for (let item of devices) {
    let device : deviceManager.USBDevice = item as deviceManager.USBDevice;
    console.info(\`Device id is ${device.deviceId}\`);
  }
} catch (error) {
  console.error(\`Failed to query device. Code is ${error.code}, message is ${error.message}\`);
}

#### deviceManager.bindDriverWithDeviceId19+

bindDriverWithDeviceId(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>

Binds a peripheral device based on the device information returned by **queryDevices()**. This API uses a promise to return the result.

You need to use [deviceManager.queryDevices](#devicemanagerquerydevices) to obtain the peripheral device list.

**Required permissions**: ohos.permission.ACCESS\_DDK\_DRIVERS

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Device ID, which can be obtained via **queryDevices()**. |
| onDisconnect | AsyncCallback<number> | Yes | Callback to be invoked when the bound peripheral device is disconnected. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RemoteDeviceDriver](#remotedevicedriver11)\> | Promise used to return a **RemoteDeviceDriver** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 26300001 | ExternalDeviceManager service exception. |
| 26300002 | The driver service does not allow any client to bind. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.bindDriverWithDeviceId(12345678, (error : BusinessError, data : number) => {
    console.error(\`Device is disconnected\`);
  }).then((data: deviceManager.RemoteDeviceDriver) => {
    console.info(\`bindDriverWithDeviceId success, Device\_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}\`);
  }, (error: BusinessError) => {
    console.error(\`bindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}\`);
  });
} catch (error) {
  console.error(\`bindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}\`);
}

#### deviceManager.unbindDriverWithDeviceId19+

unbindDriverWithDeviceId(deviceId: number): Promise<number>

Unbinds a peripheral device. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ACCESS\_DDK\_DRIVERS

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Device ID, which can be obtained via [queryDevices](#devicemanagerquerydevices). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the device ID. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 26300001 | ExternalDeviceManager service exception. |
| 26300003 | There is no binding relationship. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.unbindDriverWithDeviceId(12345678).then((data : number) => {
    console.info(\`unbindDriverWithDeviceId success, Device\_Id is ${data}.\`);
  }, (error : BusinessError) => {
    console.error(\`unbindDriverWithDeviceId async fail. Code is ${error.code}, message is ${error.message}\`);
  });
} catch (error) {
  console.error(\`unbindDriverWithDeviceId fail. Code is ${error.code}, message is ${error.message}\`);
}

#### deviceManager.bindDevice(deprecated)

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<{deviceId: number; remote: rpc.IRemoteObject;}>): void

Binds a peripheral device based on the device information returned by **queryDevices()**.

You need to use [deviceManager.queryDevices()](#devicemanagerquerydevices) to obtain the peripheral device information and device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6/v3/dMNsF70HRWO4tDsIPOpY0g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A5C4953210617C82F6B88D8849244B52C8A509956986FEF2507597336C95570)

This API is supported since API version 10 and deprecated since API version 19. You are advised to use [deviceManager.bindDriverWithDeviceId](#devicemanagerbinddriverwithdeviceid19) instead.

**Required permissions**: ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Device ID, which can be obtained via **queryDevices()**. |
| onDisconnect | AsyncCallback<number> | Yes | Callback to be invoked when the bound peripheral device is disconnected. |
| callback | AsyncCallback<{deviceId: number; remote: [rpc.IRemoteObject](../../../../../application-framework/ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#iremoteobject);}> | Yes | Callback invoked to return the communication object of the peripheral device bound. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

interface DataType {
  deviceId : number;
  remote : rpc.IRemoteObject;
}

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.bindDevice(12345678, (error : BusinessError, data : number) => {
    console.error(\`Device is disconnected\`);
  }, (error : BusinessError, data : DataType) => {
    if (error) {
      console.error(\`bindDevice async fail. Code is ${error.code}, message is ${error.message}\`);
      return;
    }
    console.info(\`bindDevice success\`);
  });
} catch (error) {
  console.error(\`bindDevice fail. Code is ${error.code}, message is ${error.message}\`);
}

#### deviceManager.bindDeviceDriver(deprecated)

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>, callback: AsyncCallback<RemoteDeviceDriver>): void

Binds a peripheral device based on the device information returned by **queryDevices()**.

You need to use [deviceManager.queryDevices()](#devicemanagerquerydevices) to obtain the peripheral device information and device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b7/v3/pMbpqRenQdi4BzF9anRhKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CD1A62001326437743B00B5B002757F75BBCAFF4EF1618DB34A55CD46D22379)

This API is supported since API version 11 and deprecated since API version 19. You are advised to use [deviceManager.bindDriverWithDeviceId](#devicemanagerbinddriverwithdeviceid19) instead.

**Required permissions**: ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Device ID, which can be obtained via **queryDevices()**. |
| onDisconnect | AsyncCallback<number> | Yes | Callback to be invoked when the bound peripheral device is disconnected. |
| callback | AsyncCallback<[RemoteDeviceDriver](#remotedevicedriver11)\> | Yes | Binding result, including the device ID and remote object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rpc } from '@kit.IPCKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.bindDeviceDriver(12345678, (error : BusinessError, data : number) => {
    console.error(\`Device is disconnected\`);
  }, (error : BusinessError, data : deviceManager.RemoteDeviceDriver) => {
    if (error) {
      console.error(\`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}\`);
      return;
    }
    console.info(\`bindDeviceDriver success\`);
  });
} catch (error) {
  console.error(\`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}\`);
}

#### deviceManager.bindDevice(deprecated)

bindDevice(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<{deviceId: number; remote: rpc.IRemoteObject;}>;

Binds a peripheral device based on the device information returned by **queryDevices()**. This API uses a promise to return the result.

You need to use [deviceManager.queryDevices](#devicemanagerquerydevices) to obtain the peripheral device information and device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/57/v3/3lx9g3VMR_WR3V39mk4ZLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E89AB93BDED66B8343E2F4DDB043355B46DBEB674F202E1C5367D8C33F3AF96)

This API is supported since API version 10 and deprecated since API version 19. You are advised to use [deviceManager.bindDriverWithDeviceId](#devicemanagerbinddriverwithdeviceid19) instead.

**Required permissions**: ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Device ID, which can be obtained via **queryDevices()**. |
| onDisconnect | AsyncCallback<number> | Yes | Callback to be invoked when the bound peripheral device is disconnected. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<{deviceId: number; remote: [rpc.IRemoteObject](../../../../../application-framework/ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#iremoteobject);}> | Promise used to return the device ID and **IRemoteObject** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.bindDevice(12345678, (error : BusinessError, data : number) => {
    console.error(\`Device is disconnected\`);
  }).then(data => {
    console.info(\`bindDevice success, Device\_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}\`);
  }, (error: BusinessError) => {
    console.error(\`bindDevice async fail. Code is ${error.code}, message is ${error.message}\`);
  });
} catch (error) {
  console.error(\`bindDevice fail. Code is ${error.code}, message is ${error.message}\`);
}

#### deviceManager.bindDeviceDriver(deprecated)

bindDeviceDriver(deviceId: number, onDisconnect: AsyncCallback<number>): Promise<RemoteDeviceDriver>;

Binds a peripheral device based on the device information returned by **queryDevices()**. This API uses a promise to return the result.

You need to use [deviceManager.queryDevices](#devicemanagerquerydevices) to obtain the peripheral device information and device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/y_x8rZOsQ8CgwCc3dQophA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=485930032B4113E1D79F0EA69DC0011FE07F938AC66B2AFB71E3ADB8D4325C5B)

This API is supported since API version 11 and deprecated since API version 19. You are advised to use [deviceManager.bindDriverWithDeviceId](#devicemanagerbinddriverwithdeviceid19) instead.

**Required permissions**: ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Device ID, which can be obtained via **queryDevices()**. |
| onDisconnect | AsyncCallback<number> | Yes | Callback to be invoked when the bound peripheral device is disconnected. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[RemoteDeviceDriver](#remotedevicedriver11)\> | Promise used to return a **RemoteDeviceDriver** object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.bindDeviceDriver(12345678, (error : BusinessError, data : number) => {
    console.error(\`Device is disconnected\`);
  }).then((data: deviceManager.RemoteDeviceDriver) => {
    console.info(\`bindDeviceDriver success, Device\_Id is ${data.deviceId}.
    remote is ${data.remote != null ? data.remote.getDescriptor() : "null"}\`);
  }, (error: BusinessError) => {
    console.error(\`bindDeviceDriver async fail. Code is ${error.code}, message is ${error.message}\`);
  });
} catch (error) {
  console.error(\`bindDeviceDriver fail. Code is ${error.code}, message is ${error.message}\`);
}

#### deviceManager.unbindDevice(deprecated)

unbindDevice(deviceId: number, callback: AsyncCallback<number>): void

Unbinds a peripheral device.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/E8Kox2ajQWGkOTo_rZyp2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CF305F5AC78F4D4BE8798FE9E81017D2A7FAFDBFCC2AC2841AF4FBFC6C610D04)

This API is supported since API version 10 and deprecated since API version 19. You are advised to use [deviceManager.unbindDriverWithDeviceId](#devicemanagerunbinddriverwithdeviceid19) instead.

**Required permissions**: ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Device ID, which can be obtained via **queryDevices()**. |
| callback | AsyncCallback<number> | Yes | Callback invoked to return the result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 22900001 | ExternalDeviceManager service exception. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.unbindDevice(12345678, (error : BusinessError, data : number) => {
    if (error) {
      console.error(\`unbindDevice async fail. Code is ${error.code}, message is ${error.message}\`);
      return;
    }
    console.info(\`unbindDevice success\`);
  });
} catch (error) {
  console.error(\`unbindDevice fail. Code is ${error.code}, message is ${error.message}\`);
}

#### deviceManager.unbindDevice(deprecated)

unbindDevice(deviceId: number): Promise<number>

Unbinds a peripheral device. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/jHB1QVbgQiygr0X5n0wmOA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062407Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A61C6FEEED1A4922D3747636A47F6D84A39D9B734FCB18A0F3DD2CCB7CD2391B)

This API is supported since API version 10 and deprecated since API version 19. You are advised to use [deviceManager.unbindDriverWithDeviceId](#devicemanagerunbinddriverwithdeviceid19) instead.

**Required permissions**: ohos.permission.ACCESS\_EXTENSIONAL\_DEVICE\_DRIVER

**System capability**: SystemCapability.Driver.ExternalDevice

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| deviceId | number | Yes | Device ID, which can be obtained via **queryDevices()**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Driver Error Codes](../../error-codes/driver-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The permission check failed. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. 3.Parameter verification failed. |
| 22900001 | ExternalDeviceManager service exception. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the device ID. |

**Example**

import { deviceManager } from '@kit.DriverDevelopmentKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  // For example, deviceId is 12345678. You can use queryDevices() to obtain the deviceId.
  deviceManager.unbindDevice(12345678).then((data : number) => {
    console.info(\`unbindDevice success, Device\_Id is ${data}.\`);
  }, (error : BusinessError) => {
    console.error(\`unbindDevice async fail. Code is ${error.code}, message is ${error.message}\`);
  });
} catch (error) {
  console.error(\`unbindDevice fail. Code is ${error.code}, message is ${error.message}\`);
}

#### Device

Represents the peripheral device information.

**System capability**: SystemCapability.Driver.ExternalDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| busType | [BusType](#bustype) | No | No | Bus type. |
| deviceId | number | No | No | ID of the peripheral device. |
| description | string | No | No | Description of the peripheral device. |

#### USBDevice

USB device information, which is inherited from [Device](#device).

**System capability**: SystemCapability.Driver.ExternalDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| vendorId | number | No | No | Vendor ID of the USB device. |
| productId | number | No | No | Product ID of the USB device. |

#### BusType

Enumerates the device bus types.

**System capability**: SystemCapability.Driver.ExternalDevice

| Name | Value | Description |
| :-- | :-- | :-- |
| USB | 1 | USB bus. |

#### RemoteDeviceDriver11+

Represents information about a remote device driver.

**System capability**: SystemCapability.Driver.ExternalDevice

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceId11+ | number | No | No | ID of the peripheral device. |
| remote11+ | [rpc.IRemoteObject](../../../../../application-framework/ipc-kit/arkts-apis/ohos-rpc-rpc/document.md#iremoteobject) | No | No | Remote driver object. |
