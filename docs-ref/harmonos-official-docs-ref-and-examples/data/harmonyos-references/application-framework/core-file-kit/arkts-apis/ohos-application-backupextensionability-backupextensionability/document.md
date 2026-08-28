# @ohos.application.BackupExtensionAbility (BackupExtensionAbility)

The **BackupExtensionAbility** module provides extended backup and restore capabilities for applications.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bd/v3/B8mdzVymTwCGZapaN653VQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=845C201C336704D5046D5EBF0E6BAF3A5A3DCFB9B5B791C038FBA2B4FD9ECB1A)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

#### BundleVersion

Defines the version information required for data restore. You can determine the application data to be restored based on the version information.

**System capability**: SystemCapability.FileManagement.StorageService.Backup

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| code | number | No | No | Internal version number of the application. |
| name | string | No | No | Version name of the application. |

#### BackupExtensionAbility

Implements backup and restore for application access data. You can use [onBackup](#onbackup) and [onRestore](#onrestore) to implement custom backup and restore operations.

#### \[h2\]Properties

**System capability**: SystemCapability.FileManagement.StorageService.Backup

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| context11+ | [BackupExtensionContext](../ohos-file-backupextensioncontext-backup-and-restore-extension-capability/document.md) | No | No | Context of the BackupExtensionAbility. This context is inherited from [ExtensionContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/extensioncontext/document.md). |

#### \[h2\]onBackup

onBackup(): void

Called when data is being backed up. You need to implement extended data backup operations.

**System capability**: SystemCapability.FileManagement.StorageService.Backup

**Example**

class BackupExt extends BackupExtensionAbility {
  async onBackup() {
    console.info('onBackup');
  }
}

#### \[h2\]onBackupEx12+

onBackupEx(backupInfo: string): string | Promise<string>

Called to pass parameters to the application during the application backup or restore process. It uses a promise to return the result.

**onBackupEx** and **onBackup** are mutually exclusive. Call **onBackupEx** preferentially if it is overridden.

The return value of **onBackupEx** cannot be an empty string. If an empty string is returned, **onBackup** will be called.

**System capability**: SystemCapability.FileManagement.StorageService.Backup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| backupInfo | string | Yes | 
Package information to be passed by the third-party application.

When it is an empty string, you need to determine how to handle this scenario.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Promise<string> | 
Information about the custom backup operation executed by the application, including the backup result and error information. The return value is in JSON format.

A promise object is returned for asynchronous operations.

A string is returned for synchronous operations.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/33/v3/ZxKP1mcURK-SYYoMMuVucA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AB9F411F54477944CF1CA5AFBA37219A668300930BE613465019CB7C6661FE3C)

The following shows the sample code for synchronous implementation.

**Example**

import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

