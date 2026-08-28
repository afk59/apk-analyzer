# assetDownloadManager (Resource Package Download Management)

This module provides the resource package download management capability.

**Start version**: 5.1.0(18)

#### Module Import

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

#### DownloadFault

Enumeration of resource package download failure causes.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

FAULT\_FILE\_ALREADY\_EXISTS

 | 

0

 | 

The resource package already exists.

 |
| 

FAULT\_FILE\_ERROR

 | 

1

 | 

File operation failed.

 |
| 

FAULT\_INSUFFICIENT\_SPACE

 | 

2

 | 

Insufficient memory space on the user device.

 |
| 

FAULT\_DISCONNECT

 | 

3

 | 

Network connection lost or disconnected during download.

 |
| 

FAULT\_TIMEOUT

 | 

4

 | 

Download timeout, for example, HTTP 408 request timeout or 504 gateway timeout.

 |
| 

FAULT\_PROTOCOL

 | 

5

 | 

HTTP protocol error, for example, HTTP 500 internal server error or HTTP 400 bad request.

 |
| 

FAULT\_DNS

 | 

6

 | 

DNS domain name resolution error. Unable to resolve the server address.

 |
| 

FAULT\_SSL

 | 

7

 | 

SSL/TLS certificate error.

 |
| 

FAULT\_REDIRECT

 | 

8

 | 

Redirect error, for example, too many redirects or invalid redirect URL.

 |
| 

FAULT\_UNKNOWN

 | 

9

 | 

Unknown error.

 |

#### State

Enumeration of resource package download task statuses.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

CREATED

 | 

0

 | 

A download task is created.

 |
| 

WAITING

 | 

1

 | 

A download task is waiting for execution.

 |
| 

DOWNLOADING

 | 

2

 | 

A download task is downloading resources.

 |
| 

PAUSED

 | 

3

 | 

A download task is paused.

 |
| 

FINISHED

 | 

4

 | 

A download task is finished.

 |
| 

FAILED

 | 

5

 | 

A download task failed.

 |

#### AssetDownloadConfig

Configuration information about a resource package download task.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

identifier

 | 

string

 | 

No

 | 

No

 | 

Task ID, which uniquely identifies a download task. It contains a maximum of 64 bytes.

 |
| 

url

 | 

string

 | 

No

 | 

No

 | 

URL of the current download task. The value must start with **http** or **https** and can contain a maximum of 512 bytes.

The domain name in the URL must comply with the domain name trustlist requirements.

