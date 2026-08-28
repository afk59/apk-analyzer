# Querying an Asset with User Authentication (ArkTS)

#### Available APIs

The following table describes the APIs used for querying an asset with user authentication. For more information, see the API reference.

| Asynchronous API | Synchronous API | Description |
| :-- | :-- | :-- |
| [preQuery(query: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetprequery) | [preQuerySync(query: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetprequerysync12) | Performs preprocessing. |
| [query(query: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetquery) | [querySync(query: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetquerysync12) | Queries the asset. |
| [postQuery(handle: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetpostquery) | [postQuerySync(handle: AssetMap)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset#assetpostquerysync12) | Performs postprocessing. |

The following table describes the attributes of **AssetMap** used for querying an asset with user authentication.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/79/v3/GeBfM_sSQG6ncdB-6-qHtQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B3BF61275D315BDE4B648F2DC8826017DDB77D4F7B5A3147123E79224428566)

In the following table, the attributes **ALIAS** and those starting with **DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

-   **preQuery()** parameters
    
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
    | AUTH\_VALIDITY\_PERIOD | 
    
    Type: number
    
    Value range: 1-600 seconds
    
     | No | The validity period of user authentication. The default value is **60**. |
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
    | REQUIRE\_ATTR\_ENCRYPTED14+ | Type: Boolean | No | Whether to query the encrypted data of service customized supplementary information. The value **true** means to query the encrypted data of service customized supplementary information; the value **false** means to query the non-encrypted data of service customized supplementary information. The default value is **false**. |
    | GROUP\_ID18+ | 
    
    Type: Uint8Array
    
    Length: 7-127 bytes
    
     | No | Group to which the asset to be queried belongs. By default, this parameter is not specified. |
    
-   **query()** parameters
    
    | Attribute Name (Tag) | Value | Mandatory | Description |
    | :-- | :-- | :-- | :-- |
    | ALIAS | 
    Type: Uint8Array
    
    Length: 1-256 bytes
    
     | Yes | Asset alias, which uniquely identifies an asset. |
    | AUTH\_CHALLENGE | 
    
    Type: Uint8Array
    
    Length: 32 bytes
    
     | Yes | Challenge for the user authentication. |
    | AUTH\_TOKEN | 
    
    Type: Uint8Array
    
    Length: 1-1024 bytes since API version 20
    
    Length: 148 bytes for API versions 11-19
    
     | Yes | Authorization token obtained after the user authentication is successful. |
    | RETURN\_TYPE | Type: number | Yes | Type of the asset query result to return. |
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
    | REQUIRE\_ATTR\_ENCRYPTED14+ | Type: Boolean | No | Whether to query the encrypted data of service customized supplementary information. The value **true** means to query the encrypted data of service customized supplementary information; the value **false** means to query the non-encrypted data of service customized supplementary information. The default value is **false**. |
    | GROUP\_ID18+ | 
    
    Type: Uint8Array
    
    Length: 7-127 bytes
    
     | No | Group to which the asset to be queried belongs. By default, this parameter is not specified. |
    
-   **postQuery()** parameters
    
    | Attribute Name (Tag) | Value | Mandatory | Description |
    | :-- | :-- | :-- | :-- |
    | AUTH\_CHALLENGE | 
    Type: Uint8Array
    
    Length: 32 bytes
    
     | Yes | Challenge for the user authentication. |
    | GROUP\_ID18+ | 
    
    Type: Uint8Array
    
    Length: 7-127 bytes
    
     | No | Group to which the asset to be cleared belongs. By default, the assets that do not belong to any group in the memory are cleared. |
    

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/eTwyQFDLSY6aqEAlnyhhxw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8224D128F008F9FD8D59F21C8900417A122C36B56F02E78D4DB6133EF04EE43)

The **asset** module provides asynchronous and synchronous APIs. The following uses the asynchronous APIs as an example. For more information about the APIs, see [Asset Store Service](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-asset).

Before querying an asset, ensure that the asset that requires user authentication exists. For details about how to add an asset, see [Adding an Asset](../adding-an-asset-arkts/document.md). Otherwise, the **NOT\_FOUND** error (24000002) is reported.

Query asset **demo\_alias** with user authentication. For details about **@ohos.userIAM.userAuth** used in the example, see [start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-useriam-userauth#start10) in the userAuth documentation.

import { asset } from '@kit.AssetStoreKit';
import { util } from '@kit.ArkTS';
import { userAuth } from '@kit.UserAuthenticationKit';
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

export async function userAuthenticate(challenge: Uint8Array): Promise<Uint8Array> {
  return new Promise((resolve, reject) => {
    const authParam: userAuth.AuthParam = {
      challenge: challenge,
      authType: \[userAuth.UserAuthType.PIN\],
      authTrustLevel: userAuth.AuthTrustLevel.ATL1,
    };
    const widgetParam: userAuth.WidgetParam = { title:' Enter the lock screen password. '};
    try {
      let userAuthInstance = userAuth.getUserAuthInstance(authParam, widgetParam);
      userAuthInstance.on('result', {
        onResult(result) {
          if (result.result == userAuth.UserAuthResultCode.SUCCESS) {
            console.info(\`User identity authentication succeeded.\`);
            resolve(result.token);
          } else {
            console.error(\`User identity authentication failed.\`);
            reject();
          }
        }
      });
      userAuthInstance.start();
    } catch (error) {
      let err = error as BusinessError;
      console.error(\`User identity authentication failed. Code is ${err.code}, message is ${err.message}\`);
      reject();
    }
  })
}

function preQueryAsset(): Promise<Uint8Array> {
  return new Promise((resolve, reject) => {
    try {
      let query: asset.AssetMap = new Map();
      query.set(asset.Tag.ALIAS, stringToArray('user\_auth\_asset'));
      asset.preQuery(query).then((challenge: Uint8Array) => {
        resolve(challenge);
      }).catch(() => {
        reject();
      })
    } catch (error) {
      let err = error as BusinessError;
      console.error(\`Failed to pre-query Asset. Code is ${err.code}, message is ${err.message}\`);
      reject();
    }
  });
}

async function postQueryAsset(challenge: Uint8Array) {
  let handle: asset.AssetMap = new Map();
  handle.set(asset.Tag.AUTH\_CHALLENGE, challenge);
  try {
    await asset.postQuery(handle);
    console.info(\`Succeeded in post-querying Asset.\`);
  } catch (error) {
    let err = error as BusinessError;
    console.error(\`Failed to post-query Asset. Code is ${err.code}, message is ${err.message}\`);
  }
}

export async function queryUserAuthAsset(): Promise<string> {
  let result: string = '';
  // Step 1. Call asset.preQuery to obtain the challenge value.
  await preQueryAsset().then(async (challenge: Uint8Array) => {
    try {
      // Step 2. Pass in the challenge value to start the user authentication dialog box.
      let authToken: Uint8Array = await userAuthenticate(challenge);
      // Step 3. After the user authentication is successful, pass in the challenge value and authorization token to query the plaintext of the asset.
      let query: asset.AssetMap = new Map();
      query.set(asset.Tag.ALIAS, stringToArray('user\_auth\_asset'));
      query.set(asset.Tag.RETURN\_TYPE, asset.ReturnType.ALL);
      query.set(asset.Tag.AUTH\_CHALLENGE, challenge);
      query.set(asset.Tag.AUTH\_TOKEN, authToken);
      let res: asset.AssetMap\[\] = await asset.query(query);
      for (let i = 0; i < res.length; i++) {
        // Parse the secret.
        let secret: Uint8Array = res\[i\].get(asset.Tag.SECRET) as Uint8Array;
        // Convert Uint8Array into the string type.
        let secretStr: string = arrayToString(secret);
      }
      // Step 4. After the plaintext is obtained, call asset.postQuery to perform postprocessing.
      postQueryAsset(challenge);
      result = 'Succeeded in querying user-auth Asset';
    } catch (error) {
      // Step 5. If the operation after preQuery() fails, call asset.postQuery to perform postprocessing.
      postQueryAsset(challenge);
      result = 'Failed to query user-auth Asset';
    }
  }).catch((err: BusinessError) => {
    console.error(\`Failed to pre-query Asset. Code is ${err.code}, message is ${err.message}\`);
    result = 'Failed to query user-auth Asset';
  })
  return result;
}
