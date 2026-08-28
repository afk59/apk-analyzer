# Adaptation Guide for Application Clone

#### Overview

During device replacement, users need to back up the data from one device and send the data to another device for restoration, implementing cross-device data migration. In this case, the clone tool is required. When accessing the clone tool, the application needs to implement its own **BackupExtensionAbility**, implementing data backup in **onBackup** and data restoration in **onRestore**. If **BackupExtensionAbility** is not implemented for the application, the cloning process only migrates the application from the old device without migrating the application data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b4/v3/Y6JssqmYTW2k84R3I4Pj1w/en-us_image_0000002497754322.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061951Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A40C1A9EA4D706DB19674640E1FC403BAE23C1EC79B73EB6CC1B0DB74C659C75)

#### Adaptation Guide

Since API version 12, third-party applications only need to access the backup and restoration capability. For details, see **[Accessing Backup and Restore](../accessing-backup-and-restore/document.md)**
