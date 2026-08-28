# Interface (AutoDeviceSwitch)

**AutoDeviceSwitch** inherits from [AutoDeviceSwitchQuery](../interface-autodeviceswitchquery/document.md) and is used to enable or disable automatic camera switch. This capability can be used only on foldable devices. For details about the development, see [Practices for Automatic Camera Switching (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-auto-switch).

It is recommended that the system automatically handle input device switching, session configuration, and parameter continuity during automatic camera switch. If the system detects that the zoom ranges of the two cameras are different during camera switching, it will notify the application through the **isDeviceCapabilityChanged** field in [AutoDeviceSwitchStatus](../interfaces-others/document.md#autodeviceswitchstatus13). However, the application still needs to handle the UX change. For example, for the zoom range adjustment, the application needs to call [getZoomRatioRange](../interface-zoomquery/document.md#getzoomratiorange11) to obtain data and update the UX. Therefore, **AutoDeviceSwitch** is more applicable to simplified UX interactions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/DaVvs1-ES1CaRWGDB3trug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E63BDF9D999A948DA8A0598B82BA5BACF8EDCFC766D27ECF3124A9F9CCC7A072)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 13.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### enableAutoDeviceSwitch13+

enableAutoDeviceSwitch(enabled: boolean): void

Enables or disables automatic camera switch. You can use [isAutoDeviceSwitchSupported](../interface-autodeviceswitchquery/document.md#isautodeviceswitchsupported13) to check whether the device supports automatic camera switch.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/eGWYc-8_SSCLVfhtME0B9w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B334132057DFFF9A696406C516D9F8BF2EFDAC9F941DDE2CF6E6CA0BE8AA5FBF)

This API is used only for foldable devices with multiple front cameras. In different fold states, the system can automatically switch to an available front camera. It does not enable automatic switching between front and rear cameras.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable automatic camera switch. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameters verification failed. |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function enableAutoDeviceSwitch(session: camera.PhotoSession, isEnable: boolean): void {
  try {
    session.enableAutoDeviceSwitch(isEnable);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The enableAutoDeviceSwitch call failed, error code: ${err.code}, error message: ${err.message}\`);
  }
}
