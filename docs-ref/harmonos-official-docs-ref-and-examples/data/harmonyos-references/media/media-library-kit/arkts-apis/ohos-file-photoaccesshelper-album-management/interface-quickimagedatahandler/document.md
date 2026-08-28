# Interface (QuickImageDataHandler)

QuickImageDataHandler is a media asset handler used to customize the media asset processing logic in **onDataPrepared**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/JhC8QiEUQX61MhC7JxO1Jw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5D0728A9970E42FDD2841FE12F87B292094D16418D471D785DD92F9A3A31D1D6)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 13.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### onDataPrepared13+

onDataPrepared(data: T, imageSource: image.ImageSource, map: Map<string, string>): void

Called when the requested image is ready. If an error occurs, **data** returned by the callback is **undefined**.

Information returned by **map**:

| Map Key | **Description** |
| :-- | :-- |
| 'quality' | Image quality. The value **high** means high quality, and **low** means poor quality. |

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | T | Yes | Data of the image asset that is ready. It is of the generic type and supports the [Picture](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-picture/document.md) type. |
| imageSource | image.ImageSource | Yes | Data of the image asset that is ready. |
| map13+ | Map<string, string> | Yes | Additional information about the image asset, such as the image quality. Currently, only **quality** is supported. |

**Example**

import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.QuickImageDataHandler<image.Picture> {
  onDataPrepared(data: image.Picture, imageSource: image.ImageSource, map: Map<string, string>) {
    console.info('on image data prepared');
  }
}
