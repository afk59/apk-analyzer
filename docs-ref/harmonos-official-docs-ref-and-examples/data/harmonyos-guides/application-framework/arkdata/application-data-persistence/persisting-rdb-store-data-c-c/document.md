# Persisting RDB Store Data (C/C++)

#### When to Use

The **RelationalStore** module provides a complete mechanism for local database management. You can use the APIs to add, delete, modify, and query data, and execute SQL statements in complex scenarios.

#### Basic Concepts

-   **Predicates**: a representation of the property or feature of a data entity, or the relationship between data entities, used to define operation conditions.
    
-   **ResultSet**: a set of query results, which allows access to the required data in flexible modes.
    

#### Constraints

-   By default, the Write Ahead Log (WAL) and the **FULL** flushing mode are used.
    
-   A maximum of four connection pools are used for read operations.
    
-   To ensure data accuracy, only one write operation is allowed at a time.
    
-   Once an application is uninstalled, related database files and temporary files are automatically deleted from the device.
    

#### Available APIs

For details about the APIs, see [RDB](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-rdb).

| API | Description |
| :-- | :-- |
| OH\_Rdb\_ConfigV2 \*OH\_Rdb\_CreateConfig() | Creates an **OH\_Rdb\_ConfigV2** instance. When the instance is no longer required, call **OH\_Rdb\_DestroyConfig** to destroy it. |
| int OH\_Rdb\_SetDatabaseDir(OH\_Rdb\_ConfigV2 \*config, const char \*databaseDir) | Sets the database file path for an **OH\_Rdb\_ConfigV2** instance. |
| int OH\_Rdb\_SetStoreName(OH\_Rdb\_ConfigV2 \*config, const char \*storeName) | Sets the RDB store name for an **OH\_Rdb\_ConfigV2** instance. |
| int OH\_Rdb\_SetBundleName(OH\_Rdb\_ConfigV2 \*config, const char \*bundleName) | Sets the application bundle name for an **OH\_Rdb\_ConfigV2** instance. |
| int OH\_Rdb\_SetModuleName(OH\_Rdb\_ConfigV2 \*config, const char \*moduleName) | Sets the module name for an **OH\_Rdb\_ConfigV2** instance. |
| int OH\_Rdb\_SetSecurityLevel(OH\_Rdb\_ConfigV2 \*config, int securityLevel) | Sets the security level for an **OH\_Rdb\_ConfigV2** instance. |
| int OH\_Rdb\_SetEncrypted(OH\_Rdb\_ConfigV2 \*config, bool isEncrypted) | Sets whether to encrypt the database for an **OH\_Rdb\_ConfigV2** instance. |
| int OH\_Rdb\_SetArea(OH\_Rdb\_ConfigV2 \*config, int area) | Sets the security area for an **OH\_Rdb\_ConfigV2** instance. |
| OH\_Rdb\_Store \*OH\_Rdb\_CreateOrOpen(const OH\_Rdb\_ConfigV2 \*config, int \*errCode) | Creates an **OH\_Rdb\_ConfigV2** instance to obtain an **OH\_Rdb\_Store** instance. |
| OH\_Rdb\_Execute(OH\_Rdb\_Store \*store, const char \*sql) | Executes an SQL statement that contains specified arguments but returns no value. |
| OH\_Rdb\_Insert(OH\_Rdb\_Store \*store, const char \*table, OH\_VBucket \*valuesBucket) | Inserts a row of data into a table. |
| int OH\_Rdb\_InsertWithConflictResolution(OH\_Rdb\_Store \*store, const char \*table, OH\_VBucket \*row, Rdb\_ConflictResolution resolution, int64\_t \*rowId) | Inserts a row of data into a table with conflict resolutions. |
| int OH\_Rdb\_UpdateWithConflictResolution(OH\_Rdb\_Store \*store, OH\_VBucket \*row, OH\_Predicates \*predicates, Rdb\_ConflictResolution resolution, int64\_t \*changes) | Updates a row of data in a table with conflict resolutions. |
| OH\_Rdb\_Update(OH\_Rdb\_Store \*store, OH\_VBucket \*valuesBucket, OH\_Predicates \*predicates) | Updates data in an RDB store. |
| OH\_Rdb\_Delete(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates) | Deletes data from an RDB store. |
| int OH\_Predicates\_NotLike(OH\_Predicates \*predicates, const char \*field, const char \*pattern) | Sets an **OH\_Predicates** object to match a string that is not similar to the specified value. |
| int OH\_Predicates\_Glob(OH\_Predicates \*predicates, const char \*field, const char \*pattern) | Sets an **OH\_Predicates** object to match a string containing a wildcard. |
| int OH\_Predicates\_NotGlob(OH\_Predicates \*predicates, const char \*field, const char \*pattern) | Sets an **OH\_Predicates** object not to match a string containing a wildcard. |
| OH\_Rdb\_Query(OH\_Rdb\_Store \*store, OH\_Predicates \*predicates, const char \*const \*columnNames, int length) | Queries data in an RDB store. |
| OH\_Rdb\_DeleteStore(const OH\_Rdb\_Config \*config) | Deletes an RDB store. |
| OH\_VBucket\_PutAsset(OH\_VBucket \*bucket, const char \*field, Rdb\_Asset \*value) | Puts an RDB asset into an **OH\_VBucket** object. |
| OH\_VBucket\_PutAssets(OH\_VBucket \*bucket, const char \*field, Rdb\_Asset \*value, uint32\_t count) | Puts RDB assets into an **OH\_VBucket** object. |
| OH\_Rdb\_FindModifyTime(OH\_Rdb\_Store \*store, const char \*tableName, const char \*columnName, OH\_VObject \*values) | Obtains the last modification time of the data in the specified column of a table. |
| OH\_RDB\_TransOptions \*OH\_RdbTrans\_CreateOptions(void) | Creates an **OH\_RDB\_TransOptions** instance to configure the transaction object. When the instance is no longer required, call **OH\_RdbTrans\_DestroyOptions** to destroy it. |
| OH\_Cursor \*OH\_RdbTrans\_Query(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, const char \*columns\[\], int len) | Queries data in the database based on specified conditions. |
| OH\_Data\_Values \*OH\_Values\_Create(void) | Creates an **OH\_Data\_Values** instance. When the instance is no longer required, call **OH\_Values\_Destroy** to destroy it. |
| int OH\_Data\_Asset\_SetName(Data\_Asset \*asset, const char \*name) | Sets the name for a data asset. |
| int OH\_Data\_Asset\_SetUri(Data\_Asset \*asset, const char \*uri) | Sets the absolute path for a data asset. |
| int OH\_Data\_Asset\_SetPath(Data\_Asset \*asset, const char \*path) | Sets the relative path in the application sandbox directory for a data asset. |
| int OH\_Data\_Asset\_SetCreateTime(Data\_Asset \*asset, int64\_t createTime) | Sets the creation time for a data asset. |
| int OH\_Data\_Asset\_SetModifyTime(Data\_Asset \*asset, int64\_t modifyTime) | Sets the last modification time for a data asset. |
| int OH\_Data\_Asset\_SetSize(Data\_Asset \*asset, size\_t size) | Sets the size of a data asset. |
| int OH\_Data\_Asset\_SetStatus(Data\_Asset \*asset, Data\_AssetStatus status) | Sets the status for a data asset. |
| int OH\_Data\_Asset\_GetName(Data\_Asset \*asset, char \*name, size\_t \*length) | Obtains the name of a data asset. |
| int OH\_Data\_Asset\_GetUri(Data\_Asset \*asset, char \*uri, size\_t \*length) | Obtains the absolute path of a data asset. |
| int OH\_Data\_Asset\_GetPath(Data\_Asset \*asset, char \*path, size\_t \*length) | Obtains the relative path of a data asset. |
| int OH\_Data\_Asset\_GetCreateTime(Data\_Asset \*asset, int64\_t \*createTime) | Obtains the creation time of a data asset. |
| int OH\_Data\_Asset\_GetModifyTime(Data\_Asset \*asset, int64\_t \*modifyTime) | Obtains the last modification time of a data asset. |
| int OH\_Data\_Asset\_GetSize(Data\_Asset \*asset, size\_t \*size) | Obtains the size of a data asset. |
| int OH\_Data\_Asset\_GetStatus(Data\_Asset \*asset, Data\_AssetStatus \*status) | Obtains the status of a data asset. |
| Data\_Asset \*OH\_Data\_Asset\_CreateOne() | Creates a data asset instance. When this data asset is no longer needed, call **OH\_Data\_Asset\_DestroyOne** to destroy it. |
| int OH\_Data\_Asset\_DestroyOne(Data\_Asset \*asset) | Destroys a data asset instance to reclaim memory. |
| Data\_Asset \*\*OH\_Data\_Asset\_CreateMultiple(uint32\_t count) | Creates an instance for multiple data assets. When the instance is no longer required, call **OH\_Data\_Asset\_DestroyMultiple** to destroy it. |
| int OH\_Data\_Asset\_DestroyMultiple(Data\_Asset \*\*assets, uint32\_t count) | Destroys multiple data assets to reclaim memory. |
| int OH\_Rdb\_CreateTransaction(OH\_Rdb\_Store \*store, const OH\_RDB\_TransOptions \*options, OH\_Rdb\_Transaction \*\*trans) | Creates an **OH\_Rdb\_Transaction** instance to start a transaction. |
| int OH\_RdbTransOption\_SetType(OH\_RDB\_TransOptions \*options, OH\_RDB\_TransType type) | Sets the transaction object type. |
| int OH\_RdbTrans\_Insert(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row, int64\_t \*rowId) | Inserts a row of data into a table. |
| int OH\_RdbTrans\_InsertWithConflictResolution(OH\_Rdb\_Transaction \*trans, const char \*table, const OH\_VBucket \*row, Rdb\_ConflictResolution resolution, int64\_t \*rowId) | Inserts a row of data into a table with conflict resolutions. |
| int OH\_RdbTrans\_UpdateWithConflictResolution(OH\_Rdb\_Transaction \*trans, const OH\_VBucket \*row, const OH\_Predicates \*predicates, Rdb\_ConflictResolution resolution, int64\_t \*changes) | Updates data with conflict resolutions in the database based on specified conditions. |
| int OH\_RdbTrans\_Delete(OH\_Rdb\_Transaction \*trans, const OH\_Predicates \*predicates, int64\_t \*changes) | Deletes data from an RDB store. |
| int OH\_Value\_Destroy(OH\_Data\_Value \*value) | Destroys an **OH\_Data\_Value** object. |
| int OH\_Values\_Destroy(OH\_Data\_Values \*values) | Destroys an **OH\_Values\_Destroy** object. |
| int OH\_RdbTrans\_Execute(OH\_Rdb\_Transaction \*trans, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result) | Executes an SQL statement that contains specified parameters. |
| int OH\_RdbTrans\_Commit(OH\_Rdb\_Transaction \*trans) | Commits a transaction. |
| int OH\_RdbTrans\_Rollback(OH\_Rdb\_Transaction \*trans) | Rolls back a transaction. |
| int OH\_RdbTrans\_Destroy(OH\_Rdb\_Transaction \*trans) | Destroys an **OH\_Rdb\_Transaction** instance. |
| int OH\_Rdb\_Attach(OH\_Rdb\_Store \*store, const OH\_Rdb\_ConfigV2 \*config, const char \*attachName, int64\_t waitTime, size\_t \*attachedNumber) | Attaches a database file to the database that is currently connected. |
| int OH\_Rdb\_Detach(OH\_Rdb\_Store \*store, const char \*attachName, int64\_t waitTime, size\_t \*attachedNumber) | Detaches a specified store from the current database. |
| int OH\_Rdb\_SetCustomDir(OH\_Rdb\_ConfigV2 \*config, const char \*customDir) | Sets the custom directory of the database. |
| int OH\_Rdb\_SetLocale(OH\_Rdb\_Store \*store, const char \*locale) | Sets locale. |
| int OH\_Rdb\_SetPlugins(OH\_Rdb\_ConfigV2 \*config, const char \*\*plugins, int32\_t length) | Sets the dynamic library with specific capabilities (such as full-text search). |

