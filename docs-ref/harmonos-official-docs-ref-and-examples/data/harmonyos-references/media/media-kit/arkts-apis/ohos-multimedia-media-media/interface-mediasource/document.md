# Interface (MediaSource)

The MediaSource class defines the media data information, which is from [createMediaSourceWithUrl](../functions/document.md#mediacreatemediasourcewithurl12).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/FzMXcMvMQNybgeo_81YmIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6F06555AAA5C39C821DAE1319949E007C6457F42C56A613623B942F64A394D5C)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 12.

#### Modules to Import

import { media } from '@kit.MediaKit';

#### setMimeType12+

setMimeType(mimeType: AVMimeTypes): void

Sets the MIME type to help the player process extended media sources.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mimeType | [AVMimeTypes](../enums/document.md#avmimetypes12) | Yes | MIME type. |

#### setMediaResourceLoaderDelegate18+

setMediaResourceLoaderDelegate(resourceLoader: MediaSourceLoader): void

Sets a MediaSourceLoader object, which is used to help the player request media data.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resourceLoader | [MediaSourceLoader](../interfaces-others/document.md#mediasourceloader18) | Yes | **MediaSourceLoader** object used to obtain media data for the player. |

**Example**

import { HashMap } from '@kit.ArkTS';
import { media } from '@kit.MediaKit';

let headers: Record<string, string> = {"User-Agent" : "User-Agent-Value"};
let mediaSource : media.MediaSource = media.createMediaSourceWithUrl("http://xxx",  headers);
let uuid: number = 1;
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();

let sourceOpenCallback: media.SourceOpenCallback = (request: media.MediaSourceLoadingRequest) => {
  console.info(\`Opening resource: ${request.url}\`);
  // Open the resource and return a unique handle, ensuring the mapping between the UUID and request.
  uuid += 1;
  requests.set(uuid, request);
  return uuid;
};

let sourceReadCallback: media.SourceReadCallback = (uuid: number, requestedOffset: number, requestedLength: number) => {
  console.info(\`Reading resource with handle ${uuid}, offset: ${requestedOffset}, length: ${requestedLength}\`);
  // Check whether the UUID is valid and store the read request. Avoid blocking the request while pushing data and header information.
};

let sourceCloseCallback: media.SourceCloseCallback = (uuid: number) => {
  console.info(\`Closing resource with handle ${uuid}\`);
  // Clear resources related to the current UUID.
  requests.remove(uuid);
};

// Implemented by applications as required.
let resourceLoader: media.MediaSourceLoader = {
  open: sourceOpenCallback,
  read: sourceReadCallback,
  close: sourceCloseCallback
};

mediaSource.setMediaResourceLoaderDelegate(resourceLoader);
