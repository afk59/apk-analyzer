# @ohos.security.identifySensitiveContent (Identifying Sensitive Content)

This module identifies sensitive information in a specified file based on the input [scan policy](#policy).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e4/v3/wgRDya_sReyqWS98q0Wzyw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062333Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABE88A9D35B0E4A9D249F5894D2B6CE14771694B9E98C39221D425E8CBE16204)

The initial APIs of this module are supported since API version 21. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { identifySensitiveContent } from '@kit.DataProtectionKit';

#### identifySensitiveContent.scanFile

scanFile(filePath: string, identifyPolicies:Array<Policy>): Promise<Array<MatchResult>>

Identifies sensitive content in a specified file based on the configured policy. This API uses a promise to return the result.

**Required permissions**: ohos.permission.ENTERPRISE\_DATA\_IDENTIFY\_FILE

**System capability**: SystemCapability.Security.DataLossPrevention

**Parameters**

| Parameter | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| filePath | string | Yes | Path of the file to be identified. |
| identifyPolicies | Array<[Policy](#policy)\> | Yes | Identification policy. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<[MatchResult](#matchresult)\>> | Promise used to return the identification result of sensitive content. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md) and [DLP Error Codes](../../error-codes/dlp-service-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | permission denied. |
| 801 | Capability not supported. |
| 19110001 | Parameter error.Possible causes:1. Incorrect policy format. 2. Invalid parameter range. |
| 19110002 | Sensitive file content identification timed out. |
| 19110003 | The file is not supported. Possible causes:1. The file path does not exist. 2. The file type is not supported. 3. The file permission is not supported. |
| 19110004 | A system error has occurred. |

**Example**

import { identifySensitiveContent } from '@kit.DataProtectionKit';

let filepath = "file://docs/storage/Users/currentUser/Desktop/test.txt";
let policies: Array<identifySensitiveContent.Policy> = \[
  {"sensitiveLabel":"1", "keywords":\[\], "regex":""}
\];
try {
  identifySensitiveContent.scanFile(filepath, policies).then(records => {
    console.info('scanFile finish');
  }).catch((err:Error) => {
    console.error('error message', err.message);
  })
} catch (err) {
  console.error('error message', err.message);
}

#### Policy

Defines the policy for sensitive content identification.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sensitiveLabel | string | No | No | Label of an identification policy. The value can contain a maximum of 30 bytes. |
| keywords | Array<string> | No | No | Keyword set. The array can contain a maximum of 50 elements, and each element can contain a maximum of 30 bytes. |
| regex | string | No | No | Regular expression. The value can contain a maximum of 512 bytes. |

#### MatchResult

Displays the identification result of sensitive content.

**System capability**: SystemCapability.Security.DataLossPrevention

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| sensitiveLabel | string | Yes | No | Label of an identification policy. |
| matchContent | string | Yes | No | Matched content. |
| matchNumber | number | Yes | No | Total number of matched items. |
