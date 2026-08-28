# Functions

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/ZBnuEv1DQI24m1BdxPifAA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062223Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27DCD474E8DF4BB8AC0BA0AA3A83A441D5A384C8FD24FD3F6E028673E924BB25)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

This module can be imported only to ArkTS files (with the file name extension .ets).

#### Modules to Import

import { ArkTSUtils } from '@kit.ArkTS'

#### ArkTSUtils.isSendable

isSendable(value: Object | null | undefined): boolean

Checks whether the passed-in value is of the sendable data type.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Utils.Lang

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| value | Object | null | undefined | Yes | Object to check. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Check result. The value **true** is returned if the passed-in value is of the sendable data type; otherwise, **false** is returned. |

**Example**

import { ArkTSUtils } from '@kit.ArkTS';

@Sendable
function sendableFunc() {
  console.info("sendableFunc");
}

if (ArkTSUtils.isSendable(sendableFunc)) {
  console.info("sendableFunc is Sendable");
} else {
  console.info("sendableFunc is not Sendable");
}
// Expected output: 'SendableFunc is Sendable'
