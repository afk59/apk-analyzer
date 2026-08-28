# @ohos.usbManager.serial (Serial Port Management)

This module provides the serial port management functions, including enabling and disabling the serial port of the device, writing and reading data, setting and obtaining the configuration parameters of the serial port, and managing permissions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/S2MYzhD5QyaYCqLgAv3IKw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2D0AA449BEFFB5E944C799E383D7B5A0C844450719C5D14348753FD5DE107561)

The initial APIs of this module are supported since API version 19. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { serialManager } from '@kit.BasicServicesKit';

#### serialManager.getPortList

getPortList(): Readonly<SerialPort>\[\]

Obtains the serial port device list, including the device name and port number.

**System capability**: SystemCapability.USB.USBManager.Serial

**Return value**

| Type | Description |
| :-- | :-- |
| Readonly<[SerialPort](#serialport)\>\[\] | Serial port information list. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/3OY3crFAQku4sEurUzobjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=20FD44900D80B68FDDB6CB1C88410E2614FC879FE448C925AE65FE2A393DE8B2)

The following sample code shows the basic process for calling the **getPortList** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port device list.
function getPortList() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;
}

#### serialManager.hasSerialRight

hasSerialRight(portId: number): boolean

Checks whether the application has the permission to access the serial port device. When an application is restarted after exits, you need to request the permission from the user again.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | The value **true** indicates that the permission is authorized, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14400005 | Database operation exception. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/paIAx_uTTLewxCU8w6uewg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A29A5A288BE9585D0698C870C24DBA0E8052469F44292A34EFB8C8680C5A660A)

The following sample code shows the basic process for calling the **hasSerialRight** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function hasSerialRight() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('portList: ', JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (serialManager.hasSerialRight(portId)) {
    console.info('The serial port is accessible');
  } else {
    console.info('No permission to access the serial port');
  }
}

#### serialManager.requestSerialRight

requestSerialRight(portId: number): Promise<boolean>

Requests the permission for the application to access the serial port device. After the application exits, the access permission on the serial port device is automatically removed. After the application is restarted, you need to request the permission again. This API uses a promise to return the result.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the permission is successfully requested, and **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14400005 | Database operation exception. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/K7ACixQxSLGv0ElzubkKSw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4661936FF37B2796583CE0FAF337698753EAC4EC36B9FFC9DD5AB12B02AA2F85)

The following sample code shows the basic process for calling the **requestSerialRight** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function requestSerialRight() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }
}

#### serialManager.open

open(portId: number): void

Opens a serial port device.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400002 | Access denied. Call requestSerialRight to request user authorization first. |
| 31400003 | PortId does not exist. |
| 31400004 | The serial port device is occupied. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/91/v3/gOV2_yN9SZ2BXK-hrlkwJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DCE133643C8B937C1D439C4094D9C7E3C8326CED348442BAE62245DC42A36E9)

The following sample code shows the basic process for calling the **open** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function open() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }
}

#### serialManager.getAttribute

getAttribute(portId: number): Readonly<SerialAttribute>

Obtains the configuration parameters of a specified serial port.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |

**Return value**

| Type | Description |
| :-- | :-- |
| Readonly<[SerialAttribute](#serialattribute)\> | Configuration parameters of the serial port. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/SUy2CGbaTrujSvHlvuO-jg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C4E1FA8B0E3B640EA3CB101046C3F24C931B50790C782F20DB0B9D044A637FA)

The following sample code shows the basic process for calling the **getAttribute** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function getAttribute() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
    return;
  }

  // Obtain the serial port configuration.
  try {
    let attribute: serialManager.SerialAttribute = serialManager.getAttribute(portId);
    if (attribute === undefined) {
      console.error('getAttribute usbSerial error, attribute is undefined');
    } else {
      console.info('getAttribute usbSerial success, attribute: ' + JSON.stringify(attribute));
    }
  } catch (error) {
    console.error('getAttribute usbSerial error, ' + JSON.stringify(error));
  }
}

#### serialManager.setAttribute

setAttribute(portId: number, attribute: SerialAttribute): void

