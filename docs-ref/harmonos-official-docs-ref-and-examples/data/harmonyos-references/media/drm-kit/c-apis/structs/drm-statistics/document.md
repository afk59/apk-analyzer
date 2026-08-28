# DRM\_Statistics

typedef struct DRM\_Statistics {...} DRM\_Statistics

#### Overview

The struct describes the metrics for a media key system.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t statisticsCount | Number of metrics. |
| char statisticsName\[MAX\_STATISTICS\_COUNT\]\[MAX\_STATISTICS\_NAME\_LEN\] | Array of metric names. |
| char statisticsDescription\[MAX\_STATISTICS\_COUNT\]\[MAX\_STATISTICS\_BUFFER\_LEN\] | Array of metric descriptions. |
