# Interface (MediaAssetDataHandler)

MediaAssetDataHandler is a media asset handler used to customize the media asset processing logic in **onDataPrepared**.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/nQgpXaEZQUGZuYYxcOAD_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062442Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=88FCE3D1471347AA75FB9224F737DCB7148714ED80F41328A796814AF108A430)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### onDataPrepared11+

onDataPrepared(data: T, map?: Map<string, string>): void

Called when the requested media asset is ready. If an error occurs, **data** returned by the callback is **undefined**. Each media asset request corresponds to a callback.

T supports the following data types: ArrayBuffer, [ImageSource](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-imagesource/document.md), [MovingPhoto](../interface-movingphoto/document.md), and boolean. ArrayBuffer indicates the image or video asset data, [ImageSource](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-imagesource/document.md) indicates the image source, [MovingPhoto](../interface-movingphoto/document.md) indicates a moving photo object, and boolean indicates whether the image or video is successfully written to the application sandbox directory.

Information returned by **map**:

| Map Key | Description |
| :-- | :-- |
| 'quality' | Image quality. The value **high** means high quality, and **low** means poor quality. |

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| data | T | Yes | Data of the image asset that is ready. It is of the generic type and supports the following data types: ArrayBuffer, [ImageSource](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-imagesource/document.md), [MovingPhoto](../interface-movingphoto/document.md), and boolean. |
| map12+ | Map<string, string> | No | Additional information about the image asset, such as the image quality. Currently, only **quality** is supported. |

**Example**

import { image } from '@kit.ImageKit';

class MediaHandler implements photoAccessHelper.MediaAssetDataHandler<image.ImageSource> {
  onDataPrepared = (data: image.ImageSource, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // Customize the processing logic for ImageSource.
    console.info('on image data prepared, photo quality is ' + map\['quality'\]);
  }
}

class MediaDataHandler implements photoAccessHelper.MediaAssetDataHandler<ArrayBuffer> {
  onDataPrepared = (data: ArrayBuffer, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // Customize the processing logic for ArrayBuffer.
    console.info('on image data prepared, photo quality is ' + map\['quality'\]);
  }
}

class MovingPhotoHandler implements photoAccessHelper.MediaAssetDataHandler<photoAccessHelper.MovingPhoto> {
  onDataPrepared = (data: photoAccessHelper.MovingPhoto, map: Map<string, string>) => {
    if (data === undefined) {
      console.error('Error occurred when preparing data');
      return;
    }
    // Customize the processing logic for MovingPhoto.
    console.info('on image data prepared, photo quality is ' + map\['quality'\]);
  }
}
