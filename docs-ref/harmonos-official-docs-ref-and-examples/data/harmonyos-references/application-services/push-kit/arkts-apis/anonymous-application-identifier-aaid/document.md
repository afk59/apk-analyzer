# Anonymous Application Identifier (AAID)

This module provides the capabilities for obtaining and deleting AAIDs, which are used to identify apps.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Start version**: 4.0.0(10)

#### Module Import

import { AAID } from '@kit.PushKit';

#### AAID.getAAID

getAAID(callback: AsyncCallback<string>): void

Obtains an AAID. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

callback

 | 

AsyncCallback<string>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined**, and **data** is the obtained AAID, which contains 36 characters; otherwise, **err** is an error object.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900006

 | 

Failed to connect to the AAID service.

 |
| 

1000900007

 | 

Internal error of the AAID service.

 |

**Example**:

import { AAID } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  AAID.getAAID((err: BusinessError, data: string) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in getting AAID');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', e.code, e.message);
}

#### AAID.getAAID

getAAID(): Promise<string>

Obtains an AAID. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

AAID returned through a promise, which contains 36 characters.

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

1000900001

 | 

System internal error.

 |
| 

1000900006

 | 

Failed to connect to the AAID service.

 |
| 

1000900007

 | 

Internal error of the AAID service.

 |

**Example**:

import { AAID } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  AAID.getAAID().then((data: string) => {
    hilog.info(0x0000, 'testTag', 'Succeeded in getting AAID');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to get AAID: %{public}d %{public}s', e.code, e.message);
}

#### AAID.deleteAAID

deleteAAID(callback: AsyncCallback<void>): void

Deletes an AAID. This API returns the result asynchronously through a callback.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

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

Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types.

 |
| 

1000900001

 | 

System internal error.

 |
| 

1000900006

 | 

Failed to connect to the AAID service.

 |
| 

1000900007

 | 

Internal error of the AAID service.

 |

**Example**:

import { AAID } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  AAID.deleteAAID((err: BusinessError) => {
    if (err) {
      hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', err.code, err.message);
    } else {
      hilog.info(0x0000, 'testTag', 'Succeeded in deleting AAID.');
    }
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', e.code, e.message);
}

#### AAID.deleteAAID

deleteAAID(): Promise<void>

Deletes an AAID. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**System capability**: SystemCapability.Push.PushService

**Device behavior differences**: For versions earlier than 5.1.0(18), this API is supported on phones, tablets, and PCs/2-in-1 devices, but does not work on other devices. For version 5.1.0(18), this API is supported on phones, tablets, PCs/2-in-1 devices, and wearables, but does not work on other devices. For version 5.1.1(19) or later, this API is supported on phones, tablets, PCs/2-in-1 devices, wearables, and TVs.

**Start version**: 4.0.0(10)

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

**Promise** object. No result is returned.

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

1000900001

 | 

System internal error.

 |
| 

1000900006

 | 

Failed to connect to the AAID service.

 |
| 

1000900007

 | 

Internal error of the AAID service.

 |

**Example**:

import { AAID } from '@kit.PushKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  AAID.deleteAAID().then(() => {
    hilog.info(0x0000, 'testTag', 'Succeeded in deleting AAID');
  }).catch((err: BusinessError) => {
    hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', err.code, err.message);
  });
} catch (err) {
  let e: BusinessError = err as BusinessError;
  hilog.error(0x0000, 'testTag', 'Failed to delete AAID: %{public}d %{public}s', e.code, e.message);
}
