# @ohos.fileio (File Management)

The **FileIO** module provides APIs for file storage and management, including basic file management, directory management, file information statistics, and stream read and write.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Drf4SBXuQ8u55xy3_H0dLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD38B5CE086DE08CC29DAF5915DE3A57989702D00A5E78090D4B16FA46A85F32)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs provided by this module are deprecated since API version 9. You are advised to use [@ohos.file.fs](../../ohos-file-fs-file-management/document.md).

#### Modules to Import

import fileio from '@ohos.fileio';

#### How to Use

Before using the APIs provided by this module to perform operations on a file or directory, obtain the application sandbox path of the file or directory as follows:

 import UIAbility from '@ohos.app.ability.UIAbility';
 import window from '@ohos.window';

 export default class EntryAbility extends UIAbility {
   onWindowStageCreate(windowStage: window.WindowStage) {
     let context = this.context;
     let pathDir = context.filesDir;
   }
 }

For details about how to obtain the application sandbox path, see [Obtaining Application File Paths](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/application-context-stage#obtaining-application-file-paths).

#### fileio.stat

stat(path: string): Promise<Stat>

Obtains file information. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/_TSvbkvHS7GkULPtf-zegQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C3C7E9828C538F5452C1A2D9488090B48AD6401D88F592B3C953E45B7B96E09)

This API is deprecated since API version 9. Use [fs.stat](../../ohos-file-fs-file-management/document.md#stat) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise that returns the file information obtained. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "test.txt";
fileio.stat(filePath).then((stat: fileio.Stat) => {
  console.info("getFileInfo succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("getFileInfo failed with error:" + err);
});

#### fileio.stat

stat(path: string, callback: AsyncCallback<Stat>): void

Obtains file information. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f3/v3/VoC35Td5TsiTLJfMk7vPRw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB0763F4F92F58CFCFF757332465FD7AFF55EA65D26ECD9AEB3D2D5C4F3499E3)

This API is deprecated since API version 9. Use [fs.stat](../../ohos-file-fs-file-management/document.md#fsstat-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| callback | AsyncCallback<[Stat](#stat)\> | Yes | Callback used to return the file information obtained. |

**Example**

import { BusinessError } from '@ohos.base';
fileio.stat(pathDir, (err: BusinessError, stat: fileio.Stat) => {
  // Example code in Stat
});

#### fileio.statSync

statSync(path: string): Stat

Obtains file information. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/rUEAKZ-lTq6JF2E2n0-hrw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CD560DC40BFCD9E536BBBD867194FAAA73FFB364CD4BF46C07DF36E55F891E8)

This API is deprecated since API version 9. Use [fs.statSync](../../ohos-file-fs-file-management/document.md#fsstatsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stat](#stat) | File information obtained. |

**Example**

let stat = fileio.statSync(pathDir);
// Example code in Stat

#### fileio.opendir

opendir(path: string): Promise<Dir>

Opens a directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/7_F60BYyQxCo26kHYgHPbw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D057DB45F51C47A86A2CA860A672FDE7B9249830E8035274C6D09A18C6B4E7F6)

This API is deprecated since API version 9. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory to open. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Dir](#dir)\> | Promise that returns the **Dir** object opened. |

**Example**

import { BusinessError } from '@ohos.base';
let dirPath = pathDir + "/testDir";
fileio.opendir(dirPath).then((dir: fileio.Dir) => {
  console.info("opendir succeed");
}).catch((err: BusinessError) => {
  console.error("opendir failed with error:" + err);
});

#### fileio.opendir

opendir(path: string, callback: AsyncCallback<Dir>): void

Opens a file directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/XK3k6kWBS8-b1vDG_NtY0Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7493697B86D16CBB215560F9992EAF5B3E88A6A5FC22F14697924403688942B9)

This API is deprecated since API version 9. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory to open. |
| callback | AsyncCallback<[Dir](#dir)\> | Yes | Callback invoked when the directory is opened asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
fileio.opendir(pathDir, (err: BusinessError, dir: fileio.Dir) => {
  // Example code in Dir struct
  // Use read/readSync/close.
});

#### fileio.opendirSync

opendirSync(path: string): Dir

Opens a directory. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/Y8rm1EIPTDCxcIeRfe0nDQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8087FFE626B6B5FB29FC1ED08FD624233ED41D141C4457BA24DF194F38E7B70E)

This API is deprecated since API version 9. Use [fs.listFileSync](../../ohos-file-fs-file-management/document.md#fslistfilesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory to open. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Dir](#dir) | The **Dir** object opened. |

**Example**

let dir = fileio.opendirSync(pathDir);
// Example code in Dir struct
// Use read/readSync/close.

#### fileio.access

access(path: string, mode?: number): Promise<void>

Checks whether this process can access a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/j5bMoAczSj-VF4uRM9RCMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=677927CB70D6EED50D909B2C7B953F993EE3C65AA82543B3A024E6978D5F7F67)

This API is deprecated since API version 9. Use [fs.access](../../ohos-file-fs-file-management/document.md#fsaccess) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | No | 
Options for accessing the file. You can specify multiple options, separated with a bitwise OR operator (|). The default value is **0**.

The options are as follows:

\- **0**: Check whether the file exists.

\- **1**: Check whether the process has the execute permission on the file.

\- **2**: Check whether the process has the write permission on the file.

\- **4**: Check whether the process has the read permission on the file.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath).then(() => {
  console.info("access succeed");
}).catch((err: BusinessError) => {
  console.error("access failed with error:" + err);
});

#### fileio.access

access(path: string, mode?: number, callback: AsyncCallback<void>): void

Checks whether this process can access a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/i2DRZB5ER6ae4DJWeAfMjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=125E2D8BCC7156BDCA7F4E3C2AC975E002ECF8E5BA5B16B27770C291CB8A2A28)

This API is deprecated since API version 9. Use [fs.access](../../ohos-file-fs-file-management/document.md#fsaccess-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | No | 
Options for accessing the file. You can specify multiple options, separated with a bitwise OR operator (|). The default value is **0**.

The options are as follows:

\- **0**: Check whether the file exists.

\- **1**: Check whether the process has the execute permission on the file.

\- **2**: Check whether the process has the write permission on the file.

\- **4**: Check whether the process has the read permission on the file.

 |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file is asynchronously checked. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.access(filePath, (err: BusinessError) => {
  // Do something.
});

#### fileio.accessSync

accessSync(path: string, mode?: number): void

Checks whether this process can access a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/6KphaOVOTWOJw2T8-qdBIw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3DB964D5902AB36476EB946A32520260224006F8836DFB35D02D03B526302189)

This API is deprecated since API version 9. Use [fs.accessSync](../../ohos-file-fs-file-management/document.md#fsaccesssync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | No | 
Options for accessing the file. You can specify multiple options, separated with a bitwise OR operator (|). The default value is **0**.

The options are as follows:

\- **0**: Check whether the file exists.

\- **1**: Check whether the process has the execute permission on the file.

\- **2**: Check whether the process has the write permission on the file.

\- **4**: Check whether the process has the read permission on the file.

 |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
try {
  fileio.accessSync(filePath);
} catch(error) {
  let err: BusinessError = error as BusinessError;
  console.error("accessSync failed with error:" + err);
}

#### fileio.close7+

close(fd: number): Promise<void>

Closes a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f5/v3/yoP_WKdMSzKuTd62UD0UEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A769D5610035545322E7EE7EFB85198C83A5F3FEFC8120AC979A23574225FFC4)

This API is deprecated since API version 9. Use [fs.close](../../ohos-file-fs-file-management/document.md#fsclose) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to close. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd).then(() => {
  console.info("close file succeed");
}).catch((err: BusinessError) => {
  console.error("close file failed with error:" + err);
});

#### fileio.close7+

close(fd: number, callback: AsyncCallback<void>): void

Closes a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/pJJAKYEYTYyFQfV5NljYcQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=25E78B795E5EB9B7867FEB8A6DB2C2FB8AB3C74AFE26A2166FE53EE38A0D683E)

This API is deprecated since API version 9. Use [fs.close](../../ohos-file-fs-file-management/document.md#fsclose-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to close. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file is closed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.close(fd, (err: BusinessError) => {
  // Do something.
});

#### fileio.closeSync

closeSync(fd: number): void

Closes a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/JsO-8PZVQzSFVlkvuaZk7w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F1A242FEFDEA0F1419ADD1E128533934BB4102B606285F7ADFE4C61225473ED)

This API is deprecated since API version 9. Use [fs.closeSync](../../ohos-file-fs-file-management/document.md#fsclosesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to close. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.closeSync(fd);

#### fileio.copyFile

copyFile(src: string|number, dest: string|number, mode?: number): Promise<void>

Copies a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/38/v3/VT32jtXeRhShsfyIipK7dg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D217EC34DC1FDE47B10771F7D7701D629EA0BEE718C34AB9DAA3F641813B4177)

This API is deprecated since API version 9. Use [fs.copyFile](../../ohos-file-fs-file-management/document.md#fscopyfile) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string|number | Yes | Path or file descriptor of the source file to copy. |
| dest | string|number | Yes | Path or file descriptor of the destination file. |
| mode | number | No | 
Option for overwriting the destination file. The default value is **0**, which is the only value supported.

**0**: Overwrite the file with the same name completely and truncate the part that is not overwritten.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath).then(() => {
  console.info("copyFile succeed");
}).catch((err: BusinessError) => {
  console.error("copyFile failed with error:" + err);
});

#### fileio.copyFile

copyFile(src: string|number, dest: string|number, mode: number, callback: AsyncCallback<void>): void

Copies a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/bWbm1HmcT2iYzOwzFdNHoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCDC3858315D974AE0B9CFEEE97BB757400714F202C697ACAE39AB0886891A23)

This API is deprecated since API version 9. Use [fs.copyFile](../../ohos-file-fs-file-management/document.md#fscopyfile-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string|number | Yes | Path or file descriptor of the source file to copy. |
| dest | string|number | Yes | Path or file descriptor of the destination file. |
| mode | number | No | 
Option for overwriting the destination file. The default value is **0**, which is the only value supported.

**0**: Overwrite the file with the same name completely and truncate the part that is not overwritten.

 |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file is copied asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFile(srcPath, dstPath, (err: BusinessError) => {
  // Do something.
});

#### fileio.copyFileSync

copyFileSync(src: string|number, dest: string|number, mode?: number): void

Copies a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/mY-FEIdYS52l_muEZFLx1A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=629F3F4ABC14FB4188D5361A9EA701045DD2FD1E8474EF0D2A1A5F86948CE15A)

