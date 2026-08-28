# moving\_photo\_capi.h

#### Overview

The file declares the APIs related to moving photos. You can use the APIs to obtain moving photo information.

**Library**: libmedia\_asset\_manager.so

**File to include**: <multimedia/media\_library/moving\_photo\_capi.h>

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Since**: 13

**Related module**: [MediaAssetManager](../../modules/mediaassetmanager/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_GetUri(OH\_MovingPhoto\* movingPhoto, const char\*\* uri)](#oh_movingphoto_geturi) | Obtains the URI of a moving photo. |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithUris(OH\_MovingPhoto\* movingPhoto, char\* imageUri, char\* videoUri)](#oh_movingphoto_requestcontentwithuris) | Requests the image data and video data of a moving photo and writes them to the specified URIs, respectively. |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithUri(OH\_MovingPhoto\* movingPhoto, MediaLibrary\_ResourceType resourceType, char\* uri)](#oh_movingphoto_requestcontentwithuri) | Requests the moving photo content of the specified resource type and writes it to the specified URI. |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithBuffer(OH\_MovingPhoto\* movingPhoto, MediaLibrary\_ResourceType resourceType, const uint8\_t\*\* buffer, uint32\_t\* size)](#oh_movingphoto_requestcontentwithbuffer) | Requests the moving photo content of the specified resource type and returns it in ArrayBuffer format. |
| [MediaLibrary\_ErrorCode OH\_MovingPhoto\_Release(OH\_MovingPhoto\* movingPhoto)](#oh_movingphoto_release) | Releases an [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) instance. |

#### Function Description

#### \[h2\]OH\_MovingPhoto\_GetUri()

MediaLibrary\_ErrorCode OH\_MovingPhoto\_GetUri(OH\_MovingPhoto\* movingPhoto, const char\*\* uri)

**Description**

Obtains the URI of a moving photo.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md)\* movingPhoto | Pointer to an [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) instance. |
| const char\*\* uri | Double pointer to the URI of the moving photo obtained. |

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

 |

#### \[h2\]OH\_MovingPhoto\_RequestContentWithUris()

MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithUris(OH\_MovingPhoto\* movingPhoto, char\* imageUri,char\* videoUri)

**Description**

Requests the image data and video data of a moving photo and writes them to the specified URIs, respectively.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md)\* movingPhoto | Pointer to an [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) instance. |
| char\* imageUri | Pointer to the URI of the file, to which the image data is written. |
| char\* videoUri | Pointer to the URI of the file, to which the video data is written. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_PERMISSION\_DENIED**: no access permission.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

 |

#### \[h2\]OH\_MovingPhoto\_RequestContentWithUri()

MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithUri(OH\_MovingPhoto\* movingPhoto,MediaLibrary\_ResourceType resourceType, char\* uri)

**Description**

Requests the moving photo content of the specified resource type and writes it to the specified URI.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md)\* movingPhoto | Pointer to an [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) instance. |
| [MediaLibrary\_ResourceType](../media-asset-base-capi-h/document.md#medialibrary_resourcetype) resourceType | Resource type, which is specified by [MediaLibrary\_ResourceType](../media-asset-base-capi-h/document.md#medialibrary_resourcetype). |
| char\* uri | Pointer to the URI of the file, to which the data is written. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_PERMISSION\_DENIED**: no access permission.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

 |

#### \[h2\]OH\_MovingPhoto\_RequestContentWithBuffer()

MediaLibrary\_ErrorCode OH\_MovingPhoto\_RequestContentWithBuffer(OH\_MovingPhoto\* movingPhoto,MediaLibrary\_ResourceType resourceType, const uint8\_t\*\* buffer, uint32\_t\* size)

**Description**

Requests the moving photo content of the specified resource type and returns it in ArrayBuffer format.

**Required permissions**: ohos.permission.READ\_IMAGEVIDEO

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md)\* movingPhoto | Pointer to an [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) instance. |
| [MediaLibrary\_ResourceType](../media-asset-base-capi-h/document.md#medialibrary_resourcetype) resourceType | Resource type, which is specified by [MediaLibrary\_ResourceType](../media-asset-base-capi-h/document.md#medialibrary_resourcetype). |
| const uint8\_t\*\* buffer | Double pointer to the buffer for storing the target file data. |
| uint32\_t\* size | Pointer to the buffer size. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible causes:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_PERMISSION\_DENIED**: no access permission.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

 |

#### \[h2\]OH\_MovingPhoto\_Release()

MediaLibrary\_ErrorCode OH\_MovingPhoto\_Release(OH\_MovingPhoto\* movingPhoto)

**Description**

Releases an [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) instance.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md)\* movingPhoto | Pointer to an [OH\_MovingPhoto](../../structs/oh-movingphoto/document.md) instance. |

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
