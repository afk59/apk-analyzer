# native\_drm\_err.h

#### Overview

The file declares the DRM error codes.

**File to include**: <multimedia/drm\_framework/native\_drm\_err.h>

**Library**: libnative\_drm.so

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

#### Summary

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [Drm\_ErrCode](#drm_errcode) | Drm\_ErrCode | Enumerates the DRM error codes. |

#### Enum Description

#### \[h2\]Drm\_ErrCode

enum Drm\_ErrCode

**Description**

Enumerates the DRM error codes.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| DRM\_ERR\_OK = 0 | Operation successful. |
| DRM\_CAPI\_ERR\_BASE = 24700500 | Base error code. |
| DRM\_ERR\_NO\_MEMORY = DRM\_CAPI\_ERR\_BASE + 1 | Insufficient memory. |
| DRM\_ERR\_OPERATION\_NOT\_PERMITTED = DRM\_CAPI\_ERR\_BASE + 2 | Operation not permitted. |
| DRM\_ERR\_INVALID\_VAL = DRM\_CAPI\_ERR\_BASE + 3 | Invalid parameter. |
| DRM\_ERR\_IO = DRM\_CAPI\_ERR\_BASE + 4 | I/O error. |
| DRM\_ERR\_TIMEOUT = DRM\_CAPI\_ERR\_BASE + 5 | Network timeout. |
| DRM\_ERR\_UNKNOWN = DRM\_CAPI\_ERR\_BASE + 6 | Unknown error. |
| DRM\_ERR\_SERVICE\_DIED = DRM\_CAPI\_ERR\_BASE + 7 | DRM service unavailable. |
| DRM\_ERR\_INVALID\_STATE = DRM\_CAPI\_ERR\_BASE + 8 | Invalid operation state. |
| DRM\_ERR\_UNSUPPORTED = DRM\_CAPI\_ERR\_BASE + 9 | Unsupported operation. |
| DRM\_ERR\_MAX\_SYSTEM\_NUM\_REACHED = DRM\_CAPI\_ERR\_BASE + 10 | Too many MediaKeySystem instances. |
| DRM\_ERR\_MAX\_SESSION\_NUM\_REACHED = DRM\_CAPI\_ERR\_BASE + 11 | Too many MediaKeySession instances. |
| DRM\_ERR\_EXTEND\_START = DRM\_CAPI\_ERR\_BASE + 100 | Extended error codes start. |
