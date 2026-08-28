# Constants

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9a/v3/36EkLm46Su272B-b6ajhng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062418Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=76131C496EF8B41C4DC1C9383114175F499B0CC0F65537D36AA5421BE86DF467)

The initial APIs of this module are supported since API version 7. Newly added APIs will be marked with a superscript to indicate their earliest API version.

| Name | Type | Read-Only | Description |
| :-- | :-- | :-- | :-- |
| DEFAULT\_VOLUME\_GROUP\_ID9+ | number | Yes | 
Default volume group ID.

**System capability**: SystemCapability.Multimedia.Audio.Volume

 |
| DEFAULT\_INTERRUPT\_GROUP\_ID9+ | number | Yes | 

Default audio interruption group ID.

**System capability**: SystemCapability.Multimedia.Audio.Interrupt

 |

**Example**

import { audio } from '@kit.AudioKit';

const defaultVolumeGroupId = audio.DEFAULT\_VOLUME\_GROUP\_ID;
const defaultInterruptGroupId = audio.DEFAULT\_INTERRUPT\_GROUP\_ID;
