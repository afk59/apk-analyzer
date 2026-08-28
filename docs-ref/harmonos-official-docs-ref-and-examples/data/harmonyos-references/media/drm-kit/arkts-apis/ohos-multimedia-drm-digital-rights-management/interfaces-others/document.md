# Interfaces (Others)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ed/v3/Tyd4IcdGQIKoj1t6XJO2fg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062430Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D8D7BA8499C52CD7889BAFC91DC6FC8C380C0A1EFDCCE9AC19CE2F001DDF1159)

The initial APIs of this module are supported since API version 11. Newly added APIs will be marked with a superscript to indicate their earliest API version.

#### ProvisionRequest

Defines a device certificate provisioning request.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| data | Uint8Array | No | No | Binary data of the provisioning request. |
| defaultURL | string | No | No | URL of the device certificate provisioning server. |

#### OptionsData

Defines optional parameters for a device certificate request.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the optional parameter. |
| value | string | No | No | Value of the optional parameter. |

#### MediaKeyRequest

Defines a media key request.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| mediaKeyRequestType | [MediaKeyRequestType](../enums/document.md#mediakeyrequesttype) | No | No | Type of the media key request. |
| data | Uint8Array | No | No | Binary data of the media key request. |
| defaultURL | string | No | No | URL of the license server. |

#### EventInfo

Defines the DRM event information.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| info | Uint8Array | No | No | Event payload data. |
| extraInfo | string | No | No | Additional event context. |

#### StatisticKeyValue

Defines a key-value pair for DRM metrics.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the metric. |
| value | string | No | No | Value of the metric. |

#### MediaKeyStatus

Defines a status attribute for a media key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Name of the media key status attribute, for example, expiration time or content protection level. |
| value | string | No | No | Value of the media key status attribute. |

#### KeysInfo

Defines the status information of a media key.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| keyId | Uint8Array | No | No | Media key ID. |
| value | string | No | No | Media key status. |

#### MediaKeySystemInfo

Defines the DRM information for encrypted content.

**Atomic service API**: This API can be used in atomic services since API version 12.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| uuid | string | No | No | UUID of the DRM system. |
| pssh | Uint8Array | No | No | Protection System Specific Header (PSSH) data. |

#### MediaKeySystemDescription12+

Defines the DRM plugin information.

**Atomic service API**: This API can be used in atomic services since API version 14.

**System capability**: SystemCapability.Multimedia.Drm.Core

| Name | Type | Read-Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Plugin name. |
| uuid | string | No | No | Unique identifier of the plugin. |
