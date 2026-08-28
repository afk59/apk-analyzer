# cloudStorage (Cloud Storage Module)

This module provides the capabilities of uploading, downloading, querying, and deleting files through the Cloud Storage service.

**Start version**: 5.0.0(12)

#### Modules to Import

import { cloudStorage } from '@kit.CloudFoundationKit';

#### bucket

bucket(name?: string): StorageBucket

Initializes a Cloud Storage instance.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

name

 | 

string

 | 

No

 | 

Name of a storage instance. The format is restricted by the cloud. Only lowercase letters, digits, and hyphens (-) are allowed. The value must start and end with a letter or digit and contain 9 to 63 characters. Two or more consecutive hyphens (-) are not allowed.

If this parameter is not specified, an asynchronous task will be initiated to query the default instance on the cloud side.

If this parameter is specified, ensure that the storage instance exists on the cloud; otherwise, subsequent operations will result in an error during storage instance query.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[StorageBucket](#section10732104881420)

 | 

Cloud Storage instance.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

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

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';

let bucket1: cloudStorage.StorageBucket = cloudStorage.bucket(); // When **name** is not specified, an asynchronous task will be initiated to query the default instance on the cloud.

/\*\*
 \* Set the Cloud Storage instance name to **mybucket-duaf5**.
 \* **mybucket** is the storage instance name set during Cloud Storage instance creation, and **duaf5** is a random character string generated during Cloud Storage instance creation. They are connected by a hyphen (-).
 \*/
let bucket2: cloudStorage.StorageBucket = cloudStorage.bucket('mybucket-duaf5'); 

#### StorageBucket

Cloud Storage instance, which provides the capabilities of uploading and downloading files through the Cloud Storage service. The instance is initialized through [bucket](#section1286815320203).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

#### \[h2\]uploadFile

uploadFile(context: common.BaseContext, parameters: UploadParams): Promise<request.agent.Task>

Uploads a specified file to the cloud. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

parameters

 | 

[UploadParams](#section2941124514298)

 | 

Yes

 | 

Upload-related parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[request.agent.Task](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagenttask10)\>

 | 

Upload task returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// ArkUI context.
bucket.uploadFile(context, {  // **context** indicates the app context.
  localPath: cacheFile,       // Local file path, located in the **context.cacheDir** directory.
  cloudPath: path             // Cloud file path. The value can be in format of _File directory/File name_ or _File name_.
}).then((task: request.agent.Task) => {
  task.on('progress', (progress) => {
    hilog.info(0x0000, 'testTag', \`on progress ${JSON.stringify(progress)}\`);
  });
  task.on('completed', (progress) => {
    hilog.info(0x0000, 'testTag', \`on completed ${JSON.stringify(progress)}\`);
  });
  task.on('failed', (progress) => {
    hilog.error(0x0000, 'testTag', \`on failed ${JSON.stringify(progress)}\`);
  });
  task.on('response', (response) => {
    hilog.info(0x0000, 'testTag', \`on response ${JSON.stringify(response)}\`);
  });

  // Start the task.
  task.start((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', \`Failed to start a file upload task, code: ${err.code}, message: ${err.message}\`);
    } else {
      hilog.info(0x0000, 'testTag', \`Succeeded in starting a file upload task.\`);
    }
  });
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to upload file, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]uploadFile

uploadFile(context: common.BaseContext, parameters: UploadParams, callback: AsyncCallback<request.agent.Task>): void

Uploads a specified file to the cloud. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

parameters

 | 

[UploadParams](#section2941124514298)

 | 

Yes

 | 

Upload-related parameters.

 |
| 

callback

 | 

AsyncCallback<[request.agent.Task](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagenttask10)\>

 | 

Yes

 | 

Callback function. If the file is uploaded successfully, **err** is **undefined** and **data** is the **request.agent.Task** obtained; otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// ArkUI context.
bucket.uploadFile(context, {  // **context** indicates the app context.
  localPath: cacheFile,       // Local file path, located in the **context.cacheDir** directory.
  cloudPath: path             // Cloud file path. The value can be in format of _File directory/File name_ or _File name_.
}, (err: BusinessError, task: request.agent.Task) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to upload file, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  task.on('progress', (progress) => {
    hilog.info(0x0000, 'testTag', \`on progress ${JSON.stringify(progress)}\`);
  });
  task.on('completed', (progress) => {
    hilog.info(0x0000, 'testTag', \`on completed ${JSON.stringify(progress)}\`);
  });
  task.on('failed', (progress) => {
    hilog.error(0x0000, 'testTag', \`on failed ${JSON.stringify(progress)}\`);
  });
  task.on('response', (response) => {
    hilog.info(0x0000, 'testTag', \`on response ${JSON.stringify(response)}\`);
  });

  // Start the task.
  task.start((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', \`Failed to start a file upload task, code: ${err.code}, message: ${err.message}\`);
    } else {
      hilog.info(0x0000, 'testTag', \`Succeeded in starting a file upload task.\`);
    }
  });
});

#### \[h2\]downloadFile

downloadFile(context: common.BaseContext, parameters: DownloadParams): Promise<request.agent.Task>

Downloads a file from the cloud to a local path. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

parameters

 | 

[DownloadParams](#section14137913019)

 | 

Yes

 | 

Download-related parameters.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[request.agent.Task](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagenttask10)\>

 | 

Download task returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// ArkUI context.
bucket.downloadFile(context, {  // **context** indicates the app context.
  cloudPath: path,              // Cloud file path. The value can be in format of _File directory/File name_ or _File name_.
  localPath: cacheFile,         // Local file path, located in the **context.cacheDir** directory.
}).then((task: request.agent.Task) => {
  task.on('progress', (progress) => {
    hilog.info(0x0000, 'testTag', \`on progress ${JSON.stringify(progress)}\`);
  });
  task.on('completed', (progress) => {
    hilog.info(0x0000, 'testTag', \`on completed ${JSON.stringify(progress)}\`);
  });
  task.on('failed', (progress) => {
    hilog.error(0x0000, 'testTag', \`on failed ${JSON.stringify(progress)}\`);
  });
  task.on('response', (response) => {
    hilog.info(0x0000, 'testTag', \`on response ${JSON.stringify(response)}\`);
  });

  // Start the task.
  task.start((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag',
        \`Failed to start a file download task, code: ${err.code}, message: ${err.message}\`);
    } else {
      hilog.info(0x0000, 'testTag', \`Succeeded in starting a file download task.\`);
    }
  });
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to download file, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]downloadFile

downloadFile(context: common.BaseContext, parameters: DownloadParams, callback: AsyncCallback<request.agent.Task>): void

Downloads a file from the cloud to a local path. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

context

 | 

common.[BaseContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

App context.

 |
| 

parameters

 | 

[DownloadParams](#section14137913019)

 | 

Yes

 | 

Download-related parameters.

 |
| 

callback

 | 

AsyncCallback<[request.agent.Task](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagenttask10)\>

 | 

Yes

 | 

Callback function. If the file is downloaded successfully, **err** is **undefined** and **data** is the **request.agent.Task** obtained; otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError, request } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// ArkUI context.
bucket.downloadFile(context, {  // **context** indicates the app context.
  cloudPath: path,              // Cloud file path. The value can be in format of _File directory/File name_ or _File name_.
  localPath: cacheFile,         // Local file path, located in the **context.cacheDir** directory.
}, (err: BusinessError, task: request.agent.Task) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to download file, code: ${err.code}, message: ${err.message}\`);
    return;
  }
  task.on('progress', (progress) => {
    hilog.info(0x0000, 'testTag', \`on progress ${JSON.stringify(progress)}\`);
  });
  task.on('completed', (progress) => {
    hilog.info(0x0000, 'testTag', \`on completed ${JSON.stringify(progress)}\`);
  });
  task.on('failed', (progress) => {
    hilog.error(0x0000, 'testTag', \`on failed ${JSON.stringify(progress)}\`);
  });
  task.on('response', (response) => {
    hilog.info(0x0000, 'testTag', \`on response ${JSON.stringify(response)}\`);
  });

  // Start the task.
  task.start((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag',
        \`Failed to start a file download task, code: ${err.code}, message: ${err.message}\`);
    } else {
      hilog.info(0x0000, 'testTag', \`Succeeded in starting a file download task.\`);
    }
  });
});

#### \[h2\]getDownloadURL

getDownloadURL(cloudPath: string): Promise<string>

Obtains the download URL of a cloud file. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

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

Cloud file download URL returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// **cloudPath** indicates the cloud file path. The value can be in format of _File directory/File name_ or _File name_.
bucket.getDownloadURL('cloudPath').then((downloadURL: string) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in getting download URL: ${downloadURL}\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to get download URL, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]getDownloadURL

getDownloadURL(cloudPath: string, callback: AsyncCallback<string>): void

Obtains the download URL of a cloud file. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

 |
| 

callback

 | 

AsyncCallback<string>

 | 

Yes

 | 

Cloud file download URL returned through a callback function.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// **cloudPath** indicates the cloud file path.
bucket.getDownloadURL('cloudPath', (err: BusinessError, downloadURL: string) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to get download URL, code: ${err.code}, message: ${err.message}\`);
  } else {
    hilog.info(0x0000, 'testTag', \`Succeeded in getting download URL: ${downloadURL}\`);
  }
});

#### \[h2\]deleteFile

deleteFile(cloudPath: string): Promise<void>

Deletes a cloud file. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

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

Promise that returns no value.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// **cloudPath** indicates the cloud file path. The value can be in format of _File directory/File name_ or _File name_.
bucket.deleteFile('cloudPath').then(() => {
  hilog.info(0x0000, 'testTag', \`Succeeded in deleting file.\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to delete file, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]deleteFile

deleteFile(cloudPath: string, callback: AsyncCallback<void>): void

Deletes a cloud file. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

 |
| 

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the cloud file is deleted successfully, **err** is **undefined**; otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// **cloudPath** indicates the cloud file path. The value can be in format of _File directory/File name_ or _File name_.
bucket.deleteFile('cloudPath', (err: BusinessError) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to delete file, Code: ${err.code}, message: ${err.message}\`);
  } else {
    hilog.info(0x0000, 'testTag', \`Succeeded in deleting file.\`);
  }
});

#### \[h2\]list

list(cloudPath: string, options?: ListOptions): Promise<ListResults>

Obtains the cloud file list. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path.

If an empty character string (**''**) is passed, the list of files in the root path on the cloud will be obtained. If **some\_directory/** is passed, the list of files in the specified folder **some\_directory** will be obtained.

 |
| 

options

 | 

[ListOptions](#section7984102813013)

 | 

No

 | 

Parameters for obtaining the file list.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ListResults](#section181654510303)\>

 | 

File list returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// Obtain the list of files in the root path on the cloud.
bucket.list('').then((result: cloudStorage.ListResults) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in listing files, result: ${JSON.stringify(result)}\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to list files, code: ${err.code}, message: ${err.message}\`);
})

// Obtain the list of files in the specified folder **some\_directory**.
bucket.list('some\_directory/').then((result: cloudStorage.ListResults) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in listing files, result: ${JSON.stringify(result)}\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to list files, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]list

list(cloudPath: string, options: ListOptions, callback: AsyncCallback<ListResults>): void

Obtains the cloud file list. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path.

If an empty character string (**''**) is passed, the list of files in the root path on the cloud will be obtained. If **some\_directory/** is passed, the list of files in the specified folder **some\_directory** will be obtained.

 |
| 

options

 | 

[ListOptions](#section7984102813013)

 | 

Yes

 | 

Parameters for obtaining the file list.

 |
| 

callback

 | 

AsyncCallback<[ListResults](#section181654510303)\>

 | 

Yes

 | 

Callback function. If the cloud file list is obtained successfully, **err** is **undefined** and **data** is the **ListResults** obtained; otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// Obtain the list of files in the root path on the cloud.
bucket.list('', { maxResults: 10, pageMarker: 'test' }, (err: BusinessError, result: cloudStorage.ListResults) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to list files, code: ${err.code}, message: ${err.message}\`);
  } else {
    hilog.info(0x0000, 'testTag', \`Succeeded in listing files, result: ${JSON.stringify(result)}\`);
  }
});

// Obtain the list of files in the specified folder **some\_directory**.
bucket.list('some\_directory/', {}, (err: BusinessError, result: cloudStorage.ListResults) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to list files, code: ${err.code}, message: ${err.message}\`);
  } else {
    hilog.info(0x0000, 'testTag', \`Succeeded in listing files, result: ${JSON.stringify(result)}\`);
  }
});

#### \[h2\]getMetadata

getMetadata(cloudPath: string): Promise<Metadata>

Obtains metadata of a cloud file. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Metadata](#section3472335144212)\>

 | 

Metadata of the cloud file, returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// **cloudPath** indicates the cloud file path. The value can be in format of _File directory/File name_ or _File name_.
bucket.getMetadata('cloudPath').then((data: cloudStorage.Metadata) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in getting metadata: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to get metadata, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]getMetadata

getMetadata(cloudPath: string, callback: AsyncCallback<Metadata>): void

Obtains metadata of a cloud file. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

 |
| 

callback

 | 

AsyncCallback<[Metadata](#section3472335144212)\>

 | 

Yes

 | 

Callback function. If the cloud file metadata is obtained successfully, **err** is **undefined** and **data** is the **Metadata** obtained; otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// **cloudPath** indicates the cloud file path. The value can be in format of _File directory/File name_ or _File name_.
bucket.getMetadata('cloudPath', (err: BusinessError, data: cloudStorage.Metadata) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to get metadata, code: ${err.code}, message: ${err.message}\`);
  } else {
    hilog.info(0x0000, 'testTag', \`Succeeded in getting metadata: ${JSON.stringify(data)}\`);
  }
});

#### \[h2\]setMetadata

setMetadata(cloudPath: string, metadata: MetadataUpdatable): Promise<Metadata>

Sets metadata of a cloud file. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

 |
| 

metadata

 | 

[MetadataUpdatable](#section1122119164218)

 | 

Yes

 | 

Metadata to be updated.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Metadata](#section3472335144212)\>

 | 

Complete metadata of the cloud file after the metadata is updated, returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// **cloudPath** indicates the cloud file path. The value can be in format of _File directory/File name_ or _File name_.
bucket.setMetadata('cloudPath', {
  customMetadata: {
    key1: "value1",
    key2: "value2"
  }
}).then((data: cloudStorage.Metadata) => {
  hilog.info(0x0000, 'testTag', \`Succeeded in setting metadata: ${JSON.stringify(data)}\`);
}).catch((err: BusinessError) => {
  hilog.error(0x0000, 'testTag', \`Failed to set metadata, code: ${err.code}, message: ${err.message}\`);
})

#### \[h2\]setMetadata

setMetadata(cloudPath: string, metadata: MetadataUpdatable, callback: AsyncCallback<Metadata>): void

Sets metadata of a cloud file. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Required permission**: ohos.permission.INTERNET

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

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

cloudPath

 | 

string

 | 

Yes

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

 |
| 

metadata

 | 

[MetadataUpdatable](#section1122119164218)

 | 

Yes

 | 

Metadata to be updated.

 |
| 

callback

 | 

AsyncCallback<[Metadata](#section3472335144212)\>

 | 

Yes

 | 

Callback function. If the cloud file metadata is set successfully, **err** is **undefined** and **data** is the **Metadata** set; otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS Error Codes](../arkts-error-codes/document.md).

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

1008220001

 | 

Network connection error.

 |
| 

1008220009

 | 

Client internal error.

 |
| 

1008221001

 | 

Server error.

 |

**Example**:

import { cloudStorage } from '@kit.CloudFoundationKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let bucket: cloudStorage.StorageBucket = cloudStorage.bucket();

// **cloudPath** indicates the cloud file path. The value can be in format of _File directory/File name_ or _File name_.
bucket.setMetadata('cloudPath', {
  customMetadata: {
    key1: "value1",
    key2: "value2"
  }
}, (err: BusinessError, data: cloudStorage.Metadata) => {
  if (err) {
    hilog.error(0x0000, 'testTag', \`Failed to set metadata, code: ${err.code}, message: ${err.message}\`);
  } else {
    hilog.info(0x0000, 'testTag', \`Succeeded in setting metadata: ${JSON.stringify(data)}\`);
  }
});

#### UploadParams

Upload-related parameters.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

localPath

 | 

string

 | 

No

 | 

No

 | 

Local file path. The root path is the **cache** directory.

 |
| 

cloudPath

 | 

string

 | 

No

 | 

No

 | 

Cloud file path. After a file is uploaded successfully, you can use this path to perform other operations.

 |
| 

metadata

 | 

[MetadataUpdatable](#section1122119164218)

 | 

No

 | 

Yes

 | 

File metadata.

 |
| 

mode

 | 

[request.agent.Mode](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagentmode10)

 | 

No

 | 

Yes

 | 

Type of the upload task. After an app is switched to the background for a period of time, background tasks are not affected but foreground tasks will fail or pause. The default value is **request.agent.Mode.BACKGROUND**.

-   **request.agent.Mode.BACKGROUND**: background tasks
-   **request.agent.Mode.FOREGROUND**: foreground task

 |
| 

network

 | 

[request.agent.Network](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagentnetwork10)

 | 

No

 | 

Yes

 | 

Network required by the upload task. If the network does not meet the preset condition, tasks that have not been executed will await for execution, and tasks that are being executed will fail or pause. The default value is **request.agent.Network.ANY**.

-   **request.agent.Network.ANY**: network of any type
-   **request.agent.Network.WIFI**: wireless network
-   **request.agent.Network.CELLULAR**: cellular data network

 |

#### DownloadParams

Download-related parameters.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

localPath

 | 

string

 | 

No

 | 

No

 | 

Local file path. The root path is the **cache** directory.

 |
| 

cloudPath

 | 

string

 | 

No

 | 

No

 | 

Cloud file path. The value can be in format of _File directory/File name_ (for example, **image/demo.jpg**) or _File name_.

 |
| 

mode

 | 

[request.agent.Mode](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagentmode10)

 | 

No

 | 

Yes

 | 

Type of the download task. After an app is switched to the background for a period of time, background tasks are not affected but foreground tasks will fail or pause. The default value is **request.agent.Mode.BACKGROUND**.

-   **request.agent.Mode.BACKGROUND**: background tasks
-   **request.agent.Mode.FOREGROUND**: foreground task

 |
| 

overwrite

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to overwrite the local file when the file to be downloaded already exists. The default value is **false**.

-   **true**: Overwrite the local file.
-   **false**: Do not overwrite the existing file. If a file with the same name exists, the download will fail.

 |
| 

network

 | 

[request.agent.Network](../../../../system/basic-functions/basic-services-kit/arkts-apis/data-file-processing/ohos-request-upload-and-download/document.md#requestagentnetwork10)

 | 

No

 | 

Yes

 | 

Network required by the download task. If the network does not meet the preset condition, tasks that have not been executed will await for execution, and tasks that are being executed will fail or pause. The default value is **request.agent.Network.ANY**.

-   **request.agent.Network.ANY**: network of any type
-   **request.agent.Network.WIFI**: wireless network
-   **request.agent.Network.CELLULAR**: cellular data network

 |

#### ListOptions

Parameters for obtaining the file list.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

maxResults

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of files in a list. The value ranges from 1 to 1000. By default, all files are listed.

 |
| 

pageMarker

 | 

string

 | 

No

 | 

Yes

 | 

Pagination marker. By default, the value is empty.

 |

#### ListResults

File listing result.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

directories

 | 

string\[\]

 | 

No

 | 

No

 | 

List of cloud directories returned.

 |
| 

files

 | 

string\[\]

 | 

No

 | 

No

 | 

List of cloud files returned.

 |
| 

pageMarker

 | 

string

 | 

No

 | 

Yes

 | 

Pagination marker. By default, the value is empty.

 |

#### MetadataUpdatable

Metadata to be updated.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

contentType

 | 

string

 | 

No

 | 

Yes

 | 

Standard HTTP header **Content-Type**.

 |
| 

cacheControl

 | 

string

 | 

No

 | 

Yes

 | 

Standard HTTP header **Cache-Control**.

 |
| 

contentDisposition

 | 

string

 | 

No

 | 

Yes

 | 

Standard HTTP header **Content-Disposition**.

 |
| 

contentEncoding

 | 

string

 | 

No

 | 

Yes

 | 

Standard HTTP header **Content-Encoding**.

 |
| 

contentLanguage

 | 

string

 | 

No

 | 

Yes

 | 

Standard HTTP header **Content-Language**.

 |
| 

customMetadata

 | 

Record<string, string>

 | 

No

 | 

Yes

 | 

Custom cloud file attributes, which are case insensitive and must comply with the standard HTTP header specifications.

 |

#### Metadata

Complete metadata, extended from [MetadataUpdatable](#section1122119164218).

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.DeviceCloudGateway.CloudFoundation

**Start version**: 5.0.0(12)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

name

 | 

string

 | 

No

 | 

No

 | 

Cloud file name.

 |
| 

size

 | 

number

 | 

No

 | 

No

 | 

Size of a cloud file, in bytes.

 |
| 

createTime

 | 

Date

 | 

No

 | 

No

 | 

Time when a cloud file was created, in format _**yyyy-MM-ddTHH:mm:ss**_**Z**.

 |
| 

modifyTime

 | 

Date

 | 

No

 | 

No

 | 

Time when a cloud file was modified, in format _**yyyy-MM-ddTHH:mm:ss**_**Z**.

 |
| 

sha256Hash

 | 

string

 | 

No

 | 

Yes

 | 

SHA-256 information of a cloud file.

 |
