# openFileBoost

This module provides the status awareness capability of file opening boost for apps. An app can integrate with the corresponding APIs to detect the file opening boost status, and then provide a unique user interface (UI) identifier for the boosted file, improving experience when opening the file.

**Start version**: 5.0.5(17)

#### Module Import

import { openFileBoost } from '@kit.PreviewKit';

#### FilePreloadState

Enumerates the file pre-loading status.

**System capability**: SystemCapability.PCService.OpenFileBoost

**Start version**: 5.0.5(17)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NOT\_PRELOADED

 | 

0

 | 

The file is not preloaded.

 |
| 

PRELOADING

 | 

1

 | 

File is preloading.

 |
| 

PRELOADED

 | 

2

 | 

File preloading completed.

 |

#### FilePreloadStatusInfo

Describes the file preloading status information.

**System capability**: SystemCapability.PCService.OpenFileBoost

**Start version**: 5.0.5(17)

| 
Parameter

 | 

Type

 | 

Read-only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

sandboxPath

 | 

string

 | 

No

 | 

No

 | 

Sandbox path of the file.

 |
| 

progress

 | 

number

 | 

No

 | 

No

 | 

File preloading progress.

 |
| 

state

 | 

[FilePreloadState](#section1081123302517)

 | 

No

 | 

No

 | 

File preloading status.

 |

#### openFileBoost.on('filePreloadStateChanged')

on(type: 'filePreloadStateChanged', callback: Callback<FilePreloadStatusInfo>): void

Registers the callback for file preloading status events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PCService.OpenFileBoost

**Start version**: 5.0.5(17)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event callback type, which is fixed to **filePreloadStateChanged**. This event is triggered whenever the file preloading status changes, returning the corresponding information.

 |
| 

callback

 | 

Callback<[FilePreloadStatusInfo](#section2913441120)\>

 | 

Yes

 | 

Callback used to return the file preloading status.

 |

**Error codes**:

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Module Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter check failed.

 |
| 

1017220001

 | 

Internal failure.

 |
| 

1017220002

 | 

Service unavailable.

 |

**Example**:

import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

function  callback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADING) {
    // The file is preloading, and the app can customize its UX design.
    hilog.info(0x0000, 'testTag', \`file is PRELOADING, suggest to show loading animation\`);
  }
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.PRELOADED) {
    // Preloading is complete, and the app can display a boost completion message.
    hilog.info(0x0000, 'testTag', \`file is PRELOADED, suggest to show loaded animation\`);
  }
  if (filePreloadStatusInfo.state === openFileBoost.FilePreloadState.NOT\_PRELOADED) {
    // No file is preloaded, and the app displays nothing.
    hilog.info(0x0000, 'testTag', \`file is UNPRELOADED, suggest do not show animation \`);
  }
}

function register(): void {
  try {
    openFileBoost.on('filePreloadStateChanged', callback);
  } catch(error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    hilog.error(0x0000, 'testTag', \`on filePreloadStateChanged failed, error code: ${code}, message: ${message}.\`);
  }
}

#### openFileBoost.off('filePreloadStateChanged')

off(type: 'filePreloadStateChanged', callback?: Callback<FilePreloadStatusInfo>): void

Unregisters the callback for file preloading status events. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.PCService.OpenFileBoost

**Start version**: 5.0.5(17)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event callback type, which is fixed to **filePreloadStateChanged**. This event is triggered whenever the file preloading status changes, returning the corresponding information.

 |
| 

callback

 | 

Callback<[FilePreloadStatusInfo](#section2913441120)\>

 | 

No

 | 

Callback used to return the result. If this parameter is specified, the subscription to the specified event with the specified callback is canceled. (The callback object cannot be an anonymous function.) Otherwise, the subscriptions to the specified event with all the callbacks are canceled.

 |

**Error codes**:

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Module Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter check failed.

 |
| 

1017220001

 | 

Internal failure.

 |
| 

1017220002

 | 

Service unavailable.

 |

**Example**:

import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

function callback1(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  hilog.info(0x0000, 'testTag', \`on filePreloadStateChanged in callback1\`);
}
function callback2(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  hilog.info(0x0000, 'testTag', \`on filePreloadStateChanged in callback2\`);
}
function callback3(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  hilog.info(0x0000, 'testTag', \`on filePreloadStateChanged in callback3\`);
}

function testUnregister(): void {
  try {
    openFileBoost.on('filePreloadStateChanged', callback1);
    openFileBoost.on('filePreloadStateChanged', callback2);
    openFileBoost.on('filePreloadStateChanged', callback3);
    // To cancel only the listening of callback1, pass callback1 as a parameter. Then callback1 will not be called for notification.
    openFileBoost.off('filePreloadStateChanged', callback1);
    // To cancel the listening of all callbacks, do not specify the second optional parameter. Then callback2 and callback3 will not be called for notification.
    openFileBoost.off('filePreloadStateChanged');
  } catch(error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    hilog.error(0x0000, 'testTag', \`off filePreloadStateChanged failed, error code: ${code}, message: ${message}.\`);
  }
}

#### openFileBoost.addFile

addFile(file: string): void

Listener for the file preloading status, which is used to listen to the file preloading status after the app passes the file path. If the file status changes, the change is returned to the app through the **filePreloadStateChanged** event callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/gPC7ZBa5QaSEtYZ6vZwnTg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062517Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9132DDA25A5585092278B17A044ED6605DE4DAD77069E208E6E1CD655A0F1EF0)

1\. You need to call [openFileBoost.on('filePreloadStateChanged')](#section298512619713) before calling this API to add a listener for file preloading status.

2\. A maximum of 50 file listeners can be added for an app.

For details about the file types that support boost, see [File Types Supported by File Open Boost](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/preview-introduction#section7910758192912). For file types that are not supported, the file will not be preloaded by default. In this case, you do not need to call this API to listen to the file preloading status change.

**System capability**: SystemCapability.PCService.OpenFileBoost

**Start version**: 5.0.5(17)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string

 | 

Yes

 | 

Sandbox path of the file.

 |

**Error codes**:

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Module Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter check failed.

 |
| 

1017220001

 | 

Internal failure.

 |
| 

1017220002

 | 

Service unavailable.

 |
| 

1017220003

 | 

The number of added files exceeds the upper limit.

 |

**Example**:

import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const file:string = "/storage/Users/currentUser/Desktop/10MB\_file.docx";
function fileStateChangedCallback(filePreloadStatusInfo: openFileBoost.FilePreloadStatusInfo): void {
  hilog.info(0x0000, 'testTag', \`on filePreloadStateChanged, state: ${filePreloadStatusInfo.state}}\`);
}

function testAddFile(): void {
  try {
    openFileBoost.on('filePreloadStateChanged', fileStateChangedCallback);
    openFileBoost.addFile(file);
  } catch(error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    hilog.error(0x0000, 'testTag', \`addFile failed, error code: ${code}, message: ${message}.\`);
  }
}

#### openFileBoost.removeFile

removeFile(file: string): void

Cancels the listening on the preloading status of a file. The preloading status change will not be notified to the app through callback.

**System capability**: SystemCapability.PCService.OpenFileBoost

**Start version**: 5.0.5(17)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string

 | 

Yes

 | 

Sandbox path of the file.

 |

**Error codes**:

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Module Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter check failed.

 |
| 

1017220001

 | 

Internal failure.

 |
| 

1017220002

 | 

Service unavailable.

 |

**Example**:

import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const file:string = "/storage/Users/currentUser/Desktop/10MB\_file.docx";
try {
  openFileBoost.removeFile(file);
} catch(error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  hilog.error(0x0000, 'testTag', \`removeFile failed, error code: ${code}, message: ${message}.\`);
}

#### openFileBoost.queryFilePreloadStatusInfo

queryFilePreloadStatusInfo(file: string): FilePreloadStatusInfo

Queries the preloading status of a file. The file preloading status will be returned after the file path is passed.

**System capability**: SystemCapability.PCService.OpenFileBoost

**Start version**: 5.0.5(17)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

file

 | 

string

 | 

Yes

 | 

Sandbox path of the file.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[FilePreloadStatusInfo](#section2913441120)

 | 

File preloading status info.

 |

**Error codes**:

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [Module Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter check failed.

 |
| 

1017220001

 | 

Internal failure.

 |
| 

1017220002

 | 

Service unavailable.

 |

**Example**:

import { openFileBoost } from '@kit.PreviewKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const file:string = "/storage/Users/currentUser/Desktop/10MB\_file.docx";
try {
  let statusInfo : openFileBoost.FilePreloadStatusInfo = openFileBoost.queryFilePreloadStatusInfo(file);
  hilog.info(0x0000, 'testTag', 'file, %{public}s, progress:%{public}d  preloadState:%{public}d',
    statusInfo.sandboxPath, statusInfo.progress, statusInfo.state);
} catch(error) {
  let code = (error as BusinessError).code;
  let message = (error as BusinessError).message;
  hilog.error(0x0000, 'testTag', \`query failed, error code: ${code}, message: ${message}.\`);
}
