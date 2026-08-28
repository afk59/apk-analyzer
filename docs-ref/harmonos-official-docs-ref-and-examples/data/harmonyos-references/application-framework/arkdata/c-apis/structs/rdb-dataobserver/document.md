# Rdb\_DataObserver

typedef struct Rdb\_DataObserver {...} Rdb\_DataObserver

#### Overview

Defines a struct for the data observer.

**Since**: 11

**Related module**: [RDB](../../modules/rdb/document.md)

**Header file**: [relational\_store.h](../../header-files/relational-store-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| void\* context | Pointer to the context of the data observer. |
| [Rdb\_SubscribeCallback](../rdb-subscribecallback/document.md) callback | Callback used to return the result. |
