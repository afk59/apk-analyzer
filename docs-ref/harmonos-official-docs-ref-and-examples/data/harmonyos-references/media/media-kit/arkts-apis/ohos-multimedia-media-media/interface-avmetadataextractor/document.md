# Interface (AVMetadataExtractor)

AVMetadataExtractor is a class for metadata retrieval. It provides APIs to obtain metadata and thumbnails from media assets. Before calling any API of AVMetadataExtractor, you must use [media.createAVMetadataExtractor](../functions/document.md#mediacreateavmetadataextractor11) to create an AVMetadataExtractor instance.

For details about the demo of obtaining audio or video metadata and video thumbnails, see [Using AVMetadataExtractor to Extract Audio and Video Metadata (ArkTS)](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/avmetadataextractor).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/-SewiIQWS_CWQ9N9qSBI6g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B49181017E43D9EAB4C0CC8F021860391C1C4670035F855CB7FE555016D7E53F)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 11.

#### Modules to Import

import { media } from '@kit.MediaKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fdSrc11+ | [AVFileDescriptor](../interfaces-others/document.md#avfiledescriptor9) | No | Yes | 
Media file descriptor, which specifies the data source. Before obtaining metadata, you must set the data source through either **fdSrc** or **dataSrc**.

**Example:**

There is a media file that stores continuous assets, the address offset is 0, and the byte length is 100. Its file descriptor is **AVFileDescriptor { fd = resourceHandle; offset = 0; length = 100; }**.

**NOTE**

After the resource handle (FD) is transferred to an AVMetadataExtractor instance, do not use the resource handle to perform other read and write operations, including but not limited to transferring this handle to other AVPlayer, AVMetadataExtractor, AVImageGenerator, or AVTranscoder instance. Competition occurs when multiple AVMetadataExtractor use the same resource handle to read and write files at the same time, resulting in errors in obtaining data.

 |
