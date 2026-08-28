# Retrieval

#### Overview

The AIP provides apps with the capabilities of vectorization, knowledge retrieval, and knowledge Q&A, and helps build on-device intelligent solutions.

The knowledge retrieval capability relies on the products generated through schema-based [knowledge processing](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-augmentation-knowledge-processing). When multiple knowledge processing data sources are configured in the **knowledgeSource** field of a schema, only the products from the first source can be retrieved.

**Start version**: 6.0.0(20)

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[aip\_retrieval.h](../../header-files-and-structs/aip-retrieval-h/document.md)

 | 

Provides APIs related to knowledge retrieval.

 |
| 

[aip\_retrieval\_condition.h](../../header-files-and-structs/aip-retrieval-condition-h/document.md)

 | 

Provides APIs related to retrieval conditions.

 |
| 

[aip\_retrieval\_condition\_vector.h](../../header-files-and-structs/aip-retrieval-condition-vector-h/document.md)

 | 

Provides APIs related to vector conditions.

 |
| 

[aip\_retrieval\_query.h](../../header-files-and-structs/aip-retrieval-query-h/document.md)

 | 

Provides APIs related to retrieval queries.

 |
| 

[aip\_retrieval\_record.h](../../header-files-and-structs/aip-retrieval-record-h/document.md)

 | 

Provides APIs related to retrieval results.

 |

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91)

 | 

Defines a retriever type. The retriever serves as the handle for performing retrieval operations.

 |
| 

typedef struct [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61)

 | 

Defines a retriever configuration.

 |
| 

typedef struct [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe)

 | 

Defines a database configuration.

 |
| 

typedef enum [Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205) [Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205)

 | 

Defines an enum of data index types. Currently, only the vector index type is supported.

 |
| 

