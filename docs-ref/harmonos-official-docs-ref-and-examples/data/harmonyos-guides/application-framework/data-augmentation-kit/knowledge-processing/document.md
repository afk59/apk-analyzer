# Knowledge Processing

Knowledge processing refers to the capability of generating a knowledge base based on actual service data. It includes the following operations:

-   Configure the schema to generate knowledge processing products (such as inverted index tables, vector libraries, and vector tables). These products are used for retrieval during knowledge Q&A. The schema configuration must be based on the database and data table structure used in actual services. Knowledge processing and retrieval are optimized for Chinese. Therefore, the Q&A performance of Chinese is better than that of English.
-   Call the API for obtaining the knowledge processing status.

The following table describes the structure of the knowledge table generated during knowledge processing.

**Table 1** Inverted index table structure
| 
Column

 | 

Type

 | 

Definition

 |
| :-- | :-- | :-- |
| 

reference\_id

 | 

UNINDEXED

 | 

ID used for association, which corresponds to the primary key ID in the service table.

 |
| 

chunk\_id

 | 

UNINDEXED

 | 

ID of a split chunk. A chunk indicates a slice of the text that needs to be processed.

 |
| 

chunk\_source

 | 

UNINDEXED

 | 

Field of a chunk in the service table.

 |
| 

chunk\_text

 | 

TEXT

 | 

Inverted index field, which is the text content of a chunk.

 |

**Table 2** Vector table structure
| 
Column

 | 

Type

 | 

Description

 |
| :-- | :-- | :-- |
| 

id

 | 

INTEGER

 | 

Auto-increment primary key.

 |
| 

reference\_id

 | 

INTEGER

 | 

ID used for association, which corresponds to the primary key ID in the service table.

 |
| 

chunk\_id

 | 

TEXT

 | 

ID of a split chunk. A chunk indicates a slice of the text that needs to be processed.

 |
| 

chunk\_source

 | 

TEXT

 | 

Field of a chunk in the service table.

 |
| 

repr

 | 

FLOATVECTOR(128)

 | 

Vector representation of the text corresponding to **chunk\_id**.

 |
| 

Scalar

 | 

TEXT

 | 

All scalar fields defined in the schema are of the TEXT type.

 |

#### Time to Trigger Knowledge Processing

Knowledge processing can be triggered in the following scenarios:

