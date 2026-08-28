# Video Playback (Video)

The **Video** component is used to play a video and control its playback. It is usually used in video players and video list pages within applications. A video automatically plays once fully loaded. When the user clicks the video area, the video is paused and the playback progress bar is displayed. The user can drag the progress bar to the desired position. For details, see [Video](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video).

#### Creating a Video Component

You can create a **Video** component by calling the following API:

Video(value: VideoOptions)

#### Loading Video

The **Video** component supports both local and online videos. For details about data source configuration, see [VideoOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video#videooptions).

## Loading a Local Video

-   Common local video
    
    To load a local video, specify the corresponding video file in the local **rawfile** directory, as shown in the following figure.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/75/v3/nystTJfmRhmi5QFfz5afyw/en-us_image_0000002537924628.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061934Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4633682FF53F410E51E1CBB33266E5B5871201DAC8F4F21477FF17D4720E2A64)
    
    Use **$rawfile()** to reference the video resource.
    
    // xxx.ets
    // ···
    @Component
    export struct LocalVideo {
      private controller: VideoController = new VideoController();
      private previewUris: Resource = $r('app.media.preview');
      private innerResource: Resource = $rawfile('videoTest.mp4');
    
      build() {
        Column() {
          Video({
            src: this.innerResource,  // Set the video source.
            previewUri: this.previewUris, // Set the preview image.
            controller: this.controller // Set the video controller to control the video playback status.
          })
        }
      }
    }
    
-   Video provided by a [DataAbility](../../../../ability-kit/fa-model-development/fa-model-application-components/dataability-component-development/dataability-overview/document.md), whose path contains the **dataability://** prefix
    
    Ensure that the corresponding video resource exists.
    
    // xxx.ets
    // ···
    @Component
    export struct LocalVideoTwo {
      private controller: VideoController = new VideoController();
      private previewUris: Resource = $r('app.media.preview');
      private videoSrc: string = 'dataability://device\_id/com.domainname.dataability.videodata/video/10';
    
      build() {
        Column() {
          Video({
            src: this.videoSrc,
            previewUri: this.previewUris,
            controller: this.controller
          })
        }
      }
    }
    

## Loading a Video in the Application Sandbox

To load a video in the application sandbox, use a string with the **file://** prefix. Ensure that there are files in the specified path and the application has the read permission to the files.

// xxx.ets
// ···
@Component
export struct Sandbox {
  private controller: VideoController = new VideoController();
  private videoSrc: string = 'file:///data/storage/el2/base/haps/entry/files/show.mp4';

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        controller: this.controller
      })
    }
  }
}

## Loading an Online Video

To load online videos, you must apply for the ohos.permission.INTERNET permission. For details about how to apply for the permission, see [Declaring Permissions](../../../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md). In this scenario, the **src** attribute indicates the URL of the online video.

// xxx.ets
// ···
@Component
export struct OnlineVideo {
  private controller: VideoController = new VideoController();
  private previewUris: Resource = $r('app.media.preview');
  private videoSrc: string = 'www.example.com/example.mp4'; // Replace the URL with that of the actual video to load.

  build() {
    Column() {
      Video({
        src: this.videoSrc,
        previewUri: this.previewUris,
        controller: this.controller
      })
    }
  }
}

#### Adding Attributes

Use the [attributes](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video#attributes) of the **Video** component to control video playback. For example, you can set whether to mute the video and whether to display the video playback control bar.

// xxx.ets
// ···
@Component
export struct AttributeVideo {
  private controller: VideoController = new VideoController();

  build() {
    Column() {
      Video({
        controller: this.controller
      })
        .muted(false) // Set whether to mute the video.
        .controls(false) // Set whether to display the video playback control bar.
        .autoPlay(false) // Set whether to enable auto play.
        .loop(false) // Set whether to repeat the video.
        .objectFit(ImageFit.Contain) // Set the video fill mode.
    }
  }
}

#### Adding Events

The **Video** component supports various callback events in addition to the universal events. For details, see [Events](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video#events).

// xxx.ets
@Entry
@Component
struct EventCall {
  private controller: VideoController = new VideoController();
  private previewUris: Resource = $r('app.media.preview');
  private innerResource: Resource = $rawfile('videoTest.mp4');

  build() {
    Column() {
      Video({
        src: this.innerResource,
        previewUri: this.previewUris,
        controller: this.controller
      })
        .onUpdate((event) => { // Triggered when the playback progress changes.
        })
        .onPrepared((event) => { // Triggered when video preparation is complete.
        })
        .onError(() => { // Triggered when the video playback fails.
        })
        .onStop(() => { // Triggered when the video playback stops.
        })
    }
  }
}

#### Using the Video Controller

The video controller is used to control video playback. For details, see [VideoController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-media-components-video#videocontroller).

-   Default controller
    
    The default controller supports four basic features: start playback, pause playback, set the video playback position, and play the video in full screen.
    
    // xxx.ets
    @Entry
    @Component
    struct VideoGuide {
      @State videoSrc: Resource = $rawfile('videoTest.mp4');
      @State previewUri: string = 'common/videoIcon.png';
      @State curRate: PlaybackSpeed = PlaybackSpeed.Speed\_Forward\_1\_00\_X;
    
      build() {
        Row() {
          Column() {
            Video({
              src: this.videoSrc,
              previewUri: this.previewUri,
              currentProgressRate: this.curRate // Set the playback speed.
            })
          }
          .width('100%')
        }
        .height('100%')
      }
    }
    
-   Custom controller
    
    To implement a custom control bar, first disable the default controller. Then, use components such as [Button](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-button) and [Slider](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-slider) to build your own control and display elements. This approach is suitable for scenarios that require a highly customized UI.
    
    // xxx.ets
    @Entry
    @Component
    struct CustomizedControl {
      @State videoSrc: Resource = $rawfile('videoTest.mp4');
      @State previewUri: string = 'common/videoIcon.png';
      @State curRate: PlaybackSpeed = PlaybackSpeed.Speed\_Forward\_1\_00\_X;
      // Initialize the current time to 0.
      @State currentTime: number = 0;
      // Initialize the current time to 0.
      @State durationTime: number = 0;
      controller: VideoController = new VideoController();
    
      build() {
        Row() {
          Column() {
            Video({
              src: this.videoSrc,
              previewUri: this.previewUri,
              currentProgressRate: this.curRate,
              controller: this.controller
            })
              .controls(false)
              .autoPlay(true)
              .onPrepared((event) => {
                if (event) {
                  this.durationTime = event.duration
                }
              })
              .onUpdate((event) => {
                if (event) {
                  this.currentTime = event.time
                }
              })
            Row() {
              Text(JSON.stringify(this.currentTime) + 's')
              Slider({
                value: this.currentTime,
                min: 0,
                max: this.durationTime
              })
                .onChange((value: number, mode: SliderChangeMode) => {
                  this.controller.setCurrentTime(value); // Set the video playback position to the specified time.
                })
                .width('90%')
              Text(JSON.stringify(this.durationTime) + 's')
            }
            .opacity(0.8)
            .width('100%')
          }
          .width('100%')
        }
        .height('40%')
      }
    }
    

#### Remarks

The **Video** component has encapsulated the basic capabilities of video playback. You do not need to create video instances or set and obtain video information. Simply set the data source and basic information to play videos. For details about how to customize video playback, see [Using AVPlayer to Play Videos (ArkTS)](../../../../../media/media-kit/media-development-arkts/playback/using-avplayer-to-play-videos-arkts/document.md).
