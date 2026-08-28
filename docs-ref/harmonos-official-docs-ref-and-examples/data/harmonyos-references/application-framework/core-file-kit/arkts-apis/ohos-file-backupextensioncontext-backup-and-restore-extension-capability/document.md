# @ohos.file.BackupExtensionContext (Backup and Restore Extension Capability)

**BackupExtensionContext** is the context of **BackupExtension** and inherits from **ExtensionContext**.

The **BackupExtensionContext** module provides the capability for accessing a specific **BackupExtension**. For a **BackupExtension**, you can directly use **BackupExtensionContext** as the context or define a context that inherits from **BackupExtensionContext**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/gN-h17FeTPavRINZdFy72w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062320Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1098B7099A28D5D62E9C4D5C4057D51B674142D7C4A9C3488653F469CF9BDDEC)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs of this module can be used only in the stage model.

#### Modules to Import

import  { BackupExtensionContext } from '@kit.CoreFileKit';

#### BackupExtensionContext

#### \[h2\]Properties

**System capability**: SystemCapability.FileManagement.StorageService.Backup

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| backupDir12+ | string | Yes | No | Temporary directory used for backup or restore. This directory cannot be used for other purposes. Currently, only the **el1** and **el2** directories are supported. If other directories are used, null is returned. |

## When to Use

**BackupExtensionContext** is used to obtain a temporary directory for backup or restore.

**Example**

import { BackupExtensionAbility } from '@kit.CoreFileKit';
import { contextConstant } from '@kit.AbilityKit';

export default class MyBackupExtAbility extends BackupExtensionAbility {
    async onBackup() {
        console.info("onBackup begin");
        // You can modify this.context.area to change the sandbox path corresponding to el1/ or el2/.
        this.context.area = contextConstant.AreaMode.EL1;
        // Use this.context.backupDir to obtain the sandbox path.
        let dir = this.context.backupDir;
        console.info(\`onBackup el1 dir: ${dir}\`);
        this.context.area = contextConstant.AreaMode.EL2;
        dir = this.context.backupDir;
        console.info(\`onBackup el2 dir: ${dir}\`);
        console.info("onBackup end");
    }

    async onRestore() {
        console.info("onRestore begin");
        this.context.area = contextConstant.AreaMode.EL1;
        let dir = this.context.backupDir;
        console.info(\`onRestore el1 dir: ${dir}\`);
        this.context.area = contextConstant.AreaMode.EL2;
        dir = this.context.backupDir;
        console.info(\`onRestore el2 dir: ${dir}\`);
        console.info("onRestore end");
    }
}
