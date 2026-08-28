# oh\_data\_values.h

#### Overview

Defines APIs and enums related to multiple data values.

**File to include**: <database/data/oh\_data\_values.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 18

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) | OH\_Data\_Values | Defines the **OH\_Data\_Values** struct. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values \*OH\_Values\_Create(void)](#oh_values_create) | Creates an [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance to store multiple KV pairs. |
| [int OH\_Values\_Destroy(OH\_Data\_Values \*values)](#oh_values_destroy) | Destroys an [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| [int OH\_Values\_Put(OH\_Data\_Values \*values, const OH\_Data\_Value \*val)](#oh_values_put) | Adds data of the **OH\_Data\_Value** type to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutNull(OH\_Data\_Values \*values)](#oh_values_putnull) | Adds empty data to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutInt(OH\_Data\_Values \*values, int64\_t val)](#oh_values_putint) | Adds an integer to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutReal(OH\_Data\_Values \*values, double val)](#oh_values_putreal) | Adds REAL data to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutText(OH\_Data\_Values \*values, const char \*val)](#oh_values_puttext) | Adds a string to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutBlob(OH\_Data\_Values \*values, const unsigned char \*val, size\_t length)](#oh_values_putblob) | Adds BLOB data to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutAsset(OH\_Data\_Values \*values, const Data\_Asset \*val)](#oh_values_putasset) | Adds an asset to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutAssets(OH\_Data\_Values \*values, const Data\_Asset \* const \* val, size\_t length)](#oh_values_putassets) | Adds assets to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutFloatVector(OH\_Data\_Values \*values, const float \*val, size\_t length)](#oh_values_putfloatvector) | Adds a float array to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_PutUnlimitedInt(OH\_Data\_Values \*values, int sign, const uint64\_t \*trueForm, size\_t length)](#oh_values_putunlimitedint) | Adds an integer array of any length to an **OH\_Data\_Values** instance. |
| [int OH\_Values\_Count(OH\_Data\_Values \*values, size\_t \*count)](#oh_values_count) | Obtains the number of values in an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetType(OH\_Data\_Values \*values, int index, OH\_ColumnType \*type)](#oh_values_gettype) | Obtains the type of a value in an **OH\_Data\_Values** instance. |
| [int OH\_Values\_Get(OH\_Data\_Values \*values, int index, OH\_Data\_Value \*\*val)](#oh_values_get) | Obtains data of the **OH\_Data\_Value** type. |
| [int OH\_Values\_IsNull(OH\_Data\_Values \*values, int index, bool \*val)](#oh_values_isnull) | Checks whether a value is null. |
| [int OH\_Values\_GetInt(OH\_Data\_Values \*values, int index, int64\_t \*val)](#oh_values_getint) | Obtains the integer from an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetReal(OH\_Data\_Values \*values, int index, double \*val)](#oh_values_getreal) | Obtains the REAL data from an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetText(OH\_Data\_Values \*values, int index, const char \*\*val)](#oh_values_gettext) | Obtains the string from an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetBlob(OH\_Data\_Values \*values, int index, const uint8\_t \*\*val, size\_t \*length)](#oh_values_getblob) | Obtains the BLOB data from an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetAsset(OH\_Data\_Values \*values, int index, Data\_Asset \*val)](#oh_values_getasset) | Obtains the asset from an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetAssetsCount(OH\_Data\_Values \*values, int index, size\_t \*length)](#oh_values_getassetscount) | Obtains the length of the asset in an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetAssets(OH\_Data\_Values \*values, int index, Data\_Asset \*\*val, size\_t inLen, size\_t \*outLen)](#oh_values_getassets) | Obtains the assets from an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetFloatVectorCount(OH\_Data\_Values \*values, int index, size\_t \*length)](#oh_values_getfloatvectorcount) | Obtains the length of the float array in an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetFloatVector(OH\_Data\_Values \*values, int index, float \*val, size\_t inLen, size\_t \*outLen)](#oh_values_getfloatvector) | Obtains the float array from an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetUnlimitedIntBand(OH\_Data\_Values \*values, int index, size\_t \*length)](#oh_values_getunlimitedintband) | Obtains the length of the unlimited integer from an **OH\_Data\_Values** instance. |
| [int OH\_Values\_GetUnlimitedInt(OH\_Data\_Values \*values, int index, int \*sign, uint64\_t \*trueForm, size\_t inLen,size\_t \*outLen)](#oh_values_getunlimitedint) | Obtains the unlimited integer from an **OH\_Data\_Values** instance. |

#### Function Description

#### \[h2\]OH\_Values\_Create()

OH\_Data\_Values \*OH\_Values\_Create(void)

**Description**

Creates an [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance to store multiple KV pairs.

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) | 
Returns a pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance created if the operation is successful; returns **nullptr** otherwise.

Use [OH\_Values\_Destroy](#oh_values_destroy) to release the memory in time.

 |

#### \[h2\]OH\_Values\_Destroy()

int OH\_Values\_Destroy(OH\_Data\_Values \*values)

**Description**

Destroys an [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_Put()

int OH\_Values\_Put(OH\_Data\_Values \*values, const OH\_Data\_Value \*val)

**Description**

Adds data of the **OH\_Data\_Value** type to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| const [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*val | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutNull()

int OH\_Values\_PutNull(OH\_Data\_Values \*values)

**Description**

Adds empty data to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutInt()

int OH\_Values\_PutInt(OH\_Data\_Values \*values, int64\_t val)

**Description**

Adds an integer to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int64\_t val | Pointer to the integer to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutReal()

int OH\_Values\_PutReal(OH\_Data\_Values \*values, double val)

**Description**

Adds REAL data to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| double val | Pointer to the REAL data to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutText()

int OH\_Values\_PutText(OH\_Data\_Values \*values, const char \*val)

**Description**

Adds a string to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| const char \*val | Pointer to the string to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutBlob()

int OH\_Values\_PutBlob(OH\_Data\_Values \*values, const unsigned char \*val, size\_t length)

**Description**

Adds BLOB data to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| const unsigned char \*val | Pointer to the BLOB data to add. |
| size\_t length | Length of the BLOB data to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutAsset()

int OH\_Values\_PutAsset(OH\_Data\_Values \*values, const Data\_Asset \*val)

**Description**

Adds an asset to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| const [Data\_Asset](../../structs/data-asset/document.md) \*val | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutAssets()

int OH\_Values\_PutAssets(OH\_Data\_Values \*values, const Data\_Asset \* const \* val, size\_t length)

**Description**

Adds assets to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| const [Data\_Asset](../../structs/data-asset/document.md) \* const \* val | Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance. |
| size\_t length | Number of elements in the [Data\_Asset](../../structs/data-asset/document.md) object to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutFloatVector()

int OH\_Values\_PutFloatVector(OH\_Data\_Values \*values, const float \*val, size\_t length)

**Description**

Adds a float array to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| const float \*val | Pointer to the float array to add. |
| size\_t length | Length of the float array to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_PutUnlimitedInt()

int OH\_Values\_PutUnlimitedInt(OH\_Data\_Values \*values, int sign, const uint64\_t \*trueForm, size\_t length)

**Description**

Adds an integer array of any length to an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int sign | Sign notation of the integer array to add. The value **0** indicates a positive integer, and the value **1** indicates a negative integer. |
| const uint64\_t \*trueForm | Pointer to the integer array to add. |
| size\_t length | Length of the integer array to add. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_Count()

int OH\_Values\_Count(OH\_Data\_Values \*values, size\_t \*count)

**Description**

Obtains the number of records in an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| size\_t \*count | Pointer to the number of values contained in **values** obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_GetType()

int OH\_Values\_GetType(OH\_Data\_Values \*values, int index, OH\_ColumnType \*type)

**Description**

Obtains the data type.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| [OH\_ColumnType](../oh-data-value-h/document.md#oh_columntype) \*type | Pointer to the data type obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_Get()

int OH\_Values\_Get(OH\_Data\_Values \*values, int index, OH\_Data\_Value \*\*val)

**Description**

Obtains data of the **OH\_Data\_Value** type.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*\*val | 
Double pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance.

You do not need to apply for or release memory for it.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_IsNull()

int OH\_Values\_IsNull(OH\_Data\_Values \*values, int index, bool \*val)

**Description**

Checks whether a value is null.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| bool \*val | Pointer to the check result. The value **true** means the value is empty, and the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Values\_GetInt()

int OH\_Values\_GetInt(OH\_Data\_Values \*values, int index, int64\_t \*val)

**Description**

Obtains the integer from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| int64\_t \*val | Pointer to the integer data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetReal()

int OH\_Values\_GetReal(OH\_Data\_Values \*values, int index, double \*val)

**Description**

Obtains the REAL data from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| double \*val | Pointer to the REAL data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetText()

int OH\_Values\_GetText(OH\_Data\_Values \*values, int index, const char \*\*val)

**Description**

Obtains the string from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| const char \*\*val | 
Pointer to the string obtained.

You do not need to apply for or release memory for it.

The lifecycle of **val** complies with the value of **index** in **values**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetBlob()

int OH\_Values\_GetBlob(OH\_Data\_Values \*values, int index, const uint8\_t \*\*val, size\_t \*length)

**Description**

Obtains the BLOB data from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| const uint8\_t \*\*val | 
Double pointer to the BLOB data obtained.

You do not need to apply for or release memory for it.

The lifecycle of **val** complies with the value of **index** in **values**.

 |
| size\_t \*length | Pointer to the length of the BLOB data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetAsset()

int OH\_Values\_GetAsset(OH\_Data\_Values \*values, int index, Data\_Asset \*val)

**Description**

Obtains the asset from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| [Data\_Asset](../../structs/data-asset/document.md) \*val | 
Pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance.

Data memory should be requested.

This function is used to fill in data only. Otherwise, the execution fails.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetAssetsCount()

int OH\_Values\_GetAssetsCount(OH\_Data\_Values \*values, int index, size\_t \*length)

**Description**

Obtains the length of the asset in an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| size\_t \*length | Pointer to the length of the ASSETS data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetAssets()

int OH\_Values\_GetAssets(OH\_Data\_Values \*values, int index, Data\_Asset \*\*val, size\_t inLen, size\_t \*outLen)

**Description**

Obtains the assets from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| [Data\_Asset](../../structs/data-asset/document.md) \*\*val | 
Double pointer to the [Data\_Asset](../../structs/data-asset/document.md) instance.

Data memory should be requested.

This function is used to fill in data only. Otherwise, the execution fails.

 |
| size\_t inLen | Size of **val**, which can be obtained using [OH\_Values\_GetAssetsCount](#oh_values_getassetscount). |
| size\_t \*outLen | Pointer to the actual length of the data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetFloatVectorCount()

int OH\_Values\_GetFloatVectorCount(OH\_Data\_Values \*values, int index, size\_t \*length)

**Description**

Obtains the length of the float array in an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| size\_t \*length | Pointer to the length of the float data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetFloatVector()

int OH\_Values\_GetFloatVector(OH\_Data\_Values \*values, int index, float \*val, size\_t inLen, size\_t \*outLen)

**Description**

Obtains the float array from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| float \*val | 
Pointer to the float array obtained.

Data memory should be requested.

This function is used to fill in data only. Otherwise, the execution fails.

 |
| size\_t inLen | Size of **val**, which can be obtained using [OH\_Values\_GetFloatVectorCount](#oh_values_getfloatvectorcount). |
| size\_t \*outLen | Pointer to the actual length of the data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetUnlimitedIntBand()

int OH\_Values\_GetUnlimitedIntBand(OH\_Data\_Values \*values, int index, size\_t \*length)

**Description**

Obtains the length of the unlimited integer from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| size\_t \*length | Pointer to the length of the integer obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |

#### \[h2\]OH\_Values\_GetUnlimitedInt()

int OH\_Values\_GetUnlimitedInt(OH\_Data\_Values \*values, int index, int \*sign, uint64\_t \*trueForm, size\_t inLen, size\_t \*outLen)

**Description**

Obtains the unlimited integer from an **OH\_Data\_Values** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*values | Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| int index | Index of the value to check, which starts from 0 in **values**. |
| int \*sign | Pointer to the sign notation of the integer obtained. The value **0** indicates a positive integer, and the value **1** indicates a negative integer. |
| uint64\_t \*trueForm | 
Pointer to the integer array obtained.

Data memory should be requested.

This function is used to fill in data only. Otherwise, the execution fails.

 |
| size\_t inLen | **trueForm** length, which can be obtained using [OH\_Values\_GetUnlimitedIntBand](#oh_values_getunlimitedintband). |
| size\_t \*outLen | Pointer to the actual length of the data obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters are specified.

**RDB\_E\_DATA\_TYPE\_NULL** indicates the stored data is empty.

**RDB\_E\_TYPE\_MISMATCH** indicates the data types do not match.

 |
