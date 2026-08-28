# @ohos.file.cloudSyncManager (Device-Cloud Sync Management)

The **cloudSyncManager** module provides APIs for managing device-cloud synergy for applications. You can use the APIs to enable or disable device-cloud synergy, change the device-cloud sync switch for an application, notify cloud data changes, and clear or retain cloud files when a cloud account exits.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/FcQj7LOyQ8m1B0a3XRfeog/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062319Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A765773E0AFC78BF78FA8FD801EB12BF958A983414C3D0523EA444DC04240777)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { cloudSyncManager } from '@kit.CoreFileKit';

#### DownloadStopReason20+

Enumerates the reasons why the download stops. The default value is **NO\_STOP**.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_STOP | 0 | Downloading. |
| NETWORK\_UNAVAILABLE | 1 | Downloading. Mobile network and Wi-Fi are unavailable. |
| LOCAL\_STORAGE\_FULL | 2 | Downloading. The device storage is full. |
| TEMPERATURE\_LIMIT | 3 | Downloading. The device temperature exceeds the upper limit. |
| USER\_STOPPED | 4 | Downloading. The user stops the download. |
| APP\_UNLOAD | 5 | Downloading. The application is uninstalled. |
| OTHER\_REASON | 6 | Downloading. The download stops due to other reasons, for example, the cloud server does not respond. |

#### DownloadState20+

Enumerates the download states.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

| Name | Value | Description |
| :-- | :-- | :-- |
| RUNNING | 0 | Downloading. |
| COMPLETED | 1 | Downloaded. |
| STOPPED | 2 | Downloading stopped. |

#### DownloadProgress20+

Represents the downgrade download progress.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| state | [DownloadState](#downloadstate20) | No | No | Download state. |
| successfulCount | number | No | No | Number of downloaded files. The value range is \[0, INT32\_MAX\]. If the progress is abnormal, **\-1** is returned. |
| failedCount | number | No | No | Number of files that fail to be downloaded. The value range is \[0, INT32\_MAX\]. If the progress is abnormal, **\-1** is returned. |
| totalCount | number | No | No | Total number of files to be downloaded. The value range is \[0, INT32\_MAX\]. If the progress is abnormal, **\-1** is returned. |
| downloadedSize | number | No | No | Size of the downloaded data, in bytes. The value range is \[0, INT64\_MAX). If the progress is abnormal, **INT64\_MAX** is returned. |
| totalSize | number | No | No | Total size of the files to be downloaded, in bytes. The value range is \[0, INT64\_MAX). If the progress is abnormal, **INT64\_MAX** is returned. |
| stopReason | [DownloadStopReason](#downloadstopreason20) | No | No | Reason why the download stops. |

#### CloudFileInfo20+

Represents the number and size of local and cloud files of an application.

**System capability**: SystemCapability.FileManagement.DistributedFileService.CloudSyncManager

## Properties

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| cloudFileCount | number | No | No | Total number of cloud files that are not downloaded locally. The value range is \[0, INT32\_MAX\]. |
| cloudFileTotalSize | number | No | No | Total size of cloud files that are not downloaded locally, in bytes. The value range is \[0, INT64\_MAX\]. |
| localFileCount | number | No | No | Total number of local files that are not uploaded to the cloud. The value range is \[0, INT32\_MAX\]. |
| localFileTotalSize | number | No | No | Total size of local files that are not uploaded to the cloud, in bytes. The value range is \[0, INT64\_MAX\]. |
| bothFileCount | number | No | No | Total number of local files that have been uploaded to the cloud. The value range is \[0, INT32\_MAX\]. |
| bothFileTotalSize | number | No | No | Total size of local files that have been uploaded to the cloud, in bytes. The value range is \[0, INT64\_MAX\]. |
