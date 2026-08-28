# OH\_AVDataSource

typedef struct OH\_AVDataSource {...} OH\_AVDataSource

#### Overview

The struct describes a user-defined data source.

**Since**: 12

**Related module**: [CodecBase](../../modules/codecbase/document.md)

**Header file**: [native\_avcodec\_base.h](../../header-files/native-avcodec-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int64\_t size | Size of the data source. |
| [OH\_AVDataSourceReadAt](../../header-files/native-avcodec-base-h/document.md#oh_avdatasourcereadat) readAt | Callback of the data source. |
