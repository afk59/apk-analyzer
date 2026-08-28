# Interface (Photo)

Photo defines a full-quality image object.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a4/v3/WSnZso-AQtm5KvdUdLOWlA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062426Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FA8680E6A650CD445DDB068F526E871C2D19A3DADE1A391FC45B2F16CD028816)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### Properties

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| main11+ | [image.Image](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-image/document.md) | No | No | Full-quality image. |

#### release11+

release(): Promise<void>

Releases output resources. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Example**

async function releasePhoto(photo: camera.Photo): Promise<void> {
  await photo.release();
}