typedef void(\* [OH\_Retrieval\_Callback](#gaf0f9144574f545243e2a035c0805b7d6)) (void \*context, [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record, int errCode)

 | 

Defines the callback function for returning a retrieval result.

 |
| 

typedef struct [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e)

 | 

Defines the retrieval condition, which can contain multiple sub-conditions.

 |
| 

typedef struct [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a)

 | 

Defines a retrieval sub-condition, which can be used for vector retrieval.

 |
| 

typedef struct [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) [OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10)

 | 

Defines a vector retrieval condition, including the retrieval parameters and filter conditions.

 |
| 

typedef struct [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e)

 | 

Defines a retrieval keyword. Currently, only plaintext retrieval is supported.

 |
| 

typedef struct [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952)

 | 

Defines the retrieval result, including the fields returned from the knowledge base and their values.

 |
| 

typedef struct [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f)

 | 

Defines the database bucket array in the retrieval result.

 |

#### \[h2\]Enums

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205) { Retrieval\_TYPE\_VECTOR = 1 }

 | 

Enumerates data index types. Currently, only the vector index type is supported.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

int [OH\_Retrieval\_CreateRetriever](#gac6d2c1dd3039a0ac1a6996435600a81b) (const [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) \*config, [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) \*\*retriever)

 | 

Obtains a retriever.

 |
| 

int [OH\_Retrieval\_DestroyRetriever](#ga1dc6c697ce9b8ff2a5901e154a7aae16) ([OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) \*retriever)

 | 

Destroys the retriever obtained through [OH\_Retrieval\_CreateRetriever](#gac6d2c1dd3039a0ac1a6996435600a81b).

 |
| 

[OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) \* [OH\_Retrieval\_CreateConfig](#ga2174e9883347dee95b57863a47b60f98) ()

 | 

Obtains the retriever configuration.

 |
| 

int [OH\_Retrieval\_DestroyConfig](#gaf7646a7caa380dcfaff025669c8336b9) ([OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) \*config)

 | 

Destroys the retrieval configuration obtained through [OH\_Retrieval\_CreateConfig](#ga2174e9883347dee95b57863a47b60f98).

 |
| 

[OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) \* [OH\_Retrieval\_CreateDbConfig](#ga238499e6ca79658b59080658ad59e717) ()

 | 

Creates a configuration to open the database.

 |
| 

int [OH\_Retrieval\_DestroyDbConfig](#ga08500cc36d88c15fc0e45e98a2534681) ([OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) \*dbConfig)

 | 

Destroys [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) created through [OH\_Retrieval\_CreateDbConfig](#ga238499e6ca79658b59080658ad59e717).

 |
| 

int [OH\_Retrieval\_SetDbConfig](#gab69fc668e86d62c8e2f1cfdfc29de12e) ([OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) \*dbConfig, [OH\_Rdb\_ConfigV2](../../../../arkdata/c-apis/structs/oh-rdb-configv2/document.md) \*rdbConfig)

 | 

Sets the database configuration in [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe).

 |
| 

int [OH\_Retrieval\_AddConfig](#ga217ef10e651eb8ed7e85fd5099c21939) ([OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) \*config, [Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205) channelType, [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) \*dbConfig)

 | 

Sets the database configuration in [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61).

 |
| 

int [OH\_Retrieval\_Retrieve](#ga9b5b65705a02d8817f65dd01955cfe77) (const [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) \*retriever, const [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) \*query, const [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) \*condition, void \*context, const [OH\_Retrieval\_Callback](#gaf0f9144574f545243e2a035c0805b7d6) \*callback)

 | 

Performs retrieval. After obtaining the retriever handle, input the retrieval keyword and perform retrieval based on the retrieval condition to obtain the retrieval result.

 |
| 

[OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) \* [OH\_Retrieval\_CreateCondition](#gaf596f89029870da548ab24229ab117d8) ()

 | 

Creates a retrieval condition as the input parameter of the retrieval API.

 |
| 

int [OH\_Retrieval\_DestroyCondition](#ga494ae3c2094d8c7d7886df7323e07a31) ([OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) \*condition)

 | 

Destroys the retrieval condition obtained through [OH\_Retrieval\_CreateCondition](#gaf596f89029870da548ab24229ab117d8).

 |
| 

int [OH\_Retrieval\_DestroySubCondition](#ga9801829d9219eff29dcc372301c3eec4) ([OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) \*condition)

 | 

Destroys an [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) object.

 |
| 

int [OH\_Retrieval\_AddSubCondition](#ga2a1a77b04c4876fb8f6836fb7c85a3fd) ([OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) \*condition, [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) \*subCondition)

 | 

Adds a sub-condition to a retrieval condition.

 |
| 

[OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) \* [OH\_Retrieval\_CreateVectorCondition](#ga9ba9d25126a97b67197b3f7b6fa90bfc) ()

 | 

Creates a vector retrieval condition.

 |
| 

int [OH\_Retrieval\_DestroyVectorCondition](#ga94ffaaedc2262aeeb5a98cc53d309b89) ([OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) \*condition)

 | 

Destroys the retrieval condition obtained through [OH\_Retrieval\_CreateVectorCondition](#ga9ba9d25126a97b67197b3f7b6fa90bfc).

 |
| 

int [OH\_Retrieval\_SetVectorRecallLimit](#ga3add0883ce112a17432b44733a965b60) ([OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) \*condition, uint32\_t limit)

 | 

Sets a maximum of 1000 results for vector retrieval within a retrieval condition.

 |
| 

int [OH\_Retrieval\_SetSimilarityThreshold](#gad92af7e32a48d8429bf06a587501e244) ([OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) \*condition, double threshold)

 | 

Sets the similarity threshold of vector retrieval in a retrieval condition.

 |
| 

[OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) \* [OH\_Retrieval\_CreateQuery](#gad5182c984d2e5d85171fd93205ea785f) ()

 | 

Creates a retrieval keyword as the input parameter of the retrieval API.

 |
| 

int [OH\_Retrieval\_DestroyQuery](#ga8810c6250f69bcb4ef1d5f9b6084a42b) ([OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) \*query)

 | 

Destroys the retrieval keyword obtained through [OH\_Retrieval\_CreateQuery](#gad5182c984d2e5d85171fd93205ea785f).

 |
| 

int [OH\_Retrieval\_SetOriginalQuestion](#ga967b4d6fd7de85f9299529598dce72e4) ([OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) \*query, const char \*question)

 | 

Sets the retrieval keyword in [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e).

 |
| 

int [OH\_Retrieval\_DestroyRecord](#ga92addac70c2eeb71b2ebf370d982aa48) ([OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record)

 | 

Destroys the retrieval result obtained through the retrieval API [OH\_Retrieval\_Retrieve](#ga9b5b65705a02d8817f65dd01955cfe77).

 |
| 

int [OH\_Retrieval\_GetRecordLength](#gae806d473b297a2d3accd5b34aca68bd9) (const [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record, uint32\_t \*length)

 | 

Obtains the length of the database bucket array in the retrieval result [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952).

 |
| 

int [OH\_Retrieval\_GetRecordItem](#ga41b814740cf743acf9c3ee6edbc0bed4) (const [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record, uint32\_t index, const [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) \*\*item)

 | 

Obtains the database bucket array in the retrieval result [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952).

 |
| 

int [OH\_Retrieval\_GetItemSize](#gaa2e5538a14e0d33ef3315551314a9044) (const [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) \*items, const char \*fieldName, size\_t \*size)

 | 

Obtains the size of the value of a specified field in the database bucket array [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f). The **size** value contains the null terminator.

 |
| 

int [OH\_Retrieval\_GetItemText](#ga273f6ae58af8630fec0f8d9c1472c659) (const [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) \*items, const char \*fieldName, char \*value, size\_t size)

 | 

Obtains the value of a specified field in the database bucket array [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f).

 |

#### Type Description

#### \[h2\]OH\_Retrieval\_Callback

typedef void(\* [OH\_Retrieval\_Callback](#gaf0f9144574f545243e2a035c0805b7d6)) (void \*context, [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record, int errCode)

**Description**

Defines the callback function for returning a retrieval result.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

context

 | 

Context data provided by a user.

 |
| 

record

 | 

Pointer to the [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) instance.

 |
| 

errCode

 | 

Returned error code.

 |

#### \[h2\]OH\_Retrieval\_Condition

typedef struct [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e)

**Description**

Defines the retrieval condition, which can contain multiple sub-conditions.

**Start version**: 6.0.0(20)

#### \[h2\]OH\_Retrieval\_Config

typedef struct [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61)

**Description**

Defines retrieval configurations, including the database path, database name, and package name.

**Start version**: 6.0.0(20)

#### \[h2\]OH\_Retrieval\_DbConfig

typedef struct [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe)

**Description**

Defines a database configuration.

**Start version**: 6.0.0(20)

#### \[h2\]OH\_Retrieval\_Query

typedef struct [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e)

**Description**

Defines a retrieval keyword. Currently, only plaintext retrieval is supported. Images, videos, and other formats are not supported.

**Start version**: 6.0.0(20)

#### \[h2\]OH\_Retrieval\_Record

typedef struct [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952)

**Description**

Defines the retrieval result, including the fields returned from the knowledge base and their values.

**Start version**: 6.0.0(20)

#### \[h2\]OH\_Retrieval\_RecordItem

typedef struct [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f)

**Description**

Defines the database bucket array in the retrieval result.

**Start version**: 6.0.0(20)

#### \[h2\]OH\_Retrieval\_Retriever

typedef struct [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91)

**Description**

Defines a retriever type. The retriever serves as the handle for performing retrieval operations.

**Start version**: 6.0.0(20)

#### \[h2\]OH\_Retrieval\_SubCondition

typedef struct [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a)

**Description**

Defines sub-conditions for retrieval. Currently, only vector retrieval is supported.

**Start version**: 6.0.0(20)

#### \[h2\]OH\_Retrieval\_VectorCondition

typedef struct [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) [OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10)

**Description**

Defines a vector retrieval condition, including the retrieval parameters and filter conditions.

**Start version**: 6.0.0(20)

#### \[h2\]Retrieval\_Channel\_Type

typedef enum [Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205) [Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205)

**Description**

Defines an enum of data index types. Currently, only the vector index type is supported.

**Start version**: 6.0.0(20)

#### Enumeration Description

#### \[h2\]Retrieval\_Channel\_Type

enum [Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205)

**Description**

Enumerates data index types. Currently, only the vector index type is supported.

**Start version**: 6.0.0(20)

| 
Enumerated Value

 | 

Description

 |
| :-- | :-- |
| 

Retrieval\_TYPE\_VECTOR

 | 

Vector index.

 |

#### Function Description

#### \[h2\]OH\_Retrieval\_AddConfig()

int OH\_Retrieval\_AddConfig ([OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) \* config, [Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205) channelType, [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) \* dbConfig )

**Description**

Sets the database configuration in [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

Pointer to the instance of a retrieval configuration [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61).

 |
| 

channelType

 | 

Data index type. Currently, only vector retrieval is supported.

 |
| 

dbConfig

 | 

Pointer to the database configuration instance.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61), [Retrieval\_Channel\_Type](#gaa9bd8706c16355372cb1eb39d7148205), [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe), and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_AddSubCondition()

int OH\_Retrieval\_AddSubCondition ([OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) \* condition, [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) \* subCondition )

**Description**

Adds a sub-condition to a retrieval condition. Currently, only one sub-condition can be added.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

condition

 | 

Pointer to the instance of a retrieval condition [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e).

 |
| 

subCondition

 | 

Pointer to the instance of a sub-condition, which can be a vector retrieval condition [OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

AIP\_E\_CONDITION\_OVER\_LIMIT - The number of conditions exceeds the upper limit.

**Reference:**

[OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e), [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a), [OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10), and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_CreateCondition()

[OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e)\* OH\_Retrieval\_CreateCondition ()

**Description**

Creates a retrieval condition as the input parameter of the retrieval API.

**Start version**: 6.0.0(20)

**Returns**:

Pointer to the instance of a retrieval condition [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) if the function is successfully executed. If the function fails to be executed, the pointer is null.

**Reference:**

[OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e)

#### \[h2\]OH\_Retrieval\_CreateConfig()

[OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61)\* OH\_Retrieval\_CreateConfig ()

**Description**

Obtains the retriever configuration to initialize the retriever.

**Start version**: 6.0.0(20)

**Returns**:

Pointer to the instance of a retriever configuration [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) if the function is successfully executed. If the function fails to be executed, the pointer is null.

**Reference:**

[OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_CreateDbConfig()

[OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe)\* OH\_Retrieval\_CreateDbConfig ()

**Description**

Creates a database configuration.

**Start version**: 6.0.0(20)

**Returns**:

Pointer to the [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) instance. If the function fails to be executed, the pointer is null.

**Reference:**

[OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_CreateQuery()

[OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e)\* OH\_Retrieval\_CreateQuery ()

**Description**

Creates a retrieval keyword as the input parameter of the retrieval API.

**Start version**: 6.0.0(20)

**Returns**:

Pointer to the [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) instance if the function is successfully executed. If the function fails to be executed, the pointer is null.

**Reference:**

[OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e)

#### \[h2\]OH\_Retrieval\_CreateRetriever()

int OH\_Retrieval\_CreateRetriever (const [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) \* config, [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) \*\* retriever )

**Description**

Reads the retrieval configuration to initialize the retriever.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

Retriever configuration item [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61), which needs to be input to the retriever during its creation.

 |
| 

retriever

 | 

Pointer to the instance of a retriever [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91), [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61), and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_CreateVectorCondition()

[OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10)\* OH\_Retrieval\_CreateVectorCondition ()

**Description**

Creates a vector retrieval condition.

**Start version**: 6.0.0(20)

**Returns**:

Pointer to the instance of a retrieval condition [OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) if the function is successfully executed. If the function fails to be executed, the pointer is null.

**Reference:**

[OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10)

#### \[h2\]OH\_Retrieval\_DestroyCondition()

int OH\_Retrieval\_DestroyCondition ([OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) \* condition)

**Description**

Destroys the retrieval condition obtained through [OH\_Retrieval\_CreateCondition](#gaf596f89029870da548ab24229ab117d8).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

condition

 | 

Pointer to a retrieval condition [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e), [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417), and [OH\_Retrieval\_CreateCondition](#gaf596f89029870da548ab24229ab117d8)

#### \[h2\]OH\_Retrieval\_DestroyConfig()

int OH\_Retrieval\_DestroyConfig ([OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61) \* config)

**Description**

Destroys the retrieval configuration obtained through [OH\_Retrieval\_CreateConfig()](#ga2174e9883347dee95b57863a47b60f98).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

config

 | 

Pointer to a retrieval configuration [OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_Config](#gaf53480d04ebd0697af001a3a00f26b61), [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417), and [OH\_Retrieval\_CreateConfig](#ga2174e9883347dee95b57863a47b60f98)

#### \[h2\]OH\_Retrieval\_DestroyDbConfig()

int OH\_Retrieval\_DestroyDbConfig ([OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) \* dbConfig)

**Description**

Destroys [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) created through [OH\_Retrieval\_CreateDbConfig](#ga238499e6ca79658b59080658ad59e717).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

dbConfig

 | 

Pointer to the [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) instance.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe), [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417), and [OH\_Retrieval\_CreateDbConfig](#ga238499e6ca79658b59080658ad59e717)

#### \[h2\]OH\_Retrieval\_DestroyQuery()

int OH\_Retrieval\_DestroyQuery ([OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) \* query)

**Description**

Destroys the retrieval keyword obtained through [OH\_Retrieval\_CreateQuery](#gad5182c984d2e5d85171fd93205ea785f).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

query

 | 

Pointer to a retrieval keyword [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e), [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417), and [OH\_Retrieval\_CreateQuery](#gad5182c984d2e5d85171fd93205ea785f)

## OH\_Retrieval\_DestroyRecord()

int OH\_Retrieval\_DestroyRecord ([OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) \* record)

**Description**

Destroys the retrieval result obtained through the retrieval API [OH\_Retrieval\_Retrieve](#ga9b5b65705a02d8817f65dd01955cfe77).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

record

 | 

Pointer to a retrieval result [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952), [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417), and [OH\_Retrieval\_Retrieve](#ga9b5b65705a02d8817f65dd01955cfe77)

#### \[h2\]OH\_Retrieval\_DestroyRetriever()

int OH\_Retrieval\_DestroyRetriever ([OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) \* retriever)

**Description**

Destroys the retriever obtained through [OH\_Retrieval\_CreateRetriever](#gac6d2c1dd3039a0ac1a6996435600a81b).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

retriever

 | 

Pointer to a retriever [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91), [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417), and [OH\_Retrieval\_CreateRetriever](#gac6d2c1dd3039a0ac1a6996435600a81b)

#### \[h2\]OH\_Retrieval\_DestroySubCondition()

int OH\_Retrieval\_DestroySubCondition ([OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) \* condition)

**Description**

Destroys a sub-condition.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

condition

 | 

Pointer to a retrieval sub-condition [OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_SubCondition](#gabf02dc24d39de7926dd144966984b06a) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_DestroyVectorCondition()

int OH\_Retrieval\_DestroyVectorCondition ([OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) \* condition)

**Description**

Destroys the retrieval condition obtained through [OH\_Retrieval\_CreateVectorCondition](#ga9ba9d25126a97b67197b3f7b6fa90bfc).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

condition

 | 

Pointer to a vector retrieval condition [OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10).

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10), [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417), and [OH\_Retrieval\_CreateVectorCondition](#ga9ba9d25126a97b67197b3f7b6fa90bfc)

#### \[h2\]OH\_Retrieval\_GetItemSize()

int OH\_Retrieval\_GetItemSize (const [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) \* items, const char \* fieldName, size\_t \* size )

**Description**

Obtains the size of the value of a specified field in the database bucket array [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f). The **size** value contains the null terminator.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

items

 | 

Pointer to the instance of a database bucket array [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f).

 |
| 

fieldName

 | 

Name of the database bucket field.

 |
| 

size

 | 

Size of the value of a database bucket field.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

AIP\_E\_NO\_SUCH\_FIELD - The field does not exist.

**Reference:**

[OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_GetItemText()

int OH\_Retrieval\_GetItemText (const [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) \* items, const char \* fieldName, char \* value, size\_t size )

**Description**

Obtains the value of a specified field in the database bucket array [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

items

 | 

Pointer to the instance of a database bucket array [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f).

 |
| 

fieldName

 | 

Name of the database bucket field.

 |
| 

value

 | 

Value of the database bucket field.

 |
| 

size

 | 

Size of the value of a database bucket field.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

AIP\_E\_NO\_SUCH\_FIELD - The field does not exist.

AIP\_E\_IS\_NULL - A null value exists in the database.

**Reference:**

[OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_GetRecordItem()

int OH\_Retrieval\_GetRecordItem (const [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) \* record, uint32\_t index, const [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) \*\* item )

**Description**

Obtains the database bucket array in the retrieval result [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

record

 | 

Pointer to the instance of a retrieval result [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952).

 |
| 

index

 | 

Index value of the **record** array. The maximum value is **999**.

 |
| 

item

 | 

Pointer to a single element [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f) in the **record** array.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

AIP\_E\_OUT\_OF\_RANGE - The index is out of range.

**Reference:**

[OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952), [OH\_Retrieval\_RecordItem](#gab0ce809958f4e406378fe926a8a9269f), and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_GetRecordLength()

int OH\_Retrieval\_GetRecordLength (const [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) \* record, uint32\_t \* length )

**Description**

Obtains the database bucket array in the retrieval result [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

record

 | 

Pointer to the instance of a retrieval result [OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952).

 |
| 

length

 | 

Length of the database bucket array.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_Record](#ga3d8c3ba973c81dc8f510a69bc6f3a952) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_Retrieve()

int OH\_Retrieval\_Retrieve (const [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) \* retriever, const [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) \* query, const [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) \* condition, void \* context, const [OH\_Retrieval\_Callback](#gaf0f9144574f545243e2a035c0805b7d6) \* callback )

**Description**

Performs retrieval. After obtaining the retriever handle, input the retrieval keyword and perform retrieval based on the retrieval condition to obtain the retrieval result. During the API call, temporary cache files are generated under the path **/data/storage/el2/base/cache**. For phones or tablets, this API supports inverted indexing only and does not support vector retrieval.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

retriever

 | 

Retriever handle, which is a pointer to the [OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91) instance.

 |
| 

query

 | 

Retrieval keyword, which is a pointer to the [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) instance.

 |
| 

condition

 | 

Retrieval condition, which is a pointer to the [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e) instance.

 |
| 

context

 | 

Context data provided by a user. The data will be passed back to the function during subsequent calls.

 |
| 

callback

 | 

Pointer to the [OH\_Retrieval\_Callback](#gaf0f9144574f545243e2a035c0805b7d6) instance.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_EXEC\_ERR - An execution error occurred.

AIP\_E\_OUT\_OF\_RANGE - The index is out of range.

AIP\_E\_NO\_SUCH\_FIELD - The field does not exist.

AIP\_E\_OVER\_LIMIT - The array length exceeds the maximum.

AIP\_E\_CONDITION\_OVER\_LIMIT - The number of conditions exceeds the upper limit.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

AIP\_E\_EMBEDDING\_ERR - Failed to generate an embedding vector.

**Reference:**

[OH\_Retrieval\_Retriever](#gadd0ee87ef07f39395b03ff4db042aa91), [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e), [OH\_Retrieval\_Condition](#gab273fa3774c357b746a8b1f3d223022e), [OH\_Retrieval\_Callback](#gaf0f9144574f545243e2a035c0805b7d6), and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_SetDbConfig()

int OH\_Retrieval\_SetDbConfig ([OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) \* dbConfig, [OH\_Rdb\_ConfigV2](../../../../arkdata/c-apis/structs/oh-rdb-configv2/document.md) \* rdbConfig )

**Description**

Sets the database configuration in [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

dbConfig

 | 

Pointer to the [OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe) instance.

 |
| 

rdbConfig

 | 

Pointer to the database configuration instance, which may be the [OH\_Rdb\_ConfigV2](../../../../arkdata/c-apis/structs/oh-rdb-configv2/document.md) instance.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_DbConfig](#ga9e93c397a65a6e6438cee50e3166f0fe), [OH\_Rdb\_ConfigV2](../../../../arkdata/c-apis/structs/oh-rdb-configv2/document.md), and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_SetOriginalQuestion()

int OH\_Retrieval\_SetOriginalQuestion ([OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) \* query, const char \* question )

**Description**

Sets the retrieval keyword in [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e).

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

query

 | 

Pointer to the instance of a retrieval keyword [OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e).

 |
| 

question

 | 

Question in plaintext.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

AIP\_E\_OVER\_LIMIT - The array length exceeds the maximum.

**Reference:**

[OH\_Retrieval\_Query](#ga754a8a9b14076a9cfd7be8dacbcae38e) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_SetSimilarityThreshold()

int OH\_Retrieval\_SetSimilarityThreshold ([OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) \* condition, double threshold )

**Description**

Sets the similarity threshold of vector retrieval in a retrieval condition.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

condition

 | 

Pointer to the instance of a retrieval condition [OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10).

 |
| 

threshold

 | 

Cosine similarity threshold of vector retrieval. The value range is \[0, 1\].

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)

#### \[h2\]OH\_Retrieval\_SetVectorRecallLimit()

int OH\_Retrieval\_SetVectorRecallLimit ([OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) \* condition, uint32\_t limit )

**Description**

Sets the maximum number of vector retrieval results in the retrieval conditions.

**Start version**: 6.0.0(20)

**Parameters**:

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

condition

 | 

Pointer to the instance of a retrieval condition [OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10).

 |
| 

limit

 | 

Maximum number of vector retrieval results. The maximum value is **1000**.

 |

**Returns**:

Execution status of the function. **AIP\_OK** will be returned if the function is successfully executed.

AIP\_OK - The function is successfully executed.

AIP\_E\_INVALID\_ARGS - Invalid parameter.

**Reference:**

[OH\_Retrieval\_VectorCondition](#ga7d0df66cb913d5948c58223864774b10) and [OH\_Aip\_ErrCode](../aip/document.md#ga1eb26b856dc8a8f5ed5c815f9a4b3417)
