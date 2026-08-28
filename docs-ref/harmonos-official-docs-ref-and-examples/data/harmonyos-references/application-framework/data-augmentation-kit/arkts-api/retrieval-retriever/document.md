# retrieval (Retriever)

The ArkData Intelligence Platform (AIP) provides on-device data intelligence capabilities, enabling AI-powered data processing on devices. To underpin AI-powered processing on devices, the AIP supports the following capabilities:

-   Multimodal embedding model: leverages embedding models to generate vector representations for multimodal data, mapping text, images, and other data into a unified vector space for semantic-based multimodal knowledge retrieval.
-   Multimodal data storage: supports on-device storage for vectors, inverted indexes, and other multimodal data, eliminating the need to send raw data to the server for processing. This reduces the risk of data leakage.
-   Knowledge retrieval: enables semantic-based retrieval of user knowledge based on functions such as semantic indexing, knowledge graphs, recall, and re-ranking.
-   Knowledge generation and collation: implements efficient data organization and knowledge generation based on user data such as user documents, messages, emails, photos, videos, calendar events, and screen context, enabling the transformation of data into knowledge.
    
    **Start version**: 6.0.0(20)
    

#### Module Import

import { retrieval } from '@kit.DataAugmentationKit';

#### getRetriever

getRetriever(config: RetrievalConfig): Promise<Retriever>

Obtains the retriever to perform multi-channel retrieval and recall. This API returns the result asynchronously through a promise.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

config

 | 