This API is deprecated since API version 9. Use [fs.copyFileSync](../../ohos-file-fs-file-management/document.md#fscopyfilesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| src | string|number | Yes | Path or file descriptor of the source file to copy. |
| dest | string|number | Yes | Path or file descriptor of the destination file. |
| mode | number | No | 
Option for overwriting the destination file. The default value is **0**, which is the only value supported.

**0**: Overwrite the file with the same name completely and truncate the part that is not overwritten.

 |

**Example**

let srcPath = pathDir + "srcDir/test.txt";
let dstPath = pathDir + "dstDir/test.txt";
fileio.copyFileSync(srcPath, dstPath);

#### fileio.mkdir

mkdir(path: string, mode?: number): Promise<void>

Creates a directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/thoLUlMESYyscprAYBT5bQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C50088A781B97BB3F55DD1078CCCF61978285F1FEB797F66FE9BA12C3FF8AB2)

This API is deprecated since API version 9. Use [fs.mkdir](../../ohos-file-fs-file-management/document.md#fsmkdir) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| mode | number | No | 
Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (|). The default value is **0o775**.

\- **0o775**: The owner has the read, write, and execute permissions, and other users have the read and execute permissions.

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath).then(() => {
  console.info("mkdir succeed");
}).catch((error: BusinessError) => {
  console.error("mkdir failed with error:" + error);
});

#### fileio.mkdir

mkdir(path: string, mode: number, callback: AsyncCallback<void>): void

Creates a directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/eiLSXg93SdyTTg4VDblyng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=446E8B35C4A3EAC49B8C2CBB6FEB0F7A4A6AD97834828C4D3F487E704E95F52E)

This API is deprecated since API version 9. Use [fs.mkdir](../../ohos-file-fs-file-management/document.md#fsmkdir-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| mode | number | No | 
Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (|). The default value is **0o775**.

\- **0o775**: The owner has the read, write, and execute permissions, and other users have the read and execute permissions.

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |
| callback | AsyncCallback<void> | Yes | Callback invoked when the directory is created asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.mkdir(dirPath, (err: BusinessError) => {
  console.info("mkdir succeed");
});

#### fileio.mkdirSync

mkdirSync(path: string, mode?: number): void

Creates a directory. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/pa27JbbvTZCAsvc3rN5g5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=213B43BA213677350DD3E205075F133E29AEA3BD16B985311B594DDA1B47A199)

This API is deprecated since API version 9. Use [fs.mkdirSync](../../ohos-file-fs-file-management/document.md#fsmkdirsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| mode | number | No | 
Permission on the directory to create. You can specify multiple permissions, separated using a bitwise OR operator (|). The default value is **0o775**.

\- **0o775**: The owner has the read, write, and execute permissions, and other users have the read and execute permissions.

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |

**Example**

let dirPath = pathDir + '/testDir';
fileio.mkdirSync(dirPath);

#### fileio.open7+

open(path: string, flags?: number, mode?: number): Promise<number>

Opens a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/df/v3/GzxmZWPwSYC-oduRX26y3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FBCF7E45F441E5539D430DEDCD47A1E9485679430129E1354F4DEA95B4C7C80B)

This API is deprecated since API version 9. Use [fs.open](../../ohos-file-fs-file-management/document.md#fsopen) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| flags | number | No | 
Option for opening the file. You must specify one of the following options. By default, the file is opened in read-only mode.

\- **0o0**: Open the file in read-only mode.

\- **0o1**: Open the file in write-only mode.

\- **0o2**: Open the file in read/write mode.

In addition, you can specify the following options, separated using a bitwise OR operator (|). By default, no additional option is specified.

\- **0o100**: If the file does not exist, create it. If you use this option, you must also specify **mode**.

\- **0o200**: If **0o100** is added and the file already exists, throw an exception.

\- **0o1000**: If the file exists and is opened in write mode, truncate the file length to 0.

\- **0o2000**: Open the file in append mode. New data will be appended to the file (added to the end of the file).

\- **0o4000**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the open file and in subsequent I/Os.

\- **0o200000**: If **path** does not point to a directory, throw an exception.

\- **0o400000**: If **path** points to a symbolic link, throw an exception.

\- **0o4010000**: Open the file in synchronous I/O mode.

 |
| mode | number | No | 

Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|). The default value is **0o660**.

\- **0o660**: The owner and user group have the read and write permissions.

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise that returns the file descriptor of the file opened. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.open(filePath, 0o1, 0o0200).then((number: number) => {
  console.info("open file succeed");
}).catch((err: BusinessError) => {
  console.error("open file failed with error:" + err);
});

#### fileio.open7+

open(path: string, flags: number, mode: number, callback: AsyncCallback<number>): void

Opens a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/9JdHblgDRCWuIPZdHh3DAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFC9A59AA03E503537BC82024B52FCFD67B18BD03ECE11D65DA8E2157F525D91)

This API is deprecated since API version 9. Use [fs.open](../../ohos-file-fs-file-management/document.md#fsopen-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| flags | number | No | 
Option for opening the file. You must specify one of the following options. By default, the file is opened in read-only mode.

\- **0o0**: Open the file in read-only mode.

\- **0o1**: Open the file in write-only mode.

\- **0o2**: Open the file in read/write mode.

In addition, you can specify the following options, separated using a bitwise OR operator (|). By default, no additional option is specified.

\- **0o100**: If the file does not exist, create it. If you use this option, you must also specify **mode**.

\- **0o200**: If **0o100** is added and the file already exists, throw an exception.

\- **0o1000**: If the file exists and is opened in write mode, truncate the file length to 0.

\- **0o2000**: Open the file in append mode. New data will be appended to the file (added to the end of the file).

\- **0o4000**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the open file and in subsequent I/Os.

\- **0o200000**: If **path** does not point to a directory, throw an exception.

\- **0o400000**: If **path** points to a symbolic link, throw an exception.

\- **0o4010000**: Open the file in synchronous I/O mode.

 |
| mode | number | No | 

Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|). The default value is **0o660**.

\- **0o660**: The owner and user group have the read and write permissions.

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |
| callback | AsyncCallback<number> | Yes | Callback invoked when the file is opened asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.open(filePath, 0, (err: BusinessError, fd: number) => {
  // Do something.
});

#### fileio.openSync

openSync(path: string, flags?: number, mode?: number): number

Opens a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/z9Qxa5HgSP6-V-TH4AoW-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B857415945EABF3E566F2336CD1828F8B66669006EF09AF90293BDCFCD9D9723)

This API is deprecated since API version 9. Use [fs.openSync](../../ohos-file-fs-file-management/document.md#fsopensync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| flags | number | No | 
Option for opening the file. You must specify one of the following options. By default, the file is opened in read-only mode.

\- **0o0**: Open the file in read-only mode.

\- **0o1**: Open the file in write-only mode.

\- **0o2**: Open the file in read/write mode.

In addition, you can specify the following options, separated using a bitwise OR operator (|). By default, no additional option is specified.

\- **0o100**: If the file does not exist, create it. If you use this option, you must also specify **mode**.

\- **0o200**: If **0o100** is added and the file already exists, throw an exception.

\- **0o1000**: If the file exists and is opened in write mode, truncate the file length to 0.

\- **0o2000**: Open the file in append mode. New data will be appended to the file (added to the end of the file).

\- **0o4000**: If **path** points to a named pipe (also known as a FIFO), block special file, or character special file, perform non-blocking operations on the open file and in subsequent I/Os.

\- **0o200000**: If **path** does not point to a directory, throw an exception.

\- **0o400000**: If **path** points to a symbolic link, throw an exception.

\- **0o4010000**: Open the file in synchronous I/O mode.

 |
| mode | number | No | 

Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|). The default value is **0o660**.

\- **0o660**: The owner and user group have the read and write permissions.

\- **0o640**: The owner has the read and write permissions, and the user group has the read permission.

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

The file permissions on newly created files are affected by umask, which is set as the process starts. Currently, the modification of umask is not open.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | File descriptor of the file opened. |

#### fileio.read

read(fd: number, buffer: ArrayBuffer, options?: { offset?: number; length?: number; position?: number; }): Promise<ReadOut>

Reads data from a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f9/v3/Ulazkqm7RRCTOatVgLKH5g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C7518FD98453FA1DF986EF7A41B974E69D92196636AEA2AE0E02BD702F08B20F)

This API is deprecated since API version 9. Use [fs.read](../../ohos-file-fs-file-management/document.md#fsread) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to read. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position to store the data read in the buffer in reference to the start address of the buffer. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

Constraints: offset + length <= Buffer size

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReadOut](#readout)\> | Promise that returns the data read. |

#### fileio.read

read(fd: number, buffer: ArrayBuffer, options: { offset?: number; length?: number; position?: number; }, callback: AsyncCallback<ReadOut>): void

Reads data from a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/TNDYwwcvQAeCktMPoZFxEQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D79E2F0A1CBB0FEDA5C32A6EC7FAAAE860DF526DB26DF3B9EFAAB0F842CEFF2)

This API is deprecated since API version 9. Use [fs.read](../../ohos-file-fs-file-management/document.md#fsread-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to read. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position to store the data read in the buffer in reference to the start address of the buffer. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

Constraints: offset + length <= Buffer size

 |
| callback | AsyncCallback<[ReadOut](#readout)\> | Yes | Callback invoked when the data is read asynchronously. |

#### fileio.readSync

readSync(fd: number, buffer: ArrayBuffer, options?: { offset?: number; length?: number; position?: number; }): number

Reads data from a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/ASPjpzx_SDmdvdeb_scxjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BCC9AA317653E78F0C1E6A86E674F7FB6CC088DBEDB3B33B533196731F3FB98C)

This API is deprecated since API version 9. Use [fs.readSync](../../ohos-file-fs-file-management/document.md#fsreadsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to read. |
| buffer | ArrayBuffer | Yes | Buffer used to store the file data read. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position to store the data read in the buffer in reference to the start address of the buffer. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

Constraints: offset + length <= Buffer size

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data read. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o2);
let buf = new ArrayBuffer(4096);
let num = fileio.readSync(fd, buf);

#### fileio.rmdir7+

rmdir(path: string): Promise<void>

Removes a directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/4fkSQBf2R1SagtSjC9bKTw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26C7779B682EF9533722A7E834E06D5880194B73E40F03F664B8A4803D37D14C)

This API is deprecated since API version 9. Use [fs.rmdir](../../ohos-file-fs-file-management/document.md#fsrmdir) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.rmdir(dirPath).then(() => {
  console.info("rmdir succeed");
}).catch((err: BusinessError) => {
  console.error("rmdir failed with error:" + err);
});

#### fileio.rmdir7+

rmdir(path: string, callback: AsyncCallback<void>): void

Removes a directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/LQZJxYP7Q52FPaXwxnSfCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2C8637A39AADF58146C31BD76A08E73CD36EA8D300D3AFF4D96CBC0A3D5358A)

