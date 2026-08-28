# Persisting Vector Store Data (ArkTS)

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
    
-   ArkTS supports basic data types such as number, string, binary, and boolean, and the special data type ValueType.
    
-   To ensure successful data access, limit the size of a data record to 2 MB. If a single data record exceeds the size limit, the data record may fail to be read even if it is successfully inserted.
    

#### Specifications

## Data Types

Types of database table fields are as follows.

| Type | Description | Supported |
| :-- | :-- | :-- |
| NULL | Null. | Yes |
| INTEGER | Integer. | Yes |
| DOUBLE | Floating point. | Yes |
| TEXT | String. | Yes |
| BLOB | Binary. | Yes |
| FLOATVECTOR | Vector data. | Yes |

## Field Constraints

Constraints on database table fields are as follows.

| Function | SQL Syntax | Supported |
| :-- | :-- | :-- |
| Not null | NOT NULL | Yes |
| Default value | DEFAULT | Yes |
| Unique index | UNIQUE | Yes |
| Primary key index | PRIMARY KEY | Yes |
| Foreign key index | FOREIGN | No |
| CHECK constraint | CHECK | No |

## Clauses

Clauses in a query statement are as follows.

| Keyword | Description | Supported |
| :-- | :-- | :-- |
| WHERE | Obtains data from one or more tables. | Yes |
| LIMIT | Restricts the data to return. | Yes |
| ORDER BY | Sorts data based on one or more columns. | Yes |
| ORDER BY vector distance | **<->** indicates the Euclidean distance, and **<=>** indicates the cosine distance. | Yes |
| GROUP BY | Groups the same data. | Yes |
| HAVING | Filters the results of aggregate functions. | Yes |
| INDEXED BY | Uses a specific index during query. | Yes |
| DISTINCT | Eliminates duplicate records. | No |

## Sets

Set statements in a query statement are as follows.

| Keyword | Description | Supported |
| :-- | :-- | :-- |
| UNION | Merges the results of two or more query statements and deduplicates the results. | Yes |
| UNION ALL | Merges the results of two or more query statements. | Yes |

## Operators

The following lists the operators used to filter data based on a condition. Generally, they are used in query statements.

| Type | Operator | Supported |
| :-- | :-- | :-- |
| Arithmetic operation | +, -, \*, /, % | Yes |
| Comparison operation | \==, =, !=, >, >=, <, <= | Yes |
| Logical operation | AND, BETWEEN, EXISTS, IN, NOT IN, NOT, OR, IS NULL, IS, IS NOT, LIKE, GLOB | Yes |
| String concatenation operation | || | Yes |
| Bitwise operation | &, |, ~, <<, >> | Yes |
| Vector distance operation | <->, <=> | Yes (used in the aggregate functions **max** and **min**) |

## Time and Date

The following lists the functions used to return dates in different formats based on different time functions. Generally, these functions are used in query statements.

| Keyword | Description | Supported |
| :-- | :-- | :-- |
| DATE | Returns a date in the format of YYYY-MM-DD. | Yes |
| TIME | Returns a time in the format of HH:MM:SS. | Yes |
| DATETIME | Returns date and time in the format of YYYY-MM-DD HH:MM:SS. | Yes |
| JULIANDAY | Returns the number of days since noon on November 24, 4714 BC in Greenwich Mean Time (GMT). | Yes |
| STRFTIME | Returns a formatted date based on the format string specified by the first parameter. | Yes |

## Functions

Functions in SQL statements are as follows.

| Keyword | Description | Supported |
| :-- | :-- | :-- |
| COUNT | Calculates the number of rows returned after a query. | Yes |
| MAX/MIN | Selects the maximum or minimum value in a column. | Yes |
| AVG | Calculates the average value of a column. | Yes |
| SUM | Calculates the sum of a column. | Yes |
| RANDOM | Returns a pseudo-random integer ranging from -9223372036854775808 to 9223372036854775807. | Yes |
| ABS | Calculates the absolute value. | Yes |
| UPPER/LOWER | Converts a string to uppercase or lowercase letters. | Yes |
| LENGTH | Returns the length of a string. | Yes |