[RetrievalConfig](#section95236010016)

 | 

Yes

 | 

Retriever configuration information.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[Retriever](#section11926161314172)\>

 | 

Promise used to return the retriever object.

 |

**Example:**

import { retrieval } from '@kit.DataAugmentationKit';
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page {
  async retrieve() {
    let vectorDBConfig:retrieval.DbConfig = {
      name:"vector\_store\_test.db",
      securityLevel:relationalStore.SecurityLevel.S3
    }

    let invidxDBConfig:retrieval.DbConfig = {
      name:"invidx\_store\_test.db",
      securityLevel:relationalStore.SecurityLevel.S3
    }
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context == undefined) {
      console.info("getHostContext failed.");
      return;
    }
    let channelConfigVector:retrieval.ChannelConfig = {
      channelType:retrieval.ChannelType.VECTOR\_DATABASE,
      context:context,
      dbConfig:vectorDBConfig
    }

    let channelConfigInvIdx:retrieval.ChannelConfig = {
      channelType:retrieval.ChannelType.INVERTED\_INDEX\_DATABASE,
      context:context,
      dbConfig:invidxDBConfig
    }

    let retrievalConfig:retrieval.RetrievalConfig = {
      channelConfigs:\[channelConfigInvIdx, channelConfigVector\]
    }

    let globalRetriever:retrieval.Retriever | undefined;
    // Obtain the retriever.
    await retrieval.getRetriever(retrievalConfig)
      .then((retriever:retrieval.Retriever) => {
        globalRetriever = retriever;
        console.info("globalRetriever is success");
      })
      .catch((err:BusinessError) => {
        globalRetriever = undefined;
        console.error("Failed to get Retriever and code is " + err.code);
      })
  }

  build() {
  }
}

#### RetrievalConfig

Recall configurations.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

channelConfigs

 | 

Array<[ChannelConfig](#section14132649320)\>

 | 

Yes

 | 

Array of configuration information of different retrieval channels.

 |

#### ChannelConfig

Configurations of retrieval channels.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

channelType

 | 

[ChannelType](#section15391712641)

 | 

No

 | 

No

 | 

Database type of the current retrieval channel.

 |
| 

context

 | 

[common.BaseContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

No

 | 

No

 | 

App context.

App context of the FA model.

App context of the stage model.

 |
| 

dbConfig

 | 

[DbConfig](#section175721121461)

 | 

No

 | 

No

 | 

Database configuration of the current retrieval channel.

 |

#### ChannelType

Enumerated values of the database type.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

VECTOR\_DATABASE

 | 

0

 | 

Vector database.

 |
| 

INVERTED\_INDEX\_DATABASE

 | 

1

 | 

Inverted index database.

 |

#### DbConfig

type DbConfig = relationalStore.StoreConfig

Database configurations.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[relationalStore.StoreConfig](../../../arkdata/arkts-apis/ohos-data-relationalstore-rdb-store/interfaces-others/document.md#storeconfig)

 | 

Database configurations.

 |

#### Retriever

Retriever, which is used to perform multi-channel retrieval and recall.

Before calling any of the following APIs, you must obtain a retriever instance by using [retrieval.getRetriever](#section48951613820).

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

#### \[h2\]retrieveRdb

retrieveRdb(query: string, condition: RetrievalCondition): Promise<RdbRecords>

Retrieves data that meets the retrieval conditions (including the query word segmentation and recall conditions) from a relational database (RDB). This API uses a promise to return the result asynchronously.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

query

 | 

string

 | 

Yes

 | 

Query keyword for the current retrieval.

 |
| 

condition

 | 

[RetrievalCondition](#section4881955192413)

 | 

Yes

 | 

Retrieval condition.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RdbRecords](#section7831184215917)\>

 | 

Promise used to return the retrieval results.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1021200001](../../arkts-api-error-codes/document.md#section1695152585411)

 | 

The database is corrupted.

 |
| 

[1021200002](../../arkts-api-error-codes/document.md#section18285155115599)

 | 

The database is closed.

 |
| 

[1021200003](../../arkts-api-error-codes/document.md#section10228950523)

 | 

The database is busy.

 |
| 

[1021200004](../../arkts-api-error-codes/document.md#section1512434117512)

 | 

The database is out of memory.

 |
| 

[1021200100](../../arkts-api-error-codes/document.md#section20133860106)

 | 

SQLite: Generic error.

 |
| 

[1021200101](../../arkts-api-error-codes/document.md#section6749146131611)

 | 

SQLite: Access permission denied.

 |
| 

[1021200102](../../arkts-api-error-codes/document.md#section17536341132517)

 | 

SQLite: The database file is locked.

 |
| 

[1021200103](../../arkts-api-error-codes/document.md#section81851635102918)

 | 

SQLite: Some kind of disk I/O error occurred.

 |
| 

[1021200104](../../arkts-api-error-codes/document.md#section0489154433217)

 | 

SQLite: The WAL file size exceeds the default limit.

 |
| 

[1021200105](../../arkts-api-error-codes/document.md#section193661963369)

 | 

SQLite: Unable to open the database file.

 |
| 

[1021201000](../../arkts-api-error-codes/document.md#section4447164716181)

 | 

Retrieval: An error occurred during the recall phase.

 |
| 

[1021201001](../../arkts-api-error-codes/document.md#section6203196115413)

 | 

Retrieval: An error occurred during the re-ranking phase.

 |
| 

[1021201002](../../arkts-api-error-codes/document.md#section68301510501)

 | 

Retrieval: The value of the numerical parameter is outside the constrained range.

 |
| 

[1021201003](../../arkts-api-error-codes/document.md#section113966140913)

 | 

Retrieval: There are invalid primary keys.

 |
| 

[1021201004](../../arkts-api-error-codes/document.md#section1917152417155)

 | 

Retrieval: A re-ranking algorithm that does not support composite primary keys was used.

 |
| 

[1021201005](../../arkts-api-error-codes/document.md#section168621258121819)

 | 

Retrieval: There are fields with empty strings.

 |
| 

[1021201006](../../arkts-api-error-codes/document.md#section15711102132214)

 | 

Retrieval: The filter input is invalid.

 |
| 

[1021201007](../../arkts-api-error-codes/document.md#section151721752182519)

 | 

Retrieval: There are invalid recall names in RecallCondition.

 |
| 

[1021201008](../../arkts-api-error-codes/document.md#section2545133262914)

 | 

Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter.

 |
| 

[1021201009](../../arkts-api-error-codes/document.md#section17815414203313)

 | 

Retrieval: RerankMethod parameters do not match the channel type.

 |
| 

[1021201010](../../arkts-api-error-codes/document.md#section18940016203611)

 | 

Retrieval: There exists a parameter value that should not be empty but is actually empty

 |
| 

[1021200012](../../arkts-api-error-codes/document.md#section2851182812325)

 | 

Unable to generate embeddings.

 |

**Example:**

import { retrieval } from '@kit.DataAugmentationKit';
import { relationalStore } from '@kit.ArkData';
import { BusinessError } from '@kit.BasicServicesKit';

@Entry
@Component
struct Page {
 
async retrieve() {
    let vectorDBConfig:retrieval.DbConfig = {
      name:"vector\_test.db",
      securityLevel:relationalStore.SecurityLevel.S3
    }

    let invidxDBConfig:retrieval.DbConfig = {
      name:"files\_test.db",
      securityLevel:relationalStore.SecurityLevel.S3
    }
    let context: Context | undefined = this.getUIContext().getHostContext();
    if (context == undefined) {
      console.info("getHostContext failed.");
      return;
    }
    let channelConfigVector:retrieval.ChannelConfig = {
      channelType:retrieval.ChannelType.VECTOR\_DATABASE,
      context:context,
      dbConfig:vectorDBConfig
    }

    let channelConfigInvIdx:retrieval.ChannelConfig = {
      channelType:retrieval.ChannelType.INVERTED\_INDEX\_DATABASE,
      context:context,
      dbConfig:invidxDBConfig
    }

    let retrievalConfig:retrieval.RetrievalConfig = {
      channelConfigs:\[channelConfigInvIdx, channelConfigVector\]
    }

    let globalRetriever:retrieval.Retriever | undefined;
    await retrieval.getRetriever(retrievalConfig)
      .then((retriever:retrieval.Retriever) => {
        globalRetriever = retriever;
        console.info("globalRetriever is success");
      })
      .catch((err:BusinessError) => {
        globalRetriever = undefined;
        console.error("Failed to get Retriever and code is " + err.code);
      })

    let fieldWeight:Record<string, number> = {
      "filename":4.0
    }

    let fieldSlops:Record<string, number> = {
      "filename":5
    }

    let bm25Strategy:retrieval.Bm25Strategy = {
      bm25Weight:1.5,
      columnWeight:fieldWeight
    }

    let exactStrategy:retrieval.ExactMatchingStrategy = {
      exactMatchingWeight:1.2,
      columnWeight:fieldWeight
    }

    let outOfOrderStrategy:retrieval.ProximityStrategy = {
      proximityWeight:1.0,
      columnWeight:fieldWeight,
      columnSlops:fieldSlops
    }

    let invertedIndexStrategies:Array<retrieval.InvertedIndexStrategy> = \[bm25Strategy, exactStrategy, outOfOrderStrategy\]

    let recallConditionInvIdx:retrieval.InvertedIndexRecallCondition ={
      ftsTableName:"files",
      primaryKey:\["fileid"\],
      fromClause:"files",
      responseColumns:\["fileid", "filename", "keywords"\],
      deepSize:2,
      invertedIndexStrategies:invertedIndexStrategies,
      recallName:"invIdxRecall"
    }

    // Modify the query representation vector specified for **floatArray** based on the service requirements.
    let floatArray = new Float32Array(\[0.006954, -0.079041, 0.046173, 0.157959, -0.017212, 0.037018, -0.072083, -0.028488, -0.099854, 0.044037, -0.008911, -0.063049, 0.035950, -0.105835, 0.057739, 0.060364, -0.062042, 0.044159, 0.143188, 0.123901, -0.069641, -0.061920, -0.086731, -0.092468, 0.092957, -0.027649, -0.005497, -0.039276, 0.017502, -0.046570, -0.115906, 0.081177, -0.153931, -0.040588, 0.123474, -0.099060, 0.062042, 0.026352, -0.041382, -0.099548, 0.071167, -0.120850, 0.082642, 0.026398, -0.035614, -0.008545, -0.076660, -0.031067, 0.192017, -0.052582, 0.005310, 0.052734, 0.199463, 0.075195, -0.070740, -0.035950, 0.073120, 0.089172, 0.075989, 0.003582, 0.050201, -0.012787, 0.016647, -0.053619, 0.001906, -0.060181, -0.068359, -0.114502, -0.045013, 0.004547, -0.004673, -0.148071, 0.126343, 0.019394, -0.063110, -0.055908, 0.071228, 0.002369, 0.041412, 0.126709, -0.053467, 0.127808, 0.055420, 0.206177, 0.002169, -0.001452, 0.095520, -0.042511, 0.099243, -0.164185, 0.093384, -0.014618, -0.129150, -0.238770, -0.085327, 0.051300, -0.020004, 0.010063, -0.084351, -0.003567, 0.064941, -0.205322, -0.158936, -0.074768, 0.104370, 0.197021, -0.080688, -0.066772, -0.036346, 0.034912, -0.019760, 0.110474, 0.128662, 0.094727, 0.024948, -0.033356, -0.081848, 0.054474, -0.065857, -0.156494, 0.002527, 0.097595, -0.027420, 0.039185, 0.063965, 0.220093, 0.029556, -0.115417\]);

    let vectorQuery:retrieval.VectorQuery = {
      column:"keywords",
      value:floatArray,
      similarityThreshold:0.35
    }

    let recallConditionVector:retrieval.VectorRecallCondition = {
      vectorQuery:vectorQuery,
      fromClause:"vector",
      primaryKey:\["fileid"\],
      responseColumns:\["filename\_text", "filename", "int64\_value", "double\_value", "bool\_value", "blob\_value"\],
      recallName:"vectorRecall",
      deepSize:2
    }

    let vectorWeights:Record<string, number> = {
      "vectorRecall":0.5
    }

    let invidxWeights:Record<string, number> = {
      "vectorRecall":0.5
    }

    let vectorRerankParameter:retrieval.VectorRerankParameter = {
      vectorWeights:vectorWeights,
      thresholds:\[0.55, 0.45\]
    }

    let invidxRerankParameter:retrieval.InvertedIndexRerankParameter = {
      invertedIndexWeights:invidxWeights,
    }

    let parameters:Record<retrieval.ChannelType, retrieval.RerankParameter> = {
      0:vectorRerankParameter,
      1:invidxRerankParameter
    }

    let rerankMethod:retrieval.RerankMethod = {
      rerankType:retrieval.RerankType.RRF,
      parameters:parameters,
      isSoftmaxNormalized:true
    }

    let groundTruthIds: Array<string> = \['1','2', '3'\];
    let explain : retrieval.ExplanationConfig ={
      groundTruths: groundTruthIds
    }

    let retrievalCondition:retrieval.RetrievalCondition = {
      rerankMethod:rerankMethod,
      recallConditions:\[recallConditionInvIdx, recallConditionVector\],
      resultCount:2,
      explanation:explain
    }

    if (globalRetriever != undefined) {
      let query:string = "Sports Live";
      // Perform retrieval.
      globalRetriever.retrieveRdb(query, retrievalCondition)
        .then((rdbdata:retrieval.RdbRecords) => {

          console.info(\`#########  retrieval result ############\`);
          for (let i = 0; i < rdbdata.records.length; i++) {
            console.info(\` primaryKey is ${rdbdata.records\[i\].primaryKey}\`);
            Object.keys(rdbdata.records\[i\].columns).forEach((key) => {
              if (rdbdata.records && rdbdata.records\[i\]) {
                let value = rdbdata.records\[i\].columns\[key\];
                console.info(\`recall Scores Key: ${key}, Value: ${value}\`);
              }
            });
            console.info(\`score is ${rdbdata.records\[i\].score}\`);

            Object.keys(rdbdata.records\[i\].recallScores).forEach((channelType) => {
              if (rdbdata.records) {
                let scores:Record<string, retrieval.RecallScore>  = rdbdata.records\[i\].recallScores\[channelType\];
                Object.keys(scores).forEach((key)=>{
                  let value = scores\[key\];
                  console.info(\`recall Scores channelType is ${channelType}, Key: ${key}, score: ${value.score}\`);
                });
              }
            });
            console.info("recall Scores", rdbdata.records\[i\].recallScores.toString());
            Object.keys(rdbdata.records\[i\].features).forEach((key) => {
              if (rdbdata.records && rdbdata.records\[i\]) {
                let value = rdbdata.records\[i\].features\[key\];
                console.info(\`features Key: ${key}, Value: ${value}\`);
              }
            });
            console.info(\`similarityLevel is ${rdbdata.records\[i\].similarityLevel}\`);

          }

          console.info(\`#########  missdGroundTruthsPrimaryKey ############\`);
          if(rdbdata.missedGroundTruths != undefined && rdbdata.missedGroundTruths.length != 0){
            for (let i = 0; i < rdbdata.missedGroundTruths.length; i++) {
              console.info(\`missdGroundTruthsPrimaryKey is ${rdbdata.missedGroundTruths\[i\].primaryKey}\`);
              Object.keys(rdbdata.missedGroundTruths\[i\].columns).forEach((key) => {
                if (rdbdata.missedGroundTruths && rdbdata.missedGroundTruths\[i\]) {
                  let value = rdbdata.missedGroundTruths\[i\].columns\[key\];
                  console.info(\`missdGroundTruths recall Scores Key: ${key}, Value: ${value}\`);
                }
              });
              console.info(\` missdGroundTruths score is ${rdbdata.missedGroundTruths\[i\].score}\`);

              Object.keys(rdbdata.missedGroundTruths\[i\].recallScores).forEach((channelType) => {
                if (rdbdata.missedGroundTruths) {
                  let scores:Record<string, retrieval.RecallScore>  = rdbdata.missedGroundTruths\[i\].recallScores\[channelType\];
                  Object.keys(scores).forEach((key)=>{
                    let value = scores\[key\];
                    console.info(\`missdGroundTruths recall Scores channelType is ${channelType}, Key: ${key}, score: ${value.score}\`);
                  });
                }
              });
              console.info("missdGroundTruths recall Scores", rdbdata.missedGroundTruths\[i\].recallScores.toString());
              Object.keys(rdbdata.missedGroundTruths\[i\].features).forEach((key) => {
                if (rdbdata.missedGroundTruths && rdbdata.missedGroundTruths\[i\]) {
                  let value = rdbdata.missedGroundTruths\[i\].features\[key\];
                  console.info(\`missdGroundTruths features Key: ${key}, Value: ${value}\`);
                }
              });
              console.info(\`missdGroundTruths similarityLevel is ${rdbdata.missedGroundTruths\[i\].similarityLevel}\`);
            }
          }
          console.info("retrieval success.");
        })
        .catch((err:BusinessError) => {
          console.error("Failure in retrieveRdb and code is " + err.code);
        })
    }
  }

  build() {
  }
}

#### RetrievalCondition

Retrieval condition.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

recallConditions

 | 

Array<[RecallCondition](#section2068311124267)\>

 | 

No

 | 

No

 | 

Recall conditions. Each element in the array corresponds to a recall operation.

 |
| 

rerankMethod

 | 

[RerankMethod](#section17423103217511)

 | 

No

 | 

Yes

 | 

Re-ranking method. The default value of **rerankType** is the RRF algorithm, and the value of **parameters** follows the retrieval channel settings in [RecallCondition](#section2068311124267).

 |
| 

resultCount

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of results that can be returned after re-ranking. The default value is **500**. The value must be a positive integer.

 |
| 

explanation

 | 

[ExplanationConfig](#section942016410511)

 | 

No

 | 

Yes

 | 

Retrieval explanation.

 |

#### ExplanationConfig

Retrieval explanation configuration.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

groundTruths

 | 

Array<string>

 | 

No

 | 

No

 | 

ID of the document to be explained. The value is a random character string.

 |

#### Recallcondition

type RecallCondition = InvertedIndexRecallCondition | VectorRecallCondition

Recall conditions.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[InvertedIndexRecallCondition](#section0840134782711)

 | 

Inverted index recall conditions.

 |
| 

[VectorRecallCondition](#section570264064815)

 | 

Vector recall conditions.

 |

#### InvertedIndexRecallCondition

Inverted index recall conditions.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

ftsTableName

 | 

string

 | 

No

 | 

No

 | 

Name of the full-text search (FTS) data table used for inverted index retrieval, which is used as the input for executing the BM25 function. The value must be an existing table name and cannot be an empty string.

 |
| 

fromClause

 | 

string

 | 

No

 | 

No

 | 

Name of the query target index. The value cannot be an empty string.

The table specified by **fromClause** contains all fields involved in **filters**. Two types of values are allowed for these fields:

1.  The same value as that of **ftsTableName**. In this case, the inverted index retrieval is performed only in the inverted index table.
2.  A value in a complete format of a **select...join** statement to connect the element table other than the FTS table as the retrieval table. (In this case, the **select** statement must contain the **rowid** field, and this field must be from the FTS table. For example, if **ftsTableName** is **files** and the element table metadata needs to be filtered, **fromClause** must be defined as follows: **"SELECT files.rowid as rowid, \* FROM metadata JOIN files ON metadata.fileid = files.fileid"**.)

 |
| 

primaryKey

 | 

Array<[ColumnName](#section7132115012719)\>

 | 

No

 | 

No

 | 

Primary key field of the recall result, which is used as one of the recall fields for aggregating the documents recalled in multiple channels. The number of primary key fields for each recall operation in a query must be the same and the fields cannot be empty.

 |
| 

responseColumns

 | 

Array<[ColumnName](#section7132115012719)\>

 | 

No

 | 

No

 | 

Set of fields that need to be recalled additionally. In **Array<[ColumnName](#section7132115012719)\>**, [ColumnName](#section7132115012719) cannot be empty.

 |
| 

invertedIndexStrategies

 | 

Array<[InvertedIndexStrategy](#section5878123034110)\>

 | 

No

 | 

Yes

 | 

Recall strategy list, which determines how the inverted index table is scored. If this parameter is left empty, full table matching is performed by default.

 |
| 

recallName

 | 

[RecallName](#section191097472303)

 | 

No

 | 

Yes

 | 

Name of the current retrieval channel, which is used to identify the re-ranking phase. The default value is a random character string. This parameter can be left unspecified in the constructor. If this parameter is specified, the value cannot be an empty string.

 |
| 

filters

 | 

Array<[FilterInfo](#section994821153216)\>

 | 

No

 | 

Yes

 | 

Additional filter conditions.

 |
| 

deepSize

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of results that can be returned in the current recall process in the re-ranking phase. The default value is **500**. The value must be a positive integer.

 |

#### ColumnName

type ColumnName = string

Column names in data tables. The value type is string.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Type of the column name of the data table. The value is a random character string.

 |

#### RecallName

type RecallName = string

Name of an inverted index recall channel or a vector recall channel, which is a character string. If two vector recall channels are available, name both of them for differentiation.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

string

 | 

Type of a recall channel name, which is a random character string.

 |

#### FilterInfo

Filter information.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

columns

 | 

Array<[ColumnName](#section7132115012719)\>

 | 

No

 | 

No

 | 

Name of the column to be filtered.

 |
| 

operator

 | 

[Operator](#section145251311409)

 | 

No

 | 

Yes

 | 

Operator in the filter condition. The filtering function takes effect only when **operator** and at least one of the **filterValue** and **filterRange** parameters are set.

 |
| 

filterValue

 | 

[FilterValue](#section11277358123613)

 | 

No

 | 

Yes

 | 

Value in the filter condition.

 |
| 

filterRange

 | 

[FilterRange](#section1283752213396)

 | 

No

 | 

Yes

 | 

Range in the filter condition.

 |

#### FilterValue

type FilterValue = number | string | bigint

Value in the filter condition.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

number

 | 

If the received value of **FilterValue** is of the number type, the filter condition is of the number type.

 |
| 

string

 | 

If the received value of **FilterValue** is of the string type, the filter condition is of the string type.

 |
| 

bigint

 | 

If the received value of **FilterValue** is of the bigint type, the filter condition is of the int64 type.

 |

#### FilterRange

Value range in the filter condition.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

max

 | 

number

 | 

Yes

 | 

Maximum filter value.

 |
| 

min

 | 

number

 | 

Yes

 | 

Minimum filter value. The value must be less than the maximum filter value.

 |

#### Operator

Operator in the filter condition. The **column** parameter indicates the field name in the database table, and **filterValue** indicates the field value.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Operation

 | 

Description

 |
| :-- | :-- |
| 

OP\_EQ = '='

 | 

Checks whether the value of **<column>** is equal to that of **<filterValue>**.

 |
| 

OP\_NE = '!='

 | 

Checks whether the value of **<column>** is not equal to that of **<filterValue>**.

 |
| 

OP\_LT = '<'

 | 

Checks whether the value of **<column>** is less than that of **<filterValue>** (a number).

 |
| 

OP\_LE = '<='

 | 

Checks whether the value of **<column>** is less than or equal to that of **<filterValue>** (a number).

 |
| 

OP\_GT = '>'

 | 

Checks whether the value of **<column>** is greater than that of **<filterValue>** (a number).

 |
| 

OP\_GE = '>='

 | 

Checks whether the value of **<column>** is greater than or equal to that of **<filterValue>** (a number).

 |
| 

OP\_IN = 'IN'

 | 

Checks whether the value of **<column>** is contained in **<filterValue>**. The **<filterValue>** parameter is a string, in which values are separated by commas (,).

 |
| 

OP\_NOT\_IN = 'NOT\_IN'

 | 

Checks whether the value of **<column>** is not contained in **<filterValue>**. The **<filterValue>** parameter is a string, in which values are separated by commas (,).

 |
| 

OP\_BETWEEN = 'BETWEEN'

 | 

Checks whether the value of **<column>** is between **<filterRange.min>** and **<filterRange.max>**.

 |
| 

OP\_LIKE = 'LIKE'

 | 

Matches **<column>** that contains **<filterValue>** through **LIKE**, in which **<filterValue>** is a string.

 |
| 

OP\_NOT\_LIKE = 'NOT\_LIKE'

 | 

Matches **<column>** that does not contain **<filterValue>** through **NOT\_LIKE**, in which **<filterValue>** is a string.

 |

#### InvertedIndexStrategy

type InvertedIndexStrategy = Bm25Strategy | ExactMatchingStrategy | ProximityStrategy

Inverted index recall strategies.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[Bm25Strategy](#section8677153210421)

 | 

BM25 strategy. A search target can be recalled as long as it matches 80% of the core terms in the query. The recalled results are scored based on the BM25 algorithm. This strategy is suitable for scenarios with relatively lenient requirements for search target matching.

 |
| 

[ExactMatchingStrategy](#section337414149441)

 | 

Exact match strategy. A search target can only be recalled if it exactly matches the query terms. This strategy is suitable for scenarios with strict requirements for search target matching.

 |
| 

[ProximityStrategy](#section661392414468)

 | 

Unordered match strategy. The word segmentation results of the query terms do not need to appear in the search target in the original order. A search target can be recalled as long as all word segmentation results appear within a specified proximity window. This strategy is suitable for scenarios with medium requirements for search target matching.

 |

#### Bm25Strategy

BM25 strategy used for inverted index retrieval.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

bm25Weight

 | 

number

 | 

No

 | 

No

 | 

Scoring weight of the BM25 strategy, which controls the impact of the strategy on the final ranking of recalled results when multiple inverted index strategies are applied simultaneously.

 |
| 

columnWeight

 | 

Record<[ColumnName](#section7132115012719), number>

 | 

No

 | 

Yes

 | 

Fields (**ColumnName**) that the strategy applies to and weight (**number**) of each field. The weight is used to control the impact of field matching on the final result.

If **ColumnName** is left empty, the strategy applies to all fields in the inverted index table by default, and a field named the inverted index table is added, with the weight value (**number**) being **1.0**.

If **ColumnName** is not empty (namely, the value is not an empty string), the weight value is a non-negative number.

 |

#### ExactMatchingStrategy

Exact match strategy used for inverted index retrieval.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

exactMatchingWeight

 | 

number

 | 

No

 | 

No

 | 

Scoring weight of the exact match strategy, which controls the impact of the strategy on the final ranking of recalled results when multiple inverted index strategies are applied simultaneously.

 |
| 

columnWeight

 | 

Record<[ColumnName](#section7132115012719), number>

 | 

No

 | 

Yes

 | 

Fields (**ColumnName**) that the strategy applies to and weight (**number**) of each field. The weight is used to control the impact of field matching on the final result.

If **ColumnName** is left empty, the strategy applies to all fields in the inverted index table by default, and a field named the inverted index table is added, with the weight value (**number**) being **1.0**.

If **ColumnName** is not empty (namely, the value is not an empty string), the weight value is a non-negative number.

 |

#### ProximityStrategy

Unordered match strategy used for inverted index retrieval.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

proximityWeight

 | 

number

 | 

No

 | 

No

 | 

Scoring weight of the unordered match strategy, which controls the impact of the strategy on the final ranking of recalled results when multiple inverted index strategies are applied simultaneously.

 |
| 

columnWeight

 | 

Record<[ColumnName](#section7132115012719), number>

 | 

No

 | 

Yes

 | 

Fields (**ColumnName**) that the strategy applies to and weight (**number**) of each field. The weight is used to control the impact of field matching on the final result.

If **ColumnName** is left empty, the strategy applies to all fields in the inverted index table by default, and a field named the inverted index table is added, with the weight value (**number**) being **1.0**.

If **ColumnName** is not empty (namely, the value is not an empty string), the weight value is a non-negative number.

 |
| 

columnSlops

 | 

Record<[ColumnName](#section7132115012719), number>

 | 

No

 | 

Yes

 | 

Offset configuration used by each field. The default value of **ColumnName** is the same as that for **columnWeight**, and the default value of **number** is **10**. The field cannot be empty, and the value must be a non-negative number.

 |

#### VectorRecallCondition

Vector recall conditions.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

vectorQuery

 | 

[VectorQuery](#section4902165514919)

 | 

No

 | 

No

 | 

Query term vector used for vector retrieval.

 |
| 

fromClause

 | 

string

 | 

No

 | 

No

 | 

Name of the vector data table.

 |
| 

primaryKey

 | 

Array<[ColumnName](#section7132115012719)\>

 | 

No

 | 

No

 | 

Primary key field of the recall result, which is used as one of the recall fields for aggregating the documents recalled in multiple channels. The number of primary key fields for each recall operation in a query must be the same and the fields cannot be empty.

 |
| 

responseColumns

 | 

Array<[ColumnName](#section7132115012719)\>

 | 

No

 | 

No

 | 

Set of fields that need to be recalled additionally. The value of **ColumnName** cannot be empty.

 |
| 

recallName

 | 

[RecallName](#section191097472303)

 | 

No

 | 

Yes

 | 

Name of the current retrieval channel, which is used to identify the re-ranking phase. The default value is a random character string and cannot be an empty string.

 |
| 

filters

 | 

Array<[FilterInfo](#section994821153216)\>

 | 

No

 | 

Yes

 | 

Additional filter conditions.

 |
| 

deepSize

 | 

number

 | 

No

 | 

Yes

 | 

Maximum number of results returned by the recall phase to the re-ranking phase. The default value is **500**. The value must be a positive integer.

 |

#### VectorQuery

Vectors generated based on the query terms.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

column

 | 

[ColumnName](#section7132115012719)

 | 

No

 | 

No

 | 

Name of the vector field to be matched. The value must be a field of the vector type existing in the specified vector database.

 |
| 

value

 | 

Float32Array

 | 

No

 | 

Yes

 | 

Vector value in the vector column.

If the **value** field is not defined, the system attempts to generate a vector based on the original query. Currently, the value can be automatically generated on PCs.

In HarmonyOS 6.0.0 Beta2 and later versions, this parameter is changed from mandatory to optional.

 |
| 

similarityThreshold

 | 

number

 | 

No

 | 

Yes

 | 

Vector threshold, which is used to filter dissimilar vectors. The default value is **1**. The minimum value is **0**, and the maximum value is the minimum value among the valid thresholds in [VectorRerankParameter](#section2019282155815).

 |

#### RerankMethod

Re-ranking strategy parameters.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

rerankType

 | 

[RerankType](#section7916104025215)

 | 

No

 | 

No

 | 

Re-ranking algorithm, which is defined by the enumeration [RerankType](#section7916104025215). The value options include **RRF** and **FUSION\_SCORE**, indicating the RRF ranking algorithm and score fusion ranking algorithm, respectively. The default value is **RRF**.

 |
| 

parameters

 | 

Record<[ChannelType](#section15391712641), [RerankParameter](#section16017065412)\>

 | 

No

 | 

Yes

 | 

Re-ranking parameters corresponding to a recall channel. If the channel type specified for **RetrievalCondition** is not configured with re-ranking parameters in **parameters**, the default values of the re-ranking parameters corresponding to the channel type are automatically filled. For the default values of inverted index re-ranking parameters, please refer to [InvertedIndexRerankParameter](#section7927313135618). For the default values of vector re-ranking parameters, please refer to [VectorRerankParameter](#section2019282155815).

 |
| 

isSoftmaxNormalized

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to use the **softmax** function to normalize the final re-ranking score in **FUSION\_SCORE** mode. The default value is **false**. The value **true** indicates that the **softmax** function is used to normalize the final re-ranking score, and **false** indicates that the **softmax** function is not used.

 |

#### RerankType

Re-ranking algorithm types.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Type

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

RRF

 | 

0

 | 

Reciprocal Rank Fusion (RRF) method, which ranks results based on their positions from multiple recall channels.

This method is applicable to scenarios that require high result diversity and equal output of each result.

 |
| 

FUSION\_SCORE

 | 

1

 | 

Score fusion ranking method, which ranks results based on their scores from multiple recall channels. This method is applicable to scenarios that require high correlation accuracy, reliable recall scores, and stable result ranking.

 |

#### RerankParameter

type RerankParameter = InvertedIndexRerankParameter| VectorRerankParameter

Re-ranking algorithm parameter settings.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

[InvertedIndexRerankParameter](#section7927313135618)

 | 

Re-ranking parameter.

 |
| 

[VectorRerankParameter](#section2019282155815)

 | 

Re-ranking parameter.

 |

#### InvertedIndexRerankParameter

Re-ranking algorithm parameters for inverted indexes.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

invertedIndexWeights

 | 

Record<[RecallName](#section191097472303), number>

 | 

No

 | 

No

 | 

Re-ranking weight of each recall channel, which reflects the importance of each recall channel during re-ranking. The **key** parameter indicates the [RecallName](#section191097472303) in **RecallCondition** for each recall channel, and the **value** parameter indicates the weight of the corresponding recall channel.

The weight value must be a non-negative number. If the weight of a recall channel is not defined, the default value **1** is used.

 |

#### VectorRerankParameter

Re-ranking algorithm parameters for vectors.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

vectorWeights

 | 

Record<[RecallName](#section191097472303), number>

 | 

No

 | 

No

 | 

Re-ranking weight of each recall channel, which reflects the importance of each recall channel during re-ranking. The **key** parameter indicates the [RecallName](#section191097472303) in **RecallCondition** for each recall channel, and the **value** parameter indicates the weight of the corresponding recall channel. The weight value must be a non-negative number. If the weight of a recall channel is not defined, the default value **1** is used.

 |
| 

thresholds

 | 

Array<number>

 | 

No

 | 

Yes

 | 

Tiered thresholds for vector recall. Set three values in \[0, 1\] as the minimum **cosine()** similarity for high, medium, and low relevance tiers. Higher values indicate stronger relevance.

If you set two values, two thresholds are defined for the high and medium tiers. All remaining results are assigned to the low tier.

If you set one value, one threshold is defined for the high tier. All remaining results are assigned to the low tier.

If you set more than three values, only the first three values (sorted in descending order) are used, and other values are ignored. If you do not set any value, the default value \[0.6, 0.45, 0.4\] is used.

 |
| 

numberInspector

 | 

Record<[RecallName](#section191097472303), [ColumnName](#section7132115012719)\>

 | 

No

 | 

Yes

 | 

Numerical match demotion strategy configuration for vector recall. If a numerical value is present in the query but does not match the corresponding number in the target field, the relevance score of the retrieved result will be demoted. The value of **key** is the value of [RecallName](#section191097472303) in the vector recall condition, and **value** is the name of the corresponding pattern matching field. By default, this parameter is left empty.

 |

#### RdbRecords

Retrieval result.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

records

 | 

Array<[ItemInfo](#section17768581101)\>

 | 

No

 | 

No

 | 

Retrieval result.

 |
| 

missedGroundTruths

 | 

Array<[ItemInfo](#section17768581101)\>

 | 

No

 | 

Yes

 | 

No information about the specified document is retrieved.

 |

#### ItemInfo

Specified content of each data record in the retrieval result.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

primaryKey

 | 

string

 | 

No

 | 

No

 | 

Primary key of the retrieval result.

 |
| 

columns

 | 

Record<string, [relationalStore.ValueType](../../../arkdata/arkts-apis/ohos-data-relationalstore-rdb-store/types/document.md#valuetype)\>

 | 

No

 | 

No

 | 

Recall column and its content.

 |
| 

score

 | 

number

 | 

No

 | 

No

 | 

Final score after re-ranking, reflecting the similarity between the re-ranked records and query terms. The value must be greater than or equal to **0**.

 |
| 

recallScores

 | 

Record<[ChannelType](#section15391712641), Record<string, [RecallScore](#section646415415210)\>>

 | 

No

 | 

No

 | 

Score for each recall channel, reflecting the assessment of the result's relevance. The value of **key** is the value of **scoreKey** for **RecallCondition** of this recall channel.

-   If **scoreKey** of **RecallCondition** for a specific recall channel is absent in **RetrievalCondition**, the recall channel considers the result insufficiently relevant and does not recall the result.

 |
| 

features

 | 

Record<string, number>

 | 

No

 | 

No

 | 

Score of an inverted index strategy. Currently, the following inverted index strategies and scores are supported:

-   **exact\_phase**: score of the exact match strategy.
-   **out\_of\_order\_phase**: score of the unordered match strategy.
-   **token\_bm25**: score of the BM25 strategy.
-   **core\_count**: total number of core terms in a single match field of a document. This parameter specifies the tiering logic of the three strategies, which indicates the text matching degree.

 |
| 

similarityLevel

 | 

[SimilarityLevel](#section336811595811)

 | 

No

 | 

No

 | 

Relevance tiers of retrieval results, which are categorized based on both semantic similarity and text matching degree, facilitating further filtering.

 |

#### RecallScore

Score of the recall phase.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

score

 | 

number

 | 

No

 | 

No

 | 

Recall score.

 |
| 

isReverseQuery

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the score comes from reverse lookup. The value **true** indicates that the score comes from reverse lookup, and **false** indicates that the score comes from the original recall process.

 |

#### SimilarityLevel

Relevance tiers (high, medium, and low) of retrieval results, which are categorized based on both semantic similarity and text matching degree, facilitating further filtering.

**System capability**: SystemCapability.DataAugmentation.Retrieval

**Start version**: 6.0.0(20)

| 
Name

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

NONE

 | 

0

 | 

This parameter is reserved and has no specific meaning.

 |
| 

LOW

 | 

1

 | 

The semantic vector distance between the result and the query is small, indicating higher semantic similarity.

 |
| 

MEDIUM

 | 

2

 | 

The semantic vector distance between the result and the query is moderate, indicating medium semantic similarity.

 |
| 

HIGH

 | 

3

 | 

The semantic vector distance between the result and the query is large, indicating significant semantic differences and low relevance.

 |