-   After the **knowledge\_schema.json** file and the database creation or opening parameters are configured in [step 1](#li1041155415158) and [step 2](#li7681121661620), a knowledge processing task is triggered each time the database is created or opened.
-   When the database is successfully created or opened and an active database connection is available, a knowledge processing task is automatically triggered upon any data change (insert, update, or delete) to the data source table.

#### Restrictions

1.  Tables used for knowledge processing do not support cross-device synchronization and device-cloud synchronization, and cannot be used for search.
2.  The knowledge processing schema does not support upgrade.
3.  Currently, the data vectorization capability for knowledge processing can be used only on PCs/2-in-1 devices. Phones and tablets do not support this capability.
4.  The value of the **version** field in the knowledge processing schema is a positive integer. The maximum value is **2147483647**.
5.  The minimum value length of the **dbName** field in the knowledge processing schema is 1 and the maximum length is 120. The value can contain digits, uppercase letters, lowercase letters, underscores (\_), and periods (.).
6.  The minimum value length of the **tableName** field in the knowledge processing schema is 1 and the maximum length is 120. The value can contain digits, uppercase letters, lowercase letters, and underscores (\_).
7.  The minimum value length of the **columnName** field in the knowledge processing schema is 1 and the maximum length is 255.
8.  In the knowledge processing schema, **referenceFields** supports only one field of the integer type. The minimum value length is 1 and the maximum length is 255.
9.  In the knowledge processing schema, the **type** value of a knowledge processing field can be **Text**, **Scalar**, or **Json**.
10.  In the knowledge processing schema, each knowledge processing field of the **Scalar** type must contain a **description** field. The minimum value length of the **description** field is 1 and the maximum length is 255. The fields of the **Scalar** type are not used for knowledge processing. The field values are the same as those in the service table.
11.  In the knowledge processing schema, each knowledge processing field of the **Json** type must contain a **parser** field to specify the parsers of file paths. Each knowledge processing field of the **Json** type can contain 1 to 5 parsers, and a maximum of five different local file paths can be parsed.
12.  Each object of the **parser** field in the knowledge processing schema must contain the **type** and **path** fields, in which the value of **type** is **File** and the length range of **path** is \[1, 255\]. The value of **path** must be a valid JSON path expression, which specifies the file path to be parsed during knowledge processing.
13.  The **pipelineHandlers** field in the knowledge processing schema is used to define the execution sequence of each processing module (that is, handler) during knowledge processing. Handlers can be customized. By properly modifying the handler process, you can determine how the original data is parsed, split, and represented, and finally written to the inverted index table and vector table. For details, please refer to the sample in step 1 of the development procedure. Set the **pipelineHandlers** field to a mapping (unordered\_map<string, vector<string>>). Each key is the current handler, and the value is the list of handlers to be executed subsequently. The following is an example:
     
     "pipelineHandlers": 
     {
       "FileParserHandler": \["SplitTextHandler"\],  
       "SplitTextHandler": \["TextEmbeddingHandler"\],
       "TextEmbeddingHandler": \["ImageEmbeddingHandler"\],
       "ImageEmbeddingHandler": \[\]
     }
     
     All handler names must be supported by the system. The supported handler names include **FileParserHandler**, **SplitTextHandler**, **TextEmbeddingHandler**, and **ImageEmbeddingHandler**. The recommended execution process is as follows:
     
     -   FileParserHandler → SplitTextHandler → TextEmbeddingHandler → ImageEmbeddingHandler
     
     Handlers cannot depend on each other cyclically. Otherwise, the system will report an error when loading the schema. The downstream of each handler can be an empty array, indicating that the processing ends here. If the configuration sequence is incorrect (for example, some handlers are skipped, the sequence is incorrect, or a closed loop is formed), files may not be processed, the processing may be interrupted, or the initialization may fail. You can simplify the configuration based on the actual scenario. For example, if only the inverted index table needs to be processed, you need to configure only the SplitTextHandler. The functions and dependencies of the handlers are as follows:
     
     -   FileParserHandler: extracts the text content from the local files specified by the knowledge processing fields of the **Json** type. The supported file formats are doc, docx, ppt, pptx, xls, xlsx, html, txt, pdf, png, jpg, and jpeg. For text files, the text content is extracted. For image files, OCR is used to extract the recognizable text. This handler does not depend on other handlers.
         
         Recommended configuration sequence: You are advised to place this handler before the SplitTextHandler so that the extracted file content can be split and represented.
         
         Impact of not configuring the handler: The files specified by the knowledge processing fields of the **Json** type will not be parsed, and the inverted index table and vector table will not contain the file content (image vector representation is not affected).
         
     -   SplitTextHandler: splits text fields into two levels. The first level is chunk, which is used for inverted indexes. The second level is segment, which is used for vector representation (embedding).
         
         Recommended configuration sequence: This handler must be configured before the TextEmbeddingHandler. Otherwise, segments will be missing in the vector representation phase, and the subsequent representation will fail.
         
         Impact of not configuring the handler: The inverted index table and vector table will not contain text content, and no text content can be returned during retrieval.
         
     -   TextEmbeddingHandler: performs text vector representation for the segments generated by the SplitTextHandler and generates data for vector retrieval. This handler depends on the result of the SplitTextHandler.
         
         Recommended configuration sequence: Place this handler after the SplitTextHandler and before the ImageEmbeddingHandler.
         
         Impact of not configuring the handler: The text representation result will not be stored in the vector table, affecting semantic search.
         
     -   ImageEmbeddingHandler: loads images from the image paths parsed based on the knowledge processing fields of the **Json** type and generates a vector representation of image features. Image processing does not depend on the SplitTextHandler and is not used in the text inverted index table. This handler is independent of text processing and does not depend on any handlers.
         
         Recommended configuration sequence: Place this handler after the TextEmbeddingHandler to prevent the image path field from being mistakenly treated as text and incorporated into the representation, which will introduce noise.
         
         Impact of not configuring the handler: The image representation result will not be stored in the vector table, affecting image search.
         
14.  The **knowledgeProcess** field in the knowledge processing schema is optional and is used to set knowledge processing fields including **embeddingModelCfg**, **chunkSplitter**, and **perRecordLimit**. For details, please refer to the sample in step 1 of the development procedure. You do not need to set all the three fields in the **knowledgeProcess** field. However, if any of the three fields is set, all the sub-fields under this field must be set.
     
     -   In the knowledge processing schema, if the **embeddingModelCfg** field is set in the **knowledgeProcess** field, the **modelVersion** field of the string type must also be set, indicating the version of the vector representation model. The value can contain a maximum of 100 characters. If the value is an empty string, the default version will be used. The field value must match the version of the deployed or supported model, and the version of the representation model for knowledge processing must be the same as that used for inference. The default value is **default**.
     -   In the knowledge processing schema, if the **chunkSplitter** field is set in the **knowledgeProcess** field, the following fields must also be set:
         -   **chunkSize**: maximum length of a chunk. The value is of the integer type. The value range is \[100, 5000\]. The default value is **3072**.
         -   **segmentSize**: maximum length of a segment in a chunk, which is the unit of vector representation. The value is of the integer type. The value range is \[128, 512\]. The default value is **300**.
         -   **overlapRatio**: overlap ratio between adjacent chunks. The value is of the floating point number type. The value range is (0.0, 0.3\]. The default value is **0.1**.
     
     These fields are used to control the text segmentation strategy, affecting the granularity of chunks and the continuity of context. If no values are specified, the system will use their default values.
     
     -   In the knowledge processing schema, if the **perRecordLimit** field is set in the **knowledgeProcess** field, the following fields must also be set:
         -   **parseFileMaxCnt**: maximum number of files that can be parsed in each record. The value is of the integer type. The value range is \[0, 200\]. The default value is **10**.
         -   **textEmbeddingMaxCnt**: maximum number of text segments that can be vectorized in each record. The value is of the integer type. The value range is \[0, 200\]. The default value is **50**. Text segments that exceed the upper limit will not be vectorized.
         -   **imageEmbeddingMaxCnt**: maximum number of images that can be processed in each record. The value is of the integer type. The value range is \[0, 200\]. The default value is **10**.
     
     These fields are used to specify the maximum processing scale of a single record during knowledge processing. If no values are specified, the system will use their default values. If a value is too small, information processing may be incomplete. If a value is too large, system resources may be consumed excessively.
     
15.  The knowledge processing schema file name must be **knowledge\_schema.json**. The file content must be a valid JSON string and the file must be stored in **src/main/resources/rawfile/arkdata/knowledge/**.
16.  Knowledge processing supports the following file types:
     -   Text and web pages: txt and html.
     -   Office files: doc, docx, ppt, pptx, xls, xlsx, and pdf. Only basic processing of plain text is supported. For complex or specific content, use the corresponding app to parse and process it and then convert it to the TXT format for subsequent processing.
     -   Images: jpeg, jpg, and png.

#### API Description

The following table lists the key APIs for knowledge processing. For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api#section10914338105311).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[getKnowledgeProcessor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api#section4623141252)(context: [common.BaseContext](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-basecontext), config: [KnowledgeProcessorConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api#section7916104025215)): Promise<[KnowledgeProcessor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api#section395619456396)\>

 | 

Obtains the knowledge processing object used for obtaining the knowledge processing status.

 |
| 

[getStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api#section1172685711116)(): Promise<[ProcessorStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api#section174782032163713)\>

 | 

Obtains the knowledge processing status.

 |
| 

[getRdbStore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-f#relationalstoregetrdbstore-1)(context: [Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), config: [StoreConfig](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-i#storeconfig)): Promise<[RdbStore](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/arkts-apis-data-relationalstore-rdbstore)\>

 | 

Creates a relational database (RDB) or opens an existing RDB. After setting database creation or opening parameters according to [step 2](#li7681121661620), this API can be called to trigger knowledge processing.

 |

#### Development Procedure

1.  Configure the knowledge processing schema file **knowledge\_schema.json** based on the service requirements. The following is a configuration example. The naming rules of knowledge processing products are as follows:
    
    -   The inverted index database and source database are the same.
    -   The name of an inverted index table is suffixed by **\_inverted** based on the name of a source table. For example, if a source table name is **email**, its inverted index table name is **email\_inverted**.
    -   The name of a vector database is suffixed by **\_vector** based on the name of a source database. For example, if a source database name is **testmail\_store.db**, its vector database name is **testmail\_store\_vector.db**.
    -   The name of a vector table is suffixed by **\_vector** based on the name of a source table. For example, if a source table name is **email**, its vector table name is **email\_vector**.
        
        // File path: src/main/resources/rawfile/arkdata/knowledge/knowledge\_schema.json
        // If the directory does not exist in the project, create it recursively.
        // Delete this comment during app development. The comment is provided only for field description.
        {
          "knowledgeSource": \[{
            "version": 1,
            "dbName": "testmail\_store.db",  // Name of the database file for storing original data.
            "tables": \[{
              "tableName": "email",  // Name of the table used for knowledge processing.
              "referenceFields": \["id"\],  // Reference fields of the knowledge data source, which are used to associate data in the knowledge base.
              "knowledgeFields": \[{  // Fields used for knowledge processing.
                "columnName": "subject",  // Column name for knowledge processing.
                "type": \["Text"\]  // Field type for knowledge processing. The value **Text** is for vector and inverted indexes.
              },
              {
                "columnName": "content",
                "type": \["Text"\]
              },
              {
                "columnName": "image\_text",
                "type": \["Text"\]
              },
              {
                "columnName": "attachment\_names",
                "type": \["Text"\]
              },
              {
                "columnName": "inline\_files",
                "type": \["Json"\],
                "parser": \[
                  {
                    "type": "File",
                    "path": "$\[\*\].uri"  // The value of **path** is a JSON path expression.
                  }
                \]
              },
              {
                "columnName": "sender",
                "type": \["Scalar"\],  // The value **Scalar** indicates a scalar field. Under this setting, knowledge will not be processed and is directly written to the corresponding column in the vector table for scalar retrieval and filtering.
                "description": "sender"
              },
              {
                "columnName": "receivers",
                "type": \["Scalar"\],
                "description": "receivers"
              },
              {
                "columnName": "received\_date",
                "type": \["Scalar"\],
                "description": "received\_date"
              }\],
              "pipelineHandlers": {
                "FileParserHandler": \["SplitTextHandler"\],  // After the file is parsed, the SplitTextHandler continues to process the file.
                "SplitTextHandler": \["TextEmbeddingHandler"\],
                "TextEmbeddingHandler": \["ImageEmbeddingHandler"\],
                "ImageEmbeddingHandler": \[\]
              }
            }\],
            "knowledgeProcess": {
              "embeddingModelCfg":
              {
                "modelVersion": "default"  // Vector representation model. The value **default** indicates the default version.
              },
              "chunkSplitter":
              {
                "chunkSize": 3072,
                "segmentSize": 300,
                "overlapRatio": 0.1
              },
              "perRecordLimit":
              {
                "parseFileMaxCnt": 10,
                "textEmbeddingMaxCnt": 50,
                "imageEmbeddingMaxCnt": 10
              }
            }
          }\]
        }
        
    
2.  Set [database creation or opening parameters](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-data-relationalstore-i#storeconfig) for the source database based on the service requirements. The following provides sample code for your reference.
    
    If the **type** field of the **inline\_files** column in the schema example is set to **Json** and the **path** field is set to the path expression pointing to a URI, the knowledge processing capability will parse the URI value in the **inline\_files** column of the database as the file path. The data values in the **inline\_files** column must be in the object array format of the file paths provided in the sample code. Knowledge construction is performed based on the file content obtained from the file paths during knowledge processing.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/kfFAzYjxQbucqU42fo7jvw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=168AFE210BFC466DDEB345A521E88609B4D64ED74A8E9E9F87FDD606B19659C7)
    
    -   Knowledge processing can be triggered only when the following conditions are met: The value of the **name** field specified for setting the **relationalStore** database creation or opening parameters is the same as the value of the **dbName** field in [1](#li1041155415158). The **enableSemanticIndex** field is set to **true**.
    -   The table name used in the table creation statement must be the same as the value of **tableName** in [1](#li1041155415158), and the column name must be the same as the value of **columnName**.
    
    import { relationalStore } from '@kit.ArkData';
    
    // Set the **relationalStore** database creation or opening parameters.
    const storeConfig: relationalStore.StoreConfig = {
      name: 'testmail\_store.db',  // The value must be the same as that of **dbName** in step 1.
      securityLevel: relationalStore.SecurityLevel.S3,
      enableSemanticIndex: true,  // Knowledge processing is triggered only when this parameter is set to **true**.
      tokenizer: relationalStore.Tokenizer.CUSTOM\_TOKENIZER
    };
    
    // The table name used in the table creation statement must be the same as the value of **tableName** in step 1, and the column name must be the same as the value of **columnName**.
    const createTableSql = "CREATE TABLE IF NOT EXISTS email(id integer primary key, subject text, " +
      "content text, image\_text text, attachment\_names text, inlineFiles text, sender text, " +
      "receivers text, received\_date text);";
    
    // Data insertion statement. Implement the statement based on the actual service requirements. The following is for reference only.
    const sql = \`insert or replace into email VALUES(0, 'Subject of an email', 'Content of an email',
      'Convert image to text through OCR', 'attachment\_name\_1.txt',
      '\[{"uri":"/data/storage/el2/base/haps/entry/files/capture\_1.png"},{"uri":"/data/storage/el2/base/haps/entry/files/capture\_2.jpeg"}\]',
      'zhangsan(zhangsan@xxx.com)', 'lisi(lisi@xxx.com), wangwu(wangwu@xxx.com)', 'Convert time to timestamp');\`;
    
3.  Call the [getStatus()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-knowledgeprocessor-api#section1172685711116) API to query the current knowledge processing status based on the service requirements.
    
    import { relationalStore } from '@kit.ArkData';
    import { knowledgeProcessor } from '@kit.DataAugmentationKit';
    import { UIAbility, common } from '@kit.AbilityKit';
    
    // Set the **relationalStore** database creation or opening parameters.
    const storeConfig: relationalStore.StoreConfig = {
      name: 'testmail\_store.db',  // The value must be the same as that of **dbName** in step 1.
      securityLevel: relationalStore.SecurityLevel.S3,
      enableSemanticIndex: true,
      tokenizer: relationalStore.Tokenizer.CUSTOM\_TOKENIZER
    };
    
    let knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
      rdbSource: storeConfig,
    }
    let knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
      sourceConfig: knowledgeSourceConfig,
    }
    
    // Asynchronous function for obtaining the knowledge processing status. Call this function based on the service requirements.
    async function getStatus() {
      const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
      try {
        // Obtain the knowledge processing object.
        const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
        // Obtain the knowledge processing status.
        const status: knowledgeProcessor.ProcessorStatus = await processor.getStatus();
        return status;
      } catch (err) {
        console.error("Error: " + err.message + " code: " + err.code);
        return undefined;
      }
    }