#### Available APIs

The following lists only the APIs for persisting vector store data. For details about more APIs and their usage, see [RDB Store](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-data-relationalstore).

| API | Description |
| :-- | :-- |
| getRdbStore(context: Context, config: StoreConfig): Promise<RdbStore> | Obtains an **RdbStore** instance for data operations. |
| execute(sql: string, txId: number, args?: Array<ValueType>): Promise<ValueType> | Executes SQL statements that contain specified parameters. The number of operators (such as =, >, and <) in the SQL statements cannot exceed 1000. |
| querySql(sql: string, bindArgs?: Array<ValueType>):Promise<ResultSet> | Queries data in the RDB store using the specified SQL statement. The number of operators (such as =, >, and <) in the SQL statements cannot exceed 1000. |
| beginTrans(): Promise<number> | Starts the transaction before executing the SQL statements. |
| commit(txId : number):Promise<void> | Commits the executed SQL statements. This API must be used together with **beginTrans**. |
| rollback(txId : number):Promise<void> | Rolls back the executed SQL statements. This API must be used together with **beginTrans**. |
| deleteRdbStore(context: Context, config: StoreConfig): Promise<void> | Deletes a database. |
| isVectorSupported(): boolean | Checks whether the system supports vector stores. |

#### How to Develop

1.  Check whether the current system supports vector stores. The sample code is as follows:
    
    import { relationalStore } from '@kit.ArkData'; // Import a module.
    import { BusinessError } from '@kit.BasicServicesKit';
    // ...
      // Check whether the current system supports vector stores.
      let ret = relationalStore.isVectorSupported();
      if (!ret) {
        console.error(\`vectorDB is not supported.\`);
        return;
      }
    
2.  If the system supports vector stores, obtain an **RdbStore** instance. Call **getRdbStore()** to create a database and create a table.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/fUmXdmCoQZ-FEygbycLSzg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B156A03AA15835CF924B2F9F2E4E1FAB36B9BE35C58CFF748CE17635D8CAD131)
    
    -   The RDB store created by an application varies with the context. Multiple RDB stores are created for the same database name with different application contexts. For example, each UIAbility has its own context.
        
    -   When an application calls **getRdbStore()** to obtain an RDB store instance for the first time, the corresponding database file is generated in the application sandbox. When the RDB store is used, temporary files ended with **\-wal** and **\-shm** may be generated in the same directory as the database file. If you want to move the database files to other places, you must also move these temporary files. After the application is uninstalled, the database files and temporary files generated on the device are also removed.
        
    -   For details about the error codes, see [Universal Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-universal) and [RDB Store Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-data-rdb).
        
    
    The sample code is as follows:
    
    let store: relationalStore.RdbStore | undefined = undefined;
    let context = getContext();
    const STORE\_CONFIG: relationalStore.StoreConfig = {
      name: 'VectorTest.db', // Database file name.
      securityLevel: relationalStore.SecurityLevel.S1, // Database security level.
      vector: true // Optional. This parameter must be true for a vector store.
    };
    // ...
      try {
        store = await relationalStore.getRdbStore(context, STORE\_CONFIG);
        // Create a table. floatvector (2) indicates that repr is 2-dimensional.
        const SQL\_CREATE\_TABLE = 'CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, repr floatvector(2));';
        // The second parameter indicates that transaction is not enabled. The third parameter undefined indicates that parameter binding is not used.
        await store!.execute(SQL\_CREATE\_TABLE, 0, undefined);
      } catch(err) {
        console.error(\`Get RdbStore failed, code is ${err.code}, message is ${err.message}\`);
      };
    
3.  Call **execute()** to insert data to the vector store.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/LoIec2-HSluaCJRpT1E-HA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B0FC5BF463B94865C7758AD23F654773ED0C2F44D318A5BC47AD7FE57F2B8FDF)
    
    **RelationalStore** does not provide explicit flush operations for data persistence. The data inserted is persisted.
    
    The sample code is as follows:
    
    try {
      // Use parameter binding.
      const vectorValue: Float32Array = Float32Array.from(\[1.2, 2.3\]);
      await store!.execute('insert into test VALUES(?, ?);', 0, \[0, vectorValue\]);
      // Do not use parameter binding.
      await store!.execute("insert into test VALUES(1, '\[1.3, 2.4\]');", 0, undefined);
    } catch (err) {
      console.error(\`execute insert failed, code is ${err.code}, message is ${err.message}\`);
    }
    
4.  Call **execute()** to modify or delete data. The sample code is as follows:
    
    // Modify data.
    try {
      // Use parameter binding.
      const vectorValue1: Float32Array = Float32Array.from(\[2.1, 3.2\]);
      await store!.execute('update test set repr = ? where id = ?', 0, \[vectorValue1, 0\]);
      // Do not use parameter binding.
      await store!.execute("update test set repr = '\[5.1, 6.1\]' where id = 0", 0, undefined);
    } catch (err) {
      console.error(\`execute update failed, code is ${err.code}, message is ${err.message}\`);
    }
    
    // Delete data.
    try {
      // Use parameter binding.
      await store!.execute('delete from test where id = ?', 0, \[0\]);
      // Do not use parameter binding.
      await store!.execute('delete from test where id = 0', 0, undefined);
    } catch (err) {
      console.error(\`execute delete failed, code is ${err.code}, message is ${err.message}\`);
    }
    
5.  Call **querySql()** to query data. A **ResultSet** instance is returned.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/Pmj0BxUQRcyN970TjGmO2w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0B2772EADDE7C90DFB39D2DA556A16C8DA4B4B96F9B459B898F0A5B22EB1F679)
    
    Use **close()** to close the **ResultSet** that is no longer used in a timely manner so that the memory allocated can be released.
    
    The sample code is as follows:
    
    // Perform single-table queries.
    try {
      // Use parameter binding.
      const QUERY\_SQL = 'select id, repr <-> ? as distance from test where id > ? order by repr <-> ? limit 5;';
      const vectorValue2: Float32Array = Float32Array.from(\[6.2, 7.3\]);
      let resultSet = await store!.querySql(QUERY\_SQL, \[vectorValue2, 0, vectorValue2\]);
      while (resultSet!.goToNextRow()) {
        let id = resultSet.getValue(0);
        let dis = resultSet.getValue(1);
      }
      resultSet!.close();
    
      // Do not use parameter binding.
      const QUERY\_SQL1 = "select id, repr <-> '\[6.2, 7.3\]' as distance from test where id > 0 order by repr <-> '\[6.2, 7.3\]' limit 5;";
      resultSet = await store!.querySql(QUERY\_SQL1);
      resultSet!.close();
    } catch (err) {
      console.error(\`query failed, code is ${err.code}, message is ${err.message}\`);
    }
    
    // Perform subqueries.
    try {
      // Create the second table.
      let CREATE\_SQL = 'CREATE TABLE IF NOT EXISTS test1(id text PRIMARY KEY);';
      await store!.execute(CREATE\_SQL);
      let resultSet = await store!.querySql('select \* from test where id in (select id from test1);');
      resultSet!.close();
    } catch (err) {
      console.error(\`query failed, code is ${err.code}, message is ${err.message}\`);
    }
    
    // Perform aggregate queries.
    try {
      let resultSet = await store!.querySql("select \* from test where repr <-> '\[1.0, 1.0\]' > 0 group by id having max(repr <=> '\[1.0, 1.0\]');");
      resultSet!.close();
    } catch (err) {
      console.error(\`query failed, code is ${err.code}, message is ${err.message}\`);
    }
    
    // Perform multi-table queries.
    try {
      // Different union all, union will delete duplicate data.
      let resultSet = await store!.querySql("select id, repr <-> '\[1.5, 5.6\]' as distance from test union select id, repr <-> '\[1.5, 5.6\]' as distance from test order by distance limit 5;");
      resultSet!.close();
    } catch (err) {
      console.error(\`query failed, code is ${err.code}, message is ${err.message}\`);
    }
    
6.  Create a view and query data. The sample code is as follows:
    
    // Perform view queries.
    try {
      // Create a view.
      await store!.execute('CREATE VIEW v1 as select \* from test where id > 0;');
      let resultSet = await store!.querySql('select \* from v1;');
      resultSet!.close();
    } catch (err) {
      console.error(\`query failed, code is ${err.code}, message is ${err.message}\`);
    }
    
7.  Query data using vector indexes.
    
    The vector store uses vectors as keys to provide efficient and fast search capabilities.
    
    It supports the basic syntax and extended syntax as follows:
    
    -   Basic syntax:
        
        // index\_name indicates the index name, index\_type indicates the index type, and dist\_function indicates the type of distance function for similarity measurement.
        CREATE INDEX \[IF NOT EXISTS\] index\_name ON table\_name USING index\_type (column\_name dist\_function);
        
        DROP INDEX table\_name.index\_name;
        
    -   Extended syntax:
        
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
    
    **Table 3** parameter (extended syntax parameters)
    
    | Parameter | Value Range | Description |
    | :-- | :-- | :-- |
    | QUEUE\_SIZE | 
    Value range: \[10, 1000\]
    
    Default value: **20**
    
     | Size of the candidate queue when an index is created for nearest neighbor search. A larger value indicates a lower construction speed and a slightly higher recall rate. |
    | OUT\_DEGREE | 
    
    Value range: \[1, 1200\]
    
    Default value: **60**
    
     | Number of outgoing edges of a node in the graph. The value of **OUT\_DEGREE** cannot exceed **pageSize**. Otherwise, the error GRD\_INVALID\_ARGS will be thrown. |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/01/v3/NFei5B36QQakGCUo4Alpsw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F298854877C365EF5FB94F34F3DC66E26558A296349983040B776ACA0B5E5934)
    
    -   When deleting an index, you need to specify the table name, that is, **Drop Index table.index\_name**.
        
    -   The index created with a table cannot be deleted, for example, the primary key cannot be deleted.
        
    -   When querying data based on vector indexes, you must use **ORDER BY** and **LIMIT**. **ORDER BY** has only one sorting condition, that is, the vector distance condition. If **ORDER BY** is used with **DESC**, vector indexes will not be used. The distance metric used for querying must match the metric used when the index is created. For example, if the vector index is created using **L2**, <-> must be used for the query. Otherwise, the index cannot be hit.
        
    
    The sample code is as follows:
    
    // Basic syntax
    try {
      // Create an index using the basic syntax. The index name is diskann\_l2\_idx, index column is repr, type is gsdiskann, and the distance metric is L2.
      await store!.execute('CREATE INDEX diskann\_l2\_idx ON test USING GSDISKANN(repr L2);');
      // Delete the diskann\_l2\_idx index from the test table.
      await store!.execute('DROP INDEX test.diskann\_l2\_idx;');
    } catch (err) {
      console.error(\`create index failed, code is ${err.code}, message is ${err.message}\`);
    }
    
    // Extended syntax
    try {
      // Set QUEUE\_SIZE to 20 and OUT\_DEGREE to 50.
      await store!.execute('CREATE INDEX diskann\_l2\_idx ON test USING GSDISKANN(repr L2) WITH (queue\_size=20, out\_degree=50);');
    } catch (err) {
      console.error(\`create ext index failed, code is ${err.code}, message is ${err.message}\`);
    }
    
8.  Manually reclaim disk fragmentation generated during index deletion. This function is supported since API version 20.
    
    After the vector store deletes vectors on the table where the GSDiskANN index has been created, disk defragmentation is automatically performed. However, automatic disk defragmentation may not be triggered in the following scenarios:
    
    -   After vectors are deleted from the GSDiskANN index, the vector store is closed immediately.
    -   After vectors are deleted in batches from the GSDiskANN index, no operation is performed on the table.
    
    Therefore, the following statement is provided for you to trigger the disk defragmentation from the GSDiskANN index:
    
    PRAGMA DISKANN\_ASYNC\_COLLECTING;
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/pp1o3mBPRjeyPDKBgWheLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061920Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=22DE1FA5F39F6D5733FFC790C834D91BF1296C81B5119E7BFF73D59CC9CE7FCC)
    
    -   This statement is triggered to reclaim disk fragmentation from GSDiskANN indexes in all tables of the vector store at a time.
        
    -   The disk defragmentation task is a background task and does not block the execution of subsequent statements.
        
    -   The disk defragmentation task is automatically scheduled by the background based on the load. Generally, the task is executed only in low-load scenarios. The time required for successful execution depends on the load.
        
    
    The sample code is as follows:
    
    try {
      // Manually trigger asynchronous deletion and sorting to execute disk defragmentation for all GSDiskANN indexes in the vector store.
      await store!.execute('PRAGMA DISKANN\_ASYNC\_COLLECTING;');
    } catch (err) {
      console.error(\`diskann async collecting failed, code is ${err.code}, message is ${err.message}\`);
    }
    
9.  Configure the data aging policy, which allows the application data to be automatically deleted by time or space.
    
    The syntax is as follows:
    
    CREATE TABLE table\_name(column\_name type \[, ...\]) \[WITH(parameter = value \[, ...\])\];
    
    **parameter** specifies the parameter to set, and **value** specifies the value of the parameter. The following table describes the fields contained in **parameter**.
    
    **Table 4** parameter (data aging policy parameters)
    
    | Parameter | Mandatory | Value Range |
    | :-- | :-- | :-- |
    | time\_col | Yes | Column name. The value must be an integer and cannot be empty. |
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
    
    try {
       // The write operation performed every 5 minutes will trigger a data aging task.
       await store!.execute("CREATE TABLE test2(rec\_time integer not null) WITH (time\_col = 'rec\_time', interval = '5 minute');");
     } catch (err) {
       console.error(\`configure data aging failed, code is ${err.code}, message is ${err.message}\`);
     }
    
10.  Configure data compression. This feature is configured when a table is created to compress column data of the text type.
     
     Data compression is supported since API version 20.
     
     The syntax is as follows:
     
     CREATE TABLE table\_name(content text \[, ...\]) \[WITH(compress\_col = 'content')\];
     
     In this syntax, **compress\_col** is mandatory, and value is the name of the data column of the text type. This parameter can be configured together with the data aging policy.
     
     The sample code is as follows:
     
     try {
       // Data compression and data aging are configured for the content column.
       await store!.execute("CREATE TABLE IF NOT EXISTS test3 (time integer not null, content text) with (time\_col = 'time', interval = '5 minute', compress\_col = 'content');");
     } catch (err) {
       console.error(\`configure data compress failed, code is ${err.code}, message is ${err.message}\`);
     }
     
11.  Delete the database.
     
     Call **deleteRdbStore()** to delete the vector store and related database files. The sample code is as follows:
     
     try {
       // Close the store object before deleting the database. Otherwise, the next call to getRdbStore() will fail.
       await store!.close();
       await relationalStore.deleteRdbStore(context, STORE\_CONFIG);
     } catch (err) {
       console.error(\`delete rdbStore failed, code is ${err.code},message is ${err.message}\`);
     }
