# knowledgeProcessor (Knowledge Processing)

This module provides the capabilities of obtaining the knowledge processing object (**KnowledgeProcessor**) and knowledge processing status (**ProcessorStatus**).

**Start version**: 6.0.0(20)

#### Module Import

import { knowledgeProcessor } from '@kit.DataAugmentationKit';

#### getKnowledgeProcessor

getKnowledgeProcessor(context: common.BaseContext, config: KnowledgeProcessorConfig): Promise<KnowledgeProcessor>

Obtains the knowledge processing object used for obtaining the knowledge processing status.

**System capability**: SystemCapability.DataAugmentation.KnowledgeProcessor

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

context

 | 

[common.BaseContext](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/basecontext/document.md)

 | 

Yes

 | 

Context of the knowledge processing object.

 |
| 

config

 | 

[KnowledgeProcessorConfig](#section7916104025215)

 | 

Yes

 | 

Knowledge processing configuration.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[KnowledgeProcessor](#section395619456396)\>

 | 

Promise used to return the knowledge processing object.

 |

**Error codes:**

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1021400000](../../arkts-api-error-codes/document.md#section184111958125913)

 | 

Internal error.

 |
| 

[1021400001](../../arkts-api-error-codes/document.md#section8963194719118)

 | 

The knowledge source is not configured.

 |
| 

[1021400002](../../arkts-api-error-codes/document.md#section18580829439)

 | 

The knowledge schema file is not found.

 |
| 

[1021400003](../../arkts-api-error-codes/document.md#section581782218519)

 | 

The knowledge schema content is invalid.

 |
| 

[1021400004](../../arkts-api-error-codes/document.md#section0678102120612)

 | 

An error occurred during operations on the RDB source.

 |

**Example:**

import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail\_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // Name of the database where knowledge processing is triggered.
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM\_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// Asynchronous function for obtaining the knowledge processor.
async function getProcessor() {
  const context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;
  try {
    // Obtain the knowledge processing object.
    const processor = await knowledgeProcessor.getKnowledgeProcessor(context, knowledgeProcessorConfig);
    return processor;
  } catch (err) {
    console.error("Error: " + err.message + " code: " + err.code);
    return undefined;
  }
}

#### KnowledgeProcessorConfig

Knowledge processing object configuration.

**System capability**: SystemCapability.DataAugmentation.KnowledgeProcessor

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

sourceConfig

 | 

[KnowledgeSourceConfig](#section5324144573013)

 | 

Yes

 | 

Data source configuration for knowledge processing.

 |

#### KnowledgeSourceConfig

Knowledge data source configuration.

**System capability**: SystemCapability.DataAugmentation.KnowledgeProcessor

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

rdbSource

 | 

[relationalStore.StoreConfig](../../../arkdata/arkts-apis/ohos-data-relationalstore-rdb-store/interfaces-others/document.md#storeconfig)

 | 

No

 | 

RDB configuration. This parameter is mandatory only when the data source is the RDB. The current version supports only the RDB as the data source. If this parameter is not specified, the API returns error code [1021400001](../../arkts-api-error-codes/document.md#section8963194719118).

 |

#### KnowledgeProcessor

Knowledge processing object used for obtaining the knowledge processing status.

**System capability**: SystemCapability.DataAugmentation.KnowledgeProcessor

**Start version**: 6.0.0(20)

#### \[h2\]getStatus

getStatus(): Promise<ProcessorStatus>

Obtains the knowledge processing status.

**System capability**: SystemCapability.DataAugmentation.KnowledgeProcessor

**Device behavior differences**: This API is available on PCs/2-in-1 devices. On phones and tablets, the knowledge processing status is returned based on whether there are data records in the data source table. If there are no data records in the data source table, the knowledge processing status **DATA\_PROCESSING\_COMPLETE** is returned, indicating that all data has been processed. Otherwise, the knowledge processing status **DATA\_REMAINING\_TO\_PROCESS** is returned, indicating that there is data to be processed.

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[ProcessorStatus](#section174782032163713)\>

 | 

Promise used to return the knowledge processing status.

 |

**Error codes:**

| 
Error Code

 | 

**Error Message**

 |
| :-- | :-- |
| 

[1021400000](../../arkts-api-error-codes/document.md#section184111958125913)

 | 

Internal error.

 |
| 

[1021400004](../../arkts-api-error-codes/document.md#section0678102120612)

 | 

An error occurred during operations on the RDB source.

 |

**Example:**

import { knowledgeProcessor } from '@kit.DataAugmentationKit';
import { common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';

const storeName: string = "testmail\_store.db";
const storeConfig: relationalStore.StoreConfig = {
  name: storeName, // Name of the database where knowledge processing is triggered.
  securityLevel: relationalStore.SecurityLevel.S3,
  tokenizer: relationalStore.Tokenizer.CUSTOM\_TOKENIZER,
};
const knowledgeSourceConfig: knowledgeProcessor.KnowledgeSourceConfig = {
  rdbSource: storeConfig,
};
const knowledgeProcessorConfig: knowledgeProcessor.KnowledgeProcessorConfig = {
  sourceConfig: knowledgeSourceConfig,
};
// Asynchronous function for obtaining the knowledge processing status.
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

#### ProcessorStatus

Knowledge processing status.

**System capability**: SystemCapability.DataAugmentation.KnowledgeProcessor

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

DATA\_REMAINING\_TO\_PROCESS

 | 

0

 | 

Indicates that there is data to be processed.

 |
| 

DATA\_PROCESSING\_IN\_PROGRESS

 | 

1

 | 

Indicates that data is being processed.

 |
| 

DATA\_PROCESSING\_COMPLETE

 | 

2

 | 

Indicates that all data has been processed.

 |
