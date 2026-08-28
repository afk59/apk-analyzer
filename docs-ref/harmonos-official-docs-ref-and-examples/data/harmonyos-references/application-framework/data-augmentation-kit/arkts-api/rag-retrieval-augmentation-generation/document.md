# rag (Retrieval Augmentation Generation)

This module provides the capabilities of creating and closing sessions ([RagSession](#section1312212528516)), streaming-requesting an LLM ([ChatLLM](#section1400115191116)), and streaming Q&A ([streamRun](#section178721756950)).

**Start version**: 6.0.0(20)

#### Module Import

import { rag } from '@kit.DataAugmentationKit';

#### LLMStreamAnswer

Single result of streaming Q&A from the LLM.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

isFinished

 | 

boolean

 | 

No

 | 

No

 | 

Indicates whether the streaming output of the LLM ends. The value **true** indicates that the streaming output already ends, and **false** indicates that more answer content will be generated.

 |
| 

chunk

 | 

string

 | 

No

 | 

No

 | 

Content of a chunk (split text unit) returned in a single round during the streaming output of the LLM. There is no upper limit on the number of chunks returned in a single round. The maximum length of all streaming output results in a single Q&A is 8192 bytes.

 |
| 

err

 | 

[BusinessError](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror)<string>

 | 

No

 | 

Yes

 | 

Error that occurs during the streaming output of the LLM. The value of [code](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#businesserror) is in the range \[1021011000, 1021012000). If the value is out of the range, error [1021000000](../../arkts-api-error-codes/document.md#section16205152494111) is reported. The maximum length of the mandatory parameters **name** and **message** for the base class is 1000 characters. Excess characters will be truncated. If this parameter is not carried, no error occurs.

 |

#### LLMRequestStatus

Enumerated values of the status of a streaming request to the LLM.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

LLM\_SUCCESS

 | 

0

 | 

Requesting the LLM succeeded.

 |
| 

LLM\_REQUEST\_ERROR

 | 

1

 | 

Request error.

 |
| 

LLM\_LOAD\_FAILED

 | 

2

 | 

LLM loading failed.

 |
| 

LLM\_TIMEOUT

 | 

3

 | 

Requesting the LLM timed out.

 |
| 

LLM\_BUSY

 | 

4

 | 

The LLM is busy.

 |

#### LLMRequestInfo

Result information of a streaming request to the LLM.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

chatId

 | 

number

 | 

No

 | 

No

 | 

ID of the LLM request.

 |
| 

status

 | 

[LLMRequestStatus](#section19522153218174)

 | 

No

 | 

No

 | 

Status of the [streamChat](#section157381918121212) request.

 |

#### ChatLLM

Abstract class for requesting the LLM. Your app needs to inherit from this class to implement the logic of each API based on the service logic.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

**Start version**: 6.0.0(20)

#### \[h2\]streamChat

abstract streamChat(query: string, callback: Callback<LLMStreamAnswer>): Promise<LLMRequestInfo>

Sends streaming requests to the LLM for interaction. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

Request content for interacting with the LLM. The content is dynamically combined based on the input question, question preprocessing result, retrieval result, and other information. The maximum length is 20,000 bytes.

**Note**: The prompt to be sent to the LLM is already included, and no additional content is required. The sample data in the prompt is solely intended to guide the model toward the desired output and serves no other purpose.

 |
| 

callback

 | 

[Callback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#callback)<[LLMStreamAnswer](#section178144421252)\>

 | 

Yes

 | 

Callback used to return the results obtained after interaction with the LLM to the RAG basic framework.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[LLMRequestInfo](#section1816505018227)\>

 | 

Promise used to return the LLM request object.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';
import { rag } from '@kit.DataAugmentationKit';

class MyChatLLM extends rag.ChatLLM {
  httpRequest: http.HttpRequest | null = http.createHttp();
  cancel(chatId: number) {
    // Implement the mapping between **chatId**s and requests as required. This allows requests to be cancelled by specifying their **chatId**s.
    this.httpRequest?.off('dataReceive');
  }
  async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
    let info: rag.LLMRequestInfo = {
      chatId: 0,
      status: rag.LLMRequestStatus.LLM\_SUCCESS,
    };
    try {
      // Select your desired LLM and implementation.
      // Assume that the answer is obtained from the LLM through httpRequest.on('dataReceive', callback).
      let err: BusinessError<string> = {
        code: 1021011000,  // Custom error code. The value range is \[1021011000, 1021012000).
        name: 'Fill custom error name here',  // If the length exceeds 1000 characters, the excess part will be truncated.
        message: 'Fill custom error message here'  // If the length exceeds 1000 characters, the excess part will be truncated.
      }
      let answer: rag.LLMStreamAnswer = {
        isFinished: true,  // If the reply is the last one from the LLM, the value is **true**. Otherwise, the value is **false**.
        chunk: 'This is the last chunk',
        err: err
      }
      callback(answer);
    } catch (err) {
      // In this example, **LLM\_REQUEST\_ERROR** is returned. Your app can determine the value of **LLMRequestStatus** to return based on the error code.
      info.status = rag.LLMRequestStatus.LLM\_REQUEST\_ERROR;
    }
    return info;
  }
}

#### \[h2\]cancel

abstract cancel(chatId: number): void

Cancels a streaming request to the LLM to pause ongoing interaction.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

chatId

 | 

number

 | 

Yes

 | 

ID of the LLM request to be canceled. The value must be the same as that of **chatId** in [LLMRequestInfo](#section1816505018227) returned by [streamChat](#section157381918121212).

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { http } from '@kit.NetworkKit';
import { rag } from '@kit.DataAugmentationKit';

class MyChatLLM extends rag.ChatLLM {
  httpRequest: http.HttpRequest | null = http.createHttp();
  cancel(chatId: number) {
    // Implement the mapping between **chatId**s and requests as required. This allows requests to be cancelled by specifying their **chatId**s.
    this.httpRequest.off('dataReceive');
  }
}

#### Config

Session configuration items.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

llm

 | 

[ChatLLM](#section1400115191116)

 | 

No

 | 

No

 | 

Provider of the [ChatLLM](#section1400115191116).

 |
| 

retrievalConfig

 | 

[retrieval.RetrievalConfig](../retrieval-retriever/document.md#section95236010016)

 | 

No

 | 

No

 | 

Configuration used for retrieval.

 |
| 

retrievalCondition

 | 

[retrieval.RetrievalCondition](../retrieval-retriever/document.md#section4881955192413)

 | 

No

 | 

No

 | 

Retrieval condition.

 |

**Example:**

import { rag, retrieval } from '@kit.DataAugmentationKit';

let retrievalConfig: retrieval.RetrievalConfig = {
  channelConfigs: \[/\*Configure as required\*/\]
};

let retrievalCondition: retrieval.RetrievalCondition = {
  recallConditions: \[/\*Configure as required\*/\]
};

let config: rag.Config = {
  llm: new MyChatLLM(),
  retrievalConfig: retrievalConfig,
  retrievalCondition: retrievalCondition
};

#### Answer

Data of streaming Q&A.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

chunk

 | 

string

 | 

No

 | 

No

 | 

Answer segment. The maximum length is 8192 bytes.

 |
| 

data

 | 

Array<[retrieval.ItemInfo](../retrieval-retriever/document.md#section17768581101)\>

 | 

No

 | 

Yes

 | 

Retrieval result.

 |

#### StreamType

Streaming answer type.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

THOUGHT

 | 

0

 | 

Thinking data.

 |
| 

REFERENCE

 | 

1

 | 

Source of the retrieved document or knowledge.

 |
| 

ANSWER

 | 

2

 | 

Final content generated.

 |

#### Stream

Result information of a single answer in streaming Q&A.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

type

 | 

[StreamType](#section172106569558)

 | 

No

 | 

No

 | 

Data type of an answer.

 |
| 

answer

 | 

[Answer](#section1473315119532)

 | 

No

 | 

No

 | 

Answer.

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

Indicates whether the streaming output ends. **true**: The streaming output for the current round of Q&A already ends. **false**: More answer content will be generated for the current round of Q&A.

 |

#### RunConfig

Streaming Q&A configuration items.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

answerTypes

 | 

Array<[StreamType](#section172106569558)\>

 | 

No

 | 

No

 | 

Data type for streaming output.

 |

#### FeedbackInfo

User feedback information.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

runId

 | 

number

 | 

No

 | 

No

 | 

Unique identifier of a specific streaming Q&A in a session.

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

Rating of the returned answer by the user. The value range is \[1, 5\].

 |
| 

source

 | 

Record<[StreamType](#section172106569558), [Answer](#section1473315119532)\>

 | 

No

 | 

Yes

 | 

Answer used by the user.

 |
| 

comment

 | 

string

 | 

No

 | 

Yes

 | 

Text comment provided by the user. The maximum length is 1000 bytes.

 |

#### RagSession

RAG session, which is used to provide the knowledge base-based intelligent Q&A capability.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

**Start version**: 6.0.0(20)

#### \[h2\]streamRun

streamRun(question: string, config: RunConfig, callback: AsyncCallback<Stream>): Promise<number>

Performs streaming Q&A. The answer is transmitted in streaming mode, and a promise is used to return the result asynchronously. Multi-thread calls are not supported.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

question

 | 

string

 | 

Yes

 | 

Question. The maximum length is 1000 bytes.

 |
| 

config

 | 

[RunConfig](#section126313912116)

 | 

Yes

 | 

Question configuration.

 |
| 

callback

 | 

[AsyncCallback](../../../../system/basic-functions/basic-services-kit/arkts-apis/others/ohos-base-public-callback-information/document.md#asynccallback)<[Stream](#section158611717585)\>

 | 

Yes

 | 

Callback for receiving the answer to the question. **Note:** The complete lifecycle of **streamRun** includes the complete callback execution. After the callback execution ends, the lifecycle of the current **streamRun** is still active. Starting a new **streamRun** or performing a cancel/close operation at this point may trigger errors related to the ongoing **streamRun**.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<number>

 | 

Promise used to return the Q&A ID.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1021000000](../../arkts-api-error-codes/document.md#section16205152494111)

 | 

Insufficient system resources or memory access exception.

 |
| 

[1021000001](../../arkts-api-error-codes/document.md#section067520119311)

 | 

A timeout occurred when calling the LLM.

 |
| 

[1021000002](../../arkts-api-error-codes/document.md#section398619111131)

 | 

A loading failure occurred when calling the LLM.

 |
| 

[1021000003](../../arkts-api-error-codes/document.md#section821961514310)

 | 

A request failure occurred when calling the LLM.

 |
| 

[1021000004](../../arkts-api-error-codes/document.md#section57321151039)

 | 

The LLM chat is busy.

 |
| 

[1021000005](../../arkts-api-error-codes/document.md#section151441316239)

 | 

The output of LLM chat does not comply with the constraints.

 |
| 

[1021000007](../../arkts-api-error-codes/document.md#section1787571610312)

 | 

The RAG session is busy.

 |
| 

[1021000008](../../arkts-api-error-codes/document.md#section16220417239)

 | 

The RAG session is Already closed.

 |
| 

[1021000009](../../arkts-api-error-codes/document.md#section12582191715318)

 | 

User has canceled the stream run.

 |
| 

[1021000010](../../arkts-api-error-codes/document.md#section13942117932)

 | 

A timeout occurred in the session.

 |
| 

[1021000011](../../arkts-api-error-codes/document.md#section3292318836)

 | 

Some parameter does not meet the constraints. Possible causes:

1\. The length of the string parameter or the length of the numeric parameter does not comply with the constraints.

2\. The string parameter contains invalid characters.

 |
| 

[1021000012](../../arkts-api-error-codes/document.md#section666413181639)

 | 

The knowledge base is not available.

 |
| 

[1021000013](../../arkts-api-error-codes/document.md#section138151918312)

 | 

Retrieval: An error occurred during the Retrieval.

 |
| 

[1021000014](../../arkts-api-error-codes/document.md#section193969191335)

 | 

Retrieval: There are invalid primary keys.

 |
| 

[1021000015](../../arkts-api-error-codes/document.md#section1273420195316)

 | 

Retrieval: A re-ranking algorithm that does not support composite primary keys was used.

 |
| 

[1021000016](../../arkts-api-error-codes/document.md#section576320538)

 | 

Retrieval: The filter input is invalid.

 |
| 

[1021000017](../../arkts-api-error-codes/document.md#section145418202032)

 | 

Retrieval: There are invalid recall names in RecallCondition.

 |
| 

[1021000018](../../arkts-api-error-codes/document.md#section78131820938)

 | 

Retrieval: The vector similarity threshold in VectorQuery is higher than the tiered threshold in VectorRerankParameter.

 |
| 

[1021000019](../../arkts-api-error-codes/document.md#section161717215314)

 | 

Retrieval: RerankMethod parameters do not match the channel type.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rag } from '@kit.DataAugmentationKit';

let session: rag.RagSession | null;

let runConfig: rag.RunConfig = {
  answerTypes: \[ rag.StreamType.THOUGHT, rag.StreamType.REFERENCE, rag.StreamType.ANSWER \]
};

let output: string = '';

if (session != null) {
  session.streamRun('Question', runConfig, ((err: BusinessError, stream: rag.Stream) => {
    if (err) {
      hilog.error(0, 'test', \`streamRun inner failed. code is ${err.code}, message is ${err.message}\`);
    } else {
      hilog.info(0, 'Index', 'StreamType: %{public}d', stream.type);
      output += stream.answer.chunk;
      if (stream.isFinished) {
        output += 'Answer ended.';
      }
    }
  })).then((data) => {
    hilog.info(0, 'Index', 'runId: %{public}d', data);
  }).catch((e: BusinessError) => {
    hilog.error(0, 'test', \`streamRun failed. code is ${e.code}, message is ${e.message}\`);
  });
}

#### \[h2\]cancel

cancel(runId: number): Promise<void>

Cancels the current Q&A. This API uses a promise to return the result asynchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

runId

 | 

number

 | 

Yes

 | 

ID of the Q&A to be canceled. The value must be the same as that returned by [streamRun](#section178721756950).

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

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1021000000](../../arkts-api-error-codes/document.md#section16205152494111)

 | 

Insufficient system resources or memory access exception.

 |
| 

[1021000008](../../arkts-api-error-codes/document.md#section16220417239)

 | 

The RAG session is Already closed.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { rag } from '@kit.DataAugmentationKit';

let session: rag.RagSession | null;

if (session != null) {
  let runId: number = 0;  // Enter the actual return value of **streamRun**.
  session.cancel(runId).then(() => {
    hilog.info(0, 'test', 'cancel successfully');
  }).catch((e: BusinessError) => {
    hilog.error(0, 'test', \`cancel failed. code is ${e.code}, message is ${e.message}\`);
  });
}

#### \[h2\]close

close(): Promise<void>

Closes a session. This API uses a promise to return the result asynchronously.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

**Start version**: 6.0.0(20)

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

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1021000000](../../arkts-api-error-codes/document.md#section16205152494111)

 | 

Insufficient system resources or memory access exception.

 |

**Example:**

import { rag } from '@kit.DataAugmentationKit';

let session: rag.RagSession | null;

onWindowStageDestroy(): void {
  // Main window is destroyed, release UI related resources
  hilog.info(0, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');

  if (session != null) {
    session.close();
  }
}

#### createRagSession

createRagSession(context: common.Context, config: Config): Promise<RagSession>

Obtains a session. This API uses a promise to return the result asynchronously. Multi-thread calls are not supported.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

[common.Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

App context.

 |
| 

config

 | 

[Config](#section1033315317182)

 | 

Yes

 | 

[RagSession](#section1312212528516) configuration.

 |

**Returns:**

| 
Type

 | 

Description

 |
| :-- | :-- |
| 

Promise<[RagSession](#section1312212528516)\>

 | 

[RagSession](#section1312212528516) object returned through a promise.

 |

**Error codes:**

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1021000000](../../arkts-api-error-codes/document.md#section16205152494111)

 | 

Insufficient system resources or memory access exception.

 |
| 

[1021000006](../../arkts-api-error-codes/document.md#section34911416737)

 | 

The RAG session already exists.

 |

**Example:**

import { AbilityConstant, ConfigurationConstant, UIAbility, Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { rag, retrieval } from '@kit.DataAugmentationKit';
import common from '@ohos.app.ability.common';
import { MyChatLLM } from './MyChatLLM';
import { window } from '@kit.ArkUI';

let session: rag.RagSession | null;

const DOMAIN = 0x0000;

onWindowStageCreate(windowStage: window.WindowStage): void {
  // Main window is created, set main page for this ability
  hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

  windowStage.loadContent('pages/Index', (err) => {
    if (err.code) {
      hilog.error(DOMAIN, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err));
      return;
    }
    hilog.info(DOMAIN, 'testTag', 'Succeeded in loading the content.');
  });

  let retrievalConfig: retrieval.RetrievalConfig = {
    channelConfigs: \[/\*Configure as required\*/\]
  };

  let retrievalCondition: retrieval.RetrievalCondition = {
    recallConditions: \[/\*Configure as required\*/\]
  };

  let config: rag.Config = {
    llm: new MyChatLLM(),
    retrievalConfig: retrievalConfig,
    retrievalCondition: retrievalCondition
  };

  rag.createRagSession(this.context, config).then((data) => {
    session = data;
  }).catch((err: BusinessError) => {
    hilog.error(DOMAIN, 'testTag', \`createRagSession failed, code is ${err.code},message is ${err.message}.\`);
  })
}

#### feedback

feedback(context: common.Context, feedbackInfo: FeedbackInfo): Promise<void>

User feedback API. After a Q&A is complete, this API can be used to evaluate this Q&A. This API returns the result asynchronously through a promise.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.DataAugmentation.RAG

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

[common.Context](../../../ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md)

 | 

Yes

 | 

App context.

 |
| 

feedbackInfo

 | 

[FeedbackInfo](#section18123940144515)

 | 

Yes

 | 

User feedback information.

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

For details about the error codes, please refer to [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md) and [ArkTS API Error Codes](../../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

[1021000000](../../arkts-api-error-codes/document.md#section16205152494111)

 | 

Insufficient system resources or memory access exception.

 |
| 

[1021000011](../../arkts-api-error-codes/document.md#section3292318836)

 | 

Some parameter does not meet the constraints. Possible causes:

1\. The length of the string parameter or the length of the numeric parameter does not comply with the constraints.

2\. The string parameter contains invalid characters.

 |

**Example:**

import { rag, retrieval } from '@kit.DataAugmentationKit';
import { relationalStore } from '@kit.ArkData';
import common from '@ohos.app.ability.common';

let context = AppStorage.get<common.UIAbilityContext>("Context") as common.UIAbilityContext;

async function feedback() {
  let valueTypeA: relationalStore.ValueType = 1;
  let valueTypeRecord: Record<string, relationalStore.ValueType> = {
    'a': valueTypeA,
    'b': valueTypeA,
  };
  let recallScoreA: retrieval.RecallScore = {
    score: 0,
    isReverseQuery: false
  };
  let recallScoreRecord: Record<string, retrieval.RecallScore> = {
    'a': recallScoreA,
    'b': recallScoreA,
    'c': recallScoreA
  };

  let channelTypeRecord: Record<number, Record<string, retrieval.RecallScore>> = {
    0: recallScoreRecord,
    1: recallScoreRecord
  };

  let itemInfo: retrieval.ItemInfo = {
    primaryKey: '',
    columns: valueTypeRecord,
    score: 0,
    recallScores: channelTypeRecord,
    features: {
      '111': 1,
      '222': 2
    },
    similarityLevel: retrieval.SimilarityLevel.LOW
  };
  let answerB: rag.Answer = {
    chunk: '111',
    data: \[itemInfo\]
  };
  let sources: Record<number, rag.Answer> = {
    0: answerB,
    1: answerB,
    2: answerB,
  };
  let feedbackInfo: rag.FeedbackInfo = {
    runId: 444,
    score: 5,
    comment: '111222333',
    source: sources
  };
  await rag.feedback(context, feedbackInfo);
}
