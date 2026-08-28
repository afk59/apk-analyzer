# @ohos.data.intelligence (ArkData Intelligence Platform)

ArkData Intelligence Platform (AIP) provides application data vectorization, which leverages embedding models to convert multi-modal data such as unstructured text and images into semantic vectors.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/H7PW0OeBTc2NjHp_nUzjDA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062216Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D70835488F8B97C680D9D9F55DC001BB55DF9B9959DA716056B75B51040861E5)

The initial APIs of this module are supported since API version 15. Newly added APIs will be marked with a superscript to indicate their earliest API version.

Considering the significant computing workload and resources of data vectorization processing, the APIs are only available to 2-in-1 device applications.

#### Modules to Import

import { intelligence } from '@kit.ArkData';

#### intelligence.getTextEmbeddingModel

getTextEmbeddingModel(config: ModelConfig): Promise<TextEmbedding>

Obtains a text embedding model. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [ModelConfig](#modelconfig) | Yes | Configuration of the embedded model to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[TextEmbedding](#textembedding)\> | Promise used to return the text embedding model object. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let textConfig: intelligence.ModelConfig = {
  version: intelligence.ModelVersion.BASIC\_MODEL,
  isNpuAvailable: false,
  cachePath: "/data"
}
let textEmbedding: intelligence.TextEmbedding;

intelligence.getTextEmbeddingModel(textConfig)
  .then((data: intelligence.TextEmbedding) => {
    console.info("Succeeded in getting TextModel");
    textEmbedding = data;
  })
  .catch((err: BusinessError) => {
    console.error("Failed to get TextModel and code is " + err.code);
  })

#### intelligence.getImageEmbeddingModel

getImageEmbeddingModel(config: ModelConfig): Promise<ImageEmbedding>

Obtains an image embedding model. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| config | [ModelConfig](#modelconfig) | Yes | Configuration of the embedded model to obtain. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[ImageEmbedding](#imageembedding)\> | Promise used to return the image embedding model object. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let imageConfig: intelligence.ModelConfig = {
  version: intelligence.ModelVersion.BASIC\_MODEL,
  isNpuAvailable: false,
  cachePath: "/data"
}
let imageEmbedding: intelligence.ImageEmbedding;

intelligence.getImageEmbeddingModel(imageConfig)
  .then((data: intelligence.ImageEmbedding) => {
    console.info("Succeeded in getting ImageModel");
    imageEmbedding = data;
  })
  .catch((err: BusinessError) => {
    console.error("Failed to get ImageModel and code is " + err.code);
  })

#### intelligence.splitText

splitText(text: string, config: SplitConfig): Promise<Array<string>>

