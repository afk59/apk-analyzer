# native\_avformat.h

#### Overview

The file declares the functions and enums related to OH\_AVFormat.

**File to include**: <multimedia/player\_framework/native\_avformat.h>

**Library**: libnative\_media\_core.so

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Related module**: [Core](../../modules/core/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) | OH\_AVFormat | Describes a native object for the OH\_AVFormat interface. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVPixelFormat](#oh_avpixelformat) | OH\_AVPixelFormat | Enumerates the video pixel formats. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat \*OH\_AVFormat\_Create(void)](#oh_avformat_create) | Create an OH\_AVFormat instance for reading data. |
| [struct OH\_AVFormat \*OH\_AVFormat\_CreateAudioFormat(const char \*mimeType, int32\_t sampleRate, int32\_t channelCount)](#oh_avformat_createaudioformat) | Creates an audio OH\_AVFormat instance with specified parameters for reading and writing data. |
| [struct OH\_AVFormat \*OH\_AVFormat\_CreateVideoFormat(const char \*mimeType, int32\_t width, int32\_t height)](#oh_avformat_createvideoformat) | Creates a video OH\_AVFormat instance with specified parameters for reading and writing data. |
| [void OH\_AVFormat\_Destroy(struct OH\_AVFormat \*format)](#oh_avformat_destroy) | Destroys an OH\_AVFormat instance. The instance cannot be destroyed repeatedly. |
| [bool OH\_AVFormat\_Copy(struct OH\_AVFormat \*to, struct OH\_AVFormat \*from)](#oh_avformat_copy) | Copies an OH\_AVFormat instance. |
| [bool OH\_AVFormat\_SetIntValue(struct OH\_AVFormat \*format, const char \*key, int32\_t value)](#oh_avformat_setintvalue) | Assigns a value of the int type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the int type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables). |
| [bool OH\_AVFormat\_SetLongValue(struct OH\_AVFormat \*format, const char \*key, int64\_t value)](#oh_avformat_setlongvalue) | Assigns a value of the long type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the long type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables). |
| [bool OH\_AVFormat\_SetFloatValue(struct OH\_AVFormat \*format, const char \*key, float value)](#oh_avformat_setfloatvalue) | Assigns a value of the float type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the float type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables). |
| [bool OH\_AVFormat\_SetDoubleValue(struct OH\_AVFormat \*format, const char \*key, double value)](#oh_avformat_setdoublevalue) | Assigns a value of the double type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the double type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables). |
| [bool OH\_AVFormat\_SetStringValue(struct OH\_AVFormat \*format, const char \*key, const char \*value)](#oh_avformat_setstringvalue) | Assigns a value of the string type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the string type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables). |
| [bool OH\_AVFormat\_SetBuffer(struct OH\_AVFormat \*format, const char \*key, const uint8\_t \*addr, size\_t size)](#oh_avformat_setbuffer) | Writes data blocks of a specified length to an OH\_AVFormat instance. This function can be used to set only parameters of the buffer type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables). |
| [bool OH\_AVFormat\_GetIntValue(struct OH\_AVFormat \*format, const char \*key, int32\_t \*out)](#oh_avformat_getintvalue) | Obtains the value of the int type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. |
| [bool OH\_AVFormat\_GetLongValue(struct OH\_AVFormat \*format, const char \*key, int64\_t \*out)](#oh_avformat_getlongvalue) | Obtains the value of the long type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. |
| [bool OH\_AVFormat\_GetFloatValue(struct OH\_AVFormat \*format, const char \*key, float \*out)](#oh_avformat_getfloatvalue) | Obtains the value of the float type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. |
| [bool OH\_AVFormat\_GetDoubleValue(struct OH\_AVFormat \*format, const char \*key, double \*out)](#oh_avformat_getdoublevalue) | Obtains the value of the double type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. |
| [bool OH\_AVFormat\_GetStringValue(struct OH\_AVFormat \*format, const char \*key, const char \*\*out)](#oh_avformat_getstringvalue) | Obtains the value of the string type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. |
| [bool OH\_AVFormat\_GetBuffer(struct OH\_AVFormat \*format, const char \*key, uint8\_t \*\*addr, size\_t \*size)](#oh_avformat_getbuffer) | Reads data blocks of a specified length from an OH\_AVFormat instance. |
| [bool OH\_AVFormat\_GetIntBuffer(struct OH\_AVFormat \*format, const char \*key, int32\_t \*\*addr, size\_t \*size)](#oh_avformat_getintbuffer) | 
Reads an array of int32\_t data from an OH\_AVFormat instance.

Note that the buffer lifecycle is bound to the OH\_AVFormat instance. The buffer becomes invalid automatically when the OH\_AVFormat instance is destroyed.

To keep the data for an extended period, explicitly copy the data to newly allocated memory.

 |
| [const char \*OH\_AVFormat\_DumpInfo(struct OH\_AVFormat \*format)](#oh_avformat_dumpinfo) | Returns a string consisting of key-value pairs in an OH\_AVFormat instance. A string of up to 1024 bytes can be returned. The string pointer is released when the OH\_AVFormat instance is destroyed. |
| [bool OH\_AVFormat\_SetIntBuffer(struct OH\_AVFormat \*format, const char \*key, const int32\_t \*addr, size\_t size)](#oh_avformat_setintbuffer) | Writes data blocks of the int32\_t type with a specified length to an OH\_AVFormat instance. |

#### Enum Description

#### \[h2\]OH\_AVPixelFormat

enum OH\_AVPixelFormat

**Description**

Enumerates the video pixel formats.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

| Value | Description |
| :-- | :-- |
| AV\_PIXEL\_FORMAT\_YUVI420 = 1 | YUV 420 Planar. |
| AV\_PIXEL\_FORMAT\_NV12 = 2 | NV12. YUV 420 semi-planar. |
| AV\_PIXEL\_FORMAT\_NV21 = 3 | NV21. YVU 420 semi-planar. |
| AV\_PIXEL\_FORMAT\_SURFACE\_FORMAT = 4 | Pixel format obtained from the surface. This value takes effect only in surface mode. |
| AV\_PIXEL\_FORMAT\_RGBA = 5 | RGBA8888. |
| AV\_PIXEL\_FORMAT\_RGBA1010102 = 6 | 
RGBA1010102.

**Since**: 20

 |

#### Function Description

#### \[h2\]OH\_AVFormat\_Create()

struct OH\_AVFormat \*OH\_AVFormat\_Create(void)

**Description**

Create an OH\_AVFormat instance for reading data.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \* | Pointer to an OH\_AVFormat instance. If system resources are insufficient, NULL is returned. |

#### \[h2\]OH\_AVFormat\_CreateAudioFormat()

struct OH\_AVFormat \*OH\_AVFormat\_CreateAudioFormat(const char \*mimeType, int32\_t sampleRate, int32\_t channelCount)

**Description**

Creates an audio OH\_AVFormat instance with specified parameters for reading and writing data.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*mimeType | Pointer to a string that describes the MIME type. For details, see [AVCODEC\_MIMETYPE](../native-avcodec-base-h/document.md#variables). |
| int32\_t sampleRate | Sampling rate, in Hz. |
| int32\_t channelCount | Number of audio channels. For example, 1 indicates mono and 2 indicates stereo. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \* | 
Pointer to the OH\_AVFormat instance created. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **mimeType** is NULL.

2\. System resources are insufficient.

 |

#### \[h2\]OH\_AVFormat\_CreateVideoFormat()

struct OH\_AVFormat \*OH\_AVFormat\_CreateVideoFormat(const char \*mimeType, int32\_t width, int32\_t height)

**Description**

Creates a video OH\_AVFormat instance with specified parameters for reading and writing data.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*mimeType | Pointer to a string that describes the MIME type. For details, see [AVCODEC\_MIMETYPE](../native-avcodec-base-h/document.md#variables). |
| int32\_t width | Image width, in pixels. |
| int32\_t height | Image height, in pixels. |

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \* | 
Pointer to the OH\_AVFormat instance created. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **mimeType** is NULL.

2\. System resources are insufficient.

 |

#### \[h2\]OH\_AVFormat\_Destroy()

void OH\_AVFormat\_Destroy(struct OH\_AVFormat \*format)

**Description**

Destroys an OH\_AVFormat instance. The instance cannot be destroyed repeatedly.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |

#### \[h2\]OH\_AVFormat\_Copy()

bool OH\_AVFormat\_Copy(struct OH\_AVFormat \*to, struct OH\_AVFormat \*from)

**Description**

Copies an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*to | Pointer to the OH\_AVFormat instance to which the data will be copied. |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*from | Pointer to the OH\_AVFormat instance from which the data will be copied. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The input parameter is nullptr.

2\. The value of **OH\_AVFormat** fails parameter structure verification.

 |

#### \[h2\]OH\_AVFormat\_SetIntValue()

bool OH\_AVFormat\_SetIntValue(struct OH\_AVFormat \*format, const char \*key, int32\_t value)

**Description**

Assigns a value of the int type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the int type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables).

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to write. |
| int32\_t value | Value of the data to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value type corresponding to the key is incorrect.

 |

#### \[h2\]OH\_AVFormat\_SetLongValue()

bool OH\_AVFormat\_SetLongValue(struct OH\_AVFormat \*format, const char \*key, int64\_t value)

**Description**

Assigns a value of the long type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the long type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables).

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to write. |
| int64\_t value | Value of the data to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value type corresponding to the key is incorrect.

 |

#### \[h2\]OH\_AVFormat\_SetFloatValue()

bool OH\_AVFormat\_SetFloatValue(struct OH\_AVFormat \*format, const char \*key, float value)

**Description**

Assigns a value of the float type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the float type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables).

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to write. |
| float value | Value of the data to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value type corresponding to the key is incorrect.

 |

#### \[h2\]OH\_AVFormat\_SetDoubleValue()

bool OH\_AVFormat\_SetDoubleValue(struct OH\_AVFormat \*format, const char \*key, double value)

**Description**

Assigns a value of the double type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the double type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables).

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to write. |
| double value | Value of the data to write. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value type corresponding to the key is incorrect.

 |

#### \[h2\]OH\_AVFormat\_SetStringValue()

bool OH\_AVFormat\_SetStringValue(struct OH\_AVFormat \*format, const char \*key, const char \*value)

**Description**

Assigns a value of the string type to a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance. This function can be used to set only parameters of the string type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables).

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to write. |
| const char \*value | Pointer to the data to be written to the string. The length should not exceed 256 bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The passed-in value of **value** is a null pointer.

5\. The value type corresponding to the key is incorrect.

 |

#### \[h2\]OH\_AVFormat\_SetBuffer()

bool OH\_AVFormat\_SetBuffer(struct OH\_AVFormat \*format, const char \*key, const uint8\_t \*addr, size\_t size)

**Description**

Writes data blocks of a specified length to an OH\_AVFormat instance. This function can be used to set only parameters of the buffer type. For details, see [native\_avcodec\_base.h](../native-avcodec-base-h/document.md#variables).

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to write. |
| const uint8\_t \*addr | Pointer to the address to which data is written. The lifecycle is managed by the developer. |
| size\_t size | Length of the data written, in MB. The value range is (0, 1\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **addr** is nullptr.

5\. The size is 0 or exceeds the upper limit 1 MB.

6\. The value type corresponding to the key is incorrect.

 |

#### \[h2\]OH\_AVFormat\_GetIntValue()

bool OH\_AVFormat\_GetIntValue(struct OH\_AVFormat \*format, const char \*key, int32\_t \*out)

**Description**

Obtains the value of the int type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to read. |
| int32\_t \*out | Pointer to the value of the data read. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **out** is nullptr.

5\. The obtained key does not exist or is not set.

 |

#### \[h2\]OH\_AVFormat\_GetLongValue()

bool OH\_AVFormat\_GetLongValue(struct OH\_AVFormat \*format, const char \*key, int64\_t \*out)

**Description**

Obtains the value of the long type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to read. |
| int64\_t \*out | Pointer to the value of the data read. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **out** is nullptr.

5\. The obtained key does not exist or is not set.

 |

#### \[h2\]OH\_AVFormat\_GetFloatValue()

bool OH\_AVFormat\_GetFloatValue(struct OH\_AVFormat \*format, const char \*key, float \*out)

**Description**

Obtains the value of the float type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to read. |
| float \*out | Pointer to the value of the data read. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **out** is nullptr.

5\. The obtained key does not exist or is not set.

 |

#### \[h2\]OH\_AVFormat\_GetDoubleValue()

bool OH\_AVFormat\_GetDoubleValue(struct OH\_AVFormat \*format, const char \*key, double \*out)

**Description**

Obtains the value of the double type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to read. |
| double \*out | Pointer to the value of the data read. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **out** is nullptr.

5\. The obtained key does not exist or is not set.

 |

#### \[h2\]OH\_AVFormat\_GetStringValue()

bool OH\_AVFormat\_GetStringValue(struct OH\_AVFormat \*format, const char \*key, const char \*\*out)

**Description**

Obtains the value of the string type of a [key](../../modules/codecbase/document.md#media-data-key-value-pairs) in an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to read. |
| const char \*\*out | Double pointer to the string read. The lifecycle of the **out** data matches the string in **format**. To keep the **out** data for an extended period of time, you must copy it to the memory. The maximum length of the output string is 256 bytes. If the length exceeds 256 bytes, **false** is returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **out** is nullptr.

5\. The system resources are insufficient.

6\. The obtained key does not exist or is not set.

7\. The length of the **out** data exceeds 256 bytes.

 |

#### \[h2\]OH\_AVFormat\_GetBuffer()

bool OH\_AVFormat\_GetBuffer(struct OH\_AVFormat \*format, const char \*key, uint8\_t \*\*addr, size\_t \*size)

**Description**

Reads data blocks of a specified length from an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to read. |
| uint8\_t \*\*addr | Double pointer to the address where the data read is stored. The data read is destroyed when the OH\_AVFormat instance is destroyed. To hold the data for an extended period of time, copy it to the memory. |
| size\_t \*size | Pointer to the size of the data read. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **addr** is nullptr.

5\. The value of **size** is nullptr.

6\. The obtained key does not exist or is not set.

 |

#### \[h2\]OH\_AVFormat\_GetIntBuffer()

bool OH\_AVFormat\_GetIntBuffer(struct OH\_AVFormat \*format, const char \*key, int32\_t \*\*addr, size\_t \*size)

**Description**

Reads an array of int32\_t data from an OH\_AVFormat instance.

Note that the buffer lifecycle is bound to the OH\_AVFormat instance. The buffer becomes invalid automatically when the OH\_AVFormat instance is destroyed.

To keep the data for an extended period, explicitly copy the data to newly allocated memory.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to read. |
| int32\_t \*\*addr | Double pointer to the memory where the data is stored. |
| size\_t \*size | Pointer to the number of elements read. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **addr** is nullptr.

5\. The value of **size** is nullptr.

 |

#### \[h2\]OH\_AVFormat\_DumpInfo()

const char \*OH\_AVFormat\_DumpInfo(struct OH\_AVFormat \*format)

**Description**

Returns a string consisting of key-value pairs in an OH\_AVFormat instance. A string of up to 1024 bytes can be returned. The string pointer is released when the OH\_AVFormat instance is destroyed.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| const char \* | 
A string consisting of key-value pairs. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **format** is NULL.

2\. System resources are insufficient.

 |

#### \[h2\]OH\_AVFormat\_SetIntBuffer()

bool OH\_AVFormat\_SetIntBuffer(struct OH\_AVFormat \*format, const char \*key, const int32\_t \*addr, size\_t size)

**Description**

Writes data blocks of the int32\_t type with a specified length to an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [struct OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |
| const char \*key | Pointer to the key of the data to write. |
| const int32\_t \*addr | Pointer to the address to which data is written. The lifecycle is managed by the developer. |
| size\_t size | Length of the data to write, in units of elements, not bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
**true** if the operation is successful; **false** otherwise.

The possible causes of an operation failure are as follows:

1\. The value of **format** is nullptr.

2\. The value of **format** fails parameter structure verification.

3\. The value of **key** is nullptr.

4\. The value of **addr** is nullptr.

5\. The value of **size** is **0**.

 |
