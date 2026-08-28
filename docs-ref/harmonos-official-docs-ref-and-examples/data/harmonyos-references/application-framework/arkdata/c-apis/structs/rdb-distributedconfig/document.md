# Rdb\_DistributedConfig

typedef struct Rdb\_DistributedConfig {...} Rdb\_DistributedConfig

#### Overview

Defines a struct for distributed configuration of a table.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int version | Version of the **Rdb\_DistributedConfig** struct. |
| bool isAutoSync | Whether the table supports automatic device-cloud synchronization. If the value is **true**, the system automatically triggers device-cloud synchronization. If the value is **false**, the system does not automatically trigger device-cloud synchronization. In this case, you need to call [OH\_Rdb\_CloudSync](../../header-files/relational-store-h/document.md#oh_rdb_cloudsync) to trigger device-cloud synchronization. |
