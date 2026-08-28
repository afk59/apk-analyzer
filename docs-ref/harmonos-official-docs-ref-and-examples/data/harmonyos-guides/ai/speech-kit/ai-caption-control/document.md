# AI Caption Control

#### Application Scenario

The AI caption control offers a captioning service for users who are unfamiliar with the audio source language or when the audio is muted. It allows them to follow along with the content through captions.

This section describes how to use [AICaptionComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-aicaptioncomponent) and [AICaptionController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-aicaptioncomponent#section816451553012) to display AI captions, as shown in the following figure.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/8XeQHVvsRceP3rn3AirhIQ/en-us_image_0000002501590110.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=877650CC905144C4E6C5B24182BCD7DB711187BA323CE58F0BF96EE64A6E8119 "Click to enlarge")

#### API Description

The AI caption function is mainly provided by [AICaptionComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-aicaptioncomponent). For more information about the APIs, please refer to the [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-aicaptioncomponent).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[AICaptionComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-aicaptioncomponent)

 | 

AI caption component.

 |
| 

[AICaptionOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-aicaptioncomponent#section15787428226)

 | 

AI caption initialization parameters.

 |
| 

[AICaptionController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/speech-aicaptioncomponent#section816451553012)

 | 

Controller of the AI caption component. It is the main function entry class of the AI caption component and is used to operate AI captions. It writes audio data and obtains audio stream information.

 |

#### Development Procedure

1.  Add the class for the AI caption control and other related classes to the **/src/main/ets/pages/Index.ets** file in the project root directory.
    
    import { AICaptionComponent, AICaptionController, AICaptionOptions } from '@kit.SpeechKit';
    
2.  Configure the page layout, add the AI caption component, and set the input parameters of the AI caption component in **aboutToAppear**.
    
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
    const TAG = 'AI\_CAPTION\_DEMO'
    
    class Logger {
      static info(...msg: string\[\]) {
        hilog.info(0x0000, TAG, msg.join())
      }
    
      static error(...msg: string\[\]) {
        hilog.error(0x0000, TAG, msg.join())
      }
    }
    
    @Entry
    @Component
    struct Index {
      private captionOption ?: AICaptionOptions;
      private controller = new AICaptionController();
      @State isShown: boolean = false;
    
      aboutToAppear(): void {
        // AI caption initialization parameters, which are used to set the caption opacity and callback functions.
        this.captionOption = {
          initialOpacity: 1,
          onPrepared: () => {
            Logger.info('onPrepared')
          },
          onError: (error) => {
            Logger.error(\`onError, code: ${error.code}, msg: ${error.message}\`)
          }
        }
      }
    
      build() {
        Column({ space: 20 }) {
          // Call the **AICaptionComponent** component to initialize captions.
          AICaptionComponent({
            isShown: this.isShown,
            controller: this.controller,
            options: this.captionOption
          })
            .width('100%')
            .height(100)
          Divider()
          if (this.isShown) {
            Text('The upper part shows the captions.')
              .fontColor(Color.White)
          }
        }
        .width('100%')
        .height('100%')
        .padding(10)
        .backgroundColor('#7A7D6A')
      }
    }
    
3.  Add two buttons and the callback functions of their click events to the layout.
    
    -   The callback function of the first button controls the display status of the AI caption component.
    -   The callback function of the second button reads the audio file in the resource directory and passes the audio data to the AI caption component.
    
    import { AudioData } from '@kit.SpeechKit';
    
    @Entry
    @Component
    struct Index {
    
      isReading: boolean = false;
    
      async readPcmAudio() {
        this.isReading = true;
        let fileData: Uint8Array | undefined = undefined;
        try {
          fileData =
            await this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent($r('app.media.chineseAudio').id);
        } catch (e) {
          Logger.info(\`get fileData fail , msg ${e} \`)
        }
        if (fileData === undefined) {
          return;
        }
        const bufferSize = 640;
        const byteLength = fileData.byteLength;
        let offset = 0;
        Logger.info('byteLength', byteLength.toString())
        let startTime = new Date().getTime();
        while (offset < byteLength) {
          // Simulate the actual situation. Reading a file is faster than returning a stream by the recorder. Therefore, you need to wait for a period of time for synchronous transmission.
          let nextOffset = offset + bufferSize
          if (offset > byteLength) {
            this.isReading = false;
            return
          }
          const arrayBuffer = fileData.buffer.slice(offset, nextOffset);
          let data = new Uint8Array(arrayBuffer);
          Logger.info('data byteLength', data.byteLength.toString())
          const audioData: AudioData = {
            data: data
          }
          Logger.info(\`offset: ${offset} | byteLength: ${byteLength} | bufferSize: ${bufferSize}\`)
    
          if (this.controller) {
            Logger.info(\`writeAudio: ${audioData.data.byteLength}\`)
           try {
              this.controller.writeAudio(audioData)
            } catch (e) {
              Logger.error(\`writeAudio exception\`)
            }
          }
          offset = offset + bufferSize;
          const waitTime = bufferSize / 32
          await this.sleep(waitTime)
        }
        let endTime = new Date().getTime()
        this.isReading = false;
        Logger.info('playtime', JSON.stringify(endTime - startTime))
      }
    
      async sleep(time: number): Promise<void> {
        return new Promise(resolve => setTimeout(resolve, time))
      }
    
      build() {
        Column({ space: 20 }) {
         // ...
          Button('Switch caption display status:' + (this.isShown ? 'Displayed' : 'Hidden'))
            .backgroundColor('#B8BDA0')
            .width(200)
            .onClick(() => {
              this.isShown = !this.isShown;
            })
          Button('Read PCM audio')
            .backgroundColor('#B8BDA0')
            .width(200)
            .onClick(() => {
              if (!this.isReading) {
                void this.readPcmAudio()
              }
            })
         // ...
        }
      }
    }
    

#### Development Example

Index.ets

import { AICaptionComponent, AICaptionOptions, AICaptionController, AudioData } from '@kit.SpeechKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

const TAG = 'AI\_CAPTION\_DEMO'

class Logger {
  static info(...msg: string\[\]) {
    hilog.info(0x0000, TAG, msg.join())
  }

  static error(...msg: string\[\]) {
    hilog.error(0x0000, TAG, msg.join())
  }
}

@Entry
@Component
struct Index {
  private captionOption?: AICaptionOptions;
  private controller: AICaptionController = new AICaptionController();
  @State isShown: boolean = false;
  isReading: boolean = false;

  aboutToAppear(): void {
    // AI caption initialization parameters, which are used to set the caption opacity and callback functions.
    this.captionOption = {
      initialOpacity: 1,
      onPrepared: () => {
        Logger.info('onPrepared')
      },
      onError: (error: BusinessError) => {
        Logger.error(\`AICaption component error. Error code: ${error.code}, message: ${error.message}\`)
      }
    }
  }

  async readPcmAudio() {
    this.isReading = true;
    // The **chineseAudio.pcm** file is stored in **entry\\src\\main\\resources\\base\\media**.
    let fileData: Uint8Array | undefined = undefined;
    try {
      fileData =
        await this.getUIContext()?.getHostContext()?.resourceManager.getMediaContent($r('app.media.chineseAudio').id);
    } catch (e) {
      Logger.info(\`get fileData fail , msg ${e} \`)
    }
    if (fileData === undefined) {
      return;
    }
    const bufferSize = 640;
    const byteLength = fileData.byteLength;
    let offset = 0;
    Logger.info(\`Pcm data total bytes: ${byteLength.toString()}\`)
    let startTime = new Date().getTime();
    while (offset < byteLength) {
      // Simulate the actual situation. Reading a file is faster than returning a stream by the recorder. Therefore, you need to wait for a period of time for synchronous transmission.
      let nextOffset = offset + bufferSize
      if (offset > byteLength) {
        this.isReading = false;
        return
      }
      const arrayBuffer = fileData.buffer.slice(offset, nextOffset);
      let data = new Uint8Array(arrayBuffer);
      const audioData: AudioData = {
        data: data
      }

      if (this.controller) {
        try {
          this.controller.writeAudio(audioData)
        } catch (e) {
          Logger.error(\`writeAudio exception\`)
        }
      }
      offset = offset + bufferSize;
      const waitTime = bufferSize / 32
      await this.sleep(waitTime)
    }
    let endTime = new Date().getTime()
    this.isReading = false;
    Logger.info(\`Audio play time: ${JSON.stringify(endTime - startTime)}\`)
  }

  async sleep(time: number): Promise<void> {
    return new Promise(resolve => setTimeout(resolve, time))
  }

  build() {
    Column({ space: 20 }) {
      Button('Switch caption display status:' + (this.isShown ? 'Displayed' : 'Hidden'))
        .backgroundColor('#B8BDA0')
        .width(200)
        .onClick(() => {
          this.isShown = !this.isShown;
        })
      Button('Read PCM audio')
        .backgroundColor('#B8BDA0')
        .width(200)
        .onClick(() => {
          if (!this.isReading) {
            void this.readPcmAudio()
          }
        })
      Divider()
      // Call the **AICaptionComponent** component to initialize captions.
      AICaptionComponent({
        isShown: this.isShown,
        controller: this.controller,
        options: this.captionOption
      })
        .width('100%')
        .height(100)
      Divider()
      if (this.isShown) {
        Text('The upper part shows the captions.')
          .fontColor(Color.White)
      }
    }
    .width('100%')
    .height('100%')
    .padding(10)
    .backgroundColor('#7A7D6A')
  }
}
