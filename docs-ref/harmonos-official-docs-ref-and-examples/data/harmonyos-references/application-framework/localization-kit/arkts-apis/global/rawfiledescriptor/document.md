# RawFileDescriptor

Provides the descriptor of the HAP where the rawfile is located.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2/v3/m7oEiH9qR3S14iFk5XqWHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B572E92BAF43719ADB1F3149E979AAD2AF16A51E75B1BD9DD3714E3001E26443)

The initial APIs of this module are supported since API version 8. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Import a module.

import { resourceManager } from '@kit.LocalizationKit'

#### RawFileDescriptor

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Global.ResourceManager

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fd | number | No | No | Pointer to the file descriptor. |
| offset | number | No | No | Start offset. |
| length | number | No | No | File length. |
