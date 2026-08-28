# Managing Assets in a Group (ArkTS)

Before managing assets in a group, ensure that you are familiar with the following operations:

-   [Adding an Asset (ArkTS)](../adding-an-asset-arkts/document.md)
-   [Removing Assets (ArkTS)](../removing-assets-arkts/document.md)
-   [Updating an Asset (ArkTS)](../updating-an-asset-arkts/document.md)
-   [Querying Assets (ArkTS)](../querying-assets-arkts/document.md)

#### Prerequisites

Set the group ID, such as **demo\_group\_id**, in the **app.json5** file. You can set multiple group IDs for a group.

{
  "app": {
    // Other configuration items are omitted here.
    "assetAccessGroups": \[
      "demo\_group\_id",
      // "another\_group\_id",
      // ...
    \]
  }
}

#### Adding an Asset to a Group

Add an asset to the group, with the password **demo\_pwd**, alias **demo\_alias**, and additional attribute **demo\_label**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function addGroupAsset(): Promise<string> {
  let result: string = '';
  let attr: asset.AssetMap = new Map();
  attr.set(asset.Tag.SECRET, stringToArray('demo\_pwd'));
  attr.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
  attr.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label'));
  attr.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
  try {
    await asset.add(attr).then(() => {
      console.info(\`Succeeded in adding Asset to the group.\`);
      result = 'Succeeded in adding Asset to the group';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to add Asset to the group. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to add Asset to the group';
    })
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to add Asset to the group. Code is ${err?.code}, message is ${err?.message}\`);
    result = 'Failed to add Asset to the group';
  }
  return result;
}

#### Removing an Asset from a Group

Remove asset **demo\_alias** from group **demo\_group\_id**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function removeGroupAsset(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // Specify the alias to delete a single asset from the group. You can also delete multiple assets without specifying the alias.
  query.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
  try {
    await asset.remove(query).then(() => {
      console.info(\`Succeeded in removing Asset from the group.\`);
      result = 'Succeeded in removing Asset from the group';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to remove Asset from the group. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to remove Asset from the group';
    });
  } catch (err) {
    console.error(\`Failed to remove Asset from the group. Code is ${err?.code}, message is ${err?.message}\`);
    result = 'Failed to remove Asset from the group';
  }
  return result;
}

#### Updating an asset in a Group

Update asset **demo\_alias** in group **demo\_group\_id** as follows: change the asset plaintext to **demo\_pwd\_new** and the additional attribute to **demo\_label\_new**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function updateGroupAsset(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
  query.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
  let attrsToUpdate: asset.AssetMap = new Map();
  attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo\_pwd\_new'));
  attrsToUpdate.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label\_new'));
  try {
    await asset.update(query, attrsToUpdate).then(() => {
      console.info(\`Succeeded in updating Asset in the group.\`);
      result = 'Succeeded in updating Asset in the group';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to update Asset in the group. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to update Asset in the group';
    });
  } catch (err) {
    console.error(\`Failed to update Asset in the group. Code is ${err?.code}, message is ${err?.message}\`);
    result = 'Failed to update Asset in the group';
  }
  return result;
}

#### Querying the Plaintext of an Asset in a Group

Query the plaintext of asset **demo\_alias** in group **demo\_group\_id**.

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

export async function queryGroupAssetPlaintext(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // Specify the alias of the asset to query.
  query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ALL); // Return all asset information, including attributes and asset plaintext.
  query.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
  try {
    await asset.query(query).then((res: Array<asset.AssetMap>) => {
      for (let i = 0; i < res.length; i++) {
        // Parse the secret.
        let secret: Uint8Array = res\[i\].get(asset.Tag.SECRET) as Uint8Array;
        // Convert Uint8Array into the string type.
        let secretStr: string = arrayToString(secret);
      }
      result = 'Succeeded in querying group Asset plaintext';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to query Asset plaintext from the group. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to query Asset plaintext from the group';
    });
  } catch (err) {
    console.error(\`Failed to query Asset plaintext from the group. Code is ${err?.code}, message is ${err?.message}\`);
    result = 'Failed to query Asset plaintext from the group';
  }
  return result;
}

#### Querying the Attributes of an Asset in a Group

Query the attributes of asset **demo\_alias** in group **demo\_group\_id**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function queryGroupAssetAttribute(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  query.set(asset.Tag.ALIAS, stringToArray('demo\_alias')); // Specify the alias of the asset to query.
  query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ATTRIBUTES); // Return only the attributes of the asset, that is, the result does not include the asset plaintext.
  query.set(asset.Tag.GROUP\_ID, stringToArray('demo\_group\_id'));
  try {
    await asset.query(query).then((res: Array<asset.AssetMap>) => {
      for (let i = 0; i < res.length; i++) {
        // Parse the attributes.
        let accessibility: number = res\[i\].get(asset.Tag.ACCESSIBILITY) as number;
        console.info(\`Succeeded in getting accessibility, which is: ${accessibility}.\`);
      }
      result = 'Succeeded in querying group Asset attribute';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to query Asset attribute from the group. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to query Asset attribute from the group';
    });
  } catch (err) {
    console.error(\`Failed to query Asset attribute from the group. Code is ${err?.code}, message is ${err?.message}\`);
    result = 'Failed to query Asset attribute from the group';
  }
  return result;
}
