# Using AVTranscoder to Transcode Videos (ArkTS)

You can use the [AVTranscoder](../../../about-this-kit/document.md#avtranscoder) to implement video transcoding. . Since API version 20, C/C++ APIs are provided for video transcoding, and transcoding is provided as a basic capability on mobile phones, tablets, and 2-in-1 devices You can check whether the current device supports the AVTranscoder by calling [canIUse](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-syscap#caniuse). If the return value of **canIUse("SystemCapability.Multimedia.Media.AVTranscoder")** is **true**, the transcoding capability can be used.

This topic describes how to use the AVTranscoder to implement video transcoding, covering the process of starting, pausing, resuming, and exiting transcoding.

#### How to Develop

Read [AVTranscoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avtranscoder) for the API reference.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/ic4hh_eMRiCIVx6g_RMFZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5E0A909E4013356F0AD8A19830200B55A07EF473D5E2B09CCF44AC55F85E7A99)

To forward, upload, or save the transcoded file, the application must call the system API **await avTranscoder.release()** after receiving the complete event. This ensures the integrity of the video file.

1.  Create an [AVTranscoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-f#mediacreateavtranscoder12) instance.
    
    import { media } from '@kit.MediaKit';
    
    private avTranscoder: media.AVTranscoder | undefined = undefined;
    // Create an AVTranscoder instance.
    this.avTranscoder = await media.createAVTranscoder();
    
2.  Set the events to listen for.
    
    | Event Type | Description |
    | :-- | :-- |
    | complete | Mandatory; used to listen for the completion of transcoding. |
    | error | Mandatory; used to listen for errors that occur during transcoding. |
    | progressUpdate | Used to listen for the transcoding progress. |
    
    import { BusinessError } from '@kit.BasicServicesKit';
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { media } from '@kit.MediaKit';
    private currentProgress: number = 0;
    private avTranscoder: media.AVTranscoder | undefined = undefined;
    
    async test() {
      // Create an AVTranscoder instance.
      this.avTranscoder = await media.createAVTranscoder();
      if (this.avTranscoder != undefined) {
        // Callback function for the completion of transcoding.
        this.avTranscoder.on('complete', async () => {
          console.info(\`AVTranscoder is completed\`);
          await this.releaseTranscoderingProcess();
        });
        // Callback function for errors.
        this.avTranscoder.on('error', (err: BusinessError) => {
          console.error(\`AVTranscoder failed, code is ${err.code}, message is ${err.message}\`);
        });
        // Callback function for progress updates.
        this.avTranscoder.on('progressUpdate', (progress: number) => {
          console.info(\`AVTranscoder progressUpdate = ${progress}\`);
          this.currentProgress = progress;
        })
      }
    }
    
    // Obtain the current progress.
    getCurrentProgress(): number {
      console.info(\`getCurrentProgress = ${this.currentProgress}\`);
      return this.currentProgress;
    }
    // Release the transcoding process.
    async releaseTranscoderingProcess() {
      if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
        if (this.avTranscoder != undefined) {
          // 1. Release the AVTranscoder instance.
          await this.avTranscoder.release();
          this.avTranscoder = undefined;
          // 2. Close the FD of the output file.
          fs.closeSync(this.avTranscoder!.fdDst);
        }
      }
    }
    
3.  Set the FD of the source video file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/30/v3/DTTe0EgoTvOwzydcXIAV-Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FEB0A9BAA87E9B0E4621B74F8F97774230D2105E2257E8FA542CED475E0E90E)
    
    The **fdSrc** value in the code snippet below is for reference only. You need to check the media asset validity and set **fdSrc** based on service requirements.
    
    -   If local files are used for transcoding, ensure that the files are available and the application sandbox path is used for access. For details about how to obtain the application sandbox path, see [Obtaining Application File Paths](../../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/context-stage-model/document.md#obtaining-application-file-paths). For details about the application sandbox and how to push files to the application sandbox directory, see [File Management](../../../../../application-framework/core-file-kit/application-files/application-sandbox/document.md).
        
    -   To obtain the application file path, you should use the Context property. You are advised to use **getUIContext** to obtain a UIContext instance and use **getHostContext** to call **getContext** of the bound instance. For details, see [Obtaining Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#gethostcontext12).
        
    -   You can also use **ResourceManager.getRawFd()** to obtain the FD of a file packed in the HAP file. For details, see [ResourceManager API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-resource-manager#getrawfd9).
        
    
    // Import the ets/transcoder/AVTranscoderManager.ets file.
    import {AVTranscoderDemo} from '../transcoder/AVTranscoderManager'
    
    @Entry
    @Component
    struct Index {
      // Obtain the context of the ability to which the current component belongs and obtain the application file path through the context.
      private context:Context | undefined = this.getUIContext()?.getHostContext();
      // Obtain the AVTranscoder instance.
      @State avTranscoder: AVTranscoderDemo | undefined = this.context ? new AVTranscoderDemo(this.context) : undefined;
    
      build() {
        RelativeContainer() {
          Column() {
            Button($r('app.string.StartTranscoder')) // Value of name:StartTranscoder in the resources/base/element/string.json file.
              .onClick(async () => {
                console.info(\`Button put\`);
                await this.avTranscoder?.avTranscoderDemo();
              })
              .id('AVTranscoderButton')
              // Obtain the transcoding progress.
              Progress({ value: 0, total: 100, type: ProgressType.Linear }).value(this.avTranscoder?.getCurrentProgress())
                .height(50)
                .width('80%')
          }
          .alignRules({
            center: { anchor: '\_\_container\_\_', align: VerticalAlign.Center },
            middle: { anchor: '\_\_container\_\_', align: HorizontalAlign.Center }
          })
        }
        .height('100%')
        .width('100%')
      }
    }
    
    import { media } from '@kit.MediaKit';
    private avTranscoder: media.AVTranscoder | undefined = undefined;
    private context: Context | undefined;
    constructor(context: Context | undefined) {
      if (context != undefined) {
        this.context = context; // this.getUIContext().getHostContext();
      }
    }
    
    async test() {
      // Create an AVTranscoder instance.
      this.avTranscoder = await media.createAVTranscoder();
      // Obtain the file descriptor of the input file. H264\_AAC.mp4 is a preset resource in the rawfile directory. Replace it with the actual one.
      if (this.context != undefined) {
        let fileDescriptor = await this.context.resourceManager.getRawFd('H264\_AAC.mp4');
        // Set fdSrc used for transcoding.
        this.avTranscoder.fdSrc = fileDescriptor;
      }
    }
    
4.  Set the FD of the target video file.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/0WyC6QlwS0mwP4SkPpoZUA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EEC7F7C88F84B5685503D8003B0C8F6390A1F259927B924C1E5F570335A6D1B1)
    
    **fdDst** specifies the FD of the output file after transcoding. The value is a number. You must call [ohos.file.fs of Core File Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-file-fs) to implement access to the application file. For details, see [Accessing Application Files](../../../../../application-framework/core-file-kit/application-files/application-file-access-and-management/accessing-application-files-arkts/document.md).
    
    import { fileIo as fs } from '@kit.CoreFileKit';
    import { media } from '@kit.MediaKit';
    private avTranscoder: media.AVTranscoder | undefined = undefined;
    private context: Context | undefined;
    constructor(context: Context | undefined) {
      if (context != undefined) {
        this.context = context; // this.getUIContext().getHostContext();
      }
    }
    
    async test() {
      // Create an AVTranscoder instance.
      this.avTranscoder = await media.createAVTranscoder();
      if (this.context != undefined) {
        // Set the sandbox path of the output target file.
        let outputFilePath = this.context.filesDir + "/output.mp4";
        // Create and open a file if the file does not exist. Open it if the file exists.
        let file = fs.openSync(outputFilePath, fs.OpenMode.READ\_WRITE | fs.OpenMode.CREATE);
        // Set fdDst of the output file.
        this.avTranscoder.fdDst = file.fd; // Obtain the file descriptor of the created video file by referring to the sample code in Accessing Application Files.
      }
    }
    
5.  Set video transcoding parameters and call **prepare()**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fa/v3/suR6pbXgSvqFQ6l5ZhB3sA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9ACE1A32E0EB0C6308B969E02B746B47F5CAC7CD67775808D471AE986EA35C74)
    
    Only transcoding-related parameters are set in the input parameter **avConfig** of the **prepare()** API.
    
    Only the supported [transcoding formats](../../../about-this-kit/document.md#avtranscoder) can be used due to the limited demultiplexing, multiplexing, encoding, and decoding capabilities.
    
    import { media } from '@kit.MediaKit';
    private avTranscoder: media.AVTranscoder | undefined = undefined;
    private avConfig: media.AVTranscoderConfig = {
      audioBitrate: 100000, // Audio bit rate.
      audioCodec: media.CodecMimeType.AUDIO\_AAC, // Audio encoding format.
      fileFormat: media.ContainerFormatType.CFT\_MPEG\_4, // Container format.
      videoBitrate: 2000000, // Video bit rate.
      videoCodec: media.CodecMimeType.VIDEO\_AVC, // Video encoding format.
    };
    
    async test() {
      // Create an AVTranscoder instance.
      this.avTranscoder = await media.createAVTranscoder();
      // Set transcoding parameters to complete the preparations.
      await this.avTranscoder.prepare(this.avConfig);
    }
    
    You can set the resolution of the target video in avConfig.
    
    let avConfig: media.AVTranscoderConfig = {
      audioBitrate: 100000, // Audio bit rate.
      audioCodec: media.CodecMimeType.AUDIO\_AAC, // Audio encoding format.
      fileFormat: media.ContainerFormatType.CFT\_MPEG\_4, // Container format.
      videoBitrate: 2000000, // Video bit rate.
      videoCodec: media.CodecMimeType.VIDEO\_AVC, // Video encoding format.
      videoFrameWidth: 640, // Video frame width: 640.
      videoFrameHeight: 480, // Video frame height: 480.
    };
    
6.  Call **start()** to start transcoding.
    
    async startTranscoderingProcess() {
      if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
        if (this.avTranscoder != undefined) {
          await this.avTranscoder.release();
          this.avTranscoder = undefined;
        }
       // Create an AVTranscoder instance, set the callback, set the file descriptor, and complete the preparation before starting transcoding.
       // For details about the creation procedure, see steps 1 to 5 above.
    
       // Start transcoding.
       await this.avTranscoder.start();
     }
    }
    
7.  Call **pause()** to pause transcoding.
    
    // Process of pausing transcoding.
    async pauseTranscoderingProcess() {
      if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
        if (this.avTranscoder != undefined) { // It is reasonable to call pause only after start is called and returns a value.
          await this.avTranscoder.pause();
        }
      }
    }
    
8.  Call **resume()** to resume transcoding.
    
    // Resume transcoding.
    async resumeTranscoderingProcess() {
      if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
        if (this.avTranscoder != undefined) { // It is reasonable to call resume only after pause is called and returns a value.
          await this.avTranscoder.resume();
        }
      }
    }
    
9.  Call **release()** to destroy the instance and exit transcoding.
    
    // Destroy the instance.
    async releaseTranscoderingProcess() {
      if (canIUse('SystemCapability.Multimedia.Media.AVTranscoder')) {
        if (this.avTranscoder != undefined) {
          // 1. Destroy the instance.
          await this.avTranscoder.release();
          this.avTranscoder = undefined;
          // 2. Close the FD of the output file.
          fs.closeSync(this.avTranscoder!.fdDst);
        }
      }
    }
    
10.  A complete example of starting, pausing, resuming, and exiting transcoding.
     

async avTranscoderDemo() {
  await this.startTranscoderingProcess(); // Start transcoding.
  await this.pauseTranscoderingProcess(); // Pause transcoding.
  await this.resumeTranscoderingProcess(); // Resume transcoding.
}

#### Running the Sample Project

Refer to the sample code below to implement transcoding, covering the process of starting, pausing, resuming, and exiting transcoding.

1.  Create a project, download the [sample project](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVTranscoder/AVTranscoderArkTS), and copy its resources to the corresponding directories.
    
    AVTranscoderArkTS
    entry/src/main/ets/
    └── pages
    │    └── Index.ets (Transcoding UI)
    │
    └── transcoder
        └── AVTranscoderManager.ets (Transcoding function)
    
    entry/src/main/resources/
    ├── base
    │   ├── element
    │   │   ├── color.json
    │   │   ├── float.json
    │   │   └── string.json
    │   └── media
    │
    └── rawfile
        └── H264\_AAC.mp4 (Video resource)
    
2.  Compile and run the project.
