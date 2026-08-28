# Interface (ColorManagement)

**ColorManagement** inherits from [ColorManagementQuery](../interface-colormanagementquery/document.md).

It provides the APIs for color space settings.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/7U7iswl3RVyx0jzjUrYacA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062425Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EDAB2F99DB15398B0EE0E9E14B993C824E10F5C3157718CCEE3E4F3A4E67E65A)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 12.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### setColorSpace12+

setColorSpace(colorSpace: colorSpaceManager.ColorSpace): void

Sets a color space.

Before the setting, call [getSupportedColorSpaces](../interface-colormanagementquery/document.md#getsupportedcolorspaces12) to obtain the supported color spaces. You are advised to call this API after [addOutput](../interface-session/document.md#addoutput11) and before [commitConfig](../interface-session/document.md#commitconfig11-1). If this API is called after [commitConfig](../interface-session/document.md#commitconfig11-1), the camera session configuration will take a longer time.

**P3 and HDR Imaging**

An application can deliver different color space parameters to declare its support for P3 and HDR.

If an application does not proactively set the color space, SDR is used by default in photo and video recording modes.

To obtain HDR images in photo capture scenarios, set the color space to P3.

For different modes, enabling HDR, setting the color space, and configuring [CameraFormat](../enums/document.md#cameraformat) in the camera output stream [profile](../interfaces-others/document.md#profile) should match. For details, see the table below. For example, to enable HDR in video recording mode, set [CameraFormat](../enums/document.md#cameraformat) in the camera preview and video output stream [profiles](../interfaces-others/document.md#profile) to **CAMERA\_FORMAT\_YCRCB\_P010** and the color space to **BT2020\_HLG\_LIMIT**.

In video recording mode, if SDR or HDR VIVID is enabled, the camera format and color space must be configured according to the relationships specified in the table below. Configurations that do not match the table will cause issues such as preview exceptions.

**Recording Mode**

| SDR/HDR Photo Capture | CameraFormat | ColorSpace |
| :-- | :-- | :-- |
| SDR(Default) | CAMERA\_FORMAT\_YUV\_420\_SP | BT709\_LIMIT |
| HDR\_VIVID | CAMERA\_FORMAT\_YCRCB\_P010 | 
BT2020\_HLG\_LIMIT,

BT2020\_HLG

 |
| HDR\_VIVID | CAMERA\_FORMAT\_YCBCR\_P010 | 

BT2020\_HLG\_LIMIT,

BT2020\_HLG

 |

**Photo Mode**

| SDR/HDR Photo Capture | ColorSpace |
| :-- | :-- |
| SDR(Default) | SRGB |
| HDR | DISPLAY\_P3 |

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| colorSpace | [colorSpaceManager.ColorSpace](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspace) | Yes | Color space, which is obtained by calling [getSupportedColorSpaces](../interface-colormanagementquery/document.md#getsupportedcolorspaces12). |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400102 | The colorSpace does not match the format. |
| 7400103 | Session not config. |
| 7400201 | Camera service fatal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function setColorSpace(session: camera.PhotoSession, colorSpaces: Array<colorSpaceManager.ColorSpace>): void {
  if (colorSpaces === undefined || colorSpaces.length <= 0) {
    return;
  }
  try {
    session.setColorSpace(colorSpaces\[0\]);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The setColorSpace call failed, error code: ${err.code}\`);
  }
}

#### getActiveColorSpace12+

getActiveColorSpace(): colorSpaceManager.ColorSpace

Obtains the color space in use.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [colorSpaceManager.ColorSpace](../../../../../graphics/arkgraphics-2d/arkts-apis/ohos-graphics-colorspacemanager-color-space-management/document.md#colorspace) | Color space. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { colorSpaceManager } from '@kit.ArkGraphics2D';

function getActiveColorSpace(session: camera.PhotoSession): colorSpaceManager.ColorSpace | undefined {
  let colorSpace: colorSpaceManager.ColorSpace | undefined = undefined;
  try {
    colorSpace = session.getActiveColorSpace();
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The getActiveColorSpace call failed. error code: ${err.code}\`);
  }
  return colorSpace;
}
