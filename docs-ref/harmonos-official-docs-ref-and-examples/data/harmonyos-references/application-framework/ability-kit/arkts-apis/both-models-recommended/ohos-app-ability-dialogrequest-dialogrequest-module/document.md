# @ohos.app.ability.dialogRequest (dialogRequest Module)

The dialogRequest module provides APIs related to modal dialog box processing, including obtaining the request information (used to bind a modal dialog box) and request callback (used to set the request result).

A modal dialog box is a system-level dialog box that blocks interactions such as mouse clicks, keyboard input, and touch events on the underlying page. The page can only be interacted with after the modal dialog box is closed.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/09/v3/6yLLsKItQtyPdTdxAoe_tQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062208Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=00C6BDB8DD896B365D7911457267B10019BE0DD0E50A9631B3799787B45EF77E)

-   The initial APIs of this module are supported since API version 9. Newly added APIs will be marked with a superscript to indicate their earliest API version.
-   The APIs provided by this module are used in ServiceExtensionAbilities. For a ServiceExtensionAbility that implements modal dialog boxes, you can use the APIs to obtain the request information and request callback and return the request result.

#### Modules to Import

import { dialogRequest } from '@kit.AbilityKit';

#### dialogRequest.getRequestInfo

getRequestInfo(want: Want): RequestInfo

Obtains the request information from Want.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/cmf7b_7eTuOCy3at4YR2Ig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062208Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0FB2856C42B66FB41C580C6B965A13C244798FDB92C594733E5A7E3204B18B55)

This API can be used by a ServiceExtensionAbility. If the ServiceExtensionAbility implements modal dialog boxes, the request information can be obtained from Want. If this API is used in other scenarios, no return value is obtained.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../ohos-app-ability-want-want/document.md) | Yes | Want passed in the request for a modal dialog box. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RequestInfo](#requestinfo) | RequestInfo object obtained, which is used to bind a modal dialog box. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestInfo = dialogRequest.getRequestInfo(want);
    } catch (err) {
      console.error(\`getRequestInfo err= ${JSON.stringify(err)}\`);
    }
  }
}

#### dialogRequest.getRequestCallback

getRequestCallback(want: Want): RequestCallback

Obtains the request callback from Want.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/68/v3/BVeKiQeEQk2OTX6IuYcNHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062208Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=738D607498B4C49CAEA88CC0BC2AA4FFF6994EF36B9B873D779265E1E0B7BC87)

This API can be used by a ServiceExtensionAbility. If the ServiceExtensionAbility implements modal dialog boxes, the request callback can be obtained from Want. If this API is used in other scenarios, no return value is obtained.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| want | [Want](../ohos-app-ability-want-want/document.md) | Yes | Want passed in the request for a modal dialog box. |

**Return value**

| Type | Description |
| :-- | :-- |
| [RequestCallback](#requestcallback) | RequestCallback object obtained, which is used to set the return result. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestCallback = dialogRequest.getRequestCallback(want);
    } catch(err) {
      console.error(\`getRequestInfo err= ${JSON.stringify(err)}\`);
    }
  }
}

#### WindowRect10+

Defines the location attributes of a modal dialog box.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| left | number | No | No | X-coordinate of the upper left corner of the dialog box. |
| top | number | No | No | Y-coordinate of the upper left corner of the dialog box. |
| width | number | No | No | Width of the dialog box, in px. |
| height | number | No | No | Height of the dialog box, in px. |

#### RequestInfo

Defines the request information, which is used as an input parameter for binding the modal dialog box.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| windowRect10+ | [WindowRect](#windowrect10) | No | Yes | Location attributes of a modal dialog box. |

**Example**

import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestInfo = dialogRequest.getRequestInfo(want);
      console.info(\`getRequestInfo windowRect=, ${JSON.stringify(requestInfo.windowRect)}\` );
    } catch(err) {
      console.error(\`getRequestInfo err= ${JSON.stringify(err)}\`);
    }
  }
}

#### ResultCode

Enumerates the result codes of the request for the modal dialog box.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| RESULT\_OK | 0 | The request succeeds. |
| RESULT\_CANCEL | 1 | The request fails. |

#### RequestResult

Defines the result of the request for the modal dialog box. It contains **ResultCode** and **ResultWant**.

#### \[h2\]Properties

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.AbilityRuntime.Core

| Name | Type | Read-only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| result | [ResultCode](#resultcode) | No | No | Result code of the request. |
| want10+ | [Want](../ohos-app-ability-want-want/document.md) | No | Yes | Want information, such as the ability name and bundle name. |

#### RequestCallback

Provides a callback for setting the modal dialog box request result.

**Model restriction**: This API can be used only in the stage model.

#### \[h2\]RequestCallback.setRequestResult

setRequestResult(result: RequestResult): void

Sets the result of the request for the modal dialog box.

**Model restriction**: This API can be used only in the stage model.

**System capability**: SystemCapability.Ability.AbilityRuntime.AbilityCore

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| result | [RequestResult](#requestresult) | Yes | Request result to set. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |

**Example**

import { AbilityConstant, UIAbility, Want, dialogRequest } from '@kit.AbilityKit';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    try {
      let requestCallback = dialogRequest.getRequestCallback(want);
      let myResult: dialogRequest.RequestResult = {
        result : dialogRequest.ResultCode.RESULT\_CANCEL,
      };
      requestCallback.setRequestResult(myResult);
    } catch(err) {
      console.error(\`getRequestInfo err= ${JSON.stringify(err)}\`);
    }
  }
}
