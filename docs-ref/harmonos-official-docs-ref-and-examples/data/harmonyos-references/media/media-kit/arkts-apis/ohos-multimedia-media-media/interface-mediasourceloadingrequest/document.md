# Interface (MediaSourceLoadingRequest)

The MediaSourceLoadingRequest class defines a loading request object. Applications use this object to obtain the location of the requested resource and to interact with the player for data exchange.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/TmEHAOdsSZWX61hRH2GPew/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062437Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB7DAF3ECEC07813B99B5C46320CEA439FECF6AF005749F736A9FBB80EA5B240)

-   The initial APIs of this module are supported since API version 6. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 18.

#### Modules to Import

import { media } from '@kit.MediaKit';

#### Properties

**System capability**: SystemCapability.Multimedia.Media.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| url | string | No | No | 
Resource URL, which is the path to the resource that the application needs to open.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |
| header | Record<string, string> | No | Yes | 

HTTP request header. If the header exists, the application should set the header information in the HTTP request when downloading data.

**Atomic service API**: This API can be used in atomic services since API version 18.

 |

#### respondData18+

respondData(uuid: number, offset: number, buffer: ArrayBuffer): number

Sends data to the player.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uuid | number | Yes | ID for the resource handle. The source is [SourceOpenCallback](../types/document.md#sourceopencallback18). |
| offset | number | Yes | Offset of the current media data relative to the start of the resource. The value cannot be less than 0. |
| buffer | ArrayBuffer | Yes | 
Media data sent to the player.

**Note**: Do not transmit irrelevant data, as it can affect normal data parsing and playback.

 |

**Return value**

| Type | Description |
| :-- | :-- |
| number | 
Number of bytes received by the server.

\- A return value less than 0 indicates failure.

\- A return value of -2 indicates that the player no longer needs the current data, and the client should stop the current read process.

\- A return value of -3 indicates that the player's buffer is full, and the client should wait for the next read.

 |

**Example**

import { HashMap } from '@kit.ArkTS';
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let uuid = 1;

let request = requests.get(uuid);
let offset = 0; // Offset of the current media data relative to the start of the resource.
let buf = new ArrayBuffer(0); // Data defined by the application and pushed to the player.
let num = request?.respondData(uuid, offset, buf);

#### respondHeader18+

respondHeader(uuid: number, header?: Record<string, string>, redirectUrl?: string): void

Sends response header information to the player. This API must be called before the first call to [respondData](#responddata18).

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uuid | number | Yes | ID for the resource handle. The source is [SourceOpenCallback](../types/document.md#sourceopencallback18). |
| header | Record<string, string> | No | 
Header information in the HTTP response. The application can intersect the header fields with the fields supported by the underlying layer for parsing or directly pass in all corresponding header information.

\- The following fields need to be parsed by the underlying player: Transfer-Encoding, Location, Content-Type, Content-Range, Content-Encode, Accept-Ranges, and content-length.

 |
| redirectUrl | string | No | Redirect URL in the HTTP response. |

**Example**

import { HashMap } from '@kit.ArkTS';
let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let uuid = 1;

// The application fills this in as needed.
let header:Record<string, string> = {
  'Transfer-Encoding':'xxx',
  'Location' : 'xxx',
  'Content-Type' : 'xxx',
  'Content-Range' : 'xxx',
  'Content-Encode' : 'xxx',
  'Accept-Ranges' : 'xxx',
  'content-length' : 'xxx'
};
let request = requests.get(uuid);
request?.respondHeader(uuid, header);

#### finishLoading18+

finishLoading(uuid: number, state: LoadingRequestError): void

Notifies the player of the current request status. After pushing all the data for a single resource, the application should send the **LOADING\_ERROR\_SUCCESS** state to notify the player that the resource push is complete.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.Multimedia.Media.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| uuid | number | Yes | ID for the resource handle. The source is [SourceOpenCallback](../types/document.md#sourceopencallback18). |
| state | [LoadingRequestError](../enums/document.md#loadingrequesterror18) | Yes | Request status. |

**Example**

import { HashMap } from '@kit.ArkTS';

let requests: HashMap<number, media.MediaSourceLoadingRequest> = new HashMap();
let uuid = 1;

let request = requests.get(uuid);
let loadingError = media.LoadingRequestError.LOADING\_ERROR\_SUCCESS;
request?.finishLoading(uuid, loadingError);
