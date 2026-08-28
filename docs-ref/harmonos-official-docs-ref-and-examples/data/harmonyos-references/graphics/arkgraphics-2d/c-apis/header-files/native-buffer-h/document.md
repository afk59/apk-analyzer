# native\_buffer.h

#### Overview

This file declares the functions for obtaining and using **NativeBuffer**.

**File to include**: <native\_buffer/native\_buffer.h>

**Library**: libnative\_buffer.so

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 9

**Related module**: [OH\_NativeBuffer](../../modules/oh-nativebuffer/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeBuffer\_Config](../../structs/oh-nativebuffer-config/document.md) | OH\_NativeBuffer\_Config | Describes the **OH\_NativeBuffer** property configuration, which is used when you apply for a new **OH\_NativeBuffer** instance or query the properties of an existing instance. |
| [OH\_NativeBuffer\_Plane](../../structs/oh-nativebuffer-plane/document.md) | OH\_NativeBuffer\_Plane | Describes the plane information of an image. |
| [OH\_NativeBuffer\_Planes](../../structs/oh-nativebuffer-planes/document.md) | OH\_NativeBuffer\_Planes | Describes the plane information of images in an **OH\_NativeBuffer** instance. |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) | OH\_NativeBuffer | Provides the declaration of an **OH\_NativeBuffer** struct. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NativeBuffer\_Usage](#oh_nativebuffer_usage) | OH\_NativeBuffer\_Usage | Defines an enum for the **OH\_NativeBuffer** usages. |
| [OH\_NativeBuffer\_ColorGamut](#oh_nativebuffer_colorgamut) | OH\_NativeBuffer\_ColorGamut | Defines an enum for the color gamuts of an **OH\_NativeBuffer** instance. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer\* OH\_NativeBuffer\_Alloc(const OH\_NativeBuffer\_Config\* config)](#oh_nativebuffer_alloc) | 
Creates an **OH\_NativeBuffer** instance based on an **OH\_NativeBuffer\_Config** struct. A new **OH\_NativeBuffer** instance is created each time this function is called.

This API must be used in pair with [OH\_NativeBuffer\_Unreference](#oh_nativebuffer_unreference). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_Reference(OH\_NativeBuffer \*buffer)](#oh_nativebuffer_reference) | 

Increases the reference count of an **OH\_NativeBuffer** instance by 1.

This API must be used in pair with [OH\_NativeBuffer\_Unreference](#oh_nativebuffer_unreference). Otherwise, memory leak occurs.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_Unreference(OH\_NativeBuffer \*buffer)](#oh_nativebuffer_unreference) | 

Decreases the reference count of an **OH\_NativeBuffer** instance by 1 and, when the reference count reaches 0, destroys the instance.

This function is not thread-safe.

 |
| [void OH\_NativeBuffer\_GetConfig(OH\_NativeBuffer buffer, OH\_NativeBuffer\_Config config)](#oh_nativebuffer_getconfig) | 

Obtains the properties of an **OH\_NativeBuffer** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_Map(OH\_NativeBuffer \*buffer, void \*\*virAddr)](#oh_nativebuffer_map) | 

Maps the ION memory allocated to an **OH\_NativeBuffer** instance to the process address space.

This API must be used in pair with [OH\_NativeBuffer\_Unmap](#oh_nativebuffer_unmap).

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_Unmap(OH\_NativeBuffer \*buffer)](#oh_nativebuffer_unmap) | 

Unmaps the ION memory allocated to an **OH\_NativeBuffer** instance from the process address space.

This function is not thread-safe.

 |
| [uint32\_t OH\_NativeBuffer\_GetSeqNum(OH\_NativeBuffer \*buffer)](#oh_nativebuffer_getseqnum) | 

Obtains the sequence number of an **OH\_NativeBuffer** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_SetColorSpace(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_ColorSpace colorSpace)](#oh_nativebuffer_setcolorspace) | 

Sets the color space for an **OH\_NativeBuffer** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_MapPlanes(OH\_NativeBuffer \*buffer, void \*\*virAddr, OH\_NativeBuffer\_Planes \*outPlanes)](#oh_nativebuffer_mapplanes) | 

Maps the multi-channel ION memory corresponding to an **OH\_NativeBuffer** instance to the process address space.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_FromNativeWindowBuffer(OHNativeWindowBuffer \*nativeWindowBuffer, OH\_NativeBuffer \*\*buffer)](#oh_nativebuffer_fromnativewindowbuffer) | 

Converts an **OHNativeWindowBuffer** instance to an **OH\_NativeBuffer** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_GetColorSpace(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_ColorSpace \*colorSpace)](#oh_nativebuffer_getcolorspace) | 

Obtains the color space of an **OH\_NativeBuffer** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_SetMetadataValue(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t size, uint8\_t \*metadata)](#oh_nativebuffer_setmetadatavalue) | 

Sets a metadata value for an **OH\_NativeBuffer** instance.

This function is not thread-safe.

 |
| [int32\_t OH\_NativeBuffer\_GetMetadataValue(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t \*size, uint8\_t \*\*metadata)](#oh_nativebuffer_getmetadatavalue) | 

Obtains the metadata value of an **OH\_NativeBuffer** instance.

This function is not thread-safe.

 |

#### Enum Description

#### \[h2\]OH\_NativeBuffer\_Usage

enum OH\_NativeBuffer\_Usage

**Description**

Defines an enum for the **OH\_NativeBuffer** usages.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 10

| Enum | Description |
| :-- | :-- |
| NATIVEBUFFER\_USAGE\_CPU\_READ = (1ULL << 0) | CPU readable. |
| NATIVEBUFFER\_USAGE\_CPU\_WRITE = (1ULL << 1) | CPU writable. |
| NATIVEBUFFER\_USAGE\_MEM\_DMA = (1ULL << 3) | Direct memory access to the buffer. |
| NATIVEBUFFER\_USAGE\_MEM\_MMZ\_CACHE = (1ULL << 5) | 
Buffer of the media memory area.

**Since**: 20

 |
| NATIVEBUFFER\_USAGE\_HW\_RENDER = (1ULL << 8) | 

GPU writable.

**Since**: 12

 |
| NATIVEBUFFER\_USAGE\_HW\_TEXTURE = (1ULL << 9) | 

GPU readable.

**Since**: 12

 |
| NATIVEBUFFER\_USAGE\_CPU\_READ\_OFTEN = (1ULL << 16) | 

Direct mapping of CPU.

**Since**: 12

 |
| NATIVEBUFFER\_USAGE\_ALIGNMENT\_512 = (1ULL << 18) | 

512-byte alignment.

**Since**: 12

 |

#### \[h2\]OH\_NativeBuffer\_ColorGamut

enum OH\_NativeBuffer\_ColorGamut

**Description**

Defines an enum for the color gamuts of an **OH\_NativeBuffer** instance.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

| Enum | Description |
| :-- | :-- |
| NATIVEBUFFER\_COLOR\_GAMUT\_NATIVE = 0 | Default gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_STANDARD\_BT601 = 1 | Standard BT.601 color gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_STANDARD\_BT709 = 2 | Standard BT.709 color gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_DCI\_P3 = 3 | DCI P3 color gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_SRGB = 4 | SRGB color gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_ADOBE\_RGB = 5 | Adobe RGB color gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_DISPLAY\_P3 = 6 | Display P3 color gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_BT2020 = 7 | BT.2020 color gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_BT2100\_PQ = 8 | BT.2100 PQ color gamut. |
| NATIVEBUFFER\_COLOR\_GAMUT\_BT2100\_HLG = 9 | BT.2100 HLG color gamut format |
| NATIVEBUFFER\_COLOR\_GAMUT\_DISPLAY\_BT2020 = 10 | Display BT.2020 color gamut. |

#### Function Description

#### \[h2\]OH\_NativeBuffer\_Alloc()

OH\_NativeBuffer\* OH\_NativeBuffer\_Alloc(const OH\_NativeBuffer\_Config\* config)

**Description**

Creates an **OH\_NativeBuffer** instance based on an **OH\_NativeBuffer\_Config** struct. A new **OH\_NativeBuffer** instance is created each time this function is called.

This API must be used in pair with [OH\_NativeBuffer\_Unreference](#oh_nativebuffer_unreference). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_NativeBuffer\_Config](../../structs/oh-nativebuffer-config/document.md)\* config | Pointer to an **OH\_NativeBuffer\_Config** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_NativeBuffer\* | Returns the pointer to the **OH\_NativeBuffer** instance created if the operation is successful; returns **NULL** otherwise. |

#### \[h2\]OH\_NativeBuffer\_Reference()

int32\_t OH\_NativeBuffer\_Reference(OH\_NativeBuffer \*buffer)

**Description**

Increases the reference count of an **OH\_NativeBuffer** instance by 1.

This API must be used in pair with [OH\_NativeBuffer\_Unreference](#oh_nativebuffer_unreference). Otherwise, memory leak occurs.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_Unreference()

int32\_t OH\_NativeBuffer\_Unreference(OH\_NativeBuffer \*buffer)

**Description**

Decreases the reference count of an **OH\_NativeBuffer** instance by 1 and, when the reference count reaches 0, destroys the instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_GetConfig()

void OH\_NativeBuffer\_GetConfig(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_Config\* config)

**Description**

Obtains the properties of an **OH\_NativeBuffer** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |
| [OH\_NativeBuffer\_Config](../../structs/oh-nativebuffer-config/document.md)\* config | Pointer to an **OH\_NativeBuffer\_Config** instance, which is used to receive the properties of **OH\_NativeBuffer**. |

#### \[h2\]OH\_NativeBuffer\_Map()

int32\_t OH\_NativeBuffer\_Map(OH\_NativeBuffer \*buffer, void \*\*virAddr)

**Description**

Maps the ION memory allocated to an **OH\_NativeBuffer** instance to the process address space.

This API must be used in pair with [OH\_NativeBuffer\_Unmap](#oh_nativebuffer_unmap).

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |
| void \*\*virAddr | Double pointer to the address of the virtual memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_Unmap()

int32\_t OH\_NativeBuffer\_Unmap(OH\_NativeBuffer \*buffer)

**Description**

Unmaps the ION memory allocated to an **OH\_NativeBuffer** instance from the process address space.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_GetSeqNum()

uint32\_t OH\_NativeBuffer\_GetSeqNum(OH\_NativeBuffer \*buffer)

**Description**

Obtains the sequence number of an **OH\_NativeBuffer** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| uint32\_t | Returns the unique sequence number of the **OH\_NativeBuffer** instance. |

#### \[h2\]OH\_NativeBuffer\_SetColorSpace()

int32\_t OH\_NativeBuffer\_SetColorSpace(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_ColorSpace colorSpace)

**Description**

Sets the color space for an **OH\_NativeBuffer** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |
| [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace) colorSpace | Pointer to the color space. For details about the available options, see [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_MapPlanes()

int32\_t OH\_NativeBuffer\_MapPlanes(OH\_NativeBuffer \*buffer, void \*\*virAddr, OH\_NativeBuffer\_Planes \*outPlanes)

**Description**

Maps the multi-channel ION memory corresponding to an **OH\_NativeBuffer** instance to the process address space.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |
| void \*\*virAddr | Double pointer to the address of the virtual memory. |
| [OH\_NativeBuffer\_Planes](../../structs/oh-nativebuffer-planes/document.md) \*outPlanes | Pointer to the plane information of all images. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_FromNativeWindowBuffer()

int32\_t OH\_NativeBuffer\_FromNativeWindowBuffer(OHNativeWindowBuffer \*nativeWindowBuffer, OH\_NativeBuffer \*\*buffer)

**Description**

Converts an **OHNativeWindowBuffer** instance to an **OH\_NativeBuffer** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) \*nativeWindowBuffer | Pointer to an [OHNativeWindowBuffer](../../structs/nativewindowbuffer/document.md) instance. |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*\*buffer | Pointer to an **OH\_NativeBuffer** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_GetColorSpace()

int32\_t OH\_NativeBuffer\_GetColorSpace(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_ColorSpace \*colorSpace)

**Description**

Obtains the color space of an **OH\_NativeBuffer** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |
| [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace) \*colorSpace | Pointer to the color space. For details about the available options, see [OH\_NativeBuffer\_ColorSpace](../buffer-common-h/document.md#oh_nativebuffer_colorspace). |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_SetMetadataValue()

int32\_t OH\_NativeBuffer\_SetMetadataValue(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t size, uint8\_t \*metadata)

**Description**

Sets a metadata value for an **OH\_NativeBuffer** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |
| [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey) metadataKey | Metadata type of [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md). For details about the available options, see [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey). |
| int32\_t size | Size of the **uint8\_t** vector. For details about the value range, see [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey). |
| uint8\_t \*metadata | Pointer to the **uint8\_t** vector. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |

#### \[h2\]OH\_NativeBuffer\_GetMetadataValue()

int32\_t OH\_NativeBuffer\_GetMetadataValue(OH\_NativeBuffer \*buffer, OH\_NativeBuffer\_MetadataKey metadataKey,int32\_t \*size, uint8\_t \*\*metadata)

**Description**

Obtains the metadata value of an **OH\_NativeBuffer** instance.

This function is not thread-safe.

**System capability**: SystemCapability.Graphic.Graphic2D.NativeBuffer

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) \*buffer | Pointer to an **OH\_NativeBuffer** instance. |
| [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey) metadataKey | Metadata type of [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md). For details about the available options, see [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey). |
| int32\_t \*size | Size of the **uint8\_t** vector. For details about the value range, see [OH\_NativeBuffer\_MetadataKey](../buffer-common-h/document.md#oh_nativebuffer_metadatakey). |
| uint8\_t \*\*metadata | Double pointer to the **uint8\_t** vector. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | Returns **0** if the operation is successful; returns an error code defined in [OHNativeErrorCode](../graphic-error-code-h/document.md#ohnativeerrorcode) otherwise. |
