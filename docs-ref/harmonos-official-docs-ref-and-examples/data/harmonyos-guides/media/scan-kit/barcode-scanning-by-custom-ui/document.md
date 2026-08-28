# Barcode Scanning by Custom UI

#### Overview

The capability of scanning barcodes using the custom UI provides APIs for controlling camera streams. You can customize the scanning UI for your app as needed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/OV7MEmvYRMSERxeJP8uACg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EB294284B9B0033CE248D07C24127B1BDEB258D6A5C47606E5DB964A21B31A04)

By using the capability of barcode scanning by custom UI, you can achieve the in-app code scanning function. To enhance user experience, you are also advised to [integrate the scan-to-access capability](../scan-to-access-capability/document.md) so your users can directly go to a specified service page in your app by scanning a barcode via either the code scanning entry on Control Panel or the in-app code scanning entry.

#### Use Cases

This capability provides the following functions: 1. Call the camera stream control API that can initialize, enable, pause, and release camera streams, as well as scan a barcode again. 2. Obtain the flash light status and turn on or off the flash light. 3. Set the focal point and continuous auto-focus for the camera. 4. Scan 1D codes, 2D codes, and multifunctional codes (for details about specific types, please refer to [ScanType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scancore#section113371139123212)) and obtain information including the type, value, and camera preview stream (YUV) of the codes. This capability can be used to scan one or multiple barcodes.

You can integrate this capability to customize the barcode scanning UI, and call the barcode scanning API to implement real-time barcode scanning based on the service process.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/7JikE1tER-aaHIK6lUs4Aw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EBFE05682A444126313AAE86760EE46DC4B4A7C6415D02A8BE5DDF82DC9E52F3)

For comprehensive scenarios that may include barcode scanning and object recognition, you need to control camera streams by yourself. However, for scenarios that involve only barcode scanning, this level of control is not necessary.

#### Restrictions

-   The camera permission is required for using this capability.
-   You need to develop the UI for barcode scanning by yourself. For example, in the scenario of scanning multiple barcodes, your app needs to stop camera streams and ask the user to choose a barcode.

#### Flowchart

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/mQ57tBRoQwqzfD6uG6rUCw/en-us_image_0000002486545968.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F60837B8EE175524DDDD97915BA0855E269CE399A9B6B391500FA28F6D2FB94E "Click to enlarge")

1.  **Initiate request**: A user sends a barcode scanning request to your app, and your defined scanning page is displayed.
2.  **Apply for permission**: Your app requests the camera permission from the user. If the permission is not granted, the barcode scanning function will be unavailable.
3.  **Open custom UI to start barcode scanning**: Your app calls the **init** API to initialize your custom scanning page and load required resources. Then your app calls the **start** API to start scanning.
4.  **Operate camera on custom UI**: Your scanning page allows the user to operate camera functions, including adjusting the flash light, zoom ratio, and focal length, and scanning a barcode again. Specific examples are as follows:
    -   Your app obtains the distance to the barcode image. If the image is too far or too close, your app can call the **getZoom** API to obtain the zoom ratio and call the **setZoom** API to set zoom ratio so as to adjust the focal length for scanning.
    -   Your app obtains the light conditions or calls **on('lightingFlash')** to obtain the flash turn-on time to determine whether to turn on or off the flash light, and then calls **getFlashLightStatus** to obtain the flash light status. Based on the obtained information, your app calls **openFlashLight** or **closeFlashLight** to turn on or off the flash light as needed to facilitate barcode scanning.
    -   Your app can call **setFocusPoint** to set the focus position and call **resetFocus** to restore the default focus mode as needed to facilitate barcode scanning.
    -   Your app calls the **stop** or **start** API to control camera streams to stop or restart barcode scanning as needed when your app is running in the foreground or background or in other special scenarios.
5.  **Scan barcode using custom UI**: Scan Kit returns the result after barcode scanning. It can also return the camera preview data stream of each frame as required. If your scanning page needs to trigger scanning again without restarting the camera, call the **rescan** API in the asynchronous callback of the **start** API. Your app calls the **release** API to release barcode scanning resources.
6.  **Obtain the result**: The app shows the target service page based on the parsing result to the user.

#### API Description

Barcode scanning by custom UI provides the **init**, **start**, **stop**, **release**, **getFlashLightStatus**, **openFlashLight**, **closeFlashLight**, **setZoom**, **getZoom**, **setFocusPoint**, **resetFocus**, **rescan**, **on('lightingFlash')**, and **off('lightingFlash')** APIs. Some of these APIs use either a callback or promise to return the result. The APIs that use a callback provide the same functions as their counterparts that use a promise. For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section447114223245)(options?: scanBarcode.[ScanOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section1285191073117)): void

 | 

Initializes the custom barcode scanning UI to load resources. No result is returned.

 |
| 

[start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section38711535114711)(viewControl: [ViewControl](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section8604949165313)): Promise<Array<scanBarcode.[ScanResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section10614317162112)\>>

 | 

Starts barcode scanning camera streams. This API uses a promise to return the scanning result asynchronously.

 |
| 

[stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section6949611114915)(): Promise<void>

 | 

Stops barcode scanning camera streams. This API uses a promise to return the result asynchronously.

 |
| 

[release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1109456134917)(): Promise<void>

 | 

Releases barcode scanning camera streams. This API uses a promise to return the result asynchronously.

 |
| 

[start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section747366165913)(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<[ScanFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1670633211200)\>): void

 | 

Starts barcode scanning camera streams. This API uses a callback to return the scanning result and YUV image data asynchronously.

 |
| 

[getFlashLightStatus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1693117333508)(): boolean

 | 

Obtains the flash light status. The return value is of the Boolean type. The value **true** indicates that the flash light is enabled, and the value **false** indicates that the flash light is disabled.

 |
| 

[openFlashLight](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section75901948175116)(): void

 | 

