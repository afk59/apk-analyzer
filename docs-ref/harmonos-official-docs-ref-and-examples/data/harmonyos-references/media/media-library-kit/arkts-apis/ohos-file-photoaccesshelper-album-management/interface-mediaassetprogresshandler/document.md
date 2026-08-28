# Interface (MediaAssetProgressHandler)

**MediaAssetProgressHandler** is used to obtain the media asset processing progress from **onProgress()**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/yI8XgG8cSfiiTWUr-oMHdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=582C5E9784067D23CE00638A0D37A161517633A9CCF863040B6572C089ED6E0D)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 15.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### onProgress15+

onProgress(progress: number): void

Called when the progress of the requested video is returned.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| progress | number | Yes | 
Progress in percentage.

Value range: \[0, 100\]

 |
