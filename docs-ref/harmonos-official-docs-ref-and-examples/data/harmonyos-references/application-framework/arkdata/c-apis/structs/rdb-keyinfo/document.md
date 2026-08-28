# Rdb\_KeyInfo

typedef struct {...} Rdb\_KeyInfo

#### Overview

Defines a struct for the primary key or number of the row that changes.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int count | Number of the changed primary keys or row numbers. |
| int type | Type of the primary key. For details, see [OH\_ColumnType](../../header-files/oh-data-value-h/document.md#oh_columntype). |
| [Rdb\_KeyData](../rdb-keydata/document.md)\* data | Pointer to the changed data. |
