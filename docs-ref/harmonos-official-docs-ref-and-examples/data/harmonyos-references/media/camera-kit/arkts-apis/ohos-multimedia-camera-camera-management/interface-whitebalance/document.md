# Interface (WhiteBalance)

**WhiteBalance** inherits from [WhiteBalanceQuery](../interface-whitebalancequery/document.md).

It provides APIs to process white balance, including obtaining and setting the white balance mode and white balance value.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/98/v3/9QJNDlZRR2q5zlOW9tgzaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D14691FF02AAFD8C4179882556BC72F0D2EAFE2F2629497056AC667AFCC66A2)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 20.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### setWhiteBalanceMode20+

setWhiteBalanceMode(mode: WhiteBalanceMode): void

Sets a white balance mode. Before the setting, run [isWhiteBalanceModeSupported](../interface-whitebalancequery/document.md#iswhitebalancemodesupported20) to check whether the device supports the specified white balance mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [WhiteBalanceMode](../enums/document.md#whitebalancemode20) | Yes | White balance mode. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setWhiteBalanceMode(session: camera.PhotoSession | camera.VideoSession): void {
  try {
    session.setWhiteBalanceMode(camera.WhiteBalanceMode.DAYLIGHT);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The setWhiteBalanceMode call failed. error code: ${err.code}\`);
  }
}

#### getWhiteBalanceMode20+

getWhiteBalanceMode(): WhiteBalanceMode

Obtains the white balance mode in use.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| [WhiteBalanceMode](../enums/document.md#whitebalancemode20) | White balance mode in use. If the API call fails, undefined is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getWhiteBalanceMode(session: camera.PhotoSession | camera.VideoSession): camera.WhiteBalanceMode | undefined {
  let whiteBalanceMode: camera.WhiteBalanceMode | undefined = undefined;
  try {
    whiteBalanceMode = session.getWhiteBalanceMode();
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The getWhiteBalanceMode call failed. error code: ${err.code}\`);
  }
  return whiteBalanceMode;
}

#### setWhiteBalance20+

setWhiteBalance(whiteBalance: number): void

Sets a white balance value.

Before the setting, run [getWhiteBalanceRange](../interface-whitebalancequery/document.md#getwhitebalancerange20) to check the white balance value range supported by the device.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| whiteBalance | number | Yes | White balance value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function setWhiteBalance(session: camera.PhotoSession | camera.VideoSession): void {
  try {
    let whiteBalance: number = 1000;
    session.setWhiteBalance(whiteBalance);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The setWhiteBalance call failed. error code: ${err.code}\`);
  }
}

#### getWhiteBalance20+

getWhiteBalance(): number

Obtains the current white balance value.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| number | White balance value. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getWhiteBalance(session: camera.PhotoSession | camera.VideoSession): number {
  let whiteBalance: number = 0;
  try {
    whiteBalance = session.getWhiteBalance();
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The getWhiteBalance call failed. error code: ${err.code}\`);
  }
  return whiteBalance;
}
