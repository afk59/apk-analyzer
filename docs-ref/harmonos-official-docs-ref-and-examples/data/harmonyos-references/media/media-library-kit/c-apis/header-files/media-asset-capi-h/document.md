# media\_asset\_capi.h

#### Overview

The file declares the APIs related to media assets. You can use the APIs to obtain image or video information.

**Library**: libmedia\_asset\_manager.so

**File to include**: <multimedia/media\_library/media\_asset\_capi.h>

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Since**: 12

**Related module**: [MediaAssetManager](../../modules/mediaassetmanager/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetUri(OH\_MediaAsset\* mediaAsset, const char\*\* uri)](#oh_mediaasset_geturi) | Obtains the URI of a media asset. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetMediaType(OH\_MediaAsset\* mediaAsset, MediaLibrary\_MediaType\* mediaType)](#oh_mediaasset_getmediatype) | Obtains the type of a media asset. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetMediaSubType(OH\_MediaAsset\* mediaAsset, MediaLibrary\_MediaSubType\* mediaSubType)](#oh_mediaasset_getmediasubtype) | Obtains the subtype of a media asset. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDisplayName(OH\_MediaAsset\* mediaAsset, const char\*\* displayName)](#oh_mediaasset_getdisplayname) | Obtains the display name of a media asset. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetSize(OH\_MediaAsset\* mediaAsset, uint32\_t\* size)](#oh_mediaasset_getsize) | Obtains the size of a media asset file. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateAdded(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateAdded)](#oh_mediaasset_getdateadded) | Obtains the date when a media asset was added. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateModified(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateModified)](#oh_mediaasset_getdatemodified) | Obtains the date when a media asset was last modified. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateTaken(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateTaken)](#oh_mediaasset_getdatetaken) | Obtains the date when a media asset was taken. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateAddedMs(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateAddedMs)](#oh_mediaasset_getdateaddedms) | Obtains the date when a media asset was added, in ms. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateModifiedMs(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateModifiedMs)](#oh_mediaasset_getdatemodifiedms) | Obtains the date when a media asset was last modified, in ms. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDuration(OH\_MediaAsset\* mediaAsset, uint32\_t\* duration)](#oh_mediaasset_getduration) | Obtains the duration of a media asset, in ms. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetWidth(OH\_MediaAsset\* mediaAsset, uint32\_t\* width)](#oh_mediaasset_getwidth) | Obtains the image width (in pixels) of a media asset. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetHeight(OH\_MediaAsset\* mediaAsset, uint32\_t\* height)](#oh_mediaasset_getheight) | Obtains the image height (in pixels) of a media asset. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetOrientation(OH\_MediaAsset\* mediaAsset, uint32\_t\* orientation)](#oh_mediaasset_getorientation) | Obtains the orientation of a media asset, in degrees. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_IsFavorite(OH\_MediaAsset\* mediaAsset, uint32\_t\* favorite)](#oh_mediaasset_isfavorite) | Checks whether a media asset is favorited. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_GetTitle(OH\_MediaAsset\* mediaAsset, const char\*\* title)](#oh_mediaasset_gettitle) | Obtains the title of a media asset. |
| [MediaLibrary\_ErrorCode OH\_MediaAsset\_Release(OH\_MediaAsset\* mediaAsset)](#oh_mediaasset_release) | Releases a media asset. |

#### Function Description

#### \[h2\]OH\_MediaAsset\_GetUri()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetUri(OH\_MediaAsset\* mediaAsset, const char\*\* uri)

**Description**

Obtains the URI of a media asset.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| const char\*\* uri | Double pointer to the URI obtained. |

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

#### \[h2\]OH\_MediaAsset\_GetMediaType()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetMediaType(OH\_MediaAsset\* mediaAsset, MediaLibrary\_MediaType\* mediaType)

**Description**

Obtains the type of a media asset.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| [MediaLibrary\_MediaType](../media-asset-base-capi-h/document.md#medialibrary_mediatype)\* mediaType | Pointer to the media asset type obtained. |

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

#### \[h2\]OH\_MediaAsset\_GetMediaSubType()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetMediaSubType(OH\_MediaAsset\* mediaAsset,MediaLibrary\_MediaSubType\* mediaSubType)

**Description**

Obtains the subtype of a media asset.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| [MediaLibrary\_MediaSubType](../media-asset-base-capi-h/document.md#medialibrary_mediasubtype)\* mediaSubType | Pointer to the media asset subtype obtained. |

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

#### \[h2\]OH\_MediaAsset\_GetDisplayName()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDisplayName(OH\_MediaAsset\* mediaAsset, const char\*\* displayName)

**Description**

Obtains the display name of a media asset.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| const char\*\* displayName | Double pointer to the display name obtained. |

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

#### \[h2\]OH\_MediaAsset\_GetSize()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetSize(OH\_MediaAsset\* mediaAsset, uint32\_t\* size)

**Description**

Obtains the size of a media asset file.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* size | Pointer to the file size obtained, in bytes. |

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

#### \[h2\]OH\_MediaAsset\_GetDateAdded()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateAdded(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateAdded)

**Description**

Obtains the date when a media asset was added.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* dateAdded | Pointer to the date obtained. The value is the number of seconds elapsed since the Unix Epoch time (00:00:00 UTC on January 1, 1970). |

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

#### \[h2\]OH\_MediaAsset\_GetDateModified()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateModified(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateModified)

**Description**

Obtains the date when a media asset (content not the media asset name) was last modified.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* dateModified | Pointer to the date obtained. The value is the number of milliseconds elapsed since the Unix Epoch time. |

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

#### \[h2\]OH\_MediaAsset\_GetDateTaken()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateTaken(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateTaken)

**Description**

Obtains the date when a media asset was taken.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* dateTaken | Pointer to the date obtained. The value is the number of seconds elapsed since the Unix Epoch time. |

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

#### \[h2\]OH\_MediaAsset\_GetDateAddedMs()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateAddedMs(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateAddedMs)

**Description**

Obtains the date when a media asset was added, in ms.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* dateAddedMs | Pointer to the date obtained, in ms. The value is the number of milliseconds elapsed since the Unix Epoch time. |

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

#### \[h2\]OH\_MediaAsset\_GetDateModifiedMs()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDateModifiedMs(OH\_MediaAsset\* mediaAsset, uint32\_t\* dateModifiedMs)

**Description**

Obtains the date when a media asset (content not the media asset name) was last modified, in ms.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* dateModifiedMs | Pointer to the date obtained, in ms. The value is the number of milliseconds elapsed since the Unix Epoch time. |

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

#### \[h2\]OH\_MediaAsset\_GetDuration()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetDuration(OH\_MediaAsset\* mediaAsset, uint32\_t\* duration)

**Description**

Obtains the duration of a media asset, in ms.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* duration | Pointer to the duration obtained, in ms. |

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

#### \[h2\]OH\_MediaAsset\_GetWidth()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetWidth(OH\_MediaAsset\* mediaAsset, uint32\_t\* width)

**Description**

Obtains the image width (in pixels) of a media asset.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* width | Pointer to the image width obtained, in pixels. |

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

#### \[h2\]OH\_MediaAsset\_GetHeight()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetHeight(OH\_MediaAsset\* mediaAsset, uint32\_t\* height)

**Description**

Obtains the image height (in pixels) of a media asset.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* height | Pointer to the image height obtained, in pixels. |

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

#### \[h2\]OH\_MediaAsset\_GetOrientation()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetOrientation(OH\_MediaAsset\* mediaAsset, uint32\_t\* orientation)

**Description**

Obtains the orientation of a media asset, in degrees.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* orientation | Pointer to the orientation of the image obtained, in degrees. |

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

#### \[h2\]OH\_MediaAsset\_IsFavorite()

MediaLibrary\_ErrorCode OH\_MediaAsset\_IsFavorite(OH\_MediaAsset\* mediaAsset, uint32\_t\* favorite)

**Description**

Checks whether a media asset is favorited.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| uint32\_t\* favorite | Pointer to the favorite status obtained. |

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

#### \[h2\]OH\_MediaAsset\_GetTitle()

MediaLibrary\_ErrorCode OH\_MediaAsset\_GetTitle(OH\_MediaAsset\* mediaAsset, const char\*\* title)

**Description**

Obtains the title of a media asset.

**Since**: 13

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |
| const char\*\* title | Pointer to the media asset title obtained. |

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

#### \[h2\]OH\_MediaAsset\_Release()

MediaLibrary\_ErrorCode OH\_MediaAsset\_Release(OH\_MediaAsset\* mediaAsset)

**Description**

Releases a media asset.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAsset](../../structs/oh-mediaasset/document.md)\* mediaAsset | Pointer to an [OH\_MediaAsset](../../structs/oh-mediaasset/document.md) instance. |

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
