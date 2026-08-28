# ArkTS API Error Codes

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/OAd9iqczSmaWoBM_VuvrCw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062322Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58CAE756580989CD477F77BA87A2248971265E938D364BCDE0DAC485DBA61057)

This topic describes only module-specific error codes. For details about universal error codes, please refer to [Universal Error Codes](../../../api-reference-overview/universal-error-codes/document.md).

#### 1021000000 Insufficient System Resource or Memory Access Exception

**Error message**

Insufficient system resources or memory access exception.

**Error description**

The system resources are insufficient or an exception occurred during memory access.

**Possible causes**

1.  The system resources are insufficient.
2.  A system error occurred, such as null pointer, unexpected restart of the data service, I/O error, or JavaScript engine exception.

**Solution**

1.  Clear the memory and try again.
2.  If the problem persists, ask the user to restart or update the app or upgrade the device version.

#### 1021000001 Calling the LLM Timed Out

**Error message**

A timeout occurred when calling the LLM.

**Error description**

A timeout error occurred during the interaction with the LLM.

**Possible causes**

A timeout error occurred when your app requested the LLM in **streamChat**.

**Solution**

1.  Call [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) again.
2.  If the retry fails multiple times, adjust the LLM parameters used in [streamChat](../arkts-api/rag-retrieval-augmentation-generation/document.md#section157381918121212) and optimize the corresponding implementation.

#### 1021000002 Loading Failed When Calling LLM

**Error message**

A loading failure occurred when calling the LLM.

**Error description**

A loading error occurred during the interaction with the LLM.

**Possible causes**

A loading error occurred when your app requested the LLM in **streamChat**.

**Solution**

1.  Call [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) again.
2.  If the retry fails multiple times, adjust the LLM parameters used in [streamChat](../arkts-api/rag-retrieval-augmentation-generation/document.md#section157381918121212) and optimize the corresponding implementation.

#### 1021000003 Calling the LLM Failed

**Error message**

A request failure occurred when calling the LLM.

**Error description**

A request failed during the interaction with the LLM.

**Possible causes**

Your app failed to request the LLM in [streamChat](../arkts-api/rag-retrieval-augmentation-generation/document.md#section157381918121212).

**Solution**

1.  Call [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) again.
2.  If the retry fails multiple times, adjust the LLM parameters used in [streamChat](../arkts-api/rag-retrieval-augmentation-generation/document.md#section157381918121212) and optimize the corresponding implementation.

#### 1021000004 LLM Busy

**Error message**

The LLM chat is busy.

**Error description**

The LLM is busy during interaction.

**Possible causes**

The LLM is busy when your app requests the LLM in [streamChat](../arkts-api/rag-retrieval-augmentation-generation/document.md#section157381918121212).

**Solution**

1.  Call [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) again.
2.  If the retry fails multiple times, adjust the LLM parameters used in [streamChat](../arkts-api/rag-retrieval-augmentation-generation/document.md#section157381918121212) and optimize the corresponding implementation.

#### 1021000005 LLM Output Does Not Meet Constraints

**Error message**

The output of LLM chat does not comply with the constraints.

**Error description**

The answer returned by the LLM exceeds 8192 bytes.

**Possible causes**

The response returned by the LLM to the request in [streamChat](../arkts-api/rag-retrieval-augmentation-generation/document.md#section157381918121212) is invalid.

**Solution**

Check the answer returned by the LLM and ensure that the return values are correctly assembled in the answer.

#### 1021000006 RAG Session Already Exists

**Error message**

The RAG session already exists.

**Error description**

The RAG session already exists.

**Possible causes**

The [RAG session](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1312212528516) is not closed and a new one cannot be created.

**Solution**

If [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182) remains unchanged, use the existing [RAG session](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1312212528516) for Q&A. Otherwise, call the [close](../arkts-api/rag-retrieval-augmentation-generation/document.md#section15625720155116) API to close the existing [RAG session](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1312212528516) and use the new [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182) information to call the [createRagSession](../arkts-api/rag-retrieval-augmentation-generation/document.md#section14201103320529) API to create a new [RAG session](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1312212528516) for Q&A.

#### 1021000007 RAG Session Busy

**Error message**

The RAG session is busy.

**Error description**

The RAG session is busy.

**Possible causes**

The [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) API is called for a new round of Q&A when the previous API call is still in progress.

**Solution**

If you want to retain the previous answer, wait until the previous [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) API call completes, and then call [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) again for a new round of Q&A.

#### 1021000008 RAG Session Closed

**Error message**

The RAG session is Already closed.

**Error description**

The RAG session has been closed.

**Possible causes**

The [RAG session](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1312212528516) has been closed when its API is called.

**Solution**

Ensure that the [RAG session](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1312212528516) exists before calling its APIs.

#### 1021000009 User Canceled streamRun

**Error message**

User has canceled the stream run.

**Error description**

The user has canceled the call to the [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) API.

**Possible causes**

The user canceled the call to the [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) API.

**Solution**

Check whether the error code is triggered as expected. No other special processing is required.

#### 1021000010 Timeout Occurred in a Session

**Error message**

A timeout occurred in the session.

**Error description**

A timeout error occurred in a session.

**Possible causes**

The retriever timed out when retrieving data.

**Solution**

Call [streamRun](../arkts-api/rag-retrieval-augmentation-generation/document.md#section178721756950) again.

#### 1021000011 Some Parameters Do Not Meet Constraints

**Error message**

Some parameter does not meet the constraints.

**Error description**

Some parameters do not meet the constraints.

**Possible causes**

The [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182) parameter passed to [createRagSession](../arkts-api/rag-retrieval-augmentation-generation/document.md#section14201103320529) does not meet the constraints.

**Solution**

Refer to the API reference to correctly configure [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182).

#### 1021000012 Knowledge Base Unavailable

**Error message**

The knowledge base is not available.

**Error description**

The knowledge base is unavailable.

**Possible causes**

1.  The knowledge processing schema is not configured.
2.  The knowledge processing schema is incorrectly configured.

**Solution**

1.  Before using the RAG capability, ensure that the [knowledge processing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-augmentation-knowledge-processing) schema has been configured.
2.  Ensure that the format and content of the schema configuration file meet related requirements.

#### 1021000013 Retrieval: Retrieval Error

**Error message**

Retrieval: An error occurred during the Retrieval.

**Error description**

An error occurred during retrieval.

**Possible causes**

1.  An error occurred in the recall phase of the retrieval module. For example, the internal status of the service is abnormal, or the input parameters are incorrect.
2.  An error occurred in the re-ranking phase of the retrieval module. For example, the service status is abnormal, or the ranking logic is incorrect.

**Solution**

1.  Ensure that the input parameters meet the requirements.
2.  Ensure that the service status is normal and initialization is complete.
3.  Check the internal logic of the service and ensure that the ranking method meets the expectation.

#### 1021000014 Retrieval: Invalid Primary Keys

**Error message**

Retrieval: There are invalid primary keys.

**Error description**

There is an invalid primary key.

**Possible causes**

1.  The number of primary keys configured for multiple recall processes is inconsistent.
2.  The configured primary key is an empty string.

**Solution**

1.  Ensure that the input primary key is correct.
2.  Correct the primary key information in **Config** and try again.

#### 1021000015 Retrieval: Re-ranking Algorithm Does Not Support Composite Primary Keys

**Error message**

Retrieval: A re-ranking algorithm that does not support composite primary keys was used.

**Error description**

A re-ranking algorithm that does not support composite primary keys is used.

**Possible causes**

Only the RRF re-ranking algorithm supports composite primary keys.

**Solution**

1.  Ensure that the number of primary keys does not exceed the upper limit allowed by the algorithm.
2.  Correct [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182) and try again.

#### 1021000016 Retrieval: Invalid Filter Input

**Error message**

Retrieval: The filter input is invalid.

**Error description**

The filter input is invalid.

**Possible causes**

1.  Mandatory fields are missing.
2.  For the BETWEEN operation, the **filterRange** field is not defined.
3.  For the non-BETWEEN operation, the **filterValue** field is not defined.

**Solution**

1.  Check the **filters** parameter.
2.  Correct [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182) and try again.

#### 1021000017 Retrieval: Invalid Recall Name in RecallCondition

**Error message**

Retrieval: There are invalid recall names in RecallCondition.

**Error description**

Invalid recall names exist in **RecallCondition**.

**Possible causes**

The values of the **recallName** fields in different **RecallCondition** are the same.

**Solution**

1.  Check the value of the **recallName** field in each **RecallCondition** and ensure that the value is valid.
2.  Correct [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182) and try again.

#### 1021000018 Retrieval: Vector Similarity Threshold in **VectorQuery** Is Higher Than the Tiering Threshold in **VectorRerankParameter**

**Error message**

Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter.

**Error description**

The similarity threshold in **VectorQuery** exceeds the tiered threshold in **VectorRerankParameter**.

**Possible causes**

The input similarity threshold in **VectorQuery** is higher than the minimum tiered threshold in **VectorRerankParameter**.

**Solution**

1.  Check the parameter settings in **VectorQuery** and ensure that the parameter settings are within a proper range.
2.  Correct [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182) and try again.

#### 1021000019 Retrieval: RerankMethod Does Not Match the Channel Type

**Error message**

Retrieval: RerankMethod parameters do not match the channel type.

**Error description**

The values of the **RerankMethod** parameters do not match the channel type.

**Possible causes**

The input parameters do not match the channel type.

**Solution**

1.  Ensure that the input parameters match the channel type.
2.  Correct [Config](../arkts-api/rag-retrieval-augmentation-generation/document.md#section1033315317182) and try again.

#### 1021200001 Database File Corrupted

**Error message**

The database is corrupted.

**Error description**

The database is corrupted when **read()** or **write()** is called.

**Possible causes**

The database file is corrupted.

**Solution**

Currently, the database cannot be backed up or restored. If data loss is acceptable, delete the database and create a new one.

#### 1021200002 Database or Transaction Closed

**Error message**

The database is closed.

**Error description**

The database or transaction is closed.

**Possible causes**

1.  Before the current operation, the **close** API has been called to close the database or the database failed to be opened or created.
2.  Before the current operation, the **commit** API has been called to commit the transaction or the **rollback** API has been called to roll back the transaction.

**Solution**

1.  Call the **getStore** API to open or create the database again. Ensure that the input parameters are correct.
2.  Call the **createTransaction** API to create a transaction again.

#### 1021200003 Database Busy

**Error message**

The database is busy.

**Error description**

The database is busy.

**Possible causes**

1.  The database is being accessed by multiple processes of the same app.
2.  Multiple threads in a process perform read and write operations at the same time, causing one thread to time out.
3.  The **write** API has been called to write data but the transaction has not been committed or rolled back.

**Solution**

1.  Avoid concurrent database operations from multiple processes.
2.  Wait for a while and try again.
3.  Commit or roll back the unclosed transaction.

#### 1021200004 Insufficient Database Memory

**Error message**

The database is out of memory.

**Error description**

The database memory is insufficient.

**Possible causes**

The data volume is too large or the memory allocated is insufficient.

**Solution**

Reduce the data volume or free up some memory by terminating unnecessary processes.

#### 1021200100 SQLite: Generic Error

**Error message**

SQLite: Generic error.

**Error description**

A generic error occurred.

**Possible causes**

An SQL statement is executed to perform any of the following operations:

1.  Insert or update data in a table that is not created.
2.  Insert or update data in a column that does not exist.
3.  Query data from a table or column that does not exist.
4.  Call an undefined function. For details, please refer to **SQLITE\_ERROR**.

**Solution**

Analyze the SQL statement and correct the error.

#### 1021200101 SQLite: Access Denied

**Error message**

SQLite: Access permission denied.

**Error description**

SQLite access is denied.

**Possible causes**

1.  SQLite does not have the required permission to access or modify a file.
2.  Refer to **SQLITE\_PERM**.

**Solution**

1.  Ensure that the file is not read-only. If the file is read-only, remove the read-only property.
2.  Ensure that the caller has the required permissions to access the file or folder.
3.  Check whether the file system is read-only. If yes, change it to writable.
4.  Ensure that the database file is not being used by another process. Terminate the process that is using the file.
5.  When handling permission issues, ensure that you have the permission to change the permissions on the file or folder.

#### 1021200102 SQLite: Database File Locked

**Error message**

SQLite: The database file is locked.

**Error description**

The SQLite database file is locked.

**Possible causes**

1.  Two processes of the same app, for example, **UIability** and **DataShareability**, perform creation, deletion, and modification operations in the same database, or processes with the same group across different apps perform creation, deletion, and modification operations in the same database via the group.
2.  Refer to **SQLITE\_BUSY**.

**Solution**

1.  Avoid concurrent database operations from multiple processes.
2.  Wait for a while and try again.

#### 1021200103 SQLite: I/O Error

**Error message**

SQLite: Some kind of disk I/O error occurred.

**Error description**

An I/O error occurred in the SQLite.

**Possible causes**

The possible causes include the following:

1.  The file does not exist.
2.  The file is read-only.
3.  The disk space is insufficient.
4.  The file is damaged.
5.  Refer to **SQLITE\_IOERR**.

**Solution**

1.  Ensure that the file path is correct and the file exists.
2.  Ensure that the file is not read-only.
3.  Delete unnecessary files to ensure sufficient disk space.
4.  Ensure that the caller has permissions to read and write the file.

#### 1021200104 WAL File Size Exceeds the Default Limit

**Error message**

SQLite: The WAL file size exceeds the default limit.

**Error description**

The WAL file size exceeds the default limit (512 MB).

**Possible causes**

Data is added, deleted, and modified continuously without closing the read transaction or result set.

**Solution**

1.  Check for unclosed result sets or transactions.
2.  Close all result sets or transactions.

#### 1021200105 Unable to Open the Database File

**Error message**

SQLite: Unable to open the database file.

**Error description**

The database file cannot be opened.

**Possible causes**

1.  The database file does not exist, and the database fails to be created.
2.  The database file exists but is damaged.
3.  The SQLite does not have permission to read or write the database file.
4.  The disk space is insufficient.
5.  Refer to **SQLITE\_CANTOPEN**.

**Solution**

1.  Ensure that the database file path is correct and the caller has permission to read and write the file.
2.  Ensure that the disk space is sufficient.

#### 1021201000 Retrieval: Recall Error

**Error message**

Retrieval: An error occurred during the recall phase.

**Error description**

An error occurred in the recall phase of the retrieval module.

**Possible causes**

The internal status of the service is abnormal, or the input parameters are incorrect.

**Solution**

1.  Ensure that the input parameters meet the requirements.
2.  Ensure that the service status is normal and initialization is complete.

#### 1021201001 Retrieval: Re-ranking Error

**Error message**

Retrieval: An error occurred during the re-ranking phase.

**Error description**

An error occurred in the re-ranking phase of the retrieval module.

**Possible causes**

The service status is abnormal, or the ranking logic is incorrect.

**Solution**

1.  Ensure that the input ranking parameters are correct.
2.  Check the internal logic of the service and ensure that the ranking method meets the expectation.

#### 1021201002 Retrieval: Numerical Parameter Out of Range

**Error message**

Retrieval: The value of the numerical parameter is outside the constrained range.

**Error description**

The value of a numeric parameter is out of range.

**Possible causes**

The provided parameter value does not meet the setting requirements.

**Solution**

1.  Check the input numeric parameter and ensure that the parameter value meets the setting requirements.
2.  Try again.

#### 1021201003 Retrieval: Invalid Primary Keys

**Error message**

Retrieval: The primary key is invalid.

**Error description**

The provided primary keys do not meet the setting requirements.

**Possible causes**

1.  The number of primary keys used in the recall parameters is inconsistent across multiple recall processes.
2.  The number of primary key fields for each recall operation in a query are different.
3.  The primary key fields in the recall API parameters are empty.

**Solution**

1.  Ensure that the input primary keys are correct.
2.  Correct the primary key information in the recall process and try again.

#### 1021201004 Retrieval: Unsupported Composite Primary Key in Re-ranking

**Error message**

Retrieval: A re-ranking algorithm that does not support composite primary keys was used.

**Error description**

More than one primary key is passed to a re-ranking algorithm that does not support composite primary keys.

**Possible causes**

Only the RRF re-ranking algorithm supports composite primary keys.

**Solution**

1.  Ensure that the number of primary keys does not exceed the upper limit allowed by the algorithm.
2.  Modify the input data and try again.

#### 1021201005 Retrieval: Empty String Parameter

**Error message**

Retrieval: There is a field with an empty string.

**Error description**

Some input parameters are set to empty strings.

**Possible causes**

Some input parameters are set to empty strings, which is invalid.

**Solution**

1.  Check the input parameter values and ensure that none of them are empty.
2.  Modify the input data and try again.

#### 1021201006 Retrieval: Illegal Filter Input

**Error message**

Retrieval: The filter input is invalid.

**Error description**

The **filters** parameter is invalid.

**Possible causes**

1.  Mandatory fields are left empty in **FilterInfo**. For example, the **columns** field is left empty, both the **filterValue** and **filterRange** fields are left empty, or the **operator** field is left empty.
2.  For the BETWEEN operation, the **filterRange** field is not defined.
3.  For the non-BETWEEN operation, the **filterValue** field is not defined.

**Solution**

1.  Check the **filters** parameter.
2.  Modify the input data and try again.

#### 1021201007 Retrieval: Invalid Recall Field Name

**Error message**

Retrieval: There is invalid recall name in RecallCondition.

**Error description**

The values of the **recallName** fields in different **RecallCondition** are the same.

**Possible causes**

The values of the **recallName** fields in different **RecallCondition** are the same.

**Solution**

1.  Check the value of the **recallName** field in each **RecallCondition** and ensure that the value is valid.
2.  Try again.

#### 1021201008 Retrieval: Vector Similarity Threshold Too High

**Error message**

Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter.

**Error description**

The similarity threshold in **VectorQuery** exceeds the tiered threshold in **VectorRerankParameter**.

**Possible causes**

The input similarity threshold in **VectorQuery** is higher than the minimum tiered threshold in **VectorRerankParameter**.

**Solution**

1.  Check the parameter settings in **VectorQuery** and ensure that the parameter settings are within a proper range.
2.  Modify the similarity threshold and try again.

#### 1021201009 Retrieval: RerankMethod Parameters Do Not Match the Channel Type

**Error message**

Retrieval: RerankMethod parameters do not match the channel type.

**Error description**

The values of the **RerankMethod** parameters do not match the channel type.

**Possible causes**

The input parameters do not match the channel type.

**Solution**

1.  Check whether the input parameters match the channel type.
2.  If not, modify the parameter settings and try again.

#### 1021201010 Retrieval: Empty Parameter Value

**Error message**

Retrieval: There exists a parameter value that should not be empty but is actually not defined.

**Error description**

The input parameter is empty.

**Possible causes**

No valid parameter is passed during the API call.

**Solution**

1.  Check whether the input parameter is valid.
2.  If not, modify the parameter settings and try again.

#### 1021200012 Unable to Generate Embeddings

**Error message**

Unable to generate embeddings

**Error description**

Loading the model failed.

**Possible causes**

1\. The current version does not support automatic generation of query vectors. You need to import the vector array.

2\. Resources are insufficient.

**Solution**

Modify the parameter settings and try again.

#### 1021400000 Internal Error

**Error message**

Internal error.

**Error description**

An internal error occurred.

**Possible causes**

1.  View the error log to determine the cause of the error. The possible causes include the following:
2.  The API execution is abnormal.
3.  The internal status is abnormal.
4.  The API is incorrectly used.
5.  A system error occurred, such as null pointer, unexpected restart of the data service, I/O error, or JavaScript engine exception.
6.  A database error occurred.

**Solution**

1.  Check whether the API is called correctly. If not, apply necessary corrections.
2.  Try again. If the problem persists, ask the user to restart or update the app or upgrade the device version.

#### 1021400001 Knowledge Source Not Configured

**Error message**

The knowledge source is not configured.

**Error description**

The **rdbSource** parameter is not set in the knowledge source configuration.

**Possible causes**

1.  The **rdbSource** parameter is not set in the knowledge source configuration.

**Solution**

1.  Set the **rdbSource** parameter according to [KnowledgeSourceConfig](../arkts-api/knowledgeprocessor-knowledge-processing/document.md#section5324144573013).

#### 1021400002 Knowledge Schema File Does Not Exist

**Error message**

The knowledge schema file is not found.

**Error description**

The knowledge schema file does not exist.

**Possible causes**

1.  The knowledge schema file is not stored in the specified directory.

**Solution**

1.  Place the **knowledge\_schema.json** file in **entry/src/main/resources/rawfile/arkdata/knowledge** by referring to [Development Procedure](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-augmentation-knowledge-processing#section912287171317).

#### 1021400003 Invalid Knowledge Schema Content

**Error message**

The knowledge schema content is invalid.

**Error description**

The knowledge schema content is invalid.

**Possible causes**

1.  The knowledge schema content does not meet the constraints.

**Solution**

1.  Modify the knowledge schema content according to [Restrictions](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-augmentation-knowledge-processing#section13189205451011).

#### 1021400004 Error Occurred When Operating the RDB Data Source

**Error message**

An error occurred during operations on the RDB source.

**Error description**

An error occurred when operating the RDB data source.

**Possible causes**

1.  An RDB data source exception occurred.

**Solution**

1.  Try again. If the problem persists, ask the user to restart or update the app or upgrade the device version.

#### 1021900001 Calling On-Device Q&A Model Timed Out

**Error message**

A timeout occurs when the local chat model is called.

**Error description**

Calling the on-device Q&A model timed out.

**Possible causes**

1.  The question is too long, causing the on-device Q&A model to take too long to process.
2.  The system is busy, and hardware resources are insufficient. Therefore, the on-device Q&A model takes too long to process.

**Solution**

1.  Try to shorten the question.
2.  Close the processes with low priority in the background and try again later.

#### 1021900002 Loading the On-Device Q&A Model Failed

**Error message**

A loading failure occurs when the local chat model is called.

**Error description**

The on-device Q&A model failed to be loaded when being called.

**Possible causes**

1.  The model file is not downloaded from the PC model manager.
2.  The PC model manager service failed to be started.

**Solution**

1.  Download the model file from the PC model manager.
2.  Restart the app and try again.

#### 1021900003 Requesting the On-Device Q&A Model Failed

**Error message**

A request failure occurs when the local chat model is called.

**Error description**

The request to the on-device Q&A model failed.

**Possible causes**

1.  An internal processing exception occurred.

**Solution**

1.  Try again later.

#### 1021900004 On-Device Q&A Model Busy

**Error message**

The local chat model is busy.

**Error description**

The on-device Q&A model is busy when being called.

**Possible causes**

1.  The on-device Q&A model is processing other tasks.

**Solution**

1.  Close other Q&A requests with low priority and try again later.

#### 1021900005 Some Parameters Do Not Meet Constraints

**Error message**

Some parameters do not meet the specified constraints.

**Error description**

Some parameters do not meet the constraints.

**Possible causes**

1.  The input parameters of the API do not meet the constraints.

**Solution**

1.  Modify the input parameters according to the constraints and try again.
