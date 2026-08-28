# customScan (Scanning Barcodes Using the Custom UI)

This module provides the capability of scanning barcodes using the custom UI.

To make it easier for you to integrate the capability, a detailed [demo project](https://gitcode.com/HarmonyOS_Samples/scan-kit_-sample-code_-clientdemo_-arkts) is provided for your reference.

**Start version**: 4.1.0(11)

#### Modules to Import

import { customScan } from '@kit.ScanKit';

#### ViewControl

Camera control parameters.

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

width

 | 

number

 | 

No

 | 

No

 | 

Width of the [XComponent](../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md). Supported units are px, lpx, and vp. The default unit is vp.

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

Height of the XComponent. Supported units are px, lpx, and vp. The default unit is vp.

 |
| 

surfaceId

 | 

string

 | 

No

 | 

No

 | 

ID of the surface held by the XComponent.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/akwGry4VTnSCDF4ZRgzFxg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=623B7FD276E3B34CD01C13C2ACC4BB19392FDEFAF696AF72DABD01BEAB911695)

1.  When setting parameters for ViewControl, ensure that the values of **width** and **height** are the same as those of XComponent. The **start** API will match the closest camera resolution based on the set values of **width** and **height**. If the ratio differs from the camera resolution ratio greatly, the preview stream experience may be compromised. XComponent, the capabilities of which are provided by the UI, offers the surface for preview streams. For details, please refer to [XComponent](../../../../application-framework/arkui/arkts-components/rendering-drawing/xcomponent/document.md).
2.  For foldable devices, you need to adjust the width and height of XComponent as needed when the folding status changes. The **start** API will readapt the camera resolution ratio.

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // Set the preview stream height. The default unit is vp.
  @State cameraHeight: number = 640;
  // Set the preview stream width. The default unit is vp.
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '\[Scan Sample\]', 'onLoad is called')
          // Obtain the surface ID of XComponent.
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, 'viewControl', \`onLoad surfaceId: ${surfaceId}\`);
          // Set parameters of ViewControl.
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
              hilog.info(0x0001, '\[Scan Sample\]',
                \`Succeeded in getting ScanResult by promise, scanResult is ${JSON.stringify(scanResult)}\`);
            }).catch((error: BusinessError) => {
              hilog.error(0x0001, '\[Scan Sample\]',
                \`Failed to get ScanResult by promise. Code: ${error.code}, message: ${error.message}\`);
            })
          } catch (error) {
            hilog.error(0x0001, '\[Scan Sample\]',
              \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}

#### ScanFrame

Camera preview stream (YUV).

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

byteBuffer

 | 

ArrayBuffer

 | 

No

 | 

No

 | 

ArrayBuffer array of the camera preview stream.

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

Width of the camera preview stream, in px.

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

Height of the camera preview stream, in px.

 |
| 

scanCodeRects

 | 

Array<scanBarcode.[ScanCodeRect](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section1456184716188)\>

 | 

No

 | 

Yes

 | 

Position information for barcode image detection in the camera preview stream.

**Device behavior differences**: This attribute can be returned only for devices with the Kirin neural-network processing unit (NPU). For other devices, null is returned.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // Set the preview stream height. The default unit is vp.
  @State cameraHeight: number = 640;
  // Set the preview stream width. The default unit is vp.
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  private callback: AsyncCallback<scanBarcode.ScanResult\[\]> =
    (error: BusinessError, result: scanBarcode.ScanResult\[\]) => {
      if (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}\`);
    }
  // Obtain ScanFrame via a callback.
  private frameCallback: AsyncCallback<customScan.ScanFrame> =
    (error: BusinessError, frameResult: customScan.ScanFrame) => {
      if (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanFrame by callback. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      // Camera YUV array in byteBuffer.
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanFrame.byteBuffer.byteLength:  ${frameResult.byteBuffer.byteLength}\`);
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanFrame.scanCodeRect: ${JSON.stringify(frameResult.scanCodeRects)}\`);
    }

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '\[Scan Sample\]', 'Succeeded in loading, onLoad is called');
          // Obtain the surface ID of XComponent.
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in getting surfaceId: ${surfaceId}\`);
          // Set parameters of ViewControl.
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback, this.frameCallback);
          } catch (error) {
            hilog.error(0x0001, '\[Scan Sample\]',
              \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b2/v3/_Rllf7MkR4OmJmdwAgK6hQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3B5ED5AD6C743A2D7F39BFA8CE5F734C95107889DE7CFFF2F7BC3701E1E5D0F9)

1.  **scanCodeRects** returns the position information of the barcode image detected from the preview stream in landscape mode. To perform further processing in portrait orientation (assuming that the device is upright and the charging port faces down), you must map these coordinates to a portrait-based coordinate system. Each element in the array contains the **left**, **top**, **right**, and **bottom** fields and they all need to be mapped. The following sample code uses the first element (**scanCodeRects\[0\]**) of **scanCodeRects** as an example to demonstrate the mapping logic.
2.  The bounding box of the QR code area can be defined and outlined using **position({x: left, y: top})**, **width: right - left**, and **height: bottom - top**.

// The start API returns the frameResult data using frameCallback.
import { customScan, scanBarcode } from '@kit.ScanKit';
// Simulate the returned frameResult: customScan.ScanFrame data of the camera preview stream.
let frameResult: customScan.ScanFrame = {
  "width": 1920,
  "height": 1080,
  // **buffer** indicates the camera stream.
  "byteBuffer": buffer,
  "scanCodeRects": \[{
    "left": 84,
    "top": 142,
    "right": 1695,
    "bottom": 996
  }\]
};
if (frameResult && frameResult.scanCodeRects) {
  let rect: scanBarcode.ScanCodeRect = frameResult.scanCodeRects\[0\];
  // Convert the dimensions of the preview stream to match the dimensions of XComponent. For example, set scanWidth to 360 vp.
  let scanWidth = 360;
  let ratio = scanWidth / frameResult.height;
  let left = (frameResult.height - rect.bottom) \* ratio;
  let top = rect.left \* ratio;
  let right = (frameResult.height - rect.top) \* ratio;
  let bottom = rect.right \* ratio;
}

#### customScan.init

init(options?: scanBarcode.ScanOptions): void

Initializes the custom UI for barcode scanning.

**Required permission**: ohos.permission.CAMERA

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

options

 | 

scanBarcode.[ScanOptions](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section1285191073117)

 | 

No

 | 

Parameters for scanning barcodes using the custom UI.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

Error code 201 is added for the **init** API of the **customScan** module in version 5.0.2(14) and later.

-   For versions earlier than 5.0.2(14), if the **init** API of the **customScan** module is called without the camera permission, error code 1000500001 is returned.
-   For version 5.0.2(14) and later, if the **init** API of the **customScan** module is called without the camera permission, error code 201 is returned.

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
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

import { scanBarcode, scanCore, customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let options: scanBarcode.ScanOptions = {
  scanTypes: \[scanCore.ScanType.ALL\],
  enableMultiMode: true,
  enableAlbum: true
};
try {
  customScan.init(options);
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to init customScan. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.start

start(viewControl: ViewControl): Promise<Array<scanBarcode.ScanResult>>

Starts barcode scanning camera streams. This API uses a promise to return the scanning result asynchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/zebzIo5bQ7mxhYM0DSkeNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB4FEFF4E781C4E2E179B54608B07A0B08570932146C497D675CDC7048FA7049)

This API can be used only after the **init** API is called.

**Required permission**: ohos.permission.CAMERA

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

viewControl

 | 

[ViewControl](#section8604949165313)

 | 

Yes

 | 

Camera control parameters.

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

**Promise** object, used to return the scanning result.

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

Error code 201 is added for the **start** API of the **customScan** module in version 5.0.2(14) and later.

-   For versions earlier than 5.0.2(14), if the **start** API of the **customScan** module is called without the camera permission, error code 1000500001 is returned.
-   For version 5.0.2(14) and later, if the **start** API of the **customScan** module is called without the camera permission, error code 201 is returned.

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
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

import { hilog } from '@kit.PerformanceAnalysisKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // Set the preview stream height. The default unit is vp.
  @State cameraHeight: number = 640
  // Set the preview stream width. The default unit is vp.
  @State cameraWidth: number = 360
  private mXComponentController: XComponentController = new XComponentController();

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '\[Scan Sample\]', 'Succeeded in loading, onLoad is called');
          // Obtain the surface ID of XComponent.
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in getting surfaceId: ${surfaceId}\`);
          // Set parameters of ViewControl.
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl).then((scanResult: Array<scanBarcode.ScanResult>) => {
              hilog.info(0x0001, '\[Scan Sample\]',
                \`Succeeded in getting ScanResult by promise, scanResult is ${JSON.stringify(scanResult)}\`);
            }).catch((error: BusinessError) => {
              hilog.error(0x0001, '\[Scan Sample\]',
                \`Failed to get ScanResult by promise. Code: ${error.code}, message: ${error.message}\`);
            });
          } catch (error) {
            hilog.error(0x0001, '\[Scan Sample\]',
              \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}

#### customScan.start

start(viewControl: ViewControl, callback: AsyncCallback<Array<scanBarcode.ScanResult>>, frameCallback?: AsyncCallback<ScanFrame>): void

Starts barcode scanning camera streams. This API uses a callback to return the scanning result and camera preview stream (YUV NV21 format based on 4:2:0 sampling) asynchronously.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/NUnKpwnYQ823asjeOw9N_A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0A0FA5C5E7ECE1B8BAF5013385BEAC28DBC5EE6DD69BB0A7F39ADE851333E7CA)

This API can be used only after the **init** API is called.

**Required permission**: ohos.permission.CAMERA

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

viewControl

 | 

[ViewControl](#section8604949165313)

 | 

Yes

 | 

Camera control parameters.

 |
| 

callback

 | 

AsyncCallback<Array<scanBarcode.[ScanResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section10614317162112)\>>

 | 

Yes

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the obtained Array<scanBarcode.[ScanResult](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section10614317162112)\>; otherwise, **err** is an error object.

 |
| 

frameCallback

 | 

AsyncCallback<[ScanFrame](#section1670633211200)\>

 | 

No

 | 

Callback used to return the result. If the operation is successful, **err** is **undefined** and **data** is the obtained camera preview stream (YUV) data [ScanFrame](#section1670633211200); otherwise, **err** is an error object.

**Start version**: 5.0.0(12)

 |

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

Error code 201 is added for the **start** API of the **customScan** module in version 5.0.2(14) and later.

-   For versions earlier than 5.0.2(14), if the **start** API of the **customScan** module is called without the camera permission, error code 1000500001 is returned.
-   For version 5.0.2(14) and later, if the **start** API of the **customScan** module is called without the camera permission, error code 201 is returned.

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

201

 | 

Permission denied.

 |
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

import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // Set the preview stream height. The default unit is vp.
  @State cameraHeight: number = 640;
  // Set the preview stream width. The default unit is vp.
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  // Return the custom scanning result in a callback.
  private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
    (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}\`);
    }
  // Obtain ScanFrame via a callback.
  private frameCallback: AsyncCallback<customScan.ScanFrame> =
    (error: BusinessError, scanFrame: customScan.ScanFrame) => {
      if (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanFrame by callback. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanFrame by callback, scanFrame is ${JSON.stringify(scanFrame)}\`);
    }

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '\[Scan Sample\]', 'Succeeded in loading, onLoad is called');
          // Obtain the surface ID of XComponent.
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in getting surfaceId: ${surfaceId}\`);
          // Set parameters of ViewControl.
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback, this.frameCallback);
          } catch (error) {
            hilog.error(0x0001, '\[Scan Sample\]',
              \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}

#### customScan.getFlashLightStatus

getFlashLightStatus(): boolean

Obtains the camera flash light status.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bc/v3/DKuopEJoR0O0bsBYt5b6bg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9DB323B6102C236CD0A2A0083FDCD9445AF2ED139D1BFA5D16FCC8D1100C6E1B)

This API must be used after the **start** API. An internal error will occur if this API is used during initialization, stop, and release of camera streams.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

boolean

 | 

**true** if the flash light is opened; **false** otherwise.

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

1000500001

 | 

Internal error.

 |

**Example:**

import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
  // Turn on or off the flash light based on the flash light status.
  if (flashLightStatus) {
    try {
      customScan.closeFlashLight();
    } catch (error) {
      hilog.error(0x0001, '\[Scan Sample\]', \`Failed to closeFlashLight. Code: ${error.code}, message: ${error.message}\`);
    }
  } else {
    try {
      customScan.openFlashLight();
    } catch (error) {
      hilog.error(0x0001, '\[Scan Sample\]', \`Failed to openFlashLight. Code: ${error.code}, message: ${error.message}\`);
    }
  }
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to getFlashLightStatus. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.openFlashLight

openFlashLight(): void

Turns on the camera flash light.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/6nGJScaWSDyKgS3H8Bv0pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A2D98234E0AA1B63A934F11EB785AA91CDB35712105ECB4AFF7A8F9C59E78EAF)

This API must be used after the **start** API. An internal error will occur if this API is used during initialization, stop, and release of camera streams.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1000500001

 | 

Internal error.

 |

**Example:**

import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
  // Turn on or off the flash light based on the flash light status.
  if (flashLightStatus) {
    try {
      customScan.closeFlashLight();
    } catch (error) {
      hilog.error(0x0001, '\[Scan Sample\]', \`Failed to closeFlashLight. Code: ${error.code}, message: ${error.message}\`);
    }
  } else {
    try {
      customScan.openFlashLight();
    } catch (error) {
      hilog.error(0x0001, '\[Scan Sample\]', \`Failed to openFlashLight. Code: ${error.code}, message: ${error.message}\`);
    }
  }
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to getFlashLightStatus. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.closeFlashLight

closeFlashLight(): void

Turns off the camera flash light.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/70/v3/dy7YOGEsQfOVM64rohtIeg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3048EF1C0EFCE8A04C0FEC61BDE8A7F9A84F6F4791BD3944DDD2609F5C1EA009)

This API must be used after the **start** API. An internal error will occur if this API is used during initialization, stop, and release of camera streams.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1000500001

 | 

Internal error.

 |

**Example:**

import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

let flashLightStatus: boolean = false;
try {
  flashLightStatus = customScan.getFlashLightStatus();
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to getFlashLightStatus. Code: ${error.code}, message: ${error.message}\`);
}
// Turn on or off the flash light based on the flash light status.
if (flashLightStatus) {
  try {
    customScan.closeFlashLight();
  } catch (error) {
    hilog.error(0x0001, '\[Scan Sample\]', \`Failed to closeFlashLight. Code: ${error.code}, message: ${error.message}\`);
  }
} else {
  try {
    customScan.openFlashLight();
  } catch (error) {
    hilog.error(0x0001, '\[Scan Sample\]', \`Failed to openFlashLight. Code: ${error.code}, message: ${error.message}\`);
  }
}

#### customScan.setZoom

setZoom(zoomValue: number): void

Sets a zoom ratio for the device, with a maximum precision of two decimal places.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/62/v3/hqrdxJLtQ-adfsGaRU9EYQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C4472F20D86669E70C3C397C5CABC21F9C76B3AD120AEA5A4BC1FA40DB0EEB2D)

This API must be used after the **start** API.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

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

zoomValue

 | 

number

 | 

Yes

 | 

Camera zoom ratio, with a maximum precision of two decimal places (for example, 1.45).

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

import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

// Set a zoom ratio for the device.
let zoomValue = 2.0;
try {
  customScan.setZoom(zoomValue);
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to setZoom. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.getZoom

getZoom(): number

Obtains the zoom ratio in use.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/rts1yPyEQ1-QPq2T8prJiQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2C3CD1C358453173115B1E1D79515DC41B5291C1FBA242A0813B6AEEC95B0529)

This API must be used after the **start** API.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

number

 | 

Zoom ratio in use.

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

1000500001

 | 

Internal error.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

try {
// Obtain the zoom ratio.
  let zoomValue = customScan.getZoom();
  hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in getting zoomValue, zoomValue is ${zoomValue}\`);
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to get zoomValue. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.setFocusPoint

setFocusPoint(point: scanBarcode.Point): void

Sets the focal point for the camera. The focal point must be in the coordinate system (0-1), where the upper left corner is {0, 0} and the lower right corner is {1, 1}. This coordinate system assumes a landscape device orientation with the charging port on the right. If your app's preview page is designed for the portrait mode with the charging port at the bottom, with a width of {w} and height of {h}, then a touch point at coordinates {x, y} in the portrait mode would be converted to {y/h, 1 - x/w} in landscape mode.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/pnuSdINNRsi-O8Pm8WqARA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=442DEAF91F082BA2D08A596C3409A6FC01A5668EDA4DED45C0E1422328BDAF5F)

This API must be used after the **start** API.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

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

point

 | 

scanBarcode.[Point](../scanbarcode-scanning-barcodes-using-the-default-ui/document.md#section9634457911)

 | 

Yes

 | 

Focal point. The value range of x and y must be within \[0, 1\]. If a value less than 0 is passed, the value **0** is used. If a value greater than **1** is passed, the value **1** is used.

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

import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
// Set the focal point.
  customScan.setFocusPoint({ x: 0.5, y: 0.5 });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to setFocusPoint. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.resetFocus

resetFocus(): void

Sets the focus mode to continuous auto-focus.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a6/v3/f0NJVhpgS6uPet16jxxzBw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F1A26E217660117F0B8FCDEDA3DC7BE48681DC3F7C9E2749F6CDC4A5B313899)

This API must be used after the **start** API.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1000500001

 | 

Internal error.

 |

**Example:**

import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
// Set the focus mode to continuous auto-focus.
  customScan.resetFocus();
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to resetFocus. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.on('lightingFlash')

on(type: 'lightingFlash', callback: AsyncCallback<boolean>): void

Subscribes to the flash light status listener. This API uses a callback to return the flash light turn-on or turn-off time asynchronously when the light conditions change.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/04/v3/ZgfX4G7YRcybXQgq8ekDjw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A79A40F7011502629B6BFEC2F6D4C0112F156C5A6C3089DDB2C0DF7D27E1479C)

This API must be used after the **start** API. An internal error will occur if this API is used when camera streams are not started.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

Event type, which is fixed to **lightingFlash**. This event is triggered when the light conditions change, based on which users can be instructed to turn on or off the flash light.

 |
| 

callback

 | 

AsyncCallback<boolean>

 | 

Yes

 | 

Callback function. If **true** is returned, the light is dim and the flash light can be turned on. If **false** is returned, the environment is light and the flash light can be turned off.

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

1000500001

 | 

Internal error.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

let callback = (error: BusinessError, bool: boolean) => {
  if (error) {
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to light Flash by callback. Code: ${error.code}, message: ${error.message}\`);
    return;
  }
  hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in lighting Flash by callback, bool is ${bool}\`);
}

try {
  customScan.on('lightingFlash', callback);
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]',
    \`Failed to listen lightingFlash. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.off('lightingFlash')

off(type: 'lightingFlash', callback?: AsyncCallback<boolean>): void

Unsubscribes from flash light status change events. This API returns the result asynchronously through a callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/60/v3/jIBMnj2gTMaIjIcJU_0ErQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F60D1ABD7C5AA0905D79B210B844F0DC98523A25039A5546FAEBE40469AE8EE7)

This API must be used after the **start** API. An internal error will occur if this API is used when camera streams are not started.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

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

type

 | 

string

 | 

Yes

 | 

Event type, which is fixed to **lightingFlash**. This event is triggered when the light conditions change, based on which users can be instructed to turn on or off the flash light.

 |
| 

callback

 | 

AsyncCallback<boolean>

 | 

No

 | 

Callback function to be unregistered. If **callback** is left empty, all callback functions bound to **lightingFlash** will be deregistered.

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

1000500001

 | 

Internal error.

 |

**Example:**

import { BusinessError } from '@kit.BasicServicesKit';
import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';

let callback = (error: BusinessError, bool: boolean) => {
  if (error) {
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to cancel Flash by callback. Code: ${error.code}, message: ${error.message}\`);
    return;
  }
  hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in cancelling Flash by callback, bool is ${bool}\`);
}
// If the callback is not specified, listening on all lightingFlash events is canceled. If the callback is specified, the event types to be listened to must be the same as those in customScan.on.
try {
  customScan.off('lightingFlash', callback);
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]',
    \`Failed to listen lightingFlash. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.rescan

rescan(): void

Initiates barcode scanning again. If the scanning result is not as expected, you can call this API to trigger scanning again.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/92/v3/YdXZKP9ZTC6jex24FuaumQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E7D6F4644A3AFA7BB32CEB66E8B1F585064398AB2B66BE579160252F1CC07E62)

This API must be used after the **start** API and before the **stop** API. An internal error will occur if this API is used when camera streams are not started.

This API applies only when the **start** API uses a callback to return the result.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.0.0(12)

**Error codes:**

For details about the error codes, please refer to [ArkTS API Error Codes](../arkts-api-error-codes/document.md).

| 
Error Code

 | 

Error Message

 |
| :-- | :-- |
| 

1000500001

 | 

Internal error.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { AsyncCallback, BusinessError } from '@kit.BasicServicesKit';
import { scanBarcode, customScan } from '@kit.ScanKit';

@Entry
@Component
struct CustomScanPage {
  // Set the preview stream height. The default unit is vp.
  @State cameraHeight: number = 640;
  // Set the preview stream width. The default unit is vp.
  @State cameraWidth: number = 360;
  private mXComponentController: XComponentController = new XComponentController();
  // Return the custom scanning result in a callback.
  private callback: AsyncCallback<Array<scanBarcode.ScanResult>> =
    (error: BusinessError, result: Array<scanBarcode.ScanResult>) => {
      if (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to get ScanResult by callback. Code: ${error.code}, message: ${error.message}\`);
        return;
      }
      hilog.info(0x0001, '\[Scan Sample\]',
        \`Succeeded in getting ScanResult by callback, result is ${JSON.stringify(result)}\`);
      // Trigger scanning again. If your scanning page needs to trigger scanning again without restarting the camera, call the rescan API in the asynchronous callback of the start API.
      try {
        customScan.rescan();
      } catch (error) {
        hilog.error(0x0001, '\[Scan Sample\]',
          \`Failed to rescan customScan. Code: ${error.code}, message: ${error.message}\`);
      }
    }

  build() {
    Stack() {
      XComponent({
        id: 'componentId',
        type: XComponentType.SURFACE,
        controller: this.mXComponentController
      })
        .onLoad(() => {
          hilog.info(0x0001, '\[Scan Sample\]', 'Succeeded in loading, onLoad is called');
          // Obtain the surface ID of XComponent.
          let surfaceId: string = this.mXComponentController.getXComponentSurfaceId();
          hilog.info(0x0001, '\[Scan Sample\]', \`Succeeded in getting surfaceId: ${surfaceId}\`);
          // Set parameters of ViewControl.
          let viewControl: customScan.ViewControl = {
            width: this.cameraWidth,
            height: this.cameraHeight,
            surfaceId: surfaceId
          };
          try {
            customScan.start(viewControl, this.callback);
          } catch (error) {
            hilog.error(0x0001, '\[Scan Sample\]',
              \`Failed to start customScan. Code: ${error.code}, message: ${error.message}\`);
          }
        })
        .height(this.cameraHeight)
        .width(this.cameraWidth)
        .position({ x: 0, y: 0 })
    }
    .alignContent(Alignment.Bottom)
    .height('100%')
    .width('100%')
    .position({ x: 0, y: 0 })
  }
}

#### customScan.setAutoZoomEnabled

setAutoZoomEnabled(enabled: boolean): void

Enables or disables the auto zoom function. The function is enabled by default.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/99/v3/mQibuXWURU6WWVMRrSMSkw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A7D03588207E8945C4A2A5A2A5395523B999FDF4B54D32BD1E2881FBD143533A)

This API must be used after the **start** API. An internal error will occur if this API is used when camera streams are not started.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 5.1.0(18)

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

enabled

 | 

boolean

 | 

Yes

 | 

Indicates whether to enable auto zoom. The options are **true** (yes) and **false** (no).

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

1000500001

 | 

Internal error.

 |

**Example:**

import { customScan } from '@kit.ScanKit';
import { hilog } from '@kit.PerformanceAnalysisKit';

try {
  // Enable or disable the auto zoom function. The options are true and false.
  customScan.setAutoZoomEnabled(false);
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]', \`Failed to setAutoZoomEnabled. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.stop

stop(): Promise<void>

Stops barcode scanning camera streams. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d8/v3/0dvCDboUT5Sq_I8i87nJYw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98A22B09674539036B5EC757840FDADF6A757163AE5BC6671C29323E16E92BE1)

This API must be used after the **start** API. An internal error will occur if this API is used when camera streams are not started.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

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

1000500001

 | 

Internal error.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.stop().then(() => {
    hilog.info(0x0001, '\[Scan Sample\]', 'Succeeded in stopping scan by promise');
  }).catch((error: BusinessError) => {
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to stop scan by promise. Code: ${error.code}, message: ${error.message}\`);
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]',
    \`Failed to stop customScan. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.stop

stop(callback: AsyncCallback<void>): void

Stops barcode scanning camera streams. This API returns the result asynchronously through a callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/24/v3/r6iSGBV6Tn65UyrCyuNjLA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E70EF1CCB4FE0C6298A27333A676E168AD002D8255A25FE9DF7CCF921C303C2)

This API must be used after the **start** API. An internal error will occur if this API is used when camera streams are not started.

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

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

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

1000500001

 | 

Internal error.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.stop((error: BusinessError) => {
    if (error) {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to stop scan by callback. Code: ${error.code}, message: ${error.message}\`);
      return;
    }
    hilog.info(0x0001, '\[Scan Sample\]', 'Succeeded in stopping scan by callback');
  })
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]',
    \`Failed to stop customScan. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.release

release(): Promise<void>

Releases barcode scanning camera streams. This API returns the result asynchronously through a promise.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/nAB7QNoxQ0-FovmbCXWvjQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39D9AF48FBDF6A59875436329670E7A0C8701FBA55DADE1CDDEA7FA987F7B95D)

You are advised to call this API after the **start** and **stop** APIs. An internal error will occur if this API is used when camera streams are not started.

**System capability**: SystemCapability.Multimedia.Scan.ScanBarcode

**Start version**: 4.1.0(11)

**Returns:**

| 
**Type**

 | 

**Description**

 |
| :-- | :-- |
| 

Promise<void>

 | 

**Promise** object. No result is returned.

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

1000500001

 | 

Internal error.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.release().then(() => {
    hilog.info(0x0001, '\[Scan Sample\]', 'Succeeded in releasing scan by promise');
  }).catch((error: BusinessError) => {
    hilog.error(0x0001, '\[Scan Sample\]',
      \`Failed to release scan by promise. Code: ${error.code}, message: ${error.message}\`);
  })
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]',
    \`Failed to release customScan. Code: ${error.code}, message: ${error.message}\`);
}

#### customScan.release

release(callback: AsyncCallback<void>): void

Releases barcode scanning camera streams. This API returns the result asynchronously through a callback.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/gBVlfPLUQlONj4XcBTbT5A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062445Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CBC9D7DA5F31D275E61838F13D794E820EFAF5F7C51966625921D46D82B2714)

You are advised to call this API after the **start** and **stop** APIs. An internal error will occur if this API is used when camera streams are not started.

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

callback

 | 

AsyncCallback<void>

 | 

Yes

 | 

Callback function. If the operation is successful, **err** is **undefined**; otherwise, **err** is an error object.

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

1000500001

 | 

Internal error.

 |

**Example:**

import { hilog } from '@kit.PerformanceAnalysisKit';
import { customScan } from '@kit.ScanKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
  customScan.release((error: BusinessError) => {
    if (error) {
      hilog.error(0x0001, '\[Scan Sample\]',
        \`Failed to release scan by callback. Code: ${error.code}, message: ${error.message}\`);
      return;
    }
    hilog.info(0x0001, '\[Scan Sample\]', 'Succeeded in releasing scan by callback');
  });
} catch (error) {
  hilog.error(0x0001, '\[Scan Sample\]',
    \`Failed to release customScan. Code: ${error.code}, message: ${error.message}\`);
}
