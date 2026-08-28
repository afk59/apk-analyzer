# DRM\_PsshInfo

typedef struct DRM\_PsshInfo {...} DRM\_PsshInfo

#### Overview

The struct describes the Protection System Specific Header (PSSH) data for a DRM system.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint8\_t uuid\[DRM\_UUID\_LEN\] | UUID identifying the DRM system for the PSSH data. |
| int32\_t dataLen | Length of the PSSH data payload. |
| uint8\_t data\[MAX\_PSSH\_DATA\_LEN\] | PSSH data payload. |
