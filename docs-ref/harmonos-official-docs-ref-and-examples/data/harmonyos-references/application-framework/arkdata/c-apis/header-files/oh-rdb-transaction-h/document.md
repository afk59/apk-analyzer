# oh\_rdb\_transaction.h

#### Overview

Defines APIs and enums related to transactions.

**File to include**: <database/rdb/oh\_rdb\_transaction.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 18

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) | OH\_RDB\_TransOptions | Defines the [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) struct. |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) | OH\_Rdb\_Transaction | Defines the [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) struct. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_RDB\_TransType](#oh_rdb_transtype) | OH\_RDB\_TransType | Enumerates the transaction types of an RDB store. |

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_RDB\_TransOptions \*OH\_RdbTrans\_CreateOptions(void)](#oh_rdbtrans_createoptions) | Creates a **TransOptions** instance. |
| [int OH\_RdbTrans\_DestroyOptions(OH\_RDB\_TransOptions \*options)](#oh_rdbtrans_destroyoptions) | Destroys a **TransOptions** instance. |
| [int OH\_RdbTransOption\_SetType(OH\_RDB\_TransOptions \*options, OH\_RDB\_TransType type)](#oh_rdbtransoption_settype) | Sets the transaction type of an RDB store. |
| [int OH\_RdbTrans\_Commit(OH\_Rdb\_Transaction \*trans)](#oh_rdbtrans_commit) | Commits a transaction. |
| [int OH\_RdbTrans\_Rollback(OH\_Rdb\_Transaction \*trans)](#oh_rdbtrans_rollback) | Rolls back a transaction. |
| [int OH\_RdbTrans\_Insert(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row, int64\_t \*rowId)](#oh_rdbtrans_insert) | Inserts a row of data into a table. |
| [int OH\_RdbTrans\_InsertWithConflictResolution(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row,Rdb\_ConflictResolution resolution, int64\_t \*rowId)](#oh_rdbtrans_insertwithconflictresolution) | Inserts a row of data into a table with conflict resolutions. |
| [int OH\_RdbTrans\_BatchInsert(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_Data\_VBuckets \*rows,Rdb\_ConflictResolution resolution, int64\_t \*changes)](#oh_rdbtrans_batchinsert) | Inserts data into a table in batches. |
| [int OH\_RdbTrans\_Update(OH\_Rdb\_Transaction \*trans, const OH\_VBucket \*row, const OH\_Predicates \*predicates,int64\_t \*changes)](#oh_rdbtrans_update) | Updates data in an RDB store based on specified conditions. |
| [int OH\_RdbTrans\_UpdateWithConflictResolution(OH\_Rdb\_Transaction \*trans, const OH\_VBucket \*row,const OH\_Predicates \*predicates, Rdb\_ConflictResolution resolution, int64\_t \*changes)](#oh_rdbtrans_updatewithconflictresolution) | Updates data in the database based on specified conditions and supports conflict resolution. |
| [int OH\_RdbTrans\_Delete(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, int64\_t \*changes)](#oh_rdbtrans_delete) | Deletes data from the database based on specified conditions. |
| [OH\_Cursor \*OH\_RdbTrans\_Query(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, const char \*columns\[\],int len)](#oh_rdbtrans_query) | Queries data from the database based on specified conditions. |
| [OH\_Cursor \*OH\_RdbTrans\_QuerySql(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args)](#oh_rdbtrans_querysql) | Queries data from the database based on the SQL statement. |
| [int OH\_RdbTrans\_Execute(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result)](#oh_rdbtrans_execute) | Executes an SQL statement that contains specified parameters. |
| [int OH\_RdbTrans\_Destroy(OH\_Rdb\_Transaction \*trans)](#oh_rdbtrans_destroy) | Destroys a transaction object. |

#### Enum Description

#### \[h2\]OH\_RDB\_TransType

enum OH\_RDB\_TransType

**Description**

Enumerates the transaction types of an RDB store.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| RDB\_TRANS\_DEFERRED = 0 | Do not start any transaction before the database is accessed for the first time. |
| RDB\_TRANS\_IMMEDIATE | Start new writes without waiting for the write statement once the database is connected. |
| RDB\_TRANS\_EXCLUSIVE | 
Start the write transaction immediately, similar to **RDB\_TRANS\_IMMEDIATE**.

In WAL mode, **RDB\_TRANS\_EXCLUSIVE** is the same as **RDB\_TRANS\_IMMEDIATE**. In other log modes, **RDB\_TRANS\_EXCLUSIVE** prevents other database connections when the transaction is reading the database.

 |
| RDB\_TRANS\_BUTT | Maximum value of the RDB transaction type. |

#### Function Description

#### \[h2\]OH\_RdbTrans\_CreateOptions()

OH\_RDB\_TransOptions \*OH\_RdbTrans\_CreateOptions(void)

**Description**

Creates a transaction configuration object.

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) | 
Returns a pointer to the [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) instance if the operation is successful; returns **nullptr** otherwise.

Use [OH\_RdbTrans\_DestroyOptions](#oh_rdbtrans_destroyoptions) to release the memory in time.

 |

#### \[h2\]OH\_RdbTrans\_DestroyOptions()

int OH\_RdbTrans\_DestroyOptions(OH\_RDB\_TransOptions \*options)

**Description**

Destroys a **TransOptions** instance.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) \*options | Pointer to the [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_RdbTransOption\_SetType()

int OH\_RdbTransOption\_SetType(OH\_RDB\_TransOptions \*options, OH\_RDB\_TransType type)

**Description**

Sets the transaction type of an RDB store.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) \*options | Pointer to the [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) instance. |
| [OH\_RDB\_TransType](#oh_rdb_transtype) type | Transaction type to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_RdbTrans\_Commit()

int OH\_RdbTrans\_Commit(OH\_Rdb\_Transaction \*trans)

**Description**

Commits a transaction.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

 |

#### \[h2\]OH\_RdbTrans\_Rollback()

int OH\_RdbTrans\_Rollback(OH\_Rdb\_Transaction \*trans)

**Description**

Rolls back a transaction.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

 |

#### \[h2\]OH\_RdbTrans\_Insert()

int OH\_RdbTrans\_Insert(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row, int64\_t \*rowId)

**Description**

Inserts a row of data into a table.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const char \*table | Name of the target table. |
| const [OH\_VBucket](../../structs/oh-vbucket/document.md) \*row | Row of data to insert. |
| int64\_t \*rowId | Pointer to the row number returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default limit.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the size limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

 |

#### \[h2\]OH\_RdbTrans\_InsertWithConflictResolution()

int OH\_RdbTrans\_InsertWithConflictResolution(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row,Rdb\_ConflictResolution resolution, int64\_t \*rowId)

**Description**

Inserts a row of data into a table with conflict resolutions.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const char \*table | Name of the target table. |
| const [OH\_VBucket](../../structs/oh-vbucket/document.md) \*row | Row of data to insert. |
| Rdb\_ConflictResolution resolution | Policy used to resolve file conflicts. |
| int64\_t \*rowId | Pointer to the row number returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default limit.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the size limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

**RDB\_E\_SQLITE\_CONSTRAINT** indicates an SQLite error code: SQLite constraint.

 |

#### \[h2\]OH\_RdbTrans\_BatchInsert()

int OH\_RdbTrans\_BatchInsert(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_Data\_VBuckets \*rows, Rdb\_ConflictResolution resolution, int64\_t \*changes)

**Description**

Inserts data into a table in batches.

A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the error code **RDB\_E\_INVALID\_ARGS** is returned. The number of inserted data records multiplied by the size of the union set of all fields in the inserted data equals the number of parameters.

For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 32760).

Ensure that you comply with this constraint when calling this API to avoid errors caused by excessive parameters.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const char \*table | Name of the target table. |
| const [OH\_Data\_VBuckets](../../structs/oh-data-vbuckets/document.md) \*rows | An array of data to insert. |
| Rdb\_ConflictResolution resolution | Policy used to resolve file conflicts. |
| int64\_t \*changes | Pointer to the number of successful insertions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default limit.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the size limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

**RDB\_E\_SQLITE\_CONSTRAINT** indicates an SQLite error code: SQLite constraint.

 |

#### \[h2\]OH\_RdbTrans\_Update()

int OH\_RdbTrans\_Update(OH\_Rdb\_Transaction \*trans, const OH\_VBucket \*row, const OH\_Predicates \*predicates, int64\_t \*changes)

**Description**

Updates data in an RDB store based on specified conditions.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const [OH\_VBucket](../../structs/oh-vbucket/document.md) \*row | Row of data to update. |
| const [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the update conditions. |
| int64\_t \*changes | Pointer to the number of successful updates. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default limit.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the size limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

 |

#### \[h2\]OH\_RdbTrans\_UpdateWithConflictResolution()

int OH\_RdbTrans\_UpdateWithConflictResolution(OH\_Rdb\_Transaction \*trans, const OH\_VBucket \*row,const OH\_Predicates \*predicates, Rdb\_ConflictResolution resolution, int64\_t \*changes)

**Description**

Updates data in the database based on specified conditions and supports conflict resolution.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const [OH\_VBucket](../../structs/oh-vbucket/document.md) \*row | Row of data to update. |
| const [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the update conditions. |
| Rdb\_ConflictResolution resolution | Policy used to resolve file conflicts. |
| int64\_t \*changes | Pointer to the number of successful updates. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default limit.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the size limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

**RDB\_E\_SQLITE\_CONSTRAINT** indicates an SQLite error code: SQLite constraint.

 |

#### \[h2\]OH\_RdbTrans\_Delete()

int OH\_RdbTrans\_Delete(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, int64\_t \*changes)

**Description**

Deletes data from the database based on specified conditions.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the deletion conditions. |
| int64\_t \*changes | Pointer to the number of successful deletions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default limit.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the size limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

 |

#### \[h2\]OH\_RdbTrans\_Query()

OH\_Cursor \*OH\_RdbTrans\_Query(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, const char \*columns\[\], int len)

**Description**

Queries data from the database based on specified conditions.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the query conditions. |
| const char \*columns\[\] | Columns to query. If null is passed in, all columns are queried. |
| int len | Number of elements in a column. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) | Returns a pointer to the [OH\_Cursor](../../structs/oh-cursor/document.md) instance if the operation is successful; returns null if the database is closed or does not respond. |

#### \[h2\]OH\_RdbTrans\_QuerySql()

OH\_Cursor \*OH\_RdbTrans\_QuerySql(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args)

**Description**

Queries data from the database based on the SQL statement.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const char \*sql | Pointer to the SQL statement to execute. |
| const [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*args | Pointer to [OH\_Data\_Values](../../structs/oh-data-values/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) | Returns a pointer to the [OH\_Cursor](../../structs/oh-cursor/document.md) instance if the operation is successful; returns null if the database is closed or does not respond. |

#### \[h2\]OH\_RdbTrans\_Execute()

int OH\_RdbTrans\_Execute(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result)

**Description**

Executes an SQL statement that contains specified parameters.

Statements starting with comments are not supported.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |
| const char \*sql | Pointer to the SQL statement to execute. |
| const [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*args | Pointer to the parameters contained in the SQL statement. |
| OH\_Data\_Value \*\*result | Double pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance. After the execution is complete, you must release the memory by calling [OH\_Value\_Destroy](../oh-data-value-h/document.md#oh_value_destroy). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the execution result.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default limit.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the size limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

 |

#### \[h2\]OH\_RdbTrans\_Destroy()

int OH\_RdbTrans\_Destroy(OH\_Rdb\_Transaction \*trans)

**Description**

Destroys a transaction object.

**Since**: 18

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*trans | Pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code.

**RDB\_OK** indicates the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |
