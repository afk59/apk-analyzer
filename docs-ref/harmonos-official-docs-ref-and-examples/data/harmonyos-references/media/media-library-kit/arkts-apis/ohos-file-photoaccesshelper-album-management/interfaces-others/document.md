# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/t2gXmeYWTy2ofnL8unqXGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4B466808E8115642AC6B9EB8696DABEFE77CF6C173FC2E879D157AD9CAF010F5)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### MediaChangeRequest11+

Media change request, which is the parent class of the asset change request and album change request.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/aDwIBZ9VTAqNrFGa2M3AAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBE885ECC28B856FA2FB6104D6ECEA64804E23B0ED8C1B821C3E3DB430AF83ED)

**MediaChangeRequest** takes effect only after [applyChanges](../interface-photoaccesshelper/document.md#applychanges11) is called.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

#### CreateOptions

Options for creating an image or video asset.

The title must meet the following requirements:

-   It must not contain a file name extension.
-   The total length of the file name must be between 1 and 255 characters.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | Yes | 
Title of the image or video.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| subtype12+ | [PhotoSubtype](../enums/document.md#photosubtype12) | No | Yes | 

Subtype of the image or video file.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### FetchOptions

Defines the retrieval options.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| fetchColumns | Array<string> | No | No | 
Names of the columns specified for query.

If this parameter is left blank for photos, photos are fetched by **'uri'**, **'media\_type'**, **'subtype'**, and **'display\_name'** by default. An error will be thrown if [get](../interface-photoasset/document.md#get) is used to obtain other attributes of this object.

Example: **fetchColumns: \['uri', 'title'\]**.

If this parameter is left blank for albums, albums are fetched by **'uri'** and **'album\_name'** by default.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| predicates | [dataSharePredicates.DataSharePredicates](../../../../../application-framework/arkdata/arkts-apis/ohos-data-datasharepredicates-datashare-predicates/document.md#datasharepredicates) | No | No | 

Predicates that specify the fetch criteria.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### RequestOptions11+

Represents request options.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deliveryMode | [DeliveryMode](../enums/document.md#deliverymode11) | No | No | Delivery mode of the requested asset. The value can be **FAST\_MODE**, **HIGH\_QUALITY\_MODE**, or **BALANCE\_MODE**. |
| compatibleMode15+ | [CompatibleMode](../enums/document.md#compatiblemode15) | No | Yes | HDR video transcoding policy, which can be **FAST\_ORIGINAL\_FORMAT\_MODE** (maintaining the original HDR format) or **COMPATIBLE\_FORMAT\_MODE** (converting HDR content to SDR format). The default value is **FAST\_ORIGINAL\_FORMAT\_MODE**. |
| mediaAssetProgressHandler15+ | [MediaAssetProgressHandler](../interface-mediaassetprogresshandler/document.md) | No | Yes | Callback used to return the HDR-to-SDR conversion progress. |

#### ChangeData

Defines the return value of the listener callback.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [NotifyType](../enums/document.md#notifytype) | No | No | Notification type. |
| uris | Array<string> | No | No | All URIs with the same [NotifyType](../enums/document.md#notifytype), which can be **PhotoAsset** or **Album**. |
| extraUris | Array<string> | No | No | URIs of the changed files in the album. The value may be undefined. Check whether the value is undefined before using it. |

#### TextContextInfo12+

Represents the text information about the recommended images.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| text | string | No | Yes | Text based on which images are recommended. The text cannot exceed 250 characters. The default value is an empty string. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let textInfo: photoAccessHelper.TextContextInfo = {
      text: 'Pandas at Shanghai Wild Zoo'
    }
    let recommendOptions: photoAccessHelper.RecommendationOptions = {
      textContextInfo: textInfo
    }
    let options: photoAccessHelper.PhotoSelectOptions = {
      MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE,
      maxSelectNumber: 1,
      recommendationOptions: recommendOptions
    }
    let photoPicker = new photoAccessHelper.PhotoViewPicker();
    photoPicker.select(options).then((PhotoSelectResult: photoAccessHelper.PhotoSelectResult) => {
      console.info('PhotoViewPicker.select successfully, PhotoSelectResult uri: ' + JSON.stringify(PhotoSelectResult));
    }).catch((err: BusinessError) => {
      console.error(\`PhotoViewPicker.select failed with err: ${err.code}, ${err.message}\`);
    });
  } catch (error) {
    let err: BusinessError = error as BusinessError;
    console.error(\`PhotoViewPicker failed with err: ${err.code}, ${err.message}\`);
  }
}

#### PhotoCreationConfig12+

Represents the configuration for saving a media asset (image or video) to the media library, including the file name.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| title | string | No | Yes | 
Title of the image or video. If this parameter is not passed, the system generates a title. The title must meet the following requirements:

\- It must not contain a file name extension.

\- The total length of the file name, which is in the format of title+file name extension, must be between 1 and 255 characters.

\- It must not contain any invalid characters, which are:\\ / : \* ? " ' \` < > | { } \[ \]

 |
| fileNameExtension | string | No | No | File name extension, for example, **'jpg'**. |
| photoType | [PhotoType](../enums/document.md#phototype) | No | No | Type of the file to create, which can be **IMAGE** or **VIDEO**. See [PhotoType](../enums/document.md#phototype). |
| subtype | [PhotoSubtype](../enums/document.md#photosubtype12) | No | Yes | Image or video file subtype. The default value is **DEFAULT**. See [PhotoSubtype](../enums/document.md#photosubtype12). |

#### PhotoAssetChangeInfo20+

Describes the information about a media asset.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uri | string | No | No | URI of the media asset. |
| mediaType | [PhotoType](../enums/document.md#phototype) | No | No | Type of the media asset (image or video). |
| albumUri | string | No | No | URI of the album that the media asset belongs to. |

#### PhotoAssetChangeData20+

Describes the detailed change data of a media asset.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| assetBeforeChange | [PhotoAssetChangeInfo](#photoassetchangeinfo20) | null | No | No | Data of the media asset before change. In the case of asset addition, **assetBeforeChange** is null. |
| assetAfterChange | [PhotoAssetChangeInfo](#photoassetchangeinfo20) | null | No | No | Data of the media asset after change. In the case of asset deletion, **assetAfterChange** is null. |
| isContentChanged | boolean | No | No | Whether the content of the media asset is changed. **true** if changed, **false** otherwise. |
| isDeleted | boolean | No | No | Whether the media asset is deleted. **true** if deleted, **false** otherwise. |

#### PhotoAssetChangeInfos20+

Describes the notification information about the change of a media asset.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [NotifyChangeType](../enums/document.md#notifychangetype20) | No | No | Type of the media asset change. |
| assetChangeDatas | [PhotoAssetChangeData](#photoassetchangedata20)\[\] | null | No | No | Array of changed media assets. If all media assets need to be queried again, **assetChangeDatas** is null. |
| isForRecheck | boolean | No | No | 
Whether the application should query all media assets again. **true** if the application should query all assets again, **false** otherwise.

**NOTE**

In scenarios involving bulk asset operations or abnormal notifications, **isForRecheck** will be **true**. In this case, the application should query all assets again.

 |

#### AlbumChangeInfo20+

Describes the album information.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| albumType | [AlbumType](../enums/document.md#albumtype) | No | No | Type of the album. |
| albumSubtype | [AlbumSubtype](../enums/document.md#albumsubtype) | No | No | Subtype of the album. |
| albumName | string | No | No | Album name. |
| albumUri | string | No | No | URI of the album. |
| imageCount | number | No | No | Number of images in the album. |
| videoCount | number | No | No | Number of videos in the album. |
| count | number | No | No | Total number of assets in the album, including images and videos. |
| coverUri | string | No | No | URI of the album cover asset. |

#### AlbumChangeData20+

Describes the detailed change data of an album.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| albumBeforeChange | [AlbumChangeInfo](#albumchangeinfo20) | null | No | No | Data of the album before change. If an album is added, **albumBeforeChange** is null. |
| albumAfterChange | [AlbumChangeInfo](#albumchangeinfo20) | null | No | No | Data of the album after change. In the case of album deletion, **albumAfterChange** is null. |

#### AlbumChangeInfos20+

Describes the notification information about the change of an album.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| type | [NotifyChangeType](../enums/document.md#notifychangetype20) | No | No | Type of the album change. |
| albumChangeDatas | [AlbumChangeData](#albumchangedata20)\[\] | null | No | No | Array of changed albums. If all albums need to be queried again, **albumChangeDatas** is null. |
| isForRecheck | boolean | No | No | 
Whether the application should query all albums again. **true** if the application should query all albums again, **false** otherwise.

**NOTE**

In scenarios involving bulk album operations or abnormal notifications, **isForRecheck** will be **true**. In this case, the application should query all albums again.

 |
