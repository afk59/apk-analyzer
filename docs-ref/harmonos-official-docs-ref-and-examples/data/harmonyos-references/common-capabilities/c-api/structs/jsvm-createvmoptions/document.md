# JSVM\_CreateVMOptions

typedef struct {...} JSVM\_CreateVMOptions

#### Overview

Defines options for creating a JavaScript VM.

**Since**: 11

**Related module**: [JSVM](../../modules/jsvm/document.md)

**Header file**: [jsvm\_types.h](../../header-files/jsvm-types-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| size\_t maxOldGenerationSize | Maximum size of the old-generation memory. |
| size\_t maxYoungGenerationSize | Maximum size of the young-generation memory. |
| size\_t initialOldGenerationSize | Initial size of the old-generation memory. |
| size\_t initialYoungGenerationSize | Initial size of the young-generation memory. |
| const char\* snapshotBlobData | Startup snapshot data. |
| size\_t snapshotBlobSize | Size of the startup snapshot data. |
| bool isForSnapshotting | Whether the VM is used for snapshotting. If the value is **true**, VM is used for snapshotting. If the value is **false**, VM is not used for snapshotting. |
