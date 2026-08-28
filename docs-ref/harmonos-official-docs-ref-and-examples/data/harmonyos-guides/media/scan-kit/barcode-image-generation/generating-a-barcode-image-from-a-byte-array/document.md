# Generating a Barcode Image from a Byte Array

#### Overview

The barcode image generation capability can convert a byte array into a barcode image of a custom format.

#### Use Cases

The barcode image generation capability can convert a byte array into a barcode image of a custom format.

For example, you can use the capability to convert a byte array into a QR code of a transportation card.

#### Restrictions

-   The barcode image generation capability supports phones, tablets, wearables, 2-in-1 devices, and TVs. Specifically, wearables are supported since version 5.1.0(18), and 2-in-1 devices and TVs are supported since version 5.1.1(19).
-   If the data that Scan Kit recognizes from a barcode image generated based on a byte array is garbled characters, a dedicated decoder is required to decode the byte array. Such cases include barcode recognition of subway turnstiles.

#### Flowchart

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1c/v3/i0mFjsh6S629U8IPAY-JuQ/en-us_image_0000002518829469.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C1A0C1C95BE2B5AD6EBFD66CE63E6DB9D7A3E793F3DD818552BABF1AE48D5BE "Click to enlarge")

1.  A user sends a barcode image generation request to your app and inputs required information, such as the barcode type and the width and height of the barcode image.
2.  Your app calls the **createBarcode** API of Scan Kit to start barcode image generation.
3.  Scan Kit converts the input byte array into a barcode image and sends it to your app.
4.  Your app sends the generated barcode image to the user.

#### API Description

Generates a barcode image from a byte array and returns the result using a promise. For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-generatebarcode).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[createBarcode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-generatebarcode#section77911759145019)(content: ArrayBuffer, options: [CreateOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-generatebarcode#section87678254617)): Promise<image.[PixelMap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-pixelmap)\>

 | 

Generates a barcode image. This API returns parameters of the **image.PixelMap** type, which can be rendered as an image using the Image component. This API returns the generated barcode image using a promise asynchronously.

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
    import { buffer } from '@kit.ArkTS';
    
2.  Call the **createBarcode** API to generate a barcode image.
    -   Obtain the generated barcode image using a promise.
        
        const TAG: string = 'Create barcode';
        
        @Entry
        @Component
        struct Index {
          @State pixelMap: image.PixelMap | undefined = undefined
          build() {
            Flex({ direction: FlexDirection.Column, alignItems: ItemAlign.Center, justifyContent: FlexAlign.Center }) {
              Button('generateBarcode Promise').onClick(() => {
                this.pixelMap = undefined;
                let content: string =
        '0177C10DD10F7768600202312110000063458FD14112345678FFFFD381012610b746365409210201b66636540ad0200020000000000110e617003201000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000006645fbec664358ECF657CB40693c92da';
                let contentBuffer: ArrayBuffer = buffer.from(content, 'hex').buffer; // Create a buffer using a character string that contains hexadecimal characters.
                let options: generateBarcode.CreateOptions = {
                  scanType: scanCore.ScanType.QR\_CODE,
                  height: 400,
                  width: 400
                }
                try {
                // Return a PixelMap-format barcode image.
                  generateBarcode.createBarcode(contentBuffer, options).then((pixelMap: image.PixelMap) => {
                    this.pixelMap = pixelMap;
                    hilog.info(0x0001, TAG, 'Succeeded in creating barCode.');
                  }).catch((error: BusinessError) => {
                    hilog.error(0x0001, TAG, \`Failed to createBarCode. Code: ${error.code}, message: ${error.message}\`);
                  })
                } catch (error) {
                  hilog.error(0x0001, TAG,
                    \`Failed to createBarcode by Promise with options. Code: ${error.code}, message: ${error.message}\`);
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
