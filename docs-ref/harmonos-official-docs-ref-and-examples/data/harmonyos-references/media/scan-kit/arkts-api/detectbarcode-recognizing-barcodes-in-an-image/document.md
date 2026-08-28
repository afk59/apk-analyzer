# detectBarcode (Recognizing Barcodes in an Image)

This module provides the capability of recognizing barcodes from an image or image data, including 1D codes, 2D codes, and multifunctional codes.

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

**Start version**: 4.1.0(11)

#### Modules to Import

import { detectBarcode } from '@kit.ScanKit';

#### InputImage

Image where barcodes are to be scanned.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

uri

 | 

string

 | 

No

 | 

No

 | 

Image path, for example, **file://media/Photo/x/xxx.jpg**.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f8/v3/azodAhGGRryFStIqAZ1iUQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6EDB5F379AB994D2C2802CBDE797C5B22927375A1A78FF25DDD7B0F6DE9186D9)

You are advised to use the [picker](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/photoaccesshelper-photoviewpicker) to obtain the image path.

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

let photoSelectOptions = new photoAccessHelper.PhotoSelectOptions();
photoSelectOptions.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
photoSelectOptions.maxSelectNumber = 1;
photoSelectOptions.isPhotoTakingSupported = false;
photoSelectOptions.isEditSupported = false;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoSelectOptions).then((result: photoAccessHelper.PhotoSelectResult) => {
  if (!result || (result.photoUris && result.photoUris.length === 0)) {
    hilog.error(0x0001, 'picker', 'Failed to get PhotoSelectResult by promise');
    return;
  }
  hilog.info(0x0001, 'picker', \`Succeeded in getting PhotoSelectResult by promise.\`);
}).catch((error: BusinessError) => {
  hilog.error(0x0001, 'picker', \`Failed to get PhotoSelectResult by promise. Code: ${error.code}\`);
});

#### detectBarcode.decode

decode(inputImage: InputImage, options?: scanBarcode.ScanOptions): Promise<Array<scanBarcode.ScanResult>>

Scans barcodes in an image based on input parameters, and asynchronously returns the result using a promise.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

inputImage

 | 

[InputImage](#section2194164873812)

 | 

Yes

 | 

Image where barcodes are to be scanned.

 |
| 

options

 | 

scanBarcode.[ScanOptions](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section1285191073117)

 | 

No

 | 

Parameters for scanning barcodes on the image.

 |

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<Array<scanBarcode.[ScanResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section10614317162112)\>>

 | 

**Promise** object, used to return the result.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

 |
| 

1000500001

 | 

Internal error.

 |

**Example:**

import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define scanning parameters.
let options: scanBarcode.ScanOptions = { scanTypes: \[scanCore.ScanType.ALL\], enableMultiMode: true, enableAlbum: true };
// Use picker to open the gallery and select an image.
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((result) => {
  // Define the barcode scanning parameter inputImage. The uri parameter indicates the image selected using picker.
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
      \`Failed to detect Barcode. Code: ${error.code}, message: ${error.message}\`);
  }
}).catch((error: BusinessError) => {
  hilog.error(0x0001, 'picker', \`Failed to get PhotoSelectResult by promise. Code: ${error.code}.\`);
});

#### detectBarcode.decode

decode(inputImage: InputImage, options: scanBarcode.ScanOptions, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

Scans barcodes in an image based on input parameters, and asynchronously returns the result using a callback.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

inputImage

 | 

[InputImage](#section2194164873812)

 | 

Yes

 | 

Image where barcodes are to be scanned.

 |
| 

options

 | 

scanBarcode.[ScanOptions](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section1285191073117)

 | 

Yes

 | 

Parameters for scanning barcodes on the image.

 |
| 

callback

 | 

AsyncCallback<Array<scanBarcode.[ScanResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section10614317162112)\>>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the recognition result (Array<scanBarcode.[ScanResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section10614317162112)\>); otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

 |
| 

1000500001

 | 

Internal error.

 |

**Example:**

import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define scanning parameters.
let options: scanBarcode.ScanOptions = { scanTypes: \[scanCore.ScanType.ALL\], enableMultiMode: true, enableAlbum: true }
// Open the photoPicker UI for users to select an image.
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((result) => {
  // Define the barcode scanning parameter inputImage. The uri parameter indicates the image selected using picker.
  let inputImage: detectBarcode.InputImage = { uri: result.photoUris\[0\] };
  try {
    // Call the API for recognizing barcodes in an image.
    detectBarcode.decode(inputImage, options, (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
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
      \`Failed to detect Barcode. Code: ${error.code}, message: ${error.message}\`);
  }
}).catch((error: BusinessError) => {
  hilog.error(0x0001, 'picker', \`Failed to get PhotoSelectResult by promise. Code: ${error.code}\`);
});

#### detectBarcode.decode

decode(inputImage: InputImage, callback: AsyncCallback<Array<scanBarcode.ScanResult>>): void

Returns the image-based scanning result using a callback.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

inputImage

 | 

[InputImage](#section2194164873812)

 | 

Yes

 | 

Image where barcodes are to be scanned.

 |
| 

callback

 | 

AsyncCallback<Array<scanBarcode.[ScanResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section10614317162112)\>>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the recognition result (Array<scanBarcode.[ScanResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section10614317162112)\>); otherwise, **err** is an error object.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

 |
| 

1000500001

 | 

Internal error.

 |

**Example:**

import { scanBarcode, detectBarcode } from '@kit.ScanKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Use picker to open the gallery and select an image.
let photoOption = new photoAccessHelper.PhotoSelectOptions();
photoOption.MIMEType = photoAccessHelper.PhotoViewMIMETypes.IMAGE\_TYPE;
photoOption.maxSelectNumber = 1;
let photoPicker = new photoAccessHelper.PhotoViewPicker();
photoPicker.select(photoOption).then((result) => {
  // Define the barcode scanning parameter inputImage. The uri parameter indicates the image selected using picker.
  let inputImage: detectBarcode.InputImage = { uri: result.photoUris\[0\] };
  try {
    // Call the API for recognizing barcodes in an image.
    detectBarcode.decode(inputImage, (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error && error.code) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}\`);
    });
  } catch (error) {
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to detect Barcode. Code: ${error.code}, message: ${error.message}\`);
  }
}).catch((error: BusinessError) => {
  hilog.error(0x0001, 'picker', \`Failed to get PhotoSelectResult by promise. Code: ${error.code}\`);
});

#### ByteImage

Contains image data to be recognized.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

byteBuffer

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

Image data.

 |
| 

width

 | 

number

 | 

No

 | 

No

 | 

Image width, in px.

 |
| 

height

 | 

number

 | 

No

 | 

No

 | 

Image height, in px.

 |
| 

format

 | 

[ImageFormat](#section326142720394)

 | 

No

 | 

No

 | 

Image data type.

 |

**Example:**

import { detectBarcode } from '@kit.ScanKit';

// Buffer, height, and width data of the YUV image, which can be obtained from the camera preview stream data. This example assumes that the width and height obtained are 1920 x 1080.
let byteImg: detectBarcode.ByteImage = {
  byteBuffer: buffer,
  width: 1920,
  height: 1080,
  format: detectBarcode.ImageFormat.NV21
};

#### ImageFormat

Defines enumerated images data types.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

NV21

 | 

0

 | 

NV21 image format.

 |

#### DetectResult

Contains the recognition result.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

| 
Parameter

 | 

Type

 | 

Read-Only

 | 

Optional

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

scanResults

 | 

Array<scanBarcode.[ScanResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section10614317162112)\>

 | 

No

 | 

No

 | 

Scanning result.

 |
| 

zoomValue

 | 

number

 | 

No

 | 

No

 | 

Camera zoom ratio. You can call [setZoomRatio](../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/interface-zoom/document.md#setzoomratio11) to control the zoom ratio.

**Note**:

1.  Call the [getZoomRatio](../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/interface-zoom/document.md#getzoomratio11) API of Camera Kit to obtain the zoom ratio in use (**zoomRatio**).
2.  Call the [setZoomRatio](../../../camera-kit/arkts-apis/ohos-multimedia-camera-camera-management/interface-zoom/document.md#setzoomratio11) API of Camera Kit to set **targetRatio** to the value of **zoomRatio** x **zoomValue**.

 |

#### detectBarcode.decodeImage

decodeImage(image: ByteImage, options?: scanBarcode.ScanOptions): Promise<DetectResult>

Scans barcodes in an image based on input parameters, and asynchronously returns the result using a promise.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

**Parameters:**

| 
Parameter

 | 

Type

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- |
| 

image

 | 

[ByteImage](#section596225419382)

 | 

Yes

 | 

Image data to be recognized.

 |
| 

options

 | 

scanBarcode.[ScanOptions](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section1285191073117)

 | 

No

 | 

Parameters for scanning barcodes on the image.

 |

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[DetectResult](#section655375703713)\>

 | 

**Promise** object, used to return the recognition result.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

401

 | 

Parameter error. Possible causes: 1. Incorrect parameter types; 2. Parameter verification failed.

 |
| 

1000500001

 | 

Internal error.

 |

**Example:**

import { scanCore, scanBarcode, detectBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Obtain the **YUVByteBuffer**, **YUVHeight**, and **YUVWidth** parameters of the image first. This example assumes that the width and height obtained are 1920 x 1080.
let byteImg: detectBarcode.ByteImage = {
  byteBuffer: YUVByteBuffer,
  width: 1920,
  height: 1080,
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
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to decode Image. Code: ${error.code}, message: ${error.message}\`);
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0e/v3/4GSWb7UIQqqjUFGzHzkMTQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4862348DEBA43CF51B71C5ABF9B11F5CA7C040F5A6AC56E2D38B58D5E9C7266B)

Concurrent calls are not supported.