This API is deprecated since API version 9. Use [fs.rmdir](../../ohos-file-fs-file-management/document.md#fsrmdir-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |
| callback | AsyncCallback<void> | Yes | Callback invoked when a directory is removed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let dirPath = pathDir + '/testDir';
fileio.rmdir(dirPath, (err: BusinessError) => {
  // Do something.
  console.info("rmdir succeed");
});

#### fileio.rmdirSync7+

rmdirSync(path: string): void

Removes a directory. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/50/v3/_BrLhTxKTG-ZYS_NcAtp0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86A41C9836BE8AF02A7DC71BD1C2C610DBA8CF80E8A3F377EBA093E4A13AE5AD)

This API is deprecated since API version 9. Use [fs.rmdirSync](../../ohos-file-fs-file-management/document.md#fsrmdirsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the directory. |

**Example**

let dirPath = pathDir + '/testDir';
fileio.rmdirSync(dirPath);

#### fileio.unlink

unlink(path: string): Promise<void>

Removes a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/RNcpxxwBR-yw0KHlPyaqOg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93BFCFBBD628EA0E1977DA2F05A848198A057A491AFEFDF41642AC9FBF6DA01E)

This API is deprecated since API version 9. Use [fs.unlink](../../ohos-file-fs-file-management/document.md#fsunlink) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.unlink(filePath).then(() => {
  console.info("remove file succeed");
}).catch((error: BusinessError) => {
  console.error("remove file failed with error:" + error);
});

#### fileio.unlink

unlink(path: string, callback: AsyncCallback<void>): void

Removes a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fc/v3/dbZiEqP3TOKNnHf6XkPBNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDFD7F36E461DC85E8F012974AC57CB21292523DF750C04A696A3CA7EE08B52C)

This API is deprecated since API version 9. Use [fs.unlink](../../ohos-file-fs-file-management/document.md#fsunlink-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file is removed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.unlink(filePath, (err: BusinessError) => {
  console.info("remove file succeed");
});

#### fileio.unlinkSync

unlinkSync(path: string): void

Removes a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/EEASYEp3T86gD0x1tkUN3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=112F4D1667DABEB9C16EF979533F2CCEA63E06571415081B064C6CA6B76AADB7)

This API is deprecated since API version 9. Use [fs.unlinkSync](../../ohos-file-fs-file-management/document.md#fsunlinksync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |

**Example**

let filePath = pathDir + "/test.txt";
fileio.unlinkSync(filePath);

#### fileio.write

write(fd: number, buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): Promise<number>

Writes data into a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/2-aA2ozWRd6NS0XP28c8ow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E08F922D367E521676A0614D0DDE41F6011AFCE0AAA593FA4CF802CCDA9FE315)

This API is deprecated since API version 9. Use [fs.write](../../ohos-file-fs-file-management/document.md#fswrite) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer|string | Yes | Data to write. It can be a string or data from a buffer. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position of the data to write in reference to the start address of the data. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

Constraints: offset + length <= Buffer size

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise that returns the length of the data written. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
fileio.write(fd, "hello, world").then((number: number) => {
  console.info("write data to file succeed and size is:" + number);
}).catch((err: BusinessError) => {
  console.error("write data to file failed with error:" + err);
});

#### fileio.write

write(fd: number, buffer: ArrayBuffer|string, options: { offset?: number; length?: number; position?: number; encoding?: string; }, callback: AsyncCallback<number>): void

Writes data to a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/jb3jqyx5QIO_ZOn6FrP2Nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CE137ACA2C7916BEACB4987A34CCDB73C70F5E9D94A9771CCEA2065769944DD3)

This API is deprecated since API version 9. Use [fs.write](../../ohos-file-fs-file-management/document.md#fswrite-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer|string | Yes | Data to write. It can be a string or data from a buffer. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position of the data to write in reference to the start address of the data. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

Constraints: offset + length <= Buffer size

 |
| callback | AsyncCallback<number> | Yes | Callback invoked when the data is written asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
fileio.write(fd, "hello, world", (err: BusinessError, bytesWritten: number) => {
  if (bytesWritten) {
    console.info("write data to file succeed and size is:" + bytesWritten);
  }
});

#### fileio.writeSync

writeSync(fd: number, buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): number

Writes data to a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/jDdT6n5PS3emqHElf61s7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9188E5F0D40A5A1114DD8DAAA0F5B68B27C3D8A55D938DB3A91F89029C894DF3)

This API is deprecated since API version 9. Use [fs.writeSync](../../ohos-file-fs-file-management/document.md#fswritesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to write. |
| buffer | ArrayBuffer|string | Yes | Data to write. It can be a string or data from a buffer. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position of the data to write in reference to the start address of the data. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

Constraints: offset + length <= Buffer size

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data written in the file. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath, 0o100 | 0o2, 0o666);
let num = fileio.writeSync(fd, "hello, world");

#### fileio.hash

hash(path: string, algorithm: string): Promise<string>

Calculates the hash value of a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/42/v3/rEK3IHJyQ_6IFoQwu0mPlw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26340E7571667D5CB1B3808D7BB114F985CA11E816068E21BEA094BD34FE94BE)

This API is deprecated since API version 9. Use [hash.write](../../ohos-file-hash-file-hash-processing/document.md#hashhash) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| algorithm | string | Yes | Algorithm used to calculate the hash value. The value can be **md5**, **sha1**, or **sha256**. **sha256** is recommended for security purposes. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise that returns the hash value. The hash value is a hexadecimal string consisting of digits and uppercase letters. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.hash(filePath, "sha256").then((str: string) => {
  console.info("calculate file hash succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("calculate file hash failed with error:" + err);
});

#### fileio.hash

hash(path: string, algorithm: string, callback: AsyncCallback<string>): void

Calculates the hash value of a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/xqZ6UjSvRlW-Ux2vABFBMA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60FD96092B0288D1840C06086253CD80A4C9B3C12DCBAFC3B0F5DC43E55894D3)

This API is deprecated since API version 9. Use [hash.write](../../ohos-file-hash-file-hash-processing/document.md#hashhash-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| algorithm | string | Yes | Algorithm used to calculate the hash value. The value can be **md5**, **sha1**, or **sha256**. **sha256** is recommended for security purposes. |
| callback | AsyncCallback<string> | Yes | Callback used to return the hash value obtained. The hash value is a hexadecimal string consisting of digits and uppercase letters. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.hash(filePath, "sha256", (err: BusinessError, hashStr: string) => {
  if (hashStr) {
    console.info("calculate file hash succeed:" + hashStr);
  }
});

#### fileio.chmod7+

chmod(path: string, mode: number): Promise<void>

Changes file permissions. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/bYYlDNf9T-ytp198ULMQPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1ACB80DFE1803B46CFFE2204D12A765988979046FB8F3D09D0B22ADF9D54A9A7)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | Yes | 
Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|).

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.chmod(filePath, 0o700).then(() => {
  console.info("chmod succeed");
}).catch((err: BusinessError) => {
  console.error("chmod failed with error:" + err);
});

#### fileio.chmod7+

chmod(path: string, mode: number, callback: AsyncCallback<void>): void

Changes file permissions. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/-ipDxMWCS2myLQbFvqnKLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B68775D95FBE4067EF702C2090F9241FCD0E9CA90624A2EE6B89AF301017A66D)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | Yes | 
Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|).

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file permissions are changed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.chmod(filePath, 0o700, (err: BusinessError) => {
  // Do something.
});

#### fileio.chmodSync7+

chmodSync(path: string, mode: number): void

Changes file permissions. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/Gtt_2-F1Q1yrw23VDVrpYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E99C5EB2364151C31B61F6E5343343659CBDFD612B7FABD823FF9CAA3BF2A1C)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | number | Yes | 
Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|).

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |

**Example**

let filePath = pathDir + "/test.txt";
fileio.chmodSync(filePath, 0o700);

#### fileio.fstat7+

fstat(fd: number): Promise<Stat>

Obtains file status based on the file descriptor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/87/v3/Wx315IguTvC-WdMTfXDyrQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CCD3C4F08497A6768A521D60F17848C108E5017FDEA86EF574EF7AC34D1359C2)

This API is deprecated since API version 9. Use [fs.stat](../../ohos-file-fs-file-management/document.md#fsstat) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file whose status is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise that returns the detailed file status obtained. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fstat(fd).then((stat: fileio.Stat) => {
  console.info("fstat succeed, the size of file is " + stat.size);
}).catch((err: BusinessError) => {
  console.error("fstat failed with error:" + err);
});

#### fileio.fstat7+

fstat(fd: number, callback: AsyncCallback<Stat>): void

Obtains file status based on the file descriptor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/EkGu9aSUSbmKtrlt5mniWA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B6C54E9C211CB2A8B23B8769CE5D0AF5D2A00BA5AC0C631EE46B2D5772B15445)

This API is deprecated since API version 9. Use [fs.stat](../../ohos-file-fs-file-management/document.md#fsstat-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file whose status is to be obtained. |
| callback | AsyncCallback<[Stat](#stat)\> | Yes | Callback used to return the file status obtained. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fstat(fd, (err: BusinessError) => {
  // Do something.
});

#### fileio.fstatSync7+

fstatSync(fd: number): Stat

Obtains file status based on the file descriptor. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/YBRA6Dr5QnmKeLcLK5-NJQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=61453E75617302D2EE72C7E86F80CEBE0CD2B4D20CE20A4BE655BAE6BB0E52D2)

This API is deprecated since API version 9. Use [fs.statSync](../../ohos-file-fs-file-management/document.md#fsstatsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file whose status is to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stat](#stat) | Detailed file status obtained. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.fstatSync(fd);

#### fileio.ftruncate7+

ftruncate(fd: number, len?: number): Promise<void>

Truncates a file based on the file descriptor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/2lNvuhRfRWKXVKKryk429Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F7A070F4DC316D7A6B6F3F4068FC80B0AD2B1B27F3741CD05C99BB316CBAE32)

This API is deprecated since API version 9. Use [fs.truncate](../../ohos-file-fs-file-management/document.md#fstruncate) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to truncate. |
| len | number | No | File length, in bytes, after truncation. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.ftruncate(fd, 5).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error:" + err);
});

#### fileio.ftruncate7+

ftruncate(fd: number, len?: number, callback: AsyncCallback<void>): void

Truncates a file based on the file descriptor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/MS4ibTvSRYqFzFrePeF6Ag/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2B3208822E9AD7C0DD8EA07C8104949D8D73BED4E2123A0CBDFAFAD240FCA94)

