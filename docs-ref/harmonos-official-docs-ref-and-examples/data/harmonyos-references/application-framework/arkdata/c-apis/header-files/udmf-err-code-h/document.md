# udmf\_err\_code.h

#### Overview

Declares the error codes used in the UDMF.

**File to include**: <database/udmf/udmf\_err\_code.h>

**Library**: libudmf.so

**System capability**: SystemCapability.DistributedDataManager.UDMF.Core

**Since**: 12

**Related module**: [UDMF](../../modules/udmf/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Udmf\_ErrCode](#udmf_errcode) | Udmf\_ErrCode | Enumerates the error codes. |
| [Udmf\_ListenerStatus](#udmf_listenerstatus) | Udmf\_ListenerStatus | Enumerates the status codes returned when data is obtained asynchronously. |

#### Enum Description

#### \[h2\]Udmf\_ErrCode

enum Udmf\_ErrCode

**Description**

Enumerates the error codes.

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| UDMF\_E\_OK = 0 | Operation successful. |
| UDMF\_ERR = 20400000 | Universal error codes. |
| UDMF\_E\_INVALID\_PARAM = (UDMF\_ERR + 1) | Invalid parameter. |

#### \[h2\]Udmf\_ListenerStatus

enum Udmf\_ListenerStatus

**Description**

Enumerates the status codes returned when data is obtained asynchronously.

**Since**: 15

| Enum Item | Description |
| :-- | :-- |
| UDMF\_FINISHED = 0 | Data is obtained successfully. |
| UDMF\_PROCESSING | This task is being processed. |
| UDMF\_CANCELED | This task is canceled. |
| UDMF\_INNER\_ERROR = 200 | An internal error occurs. |
| UDMF\_INVALID\_PARAMETERS | Invalid parameters are contained. |
| UDMF\_DATA\_NOT\_FOUND | No data is obtained. |
| UDMF\_SYNC\_FAILED | An error occurs during data synchronization. |
| UDMF\_COPY\_FILE\_FAILED | Failed to copy the file. |
