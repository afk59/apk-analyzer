# oh\_rdb\_types.h

#### Overview

Defines types related to data values.

**File to include**: <database/rdb/oh\_rdb\_types.h>

**Library**: libnative\_rdb\_ndk.z.so

**System capability**: SystemCapability.DistributedDataManager.RelationalStore.Core

**Since**: 18

**Related module**: [RDB](../../modules/rdb/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Rdb\_ConflictResolution](#rdb_conflictresolution) | Rdb\_ConflictResolution | Enumerates the conflict resolution policies. |

#### Enum Description

#### \[h2\]Rdb\_ConflictResolution

enum Rdb\_ConflictResolution

**Description**

Enumerates the conflict resolution policies.

**Since**: 18

| Enum Item | Description |
| :-- | :-- |
| RDB\_CONFLICT\_NONE = 1 | No operation is performed when a conflict occurs. |
| RDB\_CONFLICT\_ROLLBACK | Throws an error and rolls back the transaction. |
| RDB\_CONFLICT\_ABORT | Throws an error and rolls back the current change. |
| RDB\_CONFLICT\_FAIL | Throws an error and aborts the current change without rolling back the modifications before the conflict. |
| RDB\_CONFLICT\_IGNORE | Ignores the conflicted data and resolves the conflict later. |
| RDB\_CONFLICT\_REPLACE | Deletes the data and then inserts the data. If the conflict persists, applies **RDB\_CONFLICT\_ABORT**. |
