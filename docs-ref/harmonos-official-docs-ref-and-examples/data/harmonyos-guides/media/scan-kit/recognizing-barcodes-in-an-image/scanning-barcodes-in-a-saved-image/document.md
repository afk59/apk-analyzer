# Scanning Barcodes in a Saved Image

#### Overview

The image-based barcode scanning capability can scan and recognize barcodes in an image selected from the gallery to obtain information.

#### Use Cases

This capability can recognize 1D codes, 2D codes, and multifunctional codes from an image selected from the gallery and obtain the code type, value, and position information. It can be used to recognize one or multiple barcodes, such as 1D codes and payment codes, on an image.

#### Flowchart

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ce/v3/lwaQWRD8QUShhHYn29wi4Q/en-us_image_0000002518706995.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=395A885FAD715F3F52A913E89CC3E1C020B8290A4E4D772B130B833698C9E877 "Click to enlarge")

1.  A user sends an image-based barcode scanning request to your app.
2.  Your app calls the **decode** API of Scan Kit to start image-based barcode scanning.
3.  Scan Kit returns the barcode scanning result through a callback.
4.  Your app sends the barcode scanning result to the user.

#### API Description

The APIs use either a callback or promise to return the result. The table below lists the APIs using a callback and those using a promise. The APIs that use a callback provide the same functions as their counterparts that use a promise. For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[decode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode#section9221156204617)(inputImage: [InputImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode#section2194164873812), options?: scanBarcode.[ScanOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section1285191073117)): Promise<Array<scanBarcode.[ScanResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section10614317162112)\>>

 | 

Starts image-based barcode scanning. This API uses **InputImage** to pass the image, **ScanOptions** to set barcode scanning parameters (**options** is optional), and a promise to return the barcode scanning result asynchronously.

 |
| 

[decode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode#section12482559194718)(inputImage: InputImage, options: scanBarcode.ScanOptions, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

 | 

Starts image-based barcode scanning. This API uses **InputImage** to pass the image, **ScanOptions** to set barcode scanning parameters, and a callback to return the scanning result asynchronously.

 |
| 

[decode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode#section17256144317492)(inputImage: InputImage, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

 | 

Starts image-based barcode scanning. This API uses **InputImage** to pass the image and a callback to return the scanning result asynchronously.

 |

#### Development Procedure

Image-based barcode scanning can recognize 1D codes, 2D codes, and multifunctional codes in images to obtain the barcode value, type, and position information (coordinates of the upper left and lower right corners of the minimum bounding rectangle of the barcode image).

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

The following describes how to call the **detectBarcode.decode** API to scan barcodes in images:

1.  Import the image-based barcode scanning API module and other relevant API modules. This API provides parameters and methods for recognizing barcodes in images.
    
    // Import the log and picker modules required for image-based barcode scanning.
    import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
    import { photoAccessHelper } from '@kit.MediaLibraryKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    
2.  Call the **detectBarcode.decode** API to parse the barcode image.
    -   Obtain the scanning result using a promise. You are advised to obtain the **uri** parameter in the **InputImage** object through [picker](../../../media-library-kit/selecting-media-assets-using-picker/document.md).
        
        @Entry
        @Component
        struct DetectPage {
          build() {
            Column() {
              Button('Promise with options')
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
                  // Define the barcode scanning parameter options.
                  let options: scanBarcode.ScanOptions = {
                    scanTypes: \[scanCore.ScanType.ALL\],
                    enableMultiMode: true,
                  }
                  // Open the picker to select an image from the gallery.
                  let photoOption = new photoAccessHelper.PhotoSelectOptions();
                  photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
                  photoOption.maxSelectNumber = 1;
                  let photoPicker = new photoAccessHelper.PhotoViewPicker();
                  photoPicker.select(photoOption).then((result) => {
                    // Define the barcode scanning parameter inputImage. The uri parameter indicates the image selected using the picker.
                    let inputImage: detectBarcode.InputImage = { uri: result.photoUris\[0\] };
                    try {
                      // Call the API for recognizing barcodes in an image.
                      detectBarcode.decode(inputImage, options).then((result: Array<scanBarcode.ScanResult>) => {
                        hilog.info(0x0001, '\[Scan Sample\]',
                          \`Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}\`);
                      }).catch((error: BusinessError) => {
                        hilog.error(0x0001, '\[Scan Sample\]',
                          \`Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}\`);
                      });
                    } catch (error) {
                      hilog.error(0x0001, '\[Scan Sample\]',
                        \`Failed to detectBarcode. Code: ${error.code}, message: ${error.message}\`);
                    }
                  }).catch((error: BusinessError) => {
                    hilog.error(0x0001, '\[Scan Sample\]',
                      \`Failed to select a photo. Code: ${error.code}, message: ${error.message}\`);
                  })
                });
            }
            .width('100%')
            .height('100%')
            .alignItems(HorizontalAlign.Center)
            .justifyContent(FlexAlign.Center)
          }
        }
        
    -   Obtain the scanning result using a callback. You are advised to obtain the **uri** parameter in the **InputImage** object through [picker](../../../media-library-kit/selecting-media-assets-using-picker/document.md).
        
        @Entry
        
        @Component
        struct DetectPage {
          build() {
            Column() {
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
                  // Define the barcode scanning parameter **options**.
                  let options: scanBarcode.ScanOptions = {
                    scanTypes: \[scanCore.ScanType.ALL\],
                    enableMultiMode: true,
                    enableAlbum: true
                  }
                  // Open the photoPicker UI for users to select an image.
                  let photoOption = new photoAccessHelper.PhotoSelectOptions();
                  photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
                  photoOption.maxSelectNumber = 1;
                  let photoPicker = new photoAccessHelper.PhotoViewPicker();
                  photoPicker.select(photoOption).then((result) => {
                    // Define the barcode scanning parameter inputImage. The uri parameter indicates the image selected using the picker.
                    let inputImage: detectBarcode.InputImage = { uri: result.photoUris\[0\] };
                    try {
                      // Call the API for recognizing barcodes in an image.
                      detectBarcode.decode(inputImage, options,
                        (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
                          if (error && error.code) {
                            hilog.error(0x0001, '\[Scan Sample\]',
                              \`Failed to get ScanResult by callback with options. Code: ${error.code}, message: ${error.message}\`);
                            return;
                          }
                          hilog.info(0x0001, '\[Scan Sample\]',
                            \`Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(result)}\`);
                        });
                    } catch (error) {
                      hilog.error(0x0001, '\[Scan Sample\]',
                        \`Failed to detectBarcode. Code: ${error.code}, message: ${error.message}\`);
                    }
                  }).catch((error: BusinessError) => {
                    hilog.error(0x0001, '\[Scan Sample\]',
                      \`Failed to select a photo. Code: ${error.code}, message: ${error.message}\`);
                  })
                });
            }
            .width('100%')
            .height('100%')
            .alignItems(HorizontalAlign.Center)
            .justifyContent(FlexAlign.Center)
          }
        }
        

#### Emulator-based Development

This capability supports Emulator-based development. For details, please refer to [Running Your App on the Emulator](../../../../coding-and-debugging/running-your-app-on-the-emulator/document.md).
