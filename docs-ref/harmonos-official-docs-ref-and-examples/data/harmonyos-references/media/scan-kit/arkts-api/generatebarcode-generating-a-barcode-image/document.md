# generateBarcode (Generating a Barcode Image)

This module provides the capability of generating a barcode image from text or a byte array. Currently, Scan Kit can generate barcodes in 13 formats, including EAN-8, EAN-13, UPC-A, UPC-E, Codabar, Code 39, Code 93, Code 128, ITF-14, QR Code, Data Matrix, PDF417, and Aztec. Currently, this capability does not support multifunctional codes.

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

**Start version**: 4.1.0(11)

#### Modules to Import

import { generateBarcode } from '@kit.ScanKit';

#### ErrorCorrectionLevel

Error correction rate enumeration.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Multimedia.Scan.GenerateBarcode

**Start version**: 4.1.0(11)

| 
Parameter

 | 

Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

LEVEL\_L

 | 

0

 | 

The error correction rate is 7%.

 |
| 

LEVEL\_M

 | 

1

 | 

The error correction rate is 15%.

 |
| 

LEVEL\_Q

 | 

2

 | 

The error correction rate is 25%.

 |
| 

LEVEL\_H

 | 

3

 | 

The error correction rate is 30%.

 |

#### CreateOptions

Sets parameters for generating a barcode image.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Multimedia.Scan.GenerateBarcode

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

scanType

 | 