#### How to Develop

**Adding the Dynamic Link Library**

Add the following libraries to **CMakeLists.txt**:

libnative\_rdb\_ndk.z.so, libhilog\_ndk.z.so

**Including Header Files**

#include <cstdlib>
#include <database/data/data\_asset.h>
#include <database/rdb/oh\_cursor.h>
#include <database/rdb/oh\_predicates.h>
#include <database/rdb/oh\_value\_object.h>
#include <database/rdb/oh\_values\_bucket.h>
#include <database/rdb/relational\_store.h>
#include <database/rdb/relational\_store\_error\_code.h>
#include <hilog/log.h>

1.  Obtain an **OH\_Rdb\_Store** instance and create a database file.
    
    The **dataBaseDir** variable specifies the application sandbox path. In the stage model, you are advised to use the database directory. For details, see the **databaseDir** attribute of [Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context). The FA model does not provide any API for obtaining the database sandbox path. Use the application directory instead. For details, see **getFilesDir** of [Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-app-context).
    
    **area** indicates the security level of the directory for database files. For details, see [contextConstant](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-contextconstant). During development, you need to implement the conversion from **AreaMode** to **Rdb\_SecurityArea**.
    
    Example:
    
    // Create an OH\_Rdb\_ConfigV2 object.
    OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
    // The path is the application sandbox path.
    // The database file will be created in the sandbox path: /data/storage/el3/database/rdb/RdbTest.db.
    OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el3/database");
    // Secure path where database files are stored, which corresponds to the el path in the databaseDir parameter.
    OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL3);
    // Database file name.
    OH\_Rdb\_SetStoreName(config, "RdbTest.db");
    // Application bundle name.
    OH\_Rdb\_SetBundleName(config, "com.samples.rdbstore");
    // Module name.
    OH\_Rdb\_SetModuleName(config, "entry");
    // Security level of the database file.
    OH\_Rdb\_SetSecurityLevel(config, OH\_Rdb\_SecurityLevel::S3);
    // Whether the database is encrypted.
    OH\_Rdb\_SetEncrypted(config, false);
    // ···
    
    int errCode = 0;
    // Obtain an OH\_Rdb\_Store instance.
    OH\_Rdb\_Store \*store\_ = OH\_Rdb\_CreateOrOpen(config, &errCode);
    if (store\_ == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Create store failed, errCode: %{public}d", errCode);
        OH\_Rdb\_DestroyConfig(config);
        return;
    }
    if (errCode != OH\_Rdb\_ErrCode::RDB\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Create attachStore failed, errCode: %{public}d", errCode);
        OH\_Rdb\_DestroyConfig(config);
        OH\_Rdb\_CloseStore(store\_);
        return;
    }
    
    To set a custom database path, call the **OH\_Rdb\_SetCustomDir** API in the preceding code. Similarly, to open the database in read-only mode, call the **OH\_Rdb\_SetReadOnly** API.
    
    Example:
    
    // You can set a custom database path.
    // The database file will be created in the sandbox path /data/storage/el3/database/a/b/RdbTest.db.
    OH\_Rdb\_SetCustomDir(config, "../a/b");
    // Set the database to the read-only mode.
    OH\_Rdb\_SetReadOnly(config, true);
    
