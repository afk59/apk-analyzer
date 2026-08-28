# Generating a Barcode Image from Text

#### Overview

The barcode image generation capability can convert a string into a barcode image of a custom format.

#### Use Cases

This capability can convert a string into a 1D code or 2D code of a custom format.

You can use this capability to convert a string into a contact barcode or a phone clone barcode, for example, converting string "HUAWEI" into a barcode.

#### Restrictions

The barcode image generation capability supports phones, tablets, wearables, 2-in-1 devices, and TVs. Specifically, wearables are supported since version 5.1.0(18), and 2-in-1 devices and TVs are supported since version 5.1.1(19).

#### Flowchart

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ab/v3/uQDW2umsStGr6g2BlRWQ1w/en-us_image_0000002486548590.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5680D15519926331B4E4C707E4ADD304E566D633EB427996167A06AD1704118E "Click to enlarge")

1.  A user sends a barcode image generation request to your app and inputs required information, such as the barcode type and the width and height of the barcode image.
2.  Your app calls the **createBarcode** API of Scan Kit to start barcode image generation.
3.  Scan Kit converts the input string into a barcode image of the specified format and sends the generated barcode image to your app.
4.  Your app sends the generated barcode image to the user.

#### API Description

The APIs use either a callback or promise to return the result. The table below lists the APIs using a callback and those using a promise. The APIs that use a callback provide the same functions as their counterparts that use a promise. For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-generatebarcode).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createBarcode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-generatebarcode#section1841142919352)(content: string, options: [CreateOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-generatebarcode#section87678254617)): Promise<image.[PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap)\>

 | 

Generates a barcode image. This API returns parameters of the **image.PixelMap** type, which can be rendered as an image using the Image component. This API returns the generated barcode image using a promise asynchronously.

 |
| 

[createBarcode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-generatebarcode#section129941731103410)(content: string, options: CreateOptions, callback: AsyncCallback<image.PixelMap>): void

 | 

Generates a barcode image. This API returns parameters of the **image.PixelMap** type, which can be rendered as an image using the Image component. This API returns the generated barcode image using a callback asynchronously.

 |

#### Development Procedure

The barcode image generation capability directly generates the required barcode image based on fixed parameters and optional parameters that are passed.

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

The following describes how to call the **createBarcode** API to generate a barcode image:

1.  Import the barcode image generation API module. This module provides parameters and methods for generating a barcode image.
    
    // Import the image and error code modules required for generating a barcode image.
    import { scanCore, generateBarcode } from '@kit.ScanKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call the **createBarcode** API to generate a barcode image.
    -   Obtain the generated barcode image using a promise.
        
        @Entry
        @Component
        struct Index {
          @State pixelMap: image.PixelMap | undefined = undefined
        
          build() {
            Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
              Button('generateBarcode Promise').onClick(() => {
                // Set parameters for generating a barcode image, for example, a QR code image.
                this.pixelMap = undefined;
                let content: string = 'huawei';
                let options: generateBarcode.CreateOptions = {
                  scanType: scanCore.ScanType.QR\_CODE,
                  height: 400,
                  width: 400
                }
                try {
                // Return a PixelMap-format barcode image.
                  generateBarcode.createBarcode(content, options).then((pixelMap: image.PixelMap) => {
                    this.pixelMap = pixelMap;
                  }).catch((error: BusinessError) => {
                    hilog.error(0x0001, '\[generateBarcode\]',
                      \`Failed to get PixelMap by promise with options. Code: ${error.code}, message: ${error.message}\`);
                  })
                } catch (error) {
                  hilog.error(0x0001, '\[generateBarcode\]',
                    \`Failed to createBarcode by promise with options. Code: ${error.code}, message: ${error.message}\`);
                }
        
              })
              // Display the obtained barcode image.
              if (this.pixelMap) {
                Image(this.pixelMap).width(300).height(300).objectFit(ImageFit.Contain)
              }
            }
            .width('100%')
            .height('100%')
          }
        }
        
    -   Obtain the generated barcode image using a callback.
        
        @Entry
        @Component
        struct Index {
          @State pixelMap: image.PixelMap | undefined = undefined
        
          build() {
            Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
              Button('generateBarcode Callback').onClick(() => {
                // Set parameters for generating a barcode image, for example, a QR code image.
                let content = 'huawei';
                let options: generateBarcode.CreateOptions = {
                  scanType: scanCore.ScanType.QR\_CODE,
                  height: 400,
                  width: 400
                }
                try {
                // Return a PixelMap-format barcode image.
                  generateBarcode.createBarcode(content, options, (error: BusinessError, pixelMap: image.PixelMap) => {
                    if (error) {
                      hilog.error(0x0001, '\[generateBarcode\]',
                        \`Failed to get PixelMap by callback with options. Code: ${error.code}, message: ${error.message}\`);
                      return;
                    }
                    this.pixelMap = pixelMap;
                  })
                } catch (error) {
                  hilog.error(0x0001, '\[generateBarcode\]',
                    \`Failed to createBarcode by callback with options. Code: ${error.code}, message: ${error.message}\`);
                }
              })
              // Display the obtained barcode image.
              if (this.pixelMap) {
                Image(this.pixelMap).width(300).height(300).objectFit(ImageFit.Contain)
              }
            }
            .width('100%')
            .height('100%')
          }
        }
        

#### Emulator-based Development

This capability does not support Emulator-based development currently, and the error message "Emulator is not supported." will be displayed if you attempt to perform Emulator-based development.
