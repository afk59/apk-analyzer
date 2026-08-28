# @ohos.telephony.esim (eSIM Management)

The **esim** module provides basic eSIM management capabilities, including checking whether a specified card slot supports the eSIM function.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/bb/v3/47Ze2GJORc6fXLczUQLpPw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062354Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C2CC83D558F1A350B25DD38311DF35DA1B7D0782E58F0DC868A213A6A3E35CE)

The initial APIs of this module are supported since API version 18. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { eSIM } from '@kit.TelephonyKit';

#### eSIM.isSupported

isSupported(slotId: number): boolean

Checks whether the specified card slot supports the eSIM function.

**System capability**: SystemCapability.Telephony.CoreService.Esim

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| slotId | number | Yes | 
Card slot ID.

\- **0**: card slot 1.

\- **1**: card slot 2

 |

**Returns**

| Type | Description |
| :-- | :-- |
| boolean | A boolean value indicating whether the specified card slot supports the eSIM function. The value **true** indicates that the card slot supports the eSIM function, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Invalid parameter value. |
| 3120001 | Service connection failed. |
| 3120002 | System internal error. |

**Example**

import { eSIM } from '@kit.TelephonyKit';

let isSupported: boolean = eSIM.isSupported(1);
console.info(\`the esim is Supported:\` + isSupported);

#### eSIM.addProfile

addProfile(profile: DownloadableProfile): Promise<boolean>

Launches the download page for the user to add a single profile. This API uses a promise to return the result.

**Required permissions**: ohos.permission.SET\_TELEPHONY\_ESIM\_STATE\_OPEN

**System capability**: SystemCapability.Telephony.CoreService.Esim

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| profile | [DownloadableProfile](#downloadableprofile) | Yes | Profile that can be downloaded. |

**Returns**

| Type | Description |
| :-- | :-- |
| Promise<boolean> | Promise used to return the result. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | Permission denied. |
| 401 | Invalid parameter value. |
| 801 | Capability not supported. |
| 3120001 | Service connection failed. |
| 3120002 | System internal error. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';
import { eSIM } from '@kit.TelephonyKit';

let profile: eSIM.DownloadableProfile = {
  activationCode:'1',
  confirmationCode:'1',
  carrierName:'test',
  accessRules:\[{
    certificateHashHexStr:'test',
    packageName:'com.example.testcoreservice',
    accessType:0
  }\]
};

eSIM.addProfile(profile).then(() => {
    console.info(\`addProfile invoking succeeded.\`);
}).catch((err: BusinessError<void>) => {
    console.error(\`addProfile, promise: err->${JSON.stringify(err)}\`);
});

#### DownloadableProfile

Defines a downloadable profile.

**System capability**: SystemCapability.Telephony.CoreService.Esim

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| activationCode | string | No | No | Activation code. For a profile that does not require an activation code, the value may be left empty. |
| confirmationCode | string | No | Yes | Confirmation code. |
| carrierName | string | No | Yes | Carrier name. |
| accessRules | Array<[AccessRule](#accessrule20)\> | No | Yes | Access rule array. |

#### AccessRule20+

Defines access rules.

**System capability**: SystemCapability.Telephony.CoreService.Esim

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| certificateHashHexStr | string | No | No | Hex string of the certificate hash. |
| packageName | string | No | No | Package name. |
| accessType | number | No | No | Rule type. |
