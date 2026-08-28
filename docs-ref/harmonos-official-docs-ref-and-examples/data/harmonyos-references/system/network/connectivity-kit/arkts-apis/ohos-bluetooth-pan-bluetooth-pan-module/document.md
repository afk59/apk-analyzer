# @ohos.bluetooth.pan (Bluetooth PAN Module)

The **pan** module implements Bluetooth-based network sharing through Bluetooth Classic's [Personal Area Networking (PAN)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#pan), such as obtaining the network connection status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/3MBbAQO7Q-SaOBoh5soqMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2B192D68654CB375FB937C1712D4241D26958D41B6D0822699DBF681D771A754)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { pan } from '@kit.ConnectivityKit';

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

**BaseProfile** class, which provides public capabilities such as obtaining the connection status and listening for connection status changes.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [baseProfile.BaseProfile](../ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofile) | **BaseProfile** API definition. |

#### pan.createPanProfile

createPanProfile(): PanProfile

Creates a Bluetooth [NAP](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#nap) instance. Through this instance, you can use the local device as the NAP and implement functions such as obtaining the PAN service connection status.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| PanProfile | 
NAP instance.

\- The **PanProfile** class is inherited from [BaseProfile](#baseprofile). Therefore, you can use the APIs in its parent class.

\- The counterpart of the NAP role is the [PANU](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#panu) role.

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
    let panProfile : pan.PanProfile= pan.createPanProfile();
    console.info('pan success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}