Turns on the flash light. No result is returned.

 |
| 

[closeFlashLight](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section17980725135120)(): void

 | 

Turns off the flash light. No result is returned.

 |
| 

[setZoom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section070810389567)(zoomValue : number): void

 | 

Sets a zoom ratio for the device. No result is returned.

 |
| 

[getZoom](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1699185032017)(): number

 | 

Obtains the zoom ratio in use.

 |
| 

[setFocusPoint](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section288962116197)(point: scanBarcode.[Point](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section9634457911)): void

 | 

Sets the camera focus.

 |
| 

[resetFocus](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section12891152115196)(): void

 | 

Sets the focus mode to continuous auto-focus.

 |
| 

[rescan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section19244173211169)(): void

 | 

Initiates barcode scanning again. This API applies only when the **start** API uses a callback to return the result.

 |
| 

[stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section031674815483)(callback: AsyncCallback<void>): void

 | 

Stops barcode scanning camera streams. This API uses a callback to return the result asynchronously.

 |
| 

[release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section169321832184912)(callback: AsyncCallback<void>): void

 | 

Releases barcode scanning camera streams. This API uses a callback to return the result asynchronously.

 |
| 

[on](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1788353253914)(type: 'lightingFlash', callback: AsyncCallback<boolean>): void

 | 

Subscribes to the flash light status listener. This API uses a callback to return the flash light turn-on or turn-off time asynchronously when the light conditions change.

 |
| 

[off](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section128574416409)(type: 'lightingFlash', callback?: AsyncCallback<boolean>): void

 | 

Unsubscribes from the flash light status listener.

 |

#### Development Procedure

You can customize the barcode scanning UI for your app. Then, the custom UI can be used to scan 1D codes, multifunctional codes, and 2D codes to obtain the barcode value, type, position information (coordinates of the upper left and lower right corners of the minimum bounding rectangle of the barcode image), and camera preview stream (YUV).

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

The following describes how to use the function of barcode scanning by custom UI to start camera streams and obtain the barcode scanning result and camera preview stream (YUV).

1.  Request the camera permission for your app. [Configure the camera permission](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) in the **module.json5** file.
    
    | 
    Permission
    
     | 
    
    Description
    
     | 
    
    Authorization Method
    
     |
    | :-- | :-- | :-- |
    | 
    
    ohos.permission.CAMERA
    
     | 
    
    Allows an app to use the camera to scan barcodes.
    
     | 
    
    user\_grant
    
     |
    
