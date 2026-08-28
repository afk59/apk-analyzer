# Querying Assets (C/C++)

#### Available APIs

You can use [OH\_Asset\_Query](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-api-h#oh_asset_query) to query an asset.

The following table describes the attributes for querying an asset.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e6/v3/xFidkda5T1ODDb28j9H4Hg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062000Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E5917B634151D45566C082C8C050F818EFF0EA8061B0B59FCE4E23DCCC66EE48)

In the following table, the attributes **ASSET\_TAG\_ALIAS** and those starting with **ASSET\_TAG\_DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

It takes a long time to query the plaintext of the asset attribute **ASSET\_TAG\_SECRET** due to the need of decryption. Therefore, **Asset\_ReturnType** must be set to **ASSET\_RETURN\_ALL**. For other asset attributes, decryption is not required, so the query takes a short time. Therefore, **Asset\_ReturnType** must be set to **ASSET\_RETURN\_ATTRIBUTES**.

| Attribute Name (Asset\_Tag) | Attribute Content (Asset\_Value) | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ASSET\_TAG\_ALIAS | 
Type: uint8\[\]

Length: 1-256 bytes

 | No | Asset alias, which uniquely identifies an asset. |
| ASSET\_TAG\_ACCESSIBILITY | 

Type: uint32\_t

Value range: see [Asset\_Accessibility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_accessibility).

 | No | Access control based on the lock screen status. |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | Type: bool | No | Whether the asset is accessible only when a lock screen password is set. The value **true** means the asset is accessible only when a lock screen password is set. The value **false** means that the asset can be accessed regardless of whether a lock screen password is set. |
| ASSET\_TAG\_AUTH\_TYPE | 

Type: uint32\_t

Value range: see [Asset\_AuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_authtype).

 | No | Type of user authentication required for accessing the asset. |
| ASSET\_TAG\_SYNC\_TYPE | 

Type: uint32\_t

Value range: see [Asset\_SyncType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_synctype).

 | No | Type of sync supported by the asset. |
| ASSET\_TAG\_IS\_PERSISTENT | Type: bool | No | Whether to retain the asset when the application is uninstalled. The value **true** means to retain the asset even after the application is uninstalled. The value **false** means the opposite. |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_1 | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_2 | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_3 | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_4 | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service with integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | 

Asset attribute information customized by the service without integrity protection.

**Note**: The data length is 1 to 512 bytes before API version 12.

 |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_112+ | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | Local attribute information about the asset. The value is assigned by the service without integrity protection and will not be synced. |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_212+ | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | Local attribute information about the asset. The value is assigned by the service without integrity protection and will not be synced. |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_312+ | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | Local attribute information about the asset. The value is assigned by the service without integrity protection and will not be synced. |
| ASSET\_TAG\_DATA\_LABEL\_NORMAL\_LOCAL\_412+ | 

Type: uint8\[\]

Length: 1-2048 bytes

 | No | Local attribute information about the asset. The value is assigned by the service without integrity protection and will not be synced. |
| ASSET\_TAG\_RETURN\_TYPE | 

Type: uint32\_t

Value range: see [Asset\_ReturnType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_returntype).

 | No | Type of the asset query result to return. |
| ASSET\_TAG\_RETURN\_LIMIT | Type: uint32\_t | No | Maximum number of asset records returned. |
| ASSET\_TAG\_RETURN\_OFFSET | 

Type: uint32\_t

Value range: 1-65536

 | No | 

Offset of the asset query result.

**Note**: This parameter specifies the starting asset record to return in batch asset query.

 |
| ASSET\_TAG\_RETURN\_ORDERED\_BY | 

Type: uint32\_t

Value: ASSET\_TAG\_DATA\_LABEL\_xxx

 | No | 

How the query results are sorted. Currently, the results can be sorted only by **ASSET\_TAG\_DATA\_LABEL**.

**Note**: By default, assets are returned in the order in which they are added.

 |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | Type: bool | No | Whether to query the encrypted data of service customized supplementary information. The value **true** means to query the encrypted data of service customized supplementary information; the value **false** means to query the non-encrypted data of service customized supplementary information. Default value: **false**. |
| ASSET\_TAG\_GROUP\_ID18+ | 

Type: Uint8\[\]

Length: 7-127 bytes

 | No | Group to which the asset to be queried belongs. By default, this parameter is not specified. |

#### Constraints

The assets queried are transmitted to the service through an IPC channel. Due to the limitation of the IPC buffer size, the maximum number of assets to be queried at a time cannot exceed 40.

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/63/v3/9jx6g5pHRTm2U_LNlkKo9Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062000Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=56924A885ADF399598219FFC94A444A55F5FDD812FDCA52070DF9E10DE9450E5)

