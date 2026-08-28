# @ohos.bluetooth.map (Bluetooth MAP Module)

The **map** module provides Bluetooth message access capability based on [Message Access Profile (MAP)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#map), and supports functions such as obtaining the connection status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/rV6IWzE4SwGNpGFm5t11HQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=466B7526AD86EEA60C7BD6F9AAD9485092226D5FD47956807F6FC0901B39FBAE)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { map } from '@kit.ConnectivityKit';

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

**BaseProfile** class, which provides public capabilities such as obtaining the connection status and listening for connection status changes.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [baseProfile.BaseProfile](../ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofile) | **BaseProfile** API definition. |

#### map.createMapMseProfile

createMapMseProfile(): MapMseProfile

Creates a [Message Server Equipment (MSE)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#mse) instance. Through this instance, you can use the local device as the MSE and implement functions such as obtaining the Bluetooth message service connection status of the local device.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| MapMseProfile | **MapMseProfile** instance created. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let mapMseProfile = map.createMapMseProfile();
    console.info('MapMse success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### MapMseProfile

Represents the [MSE](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#mse) role in MAP.

-   The **MapMseProfile** class is inherited from [BaseProfile](#baseprofile). Therefore, you can use the APIs in its parent class.
-   Before using the APIs of this class, you need to construct an MSE instance by calling [createMapMseProfile](#mapcreatemapmseprofile).
-   The counterpart of the MSE role is the [MCE](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#mce) role.
