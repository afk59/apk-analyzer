# Syncing Assets (Backup and Restore) (ArkTS)

#### Adding Assets That Support Sync

Add an asset with the password **demo\_pwd**, alias **demo\_alias**, and additional information **demo\_label**.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { BusinessError } from '@kit.BasicServicesKit';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

export async function addSyncAsset(): Promise<string> {
  let result: string = '';
  let attr: asset.AssetMap = new Map();
  attr.set(asset.Tag.SECRET, stringToArray('demo\_pwd'));
  attr.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
  attr.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label'));
  attr.set(asset.Tag.SYNC\_TYPE, asset.SyncType.TRUSTED\_DEVICE); // You need to specify the sync type between trusted devices (for example, clone between old and new devices).

  try {
    await asset.add(attr).then(() => {
      console.info(\`Succeeded in adding Asset with sync.\`);
      result = 'Succeeded in adding Asset with sync';
    }).catch((err: BusinessError) => {
      console.error(\`Failed to add Asset with sync. Code is ${err.code}, message is ${err.message}\`);
      result = 'Failed to add Asset with sync';
    })
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to add Asset with sync. Code is ${err?.code}, message is ${err?.message}\`);
    result = 'Failed to add Asset with sync';
  }
  return result;
}

#### Accessing the Backup and Restore Extension Capability

To trigger the backup and restore of application data, see [Accessing Backup and Restore](../../../../../application-framework/core-file-kit/application-files/application-data-backup-and-restore/accessing-backup-and-restore/document.md).

#### Querying the Sync Result of Assets

## Available APIs

You can call [asset.querySyncResult](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetquerysyncresult20) to query the sync result of assets. For more information, see the API reference.

The following table describes the attributes of **AssetMap** for querying the sync result of assets.

| Attribute Name (Tag) | Attribute Content (Asset\_Value) | Mandatory/Optional | Description |
| :-- | :-- | :-- | :-- |
| REQUIRE\_ATTR\_ENCRYPTED14+ | Type: Boolean | Yes | Whether to query the sync result of the asset whose custom additional information is encrypted. The value **true** means to query the sync result; the value **false** means the opposite. The default value is **false**. |
| GROUP\_ID18+ | 
Type: Uint8Array

Length: 7-127 bytes

 | Yes | Group to which the asset to be queried belongs. By default, this parameter is not specified. |

## Sample Code

import { asset } from '@kit.AssetStoreKit';
import { BusinessError } from '@kit.BasicServicesKit';

export async function querySyncResult(): Promise<string> {
  let result: string = '';
  let query: asset.AssetMap = new Map();
  await asset.querySyncResult(query).then((res: asset.SyncResult) => {
    console.info(\`Succeeded in querying sync result: ${JSON.stringify(res)}\`);
    result = 'Succeeded in querying sync result';
  }).catch((err: BusinessError) => {
    console.error(\`Failed to query sync result of Asset. Code is ${err.code}, message is ${err.message}\`);
    result = 'Failed to query sync result of Asset';
  });
  return result;
}

#### Notes and Constraints

For a successful sync between trusted devices, the assets of both old and new devices must be accessible. Otherwise, the sync might fail.

-   For assets that are accessible only when a password is set, the sync will fail if no lock screen password is set on either the old or new device.
    
-   For assets that are accessible only when the screen is unlocked, the sync will fail if the screen of either the old or new device is locked.
    
-   For assets that are accessible only after user authentication, the sync will fail if no lock screen password is set on the old device.
