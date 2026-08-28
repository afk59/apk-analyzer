# SuperPrivacyMode

This module provides APIs related to the Super Privacy mode. Your app can process services based on the current Super Privacy status.

**Start version**: 6.0.2(22)

#### Modules to Import

import { superPrivacyMode } from '@kit.DeviceSecurityKit';

#### SuperPrivacyMode

Enumerates the Super Privacy statuses.

**System capability**: SystemCapability.Security.SecurityPrivacyServer

**Start version**: 6.0.2(22)

**Device behavior differences**: This enum has no effect on TVs and wearables. On phones, PCs/2-in-1 devices, and tablets that support the Super Privacy option, this enum functions properly. If the Super Privacy option is unavailable on these devices, using this enum results in error code **1006200005**. When using this enum, comply with the [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-getsuperprivacymode#section19314125019324).

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

OFF

 | 

0

 | 

The Super Privacy mode is disabled.

 |
| 

ON\_WHEN\_FOLDED

 | 

1

 | 

The Super Privacy mode is enabled only when the device is folded.

 |
| 

ALWAYS\_ON

 | 

2

 | 

The Super Privacy mode is always on.

 |

#### getSuperPrivacyMode

getSuperPrivacyMode(): Promise<SuperPrivacyMode>

Obtains the current Super Privacy status.

**System capability**: SystemCapability.Security.SecurityPrivacyServer

**Start version**: 6.0.2(22)

**Device behavior differences**: This API has no effect on TVs and wearables. On phones, PCs/2-in-1 devices, and tablets that support the Super Privacy option, this API functions properly. On phones, PCs/2-in-1 devices, and tablets that do not have the Super Privacy option, this API returns error code **1006200005**. When using this API, comply with the [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-getsuperprivacymode#section19314125019324).

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[SuperPrivacyMode](#section11705111513)\>

 | 

Promise used to return the Super Privacy status.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/superprivacymode/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1006200002

 | 

Internal error.

 |
| 

1006200005

 | 

This device is not support SuperPrivacy.

 |

**Example:**

import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

let mode: superPrivacyMode.SuperPrivacyMode = superPrivacyMode.SuperPrivacyMode.OFF;
try {
  mode = await superPrivacyMode.getSuperPrivacyMode();
  hilog.info(DOMAIN, TAG, \`Super privacy mode = ${mode}\`);
} catch (err) {
  hilog.error(DOMAIN, TAG, \`call getSuperPrivacyMode interface failed, errCode:${err?.code}, errMessage:${err?.message}\`);
}

#### on('superPrivacyModeChange')

on(type: 'superPrivacyModeChange', callback: Callback<SuperPrivacyMode>): void

Subscribes to Super Privacy status change events.

**System capability**: SystemCapability.Security.SecurityPrivacyServer

**Start version**: 6.0.2(22)

**Device behavior differences**: This API has no effect on TVs and wearables. On phones, PCs/2-in-1 devices, and tablets that support the Super Privacy option, this API functions properly. On phones, PCs/2-in-1 devices, and tablets that do not have the Super Privacy option, this API returns error code **1006200005**. When using this API, comply with the [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-getsuperprivacymode#section19314125019324).

**Parameters:**

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

type

 | 

string

 | 

Yes

 | 

Event type to subscribe to. The value is fixed at **superPrivacyModeChange**.

 |
| 

callback

 | 

Callback<[SuperPrivacyMode](#section11705111513)\>

 | 

Yes

 | 

Callback function used to return the result.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/superprivacymode/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1006200001

 | 

General error.

 |
| 

1006200002

 | 

Internal error.

 |
| 

1006200005

 | 

This device is not support SuperPrivacy.

 |

**Example:**

import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
  hilog.info(DOMAIN, TAG, \`super privcy mode changed, mode = ${superPrivacyMode}\`);
}

hilog.info(DOMAIN, TAG, 'start register super privacy mode changed listener');
try {
  superPrivacyMode.on('superPrivacyModeChange', superPrivacyChangedCallback);
  hilog.info(DOMAIN, TAG, 'register super privacy mode change listener success');
} catch (err) {
  hilog.error(DOMAIN, TAG, \`register super privacy changed listener failed, ${JSON.stringify(err)}\`);
}

#### off('superPrivacyModeChange')

off(type: 'superPrivacyModeChange', callback?: Callback<SuperPrivacyMode>): void

Unsubscribes from Super Privacy status change events.

**System capability**: SystemCapability.Security.SecurityPrivacyServer

**Start version**: 6.0.2(22)

**Device behavior differences**: This API has no effect on TVs and wearables. On phones, PCs/2-in-1 devices, and tablets that support the Super Privacy option, this API functions properly. On phones, PCs/2-in-1 devices, and tablets that do not have the Super Privacy option, this API returns error code **1006200005**. When using this API, comply with the [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/devicesecurity-getsuperprivacymode#section19314125019324).

**Parameters:**

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

type

 | 

string

 | 

Yes

 | 

Event type to unsubscribe from. The value is fixed at **superPrivacyModeChange**.

 |
| 

callback

 | 

Callback<[SuperPrivacyMode](#section11705111513)\>

 | 

No

 | 

Callback function used to return the result.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/superprivacymode/document.md).

| 
Error Code

 | 

Message

 |
| :-- | :-- |
| 

1006200001

 | 

General error.

 |
| 

1006200002

 | 

Internal error.

 |
| 

1006200005

 | 

This device is not support SuperPrivacy.

 |

**Example:**

import { superPrivacyMode } from '@kit.DeviceSecurityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const DOMAIN = 0x0000;
const TAG = "SuperPrivacyModeTest";

const superPrivacyChangedCallback = (superPrivacyMode: superPrivacyMode.SuperPrivacyMode): void => {
  hilog.info(DOMAIN, TAG, \`super privcy mode changed, mode = ${superPrivacyMode}\`);
}

hilog.info(DOMAIN, TAG, 'start unregister super privacy mode changed listener');
try {
  superPrivacyMode.off('superPrivacyModeChange', superPrivacyChangedCallback);
} catch (err) {
  hilog.error(DOMAIN, TAG, \`unregister super privacy changed listener failed, ${JSON.stringify(err)}\`);
}
