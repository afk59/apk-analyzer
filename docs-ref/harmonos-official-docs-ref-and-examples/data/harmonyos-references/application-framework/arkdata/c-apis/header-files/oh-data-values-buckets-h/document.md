# oh\_data\_values\_buckets.h

#### Overview

Defines structs, APIs, and enums related to stored data values.

**File to include**: <database/data/oh\_data\_values\_buckets.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 18

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) | OH\_Data\_VBuckets | Defines the **OH\_Data\_VBuckets** struct. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Data\_VBuckets \*OH\_VBuckets\_Create(void)](#oh_vbuckets_create) | Creates an **OH\_Data\_VBuckets** instance. |
| [int OH\_VBuckets\_Destroy(OH\_Data\_VBuckets \*buckets)](#oh_vbuckets_destroy) | Destroys an **OH\_Data\_VBuckets** instance. |
| [int OH\_VBuckets\_PutRow(OH\_Data\_VBuckets \*buckets, const OH\_VBucket \*row)](#oh_vbuckets_putrow) | Adds data of the **OH\_VBucket** type to an **OH\_Data\_VBuckets** instance. |
| [int OH\_VBuckets\_PutRows(OH\_Data\_VBuckets \*buckets, const OH\_Data\_VBuckets \*rows)](#oh_vbuckets_putrows) | Adds data of the **OH\_Data\_VBuckets** type to an **OH\_Data\_VBuckets** instance. |
| [int OH\_VBuckets\_RowCount(OH\_Data\_VBuckets \*buckets, size\_t \*count)](#oh_vbuckets_rowcount) | Obtains the number of **OH\_VBucket**s in an **OH\_Data\_VBuckets** instance. |

#### Function Description

#### \[h2\]OH\_VBuckets\_Create()

OH\_Data\_VBuckets \*OH\_VBuckets\_Create(void)

**Description**

Creates an **OH\_Data\_VBuckets** instance.

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) | 
Returns a pointer to the [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) instance if the operation is successful; returns **nullptr** otherwise.

Use [OH\_VBuckets\_Destroy](#oh_vbuckets_destroy) to release the memory in time.

 |

#### \[h2\]OH\_VBuckets\_Destroy()

int OH\_VBuckets\_Destroy(OH\_Data\_VBuckets \*buckets)

**Description**

Destroys an **OH\_Data\_VBuckets** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) \*buckets | Pointer to the [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_VBuckets\_PutRow()

int OH\_VBuckets\_PutRow(OH\_Data\_VBuckets \*buckets, const OH\_VBucket \*row)

**Description**

Adds data of the **OH\_VBucket** type to an **OH\_Data\_VBuckets** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) \*buckets | Pointer to the [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) instance. |
| const [OH\_VBucket](../../structs/oh-vbucket/document.md) \*row | Pointer to the [OH\_VBucket](../../structs/oh-vbucket/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_VBuckets\_PutRows()

int OH\_VBuckets\_PutRows(OH\_Data\_VBuckets \*buckets, const OH\_Data\_VBuckets \*rows)

**Description**

Adds data of the **OH\_Data\_VBuckets** type to an **OH\_Data\_VBuckets** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) \*buckets | Pointer to the [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) instance. |
| const [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) \*rows | Pointer to the [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_VBuckets\_RowCount()

int OH\_VBuckets\_RowCount(OH\_Data\_VBuckets \*buckets, size\_t \*count)

**Description**

Obtains the number of **OH\_VBucket**s in an **OH\_Data\_VBuckets** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) \*buckets | Pointer to the [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) instance. |
| size\_t \*count | Pointer to the number of [OH\_VBucket](../../structs/oh-vbucket/document.md)s in an [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |
