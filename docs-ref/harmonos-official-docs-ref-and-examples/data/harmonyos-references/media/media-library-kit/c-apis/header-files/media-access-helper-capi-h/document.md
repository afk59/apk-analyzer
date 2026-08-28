# media\_access\_helper\_capi.h

#### Overview

The file declares the APIs for album management.

You can use the APIs to create an album, and access and modify the media data in the album.

**Library**: libmedia\_asset\_manager.so

**File to include**: <multimedia/media\_library/media\_access\_helper\_capi.h>

**System capability**: SystemCapability.FileManagement.PhotoAccessHelper.Core

**Since**: 12

**Related module**: [MediaAssetManager](../../modules/mediaassetmanager/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode OH\_MediaAccessHelper\_ApplyChanges(OH\_MediaAssetChangeRequest\* changeRequest)](#oh_mediaaccesshelper_applychanges) | Applies changes to an asset or album. |

#### Function Description

#### \[h2\]OH\_MediaAccessHelper\_ApplyChanges()

MediaLibrary\_ErrorCode OH\_MediaAccessHelper\_ApplyChanges(OH\_MediaAssetChangeRequest\* changeRequest)

**Description**

Applies changes to an asset or album.

**Required permissions**: ohos.permission.WRITE\_IMAGEVIDEO

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_MediaAssetChangeRequest](../../structs/oh-mediaassetchangerequest/document.md)\* changeRequest | Change request. |

**Return value**

| Type | Description |
| :-- | :-- |
| [MediaLibrary\_ErrorCode](../media-asset-base-capi-h/document.md#medialibrary_errorcode) | 
**MEDIA\_LIBRARY\_OK**: operation success.

**MEDIA\_LIBRARY\_PARAMETER\_ERROR**: incorrect parameters. Possible reasons:

1\. A mandatory parameter is not specified.

2\. A parameter type is incorrect.

3\. Parameter verification fails.

**MEDIA\_LIBRARY\_PERMISSION\_DENIED**: access denied due to lack of permission.

**MEDIA\_LIBRARY\_INTERNAL\_SYSTEM\_ERROR**: internal system error.

 |