interface ErrorInfo {
  type: string,
  errorCode: number,
  errorInfo: string
}
class BackupExt extends BackupExtensionAbility {
  onBackupEx(backupInfo: string): string {
    try {
      if (backupInfo == "") {
        // If backupInfo is empty, the application processes the data based on the service.
        console.info("backupInfo is empty");
      }
      console.info(\`onBackupEx ok\`);
      let errorInfo: ErrorInfo = {
        type: "ErrorInfo",
        errorCode: 0,
        errorInfo: "app customized error info"
      }
      return JSON.stringify(errorInfo);
    } catch (err) {
      console.error(\`BackupExt error. Code:${err.code}, message:${err.message}\`);
    }
    return "";
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2f/v3/gWiSLwflTCeNEmw9bJs-Gg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC1E1ED5BE6101C8F3FBA5052DBEE5EF423BF35BAF7865350413B58DF4CFB502)

The following shows the sample code for asynchronous implementation.

**Example**

import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

interface ErrorInfo {
  type: string,
  errorCode: number,
  errorInfo: string
}
class BackupExt extends BackupExtensionAbility {
  // Asynchronous implementation
  async onBackupEx(backupInfo: string): Promise<string> {
    try {
      if (backupInfo == "") {
        // If backupInfo is empty, the application processes the data based on the service.
        console.info("backupInfo is empty");
      }
      console.info(\`onBackupEx ok\`);
      let errorInfo: ErrorInfo = {
        type: "ErrorInfo",
        errorCode: 0,
        errorInfo: "app customized error info"
      }
      return JSON.stringify(errorInfo);
    } catch (err) {
      console.error(\`BackupExt error. Code:${err.code}, message:${err.message}\`);
    }
    return "";
  }
}

#### \[h2\]onRestore

onRestore(bundleVersion: BundleVersion): void

Called when data is being restored. You need to implement the extended data restore operation.

**System capability**: SystemCapability.FileManagement.StorageService.Backup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleVersion | [BundleVersion](#bundleversion) | Yes | Version information of the application data to be restored. |

**Example**

import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';

class BackupExt extends BackupExtensionAbility {
  async onRestore(bundleVersion : BundleVersion) {
    console.info(\`onRestore ok ${JSON.stringify(bundleVersion)}\`);
  }
}

#### \[h2\]onRestoreEx12+

onRestoreEx(bundleVersion: BundleVersion, restoreInfo: string): string | Promise<string>

Called when data is being restored. You need to implement the extended data restore operation. It uses a promise to return the result.

**onRestoreEx** and **onRestore** are mutually exclusive. Call **onRestoreEx** preferentially if it is overridden.

The return value of **onRestoreEx** cannot be an empty string. If an empty string is returned, the system will attempt to call **onRestore**.

The return value of **onRestoreEx** is in JSON format. For details, see the sample code.

**System capability**: SystemCapability.FileManagement.StorageService.Backup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| bundleVersion | [BundleVersion](#bundleversion) | Yes | Version information of the application data to be restored. |
| restoreInfo | string | Yes | 
Parameter to be passed in the restore process. This field is reserved.

It may be an empty string in some cases.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| string | Promise<string> | 
Information about the custom restore operation executed by the application, including the restore result and error information. The return value is in JSON format.

A promise object is returned for asynchronous operations.

A string is returned for synchronous operations.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/23/v3/Fk3VEPknSluJP34wGAY4Sw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7D1D0807BD41BC5F3C717A5AABDF0EA63312F6EB97C2FB043475DDD2AFD75FB3)

The following shows the sample code for asynchronous implementation.

**Example**

import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
interface ErrorInfo {
  type: string,
  errorCode: number,
  errorInfo: string
}
class BackupExt extends BackupExtensionAbility {
  // Asynchronous implementation
  async onRestoreEx(bundleVersion : BundleVersion, restoreInfo: string): Promise<string> {
    try {
      if (restoreInfo == "") {
        // If restoreInfo is empty, the application processes the data based on the service.
        console.info("restoreInfo is empty");
      }
      console.info(\`onRestoreEx ok ${JSON.stringify(bundleVersion)}\`);
      let errorInfo: ErrorInfo = {
        type: "ErrorInfo",
        errorCode: 0,
        errorInfo: "app customized error info"
      }
      return JSON.stringify(errorInfo);
    } catch (err) {
      console.error(\`onRestoreEx error. Code:${err.code}, message:${err.message}\`);
    }
    return "";
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ff/v3/GY6YMLsKShe2yF4bIIhdMg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CDAF8543DF54BB512F54A0B40562AF74D7F22A4DA0AF933DA48E86D1B70A0CA2)

The following shows the sample code for synchronous implementation.

**Example**

import { BackupExtensionAbility, BundleVersion } from '@kit.CoreFileKit';
interface ErrorInfo {
  type: string,
  errorCode: number,
  errorInfo: string
}

class BackupExt extends BackupExtensionAbility {
  // Synchronous implementation
  onRestoreEx(bundleVersion : BundleVersion, restoreInfo: string): string {
    try {
      if (restoreInfo == "") {
        // If restoreInfo is empty, the application processes the data based on the service.
        console.info("restoreInfo is empty");
      }
      console.info(\`onRestoreEx ok ${JSON.stringify(bundleVersion)}\`);
      let errorInfo: ErrorInfo = {
        type: "ErrorInfo",
        errorCode: 0,
        errorInfo: "app customized error info"
      }
      return JSON.stringify(errorInfo);
    } catch (err) {
      console.error(\`onRestoreEx error. Code:${err.code}, message:${err.message}\`);
    }
    return "";
  }
}

#### \[h2\]onProcess12+

onProcess(): string

Called to return the progress information. This callback is executed synchronously and implemented during the execution of **onBackup/onBackupEx** or **onRestore/onRestoreEx**. This callback returns the service processing progress of the application. The return value is in JSON format. For details, see the sample code.

**System capability**: SystemCapability.FileManagement.StorageService.Backup

**Return value**

| Type | Description |
| :-- | :-- |
| string | Progress information during the execution of **onBackup** or **onRestore**. The return value is in JSON format. |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/4tJ-UNxSRH6US6eJKZ-n3g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=852D28B854919942CE218DC1BDA940CF1194B642CB872FB058C39E269104DE98)

-   The system provides the default processing mechanism if **onProcess** is not implemented. If **onProcess** is used, the return value must strictly comply with that in the sample code.
-   The execution of **onProcess** cannot exceed 1 second. The system calls **onProcess** every 5 seconds. If the execution times out for three consecutive times, the current backup or restoration task of the application is terminated.
-   If **onProcess** is used, **onBackup/onBackupEx** and **onRestore/onRestoreEx** must be asynchronously executed in a dedicated thread. Otherwise, **onProcess** cannot run properly. For details, see the sample code.
-   The following example shows the recommended use of **onProcess()**.

**Example**

import { BackupExtensionAbility } from '@kit.CoreFileKit';
import { taskpool } from '@kit.ArkTS';

@Sendable
class MigrateProgressInfo {
  private migrateProgress: string = '';
  private name: string = "test"; // appName
  private processed: number = 0; // Processed data
  private total: number = 100; // Total number
  private isPercentage: boolean = true // (Optional) The value true means to display the progress in percentage; the value false or an unimplemented field means to display the progress by the number of items.

  getMigrateProgress(): string {
    this.migrateProgress = \`{"progressInfo": \[{"name": ${this.name}, "processed": ${this.processed}, "total": ${
      this.total}, "isPercentage": ${this.isPercentage}}\]}\`;
    return this.migrateProgress;
  }

  updateProcessed(processed: number) {
    this.processed = processed;
  }
}

class BackupExt extends BackupExtensionAbility {
  private progressInfo: MigrateProgressInfo = new MigrateProgressInfo();

  // In the following code, the appJob method is the simulated service code, and args specifies the parameters of appJob(). This method is used to start a worker thread in the task pool.
  async onBackup() {
    console.info(\`onBackup begin\`);
    let args = 100; // args is a parameter of appJob().
    let jobTask: taskpool.Task = new taskpool.LongTask(appJob, this.progressInfo, args);
    try {
      await taskpool.execute(jobTask, taskpool.Priority.LOW);
    } catch (error) {
      console.error("onBackup error." + error.message);
    }
    taskpool.terminateTask(jobTask); // Manually destroy the task.
    console.info(\`onBackup end\`);
  }

  async onRestore() {
    console.info(\`onRestore begin\`);
    let args = 100; // args is a parameter of appJob().
    let jobTask: taskpool.Task = new taskpool.LongTask(appJob, this.progressInfo, args);
    try {
      await taskpool.execute(jobTask, taskpool.Priority.LOW);
    } catch (error) {
      console.error("onRestore error." + error.message);
    }
    taskpool.terminateTask(jobTask); // Manually destroy the task.
    console.info(\`onRestore end\`);
  }
 

  onProcess(): string {
    console.info(\`onProcess begin\`);
    return this.progressInfo.getMigrateProgress();
  }
}

@Concurrent
function appJob(progressInfo: MigrateProgressInfo, args: number) : string {
  console.info(\`appJob begin, args is: \` + args);
  // Update the processing progress during service execution.
  let currentProcessed: number = 0;
  // Simulate the actual service logic.
  for (let i = 0; i < args; i++) {
    currentProcessed = i;
    progressInfo.updateProcessed(currentProcessed);
  }
  return "ok";
}

#### \[h2\]onRelease20+

onRelease(scenario: number): Promise<void>

Provides secure exit APIs of the backup and restore framework. It is triggered when the application backup or restore is complete, allowing the application to perform special processing afterward, such as removing temporary files generated during these operations. This API uses a promise to return the result.

**onRelease** has a timeout mechanism. If the **onRelease** operation is not completed within 5 seconds, the application process exits when the backup and restoration are complete.

**System capability**: SystemCapability.FileManagement.StorageService.Backup

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| scenario | number | Yes | 
Indicates the backup or restore scenario.

The value **1** indicates the backup scenario.

The value **2** indicates the restore scenario.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

// The following describes an example of removing files.
import { BackupExtensionAbility, fileIo } from '@kit.CoreFileKit';

const SCENARIO\_BACKUP: number = 1;
const SCENARIO\_RESTORE: number = 2;
// Temporary directory to be removed.
let filePath: string = '/data/storage/el2/base/.temp/';

class BackupExt extends BackupExtensionAbility {
  async onRelease(scenario: number): Promise<void> {
    try {
      if (scenario == SCENARIO\_BACKUP) {
        // In the backup scenario, the application implements the processing. The following describes how to remove temporary files generated during backup.
        console.info(\`onRelease begin\`);
        await fileIo.rmdir(filePath);
        console.info(\`onRelease end, rmdir succeed\`);
      }
      if (scenario == SCENARIO\_RESTORE) {
        // In the restore scenario, the application implements the processing. The following describes how to remove temporary files generated during restoration.
        console.info(\`onRelease begin\`);
        await fileIo.rmdir(filePath);
        console.info(\`onRelease end, rmdir succeed\`);
      }
    } catch (error) {
      console.error(\`onRelease failed with error. Code: ${error.code}, message: ${error.message}\`);
    }
  }
}