This API is deprecated since API version 9. Use [fs.truncate](../../ohos-file-fs-file-management/document.md#fstruncate-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to truncate. |
| len | number | No | File length, in bytes, after truncation. |
| callback | AsyncCallback<void> | Yes | Callback that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let len = 5;
fileio.ftruncate(fd, 5, (err: BusinessError) => {
  // Do something.
});

#### fileio.ftruncateSync7+

ftruncateSync(fd: number, len?: number): void

Truncates a file based on the file descriptor. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/eRM3IdFSRi6J3N9BnfcXoQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=153871AB53C6CF8687963ACAD7949D38594BD1863A27379DC27DBBAF2A8000DF)

This API is deprecated since API version 9. Use [fs.truncateSync](../../ohos-file-fs-file-management/document.md#fstruncatesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to truncate. |
| len | number | No | File length, in bytes, after truncation. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let len = 5;
fileio.ftruncateSync(fd, len);

#### fileio.truncate7+

truncate(path: string, len?: number): Promise<void>

Truncates a file based on the file path. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/Q74VMqzERyyKtCRNej5JdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EE71E7D034B0EC396469F0BF44B64A31867B50BFDC500CE326AE9403D3E07FF0)

This API is deprecated since API version 9. Use [fs.truncate](../../ohos-file-fs-file-management/document.md#fstruncate) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file to truncate. |
| len | number | No | File length, in bytes, after truncation. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncate(filePath, len).then(() => {
  console.info("truncate file succeed");
}).catch((err: BusinessError) => {
  console.error("truncate file failed with error:" + err);
});

#### fileio.truncate7+

truncate(path: string, len?: number, callback: AsyncCallback<void>): void

Truncates a file based on the file path. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/CJd_ZKS1SqW1O6R61n3O9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1330A18ABF158C981C4AFB30A970C574F2942CA57A1535D3A0A65DE92DDDA9BE)

This API is deprecated since API version 9. Use [fs.truncate](../../ohos-file-fs-file-management/document.md#fstruncate-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file to truncate. |
| len | number | No | File length, in bytes, after truncation. |
| callback | AsyncCallback<void> | Yes | Callback that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncate(filePath, len, (err: BusinessError) => {
  // Do something.
});

#### fileio.truncateSync7+

truncateSync(path: string, len?: number): void

Truncates a file based on the file path. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/KKZKz19PTYengm8JhNI1vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4E9280B1CC0EE5D52F62B2E555A07A6C9077C4CD0BEC2D72AB1F2948C35C90B0)

This API is deprecated since API version 9. Use [fs.truncateSync](../../ohos-file-fs-file-management/document.md#fstruncatesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file to truncate. |
| len | number | No | File length, in bytes, after truncation. |

**Example**

let filePath = pathDir + "/test.txt";
let len = 5;
fileio.truncateSync(filePath, len);

#### fileio.readText7+

readText(filePath: string, options?: { position?: number; length?: number; encoding?: string; }): Promise<string>

Reads the text content of a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a3/v3/UociouzlQI25f56SSop21w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBCF8315C73924C15B385F80B78F138C82BAEDFD68E007E14B7A09A515A4571B)

This API is deprecated since API version 9. Use [fs.readText](../../ohos-file-fs-file-management/document.md#fsreadtext) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file to read. |
| options | Object | No | 
The options are as follows:

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **encoding** (string): format of the data to be encoded.

It is valid only when the data is of the string type.

The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise that returns the file content read. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.readText(filePath).then((str: string) => {
  console.info("readText succeed:" + str);
}).catch((err: BusinessError) => {
  console.error("readText failed with error:" + err);
});

#### fileio.readText7+

readText(filePath: string, options: { position?: number; length?: number; encoding?: string; }, callback: AsyncCallback<string>): void

Reads the text content of a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7a/v3/ENjfqJiXRXuE4gIfMmV82w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6C60E84F277792F086359AFBBE2902B2C668A6B7F050FC45D6CC50DF5153D33A)

This API is deprecated since API version 9. Use [fs.readText](../../ohos-file-fs-file-management/document.md#fsreadtext-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file to read. |
| options | Object | No | 
The options are as follows:

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **encoding**: format of the data to be encoded. The default value is **'utf-8'**, which is the only value supported.

 |
| callback | AsyncCallback<string> | Yes | Callback used to return the file content read. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
class Option {
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.position = 1;
option.encoding = 'utf-8';
fileio.readText(filePath, option, (err: BusinessError, str: string) => {
  // Do something.
});

#### fileio.readTextSync7+

readTextSync(filePath: string, options?: { position?: number; length?: number; encoding?: string; }): string

Reads the text content of a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/da/v3/YjUdBBHCS5S5W-srknMteA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A1D8C261F9D1EF2603303D99AF37D4DA72A5CC25288869A356312FE15BA95A6F)

This API is deprecated since API version 9. Use [fs.readTextSync](../../ohos-file-fs-file-management/document.md#fsreadtextsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Application sandbox path of the file to read. |
| options | Object | No | 
The options are as follows:

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **encoding** (string): format of the data to be encoded.

It is valid only when the data is of the string type.

The default value is **'utf-8'**, which is the only value supported.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | File content read. |

**Example**

let filePath = pathDir + "/test.txt";
class Option {
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.position = 1;
option.length = 3;
let str = fileio.readTextSync(filePath, option);

#### fileio.lstat7+

lstat(path: string): Promise<Stat>

Obtains information about a symbolic link that is used to refer to a file or directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/k3BxCeEGQye_ajVt0GWrJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2A188D2BC3F05664B8B55E9564E8D765A499955D317D62B30AE09F7C8F5224B)

This API is deprecated since API version 9. Use [fs.lstat](../../ohos-file-fs-file-management/document.md#fslstat) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the target file. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stat](#stat)\> | Promise that returns the symbolic link information obtained. For details, see **stat**. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.lstat(filePath).then((stat: fileio.Stat) => {
  console.info("get link status succeed, the size of file is" + stat.size);
}).catch((err: BusinessError) => {
  console.error("get link status failed with error:" + err);
});

#### fileio.lstat7+

lstat(path: string, callback: AsyncCallback<Stat>): void

Obtains information about a symbolic link that is used to refer to a file or directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/ARLtInSuQtewU_29IIcsGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E6C47D143476FD89805F0D396887F2D1303840595E21B7726546252481514C3)

This API is deprecated since API version 9. Use [fs.lstat](../../ohos-file-fs-file-management/document.md#fslstat-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the target file. |
| callback | AsyncCallback<[Stat](#stat)\> | Yes | Callback used to return the symbolic link information obtained. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.lstat(filePath, (err: BusinessError, stat: fileio.Stat) => {
  // Do something.
});

#### fileio.lstatSync7+

lstatSync(path: string): Stat

Obtains information about a symbolic link that is used to refer to a file or directory. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b8/v3/90VvUnXBSgir1r7WuCiplw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B81A37E703942DDE79D336C2789A659A08873D856AE78AC77A33E73EED493889)

This API is deprecated since API version 9. Use [fs.lstatSync](../../ohos-file-fs-file-management/document.md#fslstatsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the target file. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stat](#stat) | File information obtained. |

**Example**

let filePath = pathDir + "/test.txt";
let stat = fileio.lstatSync(filePath);

#### fileio.rename7+

rename(oldPath: string, newPath: string): Promise<void>

Renames a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/mcZwik29QoKvrtaPIU1-SA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=344DC772DF45661B36217FA220623436D871244F245F757012D8FCE377EFC617)

This API is deprecated since API version 9. Use [fs.rename](../../ohos-file-fs-file-management/document.md#fsrename) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oldPath | string | Yes | Application sandbox path of the file to rename. |
| newPath | string | Yes | Application sandbox path of the file renamed. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.rename(srcFile, dstFile).then(() => {
  console.info("rename succeed");
}).catch((err: BusinessError) => {
  console.error("rename failed with error:" + err);
});

#### fileio.rename7+

rename(oldPath: string, newPath: string, callback: AsyncCallback<void>): void

Renames a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/7scI6icpRwGPqrJ1zZ21Uw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7BD1DA3D56F6F5D138CA7C083F5B9D5E0BA92E84105E430542EE66853990E576)

This API is deprecated since API version 9. Use [fs.rename](../../ohos-file-fs-file-management/document.md#fsrename-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oldPath | string | Yes | Application sandbox path of the file to rename. |
| newPath | string | Yes | Application sandbox path of the file renamed. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file is asynchronously renamed. |

**Example**

import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.rename(srcFile, dstFile, (err: BusinessError) => {
});

#### fileio.renameSync7+

renameSync(oldPath: string, newPath: string): void

Renames a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/oFVQc1dHSUGPCt7vumyv_g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=471C7196B2F66769D1F6942F42DC4B7DC14A0C2662B3357115FF10FF21701EFE)

This API is deprecated since API version 9. Use [fs.renameSync](../../ohos-file-fs-file-management/document.md#fsrenamesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| oldPath | string | Yes | Application sandbox path of the file to rename. |
| newPath | string | Yes | Application sandbox path of the file renamed. |

**Example**

let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/new.txt';
fileio.renameSync(srcFile, dstFile);

#### fileio.fsync7+

fsync(fd: number): Promise<void>

Synchronizes a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/Fu69BpSBR36EQ6QzqDONwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=946BD92098915AD9F1BAAC4B8D6DECD491CF7D8087B6AB4B7A44C9F7E2C4972C)

This API is deprecated since API version 9. Use [fs.fsync](../../ohos-file-fs-file-management/document.md#fsfsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to synchronize. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsync(fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error:" + err);
});

#### fileio.fsync7+

fsync(fd: number, callback: AsyncCallback<void>): void

Synchronizes a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/iByYjI3eQ-e-68xxrPA64Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5DB0281294F2A4E699166B1B282BFF02C763D49996C09DAF39CF2D0810DA75BD)

This API is deprecated since API version 9. Use [fs.fsync](../../ohos-file-fs-file-management/document.md#fsfsync-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to synchronize. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file is synchronized in asynchronous mode. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsync(fd, (err: BusinessError) => {
  // Do something.
});

#### fileio.fsyncSync7+

fsyncSync(fd: number): void

Synchronizes a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/4sC6lyJ-RmKoufVMF9_Y8A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2F1478C7C4217271AC1BE76D8B109E62247C36CF7D475FE473FC086D8DCFB608)

This API is deprecated since API version 9. Use [fs.fsyncSync](../../ohos-file-fs-file-management/document.md#fsfsyncsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to synchronize. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fsyncSync(fd);

#### fileio.fdatasync7+

fdatasync(fd: number): Promise<void>

Synchronizes the data of a file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/R1ml56YNT7G4693qXfcjWQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B2FBFB771D60A2FD99DB9EDFE06A687FAC77BFD1987FF078962540132DA568C6)

