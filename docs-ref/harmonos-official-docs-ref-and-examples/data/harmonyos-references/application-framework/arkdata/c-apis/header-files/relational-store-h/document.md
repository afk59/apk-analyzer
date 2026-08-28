# relational\_store.h

#### Overview

Provides APIs for managing data in an RDB store. The APIs not marked as supporting vector stores are available only to RDB stores.

**File to include**: <database/rdb/relational\_store.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 10

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Rdb\_Config](../../structs/oh-rdb-config/document.md) | OH\_Rdb\_Config | Defines the configuration of an RDB store. |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) | OH\_Rdb\_Store | Defines the RDB store type. |
| [Rdb\_DistributedConfig](../../structs/rdb-distributedconfig/document.md) | Rdb\_DistributedConfig | Defines a struct for distributed configuration of a table. |
| [Rdb\_KeyInfo](../../structs/rdb-keyinfo/document.md) | Rdb\_KeyInfo | Defines a struct for the primary key or number of the row that changes. |
| [Rdb\_KeyData](../../structs/rdb-keydata/document.md) | \- | Stores the changed data. |
| [Rdb\_ChangeInfo](../../structs/rdb-changeinfo/document.md) | Rdb\_ChangeInfo | Defines a struct for the details about the device-cloud sync process. |
| [Rdb\_SubscribeCallback](../../structs/rdb-subscribecallback/document.md) | Rdb\_SubscribeCallback | Defines a callback used to return the subscribed event. |
| [Rdb\_DataObserver](../../structs/rdb-dataobserver/document.md) | Rdb\_DataObserver | Defines a struct for the data observer. |
| [Rdb\_Statistic](../../structs/rdb-statistic/document.md) | Rdb\_Statistic | Defines a struct for the device-cloud sync statistics of a database table. |
| [Rdb\_TableDetails](../../structs/rdb-tabledetails/document.md) | Rdb\_TableDetails | Defines a struct for statistics of device-cloud upload and download tasks of a database table. |
| [Rdb\_ProgressDetails](../../structs/rdb-progressdetails/document.md) | Rdb\_ProgressDetails | Defines a struct for statistics of the overall device-cloud sync (upload and download) tasks of an RDB store. |
| [Rdb\_ProgressObserver](../../structs/rdb-progressobserver/document.md) | Rdb\_ProgressObserver | Defines the observer of the device-cloud sync progress. |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) | OH\_Rdb\_ConfigV2 | Defines a struct for the RDB store configuration. Different from [OH\_Rdb\_Config](../../structs/oh-rdb-config/document.md), this struct does not expose its member variables externally. Methods are used to configure the properties of this struct. It supports vector stores. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Rdb\_SecurityLevel](#oh_rdb_securitylevel) | OH\_Rdb\_SecurityLevel | Enumerates the RDB store security levels. |
| [Rdb\_SecurityArea](#rdb_securityarea) | Rdb\_SecurityArea | Enumerates the encryption levels of database files. |
| [Rdb\_DBType](#rdb_dbtype) | Rdb\_DBType | Enumerates the database kernel types. |
| [Rdb\_Tokenizer](#rdb_tokenizer) | Rdb\_Tokenizer | Enumerates the database tokenizer types. |
| [Rdb\_DistributedType](#rdb_distributedtype) | Rdb\_DistributedType | Enumerates the distributed types. |
| [Rdb\_ChangeType](#rdb_changetype) | Rdb\_ChangeType | Enumerates the data change types. |
| [Rdb\_SubscribeType](#rdb_subscribetype) | Rdb\_SubscribeType | Enumerates the subscription types. |
| [Rdb\_SyncMode](#rdb_syncmode) | Rdb\_SyncMode | Enumerates the RDB sync modes. |
| [Rdb\_Progress](#rdb_progress) | Rdb\_Progress | Enumerates the device-cloud sync progress states. |
| [Rdb\_ProgressCode](#rdb_progresscode) | Rdb\_ProgressCode | Enumerates the device-cloud sync states. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_Rdb\_ConfigV2 \*OH\_Rdb\_CreateConfig()](#oh_rdb_createconfig) | \- | Creates an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_DestroyConfig(OH\_Rdb\_ConfigV2 \*config)](#oh_rdb_destroyconfig) | \- | Destroys an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance created by [OH\_Rdb\_CreateConfig](#oh_rdb_createconfig). |
| [int OH\_Rdb\_SetDatabaseDir(OH\_Rdb\_ConfigV2 \*config, const char \*databaseDir)](#oh_rdb_setdatabasedir) | \- | Sets the database file path for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_SetStoreName(OH\_Rdb\_ConfigV2 \*config, const char \*storeName)](#oh_rdb_setstorename) | \- | Sets the database name for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_SetBundleName(OH\_Rdb\_ConfigV2 \*config, const char \*bundleName)](#oh_rdb_setbundlename) | \- | Sets the bundle name for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_SetModuleName(OH\_Rdb\_ConfigV2 \*config, const char \*moduleName)](#oh_rdb_setmodulename) | \- | Sets the module name for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_SetEncrypted(OH\_Rdb\_ConfigV2 \*config, bool isEncrypted)](#oh_rdb_setencrypted) | \- | Sets whether to encrypt the database for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_SetSecurityLevel(OH\_Rdb\_ConfigV2 \*config, int securityLevel)](#oh_rdb_setsecuritylevel) | \- | Sets the database security level ([OH\_Rdb\_SecurityLevel](#oh_rdb_securitylevel)) for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_SetArea(OH\_Rdb\_ConfigV2 \*config, int area)](#oh_rdb_setarea) | \- | Sets the security area level ([Rdb\_SecurityArea](#rdb_securityarea)) for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_SetDbType(OH\_Rdb\_ConfigV2 \*config, int dbType)](#oh_rdb_setdbtype) | \- | Sets the database type ([Rdb\_DBType](#rdb_dbtype)) for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| [int OH\_Rdb\_SetCustomDir(OH\_Rdb\_ConfigV2 \*config, const char \*customDir)](#oh_rdb_setcustomdir) | \- | Sets the custom directory of the database. |
| [int OH\_Rdb\_SetReadOnly(OH\_Rdb\_ConfigV2 \*config, bool readOnly)](#oh_rdb_setreadonly) | \- | Sets whether the RDB store is in read-only mode. |
| [int OH\_Rdb\_SetPlugins(OH\_Rdb\_ConfigV2 \*config, const char \*\*plugins, int32\_t length)](#oh_rdb_setplugins) | \- | Sets the dynamic library with specific capabilities (such as full-text search). |
| [int OH\_Rdb\_SetCryptoParam(OH\_Rdb\_ConfigV2 \*config, const OH\_Rdb\_CryptoParam \*cryptoParam)](#oh_rdb_setcryptoparam) | \- | Sets custom encryption parameters. |
| [int OH\_Rdb\_IsTokenizerSupported(Rdb\_Tokenizer tokenizer, bool \*isSupported)](#oh_rdb_istokenizersupported) | \- | Checks whether the specified tokenizer is supported. |
| [int OH\_Rdb\_SetTokenizer(OH\_Rdb\_ConfigV2 \*config, Rdb\_Tokenizer tokenizer)](#oh_rdb_settokenizer) | \- | Sets the tokenizer type. |
| [int OH\_Rdb\_SetPersistent(OH\_Rdb\_ConfigV2 \*config, bool isPersistent)](#oh_rdb_setpersistent) | \- | Sets whether to persist an RDB store. |
| [const int \*OH\_Rdb\_GetSupportedDbType(int \*typeCount)](#oh_rdb_getsupporteddbtype) | \- | Obtains the supported database type ([Rdb\_DBType](#rdb_dbtype)). |
| [OH\_VObject \*OH\_Rdb\_CreateValueObject()](#oh_rdb_createvalueobject) | \- | Creates an [OH\_VObject](../../structs/oh-vobject/document.md) instance. |
| [OH\_VBucket \*OH\_Rdb\_CreateValuesBucket()](#oh_rdb_createvaluesbucket) | \- | Creates an [OH\_VBucket](../../structs/oh-vbucket/document.md) instance. |
| [OH\_Predicates \*OH\_Rdb\_CreatePredicates(const char \*table)](#oh_rdb_createpredicates) | \- | Creates an [OH\_Predicates](../../structs/oh-predicates/document.md) instance. |
| [OH\_Rdb\_Store \*OH\_Rdb\_GetOrOpen(const OH\_Rdb\_Config \*config, int \*errCode)](#oh_rdb_getoropen) | \- | Obtains a related [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance to operate the RDB store. |
| [OH\_Rdb\_Store \*OH\_Rdb\_CreateOrOpen(const OH\_Rdb\_ConfigV2 \*config, int \*errCode)](#oh_rdb_createoropen) | \- | Creates or opens an [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance based on the given [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md). |
| [int OH\_Rdb\_CloseStore(OH\_Rdb\_Store \*store)](#oh_rdb_closestore) | \- | Closes an [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) object and reclaims the memory occupied by the object. |
| [int OH\_Rdb\_DeleteStore(const OH\_Rdb\_Config \*config)](#oh_rdb_deletestore) | \- | Deletes an RDB store with the specified configuration. |
| [int OH\_Rdb\_DeleteStoreV2(const OH\_Rdb\_ConfigV2 \*config)](#oh_rdb_deletestorev2) | \- | 
Deletes an RDB store based on the given [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md).

Before calling **DeleteStoreV2**, ensure that the **OH\_Rdb\_Store** and **OH\_Cursor** of the vector store have been closed.

 |
| [int OH\_Rdb\_Insert(OH\_Rdb\_Store \*store, const char \*table, OH\_VBucket \*valuesBucket)](#oh_rdb_insert) | \- | Inserts a row of data into a table. |
| [int OH\_Rdb\_InsertWithConflictResolution(OH\_Rdb\_Store \*store, const char \*table, OH\_VBucket \*row,Rdb\_ConflictResolution resolution, int64\_t \*rowId)](#oh_rdb_insertwithconflictresolution) | \- | Inserts a row of data into the target table and supports conflict resolution. |
| [int OH\_Rdb\_BatchInsert(OH\_Rdb\_Store \*store, const char \*table,const OH\_Data\_VBuckets \*rows, Rdb\_ConflictResolution resolution, int64\_t \*changes)](#oh_rdb_batchinsert) | \- | Inserts data into a table in batches. |
| [int OH\_Rdb\_Update(OH\_Rdb\_Store \*store, OH\_VBucket \*valuesBucket, OH\_Predicates \*predicates)](#oh_rdb_update) | \- | Updates data in an RDB store based on specified conditions. |
| [int OH\_Rdb\_UpdateWithConflictResolution(OH\_Rdb\_Store \*store, OH\_VBucket \*row, OH\_Predicates \*predicates,Rdb\_ConflictResolution resolution, int64\_t \*changes)](#oh_rdb_updatewithconflictresolution) | \- | Updates data in the database based on specified conditions and supports conflict resolution. |
| [int OH\_Rdb\_Delete(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates)](#oh_rdb_delete) | \- | Deletes data from an RDB store based on specified conditions. |
| [OH\_Cursor \*OH\_Rdb\_Query(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates, const char \*const \*columnNames, int length)](#oh_rdb_query) | \- | Queries data in an RDB store based on specified conditions. |
| [int OH\_Rdb\_Execute(OH\_Rdb\_Store \*store, const char \*sql)](#oh_rdb_execute) | \- | Executes an SQL statement that returns no value. |
| [int OH\_Rdb\_ExecuteV2(OH\_Rdb\_Store \*store, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result)](#oh_rdb_executev2) | \- | Executes an SQL statement with a return value. This API supports vector stores. |
| [int OH\_Rdb\_ExecuteByTrxId(OH\_Rdb\_Store \*store, int64\_t trxId, const char \*sql)](#oh_rdb_executebytrxid) | \- | Executes an SQL statement that returns no value based on the specified transaction ID. This API supports only vector stores. |
| [OH\_Cursor \*OH\_Rdb\_ExecuteQuery(OH\_Rdb\_Store \*store, const char \*sql)](#oh_rdb_executequery) | \- | Queries data in the database using the specified SQL statement. This API supports vector stores. |
| [OH\_Cursor \*OH\_Rdb\_ExecuteQueryV2(OH\_Rdb\_Store \*store, const char \*sql, const OH\_Data\_Values \*args)](#oh_rdb_executequeryv2) | \- | Queries data in the database using the specified SQL statement. This API supports vector stores. |
| [int OH\_Rdb\_BeginTransaction(OH\_Rdb\_Store \*store)](#oh_rdb_begintransaction) | \- | Begins the transaction before executing SQL statements. |
| [int OH\_Rdb\_RollBack(OH\_Rdb\_Store \*store)](#oh_rdb_rollback) | \- | Rolls back the SQL statements executed. |
| [int OH\_Rdb\_Commit(OH\_Rdb\_Store \*store)](#oh_rdb_commit) | \- | Commits the executed SQL statement. |
| [int OH\_Rdb\_BeginTransWithTrxId(OH\_Rdb\_Store \*store, int64\_t \*trxId)](#oh_rdb_begintranswithtrxid) | \- | Begins a transaction. This API returns a transaction ID API and supports only vector stores. |
| [int OH\_Rdb\_RollBackByTrxId(OH\_Rdb\_Store \*store, int64\_t trxId)](#oh_rdb_rollbackbytrxid) | \- | Rolls back the executed SQL statements based on the specified transaction ID. This API supports only vector stores. |
| [int OH\_Rdb\_CommitByTrxId(OH\_Rdb\_Store \*store, int64\_t trxId)](#oh_rdb_commitbytrxid) | \- | Commits the executed SQL statements based on the specified transaction ID. This API supports only vector stores. |
| [int OH\_Rdb\_Backup(OH\_Rdb\_Store \*store, const char \*databasePath)](#oh_rdb_backup) | \- | Backs up an RDB store using the backup file of the specified path. This API supports vector stores. |
| [int OH\_Rdb\_Restore(OH\_Rdb\_Store \*store, const char \*databasePath)](#oh_rdb_restore) | \- | Restores a database from a specified database backup file. This API supports vector stores. |
| [int OH\_Rdb\_GetVersion(OH\_Rdb\_Store \*store, int \*version)](#oh_rdb_getversion) | \- | Obtains the RDB store version. |
| [int OH\_Rdb\_SetVersion(OH\_Rdb\_Store \*store, int version)](#oh_rdb_setversion) | \- | Sets the RDB store version. |
| [int OH\_Rdb\_SetDistributedTables(OH\_Rdb\_Store \*store, const char \*tables\[\], uint32\_t count, Rdb\_DistributedType type,const Rdb\_DistributedConfig \*config)](#oh_rdb_setdistributedtables) | \- | Sets distributed database tables. |
| [OH\_Cursor \*OH\_Rdb\_FindModifyTime(OH\_Rdb\_Store \*store, const char \*tableName, const char \*columnName,OH\_VObject \*values)](#oh_rdb_findmodifytime) | \- | Obtains the last modification time of a table in an RDB store. |
| [typedef void (\*Rdb\_BriefObserver)(void \*context, const char \*values\[\], uint32\_t count)](#rdb_briefobserver) | Rdb\_BriefObserver | Defines a callback used to return the device-cloud data change event. |
| [typedef void (\*Rdb\_DetailsObserver)(void \*context, const Rdb\_ChangeInfo \*\*changeInfo, uint32\_t count)](#rdb_detailsobserver) | Rdb\_DetailsObserver | Defines a callback used to return the details about the device-cloud data change. |
| [int OH\_Rdb\_Subscribe(OH\_Rdb\_Store \*store, Rdb\_SubscribeType type, const Rdb\_DataObserver \*observer)](#oh_rdb_subscribe) | \- | Registers an observer for an RDB store. The registered callback will be invoked when data in a distributed or local RDB store changes. |
| [int OH\_Rdb\_Unsubscribe(OH\_Rdb\_Store \*store, Rdb\_SubscribeType type, const Rdb\_DataObserver \*observer)](#oh_rdb_unsubscribe) | \- | Unregisters the observer of the specified type. |
| [Rdb\_TableDetails \*OH\_Rdb\_GetTableDetails(Rdb\_ProgressDetails \*progress, int32\_t version)](#oh_rdb_gettabledetails) | \- | Obtains the device-cloud sync statistics of a table. |
| [typedef void (\*Rdb\_ProgressCallback)(void \*context, Rdb\_ProgressDetails \*progressDetails)](#rdb_progresscallback) | Rdb\_ProgressCallback | Defines a callback used to return the device-cloud sync progress. |
| [typedef void (\*Rdb\_SyncCallback)(Rdb\_ProgressDetails \*progressDetails)](#rdb_synccallback) | Rdb\_SyncCallback | Defines a callback for device-cloud sync. |
| [int OH\_Rdb\_CloudSync(OH\_Rdb\_Store \*store, Rdb\_SyncMode mode, const char \*tables\[\], uint32\_t count,const Rdb\_ProgressObserver \*observer)](#oh_rdb_cloudsync) | \- | Performs device-cloud sync. |
| [int OH\_Rdb\_SubscribeAutoSyncProgress(OH\_Rdb\_Store \*store, const Rdb\_ProgressObserver \*observer)](#oh_rdb_subscribeautosyncprogress) | \- | 

Subscribes to the auto sync progress of an RDB store.

The registered callback will be invoked to return the auto sync progress.

 |
| [int OH\_Rdb\_UnsubscribeAutoSyncProgress(OH\_Rdb\_Store \*store, const Rdb\_ProgressObserver \*observer)](#oh_rdb_unsubscribeautosyncprogress) | \- | Unsubscribes from the auto sync process of an RDB store. |
| [int OH\_Rdb\_LockRow(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates)](#oh_rdb_lockrow) | \- | Locks data in an RDB store based on specified conditions. The locked data will be blocked from the device-cloud sync. |
| [int OH\_Rdb\_UnlockRow(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates)](#oh_rdb_unlockrow) | \- | Unlocks data in an RDB store based on specified conditions. |
| [OH\_Cursor \*OH\_Rdb\_QueryLockedRow(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates, const char \*const \*columnNames, int length)](#oh_rdb_querylockedrow) | \- | Queries the locked data in an RDB store. |
| [int OH\_Rdb\_CreateTransaction(OH\_Rdb\_Store \*store, const OH\_RDB\_TransOptions \*options, OH\_Rdb\_Transaction \*\*trans)](#oh_rdb_createtransaction) | \- | Creates a transaction object. |
| [int OH\_Rdb\_Attach(OH\_Rdb\_Store \*store, const OH\_Rdb\_ConfigV2 \*config, const char \*attachName, int64\_t waitTime,size\_t \*attachedNumber)](#oh_rdb_attach) | \- | Attaches a database file to the database that is currently connected. |
| [int OH\_Rdb\_Detach(OH\_Rdb\_Store \*store, const char \*attachName, int64\_t waitTime, size\_t \*attachedNumber)](#oh_rdb_detach) | \- | Detaches a specified store from the current database. |
| [int OH\_Rdb\_SetLocale(OH\_Rdb\_Store \*store, const char \*locale)](#oh_rdb_setlocale) | \- | Sets locale. |
| [int OH\_Rdb\_SetSemanticIndex(OH\_Rdb\_ConfigV2 \*config, bool enableSemanticIndex)](#oh_rdb_setsemanticindex) | \- | Sets whether to enable knowledge processing based on semantic indexes. |
| [int OH\_Rdb\_RekeyEx(OH\_Rdb\_Store \*store, OH\_Rdb\_CryptoParam \*param)](#oh_rdb_rekeyex) | \- | 

Changes the key used to encrypt the database.

Key update is not supported for databases in non-WAL mode.

Manual update requires exclusive access to the database. If any result set, transaction, or database opened by another process is not released, the update will fail.

Parameter update for an encrypted database and conversion between an encrypted database and a non-encrypted database are supported.

The larger the database, the longer the update takes.

Exercise caution when changing the encryption parameters. The correct encryption parameters must be passed when **OH\_Rdb\_CreateOrOpen** is called. Otherwise, the database may fail to be opened.

 |
| [typedef void (\*Rdb\_CorruptedHandler)(void \*context, OH\_Rdb\_ConfigV2 \*config, OH\_Rdb\_Store \*store)](#rdb_corruptedhandler) | Rdb\_CorruptedHandler | Defines a handler for processing database exceptions. |
| [int OH\_Rdb\_RegisterCorruptedHandler(const OH\_Rdb\_ConfigV2 \*config, void \*context, const Rdb\_CorruptedHandler handler)](#oh_rdb_registercorruptedhandler) | \- | 

Registers a handler for processing database exceptions. When a database exception occurs, this handler is called.

The exception handling logic is user-defined. You should ensure the service quality each time the callback is triggered.

Only one handler can be registered for each path.

 |
| [int OH\_Rdb\_UnregisterCorruptedHandler(const OH\_Rdb\_ConfigV2 \*config, void \*context, const Rdb\_CorruptedHandler handler)](#oh_rdb_unregistercorruptedhandler) | \- | 

Unregisters the handler for processing database exceptions.

The handler and context must be the same as those during subscription. Otherwise, the operation fails.

 |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| DISTRIBUTED\_CONFIG\_VERSION 1 | 
Describes the version of [Rdb\_DistributedConfig](../../structs/rdb-distributedconfig/document.md).

**Since**: 11

 |
| DISTRIBUTED\_CHANGE\_INFO\_VERSION 1 | 

Describes the version of [Rdb\_ChangeInfo](../../structs/rdb-changeinfo/document.md).

**Since**: 11

 |
| DISTRIBUTED\_PROGRESS\_DETAIL\_VERSION 1 | 

Describes the version of [Rdb\_ProgressDetails](../../structs/rdb-progressdetails/document.md).

**Since**: 11

 |

#### Enum Description

#### \[h2\]OH\_Rdb\_SecurityLevel

enum OH\_Rdb\_SecurityLevel

**Description**

Enumerates the RDB store security levels.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| S1 = 1 | Low security level. If data leakage occurs, minor impact will be caused. |
| S2 | Medium security level. If data leakage occurs, moderate impact will be caused. |
| S3 | High security level. If data leakage occurs, major impact will be caused. |
| S4 | Critical security level. If data leakage occurs, critical impact will be caused. |

#### \[h2\]Rdb\_SecurityArea

enum Rdb\_SecurityArea

**Description**

Enumerates the encryption levels of database files.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| RDB\_SECURITY\_AREA\_EL1 = 1 | Encryption level 1. |
| RDB\_SECURITY\_AREA\_EL2 | Encryption level 2. |
| RDB\_SECURITY\_AREA\_EL3 | Encryption level 3. |
| RDB\_SECURITY\_AREA\_EL4 | Encryption level 4. |
| RDB\_SECURITY\_AREA\_EL5 | 
Encryption level 5.

**Since**: 12

 |

#### \[h2\]Rdb\_DBType

enum Rdb\_DBType

**Description**

Enumerates the database kernel types.

**Since**: 14

| Enum Item | Description |
| :-- | :-- |
| RDB\_SQLITE = 1 | SQLite is used as the database kernel. |
| RDB\_CAYLEY = 2 | Cayley is used as the database kernel. |
| DBTYPE\_BUTT = 64 | Maximum value of the database kernel type, which is an invalid value. |

#### \[h2\]Rdb\_Tokenizer

enum Rdb\_Tokenizer

**Description**

Enumerates the database tokenizer types.

**Since**: 17

| Enum Item | Description |
| :-- | :-- |
| RDB\_NONE\_TOKENIZER = 1 | No tokenizer is used. |
| RDB\_ICU\_TOKENIZER = 2 | ICU tokenizer. |
| RDB\_CUSTOM\_TOKENIZER = 3 | 
Custom tokenizer.

**Since**: 18

 |

#### \[h2\]Rdb\_DistributedType

enum Rdb\_DistributedType

**Description**

Enumerates the distributed types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| RDB\_DISTRIBUTED\_CLOUD | Distributed database tables for device-cloud sync. |

#### \[h2\]Rdb\_ChangeType

enum Rdb\_ChangeType

**Description**

Enumerates the data change types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| RDB\_DATA\_CHANGE | Data change. |
| RDB\_ASSET\_CHANGE | Asset change. |

#### \[h2\]Rdb\_SubscribeType

enum Rdb\_SubscribeType

**Description**

Enumerates the subscription types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| RDB\_SUBSCRIBE\_TYPE\_CLOUD | Subscribe to cloud data changes. |
| RDB\_SUBSCRIBE\_TYPE\_CLOUD\_DETAILS | Subscribe to detailed information about cloud data changes. |
| RDB\_SUBSCRIBE\_TYPE\_LOCAL\_DETAILS | 
Subscribe to detailed information about local data changes.

**Since**: 12

 |

#### \[h2\]Rdb\_SyncMode

enum Rdb\_SyncMode

**Description**

Sync mode of the database.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| RDB\_SYNC\_MODE\_TIME\_FIRST | Synchronize with the data with the latest modification time. |
| RDB\_SYNC\_MODE\_NATIVE\_FIRST | Synchronize data from a local device to the cloud. |
| RDB\_SYNC\_MODE\_CLOUD\_FIRST | Synchronize data from the cloud to a local device. |

#### \[h2\]Rdb\_Progress

enum Rdb\_Progress

**Description**

Enumerates the device-cloud sync progress states.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| RDB\_SYNC\_BEGIN | The device-cloud sync starts. |
| RDB\_SYNC\_IN\_PROGRESS | The device-cloud sync is in progress. |
| RDB\_SYNC\_FINISH | The device-cloud sync is finished. |

#### \[h2\]Rdb\_ProgressCode

enum Rdb\_ProgressCode

**Description**

Enumerates the device-cloud sync states.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| RDB\_SUCCESS | The device-cloud sync is successful. |
| RDB\_UNKNOWN\_ERROR | An unknown error occurs during the device-cloud sync. |
| RDB\_NETWORK\_ERROR | A network error occurs during the device-cloud sync. |
| RDB\_CLOUD\_DISABLED | The cloud is unavailable. |
| RDB\_LOCKED\_BY\_OTHERS | The device-cloud sync of another device is being performed. |
| RDB\_RECORD\_LIMIT\_EXCEEDED | The number of records or size of the data to be synced exceeds the maximum. The maximum value is configured on the cloud. |
| RDB\_NO\_SPACE\_FOR\_ASSET | The remaining cloud space is less than the size of the data to be synced. |

#### Function Description

#### \[h2\]OH\_Rdb\_SetSemanticIndex()

int OH\_Rdb\_SetSemanticIndex(OH\_Rdb\_ConfigV2 \*config, bool enableSemanticIndex)

**Description**

Sets whether to enable knowledge processing based on semantic indexes.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| bool enableSemanticIndex | 
Whether to enable knowledge processing based on semantic indexes.

The value **true** indicates that the function is enabled; the value **false** indicates the opposite.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns an error code. For details about the error codes, see [OH\_Rdb\_ErrCode](../relational-store-error-code-h/document.md#oh_rdb_errcode).

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_CreateConfig()

OH\_Rdb\_ConfigV2 \*OH\_Rdb\_CreateConfig()

**Description**

Creates an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

**Since**: 14

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) | 
Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

After use, release the memory by calling the [OH\_Rdb\_DestroyConfig](#oh_rdb_destroyconfig) API.

 |

**See**

OH\_Rdb\_ConfigV2

#### \[h2\]OH\_Rdb\_DestroyConfig()

int OH\_Rdb\_DestroyConfig(OH\_Rdb\_ConfigV2 \*config)

**Description**

Destroys an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance created by [OH\_Rdb\_CreateConfig](#oh_rdb_createconfig).

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetDatabaseDir()

int OH\_Rdb\_SetDatabaseDir(OH\_Rdb\_ConfigV2 \*config, const char \*databaseDir)

**Description**

Sets the database file path for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| const char \*dataBaseDir | Pointer to the database file path to set. The full path, including the RDB store name, cannot exceed a maximum of 1024 characters. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetStoreName()

int OH\_Rdb\_SetStoreName(OH\_Rdb\_ConfigV2 \*config, const char \*storeName)

**Description**

Sets the database name for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| const char \*storeName | Pointer to the RDB store name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetBundleName()

int OH\_Rdb\_SetBundleName(OH\_Rdb\_ConfigV2 \*config, const char \*bundleName)

**Description**

Sets the bundle name for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| const char \*bundleName | Pointer to the application bundle name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetModuleName()

int OH\_Rdb\_SetModuleName(OH\_Rdb\_ConfigV2 \*config, const char \*moduleName)

**Description**

Sets the module name for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| const char \*moduleName | Pointer to the module name to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetEncrypted()

int OH\_Rdb\_SetEncrypted(OH\_Rdb\_ConfigV2 \*config, bool isEncrypted)

**Description**

Sets whether to encrypt the database for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| bool isEncrypted | Whether to encrypt the RDB store. The value **true** means to encrypt the database; the value **false** means the opposite. After the database is created, this parameter cannot be modified directly. To change the database encryption status, call the [OH\_Rdb\_RekeyEx](#oh_rdb_rekeyex) API. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetSecurityLevel()

int OH\_Rdb\_SetSecurityLevel(OH\_Rdb\_ConfigV2 \*config, int securityLevel)

**Description**

Sets the database security level ([OH\_Rdb\_SecurityLevel](#oh_rdb_securitylevel)) for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

This method must be called during database creation. Otherwise, the database file cannot be created, and the error code **RDB\_E\_INVALID\_ARGS** is returned when the [OH\_Rdb\_CreateOrOpen](#oh_rdb_createoropen) API is called.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| int securityLevel | Database security level ([OH\_Rdb\_SecurityLevel](#oh_rdb_securitylevel)). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetArea()

int OH\_Rdb\_SetArea(OH\_Rdb\_ConfigV2 \*config, int area)

**Description**

Sets the security area level ([Rdb\_SecurityArea](#rdb_securityarea)) for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

This method must be called during database creation. Otherwise, the database file cannot be created, and the error code **RDB\_E\_INVALID\_ARGS** is returned when the [OH\_Rdb\_CreateOrOpen](#oh_rdb_createoropen) API is called.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| int area | Database security area level ([Rdb\_SecurityArea](#rdb_securityarea)). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetDbType()

int OH\_Rdb\_SetDbType(OH\_Rdb\_ConfigV2 \*config, int dbType)

**Description**

Sets the database type ([Rdb\_DBType](#rdb_dbtype)) for an [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| int dbType | Database type ([Rdb\_DBType](#rdb_dbtype)). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_NOT\_SUPPORTED** indicates that the current operation is not supported.

 |

#### \[h2\]OH\_Rdb\_SetCustomDir()

int OH\_Rdb\_SetCustomDir(OH\_Rdb\_ConfigV2 \*config, const char \*customDir)

**Description**

Sets the custom directory of the database.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| const char \*customDir | Custom directory of the database, with a maximum length of 128 bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetReadOnly()

int OH\_Rdb\_SetReadOnly(OH\_Rdb\_ConfigV2 \*config, bool readOnly)

**Description**

Sets whether the RDB store is in read-only mode.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| bool readOnly | Whether the RDB store is in read-only mode. The value **true** indicates that the RDB store is in read-only mode; the value **false** indicates that the RDB store is in read/write mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetPlugins()

int OH\_Rdb\_SetPlugins(OH\_Rdb\_ConfigV2 \*config, const char \*\*plugins, int32\_t length)

**Description**

Sets the dynamic library with specific capabilities (such as full-text search).

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| const char \*\*plugins | Name array of the dynamic library. |
| int32\_t length | Size of the plugin array. The maximum value is **16**. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetCryptoParam()

int OH\_Rdb\_SetCryptoParam(OH\_Rdb\_ConfigV2 \*config, const OH\_Rdb\_CryptoParam \*cryptoParam)

**Description**

Sets custom encryption parameters.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| const [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*cryptoParam | Custom encryption parameters. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_IsTokenizerSupported()

int OH\_Rdb\_IsTokenizerSupported(Rdb\_Tokenizer tokenizer, bool \*isSupported)

**Description**

Checks whether the specified tokenizer is supported.

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Rdb\_Tokenizer](#rdb_tokenizer) tokenizer | Tokenizer to check. |
| bool \*isSupported | Pointer to the check result. The value **true** means the tokenizer is supported; the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns operation status code.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetTokenizer()

int OH\_Rdb\_SetTokenizer(OH\_Rdb\_ConfigV2 \*config, Rdb\_Tokenizer tokenizer)

**Description**

Sets the tokenizer type.

**Since**: 17

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the database configuration related to the RDB store. |
| [Rdb\_Tokenizer](#rdb_tokenizer) tokenizer | Tokenizer type to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns operation status code.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_NOT\_SUPPORTED** indicates that the current operation is not supported.

 |

#### \[h2\]OH\_Rdb\_SetPersistent()

int OH\_Rdb\_SetPersistent(OH\_Rdb\_ConfigV2 \*config, bool isPersistent)

**Description**

Sets whether to persist an RDB store.

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | 
Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance.

which specifies the database configuration.

 |
| bool isPersistent | Whether to persist the database data. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns operation status code.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_GetSupportedDbType()

const int \*OH\_Rdb\_GetSupportedDbType(int \*typeCount)

**Description**

Obtains the supported database type ([Rdb\_DBType](#rdb_dbtype)).

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| int \*typeCount | Pointer to the length of the array of the supported database types obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| const int \* | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_CreateValueObject()

OH\_VObject \*OH\_Rdb\_CreateValueObject()

**Description**

Creates an [OH\_VObject](../../structs/oh-vobject/document.md) instance.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_VObject](../../structs/oh-vobject/document.md) | Returns the pointer to the [OH\_VObject](../../structs/oh-vobject/document.md) instance created if the operation is successful; returns NULL otherwise. |

**See**

OH\_VObject

#### \[h2\]OH\_Rdb\_CreateValuesBucket()

OH\_VBucket \*OH\_Rdb\_CreateValuesBucket()

**Description**

Creates an [OH\_VBucket](../../structs/oh-vbucket/document.md) instance.

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) | Returns the pointer to the [OH\_VBucket](../../structs/oh-vbucket/document.md) instance created if the operation is successful; returns NULL otherwise. |

**See**

OH\_VBucket

#### \[h2\]OH\_Rdb\_CreatePredicates()

OH\_Predicates \*OH\_Rdb\_CreatePredicates(const char \*table)

**Description**

Creates an [OH\_Predicates](../../structs/oh-predicates/document.md) instance.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const char \*table | Pointer to the name of the database table. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Predicates](../../structs/oh-predicates/document.md) | Returns the pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance created if the operation is successful; returns NULL otherwise. |

**See**

OH\_Predicates

#### \[h2\]OH\_Rdb\_GetOrOpen()

OH\_Rdb\_Store \*OH\_Rdb\_GetOrOpen(const OH\_Rdb\_Config \*config, int \*errCode)

**Description**

Obtains a related [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance to operate the RDB store.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [OH\_Rdb\_Config](../../structs/oh-rdb-config/document.md) \*config | Pointer to the [OH\_Rdb\_Config](../../structs/oh-rdb-config/document.md) instance, which is the configuration of the RDB store. |
| int \*errCode | Pointer to the execution result of this API. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) | 
Returns the pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance created if the operation is successful; returns NULL otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_CreateOrOpen()

OH\_Rdb\_Store \*OH\_Rdb\_CreateOrOpen(const OH\_Rdb\_ConfigV2 \*config, int \*errCode)

**Description**

Creates or opens an [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance based on the given [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md).

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| int \*errCode | Pointer to the execution result of this API. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) | 
Returns the pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance created if the operation is successful; returns NULL otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_CloseStore()

int OH\_Rdb\_CloseStore(OH\_Rdb\_Store \*store)

**Description**

Closes an [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) object and reclaims the memory occupied by the object.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_DeleteStore()

int OH\_Rdb\_DeleteStore(const OH\_Rdb\_Config \*config)

**Description**

Deletes an RDB store with the specified configuration.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [OH\_Rdb\_Config](../../structs/oh-rdb-config/document.md) \*config | Pointer to the database configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_DeleteStoreV2()

int OH\_Rdb\_DeleteStoreV2(const OH\_Rdb\_ConfigV2 \*config)

**Description**

Deletes an RDB store based on the given [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md).

Before calling **DeleteStoreV2**, ensure that the **OH\_Rdb\_Store** and **OH\_Cursor** of the vector store have been closed.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| const [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the database configuration. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_Insert()

int OH\_Rdb\_Insert(OH\_Rdb\_Store \*store, const char \*table, OH\_VBucket \*valuesBucket)

**Description**

Inserts a row of data into a table.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*table | Pointer to the target table. |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) \*valuesBucket | Pointer to the data [OH\_VBucket](../../structs/oh-vbucket/document.md) to insert. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **rowID** if the operation is successful; returns a number less than **0** otherwise.

**RDB\_ERR** indicates that the operation fails.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_InsertWithConflictResolution()

int OH\_Rdb\_InsertWithConflictResolution(OH\_Rdb\_Store \*store, const char \*table, OH\_VBucket \*row,Rdb\_ConflictResolution resolution, int64\_t \*rowId)

**Description**

Inserts a row of data into the target table and supports conflict resolution.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*table | Name of the target table. |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) \*row | Pointer to the row of data to insert. |
| [Rdb\_ConflictResolution](../oh-rdb-types-h/document.md#rdb_conflictresolution) resolution | Policy used to resolve file conflicts. |
| int64\_t \*rowId | Pointer to the row number returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default value.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

**RDB\_E\_SQLITE\_CONSTRAINT** indicates an SQLite error code: SQLite constraint.

 |

#### \[h2\]OH\_Rdb\_BatchInsert()

int OH\_Rdb\_BatchInsert(OH\_Rdb\_Store \*store, const char \*table,const OH\_Data\_VBuckets \*rows, Rdb\_ConflictResolution resolution, int64\_t \*changes)

**Description**

Inserts data into a table in batches.

A maximum of 32,766 parameters can be inserted at a time. If the number of parameters exceeds this limit, the error code **RDB\_E\_INVALID\_ARGS** is returned. The number of inserted data records multiplied by the size of the union set of all fields in the inserted data equals the number of parameters.

For example, if the size of the union set is 10, a maximum of 3,276 data records can be inserted (3276 × 10 = 32760).

Ensure that you comply with this constraint when calling this API to avoid errors caused by excessive parameters.

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*tables | Pointer to the names of the distributed tables to set. |
| const [OH\_Data\_VBuckets \*rows](../../structs/oh-data-vbuckets/document.md) | An array of data to insert. |
| [Rdb\_ConflictResolution](../oh-rdb-types-h/document.md#rdb_conflictresolution) resolution | Policy used to resolve file conflicts. |
| int64\_t \*changes | Pointer to the number of successful insertions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default value.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

**RDB\_E\_SQLITE\_CONSTRAINT** indicates an SQLite error code: SQLite constraint.

 |

#### \[h2\]OH\_Rdb\_Update()

int OH\_Rdb\_Update(OH\_Rdb\_Store \*store, OH\_VBucket \*valuesBucket, OH\_Predicates \*predicates)

**Description**

Updates data in an RDB store based on specified conditions.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) \*valuesBucket | Pointer to the data [OH\_VBucket](../../structs/oh-vbucket/document.md) to update. |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the update conditions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the number of updated rows if the operation is successful; returns a number less than **0** otherwise.

**RDB\_ERR** indicates that the operation fails.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_UpdateWithConflictResolution()

int OH\_Rdb\_UpdateWithConflictResolution(OH\_Rdb\_Store \*store, OH\_VBucket \*row, OH\_Predicates \*predicates,Rdb\_ConflictResolution resolution, int64\_t \*changes)

**Description**

Updates data in the database based on specified conditions and supports conflict resolution.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [OH\_VBucket](../../structs/oh-vbucket/document.md) \*row | Pointer to the row of data to update. |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the update conditions. |
| [Rdb\_ConflictResolution](../oh-rdb-types-h/document.md#rdb_conflictresolution) resolution | Policy used to resolve file conflicts. |
| int64\_t \*changes | Pointer to the number of rows that are successfully updated. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default value.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

**RDB\_E\_SQLITE\_CONSTRAINT** indicates an SQLite error code: SQLite constraint.

 |

#### \[h2\]OH\_Rdb\_Delete()

int OH\_Rdb\_Delete(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates)

**Description**

Deletes data from an RDB store based on specified conditions.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the deletion conditions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the number of deleted rows if the operation is successful; returns a number less than **0** otherwise.

**RDB\_ERR** indicates that the operation fails.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_Query()

OH\_Cursor \*OH\_Rdb\_Query(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates, const char \*const \*columnNames, int length)

**Description**

Queries data in an RDB store based on specified conditions.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the query conditions. |
| const char \*const \*columnNames | Columns to query. If null is passed in, all columns are queried. |
| int length | Length of **columnNames**. If the length is greater than the length of **columnNames** array, an out-of-bounds access will occur. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) \* | Returns the pointer to the [OH\_Cursor](../../structs/oh-cursor/document.md) instance if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_Rdb\_Execute()

int OH\_Rdb\_Execute(OH\_Rdb\_Store \*store, const char \*sql)

**Description**

Executes an SQL statement that returns no value.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*sql | SQL statement to execute. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

**See**

OH\_Rdb\_Store

#### \[h2\]OH\_Rdb\_ExecuteV2()

int OH\_Rdb\_ExecuteV2(OH\_Rdb\_Store \*store, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result)

**Description**

Executes an SQL statement with a return value. This API supports vector stores.

Statements starting with comments are not supported.

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*sql | SQL statement to execute. |
| const [OH\_Data\_Values](../../structs/oh-data-values/document.md) \*args | (Optional) Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |
| [OH\_Data\_Value](../../structs/oh-data-value/document.md) \*\*result | Pointer to the [OH\_Data\_Value](../../structs/oh-data-value/document.md) instance when the execution is successful. Use [OH\_Value\_Destroy](../oh-data-value-h/document.md#oh_value_destroy) to release the memory in time. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_WAL\_SIZE\_OVER\_LIMIT** indicates that the size of the WAL log file exceeds the default value.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

 |

**See**

OH\_Value\_Destroy

#### \[h2\]OH\_Rdb\_ExecuteByTrxId()

int OH\_Rdb\_ExecuteByTrxId(OH\_Rdb\_Store \*store, int64\_t trxId, const char \*sql)

**Description**

Executes an SQL statement that returns no value based on the specified transaction ID. This API supports only vector stores.

Statements starting with comments are not supported.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| int64\_t trxId | Transaction ID returned by [OH\_Rdb\_BeginTransWithTrxId](#oh_rdb_begintranswithtrxid). The value **0** indicates that no transaction is enabled. |
| const char \*sql | SQL statement to execute. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters. The possible causes are as follows:

The input parameter is a null pointer.

The current transaction ID is not obtained by calling [OH\_Rdb\_BeginTransWithTrxId](#oh_rdb_begintranswithtrxid).

The current transaction ID has been submitted by calling [OH\_Rdb\_CommitByTrxId](#oh_rdb_commitbytrxid).

The current transaction ID has been rolled back by calling [OH\_Rdb\_RollBackByTrxId](#oh_rdb_rollbackbytrxid).

**store** or **sql** is **NULL**.

**RDB\_E\_NOT\_SUPPORTED** indicates that the current operation is not supported.

 |

**See**

OH\_Rdb\_Store

#### \[h2\]OH\_Rdb\_ExecuteQuery()

OH\_Cursor \*OH\_Rdb\_ExecuteQuery(OH\_Rdb\_Store \*store, const char \*sql)

**Description**

Queries data in the database using the specified SQL statement. This API supports vector stores.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*sql | SQL statement to execute. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) | Returns the pointer to the [OH\_Cursor](../../structs/oh-cursor/document.md) instance if the operation is successful; returns NULL otherwise. |

**See**

OH\_Rdb\_Store

#### \[h2\]OH\_Rdb\_ExecuteQueryV2()

OH\_Cursor \*OH\_Rdb\_ExecuteQueryV2(OH\_Rdb\_Store \*store, const char \*sql, const OH\_Data\_Values \*args)

**Description**

Queries data in the database using the specified SQL statement. This API supports vector stores.

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*sql | SQL statement to execute. |
| const OH\_Data\_Values \*args | (Optional) Pointer to the [OH\_Data\_Values](../../structs/oh-data-values/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) \* | 
Returns a pointer to the [OH\_Cursor](../../structs/oh-cursor/document.md) instance if the operation is successful. The [OH\_Cursor](../../structs/oh-cursor/document.md) instance is released if it is no longer required in time.

Returns **NULL** if the SQL statement is invalid or the memory allocation fails.

 |

**See**

OH\_Rdb\_Store

#### \[h2\]OH\_Rdb\_BeginTransaction()

int OH\_Rdb\_BeginTransaction(OH\_Rdb\_Store \*store)

**Description**

Begins the transaction before executing SQL statements.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_RollBack()

int OH\_Rdb\_RollBack(OH\_Rdb\_Store \*store)

**Description**

Rolls back the SQL statements executed.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_Commit()

int OH\_Rdb\_Commit(OH\_Rdb\_Store \*store)

**Description**

Commits the executed SQL statement.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_BeginTransWithTrxId()

int OH\_Rdb\_BeginTransWithTrxId(OH\_Rdb\_Store \*store, int64\_t \*trxId)

**Description**

Begins a transaction. This API returns a transaction ID and supports only vector stores.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| int64\_t \*trxId | Pointer to the transaction ID returned. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_NOT\_SUPPORTED** indicates that the current operation is not supported.

 |

#### \[h2\]OH\_Rdb\_RollBackByTrxId()

int OH\_Rdb\_RollBackByTrxId(OH\_Rdb\_Store \*store, int64\_t trxId)

**Description**

Rolls back the executed SQL statements based on the specified transaction ID. This API supports only vector stores.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| int64\_t trxId | ID of the transaction to be rolled back. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters. The possible causes are as follows:

The input parameter is a null pointer.

The current transaction ID is not obtained by calling [OH\_Rdb\_BeginTransWithTrxId](#oh_rdb_begintranswithtrxid).

The current transaction ID has been submitted by calling [OH\_Rdb\_CommitByTrxId](#oh_rdb_commitbytrxid).

The current transaction ID has been rolled back by calling [OH\_Rdb\_RollBackByTrxId](#oh_rdb_rollbackbytrxid).

**RDB\_E\_NOT\_SUPPORTED** indicates that the current operation is not supported.

 |

#### \[h2\]OH\_Rdb\_CommitByTrxId()

int OH\_Rdb\_CommitByTrxId(OH\_Rdb\_Store \*store, int64\_t trxId)

**Description**

Commits the executed SQL statements based on the specified transaction ID. This API supports only vector stores.

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| int64\_t trxId | Transaction ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates invalid parameters. The possible causes are as follows:

The input parameter is a null pointer.

The current transaction ID is not obtained by calling [OH\_Rdb\_BeginTransWithTrxId](#oh_rdb_begintranswithtrxid).

The current transaction ID has been submitted by calling [OH\_Rdb\_CommitByTrxId](#oh_rdb_commitbytrxid).

The current transaction ID has been rolled back by calling [OH\_Rdb\_RollBackByTrxId](#oh_rdb_rollbackbytrxid).

**RDB\_E\_NOT\_SUPPORTED** indicates that the current operation is not supported.

 |

**See**

OH\_Rdb\_Store

#### \[h2\]OH\_Rdb\_Backup()

int OH\_Rdb\_Backup(OH\_Rdb\_Store \*store, const char \*databasePath)

**Description**

Backs up an RDB store using the backup file of the specified path. This API supports vector stores.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*databasePath | Pointer to the destination directory in which the RDB store is backed up. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

**See**

OH\_Rdb\_Store

#### \[h2\]OH\_Rdb\_Restore()

int OH\_Rdb\_Restore(OH\_Rdb\_Store \*store, const char \*databasePath)

**Description**

Restores a database from a specified database backup file. This API supports vector stores.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*databasePath | Pointer to the destination directory in which the RDB store is backed up. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_GetVersion()

int OH\_Rdb\_GetVersion(OH\_Rdb\_Store \*store, int \*version)

**Description**

Obtains the RDB store version.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| int \*version | Pointer to the version number. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SetVersion()

int OH\_Rdb\_SetVersion(OH\_Rdb\_Store \*store, int version)

**Description**

Sets the RDB store version.

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| int version | Version to set. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

**See**

OH\_Rdb\_Store

#### \[h2\]OH\_Rdb\_SetDistributedTables()

int OH\_Rdb\_SetDistributedTables(OH\_Rdb\_Store \*store, const char \*tables\[\], uint32\_t count, Rdb\_DistributedType type,const Rdb\_DistributedConfig \*config)

**Description**

Sets distributed database tables.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*tables\[\] | Pointer to the names of the distributed tables to set. |
| uint32\_t count | Number of distributed database tables to be set. |
| [Rdb\_DistributedType](#rdb_distributedtype) type | [Rdb\_DistributedType](#rdb_distributedtype) of the table. |
| const [Rdb\_DistributedConfig](../../structs/rdb-distributedconfig/document.md) \*config | Pointer to the distributed configuration of a table ([Rdb\_DistributedConfig](../../structs/rdb-distributedconfig/document.md)). |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

**See**

OH\_Rdb\_Store

#### \[h2\]OH\_Rdb\_FindModifyTime()

OH\_Cursor \*OH\_Rdb\_FindModifyTime(OH\_Rdb\_Store \*store, const char \*tableName, const char \*columnName,OH\_VObject \*values)

**Description**

Obtains the last modification time of a table in an RDB store.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*tableName | Pointer to the target distributed database table name. |
| const char \*columnName | Pointer to the column name of the database table to query. |
| [OH\_VObject](../../structs/oh-vobject/document.md) \*values | Pointer to the primary keys of the rows to query. If the database table has no primary key, **rowid** must be passed in through **columnName**. In this case, **values** specifies the row number of the database table to query. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) | Returns the pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance created if the operation is successful; returns NULL otherwise. |

#### \[h2\]Rdb\_BriefObserver()

typedef void (\*Rdb\_BriefObserver)(void \*context, const char \*values\[\], uint32\_t count)

**Description**

Callback used to return the device-cloud data change event.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| void \*context | Pointer to the context of the data observer. |
| const char \*values\[\] | Pointer to the accounts whose device-cloud data is changed. |
| uint32\_t count | Number of accounts whose device-cloud data is changed. |

#### \[h2\]Rdb\_DetailsObserver()

typedef void (\*Rdb\_DetailsObserver)(void \*context, const Rdb\_ChangeInfo \*\*changeInfo, uint32\_t count)

**Description**

Callback used to return the details about the device-cloud data change.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| void \*context | Pointer to the context of the data observer. |
| const [Rdb\_ChangeInfo](../../structs/rdb-changeinfo/document.md) \*\*changeInfo | Information about the changed table ([Rdb\_ChangeInfo](../../structs/rdb-changeinfo/document.md)). |
| uint32\_t count | Number of changed tables. |

#### \[h2\]OH\_Rdb\_Subscribe()

int OH\_Rdb\_Subscribe(OH\_Rdb\_Store \*store, Rdb\_SubscribeType type, const Rdb\_DataObserver \*observer)

**Description**

Registers an observer for an RDB store. The registered callback will be invoked when data in a distributed or local RDB store changes.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [Rdb\_SubscribeType](#rdb_subscribetype) type | Subscription type ([Rdb\_SubscribeType](#rdb_subscribetype)). If the value is **RDB\_SUBSCRIBE\_TYPE\_LOCAL\_DETAILS**, the callback is called when the data in the local RDB store changes. |
| const [Rdb\_DataObserver](../../structs/rdb-dataobserver/document.md) \*observer | Pointer to the [Rdb\_DataObserver](../../structs/rdb-dataobserver/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_Unsubscribe()

int OH\_Rdb\_Unsubscribe(OH\_Rdb\_Store \*store, Rdb\_SubscribeType type, const Rdb\_DataObserver \*observer)

**Description**

Unregisters the observer of the specified type.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [Rdb\_SubscribeType](#rdb_subscribetype) type | Subscription type ([Rdb\_SubscribeType](#rdb_subscribetype)). |
| const [Rdb\_DataObserver](../../structs/rdb-dataobserver/document.md) \*observer | Pointer to the [Rdb\_DataObserver](../../structs/rdb-dataobserver/document.md) instance. If this parameter is **nullptr**, all observers of this type will be unregistered. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_GetTableDetails()

Rdb\_TableDetails \*OH\_Rdb\_GetTableDetails(Rdb\_ProgressDetails \*progress, int32\_t version)

**Description**

Obtains the device-cloud sync statistics of a table.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Rdb\_ProgressDetails](../../structs/rdb-progressdetails/document.md) \*progress | Pointer to the [Rdb\_ProgressDetails](../../structs/rdb-progressdetails/document.md) instance. |
| int32\_t version | Version of the current [Rdb\_ProgressDetails](../../structs/rdb-progressdetails/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [Rdb\_TableDetails](../../structs/rdb-tabledetails/document.md) | Returns a pointer to [Rdb\_TableDetails](../../structs/rdb-tabledetails/document.md) if the operation is successful; returns NULL otherwise. |

**See**

Rdb\_TableDetails

#### \[h2\]Rdb\_ProgressCallback()

typedef void (\*Rdb\_ProgressCallback)(void \*context, Rdb\_ProgressDetails \*progressDetails)

**Description**

Defines a callback used to return the device-cloud sync progress.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| void \*context | Pointer to the context of the callback data. |
| [Rdb\_ProgressDetails](../../structs/rdb-progressdetails/document.md) \*progressDetails | Details about the device-cloud sync progress. |

#### \[h2\]Rdb\_SyncCallback()

typedef void (\*Rdb\_SyncCallback)(Rdb\_ProgressDetails \*progressDetails)

**Description**

Defines a callback for device-cloud sync.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [Rdb\_ProgressDetails](../../structs/rdb-progressdetails/document.md) \*progressDetails | Statistics of device-cloud sync. |

#### \[h2\]OH\_Rdb\_CloudSync()

int OH\_Rdb\_CloudSync(OH\_Rdb\_Store \*store, Rdb\_SyncMode mode, const char \*tables\[\], uint32\_t count,const Rdb\_ProgressObserver \*observer)

**Description**

Performs device-cloud sync.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [Rdb\_SyncMode](#rdb_syncmode) mode | Type of the sync process ([Rdb\_SyncMode](#rdb_syncmode)). |
| const char \*tables\[\] | Pointer to the names of the tables to be synced. |
| uint32\_t count | Number of tables to sync. If the value is **0**, all tables in the RDB store are synced. |
| const [Rdb\_ProgressObserver](../../structs/rdb-progressobserver/document.md) \*observer | Pointer to the [Rdb\_ProgressObserver](../../structs/rdb-progressobserver/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_SubscribeAutoSyncProgress()

int OH\_Rdb\_SubscribeAutoSyncProgress(OH\_Rdb\_Store \*store, const Rdb\_ProgressObserver \*observer)

**Description**

Subscribes to the auto sync progress of an RDB store.

The registered callback will be invoked to return the auto sync progress.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the target [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const [Rdb\_ProgressObserver](../../structs/rdb-progressobserver/document.md) \*observer | Pointer to the [Rdb\_ProgressObserver](../../structs/rdb-progressobserver/document.md) instance, which invokes the callback to return the automatic sync progress. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_UnsubscribeAutoSyncProgress()

int OH\_Rdb\_UnsubscribeAutoSyncProgress(OH\_Rdb\_Store \*store, const Rdb\_ProgressObserver \*observer)

**Description**

Unsubscribes from the auto sync process of an RDB store.

**Since**: 11

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the target [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const [Rdb\_ProgressObserver](../../structs/rdb-progressobserver/document.md) \*observer | Pointer to the [Rdb\_ProgressObserver](../../structs/rdb-progressobserver/document.md) instance. If the pointer is null, all callbacks for the auto sync process will be unregistered. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns **RDB\_OK** if the operation is successful; returns an error code otherwise.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_LockRow()

int OH\_Rdb\_LockRow(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates)

**Description**

Locks data in an RDB store based on specified conditions. The locked data will be blocked from the device-cloud sync.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the lock conditions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_UnlockRow()

int OH\_Rdb\_UnlockRow(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates)

**Description**

Unlocks data in an RDB store based on specified conditions.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the unlock conditions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |

#### \[h2\]OH\_Rdb\_QueryLockedRow()

OH\_Cursor \*OH\_Rdb\_QueryLockedRow(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates, const char \*const \*columnNames, int length)

**Description**

Queries the locked data in an RDB store.

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [OH\_Predicates](../../structs/oh-predicates/document.md) \*predicates | Pointer to the [OH\_Predicates](../../structs/oh-predicates/document.md) instance, specifying the query conditions. |
| const char \*const \*columnNames | Columns to query. If null is passed in, all columns are queried. |
| int length | Length of **columnNames**. If the length is greater than the length of **columnNames** array, an out-of-bounds access will occur. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_Cursor](../../structs/oh-cursor/document.md) | Returns the pointer to the [OH\_Cursor](../../structs/oh-cursor/document.md) instance if the operation is successful; returns NULL otherwise. |

#### \[h2\]OH\_Rdb\_CreateTransaction()

int OH\_Rdb\_CreateTransaction(OH\_Rdb\_Store \*store, const OH\_RDB\_TransOptions \*options, OH\_Rdb\_Transaction \*\*trans)

**Description**

Creates a transaction object.

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) \*options | Pointer to the [OH\_RDB\_TransOptions](../../structs/oh-rdb-transoptions/document.md) instance. |
| [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) \*\*trans | 
Double pointer to the [OH\_Rdb\_Transaction](../../structs/oh-rdb-transaction/document.md) instance if the operation is successful; otherwise, **nullptr** is returned.

Release the memory using [OH\_RdbTrans\_Destroy](../oh-rdb-transaction-h/document.md#oh_rdbtrans_destroy) if the created transaction is used.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_DATABASE\_BUSY** indicates that the database does not respond.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_CANT\_OPEN** indicates an SQLite error: unable to open the database file.

 |

#### \[h2\]OH\_Rdb\_Attach()

int OH\_Rdb\_Attach(OH\_Rdb\_Store \*store, const OH\_Rdb\_ConfigV2 \*config, const char \*attachName, int64\_t waitTime,size\_t \*attachedNumber)

**Description**

Attaches a database file to the database that is currently connected.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance. |
| const char \*attachName | Pointer to the alias of the database. |
| int64\_t waitTime | Maximum duration for attaching a database, in seconds. The value ranges from 1 to 300. |
| size\_t \*attachedNumber | Pointer to the number of attached databases. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_NOT\_SUPPORTED** indicates that the operation is not supported.

**RDB\_E\_DATABASE\_BUSY** indicates that the database does not respond.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

**RDB\_E\_SQLITE\_CONSTRAINT** indicates an SQLite error code: SQLite constraint.

 |

#### \[h2\]OH\_Rdb\_Detach()

int OH\_Rdb\_Detach(OH\_Rdb\_Store \*store, const char \*attachName, int64\_t waitTime, size\_t \*attachedNumber)

**Description**

Detaches a specified store from the current database.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*attachName | Pointer to the alias of the database. |
| int64\_t waitTime | Maximum duration for detaching a database, in seconds. The value ranges from 1 to 300. |
| size\_t \*attachedNumber | Pointer to the number of attached databases. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_NOT\_SUPPORTED** indicates that the operation is not supported.

**RDB\_E\_DATABASE\_BUSY** indicates that the database does not respond.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_LOCKED** indicates an SQLite error: database table locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_TOO\_BIG** indicates an SQLite error: TEXT or BLOB exceeds the limit.

**RDB\_E\_SQLITE\_MISMATCH** indicates an SQLite error: data types mismatch.

**RDB\_E\_SQLITE\_CONSTRAINT** indicates an SQLite error code: SQLite constraint.

 |

#### \[h2\]OH\_Rdb\_SetLocale()

int OH\_Rdb\_SetLocale(OH\_Rdb\_Store \*store, const char \*locale)

**Description**

Sets locale.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| const char \*locale | Pointer to the locale to set, for example, zh. The value must comply with the ISO 639 standard. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_ERR** indicates that the operation fails.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

 |

#### \[h2\]OH\_Rdb\_RekeyEx()

int OH\_Rdb\_RekeyEx(OH\_Rdb\_Store \*store, OH\_Rdb\_CryptoParam \*param)

**Description**

Changes the key used to encrypt the database.

Key update is not supported for databases in non-WAL mode.

Manual update requires exclusive access to the database. If any result set, transaction, or database opened by another process is not released, the update will fail.

Parameter update for an encrypted database and conversion between an encrypted database and a non-encrypted database are supported.

The larger the database, the longer the update takes.

Exercise caution when changing the encryption parameters. The correct encryption parameters must be passed when **OH\_Rdb\_CreateOrOpen** is called. Otherwise, the database may fail to be opened.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance. |
| [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) \*param | Pointer to the [OH\_Rdb\_CryptoParam](../../structs/oh-rdb-cryptoparam/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_ERROR** indicates a common database error.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_ALREADY\_CLOSED** indicates that the database is already closed.

**RDB\_E\_SQLITE\_CORRUPT** indicates that the database is corrupted.

**RDB\_E\_SQLITE\_PERM** indicates an SQLite error: access denied.

**RDB\_E\_SQLITE\_BUSY** indicates an SQLite error: database file locked.

**RDB\_E\_SQLITE\_NOMEM** indicates an SQLite: insufficient database memory.

**RDB\_E\_SQLITE\_READONLY** indicates an SQLite error: attempt to write a read-only database.

**RDB\_E\_SQLITE\_IOERR** indicates an SQLite: disk I/O error.

**RDB\_E\_SQLITE\_FULL** indicates an SQLite error: the database is full.

 |

#### \[h2\]Rdb\_CorruptedHandler()

typedef void (\*Rdb\_CorruptedHandler)(void \*context, OH\_Rdb\_ConfigV2 \*config, OH\_Rdb\_Store \*store)

**Description**

Defines a handler for processing database exceptions.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| void \*context | Pointer to the context of the handler. The lifecycle is managed by the service. |
| [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) object, that is, the database configuration related to the RDB storage. This parameter cannot be used outside the callback function. |
| [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) \*store | Pointer to the [OH\_Rdb\_Store](../../structs/oh-rdb-store/document.md) instance, which is generated by the system and is released immediately after the callback function ends. This parameter cannot be used outside the callback function. |

#### \[h2\]OH\_Rdb\_RegisterCorruptedHandler()

int OH\_Rdb\_RegisterCorruptedHandler(const OH\_Rdb\_ConfigV2 \*config, void \*context, const Rdb\_CorruptedHandler handler)

**Description**

Registers a handler for processing database exceptions. When a database exception occurs, this handler is called.

The exception handling logic is user-defined. You should ensure the service quality each time the callback is triggered.

Only one handler can be registered for each path.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [const OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| void \*context | Pointer to the context of the handler. |
| [const Rdb\_CorruptedHandler](#rdb_corruptedhandler) handler | Handler for processing database exceptions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

**RDB\_E\_SUB\_LIMIT\_REACHED** indicates that the number of registration exceeds the upper limit.

 |

#### \[h2\]OH\_Rdb\_UnregisterCorruptedHandler()

int OH\_Rdb\_UnregisterCorruptedHandler(const OH\_Rdb\_ConfigV2 \*config, void \*context, const Rdb\_CorruptedHandler handler)

**Description**

Unregisters the handler for processing database exceptions.

The handler and context must be the same as those during subscription. Otherwise, the operation fails.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [const OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) \*config | Pointer to the [OH\_Rdb\_ConfigV2](../../structs/oh-rdb-configv2/document.md) instance, which is the configuration of the RDB store. |
| void \*context | Pointer to the context of the handler. |
| [const Rdb\_CorruptedHandler](#rdb_corruptedhandler) handler | Handler for processing database exceptions. |

**Returns**

| Type | Description |
| :-- | :-- |
| int | 
Returns the operation result.

**RDB\_OK** indicates that the operation is successful.

**RDB\_E\_INVALID\_ARGS** indicates that invalid parameters are specified.

 |
