# Recognizing Barcodes in Image Data

#### Overview

The image-based barcode scanning capability can scan and recognize a barcode image in the camera preview stream data to obtain information.

#### Use Cases

This capability can recognize 1D codes, 2D codes, and multifunctional codes from the camera preview stream data and obtain the code type, value, position information, and camera zoom ratio. It can be used to recognize one or multiple barcodes, such as 1D codes and payment codes, on an image.

#### Flowchart

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/TOYazhZ_Qversv9UTgYC9g/en-us_image_0000002486708236.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062045Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB2741C243CE7FEC033587A4D3A7EB24861CC8A8D61D25E5B7B0A032C14FF66F "Click to enlarge")

1.  A user sends a barcode recognition request to your app.
2.  Your app calls [Camera Kit](../../../camera-kit/about-this-kit/document.md) to start the camera and obtain the preview stream data.
3.  Your app calls the **decodeImage** API of Scan Kit to recognize the barcode image.
4.  Scan Kit returns the barcode recognition result.
5.  Your app sends the barcode recognition result to the user.

#### API Description

Scan Kit provides an API for recognizing a barcode image in the passed image data and returns the recognition result using a promise. For details about the APIs, please refer to the [API document](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode).

| 
API

 | 

Description

 |
| :-- | :-- |
| 

[decodeImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode#section387381185013)(image: [ByteImage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode#section596225419382), options?: scanBarcode.[ScanOptions](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-scanbarcode-api#section1285191073117)): Promise<[DetectResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode#section655375703713)\>

 | 

Starts image-based barcode scanning. This API uses **ByteImage** to pass the image data and a promise to return the recognition result asynchronously.

 |

#### Development Procedure

This capability can recognize 1D codes, 2D codes, and multifunctional codes from the camera preview stream data and obtain the code type, value, position information (coordinates of the upper left and lower right corners of the minimum bounding rectangle of a barcode image, and coordinates of the four corner points of the QR code), and camera zoom ratio.

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

The following describes how to call the **detectBarcode.decodeImage** API to obtain barcode image information.

1.  Import the image-based barcode scanning API module and other relevant API modules. This API module provides parameters and methods for recognizing barcodes in images.
    
    import { detectBarcode, scanBarcode, scanCore } from '@kit.ScanKit';
    import { BusinessError } from '@kit.BasicServicesKit';
    import { camera } from '@kit.CameraKit';
    import { image } from '@kit.ImageKit';
    import { hilog } from '@kit.PerformanceAnalysisKit';
    
2.  Call Camera Kit to start the camera to implement [dual-channel preview](../../../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/dual-channel-preview-arkts/document.md).
3.  Obtain preview image data in real time through the **ImageReceiver** object (for details, please refer to [dual-channel preview capability](../../../camera-kit/fundamental-capabilities-for-camera-application-development-arkts/dual-channel-preview-arkts/document.md)) and call the **detectBarcode.decodeImage** API to parse the image data. Release the image data after the recognition is complete.
    
    // Obtain imgComponent: image.Component and the preview stream width and height from the ImageReceiver object.
    function decodeImageBuffer(imgComponent: image.Component, width: number, height: number) {
      let byteImg: detectBarcode.ByteImage = {
        byteBuffer: imgComponent.byteBuffer,
        // Rotate the camera preview stream data by 90 degrees.
        width: height,
        height: width,
        format: detectBarcode.ImageFormat.NV21
      };
      let options: scanBarcode.ScanOptions = {
        scanTypes: \[scanCore.ScanType.ALL\],
        enableMultiMode: true,
        enableAlbum: false
      };
      try {
        detectBarcode.decodeImage(byteImg, options).then((result: detectBarcode.DetectResult) => {
          hilog.info(0x0001, '\[Scan Sample\]',
            \`Succeeded in getting DetectResult by promise with options, result is ${JSON.stringify(result)}\`);
        }).catch((error: BusinessError) => {
          hilog.error(0x0001, '\[Scan Sample\]',
            \`Failed to get DetectResult by promise with options. Code: ${error.code}, message: ${error.message}\`);
        })
      } catch (error) {
        hilog.error(0x0001, '\[Scan Sample\]', \`Failed to detectBarcode. Code: ${error.code}, message: ${error.message}\`);
      }
    }
    
4.  Process the data in **cornerPoints** returned in detectBarcode.[DetectResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/scan-imagedecode#section655375703713) as follows:
    
    -   Since the screen's orientation differs from the camera sensor's orientation, the coordinates of the four corner points in **cornerPoints** need to be converted into the coordinate system that aligns with the screen's orientation. The conversion logic for the four corner points is as follows (assuming the camera preview stream resolution is to 1080 x 1920 px):
        -   Lower right corner (x, y): (1080 - cornerPoints\[0\].y, cornerPoints\[0\].x)
        -   Lower left corner (x, y): (1080 - cornerPoints\[1\].y, cornerPoints\[1\].x)
        -   Upper left corner (x, y): (1080 - cornerPoints\[2\].y, cornerPoints\[2\].x)
        -   Upper right corner (x, y): (1080 - cornerPoints\[3\].y, cornerPoints\[3\].x)
    
    -   When there's a mismatch between the camera preview stream's resolution and XComponent's dimensions, the coordinates of the four points in **cornerPoints** need to be converted based on the zoom ratio. For example, if the camera preview stream's resolution is 1080 x 1920 and the dimensions of XComponent are represented as **width** x **height**, the zoom ratio would be **width**/1080. In this case, the converted coordinates would be (x x **Ratio**, y x **Ratio**).

#### Emulator-based Development

This capability does not support Emulator-based development currently, and the error message "Emulator is not supported." will be displayed if you attempt to perform Emulator-based development.
