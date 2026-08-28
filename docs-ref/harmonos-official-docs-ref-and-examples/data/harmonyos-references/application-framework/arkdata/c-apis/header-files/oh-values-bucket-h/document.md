# oh\_values\_bucket.h

#### Overview

Defines the types of the key and value in a KV pair.

**File to include**: <database/rdb/oh\_values\_bucket.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) | OH\_VBucket | Defines a struct for the types of the key and value in a KV pair. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int OH\_VBucket\_PutAsset(OH\_VBucket \*bucket, const char \*field, Data\_Asset \*value)](#oh_vbucket_putasset) | Puts a [Data\_Asset](../../structs/data-asset/document.md) object into the [OH\_VBucket](../../structs/oh-vbucket/document.md) object in the given column. |
| [int OH\_VBucket\_PutAssets(OH\_VBucket \*bucket, const char \*field, Data\_Asset \*\*value, uint32\_t count)](#oh_vbucket_putassets) | Puts an array of [Data\_Asset](../../structs/data-asset/document.md) objects into the [OH\_VBucket](../../structs/oh-vbucket/document.md) object in the given column. |
| [int OH\_VBucket\_PutFloatVector(OH\_VBucket \*bucket, const char \*field, const float \*vec, size\_t len)](#oh_vbucket_putfloatvector) | Puts a float array into an [OH\_VBucket](../../structs/oh-vbucket/document.md) object in the given column. |
| [int OH\_VBucket\_PutUnlimitedInt(OH\_VBucket \*bucket, const char \*field, int sign, const uint64\_t \*trueForm, size\_t len)](#oh_vbucket_putunlimitedint) | Puts an integer of any length into an [OH\_VBucket](../../structs/oh-vbucket/document.md) object in the given column. |

#### Function Description

#### \[h2\]OH\_VBucket\_PutAsset()

int OH\_VBucket\_PutAsset(OH\_VBucket \*bucket, const char \*field, Data\_Asset \*value)

**Description**

Puts a [Data\_Asset](../../structs/data-asset/document.md) object into the [OH\_VBucket](../../structs/oh-vbucket/document.md) object in the given column.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) \*bucket | Pointer to the [OH\_VBucket](../../structs/oh-vbucket/document.md) instance. |
| const char \*field | Pointer to the column name in the database table. |
| [Data\_Asset](../../structs/data-asset/document.md) \*value | Pointer to the value to put. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

 |

#### \[h2\]OH\_VBucket\_PutAssets()

int OH\_VBucket\_PutAssets(OH\_VBucket \*bucket, const char \*field, Data\_Asset \*\*value, uint32\_t count)

**Description**

Puts an array of [Data\_Asset](../../structs/data-asset/document.md) objects into the [OH\_VBucket](../../structs/oh-vbucket/document.md) object in the given column.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) \*bucket | Pointer to the [OH\_VBucket](../../structs/oh-vbucket/document.md) instance. |
| const char \*field | Pointer to the column name in the database table. |
| [Data\_Asset](../../structs/data-asset/document.md) \*\*value | Double pointer to the value to put. |
| uint32\_t count | Number of elements in the [Data\_Asset](../../structs/data-asset/document.md) object to put. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

 |

**See**

OH\_VBucket

#### \[h2\]OH\_VBucket\_PutFloatVector()

int OH\_VBucket\_PutFloatVector(OH\_VBucket \*bucket, const char \*field, const float \*vec, size\_t len)

**Description**

Puts a float array into an [OH\_VBucket](../../structs/oh-vbucket/document.md) object in the given column.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) \*bucket | Pointer to the [OH\_VBucket](../../structs/oh-vbucket/document.md) instance. |
| const char \*field | Pointer to the column name in the database table. |
| const float \*vec | Pointer to the float array to put. |
| size\_t len | Length of the float array to put. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

 |

**See**

OH\_VBucket

#### \[h2\]OH\_VBucket\_PutUnlimitedInt()

int OH\_VBucket\_PutUnlimitedInt(OH\_VBucket \*bucket, const char \*field, int sign, const uint64\_t \*trueForm, size\_t len)

**Description**

Puts an integer of any length into an [OH\_VBucket](../../structs/oh-vbucket/document.md) object in the given column.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) \*bucket | Pointer to the [OH\_VBucket](../../structs/oh-vbucket/document.md) instance. |
| const char \*field | Pointer to the column name in the database table. |
| int sign | Sign notation of the integer object. The value **0** indicates a positive integer, and the value **1** indicates a negative integer. |
| const uint64\_t \*trueForm | Pointer to the integer object to put. |
| size\_t len | Length of the integer object to put. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

 |