Sets the parameters of the serial port. If this method is not called, the default configuration parameters are used (baud rate: 9600 bit/s; data bit: 8; parity bit: 0; stop bit: 1).

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |
| attribute | [SerialAttribute](#serialattribute) | Yes | Configuration parameters of the serial port. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/2lnLZoMKQSy3fAde1L4FLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88A090726FB157A2133C6EE0C1D2C0F7FCC7D86C85D0A1032EBA28ED02A174CC)

The following sample code shows the basic process for calling the **setAttribute** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function setAttribute() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
    return;
  }

  // Set the serial port configuration.
  try {
    let attribute: serialManager.SerialAttribute = {
      baudRate: serialManager.BaudRates.BAUDRATE\_9600,
      dataBits: serialManager.DataBits.DATABIT\_8,
      parity: serialManager.Parity.PARITY\_NONE,
      stopBits: serialManager.StopBits.STOPBIT\_1
    }
    serialManager.setAttribute(portId, attribute);
    console.info('setAttribute usbSerial success, attribute: ' + JSON.stringify(attribute));
  } catch (error) {
    console.error('setAttribute usbSerial error, ' + JSON.stringify(error));
  }
}

#### serialManager.read

read(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>

Reads data from the serial port device asynchronously. This API uses a promise to return the result.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |
| buffer | Uint8Array | Yes | Buffer for reading data. |
| timeout | number | No | Timeout interval, in milliseconds. If there is no data in the buffer of the target port, this API returns the result after waiting for the specified time. The default value **0** indicates that the API returns the result without waiting. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the length of the data read. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |
| 31400006 | Data transfer timed out. |
| 31400007 | I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/80/v3/U4MiiEy7Ts6pwq8Iqo1y0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=935232DFB2B1F4CC39F4E84D18302F628E8E9B996FE6823E2960227B3A76D35B)

The following sample code shows the basic process for calling the **read** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function read() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // Read data asynchronously.
  let readBuffer: Uint8Array = new Uint8Array(64);
  serialManager.read(portId, readBuffer, 2000).then((size: number) => {
    console.info('read usbSerial success, readBuffer: ' + readBuffer.toString());
  }).catch((error: Error) => {
    console.error('read usbSerial error, ' + JSON.stringify(error));
  })
}

#### serialManager.readSync

readSync(portId: number, buffer: Uint8Array, timeout?: number): number

Reads data from the serial port device synchronously.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |
| buffer | Uint8Array | Yes | Buffer for reading data. |
| timeout | number | No | Timeout interval, in milliseconds. If there is no data in the buffer of the target port, this API returns the result after waiting for the specified time. The default value **0** indicates that the API returns the result without waiting. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data read. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |
| 31400006 | Data transfer timed out. |
| 31400007 | I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/jNPZHAn7Rx6l2zvbDKDmuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED3567D4DA5A2B49F86BD5E5FC371F2CFEB39B1887EEFB9A4B1C16496689AC99)

The following sample code shows the basic process for calling the **readSync** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function readSync() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // Read data synchronously.
  let readSyncBuffer: Uint8Array = new Uint8Array(64);
  try {
    serialManager.readSync(portId, readSyncBuffer, 2000);
    console.info('readSync usbSerial success, readSyncBuffer: ' + readSyncBuffer.toString());
  } catch (error) {
    console.error('readSync usbSerial error, ' + JSON.stringify(error));
  }
}

#### serialManager.write

write(portId: number, buffer: Uint8Array, timeout?: number): Promise<number>

Writes data to the serial port device asynchronously. The length of data written each time cannot exceed 4 KB; otherwise, data loss may occur. You are advised to write long data in multiple packets. This API uses a promise to return the result.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |
| buffer | Uint8Array | Yes | Buffer for writing data. |
| timeout | number | No | Timeout interval, in milliseconds. Whether the buffer of the target port is writable within the specified time. If yes, the API is processed properly; otherwise, a timeout message is returned after the specified time. The default value **0** indicates that the API returns the result immediately when the target port is not writable. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the length of the data written. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |
| 31400006 | Data transfer timed out. |
| 31400007 | I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/be/v3/WUXRY9neQ--hKq_OK08-YA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=59DEF30D48E91B897D74917AB0C5E312AC56425427843FBAD07D74DE4565350D)

The following sample code shows the basic process for calling the **write** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { buffer } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function write() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // Write data asynchronously.
  let writeBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
  serialManager.write(portId, writeBuffer, 2000).then((size: number) => {
    console.info('write usbSerial success, writeBuffer: ' + writeBuffer.toString());
  }).catch((error: Error) => {
    console.error('write usbSerial error, ' + JSON.stringify(error));
  })
}

#### serialManager.writeSync

writeSync(portId: number, buffer: Uint8Array, timeout?: number): number

