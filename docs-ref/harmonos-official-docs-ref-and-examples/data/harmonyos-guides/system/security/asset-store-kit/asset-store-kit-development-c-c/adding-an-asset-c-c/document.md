# Adding an Asset (C/C++)

#### Available APIs

You can use [OH\_Asset\_Add](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-api-h#oh_asset_add) to add an asset.

The following table describes the attributes for adding an asset.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a7/v3/ahCfET7oRrmwsoRZ_R2Ggg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T061959Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=85FE4687A5E9CC15E1B6D3E4ACC6C2C4AF8746A0D799B2201FC9E8622BA80FFD)

In the following table, the attributes **ASSET\_TAG\_ALIAS** and those starting with **ASSET\_TAG\_DATA\_LABEL** are custom asset attributes reserved for services. These attributes are not encrypted. Therefore, do not put sensitive personal data in these attributes.

| Attribute Name (Asset\_Tag) | Attribute Content (Asset\_Value) | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| ASSET\_TAG\_SECRET | 
Type: uint8\[\]

Length: 1-1024 bytes

 | Yes | Asset in plaintext. |
| ASSET\_TAG\_ALIAS | 

Type: uint8\[\]

Length: 1-256 bytes

 | Yes | Asset alias, which uniquely identifies an asset. |
| ASSET\_TAG\_ACCESSIBILITY | 

Type: uint32\_t

Value range: see [Asset\_Accessibility](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_accessibility).

 | No | Access control based on whether the screen is locked. The default value is **ASSET\_ACCESSIBILITY\_DEVICE\_FIRST\_UNLOCKED**, indicating that the asset can be accessed after the device is unlocked for the first time. |
| ASSET\_TAG\_REQUIRE\_PASSWORD\_SET | Type: bool | No | Whether the asset is accessible only when a lock screen password is set. The value **true** means that the asset can be accessed only when the user sets a screen lock password. The value **false** means that the asset can be accessed regardless of whether the user sets a screen lock password. The default value is **false**. |
| ASSET\_TAG\_AUTH\_TYPE | 

Type: uint32\_t

Value range: see [Asset\_AuthType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_authtype).

 | No | User authentication type required for accessing an asset. The default value is **ASSET\_AUTH\_TYPE\_NONE**, indicating that user authentication is not required before the user accesses an asset. |
| ASSET\_TAG\_SYNC\_TYPE | 

Type: uint32\_t

Value range: see [Asset\_SyncType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_synctype).

 | No | Sync type supported by the asset. The default value is **ASSET\_SYNC\_TYPE\_NEVER**, indicating that the asset cannot be synced. |
| ASSET\_TAG\_IS\_PERSISTENT | Type: bool | No | 

Whether to retain the asset when the application is uninstalled. The value **true** means to retain the asset when the application is uninstalled; the value **false** means the opposite. Default value: **false**.

**NOTE**: If this parameter is set, the application must [apply for](../../../application-access-control/application-permission-management/requesting-application-permissions/declaring-permissions/document.md) the ohos.permission.STORE\_PERSISTENT\_DATA permission.

 |
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
| ASSET\_TAG\_CONFLICT\_RESOLUTION | 

Type: uint32\_t

Value range: see [Asset\_ConflictResolution](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_conflictresolution).

 | No | Conflict (for example, duplicate aliases) resolution when an asset is added. The default value is **ASSET\_CONFLICT\_THROW\_ERROR**, indicating that an exception is thrown for subsequent processing by the service. |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | Type: bool | No | Whether to encrypt the additional asset information customized by the service. The value **true** means to encrypt the additional asset information customized by the service; the value **false** means the opposite. Default value: **false**. |
| ASSET\_TAG\_GROUP\_ID18+ | 

Type: Uint8\[\]

Length: 7-127 bytes

 | No | Group to which the asset to be added belongs. By default, this parameter is not specified. |
| ASSET\_TAG\_WRAP\_TYPE18+ | 

Type: uint32\_t

Value range: see [Asset\_WrapType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-asset-type-h#asset_wraptype).

 | No | Encrypted import/export type supported by the asset. The default value is **ASSET\_WRAP\_TYPE\_NEVER**, indicating that encrypted import/export is not supported. |

#### Constraints

-   Alias-based access
    
    Assets are stored in the ASSET database in ciphertext. The service identity and alias are used as the unique index. The alias of each asset must be unique.
    
-   Custom service data storage
    
    -   ASSET provides 12 custom asset attributes starting with **ASSET\_TAG\_DATA\_LABEL** for services. If the 12 custom attributes are used, you can combine multiple data segments in a certain format (for example, JSON) into an ASSET attribute.
        
    -   ASSET protects the integrity of the attributes starting with **ASSET\_TAG\_DATA\_LABEL\_CRITICAL**. These attributes cannot be changed once written.
        

#### Example

Add an asset with the password **demo\_pwd**, alias **demo\_alias**, and additional attribute **demo\_label**. The asset can be accessed after the device is unlocked for the first time.

For details about how to add an asset to a group, see [Adding an Asset to a Group](../managing-assets-in-a-group-c-c/document.md#adding-an-asset-to-a-group).

1.  Link the dynamic libraries in the CMake script.
    
    target\_link\_libraries(entry PUBLIC libasset\_ndk.z.so)
    
2.  Include header files.
    
    #include "napi/native\_api.h"
    #include <string.h>
    #include "asset/asset\_api.h"
    
3.  Add an asset.
    
    static napi\_value AddAsset(napi\_env env, napi\_callback\_info info)
    {
        const char \*secretStr = "demo\_pwd";
        const char \*aliasStr = "demo\_alias";
        const char \*labelStr = "demo\_label";
    
        Asset\_Blob secret = {(uint32\_t)(strlen(secretStr)), (uint8\_t \*)secretStr};
        Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
        Asset\_Blob label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
        Asset\_Attr attr\[\] = {
            {.tag = ASSET\_TAG\_ACCESSIBILITY, .value.u32 = ASSET\_ACCESSIBILITY\_DEVICE\_FIRST\_UNLOCKED},
            {.tag = ASSET\_TAG\_SECRET, .value.blob = secret},
            {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias},
            {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = label},
        };
    
        int32\_t addResult = OH\_Asset\_Add(attr, sizeof(attr) / sizeof(attr\[0\]));
        napi\_value ret;
        napi\_create\_int32(env, addResult, &ret);
        return ret;
    }
