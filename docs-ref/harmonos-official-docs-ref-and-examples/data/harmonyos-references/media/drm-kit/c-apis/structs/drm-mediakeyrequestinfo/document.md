# DRM\_MediaKeyRequestInfo

typedef struct DRM\_MediaKeyRequestInfo {...} DRM\_MediaKeyRequestInfo

#### Overview

The struct describes the information about a media key request.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [DRM\_MediaKeyType](../../header-files/native-drm-common-h/document.md#drm_mediakeytype) type | Type of the media key request. |
| int32\_t initDataLen | Length of the initialization data. |
| uint8\_t initData\[MAX\_INIT\_DATA\_LEN\] | Initialization data in PSSH format (Base64-decoded). |
| char mimeType\[MAX\_MIMETYPE\_LEN\] | MIME type of the media content. |
| uint32\_t optionsCount | Number of options. |
| char optionName\[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT\]\[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_NAME\_LEN\] | Array of option names. |
| char optionData\[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT\]\[MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_DATA\_LEN\] | Array of option values. |
