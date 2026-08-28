# DRM\_MediaKeyRequest

typedef struct DRM\_MediaKeyRequest {...} DRM\_MediaKeyRequest

#### Overview

The struct describes a media key request.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [DRM\_MediaKeyRequestType](../../header-files/native-drm-common-h/document.md#drm_mediakeyrequesttype) type | Type of the media key request. |
| int32\_t dataLen | Length of data in the media key request. |
| uint8\_t data\[MAX\_MEDIA\_KEY\_REQUEST\_DATA\_LEN\] | Data in the media key request. |
| char defaultUrl\[MAX\_DEFAULT\_URL\_LEN\] | URL of the media key server to which the media key request is sent. |
