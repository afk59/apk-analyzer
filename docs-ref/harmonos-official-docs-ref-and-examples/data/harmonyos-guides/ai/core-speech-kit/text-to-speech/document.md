# Text-to-Speech

Core Speech Kit can synthesize Chinese and English text (simplified Chinese, Traditional Chinese, digits, and English) with a maximum of 10,000 characters into speech and output the speech using a selected timbre.

You can set playback policies related to words, digits, mute pause, and Chinese character pronunciation.

#### Use Case

A system app with the TTS function integrated can offer voice narration capabilities for users with visual impairments or in scenarios where reading is not convenient, even when the device (mobile phone, tablet, and others) is disconnected from the Internet.

#### Restrictions

| 
AI Capability

 | 

Restrictions

 |
| :-- | :-- |
| 

Text-to-speech

 | 

-   Supported languages: Chinese and English (Simplified Chinese, Traditional Chinese, and English within a Chinese context)
-   Supported timbre types: Ling Xiaoshan female voice, Laura female voice for English (US), and Ling Feizhe male voice.
-   Text length: no more than 10,000 characters

 |

#### Development Procedure

1.  Add the TTS-related classes to the project.
    
    import { textToSpeech } from '@kit.CoreSpeechKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the **createEngine** API to create a [TextToSpeechEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech#section185526396124) instance.
    
    The **createEngine** API can be called in two ways. The following uses one way as an example. For details about the other way, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech).
    
    let ttsEngine: textToSpeech.TextToSpeechEngine;
    
    // Set the parameters for creating an engine.
    let extraParam: Record<string, Object> = {"style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName'};
    let initParamsInfo: textToSpeech.CreateEngineParams = {
      language: 'zh-CN',
      person: 0,
      online: 1,
      extraParams: extraParam
    };
    
    // Call the **createEngine** method.
    textToSpeech.createEngine(initParamsInfo, (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
      if (!err) {
        console.info('Succeeded in creating engine');
        // Receive the engine instance created.
        ttsEngine = textToSpeechEngine;
      } else {
        console.error(\`Failed to create engine. Code: ${err.code}, message: ${err.message}.\`);
      }
    });
    
3.  After obtaining the [TextToSpeechEngine](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech#section185526396124) instance, instantiate the [SpeakParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech#section7843122735210) and [SpeakListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech#section115395631614) objects, pass the original text **originalText** to be synthesized and played, and call [speak](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech#section140216144119) to play the speech.
    
    // Set the callbacks for the **speak** event.
    let speakListener: textToSpeech.SpeakListener = {
      // Callback triggered when playback starts.
      onStart(requestId: string, response: textToSpeech.StartResponse) {
        console.info(\`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
      },
      // Callback triggered when synthesis and playback are complete.
      onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
        console.info(\`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
      },
      // Callback triggered when playback stops.
      onStop(requestId: string, response: textToSpeech.StopResponse) {
        console.info(\`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
      },
      // Callback triggered when the audio stream is returned.
      onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
        console.info(\`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}\`);
      },
      // Callback triggered when an error occurs.
      onError(requestId: string, errorCode: number, errorMessage: string) {
        console.error(\`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
      }
    };
    // Set callbacks.
    ttsEngine.setListener(speakListener);
    let originalText: string = 'Hello HarmonyOS';
    // Set playback parameters.
    let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN',  
    "audioType": "pcm", "soundChannel": 3, "playType": 1 };
    let speakParams: textToSpeech.SpeakParams = {
      requestId: '123456', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
      extraParams: extraParam
    };
    // Call the playback method.
    // You can modify **speakParams** to [set playback policies](#section137481719163910).
    try {
      ttsEngine.speak(originalText, speakParams);
    } catch (err) {
      console.error(\`error code: ${err.code}, message: ${err.message}.\`)
    }
    
4.  (Optional) To stop synthesis and playback, call [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech#section14433919171116).
    
    ttsEngine.stop();
    
5.  (Optional) To check whether the TTS service is busy, call [isBusy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech#section35361720111113).
    
    ttsEngine.isBusy();
    
6.  (Optional) To query the supported languages and timbres, call [listVoices](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech#section813761871119).
    
    The **listVoices** API can be called in two ways. The following uses one way as an example. For details about the other way, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/hms-ai-texttospeech).
    
    // Declare and initialize the string **voiceInfo** in the component.
    @State voiceInfo: string = "";
    
    // Set query parameters.
    let voicesQuery: textToSpeech.VoiceQuery = {
      requestId: '12345678', // **requestId** can be used only once in the same instance. Do not set it repeatedly.
      online: 1
    };
    // Call **listVoices**. The result will be returned through a callback.
    ttsEngine.listVoices(voicesQuery, (err: BusinessError, voiceInfo: textToSpeech.VoiceInfo\[\]) => {
      if (!err) {
        // Receive information such as the supported languages and timbres.
        this.voiceInfo = JSON.stringify(voiceInfo);
        console.info(\`Succeeded in listing voices, voiceInfo is ${this.voiceInfo}\`);
      } else {
        console.error(\`Failed to list voices. Code: ${err.code}, message: ${err.message}\`);
      }
    });
    

#### Setting a Playback Policy

In different scenarios, playback policies automatically selected by the model may not meet the actual requirement. This section describes how to proactively set playback policies.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fd/v3/IuctYlJ4TJmorAdwzzZOSg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C90DB490B12CB408D4FD34067CEEBB76CCF27BF07E01C522F2A02A1B29682679)

Valid values are provided in the relevant sections below. If the input value is outside its range, the playback may not work as expected, and an incorrect playback result will be generated.

## Setting a Word Playback Mode

Text format: \[_hN_\] (N=**0/1/2**)

The values of _N_ are described as follows.

| 
Value

 | 

Description

 |
| :-- | :-- |
| 

0

 | 

Intelligently determines the word playback mode. This is the default value.

 |
| 

1

 | 

Plays the content in letter-by-letter mode.

 |
| 

2

 | 

Plays the content as a word.

 |

Text example:

"hello\[h1\] world"

The word "hello" is pronounced as a word, and the word "world" and subsequent words are pronounced letter by letter.

## Setting a Digit Playback Policy

Format: \[_nN_\] (N=**0/1/2**)

The values of _N_ are described as follows.

| 
Value

 | 

Description

 |
| :-- | :-- |
| 

0

 | 

Intelligently determines the digit playback policy. This is the default value.

 |
| 

1

 | 

Plays the content in digit-by-digit mode.

 |
| 

2

 | 

Plays the content as a number. Numbers exceeding 18 digits are not supported and will be read out digit by digit automatically.

 |

Text example:

"\[n2\]123\[n1\]456\[n0\]"

In the example, **123** is played as a number, **456** is played digit by digit, and how the digits in the following text are played is automatically determined.

## Inserting a Mute Pause

Format: \[_pN_\]

Description: _N_ is an unsigned integer in the unit of ms.

Text example:

"Hello\[p500\]Celia"

When this sentence is played, a 500 ms mute pause is inserted after "Hello".

## Specifying Pronunciation of Chinese Characters

The tone of a Chinese character is represented by a digit from **1** to **5**, indicating five tones: level tone, rising tone, falling-rising tone, falling tone, and light tone.

Format: \[=_MN_\]

Description: _M_ indicates pinyin, and _N_ indicates tone.

The values of _N_ are described as follows.

| 
Value

 | 

Description

 |
| :-- | :-- |
| 

1

 | 

Level tone.

 |
| 

2

 | 

Rising tone.

 |
| 

3

 | 

Falling-rising tone.

 |
| 

4

 | 

Falling tone.

 |
| 

5

 | 

Light tone

 |

Text example:

"Text to be played\[=**zhuo2**\]"

The text will be played in "zhuó" (rising tone).

#### Development Example

Implement a button that supports text-to-speech conversion and playback.

## Index.ets

import { textToSpeech } from '@kit.CoreSpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { PromptAction } from '@kit.ArkUI';
import { UIContext } from '@kit.ArkUI';
import { TreeMap } from '@kit.ArkTS';
import { fileIo as fs } from '@kit.CoreFileKit';
import PcmPlayer from './PcmPlayer';
import { audio } from '@kit.AudioKit';
import { Context } from '@kit.AbilityKit';

const TAG: string = 'TtsDemo';
let ttsEngine: textToSpeech.TextToSpeechEngine;
let bufferLength: number = 0;
let engineCreated: boolean = false;

// Define a function to concatenate ArrayBuffers.
function concatenateArrayBuffers(buffers: ArrayBuffer\[\]): ArrayBuffer {
  const totalLength = buffers.reduce((sum, buffer) => sum + buffer.byteLength, 0);
  const concatenatedBuffer = new ArrayBuffer(totalLength);
  let offset = 0;
  for (const buffer of buffers) {
    const uint8Array = new Uint8Array(buffer);
    new Uint8Array(concatenatedBuffer, offset, uint8Array.length).set(uint8Array);
    offset += uint8Array.length;
  }
  return concatenatedBuffer;
}

@Entry
@Component
struct Index {
  @State createCount: number = 0;
  @State originalText: string = "\\n\\t\\t _Text to be converted into speech_ \\n\\t\\t" + "_Text to be converted into speech_ \\n\\t\\t";
  @State uiContext: UIContext = this.getUIContext()
  @State promptAction: PromptAction = this.uiContext.getPromptAction();
  private pcmData: TreeMap<number, Uint8Array> = new TreeMap();
  private pcmPlayer: PcmPlayer = new PcmPlayer();

  build() {
    Column() {
      Scroll() {
        Column() {
          TextArea({ placeholder: 'Please enter tts original text', text: \`${this.originalText}\` })
            .margin(20)
            .focusable(false)
            .border({ width: 5, color: 0x317AE7, radius: 10, style: BorderStyle.Dotted })
            .onChange((value: string) => {
              this.originalText = value;
              console.info(TAG, "original text: " + this.originalText);
            })

          Button() {
            Text("CreateEngine")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            engineCreated = true
            this.createCount++;
            console.info(\`createByCallback: createCount:${this.createCount}\`);
            this.createByCallback();
            this.promptAction.showToast({
              message: 'CreateEngine success!',
              duration: 2000
            });
          })

          Button() {
            Text("speak")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            if (engineCreated) {
              try {
                this.speak();
                this.promptAction.showToast({
                  message: 'start speaking',
                  duration: 2000
                });
              } catch (err)  {
                  this.promptAction.showToast({
                    message: 'start speaking failed',
                    duration: 2000
                  });
                }
            } else {
              this.promptAction.showToast({
                message: 'The engine has not been created',
                duration: 2000
              });
            }
          })

          Button() {
            Text("speakOnData")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            if (engineCreated) {
              try {
                void this.speakOnData();
                this.promptAction.showToast({
                  message: 'start speakOnData',
                  duration: 2000
                });
              } catch (err) {
                this.promptAction.showToast({
                  message: 'start speakOnData failed',
                  duration: 2000
                });
              }
            } else {
              this.promptAction.showToast({
                message: 'The engine has not been created',
                duration: 2000
              });
            }
          })

          Button() {
            Text("stop")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            try {
              let isBusy: boolean = ttsEngine.isBusy();
              let isPlaying: boolean = this.pcmPlayer.isPlaying();
              if (isBusy) {
                ttsEngine.stop();
              }
              if (isPlaying) {
                this.pcmPlayer.stop()
              }
              this.promptAction.showToast({
                message: 'stop!',
                duration: 2000
              });
            } catch (err) {
              this.promptAction.showToast({
                message: 'stop failed',
                duration: 2000
              });
            }
          })

          Button() {
            Text("isBusy")
              .fontColor(Color.White)
              .fontSize(20)
          }
          .type(ButtonType.Capsule)
          .backgroundColor("#0x317AE7")
          .width("80%")
          .height(50)
          .margin(10)
          .onClick(() => {
            try {
              let isBusy: boolean = ttsEngine.isBusy();
              let isPlaying: boolean = this.pcmPlayer.isPlaying();
              console.info('isBusy :' + isBusy);
              console.info('isPlaying :' + isPlaying);
              this.promptAction.showToast({
                message: 'speak isBusy :' + isBusy + '\\nspeakOnData isBusy :' + isPlaying,
                duration: 2000
              });
            } catch (err) {
              this.promptAction.showToast({
                message: 'isBusy failed',
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
            try {
              this.pcmPlayer.release()
              ttsEngine.shutdown();
              engineCreated = false
              this.promptAction.showToast({
                message: 'shutdown success!',
                duration: 2000
              });
            } catch (err) {
              this.promptAction.showToast({
                message: 'shutdown failed',
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
  // Error code 1002300005 indicating engine creation failure is returned if the engine does not exist, engine resources do not exist, or the initialization times out.
  private createByCallback() {
    // Set the parameters for creating an engine.
    let extraParam: Record<string, Object> = { "style": 'interaction-broadcast', "locate": 'CN', "name": 'EngineName' }
    let initParamsInfo: textToSpeech.CreateEngineParams = {
      language: 'zh-CN',
      person: 0,
      online: 1,
      extraParams: extraParam
    };
    try {
      // Call the **createEngine** method.
      textToSpeech.createEngine(initParamsInfo, (err: BusinessError, textToSpeechEngine: textToSpeech.TextToSpeechEngine) => {
        if (!err) {
          console.info('createEngine is success');
          // Receive the engine instance created.
          ttsEngine = textToSpeechEngine;
        } else {
          console.error(\`error code: ${err.code}, message: ${err.message}.\`)
        }
      });
    } catch (error) {
      let message = (error as BusinessError).message;
      let code = (error as BusinessError).code;
      console.error(\`createEngine failed, error code: ${code}, message: ${message}.\`)
    }
  }

  // Call the **speak** method.
  private speak() {
    let speakListener: textToSpeech.SpeakListener = {
      // Callback triggered when playback starts.
      onStart(requestId: string, response: textToSpeech.StartResponse) {
        console.info(\`onStart, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
      },
      // Callback triggered when playback is complete.
      onComplete(requestId: string, response: textToSpeech.CompleteResponse) {
        console.info(\`onComplete, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
      },
      // Callback triggered when playback is stopped, that is, after **stop** is called and successfully executed.
      onStop(requestId: string, response: textToSpeech.StopResponse) {
        console.info(\`onStop, requestId: ${requestId} response: ${JSON.stringify(response)}\`);
      },
      // Callback triggered when the audio stream is returned.
      onData(requestId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) {
        console.info(\`onData, requestId: ${requestId} sequence: ${JSON.stringify(response)} audio: ${JSON.stringify(audio)}\`);
      },
      // Callback triggered when an error occurs during the playback.
      onError(requestId: string, errorCode: number, errorMessage: string) {
        if (errorCode === 1002300007) {
          engineCreated = false
        }
        console.error(\`onError, requestId: ${requestId} errorCode: ${errorCode} errorMessage: ${errorMessage}\`);
      }
    };
    // Set callbacks.
    ttsEngine.setListener(speakListener);
    // Set playback parameters.
    let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm", "soundChannel": 3, "playType":1}
    let speakParams: textToSpeech.SpeakParams = {
      requestId: '123456' + Date.now(), // **requestId** can be used only once in the same instance. Do not set it repeatedly.
      extraParams: extraParam
    };
    // Call the **speak** method.
    try {
      ttsEngine.speak(this.originalText, speakParams);
    } catch (err) {
      console.error(TAG, \`error code: ${err.code}, message: ${err.message}.\`)
    }
  }

  private onStart = (utteranceId: string, response: textToSpeech.StartResponse) => {
    bufferLength = 0;
    // Initialize audio data mapping.
    console.info(TAG, \`onStart | utteranceId: ${ utteranceId }, response: ${JSON.stringify(response)}\`);
  }

  private onData = (utteranceId: string, audio: ArrayBuffer, response: textToSpeech.SynthesisResponse) => {
    // Convert ArrayBuffer to Uint8Array.
    let uint8Array: Uint8Array = new Uint8Array(audio);
    this.pcmData.set(response.sequence, uint8Array)
    bufferLength += 1
    let str = ""
    // Alternatively, print each element using a loop.
    for (let i = 0; i < uint8Array.length; i++) {
      str = str + (","+uint8Array\[i\]);
    }
    console.info(TAG, \`onData | utteranceId: ${utteranceId}, sequence: ${JSON.stringify(response.sequence)}, length: ${uint8Array.length}, audio: ${JSON.stringify(str)}\`);
  }

  private onComplete = (utteranceId: string, response: textToSpeech.CompleteResponse) => {
    let buffers: ArrayBuffer\[\] = new Array();

    console.info(TAG, \`pcmData len: ${this.pcmData.length}\`)
    // Traverse the map and add each ArrayBuffer to the array.
    this.pcmData.forEach((value: Uint8Array) => {
      buffers.push(value.buffer.slice(0))
    })
    console.info(TAG, \`buffers len: ${buffers.length}\`)

    // Concatenate all ArrayBuffers in sequence.
    let audioData = concatenateArrayBuffers(buffers);
    console.info(TAG, \`audioData len: ${audioData.byteLength}\`)

    let context = this.uiContext.getHostContext() as Context
    let path = context.filesDir
    let filePath: string = \`${path}/my.pcm\`
    fs.createStream(filePath, "w+")
      .then(os => os.write(audioData))
      .then((): Promise<void> => {
        this.pcmPlayer.file = fs.openSync(filePath, fs.OpenMode.READ\_ONLY);
        return this.pcmPlayer.prepare(audio.AudioSamplingRate.SAMPLE\_RATE\_16000);
      })
      .then(() => this.pcmPlayer.play(audioData))
      .catch((err: BusinessError) => console.error(TAG, \`Error: ${err}\`));

    console.info(TAG, \`onComplete | utteranceId: ${utteranceId}, response: ${JSON.stringify(response)}\`);
  }

  // Call the **speakOnData** method.
  // Error code 1002300007 indicating synthesis and playback failure is returned if the **speak** method is called before engine initialization.
  private speakOnData() {
    // Set playback parameters.
    let extraParam: Record<string, Object> = {"queueMode": 0, "speed": 1.2, "volume": 2, "pitch": 1, "languageContext": 'zh-CN', "audioType": "pcm", "soundChannel": 1, "playType":0}
    let speakParams: textToSpeech.SpeakParams = {
      requestId: '1234567' + Date.now(),
      extraParams: extraParam
    }

    try{
      // Create a callback listener object.
      let speakListener: textToSpeech.SpeakListener = {
        // Callback triggered when recognition successfully starts.
        onStart: this.onStart,
        // Callback triggered when recognition is complete.
        onComplete: this.onComplete,
        // Callback triggered when playback stops.
        onStop(utteranceId: string, response: textToSpeech.StopResponse) {
          console.info('speakListener onStop: ' + ' utteranceId: ' + utteranceId + ' response: ' + JSON.stringify(response));
        },
        // Callback triggered when the audio stream is returned.
        onData: this.onData,
        // Callback triggered when an error occurs.
        onError(utteranceId: string, errorCode: number, errorMessage: string) {
          if (errorCode === 1002300007) {
            engineCreated = false
          }
          console.error('speakListener onError: ' + ' utteranceId: ' + utteranceId + ' errorCode: ' + errorCode + ' errorMessage: ' + errorMessage);
        }
      };
    // Set callbacks.
      ttsEngine.setListener(speakListener);
      try{
        console.info(\`speakListener before speak\`)
        // Call the **speak** method.
        for (let i = 0; i < 1; i++) {
          ttsEngine?.speak(this.originalText, speakParams);
        }
        console.info(\`speakListener after speak\`)
      }catch (error) {
        let message = (error as BusinessError).message;
        let code = (error as BusinessError).code;
        console.error(\`speakListener speak failed, error code: ${code}, message: ${message}.\`)
      }
    }catch (error) {
      let message = (error as BusinessError).message;
      let code = (error as BusinessError).code;
      console.error(\`speakListener setListener failed, error code: ${code}, message: ${message}.\`)
    }
  }
}

## PcmPlayer.ets

import { audio } from '@kit.AudioKit';
import { fileIo as fs } from '@kit.CoreFileKit';

const TAG = 'PCM\_audio';

class Options {
  offset?: number;
  length?: number;
}

export default class PcmPlayer {

  public file: fs.File | undefined;
  private writeDataCallback = (buffer: ArrayBuffer) => {
    let options: Options = {
      offset: this.bufferSize,
      length: buffer.byteLength
    };

    try {
      fs.readSync(this.file?.fd, buffer, options);
      this.bufferSize += buffer.byteLength;
      if (this.audioDataSize < this.bufferSize) {
        this.renderModel?.off('writeData');
        void this.stop()
      }
      console.info(TAG, 'reading file success');
      // The system determines that the buffer is valid and plays the data normally.
      return audio.AudioDataCallbackResult.VALID;
    } catch (error) {
      console.error(TAG, \`Reading file failed, error code: ${error.code}, message: ${error.message}.\`)
      // The system determines that the buffer is invalid and does not play the data.
      return audio.AudioDataCallbackResult.INVALID;
    }
  };
  /\*\*
   \* Buffer size.
   \*/
  private bufferSize: number = 0;
  /\*\*
   \* Total audio data size.
   \*/
  private audioDataSize: number = 0;
  /\*\*
   \* Player.
   \*/
  private renderModel: audio.AudioRenderer | null = null;
  /\*\*
   \* Playback state.
   \*/
  private audioStreamInfo: audio.AudioStreamInfo = {
    samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_16000, // Sampling rate.
    channels: audio.AudioChannel.CHANNEL\_1, // Channel.
    sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sample format.
    encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
  }
  private audioRendererInfo: audio.AudioRendererInfo = {
    usage: audio.StreamUsage.STREAM\_USAGE\_ACCESSIBILITY, // Audio stream usage type.
    rendererFlags: 0 // Audio renderer flag.
  }
  private audioRendererOptions: audio.AudioRendererOptions = {
    streamInfo: this.audioStreamInfo,
    rendererInfo: this.audioRendererInfo
  }

  public async prepare(sampleRate: number) {
    this.audioRendererOptions.streamInfo.samplingRate = sampleRate;
    this.audioRendererOptions.rendererInfo.usage = audio.StreamUsage.STREAM\_USAGE\_MUSIC;
    if (this.renderModel != null) {
      await this.renderModel.release();
    }
    let renderModel = await audio.createAudioRenderer(this.audioRendererOptions);
    if (!renderModel) {
      console.error(TAG, \`failed to create audio renderer\`);
    }
    console.info(TAG, "creating AudioRenderer success");
    this.renderModel = renderModel;
    this.bufferSize = await this.renderModel.getBufferSize();
  }

  public async play(data: ArrayBuffer): Promise<number> {
    this.audioDataSize = data.byteLength
    if (this.renderModel != null) {
      try {
        this.renderModel.on('writeData', this.writeDataCallback);
      } catch (err) {
        console.error(\`error code: ${err.code}, message: ${err.message}.\`)
      }
      // Start rendering.
      await this.renderModel.start();
      console.info(TAG, "start AudioRenderer success");
    }
    return -1;
  }

  public async stop() {
    console.info(TAG, 'Renderer begin stop');
    if (this.renderModel == null) {
      return;
    }

    // Rendering can be stopped only when the renderer is in running or paused state.
    if (this.renderModel.state !== audio.AudioState.STATE\_RUNNING
      && this.renderModel.state !== audio.AudioState.STATE\_PAUSED) {
      console.error(TAG, 'Renderer is not running or paused');
      return;
    }
    await this.renderModel.stop(); // Stop rendering.
    console.info(TAG, 'Renderer stopped');
  }

  public async release() {
    // Resources can be released only when the renderer is not in released state.
    if (this.renderModel != null) {
      if (this.renderModel.state === audio.AudioState.STATE\_RELEASED) {
        console.error(TAG, 'Renderer already released');
        return;
      }
      await this.renderModel.release(); // Release resources.
      this.renderModel = null;
      console.info(TAG, 'Renderer released');
    }
  }

  /\*\*
   \* Check the current rendering status.
   \*
   \* @returns **true** if the rendering is running; **false** otherwise.
   \*/
  public isPlaying() {
    if (this.renderModel != null) {
      console.info(TAG, "player.state:" + this.renderModel.state);
      return this.renderModel.state == audio.AudioState.STATE\_RUNNING;
    } else {
      return false;
    }
  }

  /\*\*
   \* Obtain the current rendering status.
   \*
   \* @returns **true** if the rendering is running; **false** otherwise.
   \*/
  public getRenderState(): number {
    if (this.renderModel != null) {
      console.info(TAG, "player.state:" + this.renderModel.state);
      return this.renderModel.state;
    } else {
      return audio.AudioState.STATE\_INVALID;
    }
  }

  /\*\*
   \* Obtain the minimum buffer size required by the audio renderer.
   \*/
  public getBufferSize(): number {
    return this.bufferSize;
  }
}
