# Rdb\_SubscribeCallback

typedef union Rdb\_SubscribeCallback {...} Rdb\_SubscribeCallback

#### Overview

Defines a callback used to return the subscribed event.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [Rdb\_DetailsObserver](../../header-files/relational-store-h/document.md#rdb_detailsobserver) detailsObserver | Callback used to return the details about the device-cloud data change. |
| [Rdb\_BriefObserver](../../header-files/relational-store-h/document.md#rdb_briefobserver) briefObserver | Callback used to return the device-cloud data change event. |
