# OH\_VBucket

typedef struct {...} OH\_VBucket

#### Overview

Defines a struct for the types of the key and value in a KV pair.

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [oh\_values\_bucket.h](../../header-files/oh-values-bucket-h/document.md)

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int64\_t id | Unique identifier of the **OH\_VBucket** struct. |
| uint16\_t capability | Number of the KV pairs in the struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int (\*putText)(OH\_VBucket \*bucket, const char \*field, const char \*value)](#puttext) | Puts a char\* value into the **OH\_VBucket** object in the given column. |
| [int (\*putInt64)(OH\_VBucket \*bucket, const char \*field, int64\_t value)](#putint64) | Puts an int64\_t value into the **OH\_VBucket** object in the given column. |
| [int (\*putReal)(OH\_VBucket \*bucket, const char \*field, double value)](#putreal) | Puts a double value into the **OH\_VBucket** object in the given column. |
| [int (\*putBlob)(OH\_VBucket \*bucket, const char \*field, const uint8\_t \*value, uint32\_t size)](#putblob) | Puts a const uint8\_t \* value into the **OH\_VBucket** object in the given column. |
| [int (\*putNull)(OH\_VBucket \*bucket, const char \*field)](#putnull) | Puts a null value into the **OH\_VBucket** object in the given column. |
| [int (\*clear)(OH\_VBucket \*bucket)](#clear) | Clears an **OH\_VBucket** object. |
| [int (\*destroy)(OH\_VBucket \*bucket)](#destroy) | Destroys an **OH\_VBucket** object and reclaims the memory occupied. |

#### \[h2\]Member Function Description

#### \[h2\]putText()

int (\*putText)(OH\_VBucket \*bucket, const char \*field, const char \*value)

**Description**

Puts a char\* value into the **OH\_VBucket** object in the given column.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VBucket \*bucket | Pointer to the **OH\_VBucket** instance. |
| const char \*field | Pointer to the column name in the database table. |
| const char \*value | Pointer to the value to put. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]putInt64()

int (\*putInt64)(OH\_VBucket \*bucket, const char \*field, int64\_t value)

**Description**

Puts an int64\_t value into the **OH\_VBucket** object in the given column.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VBucket \*bucket | Pointer to the **OH\_VBucket** instance. |
| const char \*field | Pointer to the column name in the database table. |
| int64\_t value | Pointer to the value to put. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]putReal()

int (\*putReal)(OH\_VBucket \*bucket, const char \*field, double value)

**Description**

Puts a double value into the **OH\_VBucket** object in the given column.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VBucket \*bucket | Pointer to the **OH\_VBucket** instance. |
| const char \*field | Pointer to the column name in the database table. |
| double value | Pointer to the value to put. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]putBlob()

int (\*putBlob)(OH\_VBucket \*bucket, const char \*field, const uint8\_t \*value, uint32\_t size)

**Description**

Puts a const uint8\_t \* value into the **OH\_VBucket** object in the given column.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VBucket \*bucket | Pointer to the **OH\_VBucket** instance. |
| const char \*field | Pointer to the column name in the database table. |
| const uint8\_t \*value | Pointer to the value to put. |
| uint32\_t size | Value length. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]putNull()

int (\*putNull)(OH\_VBucket \*bucket, const char \*field)

**Description**

Puts a null value into the **OH\_VBucket** object in the given column.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VBucket \*bucket | Pointer to the **OH\_VBucket** instance. |
| const char \*field | Pointer to the column name in the database table. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]clear()

int (\*clear)(OH\_VBucket \*bucket)

**Description**

Clears the [OH\_VBucket](#) object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VBucket \*bucket | Pointer to the **OH\_VBucket** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]destroy()

int (\*destroy)(OH\_VBucket \*bucket)

**Description**

Destroys the [OH\_VBucket](#) object and reclaims the memory occupied by the object.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_VBucket \*bucket | Pointer to the **OH\_VBucket** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |
