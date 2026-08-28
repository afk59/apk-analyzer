# @ohos.identifier.oaid (OAID Service)

This module provides APIs for obtaining and resetting Open Anonymous Device Identifiers (OAIDs).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/pjcuJjx3RO21O6gHk_yGsg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062503Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CBEBF40C0557A3D9077581A0F1DD58A576D573C39A3844D1CF738DDA8ECE2AF7)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

To use the API for obtaining OAIDs, [request the ohos.permission.APP\_TRACKING\_CONSENT permission from users](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/request-user-authorization). By default, the permission is enabled.

#### Modules to Import

import { identifier } from '@kit.AdsKit';

#### identifier.getOAID

getOAID(): Promise<string>

Obtains the OAID. This API returns the result asynchronously through a promise.

**Required permission**: ohos.permission.APP\_TRACKING\_CONSENT

**System capability**: SystemCapability.Advertising.OAID

**Returns**:

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<string>

 | 

OAID returned through a promise.

1\. If the app has configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission and **Activity tracking for this app** is set to **Allow**, the OAID is returned.

2\. If the app has configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission and **Activity tracking for this app** is set to **Deny**, **00000000-0000-0000-0000-000000000000** is returned.

3\. If the app has not configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission, **00000000-0000-0000-0000-000000000000** is returned.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/oaid-service-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

17300001

 | 

System internal error.

 |

**Example**:

import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

void identifier.getOAID().then((data: string) => {
  const oaid: string = data;
}).catch((error: BusinessError) => {
  hilog.info(0x0000, 'testTag', \`Failed to get oaid. Code is ${error.code}, message is ${error.message}\`);
});

#### identifier.getOAID

getOAID(callback: AsyncCallback<string>): void

Obtains the OAID. This API returns the result asynchronously through a callback.

**Required permission**: ohos.permission.APP\_TRACKING\_CONSENT

**System capability**: SystemCapability.Advertising.OAID

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

callback

 | 

AsyncCallback<string>

 | 

Yes

 | 

Callback function that returns the OAID.

1\. If the app has configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission and **Activity tracking for this app** is set to **Allow**, the OAID is returned.

2\. If the app has configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission and **Activity tracking for this app** is set to **Deny**, **00000000-0000-0000-0000-000000000000** is returned.

3\. If the app has not configured the **ohos.permission.APP\_TRACKING\_CONSENT** permission, **00000000-0000-0000-0000-000000000000** is returned.

 |

**Error codes:**

For details about the following error codes, please click [here](../../error-codes/oaid-service-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

17300001

 | 

System internal error.

 |

**Example**:

import { identifier } from '@kit.AdsKit';
import { BusinessError } from '@kit.BasicServicesKit';

identifier.getOAID((err: BusinessError, data: string) => {
  if (err.code) {
    return;
  }
  const oaid: string = data;
});
