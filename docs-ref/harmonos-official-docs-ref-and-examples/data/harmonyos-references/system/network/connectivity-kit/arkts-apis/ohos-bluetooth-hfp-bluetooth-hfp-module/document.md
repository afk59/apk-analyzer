# @ohos.bluetooth.hfp (Bluetooth HFP Module)

The **hfp** module provides the Bluetooth call audio capability based on the [Hands-Free Profile (HFP)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hfp)), such as obtaining the call audio connection status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/6unvA9ekSSu5Wn6SLhVaAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062341Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFCC18E50A9E8B88BA384F55A1853715E83F42CD489123370A63DB0F95420F27)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { hfp } from '@kit.ConnectivityKit';

#### BaseProfile

type BaseProfile = baseProfile.BaseProfile

**BaseProfile** class, which provides public capabilities such as obtaining the connection status and listening for connection status changes.

**System capability**: SystemCapability.Communication.Bluetooth.Core

| Type | Description |
| :-- | :-- |
| [baseProfile.BaseProfile](../ohos-bluetooth-baseprofile-bluetooth-baseprofile-module/document.md#baseprofile) | **BaseProfile** API definition. |

#### hfp.createHfpAgProfile

createHfpAgProfile(): HandsFreeAudioGatewayProfile

Creates an [HFP AG](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hfp-ag) instance. Through this instance, you can use the local device as the HFP AG and implement functions such as obtaining the Bluetooth call audio connection status.

**System capability**: SystemCapability.Communication.Bluetooth.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [HandsFreeAudioGatewayProfile](#handsfreeaudiogatewayprofile) | HFP AG instance. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter. Possible causes: 1. Mandatory parameters are left unspecified. 2. Incorrect parameter types. 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
    let hfpAgProfile = hfp.createHfpAgProfile();
    console.info('hfpAg success');
} catch (err) {
    console.error('errCode: ' + (err as BusinessError).code + ', errMessage: ' + (err as BusinessError).message);
}

#### HandsFreeAudioGatewayProfile

Represents the [HFP AG](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hfp-ag) role in Bluetooth call audio.

-   The **HandsFreeAudioGatewayProfile** class is inherited from [BaseProfile](#baseprofile). Therefore, you can use the APIs in its parent class.
-   Before using the APIs of this class, you need to construct an HFP AG instance by calling [createHfpAgProfile](#hfpcreatehfpagprofile).
-   The counterpart of the HFP AG role is the [HF](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/terminology#hf) role.
