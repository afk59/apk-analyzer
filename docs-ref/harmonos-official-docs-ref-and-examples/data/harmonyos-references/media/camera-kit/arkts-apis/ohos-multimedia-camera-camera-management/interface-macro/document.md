# Interface (Macro)

Macro inherits from [MacroQuery](../interface-macroquery/document.md).

It provides the API to enable macro photography.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/n8v2F_c_RMaVM96SkyTzdQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F25996CC8DC5EDAAD9D0726DB10EE622C00A6CFD05E1F51DE924B96C5CBCC621)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 19.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### enableMacro19+

enableMacro(enabled: boolean): void

Enables or disables macro photography.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/645G5V9wTkO9jOazuR3A1g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4CEEA32BF259DAF3EE456462213FF1904D53DFB1FFA3AE300F90C22D339A7DE4)

Before calling this API, call [isMacroSupported](../interface-macroquery/document.md#ismacrosupported19) to check whether the current device supports macro photography.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| enabled | boolean | Yes | Whether to enable macro photography. **true** to enable, **false** otherwise. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400102 | Operation not allowed. |
| 7400103 | Session not config. |

**Example**

function enableMacro(photoSession: camera.PhotoSession): void {
  let isSupported: boolean = photoSession.isMacroSupported();
  if (isSupported) {
    photoSession.enableMacro(true);
  }
}
