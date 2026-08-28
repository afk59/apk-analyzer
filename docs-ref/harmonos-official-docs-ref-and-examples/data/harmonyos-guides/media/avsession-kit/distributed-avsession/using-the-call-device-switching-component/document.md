# Using the Call Device Switching Component

#### Switching Call Output Devices

This document describes how to integrate the **AVCastPicker** component to implement call device switching. For related parameters, please refer to [@ohos.multimedia.avCastPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-avcastpicker) and [@ohos.multimedia.avCastPickerParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-avcastpickerparam). To implement audio output device routing switching, please refer to [Switching Audio Output Devices](../../../audio-kit/audio-device-routing-management/switching-audio-output-devices/document.md).

Currently, the system provides the default style and custom style for the **AVCastPicker** component.

-   If the application chooses to display the default style, when the device switches, the system displays the default component style based on the currently selected device.
-   If the application opts for a custom style, it needs to refresh its defined style in response to device changes.

## Implementing the Default Style

1.  Create an AVSession of the voice\_call type. The AVSession constructor provides **AVSessionType** to specify the session type, and **voice\_call** indicates the call type. If no AVSession is created, an empty list is displayed.
    
    import { AVCastPicker, AVCastPickerState, AVInputCastPicker, avSession } from '@kit.AVSessionKit';
    
    @Entry
    @Component
    struct Index {
      @State message: string = 'Simulated call'
      @State session: avSession.AVSession | undefined = undefined;
      @State context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
      // ...
    
      async init() {
        try {
          let context = this.getUIContext().getHostContext() as Context;
          // Create an AVSession of the voice\_call type.
          this.session = await avSession.createAVSession(context, 'voiptest', 'voice\_call');
        } catch (err) {
          console.error(\`AVSession create :  Error: Code: ${err.code}, message: ${err.message}\`);
        }
        // ...
      }
      // ...
    }
    
2.  Create the **AVCastPicker** component on the call page that provides device switching.
    
    import { AVCastPicker } from '@kit.AVSessionKit';
    
    @Entry
    @Component
    struct OutputCastPicker {
      @State normalColor:Color = Color.White;
      @State activeColor:Color = Color.Blue;
      @State pickerImage: ResourceStr = $r('app.media.sound'); // Custom resources.
      // ...
      // Create the component and set its size.
      build() {
        Row() {
          Column() {
            AVCastPicker({
              normalColor: this.normalColor,
              activeColor: this.activeColor,
              customPicker: this.ImageBuilder.bind(this), // Add a custom parameter.
            })
              .size({ width: '50%', height: '20%' })
              .id('AVCastPicker')
            // ...
          }
          .width('100%')
          .alignItems(HorizontalAlign.Center)
        }
        .alignItems(VerticalAlign.Center)
        .width('100%')
        .height('100%')
      }
    
      // Custom content.
      @Builder
      ImageBuilder() {
        Text($r('app.string.switch\_OutputDevice'))
        Image(this.pickerImage)
          .size({ width: '100%', height: '100%' })
          .backgroundColor('#00000000')
          .fillColor(Color.Black)
      }
    }
    
    Alternatively, create the **AVCastPickerHelper** component.
    
    import { common } from '@kit.AbilityKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { avSession } from '@kit.AVSessionKit';
    
    class MyPage {
      private avCastPicker: avSession.AVCastPickerHelper;
    
      constructor(context: common.UIAbilityContext) {
        this.avCastPicker = new avSession.AVCastPickerHelper(context);
      }
    
      async selectCastDevice() {
        const avCastPickerOptions: avSession.AVCastPickerOptions = {
          sessionType: 'video',
        };
    
        this.avCastPicker.select(avCastPickerOptions).then(() => {
          console.info('select successfully');
        }).catch((err: BusinessError) => {
          console.error('AVCastPicker.select failed with err: ${err.code}, ${err.message}');
        });
      }
    }
    
3.  Create an AudioRenderer of the VOICE\_COMMUNICATION type and start playing. For details about the implementation, see [Developing Audio Call](../../../audio-kit/audio-call/developing-audio-call/document.md).
    
    import { audio } from '@kit.AudioKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { common } from '@kit.AbilityKit';
    import { resourceManager } from '@kit.LocalizationKit';
    import { fileIo } from '@kit.CoreFileKit';
    
    class Options {
      public offset: number = 0;
      public length: number = 0;
    }
    export default class AudioRenderer {
      private audioRenderer: audio.AudioRenderer | undefined = undefined;
      private audioStreamInfo: audio.AudioStreamInfo = {
        // Set the parameters based on project requirements. The following parameters are for reference only.
        samplingRate: audio.AudioSamplingRate.SAMPLE\_RATE\_48000, // Sampling rate.
        channels: audio.AudioChannel.CHANNEL\_2, // Channel.
        sampleFormat: audio.AudioSampleFormat.SAMPLE\_FORMAT\_S16LE, // Sampling format.
        encodingType: audio.AudioEncodingType.ENCODING\_TYPE\_RAW // Encoding format.
      }
      public appContext?: common.UIAbilityContext | undefined = undefined;
      private audioSource = 'test1.wav';
      private fileDescriptor?: resourceManager.RawFileDescriptor | undefined = undefined;
      // ...
      async getStageFileDescriptor(fileName: string): Promise<resourceManager.RawFileDescriptor | undefined> {
        let fileDescriptor: resourceManager.RawFileDescriptor | undefined = undefined;
        if (this.appContext) {
          let mgr = this.appContext.resourceManager;
          this.fileDescriptor = mgr.getRawFdSync(fileName);
          await mgr.getRawFd(fileName).then(value => {
            fileDescriptor = value;
            console.info('case getRawFileDescriptor success fileName: ' + fileName);
          }).catch((error: BusinessError) => {
            console.error('case getRawFileDescriptor err: ' + error);
          });
        }
        return fileDescriptor;
      }
    
      async startRenderer(): Promise<void> {
        if (this.audioRenderer !== undefined) {
          return;
        }
        this.getStageFileDescriptor(this.audioSource).then((res) => {
          this.fileDescriptor = res;
        });
        if (!this.fileDescriptor) {
          return;
        }
        let file: resourceManager.RawFileDescriptor = this.fileDescriptor;
        try {
          this.audioRenderer = await audio.createAudioRenderer(this.audioRendererOption);
        } catch (error) {
          console.error(\`audioRenderer create : Error: ${JSON.stringify(error)}\`);
          return;
        }
        let bufferSize: number = this.fileDescriptor.offset;
        let writeDataCallback = (buffer: ArrayBuffer) => {
          let options: Options = {
            offset: bufferSize,
            length: buffer.byteLength
          }
          fileIo.readSync(file.fd, buffer, options);
          bufferSize += buffer.byteLength;
        };
        this.audioRenderer.on('writeData', writeDataCallback);
        await this.audioRenderer.start();
      }
    
      async stopRenderer(): Promise<void> {
        if (this.audioRenderer) {
          await this.audioRenderer.release();
          this.audioRenderer = undefined;
        }
        if (this.fileDescriptor) {
          this.closeResource(this.audioSource);
          this.fileDescriptor = undefined;
        }
      }
    
      async closeResource(fileName: string): Promise<void> {
        if (this.appContext) {
          let mgr = this.appContext.resourceManager;
          await mgr.closeRawFd(fileName).then(() => {
            console.info('case closeRawFd success fileName: ' + fileName);
          }).catch((error: BusinessError) => {
            console.error('case closeRawFd err: ' + error);
          });
        }
      }
    }
    
4.  (Optional) Subscribe to audio output device change events if you want to know the device change status.
    
    import { audio } from '@kit.AudioKit';
    // ...
    export default class AudioRenderer {
      // ...
      private audioManager: audio.AudioManager | undefined = undefined;
      private audioRoutingManager: audio.AudioRoutingManager | undefined = undefined;
      private audioRendererInfo: audio.AudioRendererInfo = {
        // Set the parameters related to the call scenario.
        usage: audio.StreamUsage.STREAM\_USAGE\_VIDEO\_COMMUNICATION, // Audio stream usage type: VoIP video call, speaker by default.
        rendererFlags: 0 // AudioRenderer flag. The default value is 0.
      }
      private  audioRendererOption: audio.AudioRendererOptions = {
        streamInfo: this.audioStreamInfo,
        rendererInfo: this.audioRendererInfo
      };
    
      async observerDevices() {
        this.audioManager = audio.getAudioManager(); // Create an AudioManager instance.
        if (!this.audioManager) {
          console.error('get audioManager failed');
          return;
        }
        // Call an API of AudioManager to create an AudioRoutingManager instance.
        this.audioRoutingManager = this.audioManager.getRoutingManager();
        if(!this.audioRoutingManager) {
          return;
        }
        // (Optional) Listen for audio output device changes.
        this.audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', this.audioRendererInfo, (desc: audio.AudioDeviceDescriptors) => {
          console.info(\`device change to: ${desc\[0\].deviceType}\`); // Device type.
        });
      }
      // ...
    }
    
5.  Destroy the AVSession when the call ends.
    
    // Destroy the AVSession created in step 1 when the call ends.
    this.session?.destroy((err) => {
      if (err) {
        console.error(\`Failed to destroy session. Code: ${err.code}, message: ${err.message}\`);
      } else {
        console.info(\`Destroy : SUCCESS \`);
      }
    });
    

## Implementing a Custom Style

You can customize a style by setting the [customPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-avcastpicker#avcastpicker) parameter of the [CustomBuilder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-types#custombuilder8) type.

The procedure for implementing a custom style is similar to that for implementing the default style. You can create an AVSession and implement audio playback by referring to [Implementing the Default Style Implementation](#implementing-the-default-style).

The differences are as follows:

1.  Create a custom AVCastPicker and add custom parameters (corresponding to step 2 of the default style implementation).
    
    import { AVCastPicker } from '@kit.AVSessionKit';
    // ...
    
    @Entry
    @Component
    struct SelfCastPicker {
      @State pickerImage:ResourceStr = $r('app.media.earpiece'); // Custom resources.
      // ...
      build() {
        Row() {
          Column() {
            AVCastPicker(
              {
                customPicker: (): void => this.ImageBuilder() // Add a custom parameter.
              }
            ).size({ height: 45, width: 45 })
          }
        }
      }
    
      // Custom content.
      @Builder
      ImageBuilder() {
        Image(this.pickerImage)
          .size({ width: '100%', height: '100%' })
          .backgroundColor('#00000000')
          .fillColor(Color.Black)
      }
    }
    
2.  If your application needs to change its custom style in response to changes in the audio output device, it must monitor device switching and then refresh the custom style in real time (corresponding to step 4 of the default style implementation).
    
    import { audio } from '@kit.AudioKit';
    
    @Entry
    @Component
    struct SelfCastPicker {
      // ...
      async selfObserverDevices() {
        let audioManager = audio.getAudioManager();
        let audioRoutingManager = audioManager.getRoutingManager();
    
        // When the AVCastPicker component is started for the first time, obtain the current device and refresh the content displayed.
        this.changePickerShow(audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(this.audioRendererInfo));
    
        // Listen for the switching of the audio output device and display different styles based on the device type.
        audioRoutingManager.on('preferOutputDeviceChangeForRendererInfo', this.audioRendererInfo, (desc: audio.AudioDeviceDescriptors) => {
          this.changePickerShow(audioRoutingManager.getPreferredOutputDeviceForRendererInfoSync(this.audioRendererInfo));
        });
      }
    
      // Refresh the custom resource pickerImage after the device is changed.
      private changePickerShow(desc: audio.AudioDeviceDescriptors) {
        if(!desc || !desc.length || !desc\[0\]) {
          return;
        }
        if (desc\[0\].deviceType === 2) {
          this.pickerImage = $r('app.media.sound');
        } else if (desc\[0\].deviceType === 7) {
          this.pickerImage = $r('app.media.bluetooth');
        } else {
          this.pickerImage = $r('app.media.earpiece');
        }
      }
      // ...
    }
    

#### Switching Call Input Devices (for PCs and 2-in-1 Devices Only)

The system no longer provides APIs for switching audio input devices. If you need to switch audio input devices within your application, implement the **AVInputCastPicker** component. For details about the component, see [@ohos.multimedia.avInputCastPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-avinputcastpicker) and [@ohos.multimedia.avCastPickerParam](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-avcastpickerparam).

This topic describes how to integrate the **AVInputCastPicker** component to implement the switching of call input devices.

Currently, the system provides the default style and custom style for the **AVCastPicker** component.

-   If the application chooses to display the default style, when the device switches, the system displays the default component style based on the currently selected device.
-   If the application opts for a custom style, it needs to refresh its defined style in response to device changes.

## Implementing the Default Style

1.  Create the **AVInputCastPicker** component on the call page that provides device switching.
    
    import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';
    
    // ...
      // (Optional) Callback for the device list state change.
      private onStateChange(state: AVCastPickerState) {
        if (state === AVCastPickerState.STATE\_APPEARING) {
          console.info('The picker starts showing.');
        } else if (state === AVCastPickerState.STATE\_DISAPPEARING) {
          console.info('The picker finishes presenting.');
        }
      }
    
      // Create the component and set its size.
      build() {
        Row() {
          Column() {
            AVInputCastPicker(
              {
                onStateChange: this.onStateChange
              }
            ).size({ height: 45, width: 45 })
          }
        }
      }
    
2.  Implement the call feature. For details, see [Developing Audio Call](../../../audio-kit/audio-call/developing-audio-call/document.md).
    

## Implementing a Custom Style

You can customize a style by setting the **customPicker** parameter of the [AVInputCastPicker](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-avinputcastpicker#avinputcastpicker).

1.  When creating a custom **AVInputCastPicker** component, you must add a custom parameter.
    
    import { AVCastPickerState, AVInputCastPicker } from '@kit.AVSessionKit';
    
    @Entry
    @Component
    struct InputCastPicker {
      @State pickerImage: ResourceStr = $r('app.media.sound'); // Custom resources.
      // ...
    
      // (Optional) Callback for the device list state change.
      private onStateChange(state: AVCastPickerState) {
        if (state === AVCastPickerState.STATE\_APPEARING) {
          console.info('The picker starts showing.');
        } else if (state === AVCastPickerState.STATE\_DISAPPEARING) {
          console.info('The picker finishes presenting.');
        }
      }
    
      build() {
        Row() {
          Column() {
            AVInputCastPicker(
              {
                customPicker: this.ImageBuilder.bind(this), // Add a custom parameter.
                onStateChange: this.onStateChange
              }
            )
              .size({ width: '50%', height: '20%' })
              .id('AVInputCastPicker')
            // ...
          }
          .width('100%')
          .alignItems(HorizontalAlign.Center)
        }
        .alignItems(VerticalAlign.Center)
        .width('100%')
        .height('100%')
      }
    
      // Custom content.
      @Builder
      ImageBuilder() {
        Text($r('app.string.switch\_InputDevice'))
        Image(this.pickerImage)
          .size({ width: '100%', height: '100%' })
          .backgroundColor('#00000000')
          .fillColor(Color.Black)
      }
    }
    
2.  Implement the call feature. For details, see [Developing Audio Call](../../../audio-kit/audio-call/developing-audio-call/document.md).
