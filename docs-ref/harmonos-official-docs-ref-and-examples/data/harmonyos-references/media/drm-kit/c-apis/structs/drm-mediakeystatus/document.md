# DRM\_MediaKeyStatus

typedef struct DRM\_MediaKeyStatus {...} DRM\_MediaKeyStatus

#### Overview

The struct describes the media key status.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t statusCount | Number of media key statuses. |
| char statusName\[MAX\_MEDIA\_KEY\_STATUS\_COUNT\]\[MAX\_MEDIA\_KEY\_STATUS\_NAME\_LEN\] | Array of status names. |
| char statusValue\[MAX\_MEDIA\_KEY\_STATUS\_COUNT\]\[MAX\_MEDIA\_KEY\_STATUS\_VALUE\_LEN\] | Array of status values. |