| dataSrc11+ | [AVDataSrcDescriptor](../interfaces-others/document.md#avdatasrcdescriptor10) | No | Yes | 

Streaming media resource descriptor, which specifies the data source. Before obtaining metadata, you must set the data source through either **fdSrc** or **dataSrc**.

When an application obtains a media file from the remote, you can set **dataSrc** to obtain the metadata before the application finishes the downloading.

 |

#### setUrlSource20+

setUrlSource(url: string, headers?: Record<string, string>): void

Sets the data source for a network on-demand resource. Only network metadata ([fetchMetadata](#fetchmetadata11)) and thumbnails ([fetchFrameByTime](#fetchframebytime20)) can be obtained. The media resource URL must be set before the retrieval.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| url | string | Yes | 
URL of the media resource.

1\. The video formats MP4, MPEG-TS, and MKV are supported.

2\. The audio formats M4A, AAC, MP3, OGG, WAV, FLAC, and AMR are supported.

**Example of supported URLs**:

1\. HTTP: http://xx

2\. HTTPS: https://xx

Note: HLS/DASH and live streaming resources cannot be set.

 |
| headers | Record<string, string> | No | Custom HTTP headers for accessing the network resource. The default value is empty. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;

media.createAVMetadataExtractor(async (error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor != null) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
    let url = "http://xx";
    let headers: Record<string, string> = {
      "User-Agent": "User-Agent-Value"
    };
    avMetadataExtractor.setUrlSource(url, headers);
  } else {
    console.error(\`Failed to create AVMetadataExtractor, error message:${error.message}\`);
  }
});

#### fetchFrameByTime20+

fetchFrameByTime(timeUs: number, options: AVImageQueryOptions, param: PixelMapParams): Promise<image.PixelMap>

Obtains a video thumbnail. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| timeUs | number | Yes | Time of the video for which a thumbnail is to be obtained, in us. |
| options | [AVImageQueryOptions](../enums/document.md#avimagequeryoptions12) | Yes | Relationship between the time passed in and the video frame. |
| param | [PixelMapParams](../interfaces-others/document.md#pixelmapparams12) | Yes | Format parameters of the thumbnail to be obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[image.PixelMap](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Promise used to return the video thumbnail. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |
| 5400108 | Parameter check failed. Returned by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

let avMetadataExtractor: media.AVMetadataExtractor | undefined = undefined;
let pixel\_map: image.PixelMap | undefined = undefined;

// Initialize input parameters.
let timeUs: number = 0;
let queryOption: media.AVImageQueryOptions = media.AVImageQueryOptions.AV\_IMAGE\_QUERY\_PREVIOUS\_SYNC;
let param: media.PixelMapParams = {
  width: 300,
  height: 300
};
// Obtain the thumbnail.
media.createAVMetadataExtractor((error: BusinessError, extractor: media.AVMetadataExtractor) => {
  if (extractor != null) {
    avMetadataExtractor = extractor;
    console.info('Succeeded in creating AVMetadataExtractor');
    avMetadataExtractor.fetchFrameByTime(timeUs, queryOption, param).then((pixelMap: image.PixelMap) => {
      pixel\_map = pixelMap;
    }).catch((error: BusinessError) => {
      console.error(\`Failed to fetch FrameByTime, error message:${error.message}\`);
    });
  } else {
    console.error(\`Failed to create AVMetadataExtractor, error message:${error.message}\`);
  }
});

#### fetchMetadata11+

fetchMetadata(callback: AsyncCallback<AVMetadata>): void

Obtains the media metadata. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[AVMetadata](../interfaces-others/document.md#avmetadata11)\> | Yes | Callback used to return the result, which is an AVMetadata instance. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Returned by callback. |
| 5400106 | Unsupported format. Returned by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.fetchMetadata((error: BusinessError, metadata: media.AVMetadata) => {
    if (error) {
      console.error(\`Failed to fetch Metadata, err = ${JSON.stringify(error)}\`);
      return;
    }
    console.info(\`Succeeded in fetching Metadata, genre: ${metadata.genre}\`);
  });
}

#### fetchMetadata11+

fetchMetadata(): Promise<AVMetadata>

Obtains the media metadata. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[AVMetadata](../interfaces-others/document.md#avmetadata11)\> | Promise used to return the result, which is an AVMetadata instance. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.fetchMetadata().then((metadata: media.AVMetadata) => {
    console.info(\`Succeeded in fetching Metadata, genre: ${metadata.genre}\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to fetch Metadata, error message:${error.message}\`);
  });
}

#### fetchAlbumCover11+

fetchAlbumCover(callback: AsyncCallback<image.PixelMap>): void

Obtains the cover of the audio album. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<[image.PixelMap](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Yes | Callback used to return the album cover. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Return by callback. |
| 5400106 | Unsupported format. Returned by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  let pixel\_map: image.PixelMap | undefined = undefined;

  avMetadataExtractor.fetchAlbumCover((error: BusinessError, pixelMap: image.PixelMap) => {
    if (error) {
      console.error(\`Failed to fetch AlbumCover, error = ${JSON.stringify(error)}\`);
      return;
    }
    pixel\_map = pixelMap;
  });
}

#### fetchAlbumCover11+

fetchAlbumCover(): Promise<image.PixelMap>

Obtains the cover of the audio album. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[image.PixelMap](../../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Promise used to return the album cover. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Returned by promise. |
| 5400106 | Unsupported format. Returned by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  let pixel\_map: image.PixelMap | undefined = undefined;

  avMetadataExtractor.fetchAlbumCover().then((pixelMap: image.PixelMap) => {
    pixel\_map = pixelMap;
  }).catch((error: BusinessError) => {
    console.error(\`Failed to fetch AlbumCover, error message:${error.message}\`);
  });
}

#### release11+

release(callback: AsyncCallback<void>): void

Releases this AVMetadataExtractor instance. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| callback | AsyncCallback<void> | Yes | Callback used to return the result. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Returned by callback. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release((error: BusinessError) => {
    if (error) {
      console.error(\`Failed to release, err = ${JSON.stringify(error)}\`);
      return;
    }
    console.info(\`Succeeded in releasing.\`);
  });
}

#### release11+

release(): Promise<void>

Releases this AVMetadataExtractor instance. This API uses a promise to return the result.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Media Error Codes](../../../error-codes/media-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 5400102 | Operation not allowed. Returned by promise. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { media } from '@kit.MediaKit';

async function test() {
  // Create an AVMetadataExtractor instance.
  let avMetadataExtractor: media.AVMetadataExtractor = await media.createAVMetadataExtractor();
  avMetadataExtractor.release().then(() => {
    console.info(\`Succeeded in releasing.\`);
  }).catch((error: BusinessError) => {
    console.error(\`Failed to release, error message:${error.message}\`);
  });
}
