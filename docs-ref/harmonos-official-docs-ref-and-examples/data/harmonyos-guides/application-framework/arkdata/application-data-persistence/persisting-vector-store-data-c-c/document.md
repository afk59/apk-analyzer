# Persisting Vector Store Data (C/C++)

#### When to Use

Vector stores are designed to store, manage, and retrieve vector data while also supporting relational data processing for scalar values. The data type **floatvector** is used to store data vectorization results, enabling rapid retrieval and similarity searches for such data.

Since API version 18, data in vector stores can be persisted.

#### Basic Concepts

-   **ResultSet**: a set of query results, which allows access to the required data in flexible modes.
-   **floatvector**: vector data, for example, **\[1.0, 3.0, 2.4, 5.1, 6.2, 11.7\]**.

#### Constraints

-   The default log mode is Write Ahead Log ([WAL](../../arkdata-glossary/document.md#write-ahead-log-wal)), and the default flush mode is [FULL](../../arkdata-glossary/document.md#full).
    
-   A vector store supports a maximum of four read connections and one write connection at a time by default. A thread can perform the read operation when acquiring an idle read connection. If there is no idle read connection, a new read connection will be created.
    
-   To ensure data accuracy, the database supports only one write operation at a time. Concurrent write operations are performed in serial mode.
    
-   Once an application is uninstalled, related database files and temporary files are automatically deleted from the device.
    
-   To ensure successful data access, limit the size of a data record to 2 MB. Data records larger than this may be inserted correctly but fail to read.
    

#### Specifications

For details, see [Specifications](../persisting-vector-store-data-arkts/document.md#specifications).

#### Available APIs

For details, see [RDB](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-rdb).

| API | Description |
| :-- | :-- |
| int OH\_Rdb\_SetDbType(OH\_Rdb\_ConfigV2 \*config, int dbType) | Sets the database type. |
| OH\_Rdb\_Store \*OH\_Rdb\_CreateOrOpen(const OH\_Rdb\_ConfigV2 \*config, int \*errCode) | Obtains an **OH\_Rdb\_Store** instance (**dbType** is set to **RDB\_CAYLEY** by using **OH\_Rdb\_SetDbType**) for vector operations. |
| int OH\_Rdb\_ExecuteV2(OH\_Rdb\_Store \*store, const char \*sql, const OH\_Data\_Values \*args, OH\_Data\_Value \*\*result) | Executes SQL statements with a return value to perform write operations. Parameter binding is supported. The number of relational operators (such as =, >, and <) in the SQL statements cannot exceed 1000. |
| int OH\_Rdb\_ExecuteByTrxId(OH\_Rdb\_Store \*store, int64\_t trxId, const char \*sql) | Executes the SQL statement that does not return a value with the specified transaction ID. If the transaction ID is **0**, no transaction is used. |
| OH\_Cursor \*OH\_Rdb\_ExecuteQuery(OH\_Rdb\_Store \*store, const char \*sql) | Queries data in a store using the specified SQL statements. |
| OH\_Cursor \*OH\_Rdb\_ExecuteQueryV2(OH\_Rdb\_Store \*store, const char \*sql, const OH\_Data\_Values \*args) | Queries data in a store using the specified SQL statements. Parameter binding is supported. The number of relational operators (such as =, >, and <) in the SQL statements cannot exceed 1000. |
| int OH\_Rdb\_DeleteStoreV2(const OH\_Rdb\_ConfigV2 \*config) | Deletes a vector store. |
| int OH\_Cursor\_GetFloatVectorCount(OH\_Cursor \*cursor, int32\_t columnIndex, size\_t \*length) | Obtains the length of the floating-point array in the specified column of the current row. |
| int OH\_Cursor\_GetFloatVector(OH\_Cursor \*cursor, int32\_t columnIndex, float \*val, size\_t inLen, size\_t \*outLen) | Obtains the value in the specified column of the current row as a floating-point array. The value of **inLen** cannot be less than the actual array size. |

#### How to Develop

**Adding dynamic link libraries**

Add the following library to **CMakeLists.txt**.

libnative\_rdb\_ndk.z.so

**Including header files**

#include <hilog/log.h>
#include <database/data/oh\_data\_values.h>
#include <database/rdb/oh\_cursor.h>
#include <database/rdb/relational\_store.h>

1.  Check whether the system supports vector stores. The sample code is as follows:
    
    int numType = 0;
    // If numType is 2, the system supports vector stores. If numType 1, the system does not support vector stores.
    OH\_Rdb\_GetSupportedDbType(&numType);
    
2.  If the system supports vector stores, obtain an **OH\_Rdb\_Store** instance. The sample code is as follows:
    
    // Create an OH\_Rdb\_Config instance.
    OH\_Rdb\_ConfigV2 \*config = OH\_Rdb\_CreateConfig();
    // The path must be an application sandbox path.
    // The database file will be created in the sandbox path: /data/storage/el2/database/rdb/rdb\_vector\_test.db.
    OH\_Rdb\_SetDatabaseDir(config, "/data/storage/el2/database");
    // Set the store name, which is the database file name.
    OH\_Rdb\_SetStoreName(config, "rdb\_vector\_test.db");
    // Set the application bundle name.
    OH\_Rdb\_SetBundleName(config, "com.samples.vectorStore");
    // Specify whether the database is encrypted.
    OH\_Rdb\_SetEncrypted(config, false);
    // Set the security level of the database files.
    OH\_Rdb\_SetSecurityLevel(config,   OH\_Rdb\_SecurityLevel::S1);
    // Set the encryption level for the directory holding the database files.
    OH\_Rdb\_SetArea(config, RDB\_SECURITY\_AREA\_EL1);
    // Set the storage type.
    OH\_Rdb\_SetDbType(config, RDB\_CAYLEY);
        
    // Create an OH\_Rdb\_Store instance.
    int errCode = 0;
    OH\_Rdb\_Store \*store\_ = OH\_Rdb\_CreateOrOpen(config, &errCode);
    
3.  Create a table and insert data into the table.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f7/v3/KvWTMabLTjWbUQSKI2M8ow/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0FB78DF82F7A00562A05845A194C30609360882580E38461A9185DDC0E9218C)
    
    **VectorStore** does not provide explicit flush operations for data persistence. The data inserted is persisted.
    
    The sample code is as follows:
    
    char createTableSql\[\] =
        "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY AUTOINCREMENT, data1 floatvector(2));";
    // Create a table.
    OH\_Rdb\_ExecuteByTrxId(store\_, 0, createTableSql);
        
    // Insert data without parameter binding.
    OH\_Rdb\_ExecuteV2(store\_, "INSERT INTO test (id, data1) VALUES (0, '\[3.4, 4.5\]');", nullptr, nullptr);
    // Insert data with parameter binding.
    OH\_Data\_Values \*values = OH\_Values\_Create();
    OH\_Values\_PutInt(values, 1);
    float test\[\] = { 1.2, 2.3 };
    size\_t len = sizeof(test) / sizeof(test\[0\]);
    OH\_Values\_PutFloatVector(values, test, len);
    char insertSql\[\] = "INSERT INTO test (id, data1) VALUES (?, ?);";
    OH\_Rdb\_ExecuteV2(store\_, insertSql, values, nullptr);
    OH\_Values\_Destroy(values);
    
4.  Modify or delete data. The sample code is as follows:
    
    // Modify data without parameter binding.
    OH\_Rdb\_ExecuteV2(store\_, "update test set data1 = '\[5.1, 6.1\]' where id = 0;", nullptr, nullptr);
        
    // Modify data with parameter binding.
    float test1\[2\] = { 5.5, 6.6 };
    OH\_Data\_Values \*values1 = OH\_Values\_Create();
    size\_t len1 = sizeof(test1) / sizeof(test1\[0\]);
    OH\_Values\_PutFloatVector(values1, test1, len1);
    OH\_Values\_PutInt(values1, 1);
    OH\_Rdb\_ExecuteV2(store\_, "update test set data1 = ? where id = ?", values1, nullptr);
    OH\_Values\_Destroy(values1);
        
    // Delete data without parameter binding.
    OH\_Rdb\_ExecuteV2(store\_, "delete from test where id = 0", nullptr, nullptr);
        
    // Delete data with parameter binding.
    OH\_Data\_Values \*values2 = OH\_Values\_Create();
    OH\_Values\_PutInt(values2, 1);
    OH\_Rdb\_ExecuteV2(store\_, "delete from test where id = ?", values2, nullptr);
    OH\_Values\_Destroy(values2);
    
5.  Query data.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/kFBk0xccTUexshBLP6lLNA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DFC1407C546BE816E6E89E71B93FCBF043A41838859DCAB5D15AA4B44C117B02)
    
    Use **destroy()** to destroy the result set (**OH\_Cursor**) that is no longer used in a timely manner so that the memory allocated can be released.
    
    The sample code is as follows:
    
    // Query data without parameter binding.
    OH\_Cursor \*cursor = OH\_Rdb\_ExecuteQueryV2(store\_, "select \* from test where id = 1;", nullptr);
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        return;
    }
    // getRowCount may cause performance redundancy. You are advised to use this function only during debugging or maintenance.
    int rowCount = 0;
    cursor->getRowCount(cursor, &rowCount);
    while (cursor->goToNextRow(cursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        size\_t count = 0;
        // The floatvector array is the second column of data. 1 indicates the column index.
        OH\_Cursor\_GetFloatVectorCount(cursor, 1, &count);
        float test\[count\];
        size\_t outLen;
        OH\_Cursor\_GetFloatVector(cursor, 1, test, count, &outLen);
    }
    cursor->destroy(cursor);
    
    // Query data with parameter binding.
    char querySql\[\] = "select \* from test where id = ?;";
    OH\_Data\_Values \*values = OH\_Values\_Create();
    OH\_Values\_PutInt(values, 1);
    OH\_Cursor \*cursor = OH\_Rdb\_ExecuteQueryV2(store\_, querySql, values);
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        return;
    }
    while (cursor->goToNextRow(cursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        size\_t count = 0;
        // The floatvector array is the second column of data. 1 indicates the column index.
        OH\_Cursor\_GetFloatVectorCount(cursor, 1, &count);
        float test\[count\];
        size\_t outLen;
        OH\_Cursor\_GetFloatVector(cursor, 1, test, count, &outLen);
    }
    OH\_Values\_Destroy(values);
    cursor->destroy(cursor);
    
    // Query data in another table, and create the table if it does not exist.
    OH\_Rdb\_ExecuteV2(store\_, "CREATE TABLE IF NOT EXISTS example(id text PRIMARY KEY);", nullptr, nullptr);
    char querySql\[\] = "select \* from test where id in (select id from example);";
    OH\_Cursor \*cursor = OH\_Rdb\_ExecuteQueryV2(store\_, querySql, nullptr);
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        return;
    }
    while (cursor->goToNextRow(cursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        size\_t count = 0;
        // The floatvector array is the second column of data. 1 indicates the column index.
        OH\_Cursor\_GetFloatVectorCount(cursor, 1, &count);
        float test\[count\];
        size\_t outLen;
        OH\_Cursor\_GetFloatVector(cursor, 1, test, count, &outLen);
    }
    cursor->destroy(cursor);
    
    // Perform aggregate query.
    OH\_Cursor \*cursor = OH\_Rdb\_ExecuteQueryV2(store\_,
        "select \* from test where data1 <-> '\[1.0, 1.0\]' > 0 group by id having max(data1 <=> '\[1.0, 1.0\]');", nullptr);
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        return;
    }
    while (cursor->goToNextRow(cursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        size\_t count = 0;
        // The floatvector array is the second column of data. 1 indicates the column index.
        OH\_Cursor\_GetFloatVectorCount(cursor, 1, &count);
        float test\[count\];
        size\_t outLen;
        OH\_Cursor\_GetFloatVector(cursor, 1, test, count, &outLen);
    }
    cursor->destroy(cursor);
    
    // Perform multi-table query.
    OH\_Cursor \*cursor = OH\_Rdb\_ExecuteQueryV2(store\_, "select id, data1 <-> '\[1.5, 5.6\]' as distance from test "
        "union select id, data1 <-> '\[1.5, 5.6\]' as distance from test order by distance limit 5;", nullptr);
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        return;
    }
    while (cursor->goToNextRow(cursor) == OH\_Rdb\_ErrCode::RDB\_OK) {
        size\_t count = 0;
        // The floatvector array is the second column of data. 1 indicates the column index.
        OH\_Cursor\_GetFloatVectorCount(cursor, 1, &count);
        float test\[count\];
        size\_t outLen;
        OH\_Cursor\_GetFloatVector(cursor, 1, test, count, &outLen);
    }
    cursor->destroy(cursor);
    
