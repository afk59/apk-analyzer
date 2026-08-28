# @ohos.net.mdns (MDNS Management)

Multicast DNS (MDNS) provides functions such as adding, removing, discovering, and resolving local services on a LAN.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/95/v3/TPqWqoRCRUKH-tjssUv5NA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9A7C2075F869249119A5618BD7F0B228D951C372A40EEF8CCFD60F59B142AAC2)

The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { mdns } from '@kit.NetworkKit';

#### mdns.addLocalService

addLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

Adds an MDNS service. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | Yes | MDNS service information. |
| callback | AsyncCallback<[LocalServiceInfo](#localserviceinfo)\> | Yes | Callback used to return the result. If the operation is successful, **error** is **undefined** and **data** is the MDNS service information. |

**Error codes**

For details about the error codes, see [MDNS Error Codes](../../error-codes/mdns-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/89/v3/cFuHDcj9T6CeMWcArJw5Tw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=800945D6273C476D4DD18C334CD4D18ABFC47E862E3E5852CCDB8422D96F706A)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "\_print.\_tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.\*\*.\*\*\*",
  },
  serviceAttribute: \[{key: "111", value: \[1\]}\]
}

mdns.addLocalService(context, localServiceInfo, (error:BusinessError, data:mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});

#### mdns.addLocalService

addLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

Adds an MDNS service. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | Yes | MDNS service information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[LocalServiceInfo](#localserviceinfo)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [MDNS Error Codes](../../error-codes/mdns-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/44/v3/n1hLVekFR8CbYGl0nqC5JQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7B4B3AFA6E21BBF177EA972628F52280630A1267C5672C8E399FEE6B8E8F1449)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "\_print.\_tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
    address: "10.14.\*\*.\*\*\*",
  },
  serviceAttribute: \[{key: "111", value: \[1\]}\]
}

mdns.addLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

#### mdns.removeLocalService

removeLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

Removes an MDNS service. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | Yes | MDNS service information. |
| callback | AsyncCallback<[LocalServiceInfo](#localserviceinfo)\> | Yes | Callback used to return the result. If the operation is successful, **error** is **undefined** and **data** is the MDNS service information. |

**Error codes**

For details about the error codes, see [MDNS Error Codes](../../error-codes/mdns-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204002 | Callback not found. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c8/v3/U7WlaSqZSIiisBzIgFFecg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=849EA0E37E956D1348F9FEF7322E11E5EB51C6978CF2895741A0F1A839CD1797)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "\_print.\_tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.\*\*.\*\*\*",
  },
  serviceAttribute: \[{key: "111", value: \[1\]}\]
}

mdns.removeLocalService(context, localServiceInfo, (error: BusinessError, data: mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});

#### mdns.removeLocalService

removeLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

Removes an MDNS service. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | Yes | MDNS service information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[LocalServiceInfo](#localserviceinfo)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [MDNS Error Codes](../../error-codes/mdns-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204002 | Callback not found. |
| 2204008 | Failed to delete the service instance. |
| 2204010 | Failed to send the message. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4a/v3/L0VsU3IJTkq3vEjPLmXrPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EAD284399F56FBC5324FCE9CE3C4AF555BF132C18F1A82D7C637301294255D87)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "\_print.\_tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.\*\*.\*\*\*",
  },
  serviceAttribute: \[{key: "111", value: \[1\]}\]
}

mdns.removeLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

#### mdns.createDiscoveryService

createDiscoveryService(context: Context, serviceType: string): DiscoveryService

Creates a **DiscoveryService** object, which is used to discover MDNS services of the specified type.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| serviceType | string | Yes | MDNS service type. |

**Return value**

| Type | Description |
| :-- | :-- |
| DiscoveryService | **DiscoveryService** object obtained based on the specified **serviceType** and **context**. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/Ztgq5FFKThGPzLZkfqHKJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=55AF599FE42A47DC017A57C4218680B7F90A056D76ECE4748CF9A85473058A69)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let serviceType = "\_print.\_tcp";
let discoveryService : Object = mdns.createDiscoveryService(context, serviceType);

