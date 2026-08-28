# Interface (AutoDeviceSwitchQuery)

**AutoDeviceSwitchQuery** is used to check whether a device supports automatic camera switch.

[Automatic Camera Switching](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/camera-auto-switch) is supported only on foldable devices. For details about how to enable this capability, see [enableAutoDeviceSwitch](../interface-autodeviceswitch/document.md#enableautodeviceswitch13).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e3/v3/H2CL3jZ7TnCj15Z1aDpcMw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=355CE93D09867CC2C6092F3BD868AE87809EED200BD736C868687D99EB05E7E9)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 13.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### isAutoDeviceSwitchSupported13+

isAutoDeviceSwitchSupported(): boolean

Checks whether the device supports automatic camera switch.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of automatic camera switch. **true** if supported, **false** otherwise. |

**Example**

// Check whether the foldable device supports automatic camera switch.
// If the sample code returns \*\*true\*\*, you can continue to use enableAutoDeviceSwitch to enable automatic camera switching.
function isAutoDeviceSwitchSupported(session: camera.PhotoSession): boolean {
  let isSupported = false;
  isSupported = session.isAutoDeviceSwitchSupported();
  return isSupported;
}
