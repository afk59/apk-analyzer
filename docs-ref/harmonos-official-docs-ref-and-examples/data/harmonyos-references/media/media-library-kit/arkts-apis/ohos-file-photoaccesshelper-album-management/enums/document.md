# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/jMYUkT1jQ7SQ_IjWhTh4nQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062443Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=92C7F6FDF021DD69AAC841D6E36F19B2A9416209FD65488013EE685690DDC491)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { photoAccessHelper } from '@kit.MediaLibraryKit';

#### PhotoType

Enumerates the media file types.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| IMAGE | 1 | Image. |
| VIDEO | 2 | Video. |

#### PhotoSubtype12+

Enumerates the [PhotoAsset](../interface-photoasset/document.md) types.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | Photo, which is the default type. |
| MOVING\_PHOTO | 3 | Moving photo. |
| BURST | 4 | Burst photo. |

#### DynamicRangeType12+

Enumerates the dynamic range types of media assets.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| SDR | 0 | Standard dynamic range (SDR). |
| HDR | 1 | High dynamic range (HDR). |

#### AlbumType

Enumerates the album types, for example, user albums, system albums, or albums created by an application.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| USER | 0 | User album. |
| SYSTEM | 1024 | System album. |

#### AlbumSubtype

Enumerate the album subtypes.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| USER\_GENERIC | 1 | User album. |
| FAVORITE | 1025 | Favorites. |
| VIDEO | 1026 | Video album. |
| IMAGE12+ | 1031 | Photo album. |
| ANY | 2147483647 | Any album. |

#### PositionType16+

Enumerates the file locations.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| LOCAL | 1 | Stored only on a local device. |
| CLOUD | 2 | Stored only on the cloud. |
| LOCAL\_AND\_CLOUD | 3 | Stored both on a local device and cloud. |

#### PhotoKeys

Enumerates the keys available for image or video files.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| URI | 'uri' | 
URI of the file.

**Note**:

