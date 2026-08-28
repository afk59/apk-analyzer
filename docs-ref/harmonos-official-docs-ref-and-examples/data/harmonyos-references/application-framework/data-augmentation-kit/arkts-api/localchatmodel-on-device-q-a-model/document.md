# localChatModel (On-Device Q&A Model)

This module provides the method for accessing the on-device Q&A model to implement the intelligent Q&A capability within the device.

**Start version**: 6.0.0(20)

#### Module Import

import { localChatModel } from '@kit.DataAugmentationKit';

#### Config

Configuration of whether streaming Q&A is supported.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.LocalChatModel

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

isStream

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether streaming Q&A is supported. The value **true** indicates that streaming Q&A is supported, and **false** indicates that streaming Q&A is not supported.

 |

**Example:**

import { localChatModel } from '@kit.DataAugmentationKit';

let localConfig: localChatModel.Config = {
  isStream: true
}

#### QuestionInfo

Question information used to interact with the on-device Q&A model.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.LocalChatModel

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

questionId

 | 

number

 | 

No

 | 

No

 | 

Question ID for interacting with the on-device Q&A model. The value range is \[0, 65535\]. The question ID must be unique for the same app.

 |
| 

content

 | 

string

 | 

No

 | 

No

 | 

Question content for interacting with the on-device Q&A model. Due to on-device model performance restrictions, the content length cannot exceed 4500 bytes.

 |

**Example:**

import { localChatModel } from '@kit.DataAugmentationKit';

let questionInfo: localChatModel.QuestionInfo = {
  questionId: 1,
  content: "Who are you?"
}

#### Answer

Result returned after interaction with the on-device Q&A model.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.LocalChatModel

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

questionId

 | 

number

 | 

No

 | 

No

 | 

Question ID corresponding to the result returned by the Q&A model, which is the same as the value of **questionId**.

 |
| 

content

 | 

string

 | 

No

 | 

No

 | 

Answer to the question corresponding to **questionId**, which is provided by the Q&A model.

 |
| 

isFinished

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the Q&A result is complete. The value **true** indicates that the Q&A result is complete, and **false** indicates that the Q&A result is incomplete.

 |

**Example:**

import { localChatModel } from '@kit.DataAugmentationKit';

let answer: localChatModel.Answer = {
  questionId: 1,
  content: "I am Qwen.",
  isFinished: true
}

#### init

init(): Promise<boolean>

Initializes the on-device Q&A model. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.LocalChatModel

**Start version**: 6.0.0(20)

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<boolean>

 | 

Promise used to return the model initialization result. The value **true** indicates that the initialization is successful, and **false** indicates that the initialization fails.

 |

**Example:**

import { localChatModel } from '@kit.DataAugmentationKit';

async function init() {
  try {
    const result = await localChatModel.init();
    console.info('init result: ', result);
  } catch (err) {
    console.error('init err: ', err);
  }
}

#### chat

chat(info: QuestionInfo, config: Config, callback: AsyncCallback<Answer>): Promise<void>

Asks questions to the on-device Q&A model. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/4YjJGxCmRH-gw17s9AKHxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062322Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AAC704B2B549B1D45A6131AF8349BE9FE05F1C21705F63757A20D582F36372DE)

Before calling the **chat** method, your app needs to call the **init** method to initialize the on-device Q&A model.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.LocalChatModel

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

info

 | 

[QuestionInfo](#section1666712479912)

 | 

Yes

 | 

Question information used to interact with the on-device Q&A model.

 |
| 

config

 | 

[Config](#section178144421252)

 | 

Yes

 | 

Question configuration item.

 |
| 

callback

 | 

AsyncCallback<[Answer](#section44611173175)\>

 | 

Yes

 | 

Callback for returning the Q&A result to the caller.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<void>

 | 

Promise that returns no value.

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

[1021900001](../../arkts-api-error-codes/document.md#section1164223410558)

 | 

A timeout occurs when the local chat model is called.

 |
| 

[1021900002](../../arkts-api-error-codes/document.md#section146422038527)

 | 

A loading failure occurs when the local chat model is called.

 |
| 

[1021900003](../../arkts-api-error-codes/document.md#section394012326616)

 | 

A request failure occurs when the local chat model is called.

 |
| 

[1021900004](../../arkts-api-error-codes/document.md#section15133164697)

 | 

The local chat model is busy.

 |
| 

[1021900005](../../arkts-api-error-codes/document.md#section933985171319)

 | 

Some parameters do not meet the specified constraints.

 |

**Example:**

import { BusinessError } from "@kit.BasicServicesKit";
import { localChatModel } from '@kit.DataAugmentationKit';

async function chat() {
  let questionInfo: localChatModel.QuestionInfo = {
    questionId: 100,
    content: "You are a translation assistant and can translate the following content into 36 languages: PC model manager"
  }
  let localConfig: localChatModel.Config = {
    isStream: true
  }
  let localChatCallback = async (err: BusinessError, ans: localChatModel.Answer): Promise<void> => {
    if (err) {
      // Error code related to model running.
      console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
      return;
    }
    console.info('questionId: ' + ans.questionId + ', content: ' + ans.content + ', isFinished: ' + ans.isFinished);
  };
  try {
    await localChatModel.chat(questionInfo, localConfig, localChatCallback);
  } catch (err) {
    // Error code related to input parameters.
    console.error('errCode: ' + err.code + ', errMessage: ' + err.message);
  }
}
