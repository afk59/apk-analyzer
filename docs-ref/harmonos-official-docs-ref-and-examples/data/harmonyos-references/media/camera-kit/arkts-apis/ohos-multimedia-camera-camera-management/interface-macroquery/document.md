# Interface (MacroQuery)

MacroQuery provides the API to check the support for macro photography.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/pJ_qtUzBT_qck_QmjxHSHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=438C58B60BB240EC502D55E5256B97A1B8F38C6B374FAEAC4D1B717FC7CF466F)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 19.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### isMacroSupported19+

isMacroSupported(): boolean

Checks whether macro photography is supported in the current state. This API must be called after [commitConfig](../interface-session/document.md#commitconfig11).

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of macro photography. **true** if supported, **false** otherwise. |

**Example**

function isMacroSupported(photoSession: camera.PhotoSession): boolean {
  let isSupported: boolean = photoSession.isMacroSupported();
  return isSupported;
}