-   For a third-party CDN: Go to AppGallery Connect to check the configured CDN domain name trustlist. For details, please refer to [Creating a Download Task](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/graphics-accelerate-assetdownload-release#en-us_topic_0000002179265860_en-us_topic_0000002177341213_section1494105011355).
-   For Huawei CDN: The domain name trustlist will be automatically configured based on the resource package download task.

 |
| 

isEssential

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether a resource to be downloaded is essential.

-   **false**: no (default value)
-   **true**: yes

The priority of downloading essential resources is higher than that of downloading non-essential resources.

 |
| 

groupId

 | 

string

 | 

No

 | 

Yes

 | 

Group ID, which is used to identify the resource version information. It contains a maximum of 32 bytes.

An empty character string is used by default.

 |
| 

fileName

 | 

string

 | 

No

 | 

Yes

 | 

File name of a resource to be downloaded. If this parameter is set, the temporary file downloaded by the system is named after the parameter value. If this parameter is not set, the downloaded file will be named after the task ID. It contains a maximum of 128 bytes.

An empty character string is used by default.

 |
| 

begins

 | 

number

 | 

No

 | 

Yes

 | 

Start byte position of an HTTP range request.

The default value is **0**.

 |
| 

ends

 | 

number

 | 

No

 | 

Yes

 | 

End byte position of an HTTP range request.

The default value is **0**.

 |
| 

userData

 | 

string

 | 

No

 | 

Yes

 | 

Extended field that can be customized. It contains a maximum of 1024 bytes.

An empty character string is used by default.

 |

#### AssetDownloadTask

Resource package download task information.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

config

 | 

[AssetDownloadConfig](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section14401125712)

 | 

Yes

 | 

No

 | 

Configuration information about a resource package download task, including the task ID, URL, and download priority.

 |
| 

taskId

 | 

string

 | 

Yes

 | 

No

 | 

Task ID, which is automatically generated by the system to uniquely identify a download task.

It contains a maximum of 36 bytes.

 |
| 

state

 | 

[State](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section15394544131416)

 | 

Yes

 | 

No

 | 

Status of a resource package download task.

 |

#### DownloadProgressInfo

Progress information about a resource package download task.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

downloadTask

 | 

[AssetDownloadTask](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)

 | 

Yes

 | 

No

 | 

Resource package download task information.

 |
| 

totalBytesWritten

 | 

number

 | 

Yes

 | 

No

 | 

Total size of resources to be downloaded, in bytes.

The default value is **0**.

 |
| 

totalExpectedBytes

 | 

number

 | 

Yes

 | 

No

 | 

Total size of downloaded resources, in bytes.

The default value is **0**.

 |

#### DownloadCompletedInfo

Completion information about a resource package download task.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

downloadTask

 | 

[AssetDownloadTask](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)

 | 

Yes

 | 

No

 | 

Resource package download task information.

 |
| 

filePath

 | 

string

 | 

Yes

 | 

No

 | 

Local sandbox address of the downloaded file.

It contains a maximum of 512 bytes.

 |

#### DownloadFailedInfo

Failure information about a resource package download task.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

downloadTask

 | 

[AssetDownloadTask](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)

 | 

Yes

 | 

No

 | 

Resource package download task information.

 |
| 

fault

 | 

[DownloadFault](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section82071855806)

 | 

Yes

 | 

No

 | 

Resource package download failure cause.

 |

#### assetDownloadManager.on('progress')

on(type: 'progress', callback: Callback<DownloadProgressInfo\[\]>): void

Subscribes to download progress events. This API returns the result through a callback.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event type. The value **progress** indicates a download progress event.

 |
| 

callback

 | 

Callback<[DownloadProgressInfo\[\]](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1791922193210)\>

 | 

Yes

 | 

Callback function, which returns the task progress information.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onProgressCallback = (progressArray: assetDownloadManager.DownloadProgressInfo\[\]) => {
  console.info('AssetAccelDemo', \`onProgressCallback progressArray length: ${progressArray.length}\`);
  // Add the handling logic based on the obtained download progress.
};
// Subscribe to download progress events.
assetDownloadManager.on("progress", onProgressCallback);

#### assetDownloadManager.off('progress')

off(type: 'progress', callback?: Callback<DownloadProgressInfo\[\]>): void

Unsubscribes from download progress events. This API returns the result through a callback.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event type. The value **progress** indicates a download progress event.

 |
| 

callback

 | 

Callback<[DownloadProgressInfo\[\]](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1791922193210)\>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks currently listening to this event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onProgressCallback = (progressArray: assetDownloadManager.DownloadProgressInfo\[\]) => {
  console.info('AssetAccelDemo', \`onProgressCallback progressArray length: ${progressArray.length}\`);
  // Add the handling logic based on the obtained download progress.
};
// Unsubscribe from download progress events.
assetDownloadManager.off("progress", onProgressCallback);

#### assetDownloadManager.on('pause')

on(type: 'pause', callback: Callback<AssetDownloadTask>): void

Subscribes to download pause events. This API returns the result through a callback.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event type. The value **pause** indicates a download pause event.

 |
| 

callback

 | 

Callback<[AssetDownloadTask](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)\>

 | 

Yes

 | 

Callback function, which returns the task information.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onPauseCallback = (downloadTaskInfo: assetDownloadManager.AssetDownloadTask) => {
  console.info('AssetAccelDemo', \`task identifier = ${downloadTaskInfo.config.identifier} has paused.\`);
  // Add the logic for handling download pausing.
};
// Subscribe to download pause events.
assetDownloadManager.on("pause", onPauseCallback);

#### assetDownloadManager.off('pause')

off(type: 'pause', callback?: Callback<AssetDownloadTask>): void

Unsubscribes from download pause events. This API returns the result through a callback.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event type. The value **pause** indicates a download pause event.

 |
| 

callback

 | 

Callback<[AssetDownloadTask](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)\>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks currently listening to this event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onPauseCallback = (downloadTaskInfo: assetDownloadManager.AssetDownloadTask) => {
  console.info('AssetAccelDemo', \`task identifier = ${downloadTaskInfo.config.identifier} has paused.\`);
  // Add the logic for handling download pausing.
};
// Unsubscribe from download pause events.
assetDownloadManager.off("pause", onPauseCallback);

#### assetDownloadManager.on('complete')

on(type: 'complete', callback: Callback<DownloadCompletedInfo>): void

Subscribes to download success events. This API returns the result through a callback.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event type. The value **complete** indicates a download success event.

 |
| 

callback

 | 

Callback<[DownloadCompletedInfo](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section13627145473413)\>

 | 

Yes

 | 

Callback function, which returns the task completion information.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onCompleteCallback = (completeInfo: assetDownloadManager.DownloadCompletedInfo) => {
  console.info('AssetAccelDemo', \`task identifier = ${completeInfo.downloadTask.config.identifier} has completed.\`);
  // Add the logic for handling download success.
};
// Subscribe to download success events.
assetDownloadManager.on("complete", onCompleteCallback);

#### assetDownloadManager.off('complete')

off(type: 'complete', callback?: Callback<DownloadCompletedInfo>): void

Unsubscribes from download success events. This API returns the result through a callback.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event type. The value **complete** indicates a download success event.

 |
| 

callback

 | 

Callback<[DownloadCompletedInfo](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section13627145473413)\>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks currently listening to this event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onCompleteCallback = (completeInfo: assetDownloadManager.DownloadCompletedInfo) => {
  console.info('AssetAccelDemo', \`task identifier = ${completeInfo.downloadTask.config.identifier} has completed.\`);
  // Add the logic for handling download success.
};
// Unsubscribe from download success events.
assetDownloadManager.off("complete", onCompleteCallback);

#### assetDownloadManager.on('fail')

on(type: 'fail', callback: Callback<DownloadFailedInfo>): void

Subscribes to download failure events. This API returns the result through a callback.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event type. The value **fail** indicates a download failure event.

 |
| 

callback

 | 

Callback<[DownloadFailedInfo](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section154451056193512)\>

 | 

Yes

 | 

Callback function, which returns the task failure information.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onFailedCallback = (failedInfo: assetDownloadManager.DownloadFailedInfo) => {
  console.info('AssetAccelDemo', \`task identifier = ${failedInfo.downloadTask.config.identifier} has failed.\`);
  // Add the logic for handling download failure.
};
// Subscribe to download failure events.
assetDownloadManager.on("fail", onFailedCallback);

#### assetDownloadManager.off('fail')

off(type: 'fail', callback?: Callback<DownloadFailedInfo>): void

Unsubscribes from download failure events. This API returns the result through a callback.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

type

 | 

string

 | 

Yes

 | 

Event type. The value **fail** indicates a download failure event.

 |
| 

callback

 | 

Callback<[DownloadFailedInfo](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section154451056193512)\>

 | 

No

 | 

Callback to be canceled, which must be the same as that passed upon subscription. If this parameter is not specified, all callbacks currently listening to this event will be canceled.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

let onFailedCallback = (failedInfo: assetDownloadManager.DownloadFailedInfo) => {
  console.info('AssetAccelDemo', \`task identifier = ${failedInfo.downloadTask.config.identifier} has failed.\`);
  // Add the logic for handling download failure.
};
// Unsubscribe from download failure events.
assetDownloadManager.off("fail", onFailedCallback);

#### assetDownloadManager.fetchManifestUrl

fetchManifestUrl(): Promise<string>

Obtains the list of resource packages to be downloaded. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Promise object. If the resources are hosted on a Huawei CDN, the resource package download list **manifestUrl** is returned. If the resources are hosted on a third-party CDN, an empty string is returned.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

async fetchManifestUrl() {
  let manifestUrl : string = '';
  try {
    manifestUrl = await assetDownloadManager.fetchManifestUrl();
    console.info('AssetAccelDemo', \`Succeeded in fetching manifestUrl, manifestUrl = ${manifestUrl}\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to fetch manifestUrl, errCode: ${error.code}, errMessage: ${error.message}\`);
    return;
  }
}

#### assetDownloadManager.addAssetDownloadTask

addAssetDownloadTask(context: common.BaseContext, downloadConfig: AssetDownloadConfig): Promise<string>

Adds a resource package download task. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

Application context.

 |
| 

downloadConfig

 | 

[AssetDownloadConfig](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section14401125712)

 | 

Yes

 | 

Configuration information about a resource package download task.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

Promise object. The download task ID is returned.

It contains a maximum of 36 bytes.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600001

 | 

The domain name of the download task is not in the domain name trustlist.

 |
| 

1016600004

 | 

The application task queue is full.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async addAssetDownloadTask() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    const taskId: string = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
  }
}

#### assetDownloadManager.pauseAssetDownloadTask

pauseAssetDownloadTask(taskId: string): Promise<void>

Pauses a resource package download task. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

taskId

 | 

string

 | 

Yes

 | 

Task ID. It contains a maximum of 36 bytes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600002

 | 

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

 |
| 

1016600003

 | 

The current task status does not support the current operator.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async pauseAssetDownloadTask() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Pause the resource package download task based on **taskId**.
    await assetDownloadManager.pauseAssetDownloadTask(taskId);
    console.info('AssetAccelDemo', \`Succeeded in pausing assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to pause assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.resumeAssetDownloadTask

resumeAssetDownloadTask(taskId: string): Promise<void>

Resumes a resource package download task. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

taskId

 | 

string

 | 

Yes

 | 

Task ID. It contains a maximum of 36 bytes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600002

 | 

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

 |
| 

1016600003

 | 

The current task status does not support the current operator.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async resumeAssetDownloadTask() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Pause the resource package download task based on **taskId**.
    assetDownloadManager.pauseAssetDownloadTask(taskId);
    console.info('AssetAccelDemo', \`Succeeded in pausing assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to pause assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Resume the resource package download task based on **taskId**.
    await assetDownloadManager.resumeAssetDownloadTask(taskId);
    console.info('AssetAccelDemo', \`Succeeded in resuming assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to resume assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.removeAssetDownloadTask

removeAssetDownloadTask(taskId: string): Promise<void>

Removes a resource package download task. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

taskId

 | 

string

 | 

Yes

 | 

Task ID. It contains a maximum of 36 bytes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600002

 | 

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async removeAssetDownloadTask() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Remove the resource package download task based on **taskId**.
    await assetDownloadManager.removeAssetDownloadTask(taskId);
    console.info('AssetAccelDemo', \`Succeeded in removing assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to remove assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.fetchAllAssetDownloadTasks

fetchAllAssetDownloadTasks(): Promise<AssetDownloadTask\[\]>

Obtains all resource package download tasks, excluding those that have been finished. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AssetDownloadTask\[\]](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)\>

 | 

Promise object. The resource package download task list is returned.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async fetchAllAssetDownloadTasks() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  let downloadTaskArr: Array<assetDownloadManager.AssetDownloadTask>;
  try {
    // Obtain all resource package download tasks.
    downloadTaskArr = await assetDownloadManager.fetchAllAssetDownloadTasks();
    console.info('AssetAccelDemo', \`Succeeded in fetching allAssetDownloadTasks success, downloadTaskArr length:${downloadTaskArr.length}.\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to fetch allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.pauseAllAssetDownloadTasks

pauseAllAssetDownloadTasks(): Promise<void>

Pauses all resource package download tasks. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async pauseAllAssetDownloadTasks() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Pause all resource package download tasks.
    await assetDownloadManager.pauseAllAssetDownloadTasks();
    console.info('AssetAccelDemo', \`Succeeded in pausing allAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to pause allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.resumeAllAssetDownloadTasks

resumeAllAssetDownloadTasks(): Promise<void>

Resumes all resource package download tasks. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async resumeAllAssetDownloadTasks() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Pause all resource package download tasks.
    await assetDownloadManager.pauseAllAssetDownloadTasks();
    console.info('AssetAccelDemo', \`Succeeded in pausing allAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to pause allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Resume all resource package download tasks.
    await assetDownloadManager.resumeAllAssetDownloadTasks();
    console.info('AssetAccelDemo', \`Succeeded in resuming allAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to resume allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.removeAllAssetDownloadTasks

removeAllAssetDownloadTasks(): Promise<void>

Removes all resource package download tasks. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async removeAllAssetDownloadTasks() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Remove all resource package download tasks.
    await assetDownloadManager.removeAllAssetDownloadTasks();
    console.info('AssetAccelDemo', \`Succeeded in removing allAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to remove allAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.fetchGroupAssetDownloadTasks

fetchGroupAssetDownloadTasks(groupId: string): Promise<AssetDownloadTask\[\]>

Obtains resource package download tasks in the same group. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

groupId

 | 

string

 | 

Yes

 | 

Group ID, which is used to identify the resource version information. It contains a maximum of 32 bytes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[AssetDownloadTask\[\]](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)\>

 | 

Promise object. The resource package download task list is returned.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600002

 | 

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async fetchGroupAssetDownloadTasks() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  let groupId = 'groupId';
  let downloadTaskArr: Array<assetDownloadManager.AssetDownloadTask>;
  try {
    // Obtain resource package download tasks with the same group ID.
    downloadTaskArr = await assetDownloadManager.fetchGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', \`Succeeded in fetching groupAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to fetch groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.pauseGroupAssetDownloadTasks

pauseGroupAssetDownloadTasks(groupId: string): Promise<void>

Pauses resource package download tasks in the same group. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

groupId

 | 

string

 | 

Yes

 | 

Group ID, which is used to identify the resource version information. It contains a maximum of 32 bytes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600002

 | 

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async pauseGroupAssetDownloadTasks() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  let groupId = 'groupId';
  try {
    // Pause resource package download tasks with the same group ID.
    await assetDownloadManager.pauseGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', \`Succeeded in pausing groupAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to pause groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.resumeGroupAssetDownloadTasks

resumeGroupAssetDownloadTasks(groupId: string): Promise<void>

Resumes resource package download tasks in the same group. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

groupId

 | 

string

 | 

Yes

 | 

Group ID, which is used to identify the resource version information. It contains a maximum of 32 bytes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1016600000

 | 

The API call from an ExtensionAbility is not allowed.

 |
| 

1016600002

 | 

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async resumeGroupAssetDownloadTasks() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  let groupId = 'groupId';
  try {
    // Pause resource package download tasks with the same group ID.
    await assetDownloadManager.pauseGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', \`Succeeded in pausing groupAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to pause groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    // Resume resource package download tasks with the same group ID.
    await assetDownloadManager.resumeGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', \`Succeeded in resuming groupAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to resume groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### assetDownloadManager.removeGroupAssetDownloadTasks

removeGroupAssetDownloadTasks(groupId: string): Promise<void>

Removes resource package download tasks in the same group. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

groupId

 | 

string

 | 

Yes

 | 

Group ID, which is used to identify the resource version information. It contains a maximum of 32 bytes.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1016600002

 | 

The task ID or group ID entered during operations such as pause, resume, and fetch does not exist.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async removeGroupAssetDownloadTasks() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  let groupId = 'groupId';
  try {
    // Remove resource package download tasks with the same group ID.
    await assetDownloadManager.removeGroupAssetDownloadTasks(groupId);
    console.info('AssetAccelDemo', \`Succeeded in removing groupAssetDownloadTasks\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to remove groupAssetDownloadTasks, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### NetSpeedLevel

Enumeration of network speed limit levels.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NO\_LIMIT

 | 

0

 | 

No speed limit.

 |
| 

LIMIT\_MEDIUM

 | 

1

 | 

Speed limit at the medium level.

 |
| 

LIMIT\_LOW

 | 

2

 | 

Speed limit at the low level.

 |

#### assetDownloadManager.limitDownloadTaskSpeed

limitDownloadTaskSpeed(taskIds: string\[\], speedLimit: NetSpeedLevel): Promise<void>

Limits the download speed of resource package download tasks. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

taskIds

 | 

string\[\]

 | 

Yes

 | 

Task ID list.

 |
| 

speedLimit

 | 

[NetSpeedLevel](#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section194602582014)

 | 

Yes

 | 

Network speed limit level.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise object without a return value.

 |

**Error codes**:

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

No Internet permission.

 |
| 

401

 | 

Parameter error.

 |
| 

1016600094

 | 

Task service ability error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';
import { common } from '@kit.AbilityKit';

async limitDownloadTaskSpeed() {
  // Construct the download task configuration information.
  let assetDownload: assetDownloadManager.AssetDownloadConfig = {
    fileName: 'fileName', // File name of a resource to be downloaded.
    url: 'url', // URL of a resource to be downloaded.
    isEssential: false, // Indicates whether a resource to be downloaded is essential.
    identifier: 'identifier', // Identifier of a resource to be downloaded.
    groupId: 'groupId' // Group ID, which is used to identify the resource version information.
  }
  let taskId: string = '';
  try {
    // Add a resource package download task.
    // Pass a proper context based on the code context.
    taskId = await assetDownloadManager.addAssetDownloadTask(this.getUIContext().getHostContext() as common.Context, assetDownload);
    console.info('AssetAccelDemo', \`Succeeded in adding assetDownloadTask\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to add assetDownloadTask, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
  try {
    const taskIds: string\[\] = \[taskId\];
    // Limit the download speed of resource package download tasks.
    assetDownloadManager.limitDownloadTaskSpeed(taskIds, assetDownloadManager.NetSpeedLevel.LIMIT\_MEDIUM);
    console.info('AssetAccelDemo', \`Succeeded in limiting downloadTaskSpeed\`);
  } catch (error) {
    console.error('AssetAccelDemo', \`Failed to limit downloadTaskSpeed, errCode:${error.code}, errMessage:${error.message}\`);
    return;
  }
}

#### AppDownloadStatus

Enumeration of resource package download statuses in the app's downloader.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.1(19)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

IN\_PROGRESS

 | 

0

 | 

Downloading.

 |
| 

FINISH

 | 

1

 | 

Download completed.

 |

#### AppDownloadProgress

Resource package download progress information in the app's downloader.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.1(19)

| 
**Name**

 | 

**Type**

 | 

**Read-Only**

 | 

Optional

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

totalBytesWritten

 | 

number

 | 

No

 | 

No

 | 

Total size of downloaded resources, in bytes. The value must be greater than or equal to 0.

The default value is **0**.

 |
| 

totalExpectedBytes

 | 

number

 | 

No

 | 

No

 | 

Total size of resources to be downloaded, in bytes. The value must be greater than or equal to 0. If an invalid value is passed, the value **0** will be used.

The default value is **0**.

 |
| 

totalFiles

 | 

number

 | 

No

 | 

No

 | 

Total number of resource files. The value must be greater than or equal to 0. If an invalid value is passed, the value **0** will be used.

The default value is **0**.

 |
| 

successCount

 | 

number

 | 

No

 | 

No

 | 

Number of files that have been successfully downloaded. The value must be greater than or equal to 0. If an invalid value is passed, the value **0** will be used.

The default value is **0**.

 |
| 

failureCount

 | 

number

 | 

No

 | 

No

 | 

Number of files whose download fails. The value must be greater than or equal to 0. If an invalid value is passed, the value **0** will be used.

The default value is **0**.

 |
| 

status

 | 

[AppDownloadStatus](#section2335333617)

 | 

No

 | 

No

 | 

Download status in the app's downloader.

 |

#### assetDownloadManager.reportDownloadProgress

reportDownloadProgress(progressInfo: AppDownloadProgress): void

Reports the resource package download progress information synchronized from the app's downloader.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.1(19)

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

progressInfo

 | 

[AppDownloadProgress](#section83637335412)

 | 

Yes

 | 

Download progress information in the app's downloader.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1016600094

 | 

Task service ability error.

 |
| 

1016600401

 | 

Parameter error.

 |

**Example**:

import { assetDownloadManager } from '@kit.GraphicsAccelerateKit';

try {
  let progressInfo: assetDownloadManager.AppDownloadProgress = {
    totalBytesWritten: 0,
    totalExpectedBytes: 0,
    totalFiles: 0,
    successCount: 0,
    failureCount: 0,
    status:assetDownloadManager.AppDownloadStatus.IN\_PROGRESS
  }
  assetDownloadManager.reportDownloadProgress(progressInfo);
  console.info('AssetAccelDemo', \`Succeeded in reporting downloadProgress\`);
} catch (error) {
  console.error('AssetAccelDemo', \`Failed to report downloadProgress, errCode:${error.code}, errMessage:${error.message}\`);
}
