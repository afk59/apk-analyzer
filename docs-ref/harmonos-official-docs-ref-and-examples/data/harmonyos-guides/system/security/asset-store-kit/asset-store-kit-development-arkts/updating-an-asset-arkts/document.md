# Updating an Asset (ArkTS)

#### Available APIs

You can use [update(query: AssetMap, attributesToUpdate: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetupdate), an asynchronous API, or [updateSync(query: AssetMap, attributesToUpdate: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetupdatesync12), a synchronous API, to update an asset.

The following table describes the attributes of **AssetMap** for updating an asset.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a8/v3/TPV6yp1PSI-NYpUpA_4Thw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=FED265976D128429DF6CF0AA1973311DB286B44F70EEE3008F18680AA409B547)

In the following table, the attributes **ALIAS** and those starting with **DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

-   Attributes of **AssetMap** in **query**:
    
    | Attribute Name (Tag) | Value | Mandatory | Description |
    | :-- | :-- | :-- | :-- |
    | ALIAS | 
    Type: Uint8Array
    
    Length: 1-256 bytes
    
     | Yes | Asset alias, which uniquely identifies an asset. |
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
    
     | No | Asset sync type. |
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
    | REQUIRE\_ATTR\_ENCRYPTED14+ | Type: Boolean | No | Whether to update the encrypted data of service customized supplementary information. The value **true** means to update the encrypted data of service customized supplementary information; the value **false** means to update the non-encrypted data of service customized supplementary information. Default value: **false**. |
    | GROUP\_ID18+ | 
    
    Type: Uint8Array
    
    Length: 7-127 bytes
    
     | No | Group to which the asset to be updated belongs. By default, this parameter is not specified. |
    
-   Attributes of **AssetMap** in **attributesToUpdate**:
    
    | Attribute Name (Tag) | Value | Mandatory | Description |
    | :-- | :-- | :-- | :-- |
    | SECRET | 
    Type: Uint8Array
    
    Length: 1-1024 bytes
    
     | No | New asset in plaintext. |
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
    

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e2/v3/pOHwWA-FR1iGBfv07-mkOQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=01F364FEDF3FECC41EC4C9A1D96E742EEE59EC4E1577C0AD5B5EAE0C9457C699)

The **asset** module provides asynchronous and synchronous APIs. The following uses the asynchronous APIs as an example. For more information about the APIs, see [Asset Store Service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset).

For details about how to update an asset in a group, see [Updating an asset in a Group](../managing-assets-in-a-group-arkts/document.md#updating-an-asset-in-a-group).

Before updating an asset, ensure that the asset exists. For details about how to add an asset, see [Adding an Asset](../adding-an-asset-arkts/document.md). Otherwise, the **NOT\_FOUND** error (24000002) is reported.

Update asset **demo\_alias** as follows: change the asset plaintext to **demo\_pwd\_new** and additional attribute to **demo\_label\_new**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function updateAsset(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
  let attrsToUpdate: asset.AssetMap = new Map();
  attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo\_pwd\_new'));
  attrsToUpdate.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label\_new'));
  try {
    await asset.update(query, attrsToUpdate).then(() => {
      console.info(\`Succeeded in updating Asset.\`);
      result = 'Succeeded in updating Asset';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to update Asset. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to update Asset';
    });
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to update Asset. Code is ${err.code}, message is ${err.message}\`);
    result = 'Failed to update Asset';
  }
  return result;
}
