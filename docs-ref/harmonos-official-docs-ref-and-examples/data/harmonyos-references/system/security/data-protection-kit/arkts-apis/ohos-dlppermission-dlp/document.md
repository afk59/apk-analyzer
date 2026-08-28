# @ohos.dlpPermission (DLP)

Data loss prevention (DLP) is a system solution provided to prevent data disclosure. The **dlpPermission** module provides APIs for cross-device file access management, encrypted storage, and access authorization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/uskODr3YT8aC2LE3eyUt5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A4532B6D6887E2BAD26655F5C64090A88E26D0DB67871A65A55C56E0074FF2C4)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The kit to which **@ohos.dlpPermission** belongs has been changed from DataLossPreventionKit to DataProtectionKit. You are advised to use the new module name @kit.DataProtectionKit to import the module. If @kit.DataLossPreventionKit is imported, only the APIs before the change can be called and the APIs after the change cannot be used.

#### Modules to Import

import { dlpPermission } from '@kit.DataProtectionKit';

#### dlpPermission.isDLPFile

isDLPFile(fd: number): Promise<boolean>

Checks whether a file is a DLP file based on the FD. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file to be checked. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the file is a DLP file; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
let file: number | undefined = undefined;
try {
  file = fileIo.openSync(uri).fd;
  let res = dlpPermission.isDLPFile(file);
  console.info('res', res);
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
} finally {
  if (file !== undefined) {
    fileIo.closeSync(file);
  }
}

#### dlpPermission.isDLPFile

isDLPFile(fd: number, callback: AsyncCallback<boolean>): void

Checks whether a file is a DLP file based on the FD. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | FD of the file to be checked. |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. The value **true** means the file is a DLP file; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
let file: number | undefined = undefined;
try {
  file = fileIo.openSync(uri).fd;
  dlpPermission.isDLPFile(file, (err, res) => {
    if (err != undefined) {
      console.error('isDLPFile error,', err.code, err.message);
    } else {
      console.info('res', res);
    }
    fileIo.closeSync(file);
  });
} catch (err) {
  console.error('isDLPFile error,', (err as BusinessError).code, (err as BusinessError).message);
  if (file !== undefined) {
    fileIo.closeSync(file);
  }
}

#### dlpPermission.getDLPPermissionInfo

getDLPPermissionInfo(): Promise<DLPPermissionInfo>

Obtains the permission information of this DLP file. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DLPPermissionInfo](#dlppermissioninfo)\> | Promise used to return the permission information about the DLP file. The operation is successful if no error is reported. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100001 | Invalid parameter value. |
| 19100006 | No permission to call this API, which is available only for DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    dlpPermission.isInSandbox().then(async (inSandbox) => { // Check whether the application is running in a sandbox.
      if (inSandbox) {
        let res: dlpPermission.DLPPermissionInfo = await dlpPermission.getDLPPermissionInfo(); // Obtain the permission information.
        console.info('res', JSON.stringify(res));
      }
    });
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  }
}

#### dlpPermission.getDLPPermissionInfo

getDLPPermissionInfo(callback: AsyncCallback<DLPPermissionInfo>): void

Obtains the permission information of this DLP file. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[DLPPermissionInfo](#dlppermissioninfo)\> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100006 | No permission to call this API, which is available only for DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.isInSandbox().then((inSandbox) => { // Check whether the application is running in a sandbox.
    if (inSandbox) {
      dlpPermission.getDLPPermissionInfo((err, res) => {
        if (err != undefined) {
          console.error('getDLPPermissionInfo error', err.code, err.message);
        } else {
          console.info('res', JSON.stringify(res));
        }
      }); // Obtain the permission information.
    }
  });
} catch (err) {
  console.error('getDLPPermissionInfo error', (err as BusinessError).code, (err as BusinessError).message);
}

#### dlpPermission.getOriginalFileName

getOriginalFileName(fileName: string): string

Obtains the original file name of a DLP file. This API returns the result synchronously.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fileName | string | Yes | Name of the target file. The value contains up to 255 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Original name of the DLP file obtained. For example, if the DLP file name is **test.txt.dlp**, the original file name returned is **test.txt**. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let res = dlpPermission.getOriginalFileName('test.txt.dlp'); // Obtain the original file name.
  console.info('res', res);
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.getDLPSuffix

