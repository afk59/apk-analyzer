# Update an Asset (C/C++)

#### Available APIs

You can use [OH\_Asset\_Update](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-api-h#oh_asset_update) to update an asset.

The following table describes the attributes for updating an asset.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e8/v3/xtRFwNOoTWyupxRh5YyVtw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062000Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ABB16DD15D1287D8D2F05EB3D904BEFEC17BD135910325E5ACD82BB68809D3EC)

In the following table, the attributes **ASSET\_TAG\_ALIAS** and those starting with **ASSET\_TAG\_DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

-   Attributes in **query**:
    
    | Attribute Name (Asset\_Tag) | Attribute Content (Asset\_Value) | Mandatory | Description |
    | :-- | :-- | :-- | :-- |
    | ASSET\_TAG\_ALIAS | 
    Type: uint8\[\]
    
    Length: 1-256 bytes
    
     | Yes | Asset alias, which uniquely identifies an asset. |
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
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_2 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service with integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_3 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service with integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_CRITICAL\_4 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service with integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service without integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service without integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service without integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service without integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
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
    | ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | Type: bool | No | Whether to update the encrypted data of service customized supplementary information. The value **true** means to update the encrypted data of service customized supplementary information; the value **false** means to update the non-encrypted data of service customized supplementary information. Default value: **false**. |
    | ASSET\_TAG\_GROUP\_ID18+ | 
    
    Type: Uint8\[\]
    
    Length: 7-127 bytes
    
     | No | Group to which the asset to be updated belongs. By default, this parameter is not specified. |
    
-   Attributes in **attributesToUpdate**:
    
    | Attribute Name (Asset\_Tag) | Attribute Content (Asset\_Value) | Mandatory | Description |
    | :-- | :-- | :-- | :-- |
    | ASSET\_TAG\_SECRET | 
    Type: uint8\[\]
    
    Length: 1-1024 bytes
    
     | No | New asset in plaintext. |
    | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service without integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_2 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service without integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_3 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service without integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
     |
    | ASSET\_TAG\_DATA\_LABEL\_NORMAL\_4 | 
    
    Type: uint8\[\]
    
    Length: 1-2048 bytes
    
     | No | 
    
    Asset attribute information customized by the service without integrity protection.
    
    **NOTE**: The data length is 1 to 512 bytes before API version 12.
    
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
    

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/mfC9nT2xTTWFTgbJ6SCJPQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062000Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=11FE9057D9186AB583D2FD1FAF9978D0B931CE2668B33F46117CBE30A46996D4)

Before updating an asset, ensure that the asset exists. For details about how to add an asset, see [Adding an Asset](../adding-an-asset-c-c/document.md). Otherwise, the **NOT\_FOUND** error (24000002) is reported.

Update asset **demo\_alias** as follows: change the asset plaintext to **demo\_pwd\_new** and additional attribute to **demo\_label\_new**.

For details about how to update an asset in a group, see [Updating an asset in a Group](../managing-assets-in-a-group-c-c/document.md#updating-an-asset-in-a-group).

1.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libasset\_ndk.z.so)
    
2.  Include header files.
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  Update an asset.
    
    static napi\_value UpdateAsset(napi\_env env, napi\_callback\_info info)
    {
        const char \*aliasStr = "demo\_alias";
        const char \*secretStr = "demo\_pwd\_new";
        const char \*labelStr = "demo\_label\_new";
    
        Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
        Asset\_Blob new\_secret = {(uint32\_t)(strlen(secretStr)), (uint8\_t \*)secretStr};
        Asset\_Blob new\_label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
        Asset\_Attr query\[\] = {{.tag = ASSET\_TAG\_ALIAS, .value.blob = alias }};
        Asset\_Attr attributesToUpdate\[\] = {
            {.tag = ASSET\_TAG\_SECRET, .value.blob = new\_secret},
            {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = new\_label},
        };
    
        int32\_t updateResult = OH\_Asset\_Update(query, sizeof(query) / sizeof(query\[0\]), attributesToUpdate,
                                               sizeof(attributesToUpdate) / sizeof(attributesToUpdate\[0\]));
        napi\_value ret;
        napi\_create\_int32(env, updateResult, &ret);
        return ret;
    }