#### mdns.resolveLocalService

resolveLocalService(context: Context, serviceInfo: LocalServiceInfo, callback: AsyncCallback<LocalServiceInfo>): void

Resolves an MDNS service. This API uses an asynchronous callback to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | Yes | MDNS service information. |
| callback | AsyncCallback<[LocalServiceInfo](#localserviceinfo)\> | Yes | Callback used to return the result. If the operation is successful, **error** is **undefined** and **data** is the MDNS service information. |

**Error codes**

For details about the error codes, see [MDNS Error Codes](../../error-codes/mdns-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204006 | Request timeout. |
| 2204010 | Failed to send the message. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/eMgm3njaTLmrKufobWG-Mg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E97E1C41ECB7F862B106A806502846EAA7BF205C6CFD3F906801CF748F455EE5)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "\_print.\_tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.\*\*.\*\*\*",
  },
  serviceAttribute: \[{key: "111", value: \[1\]}\]
}

mdns.resolveLocalService(context, localServiceInfo, (error: BusinessError, data: mdns.LocalServiceInfo) =>  {
  console.error(JSON.stringify(error));
  console.info(JSON.stringify(data));
});

#### mdns.resolveLocalService

resolveLocalService(context: Context, serviceInfo: LocalServiceInfo): Promise<LocalServiceInfo>

Resolves an MDNS service. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| context | Context | Yes | 
Application context.

For details about the application context of the FA model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/fa-model/app/context-context-base-class-of-the-fa-model/document.md).

For details about the application context of the stage model, see [Context](../../../../../application-framework/ability-kit/arkts-apis/dependent-elements-and-definitions/application/context-context-base-class-of-the-stage-model/document.md).

 |
| serviceInfo | [LocalServiceInfo](#localserviceinfo) | Yes | MDNS service information. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[LocalServiceInfo](#localserviceinfo)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [MDNS Error Codes](../../error-codes/mdns-error-codes/document.md) and [Universal Error Codes](../../../../../api-reference-overview/universal-error-codes/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | Parameter error. |
| 2100002 | Failed to connect to the service. |
| 2100003 | System internal error. |
| 2204003 | Callback duplicated. |
| 2204006 | Request timeout. |
| 2204010 | Failed to send the message. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/21/v3/0vUcUE6wSuSt7TSQcYlyLg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3638F2D28E9ECF551474550191A86530ECB79EA1378DBC772358B77504C69DF7)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;

let localServiceInfo: mdns.LocalServiceInfo = {
  serviceType: "\_print.\_tcp",
  serviceName: "servicename",
  port: 5555,
  host: {
  address: "10.14.\*\*.\*\*\*",
  },
  serviceAttribute: \[{key: "111", value: \[1\]}\]
}

mdns.resolveLocalService(context, localServiceInfo).then((data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

#### DiscoveryService

Defines a **DiscoveryService** object for discovering MDNS services of the specified type.

#### \[h2\]startSearchingMDNS

startSearchingMDNS(): void

Searches for MDNS services on the LAN.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6a/v3/hIhNQPoDTOWJMxRQZxuLuw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1559930B1193686542F15C2B7A69EC6762851E908BF756B9608EB7A4684A445B)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

#### \[h2\]stopSearchingMDNS

stopSearchingMDNS(): void

Stops searching for MDNS services on the LAN.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/77/v3/tSJSF0D1Tfi_xnWQlniAAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AF71AD3F9BDF9B84B49B30E7357DA3899C5A73F3EB5C482B20BEF1BB700F2685)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

Stage model:

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// Obtain the application context.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.stopSearchingMDNS();

#### \[h2\]on('discoveryStart')

on(type: 'discoveryStart', callback: Callback<DiscoveryEventInfo>): void

Enables listening for **discoveryStart** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **discoveryStart**.

**discoveryStart**: event of starting discovery of MDNS services on the LAN.

 |