getDLPSuffix(): string

Obtains the DLP file name extension. This API returns the result synchronously.

**System capability**: SystemCapability.Security.DataLossPrevention

**Return value**

| Type | Description |
| :-- | :-- |
| string | DLP file name extension obtained. For example, if the original file name is **text.txt**, the encrypted DLP file name is **test.txt.dlp**, and the returned extension is **.dlp**. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let res = dlpPermission.getDLPSuffix(); // Obtain the DLP file name extension.
  console.info('res', res);
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.on('openDLPFile')

on(type: 'openDLPFile', listener: Callback<AccessedDLPFileInfo>): void

Subscribes to a DLP file open event. The application will be notified when the DLP file is opened.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'openDLPFile' | Yes | Event type. It has a fixed value of **openDLPFile**, which indicates the DLP file open event. |
| listener | Callback<[AccessedDLPFileInfo](#accesseddlpfileinfo)\> | Yes | Callback invoked when a DLP file is opened. The application will be notified when the DLP file is opened. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.on('openDLPFile', (info: dlpPermission.AccessedDLPFileInfo) => {
    console.info('openDlpFile event', info.uri, info.lastOpenTime)
  }); // Subscribe to a DLP file open event.
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.off('openDLPFile')

off(type: 'openDLPFile', listener?: Callback<AccessedDLPFileInfo>): void

Unsubscribes from the DLP file open event. The application will not be notified when a DLP file is opened.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | 'openDLPFile' | Yes | Event type. It has a fixed value of **openDLPFile**, which indicates the DLP file open event. |
| listener | Callback<[AccessedDLPFileInfo](#accesseddlpfileinfo)\> | No | Callback for the DLP file open event. The application will not be notified when a DLP file is opened. By default, this parameter is left blank, which unregisters all callbacks for the file open event. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.off('openDLPFile', (info: dlpPermission.AccessedDLPFileInfo) => {
    console.info('openDlpFile event', info.uri, info.lastOpenTime)
  }); // Unsubscribe from the DLP file open event.
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.isInSandbox

isInSandbox(): Promise<boolean>

Checks whether this application is running in a DLP sandbox environment. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the application is running in a sandbox; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let inSandbox = dlpPermission.isInSandbox(); // Check whether the application is running in a sandbox.
  console.info('res', inSandbox);
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.isInSandbox

isInSandbox(callback: AsyncCallback<boolean>): void

Checks whether this application is running in a DLP sandbox environment. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<boolean> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. The value **true** means the application is running in a sandbox; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.isInSandbox((err, data) => {
    if (err) {
      console.error('isInSandbox error', err.code, err.message);
    } else {
      console.info('isInSandbox, data', JSON.stringify(data));
    }
  }); // Whether the application is running in a sandbox.
} catch (err) {
  console.error('isInSandbox error', (err as BusinessError).code, (err as BusinessError).message);
}

#### dlpPermission.getDLPSupportedFileTypes

getDLPSupportedFileTypes(): Promise<Array<string>>

Obtains the file name extension types that support DLP. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the file name extension types obtained. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let res = dlpPermission.getDLPSupportedFileTypes(); // Obtain the file types that support DLP.
  console.info('res', JSON.stringify(res));
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.getDLPSupportedFileTypes

getDLPSupportedFileTypes(callback: AsyncCallback<Array<string>>): void

