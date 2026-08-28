# DRM\_OfflineMediakeyIdArray

typedef struct DRM\_OfflineMediakeyIdArray {...} DRM\_OfflineMediakeyIdArray

#### Overview

The struct describes an array of offline media key IDs.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t idsCount | Number of IDs in the array. |
| int32\_t idsLen\[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT\] | Array of lengths for each media key ID. |
| uint8\_t ids\[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT\]\[MAX\_OFFLINE\_MEDIA\_KEY\_ID\_LEN\] | Array of media key ID data. |
