# native\_avmetadata.h

#### Overview

The file declares the definitions of playback control metadata.

**File to include**: <multimedia/av\_session/native\_avmetadata.h>

**Library**: libohavsession.so

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Since**: 13

**Related module**: [OHAVSession](../../modules/ohavsession/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVMetadataBuilderStruct](../../structs/oh-avmetadatabuilderstruct/document.md) | OH\_AVMetadataBuilder | Defines a struct for the session metadata builder. The builder is used to construct session metadata. |
| [OH\_AVMetadataStruct](../../structs/oh-avmetadatastruct/document.md) | OH\_AVMetadata | Defines a struct for the session metadata. It is an AVMetadata instance set for a media asset. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | AVMetadata\_Result | Enumerates the error codes related to metadata operations. |
| [AVMetadata\_SkipIntervals](#avmetadata_skipintervals) | AVMetadata\_SkipIntervals | Enumerates the fast-forward or rewind intervals supported by the media session. |
| [AVMetadata\_DisplayTag](#avmetadata_displaytag) | AVMetadata\_DisplayTag | Enumerates the display tags of the media asset. The display tag is a special type identifier of the media audio source. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_Create(OH\_AVMetadataBuilder\*\* builder)](#oh_avmetadatabuilder_create) | Creates a metadata builder. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_Destroy(OH\_AVMetadataBuilder\* builder)](#oh_avmetadatabuilder_destroy) | Destroys a metadata builder. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetAssetId(OH\_AVMetadataBuilder\* builder, const char\* assetId)](#oh_avmetadatabuilder_setassetid) | Sets the ID of the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetTitle(OH\_AVMetadataBuilder\* builder, const char\* title)](#oh_avmetadatabuilder_settitle) | Sets a title for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetArtist(OH\_AVMetadataBuilder\* builder, const char\* artist)](#oh_avmetadatabuilder_setartist) | Sets an artist for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetAuthor(OH\_AVMetadataBuilder\* builder, const char\* author)](#oh_avmetadatabuilder_setauthor) | Sets an author for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetAlbum(OH\_AVMetadataBuilder\* builder, const char\* album)](#oh_avmetadatabuilder_setalbum) | Sets an album name for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetWriter(OH\_AVMetadataBuilder\* builder, const char\* writer)](#oh_avmetadatabuilder_setwriter) | Sets a writer for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetComposer(OH\_AVMetadataBuilder\* builder, const char\* composer)](#oh_avmetadatabuilder_setcomposer) | Sets a composer for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetDuration(OH\_AVMetadataBuilder\* builder, int64\_t duration)](#oh_avmetadatabuilder_setduration) | Sets the playback duration for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetMediaImageUri(OH\_AVMetadataBuilder\* builder, const char\* mediaImageUri)](#oh_avmetadatabuilder_setmediaimageuri) | Sets an image for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetSubtitle(OH\_AVMetadataBuilder\* builder, const char\* subtitle)](#oh_avmetadatabuilder_setsubtitle) | Sets a subtitle for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetDescription(OH\_AVMetadataBuilder\* builder, const char\* description)](#oh_avmetadatabuilder_setdescription) | Sets a description for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetLyric(OH\_AVMetadataBuilder\* builder, const char\* lyric)](#oh_avmetadatabuilder_setlyric) | Sets lyrics for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetSkipIntervals(OH\_AVMetadataBuilder\* builder, AVMetadata\_SkipIntervals intervals)](#oh_avmetadatabuilder_setskipintervals) | Sets the skip intervals for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_SetDisplayTags(OH\_AVMetadataBuilder\* builder, int32\_t tags)](#oh_avmetadatabuilder_setdisplaytags) | Sets display tags for the media asset. |
| [AVMetadata\_Result OH\_AVMetadataBuilder\_GenerateAVMetadata(OH\_AVMetadataBuilder\* builder, OH\_AVMetadata\*\* avMetadata)](#oh_avmetadatabuilder_generateavmetadata) | Generates an OH\_AVMetadata object. |
| [AVMetadata\_Result OH\_AVMetadata\_Destroy(OH\_AVMetadata\* avMetadata)](#oh_avmetadata_destroy) | Releases an OH\_AVMetadata object. |

#### Enums

#### \[h2\]AVMetadata\_Result

enum AVMetadata\_Result

**Description**

Enumerates the error codes related to metadata operations.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| AVMETADATA\_SUCCESS = 0 | Operation successful. |
| AVMETADATA\_ERROR\_INVALID\_PARAM = 1 | Incorrect parameter. |
| AVMETADATA\_ERROR\_NO\_MEMORY = 2 | Insufficient memory. |

#### \[h2\]AVMetadata\_SkipIntervals

enum AVMetadata\_SkipIntervals

**Description**

Enumerates the fast-forward or rewind intervals supported by the media session.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| SECONDS\_10 = 10 | The time is 10 seconds. |
| SECONDS\_15 = 15 | The time is 15 seconds. |
| SECONDS\_30 = 30 | The time is 30 seconds. |

#### \[h2\]AVMetadata\_DisplayTag

enum AVMetadata\_DisplayTag

**Description**

Enumerates the display tags of the media asset. The display tag is a special type identifier of the media audio source.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| AVSESSION\_DISPLAYTAG\_AUDIO\_VIVID = 1 | AUDIO VIVID. |

#### Function Description

#### \[h2\]OH\_AVMetadataBuilder\_Create()

AVMetadata\_Result OH\_AVMetadataBuilder\_Create(OH\_AVMetadataBuilder\*\* builder)

**Description**

Creates a metadata builder.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\*\* builder | Double pointer to the builder created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**: **builder** is nullptr.

**AVMETADATA\_ERROR\_NO\_MEMORY**: There is no sufficient memory.

 |

#### \[h2\]OH\_AVMetadataBuilder\_Destroy()

AVMetadata\_Result OH\_AVMetadataBuilder\_Destroy(OH\_AVMetadataBuilder\* builder)

**Description**

Destroys a metadata builder.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**: **builder** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetAssetId()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetAssetId(OH\_AVMetadataBuilder\* builder, const char\* assetId)

**Description**

Sets the ID of the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* assetId | Pointer to the asset ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **assetId** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetTitle()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetTitle(OH\_AVMetadataBuilder\* builder, const char\* title)

**Description**

Sets a title for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* title | Pointer to the title. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **title** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetArtist()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetArtist(OH\_AVMetadataBuilder\* builder, const char\* artist)

**Description**

Sets an artist for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* artist | Pointer to the artist. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **artist** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetAuthor()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetAuthor(OH\_AVMetadataBuilder\* builder, const char\* author)

**Description**

Sets an author for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* author | Pointer to the author. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **author** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetAlbum()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetAlbum(OH\_AVMetadataBuilder\* builder, const char\* album)

**Description**

Sets an album name for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* album | Pointer to the album name. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **album** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetWriter()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetWriter(OH\_AVMetadataBuilder\* builder, const char\* writer)

**Description**

Sets a writer for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* writer | Pointer to the writer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **writer** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetComposer()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetComposer(OH\_AVMetadataBuilder\* builder, const char\* composer)

**Description**

Sets a composer for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* composer | Pointer to the composer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **composer** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetDuration()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetDuration(OH\_AVMetadataBuilder\* builder, int64\_t duration)

**Description**

Sets the playback duration for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| int64\_t duration | Playback duration, in ms. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**: **builder** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetMediaImageUri()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetMediaImageUri(OH\_AVMetadataBuilder\* builder, const char\* mediaImageUri)

**Description**

Sets an image for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* mediaImageUri | Pointer to the URI of the image. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **mediaImageUri** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetSubtitle()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetSubtitle(OH\_AVMetadataBuilder\* builder, const char\* subtitle)

**Description**

Sets a subtitle for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* subtitle | Pointer to the subtitle. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **subtitle** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetDescription()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetDescription(OH\_AVMetadataBuilder\* builder, const char\* description)

**Description**

Sets a description for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* description | Pointer to the description. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **description** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetLyric()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetLyric(OH\_AVMetadataBuilder\* builder, const char\* lyric)

**Description**

Sets lyrics for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| const char\* lyric | Pointer to the lyrics in the LRC format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **lyric** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetSkipIntervals()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetSkipIntervals(OH\_AVMetadataBuilder\* builder,AVMetadata\_SkipIntervals intervals)

**Description**

Sets the skip intervals for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| [AVMetadata\_SkipIntervals](#avmetadata_skipintervals) intervals | Skip intervals. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **intervals** is invalid.

 |

#### \[h2\]OH\_AVMetadataBuilder\_SetDisplayTags()

AVMetadata\_Result OH\_AVMetadataBuilder\_SetDisplayTags(OH\_AVMetadataBuilder\* builder, int32\_t tags)

**Description**

Sets display tags for the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| int32\_t tags | Tags of the media asset displayed on the playback control page. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**: **builder** is nullptr.

 |

#### \[h2\]OH\_AVMetadataBuilder\_GenerateAVMetadata()

AVMetadata\_Result OH\_AVMetadataBuilder\_GenerateAVMetadata(OH\_AVMetadataBuilder\* builder,OH\_AVMetadata\*\* avMetadata)

**Description**

Generates an OH\_AVMetadata object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataBuilder](../../structs/oh-avmetadatabuilderstruct/document.md)\* builder | Pointer to an OH\_AVMetadataBuilder instance. |
| [OH\_AVMetadata](../../structs/oh-avmetadatastruct/document.md)\*\* avMetadata | Double pointer to the OH\_AVMetadata object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_NO\_MEMORY**: The memory is insufficient.

**AVMETADATA\_ERROR\_INVALID\_PARAM**:

1\. **builder** is nullptr.

2\. **avMetadata** is nullptr.

 |

#### \[h2\]OH\_AVMetadata\_Destroy()

AVMetadata\_Result OH\_AVMetadata\_Destroy(OH\_AVMetadata\* avMetadata)

**Description**

Releases an OH\_AVMetadata object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadata](../../structs/oh-avmetadatastruct/document.md)\* avMetadata | Pointer to an OH\_AVMetadata object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVMetadata\_Result](#avmetadata_result) | 
**AVMETADATA\_SUCCESS**: The function is executed successfully.

**AVMETADATA\_ERROR\_INVALID\_PARAM**: **avMetadata** is nullptr.

 |
