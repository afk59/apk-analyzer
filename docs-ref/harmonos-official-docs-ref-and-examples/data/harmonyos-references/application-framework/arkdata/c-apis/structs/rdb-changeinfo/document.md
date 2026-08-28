# Rdb\_ChangeInfo

typedef struct Rdb\_ChangeInfo {...} Rdb\_ChangeInfo

#### Overview

Defines a struct for the details about the device-cloud sync process.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int version | Version of the **Rdb\_DistributedConfig** struct. |
| const char\* tableName | Name of the table with data changes. |
| int ChangeType | Type of the data changed, which can be data or asset. |
| [Rdb\_KeyInfo](../rdb-keyinfo/document.md) inserted | Location where data is inserted. If the primary key of the table is of the string type, it is the value of the primary key. Otherwise, it is the row number of the inserted data. |
| [Rdb\_KeyInfo](../rdb-keyinfo/document.md) updated | Location where data is updated. If the primary key of the table is of the string type, it is the value of the primary key. Otherwise, it is the row number of the updated data. |
| [Rdb\_KeyInfo](../rdb-keyinfo/document.md) deleted | Location where data is deleted. If the primary key of the table is of the string type, it is the value of the primary key. Otherwise, it is the row number of the deleted data. |
