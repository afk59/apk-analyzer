# OH\_Cursor

typedef struct {...} OH\_Cursor

#### Overview

Defines a struct for a result set. Provides APIs to access the result set obtained by querying the RDB store.

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [oh\_cursor.h](../../header-files/oh-cursor-h/document.md)

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int64\_t id | Unique identifier of the **OH\_Cursor** struct. |

#### \[h2\]Member Functions

| Name | Description |
| :-- | :-- |
| [int (\*getColumnCount)(OH\_Cursor \*cursor, int \*count)](#getcolumncount) | Pointer to the function used to obtain the number of columns in the result set. |
| [int (\*getColumnType)(OH\_Cursor \*cursor, int32\_t columnIndex, OH\_ColumnType \*columnType)](#getcolumntype) | Pointer to the function used to obtain the column type based on the specified column index. |
| [int (\*getColumnIndex)(OH\_Cursor \*cursor, const char \*name, int \*columnIndex)](#getcolumnindex) | Pointer to the function used to obtain the column index based on the specified column name. |
| [int (\*getColumnName)(OH\_Cursor \*cursor, int32\_t columnIndex, char \*name, int length)](#getcolumnname) | Pointer to the function used to obtain the column name based on the specified column index. |
| [int (\*getRowCount)(OH\_Cursor \*cursor, int \*count)](#getrowcount) | Pointer to the function used to obtain the number of rows in the result set. |
| [int (\*goToNextRow)(OH\_Cursor \*cursor)](#gotonextrow) | Pointer to the function used to go to the next row of the result set. |
| [int (\*getSize)(OH\_Cursor \*cursor, int32\_t columnIndex, size\_t \*size)](#getsize) | Pointer to the function used to obtain information about the memory required when the column data type in the result set is **BLOB** or **TEXT**. |
| [int (\*getText)(OH\_Cursor \*cursor, int32\_t columnIndex, char \*value, int length)](#gettext) | Pointer to the function used to obtain the value of the string type based on the specified column and the current row. |
| [int (\*getInt64)(OH\_Cursor \*cursor, int32\_t columnIndex, int64\_t \*value)](#getint64) | Pointer to the function used to obtain the value of the int64\_t type based on the specified column and the current row. |
| [int (\*getReal)(OH\_Cursor \*cursor, int32\_t columnIndex, double \*value)](#getreal) | Pointer to the function used to obtain the value of the double type based on the specified column and the current row. |
| [int (\*getBlob)(OH\_Cursor \*cursor, int32\_t columnIndex, unsigned char \*value, int length)](#getblob) | Pointer to the function used to obtain the values in the form of a byte array based on the specified column and the current row. |
| [int (\*isNull)(OH\_Cursor \*cursor, int32\_t columnIndex, bool \*isNull)](#isnull) | Pointer to the function used to check whether the value in the specified column is null. |
| [int (\*destroy)(OH\_Cursor \*cursor)](#destroy) | Pointer to the function used to destroy a result set. |
| [int (\*getAsset)(OH\_Cursor \*cursor, int32\_t columnIndex, Data\_Asset \*value)](#getasset) | Pointer to the function used to obtain the value of the asset type based on the specified column and the current row. |
| [int (\*getAssets)(OH\_Cursor \*cursor, int32\_t columnIndex, Data\_Asset \*\*value, uint32\_t \*length)](#getassets) | Pointer to the function used to obtain the values in the form of an asset array based on the specified column and the current row. |

#### Member Function Description

#### \[h2\]getColumnCount()

int (\*getColumnCount)(OH\_Cursor \*cursor, int \*count)

**Description**

Pointer to the function used to obtain the number of columns in the result set.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int \*count | Pointer to the number of columns in the result set obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getColumnType()

int (\*getColumnType)(OH\_Cursor \*cursor, int32\_t columnIndex, OH\_ColumnType \*columnType)

**Description**

Pointer to the function used to obtain the column type based on the specified column index.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| [OH\_ColumnType](../../header-files/oh-data-value-h/document.md#oh_columntype) \*columnType | Pointer to [OH\_ColumnType](../../header-files/oh-data-value-h/document.md#oh_columntype) of columns in the result set obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getColumnIndex()

int (\*getColumnIndex)(OH\_Cursor \*cursor, const char \*name, int \*columnIndex)

**Description**

Pointer to the function used to obtain the column index based on the specified column name.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| const char \*name | Column name. |
| int \*columnIndex | Pointer to the column index obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getColumnName()

 int (\*getColumnName)(OH\_Cursor \*cursor, int32\_t columnIndex, char \*name, int length)

**Description**

Pointer to the function used to obtain the column name based on the specified column index.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| char \*name | Pointer to the column name obtained. |
| int length | Total length of the column name obtained, including the terminator. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getRowCount()

int (\*getRowCount)(OH\_Cursor \*cursor, int \*count)

**Description**

Pointer to the function used to obtain the number of rows in the result set.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int \*count | Pointer to the number of columns in the result set obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]goToNextRow()

 int (\*goToNextRow)(OH\_Cursor \*cursor)

**Description**

Pointer to the function used to go to the next row of the result set.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getSize()

int (\*getSize)(OH\_Cursor \*cursor, int32\_t columnIndex, size\_t \*size)

**Description**

Pointer to the function used to obtain information about the memory required when the column data type in the result set is **BLOB** or **TEXT**.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| size\_t \*size | Pointer to the memory size obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getText()

int (\*getText)(OH\_Cursor \*cursor, int32\_t columnIndex, char \*value, int length)

**Description**

Pointer to the function used to obtain the value of the string type based on the specified column and the current row.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| char \*value | Pointer to the value of the string type obtained. |
| int length | Length of **value**, obtained by using **getSize**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getInt64()

int (\*getInt64)(OH\_Cursor \*cursor, int32\_t columnIndex, int64\_t \*value)

**Description**

Pointer to the function used to obtain the value of the int64\_t type based on the specified column and the current row.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| int64\_t \*value | Pointer to the value obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getReal()

int (\*getReal)(OH\_Cursor \*cursor, int32\_t columnIndex, double \*value)

**Description**

Pointer to the function used to obtain the value of the double type based on the specified column and the current row.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| double \*value | Pointer to the value obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getBlob()

int (\*getBlob)(OH\_Cursor \*cursor, int32\_t columnIndex, unsigned char \*value, int length)

**Description**

Pointer to the function used to obtain the values in the form of a byte array based on the specified column and the current row.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| unsigned char \*value | Pointer to the values in the form of a byte array obtained. |
| int length | Length of **value**, obtained by using **getSize**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]isNull()

int (\*isNull)(OH\_Cursor \*cursor, int32\_t columnIndex, bool \*isNull)

**Description**

Pointer to the function used to check whether the value in the specified column is null.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| bool \*isNull | Pointer to the value returned. The value **true** means the value is null; the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]destroy()

int (\*destroy)(OH\_Cursor \*cursor)

**Description**

Pointer to the function used to destroy a result set.

**Since**: 10

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getAsset()

int (\*getAsset)(OH\_Cursor \*cursor, int32\_t columnIndex, Data\_Asset \*value)

**Description**

Pointer to the function used to obtain the value of the asset type based on the specified column and the current row.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| Data\_Asset \*value | Pointer to the value obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |

#### \[h2\]getAssets()

int (\*getAssets)(OH\_Cursor \*cursor, int32\_t columnIndex, Data\_Asset \*\*value, uint32\_t \*length)

**Description**

Pointer to the function used to obtain the values in the form of an asset array based on the specified column and the current row.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_Cursor \*cursor | Pointer to the **OH\_Cursor** instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| Data\_Asset \*\*value | Double pointer to the value obtained. |
| uint32\_t \*length | Pointer to the length of the buffer, which is a variable of the uint32\_t type passed in. After the API is executed, the variable is updated to the length of the returned asset array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | Returns **RDB\_OK** if the operation is successful; returns an error code otherwise. |
