# @ohos.data.cloudData (Device-Cloud Service)

The **cloudData** module provides APIs for implementing device-cloud synergy and device-cloud sharing, and setting the device-cloud sync strategy.

Device-cloud synergy enables sync of the structured data (in RDB stores) between devices and the cloud. The cloud serves as a data hub to implement data backup in the cloud and data consistency between the devices with the same account.

This module also provides the capability of setting the device-cloud sync strategy.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a1/v3/Dt_zYYaKRb2KQbC4zzruig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062217Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2C27890B63EAEA4A5721643F74BC8243BBB4005B3F74532DD70C423195478BE)

-   The initial APIs of this module are supported since API version 12. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { cloudData } from '@kit.ArkData';

#### StrategyType

Enumerates the types of the cloud-device sync strategy.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

| Name | Value | Description |
| :-- | :-- | :-- |
| NETWORK | 0 | Sync over the network. |

#### NetWorkStrategy

Enumerates the network sync options.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

| Name | Value | Description |
| :-- | :-- | :-- |
| WIFI | 1 | Sync over Wi-Fi. |
| CELLULAR | 2 | Sync over the cellular network. |

#### cloudData.setCloudStrategy

setCloudStrategy(strategy: StrategyType, param?: Array<commonType.ValueType>): Promise<void>

Sets the device-cloud sync strategy for the application. If no strategy is set, the global strategy set by setGlobalCloudStrategy12+ is used. If the global strategy is not set, the application data is synced over Wi-Fi and the cellular network by default. This API uses a promise to return the result.

**System capability**: SystemCapability.DistributedDataManager.CloudSync.Client

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| strategy | [StrategyType](#strategytype) | Yes | Type of the strategy to set. |
| param | Array<[commonType.ValueType](../ohos-data-commontype-common-data-types/document.md#valuetype)\> | No | Strategy parameters to set. If this parameter is not specified, all the configuration is canceled. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Universal Error Codes](../../../../api-reference-overview/universal-error-codes/document.md).

| **ID** | **Error Message** |
| :-- | :-- |
| 401 | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| 801 | Capability not supported. |

**Example**

import { BusinessError } from '@kit.BasicServicesKit';

// Sync data over Wi-Fi only.
cloudData.setCloudStrategy(cloudData.StrategyType.NETWORK, \[cloudData.NetWorkStrategy.WIFI\]).then(() => {
    console.info('Succeeded in setting the cloud strategy');
}).catch((err: BusinessError) => {
    console.error(\`Failed to set cloud strategy. Code: ${err.code}, message: ${err.message}\`);
});