6.  Create a view and query data. The sample code is as follows:
    
    OH\_Rdb\_ExecuteV2(store\_, "CREATE VIEW v1 as select \* from test where id > 0;", nullptr, nullptr);
    OH\_Cursor \*cursor = OH\_Rdb\_ExecuteQueryV2(store\_, "select \* from v1;", nullptr);
    if (cursor == NULL) {
        OH\_LOG\_ERROR(LOG\_APP, "Query failed.");
        return;
    }
    cursor->destroy(cursor);
    
7.  Query data using vector indexes.
    
    The vector store uses vectors as keys to provide efficient and fast search capabilities.
    
    It supports the basic syntax and extended syntax as follows:
    
    -   Basic syntax:
        
        // index\_name indicates the index name, index\_type indicates the index type, and dist\_function indicates the type of distance function for similarity measurement.
        CREATE INDEX \[IF NOT EXISTS\] index\_name ON table\_name USING index\_type (column\_name dist\_function);
        
        DROP INDEX table\_name.index\_name;
        
    -   The extended syntax is as follows:
        
        CREATE INDEX \[Basic syntax\] \[WITH(parameter = value \[, ...\])\];
        
    
    **Table 1** index\_type
    
    | Type | Description |
    | :-- | :-- |
    | gsdiskann | Index for processing high-dimensional dense vector data, such as text embedding and image features. |
    
    **Table 2** dist\_function
    
    | Type | Operator | Description |
    | :-- | :-- | :-- |
    | L2 | <-> | Euclidean distance. |
    | COSINE | <=> | Cosine distance. |
    
    **Table 3** Extended syntax parameter (parameter)
    
    | Name | Value Range | Description |
    | :-- | :-- | :-- |
    | QUEUE\_SIZE | 
    Value range: \[10, 1000\]
    
    Default value: **20**
    
     | Size of the candidate queue when an index is created for nearest neighbor search. A larger value indicates a lower construction speed and a slightly higher recall rate. |
    | OUT\_DEGREE | 
    
    Value range: \[1, 1200\]
    
    Default value: **60**
    
     | Number of outgoing edges of a node in the graph. The value of **OUT\_DEGREE** cannot exceed **pageSize**. Otherwise, the error GRD\_INVALID\_ARGS will be thrown. |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3e/v3/pgUnxP4oRhyB7vsdCNINeA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=18BC14722BB5E5D894A68E46D43E68FFFE5992B764E473242959A605DAE25320)
    
    -   When deleting an index, you need to specify the table name, that is, **Drop Index table.index\_name**.
        
    -   The index created with a table cannot be deleted, for example, the primary key cannot be deleted.
        
    -   When querying data based on vector indexes, you must use **ORDER BY** and **LIMIT**. **ORDER BY** has only one sorting condition, that is, the vector distance condition. If **ORDER BY** is used with **DESC**, vector indexes will not be used. The distance metric used for querying must match the metric used when the index is created. For example, if the vector index is created using **L2**, <-> must be used for the query. Otherwise, the index cannot be hit.
        
    
    The sample code is as follows:
    
    // Create an index using the basic syntax. The index name is diskann\_l2\_idx, index column is repr, type is gsdiskann, and the distance metric is L2.
    OH\_Rdb\_ExecuteV2(store\_, "CREATE INDEX diskann\_l2\_idx ON test USING GSDISKANN(data1 L2);", nullptr, nullptr);
    
    // Delete the diskann\_l2\_idx index from the test table.
    OH\_Rdb\_ExecuteV2(store\_, "DROP INDEX test.diskann\_l2\_idx;", nullptr, nullptr);
    
    // Set QUEUE\_SIZE to 20 and OUT\_DEGREE to 50 using the extended syntax.
    OH\_Rdb\_ExecuteV2(store\_, "CREATE INDEX diskann\_l2\_idx ON test USING GSDISKANN(data1 L2) WITH "
        "(queue\_size=20, out\_degree=50);", nullptr, nullptr);
    