Obtains the file name extension types that support DLP. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<string>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getDLPSupportedFileTypes((err, res) => {
    if (err != undefined) {
      console.error('getDLPSupportedFileTypes error', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // Obtain the file types that support DLP.
} catch (err) {
  console.error('getDLPSupportedFileTypes error', (err as BusinessError).code, (err as BusinessError).message);
}

#### dlpPermission.setRetentionState

setRetentionState(docUris: Array<string>): Promise<void>

Sets the sandbox retention state. This API uses an asynchronous callback to return the result. A sandbox application is automatically installed when a DLP file is opened, and automatically uninstalled when the DLP file is closed. Once the sandbox retention state is set for a DLP file, the sandbox application will not be automatically uninstalled when the DLP file is closed. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| docUris | Array<string> | Yes | URIs of the files to be set with the retention state. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100006 | No permission to call this API, which is available only for DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
  try {
    let inSandbox = await dlpPermission.isInSandbox(); // Check whether the application is running in a sandbox.
    if (inSandbox) {
      dlpPermission.setRetentionState(\[uri\]); // Set the retention state for a sandbox application.
    }
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  }
}

#### dlpPermission.setRetentionState

setRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void

Sets the sandbox retention state. This API uses an asynchronous callback to return the result. A sandbox application is automatically installed when a DLP file is opened, and automatically uninstalled when the DLP file is closed. Once the sandbox retention state is set for a DLP file, the sandbox application will not be automatically uninstalled when the DLP file is closed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| docUris | Array<string> | Yes | URIs of the files to be set with the retention state. The array has no length limit, but each string cannot exceed 4095 bytes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100006 | No permission to call this API, which is available only for DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
try {
  dlpPermission.setRetentionState(\[uri\], (err, res) => {
    if (err != undefined) {
      console.error('setRetentionState error,', err.code, err.message);
    } else {
      console.info('setRetentionState success');
      console.info('res', JSON.stringify(res));
    }
  }); // Set the sandbox retention state.
} catch (err) {
  console.error('setRetentionState error,', (err as BusinessError).code, (err as BusinessError).message);
}

#### dlpPermission.cancelRetentionState

cancelRetentionState(docUris: Array<string>): Promise<void>

Cancels the sandbox retention state, that is, allows the sandbox application to be automatically uninstalled when the DLP file is closed. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| docUris | Array<string> | Yes | URIs of the files to be set with the retention state. The array has no length limit, but each string cannot exceed 4095 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
try {
  dlpPermission.cancelRetentionState(\[uri\]); // Cancel the retention state for a sandbox application.
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.cancelRetentionState

cancelRetentionState(docUris: Array<string>, callback: AsyncCallback<void>): void

Cancels the sandbox retention state, that is, allows the sandbox application to be automatically uninstalled when the DLP file is closed. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| docUris | Array<string> | Yes | URIs of the files to be set with the retention state. The array has no length limit, but each string cannot exceed 4095 bytes. |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

let uri = "file://docs/storage/Users/currentUser/Desktop/test.txt.dlp";
try {
  dlpPermission.cancelRetentionState(\[uri\], (err, res) => {
    if (err != undefined) {
      console.error('cancelRetentionState error,', err.code, err.message);
    } else {
      console.info('cancelRetentionState success');
    }
  }); // Cancel the sandbox retention state.
} catch (err) {
  console.error('cancelRetentionState error,', (err as BusinessError).code, (err as BusinessError).message);
}

#### dlpPermission.getRetentionSandboxList

getRetentionSandboxList(bundleName?: string): Promise<Array<RetentionSandboxInfo>>

Obtains the sandbox applications in the retention state of an application. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | No | Bundle name of the application. By default, this parameter is left empty, which obtains the sandbox retention information about the current application. The value contains 7 to 128 bytes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[RetentionSandboxInfo](#retentionsandboxinfo)\>> | Promise used to return the sandbox retention information obtained. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    let res:Array<dlpPermission.RetentionSandboxInfo> = await dlpPermission.getRetentionSandboxList(); // Obtain the sandbox apps in the retention state.
    console.info('res', JSON.stringify(res))
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  }
}

#### dlpPermission.getRetentionSandboxList

getRetentionSandboxList(bundleName: string, callback: AsyncCallback<Array<RetentionSandboxInfo>>): void

Obtains the sandbox applications in the retention state of an application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleName | string | Yes | Bundle name of the application. The value contains 7 to 128 bytes. |
| callback | AsyncCallback<Array<[RetentionSandboxInfo](#retentionsandboxinfo)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getRetentionSandboxList("bundleName", (err, res) => {
    if (err != undefined) {
      console.error('getRetentionSandboxList error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // Obtain the sandbox retention information.
} catch (err) {
  console.error('getRetentionSandboxList error,', (err as BusinessError).code, (err as BusinessError).message);
}

#### dlpPermission.getRetentionSandboxList

getRetentionSandboxList(callback: AsyncCallback<Array<RetentionSandboxInfo>>): void

Obtains the sandbox applications in the retention state of an application. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[RetentionSandboxInfo](#retentionsandboxinfo)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getRetentionSandboxList((err, res) => {
    if (err != undefined) {
      console.error('getRetentionSandboxList error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // Obtain the sandbox retention information.
} catch (err) {
  console.error('getRetentionSandboxList error,', (err as BusinessError).code, (err as BusinessError).message);
}

#### dlpPermission.getDLPFileAccessRecords

getDLPFileAccessRecords(): Promise<Array<AccessedDLPFileInfo>>

Obtains the list of DLP files that are accessed recently. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[AccessedDLPFileInfo](#accesseddlpfileinfo)\>> | Promise used to return the list of recently accessed files obtained. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    let res:Array<dlpPermission.AccessedDLPFileInfo> = await dlpPermission.getDLPFileAccessRecords(); // Obtain the list of recently accessed DLP files.
    console.info('res', JSON.stringify(res))
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  }
}

#### dlpPermission.getDLPFileAccessRecords

getDLPFileAccessRecords(callback: AsyncCallback<Array<AccessedDLPFileInfo>>): void

Obtains the list of DLP files that are accessed recently. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<Array<[AccessedDLPFileInfo](#accesseddlpfileinfo)\>> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**. Otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.getDLPFileAccessRecords((err, res) => {
    if (err != undefined) {
      console.error('getDLPFileAccessRecords error,', err.code, err.message);
    } else {
      console.info('res', JSON.stringify(res));
    }
  }); // Obtain the list of recently accessed DLP files.
} catch (err) {
  console.error('getDLPFileAccessRecords error,', (err as BusinessError).code, (err as BusinessError).message);
}

#### dlpPermission.startDLPManagerForResult11+

startDLPManagerForResult(context: common.UIAbilityContext, want: Want): Promise<DLPManagerResult>

Starts the DLP manager application on the current UIAbility page in borderless mode. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/uIlUQQsFQ4WFSZYj17Yhww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=338B3447C9EDD6B2E428D44472BC948B50D4E9D0A50083EBBC3FA30C1FCF798A)

This API can be called only by domain accounts.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | [common.UIAbilityContext](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/uiabilitycontext/document.md) | Yes | UIAbility context. |
| want | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | Yes | Object that requests the start of the DLP manager application. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[DLPManagerResult](#dlpmanagerresult11)\> | Promise used to return the **DLPManagerResult** object. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |
| 19100016 | The uri field is missing in the want parameter. |
| 19100017 | The displayName field is missing in the want parameter. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { common, Want } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';

try {
  let context = new UIContext().getHostContext() as common.UIAbilityContext; // Obtain the current UIAbilityContext.
  let want: Want = {
    "uri": "file://docs/storage/Users/currentUser/Desktop/1.txt",
    "parameters": {
      "displayName": "1.txt"
    }
  }; // Request parameters.
  dlpPermission.startDLPManagerForResult(context, want).then((res) => {
    console.info('res.resultCode', res.resultCode);
    console.info('res.want', JSON.stringify(res.want));
  }); // Start the DLP manager application.
} catch (err) {
  console.error('error', err.code, err.message); // Throw an error if the operation fails.
}

#### dlpPermission.setSandboxAppConfig11+

setSandboxAppConfig(configInfo: string): Promise<void>

Sets sandbox application configuration. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| configInfo | string | Yes | Sandbox application configuration. The length is less than 4 MB. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |
| 19100018 | The application is not authorized. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.setSandboxAppConfig('configInfo'); // Set sandbox application configuration.
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.cleanSandboxAppConfig11+

cleanSandboxAppConfig(): Promise<void>

Cleans sandbox application configuration. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100001 | Invalid parameter value. |
| 19100007 | No permission to call this API, which is available only for non-DLP sandbox applications. |
| 19100011 | The system ability works abnormally. |
| 19100018 | The application is not authorized. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  dlpPermission.cleanSandboxAppConfig(); // Clean sandbox application configuration.
} catch (err) {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
}

#### dlpPermission.getSandboxAppConfig11+

getSandboxAppConfig(): Promise<string>

Obtains sandbox application configuration. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.DataLossPrevention

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the sandbox application configuration obtained. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |
| 19100018 | The application is not authorized. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction() {
  try {
    let res = await dlpPermission.getSandboxAppConfig() // Obtain the sandbox application configuration.
    console.info('res', JSON.stringify(res));
  } catch (err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
  }
}

#### dlpPermission.isDLPFeatureProvided12+

isDLPFeatureProvided(): Promise<boolean>

Queries whether the current system provides the data encryption feature. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/NDPHGk3dR4eYRS_DIaZpBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B842E911B453FE81F91EB6DA2907AD53AAB59F2AAC69B42A5DC7D035484C7B0D)

This API is enabled by the [MDM](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/mdm-kit-intro) kit and is used for enterprise devices. For other devices (such as consumer devices), this API is inapplicable. Calling it returns **false**.

**System capability**: SystemCapability.Security.DataLossPrevention

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** means the current system provides the data encryption feature; the value **false** means the opposite. |

**Error codes**

For details about the error codes, see [DLP Service Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 19100011 | The system ability works abnormally. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { BusinessError } from '@kit.BasicServicesKit';

dlpPermission.isDLPFeatureProvided().then((res) => {
  console.info('res', JSON.stringify(res));
}).catch((err: BusinessError) => {
  console.error('error', (err as BusinessError).code, (err as BusinessError).message); // Throw an error if the operation fails.
});

#### dlpPermission.setEnterprisePolicy21+

setEnterprisePolicy(policy: EnterprisePolicy): void

Sets the protection policy for enterprise applications.

**Required permissions**: ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| policy | [EnterprisePolicy](#enterprisepolicy21) | Yes | Protection policy to be set for enterprise applications. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DLP Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100011 | The system ability works abnormally. |
| 19100021 | Failed to set the enterprise policy. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';

interface Attribute {
  attributeId: string;
  attributeValues: Array<string>;
  valueType: number;
  opt: number;
}

interface Rule {
  ruleId: string;
  attributes: Array<Attribute>;
}

interface Policy {
  rules: Array<Rule>;
  policyId: string;
  ruleConflictAlg: number;
}

try {
  let attributeValues: Array<string> = \[ '1' \];
  let attribute: Attribute = {
    attributeId: 'DeviceHealthyStatus',
    attributeValues: attributeValues,
    valueType: 0,
    opt: 2
  }; // Attribute information
  let rule: Rule = {
    ruleId: 'ruleId',
    attributes: \[ attribute \]
  }; // Rules
  let policy: Policy = {
    rules: \[ rule \],
    policyId: 'policyId',
    ruleConflictAlg: 0
  }; // Policy
  let enterprisePolicy: dlpPermission.EnterprisePolicy = {
    policyString: JSON.stringify(policy)
  };
  dlpPermission.setEnterprisePolicy(enterprisePolicy);
  console.info('set enterprise policy success');
} catch (err) {
  console.error('error:' + err.code + err.message); // Throw an error if the operation fails.
}

#### ActionFlagType

Enumerates the operations that can be performed on a DLP file. For example, the DLP sandbox application can dim its button based on this parameter.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Value | Description |
| :-- | :-- | :-- |
| ACTION\_VIEW | 0x00000001 | View the file. |
| ACTION\_SAVE | 0x00000002 | Save the file. |
| ACTION\_SAVE\_AS | 0x00000004 | Save the file as another file. |
| ACTION\_EDIT | 0x00000008 | Edit the file. |
| ACTION\_SCREEN\_CAPTURE | 0x00000010 | Capture screenshots of the file. |
| ACTION\_SCREEN\_SHARE | 0x00000020 | Share the screen of the file. |
| ACTION\_SCREEN\_RECORD | 0x00000040 | Record the screen on which the file is open. |
| ACTION\_COPY | 0x00000080 | Copy the file. |
| ACTION\_PRINT | 0x00000100 | Print the file. |
| ACTION\_EXPORT | 0x00000200 | Export the file. |
| ACTION\_PERMISSION\_CHANGE | 0x00000400 | Modify the permissions on the file. |

#### DLPFileAccess

Enumerates the permissions on a DLP file.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_PERMISSION | 0 | The user has no permission on the file. |
| READ\_ONLY | 1 | The user has only the permission to read the file. |
| CONTENT\_EDIT | 2 | The user has the permission to edit the file. |
| FULL\_CONTROL | 3 | The user has full control on the file. |

#### DLPPermissionInfo

Represents the permission information about a DLP file.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| dlpFileAccess | [DLPFileAccess](#dlpfileaccess) | No | No | User permission on the DLP file, for example, read-only. |
| flags | number | No | No | Operations that can be performed on the DLP file. It is a combination of different [ActionFlagTypes](#actionflagtype). |

#### AccessedDLPFileInfo

Represents the information about a DLP file opened.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | No | URI of the DLP file. The value contains up to 4095 bytes. |
| lastOpenTime | number | No | No | Time when the file was last opened. |

#### DLPManagerResult11+

Represents information about the trigger of the DLP manager application.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| resultCode | number | No | No | Result code returned after the DLP manager application is started and exits. |
| want | [Want](../../../../../application-framework/ability-kit/arkts-apis/both-models-recommended/ohos-app-ability-want-want/document.md) | No | No | Data returned after the DLP manager application is started and exits. |

#### RetentionSandboxInfo

Represents the sandbox retention information.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| appIndex | number | No | No | Index of the DLP sandbox application. |
| bundleName | string | No | No | Bundle name of the application. The value contains 7 to 128 bytes. |
| docUris | Array<string> | No | No | URI list of the DLP files. The array has no length limit, but each string cannot exceed 4095 bytes. |

#### EnterprisePolicy21+

Represents an enterprise custom policy.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| policyString | string | No | No | JSON string of an enterprise custom policy. The length cannot exceed 4 MB. |

#### dlpPermission.generateDlpFileForEnterprise21+

generateDlpFileForEnterprise(plaintextFd: number, dlpFd: number, property: DLPProperty, customProperty: CustomProperty): Promise<void>

Obtains a **DLPFile** object. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d3/v3/lnJIFg9QRvG_1hnwx3_W7A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5FA8025B6A2119F94ACD9D918990E3F36D0572E03AA7670DA163974169BB6A1)

This API can be called only by enterprise accounts. Enterprises need to set up their own enterprise account servers. This API generates a DLP file, which is an encrypted file that can be accessed only by accounts authorized by the enterprise server.

**Required permissions**: ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| plaintextFd | number | Yes | FD of a plaintext file. |
| dlpFd | number | Yes | FD of an encrypted file. |
| property | [DLPProperty](#dlpproperty21) | Yes | General policy of DLP files. |
| customProperty | [CustomProperty](#customproperty21) | Yes | Enterprise custom policy. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DLP Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |
| 19100005 | Credential authentication server error. |
| 19100009 | Failed to operate the DLP file. |
| 19100011 | The system ability works abnormally. |
| 19100014 | Account not logged in. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction(plainFilePath: string, dlpFilePath: string) {
  let plaintextFd: number | undefined = undefined;
  let dlpFd: number | undefined = undefined;
  try {
    plaintextFd = fileIo.openSync(plainFilePath, fileIo.OpenMode.READ\_ONLY).fd;
    dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE).fd;
    let dlpProperty: dlpPermission.DLPProperty = {
      ownerAccount: 'zhangsan',
      ownerAccountType: dlpPermission.AccountType.DOMAIN\_ACCOUNT,
      authUserList: \[\],
      contactAccount: 'zhangsan',
      offlineAccess: true,
      ownerAccountID: 'xxxxxxx',
      everyoneAccessList: \[\]
    };
    let customProperty: dlpPermission.CustomProperty = {
      enterprise: 'customProperty'
    };
    await dlpPermission.generateDlpFileForEnterprise(plaintextFd, dlpFd, dlpProperty, customProperty);
    console.info('Successfully generate DLP file for enterprise.');
  } catch(err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message);
  } finally {
    if (dlpFd) {
      fileIo.closeSync(dlpFd);
    }
    if (plaintextFd) {
      fileIo.closeSync(plaintextFd);
    }
  }
}

#### dlpPermission.decryptDlpFile21+

decryptDlpFile(dlpFd: number, plaintextFd: number): Promise<void>

Decrypts a DLP file to generate a plaintext file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/8aKBCmQpSg6rc_tlY0mfWg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=94BACD7841EF76A54B12DD71CECF922830B4332D0CF7499379F1C5125E6E03DA)

This API can be called only by enterprise accounts. Enterprises need to set up their own enterprise account servers. The enterprise server determines whether an account is authorized to decrypt DLP files.

**Required permissions**: ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dlpFd | number | Yes | FD of the file to be decrypted. |
| plaintextFd | number | Yes | FD of the decrypted file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DLP Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |
| 19100005 | Credential authentication server error. |
| 19100008 | The file is not a DLP file. |
| 19100009 | Failed to operate the DLP file. |
| 19100011 | The system ability works abnormally. |
| 19100013 | The user does not have the permission. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction(plainFilePath: string, dlpFilePath: string) {
  let plaintextFd: number | undefined = undefined;
  let dlpFd: number | undefined = undefined;
  try {
    plaintextFd = fileIo.openSync(plainFilePath, fileIo.OpenMode.READ\_WRITE | fileIo.OpenMode.CREATE).fd;
    dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ\_ONLY).fd;
    await dlpPermission.decryptDlpFile(dlpFd, plaintextFd);
    console.info('Successfully decrypt DLP file.');
  } catch(err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message);
  } finally {
    if (dlpFd) {
      fileIo.closeSync(dlpFd);
    }
    if (plaintextFd) {
      fileIo.closeSync(plaintextFd);
    }
  }
}

#### dlpPermission.queryDlpPolicy21+

queryDlpPolicy(dlpFd: number): Promise<string>

Parses the file header in a DLP file to obtain the DLP plaintext policy. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| dlpFd | number | Yes | FD of the file to be decrypted. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the JSON string of the DLP policy. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DLP Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |
| 19100005 | Credential authentication server error. |
| 19100008 | The file is not a DLP file. |
| 19100009 | Failed to operate the DLP file. |
| 19100011 | The system ability works abnormally. |
| 19100013 | The user does not have the permission. |

**Example**

import { dlpPermission } from '@kit.DataProtectionKit';
import { fileIo } from '@kit.CoreFileKit';
import { BusinessError } from '@kit.BasicServicesKit';

async function ExampleFunction(dlpFilePath: string) {
  let dlpFd : number | undefined = undefined;
  try {
    dlpFd = fileIo.openSync(dlpFilePath, fileIo.OpenMode.READ\_ONLY).fd;
    let policy: string = await dlpPermission.queryDlpPolicy(dlpFd);
    console.info('DLP policy:' + policy);
  } catch(err) {
    console.error('error', (err as BusinessError).code, (err as BusinessError).message);
  } finally {
    if (dlpFd) {
      fileIo.closeSync(dlpFd);
    }
  }
}

#### ActionType21+

Enumerates the actions to be performed when the file's permission expiration time is reached. The default value is **NOT\_OPEN**.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Value | Description |
| :-- | :-- | :-- |
| NOT\_OPEN | 0 | Users are not allowed to open the DLP file when the file's permission expiration time is reached. |
| OPEN | 1 | Logged-in users are allowed to edit the DLP file when the file's permission expiration time is reached. |

#### AccountType21+

Enumerates the types of authorized accounts.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Value | Description |
| :-- | :-- | :-- |
| CLOUD\_ACCOUNT | 1 | Cloud account. |
| DOMAIN\_ACCOUNT | 2 | Domain account. |
| ENTERPRISE\_ACCOUNT | 4 | Enterprise account. |

#### CustomProperty21+

Represents a custom policy.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| enterprise | string | No | No | JSON string of an enterprise custom policy. The length cannot exceed 4 MB. |

#### DLPProperty21+

Represents the authorization information.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| ownerAccount | string | No | No | Account of the owner who can set the permission. The value contains up to 255 bytes. |
| ownerAccountID | string | No | No | Account ID of the owner. The value contains up to 255 bytes. |
| ownerAccountType | [AccountType](#accounttype21) | No | No | Account type of the owner. |
| authUserList | Array<[AuthUser](#authuser21)\> | No | Yes | List of users who are authorized to access the DLP file. By default, this parameter is left blank. |
| contactAccount | string | No | No | Account of the contact. The value contains up to 255 bytes. |
| offlineAccess | boolean | No | No | Whether the file can be accessed offline. **true**: yes; **false**: no. |
| everyoneAccessList | Array<[DLPFileAccess](#dlpfileaccess)\> | No | Yes | Permission granted to everyone. This parameter is left blank by default. |
| expireTime | number | No | Yes | Timestamp when the file permission has expired. This parameter is left blank by default. |
| actionUponExpiry | [ActionType](#actiontype21) | No | Yes | Whether the file can be opened after the permission expires (with the editing permission). This parameter is valid only when **expireTime** is not empty. |
| fileId | string | No | Yes | File identifier. The value contains up to 255 bytes. |
| allowedOpenCount | number | No | Yes | Number of allowed opening times. |

#### AuthUser21+

Represents the user authorization information.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| authAccount | string | No | No | Account of the user who can access the DLP file. The value contains up to 255 bytes. |
| authAccountType | [AccountType](#accounttype21) | No | No | Type of the account. |
| dlpFileAccess | [DLPFileAccess](#dlpfileaccess) | No | No | Permission granted to the user. |
| permExpiryTime | number | No | No | Time when the authorization expires. |

#### DlpConnPlugin21+

Registers the callback capability with the system ability (SA). This API is used in the **registerPlugin** API.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/yiw6U2_5RJuaN7bisbjHvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4C418F13034D19DDE4DAFC18870A3D552ECBEF37133A43DFAC3D287D4EFEEF1)

[registerPlugin](#registerplugin21) requires identical parameters to this API. [connectServer](#connectserver21) is called by the SA and the parameters are returned through the callback.

#### \[h2\]connectServer21+

connectServer(requestId: string, requestData: string, callback: Callback<string>): void

This API is called by the SA. After processing the cloud connection capability, it will be called as a callback in the SA.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/f14RSdw3R56vmUvNyBfkTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E1247A065037E2376F3D2E64A9E3319FEB97BBC74BE0673B4523CA3519BF306)

**connectServer** indicates a call from the system capability side to the frontend.

**Required permissions**: ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| requestId | string | Yes | ID of the request transferred by the SA. |
| requestData | string | Yes | Data transferred by the SA. |
| callback | Callback<string> | Yes | API transferred by the SA, which is used for callback. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DLP Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 19100011 | The system ability works abnormally. |

#### DlpConnManager21+

Calls **registerPlugin** and **unregisterPlugin** to register and deregister callback capabilities in the SA.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/5viZ7yPsSq2bAKGRG0IVxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FE632F8DE9E259999F5021AF81A5F413B063FEB4BF63BA737191DC993049B5A2)

**registerPlugin** registers callback capabilities in the SA, and **unregisterPlugin** deregisters callback capabilities from the SA.

#### \[h2\]constructor21+

constructor()

Represents a constructor for instantiating [DlpConnManager](#dlpconnmanager21).

**Required permissions**: ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |

#### \[h2\]registerPlugin21+

static registerPlugin(plugin: DlpConnPlugin): number

Registers a callback with the SA.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/vCk7iQeORD6QnnM9m_pbUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=301CD111606700ED98887703056BF81A0B4901035932BAF5829C56F591F7511E)

**registerPlugin** registers the callback with the SA.

**Required permissions**: ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| plugin | [DlpConnPlugin](#dlpconnplugin21) | Yes | Callback capability. |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Registration result, which indicates the ID of the callback. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DLP Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |

#### \[h2\]unregisterPlugin21+

static unregisterPlugin(): void

Unregisters a callback from the SA.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/1LsQFBu_Soyega2b4qIZkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=378412CE6727AB9EDBDE2F58B2F45C81F30C0172A6A669D184A4FD35A56EE216)

**unregisterPlugin** deregisters a plug-in from the SA.

**Required permissions**: ohos.permission.ENTERPRISE\_ACCESS\_DLP\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DLP Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 19100001 | Invalid parameter value. |
| 19100002 | Credential service busy due to too many tasks or duplicate tasks. |
| 19100003 | Credential task time out. |
| 19100004 | Credential service error. |
