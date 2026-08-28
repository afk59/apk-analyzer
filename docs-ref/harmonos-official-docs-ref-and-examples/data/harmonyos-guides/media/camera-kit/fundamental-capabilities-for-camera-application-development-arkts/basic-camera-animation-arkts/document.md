# Basic Camera Animation (ArkTS)

During camera usage, preview stream replacement is inevitable in scenarios such as camera mode switching and front/rear camera lens switching. To optimize user experience, you can reasonably use animation effects for transition. This document mainly describes how to capture screenshots of the preview stream and implement animation effects for the following three core scenarios using the [explicit animation capability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-explicit-animatetoimmediately) provided by ArkUI:

-   Mode switching: Use preview stream snapshots to create a blur effect for transition.
    
    The following depicts the transition from video mode to photo mode.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2d/v3/9ETPuZwZT8OhMqtmVBLxvA/en-us_image_0000002537925114.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A48A443A505C260BE6E21AFA948AA8C8B1337CE6835BAB8DFFEEE4B670E4CD89)
    
-   Front/Rear camera switching: Use preview stream snapshots to create a blur-and-flip effect for transition.
    
    The following demonstrates the transition from using the front camera to the rear camera.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/Ofk0SFIPSLCr-bRhWMS_hg/en-us_image_0000002568684891.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C96952A6AF7FB5DC0530C2232D96120B107A24680F9F97FF3FEC7DFB70568C49)
    
-   Photo capture blackout: Use a blackout component to overlay the preview stream to create a blackout transition.
    
    The following depicts the moment of photo capture.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/08/v3/juUPGHzRT1O8SaefJdyBvg/en-us_image_0000002568764901.gif?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=37813BC29A61798208B3930FA2334BC2289E445E459C1D3D28A79D389C07F5A1)
    

#### Blackout Animation

Use component overlay to implement the blackout effect.

The sample code in the following steps is the internal method or logic of a custom component (component decorated by @Component).

1.  Import dependencies. Specifically, import the camera, image, and ArkUI modules.
    
    import { camera } from '@kit.CameraKit';
    import { image } from '@kit.ImageKit';
    import { curves } from '@kit.ArkUI';
    
2.  Build a blackout component.
    
    Define a blackout component, which is displayed during camera blackouts for photo capture or front/rear camera switching. This component will block the XComponent.
    
    Define the component's properties as follows:
    
    @State isShowBlur: boolean = false;
    @State isShowBlack: boolean = false;
    @StorageLink('modeChange') @Watch('onModeChange') modeChangeFlag: number = 0;
    @StorageLink('switchCamera') @Watch('onSwitchCamera') switchCameraFlag: number = 0;
    @StorageLink('frameStart') @Watch('onFrameStart') frameStartFlag: number = 0;
    @StorageLink('captureClick') @Watch('onCaptureClick') captureClickFlag: number = 0;
    @StorageLink('surfaceShot') screenshotPixelMap: image.PixelMap | undefined = undefined; // Snapshot of the preview stream.
    @StorageLink('curPosition') curPosition: number = 0; // Current front/rear camera lens status.
    @State shotImgBlur: number = 0;
    @State shotImgOpacity: number = 1;
    @State shotImgScale: ScaleOptions = { x: 1, y: 1 };
    @State shotImgRotation: RotateOptions = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_0 }
    @State flashBlackOpacity: number = 1;
    
    Implement the logic of the blackout component as follows:
    
    // The component is displayed during camera blackouts for photo capture or camera switching and is used to block the XComponent.
    if (this.isShowBlack) {
      Column()
        .key('black')
        .width(this.getUIContext().px2vp(Constants.X\_COMPONENT\_SURFACE\_HEIGHT))
        .height(this.getUIContext().px2vp(Constants.X\_COMPONENT\_SURFACE\_WIDTH))
        .backgroundColor(Color.Black)
        .opacity(this.flashBlackOpacity)
    }
    
