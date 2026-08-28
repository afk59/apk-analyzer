# DRM\_MediaKeySystemDescription

typedef struct DRM\_MediaKeySystemDescription {...} DRM\_MediaKeySystemDescription

#### Overview

The struct describes the DRM solution name and UUID list.

**Since**: 12

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| char name\[MAX\_MEDIA\_KEY\_SYSTEM\_NAME\_LEN\] | Name of the DRM plugin. |
| uint8\_t uuid\[DRM\_UUID\_LEN\] | UUID of the DRM plugin. |
