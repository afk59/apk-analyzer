# @ohos.bluetooth.pbap (Bluetooth PBAP Module)

The **pbap** module implements phone book access capabilities based on the [Phone Book Access Profile (PBAP)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#pbap), such as obtaining the phone book service connection status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a/v3/zqtyMxrWQHuI4cujmUwY2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F0A21666A30E359AE4CB36861B3EE5D9B3DCBD95CBF2B61D2821906F1DD5D0A2)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { pbap } from '@kit.ConnectivityKit';

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

**BaseProfile** class, which provides public capabilities such as obtaining the connection status and listening for connection status changes.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [baseProfile.BaseProfile](../ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofile) | **BaseProfile** API definition. |

#### pbap.createPbapServerProfile

createPbapServerProfile(): PbapServerProfile

Creates a [PSE](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#pse) instance. Through this instance, you can use the local device as the PSE and implement functions such as obtaining the phone book service connection status.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| PbapServerProfile | 
PSE instance.

\- The **PbapServerProfile** class is inherited from [BaseProfile](#baseprofile). Therefore, you can use the APIs in its parent class.

\- The counterpart of the PSE role is the [PCE](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#pce) role.

 |

**Error codes**

For details about the error codes, see [Bluetooth Error Codes](../../error-codes/bluetooth-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let pbapServerProfile = pbap.createPbapServerProfile();
    console.info('pbapServer success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