| callback | Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\> | Yes | Callback used to return the MDNS service and error information. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/jdFLwenSRMacXRqbiXFZHQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80D1ED8407F54A8F7FBE9D9E4E13049E1C4E5C27EE7B405AFB045D6543FC7410)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// See mdns.createDiscoveryService.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

#### \[h2\]off('discoveryStart')

off(type: 'discoveryStart', callback?: Callback<DiscoveryEventInfo>): void

Disables listening for **discoveryStart** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **discoveryStart**.

**discoveryStart**: event of starting discovery of MDNS services on the LAN.

 |
| callback | Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\> | No | Callback used to return the MDNS service and error information. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a5/v3/fyxEsv_NRNSaJp4ckF11XQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CB7E68AAEDEA1C8AE340712DCD04D428AC22C14F14ECBB8E428AC892219ADB1C)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// See mdns.createDiscoveryService.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('discoveryStart', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

#### \[h2\]on('discoveryStop')

on(type: 'discoveryStop', callback: Callback<DiscoveryEventInfo>): void

Enables listening for **discoveryStop** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **discoveryStop**.

**discoveryStop**: event of stopping discovery of MDNS services on the LAN.

 |
| callback | Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\> | Yes | Callback used to return the MDNS service and error information. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5d/v3/TN3YeUW6ThCnwYLrZ2yH1Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=EA280D2AB4BDA3F71FDADFA5D2B47CB1C6653CC93343B467D89B00C9A297312C)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// See mdns.createDiscoveryService.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

#### \[h2\]off('discoveryStop')

off(type: 'discoveryStop', callback?: Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\>): void

Disables listening for **discoveryStop** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **discoveryStop**.

**discoveryStop**: event of stopping discovery of MDNS services on the LAN.

 |
| callback | Callback<[DiscoveryEventInfo](#discoveryeventinfo11)\> | No | Callback used to return the MDNS service and error information. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/Utzkli6TR96pd8O8SAgO5w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD8538EE213A07E266F3E2A4526448B9F36D3F86893CB659E00D3E6F84F542CB)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// See mdns.createDiscoveryService.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('discoveryStop', (data: mdns.DiscoveryEventInfo) => {
  console.info(JSON.stringify(data));
});

#### \[h2\]on('serviceFound')

on(type: 'serviceFound', callback: Callback<LocalServiceInfo>): void

Enables listening for **serviceFound** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **serviceFound**.

**serviceFound**: event indicating an MDNS service is found.

 |
| callback | Callback<[LocalServiceInfo](#localserviceinfo)\> | Yes | Callback used to return the MDNS service information. You need to call **resolveLocalService** to parse the information. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/82/v3/o7YqDaDLSSyPv902bqWltQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1AF933F3C3373AED66AB7F38A8448DC04C330756B1ABC2FF42844797E523D660)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// See mdns.createDiscoveryService.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info('serviceFound', JSON.stringify(data));
  mdns.resolveLocalService(context, data, (error: BusinessError, resolveData: mdns.LocalServiceInfo) =>  {
    console.info('serviceFound', JSON.stringify(resolveData));
  });
});

discoveryService.stopSearchingMDNS();

#### \[h2\]off('serviceFound')

off(type: 'serviceFound', callback?: Callback<LocalServiceInfo>): void

Disables listening for **serviceFound** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **serviceFound**.

**serviceFound**: event indicating an MDNS service is found.

 |
| callback | Callback<[LocalServiceInfo](#localserviceinfo)\> | No | MDNS service information. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cf/v3/KB8UDCgMRUCmVOdjxuRN0A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3EBAC5D63D62118D521AFF9DB0B2A93629A02449396A3FC8EE019B7D141F46E4)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// See mdns.createDiscoveryService.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info('serviceFound', JSON.stringify(data));
  mdns.resolveLocalService(context, data, (error: BusinessError, resolveData: mdns.LocalServiceInfo) =>  {
    console.info('serviceFound', JSON.stringify(resolveData));
  });
});

discoveryService.stopSearchingMDNS();