Splits text. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text to split, which can be any value. |
| config | [SplitConfig](#splitconfig) | Yes | Configuration for splitting the text. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<string>> | Promise used to return the blocks of the text. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

let splitConfig: intelligence.SplitConfig = {
  size: 10,
  overlapRatio: 0.1
}
let splitText = 'text';

intelligence.splitText(splitText, splitConfig)
  .then((data: Array<string>) => {
    console.info("Succeeded in splitting Text");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to split Text and code is " + err.code);
  })

#### ModelConfig

Represents the configuration an embedded model.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| version | [ModelVersion](#modelversion) | No | No | Version of the model. |
| isNpuAvailable | boolean | No | No | Whether to use the NPU to accelerate the vectorization process. The value **true** means to use the NPU, and the value **false** means the opposite. If this parameter is set to **true** but the device does not support NPUs, loading an embedding model will trigger error 31300000. |
| cachePath | string | No | Yes | 
Local directory for model caching if the NPU is used. The value is in the /xxx/xxx/xxx format, for example, **/data**. The path cannot exceed 512 characters.

Default value: **""**

 |

#### ModelVersion

Enumerates the model versions.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| BASIC\_MODEL | 0 | Basic embedding model version. |

#### Image

type Image = string

Represents the URI of an image, which is of the string type.

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

| Type | Description |
| :-- | :-- |
| string | Image URI, which cannot exceed 512 characters. |

#### SplitConfig

Represents the configuration for text splitting.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| size | number | No | No | Maximum size of a block. The value is a non-negative integer. |
| overlapRatio | number | No | No | 
Overlap ratio between adjacent blocks.

Value range: \[0,1\]

The value **0** indicates the lowest overlap ratio, and **1** indicates the highest overlap ratio.

 |

#### TextEmbedding

Provides APIs for manipulating text embedding models.

Before calling any of the following APIs, you must obtain a **TextEmbedding** instance by using [intelligence.getTextEmbeddingModel](#intelligencegettextembeddingmodel).

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

#### \[h2\]loadModel

loadModel(): Promise<void>

Loads this text embedding model. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

textEmbedding.loadModel()
  .then(() => {
    console.info("Succeeded in loading Model");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to load Model and code is " + err.code);
  })

#### \[h2\]releaseModel

releaseModel(): Promise<void>

Releases this text embedding model. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

textEmbedding.releaseModel()
  .then(() => {
    console.info("Succeeded in releasing Model");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to release Model and code is " + err.code);
  })

#### \[h2\]getEmbedding

getEmbedding(text: string): Promise<Array<number>>

Obtains the embedding vector of the given text. This API uses a promise to return the result.

Before calling this API, ensure that an embedding model is successfully loaded by using [loadModel](#loadmodel).

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| text | string | Yes | Text for the embedding model, which cannot exceed 512 characters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the vectorization result. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

textEmbedding.loadModel();
let text = 'text';
textEmbedding.getEmbedding(text)
  .then((data: Array<number>) => {
    console.info("Succeeded in getting Embedding");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to get Embedding and code is " + err.code);
  })

#### \[h2\]getEmbedding

getEmbedding(batchTexts: Array<string>): Promise<Array<Array<number>>>

Obtains the embedding vector of a given batch of texts. This API uses a promise to return the result.

Before calling this API, ensure that an embedding model is successfully loaded by using [loadModel](#loadmodel).

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| batchTexts | Array<string> | Yes | Batch of texts, each of which cannot exceed 512 characters. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<Array<number>>> | Promise used to return the vectorization result. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

textEmbedding.loadModel();
let batchTexts = \['text1', 'text2'\];
textEmbedding.getEmbedding(batchTexts)
  .then((data: Array<Array<number>>) => {
    console.info("Succeeded in getting Embedding");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to get Embedding and code is " + err.code);
  })

#### ImageEmbedding

Provides APIs for manipulating image embedding models.

Before calling any of the following APIs, you must obtain a **ImageEmbedding** instance by using [intelligence.getImageEmbeddingModel](#intelligencegetimageembeddingmodel).

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

#### \[h2\]loadModel

loadModel(): Promise<void>

Loads this image embedding model. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.loadModel()
  .then(() => {
    console.info("Succeeded in loading Model");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to load Model and code is " + err.code);
  })

#### \[h2\]releaseModel

releaseModel(): Promise<void>

Releases this image embedding model. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.releaseModel()
  .then(() => {
    console.info("Succeeded in releasing Model");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to release Model and code is " + err.code);
  })

#### \[h2\]getEmbedding

getEmbedding(image: Image): Promise<Array<number>>

Obtains the embedding vector of the given image. This API uses a promise to return the result.

Before calling this API, ensure that an embedding model is successfully loaded by using [loadModel](#loadmodel).

**System capability**: SystemCapability.DistributedDataManager.DataIntelligence.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| image | [Image](#image) | Yes | URI of the target image. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<number>> | Promise used to return the vectorization result. |

**Error codes**

For details about the error codes, see [Common Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [AIP Error Codes](../../error-codes/aip-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types. |
| 801 | Capability not supported. |
| 31300000 | Inner error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

imageEmbedding.loadModel();
let image = 'file://<packageName>/data/storage/el2/base/haps/entry/files/xxx.jpg';
imageEmbedding.getEmbedding(image)
  .then((data: Array<number>) => {
    console.info("Succeeded in getting Embedding");
  })
  .catch((err: BusinessError) => {
    console.error("Failed to get Embedding and code is " + err.code);
  })
