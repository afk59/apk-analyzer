# @ohos.screenshot (Screenshot)

Provides the screen capture capability.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/sYRmH7ycSL-RhfQYyaoO8w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062231Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4510352509D40FEE66888F0AFA44D0F4702E1653243F65198E87867DC2E5E054)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { screenshot } from '@kit.ArkUI';

#### Rect

Describes the region of the screen to capture.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | Left boundary of the screen region to capture, in px. The value must be an integer. |
| top | number | No | No | Top boundary of the screen region to capture, in px. The value must be an integer. |
| width | number | No | No | Width of the screen region to capture, in px. The value must be an integer. |
| height | number | No | No | Height of the screen region to capture, in px. The value must be an integer. |

#### CaptureOption14+

Describes the capture options.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| displayId | number | No | Yes | 
ID of the [display](../ohos-display-display/document.md#display) to capture. The default value is **0**. The value must be an integer greater than or equal to 0. If a non-integer is passed, a parameter error is reported.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| blackWindowIds21+ | Array<number> | No | Yes | 

List of window IDs that are not displayed during screen capture. By default, this list is empty. Valid window IDs must be positive integers. Currently, this parameter applies only to [floating ball windows](../../window-manager/ohos-window-floatingball-floating-ball-window/document.md). If a window ID does not correspond to a floating ball window, is not a positive integer, or does not exist, error code 401 is reported. You are advised to call [getFloatingBallWindowInfo()](../../window-manager/ohos-window-floatingball-floating-ball-window/document.md#getfloatingballwindowinfo) to obtain the window ID of a floating ball window.

**Atomic service API**: This API can be used in atomic services since API version 21.

 |

#### PickInfo

Describes the screenshot options.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| pickRect | [Rect](#rect) | No | No | Region of the screen to capture. |
| pixelMap | [image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md) | No | No | PixelMap object of the captured image. |

#### screenshot.pick

pick(): Promise<PickInfo>

Obtains this screenshot. Currently, only the screenshot of the display whose ID is **0** can be obtained. (If a screenshot of the extended screen is needed, you can use the [capture](#screenshotcapture14) API.) This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Device behavior differences**: This API can be properly called on 2-in-1 devices. If it is called on other device types, error code 801 is returned.

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[PickInfo](#pickinfo)\> | Promise used to return the PickInfo object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 801 | Capability not supported on this device. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

try {
  let promise = screenshot.pick();
  promise.then((pickInfo: screenshot.PickInfo) => {
    console.info('pick Pixel bytes number: ' + pickInfo.pixelMap.getPixelBytesNumber());
    console.info('pick Rect: ' + pickInfo.pickRect);
    pickInfo.pixelMap.release(); // Release the memory in time after the PixelMap is no longer needed.
  }).catch((err: BusinessError) => {
    console.error(\`Failed to pick. Code: ' + Code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to pick Code: ' + Code: ${exception.code}, message: ${exception.message}\`);
};

#### screenshot.capture14+

capture(options?: CaptureOption): Promise<image.PixelMap>

Takes a screenshot of the entire screen. This API uses a promise to return the result.

This API allows you to take screenshots of different screens by setting various **displayId** values, but only full-screen captures are supported. The [pick](#screenshotpick) API allows you to take screenshots of a specified region.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.WindowManager.WindowManager.Core

**Device behavior differences**: In versions earlier than API version 21, this API can be properly called on 2-in-1 devices and tablets. If it is called on other device types, error code 801 is returned. Starting from API version 21, this API can be properly called on phones, 2-in-1 devices, and tablets. If it is called on other device types, error code 801 is returned.

**Required permissions**: ohos.permission.CUSTOM\_SCREEN\_CAPTURE (for versions earlier than API version 22); ohos.permission.CUSTOM\_SCREEN\_CAPTURE or ohos.permission.CUSTOM\_SCREEN\_RECORDING (since API version 22)

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| options | [CaptureOption](#captureoption14) | No | Capture options. If this parameter is left blank, the display with ID 0 is captured by default. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[image.PixelMap](../../../../../media/image-kit/arkts-apis/ohos-multimedia-image-image-processing/interface-pixelmap/document.md)\> | Promise used to return a PixelMap object. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [Display Error Codes](../../../error-codes/graphics/display-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission verification failed. The application does not have the permission required to call the API. |
| 401 | Parameter error. Possible causes: 1.Mandatory parameters are left unspecified. 2.Incorrect parameter types. |
| 801 | Capability not supported on this device. |
| 1400003 | This display manager service works abnormally. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { image } from '@kit.ImageKit';

let captureOption: screenshot.CaptureOption = {
  "displayId": 0
};
try {
  let promise = screenshot.capture(captureOption);
  promise.then((pixelMap: image.PixelMap) => {
    console.info('Succeeded in saving screenshot. Pixel bytes number: ' + pixelMap.getPixelBytesNumber());
    pixelMap.release(); // Release the memory in time after the PixelMap is used.
  }).catch((err: BusinessError) => {
    console.error(\`Failed to save screenshot. Code: ${err.code}, message: ${err.message}\`);
  });
} catch (exception) {
  console.error(\`Failed to save screenshot. Code: ${exception.code}, message: ${exception.message}\`);
};
