# Syncing Assets (Backup and Restore) (C/C++)

#### Adding Dependencies

Link the dynamic libraries in the CMake script.

target\_link\_libraries(entry PUBLIC libasset\_ndk.z.so)

Include header files.

#include "napi/native\_api.h"
#include <string.h>
#include "asset/asset\_api.h"

#### Adding Assets That Support Sync

Add an asset with the password **demo\_pwd**, alias **demo\_alias**, and additional information **demo\_label**.

static napi\_value AddSyncAsset(napi\_env env, napi\_callback\_info info)
{
    char \*secretStr = "demo\_pwd";
    char \*aliasStr = "demo\_alias";
    char \*labelStr = "demo\_label";

    Asset\_Blob secret = {(uint32\_t)(strlen(secretStr)), (uint8\_t \*)secretStr};
    Asset\_Blob alias = {(uint32\_t)(strlen(aliasStr)), (uint8\_t \*)aliasStr};
    Asset\_Blob label = {(uint32\_t)(strlen(labelStr)), (uint8\_t \*)labelStr};
    Asset\_Attr attr\[\] = {
        {.tag = ASSET\_TAG\_SECRET, .value.blob = secret},
        {.tag = ASSET\_TAG\_ALIAS, .value.blob = alias},
        {.tag = ASSET\_TAG\_DATA\_LABEL\_NORMAL\_1, .value.blob = label},
        {.tag = ASSET\_TAG\_SYNC\_TYPE, .value.u32 = ASSET\_SYNC\_TYPE\_TRUSTED\_DEVICE}, // You need to specify the sync type between trusted devices (for example, clone between old and new devices).
    };

    int32\_t addResult = OH\_Asset\_Add(attr, sizeof(attr) / sizeof(attr\[0\]));
    napi\_value ret;
    napi\_create\_int32(env, addResult, &ret);
    return ret;
}

#### Accessing the Backup and Restore Extension Capability

To trigger the backup and restore of application data, see [Accessing Backup and Restore](../../../../../application-framework/core-file-kit/application-files/application-data-backup-and-restore/accessing-backup-and-restore/document.md).

#### Querying the Sync Result of Assets

## Available APIs

You can call **OH\_Asset\_QuerySyncResult** to query the sync result of assets. For more information, see the API reference.

The following table describes the attributes for querying an asset.

| Attribute Name (Asset\_Tag) | Attribute Content (Asset\_Value) | Mandatory or Not | Description |
| :-- | :-- | :-- | :-- |
| ASSET\_TAG\_REQUIRE\_ATTR\_ENCRYPTED14+ | Type: bool | Yes | Whether to query the sync result of the asset whose custom additional information is encrypted. The value **true** means to query the sync result; the value **false** means the opposite. The default value is **false**. |
| ASSET\_TAG\_GROUP\_ID18+ | 
Type: Uint8\[\]

Length: 7-127 bytes

 | Yes | Group to which the asset to be queried belongs. By default, this parameter is not specified. |

## Sample Code

static napi\_value QuerySyncResult(napi\_env env, napi\_callback\_info info)
{
    Asset\_SyncResult syncResult = {0};
    int32\_t queryResult = OH\_Asset\_QuerySyncResult(NULL, 0, &syncResult);
    napi\_value ret;
    napi\_create\_int32(env, queryResult, &ret);
    return ret;
}

#### Notes and Constraints

For a successful sync between trusted devices, the assets of both old and new devices must be accessible. Otherwise, the sync might fail.

-   For assets that are accessible only when a password is set, the sync will fail if no lock screen password is set on either the old or new device.
    
-   For assets that are accessible only when the screen is unlocked, the sync will fail if the screen of either the old or new device is locked.
    
-   For assets that are accessible only after user authentication, the sync will fail if no lock screen password is set on the old device.
