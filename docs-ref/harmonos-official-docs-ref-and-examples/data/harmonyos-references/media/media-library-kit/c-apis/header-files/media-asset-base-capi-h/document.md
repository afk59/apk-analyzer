# media\_asset\_base\_capi.h

#### Overview

The file declares the structs and enums for the media asset manager.

**Library**: libmedia\_asset\_manager.so

**File to include**: <multimedia/media\_library/media\_asset\_base\_capi.h>

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Since**: 12

**Related module**: [MediaAssetManager](../../modules/mediaassetmanager/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md) | MediaLibrary\_RequestId | 
Describes a request ID.

A value of this type is returned when a media asset is requested.

The request ID can be used to cancel a request.

 |
| [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md) | OH\_MediaAssetManager | 

Describes the media asset manager.

You can use this struct to create a media asset manager instance.

If the creation fails, nullptr is returned.

 |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) | OH\_MediaAssetChangeRequest | 

Describes a media asset change request.

This struct provides the capability of handling media asset change requests.

 |
| [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) | OH\_MovingPhoto | 

Describes a moving photo.

This struct provides the capability of obtaining information about a moving photo.

 |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) | OH\_MediaAsset | 

Describes a media asset.

This struct provides the capability of encapsulating media file attributes.

 |
| [MediaLibrary\_RequestOptions](../../structs/medialibrary-requestoptions/document.md) | MediaLibrary\_RequestOptions | 

Defines how media assets are requested and processed.

You can use this struct to set options related to the media asset quality, delivery mode, and more.

 |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [MediaLibrary\_ErrorCode](#medialibrary_errorcode) | MediaLibrary\_ErrorCode | Enumerates the error codes of the media library. |
| [MediaLibrary\_DeliveryMode](#medialibrary_deliverymode) | MediaLibrary\_DeliveryMode | Enumerates the delivery modes of the requested media asset. |
| [MediaLibrary\_MediaType](#medialibrary_mediatype) | MediaLibrary\_MediaType | Enumerates the media asset types. |
| [MediaLibrary\_MediaSubType](#medialibrary_mediasubtype) | MediaLibrary\_MediaSubType | Enumerates the media asset subtypes. |
| [MediaLibrary\_ResourceType](#medialibrary_resourcetype) | MediaLibrary\_ResourceType | Enumerates the media library resource types. |
| [MediaLibrary\_ImageFileType](#medialibrary_imagefiletype) | MediaLibrary\_ImageFileType | Enumerates the image file types. |
| [MediaLibrary\_MediaQuality](#medialibrary_mediaquality) | MediaLibrary\_MediaQuality | Enumerates the media resource quality, which varies with the specified delivery mode for the requested media asset. |
| [MediaLibrary\_MediaContentType](#medialibrary_mediacontenttype) | MediaLibrary\_MediaContentType | Enumerates the media content types. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_MediaLibrary\_OnDataPrepared)(int32\_t result, MediaLibrary\_RequestId requestId)](#oh_medialibrary_ondataprepared) | OH\_MediaLibrary\_OnDataPrepared | Called when the requested media asset is ready. |
| [typedef void (\*OH\_MediaLibrary\_OnImageDataPrepared)(MediaLibrary\_ErrorCode result, MediaLibrary\_RequestId requestId, MediaLibrary\_MediaQuality mediaQuality, MediaLibrary\_MediaContentType type,OH\_ImageSourceNative\* imageSourceNative)](#oh_medialibrary_onimagedataprepared) | OH\_MediaLibrary\_OnImageDataPrepared | Called when the requested image is ready. |
| [typedef void (\*OH\_MediaLibrary\_OnMovingPhotoDataPrepared)(MediaLibrary\_ErrorCode result, MediaLibrary\_RequestId requestId, MediaLibrary\_MediaQuality mediaQuality, MediaLibrary\_MediaContentType type, OH\_MovingPhoto\* movingPhoto)](#oh_medialibrary_onmovingphotodataprepared) | OH\_MediaLibrary\_OnMovingPhotoDataPrepared | Called when the requested moving photo is ready. |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| static const int32\_t UUID\_STR\_MAX\_LENGTH = 37 | 
Maximum length of a request ID.

**Since**: 12

 |

#### Enum Description

#### \[h2\]MediaLibrary\_ErrorCode

enum MediaLibrary\_ErrorCode

**Description**

Enumerates the error codes of the media library.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MEDIA\_LIBRARY\_OK = 0 | Operation success. |
| MEDIA\_LIBRARY\_PERMISSION\_DENIED = 201 | No access permission. |
| MEDIA\_LIBRARY\_PARAMETER\_ERROR = 401 | A mandatory parameter is not specified, the parameter type is incorrect, or parameter verification failed. |
| MEDIA\_LIBRARY\_NO\_SUCH\_FILE = 23800101 | The file does not exist. |
| MEDIA\_LIBRARY\_INVALID\_DISPLAY\_NAME = 23800102 | Invalid display name. |
| MEDIA\_LIBRARY\_INVALID\_ASSET\_URI = 23800103 | Invalid asset URI. |
| MEDIA\_LIBRARY\_INVALID\_PHOTO\_KEY = 23800104 | Invalid PhotoKey. |
| MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED = 23800201 | Unsupported operation. |
| MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR = 23800301 | 
Internal system error. Retry the operation and check logs. Possible causes:

1\. The database is corrupted.

2\. The file system is abnormal.

3\. The IPC request timed out.

 |

#### \[h2\]MediaLibrary\_DeliveryMode

enum MediaLibrary\_DeliveryMode

**Description**

Enumerates the delivery modes of the requested media asset.

**MEDIA\_LIBRARY\_FAST\_MODE**: Deliver the media asset available without considering its quality.

**MEDIA\_LIBRARY\_HIGH\_QUALITY\_MODE**: Deliver a media asset with high quality. If there is no high-quality asset available, trigger the process for creating a high-quality asset. Then, return the high-quality asset that is successfully created.

**MEDIA\_LIBRARY\_BALANCED\_MODE**: Return the high-quality asset if there is any. Otherwise, return a low-quality asset first and trigger the process for creating a high-quality asset. Then, return the high-quality asset that is successfully created.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MEDIA\_LIBRARY\_FAST\_MODE = 0 | Fast mode. |
| MEDIA\_LIBRARY\_HIGH\_QUALITY\_MODE = 1 | High-quality mode. |
| MEDIA\_LIBRARY\_BALANCED\_MODE = 2 | Balance mode. |

#### \[h2\]MediaLibrary\_MediaType

enum MediaLibrary\_MediaType

**Description**

Enumerates the media asset types.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MEDIA\_LIBRARY\_IMAGE = 1 | Image. |
| MEDIA\_LIBRARY\_VIDEO = 2 | Video. |

#### \[h2\]MediaLibrary\_MediaSubType

enum MediaLibrary\_MediaSubType

**Description**

Enumerates the media asset subtypes.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MEDIA\_LIBRARY\_DEFAULT = 0 | Photo, which is the default type. |
| MEDIA\_LIBRARY\_MOVING\_PHOTO = 3 | Moving photo. |
| MEDIA\_LIBRARY\_BURST = 4 | Burst photo. |

#### \[h2\]MediaLibrary\_ResourceType

enum MediaLibrary\_ResourceType

**Description**

Enumerates the media library resource types.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MEDIA\_LIBRARY\_IMAGE\_RESOURCE = 1 | Image resource. |
| MEDIA\_LIBRARY\_VIDEO\_RESOURCE = 2 | Video resource. |

#### \[h2\]MediaLibrary\_ImageFileType

enum MediaLibrary\_ImageFileType

**Description**

Enumerates the image file types.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MEDIA\_LIBRARY\_IMAGE\_JPEG = 1 | JPEG. |
| MEDIA\_LIBRARY\_FILE\_VIDEO = 3 | 
MPEG type.

**Since**: 19

 |

#### \[h2\]MediaLibrary\_MediaQuality

enum MediaLibrary\_MediaQuality

**Description**

Enumerates the media resource quality,

which varies with the specified delivery mode for the requested media asset.

**MEDIA\_LIBRARY\_FAST\_MODE**: Deliver the media asset available without considering its quality.

**MEDIA\_LIBRARY\_HIGH\_QUALITY\_MODE**: Deliver a media asset with high quality. If there is no high-quality asset available, trigger the process for creating a high-quality asset. Then, return the high-quality asset that is successfully created.

**MEDIA\_LIBRARY\_BALANCED\_MODE**: Return the high-quality asset if there is any. Otherwise, return a low-quality asset first and trigger the process for creating a high-quality asset. Then, return the high-quality asset that is successfully created.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MEDIA\_LIBRARY\_QUALITY\_FAST = 1 | Media asset available without considering its quality. |
| MEDIA\_LIBRARY\_QUALITY\_FULL = 2 | High-quality media asset. |

#### \[h2\]MediaLibrary\_MediaContentType

enum MediaLibrary\_MediaContentType

**Description**

Enumerates the media content types.

**Since**: 12

| Enum | Description |
| :-- | :-- |
| MEDIA\_LIBRARY\_COMPRESSED = 1 | Common image formats, such as JPEG, HEIC, and GIF. |
| MEDIA\_LIBRARY\_PICTURE\_OBJECT = 2 | Object that encapsulates the PixelMap, GainMap, and image metadata after decoding, making it convenient for applications to perform editing and display operations. For detailed operations on this object, see [OH\_PictureNative](../../../../image-kit/c-apis/structs/oh-picturenative/document.md). |

#### Function Description

#### \[h2\]OH\_MediaLibrary\_OnDataPrepared()

typedef void (\*OH\_MediaLibrary\_OnDataPrepared)(int32\_t result, MediaLibrary\_RequestId requestId)

**Description**

Called when the requested media asset is ready.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int32\_t result | Request processing result. |
| MediaLibrary\_RequestId requestId | Request ID. |

#### \[h2\]OH\_MediaLibrary\_OnImageDataPrepared()

typedef void (\*OH\_MediaLibrary\_OnImageDataPrepared)(MediaLibrary\_ErrorCode result,MediaLibrary\_RequestId requestId, MediaLibrary\_MediaQuality mediaQuality, MediaLibrary\_MediaContentType type,OH\_ImageSourceNative\* imageSourceNative)

**Description**

Called when the requested image is ready.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](#medialibrary_errorcode) result | Request processing result, which is specified by [MediaLibrary\_ErrorCode](#medialibrary_errorcode). |
| [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md) requestId | Request ID, which is specified by [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md). |
| [MediaLibrary\_MediaQuality](#medialibrary_mediaquality) mediaQuality | Quality of the requested source, which is specified by [MediaLibrary\_MediaQuality](#medialibrary_mediaquality). |
| [MediaLibrary\_MediaContentType](#medialibrary_mediacontenttype) type | Media content type of the requested source, which is specified by [MediaLibrary\_MediaContentType](#medialibrary_mediacontenttype). |
| [OH\_ImageSourceNative](../../../../image-kit/c-apis/structs/oh-imagesourcenative/document.md)\* imageSourceNative | Pointer to the [OH\_ImageSourceNative](../../../../image-kit/c-apis/structs/oh-imagesourcenative/document.md) instance obtained when the requested image is ready. |

#### \[h2\]OH\_MediaLibrary\_OnMovingPhotoDataPrepared()

typedef void (\*OH\_MediaLibrary\_OnMovingPhotoDataPrepared)(MediaLibrary\_ErrorCode result,MediaLibrary\_RequestId requestId, MediaLibrary\_MediaQuality mediaQuality, MediaLibrary\_MediaContentType type,OH\_MovingPhoto\* movingPhoto)

**Description**

Called when the requested moving photo is ready.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](#medialibrary_errorcode) result | Request processing result, which is specified by [MediaLibrary\_ErrorCode](#medialibrary_errorcode). |
| [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md) requestId | Request ID, which is specified by [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md). |
| [MediaLibrary\_MediaQuality](#medialibrary_mediaquality) mediaQuality | Quality of the requested resource, which is specified by [MediaLibrary\_MediaQuality](#medialibrary_mediaquality). |
| [MediaLibrary\_MediaContentType](#medialibrary_mediacontenttype) type | Media content type of the requested resource, which is specified by [MediaLibrary\_MediaContentType](#medialibrary_mediacontenttype). |
| [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md)\* movingPhoto | Pointer to the [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) instance obtained when the requested moving photo is ready. |