This API is deprecated since API version 9. Use [fs.fdatasync](../../ohos-file-fs-file-management/document.md#fsfdatasync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to synchronize. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdatasync(fd).then(() => {
  console.info("sync data succeed");
}).catch((err: BusinessError) => {
  console.error("sync data failed with error:" + err);
});

#### fileio.fdatasync7+

fdatasync(fd: number, callback: AsyncCallback<void>): void

Synchronizes the data of a file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5b/v3/acsHy5KXS4ibQ1rfLfNyIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B5DBDECA87CAE4F286F9C7F8E64B6DF980F5EDE766177F308432749F3BA8D001)

This API is deprecated since API version 9. Use [fs.fdatasync](../../ohos-file-fs-file-management/document.md#fsfdatasync-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to synchronize. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file data is synchronized in asynchronous mode. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdatasync (fd, (err: BusinessError) => {
  // Do something.
});

#### fileio.fdatasyncSync7+

fdatasyncSync(fd: number): void

Synchronizes the data of a file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c3/v3/LA1IetzpT8mRqTHvwA-4Qw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FFB107334503A099DB77637D7CB427A833D845AE7D4C5F17B47154ACC85BF373)

This API is deprecated since API version 9. Use [fs.fdatasyncSync](../../ohos-file-fs-file-management/document.md#fsfdatasyncsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the file to synchronize. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.fdatasyncSync(fd);

#### fileio.symlink7+

symlink(target: string, srcPath: string): Promise<void>

Creates a symbolic link based on the file path. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/cH9I7u0sRWWzSlTBOAAO7Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACA0420E9B573A839F9411FF02D4A4F161C77E53BD3A3701BC9844B270A4A319)

This API is deprecated since API version 9. Use [fs.symlink](../../ohos-file-fs-file-management/document.md#fssymlink) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | string | Yes | Application sandbox path of the target file. |
| srcPath | string | Yes | Application sandbox path of the symbolic link. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlink(srcFile, dstFile).then(() => {
  console.info("symlink succeed");
}).catch((err: BusinessError) => {
  console.error("symlink failed with error:" + err);
});

#### fileio.symlink7+

symlink(target: string, srcPath: string, callback: AsyncCallback<void>): void

Creates a symbolic link based on the file path. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/obbiiBFbRz6x5IDWQrH5vA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A3E865CE1C2A4D125E640D72E71F9B713E4158EAA9A9DBA438115EE31ECBABB)

This API is deprecated since API version 9. Use [fs.symlink](../../ohos-file-fs-file-management/document.md#fssymlink-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | string | Yes | Application sandbox path of the target file. |
| srcPath | string | Yes | Application sandbox path of the symbolic link. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the symbolic link is created asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlink(srcFile, dstFile, (err: BusinessError) => {
  // Do something.
});

#### fileio.symlinkSync7+

symlinkSync(target: string, srcPath: string): void

Creates a symbolic link based on the file path. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/sTrf0FtqSgeLi3JeEP9GLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0994D4922C009136F30AAAE7DBA7BC4F9FA64AD8141262AEF0F6B70B85060D6F)

This API is deprecated since API version 9. Use [fs.symlinkSync](../../ohos-file-fs-file-management/document.md#fssymlinksync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| target | string | Yes | Application sandbox path of the target file. |
| srcPath | string | Yes | Application sandbox path of the symbolic link. |

**Example**

let srcFile = pathDir + "/test.txt";
let dstFile = pathDir + '/test';
fileio.symlinkSync(srcFile, dstFile);

#### fileio.chown7+

chown(path: string, uid: number, gid: number): Promise<void>

Changes the file owner based on the file path. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/MFANHuDbSHGIlhAcP_pmrA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4416BD5A279BB73458002DEA79F8F4913B9EC5803E440180D9F0D38528C5B0B)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| uid | number | Yes | New user ID (UID). |
| gid | number | Yes | New group ID (GID). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.chown(filePath, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});

#### fileio.chown7+

chown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void

Changes the file owner based on the file path. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/uIwugc4pS-SSMrxdPRqBEw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=955433B8F7D786CD9B5EA0A614540E49DE476D831D5D2FDC4850388AE9A91AB1)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file owner is changed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath)
fileio.chown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
  // Do something.
});

#### fileio.chownSync7+

chownSync(path: string, uid: number, gid: number): void

Changes the file owner based on its path. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/Nuh7t252Q4yhyjEP0Ux_CQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7E67C4C8057A6C8AF554D8569BFBF9DA30C85E20186EED84B60F05ED8FEC0ED4)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |

**Example**

let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath)
fileio.chownSync(filePath, stat.uid, stat.gid);

#### fileio.mkdtemp7+

mkdtemp(prefix: string): Promise<string>

Creates a temporary directory. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ee/v3/YSo9AIeWR3KAvFxCsT0Jdg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0198FED2399FE69A5A1320C193BA5AFD38778F3AD8FEEA881156D61AA369EA31)

This API is deprecated since API version 9. Use [fs.mkdtemp](../../ohos-file-fs-file-management/document.md#fsmkdtemp) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<string> | Promise that returns the directory created. |

**Example**

import { BusinessError } from '@ohos.base';
fileio.mkdtemp(pathDir + "/XXXXXX").then((pathDir: string) => {
  console.info("mkdtemp succeed:" + pathDir);
}).catch((err: BusinessError) => {
  console.error("mkdtemp failed with error:" + err);
});

#### fileio.mkdtemp7+

mkdtemp(prefix: string, callback: AsyncCallback<string>): void

Creates a temporary directory. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/vhZ6C17vSky0wJ0HHUEjTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E6365D760877A1D5844F095E1950A80899185CB48E215D553D7E30EFD00BD7CF)

This API is deprecated since API version 9. Use [fs.mkdtemp](../../ohos-file-fs-file-management/document.md#fsmkdtemp-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |
| callback | AsyncCallback<string> | Yes | Callback invoked when a temporary directory is created asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
fileio.mkdtemp(pathDir + "/XXXXXX", (err: BusinessError, res: string) => {
  // Do something.
});

#### fileio.mkdtempSync7+

mkdtempSync(prefix: string): string

Creates a temporary directory. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/lvlU7jAqRkWhaYthuB2PsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABBD43287574D94C3858DDC4E69521100A01F44099D833B3F604A60C185FA977)

This API is deprecated since API version 9. Use [fs.mkdtempSync](../../ohos-file-fs-file-management/document.md#fsmkdtempsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| prefix | string | Yes | String to be replaced with six randomly generated characters to create a unique temporary directory. |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Unique directory generated. |

**Example**

let res = fileio.mkdtempSync(pathDir + "/XXXXXX");

#### fileio.fchmod7+

fchmod(fd: number, mode: number): Promise<void>

Changes file permissions based on the file descriptor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b6/v3/hJAfVeXNRMuW3LaqeLQ3Lg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42758B5189DB245A90912A2EBE26C2FB5E7151B68947D2A8407A19408EB27B9F)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| mode | number | Yes | 
Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|).

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmod(fd, mode).then(() => {
  console.info("chmod succeed");
}).catch((err: BusinessError) => {
  console.error("chmod failed with error:" + err);
});

#### fileio.fchmod7+

fchmod(fd: number, mode: number, callback: AsyncCallback<void>): void

Changes file permissions based on the file descriptor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/Shw1s6txTPiiDw6vpQBzMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3F98701D7DD34870663D1B1847A011C9BA175F2504D2FE6CCAB764B80B945B12)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| mode | number | Yes | 
Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|).

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file permissions are changed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmod(fd, mode, (err: BusinessError) => {
  // Do something.
});

#### fileio.fchmodSync7+

fchmodSync(fd: number, mode: number): void

Changes the file permissions based on the file descriptor. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8b/v3/cg7oK6iKTIGnr5LG7IdT1w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9E104CB0A7A20689A57E36558CBA41B161B24E54EBE4EA234D092DABC4527F2C)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| mode | number | Yes | 
Permissions on the file. You can specify multiple permissions, separated using a bitwise OR operator (|).

\- **0o700**: The owner has the read, write, and execute permissions.

\- **0o400**: The owner has the read permission.

\- **0o200**: The owner has the write permission.

\- **0o100**: The owner has the execute permission.

\- **0o070**: The user group has the read, write, and execute permissions.

\- **0o040**: The user group has the read permission.

\- **0o020**: The user group has the write permission.

\- **0o010**: The user group has the execute permission.

\- **0o007**: Other users have the read, write, and execute permissions.

\- **0o004**: Other users have the read permission.

\- **0o002**: Other users have the write permission.

\- **0o001**: Other users have the execute permission.

 |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let mode: number = 0o700;
fileio.fchmodSync(fd, mode);

#### fileio.createStream7+

createStream(path: string, mode: string): Promise<Stream>

Creates a stream based on the file path. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/gFgIQibZRqeOZ6Vz0xLPmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E850FECDBD64C49B15DEAD3DDAFCD591E56916525DF633EBC4C263156B96D129)

This API is deprecated since API version 9. Use [fs.createStream](../../ohos-file-fs-file-management/document.md#fscreatestream) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stream](#stream)\> | Promise that returns the stream opened. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.createStream(filePath, "r+").then((stream: fileio.Stream) => {
  console.info("createStream succeed");
}).catch((err: BusinessError) => {
  console.error("createStream failed with error:" + err);
});

#### fileio.createStream7+

createStream(path: string, mode: string, callback: AsyncCallback<Stream>): void

Creates a stream based on the file path. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/XUPif5-NSoe3_OUd-XkI7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=68FEDAAFD6FB85E74776E65941E3934214C137994D928BEA025C8ED23ED68956)

This API is deprecated since API version 9. Use [fs.createStream](../../ohos-file-fs-file-management/document.md#fscreatestream-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |
| callback | AsyncCallback<[Stream](#stream)\> | Yes | Callback invoked when the stream is opened asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
fileio.createStream(filePath, "r+", (err: BusinessError, stream: fileio.Stream) => {
  // Do something.
});

#### fileio.createStreamSync7+

createStreamSync(path: string, mode: string): Stream

Creates a stream based on the file path. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d5/v3/IxQKLJuATE2i30-OpmZhgw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B7281CCD1CD9B0DDD164FB9F7C68984B1AA31395711AD01A65688B411034C79)

This API is deprecated since API version 9. Use [fs.createStreamSync](../../ohos-file-fs-file-management/document.md#fscreatestreamsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stream](#stream) | Stream opened. |

**Example**

let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");

#### fileio.fdopenStream7+

fdopenStream(fd: number, mode: string): Promise<Stream>

Opens a stream based on the file descriptor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/5SOOY-kLTCWpfJGEuBZqZQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F4C05698D29BDC438CCA969EFE7BF2F9714802D46D610799500C926CEDBDA01)

This API is deprecated since API version 9. Use [fs.fdopenStream](../../ohos-file-fs-file-management/document.md#fsfdopenstream) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Stream](#stream)\> | Promise that returns the stream opened. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdopenStream(fd, "r+").then((stream: fileio.Stream) => {
  console.info("openStream succeed");
}).catch((err: BusinessError) => {
  console.error("openStream failed with error:" + err);
});

