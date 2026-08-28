# Interface (ColorManagementQuery)

ColorManagementQuery provides the APIs for color space query.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1b/v3/JdESShjKSweR8w4Z0tdlVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4FEBE17958FB77E92D1BB461FCAFBB0A8D361CC328EBD45E46B2EFA1A92DE135)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 12.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### getSupportedColorSpaces12+

getSupportedColorSpaces(): Array<colorSpaceManager.ColorSpace>

Obtains the supported color spaces.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<[colorSpaceManager.ColorSpace](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspace)\> | Array of color spaces supported. If the API call fails, undefined is returned. |

**Example**

import { colorSpaceManager } from '@kit.ArkGraphics2D';

function getSupportedColorSpaces(session: camera.PhotoSession): Array<colorSpaceManager.ColorSpace> {
  let colorSpaces: Array<colorSpaceManager.ColorSpace> = \[\];
  colorSpaces = session.getSupportedColorSpaces();
  return colorSpaces;
}
