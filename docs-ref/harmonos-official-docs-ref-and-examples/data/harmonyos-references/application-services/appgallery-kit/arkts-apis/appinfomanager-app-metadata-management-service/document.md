# appInfoManager (App Metadata Management Service)

This module provides functions for querying information about custom icons, selecting custom icons, and disabling custom icons.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/iQQF04zWQmWl268vVF6nVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062504Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5C665E8A160B856D1250557A81D4B148E75300827CC2ACBF6364208D8EA47B26)

Exceptions need to be captured when an API is called.

**Start version**: 5.0.3(15)

#### Modules to Import

import { appInfoManager } from '@kit.AppGalleryKit';

#### DynamicIconInfo

Information about a custom icon.

**System capability**: SystemCapability.AppGalleryService.AppInfoManager

**Start version**: 5.0.3(15)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

iconUrl

 | 

string

 | 

Yes

 | 

No

 | 

URL of the custom icon.

 |
| 

iconId

 | 

string

 | 

Yes

 | 

No

 | 

ID of the custom icon.

 |
| 

enabled

 | 

boolean

 | 

Yes

 | 

No

 | 

Indicates whether the custom icon is in use. **true**: yes; **false**: no.

 |

#### appInfoManager.queryDynamicIcons

queryDynamicIcons(): Promise<DynamicIconInfo\[\]>

Queries information about a custom icon. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AppGalleryService.AppInfoManager

**Start version**: 5.0.3(15)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[DynamicIconInfo](#section1535385414136)\[\]>

 | 

Information about the custom icon that is returned through a promise.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1006800001

 | 

The specified service extension connect failed.

 |
| 

1006800009

 | 

System internal error.

 |
| 

1006800010

 | 

No dynamic icon data.

 |

**Example**:

import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appInfoManager.queryDynamicIcons()
    .then((queryResult: appInfoManager.DynamicIconInfo\[\]) => {
      hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo size = " + queryResult.length);
      for (let i = 0; i < queryResult.length; i++) {
        hilog.info(0, 'TAG', "Succeeded in getting DynamicIconInfo iconUrl = " + queryResult\[i\]\["iconUrl"\] + ", iconId = " + queryResult\[i\]\["iconId"\] + ", enabled = "+queryResult\[i\]\["enabled"\]);
      }
    }).catch((error: BusinessError) => {
      hilog.error(0, 'TAG', "queryDynamicIcons failed, code: " + error.code + ", exception message: " + error.message);
    });
} catch (error) {
  hilog.error(0, 'TAG', "queryDynamicIcons exception code: " + error.code + ", exception message: " + error.message);
}

#### appInfoManager.selectDynamicIcon

selectDynamicIcon(iconId: string): Promise<void>

Selects a custom icon. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AppGalleryService.AppInfoManager

**Start version**: 5.0.3(15)

**Parameters**:

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

iconId

 | 

string

 | 

Yes

 | 

ID of the custom icon.

 |

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error.

 |
| 

1006800009

 | 

System internal error.

 |
| 

1006800011

 | 

Select dynamic icon failed.

 |
| 

1006800013

 | 

Failed to switch to the custom icon because a custom theme icon is currently in use.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/3Q5oO4bYTGyDjqCU8t_l2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062504Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B22B296CD8686DDBFB1DF9DFABA2FD44969DCDFC75A8C4D35254D8618193457)

From version 6.0.0(20), this API can return error code 1006800013.

**Example**:

import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  let iconId: string = 'iconId';
  appInfoManager.selectDynamicIcon(iconId).then(() => {
      hilog.info(0, 'TAG', "Succeeded in selecting dynamic icon");
  }).catch((error: BusinessError) => {
    hilog.error(0, 'TAG', "selectDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
  });
} catch (error) {
  hilog.error(0, 'TAG', "selectDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
}

#### appInfoManager.disableDynamicIcon

disableDynamicIcon(): Promise<void>

Disables the custom icon and uses the default icon. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.AppGalleryService.AppInfoManager

**Start version**: 5.0.3(15)

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

 |

**Error codes**:

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1006800009

 | 

System internal error.

 |
| 

1006800012

 | 

Disable dynamic icon failed.

 |

**Example**:

import { appInfoManager } from '@kit.AppGalleryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  appInfoManager.disableDynamicIcon().then(() => {
      hilog.info(0, 'TAG', "Succeeded in disabling dynamic icon");
  }).catch((error: BusinessError) => {
    hilog.error(0, 'TAG', "disableDynamicIcon failed, code: " + error.code + ", exception message: " + error.message);
  });
} catch (error) {
  hilog.error(0, 'TAG', "disableDynamicIcon exception code: " + error.code + ", exception message: " + error.message);
}
