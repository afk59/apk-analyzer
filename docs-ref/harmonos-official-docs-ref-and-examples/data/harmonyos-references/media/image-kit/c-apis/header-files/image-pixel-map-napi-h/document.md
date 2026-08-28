# image\_pixel\_map\_napi.h

#### Overview

The file declares the APIs used to lock, access, and unlock a PixelMap.

**Library**: libpixelmap\_ndk.z.so

**System capability**: SystemCapability.Multimedia.Image.Core

**File to include**: <multimedia/image\_framework/image\_pixel\_map\_napi.h>

**Since**: 8

**Related module**: [Image](../../modules/image/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OhosPixelMapInfo](../../structs/ohospixelmapinfo/document.md) | \- | Describes the information about a PixelMap. |

#### \[h2\]Enums

| Name | Description |
| :-- | :-- |
| [Error Codes Returned by Functions](#error-codes-returned-by-functions) | Enumerates the error codes returned by the functions. |
| [Pixel Formats](#pixel-formats) | Enumerates the pixel formats. |
| [anonymous enum](#pixelmap-scale-modes) | Enumerates the PixelMap scale modes. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int32\_t OH\_GetImageInfo(napi\_env env, napi\_value value, OhosPixelMapInfo \*info)](#oh_getimageinfo) | Obtains the information about a PixelMap object and stores the information to the [OhosPixelMapInfo](../../structs/ohospixelmapinfo/document.md) struct. |
| [int32\_t OH\_AccessPixels(napi\_env env, napi\_value value, void\*\* addrPtr)](#oh_accesspixels) | 
Obtains the memory address of a PixelMap object and locks the memory.

**\*addrPtr** is the memory address obtained. After finishing the access, you must use [OH\_UnAccessPixels](#oh_unaccesspixels) to unlock the memory. Then the memory cannot be accessed or operated.

 |
| [int32\_t OH\_UnAccessPixels(napi\_env env, napi\_value value)](#oh_unaccesspixels) | Unlocks the memory of a PixelMap object. This function is used with [OH\_AccessPixels](#oh_accesspixels) in pairs. |

#### Enum Description

#### \[h2\]Error Codes Returned by Functions

enum anonymous enum

**Description**

Enumerates the error codes returned by the functions.

**Since**: 8

**Deprecated from**: 10

| Enum Item | Description |
| :-- | :-- |
| OHOS\_IMAGE\_RESULT\_SUCCESS = 0 | Operation success. |
| OHOS\_IMAGE\_RESULT\_BAD\_PARAMETER = -1 | Invalid value. |

#### \[h2\]Pixel Formats

enum anonymous enum

**Description**

Enumerates the pixel formats.

**Since**: 8

**Deprecated from**: 10

| Enum Item | Description |
| :-- | :-- |
| OHOS\_PIXEL\_MAP\_FORMAT\_NONE = 0 | Unknown format. |
| OHOS\_PIXEL\_MAP\_FORMAT\_RGBA\_8888 = 3 | RGBA\_8888 format. |
| OHOS\_PIXEL\_MAP\_FORMAT\_RGB\_565 = 2 | RGB\_565 format. |

#### \[h2\]PixelMap Scale Modes

enum anonymous enum

**Description**

Enumerates the PixelMap scale modes.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OHOS\_PIXEL\_MAP\_SCALE\_MODE\_FIT\_TARGET\_SIZE = 0 | Adapting to the target image size. |
| OHOS\_PIXEL\_MAP\_SCALE\_MODE\_CENTER\_CROP = 1 | Cropping the center portion of an image to the target size. |

#### Function Description

#### \[h2\]OH\_GetImageInfo()

int32\_t OH\_GetImageInfo(napi\_env env, napi\_value value, OhosPixelMapInfo \*info)

**Description**

Obtains the information about a PixelMap object and stores the information to the [OhosPixelMapInfo](../../structs/ohospixelmapinfo/document.md) struct.

**Since**: 8

**Deprecated from**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| napi\_value value | PixelMap object at the application layer. |
| [OhosPixelMapInfo](../../structs/ohospixelmapinfo/document.md) \*info | Pointer to the object that stores the information obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following [error codes](#error-codes-returned-by-functions):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**OHOS\_IMAGE\_RESULT\_BAD\_PARAMETER**: The operation fails.

 |

#### \[h2\]OH\_AccessPixels()

int32\_t OH\_AccessPixels(napi\_env env, napi\_value value, void\*\* addrPtr)

**Description**

Obtains the memory address of a PixelMap object and locks the memory.

**\*addrPtr** is the memory address obtained. After finishing the access, you must use [OH\_UnAccessPixels](#oh_unaccesspixels) to unlock the memory. Then the memory cannot be accessed or operated.

**Since**: 8

**Deprecated from**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| napi\_value value | PixelMap object at the application layer. |
| void\*\* addrPtr | Double pointer to the memory address. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following [error codes](#error-codes-returned-by-functions):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**OHOS\_IMAGE\_RESULT\_BAD\_PARAMETER**: The operation fails.

 |

#### \[h2\]OH\_UnAccessPixels()

int32\_t OH\_UnAccessPixels(napi\_env env, napi\_value value)

**Description**

Unlocks the memory of a PixelMap object. This function is used with [OH\_AccessPixels](#oh_accesspixels) in pairs.

**Since**: 8

**Deprecated from**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| napi\_env env | Pointer to the NAPI environment. |
| napi\_value value | PixelMap object at the application layer. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
One of the following [error codes](#error-codes-returned-by-functions):

**OHOS\_IMAGE\_RESULT\_SUCCESS**: The operation is successful.

**OHOS\_IMAGE\_RESULT\_BAD\_PARAMETER**: The operation fails.

 |
