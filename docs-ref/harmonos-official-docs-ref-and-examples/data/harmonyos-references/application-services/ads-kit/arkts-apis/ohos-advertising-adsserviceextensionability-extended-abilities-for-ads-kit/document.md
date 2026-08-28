# @ohos.advertising.AdsServiceExtensionAbility (Extended Abilities for Ads Kit)

This module provides extended abilities for device vendors. Device vendors can implement the callbacks for ad requests.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/TNZfy9J_T8iJuOezuk8WWw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=365AF9A9D48B1B48557568656DE6F8489F8580F3AED099805CAFFCC73A77B3E3)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { RespCallback } from '@kit.AdsKit';

#### RespCallback

(respData: Map<string, Array<advertising.Advertisement>>): void

Ad request callback.

**System capability**: SystemCapability.Advertising.Ads

**Parameters**:

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

respData

 | 

Map<string, Array<advertising.[Advertisement](../ohos-advertising-ads-kit-framework/document.md#advertisement)\>>

 | 

Yes

 | 

Ad request callback data.

 |

**Example**:

import { advertising, RespCallback } from '@kit.AdsKit';

function setRespCallback(respCallback: RespCallback) {
  const respData: Map<string, Array<advertising.Advertisement>> = new Map();
  // Set the data returned by the ad request.
  // ...
  respCallback(respData);
}
