# native\_avbuffer.h

#### Overview

The file declares the functions of the media struct AVBuffer.

**File to include**: <multimedia/player\_framework/native\_avbuffer.h>

**Library**: libnative\_media\_core.so

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Related module**: [Core](../../modules/core/document.md)

**Sample**: [AVCodec](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/BasicFeature/Media/AVCodec)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) | OH\_AVBuffer | Describes a native object for the media memory interface. |
| [OH\_NativeBuffer](../../../../../graphics/arkgraphics-2d/c-apis/modules/oh-nativebuffer/document.md) | OH\_NativeBuffer | Describes a native object for the graphics memory interface. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer \*OH\_AVBuffer\_Create(int32\_t capacity)](#oh_avbuffer_create) | Creates an OH\_AVBuffer instance. You must call [OH\_AVBuffer\_Destroy](#oh_avbuffer_destroy) to manually release the OH\_AVBuffer instance returned. |
| [OH\_AVErrCode OH\_AVBuffer\_Destroy(OH\_AVBuffer \*buffer)](#oh_avbuffer_destroy) | Releases an OH\_AVBuffer instance. A buffer cannot be destroyed repeatedly. |
| [OH\_AVErrCode OH\_AVBuffer\_GetBufferAttr(OH\_AVBuffer \*buffer, OH\_AVCodecBufferAttr \*attr)](#oh_avbuffer_getbufferattr) | Obtains the basic attributes, including **pts**, **size**, **offset**, and **flags**, of a buffer. |
| [OH\_AVErrCode OH\_AVBuffer\_SetBufferAttr(OH\_AVBuffer \*buffer, const OH\_AVCodecBufferAttr \*attr)](#oh_avbuffer_setbufferattr) | Sets the basic attributes, including **pts**, **size**, **offset**, and **flags**, of a buffer. |
| [OH\_AVFormat \*OH\_AVBuffer\_GetParameter(OH\_AVBuffer \*buffer)](#oh_avbuffer_getparameter) | Obtains parameters except basic attributes of a buffer. The information is carried in an OH\_AVFormat instance. You must call [OH\_AVFormat\_Destroy](../native-avformat-h/document.md#oh_avformat_destroy) to manually release the OH\_AVFormat instance returned. |
| [OH\_AVErrCode OH\_AVBuffer\_SetParameter(OH\_AVBuffer \*buffer, const OH\_AVFormat \*format)](#oh_avbuffer_setparameter) | Sets parameters except basic attributes of a buffer. The information is carried in an OH\_AVFormat instance. |
| [uint8\_t \*OH\_AVBuffer\_GetAddr(OH\_AVBuffer \*buffer)](#oh_avbuffer_getaddr) | Obtains the virtual address of a data buffer. |
| [int32\_t OH\_AVBuffer\_GetCapacity(OH\_AVBuffer \*buffer)](#oh_avbuffer_getcapacity) | Obtains the capacity (in bytes) of a buffer. |
| [OH\_NativeBuffer \*OH\_AVBuffer\_GetNativeBuffer(OH\_AVBuffer \*buffer)](#oh_avbuffer_getnativebuffer) | Obtains the pointer to an OH\_NativeBuffer instance. You must call [OH\_NativeBuffer\_Unreference](../../../../../graphics/arkgraphics-2d/c-apis/header-files/native-buffer-h/document.md#oh_nativebuffer_unreference) to manually release the OH\_NativeBuffer instance returned. |

#### Function Description

#### \[h2\]OH\_AVBuffer\_Create()

OH\_AVBuffer \*OH\_AVBuffer\_Create(int32\_t capacity)

**Description**

Creates an OH\_AVBuffer instance. You must call [OH\_AVBuffer\_Destroy](#oh_avbuffer_destroy) to manually release the OH\_AVBuffer instance returned.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| int32\_t capacity | Size of the created memory, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \* | 
Pointer to the OH\_AVBuffer instance created. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **capacity** is less than or equal to **0**.

2\. An internal error occurs, or the system does not have resources.

 |

#### \[h2\]OH\_AVBuffer\_Destroy()

OH\_AVErrCode OH\_AVBuffer\_Destroy(OH\_AVBuffer \*buffer)

**Description**

Releases an OH\_AVBuffer instance. A buffer cannot be destroyed repeatedly.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to an OH\_AVBuffer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **buffer** is nullptr or fails format verification.

**AV\_ERR\_OPERATE\_NOT\_PERMIT**: The input buffer is not created by the user.

 |

#### \[h2\]OH\_AVBuffer\_GetBufferAttr()

OH\_AVErrCode OH\_AVBuffer\_GetBufferAttr(OH\_AVBuffer \*buffer, OH\_AVCodecBufferAttr \*attr)

**Description**

Obtains the basic attributes, including **pts**, **size**, **offset**, and **flags**, of a buffer.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to an OH\_AVBuffer instance. |
| [OH\_AVCodecBufferAttr](../../structs/oh-avcodecbufferattr/document.md) \*attr | Pointer to an OH\_AVCodecBufferAttr instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The possible causes are as follows:

1\. The value of **buffer** or **attr** is nullptr.

2\. The value of **buffer** fails parameter structure verification.

 |

#### \[h2\]OH\_AVBuffer\_SetBufferAttr()

OH\_AVErrCode OH\_AVBuffer\_SetBufferAttr(OH\_AVBuffer \*buffer, const OH\_AVCodecBufferAttr \*attr)

**Description**

Sets the basic attributes, including **pts**, **size**, **offset**, and **flags**, of a buffer.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to an OH\_AVBuffer instance. |
| [const OH\_AVCodecBufferAttr](../../structs/oh-avcodecbufferattr/document.md) \*attr | Pointer to an OH\_AVCodecBufferAttr instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The possible causes are as follows:

1\. The value of **buffer** or **attr** is nullptr.

2\. The value of **buffer** fails parameter structure verification.

3\. The memory size or offset of the buffer is invalid.

 |

#### \[h2\]OH\_AVBuffer\_GetParameter()

OH\_AVFormat \*OH\_AVBuffer\_GetParameter(OH\_AVBuffer \*buffer)

**Description**

Obtains parameters except basic attributes of a buffer. The information is carried in an OH\_AVFormat instance. You must call [OH\_AVFormat\_Destroy](../native-avformat-h/document.md#oh_avformat_destroy) to manually release the OH\_AVFormat instance returned.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to an OH\_AVBuffer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVFormat](../../structs/oh-avformat/document.md) \* | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The possible causes are as follows:

1\. The value of **buffer** is nullptr.

2\. The meta of the buffer is nullptr.

3\. The value of **buffer** fails parameter structure verification.

 |

#### \[h2\]OH\_AVBuffer\_SetParameter()

OH\_AVErrCode OH\_AVBuffer\_SetParameter(OH\_AVBuffer \*buffer, const OH\_AVFormat \*format)

**Description**

Sets parameters except basic attributes of a buffer. The information is carried in an OH\_AVFormat instance.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to an OH\_AVBuffer instance. |
| [const OH\_AVFormat](../../structs/oh-avformat/document.md) \*format | Pointer to an OH\_AVFormat instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The possible causes are as follows:

1\. The value of **buffer** or **format** is nullptr.

2\. The meta of the buffer is nullptr.

3\. The value of **buffer** fails parameter structure verification.

 |

#### \[h2\]OH\_AVBuffer\_GetAddr()

uint8\_t \*OH\_AVBuffer\_GetAddr(OH\_AVBuffer \*buffer)

**Description**

Obtains the virtual address of a data buffer.

The capability to obtain virtual addresses varies in scenarios, as described in the table below.

**Encoding**

| Mode | Data Filling Mode | Capability to Obtain Virtual Addresses |
| :-- | :-- | :-- |
| Surface | OnNeedInputBuffer input | Not supported |
| Surface | OnNewOutputBuffer output | Supported |
| Buffer | OnNeedInputBuffer input | Supported |
| Buffer | OnNewOutputBuffer output | Supported |

**Decoding**

| Mode | Data Filling Mode | Capability to Obtain Virtual Addresses |
| :-- | :-- | :-- |
| Surface | OnNeedInputBuffer input | Supported |
| Surface | OnNewOutputBuffer output | Not supported |
| Buffer | OnNeedInputBuffer input | Supported |
| Buffer | OnNewOutputBuffer output | Supported |

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to an OH\_AVBuffer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint8\_t \* | 
Virtual address. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **buffer** is a null pointer.

2\. The value of **OH\_AVBuffer** fails parameter structure verification.

3\. An internal error occurs.

 |

#### \[h2\]OH\_AVBuffer\_GetCapacity()

int32\_t OH\_AVBuffer\_GetCapacity(OH\_AVBuffer \*buffer)

**Description**

Obtains the capacity (in bytes) of a buffer.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to an OH\_AVBuffer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Capacity. If the operation fails, **\-1** is returned.

The possible causes of an operation failure are as follows:

1\. The value of **buffer** is a null pointer.

2\. The value of **OH\_AVBuffer** fails parameter structure verification.

3\. An internal error occurs.

 |

#### \[h2\]OH\_AVBuffer\_GetNativeBuffer()

OH\_NativeBuffer \*OH\_AVBuffer\_GetNativeBuffer(OH\_AVBuffer \*buffer)

**Description**

Obtains the pointer to an OH\_NativeBuffer instance. You must call [OH\_NativeBuffer\_Unreference](../../../../../graphics/arkgraphics-2d/c-apis/header-files/native-buffer-h/document.md#oh_nativebuffer_unreference) to manually release the OH\_NativeBuffer instance returned.

**System capability**: SystemCapability.Multimedia.Media.Core

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to an OH\_AVBuffer instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../../../../graphics/arkgraphics-2d/c-apis/modules/oh-nativebuffer/document.md) \* | 
Pointer to the OH\_NativeBuffer instance created. If the operation fails, NULL is returned.

The possible causes of an operation failure are as follows:

1\. The value of **buffer** is a null pointer.

2\. The value of **OH\_AVBuffer** fails parameter structure verification.

3\. An internal error occurs.

 |