Writes data to the serial port device synchronously. The length of data written each time cannot exceed 4 KB; otherwise, data loss may occur. You are advised to write long data in multiple packets.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |
| buffer | Uint8Array | Yes | Destination buffer for writing data. |
| timeout | number | No | Timeout interval, in milliseconds. Whether the buffer of the target port is writable within the specified time. If yes, the API is processed properly; otherwise, a timeout message is returned after the specified time. The default value **0** indicates that the API returns the result immediately when the target port is not writable. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data written. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |
| 31400006 | Data transfer timed out. |
| 31400007 | I/O exception. Possible causes: 1. The transfer was canceled. 2. The device offered more data than allowed. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ac/v3/9oTSnn2BRQqqEb4xhkWfLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8F80B2A738A02A1116AACFF21699793D6881DDEBC4605AB8F8CA5EF1A4D380DA)

The following sample code shows the basic process for calling the **writeSync** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { buffer } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function writeSync() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
  }

  // Write data synchronously.
  let writeSyncBuffer: Uint8Array = new Uint8Array(buffer.from('Hello World', 'utf-8').buffer)
  try {
    serialManager.writeSync(portId, writeSyncBuffer, 2000);
    console.info('writeSync usbSerial success, writeSyncBuffer: ' + writeSyncBuffer.toString());
  } catch (error) {
    console.error('writeSync usbSerial error, ' + JSON.stringify(error));
  }
}

#### serialManager.close

close(portId: number): void

Closes the serial port device.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 31400001 | Serial port management exception. |
| 31400003 | PortId does not exist. |
| 31400005 | The serial port device is not opened. Call the open API first. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f6/v3/_YHpyv_2R6iFAKwh4wDT2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B51B56C7EF57F1D5EC34E87E5C9B0B6B1F2E2B8809D439BED30F2B93E43A05A7)

The following sample code shows the basic process for calling the **close** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function close() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Open a serial port device.
  try {
    serialManager.open(portId)
    console.info('open usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('open usbSerial error, ' + JSON.stringify(error));
    return;
  }

  // Close the serial port device.
  try {
    serialManager.close(portId);
    console.info('close usbSerial success, portId: ' + portId);
  } catch (error) {
    console.error('close usbSerial error, ' + JSON.stringify(error));
  }
}

#### serialManager.cancelSerialRight

cancelSerialRight(portId: number): void

Cancels the permission to access the serial port device when the application is running. This API is used to close the enabled serial port device.

**System capability**: SystemCapability.USB.USBManager.Serial

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| portId | number | Yes | Port number. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../../api-reference-overview/universal-error-codes/document.md) and [USB Error Codes](../../../error-codes/usb-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 14400005 | Database operation exception. |
| 31400001 | Serial port management exception. |
| 31400002 | Access denied. Call requestSerialRight to request user authorization first. |
| 31400003 | PortId does not exist. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/gv8zI3EPRp2EvwXt02us0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062355Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D3D96DE90787D9EE26439CBDD27EEB7AB6819A22EBD1E81F7B04C5208A6978C)

The following sample code shows the basic process for calling the **cancelSerialRight** API and it needs to be executed in a specific method. In actual calling, you must comply with the device-related protocols.

import { JSON } from '@kit.ArkTS';
import { serialManager } from '@kit.BasicServicesKit';

// Obtain the serial port list.
function cancelSerialRight() {
  let portList: serialManager.SerialPort\[\] = serialManager.getPortList();
  console.info('usbSerial portList: ' + JSON.stringify(portList));
  if (portList === undefined || portList.length === 0) {
    console.info('usbSerial portList is empty');
    return;
  }
  let portId: number = portList\[0\].portId;

  // Check whether the device can be accessed by the application.
  if (!serialManager.hasSerialRight(portId)) {
    serialManager.requestSerialRight(portId).then(result => {
      if (!result) {
        // If the application does not have the access permission and is not granted by the user, the application exits.
        console.info('user is not granted the operation  permission');
        return;
      } else {
        console.info('grant permission successfully');
      }
    });
  }

  // Cancel the granted permission.
  try {
    serialManager.cancelSerialRight(portId);
    console.info('cancelSerialRight success, portId: ', portId);
  } catch (error) {
    console.error('cancelSerialRight error, ', JSON.stringify(error));
  }
}

#### SerialAttribute

Represents the configuration parameters of a serial port.

