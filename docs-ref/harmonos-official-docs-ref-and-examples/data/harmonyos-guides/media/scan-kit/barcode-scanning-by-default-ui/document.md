# Barcode Scanning by Default UI

#### Overview

The capability of barcode scanning by default UI offers a consistent scanning UI at the system level, which includes a camera preview stream, a scanning entry for the photo gallery, and a prompt to turn on the flash light in dim light conditions. For the default UI of code scanning, the system-level camera permission has been pre-granted and the camera remains securely accessible when the UI is opened. It means that, you do not need to request the camera permission again. This capability can help you develop various barcode scanning scenarios for your app.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/4YUkNNP6Tu2Q_sHQAMDObw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DDC3A703B40313E2C9191C6D0E458285A7D5272983A041DC422545CF7FC0650A)

By using the capability of barcode scanning by default UI, you can achieve the in-app code scanning function. To enhance user experience, you are also advised to [integrate the scan-to-access capability](../scan-to-access-capability/document.md) so your users can directly go to a specified service page in your app by scanning a barcode via either the code scanning entry on Control Panel or the in-app code scanning entry.

#### Use Cases

This capability provides a default scanning UI that offers streamlined system-level barcode scanning experience and a scanning entry for the photo gallery to recognize one and multiple barcodes at a time. It can recognize multiple barcode types described in [ScanType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scancore#section113371139123212). Your app can use this capability to scan barcodes in various scenarios without needing to use a third-party library.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/71/v3/Sjy6NS_BSpWIdXNo0Ikg5Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=52D0BF08A5F205DE9464B9053B4E61C9F08370A7B51047498D068BE2B29F6F87)

1.  If it is the first time the default scanning UI is opened, your app shows a privacy banner notification to the user.
2.  The user can either tap **Learn more** for more instructions on securely accessing the camera or directly tap the button to close the notification. After the privacy banner notification is closed and the scanning page of the app is opened again, the privacy banner notification will not be displayed, but an access security tip is displayed, which will disappear in three seconds.

#### Restrictions

-   The function of barcode scanning by default UI supports the floating window and split-screen scenarios since version 6.0.0(20).
-   Gallery-based barcode scanning can only recognize one barcode at a time.
-   The default UI does not support custom settings.

#### Flowchart

The flowchart for using this capability is as follows.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c9/v3/oK1ondZdTa2UigZ14tJHKw/en-us_image_0000002518825823.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8FFFC564A60A6819FF8BCEE7F3A3BF028CF89B554928FB237A2937FEEC2C85B3 "Click to enlarge")

1.  A user sends a barcode scanning request to your app.
2.  Your app calls the **startScanForResult** API of Scan Kit to open the barcode scanning UI.
3.  If it is the first time the default scanning UI is opened, your app shows a privacy banner notification to the user.
4.  The user can tap the close button to close the notification. When the scanning page of the app is opened again, the privacy banner notification will not be displayed, but an access security tip is displayed, which will disappear in three seconds.
5.  Scan Kit returns the barcode scanning result using a callback or promise.
6.  If multiple barcodes are recognized, the user needs to select one barcode to obtain the barcode scanning result. If only one barcode is recognized, the barcode scanning result can be directly returned.
7.  The app shows the target service page based on the parsing result to the user.

#### API Description

