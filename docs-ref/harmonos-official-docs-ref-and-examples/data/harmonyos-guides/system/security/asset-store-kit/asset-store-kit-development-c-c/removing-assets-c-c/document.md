# Removing Assets (C/C++)

#### Available APIs

You can use [OH\_Asset\_Remove](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-api-h#oh_asset_remove) to remove an asset.

The following table describes the asset attributes.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b5/v3/LId3cNUlSvWC7owZELjgxQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062000Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B38E3C64759BAC8B25B7798F2AB24B1E5F212AF89CB468CF758D1C7349FD2D9)

In the following table, the attributes **ASSET\_TAG\_ALIAS** and those starting with **ASSET\_TAG\_DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

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
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | Type: bool | No | Whether to remove the encrypted data of service customized supplementary information. The value **true** means to remove the encrypted data of service customized supplementary information; the value **false** means to remove the non-encrypted data of service customized supplementary information. Default value: **false**. |
| ASSET\_TAG\_GROUP\_ID18+ | 

Type: Uint8\[\]

Length: 7-127 bytes

 | No | Group to which the asset to be removed belongs. By default, this parameter is not specified. |

#### Example

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/6b/v3/CN7lUXuaSVaMUNi7Je9JwQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062000Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=53FF180441362869F9D023CED14CBCE4A612689DE1B60C25C71A11AB2EE75CEF)

Before removing an asset, ensure that the asset exists. For details about how to add an asset, see [Adding an Asset](../adding-an-asset-c-c/document.md). Otherwise, the **NOT\_FOUND** error (24000002) is reported.

Remove asset **demo\_alias**.

For details about how to remove an asset in a group, see [Removing an Asset from a Group](../managing-assets-in-a-group-c-c/document.md#removing-an-asset-from-a-group).

1.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libasset\_ndk.z.so)
    
2.  Include header files.
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  Remove an asset.
    
    static napi\_value RemoveAsset(napi\_env env, napi\_callback\_info info)
    {
        const char \*aliasStr = "demo\_alias";
        
        Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias}, // You can specify the asset alias to remove a single asset. To remove all assets, leave the alias unspecified.
        };
    
        int32\_t removeResult = OH\_Asset\_Remove(attr, sizeof(attr) / sizeof(attr\[0\]));
        napi\_value ret;
        napi\_create\_int32(env, removeResult, &ret);
        return ret;
    }
