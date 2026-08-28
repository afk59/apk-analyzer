# scanBarcode (Scanning Barcodes Using the Default UI)

This module provides the capability of scanning barcodes using the default UI.

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

**Start version**: 4.0.0(10)

#### Modules to Import

import { scanBarcode } from '@kit.ScanKit';

#### ScanResult

Scanning result.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.0.0(10)

| 
**Parameter**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

**Description**

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

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

originalValue

 | 

string

 | 

No

 | 

No

 | 

Barcode recognition result.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

 |
| 

scanCodeRect

 | 

[ScanCodeRect](#section1456184716188)

 | 

No

 | 

Yes

 | 

Barcode position information.

**Start version**: 4.1.0(11)

 |
| 

cornerPoints

 | 

Array<[Point](#section9634457911)\>

 | 

No

 | 

Yes

 | 

Barcode position information, which contains the coordinates of the four corner points of the QR code. This parameter is returned only by the [detectBarcode.decodeImage](../detectbarcode-recognizing-barcodes-in-an-image/document.md#section387381185013) API.

**Start version**: 5.0.0(12)

 |
| 

isGS1

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether the barcode carries data that complies with GS1 standards.

The options are **true** (yes) and **false** (no). The default value is **false**.

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

**Start version**: 6.0.2(22)

 |
| 

source

 | 

scanCore.[ScanSource](../scancore-public-information-about-barcode-scanning/document.md#section152115548134)

 | 

No

 | 

Yes

 | 

Scanning result source. This parameter is returned only for the API called when barcodes are scanned using the default UI.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 6.0.2(22).

**Start version**: 6.0.2(22)

 |

#### ScanCodeRect

Barcode position information. The barcode position is not returned when the default barcode scanning APIs (**startScan** and **startScanForResult**) are used.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

| 
**Parameter**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

left

 | 

number

 | 

No

 | 

No

 | 

X coordinate of the upper left corner of the bounding rectangle, in px.

 |
| 

top

 | 

number

 | 

No

 | 

No

 | 

Y coordinate of the upper left corner of the bounding rectangle, in px.

 |
| 

right

 | 

number

 | 

No

 | 

No

 | 

X coordinate of the lower right corner of the bounding rectangle, in px.

 |
| 

bottom

 | 

number

 | 

No

 | 

No

 | 

Y coordinate of the lower right corner of the bounding rectangle, in px.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/13/v3/HSBpLs6aTPyaEUHMmYozIA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5CC73832C2E597F7E6306C68DB748D79DA8E3D794F8DEEBF767DB070609F07C)

The coordinate unit used in the result returned in the scenario of barcode scanning by custom UI is the same as that of the passed parameters **width** and **height** in [ViewControl](../customscan-scanning-barcodes-using-the-custom-ui/document.md#section8604949165313).

#### Point

Defines the coordinates of a point. This coordinate system uses the top-left corner as the origin {0, 0}. It's based on the device held horizontally, with the charging port on the right side.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

| 
**Parameter**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

x

 | 

number

 | 

No

 | 

No

 | 

X-axis coordinate. The unit is px.

 |
| 

y

 | 

number

 | 

No

 | 

No

 | 

Y-axis coordinate. The unit is px.

 |

#### ScanOptions

Barcode scan and recognition parameters.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.0.0(10)

| 
**Parameter**

 | 

**Type**

 | 

Read-Only

 | 

**Optional**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

scanTypes

 | 

Array<scanCore.[ScanType](../scancore-public-information-about-barcode-scanning/document.md#section113371139123212)\>

 | 

No

 | 

Yes

 | 

Barcode scan type. The default value is **ALL** (indicating that all types of barcodes are scanned).

 |
| 

enableMultiMode

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable the multi-barcode scanning mode. The default value is **false**.

-   **true**: yes
-   **false**: no

 |
| 

enableAlbum

 | 

boolean

 | 

No

 | 

Yes

 | 

Indicates whether to enable gallery-based barcode scanning. The default value is **true**.

-   **true**: yes
-   **false**: no

This parameter controls only gallery-based barcode scanning of the capability to scan barcodes using the default UI, and supports only single barcode recognition.

 |

**Example:**

import { scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define scanning parameters.
let options: scanBarcode.ScanOptions = { scanTypes: \[scanCore.ScanType.ALL\], enableMultiMode: true, enableAlbum: true };

function loadPage(uiContext : UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options).then((result: scanBarcode.ScanResult) => {
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}\`);
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}\`);
    });
  } catch (error) {
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to startScanForResult. Code: ${error.code}, message: ${error.message}\`);
  }
}

#### scanBarcode.startScanForResult

startScanForResult(context: common.Context, options?: ScanOptions): Promise<ScanResult>

Scans barcodes using the default UI based on input parameters. This API uses a promise to return the result asynchronously. This API must be called in the lifecycles of the UI and component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

Yes

 | 

App context.

 |
| 

options

 | 

[ScanOptions](#section1285191073117)

 | 

No

 | 

Parameters for starting barcode scanning.

 |

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[ScanResult](#section10614317162112)\>

 | 

**Promise** object, used to return the scanning result.

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
| 

1000500002

 | 

The user canceled the barcode scanning.

 |

**Example:**

import { scanBarcode, scanCore } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define scanning parameters.
let options: scanBarcode.ScanOptions = { scanTypes: \[scanCore.ScanType.ALL\], enableMultiMode: true, enableAlbum: true };

function loadPage(uiContext : UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options).then((result: scanBarcode.ScanResult) => {
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}\`);
    }).catch((error: BusinessError) => {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}\`);
    });
  } catch (error) {
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to startScanForResult. Code: ${error.code}, message: ${error.message}\`);
  }
}

#### scanBarcode.startScanForResult

startScanForResult(context: common.Context, callback: AsyncCallback<ScanResult>): void

Opens the default scanning UI to scan barcodes. This API uses a callback to return the result asynchronously. This API must be called in the lifecycles of the UI and component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

Yes

 | 

App context.

 |
| 

callback

 | 

AsyncCallback<[ScanResult](#section10614317162112)\>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined** and **data** is the obtained scanning result object [ScanResult](#section10614317162112); otherwise, **err** is an error object.

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
| 

1000500002

 | 

The user canceled the barcode scanning.

 |

**Example:**

import { scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Open the barcode scanning UI.
function loadPage(uiContext : UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), (error: BusinessError, result: scanBarcode.ScanResult) => {
      if (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}\`);
    });
  } catch (error) {
    hilog.error(0x0001, '\[Scan Sample\]', \`Failed to startScanForResult. Code: ${error.code}, message: ${error.message}\`);
  }
}

#### scanBarcode.startScanForResult

startScanForResult(context: common.Context, options: ScanOptions, callback: AsyncCallback<ScanResult>): void

Scans barcodes using the default UI based on input parameters. This API uses a callback to return the result asynchronously. This API must be called in the lifecycles of the UI and component.

**Model restriction**: This API can be used only in the stage model.

**Atomic service API**: This API can be used in atomic services since API version 4.1.0(11).

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

context

 | 

[common.Context](../../../../application-framework/ability-kit/arkts-apis/stage-model/ohos-app-ability-common-ability-common-module/document.md#context)

 | 

Yes

 | 

App context.

 |
| 

options

 | 

[ScanOptions](#section1285191073117)

 | 

Yes

 | 

Parameters for starting barcode scanning.

 |
| 

callback

 | 

AsyncCallback<[ScanResult](#section10614317162112)\>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined** and **data** is the obtained scanning result object [ScanResult](#section10614317162112); otherwise, **err** is an error object.

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
| 

1000500002

 | 

The user canceled the barcode scanning.

 |

**Example:**

import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Define scanning parameters.
let options: scanBarcode.ScanOptions = { scanTypes: \[scanCore.ScanType.ALL\], enableMultiMode: true, enableAlbum: true };
// Open the barcode scanning UI.
function loadPage(uiContext : UIContext) {
  try {
    scanBarcode.startScanForResult(uiContext.getHostContext(), options, (error: BusinessError, result: scanBarcode.ScanResult) => {
      if (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanResult by callback with options. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(result)}\`);
    });
  } catch (error) {
    hilog.error(0x0001, '\[Scan Sample\]', \`Failed to startScanForResult. Code: ${error.code}, message: ${error.message}\`);
  }
}

#### scanBarcode.startScan(deprecated)

startScan(options?: ScanOptions): Promise<ScanResult>

Scans barcodes using the default UI based on input parameters. This API uses a promise to return the scanning result asynchronously.

**Deprecation description**: This API is deprecated from API version 4.1.0(11). You are advised to use [startScanForResult](#section829511911349) instead.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.0.0(10)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[ScanOptions](#section1285191073117)

 | 

No

 | 

Parameters for starting barcode scanning.

 |

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<[ScanResult](#section10614317162112)\>

 | 

**Promise** object, used to return the scanning result.

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

**Example:**

import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Set input parameters for starting barcode scanning.
let options: scanBarcode.ScanOptions = { scanTypes: \[scanCore.ScanType.ALL\], enableMultiMode: true, enableAlbum: true };
try {
  scanBarcode.startScan(options).then((result: scanBarcode.ScanResult) => {
    hilog.info(0x0001, '\[Scan Sample\]',
      \`Succeeded in getting ScanResult by promise with options, result is ${JSON.stringify(result)}\`);
  }).catch((error: BusinessError) => {
  // Return the error occurred during barcode scanning.
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to get ScanResult by promise with options. Code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to startScan. Code: ${error.code}, message: ${error.message}\`);
}

#### scanBarcode.startScan(deprecated)

startScan(callback: AsyncCallback<ScanResult>): void

Opens the default scanning UI to scan barcodes. This API uses a callback to return the barcode scanning result asynchronously.

**Deprecation description**: This API is deprecated from API version 4.1.0(11). You are advised to use [startScanForResult](#section399311216327) instead.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.0.0(10)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

Mandatory

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

callback

 | 

AsyncCallback<[ScanResult](#section10614317162112)\>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined** and **data** is the obtained scanning result object [ScanResult](#section10614317162112); otherwise, **err** is an error object.

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

**Example:**

import { scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  scanBarcode.startScan((error: BusinessError, result: scanBarcode.ScanResult) => {
  // Error callback for returning the error occurred during barcode scanning.
    if (error) {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}\`);
      return;
    }
    hilog.info(0x0001, '\[Scan Sample\]',
      \`Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}\`);
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to startScan. Code: ${error.code}, message: ${error.message}\`);
}

#### scanBarcode.startScan(deprecated)

startScan(options: ScanOptions, callback: AsyncCallback<ScanResult>): void

Scans barcodes using the default UI based on input parameters. This API uses a callback to return the scanning result asynchronously.

**Deprecation description**: This API is deprecated from API version 4.1.0(11). You are advised to use [startScanForResult](#section1738211373353) instead.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.0.0(10)

**Parameters:**

| 
**Parameter**

 | 

**Type**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- |
| 

options

 | 

[ScanOptions](#section1285191073117)

 | 

Yes

 | 

Parameters for starting barcode scanning.

 |
| 

callback

 | 

AsyncCallback<[ScanResult](#section10614317162112)\>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined** and **data** is the obtained scanning result object [ScanResult](#section10614317162112); otherwise, **err** is an error object.

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

**Example:**

import { scanCore, scanBarcode } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';

// Set input parameters for starting barcode scanning.
let options: scanBarcode.ScanOptions = { scanTypes: \[scanCore.ScanType.ALL\], enableMultiMode: true, enableAlbum: true };
try {
  scanBarcode.startScan(options, (error: BusinessError, result: scanBarcode.ScanResult) => {
  // Error callback for returning the error occurred during barcode scanning.
    if (error) {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to get ScanResult by callback with options. Code: ${error.code}, message: ${error.message}\`);
      return;
    }
    hilog.info(0x0001, '\[Scan Sample\]',
      \`Succeeded in getting ScanResult by callback with options, result is ${JSON.stringify(result)}\`);
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to startScan. Code: ${error.code}, message: ${error.message}\`);
}