2.  Call the [requestPermissionsFromUser](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-abilityaccessctrl#requestpermissionsfromuser9-1) API to request user authorization. For details about how to request and verify the permissions, please refer to [Requesting User Authorization](../../../system/security/application-access-control/application-permission-management/requesting-application-permissions/requesting-user-authorization/document.md).
3.  Import APIs for barcode scanning using the custom UI and other relevant APIs.
    
    import { scanCore, scanBarcode, customScan } from '@kit.ScanKit';
    // Import the required permission application and callback APIs.
    import { display } from '@kit.ArkUI';
    import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { common, abilityAccessCtrl, PermissionRequestResult } from '@kit.AbilityKit';
    
4.  Follow [Flowchart](#section52491649171418) to implement barcode scanning by custom UI.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1f/v3/NXhQPbXARr29Zl9DUdNEZA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A40C4FBD9CB3C8DD2875A4E01C01BD9C0C097ECB305C01A454E4013E7331AD49)
    
    1.  When setting **viewControl** parameters of the **start** API, ensure that the values of **width** and **height** are the same as those of [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent). The **start** API will select the optimal resolution out of camera resolutions based on the ratio between the width and height of XComponent. If the ratio differs from the camera resolution ratio greatly, the preview stream experience may be compromised.
        
        Currently, the supported resolution ratios are 16:9, 4:3, and 1:1. In portrait mode, the height of XComponent must be greater than its width, and the ratio between the height and width must be one of the supported resolution ratios. In landscape mode, the width of XComponent must be greater than the height, and the ratio between the width and height must be one of the supported resolution ratios.
        
    2.  The width and height of XComponent need to be adapted for specific scenarios. For example, for foldable devices, you need to adjust the width and height of XComponent as needed when the folding status changes. The **start** API will adapt the camera resolution ratio based on the width and height of XComponent. You can call the [display.getDefaultDisplaySync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#displaygetdefaultdisplaysync9) method to obtain the width and height of the device screen. The unit of the obtained values is px and needs to be converted to vp through the [px2vp](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-uicontext-uicontext#px2vp12) method.
    
    -   Call relevant APIs of barcode scanning by custom UI to start camera streams and obtain the barcode scanning result using a promise.
        
        const TAG: string = '\[customScanPage\]';
        
        @Entry
        @Component
        struct CustomScanPage {
          @State userGrant: boolean = false // Whether the camera permission has been requested.
          @State surfaceId: string = '' // ID generated by XComponent.
          @State isShowBack: boolean = false // Whether the scanning result has been returned.
          @State isFlashLightEnable: boolean = false // Whether the flash light has been turned on.
          @State isSensorLight: boolean = false // Light conditions in the current environment.
          @State cameraHeight: number = 640 // Preview stream height. The default unit is vp.
          @State cameraWidth: number = 360 // Preview stream width. The default unit is vp.
          @State offsetX: number = 0 // X-axis offset of the preview stream. The default unit is vp.
          @State offsetY: number = 0 // Y-axis offset of the preview stream. The default unit is vp.
          @State zoomValue: number = 1 // Preview stream zoom ratio.
          @State setZoomValue: number = 1 // Preview stream zoom ratio that is set.
          @State scaleValue: number = 1 // Screen zoom ratio.
          @State pinchValue: number = 1 // Two-finger zoom ratio.
          @State displayHeight: number = 0 // Screen height, in vp.
          @State displayWidth: number = 0 // Screen width, in vp.
          @State scanResult: Array<scanBarcode.ScanResult> = \[\] // Scanning result.
          private mXComponentController: XComponentController = new XComponentController()
        
          async onPageShow() {
            // Step 1: Request required permissions from the user.
            await this.requestCameraPermission();
            // Set enableMultiMode to true for scanning multiple barcodes at a time and set it to false for scanning only one barcode at a time.
            let options: scanBarcode.ScanOptions = {
              scanTypes: \[scanCore.ScanType.ALL\],
              enableMultiMode: true,
              enableAlbum: true
            }
            // Step 2: Set the image size of the camera preview stream.
            this.setDisplay();
            try {
              // Step 3: Call the initialization API.
              customScan.init(options);
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to init customScan. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        
          onPageHide() {
            // Stop and release camera streams when the scanning UI disappears or is hidden.
            this.userGrant = false;
            this.isFlashLightEnable = false;
            this.isSensorLight = false;
            try {
              customScan.off('lightingFlash');
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to off lightingFlash. Code: ${error.code}, message: ${error.message}\`);
            }
            this.customScanStop();
            try {
              // Customize the API for releasing camera streams.
              customScan.release().catch((error: BusinessError) => {
                hilog.error(0x0001, TAG,
                  \`Failed to release customScan by promise. Code: ${error.code}, message: ${error.message}\`);
              })
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to release customScan. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        
          // Apply for required permissions from the user.
          async reqPermissionsFromUser(): Promise<number\[\]> {
            hilog.info(0x0001, TAG, 'reqPermissionsFromUser start');
            let context = this.getUIContext().getHostContext() as common.UIAbilityContext;
            let atManager = abilityAccessCtrl.createAtManager();    
            try {
              const grantStatus: PermissionRequestResult =
                await atManager.requestPermissionsFromUser(context, \['ohos.permission.CAMERA'\]);
              return grantStatus.authResults;
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to requestPermissionsFromUser. Code: ${error.code}, message: ${error.message}\`);
              return \[\];
            }
          }
        
          // Apply for the camera permission.
          async requestCameraPermission() {
            let grantStatus = await this.reqPermissionsFromUser();
            for (let i = 0; i < grantStatus.length; i++) {
              if (grantStatus\[i\] === 0) {
                // The user has granted the permission, and your app can continue barcode scanning.
                hilog.info(0x0001, TAG, 'Succeeded in getting permissions.');
                this.userGrant = true;
                break;
              }
            }
          }
        
          // Obtain the screen size when the device is in portrait mode and set the width and height of the preview stream in full screen mode.
          setDisplay() {
            try {
              // The portrait mode is used by default.
              let displayClass = display.getDefaultDisplaySync();
              this.displayHeight = this.getUIContext().px2vp(displayClass.height);
              this.displayWidth = this.getUIContext().px2vp(displayClass.width);
              let maxLen: number = Math.max(this.displayWidth, this.displayHeight);
              let minLen: number = Math.min(this.displayWidth, this.displayHeight);
              const RATIO: number = 16 / 9;
              this.cameraHeight = maxLen;
              this.cameraWidth = maxLen / RATIO;
              this.offsetX = (minLen - this.cameraWidth) / 2;
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to getDefaultDisplaySync. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        
          // Display the scanning result using a toast.
          showScanResult(result: scanBarcode.ScanResult) {
            try {
              // Display the scanning result using a toast.
              this.getUIContext().getPromptAction().showToast({
                message: JSON.stringify(result),
                duration: 5000
              });
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to showToast. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        
          initCamera() {
            this.isShowBack = false;
            this.scanResult = \[\];
            let viewControl: customScan.ViewControl = {
              width: this.cameraWidth,
              height: this.cameraHeight,
              surfaceId: this.surfaceId
            };
            try {
              // Step 4: Call the scan API to return the scanning result using a promise.
              customScan.start(viewControl)
                .then((result: Array<scanBarcode.ScanResult>) => {
                  hilog.info(0x0001, TAG, \`result: ${JSON.stringify(result)}\`);
                  if (result.length) {
                    // Parse the code value and open the specified app service page.
                    this.scanResult = result;
                    this.isShowBack = true;
                    // Stop camera streams after obtaining the scanning result.
                    this.customScanStop();
                  }
                }).catch((error: BusinessError) => {
                hilog.error(0x0001, TAG, \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
              });
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        
          customScanStop() {
            try {
              customScan.stop().catch((error: BusinessError) => {
                hilog.error(0x0001, TAG, \`Failed to stop customScan. Code: ${error.code}, message: ${error.message}\`);
              })
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to stop customScan. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        
          // Customize the back button and scanning prompt on the top of the scanning UI.
          @Builder
          TopTool() {
            Column() {
              Flex({ direction: FlexDirection.Row, justifyContent: FlexAlign.SpaceBetween, alignItems: ItemAlign.Center }) {
                Text('Back')
                  .onClick(() => {
                    this.getUIContext().getRouter().back();
                  })
              }.padding({ left: 24, right: 24, top: 40 })
        
        
              Column() {
                Text('Scan 2D Code/1D Code')
                Text('Point the camera to the 2D code/1D code to scan it.')
              }.margin({ left: 24, right: 24, top: 24 })
            }
            .height(146)
            .width('100%')
          }
        
          build() {
            Stack() {
              if (this.userGrant) {
                Column() {
                  XComponent({
                    id: 'componentId',
                    type: XComponentType.SURFACE,
                    controller: this.mXComponentController
                  })
                    .onLoad(() => {
                      hilog.info(0x0001, TAG, 'Succeeded in loading, onLoad is called.');
                      // Obtain surfaceId of XComponent.
                      this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
                      hilog.info(0x0001, TAG, \`Succeeded in getting surfaceId: ${this.surfaceId}\`);
                      this.initCamera();
                      // Call the flash light listening API.
                      customScan.on('lightingFlash', (error, isLightingFlash) => {
                        if (error) {
                          hilog.error(0x0001, TAG,
                            \`Failed to on lightingFlash. Code: ${error.code}, message: ${error.message}\`);
                          return;
                        }
                        if (isLightingFlash) {
                          this.isFlashLightEnable = true;
                        } else {
                          try {
                            if (!customScan.getFlashLightStatus()) {
                              this.isFlashLightEnable = false;
                            }
                          } catch (error) {
                            hilog.error(0x0001, TAG,
                              \`Failed to get flashLightStatus. Code: ${error.code}, message: ${error.message}\`);
                          }
                        }
                        this.isSensorLight = isLightingFlash;
                      });
                    })
                    .width(this.cameraWidth)
                    .height(this.cameraHeight)
                    .position({ x: this.offsetX, y: this.offsetY })
                }
                .height('100%')
                .width('100%')
              }
        
        
              Column() {
                this.TopTool()
                Column() {
                }
                .layoutWeight(1)
                .width('100%')
        
        
                Column() {
                  Row() {
                    // Flash light button, which is available only after camera streams are started.
                    Button('FlashLight')
                      .onClick(() => {
                        let lightStatus: boolean = false;
                        try {
                          lightStatus = customScan.getFlashLightStatus();
                        } catch (error) {
                          hilog.error(0x0001, TAG,
                            \`Failed to get flashLightStatus. Code: ${error.code}, message: ${error.message}\`);
                        }
        
        
                        // Turn on or off the flash light based on the flash light status.
                        if (lightStatus) {
                          try {
                            customScan.closeFlashLight();
                            setTimeout(() => {
                              this.isFlashLightEnable = this.isSensorLight;
                            }, 200);
                          } catch (error) {
                            hilog.error(0x0001, TAG,
                              \`Failed to close flashLight. Code: ${error.code}, message: ${error.message}\`);
                          }
                        } else {
                          try {
                            customScan.openFlashLight();
                          } catch (error) {
                            hilog.error(0x0001, TAG,
                              \`Failed to open flashLight. Code: ${error.code}, message: ${error.message}\`);
                          }
                        }
                      })
                      .visibility((this.userGrant && this.isFlashLightEnable) ? Visibility.Visible : Visibility.None)
        
        
                    // After scanning is successful, a user can tap the button to scan again.
                    Button('Scan')
                      .onClick(() => {
                        // Restart camera streams to scan the barcode again.
                        this.initCamera();
                      })
                      .visibility(this.isShowBack ? Visibility.Visible : Visibility.None)
                  }
        
        
                  Row() {
                    // Set the preview stream zoom ratio.
                    Button('Zoom ratio,Current ratio:' + this.setZoomValue)
                      .onClick(() => {
                        // Set the camera zoom ratio.
                        if (!this.isShowBack) {
                          if (!this.zoomValue || this.zoomValue === this.setZoomValue) {
                            this.setZoomValue = this.customGetZoom();
                          } else {
                            this.zoomValue = this.zoomValue;
                            this.customSetZoom(this.zoomValue);
                            setTimeout(() => {
                              if (!this.isShowBack) {
                                this.setZoomValue = this.customGetZoom();
                              }
                            }, 1000);
                          }
                        }
                      })
                  }
                  .margin({ top: 10, bottom: 10 })
        
        
                  Row() {
                    // Input the preview stream zoom ratio to be set.
                    TextInput({ placeholder: 'Input zoom ratio' })
                      .type(InputType.Number)
                      .borderWidth(1)
                      .backgroundColor(Color.White)
                      .onChange(value => {
                        this.zoomValue = Number(value);
                      })
                  }
                }
                .width('50%')
                .height(180)
              }
        
        
              // After single-code or multi-code scanning, display the radio button position of the barcode image. After the user taps the radio button, a toast containing barcode image information is displayed.
              ForEach(this.scanResult, (item: scanBarcode.ScanResult) => {
                if (item.scanCodeRect) {
                  Image($rawfile('scan\_selected2.svg')) // src/main/resources/rawfile/scan\_selected2.svg
                    .width(40)
                    .height(40)
                    .markAnchor({ x: 20, y: 20 })
                    .position({
                      x: (item.scanCodeRect.left + item?.scanCodeRect?.right) / 2 + this.offsetX,
                      y: (item.scanCodeRect.top + item?.scanCodeRect?.bottom) / 2 + this.offsetY
                    })
                    .onClick(() => {
                      this.showScanResult(item);
                    })
                }
              }, (item: scanBarcode.ScanResult) => '' + item?.scanCodeRect?.left + item?.scanCodeRect?.right + 'px')
            }
            // You are advised to set camera streams to the full screen mode.
            .width('100%')
            .height('100%')
            .onClick((event: ClickEvent) => {
              // Whether the scanning result has been obtained.
              if (this.isShowBack) {
                return;
              }
              // When the user taps on the screen, obtain the tap position coordinates (x,y) and set the camera focus.
              let x1 = this.getUIContext().vp2px(event.displayY) / (this.displayHeight + 0.0);
              let y1 = 1.0 - (this.getUIContext().vp2px(event.displayX) / (this.displayWidth + 0.0));
              try {
                customScan.setFocusPoint({ x: x1, y: y1 });
                hilog.info(0x0001, TAG, \`Succeeded in setting focusPoint x1: ${x1}, y1: ${y1}\`);
              } catch (error) {
                hilog.error(0x0001, TAG, \`Failed to set focusPoint. Code: ${error.code}, message: ${error.message}\`);
              }
              hilog.info(0x0001, TAG, \`Succeeded in setting focusPoint x1: ${x1}, y1: ${y1}\`);
              // Set the focus mode to continuous auto-focus.
              setTimeout(() => {
                try {
                  customScan.resetFocus();
                } catch (error) {
                  hilog.error(0x0001, TAG, \`Failed to reset focus. Code: ${error.code}, message: ${error.message}\`);
                }
              }, 200);
            }).gesture(PinchGesture({ fingers: 2 })
              .onActionStart(() => {
                hilog.info(0x0001, TAG, 'Pinch start');
              })
              .onActionUpdate((event: GestureEvent) => {
                if (event) {
                  this.scaleValue = event.scale;
                }
              })
              .onActionEnd(() => {
                // Whether the scanning result has been obtained.
                if (this.isShowBack) {
                  return;
                }
                // Obtain the two-finger zoom ratio and set the zoom ratio.
                try {
                  let zoom = this.customGetZoom();
                  this.pinchValue = this.scaleValue \* zoom;
                  this.customSetZoom(this.pinchValue);
                  hilog.info(0x0001, TAG, 'Pinch end');
                } catch (error) {
                  hilog.error(0x0001, TAG, \`Failed to set zoom. Code: ${error.code}, message: ${error.message}\`);
                }
              }))
          }
        
          public customGetZoom(): number {
            let zoom = 1;
            try {
              zoom = customScan.getZoom();
              hilog.info(0x0001, TAG, \`Succeeded in getting zoom, zoom: ${zoom}\`);
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to get zoom. Code: ${error.code}, message: ${error?.message}\`);
            }
            return zoom;
          }
        
          public customSetZoom(pinchValue: number): void {
            try {
              customScan.setZoom(pinchValue);
              hilog.info(0x0001, TAG, \`Succeeded in setting zoom.\`);
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to set zoom. Code: ${error.code}, message: ${error?.message}\`);
            }
          }
        }
        
    -   Use the function of barcode scanning by custom UI to start camera streams and obtain the barcode scanning result and camera preview stream (YUV) using a callback.
        
        import { bundleManager, Permissions } from '@kit.AbilityKit';
        
        const TAG = '\[YUV CPSample\]';
        
        // Apply for required permissions from the user.
        export class PermissionsUtil {
          public static async checkAccessToken(permission: Permissions): Promise<abilityAccessCtrl.GrantStatus> {
            let atManager = abilityAccessCtrl.createAtManager();
            let grantStatus: abilityAccessCtrl.GrantStatus = -1;
            // Obtain accessTokenID of the app.
            let tokenId: number = 0;    
            try {
              let bundleInfo: bundleManager.BundleInfo =
                await bundleManager.getBundleInfoForSelf(bundleManager.BundleFlag.GET\_BUNDLE\_INFO\_WITH\_APPLICATION);
              let appInfo: bundleManager.ApplicationInfo = bundleInfo.appInfo;
              tokenId = appInfo.accessTokenId;
            // Check whether the app has granted the required permission.
              grantStatus = await atManager.checkAccessToken(tokenId, permission);
            } catch (error) {
              hilog.error(0x0001, TAG,
               \`Failed to getBundleInfoForSelf or checkAccessToken. Code: ${error.code}, message: ${error.message}\`);
            }
            return grantStatus;
          }
        
        
          // Apply for the camera permission.
          public static async reqPermissionsFromUser(context: Context): Promise<number\[\]> {
            hilog.info(0x0001, TAG, 'Succeeded in getting permissions by promise.')
            let atManager = abilityAccessCtrl.createAtManager();    
            try {
              const grantStatus: PermissionRequestResult =
                await atManager.requestPermissionsFromUser(context, \['ohos.permission.CAMERA'\]);
              return grantStatus.authResults;
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to requestPermissionsFromUser. Code: ${error.code}, message: ${error.message}\`);
              return \[\];
            }
          }
        }
        
        
        @Extend(Column)
        function mainStyle() {
          .width('100%')
          .height('100%')
          .padding({
            top: 40
          })
          .justifyContent(FlexAlign.Center)
        }
        
        
        @Entry
        @Component
        struct YUVScan {
          @State userGrant: boolean = false // Whether the camera permission has been requested.
          @State surfaceId: string = '' // ID generated by XComponent.
          @State cameraHeight: number = 640 // Preview stream height. The default unit is vp.
          @State cameraWidth: number = 360 // Preview stream width. The default unit is vp.
          @State zoomValue: number = 1 // Preview stream zoom ratio.
          @State setZoomValue: number = 1 // Preview stream zoom ratio that is set.
          @State isReleaseCamera: boolean = false // Whether camera streams have been released.
          @State scanWidth: number = 384 // XComponent width. The default value is 384, in vp.
          @State scanHeight: number = 682 // XComponent height. The default value is 682, in vp.
          @State scanBottom: number = 220
          @State offsetX: number = 0 // XComponent X-axis offset, in vp.
          @State offsetY: number = 0 // XComponent Y-axis offset, in vp.
          @State scanCodeRect: Array<scanBarcode.ScanCodeRect> = \[\] // Location of the barcode image.
          @State scanFlag: boolean = false // Whether the scanning result has been obtained.
          @State scanFrameResult: string = ''
          @State scaleValue: number = 1 // Screen zoom ratio.
          @State pinchValue: number = 1 // Two-finger zoom ratio.
          @State displayHeight: number = 0 // Screen height, in vp.
          @State displayWidth: number = 0 // Screen width, in vp.
          private mXComponentController: XComponentController = new XComponentController()
          private viewControl: customScan.ViewControl = { width: 1920, height: 1080, surfaceId: this.surfaceId }
          options: scanBarcode.ScanOptions = {
            // (Optional) Scanning type.
            scanTypes: \[scanCore.ScanType.ALL\],
            // (Optional) Whether multi-code scanning has been enabled.
            enableMultiMode: true,
            // (Optional) Whether gallery-based barcode scanning has been enabled.
            enableAlbum: true,
          }
          // Return the custom scanning result in a callback.
          private callback: AsyncCallback<scanBarcode.ScanResult\[\]> =
            (error: BusinessError, result: scanBarcode.ScanResult\[\]) => {
              if (error && error.code) {
                hilog.error(0x0001, TAG,
                  \`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}\`);
                return;
              }
              // Parse the code value and open the specified app service page.
              hilog.info(0x0001, TAG, \`Succeeded in getting ScanResult by callback, result: ${JSON.stringify(result)}\`);
            }
          // Return frames in a callback.
          private frameCallback: AsyncCallback<customScan.ScanFrame> =
            (error: BusinessError, frameResult: customScan.ScanFrame) => {
              if (error) {
                hilog.error(0x0001, TAG, \`Failed to get ScanFrame by callback. Code: ${error.code}, message: ${error.message}\`);
                return;
              }
              // Camera YUV image array in byteBuffer.
              hilog.info(0x0001, TAG,
                \`Succeeded in getting ScanFrame.byteBuffer.byteLength: ${frameResult.byteBuffer.byteLength}\`)
              hilog.info(0x0001, TAG, \`Succeeded in getting ScanFrame.width: ${frameResult.width}\`)
              hilog.info(0x0001, TAG, \`Succeeded in getting ScanFrame.height: ${frameResult.height}\`)
              this.scanFrameResult = JSON.stringify(frameResult.scanCodeRects);
              if (frameResult && frameResult.scanCodeRects && frameResult.scanCodeRects.length > 0 && !this.scanFlag) {
                if (frameResult.scanCodeRects\[0\]) {
                  this.stopCamera();
                  this.scanCodeRect = \[\];
                  this.scanFlag = true;
                  // Convert the location information of the barcode image.
                  this.changeToXComponent(frameResult);
                } else {
                  this.scanFlag = false;
                }
              }
            }
        
          // Convert the location information of the landscape barcode image in **frameCallback** into the barcode image location information of XComponent for the preview stream.
          changeToXComponent(frameResult: customScan.ScanFrame) {
            if (frameResult && frameResult.scanCodeRects) {
              let frameHeight = frameResult.height;
              let ratio = this.scanWidth / frameHeight;
              frameResult.scanCodeRects.forEach((item) => {
                this.scanCodeRect.push({
                  left: this.toFixedNumber((frameHeight - item.bottom) \* ratio),
                  top: this.toFixedNumber(item.left \* ratio),
                  right: this.toFixedNumber((frameHeight - item.top) \* ratio),
                  bottom: this.toFixedNumber(item.right \* ratio)
                });
              });
              this.scanFrameResult = JSON.stringify(this.scanCodeRect);
            }
          }
        
          toFixedNumber(no: number): number {
            return Number((no).toFixed(1));
          }
        
          async onPageShow() {
            // Step 1: Request required permissions from the user.
            const permissions: Array<Permissions> = \['ohos.permission.CAMERA'\];
            // Step 2: Set the image size of the camera preview stream.
            this.setDisplay();
            let grantStatus = await PermissionsUtil.checkAccessToken(permissions\[0\]);
            if (grantStatus === abilityAccessCtrl.GrantStatus.PERMISSION\_GRANTED) {
              // The user has granted the permission, and your app can continue barcode scanning.
              this.userGrant = true;
              if (this.surfaceId) {
                // Step 3: Call the initialization API.
                this.initCamera();
              }
            } else {
              // Apply for the camera permission.
              await this.requestCameraPermission();
            }
          }
        
          async onPageHide() {
            await this.releaseCamera();
          }
        
          // Apply for required permissions from the user.
          async requestCameraPermission() {
            let grantStatus =
              await PermissionsUtil.reqPermissionsFromUser(this.getUIContext().getHostContext() as common.UIAbilityContext)
            let length: number = grantStatus.length;
            let userGrant: boolean = false; // If the user denies the permission, display a message indicating that user authorization is required, and direct the user to set the permission on the **Settings** page.
            for (let i = 0; i < length; i++) {
              if (grantStatus\[i\] === 0) {
                // The user has granted the permission, and your app can continue barcode scanning.
                userGrant = true;
              }
            }
            this.userGrant = userGrant;
          }
        
          // Obtain the screen size when the device is in portrait mode and set the width and height of the preview stream in full screen mode.
          setDisplay() {
            try {
            // Calculate the width and height using a mobile phone as an example.
              let displayClass = display.getDefaultDisplaySync();
              this.displayHeight = this.getUIContext().px2vp(displayClass.height);
              this.displayWidth = this.getUIContext().px2vp(displayClass.width);
              if (displayClass !== null) {
                this.scanWidth = this.getUIContext().px2vp(displayClass.width);
                this.scanHeight = Math.round(this.scanWidth \* this.viewControl.width / this.viewControl.height);
                this.scanBottom = Math.max(220, this.getUIContext().px2vp(displayClass.height) - this.scanHeight);
                this.offsetX = 0;
                this.offsetY = 0;
              }
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to getDefaultDisplaySync. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        
          // Initialize camera streams.
          initCamera() {
            this.isReleaseCamera = false;
            try {
              // Step 3: Call the initialization API.
              customScan.init(this.options);
              hilog.info(0x0001, TAG, 'Succeeded in initializing customScan with options.');
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to init customScan. Code: ${error.code}, message: ${error.message}\`);
            }
            this.scanCodeRect = \[\];
            this.scanFlag = false;
            try {
              // Step 4: Call the scan API.
              customScan.start(this.viewControl, this.callback, this.frameCallback);
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
            }
          }
        
          // Stop camera streams.
          stopCamera() {
            if (!this.isReleaseCamera) {
              try {
                customScan.stop().catch((error: BusinessError) => {
                  hilog.error(0x0000, TAG, \`Failed to stop customScan. Code: ${error.code}, message: ${error.message}\`);
                });
              } catch (error) {
                hilog.error(0x0001, TAG, \`Failed to stop customScan. Code: ${error.code}, message: ${error.message}\`);
              }
            }
          }
        
          // Release camera streams.
          async releaseCamera() {
            if (!this.isReleaseCamera) {
              this.stopCamera();
              try {
                await customScan.release();
              } catch (error) {
                hilog.error(0x0001, TAG, \`Failed to release customScan. Code: ${error.code}, message: ${error.message}\`);
              }
              this.isReleaseCamera = true;
            }
          }
        
          build() {
            Stack() {
              // Camera preview stream displayed in XComponent.
              if (this.userGrant) {
                Column() {
                  XComponent({
                    id: 'componentId',
                    type: XComponentType.SURFACE,
                    controller: this.mXComponentController
                  })
                    .onLoad(() => {
                      hilog.info(0x0001, TAG, 'Succeeded in loading, onLoad is called.');
                      this.surfaceId = this.mXComponentController.getXComponentSurfaceId();
                      hilog.info(0x0001, TAG, \`Succeeded in getting surfaceId is ${this.surfaceId}\`);
                      this.viewControl = { width: this.scanWidth, height: this.scanHeight, surfaceId: this.surfaceId };
                      // Start the camera to scan barcodes.
                      this.initCamera();
                    })
                    .height(this.scanHeight)
                    .width(this.scanWidth)
                    .position({ x: 0, y: 0 })
                }
                .height('100%')
                .width('100%')
                .position({ x: this.offsetX, y: this.offsetY })
              }
        
        
              Column() {
                Column() {
                }
                .layoutWeight(1)
                .width('100%')
        
        
                Column() {
        
        
                  Row() {
                    // Flash light button, which is available only after camera streams are started.
                    Button('FlashLight')
                      .onClick(() => {
                        let lightStatus: boolean = false;
                        try {
                          lightStatus = customScan.getFlashLightStatus();
                        } catch (error) {
                          hilog.error(0x0001, TAG,
                            \`Failed to get flashLightStatus. Code: ${error.code}, message: ${error.message}\`);
                        }
                        // Turn on or off the flash light based on the flash light status.
                        if (lightStatus) {
                          try {
                            customScan.closeFlashLight();
                          } catch (error) {
                            hilog.error(0x0001, TAG,
                              \`Failed to close flashLight. Code: ${error.code}, message: ${error.message}\`);
                          }
                        } else {
                          try {
                            customScan.openFlashLight();
                          } catch (error) {
                            hilog.error(0x0001, TAG,
                              \`Failed to open flashLight. Code: ${error.code}, message: ${error.message}\`);
                          }
                        }
                      })
                      .visibility(this.scanFlag ? Visibility.None : Visibility.Visible)
                  }
        
        
                  Row() {
                    // Set the preview stream zoom ratio.
                    Button('Zoom ratio,Current ratio:' + this.setZoomValue)
                      .width(200)
                      .alignSelf(ItemAlign.Center)
                      .onClick(() => {
                        // Set the camera zoom ratio.
                        if (!this.scanFlag) {
                          if (!this.zoomValue || this.zoomValue === this.setZoomValue) {
                            this.setZoomValue = this.customGetZoom();
                          } else {
                            this.zoomValue = this.zoomValue;
                            this.customSetZoom(this.zoomValue);
                            setTimeout(() => {
                              if (!this.scanFlag) {
                                this.setZoomValue = this.customGetZoom();
                              }
                            }, 1000);
                          }
                        }
                      })
                  }
                  .margin({ top: 10, bottom: 10 })
                  .visibility(this.scanFlag ? Visibility.None : Visibility.Visible)
        
        
                  Row() {
                    // Input the preview stream zoom ratio to be set.
                    TextInput({ placeholder: 'Input zoom ratio' })
                      .width(200)
                      .type(InputType.Number)
                      .borderWidth(1)
                      .backgroundColor(Color.White)
                      .onChange(value => {
                        this.zoomValue = Number(value);
                      })
                  }
                  .visibility(this.scanFlag ? Visibility.None : Visibility.Visible)
        
        
                  Text(this.scanFlag ? 'Continue' : 'Scanning')
                    .height(30)
                    .fontSize(16)
                    .fontColor(Color.White)
                    .onClick(() => {
                      if (this.scanFlag) {
                        this.scanFrameResult = '';
                        this.initCamera();
                      }
                    })
                  Text('Result:' + this.scanFrameResult).fontColor(Color.White).fontSize(12)
                }
                .width('100%')
                .height(this.scanBottom)
                .backgroundColor(Color.Black)
              }
              .mainStyle()
        
        
              Image($rawfile('scan\_back.svg')) // src/main/resources/rawfile/scan\_back.svg
                .width(20)
                .height(20)
                .position({
                  x: 40,
                  y: 40
                })
                .onClick(() => {
                  this.getUIContext().getRouter().back();
                })
        
        
              // Center point of the barcode image that is being scanned in real time.
              if (this.scanFlag && this.scanCodeRect.length > 0) {
                ForEach(this.scanCodeRect, (item: scanBarcode.ScanCodeRect) => {
                  Image($rawfile('scan\_selected2.svg')) // src/main/resources/rawfile/scan\_selected2.svg
                    .width(40)
                    .height(40)
                    .markAnchor({ x: 20, y: 20 })
                    .position({
                      x: (item.left + item.right) / 2 + this.offsetX,
                      y: (item.top + item.bottom) / 2 + this.offsetY
                    })
                }, (item: scanBarcode.ScanCodeRect) => '' + item.left + item.right)
              }
            }
            .width('100%')
            .height('100%')
            .backgroundColor(this.userGrant ? Color.Transparent : Color.Black)
            .onClick((event: ClickEvent) => {
              // Whether the scanning result has been obtained.
              if (this.scanFlag) {
                return;
              }
              // When the user taps on the screen, obtain the tap position coordinates (x,y) and set the camera focus.
              let x1 = this.getUIContext().vp2px(event.displayY) / (this.displayHeight + 0.0);
              let y1 = 1.0 - (this.getUIContext().vp2px(event.displayX) / (this.displayWidth + 0.0));
              try {
                customScan.setFocusPoint({ x: x1, y: y1 });
                hilog.info(0x0001, TAG, \`Succeeded in setting focusPoint x1: ${x1}, y1: ${y1}\`);
              } catch (error) {
                hilog.error(0x0001, TAG, \`Failed to set focusPoint. Code: ${error.code}, message: ${error.message}\`);
              }
              setTimeout(() => {
                try {
                  customScan.resetFocus();
                } catch (error) {
                  hilog.error(0x0001, TAG, \`Failed to reset focus. Code: ${error.code}, message: ${error.message}\`);
                }
              }, 200);
            })
            .gesture(PinchGesture({ fingers: 2 })
              .onActionStart(() => {
                hilog.info(0x0001, TAG, 'Pinch start');
              })
              .onActionUpdate((event: GestureEvent) => {
                if (event) {
                  this.scaleValue = event.scale;
                }
              })
              .onActionEnd(() => {
                // Whether the scanning result has been obtained.
                if (this.scanFlag) {
                  return;
                }
                // Obtain the two-finger zoom ratio and set the zoom ratio.
                try {
                  let zoom = this.customGetZoom();
                  this.pinchValue = this.scaleValue \* zoom;
                  this.customSetZoom(this.pinchValue);
                  hilog.info(0x0001, TAG, 'Pinch end');
                } catch (error) {
                  hilog.error(0x0001, TAG, \`Failed to set zoom. Code: ${error.code}, message: ${error.message}\`);
                }
              }))
          }
        
          public customGetZoom(): number {
            let zoom = 1;
            try {
              zoom = customScan.getZoom();
              hilog.info(0x0001, TAG, \`Succeeded in getting zoom, zoom: ${zoom}\`);
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to get zoom. Code: ${error.code}, message: ${error?.message}\`);
            }
            return zoom;
          }
        
          public customSetZoom(pinchValue: number): void {
            try {
              customScan.setZoom(pinchValue);
              hilog.info(0x0001, TAG, \`Succeeded in setting zoom.\`);
            } catch (error) {
              hilog.error(0x0001, TAG, \`Failed to set zoom. Code: ${error.code}, message: ${error?.message}\`);
            }
          }
        }
        
5.  Determine the center point of the barcode image based on **scanCodeRect**.
    
    -   The following assumes that the phone orientation is portrait, with the charging port facing downwards:
        -   **scanCodeRect** contains the coordinates of the four points, based on which your app can draw a rectangular box around the barcode image.
            
            -   Upper left corner coordinates (x, y)
            
            -   Upper right corner coordinates (x, y)
            
            -   Lower left corner coordinates (x, y)
            
            -   Lower right corner coordinates (x, y)
        -   To ensure that the barcode image's center point aligns with the XComponent's coordinates, any offsets on the XComponent's X and Y axes must be applied correspondingly to the barcode image position. For example, if the offset on the x-axis is represented as **offsetX** and that on the y-axis is represented as **offsetY**, the coordinates of the center point need to be adjusted as follows:
            
            -   x = (left + right) / 2 + offsetX
            
            -   y = (top + bottom) / 2 + offsetY
    -   If the device may be rotated, the center point of the barcode image needs to adapt to the screen rotation angle ([Display.rotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#properties)) to ensure that the center point is correct at any rotation angle. For details, please refer to the [sample code](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts).
        
        For example, in the scenario where the XComponent with the **width** and **height** attributes has an x-axis misalignment by **offsetX** and a y-axis misalignment by **offsetY**:
        
        -   When [Display.rotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#properties) = 0, the center point coordinates are:
            -   x = (left + right) / 2 + offsetX
            -   y = (top + bottom) / 2 + offsetY
        -   When [Display.rotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#properties) = 1, the center point coordinates are:
            -   x = width - (top + bottom) / 2 + offsetX
            -   y = (left + right) / 2 + offsetY
        -   When [Display.rotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#properties) = 2, the center point coordinates are:
            -   x = width - (left + right) / 2 + offsetX
            -   y = height - (top + bottom) / 2 + offsetY
        -   When [Display.rotation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-display#properties) = 3, the center point coordinates are:
            -   x = (top + bottom) / 2 + offsetX
            -   y = height - (left + right) / 2+ offsetY
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/y7BBX3JsRr-P3FUMBBJiXA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA51905B83963446D36A5FF90A7976343A4075B3C36AE378A84333556764DBFA)
    
    For version 5.0.2(14) and later, the **rotation** and **orientation** attributes of the **Display** object are changed. As a result, the barcode image position needs to be adapted whenever the device is rotated to different angles.
    
    -   For versions earlier than 5.0.2(14), you can use the **rotation** or **orientation** attribute of the **Display** object to process the barcode image position when the device is rotated to different angles. Adaptations are needed for specific device types.
    -   For version 5.0.2(14) and later, you need to use the **rotation** attribute of the **Display** object to process the barcode image position when the device is rotated to different angles for all device types, without the need for any extra adaptations based on device types.
    

#### Emulator-based Development

Some APIs support Emulator-based development. For details, please refer to [Running Your App on the Emulator](../../../coding-and-debugging/running-your-app-on-the-emulator/document.md).

-   Since version 6.0.0(20), Emulator-based development is available for certain APIs regarding barcode scanning by custom UI (including [init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section447114223245), [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section38711535114711), [stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section6949611114915), [release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section1109456134917), and [rescan](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-customscan-api#section19244173211169)), which are enough for implementing basic functions of this barcode scanning scenario.
-   On the Emulator, barcode scanning by custom UI supports only 1280 x 720 px. Other resolutions will be converted to 1280 x 720 px.
