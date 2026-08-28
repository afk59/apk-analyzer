# Module Description

The Digital Rights Management (DRM) framework enables you to develop digital rights management features for audio and video services. By calling the DRM plugins provided by the system, you can achieve the following:

-   DRM certificate management: Generate certificate requests and handle certificate responses to facilitate certificate provisioning (downloading).
-   DRM media key management: Generate media key requests, manage media key responses, and handle offline media keys.
-   DRM content authorization: Allow DRM plugins to authorize content based on media key permissions.
-   DRM content decryption: Decrypt DRM content to support media playback functionality.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/51/v3/6BZWB2cRTA-8mjzoGEs7Zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062430Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D4137529B6F1314D33B999C5C433DDFE1302F9CCEDEB326F0DF9BEBB2181E0C6)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { drm } from '@kit.DrmKit';
