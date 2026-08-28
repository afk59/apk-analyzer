# Removing Assets (ArkTS)

#### Available APIs

You can use [remove(query: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetremove), an asynchronous API, or [removeSync(query: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetremovesync12), a synchronous API, to remove assets. If the asset alias is specified, the specified asset will be removed. If no asset alias is specified, all assets will be removed.

The following table describes the attributes of **AssetMap** for removing an asset.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/39/v3/Uk2gQ2jkRsSDHMhILopbXw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=67121D87F58F00B03F49D0D93EE7D8176F555CBCC5D939AA742F935D99D48B14)

In the following table, the attributes **ALIAS** and those starting with **DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

| Attribute Name (Tag) | Value | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ALIAS | 
Type: Uint8Array

Length: 1-256 bytes

 | No | Asset alias, which uniquely identifies an asset. |
| ACCESSIBILITY | 

Type: number

Value range: see [Accessibility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#accessibility)

 | No | Access control based on the lock screen status. |
| REQUIRE\_PASSWORD\_SET | Type: Boolean | No | Whether the asset is accessible only when a lock screen password is set. The value **true** means the asset is accessible only when a lock screen password is set. The value **false** means that the asset can be accessed regardless of whether a lock screen password is set. |
| AUTH\_TYPE | 

Type: number

Value range: see [AuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#authtype)

 | No | Type of user authentication required for accessing the asset. |
| SYNC\_TYPE | 

Type: number

Value range: see [SyncType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#synctype)

 | No | Type of sync supported by the asset. |
| IS\_PERSISTENT | Type: Boolean | No | Whether to retain the asset when the application is uninstalled. The value **true** means to retain the asset even after the application is uninstalled. The value **false** means the opposite. |
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
| REQUIRE\_ATTR\_ENCRYPTED14+ | Type: Boolean | No | Whether to delete the encrypted data of service customized supplementary information. The value **true** means to delete the encrypted data of service customized supplementary information; the value **false** means to delete the non-encrypted data of service customized supplementary information. The default value is **false**. |
| GROUP\_ID18+ | 

Type: Uint8Array

Length: 7-127 bytes

 | No | Group to which the asset to be removed belongs. By default, this parameter is not specified. |

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/r2-3WkbrRfC9mrPhJvi2tA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56FA75DC59706E923E470362325D9BB421BC7FA0A2242D97C83A8CD9765BE75F)

The **asset** module provides asynchronous and synchronous APIs. The following uses the asynchronous APIs as an example. For more information about the APIs, see [Asset Store Service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset).

For details about how to remove an asset from a group, see [Removing an Asset from a Group](../managing-assets-in-a-group-arkts/document.md#removing-an-asset-from-a-group).

Before removing an asset, ensure that the asset exists. For details about how to add an asset, see [Adding an Asset](../adding-an-asset-arkts/document.md). Otherwise, the **NOT\_FOUND** error (24000002) is reported.

Remove asset **demo\_alias**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function removeAsset(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // Specify the asset alias to remove a single asset. To remove all assets, leave the alias unspecified.
  try {
    await asset.remove(query).then(() => {
      console.info(\`Succeeded in removing Asset.\`);
      result = 'Succeeded in removing Asset';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to remove Asset. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to remove Asset';
    });
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to remove Asset. Code is ${err.code}, message is ${err.message}\`);
    result = 'Failed to remove Asset';
  }
  return result;
}
