# avmetadata\_extractor.h

#### Overview

The file declares the AVMetadataExtractor APIs. You can use the APIs to obtain metadata from media assets.

**File to include**: <multimedia/player\_framework/avmetadata\_extractor.h>

**Library**: libavmetadata\_extractor.so

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Since**: 18

**Related module**: [AVMetadataExtractor](../../modules/avmetadataextractor/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVMetadataExtractor](../../structs/oh-avmetadataextractor/document.md) | OH\_AVMetadataExtractor | Describes the OH\_AVMetadataExtractor. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVMetadataExtractor\* OH\_AVMetadataExtractor\_Create(void)](#oh_avmetadataextractor_create) | Creates an OH\_AVMetadataExtractor instance. |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_SetFDSource(OH\_AVMetadataExtractor\* extractor, int32\_t fd, int64\_t offset, int64\_t size)](#oh_avmetadataextractor_setfdsource) | Sets a data source based on the media file descriptor. |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_FetchMetadata(OH\_AVMetadataExtractor\* extractor, OH\_AVFormat\* avMetadata)](#oh_avmetadataextractor_fetchmetadata) | Obtains metadata from a media asset. This function must be called after [OH\_AVMetadataExtractor\_SetFDSource](#oh_avmetadataextractor_setfdsource). |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_FetchAlbumCover(OH\_AVMetadataExtractor\* extractor, OH\_PixelmapNative\*\* pixelMap)](#oh_avmetadataextractor_fetchalbumcover) | Obtains the cover of an audio album. This function must be called after [OH\_AVMetadataExtractor\_SetFDSource](#oh_avmetadataextractor_setfdsource). |
| [OH\_AVErrCode OH\_AVMetadataExtractor\_Release(OH\_AVMetadataExtractor\* extractor)](#oh_avmetadataextractor_release) | Releases the resources used by the OH\_AVMetadataExtractor instance and destroys the instance. |

#### Function Description

#### \[h2\]OH\_AVMetadataExtractor\_Create()

OH\_AVMetadataExtractor\* OH\_AVMetadataExtractor\_Create(void)

**Description**

Creates an OH\_AVMetadataExtractor instance.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Since**: 18

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVMetadataExtractor](../../structs/oh-avmetadataextractor/document.md)\* | 
Pointer to the OH\_AVMetadataExtractor instance created if the operation is successful; nullptr otherwise.

Possible cause of failures: **HstEngineFactory::CreateAVMetadataHelperEngine** fails to run.

 |

#### \[h2\]OH\_AVMetadataExtractor\_SetFDSource()

OH\_AVErrCode OH\_AVMetadataExtractor\_SetFDSource(OH\_AVMetadataExtractor\* extractor,int32\_t fd, int64\_t offset, int64\_t size)

**Description**

Sets a data source based on the media file descriptor.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVMetadataExtractor](../../structs/oh-avmetadataextractor/document.md)\* extractor | Pointer to the OH\_AVMetadataExtractor instance. |
| int32\_t fd | File descriptor of the media source. |
| int64\_t offset | Offset of the media source in the file descriptor. |
| int64\_t size | Size of the media source. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **extractor** is nullptr or a parameter is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is forbidden.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVMetadataExtractor\_FetchMetadata()

OH\_AVErrCode OH\_AVMetadataExtractor\_FetchMetadata(OH\_AVMetadataExtractor\* extractor, OH\_AVFormat\* avMetadata)

**Description**

Obtains metadata from a media asset.

This function must be called after [OH\_AVMetadataExtractor\_SetFDSource](#oh_avmetadataextractor_setfdsource).

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVMetadataExtractor](../../structs/oh-avmetadataextractor/document.md)\* extractor | Pointer to the OH\_AVMetadataExtractor instance. |
| [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* avMetadata | Pointer to the OH\_AVFormat instance, which contains the obtained metadata. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **extractor** is nullptr or a parameter is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is forbidden.

**AV\_ERR\_UNSUPPORTED\_FORMAT**: The format is not supported.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVMetadataExtractor\_FetchAlbumCover()

OH\_AVErrCode OH\_AVMetadataExtractor\_FetchAlbumCover(OH\_AVMetadataExtractor\* extractor, OH\_PixelmapNative\*\* pixelMap)

**Description**

Obtains the cover of an audio album.

This function must be called after [OH\_AVMetadataExtractor\_SetFDSource](#oh_avmetadataextractor_setfdsource).

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVMetadataExtractor](../../structs/oh-avmetadataextractor/document.md)\* extractor | Pointer to the OH\_AVMetadataExtractor instance. |
| [OH\_PixelmapNative](../../../../image-kit/c-apis/structs/oh-pixelmapnative/document.md)\*\* pixelMap | Double pointer to the album cover obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **extractor** is nullptr or a parameter is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is forbidden.

**AV\_ERR\_UNSUPPORTED\_FORMAT**: The format is not supported.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVMetadataExtractor\_Release()

OH\_AVErrCode OH\_AVMetadataExtractor\_Release(OH\_AVMetadataExtractor\* extractor)

**Description**

Releases the resources used by the OH\_AVMetadataExtractor instance and destroys the instance.

**System capability**: SystemCapability.Multimedia.Media.AVMetadataExtractor

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVMetadataExtractor](../../structs/oh-avmetadataextractor/document.md)\* extractor | Pointer to the OH\_AVMetadataExtractor instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **extractor** is nullptr or a parameter is invalid.

 |