**System capability**: SystemCapability.USB.USBManager.Serial

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| baudRate | [BaudRates](#baudrates) | No | No | Baud rate. |
| dataBits | [DataBits](#databits) | No | Yes | Data bits. The default value is **8**. |
| parity | [Parity](#parity) | No | Yes | Parity check. The default value is **None**, indicating that no parity check is performed. |
| stopBits | [StopBits](#stopbits) | No | Yes | Stop bits. The default value is **1**. |

#### SerialPort

Represents the parameters of a serial port.

**System capability**: SystemCapability.USB.USBManager.Serial

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| portId | number | No | No | Port number. |
| deviceName | string | No | No | Serial port device name. |

#### BaudRates

Enumerates the baud rates.

**System capability**: SystemCapability.USB.USBManager.Serial

| Name | Value | Description |
| :-- | :-- | :-- |
| BAUDRATE\_50 | 50 | The baud rate is 50 bit/s. |
| BAUDRATE\_75 | 75 | The baud rate is 75 bit/s. |
| BAUDRATE\_110 | 110 | The baud rate is 110 bit/s. |
| BAUDRATE\_134 | 134 | The baud rate is 134 bit/s. |
| BAUDRATE\_150 | 150 | The baud rate is 150 bit/s. |
| BAUDRATE\_200 | 200 | The baud rate is 200 bit/s. |
| BAUDRATE\_300 | 300 | The baud rate is 300 bit/s. |
| BAUDRATE\_600 | 600 | The baud rate is 600 bit/s. |
| BAUDRATE\_1200 | 1200 | The baud rate is 1200 bit/s. |
| BAUDRATE\_1800 | 1800 | The baud rate is 1800 bit/s. |
| BAUDRATE\_2400 | 2400 | The baud rate is 2400 bit/s. |
| BAUDRATE\_4800 | 4800 | The baud rate is 4800 bit/s. |
| BAUDRATE\_9600 | 9600 | The baud rate is 9600 bit/s. |
| BAUDRATE\_19200 | 19200 | The baud rate is 19200 bit/s. |
| BAUDRATE\_38400 | 38400 | The baud rate is 38400 bit/s. |
| BAUDRATE\_57600 | 57600 | The baud rate is 57600 bit/s. |
| BAUDRATE\_115200 | 115200 | The baud rate is 115200 bit/s. |
| BAUDRATE\_230400 | 230400 | The baud rate is 230400 bit/s. |
| BAUDRATE\_460800 | 460800 | The baud rate is 460800 bit/s. |
| BAUDRATE\_500000 | 500000 | The baud rate is 500000 bit/s. |
| BAUDRATE\_576000 | 576000 | The baud rate is 576000 bit/s. |
| BAUDRATE\_921600 | 921600 | The baud rate is 921600 bit/s. |
| BAUDRATE\_1000000 | 1000000 | The baud rate is 1000000 bit/s. |
| BAUDRATE\_1152000 | 1152000 | The baud rate is 1152000 bit/s. |
| BAUDRATE\_1500000 | 1500000 | The baud rate is 1500000 bit/s. |
| BAUDRATE\_2000000 | 2000000 | The baud rate is 2000000 bit/s. |
| BAUDRATE\_2500000 | 2500000 | The baud rate is 2500000 bit/s. |
| BAUDRATE\_3000000 | 3000000 | The baud rate is 3000000 bit/s. |
| BAUDRATE\_3500000 | 3500000 | The baud rate is 3500000 bit/s. |
| BAUDRATE\_4000000 | 4000000 | The baud rate is 4000000 bit/s. |

#### DataBits

Enumerates the number of data bits.

**System capability**: SystemCapability.USB.USBManager.Serial

| Name | Value | Description |
| :-- | :-- | :-- |
| DATABIT\_8 | 8 | The number of data bits is 8. |
| DATABIT\_7 | 7 | The number of data bits is 7. |
| DATABIT\_6 | 6 | The number of data bits is 6. |
| DATABIT\_5 | 5 | The number of data bits is 5. |

#### Parity

Enumerates the parity check modes.

**System capability**: SystemCapability.USB.USBManager.Serial

| Name | Value | Description |
| :-- | :-- | :-- |
| PARITY\_NONE | 0 | No parity. |
| PARITY\_ODD | 1 | Odd parity. |
| PARITY\_EVEN | 2 | Even parity. |
| PARITY\_MARK | 3 | Mark parity, whose parity bit is fixed at **1**. |
| PARITY\_SPACE | 4 | Space parity, whose parity bit is fixed at **0**. |

#### StopBits

Enumerates of the number of stop bits.

**System capability**: SystemCapability.USB.USBManager.Serial

| Name | Value | Description |
| :-- | :-- | :-- |
| STOPBIT\_1 | 0 | The number of stop bits is 1. |
| STOPBIT\_2 | 1 | The number of stop bits is 2. |
