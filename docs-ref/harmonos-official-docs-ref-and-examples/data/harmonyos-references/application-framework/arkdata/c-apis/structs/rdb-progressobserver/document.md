# Rdb\_ProgressObserver

typedef struct Rdb\_ProgressObserver {...} Rdb\_ProgressObserver

#### Overview

Defines a struct for the observer for the device-cloud sync progress.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| void\* context | Context of the device-cloud sync progress observer. |
| [Rdb\_ProgressCallback](../../header-files/relational-store-h/document.md#rdb_progresscallback) callback | Callback used to return the device-cloud sync progress. |