#### fileio.fdopenStream7+

fdopenStream(fd: number, mode: string, callback: AsyncCallback<Stream>): void

Opens a stream based on the file descriptor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e9/v3/YuOXquirTRql1EyCSS79Ig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89A235EAC188FCEE6841319CC0417BB3FB7C71B36A2013EECD037200EC1E023D)

This API is deprecated since API version 9. Use [fs.fdopenStream](../../ohos-file-fs-file-management/document.md#fsfdopenstream-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |
| callback | AsyncCallback<[Stream](#stream)\> | Yes | Callback invoked when the stream is opened asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
fileio.fdopenStream(fd, "r+", (err: BusinessError, stream: fileio.Stream) => {
  // Do something.
});

#### fileio.fdopenStreamSync7+

fdopenStreamSync(fd: number, mode: string): Stream

Opens a stream based on the file descriptor. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/hSZEQfx7T_iXmNWsytJ5Lw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F14FC793270DB3E75A2D91D51FADCDBBE81BCA5CF54CC48FE5C8FC4D5B0ACE1E)

This API is deprecated since API version 9. Use [fs.fdopenStreamSync](../../ohos-file-fs-file-management/document.md#fsfdopenstreamsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| mode | string | Yes | 
\- **r**: Open a file for reading. The file must exist.

\- **r+**: Open a file for both reading and writing. The file must exist.

\- **w**: Open a file for writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **w+**: Open a file for both reading and writing. If the file exists, clear its content. If the file does not exist, create a file.

\- **a**: Open a file in append mode for writing at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

\- **a+**: Open a file in append mode for reading or updating at the end of the file. If the file does not exist, create a file. If the file exists, write data to the end of the file (the original content of the file is reserved).

 |

**Return value**

| Type | Description |
| :-- | :-- |
| [Stream](#stream) | Stream opened. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let ss = fileio.fdopenStreamSync(fd, "r+");

#### fileio.fchown7+

fchown(fd: number, uid: number, gid: number): Promise<void>

Changes the file owner based on the file descriptor. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/RHRsLvlpQ1qtwqvkjQ4Flw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=28620E6183CD8B4217AD6459C2D3AA8F09BF7F1529D5E569761CA3978FA7736A)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchown(fd, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});

#### fileio.fchown7+

fchown(fd: number, uid: number, gid: number, callback: AsyncCallback<void>): void

Changes the file owner based on the file descriptor. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/uQiCeozTQg6HugJ0eajj8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DAE44782666DEC755F1D8EFE6514035FCA7D0DA4DF1578B5E1C4D25CA504275A)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file owner is changed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchown(fd, stat.uid, stat.gid, (err: BusinessError) => {
  // Do something.
});

#### fileio.fchownSync7+

fchownSync(fd: number, uid: number, gid: number): void

Changes the file owner based on the file descriptor. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/mn3d1tNyR6KhNwVhddInfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B21C3195E1487E8EA7A4F10B01F73A0F4F28985E4C073451982DC90DA87C1AB)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| fd | number | Yes | File descriptor of the target file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |

**Example**

let filePath = pathDir + "/test.txt";
let fd = fileio.openSync(filePath);
let stat = fileio.statSync(filePath);
fileio.fchownSync(fd, stat.uid, stat.gid);

#### fileio.lchown7+

lchown(path: string, uid: number, gid: number): Promise<void>

Changes the file owner (owner of the symbolic link, not the file referred to by the symbolic link) based on the file path. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a0/v3/AUPdtU7eStKwuELX3GH1NQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FD9F699A23458D12603395DA17EC7BF22AC0FA904B8D8CE122743D5BAA3D3C37)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchown(filePath, stat.uid, stat.gid).then(() => {
  console.info("chown succeed");
}).catch((err: BusinessError) => {
  console.error("chown failed with error:" + err);
});

#### fileio.lchown7+

lchown(path: string, uid: number, gid: number, callback: AsyncCallback<void>): void

Changes the file owner (owner of the symbolic link, not the file referred to by the symbolic link) based on a file path. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/Fo6jFiaqTVGrfExKOp7r-g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=467B24BEB2BA3654924510519D078D61B7B1885D4D800AC11102BCDC7910F22E)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file owner is changed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchown(filePath, stat.uid, stat.gid, (err: BusinessError) => {
  // Do something.
});

#### fileio.lchownSync7+

lchownSync(path: string, uid: number, gid: number): void

Changes the file owner based on a file path and changes the owner of the symbolic link (not the referenced file). This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/4CxO_h-YTWWh8UNRG3V_QQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=54B5D4EBD519D657DB5FAB3C4D27BE84C19B0737E5D70F7CC05D26AB513AD06A)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| path | string | Yes | Application sandbox path of the file. |
| uid | number | Yes | New UID. |
| gid | number | Yes | New GID. |

**Example**

let filePath = pathDir + "/test.txt";
let stat = fileio.statSync(filePath);
fileio.lchownSync(filePath, stat.uid, stat.gid);

#### fileio.createWatcher7+

createWatcher(filename: string, events: number, callback: AsyncCallback<number>): Watcher

Listens for file or directory changes. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/OJSoSoZuQ8aC-EXwQtOQ8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F6AB92155738F3193A1753E54BC057DB1603DE987DE642C022BD768EC4F4ACF7)

This API is deprecated since API version 10.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filename | string | Yes | Application sandbox path of the file. |
| events | number | Yes | 
\- **1**: The file or directory is renamed.

\- **2**: The file or directory is modified.

\- **3**: The file or directory is modified and renamed.

 |
| callback | AsyncCallback<number> | Yes | Called each time a change is detected. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Watcher](#watcher7) | Promise that returns the file change. |

**Example**

let filePath = pathDir + "/test.txt";
fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});

#### Readout

Obtains the file read result. This class applies only to the **read()** method.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/RzI4N2hHQnSDVdxLsILBKA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=742B0F2B3408D05B49949FB6B4BE85910D536438112D3F7D190887C466124593)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

| Name | Type | Read-Only | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| bytesRead | number | Yes | Yes | Length of the data read. |
| offset | number | Yes | Yes | Position of the buffer to which the data to be read in reference to the start address of the buffer. |
| buffer | ArrayBuffer | Yes | Yes | Buffer for storing the data read. |

#### Stat

Provides detailed file information. Before calling a method of the **Stat** class, use the [stat()](#fileiostat) method synchronously or asynchronously to create a **Stat** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/Lx7Wyo9tRbqiJQsOmhNBUw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=05C35CF56501C48CF1C5F3951EF86B01B7854CDDAA62F0778210C448709D94E3)

This API is deprecated since API version 9. Use [fs.stat](../../ohos-file-fs-file-management/document.md#stat) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

## Properties

| Name | Type | Read-Only | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| dev | number | Yes | No | Major device number. |
| ino | number | Yes | No | File identifier, which varies with files on the same device. |
| mode | number | Yes | No | 
File type and permissions. The first four bits indicate the file type, and the last 12 bits indicate the permissions. The bit fields are described as follows:

\- **0o170000**: mask used to obtain the file type.

\- **0o140000**: The file is a socket.

\- **0o120000**: The file is a symbolic link.

\- **0o100000**: The file is a regular file.

\- **0o060000**: The file is a block device.

\- **0o040000**: The file is a directory.

\- **0o020000**: The file is a character device.

\- **0o010000**: The file is a named pipe (FIFO).

\- **0o0700**: mask used to obtain the owner permissions.

\- **0o0400**: The owner has the permission to read a regular file or a directory entry.

\- **0o0200**: The owner has the permission to write a regular file or create and delete a directory entry.

\- **0o0100**: The owner has the permission to execute a regular file or search for the specified path in a directory.

\- **0o0070**: mask used to obtain the user group permissions.

\- **0o0040**: The user group has the permission to read a regular file or a directory entry.

\- **0o0020**: The user group has the permission to write a regular file or create and delete a directory entry.

\- **0o0010**: The user group has the permission to execute a regular file or search for the specified path in a directory.

\- **0o0007**: mask used to obtain the permissions of other users.

\- **0o0004**: Other users have the permission to read a regular file or a directory entry.

\- **0o0002**: Other users have the permission to write a regular file or create and delete a directory entry.

\- **0o0001**: Other users have the permission to execute a regular file or search for the specified path in a directory.

 |
| nlink | number | Yes | No | Number of hard links in the file. |
| uid | number | Yes | No | ID of the file owner. |
| gid | number | Yes | No | ID of the user group of the file. |
| rdev | number | Yes | No | Minor device number. |
| size | number | Yes | No | File size, in bytes. This parameter is valid only for regular files. |
| blocks | number | Yes | No | Number of blocks occupied by a file. Each block is 512 bytes. |
| atime | number | Yes | No | Time when the file was last accessed. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970. |
| mtime | number | Yes | No | Time when the file content was last modified. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970. |
| ctime | number | Yes | No | Time of the last status change of the file. The value is the number of seconds elapsed since 00:00:00 on January 1, 1970. |

#### \[h2\]isBlockDevice

isBlockDevice(): boolean

Checks whether this file is a block special file. A block special file supports access by block only, and it is cached when accessed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/58/v3/1_jUld0bR-2VvQiBXM94_Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D6C2D964D22B9325EFB6A4C43072690739D33C60143485200B9A3C1A0F70787)

This API is deprecated since API version 9. Use [fs.Stat.isBlockDevice](../../ohos-file-fs-file-management/document.md#isblockdevice) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a block special file; returns **false** otherwise. |

**Example**

let filePath = pathDir + "/test.txt";
let isBLockDevice = fileio.statSync(filePath).isBlockDevice();

#### \[h2\]isCharacterDevice

isCharacterDevice(): boolean

Checks whether this file is a character special file. A character special file supports random access, and it is not cached when accessed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/Dt7hsp_ESue_1LFvoxuNuQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04CDFB203967F573DAE33B5017E97A418041BF415D2A8079CE6F5CAE6C5CFAA9)

This API is deprecated since API version 9. Use [fs.Stat.isCharacterDevice](../../ohos-file-fs-file-management/document.md#ischaracterdevice) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a character special file; returns **false** otherwise. |

**Example**

let filePath = pathDir + "/test.txt";
let isCharacterDevice = fileio.statSync(filePath).isCharacterDevice();

#### \[h2\]isDirectory

isDirectory(): boolean

Checks whether this file is a directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/8e-KgVQbQDeXaEVinONdaA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B8AB4A82DE5140FF20083C1548E4705DA5BFC4231749E5966554F23FD6F2FEA)

This API is deprecated since API version 9. Use [fs.Stat.isDirectory](../../ohos-file-fs-file-management/document.md#isdirectory) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a directory; returns **false** otherwise. |

**Example**

let dirPath = pathDir + "/test";
let isDirectory = fileio.statSync(dirPath).isDirectory();

#### \[h2\]isFIFO

isFIFO(): boolean

Checks whether this file is a named pipe (or FIFO). Named pipes are used for inter-process communication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/a5r1GxKITVytknBRz5h1Bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C65CCD7BBFD7AF94E3390F2747E98896EC32E8CEB35F4462C708197E45258297)

This API is deprecated since API version 9. Use [fs.Stat.isFIFO](../../ohos-file-fs-file-management/document.md#isfifo) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a named pipe; returns **false** otherwise. |

**Example**

let filePath = pathDir + "/test.txt";
let isFIFO = fileio.statSync(filePath).isFIFO();

#### \[h2\]isFile

isFile(): boolean

Checks whether this file is a regular file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/fAMmwGR2QCiPHBuIZOG0Mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E83A649ACFEA091F9D09A4C94B8A379050C3015C13485FF7A213432F81A1C06)

This API is deprecated since API version 9. Use [fs.Stat.isFile](../../ohos-file-fs-file-management/document.md#isfile) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a regular file; returns **false** otherwise. |

**Example**

let filePath = pathDir + "/test.txt";
let isFile = fileio.statSync(filePath).isFile();

#### \[h2\]isSocket

isSocket(): boolean

Checks whether this file is a socket.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4f/v3/IgmNcC60S4axAjnJOe9nYg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0D3F98A746B86774659B280E59D71F9A2F03F7DBBB71818E9168D241BC02493E)

This API is deprecated since API version 9. Use [fs.Stat.isSocket](../../ohos-file-fs-file-management/document.md#issocket) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a socket; returns **false** otherwise. |

**Example**

let filePath = pathDir + "/test.txt";
let isSocket = fileio.statSync(filePath).isSocket();

#### \[h2\]isSymbolicLink

isSymbolicLink(): boolean

Checks whether this file is a symbolic link.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/05/v3/4TSc6gocQcal1tXzcfb9sg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1F22CDF60EED24480B9A61CF8DBF088F94EC325007BF645DF2E6554F2E17D642)

This API is deprecated since API version 9. Use [fs.Stat.isSymbolicLink](../../ohos-file-fs-file-management/document.md#issymboliclink) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a symbolic link; returns **false** otherwise. |

**Example**

let filePath = pathDir + "/test";
let isSymbolicLink = fileio.statSync(filePath).isSymbolicLink();

#### Watcher7+

Listens for file change. You can call the **Watcher.stop()** method synchronously or asynchronously to stop the listening.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9/v3/_M5oehrNRrOx7SgFytkZsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=77A871E66C4BF81C94F1D1BFE49312F78B4F9E445E04BAF9F083F21D20060D5A)

This API is deprecated since API version 10.

#### \[h2\]stop7+

stop(): Promise<void>

Stops the **watcher** instance. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/SwQwKhcfRGCar8duwad6Fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9D60D41B502BF54D4C48A1B2A6BDD85FE5B0361C908B512AB9F09320E1034B67)

