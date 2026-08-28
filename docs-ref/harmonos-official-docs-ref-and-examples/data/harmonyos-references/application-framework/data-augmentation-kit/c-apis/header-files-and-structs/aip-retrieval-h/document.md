# aip\_retrieval.h

#### Overview

Provides APIs related to knowledge retrieval.

**Library**: libnative\_aip\_retrieval\_ndk.so

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

**Related module**: [Retrieval](../../modules/retrieval/document.md)

#### Summary

#### \[h2\]Types

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [OH\_Retrieval\_Retriever](../../modules/retrieval/document.md#gadd0ee87ef07f39395b03ff4db042aa91) [OH\_Retrieval\_Retriever](../../modules/retrieval/document.md#gadd0ee87ef07f39395b03ff4db042aa91)

 | 

Defines a retriever type. The retriever serves as the handle for performing retrieval operations.

 |
| 

typedef struct [OH\_Retrieval\_Config](../../modules/retrieval/document.md#gaf53480d04ebd0697af001a3a00f26b61) [OH\_Retrieval\_Config](../../modules/retrieval/document.md#gaf53480d04ebd0697af001a3a00f26b61)

 | 

Defines a retriever configuration.

 |
| 

typedef struct [OH\_Retrieval\_DbConfig](../../modules/retrieval/document.md#ga9e93c397a65a6e6438cee50e3166f0fe) [OH\_Retrieval\_DbConfig](../../modules/retrieval/document.md#ga9e93c397a65a6e6438cee50e3166f0fe)

 | 

Defines a database configuration.

 |
| 

typedef enum [Retrieval\_Channel\_Type](../../modules/retrieval/document.md#gaa9bd8706c16355372cb1eb39d7148205) [Retrieval\_Channel\_Type](../../modules/retrieval/document.md#gaa9bd8706c16355372cb1eb39d7148205)

 | 

Defines an enum of data index types. Currently, only the vector index type is supported.

 |
| 

typedef void(\* [OH\_Retrieval\_Callback](../../modules/retrieval/document.md#gaf0f9144574f545243e2a035c0805b7d6)) (void \*context, [OH\_Retrieval\_Record](../../modules/retrieval/document.md#ga3d8c3ba973c81dc8f510a69bc6f3a952) \*record, int errCode)

 | 

Defines the callback function for returning a retrieval result.

 |

#### \[h2\]Enums

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[Retrieval\_Channel\_Type](../../modules/retrieval/document.md#gaa9bd8706c16355372cb1eb39d7148205) { RETRIEVAL\_TYPE\_VECTOR = 1 }

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

int [OH\_Retrieval\_CreateRetriever](../../modules/retrieval/document.md#gac6d2c1dd3039a0ac1a6996435600a81b) (const [OH\_Retrieval\_Config](../../modules/retrieval/document.md#gaf53480d04ebd0697af001a3a00f26b61) \*config, [OH\_Retrieval\_Retriever](../../modules/retrieval/document.md#gadd0ee87ef07f39395b03ff4db042aa91) \*\*retriever)

 | 

Reads the retrieval configuration to initialize the retriever.

 |
| 

int [OH\_Retrieval\_DestroyRetriever](../../modules/retrieval/document.md#ga1dc6c697ce9b8ff2a5901e154a7aae16) ([OH\_Retrieval\_Retriever](../../modules/retrieval/document.md#gadd0ee87ef07f39395b03ff4db042aa91) \*retriever)

 | 

Destroys the retriever obtained through [OH\_Retrieval\_CreateRetriever](../../modules/retrieval/document.md#gac6d2c1dd3039a0ac1a6996435600a81b).

 |
| 

[OH\_Retrieval\_Config](../../modules/retrieval/document.md#gaf53480d04ebd0697af001a3a00f26b61) \* [OH\_Retrieval\_CreateConfig](../../modules/retrieval/document.md#ga2174e9883347dee95b57863a47b60f98) ()

 | 

Obtains the retriever configuration to initialize the retriever.

 |
| 

int [OH\_Retrieval\_DestroyConfig](../../modules/retrieval/document.md#gaf7646a7caa380dcfaff025669c8336b9) ([OH\_Retrieval\_Config](../../modules/retrieval/document.md#gaf53480d04ebd0697af001a3a00f26b61) \*config)

 | 

Destroys the retrieval configuration obtained through [OH\_Retrieval\_CreateConfig](../../modules/retrieval/document.md#ga2174e9883347dee95b57863a47b60f98).

 |
| 

[OH\_Retrieval\_DbConfig](../../modules/retrieval/document.md#ga9e93c397a65a6e6438cee50e3166f0fe) \* [OH\_Retrieval\_CreateDbConfig](../../modules/retrieval/document.md#ga238499e6ca79658b59080658ad59e717) ()

 | 

Creates a configuration to open the database.

 |
| 

int [OH\_Retrieval\_DestroyDbConfig](../../modules/retrieval/document.md#ga08500cc36d88c15fc0e45e98a2534681) ([OH\_Retrieval\_DbConfig](../../modules/retrieval/document.md#ga9e93c397a65a6e6438cee50e3166f0fe) \*dbConfig)

 | 

Destroys [OH\_Retrieval\_DbConfig](../../modules/retrieval/document.md#ga9e93c397a65a6e6438cee50e3166f0fe) created by [OH\_Retrieval\_CreateDbConfig](../../modules/retrieval/document.md#ga238499e6ca79658b59080658ad59e717).

 |
| 

int [OH\_Retrieval\_SetDbConfig](../../modules/retrieval/document.md#gab69fc668e86d62c8e2f1cfdfc29de12e) ([OH\_Retrieval\_DbConfig](../../modules/retrieval/document.md#ga9e93c397a65a6e6438cee50e3166f0fe) \*dbConfig, [OH\_Rdb\_ConfigV2](../../../../arkdata/c-apis/structs/oh-rdb-configv2/document.md) \*rdbConfig)

 | 

Sets the database configuration in [OH\_Retrieval\_DbConfig](../../modules/retrieval/document.md#ga9e93c397a65a6e6438cee50e3166f0fe).

 |
| 

int [OH\_Retrieval\_AddConfig](../../modules/retrieval/document.md#ga217ef10e651eb8ed7e85fd5099c21939) ([OH\_Retrieval\_Config](../../modules/retrieval/document.md#gaf53480d04ebd0697af001a3a00f26b61) \*config, [Retrieval\_Channel\_Type](../../modules/retrieval/document.md#gaa9bd8706c16355372cb1eb39d7148205) channelType, [OH\_Retrieval\_DbConfig](../../modules/retrieval/document.md#ga9e93c397a65a6e6438cee50e3166f0fe) \*dbConfig)

 | 

Sets the database configuration in [OH\_Retrieval\_Config](../../modules/retrieval/document.md#gaf53480d04ebd0697af001a3a00f26b61).

 |
| 

int [OH\_Retrieval\_Retrieve](../../modules/retrieval/document.md#ga9b5b65705a02d8817f65dd01955cfe77) (const [OH\_Retrieval\_Retriever](../../modules/retrieval/document.md#gadd0ee87ef07f39395b03ff4db042aa91) \*retriever, const [OH\_Retrieval\_Query](../../modules/retrieval/document.md#ga754a8a9b14076a9cfd7be8dacbcae38e) \*query, const [OH\_Retrieval\_Condition](../../modules/retrieval/document.md#gab273fa3774c357b746a8b1f3d223022e) \*condition, void \*context, const [OH\_Retrieval\_Callback](../../modules/retrieval/document.md#gaf0f9144574f545243e2a035c0805b7d6) \*callback)

 | 

Performs retrieval. After obtaining the retriever handle, input the retrieval keyword and perform retrieval based on the retrieval condition to obtain the retrieval result.

 |