3.  Implement the blackout effect.
    
    private flashBlackAnim() {
      Logger.info(TAG, 'flashBlackAnim E');
      this.flashBlackOpacity = 1;
      this.isShowBlack = true;
      animateToImmediately({
        curve: curves.interpolatingSpring(1, 1, 410, 38),
        delay: 50,
        onFinish: () => {
          this.isShowBlack = false;
          this.flashBlackOpacity = 1;
          Logger.info(TAG, 'flashBlackAnim X');
        }
      }, () => {
        this.flashBlackOpacity = 0;
      })
    }
    
4.  Trigger the blackout effect.
    
    Tap the capture button to update the value of **CaptureClick** bound to [@StorageLink](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/application-state-management/appstorage-storing-application-wide-ui-state/document.md#storagelink). This triggers the **onCaptureClick** method and starts playing the animation effect.
    
    onCaptureClick(): void {
      Logger.info(TAG, 'onCaptureClick');
      this.flashBlackAnim();
    }
    

#### Blur Animation

You can use preview stream snapshots to create a blur effect for mode switching or front/rear camera switching.

The sample code in the following steps (except step 2) is the internal method or logic of a custom component (component decorated by @Component).

1.  Import dependencies. Specifically, import the camera, image, and ArkUI modules.
    
    import { camera } from '@kit.CameraKit';
    import { image } from '@kit.ImageKit';
    import { curves } from '@kit.ArkUI';
    
2.  Obtain a preview stream snapshot.
    
    Preview stream snapshots are obtained by calling [image.createPixelMapFromSurface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmapfromsurface11) provided by the image module. In this API, **surfaceId** is the surface ID of the current preview stream, and **size** is the width and height of the current preview stream profile. Create a snapshot utility class (TS file), import the dependency, and export the snapshot retrieval API for the page to use. The code snippet below shows the implementation of the snapshot utility class.
    
    export class BlurAnimateUtil {
      public static surfaceShot: image.PixelMap;
      // ...
    
      /\*\*
       \* Obtain a surface snapshot.
       \* @param surfaceId
       \* @returns
       \*/
      public static async doSurfaceShot(surfaceId: string) {
        Logger.info(TAG, \`doSurfaceShot surfaceId:${surfaceId}.\`);
        if ('' === surfaceId) {
          Logger.error(TAG, 'surface not ready!');
          return;
        }
        try {
          if (this.surfaceShot) {
            await this.surfaceShot.release();
          }
          this.surfaceShot = await image.createPixelMapFromSurface(surfaceId, {
            size: { width: Constants.X\_COMPONENT\_SURFACE\_WIDTH, height: Constants.X\_COMPONENT\_SURFACE\_HEIGHT }, // Obtain the width and height of the preview stream profile.
            x: 0,
            y: 0
          });
          let imageInfo: image.ImageInfo = await this.surfaceShot.getImageInfo();
          Logger.info('doSurfaceShot surfaceShot:' + JSON.stringify(imageInfo.size));
        } catch (err) {
          Logger.error(JSON.stringify(err))
        }
      }
    
      public static getSurfaceShot() {
        return this.surfaceShot;
      }
    }
    
3.  Build a snapshot component.
    
    Define a snapshot component, and place it above the XComponent of the preview stream to block the XComponent.
    
    Define the component's properties as follows:
    
    @State isShowBlur: boolean = false;
    @State isShowBlack: boolean = false;
    @StorageLink('modeChange') @Watch('onModeChange') modeChangeFlag: number = 0;
    @StorageLink('switchCamera') @Watch('onSwitchCamera') switchCameraFlag: number = 0;
    @StorageLink('frameStart') @Watch('onFrameStart') frameStartFlag: number = 0;
    @StorageLink('captureClick') @Watch('onCaptureClick') captureClickFlag: number = 0;
    @StorageLink('surfaceShot') screenshotPixelMap: image.PixelMap | undefined = undefined; // Snapshot of the preview stream.
    @StorageLink('curPosition') curPosition: number = 0; // Current front/rear camera lens status.
    @State shotImgBlur: number = 0;
    @State shotImgOpacity: number = 1;
    @State shotImgScale: ScaleOptions = { x: 1, y: 1 };
    @State shotImgRotation: RotateOptions = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_0 }
    @State flashBlackOpacity: number = 1;
    
    Implement the snapshot component as follows:
    
    if (this.isShowBlur) {
      Column() {
        Image(this.screenshotPixelMap)
          .blur(this.shotImgBlur)
          .opacity(this.shotImgOpacity)
          .rotate(this.shotImgRotation) // Rotation capability provided by ArkUI, used to rotate components along a specified coordinate system.
          .scale(this.shotImgScale)
          .width(this.getUIContext().px2vp(Constants.X\_COMPONENT\_SURFACE\_HEIGHT))
          .height(this.getUIContext().px2vp(Constants.X\_COMPONENT\_SURFACE\_WIDTH))
          .syncLoad(true)
      }
      .width(this.getUIContext().px2vp(Constants.X\_COMPONENT\_SURFACE\_HEIGHT))
      .height(this.getUIContext().px2vp(Constants.X\_COMPONENT\_SURFACE\_WIDTH))
    }
    
4.  (Optional) Implement the fade-in blur effect.
    
    The mode switching animation is implemented in two phases: fade-in blur animation and fade-out blur animation.
    
    When a user touches a button, and the camera takes a snapshot of the preview stream. The snapshot component is displayed, which gradually blurs over the existing preview stream, implementing the fade-in blur animation.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/MUeBjj16Tyq3LbQVw6HqLQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8CAB89EC4FF96E1C25160847DEEE39489698A68D1D7BBD0D25425123A069F57D)
    
    Since the [image.createPixelMapFromSurface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-f#imagecreatepixelmapfromsurface11) API provided by the graphics framework retrieves a [PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap) by capturing the surface, its output differs from the rendering logic of the [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) component. You must apply different **rotation compensation to both the image content and the component** based on **whether the front or rear camera is in use**.
    
    private async showBlurAnim() {
      Logger.info(TAG, 'showBlurAnim E');
      // Obtain the surface snapshot.
      let shotPixel = BlurAnimateUtil.getSurfaceShot();
      // The rear camera is used.
      if (this.curPosition === 0) {
        Logger.info(TAG, 'showBlurAnim BACK');
        // Rotation compensation of 90° for rear camera snapshots on bar phones.
        await shotPixel.rotate(BlurAnimateUtil.IMG\_ROTATE\_ANGLE\_90);
        // Initial flip angle of 0° for rear camera snapshots on bar phones.
        this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_0 };
      } else {
        Logger.info(TAG, 'showBlurAnim FRONT');
        // Rotation compensation of 270° for front camera snapshots on bar phones.
        await shotPixel.rotate(BlurAnimateUtil.IMG\_ROTATE\_ANGLE\_270);
        // Mirror compensation for front camera snapshots on bar phones.
        this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_180 };
      }
      this.screenshotPixelMap = shotPixel;
      // Initialize animation parameters.
      this.shotImgBlur = 0; // No blur.
      this.shotImgOpacity = 1; // Opaque.
      // Trigger page rendering.
      this.isShowBlur = true;
      animateToImmediately(
        {
          duration: BlurAnimateUtil.SHOW\_BLUR\_DURATION,
          curve: Curve.Friction,
          onFinish: async () => {
            Logger.info(TAG, 'showBlurAnim X');
          }
        },
        () => {
          // Implement the blur change animation.
          this.shotImgBlur = BlurAnimateUtil.ANIM\_MODE\_SWITCH\_BLUR;
        }
      );
    }
    
5.  Implement the fade-out blur animation.
    
    The fade-out blur animation is triggered by the event [on('frameStart')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-previewoutput#onframestart) of the new preview stream. During this effect, the snapshot component gradually becomes clear, revealing the new preview stream.
    
    private hideBlurAnim(): void {
      this.isShowBlack = false;
      Logger.info(TAG, 'hideBlurAnim E');
      animateToImmediately({
        duration: BlurAnimateUtil.HIDE\_BLUR\_DURATION,
        curve: Curve.FastOutSlowIn,
        onFinish: () => {
          // Remove the blur component from the component tree.
          this.isShowBlur = false;
          this.shotImgBlur = 0;
          this.shotImgOpacity = 1;
          Logger.info(TAG, 'hideBlurAnim X');
        }
      }, () => {
        // Change the opacity of the snapshot component.
        this.shotImgOpacity = 0;
      });
    }
    
6.  (Optional) Implement the blur-and-flip animation.
    
    The animation is carried out in two phases: blur-and-flip and fade-out blur, where fade-out blur is the same as that in step 5.
    
    The blur-and-flip animation is realized through two stages of component rotation—initially a 90° rotation outwards, and then a 90° rotation inwards—accompanied by additional effects such as blur, opacity changes, and scaling.
    
    To ensure that the preview stream is not exposed during flip, you must also build a blackout component to mask the XComponent, following the instructions provided in step 2 in [Blackout Animation](#blackout-animation).
    
    /\*\*
     \* A 90° rotation outwards first for transition between the front and real cameras.
     \*/
    private async rotateFirstAnim() {
      Logger.info(TAG, 'rotateFirstAnim E');
      // Obtain the surface snapshot.
      let shotPixel = BlurAnimateUtil.getSurfaceShot();
      // Switch from the rear camera to the front camera.
      if (this.curPosition === 1) {
        Logger.info(TAG, 'rotateFirstAnim BACK');
          // Rotation compensation of 90° for snapshots when switching from rear to front camera on bar phones.
        Rotation provided by await shotPixel.rotate(BlurAnimateUtil.IMG\_ROTATE\_ANGLE\_90); // Rotation capability provided by Image Kit, used to handle rotation of the image itself.
        // Initial flip angle of 0° for snapshots when switching from rear to front camera on bar phones.
        this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_0 };
      } else {
        Logger.info(TAG, 'rotateFirstAnim FRONT');
        // Rotation compensation of 270° for snapshots when switching from front to rear camera on bar phones.
        await shotPixel.rotate(BlurAnimateUtil.IMG\_ROTATE\_ANGLE\_270);
        // Initial flip angle of 180° for snapshots when switching from front to rear camera on bar phones.
        this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_180 };
      }
      this.screenshotPixelMap = shotPixel;
      // Trigger page rendering.
      this.isShowBlack = true;
      this.isShowBlur = true;
      animateToImmediately(
        {
          duration: BlurAnimateUtil.ROTATION\_DURATION,
          delay: BlurAnimateUtil.FLIP\_DELAY, // This delay ensures that the component's scaling and blur effects are triggered in prior to the flip effect.
          curve: curves.cubicBezierCurve(0.20, 0.00, 0.83, 1.00),
          onFinish: () => {
            Logger.info(TAG, 'rotateFirstAnim X');
            // Trigger the second-stage rotation after onFinish is invoked.
            this.rotateSecondAnim();
          }
        },
        () => {
          // Flip animation effect for the snapshot.
          if (this.curPosition === 1) {
            this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_90 };
          } else {
            this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_270 };
          }
        }
      )
    }
    
    /\*\*
     \* Flip inwards by 90°.
     \*/
    async rotateSecondAnim() {
      Logger.info(TAG, 'rotateSecondAnim E');
      // Obtain the surface snapshot.
      let shotPixel = BlurAnimateUtil.getSurfaceShot();
      // The rear camera is used.
      if (this.curPosition === 1) {
        // Rotation compensation of 90° for rear camera on bar phones.
        Rotation provided by await shotPixel.rotate(BlurAnimateUtil.IMG\_ROTATE\_ANGLE\_90); // Rotation capability provided by Image Kit, used to handle rotation of the image itself.
        // Instantly adjust to -90° to ensure the image is not mirrored after the second-stage rotation.
        this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_MINUS\_90 };
      } else { // The front camera is used.
        // Rotation compensation of 270° for front camera snapshots on bar phones.
        await shotPixel.rotate(BlurAnimateUtil.IMG\_ROTATE\_ANGLE\_270);
        // Mirror compensation for front camera snapshots on bar phones.
        this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_180 };
      }
      this.screenshotPixelMap = shotPixel;
    
      animateToImmediately(
        {
          duration: BlurAnimateUtil.ROTATION\_DURATION,
          curve: curves.cubicBezierCurve(0.17, 0.00, 0.20, 1.00),
          onFinish: () => {
            Logger.info(TAG, 'rotateSecondAnim X');
          }
        },
        () => {
          // Flip to the initial state.
          if (this.curPosition === 1) {
            this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_0 };
          } else {
            this.shotImgRotation = { y: BlurAnimateUtil.ROTATE\_AXIS, angle: BlurAnimateUtil.IMG\_FLIP\_ANGLE\_180 };
          }
        }
      )
    }
    
    /\*\*
     \* Flip outwards by 90°.
     \*/
    blurFirstAnim() {
      Logger.info(TAG, 'blurFirstAnim E');
      // Initialize animation parameters.
      this.shotImgBlur = 0; // No blur.
      this.shotImgOpacity = 1; // Opaque.
      this.shotImgScale = { x: 1, y: 1 };
      animateToImmediately(
        {
          duration: BlurAnimateUtil.ROTATION\_DURATION,
          curve: Curve.Sharp,
          onFinish: () => {
            Logger.info(TAG, 'blurFirstAnim X');
            this.blurSecondAnim();
          }
        },
        () => {
          // Implement the blur change animation.
          this.shotImgBlur = BlurAnimateUtil.ANIM\_MODE\_SWITCH\_BLUR;
          // Implement the scale change animation.
          this.shotImgScale = { x: BlurAnimateUtil.IMG\_SCALE, y: BlurAnimateUtil.IMG\_SCALE };
        }
      );
    }
    
    /\*\*
     \* Flip inwards by 90°.
     \*/
    blurSecondAnim() {
      Logger.info(TAG, 'blurSecondAnim E');
      animateToImmediately(
        {
          duration: BlurAnimateUtil.ROTATION\_DURATION,
          curve: Curve.Sharp,
          onFinish: () => {
            Logger.info(TAG, 'blurSecondAnim X');
          }
        },
        () => {
          this.shotImgScale = { x: 1, y: 1 };
        }
      )
    }
    
7.  Trigger the animations on demand.
    
    Mode switch animation trigger: Tap the mode button to immediately execute the **doSurfaceShot** snapshot method, update the value of **modeChange** bound to [@StorageLink](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/application-state-management/appstorage-storing-application-wide-ui-state/document.md#storagelink), and trigger the **onModeChange** method to start the animation.
    
    onModeChange(): void {
      Logger.info(TAG, 'onModeChange');
      this.showBlurAnim();
    }
    
    Front/rear camera switch animation trigger: Tap the front/rear switch button to immediately execute the **doSurfaceShot** snapshot, update the value of **switchCamera** bound to [@StorageLink](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/application-state-management/appstorage-storing-application-wide-ui-state/document.md#storagelink), and trigger the **onSwitchCamera** method to start the animation.
    
    onSwitchCamera(): void {
      Logger.info(TAG, 'onSwitchCamera');
      this.blurFirstAnim();
      this.rotateFirstAnim();
    }
    
    Fade-out blur animation trigger: Listen for the preview stream first frame callback [on('frameStart')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-previewoutput#onframestart), update the value of **frameStart** bound to [@StorageLink](../../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/ui-paradigm-state-management/state-management-v1/application-state-management/appstorage-storing-application-wide-ui-state/document.md#storagelink), and trigger the **onFrameStart** method to start the animation.
    
    onFrameStart(): void {
      Logger.info(TAG, 'onFrameStart');
      this.hideBlurAnim();
    }