discoveryService.off('serviceFound', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

#### \[h2\]on('serviceLost')

on(type: 'serviceLost', callback: Callback<LocalServiceInfo>): void

Enables listening for **serviceLost** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **serviceLost**.

**serviceLost**: event indicating that an MDNS service is removed.

 |
| callback | Callback<[LocalServiceInfo](#localserviceinfo)\> | Yes | MDNS service information. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c4/v3/IwtN3ItpRwyZWJeCc2h72g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67A36EDC85F2F7F2E9948A3ED21FF7AAB4289EB57F05C82A954B6ED923AAF0B5)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// See mdns.createDiscoveryService.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

#### \[h2\]off('serviceLost')

off(type: 'serviceLost', callback?: Callback<LocalServiceInfo>): void

Disables listening for **serviceLost** events.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| type | string | Yes | 
Event type. This field has a fixed value of **serviceLost**.

**serviceLost**: event indicating that an MDNS service is removed.

 |
| callback | Callback<[LocalServiceInfo](#localserviceinfo)\> | No | MDNS service information. You can pass the callback of the **on** function if you want to cancel listening for a certain type of events. If you do not pass the callback, you will cancel listening for all events. |

**Example**

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2b/v3/QCu-dxrAQZyNULfXNxzD4w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062345Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=218B5AE6B197CBFDA9D4DD452257BA3F9788F120DD6E67AFC450A82FEC13C81D)

In the sample code provided in this topic, **this.context** is used to obtain **UIAbilityContext**, where **this** indicates a UIAbility instance inherited from **UIAbility**. To use **UIAbilityContext** APIs on pages, see [Obtaining the Context of UIAbility](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/uiability-usage#obtaining-the-context-of-uiability).

import { mdns } from '@kit.NetworkKit';
import { BusinessError } from '@kit.BasicServicesKit';
import { common } from '@kit.AbilityKit';

// See mdns.createDiscoveryService.
let context: common.UIAbilityContext = this.getUIContext().getHostContext() as common.UIAbilityContext;
let serviceType = "\_print.\_tcp";
let discoveryService = mdns.createDiscoveryService(context, serviceType);
discoveryService.startSearchingMDNS();

discoveryService.on('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

discoveryService.stopSearchingMDNS();

discoveryService.off('serviceLost', (data: mdns.LocalServiceInfo) => {
  console.info(JSON.stringify(data));
});

#### LocalServiceInfo

MDNS service information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceType | string | No | No | MDNS service type. The value is in the format of **\_<name>.<\_tcp/\_udp>**, where **name** contains a maximum of 63 characters excluding periods (.). |
| serviceName | string | No | No | MDNS service name. |
| port | number | No | Yes | Service port number. The value range is \[0, 65535\]. |
| host | [NetAddress](../ohos-net-connection-network-connection-management/document.md#netaddress) | No | Yes | IP address of the device that provides the MDNS service. The IP address is not effective when an MDNS service is added or removed. |
| serviceAttribute | Array<[ServiceAttribute](#serviceattribute)\> | No | Yes | MDNS service attribute information. |

#### ServiceAttribute

MDNS service attribute information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| key | string | No | No | MDNS service attribute key. The value contains a maximum of 9 characters. |
| value | Array<number> | No | No | MDNS service attribute value. |

#### DiscoveryEventInfo11+

Defines the MDNS service event information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| serviceInfo | LocalServiceInfo | No | No | MDNS service information. |
| errorCode | MdnsError | No | Yes | MDNS error information. |

#### MdnsError

Defines the MDNS error information.

**Atomic service API**: This API can be used in atomic services since API version 11.

**System capability**: SystemCapability.Communication.NetManager.MDNS

| Name | Value | Description |
| :-- | :-- | :-- |
| INTERNAL\_ERROR | 0 | Operation failed because of an internal error. |
| ALREADY\_ACTIVE | 1 | Operation failed because the service already exists. |
| MAX\_LIMIT | 2 | Operation failed because the number of requests exceeds the maximum value. |

#### NetAddress

type NetAddress = connection.NetAddress

Obtains the network address.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Communication.NetManager.Core

| Type | Description |
| :-- | :-- |
| connection.NetAddress | Network address. |
