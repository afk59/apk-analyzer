# @ohos.security.asset (Asset Store Service)

The asset store service (ASSET) provides secure storage and management of sensitive data less than 1024 bytes in size, including passwords, app tokens, and other critical data (such as bank card numbers).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/gM9JrjOJTcucQZ-B_SIRnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=98FC9416D5C5F6171E49275A33FDDF2BD2B6D267315D69FA20BD9EE2CDE59B6F)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### Modules to Import

import { asset } from '@kit.AssetStoreKit';

#### asset.add

add(attributes: AssetMap): Promise<void>

Adds an asset. This API uses a promise to return the result.

To set [IS\_PERSISTENT](#tag), the application must have the ohos.permission.STORE\_PERSISTENT\_DATA permission.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attributes | [AssetMap](#assetmap) | Yes | Attributes of the asset to add, including the asset plaintext, access control attributes, and custom data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The caller doesn't have the permission. |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000003 | The asset already exists. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000014 | The file operation failed. |
| 24000015 | Getting the system time failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo\_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE\_FIRST\_UNLOCKED);
attr.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label'));
asset.add(attr).then(() => {
  console.info(\`Succeeded in adding Asset.\`);
});

#### asset.addSync12+

addSync(attributes: AssetMap): void

Add an asset. This API returns the result synchronously.

To set [IS\_PERSISTENT](#tag), the application must have the ohos.permission.STORE\_PERSISTENT\_DATA permission.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| attributes | [AssetMap](#assetmap) | Yes | Attributes of the asset to add, including the asset plaintext, access control attributes, and custom data. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 201 | The caller doesn't have the permission. |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000003 | The asset already exists. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000014 | The file operation failed. |
| 24000015 | Getting the system time failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let attr: asset.AssetMap = new Map();
attr.set(asset.Tag.SECRET, stringToArray('demo\_pwd'));
attr.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
attr.set(asset.Tag.ACCESSIBILITY, asset.Accessibility.DEVICE\_FIRST\_UNLOCKED);
attr.set(asset.Tag.DATA\_LABEL\_NORMAL\_1, stringToArray('demo\_label'));
asset.addSync(attr);

#### asset.remove

remove(query: AssetMap): Promise<void>

Removes one or more assets. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the asset to remove, such as the asset alias, access control attributes, and custom data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Incorrect parameter types.

2\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000015 | Getting the system time failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
asset.remove(query).then(() => {
  console.info(\`Succeeded in removing Asset.\`);
});

#### asset.removeSync12+

removeSync(query: AssetMap): void

Removes one or more assets. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the asset to remove, such as the asset alias, access control attributes, and custom data. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Incorrect parameter types.

2\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000015 | Getting the system time failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
asset.removeSync(query);

#### asset.update

update(query: AssetMap, attributesToUpdate: AssetMap): Promise<void>

Updates an asset. This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the asset to update, such as the asset alias, access control attributes, and custom data. |
| attributesToUpdate | [AssetMap](#assetmap) | Yes | New attributes of the asset, such as the asset plaintext and custom data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000015 | Getting the system time failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo\_pwd\_new'));
asset.update(query, attrsToUpdate).then(() => {
  console.info(\`Succeeded in updating Asset.\`);
});

#### asset.updateSync12+

updateSync(query: AssetMap, attributesToUpdate: AssetMap): void

Updates an asset. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the asset to update, such as the asset alias, access control attributes, and custom data. |
| attributesToUpdate | [AssetMap](#assetmap) | Yes | New attributes of the asset, such as the asset plaintext and custom data. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000015 | Getting the system time failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
let attrsToUpdate: asset.AssetMap = new Map();
attrsToUpdate.set(asset.Tag.SECRET, stringToArray('demo\_pwd\_new'));
asset.updateSync(query, attrsToUpdate);

#### asset.preQuery

preQuery(query: AssetMap): Promise<Uint8Array>

Performs preprocessing for the asset query. This API is used when user authentication is required for the access to the asset. After the user authentication is successful, call [asset.query](#assetquery) and [asset.postQuery](#assetpostquery). This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the asset to query, such as the asset alias, access control attributes, and custom data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Uint8Array> | 
Promise used to return a challenge value.

**Note**: The challenge value is used for subsequent user authentication.

 |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Incorrect parameter types.

2\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000016 | The cache exceeds the limit. |
| 24000017 | The capability is not supported. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
asset.preQuery(query).then((challenge: Uint8Array) => {
  console.info(\`Succeeded in pre-querying Asset.\`);
});

#### asset.preQuerySync12+

preQuerySync(query: AssetMap): Uint8Array

Performs preprocessing for the asset query. This API is used when user authentication is required for the access to the asset. After the user authentication is successful, call [asset.querySync](#assetquerysync12) and [asset.postQuerySync](#assetpostquerysync12). This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the asset to query, such as the asset alias, access control attributes, and custom data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Uint8Array | 
Challenge value.

**Note**: The challenge value is used for subsequent user authentication.

 |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Incorrect parameter types.

2\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000016 | The cache exceeds the limit. |
| 24000017 | The capability is not supported. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
let challenge: Uint8Array = asset.preQuerySync(query);
console.info(\`Succeeded in pre-querying with sync, the challenge is: \`, challenge);

#### asset.query

query(query: AssetMap): Promise<Array<AssetMap>>

Queries one or more assets. If user authentication is required for the access to the asset, call [asset.preQuery](#assetprequery) before this API and call [asset.postQuery](#assetpostquery) after this API. For details about the development procedure, see [Querying an Asset with User Authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/asset-js-query-auth). This API uses a promise to return the result.

If no asset is found, an exception indicating that no asset is found is thrown instead of an empty query result list.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the asset to query, such as the asset alias, access control attributes, and custom data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<Array<AssetMap>> | Promise used to return the result obtained. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Incorrect parameter types.

2\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000004 | Access denied. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000017 | The capability is not supported. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
// If only the asset attributes need to be returned, set RETURN\_TYPE to ATTRIBUTES. The attributes do not need to be decrypted, so the query takes a short time.
query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ALL); // Return all asset information, including the attributes and asset plaintext. The plaintext needs to be decrypted, so the query takes a long time.
asset.query(query).then((res: Array<asset.AssetMap>) => {
  for (let i = 0; i < res.length; i++) {
    // Parse the attributes.
    let accessibility: number = res\[i\].get(asset.Tag.ACCESSIBILITY) as number;
    console.info(\`Succeeded in getting accessibility, which is: ${accessibility}.\`);
  }
  console.info(\`Succeeded in querying Asset.\`);
});

#### asset.querySync12+

querySync(query: AssetMap): Array<AssetMap>

Queries one or more assets. If user authentication is required for the access to the asset, call [asset.preQuerySync](#assetprequerysync12) before this API and call [asset.postQuerySync](#assetpostquerysync12) after this API. For details about the development procedure, see [Querying an Asset with User Authentication](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/asset-js-query-auth). This API returns the result synchronously.

If no asset is found, an exception indicating that no asset is found is thrown instead of an empty query result list.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the asset to query, such as the asset alias, access control attributes, and custom data. |

**Return value**

| Type | Description |
| :-- | :-- |
| Array<AssetMap> | Array of query results. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Incorrect parameter types.

2\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000002 | The asset is not found. |
| 24000004 | Access denied. |
| 24000005 | The screen lock status does not match. |
| 24000006 | Insufficient memory. |
| 24000007 | The asset is corrupted. |
| 24000008 | The database operation failed. |
| 24000009 | The cryptography operation failed. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000017 | The capability is not supported. |

**Example**

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';

function stringToArray(str: string): Uint8Array {
  let textEncoder = new util.TextEncoder();
  return textEncoder.encodeInto(str);
}

let query: asset.AssetMap = new Map();
query.set(asset.Tag.ALIAS, stringToArray('demo\_alias'));
// If only the asset attributes need to be returned, set RETURN\_TYPE to ATTRIBUTES. The attributes do not need to be decrypted, so the query takes a short time.
query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ALL); // Return all asset information, including the attributes and asset plaintext. The plaintext needs to be decrypted, so the query takes a long time.
let res: Array<asset.AssetMap> = asset.querySync(query);
for (let i = 0; i < res.length; i++) {
  // Parse the attributes.
  let accessibility: number = res\[i\].get(asset.Tag.ACCESSIBILITY) as number;
  console.info(\`Succeeded in getting accessibility, which is: ${accessibility}.\`);
}
console.info(\`Succeeded in querying Asset.\`);

#### asset.postQuery

postQuery(handle: AssetMap): Promise<void>

Performs postprocessing for the asset query. This API is used when user authentication is required for the access to an asset. It must be used with [asset.preQuery](#assetprequery). This API uses a promise to return the result.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handle | [AssetMap](#assetmap) | Yes | Handle of the query operation, including the challenge value returned by [asset.preQuery](#assetprequery). |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<void> | Promise that returns no value. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';

let handle: asset.AssetMap = new Map();
// The new Uint8Array(32) is only an example. Pass in the challenge value returned by asset.preQuery.
handle.set(asset.Tag.AUTH\_CHALLENGE, new Uint8Array(32));
asset.postQuery(handle).then(() => {
  console.info(\`Succeeded in post-querying Asset.\`);
});

#### asset.postQuerySync12+

postQuerySync(handle: AssetMap): void

Performs postprocessing for the asset query. This API is used when user authentication is required for the access to the asset. This API must be used with [asset.preQuerySync](#assetprequerysync12) together. This API returns the result synchronously.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| handle | [AssetMap](#assetmap) | Yes | Handle of the query operation, including the challenge value returned by [asset.preQuerySync](#assetprequerysync12). |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 401 | 
Parameter error. Possible causes:

1\. Mandatory parameters are left unspecified.

2\. Incorrect parameter types.

3\. Parameter verification failed.

 |
| 24000001 | The ASSET service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';

let handle: asset.AssetMap = new Map();
// The new Uint8Array(32) is only an example. Pass in the challenge value returned by asset.preQuerySync.
handle.set(asset.Tag.AUTH\_CHALLENGE, new Uint8Array(32));
asset.postQuerySync(handle)

#### asset.querySyncResult20+

querySyncResult(query: AssetMap): Promise<SyncResult>

Queries the result of the sync operation. This API uses a promise to return the result.

**System capability**: SystemCapability.Security.Asset

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| query | [AssetMap](#assetmap) | Yes | Attributes of the sync result to query, such as the group to which the asset belongs and whether the custom attribute information is encrypted. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[SyncResult](#syncresult20)\> | Promise used to return the result. |

**Error codes**

For details about the error codes, see [Asset Store Service Error Codes](../../error-codes/asset-store-service-error-code/document.md).

| ID | Error Message |
| :-- | :-- |
| 24000001 | The ASSET service is unavailable. |
| 24000006 | Insufficient memory. |
| 24000010 | IPC failed. |
| 24000011 | Calling the Bundle Manager service failed. |
| 24000012 | Calling the OS Account service failed. |
| 24000013 | Calling the Access Token service failed. |
| 24000014 | The file operation failed. |
| 24000018 | Parameter verification failed. |

**Example**

import { asset } from '@kit.AssetStoreKit';

let query: asset.AssetMap = new Map();
asset.querySyncResult(query).then((res: asset.SyncResult) => {
  console.info(\`Succeeded in querying sync result: ${JSON.stringify(res)}\`);
});

#### TagType

Enumerates the asset attribute types.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| BOOL | 0x01 << 28 | Boolean. |
| NUMBER | 0x02 << 28 | Number. |
| BYTES | 0x03 << 28 | Byte array. |

#### Tag

Enumerate the keys of asset attributes ([AssetMap](#assetmap)), which are in key-value (KV) pairs.

**System capability**: SystemCapability.Security.Asset

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/K0P4J3ddRJid5naFuCSXBQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062329Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0F311E996B0A300D65FE07CE0217FEC263EE8C565F3C06B66D6A8B9DABB62B05)

The following table lists all enums of **Tag**. The specific tags and the value range of tag values vary with the API you use. For details, see [Introduction to Asset Store Kit](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/asset-store-kit-overview).

| Name | Value | Description |
| :-- | :-- | :-- |
| SECRET | TagType.BYTES | 0x01 | 
Asset plaintext.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| ALIAS | TagType.BYTES | 0x02 | 

Asset alias, which uniquely identifies an asset.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| ACCESSIBILITY | TagType.NUMBER | 0x03 | 

Access control based on the lock screen status.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| REQUIRE\_PASSWORD\_SET | TagType.BOOL | 0x04 | 

Whether the asset is accessible only when a lock screen password is set.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AUTH\_TYPE | TagType.NUMBER | 0x05 | 

Type of user authentication required for accessing the asset.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AUTH\_VALIDITY\_PERIOD | TagType.NUMBER | 0x06 | 

Validity period of the user authentication.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AUTH\_CHALLENGE | TagType.BYTES | 0x07 | 

Challenge for the user authentication.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| AUTH\_TOKEN | TagType.BYTES | 0x08 | 

Authorization token obtained after the user authentication is successful.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| SYNC\_TYPE | TagType.NUMBER | 0x10 | 

Asset sync type.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| IS\_PERSISTENT | TagType.BOOL | 0x11 | Whether to retain the asset when the application is uninstalled. |
| DATA\_LABEL\_CRITICAL\_1 | TagType.BYTES | 0x20 | 

Additional asset data customized by the service with integrity protection.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_CRITICAL\_2 | TagType.BYTES | 0x21 | 

Additional asset data customized by the service with integrity protection.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_CRITICAL\_3 | TagType.BYTES | 0x22 | 

Additional asset data customized by the service with integrity protection.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_CRITICAL\_4 | TagType.BYTES | 0x23 | 

Additional asset data customized by the service with integrity protection.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_NORMAL\_1 | TagType.BYTES | 0x30 | 

Additional asset data customized by the service without integrity protection.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_NORMAL\_2 | TagType.BYTES | 0x31 | 

Additional asset data customized by the service without integrity protection.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_NORMAL\_3 | TagType.BYTES | 0x32 | 

Additional asset data customized by the service without integrity protection.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_NORMAL\_4 | TagType.BYTES | 0x33 | 

Additional asset data customized by the service without integrity protection.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_NORMAL\_LOCAL\_112+ | TagType.BYTES | 0x34 | 

Local information about the asset. The value is assigned by the service without integrity protection and will not be synced.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_NORMAL\_LOCAL\_212+ | TagType.BYTES | 0x35 | 

Local information about the asset. The value is assigned by the service without integrity protection and will not be synced.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_NORMAL\_LOCAL\_312+ | TagType.BYTES | 0x36 | 

Local information about the asset. The value is assigned by the service without integrity protection and will not be synced.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_LABEL\_NORMAL\_LOCAL\_412+ | TagType.BYTES | 0x37 | 

Local information about the asset. The value is assigned by the service without integrity protection and will not be synced.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| RETURN\_TYPE | TagType.NUMBER | 0x40 | 

Type of the asset query result to return.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| RETURN\_LIMIT | TagType.NUMBER | 0x41 | 

Maximum number of asset records to return.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| RETURN\_OFFSET | TagType.NUMBER | 0x42 | 

Offset of the asset query result.

**Note**: This parameter specifies the starting asset record to return in batch asset query.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| RETURN\_ORDERED\_BY | TagType.NUMBER | 0x43 | 

Sorting order of the query results. Currently, the results can be sorted only by **ASSET\_TAG\_DATA\_LABEL**.

**Note**: By default, assets are returned in the order in which they are added.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| CONFLICT\_RESOLUTION | TagType.NUMBER | 0x44 | 

Policy for resolving the conflict (for example, a duplicate alias).

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| UPDATE\_TIME12+ | TagType.BYTES | 0x45 | 

Data update time, in timestamp.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| OPERATION\_TYPE12+ | TagType.NUMBER | 0x46 | Additional operation type. |
| REQUIRE\_ATTR\_ENCRYPTED14+ | TagType.BOOL | 0x47 | 

Whether to encrypt the additional asset information customized by the service.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| GROUP\_ID18+ | TagType.BYTES | 0x48 | 

Group to which the asset belongs.

 |
| WRAP\_TYPE18+ | TagType.NUMBER | 0x49 | 

Encrypted import/export type supported by the asset.

 |

#### Value

type Value = boolean | number | Uint8Array

Represents the value of each attribute in [AssetMap](#assetmap).

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

| Type | Description |
| :-- | :-- |
| boolean | The value is a Boolean value, that is, **true** or **false**. |
| number | The value is a number. It can be an enumerated value or a numeric value. |
| Uint8Array | The value is a byte array, and the content is defined by the service. |

#### AssetMap

type AssetMap = Map<Tag, Value>

Represents a set of asset attributes in the form of KV pairs.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

| Type | Description |
| :-- | :-- |
| Map<Tag, Value> | The value type is Map. For details about the range of the KV pair, see [Tag](#tag) and [Value](#value). |

#### Accessibility

Enumerates the types of access control based on the lock screen status.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| DEVICE\_POWERED\_ON | 0 | The asset can be accessed after the device is powered on. |
| DEVICE\_FIRST\_UNLOCKED | 1 | 
The asset can be accessed only after the device is unlocked for the first time.

**Note**: If no lock screen password is set, this option is equivalent to **DEVICE\_POWERED\_ON**.

 |
| DEVICE\_UNLOCKED | 2 | 

The asset can be accessed only when the device is unlocked.

**Note**: If no lock screen password is set, this option is equivalent to **DEVICE\_POWERED\_ON**.

 |

#### AuthType

Enumerates the types of user authentication supported by an asset.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| NONE | 0x00 | No user authentication is required before the asset is accessed. |
| ANY | 0xFF | The asset can be accessed if any user authentication (such as PIN, facial, or fingerprint authentication) is successful. |

#### SyncType

Enumerates the sync types supported by an asset.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| NEVER | 0 | Asset sync is not allowed. |
| THIS\_DEVICE | 1 << 0 | 
Asset sync is allowed only on the local device, for example, in data restore on the local device.

**Note**: This field is reserved for future use and is not supported currently.

 |
| TRUSTED\_DEVICE | 1 << 1 | Asset sync is allowed only between trusted devices, for example, in the case of cloning. |
| TRUSTED\_ACCOUNT12+ | 1 << 2 | 

Asset sync is allowed only between the devices that are logged in with trusted accounts, for example, in cloud sync scenarios.

**Note**: This field is reserved for future use and is not supported currently.

 |

#### ReturnType

Enumerates the type of information returned by an asset query operation.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| ALL | 0 | 
The query result contains the asset in plaintext and its attributes.

**Note**: Use this option when you need to query the plaintext of a single asset.

 |
| ATTRIBUTES | 1 | 

The query result contains only the asset attributes.

**Note**: Use this option when you need to query attributes of multiple assets.

 |

#### ConflictResolution

Enumerates the policies for resolving conflicts (for example, a duplicate alias) when an asset is added.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| OVERWRITE | 0 | Overwrite the original asset. |
| THROW\_ERROR | 1 | Throw an exception for the service to perform subsequent processing. |

#### OperationType12+

Enumerates the types of additional operation to perform.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| NEED\_SYNC | 0 | Sync. |
| NEED\_LOGOUT | 1 | Logout. |

#### WrapType18+

Enumerates the encrypted import/export types supported by the asset.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| NEVER | 0 | Encrypted import/export is not allowed for the asset. |
| TRUSTED\_ACCOUNT | 1 | Encrypted import/export is allowed for the asset only on devices where a trusted account is logged in. |

#### SyncResult20+

Represents the sync result of an asset.

**System capability**: SystemCapability.Security.Asset

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| resultCode | number | Yes | No | Sync result code of an asset. If the sync is successful, the result code is **0**. If the sync fails, see [ErrorCode](#errorcode) for the result code. |
| totalCount | number | Yes | Yes | Total number of assets to be synced. |
| failedCount | number | Yes | Yes | Number of assets that fail to be synced. |

#### ErrorCode

Enumerates the error codes.

**System capability**: SystemCapability.Security.Asset

| Name | Value | Description |
| :-- | :-- | :-- |
| PERMISSION\_DENIED | 201 | The caller does not have the permission. |
| NOT\_SYSTEM\_APPLICATION12+ | 202 | The caller is not a system application. |
| INVALID\_ARGUMENT | 401 | 
Incorrect parameters are detected.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| SERVICE\_UNAVAILABLE | 24000001 | 

The asset service is unavailable.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| NOT\_FOUND | 24000002 | 

Failed to find the asset.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DUPLICATED | 24000003 | 

The specified asset already exists.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| ACCESS\_DENIED | 24000004 | 

The access is denied.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| STATUS\_MISMATCH | 24000005 | 

The screen lock status does not match.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| OUT\_OF\_MEMORY | 24000006 | 

The system memory is insufficient.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATA\_CORRUPTED | 24000007 | 

The asset is corrupted.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| DATABASE\_ERROR | 24000008 | 

The database operation failed.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| CRYPTO\_ERROR | 24000009 | 

The crypto operation failed.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| IPC\_ERROR | 24000010 | 

IPC failed.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| BMS\_ERROR | 24000011 | 

The Bundle Manager service is abnormal.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| ACCOUNT\_ERROR | 24000012 | 

The account system service is abnormal.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| ACCESS\_TOKEN\_ERROR | 24000013 | 

The Access Token service is abnormal.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| FILE\_OPERATION\_ERROR | 24000014 | 

The file operation failed.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| GET\_SYSTEM\_TIME\_ERROR | 24000015 | 

Failed to obtain the system time.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| LIMIT\_EXCEEDED | 24000016 | 

The number of cached records exceeds the upper limit.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| UNSUPPORTED | 24000017 | 

The feature is not supported.

**Atomic service API**: This API can be used in atomic services since API version 14.

 |
| PARAM\_VERIFICATION\_FAILED20+ | 24000018 | 

Parameter verification failed.

**Atomic service API**: This API can be used in atomic services since API version 20.

 |
