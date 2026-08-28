# ddk\_api.h

#### Overview

Declares the BASE DDK APIs used by the USB host to access USB devices.

**File to include**: <ddk/ddk\_api.h>

**Library**: libddk\_base.z.so

**System capability**: SystemCapability.Driver.DDK.Extension

**Since**: 12

**Related module**: [Ddk](../../modules/baseddk/document.md)

#### Summary

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [DDK\_RetCode OH\_DDK\_CreateAshmem(const uint8\_t \*name, uint32\_t size, DDK\_Ashmem \*\*ashmem)](#oh_ddk_createashmem) | Creates an **Ashmem** object. To prevent resource leakage, call **OH\_DDK\_DestroyAshmem** to destroy the **Ashmem** object when it is no longer needed. |
| [DDK\_RetCode OH\_DDK\_MapAshmem(DDK\_Ashmem \*ashmem, const uint8\_t ashmemMapType)](#oh_ddk_mapashmem) | Maps the created **Ashmem** object to the user space. Call **OH\_DDK\_UnmapAshmem** to unmap the **Ashmem** object when it is no longer needed. |
| [DDK\_RetCode OH\_DDK\_UnmapAshmem(DDK\_Ashmem \*ashmem)](#oh_ddk_unmapashmem) | Unmaps an **Ashmem** object. |
| [DDK\_RetCode OH\_DDK\_DestroyAshmem(DDK\_Ashmem \*ashmem)](#oh_ddk_destroyashmem) | Destroys an **Ashmem** object. |

#### Function Description

#### \[h2\]OH\_DDK\_CreateAshmem()

DDK\_RetCode OH\_DDK\_CreateAshmem(const uint8\_t \*name, uint32\_t size, DDK\_Ashmem \*\*ashmem)

**Description**

Creates an **Ashmem** object. To prevent resource leakage, call **OH\_DDK\_DestroyAshmem** to destroy the **Ashmem** object when it is no longer needed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| const uint8\_t \*name | Pointer to the name of the **Ashmem** object. |
| uint32\_t size | Buffer size of the **Ashmem** object. |
| [DDK\_Ashmem](../../structs/ddk-ashmem/document.md) \*\*ashmem | Pointer to the **Ashmem** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [DDK\_RetCode](../ddk-types-h/document.md#ddk_retcode) | 
[DDK\_SUCCESS](../ddk-types-h/document.md#ddk_retcode): The API call is successful.

[DDK\_INVALID\_PARAMETER](../ddk-types-h/document.md#ddk_retcode): The input **name** is a null pointer, the value of **size** is 0, or the input **ashmem** is a null pointer.

[DDK\_FAILURE](../ddk-types-h/document.md#ddk_retcode): The attempt to create an **Ashmem** object or the DDK\_Ashmem structure fails.

 |

#### \[h2\]OH\_DDK\_MapAshmem()

DDK\_RetCode OH\_DDK\_MapAshmem(DDK\_Ashmem \*ashmem, const uint8\_t ashmemMapType)

**Description**

Maps the created **Ashmem** object to the user space. Call **OH\_DDK\_UnmapAshmem** to unmap the **Ashmem** object when it is no longer needed.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [DDK\_Ashmem](../../structs/ddk-ashmem/document.md) \*ashmem | Pointer to the **Ashmem** object. |
| const uint8\_t ashmemMapType | Mapping type for the **Ashmem** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [DDK\_RetCode](../ddk-types-h/document.md#ddk_retcode) | 
[DDK\_SUCCESS](../ddk-types-h/document.md#ddk_retcode): The API call is successful.

[DDK\_NULL\_PTR](../ddk-types-h/document.md#ddk_retcode): The input **ashmem** is a null pointer.

[DDK\_FAILURE](../ddk-types-h/document.md#ddk_retcode): The file descriptor of the **Ashmem** object is invalid.

[DDK\_INVALID\_OPERATION](../ddk-types-h/document.md#ddk_retcode): The attempt to call MapAshmem fails.

 |

#### \[h2\]OH\_DDK\_UnmapAshmem()

DDK\_RetCode OH\_DDK\_UnmapAshmem(DDK\_Ashmem \*ashmem)

**Description**

Unmaps an **Ashmem** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [DDK\_Ashmem](../../structs/ddk-ashmem/document.md) \*ashmem | Pointer to the **Ashmem** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [DDK\_RetCode](../ddk-types-h/document.md#ddk_retcode) | 
[DDK\_SUCCESS](../ddk-types-h/document.md#ddk_retcode): The API call is successful.

[DDK\_NULL\_PTR](../ddk-types-h/document.md#ddk_retcode): The input **ashmem** is a null pointer.

[DDK\_FAILURE](../ddk-types-h/document.md#ddk_retcode): The file descriptor of the **Ashmem** object is invalid.

 |

#### \[h2\]OH\_DDK\_DestroyAshmem()

DDK\_RetCode OH\_DDK\_DestroyAshmem(DDK\_Ashmem \*ashmem)

**Description**

Destroys an **Ashmem** object.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [DDK\_Ashmem](../../structs/ddk-ashmem/document.md) \*ashmem | Pointer to the **Ashmem** object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [DDK\_RetCode](../ddk-types-h/document.md#ddk_retcode) | 
[DDK\_SUCCESS](../ddk-types-h/document.md#ddk_retcode): The API call is successful.

[DDK\_NULL\_PTR](../ddk-types-h/document.md#ddk_retcode): The input **ashmem** is a null pointer.

[DDK\_FAILURE](../ddk-types-h/document.md#ddk_retcode): The file descriptor of the **Ashmem** object is invalid.

 |
