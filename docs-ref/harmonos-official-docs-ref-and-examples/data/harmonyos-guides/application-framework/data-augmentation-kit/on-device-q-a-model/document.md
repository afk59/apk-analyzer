# On-Device Q&A Model

#### Overview

When an app performs knowledge Q&A through the RAG API, the system goes through the following process: question decomposition, query rewriting, knowledge retrieval, and retrieval-augmented generation. This process requires multiple interactions with the LLM. You can select either of the following deployment solutions:

-   Self-built on-cloud LLMs
-   On-device Q&A model capability provided by the Kit

The on-device Q&A model solution has the following advantages:

-   No O&M costs for on-cloud LLMs
-   Enhanced data security (data processed on the device)

#### Restrictions

Currently, the on-device Q&A model supports only the Qwen model, with a model size of 7B.

You must apply for the trustlist permission before using the on-device Q&A model.

#### API Description

The following table lists the key APIs for the on-device Q&A model. For details about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-localchatmodel-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-localchatmodel-api#section48951613820)(): Promise<boolean>

 | 

Initializes the on-device Q&A model and starts the model management application.

 |
| 

[chat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-localchatmodel-api#section157381918121212)(info: [QuestionInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-localchatmodel-api#section1666712479912), config: [Config](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-localchatmodel-api#section178144421252), callback: AsyncCallback<[Answer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-localchatmodel-api#section44611173175)\>): Promise<void>

 | 

Interacts with the on-device model to implement the Q&A function.

 |

#### Applying for the Trustlist Permission

Open the [Submit a ticket online](https://developer.huawei.com/consumer/en/support/feedback/#/) page of HUAWEI Developers, describe your application for the on-device Q&A trustlist in **Overview**, select **HarmonyOS 5.0 or Later** > **App Framework** > **Data Augmentation Kit** from **Issue category**, enter detailed information in **Description**, and click **Submit**. We may need you to get the questions further clarified, so please pay attention to the progress and reply in a timely manner.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c7/v3/pe3f3ou0T9Cngow20r0IwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061952Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8521651AF3B60DFF1CF33079A8917ED8C7D61E0C83661723FA4690121735734F)

Template of the trustlist application information:

1.  App name: XXX
2.  bundleName: XXX
3.  AppID: XXX
4.  Reason for the application: Apply for the on-device Q&A model capability for XXX.

#### Development Procedure

1.  Call the [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-localchatmodel-api#section48951613820) API to start the model management application.
2.  If the model management application is started for the first time, the model management application screen is displayed. After agreeing to manage the local AI model on HarmonyOS, you can download the Qwen model.
3.  If the model management application has been started before, open the hidden icon menu in the lower right corner of the home screen and tap the AI icon. On the model management application screen that is displayed, download the Qwen model.
4.  After the model is downloaded, call the [chat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/dataaugmentation-localchatmodel-api#section157381918121212) API to start on-device Q&A.

#### Full Sample Code

import { BusinessError } from "@kit.BasicServicesKit";
import { localChatModel } from '@kit.DataAugmentationKit'

type MessageRole = 'system' | 'user' | 'assistant';

interface ChatMessage {
  role: MessageRole;
  content: string;
}

@Entry
@Component
struct Index {
  @State title: string = 'On-device LLM Q&A assistant';
  @State isStreamMode: boolean = true;
  @State messages: ChatMessage\[\] = \[\];
  @State inputText: string = '';
  @State initFlag: boolean = false;
  @State isProcessing: boolean = false;
  @State assistantContent: string = '';
  @State chatCounter: number = 0;

  // Start the model management application when loading the page.
  onPageShow() {
    console.info('modelChat onPageShow');
    this.initModel();
  }

  private scroller: Scroller = new Scroller();

  private scrollToBottom() {
    setTimeout(() => {
      this.scroller.scrollEdge(Edge.Bottom);
    }, 50);
  }

  private addMessage(role: MessageRole, content: string): void {
    const newMessage: ChatMessage = {
      role: role,
      content: content,
    };
    this.messages = \[...this.messages, newMessage\];
  }

  private async initModel(): Promise<void> {
    try {
      await localChatModel.init();
      this.initFlag = true;
      this.addMessage('system', 'Model initialization completed.');
    } catch (err) {
      const error = err as BusinessError;
      this.initFlag = false;
      this.addMessage('system', \`Model initialization error: ${error.message}\`);
    }
  }

  private async DoChat(questionId: number): Promise<void> {
    if (!this.inputText.trim() || this.isProcessing) {
      return;
    }
    const userQuestion = this.inputText.trim();
    if (!userQuestion) {
      return;
    }
    this.inputText = '';
    this.addMessage('user', userQuestion);
    this.assistantContent = "Thinking...";
    this.isProcessing = true;

    const questionInfo: localChatModel.QuestionInfo = {
      questionId: questionId,
      content: userQuestion
    };

    const localConfig: localChatModel.Config = {
      isStream: this.isStreamMode
    };

    const localChatCallback = async (err: BusinessError, ans: localChatModel.Answer): Promise<void> => {
      this.scrollToBottom();
      if (err) {
        if (this.assistantContent == "Thinking...") {
          this.assistantContent = "";
          this.isProcessing = false;
        }
        // Error code related to model running.
        console.error('modelChat Callback failed:', err.message);
        this.addMessage('system', \`localChatCallback: error code is ${err.code},  ${err.message}\`);
        this.scrollToBottom();
      }
      if (ans.content && ans.content.trim() !== '') {
        if (this.assistantContent == "Thinking...") {
          this.assistantContent = "";
        }
        this.assistantContent += ans.content;
        this.scrollToBottom();
      }
      this.scrollToBottom();
      if (ans.isFinished) {
        console.log('modelChat finished');
        this.addMessage('assistant', this.assistantContent);
        this.isProcessing = false;
      }

    };
    try {
      console.log('modelChat Starting chat...');
      localChatModel.chat(questionInfo, localConfig, localChatCallback);
    } catch (err) {
      // Error code related to input parameters.
      const error = err as BusinessError;
      console.error('modelChat Chat failed:', error.message);
      this.addMessage('system', \`chat: error code is ${error.code},  ${error.message}\`);
      this.isProcessing = false;
    }
  }

  private clearChat(): void {
    this.messages = \[\];
  }

  build() {
    Stack({ alignContent: Alignment.Top }) {
      Column() {
        Row() {
          Text(this.title)
            .fontSize(20)
            .fontWeight(FontWeight.Bold)
            .fontColor('#1a73e8')
            .margin({ left: 12 })

          Circle()
            .width(10)
            .height(10)
            .margin({ left: 12 })
            .fill(this.initFlag ? '#0f0' : '#f00')
            .opacity(0.8)

          Text(this.initFlag ? 'Ready' : 'Not ready')
            .margin({ left: 6 })
            .fontSize(12)
            .fontColor('#666')

          Blank()

          Row() {
            Button(this.isStreamMode ? 'Streaming' : 'Non-streaming')
              .width(70)
              .height(25)
              .fontSize(12)
              .margin({ right: 20 })
              .backgroundColor(Color.Gray)
              .fontColor(Color.White)
              .borderRadius(12.5)
              .onClick(() => {
                this.isStreamMode = !this.isStreamMode;
                this.addMessage('system', \`Switched to ${this.isStreamMode ? 'Streaming Q&A' : 'Non-streaming Q&A'} Mode\`);
              })
          }
          .margin({ right: 12 })
        }
        .width('100%')
        .height(50)
        .backgroundColor(Color.White)
        .borderRadius(16)
        .shadow({
          radius: 4,
          color: '#1a73e888',
          offsetX: 0,
          offsetY: 2
        })
        .margin({ bottom: 12 })

        // Chat area.
        Scroll(this.scroller) {
          Column() {
            ForEach(this.messages, (msg: ChatMessage, index: number) => {
              if (msg.role === 'system') {
                Row() {
                  Text(msg.content)
                    .fontSize(14)
                    .fontColor('#666')
                    .textAlign(TextAlign.Center)
                    .padding(8)
                }
                .width('100%')
                .justifyContent(FlexAlign.Center)
                .margin({ top: index === 0 ? 0 : 12 })
              } else if (msg.role === 'user') {
                Row() {
                  Blank()
                  Text(msg.content)
                    .fontSize(16)
                    .fontColor(Color.White)
                    .padding(10)
                    .backgroundColor('#1a73e8')
                    .borderRadius(12)
                }
                .width('100%')
                .margin({ top: 12 })
                .justifyContent(FlexAlign.End)
              } else if (msg.role === 'assistant') {
                Row() {
                  Column() {
                    Text(msg.content)
                      .fontSize(16)
                      .fontColor('#333')
                      .lineHeight(20)
                      .padding(10)
                      .backgroundColor(Color.White)
                      .borderRadius(12)
                  }
                  .borderRadius(12)
                  .margin({ left: 8 })

                  Blank()
                }
                .width('100%')
                .margin({ top: 12 })
                .justifyContent(FlexAlign.Start)
              }
            }, (msg: ChatMessage) => msg.toString())

            // Loading indicator.
            if (this.isProcessing) {
              Row() {
                Column() {
                  Text(this.assistantContent)
                    .fontSize(16)
                    .fontColor('#333')
                    .lineHeight(20)
                    .padding(10)
                    .backgroundColor(Color.White)
                    .borderRadius(12)
                }
                .borderRadius(12)
                .margin({ left: 8 })

                Blank()
              }
              .width('100%')
              .margin({ top: 12 })
            }
          }
          .padding(12)
          .width('100%')
        }
        .width('100%')
        .layoutWeight(1)
        .margin({ bottom: 12 })

        // Input area.
        Column() {
          Row() {
            TextInput({ text: this.inputText, placeholder: 'Enter your question...' })
              .flexGrow(1)
              .height(42)
              .fontSize(16)
              .padding(8)
              .backgroundColor(Color.White)
              .borderRadius(21)
              .width('85%')
              .onChange((value: string) => {
                this.inputText = value;
              })
              .onSubmit(() => {
                if (!this.isProcessing && this.inputText.trim() !== '') {
                  const chatId = this.chatCounter++;
                  this.DoChat(chatId);
                }
              })

            Button('Send')
              .width(72)
              .height(42)
              .fontSize(16)
              .margin({ left: 8 })
              .backgroundColor('#1a73e8')
              .fontColor(Color.White)
              .borderRadius(21)
              .onClick(() => {
                if (!this.isProcessing && this.inputText.trim() !== '') {
                  const chatId = this.chatCounter++;
                  this.DoChat(chatId);
                }
              })
              .opacity(this.isProcessing || this.inputText.trim() === '' ? 0.6 : 1)

            Button("Clear")
              .width(72)
              .height(42)
              .fontSize(16)
              .margin({ left: 8 })
              .fontColor('#fff')
              .backgroundColor('#ea4335')
              .borderRadius(18)
              .onClick(() => {
                this.clearChat();
              })
          }
          .width('100%')
          .justifyContent(FlexAlign.SpaceBetween)
          .alignItems(VerticalAlign.Center)
        }
        .width('100%')
        .padding(8)
        .backgroundColor(Color.White)
        .borderRadius(16)
        .shadow({
          radius: 4,
          color: '#1a73e888',
          offsetX: 0,
          offsetY: 2
        })
      }
      .width('100%')
      .height('100%')
      .padding(12)
      .backgroundColor('#f0f5ff')
    }
    .width('100%')
    .height('100%')
  }
}

The Q&A process requires interaction with the LLM. Therefore, you need to apply for the network permission for your app.

// Set the **requestPermissions** field in **module.json5**.
"requestPermissions": \[
  {
    "name": "ohos.permission.INTERNET"
  }
\],
