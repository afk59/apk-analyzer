# Rdb\_ProgressDetails

typedef struct Rdb\_ProgressDetails {...} Rdb\_ProgressDetails

#### Overview

Defines a struct for statistics of the overall device-cloud sync (upload and download) tasks of an RDB store.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int version | Version of the **OH\_TableDetails** struct. |
| int schedule | Device-cloud sync process. |
| int code | Device-cloud sync state. |
| int32\_t tableLength | Number of the tables synced between the device and cloud. |