Only the [DataSharePredicates.equalTo](../../../../../application-framework/arkdata/arkts-apis/ohos-data-datasharepredicates-datashare-predicates/document.md#equalto10) predicate can be used for this field during photo query.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| PHOTO\_TYPE | 'media\_type' | 

Type of the file.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DISPLAY\_NAME | 'display\_name' | 

File name displayed. The file name must meet the following requirements:

\- A valid file name must include a base name and a supported image or video extension.

\- The file name length ranges from 1 to 255.

\- The base name must not contain any invalid characters, which are:.. \\ / : \* ? " ' \` < > | { } \[ \]

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| SIZE | 'size' | 

File size, in bytes. The size of a moving photo includes the total size of the image and video.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DATE\_ADDED | 'date\_added' | 

Unix timestamp when the file was created, in seconds.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DATE\_MODIFIED | 'date\_modified' | 

Unix timestamp when the file content (not the file name) was last modified, in seconds. This value is updated when the file content is modified, but not when the file name is modified.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DURATION | 'duration' | 

Duration, in ms.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| WIDTH | 'width' | 

Image width, in pixels.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| HEIGHT | 'height' | 

Image height, in pixels.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DATE\_TAKEN | 'date\_taken' | 

Unix timestamp when the photo was taken, in seconds.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| ORIENTATION | 'orientation' | 

Orientation of the file, in degrees.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| FAVORITE | 'is\_favorite' | 

Whether the file is marked as favorites.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| TITLE | 'title' | 

Title of the file.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DATE\_ADDED\_MS12+ | 'date\_added\_ms' | 

Unix timestamp when the file was created, in milliseconds.

**Note**:

The photos queried cannot be sorted based on this field.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DATE\_MODIFIED\_MS12+ | 'date\_modified\_ms' | 

Unix timestamp when the file was modified, in milliseconds. This value is updated when the file content is modified, but not when the file name is modified.

**Note**:

The photos queried cannot be sorted based on this field.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| PHOTO\_SUBTYPE12+ | 'subtype' | 

Subtype of the media file.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DYNAMIC\_RANGE\_TYPE12+ | 'dynamic\_range\_type' | 

Dynamic range type of the media asset.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| COVER\_POSITION12+ | 'cover\_position' | 

Position of the moving photo cover, which is the video timestamp (in μs) corresponding to the cover frame.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| BURST\_KEY12+ | 'burst\_key' | 

Unique ID of a group of burst photos.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| LCD\_SIZE12+ | 'lcd\_size' | 

Width and height of an LCD image, in the format of a **width:height** string.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| THM\_SIZE12+ | 'thm\_size' | 

Width and height of a thumbnail image, in the format of a **width:height** string.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DETAIL\_TIME13+ | 'detail\_time' | 

Detailed time. The value is a string of time when the image or video was taken in the time zone and does not change with the time zone.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| DATE\_TAKEN\_MS13+ | 'date\_taken\_ms' | 

Unix timestamp when the image was captured, in milliseconds.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| POSITION16+ | 'position' | 

File location type.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| MEDIA\_SUFFIX18+ | 'media\_suffix' | File name extension. |
| OWNER\_ALBUM\_ID22+ | 'owner\_album\_id' | ID of the album to which the photo belongs. |
| ASPECT\_RATIO22+ | 'aspect\_ratio' | 

Aspect ratio of the image or video.

**Model restriction**: This API can be used only in the stage model.

 |

#### AlbumKeys

Enumerates the album keys.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| URI | 'uri' | URI of the album. |
| ALBUM\_NAME | 'album\_name' | Name of the album. |

#### ResourceType11+

Enumerates the types of the resources to write.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| IMAGE\_RESOURCE | 1 | Image resource. |
| VIDEO\_RESOURCE | 2 | Video resource. |

#### ImageFileType13+

Enumerates the types of image files to save.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| JPEG | 1 | JPEG. |
| HEIF | 2 | HEIF. |

#### NotifyType

Enumerates the notification event types.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NOTIFY\_ADD | 0 | A file asset or album is added. |
| NOTIFY\_UPDATE | 1 | A file asset or album is updated. |
| NOTIFY\_REMOVE | 2 | A file asset or album is removed. |
| NOTIFY\_ALBUM\_ADD\_ASSET | 3 | A file asset is added to the album. |
| NOTIFY\_ALBUM\_REMOVE\_ASSET | 4 | A file asset is removed from the album. |

#### DefaultChangeUri

Enumerates the **DefaultChangeUri** subtypes.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT\_PHOTO\_URI | 'file://media/Photo' | Default **PhotoAsset** URI, which must be used with **forChildUris{true}** to subscribe to change notifications of all photo assets. |
| DEFAULT\_ALBUM\_URI | 'file://media/PhotoAlbum' | Default album URI, which must be used with **forChildUris{true}** to subscribe to change notifications of all albums. |

#### PhotoViewMIMETypes

Enumerates the media file types.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| IMAGE\_TYPE | 'image/\*' | 
Image.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| VIDEO\_TYPE | 'video/\*' | 

Video.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| IMAGE\_VIDEO\_TYPE | '\*/\*' | 

Image and video.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| MOVING\_PHOTO\_IMAGE\_TYPE12+ | 'image/movingPhoto' | 

Moving photo.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

#### RecommendationType11+

Enumerates the types of recommended images.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| QR\_OR\_BAR\_CODE | 1 | 
QR code or barcode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| QR\_CODE | 2 | 

QR code.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| BAR\_CODE | 3 | 

Barcode.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| ID\_CARD | 4 | 

ID card.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PROFILE\_PICTURE | 5 | 

Profile.

**Atomic service API**: This API can be used in atomic services since API version 11.

 |
| PASSPORT12+ | 6 | 

Passport.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| BANK\_CARD12+ | 7 | 

Bank card.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DRIVER\_LICENSE12+ | 8 | 

Driver license.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| DRIVING\_LICENSE12+ | 9 | 

Vehicle license.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |
| FEATURED\_SINGLE\_PORTRAIT12+ | 10 | 

Recommended portrait.

**Atomic service API**: This API can be used in atomic services since API version 12.

 |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

async function example(phAccessHelper: photoAccessHelper.PhotoAccessHelper) {
  try {
    let recommendOptions: photoAccessHelper.RecommendationOptions = {
      recommendationType: photoAccessHelper.RecommendationType.ID\_CARD
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

#### SingleSelectionMode18+

Enumerates the single selection mode types.

**Atomic service API**: This API can be used in atomic services since API version 18.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BROWSER\_MODE | 0 | Mode for previewing large images. |
| SELECT\_MODE | 1 | Mode for direct selection. |
| BROWSER\_AND\_SELECT\_MODE | 2 | Compatibility mode. Tapping the bottom-right area enables direct selection, whereas tapping elsewhere switches to large image preview mode. |

#### FilterOperator19+

Enumerates the operators that can be used for filtering.

**Atomic service API**: This API can be used in atomic services since API version 19.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| EQUAL\_TO | 0 | Equal to. |
| NOT\_EQUAL\_TO | 1 | Not equal to. |
| MORE\_THAN | 2 | Greater than. |
| LESS\_THAN | 3 | Less than. |
| MORE\_THAN\_OR\_EQUAL\_TO | 4 | Greater than or equal to. |
| LESS\_THAN\_OR\_EQUAL\_TO | 5 | Less than or equal to. |
| BETWEEN | 6 | Within the specified range. |

#### DeliveryMode11+

Enumerates the asset delivery modes.

These modes are used for segmented photo or video delivery. If the device does not support segmentation, the three delivery modes below work the same way and just return the requested image or video directly. The request result is returned through the [onDataPrepared](../interface-mediaassetdatahandler/document.md#ondataprepared11) callback.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| FAST\_MODE | 0 | 
Fast mode.

For segmented photo or video delivery, if a high-quality version is available, it quickly returns the callback for that high-quality version. If only a low-quality version is available, it returns the callback for the low-quality version right away.

 |
| HIGH\_QUALITY\_MODE | 1 | 

High-quality mode.

For segmented photo or video delivery, if a high-quality version is available, it quickly returns the callback for that high-quality version. If only a low-quality version is available, it starts a task to generate a high-quality version and returns the callback for the high-quality version once that version is ready.

 |
| BALANCE\_MODE | 2 | 

Balance mode.

\- For segmented photo delivery, if a high-quality version is available, it quickly returns the callback for that high-quality version. If only a low-quality version is available, it returns the callback for the low-quality version, starts a task to generate a high-quality version, and returns the callback for the high-quality version once that version is ready.

\- For segmented video delivery, if a high-quality version is available, it quickly returns the callback for that high-quality version. If only a low-quality version is available, it returns the callback for the low-quality version right away.

 |

#### CompatibleMode15+

Enumerates the compatible modes.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ORIGINAL\_FORMAT\_MODE | 0 | Maintains the original video format. |
| COMPATIBLE\_FORMAT\_MODE | 1 | Converts the HDR content to SDR format. |

#### CompleteButtonText14+

Enumerates the text displayed on the complete button.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| TEXT\_DONE14+ | 0 | 
The text "Done" is displayed.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| TEXT\_SEND14+ | 1 | 

The text "Send" is displayed.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| TEXT\_ADD14+ | 2 | 

The text "Add" is displayed.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |

#### NotifyChangeType20+

Enumerates the types of changes that trigger the media asset or album change events.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NOTIFY\_CHANGE\_ADD | 0 | A media asset or an album is created. |
| NOTIFY\_CHANGE\_UPDATE | 1 | A media asset or an album is modified. |
| NOTIFY\_CHANGE\_REMOVE | 2 | A media asset or an album is deleted. |

#### PhotoSource20+

Enumerates the sources of the image or video data.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL | 0 | 
Images and videos from all sources.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| CAMERA | 1 | 

Image or video taken by the camera.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
| SCREENSHOT | 2 | 

Screenshot or screen capture video.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |

#### MovingPhotoBadgeStateType22+

Enumerates the states of moving photo badges.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| NOT\_MOVING\_PHOTO | 0 | The media file is not a moving photo. |
| MOVING\_PHOTO\_ENABLED | 1 | The moving photo effect is enabled. |
| MOVING\_PHOTO\_DISABLED | 2 | The moving photo effect is disabled. |

#### VideoMode22+

Enumerates the log modes of video files.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT | 0 | 
Default type.

A value of **0** indicates that the video is either not in log mode or its type has not yet been determined. This value may later be updated to **1** for some videos after type determination, so it is not recommended for use in queries.

 |
| LOG\_VIDEO | 1 | Video file in log mode. |

#### OperationType22+

Enumerates the predicates.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 22.

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| EQUAL\_TO | 1 | Checks for equality, using the first element of the **value** array to match the predicate. If the array is longer, only the first element is considered. |
| NOT\_EQUAL\_TO | 2 | Checks for inequality, using the first element of the **value** array to match the predicate. If the array is longer, only the first element is considered. |
| GREATER\_THAN | 3 | Checks whether the value is greater than the predicate, using the first element of the **value** array to match the predicate. If the array is longer, only the first element is considered. |
| LESS\_THAN | 4 | Checks whether the value is less than the predicate, using the first element of the **value** array to match the predicate. If the array is longer, only the first element is considered. |
| GREATER\_THAN\_OR\_EQUAL\_TO | 5 | Checks whether the value is greater than or equal to the predicate, using the first element of the **value** array to match the predicate. If the array is longer, only the first element is considered. |
| LESS\_THAN\_OR\_EQUAL\_TO | 6 | Checks whether the value is less than or equal to the predicate, using the first element of the **value** array to match the predicate. If the array is longer, only the first element is considered. |
| AND | 7 | Logical 'AND', similar to 'and' in database queries. No **field** or **value** is needed. |
| OR | 8 | Logical 'OR', similar to 'or' in database queries. No **field** or **value** is needed. |
| IN | 9 | Matches fields within a specified range, with a maximum value length of 10. |
| NOT\_IN | 10 | Matches fields outside a specified range, with a maximum value length of 10. |
| BEGIN\_WRAP | 11 | Adds a left parenthesis to the predicate, similar to "(" in database queries. It must be used with a right parenthesis. No **field** or **value** is needed. |
| END\_WRAP | 12 | Adds a right parenthesis to the predicate, similar to ")" in database queries. It must be used with a left parenthesis. No **field** or **value** is needed. |
| BETWEEN | 13 | 
Matches fields within a specified range,

including both endpoints (closed interval). It uses the first two elements of the **value** array, where the first element is the lower boundary and the second is the upper boundary. For example, in the array \[1, 2, 3, 4\], the first two elements are used, with 1 as the lower boundary and 2 as the upper boundary.

 |
| NOT\_BETWEEN | 14 | 

Matches fields outside a specified range,

excluding both endpoints (open interval). It uses the first two elements of the **value** array, where the first element is the lower boundary and the second is the upper boundary. For example, in the array \[1, 2, 3, 4\], the first two elements are used, with 1 as the lower boundary and 2 as the upper boundary.

 |
