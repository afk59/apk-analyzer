# Rdb\_TableDetails

typedef struct Rdb\_TableDetails {...} Rdb\_TableDetails

#### Overview

Defines a struct for statistics of device-cloud upload and download tasks of a database table.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| const char\* table | Database table name. |
| [Rdb\_Statistic](../rdb-statistic/document.md) upload | Statistics of the device-cloud upload tasks. |
| [Rdb\_Statistic](../rdb-statistic/document.md) download | Statistics of the device-cloud download tasks. |