The APIs use either a callback or promise to return the result. The table below lists the APIs using a callback and those using a promise. The APIs that use a callback provide the same functions as their counterparts that use a promise. The **startScanForResult** API is used to open the barcode scanning UI in your app. For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[startScanForResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section829511911349)(context: [common.Context](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-app-ability-common#context), options?: [ScanOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section1285191073117)): Promise<[ScanResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section10614317162112)\>

 | 

Opens the default scanning UI to scan barcodes. This API uses **ScanOptions** to set barcode scanning parameters and uses a promise to return the barcode scanning result asynchronously.

 |
| 

[startScanForResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section1738211373353)(context: common.Context, options: ScanOptions, callback: AsyncCallback<ScanResult>): void

 | 

Opens the default scanning UI to scan barcodes. This API uses **ScanOptions** to set barcode scanning parameters and uses a callback to return the barcode scanning result asynchronously.

 |
| 

[startScanForResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section399311216327)(context: common.Context, callback: AsyncCallback<ScanResult>): void

 | 

Opens the default scanning UI to scan barcodes. This API uses a callback to return the barcode scanning result asynchronously.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/yUlmdzZoSkCildRZZnkgzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=B7A23DB9DCD5AE98E0D624FC066C2C96E23A65E8C67AB006245F238554B6F017)

The **startScanForResult** API must be called in the lifecycles of the UI and component. To use the scanning UI in full screen or immersive mode, please refer to the [development guide](../../../application-framework/arkui/ui-development-arkts-based-declarative-development-paradigm/component-layouts/immersive-effect-development/document.md).

#### Development Procedure

Scan Kit provides the function of scanning barcodes using the default UI. The barcode scanning API directly controls the camera for optimal zoom control, automatic exposure adjustment, and auto-focus, creating a smooth barcode scanning experience and lowering workload for you.

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

The following describes how to call the **startScanForResult** API of Scan Kit to open the barcode scanning UI:

1.  Import the module for scanning barcodes using the default UI. In the code, [scanCore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scancore) provides definition of scanning types and [scanBarcode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api) provides methods and parameters for opening the default scanning UI.
    
    import { scanCore, scanBarcode } from '@kit.ScanKit';
    // Import the required log and error code modules.
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the **startScanForResult** method to open the default UI for scanning.
    -   Obtain the scanning result using a promise.
        
        @Entry
        @Component
        struct ScanBarCodePage {
          build() {
            Column() {
              Row() {
                Button("Promise with options")
                  .backgroundColor('#0D9FFB')
                  .fontSize(20)
                  .fontColor($r('sys.color.comp\_background\_list\_card'))
                  .fontWeight(FontWeight.Normal)
                  .align(Alignment.Center)
                  .type(ButtonType.Capsule)
                  .width('90%')
                  .height(40)
                  .margin({ top: 5, bottom: 5 })
                  .onClick(() => {
                    // Define scanning parameters.
                    let options: scanBarcode.ScanOptions = {
                      scanTypes: \[scanCore.ScanType.ALL\],
                      enableMultiMode: true,
                      enableAlbum: true
                    };
                    try {
                      // Call the getHostContext API to obtain the context associated with the current page.
                      scanBarcode.startScanForResult(this.getUIContext().getHostContext(), options).then((result: scanBarcode.ScanResult) => {
                        // Parse the code value and open the specified app service page.
                        hilog.info(0x0001, '\[Scan CPSample\]', \`Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}\`);
                      }).catch((error: BusinessError) => {
                        hilog.error(0x0001, '\[Scan CPSample\]',
                          \`Failed to get ScanResult by promise with options. Code:${error.code}, message: ${error.message}\`);
                      });
                    } catch (error) {
                      hilog.error(0x0001, '\[Scan CPSample\]',
                        \`Failed to start the scanning service. Code:${error.code}, message: ${error.message}\`);
                    }
                  })
              }
              .height('100%')
            }
            .width('100%')
          }
        }
        
    -   Obtain the scanning result using a callback.
        
        @Entry
        @Component
        struct ScanBarCodePage {
          build() {
            Column() {
              Row() {
                Button('Callback with options')
                  .backgroundColor('#0D9FFB')
                  .fontSize(20)
                  .fontColor($r('sys.color.comp\_background\_list\_card'))
                  .fontWeight(FontWeight.Normal)
                  .align(Alignment.Center)
                  .type(ButtonType.Capsule)
                  .width('90%')
                  .height(40)
                  .margin({ top: 5, bottom: 5 })
                  .onClick(() => {
                    // Define scanning parameters.
                    let options: scanBarcode.ScanOptions = {
                      scanTypes: \[scanCore.ScanType.ALL\],
                      enableMultiMode: true,
                      enableAlbum: true
                    };
                    try {
                      // Call the getHostContext API to obtain the context associated with the current page.
                      scanBarcode.startScanForResult(this.getUIContext().getHostContext(), options,
                        (error: BusinessError, result: scanBarcode.ScanResult) => {
                          if (error) {
                            hilog.error(0x0001, '\[Scan CPSample\]',
                              \`Failed to get ScanResult by callback with options. Code: ${error.code}, message: ${error.message}\`);
                            return;
                          }
                          // Parse the code value and open the specified app service page.
                          hilog.info(0x0001, '\[Scan CPSample\]', \`Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(result)}\`);
                        })
                    } catch (error) {
                      hilog.error(0x0001, '\[Scan CPSample\]',
                        \`Failed to start the scanning service. Code:${error.code}, message: ${error.message}\`);
                    }
                  })
              }
              .height('100%')
            }
            .width('100%')
          }
        }
        

#### Emulator-based Development

Since version 6.0.0(20), using the Emulator for developing the function of barcode scanning on the default UI is supported. For details, please refer to [Running Your App on the Emulator](../../../coding-and-debugging/running-your-app-on-the-emulator/document.md).

On the Emulator, the camera stream on the default scanning UI is flipped horizontally, and black borders will appear at the top and bottom of the scanning UI due to the fixed resolution of the camera stream.
