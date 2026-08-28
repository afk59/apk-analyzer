# AssetAccelerationExtensionAbility (ExtensionAbility for Resource Acceleration)

This module is the framework for resource package background download and provides key lifecycle functions. Corresponding callback functions are called when background download tasks succeed, fail, or end. The module has the following restrictions:

-   **AssetAccelerationExtensionAbility** is a lightweight independent subprocess and it is not allowed to wake up the main process.
-   Only the following APIs provided by **assetDownloadManager** can be called:
    -   [assetDownloadManager.fetchManifestUrl](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section81101219425)
    -   [assetDownloadManager.removeAssetDownloadTask](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section222042984419)
    -   [assetDownloadManager.fetchAllAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section918114094718)
    -   [assetDownloadManager.removeAllAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section2809432393)
    -   [assetDownloadManager.fetchGroupAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section93791016111111)
    -   [assetDownloadManager.removeGroupAssetDownloadTasks](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section641613495177)
    -   [assetDownloadManager.limitDownloadTaskSpeed](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section17279143882113)
    -   [assetDownloadManager.reportDownloadProgress](../assetdownloadmanager-resource-package-download-management/document.md#section1492357144916)

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

#### Module Import

import { AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

#### AssetAccelerationExtensionInfo

Information about the resource acceleration ExtensionAbility.

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

maxBackgroundDownloadSize

 | 

number

 | 

Yes

 | 

No

 | 

Maximum resource size, in bytes. The resource acceleration ExtensionAbility is enabled only when the remaining storage space on a user device is greater than three times the value of **maxBackgroundDownloadSize**.

The default value is **0**.

 |
| 

domainList

 | 

string\[\]

 | 

Yes

 | 

No

 | 

Domain name trustlist. Download tasks with domain names not in this trustlist will directly fail.

 |

#### ContentRequestType

type ContentRequestType = 'INSTALL' | 'UPDATE' | 'IDLE'

Content request type.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

'INSTALL'

 | 

Installation.

 |
| 

'UPDATE'

 | 

Update.

 |
| 

'IDLE'

 | 

Idle.

 |

#### AssetAccelerationExtensionAbility

Resource acceleration extension capability class.

**System capability**: SystemCapability.GraphicsGame.AssetAcceleration

**Model restriction**: This API can be used only in the stage model.

**Start version**: 5.1.0(18)

#### \[h2\]Attributes

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

context

 | 

[AssetAccelerationExtensionContext](../assetaccelerationextensioncontext-extensioncontext-for-resource-acceleration/document.md)

 | 

No

 | 

No

 | 

Context of **AssetAccelerationExtensionAbility**, which inherits from [ExtensionContext](../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md).

 |

#### \[h2\]onDownloadContentRequest

onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<assetDownloadManager.AssetDownloadConfig\[\]>

Obtains the resource package download task list when the app is installed or updated, or when the user device is idle. The number of tasks returned cannot exceed 200. This API returns the result asynchronously through a promise.

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

requestType

 | 

[ContentRequestType](#en-us_topic_0000002179272700_section48341532123214)

 | 

Yes

 | 

Content request type.

 |
| 

manifestUrl

 | 

string

 | 

Yes

 | 

Resource package download URL.

-   If a Huawei CDN is used, this parameter is not empty.
-   If a third-party CDN is used, leave this parameter empty.

An empty character string is used by default.

 |
| 

assetAccelerationExtensionInfo

 | 

[AssetAccelerationExtensionInfo](#en-us_topic_0000002179272700_en-us_topic_0000002137765132_section14401125712)

 | 

Yes

 | 

Information about the resource acceleration ExtensionAbility.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[assetDownloadManager.AssetDownloadConfig\[\]](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section14401125712)\>

 | 

Promise object. A configuration information list of a maximum of 200 download tasks is returned.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { assetDownloadManager, AssetAccelerationExtensionAbility, AssetAccelerationExtensionInfo, ContentRequestType } from '@kit.GraphicsAccelerateKit';

// In this example, **AssetAccelExtAbility** inherits from **AssetAccelerationExtensionAbility**.
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  async onDownloadContentRequest(requestType: ContentRequestType, manifestUrl: string,
    assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<assetDownloadManager.AssetDownloadConfig\[\]> {
    const context = this.context as common.ExtensionContext; // If the API needs to use a context of the common.Context type, you can obtain the context object of the common.ExtensionContext type from **this.context**.
    console.info('AssetAccelDemo', \`application file directory = ${context.filesDir}\`);
    console.info('AssetAccelDemo', \`onDownloadContentRequest enter, requestType: ${requestType}, manifestUrl: ${manifestUrl}.\`);
    // Construct the download task configuration information used as the API's return value.
    let downloadList: Array<assetDownloadManager.AssetDownloadConfig> = \[\];
    let download: assetDownloadManager.AssetDownloadConfig = {
        identifier: 'identifier',
        url: 'url',
        isEssential: false,
        groupId:'groupId',
        fileName: 'fileName'
      }
    downloadList.push(download);
    return downloadList;
  }
};

#### \[h2\]onDownloadWithAppControl

onDownloadWithAppControl(requestType: ContentRequestType, manifestUrl: string, assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<boolean>

Triggers the ExtensionAbility to initiate coordinated download when the app is installed or updated, or when the user device is idle. If there is a resource package download task, **true** is returned. Otherwise, **false** is returned. This API returns the result asynchronously through a promise.

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

requestType

 | 

[ContentRequestType](#en-us_topic_0000002179272700_section48341532123214)

 | 

Yes

 | 

Content request type.

 |
| 

manifestUrl

 | 

string

 | 

Yes

 | 

Resource package download URL.

-   If a Huawei CDN is used to host resources, the URL is provided by the Huawei CDN.
-   If a third-party CDN is used, leave this parameter empty.

An empty character string is used by default.

 |
| 

assetAccelerationExtensionInfo

 | 

[AssetAccelerationExtensionInfo](#en-us_topic_0000002179272700_en-us_topic_0000002137765132_section14401125712)

 | 

Yes

 | 

Information about the resource acceleration ExtensionAbility.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise object.

-   **true**: There is a download task in the app's downloader.
-   **false**: There is no download task in the app's downloader.

 |

**Example**:

import { common } from '@kit.AbilityKit';
import { AssetAccelerationExtensionAbility, AssetAccelerationExtensionInfo, ContentRequestType } from '@kit.GraphicsAccelerateKit';

// In this example, **AssetAccelExtAbility** inherits from **AssetAccelerationExtensionAbility**.
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  async onDownloadWithAppControl(requestType: ContentRequestType, manifestUrl: string,
    assetAccelerationExtensionInfo: AssetAccelerationExtensionInfo): Promise<boolean> {
    const context = this.context as common.ExtensionContext; // If the API needs to use a context of the common.Context type, you can obtain the context object of the common.ExtensionContext type from **this.context**.
    console.info('AssetAccelDemo', \`application file directory = ${context.filesDir}\`);
    console.info('AssetAccelDemo', \`onDownloadWithAppControl enter, requestType: ${requestType}, manifestUrl: ${manifestUrl}.\`);
    // If there is a download task, **true** is returned and the app's downloader is called to download resource packages. Otherwise, **false** is returned.
    // ...
    let result = true;
    return result;
  }
};

#### \[h2\]onBackgroundDownloadSucceeded

onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask, filePath: string): Promise<void>

Notifies the resource acceleration ExtensionAbility of download success. It is executed when a system background download task is successful. This API returns the result asynchronously through a promise.

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

downloadTask

 | 

[assetDownloadManager.AssetDownloadTask](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)

 | 

Yes

 | 

Download task information.

 |
| 

filePath

 | 

string

 | 

Yes

 | 

Local sandbox address of the downloaded file. Located in the app's **cache** directory. The following is an example path:

/data/storage/el2/base/haps/entry/cache/asset\_acceleration/1.8.2/xxx.bin

It contains a maximum of 512 bytes.

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

**Example**:

import { assetDownloadManager, AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// In this example, **AssetAccelExtAbility** inherits from **AssetAccelerationExtensionAbility**.
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // Receive the background download success notification.
  async onBackgroundDownloadSucceeded(downloadTask: assetDownloadManager.AssetDownloadTask,
    filePath: string): Promise<void> {
    console.info('AssetAccelDemo', \`onBackgroundDownloadSucceeded enter, taskId is ${downloadTask.taskId}, filePath = ${filePath}\`);
    // Add the logic for transferring files.
  }
};

#### \[h2\]onBackgroundDownloadFailed

onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask, fault: assetDownloadManager.DownloadFault): Promise<void>

Notifies the resource acceleration ExtensionAbility of download failure. It is executed when a system background download task fails. This API returns the result asynchronously through a promise.

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

downloadTask

 | 

[assetDownloadManager.AssetDownloadTask](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section1639510932819)

 | 

Yes

 | 

Download task information.

 |
| 

fault

 | 

[assetDownloadManager.DownloadFault](../assetdownloadmanager-resource-package-download-management/document.md#en-us_topic_0000002214513333_en-us_topic_0000002137922672_section82071855806)

 | 

Yes

 | 

Download failure cause.

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

**Example**:

import { assetDownloadManager, AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// In this example, **AssetAccelExtAbility** inherits from **AssetAccelerationExtensionAbility**.
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // Receive the background download failure notification.
  async onBackgroundDownloadFailed(downloadTask: assetDownloadManager.AssetDownloadTask,
    fault: assetDownloadManager.DownloadFault): Promise<void> {
    console.info('AssetAccelDemo', \`onBackgroundDownloadFailed enter, download url: ${downloadTask.config.url}, err: ${fault}\`);
    // Add the logic for handling download exceptions.
  }
};

#### \[h2\]onExtensionWillTerminate

onExtensionWillTerminate(error?: BusinessError<void>): Promise<void>

Notifies the resource acceleration ExtensionAbility that the resource package background download function is to be disabled. The API is executed when the resource acceleration ExtensionAbility will terminate, either normally or due to a scheduling error. You are advised to perform resource clearing operations in this method. Do not perform time-consuming operations. This API returns the result asynchronously through a promise.

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

error

 | 

BusinessError<void>

 | 

No

 | 

Error code.

-   **401**: parameter error.
-   **1016600005**: The execution of a resource acceleration ExtensionAbility method times out.
-   **1016600006**: There is an abnormal method within the resource acceleration ExtensionAbility lifecycle.
-   **1016600094**: Service error.

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

**Example**:

import { BusinessError } from '@kit.BasicServicesKit';
import { AssetAccelerationExtensionAbility } from '@kit.GraphicsAccelerateKit';

// In this example, **AssetAccelExtAbility** inherits from **AssetAccelerationExtensionAbility**.
export default class AssetAccelExtAbility extends AssetAccelerationExtensionAbility {
  // This callback is executed when **AssetAccelerationExtensionAbility** will terminate, either normally or due to a scheduling error.
  async onExtensionWillTerminate(error?: BusinessError<void>): Promise<void> {
    // Add the logic for performing operations such as resource cleanup. Avoid time-consuming operations.
    if (!error) {
      console.info('AssetAccelDemo', \`onExtensionWillTerminate enter, BusinessError is null;\`);
      return;
    }
    console.error('AssetAccelDemo', \`onExtensionWillTerminate enter, BusinessError: ${error?.code}, msg: ${error?.message}\`);
  }
};
