# media\_asset\_change\_request\_capi.h

#### Overview

The file declares the APIs related to media asset change requests. You can use the APIs to change media assets.

**Library**: libmedia\_asset\_manager.so

**File to include**: <multimedia/media\_library/media\_asset\_change\_request\_capi.h>

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Since**: 12

**Related module**: [MediaAssetManager](../../modules/mediaassetmanager/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest\* OH\_MediaAssetChangeRequest\_Create(OH\_MediaAsset\* mediaAsset)](#oh_mediaassetchangerequest_create) | Creates an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_AddResourceWithUri(OH\_MediaAssetChangeRequest\* changeRequest, MediaLibrary\_ResourceType resourceType, char\* fileUri)](#oh_mediaassetchangerequest_addresourcewithuri) | Adds a resource of the given URI. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_AddResourceWithBuffer(OH\_MediaAssetChangeRequest\* changeRequest, MediaLibrary\_ResourceType resourceType, uint8\_t\* buffer, uint32\_t length)](#oh_mediaassetchangerequest_addresourcewithbuffer) | Adds a resource using ArrayBuffer data. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_GetWriteCacheHandler(OH\_MediaAssetChangeRequest\* changeRequest, int32\_t\* fd)](#oh_mediaassetchangerequest_getwritecachehandler) | Obtains the handler used for writing a file to cache. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_SaveCameraPhoto(OH\_MediaAssetChangeRequest\* changeRequest, MediaLibrary\_ImageFileType imageFileType)](#oh_mediaassetchangerequest_savecameraphoto) | Saves the photo taken by the camera. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_DiscardCameraPhoto(OH\_MediaAssetChangeRequest\* changeRequest)](#oh_mediaassetchangerequest_discardcameraphoto) | Discards the photo taken by the camera. |
| [MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_Release(OH\_MediaAssetChangeRequest\* changeRequest)](#oh_mediaassetchangerequest_release) | Releases an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance. |

#### Function Description

#### \[h2\]OH\_MediaAssetChangeRequest\_Create()

OH\_MediaAssetChangeRequest\* OH\_MediaAssetChangeRequest\_Create(OH\_MediaAsset\* mediaAsset)

**Description**

Creates an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md)\* | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

 |

#### \[h2\]OH\_MediaAssetChangeRequest\_AddResourceWithUri()

MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_AddResourceWithUri(OH\_MediaAssetChangeRequest\* changeRequest,MediaLibrary\_ResourceType resourceType, char\* fileUri)

**Description**

Adds a resource of the given URI.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md)\* changeRequest | Pointer to an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance. |
| [MediaLibrary\_ResourceType](../media-asset-base-capi-h/document.md#medialibrary_resourcetype) resourceType | Type of the resource to add, which is specified by [MediaLibrary\_ResourceType](../media-asset-base-capi-h/document.md#medialibrary_resourcetype). |
| char\* fileUri | Pointer to the URI of the file. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_NO\_SUCH\_FILE**: The file does not exist.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

**MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED**: unsupported operation.

 |

#### \[h2\]OH\_MediaAssetChangeRequest\_AddResourceWithBuffer()

MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_AddResourceWithBuffer(OH\_MediaAssetChangeRequest\* changeRequest,MediaLibrary\_ResourceType resourceType, uint8\_t\* buffer, uint32\_t length)

**Description**

Adds a resource using ArrayBuffer data.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md)\* changeRequest | Pointer to an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance. |
| [MediaLibrary\_ResourceType](../media-asset-base-capi-h/document.md#medialibrary_resourcetype) resourceType | Type of the resource to add. |
| uint8\_t\* buffer | Pointer to the data buffer. |
| uint32\_t length | Length of the data buffer. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

**MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED**: unsupported operation.

 |

#### \[h2\]OH\_MediaAssetChangeRequest\_GetWriteCacheHandler()

MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_GetWriteCacheHandler(OH\_MediaAssetChangeRequest\* changeRequest,int32\_t\* fd)

**Description**

Obtains the handler used for writing a file to cache.

**Required permissions**: ohos.permission.WRITE\_IMAGEVIDEO

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md)\* changeRequest | Pointer to an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance. |
| int32\_t\* fd | Pointer to the file descriptor (FD) obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

**MEDIA\_LIBRARY\_PERMISSION\_DENIED**: no access permission.

**MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED**: unsupported operation.

 |

#### \[h2\]OH\_MediaAssetChangeRequest\_SaveCameraPhoto()

MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_SaveCameraPhoto(OH\_MediaAssetChangeRequest\* changeRequest,MediaLibrary\_ImageFileType imageFileType)

**Description**

Saves the photo taken by the camera.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md)\* changeRequest | Pointer to an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance. |
| [MediaLibrary\_ImageFileType](../media-asset-base-capi-h/document.md#medialibrary_imagefiletype) imageFileType | Type of the image file of the photo. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

**MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED**: unsupported operation.

 |

#### \[h2\]OH\_MediaAssetChangeRequest\_DiscardCameraPhoto()

MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_DiscardCameraPhoto(OH\_MediaAssetChangeRequest\* changeRequest)

**Description**

Discards the photo taken by the camera.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md)\* changeRequest | Pointer to an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

**MEDIA\_LIBRARY\_OPERATION\_NOT\_SUPPORTED**: unsupported operation.

 |

#### \[h2\]OH\_MediaAssetChangeRequest\_Release()

MediaLibrary\_ErrorCode OH\_MediaAssetChangeRequest\_Release(OH\_MediaAssetChangeRequest\* changeRequest)

**Description**

Releases an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md)\* changeRequest | Pointer to an [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md) instance. |

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