2.  Call **OH\_Rdb\_Execute** to create a table, and call **OH\_Rdb\_Insert** to insert data to the table.
    
    Example:
    
    char createTableSql\[\] = "CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, "
        "NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)";
    // Create a table.
    OH\_Rdb\_Execute(store\_, createTableSql);
    
    // Create a key-value (KV) pair instance.
    OH\_VBucket \*valueBucket = OH\_Rdb\_CreateValuesBucket();
    valueBucket->putText(valueBucket, "NAME", "Lisa");
    valueBucket->putInt64(valueBucket, "AGE", 18); // The value of AGE is 18
    valueBucket->putReal(valueBucket, "SALARY", 100.5); // The value of SALARY is 100.5
    uint8\_t arr\[\] = {1, 2, 3, 4, 5};
    int len = sizeof(arr) / sizeof(arr\[0\]);
    valueBucket->putBlob(valueBucket, "CODES", arr, len);
    // Insert data.
    int rowId = OH\_Rdb\_Insert(store\_, "EMPLOYEE", valueBucket);
    
    OH\_VBucket \*valueBucket2 = OH\_Rdb\_CreateValuesBucket();
    valueBucket2->putInt64(valueBucket2, "ID", 2); // The value of ID is 2
    valueBucket2->putText(valueBucket2, "NAME", "zhangsan");
    valueBucket2->putInt64(valueBucket2, "AGE", 24); // The value of AGE is 24
    valueBucket2->putReal(valueBucket2, "SALARY", 120.4); // The value of SALARY is 120.4
    int64\_t rowId2 = -1;
    // Configure conflict resolutions when data is inserted.
    int result = OH\_Rdb\_InsertWithConflictResolution(store\_, "EMPLOYEE", valueBucket2,
        Rdb\_ConflictResolution::RDB\_CONFLICT\_REPLACE, &rowId2);
    // Destroy the KV pair instance.
    valueBucket->destroy(valueBucket);
    valueBucket2->destroy(valueBucket2);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/CrxoLtiZRC-KkmfEoNzsVQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08521DE6DA1E9D5174923DEBE2A299CC6F88791535B89761494ACDD350C6DD23)
    
    **RelationalStore** does not provide explicit flush operations for data persistence. The **insert()** API stores data persistently.
    
