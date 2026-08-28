# DRM\_KeysInfo

typedef struct DRM\_KeysInfo {...} DRM\_KeysInfo

#### Overview

The struct describes the information about media keys.

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

**Header file**: [native\_drm\_common.h](../../header-files/native-drm-common-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t keysInfoCount | Number of keys. |
| uint8\_t keyId\[MAX\_KEY\_INFO\_COUNT\]\[MAX\_KEY\_ID\_LEN\] | Array of key IDs. |
| char statusValue\[MAX\_KEY\_INFO\_COUNT\]\[MAX\_KEY\_STATUS\_VALUE\_LEN\] | Value of the key status attribute. |