scanCore.[ScanType](../scancore-public-information-about-barcode-scanning/document.md#section113371139123212)

 | 

No

 | 

No

 | 

Barcode type.

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

Barcode image width, in px. The value ranges from 200 to 4096.

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

Barcode image height, in px. The value ranges from 200 to 4096.

 |
| 

margin

 | 

number

 | 

No

 | 

Yes

 | 

Minimum margin of the generated barcode image, in px. The value ranges from 1 to 10. The default value is **1**.

 |
| 

level

 | 

[ErrorCorrectionLevel](#section1829612519455)

 | 

No

 | 

Yes

 | 

Error correction level. The default value is **LEVEL\_H**. This parameter is valid only when a QR code is generated.

 |
| 

backgroundColor

 | 

number

 | 

No

 | 

Yes

 | 

Background color of the generated barcode image, which is in HEX format. The default background color is white (0xffffff).

 |
| 

pixelMapColor

 | 

number

 | 

No

 | 

Yes

 | 

Barcode color of the generated barcode image, which is in HEX format. The default color is black (0x000000).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/KRhzk71dQ-6KNvsf8Pn7qA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3FD4AEB8DAC01DD787C0BE423C416670BD05F9B2F5FA34747489DC3093BB17C2)

Suggestions on setting parameters for generating a barcode image:

-   Background color and barcode color of the barcode image
    
    You are advised to use the default background color (white) and barcode color (black). The barcode recognition rate will be deteriorated if the contrast between the background color and barcode color is small.
    
-   Minimum barcode image margin
    
    You are advised to use the default minimum margin, which is 1 px. The value ranges from 1 to 10.
    
-   Barcode image size
    1.  When you generate a barcode of the QR Code, Data Matrix, or Aztec format, it is recommended that **width** and **height** be set to the same value ranging from 200 to 4096, in px. Otherwise, the generated barcode image would be too small to recognize.
    2.  When you generate a barcode of the EAN-8, EAN-13, UPC-A, UPC-E, Codabar, Code 39, Code 93, Code 128, ITF-14, or PDF417 format, it is recommended that the ratio between the values of **width** and **height** be 2:1 and that the value of **width** be greater than 400, in px. Otherwise, the generated barcode image is too small, making it hard to be recognized.

**Example:**

import { scanCore, generateBarcode } from '@kit.ScanKit';

// The QR code is used as an example.
let options: generateBarcode.CreateOptions = {
  scanType: scanCore.ScanType.QR\_CODE,
  height: 200,
  width: 200,
  backgroundColor: 0xFFFFFF,
  pixelMapColor: 0x000000,
  margin: 1,
  level: generateBarcode.ErrorCorrectionLevel.LEVEL\_H
}

#### generateBarcode.createBarcode

createBarcode(content: string, options: CreateOptions): Promise<image.PixelMap>

Generates a barcode image from text. This API returns the generated barcode image using a promise asynchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Multimedia.Scan.GenerateBarcode

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

content

 | 

string

 | 

Yes

 | 

Character string used to generate a barcode image. You can check "Table 1 Restrictions on the content parameter" below to learn more about the restrictions on this parameter.

 |
| 

options

 | 

[CreateOptions](#section87678254617)

 | 

Yes

 | 

Parameters for generating a barcode image.

 |

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<image.[PixelMap](../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

**Promise** object, used to return the generated barcode image object.

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

import { image } from '@kit.ImageKit';
import { scanCore, generateBarcode } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Set parameters for generating a barcode image, for example, a QR code image.
let content: string = 'Huawei@HMSCore';
let options: generateBarcode.CreateOptions = {
  scanType: scanCore.ScanType.QR\_CODE,
  height: 200,
  width: 200
}
try {
  generateBarcode.createBarcode(content, options).then((result: image.PixelMap) => {
// Return a PixelMap-format barcode image.
    hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in getting PixelMap by promise with options, size: ${result.getImageInfoSync().size}\`);
  }).catch((error: BusinessError) => {
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to get PixelMap by promise with options. Code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to generateBarcode. Code: ${error.code}, message: ${error.message}\`);
}

**Table 1** Restrictions on the content parameter
| 
Barcode Type

 | 

Restriction

 |
| :-- | :-- |
| 

QR Code

 | 

The string can contain up to 512 characters and supports Chinese characters. If the string is too long, the generated barcode will be complex and hard to be recognized.

 |
| 

Aztec

 | 

The string can contain up to 512 characters and supports Chinese characters. If the string is too long, the generated barcode will be complex and hard to be recognized.

 |
| 

PDF417

 | 

The string can contain up to 512 characters and supports Chinese characters. If the string is too long, the generated barcode will be complex and hard to be recognized.

 |
| 

Data Matrix

 | 

The string can contain up to 512 characters. If the string is too long, the generated barcode will be complex and hard to be recognized.

 |
| 

UPC-A

 | 

The string can contain 11 digits and can contain only digits. It will be converted into a 12-digit barcode image, with the last digit being a verification digit.

 |
| 

UPC-E

 | 

The string can contain 7 digits and can contain only digits. The first digit must be 0 or 1. It will be converted into an 8-digit barcode image, with the last digit being a verification digit.

 |
| 

ITF-14

 | 

The string can contain an even number of digits (up to 80 digits) and contain only digits. It will be converted into a barcode image containing an even number of digits. If the string is too long, the generated barcode will be complex and hard to be recognized.

 |
| 

EAN-8

 | 

The string can contain 7 digits and can contain only digits. It will be converted into an 8-digit barcode image, with the last digit being a verification digit.

 |
| 

EAN-13

 | 

The string can contain 12 digits and can contain only digits. The first digit cannot be 0. It will be converted into a 13-digit barcode image, with the last digit being a verification digit.

 |
| 

Code 39

 | 

The string can contain up to 80 bytes, including digits, uppercase letters, lowercase letters, hyphens (-), periods (.), dollar signs ($), slashes (/), plus signs (+), percent signs (%), asterisks (\*), and spaces. Note that a lowercase letter occupies two bytes.

 |
| 

Code 93

 | 

The string can contain up to 80 bytes, including digits, uppercase letters, lowercase letters, hyphens (-), periods (.), dollar signs ($), slashes (/), plus signs (+), percent signs (%), asterisks (\*), and spaces. Note that a lowercase letter occupies two bytes.

 |
| 

Code 128

 | 

The string can contain up to 80 bytes, including digits, uppercase letters, lowercase letters, hyphens (-), periods (.), dollar signs ($), slashes (/), plus signs (+), percent signs (%), asterisks (\*), and spaces. Note that a lowercase letter occupies one byte.

 |
| 

Codabar

 | 

The string can contain up to 512 characters and begin and end with any of letters A, B, C, and D. (In special cases, characters T, N, \*, and E are also encoded as A, B, C, and D. Therefore, letters A, B, C, and D are recommended.) Other characters can be digits, hyphens (-), periods (.), dollar signs ($), slashes (/), colons (:), and plus signs (+).

 |

#### generateBarcode.createBarcode

createBarcode(content: string, options: CreateOptions, callback: AsyncCallback<image.PixelMap>): void

Generates a barcode image from text. This API returns the generated barcode image using a callback asynchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Multimedia.Scan.GenerateBarcode

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

content

 | 

string

 | 

Yes

 | 

Character string used to generate a barcode image. You can check "Table 1 Restrictions on the content parameter" in [generateBarcode.createBarcode](#section1841142919352) to learn more about the restrictions on this parameter.

 |
| 

options

 | 

[CreateOptions](#section87678254617)

 | 

Yes

 | 

Parameters for generating a barcode image.

 |
| 

callback

 | 

AsyncCallback<image.[PixelMap](../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

Yes

 | 

Callback function. If the generation is successful, **err** is **undefined** and **data** is the **image.PixelMap** object generated; otherwise, **err** is an error object.

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

import { image } from '@kit.ImageKit';
import { scanCore, generateBarcode } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Set parameters for generating a barcode image, for example, a QR code image.
let content: string = 'Huawei@HMSCore';
let options: generateBarcode.CreateOptions = {
  scanType: scanCore.ScanType.QR\_CODE,
  height: 200,
  width: 200
}
try {
  generateBarcode.createBarcode(content, options, (error: BusinessError, result: image.PixelMap) => {
    if (error) {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to get PixelMap by callback with options. Code: ${error.code}, message: ${error.message}\`);
      return;
    }
// Return a PixelMap-format barcode image.
    hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in getting PixelMap by callback with options, size: ${result.getImageInfoSync().size}\`);
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to generateBarcode. Code: ${error.code}, message: ${error.message}\`);
}

#### generateBarcode.createBarcode

createBarcode(content: ArrayBuffer, options: CreateOptions): Promise<image.PixelMap>

Generates a barcode image from a byte array. This API returns the generated barcode image using a promise asynchronously.

**Atomic service API**: This API can be used in atomic services since API version 5.0.2(14).

**System capability**: SystemCapability.Multimedia.Scan.GenerateBarcode

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

content

 | 

ArrayBuffer

 | 

Yes

 | 

Byte array used to generate a barcode image. You can check "Table 2 Restrictions on the content parameter" below to learn more about restrictions on this parameter.

 |
| 

options

 | 

[CreateOptions](#section87678254617)

 | 

Yes

 | 

Parameters used to generate a barcode image. The **ScanType** parameter can only be set to **QR Code**.

 |

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<image.[PixelMap](../../../image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\>

 | 

**Promise** object, used to return the generated barcode image object.

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

import { image } from '@kit.ImageKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanCore, generateBarcode } from '@kit.ScanKit';
import { buffer } from '@kit.ArkTS';

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
            hilog.error(0x0001, TAG, \`Failed to create barCode. Code: ${error.code}, message: ${error.message}\`);
          });
        } catch (error) {
          hilog.error(0x0001, TAG, \`Failed to generateBarcode. Code: ${error.code}, message: ${error.message}\`);
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

**Table 2** The following table describes restrictions on the **content** parameter.
| 
Correction Level

 | 

Parameter Restrictions

 |
| :-- | :-- |
| 

LEVEL\_L

 | 

It is recommended that the number of bytes in the byte array do not exceed 2048.

 |
| 

LEVEL\_M

 | 

It is recommended that the number of bytes in the byte array do not exceed 2048.

 |
| 

LEVEL\_Q

 | 

It is recommended that the number of bytes in the byte array do not exceed 1536.

 |
| 

LEVEL\_H

 | 

It is recommended that the number of bytes in the byte array do not exceed 1024.

 |
