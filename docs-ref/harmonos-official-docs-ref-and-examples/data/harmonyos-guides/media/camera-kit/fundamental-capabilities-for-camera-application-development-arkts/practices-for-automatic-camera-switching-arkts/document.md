# Practices for Automatic Camera Switching (ArkTS)

When adapting your application for foldable devices, for simple UX interaction scenarios (e.g., facial recognition), you are advised to use the automatic camera switching capability. On foldable devices equipped with multiple front cameras, after your application enables the automatic camera switching capability, the system automatically completes camera switching and session configuration. It can automatically switch to the currently available front camera for different fold states, preventing black screens caused by the front camera being folded inward.

For example, a foldable device has three cameras: rear camera A, front camera B, and front camera C. In the unfolded state, you can obtain rear camera A and front camera B via the [CameraManager.getSupportedCameras](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-cameramanager#getsupportedcameras) API; in the folded state, you can obtain rear camera A and front camera C. You can enable the front camera for the current fold state, then call [enableAutoDeviceSwitch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-autodeviceswitch#enableautodeviceswitch13) to activate automatic camera switching. This way, when the device's fold state changes next time, the system will automatically switch to the front camera corresponding to the new fold state.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/xUvQNpNoRfS9DY-cX3tnmQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062038Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6E8BEFCF9FD7494F6EB762E94AD90556F819A73E4A23173F64220A0649D9F4BD)

The automatic camera switching feature enables the system to automatically handle input device switching, session configuration, and parameter continuity. If the system detects a camera switch and finds that the zoom ranges of the two cameras are inconsistent, it will notify your application via the **isDeviceCapabilityChanged** field in **AutoDeviceSwitchStatus**. Your application must then handle UX changes on its own (e.g., for zoom range adjustments, you need to re-fetch data via the **getZoomRatioRange** API and update the UX accordingly). Therefore, for camera selection in complex scenarios such as photo capture or video recording, see [Adapting Camera Changes in Different Fold States](../adapting-camera-changes-in-different-fold-states-arkts/document.md).

Read [Camera](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera) for the API reference.

For details about how to obtain the context, see [Obtaining the Context of UIAbility](../../../../application-framework/ability-kit/stage-model-development/stage-model-application-components/uiability-component/uiability-usage/document.md#obtaining-the-context-of-uiability).

Before developing a camera application, you must [request required permissions](../../requesting-camera-development-permissions/document.md).

#### Importing Dependencies

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl } from '@kit.AbilityKit';

#### Creating an XComponent

Use [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent) to display the camera preview.

@Entry
@Component
struct Index {
  private mXComponentController: XComponentController = new XComponentController();
  private mCameraPosition: camera.CameraPosition = camera.CameraPosition.CAMERA\_POSITION\_BACK;
  private mXComponentOptions: XComponentOptions = {
    type: XComponentType.SURFACE,
    controller: this.mXComponentController
  }

  async loadXComponent() {
    // Initialize the XComponent.
  }

  build() {
    Stack() {
      XComponent(this.mXComponentOptions)
        .onLoad(async () => {
          await this.loadXComponent();
        })
        .width(this.getUIContext().px2vp(1080))
        .height(this.getUIContext().px2vp(1920))
      Text('Switch camera')
        .size({ width: 80, height: 48 })
        .position({ x: 1, y: 1 })
        .backgroundColor(Color.White)
        .textAlign(TextAlign.Center)
        .borderRadius(24)
        .onClick(async () => {
          this.mCameraPosition = this.mCameraPosition === camera.CameraPosition.CAMERA\_POSITION\_BACK ?
            camera.CameraPosition.CAMERA\_POSITION\_FRONT : camera.CameraPosition.CAMERA\_POSITION\_BACK;
          await this.loadXComponent();
        })
    }
    .size({ width: '100%', height: '100%' })
    .backgroundColor(Color.Black)
  }
}

#### Enabling Automatic Camera Switching

Before calling [enableAutoDeviceSwitch](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-autodeviceswitch#enableautodeviceswitch13), use [isAutoDeviceSwitchSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-autodeviceswitchquery#isautodeviceswitchsupported13) to check whether the device supports automatic camera switching.

function enableAutoDeviceSwitch(session: camera.PhotoSession) {
  if (session.isAutoDeviceSwitchSupported()) {
    try {
      session.enableAutoDeviceSwitch(true);
    } catch (error) {
      let err = error as BusinessError;
      console.error(\`The enableAutoDeviceSwitch call failed, error code: ${err.code}, error message: ${err.message}\`);
    }
  }
}

#### Listening for Automatic Camera Switching

Use [on('autoDeviceSwitchStatusChange')](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-photosession#onautodeviceswitchstatuschange13) to listen for automatic camera switching. A callback is invoked once the switch is complete.

Do not call any [session](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-camera-session)\-related APIs during the automatic camera switching.

function callback(err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus): void {
  if (err !== undefined && err.code !== 0) {
    console.error(\`Callback Error, errorCode: ${err.code}\`);
    return;
  }
  console.info(\`isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}\`);
}

function registerAutoDeviceSwitchStatus(photoSession: camera.PhotoSession): void {
  photoSession.on('autoDeviceSwitchStatusChange', callback);
}
function unregisterAutoDeviceSwitchStatus(photoSession: camera.PhotoSession): void {
  photoSession.off('autoDeviceSwitchStatusChange', callback);
}

#### Complete Sample Code

import { camera } from '@kit.CameraKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { abilityAccessCtrl } from '@kit.AbilityKit';

const TAG = 'AutoSwitchCameraDemo ';

@Entry
@Component
struct Index {
  @State isShow: boolean = false;
  @State reloadXComponentFlag: boolean = false;
  private mXComponentController: XComponentController = new XComponentController();
  private mXComponentOptions: XComponentOptions = {
    type: XComponentType.SURFACE,
    controller: this.mXComponentController
  }
  private mSurfaceId: string = '';
  private mCameraPosition: camera.CameraPosition = camera.CameraPosition.CAMERA\_POSITION\_BACK;
  private mCameraManager: camera.CameraManager | undefined = undefined;
  private curCameraDevice: camera.CameraDevice | undefined = undefined;
  private mCameraInput: camera.CameraInput | undefined = undefined;
  private mPreviewOutput: camera.PreviewOutput | undefined = undefined;
  private mPhotoSession: camera.PhotoSession | undefined = undefined;
  // One of the recommended preview resolutions.
  private previewProfileObj: camera.Profile = {
    format: 1003,
    size: {
      width: 1920,
      height: 1080
    }
  };
  private mContext: Context | undefined = undefined;
  autoDeviceSwitchCallback: (err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus) => void =
    (err: BusinessError, autoDeviceSwitchStatus: camera.AutoDeviceSwitchStatus) => {
      if (err !== undefined && err.code !== 0) {
        console.error(\`${TAG} Callback Error, errorCode: ${err.code}\`);
        return;
      }
      console.info(\`${TAG} isDeviceSwitched: ${autoDeviceSwitchStatus.isDeviceSwitched}, isDeviceCapabilityChanged: ${autoDeviceSwitchStatus.isDeviceCapabilityChanged}\`);
  }

  requestPermissionsFn(): void {
    let atManager = abilityAccessCtrl.createAtManager();
    atManager.requestPermissionsFromUser(this.mContext, \[
      'ohos.permission.CAMERA'
    \]).then((): void => {
      this.isShow = true;
    }).catch((error: BusinessError): void => {
      console.error(TAG + \`ohos.permission.CAMERA no permission, error: ${error.code}\`);
    });
  }

  initContext(): void {
    let uiContext = this.getUIContext();
    this.mContext = uiContext.getHostContext();
  }

  initCameraManager(): void {
    try {
      this.mCameraManager = camera.getCameraManager(this.mContext);
    } catch (error) {
      let err = error as BusinessError;
      console.error(\`getCameraManager failed, error: ${err.code}\`);
    }
  }

  aboutToAppear(): void {
    console.info(TAG + 'aboutToAppear is called');
    this.initContext();
    this.requestPermissionsFn();
    this.initCameraManager();
  }

  async aboutToDisappear(): Promise<void> {
    await this.releaseCamera();
  }

  async onPageShow(): Promise<void> {
    await this.initCamera(this.mSurfaceId, this.mCameraPosition);
  }

  async releaseCamera(): Promise<void> {
    // Stop the session.
    try {
      await this.mPhotoSession?.stop();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to stop session, errorCode = ' + err.code);
    }

    // Release the camera input stream.
    try {
      await this.mCameraInput?.close();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to close device, errorCode = ' + err.code);
    }

    // Release the preview output stream.
    try {
      await this.mPreviewOutput?.release();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to release previewOutput, errorCode = ' + err.code);
    }

    this.mPreviewOutput = undefined;

    // Release the session.
    try {
      await this.mPhotoSession?.release();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to release photoSession, errorCode = ' + err.code);
    }

    // Set the session to null.
    this.mPhotoSession = undefined;
  }

  async loadXComponent(): Promise<void> {
    this.mSurfaceId = this.mXComponentController.getXComponentSurfaceId();
    console.info(TAG + \`mCameraPosition: ${this.mCameraPosition}\`)
    await this.initCamera(this.mSurfaceId, this.mCameraPosition);
  }

  getPreviewProfile(cameraOutputCapability: camera.CameraOutputCapability): camera.Profile | undefined {
    let previewProfiles = cameraOutputCapability.previewProfiles;
    if (previewProfiles.length < 1) {
      return undefined;
    }
    let index = previewProfiles.findIndex((previewProfile: camera.Profile) => {
      return previewProfile.size.width === this.previewProfileObj.size.width &&
        previewProfile.size.height === this.previewProfileObj.size.height &&
        previewProfile.format === this.previewProfileObj.format;
    })
    if (index === -1) {
      return undefined;
    }
    return previewProfiles\[index\];
  }

  async initCamera(surfaceId: string, cameraPosition: camera.CameraPosition,
    connectionType: camera.ConnectionType = camera.ConnectionType.CAMERA\_CONNECTION\_BUILT\_IN): Promise<void> {
    await this.releaseCamera();
    // Create a CameraManager object.
    if (!this.mCameraManager) {
      console.error(TAG + 'camera.getCameraManager error');
      return;
    }

    // Obtain the camera list.
    let cameraArray: Array<camera.CameraDevice> = this.mCameraManager.getSupportedCameras();
    if (cameraArray.length <= 0) {
      console.error(TAG + 'cameraManager.getSupportedCameras error');
      return;
    }

    for (let index = 0; index < cameraArray.length; index++) {
      console.info(TAG + 'cameraId : ' + cameraArray\[index\].cameraId); // Obtain the camera ID.
      console.info(TAG + 'cameraPosition : ' + cameraArray\[index\].cameraPosition); // Obtain the camera position.
      console.info(TAG + 'cameraType : ' + cameraArray\[index\].cameraType); // Obtain the camera type.
      console.info(TAG + 'connectionType : ' + cameraArray\[index\].connectionType); // Obtain the camera connection type.
    }

    let deviceIndex = cameraArray.findIndex((cameraDevice: camera.CameraDevice) => {
      return cameraDevice.cameraPosition === cameraPosition && cameraDevice.connectionType === connectionType;
    })
    // If no camera is found at the specified position, you can select another camera. Handle the situation based on the specific scenario.
    if (deviceIndex === -1) {
      deviceIndex = 0;
      console.error(TAG + 'not found camera');
    }
    this.curCameraDevice = cameraArray\[deviceIndex\];

    // Create a camera input stream.
    try {
      this.mCameraInput = this.mCameraManager.createCameraInput(this.curCameraDevice);
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to createCameraInput errorCode = ' + err.code);
    }
    if (this.mCameraInput === undefined) {
      return;
    }

    // Open the camera.
    try {
      await this.mCameraInput.open();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to open device, errorCode = ' + err.code);
    }

    // Obtain the supported modes.
    let sceneModes: Array<camera.SceneMode> = this.mCameraManager.getSupportedSceneModes(this.curCameraDevice);
    let isSupportPhotoMode: boolean = sceneModes.indexOf(camera.SceneMode.NORMAL\_PHOTO) >= 0;
    if (!isSupportPhotoMode) {
      console.error(TAG + 'photo mode not support');
      return;
    }

    // Obtain the output stream capability supported by the camera.
    let cameraOutputCapability: camera.CameraOutputCapability =
      this.mCameraManager.getSupportedOutputCapability(this.curCameraDevice, camera.SceneMode.NORMAL\_PHOTO);
    if (!cameraOutputCapability) {
      console.error(TAG + 'cameraManager.getSupportedOutputCapability error');
      return;
    }
    console.info(TAG + 'outputCapability: ' + JSON.stringify(cameraOutputCapability));
    let previewProfile = this.getPreviewProfile(cameraOutputCapability);
    if (previewProfile === undefined) {
      console.error(TAG + 'The resolution of the current preview stream is not supported.');
      return;
    }
    this.previewProfileObj = previewProfile;

    // Create a preview output stream. For details about the surfaceId parameter, see the XComponent. The preview stream uses the surface provided by the XComponent.
    try {
      this.mPreviewOutput = this.mCameraManager.createPreviewOutput(this.previewProfileObj, surfaceId);
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + \`Failed to create the PreviewOutput instance. error code: ${err.code}\`);
    }
    if (this.mPreviewOutput === undefined) {
      return;
    }

    // Create a session.
    try {
      this.mPhotoSession = this.mCameraManager.createSession(camera.SceneMode.NORMAL\_PHOTO) as camera.PhotoSession;
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to create the session instance. errorCode = ' + err.code);
    }
    if (this.mPhotoSession === undefined) {
      return;
    }
    if (this.mPhotoSession.isAutoDeviceSwitchSupported()) {
      this.mPhotoSession.enableAutoDeviceSwitch(true);
      this.mPhotoSession.on('autoDeviceSwitchStatusChange', this.autoDeviceSwitchCallback);
    }
    // Start configuration for the session.
    try {
      this.mPhotoSession.beginConfig();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to beginConfig. errorCode = ' + err.code);
    }

    // Add the camera input stream to the session.
    try {
      this.mPhotoSession.addInput(this.mCameraInput);
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to addInput. errorCode = ' + err.code);
    }

    // Add the preview output stream to the session.
    try {
      this.mPhotoSession.addOutput(this.mPreviewOutput);
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to addOutput(previewOutput). errorCode = ' + err.code);
    }

    // Commit the session configuration.
    try {
      await this.mPhotoSession.commitConfig();
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to commit session configuration, errorCode = ' + err.code);
    }

    // Start the session.
    try {
      await this.mPhotoSession.start()
    } catch (error) {
      let err = error as BusinessError;
      console.error(TAG + 'Failed to start session. errorCode = ' + err.code);
    }
  }

  build() {
    if (this.isShow) {
      Stack() {
        XComponent(this.mXComponentOptions)
          .onLoad(async () => {
            await this.loadXComponent();
          })
          .width(this.getUIContext().px2vp(1080))
          .height(this.getUIContext().px2vp(1920))
        Text('Switch camera')
          .size({ width: 80, height: 48 })
          .position({ x: 1, y: 1 })
          .backgroundColor(Color.White)
          .textAlign(TextAlign.Center)
          .borderRadius(24)
          .onClick(async () => {
            this.mCameraPosition = this.mCameraPosition === camera.CameraPosition.CAMERA\_POSITION\_BACK ?
            camera.CameraPosition.CAMERA\_POSITION\_FRONT : camera.CameraPosition.CAMERA\_POSITION\_BACK;
            await this.loadXComponent();
          })
      }
      .size({ width: '100%', height: '100%' })
      .backgroundColor(Color.Black)
    }
  }
}