8.  Configure the data aging policy, which allows the application data to be automatically deleted by time or space.
    
    The syntax is as follows:
    
    CREATE TABLE table\_name(column\_name type \[, ...\]) \[WITH(parameter = value \[, ...\])\];
    
    **parameter** specifies the parameter to set, and **value** specifies the value of the parameter. The following table describes the fields contained in **parameter**.
    
    **Table 4** parameter (data aging policy parameters)
    
    | Name | Mandatory | Description |
    | :-- | :-- | :-- |
    | time\_col | Yes | Column name The value must be an integer and cannot be empty. |
    | interval | No | 
    Interval for executing the aging task thread. If a write operation is performed after the interval, an aging task will be triggered to delete the data that meets the aging conditions. If the write operation is performed within the interval, no aging task will be triggered.
    
    Value range: \[5 second, 1 year\]
    
    Default value: **1 day**
    
    Time units supported include **second**, **minute**, **hour**, **day**, **month** and **year**. The value is case-insensitive and supports both singular and plural forms (for example, **2 hour** and **2 hours** are acceptable).
    
     |
    | ttl | No | 
    
    Data retention period.
    
    Value range: \[1 hour, 1 year\]
    
    Default value: **3 month**
    
    Time units supported include **second**, **minute**, **hour**, **day**, **month** and **year**. The value is case-insensitive and supports both singular and plural forms (for example, **2 hour** and **2 hours** are acceptable).
    
     |
    | max\_num | No | 
    
    Maximum data volume allowed.
    
    Value range: \[100, 1024\]
    
    Default value: **1024**
    
    After the aging task deletes expired data, if the remaining data in the table exceeds the value of **max\_num**, data tied to the nearest expiration-adjacent time point will be deleted until the total row count falls below **max\_num**.
    
     |
    
    Time-related parameters are converted into seconds as follows.
    
    | Unit | Value in Seconds |
    | :-- | :-- |
    | year | 365 × 24 × 60 × 60 |
    | month | 30 × 24 × 60 × 60 |
    | day | 24 × 60 × 60 |
    | hour | 60 × 60 |
    | minute | 60 |
    
    For example, if **ttl** is set to **3 months**, the value will be converted into 7,776,000 seconds (3 × (30 × 24 × 60 × 60)).
    
    The sample code is as follows:
    
    // The write operation performed every 5 minutes will trigger a data aging task.
    OH\_Rdb\_ExecuteV2(store\_,"CREATE TABLE test2(rec\_time integer not null) WITH "
        "(time\_col = 'rec\_time', interval = '5 minute');", nullptr, nullptr);
    
9.  Configure data compression. This feature is configured when a table is created to compress column data of the text type.
    
    Data compression is supported since API version 20.
    
    The syntax is as follows:
    
    CREATE TABLE table\_name(content text \[, ...\]) \[WITH(compress\_col = 'content')\];
    
    In this syntax, **compress\_col** is mandatory, and value is the column name of the text data. This parameter can be configured together with the data aging policy.
    
    The sample code is as follows:
    
    // Data compression and data aging are configured for the content column.
    OH\_Rdb\_ExecuteV2(store\_,"CREATE TABLE IF NOT EXISTS test3 (time integer not null, content text) with "
        "(time\_col = 'time', interval = '5 minute', compress\_col = 'content');", nullptr, nullptr);
    
10.  Delete the vector store. The sample code is as follows:
     
     OH\_Rdb\_CloseStore(store\_);
     OH\_Rdb\_DeleteStoreV2(config);
