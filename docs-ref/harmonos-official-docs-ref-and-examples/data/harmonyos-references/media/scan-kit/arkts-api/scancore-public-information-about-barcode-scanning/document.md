# scanCore (Public Information About Barcode Scanning)

This module provides public information about barcode scanning.

**Start version**: 4.0.0(10)

#### Modules to Import

import { scanCore } from '@kit.ScanKit';

#### ScanType

Barcode type enumeration.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Multimedia.Scan.Core

**Start version**: 4.0.0(10)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

FORMAT\_UNKNOWN

 | 

0

 | 

Unknown type. This parameter is used for scenarios where the type of code to be scanned is unknown beforehand. It cannot be used for barcode image generation.

 |
| 

AZTEC\_CODE

 | 

1

 | 

Aztec code.

 |
| 

CODABAR\_CODE

 | 

2

 | 

Codabar code.

 |
| 

CODE39\_CODE

 | 

3

 | 

Code 39 code.

 |
| 

CODE93\_CODE

 | 

4

 | 

Code 93 code.

 |
| 

CODE128\_CODE

 | 

5

 | 

Code 128 code.

 |
| 

DATAMATRIX\_CODE

 | 

6

 | 

Data Matrix code.

 |
| 

EAN8\_CODE

 | 

7

 | 

EAN-8 code.

 |
| 

EAN13\_CODE

 | 

8

 | 

EAN-13 code.

 |
| 

ITF14\_CODE

 | 

9

 | 

ITF-14 code.

 |
| 

PDF417\_CODE

 | 

10

 | 

PDF417 code.

 |
| 

QR\_CODE

 | 

11

 | 

QR code.

 |
| 

UPC\_A\_CODE

 | 

12

 | 

UPC-A code.

 |
| 

UPC\_E\_CODE

 | 

13

 | 

UPC-E code.

 |
| 

MULTIFUNCTIONAL\_CODE

 | 

14

 | 

Multifunctional code. The barcode image generation capability does not support this type currently.

 |
| 

ONE\_D\_CODE

 | 

100

 | 

Barcode, including the CODABAR, CODE 39, CODE 93, CODE 128, EAN-8, EAN-13, ITF-14, UPC-A and UPC-E formats. This parameter cannot be used to generate barcode images.

 |
| 

TWO\_D\_CODE

 | 

101

 | 

QR code, including the AZTEC, DATA MATRIX, PDF417, QR CODE, and multifunctional code formats. This parameter cannot be used to generate barcode images.

 |
| 

ALL

 | 

1001

 | 

All preceding types. This parameter cannot be used to generate barcode images.

 |

#### ScanErrorCode

Scanning error code enumeration.

**System capability**: SystemCapability.Multimedia.Scan.Core

**Start version**: 4.1.0(11)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

INTERNAL\_ERROR

 | 

1000500001

 | 

Internal error.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

SCAN\_SERVICE\_CANCELED

 | 

1000500002

 | 

The user canceled the barcode scanning.

**Atomic service API**: This API can be used in atomic services since API version 5.0.0(12).

**Start version**: 5.0.0(12)

 |

#### ScanSource

Enumerates scanning result sources.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

**System capability**: SystemCapability.Multimedia.Scan.Core

**Start version**: 6.0.2(22)

| 
**Parameter**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

CAMERA

 | 

0

 | 

Barcodes are scanned directly using the camera stream.

 |
| 

PHOTO

 | 

1

 | 

Barcodes are scanned from a photo.

 |
