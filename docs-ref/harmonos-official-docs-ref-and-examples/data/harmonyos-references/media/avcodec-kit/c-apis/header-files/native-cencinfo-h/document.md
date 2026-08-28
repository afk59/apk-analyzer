# native\_cencinfo.h

#### Overview

The file declares the native APIs used to set decryption parameters.

**File to include**: <multimedia/player\_framework/native\_cencinfo.h>

**Library**: libnative\_media\_avcencinfo.so

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Related module**: [Multimedia\_Drm](../../modules/multimedia-drm/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DrmSubsample](../../structs/drmsubsample/document.md) | DrmSubsample | Describes the subsample type. |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) | OH\_AVBuffer | Describes the audio/video buffer. |
| [OH\_AVCencInfo](../../structs/oh-avcencinfo/document.md) | OH\_AVCencInfo | Describes the audio/video Common Encryption Scheme (CENC) information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DrmCencAlgorithm](#drmcencalgorithm) | DrmCencAlgorithm | Enumerates the DRM CENC algorithm types. |
| [DrmCencInfoMode](#drmcencinfomode) | DrmCencInfoMode | Enumerates the modes for setting the key ID, IV, and subsample in the CENC information. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| DRM\_KEY\_ID\_SIZE 16 | 
The length of the key ID is 16 bytes.

**Since**: 12

 |
| DRM\_KEY\_IV\_SIZE 16 | 

The length of the Initialization Vector (IV) is 16 bytes.

**Since**: 12

 |
| DRM\_KEY\_MAX\_SUB\_SAMPLE\_NUM 64 | 

The maximum number of subsamples is 64.

**Since**: 12

 |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVCencInfo \*OH\_AVCencInfo\_Create()](#oh_avcencinfo_create) | Creates an OH\_AVCencInfo instance for setting the CENC information. |
| [OH\_AVErrCode OH\_AVCencInfo\_Destroy(OH\_AVCencInfo \*cencInfo)](#oh_avcencinfo_destroy) | 
Destroys an OH\_AVCencInfo instance and clears internal resources.

An instance can be destroyed only once. Do not use the instance until it is created again. You are advised to set the instance pointer to nullptr once the instance is destroyed.

 |
| [OH\_AVErrCode OH\_AVCencInfo\_SetAlgorithm(OH\_AVCencInfo \*cencInfo, enum DrmCencAlgorithm algo)](#oh_avcencinfo_setalgorithm) | Sets an encryption algorithm of the CENC information. |
| [OH\_AVErrCode OH\_AVCencInfo\_SetKeyIdAndIv(OH\_AVCencInfo \*cencInfo, uint8\_t \*keyId, uint32\_t keyIdLen, uint8\_t \*iv, uint32\_t ivLen)](#oh_avcencinfo_setkeyidandiv) | Sets the key ID and IV in the CENC information. |
| [OH\_AVErrCode OH\_AVCencInfo\_SetSubsampleInfo(OH\_AVCencInfo \*cencInfo, uint32\_t encryptedBlockCount, uint32\_t skippedBlockCount, uint32\_t firstEncryptedOffset, uint32\_t subsampleCount, DrmSubsample \*subsamples)](#oh_avcencinfo_setsubsampleinfo) | Sets the subsample information in the CENC information. |
| [OH\_AVErrCode OH\_AVCencInfo\_SetMode(OH\_AVCencInfo \*cencInfo, enum DrmCencInfoMode mode)](#oh_avcencinfo_setmode) | Sets the CENC information mode. |
| [OH\_AVErrCode OH\_AVCencInfo\_SetAVBuffer(OH\_AVCencInfo \*cencInfo, OH\_AVBuffer \*buffer)](#oh_avcencinfo_setavbuffer) | Sets the CENC information to an AVBuffer. |

#### Enum Description

#### \[h2\]DrmCencAlgorithm

enum DrmCencAlgorithm

**Description**

Enumerates the DRM CENC algorithm types.

**Since**: 12

| Value | Description |
| :-- | :-- |
| DRM\_ALG\_CENC\_UNENCRYPTED = 0x0 | No encryption algorithm is used. |
| DRM\_ALG\_CENC\_AES\_CTR = 0x1 | AES CTR algorithm. |
| DRM\_ALG\_CENC\_AES\_WV = 0x2 | AES WV algorithm. |
| DRM\_ALG\_CENC\_AES\_CBC = 0x3 | AES CBC algorithm. |
| DRM\_ALG\_CENC\_SM4\_CBC = 0x4 | SM4 CBC algorithm. |
| DRM\_ALG\_CENC\_SM4\_CTR = 0x5 | SM4 CTR algorithm. |

#### \[h2\]DrmCencInfoMode

enum DrmCencInfoMode

**Description**

Enumerates the modes for setting the key ID, IV, and subsample in the CENC information.

**Since**: 12

| Value | Description |
| :-- | :-- |
| DRM\_CENC\_INFO\_KEY\_IV\_SUBSAMPLES\_SET = 0x0 | The key ID, IV, and subsample are set. |
| DRM\_CENC\_INFO\_KEY\_IV\_SUBSAMPLES\_NOT\_SET = 0x1 | The key ID, IV, and subsample are not set. |

#### Function Description

#### \[h2\]OH\_AVCencInfo\_Create()

OH\_AVCencInfo \*OH\_AVCencInfo\_Create()

**Description**

Creates an OH\_AVCencInfo instance for setting the CENC information.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVCencInfo](../../structs/oh-avcencinfo/document.md) \* | 
Pointer to the OH\_AVCencInfo instance created. If the operation fails, nullptr is returned.

The possible causes of an operation failure are as follows: The application address space is full, or the data in the object fails to be initialized.

 |

#### \[h2\]OH\_AVCencInfo\_Destroy()

OH\_AVErrCode OH\_AVCencInfo\_Destroy(OH\_AVCencInfo \*cencInfo)

**Description**

Destroys an OH\_AVCencInfo instance and clears internal resources.

An instance can be destroyed only once. Do not use the instance until it is created again. You are advised to set the instance pointer to nullptr once the instance is destroyed.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCencInfo](../../structs/oh-avcencinfo/document.md) \*cencInfo | Pointer to an OH\_AVCencInfo instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **cencInfo** is null.

 |

#### \[h2\]OH\_AVCencInfo\_SetAlgorithm()

OH\_AVErrCode OH\_AVCencInfo\_SetAlgorithm(OH\_AVCencInfo \*cencInfo, enum DrmCencAlgorithm algo)

**Description**

Sets an encryption algorithm of the CENC information.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCencInfo](../../structs/oh-avcencinfo/document.md) \*cencInfo | Pointer to an OH\_AVCencInfo instance. |
| [enum DrmCencAlgorithm](#drmcencalgorithm) algo | Encryption algorithm. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **cencInfo** is null.

 |

#### \[h2\]OH\_AVCencInfo\_SetKeyIdAndIv()

OH\_AVErrCode OH\_AVCencInfo\_SetKeyIdAndIv(OH\_AVCencInfo \*cencInfo, uint8\_t \*keyId, uint32\_t keyIdLen, uint8\_t \*iv, uint32\_t ivLen)

**Description**

Sets the key ID and IV in the CENC information.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCencInfo](../../structs/oh-avcencinfo/document.md) \*cencInfo | Pointer to an OH\_AVCencInfo instance. |
| uint8\_t \*keyId | Pointer to the key ID. |
| uint32\_t keyIdLen | Length of the key ID. |
| uint8\_t \*iv | Pointer to the IV. |
| uint32\_t ivLen | Length of the IV. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **cencInfo**, **keyId**, or **iv** is null, **keyIdLen** is not equal to **DRM\_KEY\_ID\_SIZE**, **ivLen** is not equal to **DRM\_KEY\_IV\_SIZE**, the key ID or IV fails to be copied.

 |

#### \[h2\]OH\_AVCencInfo\_SetSubsampleInfo()

OH\_AVErrCode OH\_AVCencInfo\_SetSubsampleInfo(OH\_AVCencInfo \*cencInfo, uint32\_t encryptedBlockCount, uint32\_t skippedBlockCount, uint32\_t firstEncryptedOffset, uint32\_t subsampleCount, DrmSubsample \*subsamples)

**Description**

Sets the subsample information in the CENC information.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCencInfo](../../structs/oh-avcencinfo/document.md) \*cencInfo | Pointer to an OH\_AVCencInfo instance. |
| uint32\_t encryptedBlockCount | Number of encrypted blocks. |
| uint32\_t skippedBlockCount | Number of non-encrypted blocks. |
| uint32\_t firstEncryptedOffset | Offset of the first encrypted payload. |
| uint32\_t subsampleCount | Number of subsamples. |
| [DrmSubsample](../../structs/drmsubsample/document.md) \*subsamples | Pointer to the subsamples. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **cencInfo** is null, **subsampleCount** is greater than **DRM\_KEY\_MAX\_SUB\_SAMPLE\_NUM**, or **subsamples** is null.

 |

#### \[h2\]OH\_AVCencInfo\_SetMode()

OH\_AVErrCode OH\_AVCencInfo\_SetMode(OH\_AVCencInfo \*cencInfo, enum DrmCencInfoMode mode)

**Description**

Sets the CENC information mode.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCencInfo](../../structs/oh-avcencinfo/document.md) \*cencInfo | Pointer to an OH\_AVCencInfo instance. |
| [enum DrmCencInfoMode](#drmcencinfomode) mode | CENC information mode, indicating whether the key ID, IV, and subsample are set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **cencInfo** is null.

 |

#### \[h2\]OH\_AVCencInfo\_SetAVBuffer()

OH\_AVErrCode OH\_AVCencInfo\_SetAVBuffer(OH\_AVCencInfo \*cencInfo, OH\_AVBuffer \*buffer)

**Description**

Sets the CENC information to an AVBuffer.

**System capability**: SystemCapability.Multimedia.Media.Spliter

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVCencInfo](../../structs/oh-avcencinfo/document.md) \*cencInfo | Pointer to an OH\_AVCencInfo instance. |
| [OH\_AVBuffer](../../structs/oh-avbuffer/document.md) \*buffer | Pointer to the frame buffer that carries data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The value of **cencInfo**, **buffer**, **buffer->buffer\_**, or **buffer->buffer\_->meta\_** is null.

 |