3.  Modify or delete data based on the conditions specified by **OH\_Predicates**.
    
    Call **OH\_Rdb\_Update** to modify data, and call **OH\_Rdb\_Delete** to delete data.
    
    Example:
    
    // Create a valueBucket object to store the new data to be updated.
    OH\_VBucket \*valueBucket = OH\_Rdb\_CreateValuesBucket();
    valueBucket->putText(valueBucket, "NAME", "Rose");
    valueBucket->putInt64(valueBucket, "AGE", 22); // The value of AGE is 22
    valueBucket->putReal(valueBucket, "SALARY", 200.5); // The value of SALARY is 200.5
    uint8\_t arr\[\] = {1, 2, 3, 4, 5};
    int len = sizeof(arr) / sizeof(arr\[0\]);
    valueBucket->putBlob(valueBucket, "CODES", arr, len);
    // Create a predicate object and specify the update condition: NAME is Lisa and SALARY is 100.5.
    OH\_Predicates \*predicates = OH\_Rdb\_CreatePredicates("EMPLOYEE");
    if (predicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        valueBucket->destroy(valueBucket);
        return;
    }
    OH\_VObject \*valueObject = OH\_Rdb\_CreateValueObject();
    const char \*name = "Lisa";
    valueObject->putText(valueObject, name);
    predicates->equalTo(predicates, "NAME", valueObject)->andOperate(predicates);
    uint32\_t count = 1;
    double salary = 100.5;
    valueObject->putDouble(valueObject, &salary, count);
    predicates->equalTo(predicates, "SALARY", valueObject);
    // Update the data that meets the condition to the value in valueBucket.
    int changeRows = OH\_Rdb\_Update(store\_, valueBucket, predicates);
    OH\_Predicates \*predicates2 = OH\_Rdb\_CreatePredicates("EMPLOYEE");
    if (predicates2 == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        valueObject->destroy(valueObject);
        valueBucket->destroy(valueBucket);
        return;
    }
    OH\_VObject \*valueObject2 = OH\_Rdb\_CreateValueObject();
    valueObject2->putText(valueObject2, "Rose");
    predicates2->equalTo(predicates2, "NAME", valueObject2);
    valueBucket->putInt64(valueBucket, "ID", 1); // The value of ID is 1
    valueBucket->putText(valueBucket, "NAME", "zhangsan");
    int64\_t changeRows2 = -1;
    
    // Configure conflict resolutions when data is updated.
    int result = OH\_Rdb\_UpdateWithConflictResolution(store\_, valueBucket, predicates2,
        Rdb\_ConflictResolution::RDB\_CONFLICT\_REPLACE, &changeRows2);
    valueObject->destroy(valueObject);
    valueObject2->destroy(valueObject2);
    valueBucket->destroy(valueBucket);
    predicates->destroy(predicates);
    predicates2->destroy(predicates2);
    
    // Delete data.
    OH\_Predicates \*predicates = OH\_Rdb\_CreatePredicates("EMPLOYEE");
    if (predicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        return;
    }
    OH\_VObject \*valueObject = OH\_Rdb\_CreateValueObject();
    const char \*name = "Lisa";
    valueObject->putText(valueObject, name);
    predicates->equalTo(predicates, "NAME", valueObject);
    int deleteRows = OH\_Rdb\_Delete(store\_, predicates);
    valueObject->destroy(valueObject);
    predicates->destroy(predicates);
    
