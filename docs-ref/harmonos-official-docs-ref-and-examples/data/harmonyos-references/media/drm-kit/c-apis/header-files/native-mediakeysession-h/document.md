# native\_mediakeysession.h

#### Overview

The file declares the MediaKeySession APIs for DRM operations.

The APIs can be used to generate media key requests, process responses to media key requests, listen for events, obtain content protection levels, check media key status, and remove media keys.

**File to include**: <multimedia/drm\_framework/native\_mediakeysession.h>

**Library**: libnative\_drm.so

**System capability**: SystemCapability.Multimedia.Drm.Core

**Since**: 11

**Related module**: [Drm](../../modules/drm/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [MediaKeySession\_Callback](../../structs/mediakeysession-callback/document.md) | MediaKeySession\_Callback | Defines the callbacks for media key session events such as key expiration and key changes. It does not provide a MediaKeySession instance, making it suitable for single-session decryption scenarios. |
| [OH\_MediaKeySession\_Callback](../../structs/oh-mediakeysession-callback/document.md) | OH\_MediaKeySession\_Callback | Defines the callbacks for media key session events such as key expiration and key changes. It provides a MediaKeySession instance, making it suitable for multi-session decryption scenarios. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef Drm\_ErrCode (\*MediaKeySession\_EventCallback)(DRM\_EventType eventType, uint8\_t \*info,int32\_t infoLen, char \*extra)](#mediakeysession_eventcallback) | MediaKeySession\_EventCallback | Defines the callback used to listen for media key session events, for example, key expiration events. |
| [typedef Drm\_ErrCode (\*MediaKeySession\_KeyChangeCallback)(DRM\_KeysInfo \*keysInfo, bool newKeysAvailable)](#mediakeysession_keychangecallback) | MediaKeySession\_KeyChangeCallback | Defines the callback used to listen for media key change events. |
| [typedef Drm\_ErrCode (\*OH\_MediaKeySession\_EventCallback)(MediaKeySession \*mediaKeySession, DRM\_EventType eventType,uint8\_t \*info, int32\_t infoLen, char \*extra)](#oh_mediakeysession_eventcallback) | OH\_MediaKeySession\_EventCallback | Defines the callback used to listen for media key session events. |
| [typedef Drm\_ErrCode (\*OH\_MediaKeySession\_KeyChangeCallback)(MediaKeySession \*mediaKeySession, DRM\_KeysInfo \*keysInfo, bool newKeysAvailable)](#oh_mediakeysession_keychangecallback) | OH\_MediaKeySession\_KeyChangeCallback | Defines the callback used to listen for media key change events. |
| [Drm\_ErrCode OH\_MediaKeySession\_GenerateMediaKeyRequest(MediaKeySession \*mediaKeySession, DRM\_MediaKeyRequestInfo \*info, DRM\_MediaKeyRequest \*mediaKeyRequest)](#oh_mediakeysession_generatemediakeyrequest) | \- | Generates a media key request. |
| [Drm\_ErrCode OH\_MediaKeySession\_ProcessMediaKeyResponse(MediaKeySession \*mediaKeySession, uint8\_t \*response, int32\_t responseLen, uint8\_t \*offlineMediaKeyId, int32\_t \*offlineMediaKeyIdLen)](#oh_mediakeysession_processmediakeyresponse) | \- | Processes the response to a media key request. |
| [Drm\_ErrCode OH\_MediaKeySession\_CheckMediaKeyStatus(MediaKeySession \*mediaKeySession, DRM\_MediaKeyStatus \*mediaKeyStatus)](#oh_mediakeysession_checkmediakeystatus) | \- | Checks the status of a media key. |
| [Drm\_ErrCode OH\_MediaKeySession\_ClearMediaKeys(MediaKeySession \*mediaKeySession)](#oh_mediakeysession_clearmediakeys) | \- | Clears media keys. |
| [Drm\_ErrCode OH\_MediaKeySession\_GenerateOfflineReleaseRequest(MediaKeySession \*mediaKeySession, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, uint8\_t \*releaseRequest,int32\_t \*releaseRequestLen)](#oh_mediakeysession_generateofflinereleaserequest) | \- | Generates a request to release offline media keys. |
| [Drm\_ErrCode OH\_MediaKeySession\_ProcessOfflineReleaseResponse(MediaKeySession \*mediaKeySession, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, uint8\_t \*releaseResponse,int32\_t releaseResponseLen)](#oh_mediakeysession_processofflinereleaseresponse) | \- | Processes the response to a request for releasing offline media keys. |
| [Drm\_ErrCode OH\_MediaKeySession\_RestoreOfflineMediaKeys(MediaKeySession \*mediaKeySession, uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen)](#oh_mediakeysession_restoreofflinemediakeys) | \- | Restores offline media keys. |
| [Drm\_ErrCode OH\_MediaKeySession\_GetContentProtectionLevel(MediaKeySession \*mediaKeySession, DRM\_ContentProtectionLevel \*contentProtectionLevel)](#oh_mediakeysession_getcontentprotectionlevel) | \- | Obtains the content protection level of a media key session. |
| [Drm\_ErrCode OH\_MediaKeySession\_RequireSecureDecoderModule(MediaKeySession \*mediaKeySession, const char \*mimeType, bool \*status)](#oh_mediakeysession_requiresecuredecodermodule) | \- | Checks whether secure decoding is required. |
| [Drm\_ErrCode OH\_MediaKeySession\_SetMediaKeySessionCallback(MediaKeySession \*mediaKeySession, MediaKeySession\_Callback \*callback)](#oh_mediakeysession_setmediakeysessioncallback) | \- | Sets a media key session event callback. |
| [Drm\_ErrCode OH\_MediaKeySession\_SetCallback(MediaKeySession \*mediaKeySession, OH\_MediaKeySession\_Callback \*callback)](#oh_mediakeysession_setcallback) | \- | Sets a media key session event callback. |
| [Drm\_ErrCode OH\_MediaKeySession\_Destroy(MediaKeySession \*mediaKeySession)](#oh_mediakeysession_destroy) | \- | Destroys a MediaKeySession instance. |

#### Function Description

#### \[h2\]MediaKeySession\_EventCallback()

typedef  Drm\_ErrCode (\*MediaKeySession\_EventCallback)(DRM\_EventType eventType, uint8\_t \*info,int32\_t infoLen, char \*extra)

**Description**

Defines the callback used to listen for media key session events, for example, key expiration events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [DRM\_EventType](../native-drm-common-h/document.md#drm_eventtype) eventType | Event type. |
| uint8\_t \*info | Pointer to the event information obtained from the media key session. |
| int32\_t infoLen | Length of the event information. |
| char \*extra | Pointer to the additional information obtained from the media key session. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | Error code. |

#### \[h2\]MediaKeySession\_KeyChangeCallback()

typedef  Drm\_ErrCode (\*MediaKeySession\_KeyChangeCallback)(DRM\_KeysInfo \*keysInfo, bool newKeysAvailable)

**Description**

Defines the callback used to listen for media key change events.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [DRM\_KeysInfo](../../structs/drm-keysinfo/document.md) \*keysInfo | Pointer to the media key information. |
| bool newKeysAvailable | Whether the new keys are available. **true** if available, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: Parameter check fails.

 |

#### \[h2\]OH\_MediaKeySession\_EventCallback()

typedef Drm\_ErrCode (\*OH\_MediaKeySession\_EventCallback)(MediaKeySession \*mediaKeySession, DRM\_EventType eventType,uint8\_t \*info, int32\_t infoLen, char \*extra)

**Description**

Defines the callback used to listen for media key session events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| [DRM\_EventType](../native-drm-common-h/document.md#drm_eventtype) eventType | Event type. |
| uint8\_t \*info | Pointer to the event information. |
| int32\_t infoLen | Length of the event information. |
| char \*extra | Pointer to the additional information. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | Error code. |

#### \[h2\]OH\_MediaKeySession\_KeyChangeCallback()

typedef Drm\_ErrCode (\*OH\_MediaKeySession\_KeyChangeCallback)(MediaKeySession \*mediaKeySession, DRM\_KeysInfo \*keysInfo,bool newKeysAvailable)

**Description**

Defines the callback used to listen for media key change events.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| [DRM\_KeysInfo](../../structs/drm-keysinfo/document.md) \*keysInfo | Pointer to the media key information. |
| bool newKeysAvailable | Whether the new keys are available. **true** if available, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: Parameter check fails.

 |

#### \[h2\]OH\_MediaKeySession\_GenerateMediaKeyRequest()

Drm\_ErrCode OH\_MediaKeySession\_GenerateMediaKeyRequest(MediaKeySession \*mediaKeySession,DRM\_MediaKeyRequestInfo \*info, DRM\_MediaKeyRequest \*mediaKeyRequest)

**Description**

Generates a media key request.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| [DRM\_MediaKeyRequestInfo](../../structs/drm-mediakeyrequestinfo/document.md) \*info | Pointer to the information about the media key request. |
| [DRM\_MediaKeyRequest](../../structs/drm-mediakeyrequest/document.md) \*mediaKeyRequest | Pointer to the media key request. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or **info** or **mediaKeyRequest** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_ProcessMediaKeyResponse()

Drm\_ErrCode OH\_MediaKeySession\_ProcessMediaKeyResponse(MediaKeySession \*mediaKeySession,uint8\_t \*response, int32\_t responseLen, uint8\_t \*offlineMediaKeyId, int32\_t \*offlineMediaKeyIdLen)

**Description**

Processes the response to a media key request.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| uint8\_t \*response | Pointer to the response to a media key request. |
| int32\_t responseLen | Pointer to the length of the response. |
| uint8\_t \*offlineMediaKeyId | Pointer to the ID of an offline media key. |
| int32\_t \*offlineMediaKeyIdLen | Length of the offline media key ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or another parameter of the pointer type is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_CheckMediaKeyStatus()

Drm\_ErrCode OH\_MediaKeySession\_CheckMediaKeyStatus(MediaKeySession \*mediaKeySession,DRM\_MediaKeyStatus \*mediaKeyStatus)

**Description**

Checks the status of a media key.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| [DRM\_MediaKeyStatus](../../structs/drm-mediakeystatus/document.md) \*mediaKeyStatus | Pointer to the media key status obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or **mediaKeyStatus** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_ClearMediaKeys()

Drm\_ErrCode OH\_MediaKeySession\_ClearMediaKeys(MediaKeySession \*mediaKeySession)

**Description**

Clears media keys.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_GenerateOfflineReleaseRequest()

Drm\_ErrCode OH\_MediaKeySession\_GenerateOfflineReleaseRequest(MediaKeySession \*mediaKeySession,uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, uint8\_t \*releaseRequest,int32\_t \*releaseRequestLen)

**Description**

Generates a request to release offline media keys.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| uint8\_t \*offlineMediaKeyId | Pointer to the ID of an offline media key. |
| int32\_t \*releaseRequestLen | Length of the offline media key ID. |
| uint8\_t \*releaseRequest | Pointer to the request to release offline media keys. |
| int32\_t \*releaseRequestLen | Length of the request to release offline media keys. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_NO\_MEMORY**: Memory allocation fails due to insufficient system memory.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or another parameter of the pointer type is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs or the DRM solution on the device does not support the release of offline media keys. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_ProcessOfflineReleaseResponse()

Drm\_ErrCode OH\_MediaKeySession\_ProcessOfflineReleaseResponse(MediaKeySession \*mediaKeySession,uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen, uint8\_t \*releaseResponse,int32\_t releaseResponseLen)

**Description**

Processes the response to a request for releasing offline media keys.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| uint8\_t \*offlineMediaKeyId | Pointer to the ID of an offline media key. |
| int32\_t offlineMediaKeyIdLen | Length of the offline media key ID. |
| uint8\_t \*releaseResponse | Pointer to the response. |
| int32\_t releaseResponseLen | Length of the response. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or another parameter of the pointer type is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs or the DRM solution on the device does not support the release of offline media keys. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_RestoreOfflineMediaKeys()

Drm\_ErrCode OH\_MediaKeySession\_RestoreOfflineMediaKeys(MediaKeySession \*mediaKeySession,uint8\_t \*offlineMediaKeyId, int32\_t offlineMediaKeyIdLen)

**Description**

Restores offline media keys.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| uint8\_t \*offlineMediaKeyId | Pointer to the ID of an offline media key. |
| int32\_t offlineMediaKeyIdLen | Length of the offline media key ID. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or another parameter of the pointer type is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_GetContentProtectionLevel()

Drm\_ErrCode OH\_MediaKeySession\_GetContentProtectionLevel(MediaKeySession \*mediaKeySession,DRM\_ContentProtectionLevel \*contentProtectionLevel)

**Description**

Obtains the content protection level of a media key session.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| [DRM\_ContentProtectionLevel](../native-drm-common-h/document.md#drm_contentprotectionlevel) \*contentProtectionLevel | Pointer to the content protection level. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or **contentProtectionLevel** is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_RequireSecureDecoderModule()

Drm\_ErrCode OH\_MediaKeySession\_RequireSecureDecoderModule(MediaKeySession \*mediaKeySession,const char \*mimeType, bool \*status)

**Description**

Checks whether secure decoding is required.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| const char \*mimeType | Pointer to the MIME type. The supported MIME types depend on the DRM solution. Example types are video/avc and video/hev. |
| bool \*status | Pointer to the result indicating whether secure decoding is required. The value **true** means that secure decoding is required, and the value **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or another parameter of the pointer type is nullptr.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |

#### \[h2\]OH\_MediaKeySession\_SetMediaKeySessionCallback()

Drm\_ErrCode OH\_MediaKeySession\_SetMediaKeySessionCallback(MediaKeySession \*mediaKeySession,MediaKeySession\_Callback \*callback)

**Description**

Sets a media key session event callback.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| [MediaKeySession\_Callback](../../structs/mediakeysession-callback/document.md) \*callback | Pointer to the callback for the media key session event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or **callback** is nullptr.

 |

#### \[h2\]OH\_MediaKeySession\_SetCallback()

Drm\_ErrCode OH\_MediaKeySession\_SetCallback(MediaKeySession \*mediaKeySession,OH\_MediaKeySession\_Callback \*callback)

**Description**

Sets a media key session event callback.

**Since**: 12

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |
| [OH\_MediaKeySession\_Callback](../../structs/oh-mediakeysession-callback/document.md) \*callback | Pointer to the callback for the media key session event. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid, or **callback** is nullptr.

 |

#### \[h2\]OH\_MediaKeySession\_Destroy()

Drm\_ErrCode OH\_MediaKeySession\_Destroy(MediaKeySession \*mediaKeySession)

**Description**

Destroys a MediaKeySession instance.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [MediaKeySession](../../structs/mediakeysession/document.md) \*mediaKeySession | Pointer to the MediaKeySession instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [Drm\_ErrCode](../native-drm-err-h/document.md#drm_errcode) | 
**DRM\_ERR\_OK**: The operation is successful.

**DRM\_ERR\_INVALID\_VAL**: The input parameter **mediaKeySession** is nullptr or invalid.

**DRM\_ERR\_UNKNOWN**: An internal error occurs. Check the log details.

 |
