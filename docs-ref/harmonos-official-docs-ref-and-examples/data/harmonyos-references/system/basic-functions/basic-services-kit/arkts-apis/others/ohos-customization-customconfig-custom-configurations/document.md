# @ohos.customization.customConfig (Custom Configurations)

This module provides APIs for applications to obtain custom configurations, such as channel IDs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/9nW5i3eHTFqC2SIIM4A0wg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062358Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E77AF96993E9A029DAF63B47591C2E16DB86084FF2B25A7928D9A4BCF0FD8C1)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { customConfig } from '@kit.BasicServicesKit';

#### customConfig.getChannelId

getChannelId(): string

Obtains a pre-installed channel ID of this application.

**Atomic service API**: This API can be used in atomic services since API version 13.

**System capability**: SystemCapability.Customization.CustomConfig

**Return value**

| Type | Description |
| :-- | :-- |
| string | Channel ID obtained. |

**Example**

import { customConfig } from '@kit.BasicServicesKit';

let channelId: string = customConfig.getChannelId();
console.info('app channelId is ' + channelId);
