# Interface (ZoomQuery)

ZoomQuery provides APIs to query the zoom feature of a device camera, including the API to obtain the supported zoom ratio range.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ec/v3/5oENNpfqQ9migBK8AJKApA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9EF2EFE6C75C1E62320C7D74D08340C0BA5865DE8676F3D0091F4D08602A0B27)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   This interface was first introduced in API version 12. In this version, a compatibility change was made that preserved the initial version information of inner elements. As a result, you might see outer element's @since version number being higher than that of the inner elements. However, this discrepancy does not affect the functionality of the interface.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### getZoomRatioRange11+

getZoomRatioRange(): Array<number>

Obtains the supported zoom ratio range.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Array containing the minimum and maximum zoom ratios. If the operation fails, undefined is returned and an error code defined in [CameraErrorCode](../enums/document.md#cameraerrorcode) is thrown. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config, only throw in session usage. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getZoomRatioRange(photoSession: camera.PhotoSession): Array<number> {
  let zoomRatioRange: Array<number> = \[\];
  try {
    zoomRatioRange = photoSession.getZoomRatioRange();
  } catch (error) {
    // If the operation fails, error.code is returned and processed.
    let err = error as BusinessError;
    console.error(\`The getZoomRatioRange call failed. error code: ${err.code}\`);
  }
  return zoomRatioRange;
}
