# OH\_AVDataSourceExt

typedef struct OH\_AVDataSourceExt {...} OH\_AVDataSourceExt

#### Overview

The struct describes a user-defined data source. User-defined data can be passed to its callback functions through the **userData** parameter.

**Since**: 20

**Related module**: [CodecBase](../../modules/codecbase/document.md)

**Header file**: [native\_avcodec\_base.h](../../header-files/native-avcodec-base-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| int64\_t size | Size of the data source. |
| [OH\_AVDataSourceReadAtExt](../../header-files/native-avcodec-base-h/document.md#oh_avdatasourcereadatext) readAt | Callback of the data source. |
