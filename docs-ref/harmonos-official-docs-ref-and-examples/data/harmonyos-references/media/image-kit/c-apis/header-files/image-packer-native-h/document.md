# image\_packer\_native.h

#### Overview

The file declares the APIs for image encoding.

**File to include**: <multimedia/image\_framework/image/image\_packer\_native.h>

**Library**: libimage\_packer.so

**System capability**: SystemCapability.Multimedia.Image.ImagePacker

**Since**: 12

**Related module**: [Image\_NativeModule](../../modules/image-nativemodule/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) | OH\_ImagePackerNative | Describes the image packer, which is used to perform operations related to an image packer. |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) | OH\_PackingOptions | OH\_PackingOptions is an image encoding option struct encapsulated at the native layer. It cannot be manipulated directly; instead, functions shall be called to create and release the struct, and operate on its specific fields. |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) | OH\_PackingOptionsForSequence | OH\_PackingOptionsForSequence is an image sequence encoding option struct encapsulated at the native layer. It cannot be manipulated directly; instead, functions shall be called to create and release the struct, and operate on its specific fields. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [IMAGE\_PACKER\_DYNAMIC\_RANGE](#image_packer_dynamic_range) | IMAGE\_PACKER\_DYNAMIC\_RANGE | Enumerates the dynamic range for encoding. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [Image\_ErrorCode OH\_PackingOptions\_Create(OH\_PackingOptions \*\*options)](#oh_packingoptions_create) | Creates the pointer to an OH\_PackingOptions struct. |
| [Image\_ErrorCode OH\_PackingOptions\_GetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format)](#oh_packingoptions_getmimetype) | Obtains the MIME type. The **value.data** obtained through this API lacks the string terminator **\\0**. Please use it with caution. |
| [Image\_ErrorCode OH\_PackingOptions\_GetMimeTypeWithNull(OH\_PackingOptions \*options, Image\_MimeType \*format)](#oh_packingoptions_getmimetypewithnull) | Obtains the MIME type in the packing options. The output of **format.data** ends with the string terminator **\\0**. |
| [Image\_ErrorCode OH\_PackingOptions\_SetMimeType(OH\_PackingOptions \*options, Image\_MimeType \*format)](#oh_packingoptions_setmimetype) | Sets the MIME type. |
| [Image\_ErrorCode OH\_PackingOptions\_GetQuality(OH\_PackingOptions \*options, uint32\_t \*quality)](#oh_packingoptions_getquality) | Obtains the encoding quality. |
| [Image\_ErrorCode OH\_PackingOptions\_SetQuality(OH\_PackingOptions \*options, uint32\_t quality)](#oh_packingoptions_setquality) | Sets the encoding quality. |
| [Image\_ErrorCode OH\_PackingOptions\_GetNeedsPackProperties(OH\_PackingOptions \*options, bool \*needsPackProperties)](#oh_packingoptions_getneedspackproperties) | Obtains the **needsPackProperties** parameter in the OH\_PackingOptions struct. |
| [Image\_ErrorCode OH\_PackingOptions\_SetNeedsPackProperties(OH\_PackingOptions \*options, bool needsPackProperties)](#oh_packingoptions_setneedspackproperties) | Sets the **needsPackProperties** parameter in the OH\_PackingOptions struct. |
| [Image\_ErrorCode OH\_PackingOptions\_GetDesiredDynamicRange(OH\_PackingOptions options, int32\_t desiredDynamicRange)](#oh_packingoptions_getdesireddynamicrange) | Obtains the desired dynamic range during encoding. |
| [Image\_ErrorCode OH\_PackingOptions\_SetDesiredDynamicRange(OH\_PackingOptions \*options, int32\_t desiredDynamicRange)](#oh_packingoptions_setdesireddynamicrange) | Sets the desired dynamic range during encoding. |
| [Image\_ErrorCode OH\_PackingOptions\_Release(OH\_PackingOptions \*options)](#oh_packingoptions_release) | Releases the pointer to an OH\_PackingOptions struct. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_Create(OH\_PackingOptionsForSequence \*\*options)](#oh_packingoptionsforsequence_create) | Creates the pointer to an OH\_PackingOptionsForSequence struct. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetFrameCount(OH\_PackingOptionsForSequence \*options, uint32\_t frameCount)](#oh_packingoptionsforsequence_setframecount) | Sets the number of frames for image sequence encoding. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_GetFrameCount(OH\_PackingOptionsForSequence \*options, uint32\_t \*frameCount)](#oh_packingoptionsforsequence_getframecount) | Obtains the number of frames for image sequence encoding. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetDelayTimeList(OH\_PackingOptionsForSequence \*options, int32\_t \*delayTimeList, size\_t delayTimeListLength)](#oh_packingoptionsforsequence_setdelaytimelist) | Sets the delay time array for image sequence encoding. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_GetDelayTimeList(OH\_PackingOptionsForSequence \*options, int32\_t \*delayTimeList, size\_t delayTimeListLength)](#oh_packingoptionsforsequence_getdelaytimelist) | Obtains the delay time array for image sequence encoding. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetDisposalTypes(OH\_PackingOptionsForSequence \*options, uint32\_t \*disposalTypes, size\_t disposalTypesLength)](#oh_packingoptionsforsequence_setdisposaltypes) | Sets the disposal type array for image sequence encoding. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_GetDisposalTypes(OH\_PackingOptionsForSequence \*options, uint32\_t \*disposalTypes, size\_t disposalTypesLength)](#oh_packingoptionsforsequence_getdisposaltypes) | Obtains the disposal type array for image sequence encoding. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_SetLoopCount(OH\_PackingOptionsForSequence \*options, uint32\_t loopCount)](#oh_packingoptionsforsequence_setloopcount) | Sets the number of loops for image sequence encoding. The value range is \[0, 65535\], where **0** means an infinite loop. If this field is not carried, loop playback is not performed. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_GetLoopCount(OH\_PackingOptionsForSequence \*options, uint32\_t \*loopCount)](#oh_packingoptionsforsequence_getloopcount) | Obtains the number of loops for image sequence encoding. |
| [Image\_ErrorCode OH\_PackingOptionsForSequence\_Release(OH\_PackingOptionsForSequence \*options)](#oh_packingoptionsforsequence_release) | Releases the pointer to an OH\_PackingOptionsForSequence struct. |
| [Image\_ErrorCode OH\_ImagePackerNative\_Create(OH\_ImagePackerNative \*\*imagePacker)](#oh_imagepackernative_create) | Creates the pointer to an OH\_ImagePackerNative struct. |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromImageSource(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_ImageSourceNative \*imageSource, uint8\_t \*outData, size\_t \*size)](#oh_imagepackernative_packtodatafromimagesource) | Encodes an image source into data in a given format. |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPixelmap(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_PixelmapNative \*pixelmap, uint8\_t \*outData, size\_t \*size)](#oh_imagepackernative_packtodatafrompixelmap) | Encodes a PixelMap into data in a given format. |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPicture(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_PictureNative \*picture, uint8\_t \*outData, size\_t \*size)](#oh_imagepackernative_packtodatafrompicture) | Encodes a picture into data in a given format. |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPixelmapSequence(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptionsForSequence \*options, OH\_PixelmapNative \*\*pixelmapSequence,size\_t sequenceLength, uint8\_t \*outData, size\_t \*outDataSize)](#oh_imagepackernative_packtodatafrompixelmapsequence) | Encodes a PixelMap sequence into data. |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromImageSource(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_ImageSourceNative \*imageSource, int32\_t fd)](#oh_imagepackernative_packtofilefromimagesource) | Encodes an image source into a file. |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPixelmap(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_PixelmapNative \*pixelmap, int32\_t fd)](#oh_imagepackernative_packtofilefrompixelmap) | Encodes a PixelMap into a file. |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPicture(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptions \*options, OH\_PictureNative \*picture, int32\_t fd)](#oh_imagepackernative_packtofilefrompicture) | Encodes a picture into a file. |
| [Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPixelmapSequence(OH\_ImagePackerNative \*imagePacker, OH\_PackingOptionsForSequence \*options, OH\_PixelmapNative \*\*pixelmapSequence, size\_t sequenceLength, int32\_t fd)](#oh_imagepackernative_packtofilefrompixelmapsequence) | Encodes a PixelMap sequence into a file. |
| [Image\_ErrorCode OH\_ImagePackerNative\_GetSupportedFormats(Image\_MimeType \*\*supportedFormats, size\_t \*length)](#oh_imagepackernative_getsupportedformats) | Obtains the supported image formats that can be encoded. |
| [Image\_ErrorCode OH\_ImagePackerNative\_Release(OH\_ImagePackerNative \*imagePacker)](#oh_imagepackernative_release) | Releases the pointer to an OH\_ImagePackerNative struct. |

#### Enum Description

#### \[h2\]IMAGE\_PACKER\_DYNAMIC\_RANGE

enum IMAGE\_PACKER\_DYNAMIC\_RANGE

**Description**

Enumerates the dynamic range for encoding.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_PACKER\_DYNAMIC\_RANGE\_AUTO = 0 | Adaptive processing. |
| IMAGE\_PACKER\_DYNAMIC\_RANGE\_SDR = 1 | Standard dynamic range (SDR). |

#### Function Description

#### \[h2\]OH\_PackingOptions\_Create()

Image\_ErrorCode OH\_PackingOptions\_Create(OH\_PackingOptions \*\*options)

**Description**

Creates the pointer to an OH\_PackingOptions struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*\*options | Double pointer to the OH\_PackingOptions struct created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_GetMimeType()

Image\_ErrorCode OH\_PackingOptions\_GetMimeType(OH\_PackingOptions \*options,Image\_MimeType \*format)

**Description**

Obtains the MIME type. The **value.data** obtained through this API lacks the string terminator **\\0**. Please use it with caution.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [Image\_MimeType](../../structs/image-string/document.md) \*format | Pointer to the image format. You can pass in a null pointer with the size set to zero. In this case, the system will allocate memory, but you must release the memory after use. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_GetMimeTypeWithNull()

Image\_ErrorCode OH\_PackingOptions\_GetMimeTypeWithNull(OH\_PackingOptions \*options,Image\_MimeType \*format)

**Description**

Obtains the MIME type in the packing options. The output of **format.data** ends with the string terminator **\\0**.

**Since**: 19

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [Image\_MimeType](../../structs/image-string/document.md) \*format | Pointer to the MIME type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_PACKER\_INVALID\_PARAMETER**: The **options** or **format** parameter is a null pointer.

 |

#### \[h2\]OH\_PackingOptions\_SetMimeType()

Image\_ErrorCode OH\_PackingOptions\_SetMimeType(OH\_PackingOptions \*options,Image\_MimeType \*format)

**Description**

Sets the MIME type.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [Image\_MimeType](../../structs/image-string/document.md) \*format | Pointer to the image format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_GetQuality()

Image\_ErrorCode OH\_PackingOptions\_GetQuality(OH\_PackingOptions \*options,uint32\_t \*quality)

**Description**

Obtains the encoding quality.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| uint32\_t \*quality | Pointer to the encoding quality. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_SetQuality()

Image\_ErrorCode OH\_PackingOptions\_SetQuality(OH\_PackingOptions \*options,uint32\_t quality)

**Description**

Sets the encoding quality.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| uint32\_t quality | Encoding quality. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_GetNeedsPackProperties()

 Image\_ErrorCode OH\_PackingOptions\_GetNeedsPackProperties(OH\_PackingOptions \*options,bool \*needsPackProperties)

**Description**

Obtains the **needsPackProperties** parameter in the OH\_PackingOptions struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| bool \*needsPackProperties | Whether to encode image property information (for example, Exif). The values include **true** (yes) and **false** (no). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_SetNeedsPackProperties()

Image\_ErrorCode OH\_PackingOptions\_SetNeedsPackProperties(OH\_PackingOptions \*options,bool needsPackProperties)

**Description**

Sets the **needsPackProperties** parameter in the OH\_PackingOptions struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| bool needsPackProperties | Whether to encode image property information (for example, Exif). The values include **true** (yes) and **false** (no). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_GetDesiredDynamicRange()

Image\_ErrorCode OH\_PackingOptions\_GetDesiredDynamicRange(OH\_PackingOptions \*options, int32\_t\* desiredDynamicRange)

**Description**

Obtains the desired dynamic range during encoding.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| int32\_t\* desiredDynamicRange | Pointer to the desired dynamic range. For details about the available options, please refer to \[IMAGE\_PACKER\_DYNAMIC\_RANGE\]#image\_packer\_dynamic\_range). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_SetDesiredDynamicRange()

Image\_ErrorCode OH\_PackingOptions\_SetDesiredDynamicRange(OH\_PackingOptions \*options, int32\_t desiredDynamicRange)

**Description**

Sets the desired dynamic range during encoding.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| int32\_t desiredDynamicRange | Desired dynamic range. For details about the available options, see \[IMAGE\_PACKER\_DYNAMIC\_RANGE\]#image\_packer\_dynamic\_range). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptions\_Release()

Image\_ErrorCode OH\_PackingOptions\_Release(OH\_PackingOptions \*options)

**Description**

Releases the pointer to an OH\_PackingOptions struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_Create()

Image\_ErrorCode OH\_PackingOptionsForSequence\_Create(OH\_PackingOptionsForSequence \*\*options)

**Description**

Creates the pointer to an OH\_PackingOptionsForSequence struct.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*\*options | Double pointer to the OH\_PackingOptionsForSequence struct created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_SetFrameCount()

Image\_ErrorCode OH\_PackingOptionsForSequence\_SetFrameCount(OH\_PackingOptionsForSequence \*options,uint32\_t frameCount)

**Description**

Sets the number of frames for image sequence encoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to an OH\_PackingOptionsForSequence struct. |
| uint32\_t frameCount | Number of frames. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_GetFrameCount()

Image\_ErrorCode OH\_PackingOptionsForSequence\_GetFrameCount(OH\_PackingOptionsForSequence \*options,uint32\_t \*frameCount)

**Description**

Obtains the number of frames for image sequence encoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to an OH\_PackingOptionsForSequence struct. |
| uint32\_t \*frameCount | Pointer to the number of frames. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_SetDelayTimeList()

Image\_ErrorCode OH\_PackingOptionsForSequence\_SetDelayTimeList(OH\_PackingOptionsForSequence \*options,int32\_t \*delayTimeList, size\_t delayTimeListLength)

**Description**

Sets the delay time array for image sequence encoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to an OH\_PackingOptionsForSequence struct. |
| int32\_t \*delayTimeList | Pointer to the delay time array. |
| size\_t delayTimeListLength | Length of the delay time array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_GetDelayTimeList()

Image\_ErrorCode OH\_PackingOptionsForSequence\_GetDelayTimeList(OH\_PackingOptionsForSequence \*options,int32\_t \*delayTimeList, size\_t delayTimeListLength)

**Description**

Obtains the delay time array for image sequence encoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to OH\_PackingOptionsForSequence. |
| int32\_t \*delayTimeList | Pointer to the delay time array. |
| size\_t delayTimeListLength | Length of the delay time array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_SetDisposalTypes()

Image\_ErrorCode OH\_PackingOptionsForSequence\_SetDisposalTypes(OH\_PackingOptionsForSequence \*options,uint32\_t \*disposalTypes, size\_t disposalTypesLength)

**Description**

Sets the disposal type array for image sequence encoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to OH\_PackingOptionsForSequence. |
| uint32\_t \*disposalTypes | 
Pointer to an array that defines how each image frame transitions. If the array length is less than **frameCount**, the last value in the array will be used for the remaining frames. The values can be:

**0**: No operation is required.

**1**: Keeps the image unchanged.

**2**: Restores the background color.

**3**: Restores to the previous state.

 |
| size\_t disposalTypesLength | Length of the disposal type array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_GetDisposalTypes()

Image\_ErrorCode OH\_PackingOptionsForSequence\_GetDisposalTypes(OH\_PackingOptionsForSequence \*options,uint32\_t \*disposalTypes, size\_t disposalTypesLength)

**Description**

Obtains the disposal type array for image sequence encoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to OH\_PackingOptionsForSequence. |
| uint32\_t \*disposalTypes | Pointer to the disposal type array. |
| size\_t disposalTypesLength | Length of the disposal type array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_SetLoopCount()

Image\_ErrorCode OH\_PackingOptionsForSequence\_SetLoopCount(OH\_PackingOptionsForSequence \*options, uint32\_t loopCount)

**Description**

Sets the number of loops for image sequence encoding. The value range is \[0, 65535\], where **0** means an infinite loop. If this field is not carried, loop playback is not performed.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to OH\_PackingOptionsForSequence. |
| uint32\_t loopCount | Number of loops. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_GetLoopCount()

Image\_ErrorCode OH\_PackingOptionsForSequence\_GetLoopCount(OH\_PackingOptionsForSequence \*options, uint32\_t \*loopCount)

**Description**

Obtains the number of loops for image sequence encoding.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to OH\_PackingOptionsForSequence. |
| uint32\_t \*loopCount | Pointer to the number of loops. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_PackingOptionsForSequence\_Release()

Image\_ErrorCode OH\_PackingOptionsForSequence\_Release(OH\_PackingOptionsForSequence \*options)

**Description**

Releases the pointer to an OH\_PackingOptionsForSequence struct.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to OH\_PackingOptionsForSequence. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImagePackerNative\_Create()

Image\_ErrorCode OH\_ImagePackerNative\_Create(OH\_ImagePackerNative \*\*imagePacker)

**Description**

Creates the pointer to an OH\_ImagePackerNative struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*\*imagePacker | Double pointer to OH\_ImagePackerNative. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |

#### \[h2\]OH\_ImagePackerNative\_PackToDataFromImageSource()

Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromImageSource(OH\_ImagePackerNative \*imagePacker,OH\_PackingOptions \*options, OH\_ImageSourceNative \*imageSource, uint8\_t \*outData, size\_t \*size)

**Description**

Encodes an image source into data in a given format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [OH\_ImageSourceNative](../../structs/oh-imagesourcenative/document.md) \*imageSource | Pointer to the image source to encode. |
| uint8\_t \*outData | Pointer to the buffer used to store the output data. |
| size\_t \*size | Pointer to the size of the buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

**IMAGE\_TOO\_LARGE**: The data or image is too large.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_ImagePackerNative\_PackToDataFromPixelmap()

Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPixelmap(OH\_ImagePackerNative \*imagePacker,OH\_PackingOptions \*options, OH\_PixelmapNative \*pixelmap, uint8\_t \*outData, size\_t \*size)

**Description**

Encodes a PixelMap into data in a given format.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the PixelMap to encode. |
| uint8\_t \*outData | Pointer to the buffer used to store the output data. |
| size\_t \*size | Pointer to the size of the buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_ALLOC\_FAILED**: Memory allocation fails.

**IMAGE\_TOO\_LARGE**: The data or image is too large.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_ImagePackerNative\_PackToDataFromPicture()

Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPicture(OH\_ImagePackerNative \*imagePacker,OH\_PackingOptions \*options, OH\_PictureNative \*picture, uint8\_t \*outData, size\_t \*size)

**Description**

Encodes a picture into data in a given format.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to the picture to encode. |
| uint8\_t \*outData | Pointer to the buffer used to store the output data. |
| size\_t \*size | Pointer to the size of the buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

 |

#### \[h2\]OH\_ImagePackerNative\_PackToDataFromPixelmapSequence()

Image\_ErrorCode OH\_ImagePackerNative\_PackToDataFromPixelmapSequence(OH\_ImagePackerNative \*imagePacker,OH\_PackingOptionsForSequence \*options, OH\_PixelmapNative \*\*pixelmapSequence,size\_t sequenceLength, uint8\_t \*outData, size\_t \*outDataSize)

**Description**

Encodes a PixelMap sequence into data.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to an [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) struct. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmapSequence | Double pointer to the PixelMap sequence to encode. |
| size\_t sequenceLength | Length of the PixelMap sequence. |
| uint8\_t \*outData | Pointer to the buffer used to store the output data. |
| size\_t \*outDataSize | Pointer to the size of the buffer. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

 |

#### \[h2\]OH\_ImagePackerNative\_PackToFileFromImageSource()

Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromImageSource(OH\_ImagePackerNative \*imagePacker,OH\_PackingOptions \*options, OH\_ImageSourceNative \*imageSource, int32\_t fd)

**Description**

Encodes an image source into a file.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [OH\_ImageSourceNative](../../structs/oh-imagesourcenative/document.md) \*imageSource | Pointer to the image source to encode. |
| int32\_t fd | File descriptor, which is writable. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_ImagePackerNative\_PackToFileFromPixelmap()

Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPixelmap(OH\_ImagePackerNative \*imagePacker,OH\_PackingOptions \*options, OH\_PixelmapNative \*pixelmap, int32\_t fd)

**Description**

Encodes a PixelMap into a file.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*pixelmap | Pointer to the PixelMap to encode. |
| int32\_t fd | File descriptor, which is writable. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_ImagePackerNative\_PackToFileFromPicture()

Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPicture(OH\_ImagePackerNative \*imagePacker,OH\_PackingOptions \*options, OH\_PictureNative \*picture, int32\_t fd)

**Description**

Encodes a picture into a file.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |
| [OH\_PackingOptions](../../structs/oh-packingoptions/document.md) \*options | Pointer to an OH\_PackingOptions struct. |
| [OH\_PictureNative](../../structs/oh-picturenative/document.md) \*picture | Pointer to the picture to encode. |
| int32\_t fd | File descriptor, which is writable. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

**IMAGE\_UNKNOWN\_ERROR**: An unknown error occurs.

 |

#### \[h2\]OH\_ImagePackerNative\_PackToFileFromPixelmapSequence()

Image\_ErrorCode OH\_ImagePackerNative\_PackToFileFromPixelmapSequence(OH\_ImagePackerNative \*imagePacker,OH\_PackingOptionsForSequence \*options, OH\_PixelmapNative \*\*pixelmapSequence, size\_t sequenceLength, int32\_t fd)

**Description**

Encodes a PixelMap sequence into a file.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |
| [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) \*options | Pointer to an [OH\_PackingOptionsForSequence](../../structs/oh-packingoptionsforsequence/document.md) struct. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) \*\*pixelmapSequence | Double pointer to the PixelMap sequence to encode. |
| size\_t sequenceLength | Length of the PixelMap sequence. |
| int32\_t fd | File descriptor, which is writable. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

**IMAGE\_DECODE\_FAILED**: Decoding fails.

 |

#### \[h2\]OH\_ImagePackerNative\_GetSupportedFormats()

Image\_ErrorCode OH\_ImagePackerNative\_GetSupportedFormats(Image\_MimeType \*\*supportedFormats, size\_t \*length)

**Description**

Obtains the supported image formats that can be encoded.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [Image\_MimeType](../../structs/image-string/document.md) \*\*supportedFormats | Double pointer to the supported image formats. |
| size\_t \*length | Pointer to the size of the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_PACKER\_INVALID\_PARAMETER**: The **supportedFormats** or **length** parameter is a null pointer.

 |

#### \[h2\]OH\_ImagePackerNative\_Release()

Image\_ErrorCode OH\_ImagePackerNative\_Release(OH\_ImagePackerNative \*imagePacker)

**Description**

Releases the pointer to an OH\_ImagePackerNative struct.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImagePackerNative](../../structs/oh-imagepackernative/document.md) \*imagePacker | Pointer to OH\_ImagePackerNative. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Image\_ErrorCode](../image-common-h/document.md#image_errorcode) | 
**IMAGE\_SUCCESS**: The operation is successful.

**IMAGE\_BAD\_PARAMETER**: A parameter is incorrect.

 |
