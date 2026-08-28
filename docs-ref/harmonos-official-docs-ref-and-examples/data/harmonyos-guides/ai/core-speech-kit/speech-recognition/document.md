# Speech Recognition

This capability can be used to convert a piece of audio information (English within a Chinese context and Chinese, no more than 60s in short speech mode and no more than 8 hours in long speech mode) into text. The audio information can be a PCM audio file or real-time audio.

#### Use Case

Devices such as mobile phones and tablets, even disconnected from the Internet, can offer the ASR function for users with hearing impairments or in scenarios where listening is not convenient.

#### Restrictions

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

Speech recognition

 | 

-   Supported language: Mandarin Chinese
-   Supported model type: offline
-   Speech duration: no more than 60s in short speech mode and no more than 8 hours in long speech mode

 |

#### Development Procedure

1.  Add the classes related to speech recognition to the project.
    
    import { speechRecognizer } from '@kit.CoreSpeechKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the [createEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section53411946183318) method to initialize the engine and create a [SpeechRecognitionEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section153101728203110) instance.
    
    The **createEngine** method can be called in two ways. The following uses one way as an example. For details about the other way, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer).
    
    let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;
    let sessionId: string = '123456';
    // Create an engine. The result will be returned through a callback.
    // Set the parameters for creating an engine.
    let extraParam: Record<string, Object> = {"locate": "CN", "recognizerMode": "short"};
    let initParamsInfo: speechRecognizer.CreateEngineParams = {
      language: 'zh-CN',
      online: 1,
      extraParams: extraParam
    };
    // Call the **createEngine** method.
    speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine: speechRecognizer.SpeechRecognitionEngine) => {
      if (!err) {
        console.info('Succeeded in creating engine.');
        // Receive the engine instance created.
        asrEngine = speechRecognitionEngine;
      } else {
        console.error(\`Failed to create engine. Code: ${err.code}, message: ${err.message}.\`);
      }
    });
    
3.  After obtaining the [SpeechRecognitionEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section153101728203110) instance, instantiate the [RecognitionListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section845815011389) object and call the [setListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section1745872517348) method to set a callback to receive callback information related to speech recognition.
    
    // Create a callback listener object.
    let setListener: speechRecognizer.RecognitionListener = {
      // Callback triggered when recognition successfully starts.
      onStart(sessionId: string, eventMessage: string) {
        console.info(\`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
      },
      // Callback triggered when an event occurs.
      onEvent(sessionId: string, eventCode: number, eventMessage: string) {
        console.info(\`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}\`);
      },
      // Callback triggered when the recognition result is generated, including the intermediate result and final result.
      onResult(sessionId: string, result: speechRecognizer.SpeechRecognitionResult) {
        console.info(\`onResult, sessionId: ${sessionId} result: ${JSON.stringify(result)}\`);
      },
      // Callback triggered when recognition is complete.
      onComplete(sessionId: string, eventMessage: string) {
        console.info(\`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
      },
      // Callback triggered when an error occurs. The error code is returned through this method.
      // Error code 1002200002 indicating recognition start failure is returned if the **startListening** method is repeatedly called.
      // For details about other error codes, please refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-corespeech).
      onError(sessionId: string, errorCode: number, errorMessage: string) {
        console.error(\`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
      },
    }
    // Set callbacks.
    asrEngine?.setListener(setListener);
    
4.  Set parameters for starting speech-to-text from audio files and microphone input. Then, call the [startListening](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section140216144119) method to start recognition.
    
    private startListeningForRecording() {
      let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 }// For details about how to set **audioInfo** parameters, please refer to [AudioInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section85771521101910).
      let extraParam: Record<string, Object> = {
        "recognitionMode": 0,
        "vadBegin": 2000,
        "vadEnd": 3000,
        "maxAudioDuration": 20000
      }
      let recognizerParams: speechRecognizer.StartParams = {
        sessionId: this.sessionId,
        audioInfo: audioParam,
        extraParams: extraParam
      }
      console.info('startListening start');
      asrEngine?.startListening(recognizerParams);
    }
    
5.  Pass the audio stream and call the [writeAudio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section72131731149) method to write the audio stream. Before your app reads an audio file, you need to prepare an audio file in PCM format.
    
    let uint8Array: Uint8Array = new Uint8Array();
    // Audio streams can be obtained in either of the following ways: 1. Obtain audio streams through recording. 2. Read audio streams from audio files.
    // The examples of both methods have been implemented. For details, please refer to the [demo](#section56481271497).
    // Write an audio stream. The audio stream length can only be 640 bytes or 1280 bytes.
    asrEngine?.writeAudio(sessionId, uint8Array);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/hW3FVd9hRfm1oopLL1YLNw/caution_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1BDD86ACCBF3B83AF90612CB0117341797CFFFF9D106E559318112CF9AB722F0)
    
    1\. To obtain audio streams through recording, enable the microphone permission. For details, please refer to [step 10](#li1723555443715).
    
    2\. To read audio streams from an audio file, store the PCM file in the **main\\resources\\resfile** directory of your project.
    
6.  (Optional) To query the languages supported by speech recognition, call the [listLanguages](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section813761871119) method.
    
    The **listLanguages** method can be called in two ways. The following uses one way as an example. For details about the other way, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer).
    
    // Set query parameters.
    let languageQuery: speechRecognizer.LanguageQuery = {
      sessionId: sessionId
    };
    // Call the **listLanguages** method.
    asrEngine?.listLanguages(languageQuery).then((res: Array<string>) => {
      console.info(\`Succeeded in listing languages.\`);
    }).catch((err: BusinessError) => {
      console.error(\`Failed to list languages. Code: ${err.code}, message: ${err.message}.\`);
    });
    
7.  (Optional) To end recognition, call the [finish](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section14433919171116) method.
    
    // End recognition.
    asrEngine?.finish(sessionId);
    
8.  (Optional) To cancel recognition, call the [cancel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section3235541759) method.
    
    // Cancel recognition.
    asrEngine?.cancel(sessionId);
    
9.  (Optional) Call the [shutdown](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section444415855615) method to release speech recognition engine resources.
    
    // Release engine resources.
    asrEngine?.shutdown();
    
10.  Add the **ohos.permission.MICROPHONE** permission to the [module.json5 configuration file](../../../getting-started/development-fundamentals/application-configuration-files-in-stage-model/module-json5-configuration-file/document.md) to ensure that the microphone can be used normally. For details, please refer to [Declaring Permissions](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md).
     
     // ...
     "requestPermissions": \[
       {
         "name" : "ohos.permission.MICROPHONE",
         "reason": "$string:reason",
         "usedScene": {
           "abilities": \[
             "EntryAbility"
           \],
           "when":"inuse"
         }
       }
     \],
     // ...
     

#### Development Example

Implement a button that converts a piece of audio into text.

## Index.ets

import { speechRecognizer } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { fileIo } from '@kit.CoreFileKit';
import { PromptAction } from '@kit.ArkUI';
import FileCapturer from './FileCapturer';

const TAG = 'AsrDemo';

let asrEngine: speechRecognizer.SpeechRecognitionEngine | undefined = undefined;

@Entry
@Component
struct Index {
  @State createCount: number = 0;
  @State result: boolean = false;
  @State voiceInfo: string = "";
  @State sessionId: string = "123456";
  @State sessionId2: string = "1234567";
  @State generatedText: string = "Default Text";
  @State uiContext: UIContext = this.getUIContext()
  @State promptAction: PromptAction = this.uiContext.getPromptAction();

  private mFileCapturer: FileCapturer = new FileCapturer();

  build() {
    Column() {
      Scroll() {
        Column() {
          Row() {
            Column() {
              Text(this.generatedText)
                .fontColor($r('sys.color.ohos\_id\_color\_text\_secondary'))
            }
            .width('100%')
            .constraintSize({ minHeight: 100 })
            .border({ width: 1, radius: 5 })
            .backgroundColor('#d3d3d3')
            .padding(20)
            .alignItems(HorizontalAlign.Start)
          }
          .width('100%')
          .padding({ left: 20, right: 20, top: 20, bottom: 20 })

          Button() {
            Text("CreateEngineByCallback")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            this.createByCallback();
            this.createCount++;
            console.info(TAG, \`CreateAsrEngine: createCount:${this.createCount}\`);

            this.sleep(500).then(() => {
              this.setListener();
              this.promptAction.showToast({
                message: 'CreateEngine succeeded!',
                duration: 2000
              });
            }).catch((err: BusinessError) => {
              console.error(TAG, \`Error in create engine: ${err}\`);
              this.promptAction.showToast({
                message: 'CreateEngine failed!',
                duration: 2000
              });
            });
          })

          Button() {
            Text("startRecording")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            this.startRecording();
            this.promptAction.showToast({
              message: 'start Recording',
              duration: 2000
            });
          })

          Button() {
            Text("audioToText")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            void this.audioToText();
            this.promptAction.showToast({
              message: 'start audioToText',
              duration: 2000
            });
          })

          Button() {
            Text("queryLanguagesCallback")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            try{
              this.queryLanguagesCallback();
              this.promptAction.showToast({
                message: 'queryLanguages succeeded!',
                duration: 2000
              });
            } catch (err) {
              this.generatedText = \`Failed to query language information. message: ${err.message}.\`
              this.promptAction.showToast({
                message: 'queryLanguages failed!',
                duration: 2000
              });
            }
          })

          Button() {
            Text("shutdown")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AA7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            // Release the engine.
            try{
              asrEngine?.shutdown();
              this.generatedText = \`The engine has been released.\`
              this.promptAction.showToast({
                message: 'shutdown succeeded!',
                duration: 2000
              });
            } catch (err) {
              this.generatedText = \`Failed to release engine. message: ${err.message}.\`
              this.promptAction.showToast({
                message: 'shutdown failed!',
                duration: 2000
              });
            }
          })
        }
        .layoutWeight(1)
      }
      .width('100%')
      .height('100%')

    }
  }

  // Create an engine. The result will be returned through a callback.
  private createByCallback() {
    // Set the parameters for creating an engine.
    let extraParam: Record<string, Object> = {"locate": "CN", "recognizerMode": "short"};
    let initParamsInfo: speechRecognizer.CreateEngineParams = {
      language: 'zh-CN',
      online: 1,
      extraParams: extraParam
    };

    // Call the **createEngine** method.
    speechRecognizer.createEngine(initParamsInfo, (err: BusinessError, speechRecognitionEngine:
      speechRecognizer.SpeechRecognitionEngine) => {
      if (!err) {
        console.info(TAG, 'succeeded in creating engine.');
        // Receive the engine instance created.
        asrEngine = speechRecognitionEngine;
      } else {
        // Error code 1002200001 indicating engine creation failure is returned if the language or mode is not supported, initialization times out, or the resources do not exist.
        // Error code 1002200006 indicating that the engine is busy is returned if multiple apps are calling the speech recognition engine simultaneously.
        // Error code 1002200008 is returned if the engine has been destroyed.
        console.error(TAG, \`Failed to create engine. Message: ${err.message}.\`);
      }
    });
  }

  // Query languages. The result will be returned through a callback.
  private queryLanguagesCallback() {
    // Set query parameters.
    let languageQuery: speechRecognizer.LanguageQuery = {
      sessionId: this.sessionId
    };
    // Call the **listLanguages** method.
    asrEngine?.listLanguages(languageQuery, (err: BusinessError, languages: Array<string>) => {
      if (!err) {
        // Receive information about the supported languages.
        console.info(TAG, \`succeeded in listing languages, result: ${JSON.stringify(languages)}\`);
        this.generatedText = \`languages result: ${JSON.stringify(languages)}\`
      } else {
        console.error(TAG, \`Failed to create engine. Message: ${err.message}.\`);
        this.generatedText = \`Failed to create engine. Message: ${err.message}.\`
      }
    });
  }

  private startListeningForRecording() {
    let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 } // For details about how to set **audioInfo** parameters, please refer to [AudioInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-speechrecognizer#section85771521101910).
    let extraParam: Record<string, Object> = {
      "recognitionMode": 0,
      "vadBegin": 2000,
      "vadEnd": 3000,
      "maxAudioDuration": 20000
    }
    let recognizerParams: speechRecognizer.StartParams = {
      sessionId: this.sessionId,
      audioInfo: audioParam,
      extraParams: extraParam
    }
    console.info(TAG, 'startListening start');
    try {
      asrEngine?.startListening(recognizerParams);
    } catch (err) {
      console.error(\`error code: ${err.code}, message: ${err.message}.\`)
    }
  }

  // Write an audio stream.
  private async audioToText() {
    try {
      this.setListener();
      // Set the parameters related to the start of recognition.
      let audioParam: speechRecognizer.AudioInfo = { audioType: 'pcm', sampleRate: 16000, soundChannel: 1, sampleBit: 16 }
      let recognizerParams: speechRecognizer.StartParams = {
        sessionId: this.sessionId2,
        audioInfo: audioParam
      }
      // Call the start recognition method.
      asrEngine?.startListening(recognizerParams);

      // Obtain the audio from a file.
      let data: ArrayBuffer | undefined = undefined;
      let ctx = this.getUIContext().getHostContext() as Context;
      let filenames: string\[\] = fileIo.listFileSync(ctx.resourceDir);
      if (filenames.length <= 0) {
        console.error('length is null');
        return;
      }
      let filePath: string = ctx.resourceDir + '/' + filenames\[0\];
      (this.mFileCapturer as FileCapturer).setFilePath(filePath);
      this.mFileCapturer.init((dataBuffer: ArrayBuffer) => {
        data = dataBuffer
        let uint8Array: Uint8Array = new Uint8Array(data);
        asrEngine?.writeAudio(this.sessionId2, uint8Array);
      });
      await this.mFileCapturer.start();
      asrEngine?.finish(this.sessionId);
      this.mFileCapturer.release();
    } catch (err) {
      this.generatedText = \`Message: ${err.message}.\`
    }
  }

  // Convert microphone input to text.
  private startRecording() {
    try {
      this.startListeningForRecording();
    } catch (err) {
      this.generatedText = \`Message: ${err.message}.\`;
    }
  }

  // Sleep.
  private async sleep(ms: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  // Set callbacks.
  private setListener() {
    // Create a callback listener object.
    let setListener: speechRecognizer.RecognitionListener = {
      // Callback triggered when recognition successfully starts.
      onStart: (sessionId: string, eventMessage: string) => {
        this.generatedText = '';
        console.info(TAG, \`onStart, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
      },
      // Callback triggered when an event occurs.
      onEvent(sessionId: string, eventCode: number, eventMessage: string) {
        console.info(TAG, \`onEvent, sessionId: ${sessionId} eventCode: ${eventCode} eventMessage: ${eventMessage}\`);
      },
      // Callback triggered when the recognition result is generated, including the intermediate result and final result.
      onResult: (sessionId: string, result: speechRecognizer.SpeechRecognitionResult) => {
        console.info(TAG, \`onResult, sessionId: ${sessionId} result: ${JSON.stringify(result)}\`);
        this.generatedText = result.result;
      },
      // Callback triggered when recognition is complete.
      onComplete(sessionId: string, eventMessage: string) {
        console.info(TAG, \`onComplete, sessionId: ${sessionId} eventMessage: ${eventMessage}\`);
      },
      // Callback triggered when an error occurs. The error code is returned through this method.
      // Error code 1002200002 indicating recognition start failure is returned if the **startListening** method is repeatedly called.
      // For details about other error codes, please refer to [ArkTS API Error Codes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/errorcode-corespeech).
      onError(sessionId: string, errorCode: number, errorMessage: string) {
        console.error(TAG, \`onError, sessionId: ${sessionId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
      },
    }
    // Set callbacks.
    asrEngine?.setListener(setListener);
  }
}

## FileCapturer.ets

Add the **FileCapturer.ets** file to capture PCM audio streams.

import { fileIo } from '@kit.CoreFileKit';

const TAG = 'FileCapturer';
const SEND\_SIZE: number = 1280;

/\*\*
 \* File collector tool.
 \*/
export default class FileCapturer {
  /\*\*
   \* Indicates whether the audio is being written.
   \*/
  private mIsWriting: boolean = false;

  /\*\*
   \* File path.
   \*/
  private mFilePath: string = '';

  /\*\*
   \* Open file object.
   \*/
  private mFile: fileIo.File | null = null;

  /\*\*
   \* Indicates whether the file can be read.
   \*/
  private mIsReadFile: boolean = true;

  /\*\*
   \* Audio data callback method.
   \*/
  private mDataCallBack: ((data: ArrayBuffer) => void ) | null = null;

  /\*\*
   \* Set the file path.
   \* @param filePath
   \*/
  public setFilePath(filePath: string) {
    this.mFilePath = filePath;
  }

  init(dataCallBack: (data: ArrayBuffer) => void) {
    if (null != this.mDataCallBack) {
      return;
    }
    this.mDataCallBack = dataCallBack;
    try {
      if (!fileIo.accessSync(this.mFilePath)) {
        return
      }
    } catch (err) {
      console.error(\`error code: ${err.code}, message: ${err.message}.\`)
    }
    console.error(TAG, "init start ");
  }

  async start(): Promise<void> {
    try {
      if (this.mIsWriting || null == this.mDataCallBack) {
        return;
      }
      this.mIsWriting = true;
      this.mIsReadFile = true;
      this.mFile = fileIo.openSync(this.mFilePath, fileIo.OpenMode.READ\_ONLY);
      let buf: ArrayBuffer = new ArrayBuffer(SEND\_SIZE);
      let offset: number = 0;
      while (SEND\_SIZE == fileIo.readSync(this.mFile.fd, buf, {
        offset: offset
      }) && this.mIsReadFile) {
        this.mDataCallBack(buf);
        await sleep(40);
        offset = offset + SEND\_SIZE;
      }
    } catch (e) {
      console.error(TAG, "read file error " + e);
    } finally {
      if (null != this.mFile) {
        try {
          fileIo.closeSync(this.mFile);
        } catch (err) {
          console.error(\`error code: ${err.code}, message: ${err.message}.\`)
        }
      }
      this.mIsWriting = false;
    }
  }

  stop() {
    if (null == this.mDataCallBack) {
      return;
    }
    try {
      this.mIsReadFile = false;
    } catch (e) {
      console.error(TAG, "read file error " + e);
    }
  }

  release() {
    if (null == this.mDataCallBack) {
      return;
    }
    try {
      this.mDataCallBack = null;
      this.mIsReadFile = false;
    } catch (e) {
      console.error(TAG, "read file error " + e);
    }
  }
}

async function sleep(ms: number): Promise<void> {
  return new Promise<void>(resolve => setTimeout(resolve, ms));
}

## EntryAbility.ets

Add the microphone permission to the **EntryAbility.ets** file.

import { abilityAccessCtrl, AbilityConstant, UIAbility, Want } from '@kit.AbilityKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { window } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

export default class EntryAbility extends UIAbility {
  onCreate(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onCreate');
  }

  onDestroy(): void {
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onDestroy');
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    // Main window is created, set main page for this ability
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');

    let atManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.context, \['ohos.permission.MICROPHONE'\]).then((data) => {
      hilog.info(0x0000, 'testTag', 'data:' + JSON.stringify(data));
      hilog.info(0x0000, 'testTag', 'data permissions:' + data.permissions);
      hilog.info(0x0000, 'testTag', 'data authResults:' + data.authResults);
    }).catch((err: BusinessError) => {
      hilog.error(0x0000, 'testTag', 'errCode: ' + err.code + 'errMessage: ' + err.message);
    });

    windowStage.loadContent('pages/Index', (err, data) => {
      if (err.code) {
        hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
        return;
      }
      hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
    });
  }

  onWindowStageDestroy(): void {
    // Main window is destroyed, release UI related resources
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageDestroy');
  }

  onForeground(): void {
    // Ability has brought to foreground
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onForeground');
  }

  onBackground(): void {
    // Ability has back to background
    hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onBackground');
  }
}