This API is deprecated since API version 10.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Example**

let filePath = pathDir + "/test.txt";
let watcher = fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});
watcher.stop().then(() => {
  console.info("close watcher succeed");
});

#### \[h2\]stop7+

stop(callback: AsyncCallback<void>): void

Stops the **watcher** instance. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/VzIwJNEzRzSyBfChzdKgjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF5E97C7726C09A0A17AD365749DB5CAAFA843171CCF5A0840A3551D404FEB79)

This API is deprecated since API version 10.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback invoked when **watcher** is stopped asynchronously. |

**Example**

let filePath = pathDir + "/test.txt";
let watcher = fileio.createWatcher(filePath, 1, (err: BusinessError, event: number) => {
  console.info("event: " + event + "errmsg: " + JSON.stringify(err));
});
watcher.stop(() => {
  console.info("close watcher succeed");
})

#### Stream

Provides a stream for file operations. Before calling any API of the **Stream** class, use **createStream()** to create a **Stream** instance synchronously or asynchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/Pkmow56XQJWIKEj64gz7QA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E4CF2D8BAA41924DF182527EC3B1F67C8428790ACFF959F6306F1EE833999E91)

This API is deprecated since API version 9. Use [fs.Stream](../../ohos-file-fs-file-management/document.md#stream) instead.

#### \[h2\]close7+

close(): Promise<void>

Closes the file stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/uiQ8vH5uSdWcKyAP1dwwPA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3D168E4179CA792199997E67DB9B9AD7B22ABA6A9E4A3E092F6E8C81E2C1FBC8)

This API is deprecated since API version 9. Use [fs.Stream.close](../../ohos-file-fs-file-management/document.md#close) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns the file stream closed. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close().then(() => {
  console.info("close fileStream succeed");
}).catch((err: BusinessError) => {
  console.error("close fileStream  failed with error:" + err);
});

#### \[h2\]close7+

close(callback: AsyncCallback<void>): void

Closes the file stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c5/v3/l6SzMoHIQ_mSz56ziNnS3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B77D1331EA4C5F6359512B4534C4639B4AB1554965EE4E354585356FD23A61BE)

This API is deprecated since API version 9. Use [fs.Stream.close](../../ohos-file-fs-file-management/document.md#close-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file stream is closed asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.close((err: BusinessError) => {
  // Do something.
});

#### \[h2\]closeSync

closeSync(): void

Closes the file stream. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/66/v3/iHurL5YRQOiSNP9vRDt3QA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D00B84B82D03ABAFF31D3264A569A1DFF0A305C5D9B68E24E2496E9A30024F2C)

This API is deprecated since API version 9. Use [fs.Stream.closeSync](../../ohos-file-fs-file-management/document.md#closesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Example**

let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.closeSync();

#### \[h2\]flush7+

flush(): Promise<void>

Flushes the file stream. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/64/v3/8zYdqud3Ta66N-4gFBa8oA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=26D920C0284BD27C0AE739AA77027CFCCBB72134D74AD8BC368E1EE66A8CB5C6)

This API is deprecated since API version 9. Use [fs.Stream.flush](../../ohos-file-fs-file-management/document.md#flush) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns the file stream flushed. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flush().then(() => {
  console.info("flush succeed");
}).catch((err: BusinessError) => {
  console.error("flush failed with error:" + err);
});

#### \[h2\]flush7+

flush(callback: AsyncCallback<void>): void

Flushes the file stream. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8/v3/73K7ijPaQtO0JhRH9uBMbQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E335469BFAF6808268E0216F1FE8007B9E7C4441D9E36D4156032E02F58C4703)

This API is deprecated since API version 9. Use [fs.Stream.flush](../../ohos-file-fs-file-management/document.md#flush-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback invoked when the file stream is asynchronously flushed. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flush((err: BusinessError) => {
  // Do something.
});

#### \[h2\]flushSync7+

flushSync(): void

Flushes the file stream. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ad/v3/YBkNhMUYQICdb1mO6_jmEg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C056C64DE1834D11B01A9F57E46301C4C258EEA58CE5D3D7828455E836F31C0C)

This API is deprecated since API version 9. Use [fs.Stream.flushSync](../../ohos-file-fs-file-management/document.md#flushsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Example**

let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
ss.flushSync();

#### \[h2\]write7+

write(buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): Promise<number>

Writes data to a stream file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f1/v3/BOlG8IKiQTivUAH9DdIJ5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=667F703F83AA372BF8A8871D97976AC0020821390BCE3C3FAF607FCE52BB1CFF)

This API is deprecated since API version 9. Use [fs.Stream.write](../../ohos-file-fs-file-management/document.md#write) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer|string | Yes | Data to write. It can be a string or data from a buffer. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position of the data to write in reference to the start address of the data. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

Constraints: offset + length <= Buffer size

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<number> | Promise that returns the length of the data written. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.write("hello, world", option).then((number: number) => {
  console.info("write succeed and size is:" + number);
}).catch((err: BusinessError) => {
  console.error("write failed with error:" + err);
});

#### \[h2\]write7+

write(buffer: ArrayBuffer|string, options: { offset?: number; length?: number; position?: number; encoding?: string; }, callback: AsyncCallback<number>): void

Writes data to a stream file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cc/v3/BAVVvybtTKm538-H7reThw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=413C205BDA84E98A412836695629291281714062625E13A4E4C395482FFA9170)

This API is deprecated since API version 9. Use [fs.Stream.write](../../ohos-file-fs-file-management/document.md#write-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer|string | Yes | Data to write. It can be a string or data from a buffer. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position of the data to write in reference to the start address of the data. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

Constraints: offset + length <= Buffer size

 |
| callback | AsyncCallback<number> | Yes | Callback invoked when the data is written asynchronously. |

**Example**

import { BusinessError } from '@ohos.base';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.write("hello, world", option, (err: BusinessError, bytesWritten: number) => {
  if (bytesWritten) {
    // Do something.
    console.info("write succeed and size is:" + bytesWritten);
  }
});

#### \[h2\]writeSync7+

writeSync(buffer: ArrayBuffer|string, options?: { offset?: number; length?: number; position?: number; encoding?: string; }): number

Writes data to a stream file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/WW9nyKHtSAucMFlNFPKgVg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04BFB9E3BEEABDB9C9CFF514BD90309B96DC7C273A2FCDE088999DE97B40BAB1)

This API is deprecated since API version 9. Use [fs.Stream.writeSync](../../ohos-file-fs-file-management/document.md#writesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer|string | Yes | Data to write. It can be a string or data from a buffer. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position of the data to write in reference to the start address of the data. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to write. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): start position to write the data in the file. This parameter is optional. By default, data is written from the current position.

\- **encoding** (string): format of the data to be encoded when the data is a string. The default value is **'utf-8'**, which is the only value supported.

Constraints: offset + length <= Buffer size

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data written in the file. |

**Example**

let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath,"r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
  encoding: string = 'utf-8';
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let num = ss.writeSync("hello, world", option);

#### \[h2\]read7+

read(buffer: ArrayBuffer, options?: { position?: number; offset?: number; length?: number; }): Promise<ReadOut>

Reads data from a stream file. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/c8JV76DpRrajLHdqgXnw3w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2420AD8BAD1587C9E9D00A45DFFE3D4F083F77EE2C4B6A79E1A2A129F853E4AF)

