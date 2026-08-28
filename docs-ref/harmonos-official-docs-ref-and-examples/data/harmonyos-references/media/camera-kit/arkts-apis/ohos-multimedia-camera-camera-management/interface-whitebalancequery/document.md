# Interface (WhiteBalanceQuery)

WhiteBalanceQuery provides APIs to check whether a white balance mode is supported and obtain the white balance mode range supported.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6e/v3/_0E6pPsxTjCgUP2Ar82SKg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062427Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5F2C8FFF1889898444F8089E4E9DEDD06E473EE705AD7F1C4A5147D590118FF5)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The initial APIs of this interface are supported since API version 20.

#### Modules to Import

import { camera } from '@kit.CameraKit';

#### isWhiteBalanceModeSupported20+

isWhiteBalanceModeSupported(mode: WhiteBalanceMode): boolean

Checks whether a white balance mode is supported.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| mode | [WhiteBalanceMode](../enums/document.md#whitebalancemode20) | Yes | White balance mode. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result for the support of the white balance mode. **true** if supported, **false** otherwise. If the API call fails, undefined is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400101 | Parameter missing or parameter type incorrect. |
| 7400103 | Session not config, only throw in session usage. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function isWhiteBalanceModeSupported(session: camera.PhotoSession | camera.VideoSession): boolean {
  let status: boolean = false;
  try {
  let mode: camera.WhiteBalanceMode = camera.WhiteBalanceMode.DAYLIGHT;
    status = session.isWhiteBalanceModeSupported(mode);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The isWhiteBalanceModeSupported call failed. error code: ${err.code}\`);
  }
  return status;
}

#### getWhiteBalanceRange20+

getWhiteBalanceRange(): Array<number>

Obtains the range of white balance values in manual white balance mode.

**Atomic service API**: This API can be used in atomic services since API version 20.

**System capability**: SystemCapability.Multimedia.Camera.Core

**Return value**

| Type | Description |
| :-- | :-- |
| Array<number> | Range of white balance values, for example, \[2800, ...,10000\], in units of K (Kelvin). The actual value depends on the bottom-layer capability. If the API call fails, undefined is returned. |

**Error codes**

For details about the error codes, see [Camera Error Codes](../../../error-codes/camera-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 7400103 | Session not config, only throw in session usage. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

function getWhiteBalanceRange(session: camera.PhotoSession | camera.VideoSession): Array<number> {
  let range: Array<number> = \[\];
  try {
    range = session.getWhiteBalanceRange();
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`The getWhiteBalanceRange call failed. error code: ${err.code}\`);
  }
  return range;
}
