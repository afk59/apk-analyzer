# purgeable\_memory.h

#### Overview

Provides APIs for managing the purgeable memory.

For example, you can create a purgeable memory, start or end the memory reading/writing, and rebuild the memory.

Link to the **libpurgeable\_memory\_ndk.z.so** file when you use the API.

**File to include**: <purgeable\_memory/purgeable\_memory.h>

**Library**: libpurgeable\_memory\_ndk.z.so

**System capability**: SystemCapability.Kernel.Memory

**Since**: 10

**Related module**: [memory](../../modules/memory/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [PurgMem](../../structs/purgmem/document.md) | OH\_PurgeableMemory | Defines a purgeable memory struct. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef bool (\*OH\_PurgeableMemory\_ModifyFunc)(void \*, size\_t, void \*)](#oh_purgeablememory_modifyfunc) | OH\_PurgeableMemory\_ModifyFunc | Pointer to a function used to construct the content of a purgeable memory object. |
| [OH\_PurgeableMemory \*OH\_PurgeableMemory\_Create(size\_t size, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara)](#oh_purgeablememory_create) | \- | Creates a [PurgMem](../../structs/purgmem/document.md) object. |
| [bool OH\_PurgeableMemory\_Destroy(OH\_PurgeableMemory \*purgObj)](#oh_purgeablememory_destroy) | \- | Destroys a [PurgMem](../../structs/purgmem/document.md) object. |
| [bool OH\_PurgeableMemory\_BeginRead(OH\_PurgeableMemory \*purgObj)](#oh_purgeablememory_beginread) | \- | Starts reading a [PurgMem](../../structs/purgmem/document.md) object. |
| [void OH\_PurgeableMemory\_EndRead(OH\_PurgeableMemory \*purgObj)](#oh_purgeablememory_endread) | \- | Stops reading a [PurgMem](../../structs/purgmem/document.md) object. |
| [bool OH\_PurgeableMemory\_BeginWrite(OH\_PurgeableMemory \*purgObj)](#oh_purgeablememory_beginwrite) | \- | Starts writing a [PurgMem](../../structs/purgmem/document.md) object. |
| [void OH\_PurgeableMemory\_EndWrite(OH\_PurgeableMemory \*purgObj)](#oh_purgeablememory_endwrite) | \- | Stops writing a [PurgMem](../../structs/purgmem/document.md) object. |
| [void \*OH\_PurgeableMemory\_GetContent(OH\_PurgeableMemory \*purgObj)](#oh_purgeablememory_getcontent) | \- | Obtains the content of a [PurgMem](../../structs/purgmem/document.md) object. |
| [size\_t OH\_PurgeableMemory\_ContentSize(OH\_PurgeableMemory \*purgObj)](#oh_purgeablememory_contentsize) | \- | Obtains the content size of a [PurgMem](../../structs/purgmem/document.md) object. |
| [bool OH\_PurgeableMemory\_AppendModify(OH\_PurgeableMemory \*purgObj, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara)](#oh_purgeablememory_appendmodify) | \- | Appends the modification to a [PurgMem](../../structs/purgmem/document.md) object. |

#### Function Description

#### \[h2\]OH\_PurgeableMemory\_ModifyFunc()

typedef bool (\*OH\_PurgeableMemory\_ModifyFunc)(void \*, size\_t, void \*)

**Description**

Pointer to a function used to construct the content of a purgeable memory object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| void \* | Pointer to the start address of the content of a purgeable memory object. |
| size\_t | Data size of the content. |
| void \* | Pointer to other private parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Whether the content is successfully constructed. The value **true** indicates that the operation is successful, and **false** indicates the opposite. |

#### \[h2\]OH\_PurgeableMemory\_Create()

OH\_PurgeableMemory \*OH\_PurgeableMemory\_Create(size\_t size, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara)

**Description**

Creates a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| size\_t size | Data size of the content of a purgeable memory object. |
| [OH\_PurgeableMemory\_ModifyFunc](#oh_purgeablememory_modifyfunc) func | Function used to restore data when the content of a purgeable memory object is cleared. |
| void \*funcPara | Pointer to the parameter used by @func. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_PurgeableMemory \*](../../structs/purgmem/document.md) | Returns the purgeable memory object created. |

#### \[h2\]OH\_PurgeableMemory\_Destroy()

bool OH\_PurgeableMemory\_Destroy(OH\_PurgeableMemory \*purgObj)

**Description**

Destroys a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PurgeableMemory](../../structs/purgmem/document.md) \*purgObj | Pointer to the purgeable memory object to be destroyed. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Whether the destruction is successful. The value **true** indicates that the destruction is successful, and **false** indicates the opposite. Returns **true** if the purgeable memory object is **NULL**.

Returns **true** if the destruction is successful. The purgeable memory object is set to **NULL** to avoid Use-After-Free.

 |

#### \[h2\]OH\_PurgeableMemory\_BeginRead()

bool OH\_PurgeableMemory\_BeginRead(OH\_PurgeableMemory \*purgObj)

**Description**

Starts reading a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PurgeableMemory](../../structs/purgmem/document.md) \*purgObj | Pointer to the purgeable memory object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Whether the reading is successful. Returns **true** if the content of the purgeable memory object exists.

If the content is cleared (that is, the content does not exist), the system attempts to restore the data.

Returns **false** if the restore fails.

Returns **true** if the restore is successful.

When this function returns **true**, the system cannot reclaim the memory of the content of the purgeable memory object until [OH\_PurgeableMemory\_EndRead()](#oh_purgeablememory_endread) is called.

 |

#### \[h2\]OH\_PurgeableMemory\_EndRead()

void OH\_PurgeableMemory\_EndRead(OH\_PurgeableMemory \*purgObj)

**Description**

Stops reading a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PurgeableMemory](../../structs/purgmem/document.md) \*purgObj | Pointer to the purgeable memory object. When this function ends, the OS may reclaim the memory of the content of the purgeable memory object later. |

#### \[h2\]OH\_PurgeableMemory\_BeginWrite()

bool OH\_PurgeableMemory\_BeginWrite(OH\_PurgeableMemory \*purgObj)

**Description**

Starts writing a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PurgeableMemory](../../structs/purgmem/document.md) \*purgObj | Pointer to the purgeable memory object. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | 
Whether the content of the purgeable memory object exists. Returns **true** if the content exists.

If the content is cleared, the system restores its data.

Returns **false** if the content is cleared and the restore fails.

Returns **true** if the restore is successful.

When this function returns **true**, the OS cannot reclaim the memory of the content of the purgeable memory object until [OH\_PurgeableMemory\_EndWrite()](#oh_purgeablememory_endwrite) is called.

 |

#### \[h2\]OH\_PurgeableMemory\_EndWrite()

void OH\_PurgeableMemory\_EndWrite(OH\_PurgeableMemory \*purgObj)

**Description**

Stops writing a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PurgeableMemory](../../structs/purgmem/document.md) \*purgObj | Pointer to the purgeable memory object. When this function ends, the OS may reclaim the memory of the content of the purgeable memory object later. |

#### \[h2\]OH\_PurgeableMemory\_GetContent()

void \*OH\_PurgeableMemory\_GetContent(OH\_PurgeableMemory \*purgObj)

**Description**

Obtains the content of a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PurgeableMemory](../../structs/purgmem/document.md) \*purgObj | Pointer to the purgeable memory object. |

**Returns**

| Type | Description |
| :-- | :-- |
| void \* | 
Returns the start address of the content of the purgeable memory object.

Returns **NULL** if the purgeable memory object is **NULL**.

This function should be protected by [OH\_PurgeableMemory\_BeginRead()](#oh_purgeablememory_beginread)/[OH\_PurgeableMemory\_EndRead()](#oh_purgeablememory_endread) or [OH\_PurgeableMemory\_BeginWrite()](#oh_purgeablememory_beginwrite)/[OH\_PurgeableMemory\_EndWrite()](#oh_purgeablememory_endwrite).

 |

#### \[h2\]OH\_PurgeableMemory\_ContentSize()

size\_t OH\_PurgeableMemory\_ContentSize(OH\_PurgeableMemory \*purgObj)

**Description**

Obtains the content size of a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PurgeableMemory](../../structs/purgmem/document.md) \*purgObj | Pointer to the purgeable memory object. |

**Returns**

| Type | Description |
| :-- | :-- |
| size\_t | 
Returns the content size of the purgeable memory object obtained.

Returns **0** if the purgeable memory object is **NULL**.

 |

#### \[h2\]OH\_PurgeableMemory\_AppendModify()

bool OH\_PurgeableMemory\_AppendModify(OH\_PurgeableMemory \*purgObj, OH\_PurgeableMemory\_ModifyFunc func, void \*funcPara)

**Description**

Appends the modification to a [PurgMem](../../structs/purgmem/document.md) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_PurgeableMemory](../../structs/purgmem/document.md) \*purgObj | Pointer to the purgeable memory object. |
| [OH\_PurgeableMemory\_ModifyFunc](#oh_purgeablememory_modifyfunc) func | Function used to modify the content of a purgeable memory object. |
| void \*funcPara | Pointer to the parameter used by @func. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Returns the operation result. The value **true** indicates that the operation is successful, and **false** indicates the opposite. |
