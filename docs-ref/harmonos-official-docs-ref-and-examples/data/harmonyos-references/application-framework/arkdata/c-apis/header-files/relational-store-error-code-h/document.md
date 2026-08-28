# relational\_store\_error\_code.h

#### Overview

Declares the error codes used for relational database (RDB) stores.

**File to include**: <database/rdb/relational\_store\_error\_code.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Rdb\_ErrCode](#oh_rdb_errcode) | OH\_Rdb\_ErrCode | Enumerates the RDB store error codes. |

#### Enum Description

#### \[h2\]OH\_Rdb\_ErrCode

enum OH\_Rdb\_ErrCode

**Description**

Enumerates the RDB store error codes.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| RDB\_ERR = -1 | Execution failed. |
| RDB\_OK = 0 | Execution successful. |
| E\_BASE = 14800000 | Base of the error code. |
| RDB\_E\_NOT\_SUPPORTED = 801 | The RDB store does not have this capability. |
| RDB\_E\_ERROR = E\_BASE | Common exception. |
| RDB\_E\_INVALID\_ARGS = (E\_BASE + 1) | Invalid parameter. |
| RDB\_E\_CANNOT\_UPDATE\_READONLY = (E\_BASE + 2) | Failed to update data because the RDB store is read-only. |
| RDB\_E\_REMOVE\_FILE = (E\_BASE + 3) | Failed to delete the file. |
| RDB\_E\_EMPTY\_TABLE\_NAME = (E\_BASE + 5) | The table name is empty. |
| RDB\_E\_EMPTY\_VALUES\_BUCKET = (E\_BASE + 6) | The content of the KV pair is empty. |
| RDB\_E\_EXECUTE\_IN\_STEP\_QUERY = (E\_BASE + 7) | The SQL statement executed during the query is incorrect. |
| RDB\_E\_INVALID\_COLUMN\_INDEX = (E\_BASE + 8) | The column index is invalid. |
| RDB\_E\_INVALID\_COLUMN\_TYPE = (E\_BASE + 9) | The column type is invalid. |
| RDB\_E\_EMPTY\_FILE\_NAME = (E\_BASE + 10) | The file name is empty. |
| RDB\_E\_INVALID\_FILE\_PATH = (E\_BASE + 11) | The file path is invalid. |
| RDB\_E\_TRANSACTION\_IN\_EXECUTE = (E\_BASE + 12) | Failed to start the transaction. |
| RDB\_E\_INVALID\_STATEMENT = (E\_BASE + 13) | Failed to precompile the SQL statements. |
| RDB\_E\_EXECUTE\_WRITE\_IN\_READ\_CONNECTION = (E\_BASE + 14) | Failed to perform a write operation in a read connection. |
| RDB\_E\_BEGIN\_TRANSACTION\_IN\_READ\_CONNECTION = (E\_BASE + 15) | Failed to start the transaction in a read connection. |
| RDB\_E\_NO\_TRANSACTION\_IN\_SESSION = (E\_BASE + 16) | The transaction to start does not exist in the database session. |
| RDB\_E\_MORE\_STEP\_QUERY\_IN\_ONE\_SESSION = (E\_BASE + 17) | Multiple queries are executed in a database session. |
| RDB\_E\_NO\_ROW\_IN\_QUERY = (E\_BASE + 18) | The result set does not contain any record. |
| RDB\_E\_INVALID\_BIND\_ARGS\_COUNT = (E\_BASE + 19) | The number of parameters bound in the SQL statement is invalid. |
| RDB\_E\_INVALID\_OBJECT\_TYPE = (E\_BASE + 20) | The object type is invalid. |
| RDB\_E\_INVALID\_CONFLICT\_FLAG = (E\_BASE + 21) | The conflict resolution type is invalid. |
| RDB\_E\_HAVING\_CLAUSE\_NOT\_IN\_GROUP\_BY = (E\_BASE + 22) | The **HAVING** keyword can be used only after **GROUP BY**. |
| RDB\_E\_NOT\_SUPPORTED\_BY\_STEP\_RESULT\_SET = (E\_BASE + 23) | The result set by step is not supported. |
| RDB\_E\_STEP\_RESULT\_SET\_CROSS\_THREADS = (E\_BASE + 24) | Failed to obtain the result set. |
| RDB\_E\_STEP\_RESULT\_QUERY\_NOT\_EXECUTED = (E\_BASE + 25) | The result set query statement is not executed. |
| RDB\_E\_STEP\_RESULT\_IS\_AFTER\_LAST = (E\_BASE + 26) | The pointer of the result set is already in the last row. |
| RDB\_E\_STEP\_RESULT\_QUERY\_EXCEEDED = (E\_BASE + 27) | The number of result set query times exceeds the limit. |
| RDB\_E\_STATEMENT\_NOT\_PREPARED = (E\_BASE + 28) | The SQL statement is not precompiled. |
| RDB\_E\_EXECUTE\_RESULT\_INCORRECT = (E\_BASE + 29) | The database execution result is incorrect. |
| RDB\_E\_STEP\_RESULT\_CLOSED = (E\_BASE + 30) | The result set has been closed. |
| RDB\_E\_RELATIVE\_PATH = (E\_BASE + 31) | The file path is a relative path. |
| RDB\_E\_EMPTY\_NEW\_ENCRYPT\_KEY = (E\_BASE + 32) | The new encrypt key is empty. |
| RDB\_E\_CHANGE\_UNENCRYPTED\_TO\_ENCRYPTED = (E\_BASE + 33) | The RDB store is non-encrypted and cannot be changed. |
| RDB\_E\_CHANGE\_ENCRYPT\_KEY\_IN\_BUSY = (E\_BASE + 34) | The database does not respond when the database key is updated. |
| RDB\_E\_STEP\_STATEMENT\_NOT\_INIT = (E\_BASE + 35) | The precompiled SQL statement is not initialized. |
| RDB\_E\_NOT\_SUPPORTED\_ATTACH\_IN\_WAL\_MODE = (E\_BASE + 36) | The WAL mode does not support the ATTACH operation. |
| RDB\_E\_CREATE\_FOLDER\_FAIL = (E\_BASE + 37) | Failed to create the folder. |
| RDB\_E\_SQLITE\_SQL\_BUILDER\_NORMALIZE\_FAIL = (E\_BASE + 38) | Failed to build the SQL statement. |
| RDB\_E\_STORE\_SESSION\_NOT\_GIVE\_CONNECTION\_TEMPORARILY = (E\_BASE + 39) | The database session does not provide a connection. |
| RDB\_E\_STORE\_SESSION\_NO\_CURRENT\_TRANSACTION = (E\_BASE + 40) | The transaction does not exist in the database session. |
| RDB\_E\_NOT\_SUPPORT = (E\_BASE + 41) | The current operation is not supported. |
| RDB\_E\_INVALID\_PARCEL = (E\_BASE + 42) | The current PARCEL is invalid. |
| RDB\_E\_QUERY\_IN\_EXECUTE = (E\_BASE + 43) | Failed to execute query. |
| RDB\_E\_SET\_PERSIST\_WAL = (E\_BASE + 44) | Failed to set the persistence of the database file in WAL mode. |
| RDB\_E\_DB\_NOT\_EXIST = (E\_BASE + 45) | The database does not exist. |
| RDB\_E\_ARGS\_READ\_CON\_OVERLOAD = (E\_BASE + 46) | The number of read connections to set is greater than the limit. |
| RDB\_E\_WAL\_SIZE\_OVER\_LIMIT = (E\_BASE + 47) | The WAL log file size exceeds the default value. |
| RDB\_E\_CON\_OVER\_LIMIT = (E\_BASE + 48) | The number of database connections has reached the limit. |
| RDB\_E\_ALREADY\_CLOSED = (E\_BASE + 50) | 
The RDB store is already closed.

**Since**: 18

 |
| RDB\_E\_DATABASE\_BUSY = (E\_BASE + 51) | 

The database does not respond.

**Since**: 18

 |
| RDB\_E\_SQLITE\_CORRUPT = (E\_BASE + 52) | 

The database is corrupted.

**Since**: 18

 |
| RDB\_E\_SQLITE\_PERM = (E\_BASE + 53) | 

SQLite: access denied.

**Since**: 18

 |
| RDB\_E\_SQLITE\_BUSY = (E\_BASE + 54) | 

SQLite: database file locked.

**Since**: 18

 |
| RDB\_E\_SQLITE\_LOCKED = (E\_BASE + 55) | 

SQLite: database table locked.

**Since**: 18

 |
| RDB\_E\_SQLITE\_NOMEM = (E\_BASE + 56) | 

SQLite: insufficient database memory.

**Since**: 18

 |
| RDB\_E\_SQLITE\_READONLY = (E\_BASE + 57) | 

SQLite: attempt to write a read-only database.

**Since**: 18

 |
| RDB\_E\_SQLITE\_IOERR = (E\_BASE + 58) | 

SQLite: disk I/O error.

**Since**: 18

 |
| RDB\_E\_SQLITE\_FULL = (E\_BASE + 59) | 

SQLite: database is full.

**Since**: 18

 |
| RDB\_E\_SQLITE\_CANT\_OPEN = (E\_BASE + 60) | 

SQLite: unable to open the database file.

**Since**: 18

 |
| RDB\_E\_SQLITE\_TOO\_BIG = (E\_BASE + 61) | 

SQLite: TEXT or BLOB exceeds the limit.

**Since**: 18

 |
| RDB\_E\_SQLITE\_MISMATCH = (E\_BASE + 62) | 

SQLite: data types mismatch.

**Since**: 18

 |
| RDB\_E\_DATA\_TYPE\_NULL = (E\_BASE + 63) | 

The data to be stored is empty.

**Since**: 18

 |
| RDB\_E\_TYPE\_MISMATCH = (E\_BASE + 64) | 

The data type is incorrect.

**Since**: 18

 |
| RDB\_E\_SQLITE\_CONSTRAINT = (E\_BASE + 65) | 

SQLite error code: SQLite constraint.

**Since**: 18

 |
| RDB\_E\_SUB\_LIMIT\_REACHED = (E\_BASE + 66) | 

The number of subscriptions exceeds the upper limit.

**Since**: 22

 |