4.  Query data based on the conditions specified by **OH\_Predicates**.
    
    Call **OH\_Rdb\_Query** to query data. The data obtained is returned in an **OH\_Cursor** object.
    
    Example:
    
    OH\_Predicates \*predicates = OH\_Rdb\_CreatePredicates("EMPLOYEE");
    if (predicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        return;
    }
    const char \*columnNames\[\] = {"NAME", "AGE"};
    int len = sizeof(columnNames) / sizeof(columnNames\[0\]);
    OH\_Cursor \*cursor = OH\_Rdb\_Query(store\_, predicates, columnNames, len);
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        predicates->destroy(predicates);
        return;
    }
    int columnCount = 0;
    cursor->getColumnCount(cursor, &columnCount);
    
    // OH\_Cursor is a cursor of a data set. By default, the cursor points to the -1st record. Valid data starts from 0.
    int64\_t age;
    while (cursor->goToNextRow(cursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        int32\_t ageColumnIndex = -1;
        cursor->getColumnIndex(cursor, "AGE", &ageColumnIndex);
        if (ageColumnIndex != -1) {
            cursor->getInt64(cursor, ageColumnIndex, &age);
        }
    }
    
    // Destroy the OH\_Predicates instance.
    predicates->destroy(predicates);
    // Destroy the result set.
    cursor->destroy(cursor);
    
    Configure predicates to match data in LIKE or NOT LIKE mode.
    
    Example:
    
    OH\_Predicates \*likePredicates = OH\_Rdb\_CreatePredicates("EMPLOYEE");
    if (likePredicates == NULL) {
        return;
    }
    OH\_VObject \*likePattern = OH\_Rdb\_CreateValueObject();
    likePattern->putText(likePattern, "zh%");
    // Configure predicates to match data in LIKE mode.
    likePredicates->like(likePredicates, "NAME", likePattern);
    
    char \*colName\[\] = { "NAME", "AGE" };
    auto \*likeQueryCursor = OH\_Rdb\_Query(store\_, likePredicates, colName, 2); // the length of columnNamesis 2
    if (likeQueryCursor == NULL) {
        likePredicates->destroy(likePredicates);
        likePattern->destroy(likePattern);
        return;
    }
    size\_t dataLength = 0;
    int colIndex = -1;
    while (likeQueryCursor->goToNextRow(likeQueryCursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        likeQueryCursor->getColumnIndex(likeQueryCursor, "NAME", &colIndex);
        likeQueryCursor->getSize(likeQueryCursor, colIndex, &dataLength);
        char \*name = (char \*)malloc((dataLength + 1) \* sizeof(char));
        likeQueryCursor->getText(likeQueryCursor, colIndex, name, dataLength + 1);
        free(name);
    }
    likeQueryCursor->destroy(likeQueryCursor);
    likePredicates->destroy(likePredicates);
    likePattern->destroy(likePattern);
    
    OH\_Predicates \*notLikePredicates = OH\_Rdb\_CreatePredicates("EMPLOYEE");
    if (notLikePredicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        return;
    }
    // Configure predicates to match data in NOT LIKE mode.
    OH\_Predicates\_NotLike(notLikePredicates, "NAME", "zh%");
    auto \*notLikeQueryCursor = OH\_Rdb\_Query(store\_, notLikePredicates, colName, 2); // the length ofcolumnNames is 2
    if (notLikeQueryCursor == NULL) {
        notLikePredicates->destroy(notLikePredicates);
        return;
    }
    dataLength = 0;
    colIndex = -1;
    while (notLikeQueryCursor->goToNextRow(notLikeQueryCursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        notLikeQueryCursor->getColumnIndex(notLikeQueryCursor, "NAME", &colIndex);
        notLikeQueryCursor->getSize(notLikeQueryCursor, colIndex, &dataLength);
        char \*name2 = (char \*)malloc((dataLength + 1) \* sizeof(char));
        notLikeQueryCursor->getText(notLikeQueryCursor, colIndex, name2, dataLength + 1);
        free(name2);
    }
    
    notLikePredicates->destroy(notLikePredicates);
    notLikeQueryCursor->destroy(notLikeQueryCursor);
    
    Configure predicates to match data in GLOB or NOT GLOB mode.
    
    Example:
    
    OH\_Predicates \*globPredicates = OH\_Rdb\_CreatePredicates("EMPLOYEE");
    if (globPredicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        return;
    }
    // Configure predicates to match in GLOB mode.
    OH\_Predicates\_Glob(globPredicates, "NAME", "zh\*");
    
    char \*colName\[\] = { "NAME", "AGE" };
    auto \*globQueryCursor = OH\_Rdb\_Query(store\_, globPredicates, colName, 2); // the length of columnNamesis 2
    if (globQueryCursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        globPredicates->destroy(globPredicates);
        return;
    }
    size\_t dataLength = 0;
    int colIndex = -1;
    while (globQueryCursor->goToNextRow(globQueryCursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        globQueryCursor->getColumnIndex(globQueryCursor, "NAME", &colIndex);
        globQueryCursor->getSize(globQueryCursor, colIndex, &dataLength);
        char \*name = (char \*)malloc((dataLength + 1) \* sizeof(char));
        globQueryCursor->getText(globQueryCursor, colIndex, name, dataLength + 1);
        free(name);
    }
    globQueryCursor->destroy(globQueryCursor);
    globPredicates->destroy(globPredicates);
    
    OH\_Predicates \*notGlobPredicates = OH\_Rdb\_CreatePredicates("EMPLOYEE");
    if (notGlobPredicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        return;
    }
    // Configure predicates to match in NOT GLOB mode.
    OH\_Predicates\_NotGlob(notGlobPredicates, "NAME", "zh\*");
    auto \*notGlobQueryCursor = OH\_Rdb\_Query(store\_, notGlobPredicates, colName, 2); // the length ofcolumnNames is 2
    if (notGlobQueryCursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        notGlobPredicates->destroy(notGlobPredicates);
        return;
    }
    dataLength = 0;
    colIndex = -1;
    while (notGlobQueryCursor->goToNextRow(notGlobQueryCursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        notGlobQueryCursor->getColumnIndex(notGlobQueryCursor, "NAME", &colIndex);
        notGlobQueryCursor->getSize(notGlobQueryCursor, colIndex, &dataLength);
        char \*name2 = (char \*)malloc((dataLength + 1) \* sizeof(char));
        notGlobQueryCursor->getText(notGlobQueryCursor, colIndex, name2, dataLength + 1);
        free(name2);
    }
    notGlobQueryCursor->destroy(notGlobQueryCursor);
    notGlobPredicates->destroy(notGlobPredicates);
    
    You can set locale used for sorting. For example, **zh\_CN** indicates Chinese, and **tr\_TR** indicates Turkish. Call **OH\_Rdb\_SetLocale** to configure the rule.
    
    OH\_Rdb\_SetLocale(store\_, "zh\_CN");
    
    To configure the full-text search (FTS) dynamic library, use **OH\_Rdb\_SetPlugins**.
    
    For details about the constraints, see the **pluginLibs** configuration item in [StoreConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-data-relationalstore-i#storeconfig).
    
    const char \*plugins\[\] = {
        "/data/storage/el1/bundle/libs/arm64/libtokenizer.so"
    };
    
    int32\_t count = sizeof(plugins) / sizeof(plugins\[0\]);
    auto setResult = OH\_Rdb\_SetPlugins(config, plugins, count);
    
5.  Insert, delete, or update data using a transaction object.
    
    Call **OH\_RdbTransOption\_SetType** to configure the type of the transaction to be created. The supported transaction types are **DEFERRED** (default), **IMMEDIATE**, and **EXCLUSIVE**.
    
    Call **OH\_Rdb\_CreateTransaction** to create a transaction object and use this object to execute the corresponding transaction operation.
    
    OH\_RDB\_TransOptions \*options = OH\_RdbTrans\_CreateOptions();
    // Configure the transaction type.
    OH\_RdbTransOption\_SetType(options, RDB\_TRANS\_DEFERRED);
    OH\_Rdb\_Transaction \*trans = nullptr;
    // Create a transaction object.
    int res = OH\_Rdb\_CreateTransaction(store\_, options, &trans);
    OH\_RdbTrans\_DestroyOptions(options);
    
    char transCreateTableSql\[\] =
        "CREATE TABLE IF NOT EXISTS transaction\_table (id INTEGER PRIMARY KEY AUTOINCREMENT, data1 INTEGER, "
        "data2 INTEGER, data3 FLOAT, data4 TEXT, data5 BLOB, data6 ASSET, data7 ASSETS, data8 UNLIMITED INT, "
        "data9 FLOATVECTOR);";
    
    auto \*execResult = OH\_Value\_Create();
    
    // Execute SQL statements to create a database table through the transaction object.
    int ret = OH\_RdbTrans\_Execute(trans, transCreateTableSql, nullptr, &execResult);
    
    // Create an OH\_Data\_Values instance.
    OH\_Data\_Values \*values = OH\_Values\_Create();
    ret = OH\_Values\_PutInt(values, 1); // The value of id is 1
    ret = OH\_Values\_PutInt(values, 2); // The value of datat2 is 2
    ret = OH\_Values\_PutReal(values, 1.1); // The value of datat3 is 1.1
    ret = OH\_Values\_PutText(values, "1"); // The value of datat3 is 1
    unsigned char val\[\] = {1, 2};
    ret = OH\_Values\_PutBlob(values, val, sizeof(val) / sizeof(val\[0\]));
    
    Data\_Asset \*asset = OH\_Data\_Asset\_CreateOne();
    ret = OH\_Data\_Asset\_SetName(asset, "name");
    ret = OH\_Values\_PutAsset(values, asset);
    OH\_Data\_Asset\_DestroyOne(asset);
    
    Data\_Asset \*\*assets = OH\_Data\_Asset\_CreateMultiple(2); // The number of created Data\_Assets is 2
    ret = OH\_Data\_Asset\_SetName(assets\[0\], "name1");
    ret = OH\_Data\_Asset\_SetName(assets\[1\], "name2");
    ret = OH\_Values\_PutAssets(values, assets, 2); // The number of Data\_ Assets is 2
    ret = OH\_Data\_Asset\_DestroyMultiple(assets, 2); // The number of destroyed Data\_Assets is 2
    
    uint64\_t bigInt\[\] = {1, 2, 3, 4, 5};
    ret = OH\_Values\_PutUnlimitedInt(values, 0, bigInt, sizeof(bigInt) / sizeof(bigInt\[0\]));
    
    const char \*insertSql = "INSERT INTO transaction\_table "
                            "(data1, data2, data3, data4, data5, data6, data7, data8) VALUES (?, ?, ?, ?, ?, ?, ?, ?)";
    OH\_Data\_Value \*outValue = nullptr;
    
    // Execute SQL statements to insert data through the transaction object.
    ret = OH\_RdbTrans\_Execute(trans, insertSql, values, &outValue);
    OH\_Value\_Destroy(outValue);
    OH\_Values\_Destroy(values);
    
    OH\_VBucket \*transValueBucket = OH\_Rdb\_CreateValuesBucket();
    transValueBucket->putInt64(transValueBucket, "data1", 1); // The value of datat1 is 1
    transValueBucket->putInt64(transValueBucket, "data2", 2); // The value of datat2 is 2
    transValueBucket->putReal(transValueBucket, "data3", 1.1); // The value of datat3 is 1.1
    transValueBucket->putText(transValueBucket, "data4", "1"); // The value of datat4 is 1
    transValueBucket->putBlob(transValueBucket, "data5", val, sizeof(val) / sizeof(val\[0\]));
    int64\_t insertRowId = -1;
    // Insert the OH\_VBucket data through the transaction object.
    int insertRet = OH\_RdbTrans\_Insert(trans, "transaction\_table", transValueBucket, &insertRowId);
    transValueBucket->destroy(transValueBucket);
    
    OH\_VBucket \*transValueBucket2 = OH\_Rdb\_CreateValuesBucket();
    transValueBucket2->putInt64(transValueBucket2, "id", 1); // The value of id is 1
    transValueBucket2->putInt64(transValueBucket2, "data2", 2); // The value of datat2 is 2
    transValueBucket2->putReal(transValueBucket2, "data3", 1.2); // The value of datat3 is 1.2
    
    int64\_t transInsertRow = -1;
    // Configure conflict resolutions when data is inserted.
    int result = OH\_RdbTrans\_InsertWithConflictResolution(
        trans, "transaction\_table", transValueBucket2, Rdb\_ConflictResolution::RDB\_CONFLICT\_REPLACE, &transInsertRow);
    
    transValueBucket2->destroy(transValueBucket2);
    
    OH\_VBucket \*transValueBucket3 = OH\_Rdb\_CreateValuesBucket();
    transValueBucket3->putInt64(transValueBucket3, "id", 1); // The value of id is 1
    transValueBucket3->putInt64(transValueBucket3, "data2", 3); // The value of data2 is 3
    transValueBucket3->putReal(transValueBucket3, "data3", 1.2); // The value of data3 is 1.2
    
    OH\_Predicates \*transUpdatePredicates = OH\_Rdb\_CreatePredicates("transaction\_table");
    if (transUpdatePredicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        transValueBucket3->destroy(transValueBucket3);
        return;
    }
    auto targetValue = OH\_Rdb\_CreateValueObject();
    int64\_t two = 2;
    targetValue->putInt64(targetValue, &two, 1); // The value of id is 1
    transUpdatePredicates->equalTo(transUpdatePredicates, "data2", targetValue);
    
    int64\_t updateRows = -1;
    // Configure conflict resolutions when data is updated.
    OH\_RdbTrans\_UpdateWithConflictResolution(trans, transValueBucket3, transUpdatePredicates,
                                             Rdb\_ConflictResolution::RDB\_CONFLICT\_REPLACE, &updateRows);
    targetValue->destroy(targetValue);
    transValueBucket3->destroy(transValueBucket3);
    transUpdatePredicates->destroy(transUpdatePredicates);
    
    OH\_Predicates \*predicates = OH\_Rdb\_CreatePredicates("transaction\_table");
    if (predicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        return;
    }
    const char \*columns\[\] = {"data1", "data2", "data3"};
    // Query data through the transaction object.
    OH\_Cursor \*cursor = OH\_RdbTrans\_Query(trans, predicates, columns, sizeof(columns) / sizeof(columns\[0\]));
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        predicates->destroy(predicates);
        return;
    }
    int columnCount = 0;
    cursor->getColumnCount(cursor, &columnCount);
    
    predicates->destroy(predicates);
    cursor->destroy(cursor);
    
    OH\_Predicates \*predicates2 = OH\_Rdb\_CreatePredicates("transaction\_table");
    if (predicates2 == NULL) {
       OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
       return;
    }
    OH\_VObject \*valueObject = OH\_Rdb\_CreateValueObject();
    if (valueObject == NULL) {
       OH\_LOG\_ERROR(LOG\_APP, "CreateValueObject failed.");
       predicates2->destroy(predicates2);
       return;
    }
    valueObject->putText(valueObject, "1"); // Change the text value of the object to 1
    predicates2->equalTo(predicates2, "data4", valueObject);
    int64\_t changes = -1;
    // Delete data through the transaction object.
    int deleteRet = OH\_RdbTrans\_Delete(trans, predicates2, &changes);
    predicates2->destroy(predicates2);
    valueObject->destroy(valueObject);
    
    // Commit a transaction.
    OH\_RdbTrans\_Commit(trans);
    // Destroy the transaction.
    OH\_RdbTrans\_Destroy(trans);
    
    OH\_RDB\_TransOptions \*options2 = OH\_RdbTrans\_CreateOptions();
    OH\_RdbTransOption\_SetType(options2, RDB\_TRANS\_DEFERRED);
    OH\_Rdb\_Transaction \*trans2 = nullptr;
    int transCreateRet = OH\_Rdb\_CreateTransaction(store\_, options2, &trans2);
    OH\_RdbTrans\_DestroyOptions(options2);
    
    // Roll back the transaction.
    OH\_RdbTrans\_Rollback(trans2);
    OH\_RdbTrans\_Destroy(trans2);
    
6.  Attach a database.
    
    Call **OH\_Rdb\_Attach** to attach an RDB store file to an RDB store so that the data in the attached RDB store can be directly accessed using the SQL statement.
    
    This API does not support encrypted databases.
    
    After the **attach** API is called, the RDB store is switched to the non-WAL mode, which may undermine the performance. Before switching the mode, ensure that all **OH\_Cursor** objects have been destroyed and all write operations have been completed. Otherwise, error 14800015 is reported.
    
    The **attach** API cannot be called concurrently. Concurrent calls may cause the system to become unresponsive and trigger 14800015. If this occurs, try to call **attach()** again later.
    
    When the attached database is no longer used, call **OH\_Rdb\_Detach** to detach it.
    
    char attachStoreTableCreateSql\[\] = "CREATE TABLE IF NOT EXISTS EMPLOYEE (ID INTEGER PRIMARY KEY AUTOINCREMENT, "
        "NAME TEXT NOT NULL, AGE INTEGER, SALARY REAL, CODES BLOB)";
    OH\_Rdb\_ConfigV2 \*attachDbConfig = OH\_Rdb\_CreateConfig();
    if (attachDbConfig == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Create store config failed.");
        return;
    }
    OH\_Rdb\_SetModuleName(attachDbConfig, "entry");
    OH\_Rdb\_SetDatabaseDir(attachDbConfig, "/data/storage/el3/database");
    OH\_Rdb\_SetArea(attachDbConfig, RDB\_SECURITY\_AREA\_EL3);
    OH\_Rdb\_SetStoreName(attachDbConfig, "RdbAttach.db");
    OH\_Rdb\_SetSecurityLevel(attachDbConfig, OH\_Rdb\_SecurityLevel::S3);
    OH\_Rdb\_SetBundleName(attachDbConfig, "com.example.nativedemo");
    
    int errCode1 = 0;
    // Create the additional sample database RdbAttach.db.
    OH\_Rdb\_Store \*attachStore = OH\_Rdb\_CreateOrOpen(attachDbConfig, &errCode1);
    
    if (attachStore == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Create attachStore failed, errCode: %{public}d", errCode1);
        OH\_Rdb\_DestroyConfig(attachDbConfig);
        return;
    }
    
    if (errCode1 != OH\_Rdb\_ErrCode::RDB\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Create attachStore failed, errCode: %{public}d", errCode1);
        OH\_Rdb\_DestroyConfig(attachDbConfig);
        OH\_Rdb\_CloseStore(attachStore);
        return;
    }
    errCode1 = OH\_Rdb\_Execute(attachStore, attachStoreTableCreateSql);
    if (errCode1 != OH\_Rdb\_ErrCode::RDB\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Create table failed, errCode: %{public}d", errCode1);
        OH\_Rdb\_DestroyConfig(attachDbConfig);
        OH\_Rdb\_CloseStore(attachStore);
        return;
    }
    OH\_VBucket \*valueBucket = OH\_Rdb\_CreateValuesBucket();
    valueBucket->putText(valueBucket, "NAME", "Lisa");
    valueBucket->putInt64(valueBucket, "AGE", 18); // The value of AGE is 18
    valueBucket->putReal(valueBucket, "SALARY", 100.5); // The value of AGE is 100.5
    uint8\_t arr\[\] = {1, 2, 3, 4, 5};
    int len = sizeof(arr) / sizeof(arr\[0\]);
    valueBucket->putBlob(valueBucket, "CODES", arr, len);
    int rowId = OH\_Rdb\_Insert(attachStore, "EMPLOYEE", valueBucket);
    OH\_LOG\_INFO(LOG\_APP, "Insert data result: %{public}d", rowId);
    valueBucket->destroy(valueBucket);
    OH\_Rdb\_CloseStore(attachStore);
    
    // Attach databases.
    size\_t attachedNumber = 0;
    // The maximum waiting time allowed for attaching databases is 10
    errCode = OH\_Rdb\_Attach(store\_, attachDbConfig, "attach", 10, &attachedNumber);
    OH\_Rdb\_DestroyConfig(attachDbConfig);
    if (errCode != OH\_Rdb\_ErrCode::RDB\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Attach store failed, errCode: %{public}d", errCode);
        return;
    }
    OH\_Predicates \*predicates = OH\_Rdb\_CreatePredicates("attach.EMPLOYEE");
    if (predicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        // The maximum waiting time allowed for detaching databases is 10
        errCode = OH\_Rdb\_Detach(store\_, "attach", 10, &attachedNumber);
        OH\_LOG\_INFO(LOG\_APP, "Detach result: %{public}d", errCode);
        return;
    }
    char \*colName\[\] = {};
    int len = sizeof(colName) / sizeof(colName\[0\]);
    OH\_Cursor \*cursor = OH\_Rdb\_Query(store\_, predicates, colName, len);
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        // The maximum waiting time allowed for detaching databases is 10
        errCode = OH\_Rdb\_Detach(store\_, "attach", 10, &attachedNumber);
        OH\_LOG\_INFO(LOG\_APP, "Detach result: %{public}d", errCode);
        predicates->destroy(predicates);
        return;
    }
    int rowCount = -1;
    errCode = cursor->getRowCount(cursor, &rowCount);
    if (errCode != OH\_Rdb\_ErrCode::RDB\_OK) {
        OH\_LOG\_ERROR(LOG\_APP, "Get row count failed, errCode: %{public}d", errCode);
    } else {
        OH\_LOG\_INFO(LOG\_APP, "Query success, row count: %{public}d", rowCount);
    }
    cursor->destroy(cursor);
    predicates->destroy(predicates);
    // Detach databases.
    // The maximum waiting time allowed for detaching databases is 10
    errCode = OH\_Rdb\_Detach(store\_, "attach", 10, &attachedNumber);
    OH\_LOG\_INFO(LOG\_APP, "Detach result: %{public}d", errCode);
    
7.  Insert data assets into a table.
    
    // If the column attribute is a single asset, use asset in the SQL statements. If the column attribute is multiple assets, use assets in the SQL statements.
    char createAssetTableSql\[\] = "CREATE TABLE IF NOT EXISTS asset\_table (id INTEGER PRIMARY KEY AUTOINCREMENT,"
        "data1 ASSET, data2 ASSETS );";
    const char \*table = "asset\_table";
    int errCode = OH\_Rdb\_Execute(store\_, createAssetTableSql);
    OH\_VBucket \*valueBucket = OH\_Rdb\_CreateValuesBucket();
    Data\_Asset \*asset = OH\_Data\_Asset\_CreateOne();
    OH\_Data\_Asset\_SetName(asset, "name0");
    OH\_Data\_Asset\_SetUri(asset, "uri0");
    OH\_Data\_Asset\_SetPath(asset, "path0");
    OH\_Data\_Asset\_SetCreateTime(asset, 1); // Set the creation time of Data\_Asset to 1
    OH\_Data\_Asset\_SetModifyTime(asset, 1); // Set the modify time of Data\_Asset to 1
    OH\_Data\_Asset\_SetSize(asset, 1); // Set the size of the Data\_Asset to 1
    OH\_Data\_Asset\_SetStatus(asset, Data\_AssetStatus::ASSET\_NORMAL);
    errCode = OH\_VBucket\_PutAsset(valueBucket, "data1", asset);
    
    Data\_Asset \*\*assets = OH\_Data\_Asset\_CreateMultiple(2);
    
    OH\_Data\_Asset\_SetName(assets\[0\], "name0");
    OH\_Data\_Asset\_SetUri(assets\[0\], "uri0");
    OH\_Data\_Asset\_SetPath(assets\[0\], "path0");
    OH\_Data\_Asset\_SetCreateTime(assets\[0\], 1); // Set the creation time of Data\_Asset to 1
    OH\_Data\_Asset\_SetModifyTime(assets\[0\], 1); // Set the modify time of Data\_Asset to 1
    OH\_Data\_Asset\_SetSize(assets\[0\], 1); // Set the size of the Data\_Asset to 1
    OH\_Data\_Asset\_SetStatus(assets\[0\], Data\_AssetStatus::ASSET\_NORMAL);
    
    OH\_Data\_Asset\_SetName(assets\[1\], "name1");
    OH\_Data\_Asset\_SetUri(assets\[1\], "uri1");
    OH\_Data\_Asset\_SetPath(assets\[1\], "path1");
    OH\_Data\_Asset\_SetCreateTime(assets\[1\], 1); // Set the creation time of Data\_Asset to 1
    OH\_Data\_Asset\_SetModifyTime(assets\[1\], 1); // Set the modify time of Data\_Asset to 1
    OH\_Data\_Asset\_SetSize(assets\[1\], 1); // Set the size of the Data\_Asset to 1
    OH\_Data\_Asset\_SetStatus(assets\[1\], Data\_AssetStatus::ASSET\_NORMAL);
    
    uint32\_t assetsCount = 2;
    errCode = OH\_VBucket\_PutAssets(valueBucket, "data2", assets, assetsCount);
    int rowID = OH\_Rdb\_Insert(store\_, table, valueBucket);
    // Destroy Data\_Asset\* and Data\_Asset\*\*.
    OH\_Data\_Asset\_DestroyMultiple(assets, assetsCount);
    OH\_Data\_Asset\_DestroyOne(asset);
    valueBucket->destroy(valueBucket);
    
8.  Read data assets from the result set.
    
    OH\_Predicates \*predicates = OH\_Rdb\_CreatePredicates("asset\_table");
    if (predicates == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "CreatePredicates failed.");
        return;
    }
    OH\_Cursor \*cursor = OH\_Rdb\_Query(store\_, predicates, NULL, 0);
    if (cursor == NULL) {
        predicates->destroy(predicates);
    } else {
        cursor->goToNextRow(cursor);
        
        uint32\_t assetCount = 0;
        // assetCount is an output parameter that indicates the number of assets in this column.
        int errCode = cursor->getAssets(cursor, 2, nullptr, &assetCount); // Column index is 2
        Data\_Asset \*\*assets = OH\_Data\_Asset\_CreateMultiple(assetCount);
        errCode = cursor->getAssets(cursor, 2, assets, &assetCount); // Column index is 2
        // The number of Data\_Assets is 2
        if (assetCount < 2) {
            predicates->destroy(predicates);
            cursor->destroy(cursor);
        } else {
            Data\_Asset \*asset = assets\[1\];
            char name\[10\] = "";
            size\_t nameLength = 10;
            errCode = OH\_Data\_Asset\_GetName(asset, name, &nameLength);
            
            char uri\[10\] = "";
            size\_t uriLength = 10;
            errCode = OH\_Data\_Asset\_GetUri(asset, uri, &uriLength);
            
            char path\[10\] = "";
            size\_t pathLength = 10;
            errCode = OH\_Data\_Asset\_GetPath(asset, path, &pathLength);
            
            int64\_t createTime = 0;
            errCode = OH\_Data\_Asset\_GetCreateTime(asset, &createTime);
            
            int64\_t modifyTime = 0;
            errCode = OH\_Data\_Asset\_GetModifyTime(asset, &modifyTime);
            
            size\_t size = 0;
            errCode = OH\_Data\_Asset\_GetSize(asset, &size);
            
            Data\_AssetStatus status = Data\_AssetStatus::ASSET\_NULL;
            errCode = OH\_Data\_Asset\_GetStatus(asset, &status);
            
            predicates->destroy(predicates);
            OH\_Data\_Asset\_DestroyMultiple(assets, assetCount);
            cursor->destroy(cursor);
        }
    }
    
9.  Obtain the last modification time of data.
    
    Call **OH\_Rdb\_FindModifyTime** to obtain the last modification time of data in the specified column of a table. This API returns an **OH\_Cursor** object with two columns of data. The first column is the input primary key or row ID, and the second column is the last modification time.
    
    Example:
    
    constexpr uint32\_t  tableCount = 1;
    const char \*table\[tableCount\];
    table\[0\] = "EMPLOYEE";
    Rdb\_DistributedConfig distributedConfig{ .version = 1, .isAutoSync = true };
    // Set a distributed table.
    OH\_Rdb\_SetDistributedTables(store\_, table, tableCount, RDB\_DISTRIBUTED\_CLOUD, &distributedConfig);
    // Obtain the last modification time of data.
    OH\_VObject \*values = OH\_Rdb\_CreateValueObject();
    int64\_t keys\[\] = { 1 };
    values->putInt64(values, keys, 1); // The value of keys is 1
    OH\_Cursor \*cursor = OH\_Rdb\_FindModifyTime(store\_, "EMPLOYEE", "ROWID", values);
    if (cursor == NULL) {
        return;
    }
    while (cursor->goToNextRow(cursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        int64\_t rowId;
        cursor->getInt64(cursor, 1, &rowId); // 1 is the column index
    }
    
10.  Delete the database. Call the **OH\_Rdb\_DeleteStoreV2** method to delete the RDB store and related database files.
     
     Example:
     
     // Close the database instance.
     OH\_Rdb\_CloseStore(store\_);
     // Delete the database file.
     OH\_Rdb\_DeleteStoreV2(config);
