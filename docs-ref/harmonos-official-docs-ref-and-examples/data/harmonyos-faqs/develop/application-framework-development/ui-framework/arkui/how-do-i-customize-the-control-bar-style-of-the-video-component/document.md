# How do I customize the control bar style of the Video component?

1.  Set **controls** to **false** to disable the default control bar.
2.  Sets **controller** for the **Video** component.
3.  Implement a custom control bar in ArkTS and use **VideoController** to control video playback.
    
    @Entry
    @Component
    struct VideoCreateComponent {
      @State videoSrc: Resource = $rawfile('xxx.mp4')
      @State previewUri: Resource = $r('app.media.xxx')
      @State curRate: PlaybackSpeed = PlaybackSpeed.Speed\_Forward\_1\_00\_X
      @State isAutoPlay: boolean = false
      @State showControls: boolean = true
      controller: VideoController = new VideoController()
    
      build() {
        Column() {
          Video({
            src: this.videoSrc,
            previewUri: this.previewUri,
            currentProgressRate: this.curRate,
            controller: this.controller
          })
            .width('100%')
            .height(600)
            .autoPlay(this.isAutoPlay)
            .controls(this.showControls)
            .onStart(() => {
              console.info('onStart')
            })
            .onPause(() => {
              console.info('onPause')
            })
            .onFinish(() => {
              console.info('onFinish')
            })
            .onError(() => {
              console.info('onError')
            })
            .onPrepared((e) => {
              console.info('onPrepared is ' + e.duration)
            })
            .onSeeking((e) => {
              console.info('onSeeking is ' + e.time)
            })
            .onSeeked((e) => {
              console.info('onSeeked is ' + e.time)
            })
            .onUpdate((e) => {
              console.info('onUpdate is ' + e.time)
            })
          Row() {
            Button('src').onClick(() => {
              this.videoSrc = $rawfile('xxx.mp4') // Switch video source
            }).margin(5)
            Button('previewUri').onClick(() => {
              this.previewUri = $r('app.media.xxx') // Switch video preview poster
            }).margin(5)
    
            Button('controls').onClick(() => {
                this.showControls = !this.showControls // Switch whether to display the video control bar
            }).margin(5)
          }
    
          Row() {
            Button('start').onClick(() => {
              this.controller.start() // Start playback.
            }).margin(5)
            Button('pause').onClick(() => {
              this.controller.pause() // Pause playback.
            }).margin(5)
            Button('stop').onClick(() => {
              this.controller.stop() // Stop playback.
            }).margin(5)
            Button('setTime').onClick(() => {
              this.controller.setCurrentTime(10, SeekMode.Accurate) // Accurately jump to the 10s position of the video
            }).margin(5)
          }
    
          Row() {
            Button('rate 0.75').onClick(() => {
              this.curRate = PlaybackSpeed.Speed\_Forward\_0\_75\_X // 0.75 times playback speed
            }).margin(5)
            Button('rate 1').onClick(() => {
              this.curRate = PlaybackSpeed.Speed\_Forward\_1\_00\_X // Original speed playback
            }).margin(5)
            Button('rate 2').onClick(() => {
              this.curRate = PlaybackSpeed.Speed\_Forward\_2\_00\_X // Play at 2x speed
            }).margin(5)
          }
        }
      }
    }
    

**Reference**

[Video](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-common-components-video-player)