Before querying an asset, ensure that the asset exists. For details about how to add an asset, see [Adding an Asset](../adding-an-asset-c-c/document.md). Otherwise, the **NOT\_FOUND** error (24000002) is reported.

## Querying the Plaintext of an Asset

Query the plaintext of asset **demo\_alias**.

For details about how to query the plaintext of an asset in a group, see [Querying the Plaintext of an Asset in a Group](../managing-assets-in-a-group-c-c/document.md#querying-the-plaintext-of-an-asset-in-a-group).

1.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libasset\_ndk.z.so)
    
2.  Include header files.
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  Query an asset.
    
    static napi\_value QueryAssetPlaintext(napi\_env env, napi\_callback\_info info)
    {
        const char \*aliasStr = "demo\_alias";
        
        Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // Specify the alias of the asset to query.
            {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ALL}, // Return all asset information, including the attributes and asset plaintext. The plaintext needs to be decrypted, so the query takes a long time.
        };
    
        Asset\_ResultSet resultSet = {0};
        int32\_t queryResult = OH\_Asset\_Query(attr, sizeof(attr) / sizeof(attr\[0\]), &resultSet);
        if (queryResult == ASSET\_SUCCESS) {
            // Parse resultSet.
            for (uint32\_t i = 0; i < resultSet.count; i++) {
                // Parse the secret attribute. The data corresponds to secret->blob.data, and the size corresponds to secret->blob.size.
                Asset\_Attr \*secret = OH\_Asset\_ParseAttr(resultSet.results + i, ASSET\_TAG\_SECRET);
            }
        }
        OH\_Asset\_FreeResultSet(&resultSet);
     
        napi\_value ret;
        napi\_create\_int32(env, queryResult, &ret);
        return ret;
    }
    

## Querying Attributes of an Asset

Query attributes of asset **demo\_alias**.

For details about how to query the attributes of an asset in a group, see [Querying the Attributes of an Asset in a Group](../managing-assets-in-a-group-c-c/document.md#querying-the-attributes-of-an-asset-in-a-group).

1.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libasset\_ndk.z.so)
    
2.  Include header files.
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  Query an asset.
    
    static napi\_value QueryAssetAttribute(napi\_env env, napi\_callback\_info info)
    {
        const char \*aliasStr = "demo\_alias";
        
        Asset\_Blob alias = { (uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr };
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // Specify the alias of the asset to query.
            {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ATTRIBUTES}, // Return only the asset attributes. The attributes do not need to be decrypted, so the query takes a short time.
        };
    
        Asset\_ResultSet resultSet = {0};
        int32\_t queryResult = OH\_Asset\_Query(attr, sizeof(attr) / sizeof(attr\[0\]), &resultSet);
        if (queryResult == ASSET\_SUCCESS) {
            // Parse the result
            for (uint32\_t i = 0; i < resultSet.count; i++) {
                // Parse the data label. The data corresponds to label->blob.data, and the size corresponds to label->blob.size.
                Asset\_Attr \*label = OH\_Asset\_ParseAttr(resultSet.results + i, ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1);
            }
        }
        OH\_Asset\_FreeResultSet(&resultSet);
     
        napi\_value ret;
        napi\_create\_int32(env, queryResult, &ret);
        return ret;
    }
    

## Querying Attributes of Assets

Query attributes of assets with the tag of **demo\_label** and return a total of 10 records sorted by **DATA\_LABEL\_NORMAL\_1** starting from the fifth record that matches the search criteria.

1.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libasset\_ndk.z.so)
    
2.  Include header files.
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  Query an asset.
    
    static napi\_value QueryBatchAssetAttributes(napi\_env env, napi\_callback\_info info)
    {
        const char \*labelStr = "demo\_label";
        
        Asset\_Blob label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_RETURN\_TYPE, .value.u32 = ASSET\_RETURN\_ATTRIBUTES},
            {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = label},
            {.tag = ASSET\_TAG\_RETURN\_LIMIT, .value.u32 = 10},
            {.tag = ASSET\_TAG\_RETURN\_ORDERED\_BY, .value.u32 = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1},
        };
    
        Asset\_ResultSet resultSet = { 0 };
        int32\_t queryResult = OH\_Asset\_Query(attr, sizeof(attr) / sizeof(attr\[0\]), &resultSet);
        if (queryResult == ASSET\_SUCCESS) {
            // Parse the result
            for (uint32\_t i = 0; i < resultSet.count; i++) {
                // Parse the data alias. The alias corresponds to label->blob.data, and the size corresponds to label->blob.size.
                Asset\_Attr \*alias = OH\_Asset\_ParseAttr(resultSet.results + i, ASSET\_TAG\_ALIAS);
            }
        }
        OH\_Asset\_FreeResultSet(&resultSet);
     
        napi\_value ret;
        napi\_create\_int32(env, queryResult, &ret);
        return ret;
    }