This API is deprecated since API version 9. Use [fs.Stream.read](../../ohos-file-fs-file-management/document.md#read) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position to store the data read in the buffer in reference to the start address of the buffer. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

Constraints: offset + length <= Buffer size

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ReadOut](#readout)\> | Promise that returns the data read. |

**Example**

import { BusinessError } from '@ohos.base';
import buffer from '@ohos.buffer';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.read(arrayBuffer, option).then((readResult: fileio.ReadOut) => {
  console.info("read data succeed");
  let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
  console.info(\`The content of file: ${buf.toString()}\`);
}).catch((err: BusinessError) => {
  console.error("read data failed with error:" + err);
});

#### \[h2\]read7+

read(buffer: ArrayBuffer, options: { position?: number; offset?: number; length?: number; }, callback: AsyncCallback<ReadOut>): void

Reads data from a stream file. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/fEioB8onQrau1nQnxmWCqA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=72713434AAB624F7C5E03016C99FAA755C96F12FE68F9A2E130D1E2FA08FCB17)

This API is deprecated since API version 9. Use [fs.Stream.read](../../ohos-file-fs-file-management/document.md#read-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position to store the data read in the buffer in reference to the start address of the buffer. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

Constraints: offset + length <= Buffer size

 |
| callback | AsyncCallback<[ReadOut](#readout)\> | Yes | Callback invoked when data is read asynchronously from the stream file. |

**Example**

import { BusinessError } from '@ohos.base';
import buffer from '@ohos.buffer';
let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
let arrayBuffer = new ArrayBuffer(4096);
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
ss.read(arrayBuffer, option, (err: BusinessError, readResult: fileio.ReadOut) => {
  if (readResult.bytesRead) {
    console.info("read data succeed");
    let buf = buffer.from(arrayBuffer, 0, readResult.bytesRead);
    console.info(\`The content of file: ${buf.toString()}\`);
  }
});

#### \[h2\]readSync7+

readSync(buffer: ArrayBuffer, options?: { position?: number; offset?: number; length?: number; }): number

Reads data from a stream file. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6f/v3/503E0hqBTCuAMPxWWDtOcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=859CDE844C222150716E10D4CA848F288A8AE1839D09FF36399FA3775DFAB458)

This API is deprecated since API version 9. Use [fs.Stream.readSync](../../ohos-file-fs-file-management/document.md#readsync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| buffer | ArrayBuffer | Yes | Buffer used to store the file read. |
| options | Object | No | 
The options are as follows:

\- **offset** (number): position to store the data read in the buffer in reference to the start address of the buffer. This parameter is optional. The default value is **0**.

\- **length** (number): length of the data to read. This parameter is optional. The default value is the buffer length minus the offset.

\- **position** (number): position of the data to read in the file. This parameter is optional. By default, data is read from the current position.

Constraints: offset + length <= Buffer size

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | Length of the data read. |

**Example**

let filePath = pathDir + "/test.txt";
let ss = fileio.createStreamSync(filePath, "r+");
class Option {
  offset: number = 0;
  length: number = 4096;
  position: number = 0;
}
let option = new Option();
option.offset = 1;
option.length = 5;
option.position = 5;
let buf = new ArrayBuffer(4096)
let num = ss.readSync(buf, option);

#### Dir

Manages directories. Before calling a method of the **Dir** class, use the **opendir()** method synchronously or asynchronously to create a **Dir** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7e/v3/NhsHjGdGRuGVi3yJkNdDXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DF5E6E4A4A4849FA04474242E874B3239B218503F7EA162EFF30A52C40DD50A1)

This API is deprecated since API version 9. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile) instead.

#### \[h2\]read

read(): Promise<Dirent>

Reads the next directory entry. This API uses a promise to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/_Mwt1rAERzaTmGdsx41ZdA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F4489E05D2D44464620278E5D6BB06E527345EAFD27D8F545ABBF3DD03AB3188)

This API is deprecated since API version 9. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Dirent](#dirent)\> | Promise that returns the next directory entry. |

**Example**

import { BusinessError } from '@ohos.base';
dir.read().then((dirent: fileio.Dirent) => {
  console.info("read succeed, the name of dirent is " + dirent.name);
}).catch((err: BusinessError) => {
  console.error("read failed with error:" + err);
});

#### \[h2\]read

read(callback: AsyncCallback<Dirent>): void

Reads the next directory entry. This API uses an asynchronous callback to return the result.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/Xf5p60aVQuySDx1pz9Up3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=75675F152D50E5F97C71CDDE14B17D8BA2ECD8CF66899B5B101860BF50CF5CD7)

This API is deprecated since API version 9. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[Dirent](#dirent)\> | Yes | Callback invoked when the next directory entry is asynchronously read. |

**Example**

import { BusinessError } from '@ohos.base';
dir.read((err: BusinessError, dirent: fileio.Dirent) => {
  if (dirent) {
    // Do something.
    console.info("read succeed, the name of file is " + dirent.name);
  }
});

#### \[h2\]readSync

readSync(): Dirent

Reads the next directory entry. This API returns the result synchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/53RuzXTLSw-vkPqJaRMd8g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38A7E47F83F270C2ED7E8B012500D6912792F4B1E5EF626CDC23CA623BF383E0)

This API is deprecated since API version 9. Use [fs.listFileSync](../../ohos-file-fs-file-management/document.md#fslistfilesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| [Dirent](#dirent) | Directory entry read. |

**Example**

let dirent = dir.readSync();

#### \[h2\]close7+

close(): Promise<void>

Closes a directory. This API uses a promise to return the result. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/SYpbxDICQzybBE-QqLQt9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=51E29A90EDB3EE9FBCAEE14FEB61C11F3453EAB1656995FE8C154D185E6902E6)

This API is deprecated since API version 9. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Example**

import { BusinessError } from '@ohos.base';
dir.close().then(() => {
  console.info("close dir successfully");
});

#### \[h2\]close7+

close(callback: AsyncCallback<void>): void

Closes a directory. This API uses an asynchronous callback to return the result. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/2FFIvSrbSXSf9Al0aUS4Rg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B8243DF6522B860E9CDA2F5FD903047E4B16EC0265FA7D5F02DCCC59BDE602C)

This API is deprecated since API version 9. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile-1) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Example**

import { BusinessError } from '@ohos.base';
dir.close((err: BusinessError) => {
  console.info("close dir successfully");
});

#### \[h2\]closeSync

closeSync(): void

Closes a directory. After a directory is closed, the file descriptor in **Dir** will be released and no directory entry can be read from **Dir**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/q7L1i4R0Ty2X5_kUO--CFg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=36A2B937A29E860271C4674A04402C8909A852D3D48C7B0FD9C5A1EB463EE9EA)

This API is deprecated since API version 9. Use [fs.listFileSync](../../ohos-file-fs-file-management/document.md#fslistfilesync) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Example**

dir.closeSync();

#### Dirent

Provides information about files and directories. Before calling an API of the **Dirent** class, use [dir.read()](#read) synchronously or asynchronously to create a **Dirent** instance.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/_6EtQVU4RU2DJLL4tSwkHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F15CFE4747F2EB17EB39A8E7F438F4648658326F6C0BC49E2527F45D996CF9F3)

This API is deprecated since API version 9. Use [fs.listFile](../../ohos-file-fs-file-management/document.md#fslistfile) instead.

**System capability**: SystemCapability.FileManagement.File.FileIO

## Properties

| Name | Type | Read-Only | Writable | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | Yes | No | Directory entry name. |

#### \[h2\]isBlockDevice

isBlockDevice(): boolean

Checks whether this directory entry is a block special file. A block special file supports access by block only, and it is cached when accessed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/GBAvO5eXTcaLPnMQqRq5hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=579DF7F052BC2A16F734EC9D40F6764686FB8274C65AA18DE24478218CB83075)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a block special file; returns **false** otherwise. |

**Example**

let dir = fileio.opendirSync(pathDir);
let isBLockDevice = dir.readSync().isBlockDevice();

#### \[h2\]isCharacterDevice

isCharacterDevice(): boolean

Checks whether this directory entry is a character special file. A character special file supports random access, and it is not cached when accessed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/Et2ltB3qQc-UpCAJcVYoNQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=21019FE4BDB11BED0FB912DC46086820246956C6B51B682EA53E2812BA7CEBD2)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a character special file; returns **false** otherwise. |

**Example**

let dir = fileio.opendirSync(pathDir);
let isCharacterDevice = dir.readSync().isCharacterDevice();

#### \[h2\]isDirectory

isDirectory(): boolean

Checks whether this directory entry is a directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/T6B9VP0MT4mV-eMe7mgUZw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=38A638C9E3F56CB085BCA39CF65DB789A0E419DF58F33DAB7F73C7760D761113)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a directory; returns **false** otherwise. |

**Example**

let dir = fileio.opendirSync(pathDir);
let isDirectory = dir.readSync().isDirectory();

#### \[h2\]isFIFO

isFIFO(): boolean

Checks whether this directory entry is a named pipe (also called FIFO). Named pipes are used for inter-process communication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/db/v3/POOiDwrlRgiyLp36DiCW7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5977C0BEF78FACC530778DE873E7D2A4A0654AAB57A7DF5E38ADF92C13E83F90)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a named pipe; returns **false** otherwise. |

**Example**

let dir = fileio.opendirSync(pathDir);
let isFIFO = dir.readSync().isFIFO();

#### \[h2\]isFile

isFile(): boolean

Checks whether this directory entry is a regular file.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/54/v3/8sgCLz-LRKq9rJ1casx40g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7248FA744DBBB2B80949D5E30B70CB0BCA9BACB09237EF699A177658CD4AEF8C)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a regular file; returns **false** otherwise. |

**Example**

let dir = fileio.opendirSync(pathDir);
let isFile = dir.readSync().isFile();

#### \[h2\]isSocket

isSocket(): boolean

Checks whether this directory entry is a socket.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/qy5PsFvbSayiW8OqKAW9_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67A65CEA0CBD101F65A83A93FF86C27D18D0227B9CC93CB6B85EEFA287FD732B)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a socket; returns **false** otherwise. |

**Example**

let dir = fileio.opendirSync(pathDir);
let isSocket = dir.readSync().isSocket();

#### \[h2\]isSymbolicLink

isSymbolicLink(): boolean

Checks whether this directory entry is a symbolic link.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/6pQcaoSjTkipKxlbaSRuBg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CC8E6549EFDB0C19C2F77447E9178B613C43DFF86FAB84AE9797E6A679B32A3)

This API is deprecated since API version 9.

**System capability**: SystemCapability.FileManagement.File.FileIO

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Returns **true** if it is a symbolic link; returns **false** otherwise. |

**Example**

let dir = fileio.opendirSync(pathDir);
let isSymbolicLink = dir.readSync().isSymbolicLink();
