# @ohos.file.securityLabel (Data Label)

The **securityLabel** module provides APIs for managing data security levels of files, including obtaining and setting file security levels.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/MBvzoHLNTXS0eWZRuBaZig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=09959BB3A4DC3943BA9286D848B01BDE22F56949B41C323DC26DA2A05814579D)

The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { securityLabel } from '@kit.CoreFileKit';

#### How to Use

Before using the APIs provided by this module to perform operations on a file or directory, obtain the application sandbox path of the file or directory as follows:

import { UIAbility } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onWindowStageCreate(windowStage: window.WindowStage) {
    let context = this.context;
    let pathDir = context.filesDir;
  }
}

For details about how to obtain the application sandbox path, see [Obtaining Application File Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#obtaining-application-file-paths).

#### DataLevel

type DataLevel = 's0' | 's1' | 's2' | 's3' | 's4'

Represents the data security level.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Type | Description |
| :-- | :-- |
| 's0' | Level S0 |
| 's1' | Level S1 |
| 's2' | Level S2 |
| 's3' | Level S3 |
| 's4' | Level S4 |

For details, see [Data Security Labels](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/access-control-by-device-and-data-level#data-security-labels).

#### securityLabel.setSecurityLabel

setSecurityLabel(path:string, type:DataLevel):Promise<void>

Sets the data security level for a file or directory. The level can only be adjusted from low to high, or set to the same level. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path. |
| type | [DataLevel](#datalevel) | Yes | Data security level. The value can only be **s0**, **s1**, **s2**, **s3**, or **s4**. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabel(filePath, "s0").then(() => {
  console.info("setSecurityLabel successfully");
}).catch((err: BusinessError) => {
  console.error("setSecurityLabel failed with error message: " + err.message + ", error code: " + err.code);
});

#### securityLabel.setSecurityLabel

setSecurityLabel(path:string, type:DataLevel, callback: AsyncCallback<void>):void

Sets the data security level for a file or directory. The level can only be adjusted from low to high, or set to the same level. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path. |
| type | [DataLevel](#datalevel) | Yes | Data security level. The value can only be **s0**, **s1**, **s2**, **s3**, or **s4**. |
| callback | AsyncCallback<void> | Yes | Callback used to return the security level. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabel(filePath, "s0", (err: BusinessError) => {
  if (err) {
    console.error("setSecurityLabel failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("setSecurityLabel successfully.");
  }
});

#### securityLabel.setSecurityLabelSync

setSecurityLabelSync(path:string, type:DataLevel):void

Sets the data security level for a file or directory in synchronous mode. The level can only be adjusted from low to high, or set to the same level.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path. |
| type | [DataLevel](#datalevel) | Yes | Data security level. The value can only be **s0**, **s1**, **s2**, **s3**, or **s4**. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Example**

let filePath = pathDir + '/test.txt';
securityLabel.setSecurityLabelSync(filePath, "s0");

#### securityLabel.getSecurityLabel

getSecurityLabel(path:string):Promise<string>

Obtains the data security level of a file or directory. If no data security level has been set, **s3** is returned by default. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise used to return the data security level. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.getSecurityLabel(filePath).then((type: string) => {
  console.info("getSecurityLabel successfully, Label: " + type);
}).catch((err: BusinessError) => {
  console.error("getSecurityLabel failed with error message: " + err.message + ", error code: " + err.code);
});

#### securityLabel.getSecurityLabel

getSecurityLabel(path:string, callback:AsyncCallback<string>): void

Obtains the data security level of a file or directory. If no data security level has been set, **s3** is returned by default. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path. |
| callback | AsyncCallback<string> | Yes | Callback after the data security level is obtained asynchronously. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
let filePath = pathDir + '/test.txt';
securityLabel.getSecurityLabel(filePath, (err: BusinessError, type: string) => {
  if (err) {
    console.error("getSecurityLabel failed with error message: " + err.message + ", error code: " + err.code);
  } else {
    console.info("getSecurityLabel successfully, Label: " + type);
  }
});

#### securityLabel.getSecurityLabelSync

getSecurityLabelSync(path:string):string

Obtains the data security level of a file or directory in synchronous mode. If no data security level has been set, **s3** is returned by default.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | File path. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Promise used to return the data security level. |

**Error codes**

For details about the error codes, see [Basic File IO Error Codes](../../error-codes/file-management-error-codes/document.md#basic-file-io-error-codes).

| ID | Error Message |
| :-- | :-- |
| 13900001 | Operation not permitted |
| 13900007 | Arg list too long |
| 13900015 | File exists |
| 13900020 | Invalid argument |
| 13900025 | No space left on device |
| 13900037 | No data available |
| 13900041 | Quota exceeded |
| 13900042 | Unknown error |

**Example**

let filePath = pathDir + '/test.txt';
let type = securityLabel.getSecurityLabelSync(filePath);
console.info("getSecurityLabel successfully, Label: " + type);
