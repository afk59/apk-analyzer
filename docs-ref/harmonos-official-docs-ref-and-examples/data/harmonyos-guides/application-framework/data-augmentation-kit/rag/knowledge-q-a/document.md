# Knowledge Q&A

#### Restrictions

1.  Knowledge Q&A requires that knowledge from the source database be processed to generate a knowledge base. Otherwise, Q&A cannot be performed.
2.  The [createRagSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section14201103320529) and [streamRun](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section178721756950) APIs do not support multi-thread calls.
3.  The maximum question length is 1000 characters. (A Chinese character in UTF-8 occupies three characters.)
4.  When a user asks a question, RAG uses the user's latest Q&A content as the context to generate an answer to this question.
5.  RAG can return a maximum of 600 chunks during recall.
6.  RAG does not provide sensitive keyword detection. You need to provide sensitive keyword detection on user input and the content returned by RAG.
7.  The LLM you use must support a context window of at least 30,000 tokens. For example, you can choose models like Qwen2.5-7B-32K, Mistral-7B-Instruct-v0.2, or Llama-3.1-8B. Otherwise, knowledge Q&A may fail due to the context length limit of the LLM.
8.  You can choose your desired LLM, but the languages supported for Q&A depend on the LLM you choose.

#### API Description

The following table lists the key APIs for knowledge Q&A. For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

abstract [streamChat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section157381918121212)(query: string, callback: Callback<[LLMStreamAnswer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section178144421252)\>): Promise<[LLMRequestInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section1816505018227)\>

 | 

This API must be implemented when the ChatLLM class is inherited to implement an LLM client. RAG calls this API to interact with the LLM when preprocessing questions before retrieval and generating answers after retrieval.

 |
| 

[createRagSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section14201103320529)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-inner-application-context), config: [Config](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section1033315317182)): Promise<[RagSession](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section1312212528516)\>

 | 

This API obtains a session for knowledge Q&A.

 |
| 

[streamRun](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section178721756950)(question: string, config: [RunConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section126313912116), callback: AsyncCallback<[Stream](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section158611717585)\>): Promise<number>

 | 

This API is used for knowledge Q&A. It passes questions and Q&A configuration items. When RAG generates answers to questions, this API triggers the callback function to stream data.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/65/v3/M-zXzNbARM2AIjso85yIWw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ACC8FB23AFDA72E0D4351B70C448276F628549A0B4C8DA5274D28729441FA42B)

The above APIs must be called within the lifecycle of a page or custom component.

#### Getting Started

1.  Apply for the network permission. The [streamChat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section157381918121212) API requires interaction with the LLM. Therefore, you need to apply for the network permission for your app.
    
    // Set the **requestPermissions** field in **module.json5**.
    // src/main/module.json5
    "requestPermissions": \[
      {
        "name": "ohos.permission.INTERNET"
      }
    \],
    
2.  Configure knowledge processing. For details, please refer to [Knowledge Processing](../../knowledge-processing/document.md).

#### Development Procedure

