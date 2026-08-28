# Querying Assets (ArkTS)

#### Available APIs

You can use [query(query: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetquery), an asynchronous API, and [querySync(query: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetquerysync12), a synchronous API, to query assets.

The following table describes the attributes of **AssetMap** for querying an asset.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/55/v3/7tIglOJHR_6Av896EcvTAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=42496390004A0893214F654B566B70FBA6701C6C6DBD53C087B40A72D2E459CE)

In the following table, the attributes **ALIAS** and those starting with **DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

It takes a long time to query the plaintext of the asset attribute **SECRET** due to the need of decryption. Therefore, **RETURN\_TYPE** must be set to **ALL**. For other asset attributes, decryption is not required, so the query takes a short time. Therefore, **RETURN\_TYPE** must be set to **ATTRIBUTES**.

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

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_CRITICAL\_2 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_CRITICAL\_3 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_CRITICAL\_4 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_1 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_2 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_3 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| DATA\_LABEL\_NORMAL\_4 | 

Type: Uint8Array

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

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
| RETURN\_TYPE | 

Type: number

Value range: see [ReturnType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#returntype)

 | No | Type of the asset query result to return. |
| RETURN\_LIMIT | Type: number | No | Maximum number of asset records returned. |
| RETURN\_OFFSET | 

Type: number

Value range: 1-65536

 | No | 

Offset of the asset query result.

**Note**: This parameter specifies the starting asset record to return in batch asset query.

 |
| RETURN\_ORDERED\_BY | 

Type: number

Value: asset.Tag.DATA\_LABEL\_xxx.

 | No | 

How the query results are sorted. Currently, the results can be sorted only by **DATA\_LABEL**.

**Note**: By default, assets are returned in the order in which they are added.

 |
| REQUIRE\_ATTR\_ENCRYPTED14+ | Type: Boolean | No | Whether to query the encrypted data of service customized supplementary information. The value **true** means to query the encrypted data of service customized supplementary information; the value **false** means to query the non-encrypted data of service customized supplementary information. The default value is **false**. |
| GROUP\_ID18+ | 

Type: Uint8Array

Length: 7-127 bytes

 | No | Group to which the asset to be queried belongs. By default, this parameter is not specified. |

#### Constraints

Assets queried in batches need to be transmitted to services through the IPC channel. Due to the limitation of the IPC buffer size, you are advised to query a maximum of 40 assets at a time.

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/49/v3/H_JDeqKURxal8TrRhnd4hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9B58B12D9FE58497905DCB70941F67700183E21FB5BA1FF504B7AC8F78A3F275)

The **asset** module provides asynchronous and synchronous APIs. The following uses the asynchronous APIs as an example. For more information about the APIs, see [Asset Store Service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset).

For details about how to query the plaintext of an asset in a group, see [Querying the Plaintext of an Asset in a Group](../managing-assets-in-a-group-arkts/document.md#querying-the-plaintext-of-an-asset-in-a-group). For details about how to query the attributes of an asset in a group, see [Querying the Attributes of an Asset in a Group](../managing-assets-in-a-group-arkts/document.md#querying-the-attributes-of-an-asset-in-a-group).

Before querying an asset, ensure that the asset exists. For details about how to add an asset, see [Adding an Asset](../adding-an-asset-arkts/document.md). Otherwise, the **NOT\_FOUND** error (24000002) is reported.

## Querying the Plaintext of an Asset

Query the plaintext of asset **demo\_alias**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

function arrayToString(arr: Uint8Array): string {
  let textDecoder = util.TextDecoder.create('utf-8', { ignoreBOM: true });
  let str = textDecoder.decodeToString(arr, { stream: false });
  return str;
}

export async function queryAssetPlaintext(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // Specify the alias of the asset to query.
  query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ALL); // Return all asset information, including the attributes and asset plaintext. The plaintext needs to be decrypted, so the query takes a long time.
  try {
    await asset.query(query).then((res: Array<asset.AssetMap>) => {
      for (let i = 0; i < res.length; i++) {
        // Parse the secret.
        let secret: Uint8Array = res\[i\].get(asset.Tag.SECRET) as Uint8Array;
        // Convert Uint8Array into the string type.
        let secretStr: string = arrayToString(secret);
      }
      result = 'Succeeded in querying Asset plaintext';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to query Asset plaintext. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to query Asset plaintext';
    });
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to query Asset plaintext. Code is ${err.code}, message is ${err.message}\`);
    result = 'Failed to query Asset plaintext';
  }
  return result;
}

## Querying Attributes of an Asset

Query attributes of asset **demo\_alias**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function queryAssetAttribute(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // Specify the alias of the asset to query.
  query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ATTRIBUTES); // Return only the attributes of the asset, that is, the result does not include the asset plaintext.
  try {
    await asset.query(query).then((res: Array<asset.AssetMap>) => {
      for (let i = 0; i < res.length; i++) {
        // Parse the attributes.
        let accessibility: number = res\[i\].get(asset.Tag.ACCESSIBILITY) as number;
        console.info(\`Succeeded in getting accessibility, which is: ${accessibility}.\`);
      }
      result = 'Succeeded in querying Asset attribute';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to query Asset attribute. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to query Asset attribute';
    });
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to query Asset attribute. Code is ${err.code}, message is ${err.message}\`);
    result = 'Failed to query Asset attribute';
  }
  return result;
}

## Querying Attributes of Assets

Query attributes of assets whose label is **demo\_label** in batches. A total of 10 records that meet the conditions are returned. The results are sorted by the content of the **DATA\_LABEL\_NORMAL\_1** attribute.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function queryBatchAssetAttributes(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ATTRIBUTES); // Return only the attributes of the asset, that is, the result does not include the asset plaintext.
  query.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label'));
  query.set(asset.Tag.RETURN\_LIMIT, 10); // Return information about 10 assets that match the search criteria.
  query.set(asset.Tag.RETURN\_ORDERED\_BY, asset.Tag.DATA\_LABEL\_NORMAL\_1); // Sort the query results by DATA\_LABEL\_NORMAL\_1.
  try {
    await asset.query(query).then((res: Array<asset.AssetMap>) => {
      for (let i = 0; i < res.length; i++) {
        // Parse the attributes.
        let accessibility: number = res\[i\].get(asset.Tag.ACCESSIBILITY) as number;
        console.info(\`Succeeded in getting accessibility, which is: ${accessibility}.\`);
      }
      result = 'Succeeded in querying batch Asset attributes';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to query batch Asset attributes. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to query batch Asset attributes';
    });
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to query batch Asset attributes. Code is ${err.code}, message is ${err.message}\`);
    result = 'Failed to query batch Asset attributes';
  }
  return result;
}
