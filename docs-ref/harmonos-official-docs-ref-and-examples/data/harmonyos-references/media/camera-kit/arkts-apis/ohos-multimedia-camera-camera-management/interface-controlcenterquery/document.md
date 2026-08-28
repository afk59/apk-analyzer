# Interface (ControlCenterQuery)

ControlCenterQuery is used to check whether the camera controller is supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7d/v3/tF2_fTiMTjiPmspJTAdHyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=689CD9E1AB98E183F5FD119C742BEF7FD4CA2F63B32E825EABC1C2DF7DE0A94B)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 20.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### isControlCenterSupported20+

isControlCenterSupported(): boolean

Checks whether the camera controller is supported.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the camera controller. **true** if supported, **false** otherwise. |

**Example**

function isControlCenterSupported(videoSession: camera.VideoSession): boolean {
    let isSupported: boolean = videoSession.isControlCenterSupported();
    return isSupported;
}

#### getSupportedEffectTypes20+

getSupportedEffectTypes(): Array<ControlCenterEffectType>

Obtains the effect types supported by the camera controller.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[ControlCenterEffectType](../enums/document.md#controlcentereffecttype20)\> | Array of effect types supported. |

**Example**

function getSupportedEffectTypes(videoSession: camera.VideoSession): Array<camera.ControlCenterEffectType> {
    let effectTypes: Array<camera.ControlCenterEffectType> = \[\];
    effectTypes = videoSession.getSupportedEffectTypes();
    return effectTypes;
}