The following describes only the key development steps using key code. For details about development cases, please refer to [Full Sample Code](../full-sample-code/document.md). For details about a streaming Q&A process involving interactions with the RagSession, ChatLLM, and knowledge base, please refer to [Streaming Q&A Process](#section1350294615400).

1.  Import the kit. The main dependency of this module is as follows. You can add other dependencies as required.
    
    import { rag } from '@kit.DataAugmentationKit';
    
2.  Create an HTTP utility class to interact with the LLM. You can also use WebSocket (see [Network Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/network-api-arkts)) or other methods to interact with the LLM. Here, the qwen3-235b-a22b model of the [ModelArts](https://console.huaweicloud.com/modelarts) is used as an example. You can select a proper LLM as required. The sample code includes the following sections:
    
    -   Assemble the request packet for interacting with the LLM. Streaming interaction is recommended for better experience.
    -   Register the callback functions for the LLM to receive data and end output, implementing streaming access to the LLM.
    -   Initialize the LLM and send a request to the LLM.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { http } from '@kit.NetworkKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = 'HttpUtils';
    
    class HttpUtils {
      httpRequest?: http.HttpRequest;
      url: string = 'https://api.modelarts-maas.com/v1/chat/completions'; // You need to change the URL and the model in the following content to those of the LLM you have chosen.
      isFinished: boolean = false;
    
      initOption(question: string) {
        let option: http.HttpRequestOptions = {
          // Request method.
          method: http.RequestMethod.POST,
          // Request header.
          header: {
            'Content-Type': 'application/json',
            // API-KEY from Model
            'Authorization': \`Bearer \*\*\*\*replace your API key in here\*\*\*\*\`
          },
          // Request body.
          extraData: {
            'stream': true,
            'temperature': 0.1,
            'max\_tokens': 1000,
            'frequency\_penalty': 1,
            'model': 'qwen3-235b-a22b',
            'top\_p': 0.1,
            'presence\_penalty': -1,
            'messages': JSON.parse(question),
            "chat\_template\_kwargs": {
              // Disable thinking.
              "enable\_thinking": false
            }
          }
        };
        return option;
      }
    
      async requestInStream(question: string) { // Assemble the options of the streaming request and initiate the streaming request.
        if (!this.httpRequest) {
          this.httpRequest = http.createHttp();
        }
        this.httpRequest?.requestInStream(this.url, this.initOption(question)).catch((err: BusinessError) => {
          hilog.error(0, TAG, 'Failed to request. Cause: %{public}s', JSON.stringify(err));
        });
        this.isFinished = false;
      }
    
      on(callback: Callback<ArrayBuffer>) { // Register the data receiving and data ending listeners.
        if (!this.httpRequest) {
          this.httpRequest = http.createHttp();
        }
        this.httpRequest.on('dataReceive', callback);
      }
    }
    
    export default new HttpUtils;
    
3.  Inherit from and implement the [ChatLLM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section1400115191116) class. Interact with the LLM in this class and send the result returned by the LLM to the RagSession through the callback function.
    
    import { rag } from '@kit.DataAugmentationKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { JSON, util } from '@kit.ArkTS';
    import HttpUtils from './HttpUtils';
    
    const TAG = "MyChatLLM";
    
    export default class MyChatLLM extends rag.ChatLLM {
      async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
        let ret: rag.LLMRequestStatus = rag.LLMRequestStatus.LLM\_SUCCESS;
        try {
          let dataCallback = async (data: ArrayBuffer) => { // The callback function receives data, parses data, and assembles and returns **LLMStreamAnswer**.
            hilog.debug(0, TAG, 'on callback enter. data length: %{public}d', data.byteLength);
            // Parse the packet returned by the LLM. The logic varies depending on the selected model. The specific parsing code is omitted here. For details, please refer to the full sample code.
            const answer = parseLLMResponse(data);
            if (!answer) {
              return;
            }
            HttpUtils.isFinished = answer.isFinished;
            callback(answer);
            hilog.debug(0, 'MyChatLLM', 'Request LLM success. isFinished: %{public}s, data: %{public}s',
              Number(answer.isFinished).toString(), answer.chunk);
          };
    
          HttpUtils.on(dataCallback);
          HttpUtils.requestInStream(query);
        } catch (err) {
          hilog.error(0, TAG, \`Request LLM failed, error code: ${err.code}, error message: ${err.message}\`);
          ret = rag.LLMRequestStatus.LLM\_REQUEST\_ERROR; // This error code is for reference only. Your app can return other LLM error codes according to the service requirements.
        }
        return {
          chatId: 0,
          status: ret,
        };
      }
      cancel(chatId: number): void {
        hilog.info(0, TAG, \`The request for the large model has been canceled. chatId: ${chatId}\`);
        HttpUtils.cancel();
      }
    }
    
4.  Create the parameters in [Config](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section1033315317182). The following describes only the main parameters. For details about all parameters, please refer to [Intelligent Data Retrieval](../../intelligent-data-retrieval/document.md).
    
    -   [RetrievalConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-retrieval-api#section95236010016) configures the database of the knowledge base. During [knowledge processing](../../knowledge-processing/document.md#section13189205451011), two types of knowledge base tables are generated: vector table and inverted index table.
        
        import { common, UIAbility } from '@kit.AbilityKit';
        import { rag, retrieval } from '@kit.DataAugmentationKit';
        import { relationalStore } from '@kit.ArkData';
        
        let storeConfigVector: relationalStore.StoreConfig = {
          name: 'testmail\_store\_vector.db', // Name of the vector database file after knowledge processing, which is suffixed with **\_vector** based on the original database name.
          securityLevel: relationalStore.SecurityLevel.S3,
          vector: true  // Set this parameter to **true** for the vector database.
        };
        let storeConfigInvIdx: relationalStore.StoreConfig = {
          name: 'testmail\_store.db', // Name of the inverted index database after knowledge processing. The inverted index database is the original database.
          securityLevel: relationalStore.SecurityLevel.S3,
          tokenizer: relationalStore.Tokenizer.CUSTOM\_TOKENIZER
        };
        let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext;
        let channelConfigVector: retrieval.ChannelConfig = {
          channelType: retrieval.ChannelType.VECTOR\_DATABASE,
          context: context,
          dbConfig: storeConfigVector
        };
        let channelConfigInvIdx: retrieval.ChannelConfig = {
          channelType: retrieval.ChannelType.INVERTED\_INDEX\_DATABASE,
          context: context,
          dbConfig: storeConfigInvIdx
        };
        // **RetrievalConfig** data that is successfully created.
        let retrievalConfig: retrieval.RetrievalConfig = {
          channelConfigs: \[channelConfigInvIdx, channelConfigVector\]
        };
        
    -   [RetrievalCondition](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-retrieval-api#section4881955192413) configures retrieval conditions and ranking after multi-channel recall. The **fromClause** parameter indicates the name of the target index to be queried. You can set it to a virtual table formed by the service database table and the database table generated during knowledge processing based on the following sample code. The **responseColumns** parameter indicates the collection of recalled fields, which are columns in the database table specified by **fromClause**. For details about the database table structure of the knowledge base, please refer to [Table 1](../../knowledge-processing/document.md#table1186182016388) and [Table 2](../../knowledge-processing/document.md#table57920393405).
        
        import { retrieval } from '@kit.DataAugmentationKit';
        
        let recallConditionInvIdx: retrieval.InvertedIndexRecallCondition = {
          ftsTableName: 'email\_inverted',
          // Use **id** (primary key of the original database table, which is configured in the knowledge processing schema) and **reference\_id** (field in the knowledge base table) to associate the original database table with the knowledge base table, increasing the data range for retrieval and recall.
          fromClause: 'select email\_inverted.reference\_id as rowid, \* from email INNER JOIN email\_inverted ON email.id = email\_inverted.reference\_id',
          primaryKey: \['chunk\_id'\],
          // Set **responseColumns** to the columns in the database table specified by **fromClause**. If the columns exceed the range configured in **fromClause**, the retrieval fails.
          responseColumns: \['reference\_id', 'chunk\_id', 'chunk\_source', 'chunk\_text', 'subject', 'image\_text',
            'attachment\_names'\],
          deepSize: 500,
          recallName: 'invertedvectorRecall',
        };
        let floatArray = new Float32Array(128).fill(0.1);
        let vectorQuery: retrieval.VectorQuery = {
          column: 'repr',
          value: floatArray,
          similarityThreshold: 0.1
        };
        let recallConditionVector: retrieval.VectorRecallCondition = {
          vectorQuery: vectorQuery,
          // Configure only the vector table of the knowledge base as the query target.
          fromClause: 'email\_vector',
          primaryKey: \['id'\],
          // Configure the columns in the vector table of the knowledge base as the recall columns.
          responseColumns: \['reference\_id', 'chunk\_id', 'chunk\_source', 'repr'\],
          recallName: 'vectorRecall',
          deepSize: 500
        };
        let rerankMethod: retrieval.RerankMethod = {
          rerankType: retrieval.RerankType.RRF,
          isSoftmaxNormalized: true,
        };
        // **RetrievalCondition** data that is successfully created.
        let retrievalCondition: retrieval.RetrievalCondition = {
          rerankMethod: rerankMethod,
          recallConditions: \[recallConditionInvIdx, recallConditionVector\],
          resultCount: 5
        };
        
    -   Construct the **Config** data. Use the instances of the custom class of the ChatLLM inherited in step 3 as the parameters in [ChatLLM](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section1400115191116).
        
        import { rag } from "@kit.DataAugmentationKit";
        
        let config: rag.Config = {
          llm: new MyChatLlm(), // For details, see the sample code in step 3.
          retrievalConfig: retrievalConfig, // For details, see the **RetrievalConfig** sample code in this step.
          retrievalCondition: retrievalCondition  // For details, see the **RetrievalCondition** sample code in this step.
        }
        
    
5.  Create a RagSession.
    
    import { UIAbility } from '@kit.AbilityKit';
    import { rag } from '@kit.DataAugmentationKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
    // Create a RagSession and save it to the app context.
    rag.createRagSession(this.context, config).then((data) => { // For details about the value of **config**, see the sample code in step 4.
      AppStorage.setOrCreate<rag.RagSession>('RagSessionObject', data);
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, 'testTag', \`createRagSession failed, code is ${err.code},message is ${err.message}.\`);
    });
    
6.  Use the **streamRun()** function of the RagSession created in step 5 to perform Q&A.
    
    -   The **answerTypes** parameter is used to specify the data type ([StreamType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-rag-api#section172106569558)) of the streaming output. Currently, three data types are configured in the sample code. Therefore, the callback function of the **streamRun()** function will generate data of the three types.
    -   The **streamRun()** function generates data in incremental streaming mode. Therefore, you need to concatenate the results.
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { rag } from '@kit.DataAugmentationKit';
    import hilog from '@ohos.hilog';
    
    // Obtain the created RagSession.
    let session: rag.RagSession = AppStorage.get<rag.RagSession>('RagSessionObject') as rag.RagSession;
    let config: rag.RunConfig = {
      // Specify the streaming output type.
      answerTypes: \[rag.StreamType.THOUGHT, rag.StreamType.ANSWER\]
    };
    this.thoughtStr = '';
    this.answerStr = '';
    // Initiate a question.
    session.streamRun(this.inputStr, config, ((err: BusinessError, stream: rag.Stream) => {
      // Trigger the callback to receive the answer and process the answer information.
      if (err) {
        this.answerStr = \`streamRun inner failed. code is ${err.code}, message is ${err.message}\`;
      } else {
        // Select a processing method based on the data type.
        switch (stream.type) {
          case rag.StreamType.THOUGHT:
            this.thoughtStr += stream.answer.chunk;
            break;
          case rag.StreamType.ANSWER:
            this.answerStr += stream.answer.chunk;
            break;
          case rag.StreamType.REFERENCE:
          default:
            hilog.info(0, 'Index', \`streamRun msg: ${JSON.stringify(stream)}\`);
        }
      }
    })).catch((e: BusinessError) => {
      this.answerStr = \`streamRun failed. code is ${e.code}, message is ${e.message}\`;
    });
    

#### Streaming Q&A Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d/v3/Do54qdGEQCeDFVZRW_SpCw/en-us_image_0000002402299685.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF856C9A69227A1678C5820B053F5CCE53FFF986D05307AD69B80B4667EB3982)
