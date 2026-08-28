# Adding an Asset (ArkTS)

#### Available APIs

You can use [add(attributes: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetadd), an asynchronous API, or [addSync(attributes: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetaddsync12), a synchronous API, to add an asset.

The following table describes the attributes of **AssetMap** for adding an asset.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/OTLKiXIqRvOp8jwF85QOwg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4116AF2D6258126A04B795B19F9177A3D59E939EE7466EB5A7D332BFE996E6E2)

In the following table, the attributes **ALIAS** and those starting with **DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

| Attribute Name (Tag) | Value | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| SECRET | 
Type: Uint8Array

Length: 1-1024 bytes

 | Yes | Asset in plaintext. |
| ALIAS | 

Type: Uint8Array

Length: 1-256 bytes

 | Yes | Asset alias, which uniquely identifies an asset. |
| ACCESSIBILITY | 

Type: number

Value range: see [Accessibility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#accessibility)

 | No | Access control based on whether the screen is locked. The default value is **DEVICE\_FIRST\_UNLOCKED**, indicating that the asset can be accessed after the device is unlocked for the first time. |
| REQUIRE\_PASSWORD\_SET | Type: Boolean | No | Whether the asset is accessible only when a lock screen password is set. The value **true** means that the asset can be accessed only when the user sets a screen lock password. The value **false** means that the asset can be accessed regardless of whether the user sets a screen lock password. The default value is **false**. |
| AUTH\_TYPE | 

Type: number

Value range: see [AuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#authtype)

 | No | User authentication type required for accessing an asset. The default value is **NONE**, indicating that user authentication is not required before the user accesses an asset. |
| SYNC\_TYPE | 

Type: number

Value range: see [SyncType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#synctype)

 | No | Sync type supported by the asset. The default value is **NEVER**, indicating that the asset cannot be synced. |
| IS\_PERSISTENT | Type: Boolean | No | 

Whether to retain the asset when the application is uninstalled. The value **true** means to retain the asset when the application is uninstalled; the value **false** means the opposite. The default value is **false**.

**NOTE**: If this parameter is set, the application must [apply for](../../../application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) the ohos.permission.STORE\_PERSISTENT\_DATA permission.

 |
| DATA\_LABEL\_CRITICAL\_1 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**NOTE**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_CRITICAL\_2 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**NOTE**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_CRITICAL\_3 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**NOTE**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_CRITICAL\_4 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**NOTE**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_1 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**NOTE**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_2 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**NOTE**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_3 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**NOTE**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_4 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**NOTE**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | Local attribute information about the asset. The value is assigned by the service without integrity protection and will not be synced. |
| DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | Local attribute information about the asset. The value is assigned by the service without integrity protection and will not be synced. |
| DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | Local attribute information about the asset. The value is assigned by the service without integrity protection and will not be synced. |
| DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | Local attribute information about the asset. The value is assigned by the service without integrity protection and will not be synced. |
| CONFLICT\_RESOLUTION | 

Type: number

Value range: see [ConflictResolution](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#conflictresolution)

 | No | Conflict (for example, duplicate aliases) resolution when an asset is added. The default value is **THROW\_ERROR**, indicating that an exception is thrown for subsequent processing by the service. |
| REQUIRE\_ATTR\_ENCRYPTED14+ | Type: Boolean | No | Whether to encrypt the additional asset information customized by the service. The value **true** means to encrypt the additional asset information customized by the service; the value **false** means the opposite. The default value is **false**. |
| GROUP\_ID18+ | 

Type: Uint8Array

Length: 7-127 bytes

 | No | Group to which the asset to be added belongs. By default, this parameter is not specified. |
| WRAP\_TYPE18+ | 

Type: number

Value range: see [WrapType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#wraptype18)

 | No | Encrypted import/export type supported by the asset. The default value is **NEVER**, indicating that encrypted import/export is not supported. |

#### Constraints

-   Alias-based access
    
    Assets are stored in the ASSET database in ciphertext and uniquely identified by the service identity and alias. The alias of each asset must be unique.
    
-   Custom service data storage
    
    Asset Store Kit provides 12 custom asset attributes starting with **DATA\_LABEL** for services. If the 12 custom attributes are used, you can combine multiple data segments in a certain format (for example, JSON) into an attribute of this kit.
    
    Asset Store Kit protects the integrity of the attributes starting with **DATA\_LABEL\_CRITICAL**. These attributes cannot be changed once written.
    

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/46/v3/Q1dU2iKbQYWChO73mblPJA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7CA6ED76E110CCE8769FF762249153182809520F4ECC2DAAFE0BEEA5D1057101)

The **asset** module provides asynchronous and synchronous APIs. The following uses the asynchronous APIs as an example. For more information about the APIs, see [Asset Store Service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset).

For details about how to add an asset to a group, see [Adding an Asset to a Group](../managing-assets-in-a-group-arkts/document.md#adding-an-asset-to-a-group).

Add an asset that is accessible when the user unlocks the device for the first time. The asset includes password **demo\_pwd**, alias **demo\_alias**, and additional information **demo\_label**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function addAsset(): Promise<string> {
  let result: string = '';
  let attr: asset.AssetMap = new Map();
  attr.set(asset.Tag.SECRET, stringToArray('demo\_pwd'));
  attr.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
  attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE\_FIRST\_UNLOCKED);
  attr.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label'));
  try {
    await asset.add(attr).then(() => {
      console.info(\`Succeeded in adding Asset.\`);
      result = 'Succeeded in adding Asset';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to add Asset. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to add Asset';
    })
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to add Asset. Code is ${err.code}, message is ${err.message}\`);
    result = 'Failed to add Asset';
  }
  return result;
}
