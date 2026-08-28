# Full Sample Code

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6d/v3/Nt5n1COTSyuqG2uPbAAmCg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6A78B077D03FA3FFC71CD94DE2A7C4029507FFAB5E2370B5FA9DC3D33D4A6BA6)

Apply for the network permission first. For details, please refer to [Getting Started](../knowledge-q-a/document.md#section84162596597).

#### EntryAbility.ets

This file implements the app lifecycle. When starting an app, this file creates a connection between the RagSession and database. When closing an app, this file releases the connection between the RagSession and database.

// src/main/ets/entryability/EntryAbility.ets
import { AbilityConstant, UIAbility, Want, common } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';
import SetUp from '../entryability/SetUp';
import Config from '../entryability/Config';
import { rag } from '@kit.DataAugmentationKit';

const DOMAIN = 0x0000;

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onDestroy');
  }

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

    AppStorage.setOrCreate<common.UIAbilityContext>('Context', this.context);

    let setUp: SetUp = new SetUp();
    setUp.initTable().then(() => {
      setUp.insertData();
      AppStorage.setOrCreate<SetUp>('SetUpObject', setUp);
    });

    let config: Config = new Config();
    rag.createRagSession(this.context, config.getRAGConfig()).then((data) => {
      AppStorage.setOrCreate<rag.RagSession>('RagSessionObject', data);
    }).catch((err: BusinessError) => {
      hilog.error(DOMAIN, 'testTag', \`createRagSession failed, code is ${err.code},message is ${err.message}.\`);
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
    const session = AppStorage.get<rag.RagSession>('RagSessionObject') as rag.RagSession;
    session?.close().catch(() => {
      hilog.error(DOMAIN, 'testTag', 'close rag session failed');
    });
    const setup = AppStorage.get<SetUp>('SetUpObject') as SetUp;
    setup?.closeStore();
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(DOMAIN, 'testTag', '%{public}s', 'Ability onBackground');
  }
}

#### SetUp.ets

The **SetUp.ets** file constructs data sources. Currently, this file reads data from a built-in JSON file and inserts the data into a database with knowledge processing enabled. After the data is updated, knowledge processing is automatically triggered to form a knowledge base.

// src/main/ets/entryability/SetUp.ets
import { UIAbility, common } from '@kit.AbilityKit';
import { relationalStore } from '@kit.ArkData';
import { buffer } from '@kit.ArkTS';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'SetUp';

export default class SetUp extends UIAbility {
  storeName: string = 'testmail\_store.db';  // Use the database name specified in the **knowledge\_schema.json** file.
  storeConfig: relationalStore.StoreConfig = {
    name: this.storeName,
    securityLevel: relationalStore.SecurityLevel.S3,
    enableSemanticIndex: true,  // For the source database, set this parameter to **true** to trigger knowledge processing.
    tokenizer: relationalStore.Tokenizer.CUSTOM\_TOKENIZER
  };
  store?: relationalStore.RdbStore;

  async getStore() {
    try {
      if (!this.store) {
        let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext; // Obtain the global context.
        this.store = await relationalStore.getRdbStore(context, this.storeConfig);
      }
    } catch (err) {
      hilog.error(0, TAG, \`Init DB failed, code is ${err.code},message is ${err.message}.\`);
    }
    return this.store;
  }

  async initTable() {
    try {
      const tmpStore = await this.getStore();
      const createTableSql = 'CREATE TABLE IF NOT EXISTS email(id integer primary key, subject text, content text, ' +
        'image\_text text, attachment\_names text, inline\_files text, sender text, receivers text, received\_date text);';
      await tmpStore?.execute(createTableSql, 0, undefined);
      hilog.info(0, TAG, 'InitTable success');
    } catch (err) {
      hilog.error(0, TAG, \`Init DB failed, code is ${err.code},message is ${err.message}.\`);
    }
  }

  async insertData() {
    try {
      let context = AppStorage.get<common.UIAbilityContext>('Context') as common.UIAbilityContext; // Obtain the global context.
      const fileList = context.resourceManager.getRawFileListSync('');
      let dataIndex = 0;
      for (let file of fileList) {  // Parse data from the JSON file to the database.
        if (!file.startsWith('sourceData') || !file.endsWith('.json')) {
          hilog.info(0, TAG, \`file ${file} skip\`);
          continue;
        }
        hilog.info(0, TAG, \`file ${file} start\`);
        try {
          const rawFileData = await context.resourceManager.getRawFileContent(file);
          const fileData: string = buffer.from(rawFileData).toString();
          const resultObjArr = JSON.parse(fileData) as Array<object>;
          let jsonObj: object | undefined;
          for (let i = 0; i < resultObjArr.length; i++) {
            try {
              jsonObj = resultObjArr\[i\];
              let sender: string = jsonObj?.\['sender\_name'\];
              if (!sender || sender.length == 0) {
                sender = 'undefined';
              }
              const receiverStr: string = JSON.stringify(jsonObj\['to'\]);
              const formattedDateStr: string = jsonObj?.\['received\_time'\]?.replace(' ', 'T');
              let received\_date = Date.parse(formattedDateStr);
              if (!received\_date || Number.isNaN(received\_date)) {
                received\_date = 0;
              }
              let subject: string = jsonObj?.\['subject'\]?.replace(/'/g, '');
              let doc: string = jsonObj?.\['body'\]?.replace(/'/g, '');
              let sql = \`insert or replace into email VALUES(${dataIndex}, '${subject}', '${doc}', '',\` +
                \` '', '', '${sender}', '${receiverStr}', '${received\_date}');\`
              const tmpStore = await this.getStore();
              await tmpStore?.executeSql(sql);
              dataIndex++;
            } catch (e) {
              hilog.error(0, TAG, \`Insert failed, code is ${e.code},message is ${e.message}, jsonObj: ${jsonObj}\`);
            }
          }
        } catch (e) {
          hilog.error(0, TAG, \`Load file failed, code is ${e.code},message is ${e.message}\`);
        }
        hilog.info(0, TAG, \`file ${file} end\`);
      }
      hilog.info(0, TAG, 'insertData end');
    } catch (err) {
      hilog.error(0, TAG, \`Init DB failed, code is ${err.code},message is ${err.message}.\`);
    }
  }

  async closeStore() {
    try {
      await this.store?.close();
    } catch (e) {
      hilog.error(0, TAG, \`Close store failed, code is ${e.code},message is ${e.message}.\`);
    }
  }
}

#### HttpUtils.ets

The **HttpUtils.ets** file contains an HTTP utility class for interacting with the LLM. It assembles packets to be sent to the LLM and registers the callback for receiving streaming HTTP messages. You can select a proper LLM as required. The sample code uses [ModelArts](https://console.huaweicloud.com/modelarts). You need to replace **\*\*\*\*replace your API key in here\*\*\*\*** with the actual API key.

// src/main/ets/entryability/HttpUtils.ets
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

  end() { // Unregister the data receiving and data ending listeners and release the httpRequest.
    this.httpRequest?.off('dataReceive');
    this.httpRequest?.destroy();
    this.httpRequest = undefined;
  }

  cancel() {
    this.httpRequest?.off('dataReceive');
    this.httpRequest?.destroy();
    this.httpRequest = undefined;
  }
}

export default new HttpUtils;

#### MyChatLlm.ets

An app inherits from and implements the ChatLLM class, which is equivalent to the process of implementing an LLM client in the app. The LLM client will be passed as an input parameter to the RagSession during RagSession creation.

// src/main/ets/entryability/MyChatLlm.ets
import { rag } from '@kit.DataAugmentationKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { JSON, util } from '@kit.ArkTS';
import HttpUtils from './HttpUtils';

const TAG = "MyChatLLM";

function parseLLMResponse(data: ArrayBuffer): rag.LLMStreamAnswer | undefined {
  try {
    let decoder = util.TextDecoder.create(\`"utf-8"\`);
    let str = decoder.decodeToString(new Uint8Array(data));
    hilog.info(0, TAG, str);
    let chunk = '';
    let isFinished: boolean = (str.length < 20);
    for (let resultStr of str.split('data:')) {
      if (resultStr.trim() == ('\[DONE\]')) {
        isFinished = true;
        break;
      }
      if (resultStr.trim().length == 0) {
        continue;
      }
      try {
        let obj = JSON.parse(resultStr.trim());
        if ((obj as object)?.\['choices'\].length === 0) {
          continue;
        }
        if ((obj as object)?.\['choices'\]\[0\]?.\['delta'\]?.\['reasoning\_content'\]) {
          chunk += (obj as object)?.\['choices'\]\[0\]\['delta'\]\['reasoning\_content'\];
        } else if ((obj as object)?.\['choices'\]\[0\]?.\['delta'\]?.\['content'\]) {
          chunk += (obj as object)?.\['choices'\]\[0\]\['delta'\]\['content'\];
        }
      } catch (err) {
        hilog.error(0, TAG, \`Parse LLM response failed, resultStr: ${resultStr}\`);
      }
    }
    let answer: rag.LLMStreamAnswer = {
      isFinished: isFinished,
      chunk: chunk
    };
    return answer;
  } catch (err) {
    hilog.error(0, TAG, \`Parse LLM response failed, error code: ${err.code}, error message: ${err.message}\`);
  }
  return undefined;
}

export default class MyChatLLM extends rag.ChatLLM {
  async streamChat(query: string, callback: Callback<rag.LLMStreamAnswer>): Promise<rag.LLMRequestInfo> {
    let ret: rag.LLMRequestStatus = rag.LLMRequestStatus.LLM\_SUCCESS;
    try {
      let dataCallback = async (data: ArrayBuffer) => { // The callback function receives data, parses data, and assembles and returns **LLMStreamAnswer**.
        hilog.debug(0, TAG, 'on callback enter. data length: %{public}d', data.byteLength);
        // Parse the packet returned by the LLM. The logic varies depending on the selected model.
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
      ret = rag.LLMRequestStatus.LLM\_REQUEST\_ERROR;  // This error code is for reference only. Your app can return other LLM error codes according to the service requirements.
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

#### Config.ets

The **Config.ets** file assembles the input parameters used for creating a RagSession. For details about how to set the parameters, see [Intelligent Data Retrieval](../../intelligent-data-retrieval/document.md).

// src/main/ets/entryability/Config.ets
import { common, UIAbility } from '@kit.AbilityKit';
import { rag, retrieval } from '@kit.DataAugmentationKit';
import { relationalStore } from '@kit.ArkData';
import MyChatLlm from './MyChatLlm';

export default class Config extends UIAbility {
  getRetrievalConfig() {
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
    let retrievalConfig: retrieval.RetrievalConfig = {
      channelConfigs: \[channelConfigInvIdx, channelConfigVector\]
    };
    return retrievalConfig;
  }

  getRetrivalCondition() {
    let recallConditionInvIdx: retrieval.InvertedIndexRecallCondition = {
      ftsTableName: 'email\_inverted',
      fromClause: 'select email\_inverted.reference\_id as rowid, \* from email INNER JOIN email\_inverted ON email.id = email\_inverted.reference\_id',
      primaryKey: \['chunk\_id'\],
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
      fromClause: 'email\_vector',
      primaryKey: \['id'\],
      responseColumns: \['reference\_id', 'chunk\_id', 'chunk\_source', 'repr'\],
      recallName: 'vectorRecall',
      deepSize: 500
    };
    let rerankMethod: retrieval.RerankMethod = {
      rerankType: retrieval.RerankType.RRF,
      isSoftmaxNormalized: true,
    };
    let retrievalCondition: retrieval.RetrievalCondition = {
      rerankMethod: rerankMethod,
      recallConditions: \[recallConditionInvIdx, recallConditionVector\],
      resultCount: 5
    };
    return retrievalCondition;
  }

  getRAGConfig() {
    let retrievalConfig: retrieval.RetrievalConfig = this.getRetrievalConfig();
    let retrievalCondition: retrieval.RetrievalCondition = this.getRetrivalCondition();
    let config: rag.Config = {
      llm: new MyChatLlm(),
      retrievalConfig: retrievalConfig,
      retrievalCondition: retrievalCondition
    };
    return config;
  }
}

#### Index.ets

The **Index.ets** file implements the app UI, including the question input text box, button for starting Q&A, and answer output text box.

// src/main/ets/pages/Index.ets
import { BusinessError } from '@kit.BasicServicesKit';
import { rag } from '@kit.DataAugmentationKit';
import hilog from '@ohos.hilog';

@Entry
@Component
struct Index {
  @State inputStr: string = 'Full sample code for the knowledge Q&A development guide';
  @State answerStr: string = '';
  @State thoughtStr: string = '';

  build() {
    Column() {
      Row({ space: 8 }) {
        TextArea({ text: this.inputStr, placeholder: 'Input question here!' })
          .margin({ top: 8 })
          .borderStyle(BorderStyle.Dotted)
          .onChange((newValue) => {
            this.inputStr = newValue;
          })
          .width('95%')
          .height('15%')
          .fontWeight(FontWeight.Bold)
      }

      Button('streamRun')
        .onClick(async () => {
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
        })
        .width('30%')
        .height('5%')
      Column({ space: 2 }) {
        Text(this.thoughtStr)
          .fontSize(12)
          .fontColor(Color.Gray)
          .padding(8)
          .width('95%')
          .height('auto')
        Text(this.answerStr)
          .padding(8)
          .width('95%')
          .height('auto')
      }
      .backgroundColor(0xF5DEB3)
      .width('95%')
      .height('75%')
    }
    .height('100%')
    .width('100%')
  }
}

#### knowledge\_schema.json

This file is a schema file for knowledge processing, which is used to define the processing logic for the source database during knowledge processing.

// src/main/resources/rawfile/arkdata/knowledge/knowledge\_schema.json ------ Delete this comment during app development.
{
  "knowledgeSource": \[{
    "version": 1,
    "dbName": "testmail\_store.db",
    "tables": \[{
      "tableName": "email",
      "referenceFields": \["id"\],
      "knowledgeFields": \[{
        "columnName": "subject",
        "type": \["Text"\]
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
	    "path": "$\[\*\].uri"
	  }
	\]
      },
      {
        "columnName": "sender",
        "type": \["Scalar"\],
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
      }\]
    }\]
  }\]
}

#### sourceData.json

The content in the **sourceData.json** file is the simulated source data for testing, which is inserted into the app database table. In actual scenarios, app data is specified on the UI or obtained from the server.

// src/main/resources/rawfile/sourceData.json ------ This file is used only for inserting test data. Preconfigure database data as required.
\[{
  "subject": "Mobile Phone Discount Policy",
  "sender\_name": "zhangsan",
  "sender\_email": "zhangsan@xxx.com",
  "received\_time": "2025-05-15 15:49:04.135",
  "recipients": \[
    {
      "Address": "lisi@xxx.com",
      "name": "lisi",
      "Type": 1
    },
    {
      "Address": "wangwu@xxx.com",
      "name": "wangwu",
      "Type": 2
    },
    {
      "Address": "zhaoliu@xxx.com",
      "name": "zhaoliu",
      "Type": 3
    }
  \],
  "to": \[
    "lisi"
  \],
  "cc": \[
    "wangwu"
  \],
  "bcc": \[
    "zhaoliu"
  \],
  "attachment": \[\],
  "body": "Preference policy: \\r\\n10% discount for flagship series; 20% discount for non-flagship series.",
  "unread": false
}\]
