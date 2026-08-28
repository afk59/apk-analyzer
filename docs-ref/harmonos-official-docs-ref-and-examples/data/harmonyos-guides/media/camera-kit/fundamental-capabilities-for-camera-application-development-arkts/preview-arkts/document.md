# Preview (ArkTS)

Before developing a camera application, you must [request required permissions](../../requesting-camera-development-permissions/document.md).

Preview is the image you see after you start the camera application but before you take photos or record videos.

#### How to Develop

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

1.  Import the camera module, which provides camera-related properties and methods.
    
    import { camera } from '@kit.CameraKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Create a surface.
    
    The camera development model relies on the surface model, which uses surface for data interaction. When developing the camera application UI, you need to create an XComponent to provide a surface for the preview stream, and then obtain the surface ID associated with the XComponent to create a preview stream. The preview stream can be directly rendered within the XComponent. For details about how to obtain the surface ID, see [getXComponentSurfaceId](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent#getxcomponentsurfaceid9). The capabilities of the XComponent are provided by the UI. For details, see [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9f/v3/zkQlfN1JSQ63af4vAUD_PQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFBA4861BDAF26669BAEF55D0853740EB76CD7B0166D5CBD3CE3458374294A34)
    
    The preview stream and video output stream must have the same aspect ratio of the resolution. For example, the aspect ratio of the surface of the **XComponent** is 1920:1080 (which is equal to 16:9), then the aspect ratio of the resolution of the preview stream must also be 16:9. This means that the resolution can be 640:360, 960:540, 1920:1080, or the like.
    
    @Entry
    @Component
    struct example {
      xComponentCtl: XComponentController = new XComponentController();
      surfaceId:string = '';
      imageWidth: number = 1920;
      imageHeight: number = 1080;
      private uiContext: UIContext = this.getUIContext();
      private mXComponentOptions: XComponentOptions = {
        type: XComponentType.SURFACE,
        controller: this.xComponentCtl
      }
    
      build() {
        XComponent(this.mXComponentOptions)
          .onLoad(async () => {
            console.info('onLoad is called');
            this.surfaceId = this.xComponentCtl.getXComponentSurfaceId(); // Obtain the surface ID of the component.
            // Use the surface ID to create a preview stream and start the camera. The component renders the preview stream data of each frame in real time.
          })
          // The width and height of the surface are opposite to those of the XComponent. Alternatively, you can use .renderFit(RenderFit.RESIZE\_CONTAIN) to automatically adjust the display without manually setting the width and height.
          .width(this.uiContext.px2vp(this.imageHeight))
          .height(this.uiContext.px2vp(this.imageWidth))
      }
    }
    
3.  Use **previewProfiles** in [CameraOutputCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-i#cameraoutputcapability) to obtain the preview output capabilities, in the format of an **previewProfilesArray** array, supported by the current device. Then call [createPreviewOutput](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#createpreviewoutput) to create a PreviewOutput object, with the first parameter set to the preview profile supported by the camera and the second parameter set to the surface ID obtained in step 2.
    
    function getPreviewOutput(cameraManager: camera.CameraManager, cameraOutputCapability: camera.CameraOutputCapability, surfaceId: string): camera.PreviewOutput | undefined {
      if (!cameraOutputCapability || !cameraOutputCapability.previewProfiles) {
        return;
      }
      let previewProfilesArray: Array<camera.Profile> = cameraOutputCapability.previewProfiles;
      if (!previewProfilesArray || previewProfilesArray.length === 0) {
        console.error("previewProfilesArray is null or \[\]");
        return;
      }
      let previewOutput: camera.PreviewOutput | undefined = undefined;
      try {
        // Choose the preview profile from previewProfilesArray that matches the aspect ratio set in Step 2. Selecting the first item in the array here is for API usage example only.
        previewOutput = cameraManager.createPreviewOutput(previewProfilesArray\[0\], surfaceId);
      } catch (error) {
        let err = error as BusinessError;
        console.error("Failed to create the PreviewOutput instance. error code: " + err.code);
      }
      return previewOutput;
    }
    
4.  Call [Session.start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session#start11) to start outputting the preview stream. If the call fails, an error code is returned. For details, see [CameraErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#cameraerrorcode).
    
    async function startPreviewOutput(cameraManager: camera.CameraManager, previewOutput: camera.PreviewOutput): Promise<void> {
      try {
        let cameraArray: Array<camera.CameraDevice> = \[\];
        cameraArray = cameraManager.getSupportedCameras();
        if (cameraArray.length == 0) {
          console.error('no camera.');
          return;
        }
        // Obtain the supported modes.
        let sceneModes: Array<camera.SceneMode> = cameraManager.getSupportedSceneModes(cameraArray\[0\]);
        let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL\_PHOTO) >= 0;
        if (!isSupportPhotoMode) {
          console.error('photo mode not support');
          return;
        }
        let cameraInput: camera.CameraInput | undefined;
        cameraInput = cameraManager.createCameraInput(cameraArray\[0\]);
        if (cameraInput === undefined) {
          console.error('cameraInput is undefined');
          return;
        }
        // Open the camera.
        await cameraInput.open();
        let session = cameraManager.createSession(camera.SceneMode.NORMAL\_PHOTO);
        if (!session) {
          console.error('session is null');
          return;
        }
        let photoSession: camera.PhotoSession = session as camera.PhotoSession;
        photoSession.beginConfig();
        photoSession.addInput(cameraInput);
        photoSession.addOutput(previewOutput);
        await photoSession.commitConfig();
        await photoSession.start();
      } catch (error) {
        console.error(\`startPreviewOutput call failed, error: ${error}\`);
      }
    }
    

#### Status Listening

During camera application development, you can listen for the preview output stream status, including preview stream start, preview stream end, and preview stream output errors.

-   Register the [on('frameStart')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-previewoutput#onframestart) callback function to listen for preview stream start results. The callback is registered once the **previewOutput** is successfully created, and is triggered when the preview is exposed for the first time. If a result is returned, the preview stream is considered started.
    
    function onPreviewOutputFrameStart(previewOutput: camera.PreviewOutput): void {
      previewOutput.on('frameStart', (err: BusinessError) => {
        if (err !== undefined && err.code !== 0) {
          return;
        }
        console.info('Preview frame started');
      });
    }
    
-   Register the [on('frameEnd')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-previewoutput#onframeend) callback function to listen for preview stream end results. The callback is registered once the **previewOutput** is successfully created, and is triggered when the preview finishes the last frame. If a result is returned, the preview stream is considered ended.
    
    function onPreviewOutputFrameEnd(previewOutput: camera.PreviewOutput): void {
      previewOutput.on('frameEnd', (err: BusinessError) => {
        if (err !== undefined && err.code !== 0) {
          return;
        }
        console.info('Preview frame ended');
      });
    }
    
-   Register the **'error'** event to listen for preview output errors. The callback function returns an error code when an API is incorrectly used. For details about the error code types, see [CameraErrorCode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-e#cameraerrorcode).
    
    function onPreviewOutputError(previewOutput: camera.PreviewOutput): void {
      previewOutput.on('error', (previewOutputError: BusinessError) => {
        console.error(\`Preview output error code: ${previewOutputError.code}\`);
      });
    }
    

#### Complete Sample Code

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl, Permissions } from '@kit.AbilityKit';

@Entry
@Component
struct Index {
  private xComponentCtl: XComponentController = new XComponentController();
  private xComponentSurfaceId: string = '';
  @State imageWidth: number = 1920;
  @State imageHeight: number = 1080;
  private cameraManager: camera.CameraManager | undefined = undefined;
  private cameras: Array<camera.CameraDevice> | undefined = \[\];
  private cameraInput: camera.CameraInput | undefined = undefined;
  private previewOutput: camera.PreviewOutput | undefined = undefined;
  private session: camera.VideoSession | undefined = undefined;
  private uiContext: UIContext = this.getUIContext();
  private context: Context | undefined = this.uiContext.getHostContext();
  private cameraPermission: Permissions = 'ohos.permission.CAMERA'; // For details about how to request permissions, see the instructions provided at the beginning of this topic.
  @State isShow: boolean = false;
  private mXComponentOptions: XComponentOptions = {
    type: XComponentType.SURFACE,
    controller: this.xComponentCtl
  }

  async requestPermissionsFn(): Promise<void> {
    let atManager = abilityAccessCtrl.createAtManager();
    if (this.context) {
      let res = await atManager.requestPermissionsFromUser(this.context, \[this.cameraPermission\]);
      for (let i = 0; i < res.permissions.length; i++) {
        if (this.cameraPermission.toString() === res.permissions\[i\] && res.authResults\[i\] === 0) {
          this.isShow = true;
        }
      }
    }
  }

  aboutToAppear(): void {
    this.requestPermissionsFn();
  }

  onPageShow(): void {
    console.info('onPageShow');
    if (this.xComponentSurfaceId !== '') {
      this.initCamera();
    }
  }

  onPageHide(): void {
    console.info('onPageHide');
    this.releaseCamera();
  }

  build() {
    Column() {
      if (this.isShow) {
        XComponent(this.mXComponentOptions)
          .onLoad(async () => {
            console.info('onLoad is called');
            this.xComponentSurfaceId = this.xComponentCtl.getXComponentSurfaceId(); // Obtain the surface ID of the component.
            // Initialize the camera. The component renders the preview stream data of each frame in real time.
            this.initCamera()
          })
          .width(this.uiContext.px2vp(this.imageHeight))
          .height(this.uiContext.px2vp(this.imageWidth))
      }
    }
    .justifyContent(FlexAlign.Center)
    .height('100%')
    .width('100%')
  }

  // Initialize the camera.
  async initCamera(): Promise<void> {
    console.info(\`initCamera previewOutput xComponentSurfaceId:${this.xComponentSurfaceId}\`);
    try {
      // Obtain a camera manager instance.
      this.cameraManager = camera.getCameraManager(this.context);
      if (!this.cameraManager) {
        console.error('initCamera getCameraManager');
        return;
      }
      // Obtain the list of cameras supported by the device.
      this.cameras = this.cameraManager.getSupportedCameras();
      if (!this.cameras) {
        console.error('initCamera getSupportedCameras');
      }
      // Select a camera device and create a CameraInput object.
      this.cameraInput = this.cameraManager.createCameraInput(this.cameras\[0\]);
      if (!this.cameraInput) {
        console.error('initCamera createCameraInput');
        return;
      }
      // Open the camera.
      await this.cameraInput.open();
      // Obtain the profile supported by the camera device.
      let capability: camera.CameraOutputCapability =
        this.cameraManager.getSupportedOutputCapability(this.cameras\[0\], camera.SceneMode.NORMAL\_VIDEO);
      if (!capability || capability.previewProfiles.length === 0) {
        console.error('capability is null || \[\]');
        this.releaseCamera();
        return;
      }
      let minRatioDiff : number = 0.1;
      let surfaceRatio : number = this.imageWidth / this.imageHeight; // The closest aspect ratio to 16:9.
      let previewProfile: camera.Profile = capability.previewProfiles\[0\];
      // Select a supported preview stream profile based on service requirements.
      // The following uses the preview stream profile with the CAMERA\_FORMAT\_YUV\_420\_SP (NV21) format that meets the resolution constraints as an example.
      for (let index = 0; index < capability.previewProfiles.length; index++) {
        const tempProfile = capability.previewProfiles\[index\];
        let tempRatio = tempProfile.size.width >= tempProfile.size.height ?
          tempProfile.size.width / tempProfile.size.height : tempProfile.size.height / tempProfile.size.width;
        let currentRatio = Math.abs(tempRatio - surfaceRatio);
        if (currentRatio <= minRatioDiff && tempProfile.format == camera.CameraFormat.CAMERA\_FORMAT\_YUV\_420\_SP) {
          previewProfile = tempProfile;
          break;
        }
      }
      this.imageWidth = previewProfile.size.width; // Update the width of the XComponent.
      this.imageHeight = previewProfile.size.height; // Update the height of the XComponent.
      console.info(\`initCamera imageWidth:${this.imageWidth} imageHeight:${this.imageHeight}\`);

      // Create a preview using xComponentSurfaceId.
      this.previewOutput = this.cameraManager.createPreviewOutput(previewProfile, this.xComponentSurfaceId);
      if (!this.previewOutput) {
        console.error('initCamera createPreviewOutput');
        this.releaseCamera();
        return;
      }
      // Create a camera session in recording mode.
      let session = this.cameraManager.createSession(camera.SceneMode.NORMAL\_VIDEO);
      if (!session) {
        console.error('session is null');
        this.releaseCamera();
        return;
      }
      this.session = session as camera.VideoSession;
      // Start configuration for the session.
      this.session.beginConfig();
      // Add a camera input.
      this.session.addInput(this.cameraInput);
      // Add a preview output stream.
      this.session.addOutput(this.previewOutput);
      // Commit the session configuration.
      await this.session.commitConfig();
      // Start the configured input and output streams.
      await this.session.start();
    } catch (error) {
      console.error(\`initCamera fail: ${JSON.stringify(error)}\`);
      this.releaseCamera();
    }
  }

  // Release the camera.
  async releaseCamera(): Promise<void> {
    console.info('releaseCamera');
    // Stop the session.
    await this.session?.stop().catch((e: BusinessError) => {console.error('Failed to stop session: ', e)});
    // Release the camera input stream.
    await this.cameraInput?.close().catch((e: BusinessError) => {console.error('Failed to close the camera: ', e)});
    // Release the preview output stream.
    await this.previewOutput?.release().catch((e: BusinessError) => {console.error('Failed to stop the preview stream: ', e)});
    // Release the session.
    await this.session?.release().catch((e: BusinessError) => {console.error('Failed to release session: ', e)});
  }
}
