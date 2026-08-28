# native\_drm\_common.h

#### Overview

The file declares the DRM data types.

**File to include**: <multimedia/drm\_framework/native\_drm\_common.h>

**Library**: libnative\_drm.so

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DRM\_MediaKeyRequestInfo](../../structs/drm-mediakeyrequestinfo/document.md) | DRM\_MediaKeyRequestInfo | Describes the information about a media key request. |
| [DRM\_MediaKeyRequest](../../structs/drm-mediakeyrequest/document.md) | DRM\_MediaKeyRequest | Describes the media key request. |
| [DRM\_Statistics](../../structs/drm-statistics/document.md) | DRM\_Statistics | Describes the metrics for a media key system. |
| [DRM\_OfflineMediakeyIdArray](../../structs/drm-offlinemediakeyidarray/document.md) | DRM\_OfflineMediakeyIdArray | Describes an array of offline media key IDs. |
| [DRM\_KeysInfo](../../structs/drm-keysinfo/document.md) | DRM\_KeysInfo | Describes the information about media keys. |
| [DRM\_MediaKeyStatus](../../structs/drm-mediakeystatus/document.md) | DRM\_MediaKeyStatus | Describes the media key status. |
| [DRM\_PsshInfo](../../structs/drm-psshinfo/document.md) | DRM\_PsshInfo | Describes the Protection System Specific Header (PSSH) data for a DRM system. |
| [DRM\_MediaKeySystemInfo](../../structs/drm-mediakeysysteminfo/document.md) | DRM\_MediaKeySystemInfo | Describes the DRM information for encrypted content. |
| [DRM\_MediaKeySystemDescription](../../structs/drm-mediakeysystemdescription/document.md) | DRM\_MediaKeySystemDescription | Describes the DRM solution name and UUID list. |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) | MediaKeySystem | Describes the media key system. |
| [MediaKeySession](../../structs/mediakeysession/document.md) | MediaKeySession | Describes the media key session. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [DRM\_EventType](#drm_eventtype) | DRM\_EventType | Enumerates the types of events that can be subscribed to. |
| [DRM\_ContentProtectionLevel](#drm_contentprotectionlevel) | DRM\_ContentProtectionLevel | Enumerates the content protection levels. |
| [DRM\_MediaKeyType](#drm_mediakeytype) | DRM\_MediaKeyType | Enumerates the types of media keys. |
| [DRM\_MediaKeyRequestType](#drm_mediakeyrequesttype) | DRM\_MediaKeyRequestType | Enumerates the types of media key requests. |
| [DRM\_OfflineMediaKeyStatus](#drm_offlinemediakeystatus) | DRM\_OfflineMediaKeyStatus | Enumerates the statuses of offline media keys. |
| [DRM\_CertificateStatus](#drm_certificatestatus) | DRM\_CertificateStatus | Enumerates the device certificate statuses. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*DRM\_MediaKeySystemInfoCallback)(DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)](#drm_mediakeysysteminfocallback) | DRM\_MediaKeySystemInfoCallback | Defines the callback used to obtain DRM information from a media source. |

#### \[h2\]Macros

| Name | Description |
| :-- | :-- |
| MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_COUNT 16 | 
Maximum number of optional data entries in a media key request.

**Since**: 11

 |
| MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_NAME\_LEN 64 | 

Maximum length of an optional data name in a media key request.

**Since**: 11

 |
| MAX\_MEDIA\_KEY\_REQUEST\_OPTION\_DATA\_LEN 128 | 

Maximum length of optional data in a media key request.

**Since**: 11

 |
| MAX\_INIT\_DATA\_LEN 2048 | 

Maximum length of initialization data for a media key request.

**Since**: 11

 |
| MAX\_MIMETYPE\_LEN 64 | 

Maximum length of a MIME type.

**Since**: 11

 |
| MAX\_MEDIA\_KEY\_REQUEST\_DATA\_LEN 8192 | 

Maximum length of data in a media key request.

**Since**: 11

 |
| MAX\_DEFAULT\_URL\_LEN 2048 | 

Maximum length of a URL.

**Since**: 11

 |
| MAX\_STATISTICS\_COUNT 10 | 

Maximum number of metric records.

**Since**: 11

 |
| MAX\_STATISTICS\_NAME\_LEN 64 | 

Maximum length of a metric name.

**Since**: 11

 |
| MAX\_STATISTICS\_BUFFER\_LEN 256 | 

Maximum length of a metric buffer.

**Since**: 11

 |
| MAX\_OFFLINE\_MEDIA\_KEY\_ID\_COUNT 512 | 

Maximum number of offline media key IDs.

**Since**: 11

 |
| MAX\_OFFLINE\_MEDIA\_KEY\_ID\_LEN 64 | 

Maximum length of an offline media key ID.

**Since**: 11

 |
| MAX\_KEY\_INFO\_COUNT 64 | 

Maximum number of key information entries.

**Since**: 11

 |
| MAX\_KEY\_ID\_LEN 16 | 

Maximum length of a key ID.

**Since**: 11

 |
| MAX\_KEY\_STATUS\_VALUE\_LEN 128 | 

Maximum length of a key status value.

**Since**: 11

 |
| MAX\_MEDIA\_KEY\_STATUS\_COUNT 64 | 

Maximum number of media key statuses.

**Since**: 11

 |
| MAX\_MEDIA\_KEY\_STATUS\_NAME\_LEN 64 | 

Maximum length of a media key status name.

**Since**: 11

 |
| MAX\_MEDIA\_KEY\_STATUS\_VALUE\_LEN 256 | 

Maximum length of a media key status value.

**Since**: 11

 |
| DRM\_UUID\_LEN 16 | 

Length of the UUID of a DRM solution.

**Since**: 11

 |
| MAX\_PSSH\_DATA\_LEN 2048 | 

Maximum length of PSSH data.

**Since**: 11

 |
| MAX\_PSSH\_INFO\_COUNT 8 | 

Maximum number of PSSH data entries.

**Since**: 11

 |
| MAX\_MEDIA\_KEY\_SYSTEM\_NAME\_LEN 128 | 

Maximum length of a MediaKeySystem instance name.

**Since**: 12

 |
| MAX\_MEDIA\_KEY\_SYSTEM\_NUM 8 | 

Maximum number of MediaKeySystem instances.

**Since**: 12

 |

#### Enum Description

#### \[h2\]DRM\_EventType

enum DRM\_EventType

**Description**

Enumerates the types of events that can be subscribed to.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| EVENT\_DRM\_BASE = 200 | DRM event. |
| EVENT\_PROVISION\_REQUIRED = 201 | Event indicating that the application needs to request a device certificate. |
| EVENT\_KEY\_REQUIRED = 202 | Event indicating that the application needs to request a media key. |
| EVENT\_KEY\_EXPIRED = 203 | Event indicating that the media key expires. |
| EVENT\_VENDOR\_DEFINED = 204 | Vendor-defined event. |
| EVENT\_EXPIRATION\_UPDATE = 206 | Event indicating that the media key is updated on expiry. |

#### \[h2\]DRM\_ContentProtectionLevel

enum DRM\_ContentProtectionLevel

**Description**

Enumerates the content protection levels.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| CONTENT\_PROTECTION\_LEVEL\_UNKNOWN = 0 | Unknown level. |
| CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO | Software-based content protection. |
| CONTENT\_PROTECTION\_LEVEL\_HW\_CRYPTO | Hardware-based content protection. |
| CONTENT\_PROTECTION\_LEVEL\_ENHANCED\_HW\_CRYPTO | Enhanced hardware-based content protection. |
| CONTENT\_PROTECTION\_LEVEL\_MAX | Maximum content protection level. |

#### \[h2\]DRM\_MediaKeyType

enum DRM\_MediaKeyType

**Description**

Enumerates the types of media keys.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| MEDIA\_KEY\_TYPE\_OFFLINE = 0 | Offline media key. |
| MEDIA\_KEY\_TYPE\_ONLINE | Online media key. |

#### \[h2\]DRM\_MediaKeyRequestType

enum DRM\_MediaKeyRequestType

**Description**

Enumerates the types of media key requests.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| MEDIA\_KEY\_REQUEST\_TYPE\_UNKNOWN = 0 | Unknown type. |
| MEDIA\_KEY\_REQUEST\_TYPE\_INITIAL | Initialization request. |
| MEDIA\_KEY\_REQUEST\_TYPE\_RENEWAL | Renewal request. |
| MEDIA\_KEY\_REQUEST\_TYPE\_RELEASE | Release request. |
| MEDIA\_KEY\_REQUEST\_TYPE\_NONE | No request. |
| MEDIA\_KEY\_REQUEST\_TYPE\_UPDATE | Update request. |

#### \[h2\]DRM\_OfflineMediaKeyStatus

enum DRM\_OfflineMediaKeyStatus

**Description**

Enumerates the statuses of offline media keys.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| OFFLINE\_MEDIA\_KEY\_STATUS\_UNKNOWN = 0 | Unknown status. |
| OFFLINE\_MEDIA\_KEY\_STATUS\_USABLE | The media key is available. |
| OFFLINE\_MEDIA\_KEY\_STATUS\_INACTIVE | The media key is inactive. |

#### \[h2\]DRM\_CertificateStatus

enum DRM\_CertificateStatus

**Description**

Enumerates the device certificate statuses.

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| CERT\_STATUS\_PROVISIONED = 0 | A device certificate is provisioned. |
| CERT\_STATUS\_NOT\_PROVISIONED | No device certificate is provisioned or the certificate status is abnormal. |
| CERT\_STATUS\_EXPIRED | The device certificate has expired. |
| CERT\_STATUS\_INVALID | The device certificate is invalid. |
| CERT\_STATUS\_UNAVAILABLE | The device certificate is unavailable. |

#### Function Description

#### \[h2\]DRM\_MediaKeySystemInfoCallback()

typedef void (\*DRM\_MediaKeySystemInfoCallback)(DRM\_MediaKeySystemInfo \*mediaKeySystemInfo)

**Description**

Defines the callback used to obtain DRM information from a media source.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [DRM\_MediaKeySystemInfo](../../structs/drm-mediakeysysteminfo/document.md) \*mediaKeySystemInfo | Pointer to the DRM information obtained from the media source. |
