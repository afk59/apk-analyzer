# avimage\_generator.h

#### Overview

The file declares the AVImageGenerator APIs. You can use the APIs to extract video frames at given time points from videos.

**File to include**: <multimedia/player\_framework/avimage\_generator.h>

**Library**: libavimage\_generator.so

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Since**: 18

**Related module**: [AVImageGenerator](../../modules/avimagegenerator/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVImageGenerator](../../structs/oh-avimagegenerator/document.md) | OH\_AVImageGenerator | Defines the type used for generating video frames at given time points. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVImageGenerator\* OH\_AVImageGenerator\_Create(void)](#oh_avimagegenerator_create) | Creates an OH\_AVImageGenerator instance, which is used to generate video frames at given time points. |
| [OH\_AVErrCode OH\_AVImageGenerator\_SetFDSource(OH\_AVImageGenerator\* generator, int32\_t fd, int64\_t offset, int64\_t size)](#oh_avimagegenerator_setfdsource) | Sets a data source based on the media file descriptor. |
| [OH\_AVErrCode OH\_AVImageGenerator\_FetchFrameByTime(OH\_AVImageGenerator\* generator, int64\_t timeUs, OH\_AVImageGenerator\_QueryOptions options, OH\_PixelmapNative\*\* pixelMap)](#oh_avimagegenerator_fetchframebytime) | 
Extracts a video frame at a given time from a video.

This function must be called after [OH\_AVImageGenerator\_SetFDSource](#oh_avimagegenerator_setfdsource).

 |
| [OH\_AVErrCode OH\_AVImageGenerator\_Release(OH\_AVImageGenerator\* generator)](#oh_avimagegenerator_release) | Releases the resources used by the OH\_AVImageGenerator instance and destroys the instance. |

#### Function Description

#### \[h2\]OH\_AVImageGenerator\_Create()

OH\_AVImageGenerator\* OH\_AVImageGenerator\_Create(void)

**Description**

Creates an OH\_AVImageGenerator instance, which is used to generate video frames at given time points.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Since**: 18

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVImageGenerator](../../structs/oh-avimagegenerator/document.md)\* | 
Pointer to the OH\_AVImageGenerator instance created if the operation is successful; nullptr otherwise.

Possible cause of failures: HstEngineFactory fails to create an AVMetadataHelperEngine.

 |

#### \[h2\]OH\_AVImageGenerator\_SetFDSource()

OH\_AVErrCode OH\_AVImageGenerator\_SetFDSource(OH\_AVImageGenerator\* generator,int32\_t fd, int64\_t offset, int64\_t size)

**Description**

Sets a data source based on the media file descriptor.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVImageGenerator](../../structs/oh-avimagegenerator/document.md)\* generator | Pointer to the OH\_AVImageGenerator instance. |
| int32\_t fd | File descriptor of the media source. |
| int64\_t offset | Offset of the media source in the file descriptor. |
| int64\_t size | Size of the media source. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **generator** is nullptr or a parameter is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is forbidden.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVImageGenerator\_FetchFrameByTime()

OH\_AVErrCode OH\_AVImageGenerator\_FetchFrameByTime(OH\_AVImageGenerator\* generator,int64\_t timeUs, OH\_AVImageGenerator\_QueryOptions options, OH\_PixelmapNative\*\* pixelMap)

**Description**

Extracts a video frame at a given time from a video.

This function must be called after [OH\_AVImageGenerator\_SetFDSource](#oh_avimagegenerator_setfdsource).

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVImageGenerator](../../structs/oh-avimagegenerator/document.md)\* generator | Pointer to the OH\_AVImageGenerator instance. |
| int64\_t timeUs | Time point of the video frame to be extracted in the video, in μs. |
| [OH\_AVImageGenerator\_QueryOptions](../avimage-generator-base-h/document.md#oh_avimagegenerator_queryoptions) options | Mappings between the given time points and video frames. |
| [OH\_PixelmapNative](../../../../image-kit/c-apis/structs/oh-pixelmapnative/document.md)\*\* pixelMap | Double pointer to the video frame object obtained. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **generator** is nullptr or a parameter is invalid.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is forbidden.

**AV\_ERR\_UNSUPPORTED\_FORMAT**: The format is not supported.

**AV\_ERR\_NO\_MEMORY**: Internal memory allocation failed.

 |

#### \[h2\]OH\_AVImageGenerator\_Release()

OH\_AVErrCode OH\_AVImageGenerator\_Release(OH\_AVImageGenerator\* generator)

**Description**

Releases the resources used by the OH\_AVImageGenerator instance and destroys the instance.

**System capability**: SystemCapability.Multimedia.Media.AVImageGenerator

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVImageGenerator](../../structs/oh-avimagegenerator/document.md)\* generator | Pointer to the OH\_AVImageGenerator instance. |

**Return value**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **generator** is nullptr or a parameter is invalid.

 |
