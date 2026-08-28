# Rdb\_Statistic

typedef struct Rdb\_Statistic {...} Rdb\_Statistic

#### Overview

Defines a struct for the device-cloud sync statistics of a database table.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int total | Total number of rows to be synced between the device and cloud in the database table. |
| int successful | Number of rows that are successfully synced between the device and cloud in the database table. |
| int failed | Number of rows that failed to be synced between the device and cloud in the database table. |
| int remained | Number of rows that are not executed for device-cloud sync in the database table. |
