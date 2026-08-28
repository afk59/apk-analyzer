# oh\_cursor.h

#### Overview

Provides APIs to access the result set obtained by querying the RDB store. A result set is a set of results returned by **query()**.

**File to include**: <database/rdb/oh\_cursor.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) | OH\_Cursor | Provides APIs to access the result set obtained by querying the RDB store. A result set is a set of results returned by **query()**. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [int OH\_Cursor\_GetFloatVectorCount(OH\_Cursor \*cursor, int32\_t columnIndex, size\_t \*length)](#oh_cursor_getfloatvectorcount) | Obtains the length of a floating-point array in the specified column of the current row. |
| [int OH\_Cursor\_GetFloatVector(OH\_Cursor \*cursor, int32\_t columnIndex, float \*val, size\_t inLen, size\_t \*outLen)](#oh_cursor_getfloatvector) | Obtains the value in the specified column of the current row in the form of a floating-point array. |

#### Function Description

#### \[h2\]OH\_Cursor\_GetFloatVectorCount()

int OH\_Cursor\_GetFloatVectorCount(OH\_Cursor \*cursor, int32\_t columnIndex, size\_t \*length)

**Description**

Obtains the length of a floating-point array in the specified column of the current row.

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) \*cursor | Pointer to the [OH\_Cursor](../../structs/oh-cursor/document.md) instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| size\_t \*length | Pointer to the length of the float array obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_STEP\_RESULT\_CLOSED** indicates the result set is closed.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

 |

#### \[h2\]OH\_Cursor\_GetFloatVector()

int OH\_Cursor\_GetFloatVector(OH\_Cursor \*cursor, int32\_t columnIndex, float \*val, size\_t inLen, size\_t \*outLen)

**Description**

Obtains the value in the specified column of the current row in the form of a floating-point array.

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) \*cursor | Pointer to the [OH\_Cursor](../../structs/oh-cursor/document.md) instance. |
| int32\_t columnIndex | Index of the column, which starts from **0**. |
| float \*val | Ponter to the value obtained, in a float array. The caller needs to apply for the memory. |
| size\_t inLen | Length of the float array requested. |
| size\_t \*outLen | Pointer to the actual length of the float array. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an execution result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_STEP\_RESULT\_CLOSED** indicates the result set is closed.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

 |
