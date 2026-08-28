# Playing Moving Photos with MovingPhotoView

The system provides the **MovingPhotoView** component, which can be used to play moving photos in social networking and gallery applications.

#### Constraints

The restrictions on using the **MovingPhotoView** component are as follows:

-   Currently, live properties cannot be set.
-   Currently, the ArkUI [expandSafeArea](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-universal-attributes-expand-safe-area#expandsafearea) cannot be set.
-   When this component is long pressed to trigger playback, the component area is zoomed in to 1.1 times.
-   This component uses [AVPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-media-avplayer) to play moving photos. A maximum of three AVPlayers can be used at the same time. Otherwise, frame freezing may occur.

#### How to Develop

1.  Import modules.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8f/v3/h64Hw0fwRviYLWBvQ1r9nw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E97AC59C56C358994EDD8B69693A16DB8BDC01A5AB0E7D4EC1584C373F5F7518)
    
    -   **MovingPhotoViewAttribute** is essential for configuring the **MovingPhotoView** component. In API version 21 and earlier, you must manually import **MovingPhotoViewAttribute** after importing the **MovingPhotoView** component. Otherwise, a compilation error is reported. However, starting from API version 22, the compilation toolchain automatically imports **MovingPhotoViewAttribute** when it detects the **MovingPhotoView** component, so manual import is no longer necessary.
    -   After **MovingPhotoViewAttribute** is imported, DevEco Studio displays it as grayed out, but this does not affect its usage.
    
    API version 21 and earlier:
    
    import { MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
    
    API version 22 and later:
    
    import { MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';
    
2.  Obtain a [MovingPhoto](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-photoaccesshelper-movingphoto) object.
    
    Use the **photoAccessHelper** APIs to create or obtain a moving photo object. The **MovingPhotoView** receives only the constructed moving photo object.
    
    For details about how to create and obtain a moving photo object, see [Accessing and Managing Moving Photo Assets](../accessing-and-managing-moving-photos/document.md).
    
    src: photoAccessHelper.MovingPhoto | undefined = undefined;
    
3.  Create a [MovingPhotoViewController](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-movingphotoview#movingphotoviewcontroller) to control the playback status (such as playing or stopping) of the moving photo.
    
    controller: MovingPhotoViewController = new MovingPhotoViewController();
    
4.  Create a MovingPhotoView instance.
    
    The values in the following sample code are only examples. For details about the value range of each parameter, see [@ohos.multimedia.movingphotoview](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ohos-multimedia-movingphotoview).
    
     // For API version 21 and earlier, use the following: import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController, MovingPhotoViewAttribute } from '@kit.MediaLibraryKit';
     // For API version 22 and later, use the following:
     import { photoAccessHelper, MovingPhotoView, MovingPhotoViewController } from '@kit.MediaLibraryKit';
    
     @Entry
     @Component
     struct Index {
       @State src: photoAccessHelper.MovingPhoto | undefined = undefined
       @State isMuted: boolean = false
       controller: MovingPhotoViewController = new MovingPhotoViewController();
       build() {
         Column() {
           MovingPhotoView({
             movingPhoto: this.src,
             controller: this.controller
           })
             // Whether to mute the playback. The default value is false. In this example, it is controlled by the button.
             .muted(this.isMuted)
             // Video display mode. The default value is Cover.
             .objectFit(ImageFit.Cover)
             // Triggered when the playback starts.
             .onStart(() => {
               console.info('onStart');
             })
             // Triggered when the playback ends.
             .onFinish(() => {
               console.info('onFinish');
             })
             // Triggered when the playback stops.
             .onStop(() => {
               console.info('onStop')
             })
             // Triggered when an error occurs.
             .onError(() => {
               console.error('onError');
             })
     
           Row() {
             // Button for starting playback.
             Button('start')
               .onClick(() => {
                 this.controller.startPlayback()
               })
               .margin(5)
             // Button for stopping playback.
             Button('stop')
               .onClick(() => {
                 this.controller.stopPlayback()
               })
               .margin(5)
           }
           .alignItems(VerticalAlign.Center)
           .justifyContent(FlexAlign.Center)
           .height('15%')
         }
       }
     }
    

#### Effect

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/5i4Q9haGTLaOgSYeU_KWzQ/en-us_image_0000002568684911.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062044Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8E95D7A1F74134EC84447B44227BBFD9211020561BD0C87E5BD1B32E29E4BB48)
