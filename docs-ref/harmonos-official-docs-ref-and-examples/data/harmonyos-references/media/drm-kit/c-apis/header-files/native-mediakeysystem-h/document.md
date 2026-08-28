# native\_mediakeysystem.h

#### Overview

The file declares the MediaKeySystem APIs for DRM operations.

The APIs can be used to check the support for a DRM solution, create a media key session, obtain and set configurations, obtain DRM metrics, obtain the content protection level, generate media key system requests, process responses to media key system requests, listen for events, and manage offline media keys.

**File to include**: <multimedia/drm\_framework/native\_mediakeysystem.h>

**Library**: libnative\_drm.so

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef Drm\_ErrCode (\*MediaKeySystem\_Callback)(DRM\_EventType eventType, uint8\_t \*info, int32\_t infoLen, char \*extra)](#mediakeysystem_callback) | MediaKeySystem\_Callback | Defines the callbacks for media key system events. It does not provide a MediaKeySystem instance, making it suitable for single-system scenarios. |
| [typedef Drm\_ErrCode (\*OH\_MediaKeySystem\_Callback)(MediaKeySystem \*mediaKeySystem, DRM\_EventType eventType, uint8\_t \*info, int32\_t infoLen, char \*extra)](#oh_mediakeysystem_callback) | OH\_MediaKeySystem\_Callback | Defines the callbacks for media key system events. It provides a MediaKeySystem instance, making it suitable for multi-system scenarios. |
| [Drm\_ErrCode OH\_MediaKeySystem\_SetCallback(MediaKeySystem \*mediaKeySystem, OH\_MediaKeySystem\_Callback callback)](#oh_mediakeysystem_setcallback) | \- | Sets a media key system event callback. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetMediaKeySystems(DRM\_MediaKeySystemDescription \*descs, uint32\_t \*count)](#oh_mediakeysystem_getmediakeysystems) | \- | Obtains the name and ID list of DRM solutions supported by the device. |
| [bool OH\_MediaKeySystem\_IsSupported(const char \*name)](#oh_mediakeysystem_issupported) | \- | Checks whether the device supports the specified DRM solution. |
| [bool OH\_MediaKeySystem\_IsSupported2(const char \*name, const char \*mimeType)](#oh_mediakeysystem_issupported2) | \- | Checks whether the device supports the combination of the DRM solution and MIME type. |
| [bool OH\_MediaKeySystem\_IsSupported3(const char \*name, const char \*mimeType, DRM\_ContentProtectionLevel contentProtectionLevel)](#oh_mediakeysystem_issupported3) | \- | Checks whether the device supports the combination of the DRM solution, MIME type, and content protection level. |
| [Drm\_ErrCode OH\_MediaKeySystem\_Create(const char \*name, MediaKeySystem \*\*mediaKeySystem)](#oh_mediakeysystem_create) | \- | Creates a MediaKeySystem instance. |
| [Drm\_ErrCode OH\_MediaKeySystem\_SetConfigurationString(MediaKeySystem \*mediaKeySystem, const char \*configName, const char \*value)](#oh_mediakeysystem_setconfigurationstring) | \- | Sets a configuration item in the form of a string. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetConfigurationString(MediaKeySystem \*mediaKeySystem, const char \*configName, char \*value, int32\_t valueLen)](#oh_mediakeysystem_getconfigurationstring) | \- | Obtains the value of a configuration item in the form of a string. |
| [Drm\_ErrCode OH\_MediaKeySystem\_SetConfigurationByteArray(MediaKeySystem \*mediaKeySystem, const char \*configName, uint8\_t \*value, int32\_t valueLen)](#oh_mediakeysystem_setconfigurationbytearray) | \- | Sets a configuration item in the form of an array. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetConfigurationByteArray(MediaKeySystem \*mediaKeySystem, const char \*configName, uint8\_t \*value, int32\_t \*valueLen)](#oh_mediakeysystem_getconfigurationbytearray) | \- | Obtains the value of a configuration item in the form of an array. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetStatistics(MediaKeySystem \*mediaKeySystem, DRM\_Statistics \*statistics)](#oh_mediakeysystem_getstatistics) | \- | Obtains the metrics of a media key system. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetMaxContentProtectionLevel(MediaKeySystem \*mediaKeySystem, DRM\_ContentProtectionLevel \*contentProtectionLevel)](#oh_mediakeysystem_getmaxcontentprotectionlevel) | \- | Obtains the maximum content protection level supported by the device. |
| [Drm\_ErrCode OH\_MediaKeySystem\_SetMediaKeySystemCallback(MediaKeySystem \*mediaKeySystem, MediaKeySystem\_Callback callback)](#oh_mediakeysystem_setmediakeysystemcallback) | \- | Sets a media key system event callback. |
| [Drm\_ErrCode OH\_MediaKeySystem\_CreateMediaKeySession(MediaKeySystem \*mediaKeySystem, DRM\_ContentProtectionLevel \*level, MediaKeySession \*\*mediaKeySession)](#oh_mediakeysystem_createmediakeysession) | \- | Creates a MediaKeySession instance. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GenerateKeySystemRequest(MediaKeySystem \*mediaKeySystem, uint8\_t \*request, int32\_t \*requestLen, char \*defaultUrl, int32\_t defaultUrlLen)](#oh_mediakeysystem_generatekeysystemrequest) | \- | Generates a request to obtain a device certificate. |
| [Drm\_ErrCode OH\_MediaKeySystem\_ProcessKeySystemResponse(MediaKeySystem \*mediaKeySystem, uint8\_t \*response, int32\_t responseLen)](#oh_mediakeysystem_processkeysystemresponse) | \- | Processes the response to a previously generated device certificate request. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetOfflineMediaKeyIds(MediaKeySystem \*mediaKeySystem, DRM\_OfflineMediakeyIdArray \*offlineMediaKeyIds)](#oh_mediakeysystem_getofflinemediakeyids) | \- | Obtains the list of offline media key IDs, which are used to manage offline media keys. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetOfflineMediaKeyStatus(MediaKeySystem \*mediaKeySystem, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, DRM\_OfflineMediaKeyStatus \*status)](#oh_mediakeysystem_getofflinemediakeystatus) | \- | Obtains the status of an offline media key. |
| [Drm\_ErrCode OH\_MediaKeySystem\_ClearOfflineMediaKeys(MediaKeySystem \*mediaKeySystem, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen)](#oh_mediakeysystem_clearofflinemediakeys) | \- | Clears offline media keys with the specified IDs. |
| [Drm\_ErrCode OH\_MediaKeySystem\_GetCertificateStatus(MediaKeySystem \*mediaKeySystem, DRM\_CertificateStatus \*certStatus)](#oh_mediakeysystem_getcertificatestatus) | \- | Obtains the status of a device certificate. |
| [Drm\_ErrCode OH\_MediaKeySystem\_Destroy(MediaKeySystem \*mediaKeySystem)](#oh_mediakeysystem_destroy) | \- | Destroys a MediaKeySystem instance. |

#### Function Description

#### \[h2\]MediaKeySystem\_Callback()

typedef  Drm\_ErrCode (\*MediaKeySystem\_Callback)(DRM\_EventType eventType, uint8\_t \*info,int32\_t infoLen, char \*extra)

**Description**

Defines the callbacks for media key system events. It does not provide a MediaKeySystem instance, making it suitable for single-system scenarios.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [DRM\_EventType](../native-drm-common-h/document.md#drm_eventtype) eventType | Event type. |
| uint8\_t \*info | Pointer to the event information. |
| int32\_t infoLen | Length of the event information. |
| char \*extra | Pointer to the additional information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: An input parameter is invalid.

 |

#### \[h2\]OH\_MediaKeySystem\_Callback()

typedef Drm\_ErrCode (\*OH\_MediaKeySystem\_Callback)(MediaKeySystem \*mediaKeySystem, DRM\_EventType eventType,uint8\_t \*info, int32\_t infoLen, char \*extra)

**Description**

Defines the callbacks for media key system events. It provides a MediaKeySystem instance, making it suitable for multi-system scenarios.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| [DRM\_EventType](../native-drm-common-h/document.md#drm_eventtype) eventType | Event type. |
| uint8\_t \*info | Pointer to the event information. |
| int32\_t infoLen | Length of the event information. |
| char \*extra | Pointer to the additional information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: An input parameter is invalid.

 |

#### \[h2\]OH\_MediaKeySystem\_SetCallback()

Drm\_ErrCode OH\_MediaKeySystem\_SetCallback(MediaKeySystem \*mediaKeySystem, OH\_MediaKeySystem\_Callback callback)

**Description**

Sets a media key system event callback.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| [OH\_MediaKeySystem\_Callback](#oh_mediakeysystem_callback) callback | Callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid.

 |

#### \[h2\]OH\_MediaKeySystem\_GetMediaKeySystems()

Drm\_ErrCode OH\_MediaKeySystem\_GetMediaKeySystems(DRM\_MediaKeySystemDescription \*descs, uint32\_t \*count)

**Description**

Obtains the name and ID list of DRM solutions supported by the device.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [DRM\_MediaKeySystemDescription](../../structs/drm-mediakeysystemdescription/document.md) \*descs | Pointer to the list of the names and UUIDs of DRM solutions. |
| uint32\_t \*count | Pointer to the number of DRM solutions in the list. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: Possible causes:

1\. The input parameter **descs** or **count** is a null pointer.

2\. The length of the input parameter **descs** is insufficient.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_IsSupported()

bool OH\_MediaKeySystem\_IsSupported(const char \*name)

**Description**

Checks whether the device supports the specified DRM solution.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Pointer to the DRM solution name. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of the DRM solution. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_MediaKeySystem\_IsSupported2()

bool OH\_MediaKeySystem\_IsSupported2(const char \*name, const char \*mimeType)

**Description**

Checks whether the device supports the combination of the DRM solution and MIME type.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Pointer to the DRM solution name. |
| const char \*mimeType | Pointer to the MIME type. The supported MIME types depend on the DRM solution. Example types are video/avc and video/hev. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of the combination. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_MediaKeySystem\_IsSupported3()

bool OH\_MediaKeySystem\_IsSupported3(const char \*name, const char \*mimeType,DRM\_ContentProtectionLevel contentProtectionLevel)

**Description**

Checks whether the device supports the combination of the DRM solution, MIME type, and content protection level.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Pointer to the DRM solution name. |
| const char \*mimeType | Pointer to the MIME type. The supported MIME types depend on the DRM solution. Example types are video/avc and video/hev. |
| [DRM\_ContentProtectionLevel](../native-drm-common-h/document.md#drm_contentprotectionlevel) contentProtectionLevel | Content protection level. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of the combination. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_MediaKeySystem\_Create()

Drm\_ErrCode OH\_MediaKeySystem\_Create(const char \*name, MediaKeySystem \*\*mediaKeySystem)

**Description**

Creates a MediaKeySystem instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| const char \*name | Pointer to the DRM solution name. |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*\*mediaKeySystem | Double pointer to the MediaKeySystem instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: Possible causes:

1\. The input parameter **name** is nullptr or its length is 0.

2\. The input parameter **mediaKeySystem** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

**DRM\_ERR\_SERVICE\_DIED**: The service is dead.

**DRM\_ERR\_MAX\_SYSTEM\_NUM\_REACHED**: The number of created MediaKeySystem instances has reached the upper limit (64).

 |

#### \[h2\]OH\_MediaKeySystem\_SetConfigurationString()

Drm\_ErrCode OH\_MediaKeySystem\_SetConfigurationString(MediaKeySystem \*mediaKeySystem,const char \*configName, const char \*value)

**Description**

Sets a configuration item in the form of a string.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| const char \*configName | Pointer to the name of the configuration item in the form of a string. It is determined by the DRM solution on the device and cannot be empty. |
| const char \*value | Pointer to the value of the configuration item in the form of a string. It is determined by the DRM solution on the device and cannot be empty. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **configName** or **value** is nullptr.

 |

#### \[h2\]OH\_MediaKeySystem\_GetConfigurationString()

Drm\_ErrCode OH\_MediaKeySystem\_GetConfigurationString(MediaKeySystem \*mediaKeySystem,const char \*configName, char \*value, int32\_t valueLen)

**Description**

Obtains the value of a configuration item in the form of a string.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| const char \*configName | Pointer to the name of the configuration item. |
| char \*value | Pointer to the value of the configuration item. |
| int32\_t valueLen | Length of the value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **configName** or **value** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_SetConfigurationByteArray()

Drm\_ErrCode OH\_MediaKeySystem\_SetConfigurationByteArray(MediaKeySystem \*mediaKeySystem,const char \*configName, uint8\_t \*value, int32\_t valueLen)

**Description**

Sets a configuration item in the form of an array.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| const char \*configName | Pointer to the name of the configuration item in the form of a character array. It is determined by the DRM solution on the device and cannot be empty. |
| uint8\_t \*value | Pointer to the value of the configuration item in the form of a character array. It is determined by the DRM solution on the device and cannot be empty. |
| int32\_t valueLen | Length of the value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **configName** or **value** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_GetConfigurationByteArray()

Drm\_ErrCode OH\_MediaKeySystem\_GetConfigurationByteArray(MediaKeySystem \*mediaKeySystem,const char \*configName, uint8\_t \*value, int32\_t \*valueLen)

**Description**

Obtains the value of a configuration item in the form of an array.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| const char \*configName | Pointer to the name of the configuration item in the form of a character array. It is determined by the DRM solution on the device and cannot be empty. |
| uint8\_t \*value | Pointer to the value of the configuration item. |
| int32\_t \*valueLen | Pointer to the length of the value. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **configName**, **value**, or **valueLen** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_GetStatistics()

Drm\_ErrCode OH\_MediaKeySystem\_GetStatistics(MediaKeySystem \*mediaKeySystem, DRM\_Statistics \*statistics)

**Description**

Obtains the metrics of a media key system.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| [DRM\_Statistics](../../structs/drm-statistics/document.md) \*statistics | Pointer to the metrics. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **statistics** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_GetMaxContentProtectionLevel()

Drm\_ErrCode OH\_MediaKeySystem\_GetMaxContentProtectionLevel(MediaKeySystem \*mediaKeySystem,DRM\_ContentProtectionLevel \*contentProtectionLevel)

**Description**

Obtains the maximum content protection level supported by the device.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| [DRM\_ContentProtectionLevel](../native-drm-common-h/document.md#drm_contentprotectionlevel) \*contentProtectionLevel | Pointer to the content protection level. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **contentProtectionLevel** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_SetMediaKeySystemCallback()

Drm\_ErrCode OH\_MediaKeySystem\_SetMediaKeySystemCallback(MediaKeySystem \*mediaKeySystem,MediaKeySystem\_Callback callback)

**Description**

Sets a media key system event callback.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| [MediaKeySystem\_Callback](#mediakeysystem_callback) callback | Callback. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid.

 |

#### \[h2\]OH\_MediaKeySystem\_CreateMediaKeySession()

Drm\_ErrCode OH\_MediaKeySystem\_CreateMediaKeySession(MediaKeySystem \*mediaKeySystem,DRM\_ContentProtectionLevel \*level, MediaKeySession \*\*mediaKeySession)

**Description**

Creates a MediaKeySession instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| [DRM\_ContentProtectionLevel](../native-drm-common-h/document.md#drm_contentprotectionlevel) \*level | Pointer to the content protection level. |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*\*mediaKeySession | Double pointer to the MediaKeySession instance created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, **level** is out of range, or **mediaKeySession** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

**DRM\_ERR\_SERVICE\_DIED**: The service is dead.

**DRM\_ERR\_MAX\_SESSION\_NUM\_REACHED**: The number of MediaKeySession instances created by the MediaKeySystem instance reaches the upper limit (64).

 |

#### \[h2\]OH\_MediaKeySystem\_GenerateKeySystemRequest()

Drm\_ErrCode OH\_MediaKeySystem\_GenerateKeySystemRequest(MediaKeySystem \*mediaKeySystem, uint8\_t \*request,int32\_t \*requestLen, char \*defaultUrl, int32\_t defaultUrlLen)

**Description**

Generates a request to obtain a device certificate.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| uint8\_t \*request | Pointer to the device certificate request. |
| int32\_t \*requestLen | Pointer to the length of the device certificate request. |
| char \*defaultUrl | Pointer to the URL of the provisioning server. |
| int32\_t defaultUrlLen | Length of the URL of the provisioning server. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or another parameter of the pointer type is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_ProcessKeySystemResponse()

Drm\_ErrCode OH\_MediaKeySystem\_ProcessKeySystemResponse(MediaKeySystem \*mediaKeySystem,uint8\_t \*response, int32\_t responseLen)

**Description**

Processes the response to a previously generated device certificate request.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| uint8\_t \*response | Pointer to the response to a previously generated device certificate request. |
| int32\_t responseLen | Length of the response. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **response** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_GetOfflineMediaKeyIds()

Drm\_ErrCode OH\_MediaKeySystem\_GetOfflineMediaKeyIds(MediaKeySystem \*mediaKeySystem,DRM\_OfflineMediakeyIdArray \*offlineMediaKeyIds)

**Description**

Obtains the list of offline media key IDs, which are used to manage offline media keys.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| [DRM\_OfflineMediakeyIdArray](../../structs/drm-offlinemediakeyidarray/document.md) \*offlineMediaKeyIds | Pointer to the IDs of offline media keys. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **offlineMediaKeyIds** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_GetOfflineMediaKeyStatus()

Drm\_ErrCode OH\_MediaKeySystem\_GetOfflineMediaKeyStatus(MediaKeySystem \*mediaKeySystem,uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, DRM\_OfflineMediaKeyStatus \*status)

**Description**

Obtains the status of an offline media key.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| uint8\_t \*offlineMediaKeyId | Pointer to the ID of an offline media key. |
| int32\_t offlineMediaKeyIdLen | Length of the offline media key ID. |
| [DRM\_OfflineMediaKeyStatus](../native-drm-common-h/document.md#drm_offlinemediakeystatus) \*status | Pointer to the media key status obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or another parameter of the pointer type is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_ClearOfflineMediaKeys()

Drm\_ErrCode OH\_MediaKeySystem\_ClearOfflineMediaKeys(MediaKeySystem \*mediaKeySystem,uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen)

**Description**

Clears offline media keys with the specified IDs.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| uint8\_t \*offlineMediaKeyId | Pointer to the ID of an offline media key. |
| int32\_t offlineMediaKeyIdLen | Length of the offline media key ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **offlineMediaKeyId** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_GetCertificateStatus()

Drm\_ErrCode OH\_MediaKeySystem\_GetCertificateStatus(MediaKeySystem \*mediaKeySystem,DRM\_CertificateStatus \*certStatus)

**Description**

Obtains the status of a device certificate.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |
| [DRM\_CertificateStatus](../native-drm-common-h/document.md#drm_certificatestatus) \*certStatus | Pointer to the device certificate status. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid, or **certStatus** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySystem\_Destroy()

Drm\_ErrCode OH\_MediaKeySystem\_Destroy(MediaKeySystem \*mediaKeySystem)

**Description**

Destroys a MediaKeySystem instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySystem](../../structs/mediakeysystem/document.md) \*mediaKeySystem | Pointer to the MediaKeySystem instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySystem** is nullptr or invalid.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |
