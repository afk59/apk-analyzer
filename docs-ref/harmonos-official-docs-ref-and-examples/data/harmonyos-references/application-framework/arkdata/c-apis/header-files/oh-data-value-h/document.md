# oh\_data\_value.h

#### Overview

Defines APIs and enums related to a single data value.

Since API version 18, **OH\_ColumnType** is moved from **oh\_cursor.h** to this file. This type is supported in versions earlier than API version 18 and can be used in all versions.

**File to include**: <database/data/oh\_data\_value.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 18

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) | OH\_Data\_Value | Defines the [OH\_Data\_Value](../../structs/oh-data-value/document.md) struct. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_ColumnType](#oh_columntype) | OH\_ColumnType | Enumerates the column types. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value \*OH\_Value\_Create(void)](#oh_value_create) | Creates an [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance to store a single KV pair. |
| [int OH\_Value\_Destroy(OH\_Data\_Value \*value)](#oh_value_destroy) | Destroys an [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| [int OH\_Value\_PutNull(OH\_Data\_Value \*value)](#oh_value_putnull) | Adds empty data to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_PutInt(OH\_Data\_Value \*value, int64\_t val)](#oh_value_putint) | Adds an integer to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_PutReal(OH\_Data\_Value \*value, double val)](#oh_value_putreal) | Adds REAL data to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_PutText(OH\_Data\_Value \*value, const char \*val)](#oh_value_puttext) | Adds a string to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_PutBlob(OH\_Data\_Value \*value, const unsigned char \*val, size\_t length)](#oh_value_putblob) | Adds BLOB data to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_PutAsset(OH\_Data\_Value \*value, const Data\_Asset \*val)](#oh_value_putasset) | Adds an asset to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_PutAssets(OH\_Data\_Value \*value, const Data\_Asset \* const \* val, size\_t length)](#oh_value_putassets) | Adds assets to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_PutFloatVector(OH\_Data\_Value \*value, const float \*val, size\_t length)](#oh_value_putfloatvector) | Adds a float array to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_PutUnlimitedInt(OH\_Data\_Value \*value, int sign, const uint64\_t \*trueForm, size\_t length)](#oh_value_putunlimitedint) | Adds an integer array of any length to an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetType(OH\_Data\_Value \*value, OH\_ColumnType \*type)](#oh_value_gettype) | Obtains the type of a value in an **OH\_Data\_Values** instance. |
| [int OH\_Value\_IsNull(OH\_Data\_Value \*value, bool \*val)](#oh_value_isnull) | Checks whether a value is null. |
| [int OH\_Value\_GetInt(OH\_Data\_Value \*value, int64\_t \*val)](#oh_value_getint) | Obtains the integer from an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetReal(OH\_Data\_Value \*value, double \*val)](#oh_value_getreal) | Obtains the REAL data from an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetText(OH\_Data\_Value \*value, const char \*\*val)](#oh_value_gettext) | Obtains the string from an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetBlob(OH\_Data\_Value \*value, const uint8\_t \*\*val, size\_t \*length)](#oh_value_getblob) | Obtains the BLOB data from an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetAsset(OH\_Data\_Value \*value, Data\_Asset \*val)](#oh_value_getasset) | Obtains the asset from an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetAssetsCount(OH\_Data\_Value \*value, size\_t \*length)](#oh_value_getassetscount) | Obtains the length of the assets in an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetAssets(OH\_Data\_Value \*value, Data\_Asset \*\*val, size\_t inLen, size\_t \*outLen)](#oh_value_getassets) | Obtains the assets from an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetFloatVectorCount(OH\_Data\_Value \*value, size\_t \*length)](#oh_value_getfloatvectorcount) | Obtains the length of the float array in an **OH\_Data\_Values** instance. |
| [int OH\_Value\_GetFloatVector(OH\_Data\_Value \*value, float \*val, size\_t inLen, size\_t \*outLen)](#oh_value_getfloatvector) | Obtains the float array from an **OH\_Data\_Values** instance. |
| [int OH\_Value\_GetUnlimitedIntBand(OH\_Data\_Value \*value, size\_t \*length)](#oh_value_getunlimitedintband) | Obtains the length of the unlimited integer from an **OH\_Data\_Value** instance. |
| [int OH\_Value\_GetUnlimitedInt(OH\_Data\_Value \*value, int \*sign, uint64\_t \*trueForm, size\_t inLen, size\_t \*outLen)](#oh_value_getunlimitedint) | Obtains the unlimited integer from an **OH\_Data\_Value** instance. |

#### Enum Description

#### \[h2\]OH\_ColumnType

enum OH\_ColumnType

**Description**

Enumerates the column types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| TYPE\_NULL = 0 | NULL. |
| TYPE\_INT64 | INT64. |
| TYPE\_REAL | REAL. |
| TYPE\_TEXT | TEXT. |
| TYPE\_BLOB | BLOB. |
| TYPE\_ASSET | 
ASSET (asset attachment).

**Since**: 11

 |
| TYPE\_ASSETS | 

ASSETS (multiple asset attachments).

**Since**: 11

 |
| TYPE\_FLOAT\_VECTOR | 

FLOAT VECTOR.

**Since**: 18

 |
| TYPE\_UNLIMITED\_INT | 

Number longer than 64 digits.

**Since**: 18

 |

#### Function Description

#### \[h2\]OH\_Value\_Create()

OH\_Data\_Value \*OH\_Value\_Create(void)

**Description**

Creates an [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance to store a single KV pair.

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) | 
Returns a pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance if the operation is successful; returns **nullptr** otherwise.

Use [OH\_Value\_Destroy](#oh_value_destroy) to release the memory in time.

 |

#### \[h2\]OH\_Value\_Destroy()

int OH\_Value\_Destroy(OH\_Data\_Value \*value)

**Description**

Destroys an [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutNull()

int OH\_Value\_PutNull(OH\_Data\_Value \*value)

**Description**

Adds empty data to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutInt()

int OH\_Value\_PutInt(OH\_Data\_Value \*value, int64\_t val)

**Description**

Adds an integer to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| int64\_t val | Integer to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutReal()

int OH\_Value\_PutReal(OH\_Data\_Value \*value, double val)

**Description**

Adds REAL data to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| double val | REAL data to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutText()

int OH\_Value\_PutText(OH\_Data\_Value \*value, const char \*val)

**Description**

Adds a string to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| const char \*val | Pointer to the string to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutBlob()

int OH\_Value\_PutBlob(OH\_Data\_Value \*value, const unsigned char \*val, size\_t length)

**Description**

Adds BLOB data to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| const unsigned char \*val | Pointer to the BLOB data to add. |
| size\_t length | Length of the BLOB data to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutAsset()

int OH\_Value\_PutAsset(OH\_Data\_Value \*value, const Data\_Asset \*val)

**Description**

Adds an asset to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| const [Data\_Asset](../../structs/data-asset/document.md) \*val | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutAssets()

int OH\_Value\_PutAssets(OH\_Data\_Value \*value, const Data\_Asset \* const \* val, size\_t length)

**Description**

Adds assets to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| const [Data\_Asset](../../structs/data-asset/document.md) \* const \* val | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| size\_t length | Number of elements in the [Data\_Asset](../../structs/data-asset/document.md) object to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutFloatVector()

int OH\_Value\_PutFloatVector(OH\_Data\_Value \*value, const float \*val, size\_t length)

**Description**

Adds a float array to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| const float \*val | Pointer to the float array to add. |
| size\_t length | Length of the float array to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_PutUnlimitedInt()

int OH\_Value\_PutUnlimitedInt(OH\_Data\_Value \*value, int sign, const uint64\_t \*trueForm, size\_t length)

**Description**

Adds an integer array of any length to an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| int sign | Sign notation of the integer array to add. The value **0** indicates a positive integer, and the value **1** indicates a negative integer. |
| const uint64\_t \*trueForm | Pointer to the integer array to add. |
| size\_t length | Length of the integer array to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_GetType()

int OH\_Value\_GetType(OH\_Data\_Value \*value, OH\_ColumnType \*type)

**Description**

Obtains the data type.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| [OH\_ColumnType](#oh_columntype) \*type | Pointer to the data type obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_IsNull()

int OH\_Value\_IsNull(OH\_Data\_Value \*value, bool \*val)

**Description**

Checks whether a value is null.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| bool \*val | Pointer to the check result. The value **true** means the value is empty, and the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

 |

#### \[h2\]OH\_Value\_GetInt()

int OH\_Value\_GetInt(OH\_Data\_Value \*value, int64\_t \*val)

**Description**

Obtains the integer from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| int64\_t \*val | Pointer to the integer data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetReal()

int OH\_Value\_GetReal(OH\_Data\_Value \*value, double \*val)

**Description**

Obtains the REAL data from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| double \*val | Pointer to the REAL data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetText()

int OH\_Value\_GetText(OH\_Data\_Value \*value, const char \*\*val)

**Description**

Obtains the string from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| const char \*\*val | 
Double pointer to the string obtained.

You do not need to apply for or release memory for it.

The lifecycle of **val** complies with the value of **index** in **value**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetBlob()

int OH\_Value\_GetBlob(OH\_Data\_Value \*value, const uint8\_t \*\*val, size\_t \*length)

**Description**

Obtains the BLOB data from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| const uint8\_t \*\*val | 
Double pointer to the BLOB data obtained.

You do not need to apply for or release memory for it.

The lifecycle of **val** complies with the value of **index** in **value**.

 |
| size\_t \*length | Pointer to the length of the BLOB data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetAsset()

int OH\_Value\_GetAsset(OH\_Data\_Value \*value, Data\_Asset \*val)

**Description**

Obtains the asset from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| [Data\_Asset](../../structs/data-asset/document.md) \*val | 
Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance.

Data memory should be requested.

This function is used to fill in data only. Otherwise, the operation fails.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetAssetsCount()

int OH\_Value\_GetAssetsCount(OH\_Data\_Value \*value, size\_t \*length)

**Description**

Obtains the length of the assets in an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| size\_t \*length | Pointer to the length of the ASSETS data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetAssets()

int OH\_Value\_GetAssets(OH\_Data\_Value \*value, Data\_Asset \*\*val, size\_t inLen, size\_t \*outLen)

**Description**

Obtains the assets from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| [Data\_Asset](../../structs/data-asset/document.md) \*\*val | 
Double pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance.

Data memory should be requested.

This function is used to fill in data only. Otherwise, the operation fails.

 |
| size\_t inLen | Size of **val**, which can be obtained using [OH\_Values\_GetAssetsCount](../oh-data-values-h/document.md#oh_values_getassetscount). |
| size\_t \*outLen | Pointer to the actual length of the data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetFloatVectorCount()

int OH\_Value\_GetFloatVectorCount(OH\_Data\_Value \*value, size\_t \*length)

**Description**

Obtains the length of the float array in an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| size\_t \*length | Pointer to the length of the float data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetFloatVector()

int OH\_Value\_GetFloatVector(OH\_Data\_Value \*value, float \*val, size\_t inLen, size\_t \*outLen)

**Description**

Obtains the float array from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| float \*val | 
Pointer to the float array obtained.

Data memory should be requested.

This function is used to fill in data only. Otherwise, the operation fails.

 |
| size\_t inLen | Size of **val**, which can be obtained using [OH\_Values\_GetFloatVectorCount](../oh-data-values-h/document.md#oh_values_getfloatvectorcount). |
| size\_t \*outLen | Pointer to the actual length of the data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetUnlimitedIntBand()

int OH\_Value\_GetUnlimitedIntBand(OH\_Data\_Value \*value, size\_t \*length)

**Description**

Obtains the length of the unlimited integer from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| size\_t \*length | Pointer to the length of the integer obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Value\_GetUnlimitedInt()

int OH\_Value\_GetUnlimitedInt(OH\_Data\_Value \*value, int \*sign, uint64\_t \*trueForm, size\_t inLen, size\_t \*outLen)

**Description**

Obtains the unlimited integer from an **OH\_Data\_Value** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*value | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |
| int \*sign | Pointer to the sign notation of the integer obtained. The value **0** indicates a positive integer, and the value **1** indicates a negative integer. |
| uint64\_t \*trueForm | 
Pointer to the integer array obtained.

Data memory should be requested.

This function is used to fill in data only. Otherwise, the operation fails.

 |
| size\_t inLen | **trueForm** length, which can be obtained using [OH\_Values\_GetUnlimitedIntBand](../oh-data-values-h/document.md#oh_values_getunlimitedintband). |
| size\_t \*outLen | Pointer to the actual length of the data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates the parameters are invalid.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |
