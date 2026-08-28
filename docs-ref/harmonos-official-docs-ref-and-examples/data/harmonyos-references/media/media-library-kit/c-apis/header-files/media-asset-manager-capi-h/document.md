# media\_asset\_manager\_capi.h

#### Overview

The file declares the APIs of the media asset manager. You can use the functions to request media assets in the media library.

**Library**: libmedia\_asset\_manager.so

**File to include**: <multimedia/media\_library/media\_asset\_manager\_capi.h>

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Since**: 12

**Related module**: [MediaAssetManager](../../modules/mediaassetmanager/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_MediaAssetManager\* OH\_MediaAssetManager\_Create(void)](#oh_mediaassetmanager_create) | Creates an OH\_MediaAssetManager instance. |
| [MediaLibrary\_RequestId OH\_MediaAssetManager\_RequestImageForPath(OH\_MediaAssetManager\* manager, const char\* uri, MediaLibrary\_RequestOptions requestOptions, const char\* destPath, OH\_MediaLibrary\_OnDataPrepared callback)](#oh_mediaassetmanager_requestimageforpath) | Requests an image in the specified directory. |
| [MediaLibrary\_RequestId OH\_MediaAssetManager\_RequestVideoForPath(OH\_MediaAssetManager\* manager, const char\* uri, MediaLibrary\_RequestOptions requestOptions, const char\* destPath, OH\_MediaLibrary\_OnDataPrepared callback)](#oh_mediaassetmanager_requestvideoforpath) | Requests a video in the specified directory. |
| [bool OH\_MediaAssetManager\_CancelRequest(OH\_MediaAssetManager\* manager, const MediaLibrary\_RequestId requestId)](#oh_mediaassetmanager_cancelrequest) | Cancels a request based on the request ID. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetManager\_RequestMovingPhoto(OH\_MediaAssetManager\* manager, OH\_MediaAsset\* mediaAsset, MediaLibrary\_RequestOptions requestOptions, MediaLibrary\_RequestId\* requestId, OH\_MediaLibrary\_OnMovingPhotoDataPrepared callback)](#oh_mediaassetmanager_requestmovingphoto) | Requests a moving photo based on different policies. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetManager\_RequestImage(OH\_MediaAssetManager\* manager, OH\_MediaAsset\* mediaAsset, MediaLibrary\_RequestOptions requestOptions, MediaLibrary\_RequestId\* requestId, OH\_MediaLibrary\_OnImageDataPrepared callback)](#oh_mediaassetmanager_requestimage) | Requests an image based on different policies. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetManager\_Release(OH\_MediaAssetManager\* manager)](#oh_mediaassetmanager_release) | Releases an [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md) instance. |

#### Function Description

#### \[h2\]OH\_MediaAssetManager\_Create()

OH\_MediaAssetManager\* OH\_MediaAssetManager\_Create(void)

**Description**

Creates an OH\_MediaAssetManager instance.

**Since**: 12

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md)\* | Pointer to the OH\_MediaAssetManager instance created. |

#### \[h2\]OH\_MediaAssetManager\_RequestImageForPath()

MediaLibrary\_RequestId OH\_MediaAssetManager\_RequestImageForPath(OH\_MediaAssetManager\* manager, const char\* uri,MediaLibrary\_RequestOptions requestOptions, const char\* destPath, OH\_MediaLibrary\_OnDataPrepared callback)

**Description**

Requests an image in the specified directory.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md)\* manager | Pointer to an OH\_MediaAssetManager instance. |
| const char\* uri | Pointer to the URI of the requested image. |
| [MediaLibrary\_RequestOptions](../../structs/medialibrary-requestoptions/document.md) requestOptions | Options related to the media asset quality and delivery mode. |
| const char\* destPath | Pointer to the destination directory of the requested image. |
| [OH\_MediaLibrary\_OnDataPrepared](../media-asset-base-capi-h/document.md#oh_medialibrary_ondataprepared) callback | Callback to be invoked when the requested image is ready. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md) | Request ID. |

#### \[h2\]OH\_MediaAssetManager\_RequestVideoForPath()

MediaLibrary\_RequestId OH\_MediaAssetManager\_RequestVideoForPath(OH\_MediaAssetManager\* manager, const char\* uri,MediaLibrary\_RequestOptions requestOptions, const char\* destPath, OH\_MediaLibrary\_OnDataPrepared callback)

**Description**

Requests a video in the specified directory.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md)\* manager | Pointer to an OH\_MediaAssetManager instance. |
| const char\* uri | Pointer to the URI of the requested video. |
| [MediaLibrary\_RequestOptions](../../structs/medialibrary-requestoptions/document.md) requestOptions | Options related to the media asset quality and delivery mode. |
| const char\* destPath | Pointer to the destination directory of the requested video. |
| [OH\_MediaLibrary\_OnDataPrepared](../media-asset-base-capi-h/document.md#oh_medialibrary_ondataprepared) callback | Callback to be invoked when the requested video is ready. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md) | Request ID. |

#### \[h2\]OH\_MediaAssetManager\_CancelRequest()

bool OH\_MediaAssetManager\_CancelRequest(OH\_MediaAssetManager\* manager, const MediaLibrary\_RequestId requestId)

**Description**

Cancels a request based on the request ID.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md)\* manager | Pointer to an OH\_MediaAssetManager instance. |
| const [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md) requestId | ID of the request to cancel. |

**Return value**

| Type | Description |
| :-- | :-- |
| bool | Operation result. The value **true** is returned if the request is successfully canceled, and **false** is returned otherwise. |

#### \[h2\]OH\_MediaAssetManager\_RequestMovingPhoto()

MediaLibrary\_ErrorCode OH\_MediaAssetManager\_RequestMovingPhoto(OH\_MediaAssetManager\* manager,OH\_MediaAsset\* mediaAsset, MediaLibrary\_RequestOptions requestOptions, MediaLibrary\_RequestId\* requestId,OH\_MediaLibrary\_OnMovingPhotoDataPrepared callback)

**Description**

Requests a moving photo based on different policies.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md)\* manager | Pointer to an [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md) instance. |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to the [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance to be requested. |
| [MediaLibrary\_RequestOptions](../../structs/medialibrary-requestoptions/document.md) requestOptions | Options related to the media asset quality and delivery mode. The options are specified by [MediaLibrary\_RequestOptions](../../structs/medialibrary-requestoptions/document.md). |
| [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md)\* requestId | Pointer to the request ID, which is specified by [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md). |
| [OH\_MediaLibrary\_OnMovingPhotoDataPrepared](../media-asset-base-capi-h/document.md#oh_medialibrary_onmovingphotodataprepared) callback | Callback to be invoked when the requested moving photo is ready. The callback is specified by [OH\_MediaLibrary\_OnMovingPhotoDataPrepared](../media-asset-base-capi-h/document.md#oh_medialibrary_onmovingphotodataprepared). |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED**: unsupported operation.

**MEDIA\_LIBRARY\_PERMISSION\_DENIED**: no access permission.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

 |

#### \[h2\]OH\_MediaAssetManager\_RequestImage()

MediaLibrary\_ErrorCode OH\_MediaAssetManager\_RequestImage(OH\_MediaAssetManager\* manager, OH\_MediaAsset\* mediaAsset,MediaLibrary\_RequestOptions requestOptions, MediaLibrary\_RequestId\* requestId,OH\_MediaLibrary\_OnImageDataPrepared callback)

**Description**

Requests an image based on different policies.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md)\* manager | Pointer to an [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md) instance. |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to the [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance to be requested. |
| [MediaLibrary\_RequestOptions](../../structs/medialibrary-requestoptions/document.md) requestOptions | Options related to the media asset quality and delivery mode. The options are specified by [MediaLibrary\_RequestOptions](../../structs/medialibrary-requestoptions/document.md). |
| [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md)\* requestId | Pointer to the request ID, which is specified by [MediaLibrary\_RequestId](../../structs/medialibrary-requestid/document.md). |
| [OH\_MediaLibrary\_OnImageDataPrepared](../media-asset-base-capi-h/document.md#oh_medialibrary_onimagedataprepared) callback | Callback to be invoked when the requested image is ready. The callback is specified by [OH\_MediaLibrary\_OnImageDataPrepared](../media-asset-base-capi-h/document.md#oh_medialibrary_onimagedataprepared). |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED**: unsupported operation.

**MEDIA\_LIBRARY\_PERMISSION\_DENIED**: no access permission.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

 |

#### \[h2\]OH\_MediaAssetManager\_Release()

MediaLibrary\_ErrorCode OH\_MediaAssetManager\_Release(OH\_MediaAssetManager\* manager)

**Description**

Releases an [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md) instance.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md)\* manager | Pointer to an [OH\_MediaAssetManager](../../structs/oh-mediaassetmanager/document.md) instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

 |
