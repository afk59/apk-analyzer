# @ohos.data.commonType (Common Data Types)

The **commonType** module defines common data types in data management.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/_ckIsOVEQ4a-YFfA-FbZzA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062214Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=93C47303EA518A8C856A342EC6FCF4A509BD71963618C2A5720F3DA049B1E5E3)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { commonType } from '@kit.ArkData';

#### AssetStatus

Enumerates the asset statuses. Use the enum name rather than the enum value.

**System capability**: SystemCapability.DistributedDataManager.CommonType

| Name | Value | Description |
| :-- | :-- | :-- |
| ASSET\_NORMAL | 1 | The asset is in normal status. |
| ASSET\_INSERT | 2 | The asset is to be inserted to the cloud. |
| ASSET\_UPDATE | 3 | The asset is to be updated to the cloud. |
| ASSET\_DELETE | 4 | The asset is to be deleted from the cloud. |
| ASSET\_ABNORMAL | 5 | The asset is in abnormal status. |
| ASSET\_DOWNLOADING | 6 | The asset is being downloaded to a local device. |

#### Asset

Represents asset (such as a file, image, or video) information. For details, see the sample code in [Using Distributed Data Objects in Cross-Device Migration](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/data-sync-of-distributed-data-object#using-distributed-data-objects-in-cross-device-migration).

**System capability**: SystemCapability.DistributedDataManager.CommonType

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Asset name. |
| uri | string | No | No | Asset URI, which is an absolute path in the system. |
| path | string | No | No | Application sandbox path of the asset. |
| createTime | string | No | No | Time when the asset was created. |
| modifyTime | string | No | No | Time when the asset was last modified. |
| size | string | No | No | Size of the asset. Ensure that the storage format and value logic are consistent across the end-to-end link. It is recommended that all system nodes use the standard processing format (unit: byte; value: a non-negative integer). |
| status | [AssetStatus](#assetstatus) | No | Yes | Asset status. The default value is **ASSET\_NORMAL**. |

#### Assets

type Assets = Array<Asset>

Represents an array of [Assets](#asset).

**System capability**: SystemCapability.DistributedDataManager.CommonType

| Type | Description |
| :-- | :-- |
| Array<[Asset](#asset)\> | Array of assets. |

#### ValueType

type ValueType = null | number | string | boolean | Uint8Array | Asset | Assets

Enumerates the value types, which vary with the parameter function.

**System capability**: SystemCapability.DistributedDataManager.CommonType

| Type | Description |
| :-- | :-- |
| null | The value is null. |
| number | The value is a number. |
| string | The value is a string. |
| boolean | The value is true or false. |
| Uint8Array | The value is a Uint8 array. |
| Asset | The value is an [Asset](#asset). |
| Assets | The value is an array of [Assets](#assets). |

#### ValuesBucket

type ValuesBucket = Record<string, ValueType>

Defines the types of the key and value in a KV pair. This type is not multi-thread safe. If a **ValuesBucket** instance is operated by multiple threads at the same time in an application, use a lock for the instance.

**System capability**: SystemCapability.DistributedDataManager.CommonType

| Type | Description |
| :-- | :-- |
| Record<string, [ValueType](#valuetype)\> | Types of the key and value in a KV pair. The key type is string, and the value type is [ValueType](#valuetype). |
