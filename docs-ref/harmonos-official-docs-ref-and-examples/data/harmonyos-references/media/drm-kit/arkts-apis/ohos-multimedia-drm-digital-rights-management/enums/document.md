# Enums

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/37/v3/eZ7e11-JQJaEYgQHcetGww/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062430Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8B9D6379CAFAB7D7EF7397CDADA550D517062115FBAA716A84183B76C5E4CE8A)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### DrmErrorCode

Enumerates the DRM error codes.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| ERROR\_UNKNOWN | 24700101 | Unknown error. |
| MAX\_SYSTEM\_NUM\_REACHED | 24700103 | Maximum number of MediaKeySystem instances (64) reached. |
| MAX\_SESSION\_NUM\_REACHED | 24700104 | Maximum number of MediaKeySession instances (64) reached. |
| SERVICE\_FATAL\_ERROR | 24700201 | DRM service fatal error. |

#### PreDefinedConfigName

Enumerates the predefined configuration properties.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CONFIG\_DEVICE\_VENDOR | 'vendor' | Plugin vendor name, which corresponds to the value of **vendor** in the return value of [getConfigurationString](../interface-mediakeysystem/document.md#getconfigurationstring). |
| CONFIG\_DEVICE\_VERSION | 'version' | Plugin version number, which corresponds to the value of **version** in the return value of [getConfigurationString](../interface-mediakeysystem/document.md#getconfigurationstring). |
| CONFIG\_DEVICE\_DESCRIPTION | 'description' | Device description, which corresponds to the value of **description** in the return value of [getConfigurationString](../interface-mediakeysystem/document.md#getconfigurationstring). |
| CONFIG\_DEVICE\_ALGORITHMS | 'algorithms' | Supported algorithms, which correspond to the value of **algorithms** in the return value of [getConfigurationString](../interface-mediakeysystem/document.md#getconfigurationstring). |
| CONFIG\_DEVICE\_UNIQUE\_ID | 'deviceUniqueId' | Unique device ID, which corresponds to the value of **deviceUniqueId** in the return value of [getConfigurationByteArray](../interface-mediakeysystem/document.md#getconfigurationbytearray). |
| CONFIG\_SESSION\_MAX | 'maxSessionNum' | Maximum number of supported sessions, which corresponds to the value of **maxSessionNum** in the return value of [getConfigurationString](../interface-mediakeysystem/document.md#getconfigurationstring). |
| CONFIG\_SESSION\_CURRENT | 'currentSessionNum' | Number of active sessions, which corresponds to the value of **currentSessionNum** in the return value of [getConfigurationString](../interface-mediakeysystem/document.md#getconfigurationstring). |

#### MediaKeyType

Enumerates the types of media keys.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MEDIA\_KEY\_TYPE\_OFFLINE | 0 | Offline media key. |
| MEDIA\_KEY\_TYPE\_ONLINE | 1 | Online media key. |

#### OfflineMediaKeyStatus

Enumerates the statuses of offline media keys.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| OFFLINE\_MEDIA\_KEY\_STATUS\_UNKNOWN | 0 | Unknown status. |
| OFFLINE\_MEDIA\_KEY\_STATUS\_USABLE | 1 | The media key is available. |
| OFFLINE\_MEDIA\_KEY\_STATUS\_INACTIVE | 2 | The media key is inactive. |

#### CertificateStatus

Enumerates the statuses of device certificates.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CERT\_STATUS\_PROVISIONED | 0 | A device certificate is provisioned. |
| CERT\_STATUS\_NOT\_PROVISIONED | 1 | A device certificate is not provisioned. |
| CERT\_STATUS\_EXPIRED | 2 | The device certificate has expired. |
| CERT\_STATUS\_INVALID | 3 | The device certificate is invalid. |
| CERT\_STATUS\_UNAVAILABLE | 4 | The device certificate is unavailable. |

#### MediaKeyRequestType

Enumerates the types of media key requests.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| MEDIA\_KEY\_REQUEST\_TYPE\_UNKNOWN | 0 | Unknown type. |
| MEDIA\_KEY\_REQUEST\_TYPE\_INITIAL | 1 | Initial request. |
| MEDIA\_KEY\_REQUEST\_TYPE\_RENEWAL | 2 | Renewal request. |
| MEDIA\_KEY\_REQUEST\_TYPE\_RELEASE | 3 | Release request. |
| MEDIA\_KEY\_REQUEST\_TYPE\_NONE | 4 | No request. |
| MEDIA\_KEY\_REQUEST\_TYPE\_UPDATE | 5 | Update request. |

#### ContentProtectionLevel

Enumerates the content protection levels.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Value | Description |
| :-- | :-- | :-- |
| CONTENT\_PROTECTION\_LEVEL\_UNKNOWN | 0 | Unknown content protection level. |
| CONTENT\_PROTECTION\_LEVEL\_SW\_CRYPTO | 1 | Software-based content protection. |
| CONTENT\_PROTECTION\_LEVEL\_HW\_CRYPTO | 2 | Hardware-based content protection. |
| CONTENT\_PROTECTION\_LEVEL\_ENHANCED\_HW | 3 | Enhanced hardware-based content protection. |
| CONTENT\_PROTECTION\_LEVEL\_MAX | 4 | Maximum content protection level. |
