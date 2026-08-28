# @ohos.statfs (statfs)

The **statfs** module provides APIs for obtaining file system information, including the total size and free size of a file system, in bytes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/3ynl37KhQ_SCvpJMCLDhIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F13CBD1057482F7BFB31F0F68E9947BA9D6383AE071156CAB7BD35657BE27083)

-   The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs provided by this module are deprecated since API version 9. You are advised to use [@ohos.file.statvfs](../../ohos-file-statvfs-file-system-space-statistics/document.md).

#### Modules to Import

import statfs from '@ohos.statfs';

#### Statfs.getFreeBytes

getFreeBytes(path:string):Promise<number>

Obtains the free size of the specified file system, in bytes. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the file system. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the free size obtained. |

**Example**

import { BusinessError } from '@ohos.base';
let path = "/dev";
statfs.getFreeBytes(path).then((number: number) => {
  console.info("getFreeBytes promise successfully:" + number);
}).catch((err: BusinessError) => {
  console.error("getFreeBytes failed with error:" + JSON.stringify(err));
});

#### Statfs.getFreeBytes

getFreeBytes(path:string, callback:AsyncCallback<number>): void

Obtains the free size of the specified file system, in bytes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the file system. |
| callback | AsyncCallback<number> | Yes | Callback used to return the free size obtained. |

**Example**

import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
let context = getContext(this) as common.UIAbilityContext;
let path = context.filesDir;
statfs.getFreeBytes(path, (err: BusinessError, freeBytes:Number) => {
    if (err) {
        console.error('getFreeBytes callback failed');
    } else {
        console.info('getFreeBytes callback success' + freeBytes);
    }
});

#### Statfs.getTotalBytes

getTotalBytes(path: string): Promise<number>

Obtains the total size of the specified file system, in byte. This API uses a promise to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the file system. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise used to return the total size obtained. |

**Example**

import { BusinessError } from '@ohos.base';
let path = "/dev";
statfs.getTotalBytes(path).then((number: number) => {
  console.info("getTotalBytes promise successfully:" + number);
}).catch((err: BusinessError) => {
  console.error("getTotalBytes failed with error:" + JSON.stringify(err));
});

#### Statfs.getTotalBytes

getTotalBytes(path: string, callback: AsyncCallback<number>): void

Obtains the total size of the specified file system, in bytes. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Path of the file system. |
| callback | AsyncCallback<number> | Yes | Callback used to return the total size obtained. |

**Example**

import common from '@ohos.app.ability.common';
import { BusinessError } from '@ohos.base';
let context = getContext(this) as common.UIAbilityContext;
let path = context.filesDir;
statfs.getTotalBytes(path, (err: BusinessError, totalBytes:Number) => {
    if (err) {
        console.error('getTotalBytes callback failed');
    } else {
        console.info('getTotalBytes callback success' + totalBytes);
    }
});
