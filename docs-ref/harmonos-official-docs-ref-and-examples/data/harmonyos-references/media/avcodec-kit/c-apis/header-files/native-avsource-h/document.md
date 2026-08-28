# native\_avsource.h

#### Overview

The file declares the APIs for parsing audio and video media data.

**File to include**: <multimedia/player\_framework/native\_avsource.h>

**Library**: libnative\_media\_avsource.so

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Related module**: [AVSource](../../modules/avsource/document.md)

**Sample**: [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) | OH\_AVSource | Describes a native object for the media source interface. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVSource \*OH\_AVSource\_CreateWithDataSource(OH\_AVDataSource \*dataSource)](#oh_avsource_createwithdatasource) | 
Creates an OH\_AVSource instance with a user-defined data source. You can release the instance by calling [OH\_AVSource\_Destroy](#oh_avsource_destroy).

The lifecycle of **dataSource** must be the same as that of the returned OH\_AVSource \* pointer.

 |
| [OH\_AVSource \*OH\_AVSource\_CreateWithDataSourceExt(OH\_AVDataSourceExt \*dataSource, void \*userData)](#oh_avsource_createwithdatasourceext) | 

Creates an OH\_AVSource instance with a user-defined data source. You can release the instance by calling [OH\_AVSource\_Destroy](#oh_avsource_destroy).

User-defined data can be passed to its callback functions through the **userData** parameter.

The lifecycle of **dataSource** must be the same as that of the returned OH\_AVSource \* pointer.

 |
| [OH\_AVSource \*OH\_AVSource\_CreateWithURI(char \*uri)](#oh_avsource_createwithuri) | Creates an OH\_AVSource instance based on a URI. You can release the instance by calling [OH\_AVSource\_Destroy](#oh_avsource_destroy). This function supports only HTTP progressive streaming media, but not HLS/DASH streaming media. For HLS/DASH streaming media playback, use the AVPlayer for development. |
| [OH\_AVSource \*OH\_AVSource\_CreateWithFD(int32\_t fd, int64\_t offset, int64\_t size)](#oh_avsource_createwithfd) | 

Creates an OH\_AVSource instance based on an FD. You can release the instance by calling [OH\_AVSource\_Destroy](#oh_avsource_destroy).

If **offset** is not the start position of the file or **size** is not the file size, undefined errors such as creation failure and demultiplexing failure may occur due to incomplete data obtained.

 |
| [OH\_AVErrCode OH\_AVSource\_Destroy(OH\_AVSource \*source)](#oh_avsource_destroy) | 

Destroys an OH\_AVSource instance and clears internal resources.

An instance can be destroyed only once. The destroyed instance cannot be used until it is re-created. You are advised to set the pointer to NULL after the instance is destroyed.

 |
| [OH\_AVFormat \*OH\_AVSource\_GetSourceFormat(OH\_AVSource \*source)](#oh_avsource_getsourceformat) | 

Obtains the basic information about a media resource file.

You must call [OH\_AVFormat\_Destroy](../native-avformat-h/document.md#oh_avformat_destroy) to release the OH\_AVFormat instance when its lifecycle ends.

 |
| [OH\_AVFormat \*OH\_AVSource\_GetTrackFormat(OH\_AVSource \*source, uint32\_t trackIndex)](#oh_avsource_gettrackformat) | 

Obtains the basic information about a track.

You must call [OH\_AVFormat\_Destroy](../native-avformat-h/document.md#oh_avformat_destroy) to release the OH\_AVFormat instance when its lifecycle ends.

 |
| [OH\_AVFormat \*OH\_AVSource\_GetCustomMetadataFormat(OH\_AVSource \*source)](#oh_avsource_getcustommetadataformat) | 

Obtains the basic information about custom metadata.

You must call [OH\_AVFormat\_Destroy](../native-avformat-h/document.md#oh_avformat_destroy) to release the OH\_AVFormat instance when its lifecycle ends.

 |

#### Function Description

#### \[h2\]OH\_AVSource\_CreateWithDataSource()

OH\_AVSource \*OH\_AVSource\_CreateWithDataSource(OH\_AVDataSource \*dataSource)

**Description**

Creates an OH\_AVSource instance with a user-defined data source. You can release the instance by calling [OH\_AVSource\_Destroy](#oh_avsource_destroy).

The lifecycle of **dataSource** must be the same as that of the returned OH\_AVSource \* pointer.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDataSource](../../structs/oh-avdatasource/document.md) \*dataSource | Pointer to user-defined data source. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \* | 
Pointer to the OH\_AVSource instance created. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **dataSource** is nullptr.

2\. The size of the data source is 0.

3\. Setting the data source fails.

4\. The memory is insufficient.

5\. The decoder engine is nullptr.

6\. dataSource->readAt == nullptr.

 |

#### \[h2\]OH\_AVSource\_CreateWithDataSourceExt()

OH\_AVSource \*OH\_AVSource\_CreateWithDataSourceExt(OH\_AVDataSourceExt \*dataSource, void \*userData)

**Description**

Creates an OH\_AVSource instance with a user-defined data source. You can release the instance by calling [OH\_AVSource\_Destroy](#oh_avsource_destroy).

User-defined data can be passed to its callback functions through the **userData** parameter.

The lifecycle of **dataSource** must be the same as that of the returned OH\_AVSource \* pointer.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVDataSourceExt](../../structs/oh-avdatasourceext/document.md) \*dataSource | Pointer to the data source struct, which is used to obtain the input data. |
| void \*userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \* | 
Pointer to the OH\_AVSource instance created. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **dataSource** is nullptr.

2\. The size of the data source is 0.

3\. Setting the data source fails.

4\. The memory is insufficient.

5\. The decoder engine is nullptr.

6\. dataSource->readAt == nullptr.

 |

#### \[h2\]OH\_AVSource\_CreateWithURI()

OH\_AVSource \*OH\_AVSource\_CreateWithURI(char \*uri)

**Description**

Creates an OH\_AVSource instance based on a URI. You can release the instance by calling [OH\_AVSource\_Destroy](#oh_avsource_destroy). This function supports only HTTP progressive streaming media, but not HLS/DASH streaming media. For HLS/DASH streaming media playback, use the AVPlayer for development.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| char \*uri | URI of the media resource. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \* | 
Pointer to the OH\_AVSource instance created. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The network is abnormal.

2\. The resource is invalid.

3\. The file format is not supported.

4\. The application configuration is intercepted because it contains plaintext data.

 |

#### \[h2\]OH\_AVSource\_CreateWithFD()

OH\_AVSource \*OH\_AVSource\_CreateWithFD(int32\_t fd, int64\_t offset, int64\_t size)

**Description**

Creates an OH\_AVSource instance based on an FD. You can release the instance by calling [OH\_AVSource\_Destroy](#oh_avsource_destroy).

If **offset** is not the start position of the file or **size** is not the file size, undefined errors such as creation failure and demultiplexing failure may occur due to incomplete data obtained.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t fd | FD of a media resource file. |
| int64\_t offset | Position from which data is to read. |
| int64\_t size | File size, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \* | 
Pointer to the OH\_AVSource instance created. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The FD is invalid.

2\. The offset is not the start position of the file.

3\. The size is incorrect.

4\. The resource is invalid.

5\. The file format is not supported.

 |

#### \[h2\]OH\_AVSource\_Destroy()

OH\_AVErrCode OH\_AVSource\_Destroy(OH\_AVSource \*source)

**Description**

Destroys an OH\_AVSource instance and clears internal resources.

An instance can be destroyed only once. The destroyed instance cannot be used until it is re-created. You are advised to set the pointer to NULL after the instance is destroyed.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \*source | Pointer to an OH\_AVSource instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**:

1\. The value of **source** is nullptr.

2\. The value of **source** does not point to an OH\_AVSource instance.

 |

#### \[h2\]OH\_AVSource\_GetSourceFormat()

OH\_AVFormat \*OH\_AVSource\_GetSourceFormat(OH\_AVSource \*source)

**Description**

Obtains the basic information about a media resource file.

You must call [OH\_AVFormat\_Destroy](../native-avformat-h/document.md#oh_avformat_destroy) to release the OH\_AVFormat instance when its lifecycle ends.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \*source | Pointer to an OH\_AVSource instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \* | 
Basic information about the file. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **source** is nullptr.

2\. The pointer is null or does not point to an OH\_AVSource instance.

3\. The source is not initialized.

 |

#### \[h2\]OH\_AVSource\_GetTrackFormat()

OH\_AVFormat \*OH\_AVSource\_GetTrackFormat(OH\_AVSource \*source, uint32\_t trackIndex)

**Description**

Obtains the basic information about a track.

You must call [OH\_AVFormat\_Destroy](../native-avformat-h/document.md#oh_avformat_destroy) to release the OH\_AVFormat instance when its lifecycle ends.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \*source | Pointer to an OH\_AVSource instance. |
| uint32\_t trackIndex | Index of the track whose information is to be obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \* | 
Basic information about the track. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **source** is invalid (either nullptr or a pointer to a non-OH\_AVSource instance).

2\. The track index is out of range.

3\. The source is not initialized.

 |

#### \[h2\]OH\_AVSource\_GetCustomMetadataFormat()

OH\_AVFormat \*OH\_AVSource\_GetCustomMetadataFormat(OH\_AVSource \*source)

**Description**

Obtains the basic information about custom metadata.

You must call [OH\_AVFormat\_Destroy](../native-avformat-h/document.md#oh_avformat_destroy) to release the OH\_AVFormat instance when its lifecycle ends.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSource](../../structs/oh-avsource/document.md) \*source | Pointer to an OH\_AVSource instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \* | 
Basic information about the metadata. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **source** is nullptr.

2\. The pointer is null or does not point to an OH\_AVSource instance.

3\. The source is not initialized.

 |
