# @ohos.sendableResourceManager (Resource Manager)

The **sendableResourceManager** module provides the [resourceToSendableResource](#sendableresourcemanagerresourcetosendableresource) and [sendableResourceToResource](#sendableresourcemanagersendableresourcetoresource) APIs to implement conversion between [Resource](#resource) and [SendableResource](#sendableresource) objects.

A **Resource** object can be held by the [Sendable](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/arkts-sendable) class after being converted into a **SendableResource** object. After cross-thread transmission, the **Sendable** class converts the **SendableResource** object into a **Resource** object and uses it as an input parameter for the API used to obtain resources.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/85/v3/HMtwZFbvSo-gWZFE2Fsrug/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062326Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CA6D49B63C70924598FA123A38AFD5B2FA4C39A951417D128EAF8183CAA791E5)

The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { sendableResourceManager } from '@kit.LocalizationKit';

#### sendableResourceManager.resourceToSendableResource

resourceToSendableResource(resource: Resource): SendableResource

Converts a **Resource** object to a **SendableResource** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [Resource](#resource) | Yes | **Resource** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [SendableResource](#sendableresource) | **SendableResource** object after conversion. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { sendableResourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let sendableResource: sendableResourceManager.SendableResource = sendableResourceManager.resourceToSendableResource($r('app.string.test'));
} catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error(\`resourceToSendableResource failed, error code: ${code}, message: ${message}.\`);
}

#### sendableResourceManager.sendableResourceToResource

sendableResourceToResource(resource: SendableResource): Resource

Converts a **SendableResource** object to a **Resource** object.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| resource | [SendableResource](#sendableresource) | Yes | **SendableResource** object. |

**Return value**

| Type | Description |
| :-- | :-- |
| [Resource](#resource) | **Resource** object after conversion. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | If the input parameter invalid. Possible causes: 1.Incorrect parameter types; 2.Parameter verification failed. |

**Example**

// Resource file path: src/main/resources/base/element/string.json
{
  "string": \[
    {
      "name": "test",
      "value": "I'm a test string resource."
    }
  \]
}

import { sendableResourceManager } from '@kit.LocalizationKit';
import { BusinessError } from '@kit.BasicServicesKit';

try {
    let resource: sendableResourceManager.Resource = sendableResourceManager.sendableResourceToResource(sendableResourceManager.resourceToSendableResource($r('app.string.test')));
} catch (error) {
    let code = (error as BusinessError).code;
    let message = (error as BusinessError).message;
    console.error(\`sendableResourceToResource failed, error code: ${code}, message: ${message}.\`);
}

#### Resource

type Resource = \_Resource

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

| Type | Description |
| :-- | :-- |
| [\_Resource](../global/resource/document.md#resource-1) | Defines a **Resource** object. |

#### SendableResource

type SendableResource = \_SendableResource

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Global.ResourceManager

| Type | Description |
| :-- | :-- |
| [\_SendableResource](../global/sendableresource/document.md#sendableresource-1) | **SendableResource** object. |
