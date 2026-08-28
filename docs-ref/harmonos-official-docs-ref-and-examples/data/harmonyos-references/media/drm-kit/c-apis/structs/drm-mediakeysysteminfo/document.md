# DRM\_MediaKeySystemInfo

typedef struct DRM\_MediaKeySystemInfo {...} DRM\_MediaKeySystemInfo

#### Overview

The struct describes the DRM information for encrypted content.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t psshCount | Number of Protection Scheme Specific Header (PSSH) data entries. |
| [DRM\_PsshInfo](../drm-psshinfo/document.md) psshInfo\[MAX\_PSSH\_INFO\_COUNT\] | Array containing PSSH data entries. |
