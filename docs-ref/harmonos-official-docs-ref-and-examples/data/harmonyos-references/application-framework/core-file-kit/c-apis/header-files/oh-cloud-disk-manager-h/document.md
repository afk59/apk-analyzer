# oh\_cloud\_disk\_manager.h

#### Overview

This file defines the APIs for the cloud disk management module.

**File to include**: <filemanagement/clouddiskmanager/oh\_cloud\_disk\_manager.h>

**Library**: libohclouddiskmanager.so

**System capability**: SystemCapability.FileManagement.CloudDiskManager

**Since**: 21

**Related module**: [CloudDisk](../../modules/clouddisk/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md) | CloudDisk\_PathInfo/CloudDisk\_FileIdInfo/CloudDisk\_SyncFolderPath | 
**CloudDisk\_PathInfo**: a struct that encapsulates the file path information.

**CloudDisk\_FileIdInfo**: a struct that encapsulates the file ID.

**CloudDisk\_SyncFolderPath**: a struct that encapsulates the sync root path.

 |
| [CloudDisk\_FileSyncState](../../structs/clouddisk-filesyncstate/document.md) | CloudDisk\_FileSyncState | A struct that encapsulates the file sync state. |
| [CloudDisk\_ChangeData](../../structs/clouddisk-changedata/document.md) | CloudDisk\_ChangeData | A struct that encapsulates the event data generated when a single file under the sync root path is changed. It includes the file's unique ID, the parent directory's unique ID, relative path, change type, file size, and timestamp. |
| [CloudDisk\_ChangesResult](../../structs/clouddisk-changesresult/document.md) | CloudDisk\_ChangesResult | A struct that encapsulates the file change result under the sync root path. It includes the next change sequence number, end flag, and an array of change data items. |
| [CloudDisk\_FailedList](../../structs/clouddisk-failedlist/document.md) | CloudDisk\_FailedList | A struct that encapsulates the list of files that failed to synchronize. It includes the file path information and the specific error cause. |
| [CloudDisk\_ResultList](../../structs/clouddisk-resultlist/document.md) | CloudDisk\_ResultList | A struct that encapsulates the file sync result. It includes the absolute path of the file, sync result, and sync state or failure cause. |
| [CloudDisk\_DisplayNameInfo](../../structs/clouddisk-displaynameinfo/document.md) | CloudDisk\_DisplayNameInfo | A struct that encapsulates the display name of the sync root path. |
| [CloudDisk\_SyncFolder](../../structs/clouddisk-syncfolder/document.md) | CloudDisk\_SyncFolder | A struct that encapsulates the sync root property information. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [CloudDisk\_SyncState](#clouddisk_syncstate) | CloudDisk\_SyncState | Enumerates the file sync states. |
| [CloudDisk\_OperationType](#clouddisk_operationtype) | CloudDisk\_OperationType | Enumerates the file change types. |
| [CloudDisk\_ErrorReason](#clouddisk_errorreason) | CloudDisk\_ErrorReason | Enumerates the file sync failure causes. |
| [CloudDisk\_SyncFolderState](#clouddisk_syncfolderstate) | CloudDisk\_SyncFolderState | Enumerates the sync root path states. |

#### \[h2\]Function

| Name | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath, void (\*callback)(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_ChangeData changeDatas\[\], size\_t bufferLength))](#oh_clouddisk_registersyncfolderchanges) | Registers a callback to obtain file changes in the sync root path. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath)](#oh_clouddisk_unregistersyncfolderchanges) | Unregisters the callback for file changes in the sync root path. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath, uint64\_t startUsn, size\_t count, CloudDisk\_ChangesResult \*\*changesResult)](#oh_clouddisk_getsyncfolderchanges) | Obtains the change history in the sync root path. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_SetFileSyncStates(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_FileSyncState fileSyncStates\[\], size\_t bufferLength, CloudDisk\_FailedList \*\*failedLists, size\_t \*failedCount)](#oh_clouddisk_setfilesyncstates) | Sets the file sync state in the sync root path. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetFileSyncStates(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo paths\[\], size\_t bufferLength, CloudDisk\_ResultList \*\*resultLists, size\_t \*resultCount)](#oh_clouddisk_getfilesyncstates) | Obtains the file sync state in the sync root path. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolder(const CloudDisk\_SyncFolder \*syncFolder)](#oh_clouddisk_registersyncfolder) | Registers a sync root. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](#oh_clouddisk_unregistersyncfolder) | Unregisters the sync root. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_ActiveSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](#oh_clouddisk_activesyncfolder) | Activates the sync root. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_DeactiveSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)](#oh_clouddisk_deactivesyncfolder) | Deactivates the sync root. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFolders(CloudDisk\_SyncFolder \*\*syncFolders, size\_t \*count)](#oh_clouddisk_getsyncfolders) | Obtains all sync roots. |
| [CloudDisk\_ErrorCode OH\_CloudDisk\_UpdateCustomAlias(const CloudDisk\_SyncFolderPath syncFolderPath, const char \*customAlias, size\_t customAliasLength)](#oh_clouddisk_updatecustomalias) | Updates the sync root alias. |

#### Enum Description

#### \[h2\]CloudDisk\_SyncState

enum CloudDisk\_SyncState

**Description**

Enumerates the file sync states.

**Since**: 21

| Value | Description |
| :-- | :-- |
| IDLE = 0 | The file is idle, and no sync operation is performed. |
| SYNCING = 1 | The file is being synced. |
| SYNC\_SUCCEEDED = 2 | The file is synced successfully. |
| SYNC\_FAILED = 3 | The file fails to be synced. |
| SYNC\_CANCELED = 4 | The file sync is canceled. |
| SYNC\_CONFLICTED = 5 | The file sync conflicts. |

#### \[h2\]CloudDisk\_OperationType

enum CloudDisk\_OperationType

**Description**

Enumerates the file change types.

**Since**: 21

| Value | Description |
| :-- | :-- |
| CREATE = 0 | Create a file or directory. |
| DELETE = 1 | Delete a file or directory. |
| MOVE\_FROM = 2 | Move this file or directory. |
| MOVE\_TO = 3 | Move to this file or directory. |
| CLOSE\_WRITE = 4 | Close the file after the write operation. |
| SYNC\_FOLDER\_INVALID = 5 | Invalid sync root path. |

#### \[h2\]CloudDisk\_ErrorReason

enum CloudDisk\_ErrorReason

**Description**

Enumerates the file sync failure causes.

**Since**: 21

| Value | Description |
| :-- | :-- |
| INVALID\_ARGUMENT = 0 | The input parameter is invalid. |
| NO\_SUCH\_FILE = 1 | The file or directory does not exist. |
| NO\_SPACE\_LEFT = 2 | The remaining space on the device is insufficient. |
| OUT\_OF\_RANGE = 3 | The file is not in the sync root path. |
| NO\_SYNC\_STATE = 4 | The sync state is not set. |

#### \[h2\]CloudDisk\_SyncFolderState

enum CloudDisk\_SyncFolderState

**Description**

Enumerates the sync root path states.

**Since**: 21

| Value | Description |
| :-- | :-- |
| INACTIVE = 0 | The sync root path is inactive. |
| ACTIVE = 1 | The sync root path is active. |

#### Function Description

#### \[h2\]OH\_CloudDisk\_RegisterSyncFolderChanges()

CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath, void (\*callback)(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_ChangeData changeDatas\[\], size\_t bufferLength))

**Description**

Registers a callback to obtain file changes in the sync root path.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |
| callback | Registered callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_UnregisterSyncFolderChanges()

CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath)

**Description**

Unregisters the callback for file changes in the sync root path.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_GetSyncFolderChanges()

CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFolderChanges(const CloudDisk\_SyncFolderPath syncFolderPath, uint64\_t startUsn, size\_t count, CloudDisk\_ChangesResult \*\*changesResult)

**Description**

Obtains the change history in the sync root path.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |
| uint64\_t startUsn | Start change sequence number. The value range is \[0, 2^64 – 1\]. |
| size\_t count | Number of file changes. The value range is \[1, 100\]. |
| [CloudDisk\_ChangesResult](../../structs/clouddisk-changesresult/document.md) \*\*changesResult | File change result. For details, see [CloudDisk\_ChangesResult](../../structs/clouddisk-changesresult/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_SetFileSyncStates()

CloudDisk\_ErrorCode OH\_CloudDisk\_SetFileSyncStates(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_FileSyncState fileSyncStates\[\], size\_t bufferLength, CloudDisk\_FailedList \*\*failedLists, size\_t \*failedCount)

**Description**

Sets the file sync state in the sync root path.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |
| [const CloudDisk\_FileSyncState](../../structs/clouddisk-filesyncstate/document.md) fileSyncStates\[\] | [CloudDisk\_FileSyncState](../../structs/clouddisk-filesyncstate/document.md) array of the file path and its target sync state. |
| size\_t bufferLength | Length of the sync state array to be set. The value range is \[1, 100\]. |
| [CloudDisk\_FailedList](../../structs/clouddisk-failedlist/document.md) \*\*failedLists | Double pointer to the [CloudDisk\_FailedList](../../structs/clouddisk-failedlist/document.md) array that contains files whose sync states failed to be set. |
| size\_t \*failedCount | Pointer to the length of the file list array whose sync states failed to be set. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_GetFileSyncStates()

CloudDisk\_ErrorCode OH\_CloudDisk\_GetFileSyncStates(const CloudDisk\_SyncFolderPath syncFolderPath, const CloudDisk\_PathInfo paths\[\], size\_t bufferLength, CloudDisk\_ResultList \*\*resultLists, size\_t \*resultCount)

**Description**

Obtains the file sync state in the sync root path.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |
| [const CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md) paths\[\] | [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md) array of the sync state. |
| size\_t bufferLength | Length of the sync state array. The value range is \[1, 100\]. |
| [CloudDisk\_ResultList](../../structs/clouddisk-resultlist/document.md) \*\*resultLists | Double pointer to the file sync result. For details, see [CloudDisk\_ResultList](../../structs/clouddisk-resultlist/document.md). |
| size\_t \*resultCount | Pointer to the number of files that fail to be synchronized. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_RegisterSyncFolder()

CloudDisk\_ErrorCode OH\_CloudDisk\_RegisterSyncFolder(const CloudDisk\_SyncFolder \*syncFolder)

**Description**

Registers a sync root.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [const CloudDisk\_SyncFolder](../../structs/clouddisk-syncfolder/document.md) \*syncFolder | Sync root path to be registered. For details, see [CloudDisk\_SyncFolder](../../structs/clouddisk-syncfolder/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_UnregisterSyncFolder()

CloudDisk\_ErrorCode OH\_CloudDisk\_UnregisterSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)

**Description**

Unregisters the sync root.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_ActiveSyncFolder()

CloudDisk\_ErrorCode OH\_CloudDisk\_ActiveSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)

**Description**

Activates the sync root.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_DeactiveSyncFolder()

CloudDisk\_ErrorCode OH\_CloudDisk\_DeactiveSyncFolder(const CloudDisk\_SyncFolderPath syncFolderPath)

**Description**

Deactivates the sync root.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_GetSyncFolders()

CloudDisk\_ErrorCode OH\_CloudDisk\_GetSyncFolders(CloudDisk\_SyncFolder \*\*syncFolders, size\_t \*count)

**Description**

Obtains all sync roots.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| [CloudDisk\_SyncFolder](../../structs/clouddisk-syncfolder/document.md) \*\*syncFolders | Double pointer to the sync root path array [CloudDisk\_SyncFolder](../../structs/clouddisk-syncfolder/document.md). |
| size\_t \*count | Pointer to the number of sync roots registered by the current cloud disk. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |

#### \[h2\]OH\_CloudDisk\_UpdateCustomAlias()

CloudDisk\_ErrorCode OH\_CloudDisk\_UpdateCustomAlias(const CloudDisk\_SyncFolderPath syncFolderPath, const char \*customAlias, size\_t customAliasLength)

**Description**

Updates the sync root alias.

**Since**: 21

**Parameters**

| Name | Description |
| :-- | :-- |
| const CloudDisk\_SyncFolderPath syncFolderPath | Sync root path. For details, see [CloudDisk\_PathInfo](../../structs/clouddisk-pathinfo/document.md). |
| const char \*customAlias | Pointer to the custom alias, which cannot contain the following characters: \\/\*?<>|:". Additionally, the full name cannot be composed solely of spaces, a single dot (.), or two consecutive dots (..). |
| size\_t customAliasLength | Length of the custom alias. Value range: \[0, 255\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) | Returns [CLOUD\_DISK\_OK](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) if the API is called successfully; returns [CloudDisk\_ErrorCode](../cloud-disk-error-code-h/document.md#clouddisk_errorcode) otherwise. |
