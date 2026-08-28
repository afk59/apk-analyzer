# What can I do if a black screen is displayed without any error information during preview?

**Possible Causes**

-   Operations such as initializing the camera and obtaining the camera input stream are performed before the camera permission is obtained.
-   After the application is switched to the background and then switched back, the camera resources are reclaimed, but the permission is not requested again. Consequently, the preview fails to start.
-   The preview stream size is not supported.

**Solution**

-   Ensure that the camera permission is correctly obtained before the camera is initialized and the camera input stream is obtained.
    1.  Declare the required permissions in the module.json5 file (the geolocation permission can be applied for as required and is optional).
        
        "requestPermissions": \[
          {
            "name": "ohos.permission.CAMERA",
            "usedScene": {
              "abilities": \[
                "FormAbility"
              \],
              "when": "always"
            },
            "reason": "$string:Camera\_Permission\_Request"
          },
          {
            "name": "ohos.permission.MICROPHONE",
            "usedScene": {
              "abilities": \[
                "FormAbility"
              \],
              "when": "always"
            },
            "reason": "$string:Camera\_Permission\_Request"
          },
          {
            "name": "ohos.permission.WRITE\_MEDIA",
            "usedScene": {
              "abilities": \[
                "FormAbility"
              \],
              "when": "always"
            },
            "reason": "$string:Camera\_Permission\_Request"
          },
          {
            "name": "ohos.permission.READ\_MEDIA",
            "usedScene": {
              "abilities": \[
                "FormAbility"
              \],
              "when": "always"
            },
            "reason": "$string:Camera\_Permission\_Request"
          },
          // The geographical location permission can be applied for as required. This parameter is optional.
          {
            "name": "ohos.permission.MEDIA\_LOCATION",
            "usedScene": {
            "abilities": \[
                "FormAbility"
            \],
            "when": "always"
            },
            "reason": "$string:Camera\_Permission\_Request"
          }
        \],
        
    2.  Use [requestPermissionsFromUser](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9) in **onWindowStageCreate** of **EntryAbility.ets** to request the permission.
        
        onWindowStageCreate(windowStage: window.WindowStage): void {
          let atManager = abilityAccessCtrl.createAtManager();
          atManager.requestPermissionsFromUser(this.context,
            \[
              'ohos.permission.CAMERA',
              'ohos.permission.MICROPHONE',
              'ohos.permission.MEDIA\_LOCATION',
              'ohos.permission.READ\_MEDIA',
              'ohos.permission.WRITE\_MEDIA'
            \]
          ).then((data) => {
            console.info('data:' + JSON.stringify(data));
            console.info('data permissions:' + data.permissions);
            console.info('data authResults:' + data.authResults);
            // Main window is created, set main page for this ability
            hilog.info(0x0000, 'testTag', '%{public}s', 'Ability onWindowStageCreate');
        
            windowStage.loadContent('pages/CameraPreviewFlow', (err, data) => {
              if (err.code) {
                hilog.error(0x0000, 'testTag', 'Failed to load the content. Cause: %{public}s', JSON.stringify(err) ?? '');
                return;
              }
              hilog.info(0x0000, 'testTag', 'Succeeded in loading the content. Data: %{public}s', JSON.stringify(data) ?? '');
            });
          }).catch((err: BusinessError) => {
            console.info('data:' + JSON.stringify(err));
          });
        }
        
-   After the application is switched to the background, all camera resources are reclaimed. To avoid black screen of the preview stream during the switchover between the foreground and background, you must re-create a session, configure the session, and start the camera in **onPageShow**. In addition, release the camera resources in **onPageHide**.
    
    async onPageShow() {
      let baseContext = this.getUIContext().getHostContext()! as common.BaseContext;
      await this.initCamera(baseContext, this.surfaceId);
    }
    
    async onPageHide() {
      await this.releaseCamera();
    }
    
-   You can obtain the output stream capabilities supported by the camera to determine the supported preview sizes.
    
    // Obtain the output stream capability supported by the camera device
    let cameraOutputCap: camera.CameraOutputCapability =
      cameraManager.getSupportedOutputCapability(cameraArray\[0\], camera.SceneMode.NORMAL\_PHOTO);
    if (!cameraOutputCap) {
      console.error(TAG, "cameraManager.getSupportedOutputCapability error");
      return;
    }
    console.info(TAG, "outputCapability: " +
    JSON.stringify(cameraOutputCap));  //The aspect ratio of the preview stream and the video output stream resolution should be consistent
    let previewProfilesArray: Array<camera.Profile> = cameraOutputCap.previewProfiles;
    let position: number = 0;
    if (previewProfilesArray != null) {
      previewProfilesArray.forEach((value: camera.Profile,
        index: number) => { // View supported preview sizes
        console.info(TAG,
          \`Supported preview sizes: \[${value.size.width},${value.size.height},${value.size.width / value.size.height}\]\`);
        if (value.size.width === 2592 && value.size.height === 1200) {
          position = index;
        }
      })
    } else {
      console.error(TAG, "createOutput photoProfilesArray == null || undefined");
    }
