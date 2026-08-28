# native\_avsession.h

#### Overview

The file declares the AVSession definition, which can be used to set metadata, playback state, and other information.

**File to include**: <multimedia/av\_session/native\_avsession.h>

**Library**: libohavsession.so

**System capability**: SystemCapability.Multimedia.AVSession.Core

**Since**: 13

**Related module**: [OHAVSession](../../modules/ohavsession/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AVSession\_PlaybackPosition](../../structs/avsession-playbackposition/document.md) | AVSession\_PlaybackPosition | Describes the information related to the playback position. |
| [OH\_AVSession](../../structs/oh-avsession/document.md) | OH\_AVSession | Defines a struct for the playback control session object. You can use **OH\_AVSession\_Create** to create such an object. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [AVSession\_Type](#avsession_type) | AVSession\_Type | Enumerates the session types. |
| [AVSession\_PlaybackState](#avsession_playbackstate) | AVSession\_PlaybackState | Enumerates the media playback states. |
| [AVSession\_LoopMode](#avsession_loopmode) | AVSession\_LoopMode | Enumerates the loop modes of media playback. |
| [AVSession\_ControlCommand](#avsession_controlcommand) | AVSession\_ControlCommand | Enumerates the playback control commands. |
| [AVSessionCallback\_Result](#avsessioncallback_result) | AVSessionCallback\_Result | Enumerates the callback execution results. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnCommand)(OH\_AVSession\* session, AVSession\_ControlCommand command, void\* userData)](#oh_avsessioncallback_oncommand) | OH\_AVSessionCallback\_OnCommand | Defines a callback for a common playback control command. |
| [typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnFastForward)(OH\_AVSession\* session, uint32\_t seekTime, void\* userData)](#oh_avsessioncallback_onfastforward) | OH\_AVSessionCallback\_OnFastForward | Defines a callback for the fast-forward operation. |
| [typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnRewind)(OH\_AVSession\* session, uint32\_t seekTime, void\* userData)](#oh_avsessioncallback_onrewind) | OH\_AVSessionCallback\_OnRewind | Defines a callback for the rewind operation. |
| [typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnSeek)(OH\_AVSession\* session, uint64\_t seekTime, void\* userData)](#oh_avsessioncallback_onseek) | OH\_AVSessionCallback\_OnSeek | Defines a callback for the seek operation. |
| [typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnSetLoopMode)(OH\_AVSession\* session, AVSession\_LoopMode curLoopMode, void\* userData)](#oh_avsessioncallback_onsetloopmode) | OH\_AVSessionCallback\_OnSetLoopMode | Defines a callback for the operation of setting the loop mode. |
| [typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnToggleFavorite)(OH\_AVSession\* session, const char\* assetId, void\* userData)](#oh_avsessioncallback_ontogglefavorite) | OH\_AVSessionCallback\_OnToggleFavorite | Defines a callback for the operation of favoriting a media asset. |
| [AVSession\_ErrCode OH\_AVSession\_Create(AVSession\_Type sessionType, const char\* sessionTag,const char\* bundleName, const char\* abilityName, OH\_AVSession\*\* avsession)](#oh_avsession_create) | \- | Creates a session object. |
| [AVSession\_ErrCode OH\_AVSession\_Destroy(OH\_AVSession\* avsession)](#oh_avsession_destroy) | \- | Destroys a session object. |
| [AVSession\_ErrCode OH\_AVSession\_Activate(OH\_AVSession\* avsession)](#oh_avsession_activate) | \- | Activates a session. |
| [AVSession\_ErrCode OH\_AVSession\_Deactivate(OH\_AVSession\* avsession)](#oh_avsession_deactivate) | \- | Deactivates a session. |
| [AVSession\_ErrCode OH\_AVSession\_GetSessionType(OH\_AVSession\* avsession, AVSession\_Type\* sessionType)](#oh_avsession_getsessiontype) | \- | Obtains the session type. |
| [AVSession\_ErrCode OH\_AVSession\_GetSessionId(OH\_AVSession\* avsession, const char\*\* sessionId)](#oh_avsession_getsessionid) | \- | Obtains the session ID. |
| [AVSession\_ErrCode OH\_AVSession\_SetAVMetadata(OH\_AVSession\* avsession, OH\_AVMetadata\* avmetadata)](#oh_avsession_setavmetadata) | \- | Sets media metadata. |
| [AVSession\_ErrCode OH\_AVSession\_SetPlaybackState(OH\_AVSession\* avsession, AVSession\_PlaybackState playbackState)](#oh_avsession_setplaybackstate) | \- | Sets the playback state. |
| [AVSession\_ErrCode OH\_AVSession\_SetPlaybackPosition(OH\_AVSession\* avsession, AVSession\_PlaybackPosition\* playbackPosition)](#oh_avsession_setplaybackposition) | \- | Sets the playback position. |
| [AVSession\_ErrCode OH\_AVSession\_SetFavorite(OH\_AVSession\* avsession, bool favorite)](#oh_avsession_setfavorite) | \- | Favorites or unfavorites the media asset. |
| [AVSession\_ErrCode OH\_AVSession\_SetLoopMode(OH\_AVSession\* avsession, AVSession\_LoopMode loopMode)](#oh_avsession_setloopmode) | \- | Sets a loop mode. |
| [AVSession\_ErrCode OH\_AVSession\_RegisterCommandCallback(OH\_AVSession\* avsession,AVSession\_ControlCommand command, OH\_AVSessionCallback\_OnCommand callback, void\* userData)](#oh_avsession_registercommandcallback) | \- | Registers a callback for a common playback control command. |
| [AVSession\_ErrCode OH\_AVSession\_UnregisterCommandCallback(OH\_AVSession\* avsession, AVSession\_ControlCommand command, OH\_AVSessionCallback\_OnCommand callback)](#oh_avsession_unregistercommandcallback) | \- | Unregisters the callback for a common playback control command. |
| [AVSession\_ErrCode OH\_AVSession\_RegisterForwardCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnFastForward callback, void\* userData)](#oh_avsession_registerforwardcallback) | \- | Registers a callback for the fast-forward operation. |
| [AVSession\_ErrCode OH\_AVSession\_UnregisterForwardCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnFastForward callback)](#oh_avsession_unregisterforwardcallback) | \- | Unregisters the callback for the fast-forward operation. |
| [AVSession\_ErrCode OH\_AVSession\_RegisterRewindCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnRewind callback, void\* userData)](#oh_avsession_registerrewindcallback) | \- | Registers a callback for the rewind operation. |
| [AVSession\_ErrCode OH\_AVSession\_UnregisterRewindCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnRewind callback)](#oh_avsession_unregisterrewindcallback) | \- | Unregisters the callback for the rewind operation. |
| [AVSession\_ErrCode OH\_AVSession\_RegisterSeekCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnSeek callback, void\* userData)](#oh_avsession_registerseekcallback) | \- | Registers a callback for the seek operation. |
| [AVSession\_ErrCode OH\_AVSession\_UnregisterSeekCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnSeek callback)](#oh_avsession_unregisterseekcallback) | \- | Unregisters the callback for the seek operation. |
| [AVSession\_ErrCode OH\_AVSession\_RegisterSetLoopModeCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnSetLoopMode callback, void\* userData)](#oh_avsession_registersetloopmodecallback) | \- | Registers a callback for the operation of setting the loop mode. |
| [AVSession\_ErrCode OH\_AVSession\_UnregisterSetLoopModeCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnSetLoopMode callback)](#oh_avsession_unregistersetloopmodecallback) | \- | Unregisters the callback for the operation of setting the loop mode. |
| [AVSession\_ErrCode OH\_AVSession\_RegisterToggleFavoriteCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnToggleFavorite callback, void\* userData)](#oh_avsession_registertogglefavoritecallback) | \- | Registers a callback for the operation of favoriting a media asset. |
| [AVSession\_ErrCode OH\_AVSession\_UnregisterToggleFavoriteCallback(OH\_AVSession\* avsession, OH\_AVSessionCallback\_OnToggleFavorite callback)](#oh_avsession_unregistertogglefavoritecallback) | \- | Unregisters the callback for the operation of favoriting a media asset. |

#### Enums

#### \[h2\]AVSession\_Type

enum AVSession\_Type

**Description**

Enumerates the session types.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| SESSION\_TYPE\_AUDIO = 0 | Audio. |
| SESSION\_TYPE\_VIDEO = 1 | Video. |
| SESSION\_TYPE\_VOICE\_CALL = 2 | Audio call. |
| SESSION\_TYPE\_VIDEO\_CALL = 3 | Video call. |

#### \[h2\]AVSession\_PlaybackState

enum AVSession\_PlaybackState

**Description**

Enumerates the media playback states.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| PLAYBACK\_STATE\_INITIAL = 0 | Initial state. |
| PLAYBACK\_STATE\_PREPARING = 1 | Ready. |
| PLAYBACK\_STATE\_PLAYING = 2 | Playing. |
| PLAYBACK\_STATE\_PAUSED = 3 | Paused. |
| PLAYBACK\_STATE\_FAST\_FORWARDING = 4 | Fast-forwarding. |
| PLAYBACK\_STATE\_REWINDED = 5 | Rewinded. |
| PLAYBACK\_STATE\_STOPPED = 6 | Stopped. |
| PLAYBACK\_STATE\_COMPLETED = 7 | Playback complete. |
| PLAYBACK\_STATE\_RELEASED = 8 | Released. |
| PLAYBACK\_STATE\_ERROR = 9 | Error. |
| PLAYBACK\_STATE\_IDLE = 10 | Idle. |
| PLAYBACK\_STATE\_BUFFERING = 11 | Buffering. |
| PLAYBACK\_STATE\_MAX = 12 | Maximum value. (Error code 401 is returned in this case.) |

#### \[h2\]AVSession\_LoopMode

enum AVSession\_LoopMode

**Description**

Enumerates the loop modes of media playback.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| LOOP\_MODE\_SEQUENCE = 0 | Sequential playback. |
| LOOP\_MODE\_SINGLE = 1 | Single loop. |
| LOOP\_MODE\_LIST = 2 | Playlist loop. |
| LOOP\_MODE\_SHUFFLE = 3 | Shuffle. |
| LOOP\_MODE\_CUSTOM = 4 | Custom playback. |

#### \[h2\]AVSession\_ControlCommand

enum AVSession\_ControlCommand

**Description**

Enumerates the playback control commands.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| CONTROL\_CMD\_INVALID = -1 | Invalid control command. |
| CONTROL\_CMD\_PLAY = 0 | Play command. |
| CONTROL\_CMD\_PAUSE = 1 | Pause command. |
| CONTROL\_CMD\_STOP = 2 | Stop command. |
| CONTROL\_CMD\_PLAY\_NEXT = 3 | Command for playing the next media asset. |
| CONTROL\_CMD\_PLAY\_PREVIOUS = 4 | Command for playing the previous media asset. |

#### \[h2\]AVSessionCallback\_Result

enum AVSessionCallback\_Result

**Description**

Enumerates the callback execution results.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| AVSESSION\_CALLBACK\_RESULT\_SUCCESS = 0 | The operation is successful. |
| AVSESSION\_CALLBACK\_RESULT\_FAILURE = -1 | The operation fails. |

#### Function Description

#### \[h2\]OH\_AVSessionCallback\_OnCommand()

typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnCommand)(OH\_AVSession\* session,AVSession\_ControlCommand command, void\* userData)

**Description**

Defines a callback for a common playback control command.

**Since**: 13

#### \[h2\]OH\_AVSessionCallback\_OnFastForward()

typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnFastForward)(OH\_AVSession\* session,uint32\_t seekTime, void\* userData)

**Description**

Defines a callback for the fast-forward operation.

**Since**: 13

#### \[h2\]OH\_AVSessionCallback\_OnRewind()

typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnRewind)(OH\_AVSession\* session,uint32\_t seekTime, void\* userData)

**Description**

Defines a callback for the rewind operation.

**Since**: 13

#### \[h2\]OH\_AVSessionCallback\_OnSeek()

typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnSeek)(OH\_AVSession\* session,uint64\_t seekTime, void\* userData)

**Description**

Defines a callback for the seek operation.

**Since**: 13

#### \[h2\]OH\_AVSessionCallback\_OnSetLoopMode()

typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnSetLoopMode)(OH\_AVSession\* session,AVSession\_LoopMode curLoopMode, void\* userData)

**Description**

Defines a callback for the operation of setting the loop mode.

**Since**: 13

#### \[h2\]OH\_AVSessionCallback\_OnToggleFavorite()

typedef AVSessionCallback\_Result (\*OH\_AVSessionCallback\_OnToggleFavorite)(OH\_AVSession\* session,const char\* assetId, void\* userData)

**Description**

Defines a callback for the operation of favoriting a media asset.

**Since**: 13

#### \[h2\]OH\_AVSession\_Create()

AVSession\_ErrCode OH\_AVSession\_Create(AVSession\_Type sessionType, const char\* sessionTag,const char\* bundleName, const char\* abilityName, OH\_AVSession\*\* avsession)

**Description**

Creates a session object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [AVSession\_Type](#avsession_type) sessionType | Session type. For details about the available options, see [AVSession\_Type](#avsession_type). |
| const char\* sessionTag | Pointer to the session tag. |
| const char\* bundleName | Pointer to the bundle name. |
| const char\* abilityName | Pointer to the ability name. |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\*\* avsession | Double pointer to the session object created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **sessionType** is invalid.

2\. **sessionTag** is nullptr.

3\. **bundleName** is nullptr.

4\. **abilityName** is nullptr.

5\. **avsession** is nullptr.

 |

#### \[h2\]OH\_AVSession\_Destroy()

AVSession\_ErrCode OH\_AVSession\_Destroy(OH\_AVSession\* avsession)

**Description**

Destroys a session object.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**: **avsession** is nullptr.

 |

#### \[h2\]OH\_AVSession\_Activate()

AVSession\_ErrCode OH\_AVSession\_Activate(OH\_AVSession\* avsession)

**Description**

Activates a session.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**: **avsession** is nullptr.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

 |

#### \[h2\]OH\_AVSession\_Deactivate()

AVSession\_ErrCode OH\_AVSession\_Deactivate(OH\_AVSession\* avsession)

**Description**

Deactivates a session.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**: **avsession** is nullptr.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

 |

#### \[h2\]OH\_AVSession\_GetSessionType()

AVSession\_ErrCode OH\_AVSession\_GetSessionType(OH\_AVSession\* avsession, AVSession\_Type\* sessionType)

**Description**

Obtains the session type.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [AVSession\_Type](#avsession_type)\* sessionType | Pointer to the session type obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal or an error occurs.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **sessionType** is nullptr.

 |

#### \[h2\]OH\_AVSession\_GetSessionId()

AVSession\_ErrCode OH\_AVSession\_GetSessionId(OH\_AVSession\* avsession, const char\*\* sessionId)

**Description**

Obtains the session ID.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| const char\*\* sessionId | Double pointer to the session ID obtained. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **sessionId** is nullptr.

 |

#### \[h2\]OH\_AVSession\_SetAVMetadata()

AVSession\_ErrCode OH\_AVSession\_SetAVMetadata(OH\_AVSession\* avsession, OH\_AVMetadata\* avmetadata)

**Description**

Sets media metadata.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVMetadata](../../structs/oh-avmetadatastruct/document.md)\* avmetadata | Pointer to the media metadata. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **avmetadata** is nullptr.

 |

#### \[h2\]OH\_AVSession\_SetPlaybackState()

AVSession\_ErrCode OH\_AVSession\_SetPlaybackState(OH\_AVSession\* avsession,AVSession\_PlaybackState playbackState)

**Description**

Sets the playback state.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [AVSession\_PlaybackState](#avsession_playbackstate) playbackState | Playback state. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **playbackState** is invalid.

 |

#### \[h2\]OH\_AVSession\_SetPlaybackPosition()

AVSession\_ErrCode OH\_AVSession\_SetPlaybackPosition(OH\_AVSession\* avsession,AVSession\_PlaybackPosition\* playbackPosition)

**Description**

Sets the playback position.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [AVSession\_PlaybackPosition](../../structs/avsession-playbackposition/document.md)\* playbackPosition | Pointer to the playback position. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **playbackPosition** is nullptr.

 |

#### \[h2\]OH\_AVSession\_SetFavorite()

AVSession\_ErrCode OH\_AVSession\_SetFavorite(OH\_AVSession\* avsession, bool favorite)

**Description**

Favorites or unfavorites the media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| bool favorite | Whether to favorite or unfavorite the media asset. **true** means to favorite, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**: **avsession** is nullptr.

 |

#### \[h2\]OH\_AVSession\_SetLoopMode()

AVSession\_ErrCode OH\_AVSession\_SetLoopMode(OH\_AVSession\* avsession, AVSession\_LoopMode loopMode)

**Description**

Sets a loop mode.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [AVSession\_LoopMode](#avsession_loopmode) loopMode | Loop mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **loopMode** is invalid.

 |

#### \[h2\]OH\_AVSession\_RegisterCommandCallback()

AVSession\_ErrCode OH\_AVSession\_RegisterCommandCallback(OH\_AVSession\* avsession,AVSession\_ControlCommand command, OH\_AVSessionCallback\_OnCommand callback, void\* userData)

**Description**

Registers a callback for a common playback control command.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [AVSession\_ControlCommand](#avsession_controlcommand) command | Playback control command. |
| [OH\_AVSessionCallback\_OnCommand](#oh_avsessioncallback_oncommand) callback | Callback for the control command. |
| void\* userData | Pointer to the application data passed through the callback functions. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_CODE\_COMMAND\_INVALID**: The playback control command is invalid.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_UnregisterCommandCallback()

AVSession\_ErrCode OH\_AVSession\_UnregisterCommandCallback(OH\_AVSession\* avsession,AVSession\_ControlCommand command, OH\_AVSessionCallback\_OnCommand callback)

**Description**

Unregisters the callback for a common playback control command.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [AVSession\_ControlCommand](#avsession_controlcommand) command | Playback control command. |
| [OH\_AVSessionCallback\_OnCommand](#oh_avsessioncallback_oncommand) callback | Callback for the control command. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_CODE\_COMMAND\_INVALID**: The playback control command is invalid.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_RegisterForwardCallback()

AVSession\_ErrCode OH\_AVSession\_RegisterForwardCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnFastForward callback, void\* userData)

**Description**

Registers a callback for the fast-forward operation.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnFastForward](#oh_avsessioncallback_onfastforward) callback | Callback for the fast-forward operation. |
| void\* userData | Pointer to the application data passed through the callback functions. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_UnregisterForwardCallback()

AVSession\_ErrCode OH\_AVSession\_UnregisterForwardCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnFastForward callback)

**Description**

Unregisters the callback for the fast-forward operation.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnFastForward](#oh_avsessioncallback_onfastforward) callback | Callback for the fast-forward operation. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_RegisterRewindCallback()

AVSession\_ErrCode OH\_AVSession\_RegisterRewindCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnRewind callback, void\* userData)

**Description**

Registers a callback for the rewind operation.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnRewind](#oh_avsessioncallback_onrewind) callback | Callback for the rewind operation. |
| void\* userData | Pointer to the application data passed through the callback functions. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_UnregisterRewindCallback()

AVSession\_ErrCode OH\_AVSession\_UnregisterRewindCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnRewind callback)

**Description**

Unregisters the callback for the rewind operation.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnRewind](#oh_avsessioncallback_onrewind) callback | Callback for the rewind operation. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_RegisterSeekCallback()

AVSession\_ErrCode OH\_AVSession\_RegisterSeekCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnSeek callback, void\* userData)

**Description**

Registers a callback for the seek operation.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnSeek](#oh_avsessioncallback_onseek) callback | Callback for the seek operation. |
| void\* userData | Pointer to the application data passed through the callback functions. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_UnregisterSeekCallback()

AVSession\_ErrCode OH\_AVSession\_UnregisterSeekCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnSeek callback)

**Description**

Unregisters the callback for the seek operation.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnSeek](#oh_avsessioncallback_onseek) callback | Callback for the seek operation. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_RegisterSetLoopModeCallback()

AVSession\_ErrCode OH\_AVSession\_RegisterSetLoopModeCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnSetLoopMode callback, void\* userData)

**Description**

Registers a callback for the operation of setting the loop mode.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnSetLoopMode](#oh_avsessioncallback_onsetloopmode) callback | Callback for the operation of setting the loop mode. |
| void\* userData | Pointer to the application data passed through the callback functions. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_UnregisterSetLoopModeCallback()

AVSession\_ErrCode OH\_AVSession\_UnregisterSetLoopModeCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnSetLoopMode callback)

**Description**

Unregisters the callback for the operation of setting the loop mode.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnSetLoopMode](#oh_avsessioncallback_onsetloopmode) callback | Callback for the operation of setting the loop mode. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_RegisterToggleFavoriteCallback()

AVSession\_ErrCode OH\_AVSession\_RegisterToggleFavoriteCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnToggleFavorite callback, void\* userData)

**Description**

Registers a callback for the operation of favoriting a media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnToggleFavorite](#oh_avsessioncallback_ontogglefavorite) callback | Callback for the operation of favoriting a media asset. |
| void\* userData | Pointer to the application data passed through the callback functions. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |

#### \[h2\]OH\_AVSession\_UnregisterToggleFavoriteCallback()

AVSession\_ErrCode OH\_AVSession\_UnregisterToggleFavoriteCallback(OH\_AVSession\* avsession,OH\_AVSessionCallback\_OnToggleFavorite callback)

**Description**

Unregisters the callback for the operation of favoriting a media asset.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AVSession](../../structs/oh-avsession/document.md)\* avsession | Pointer to a session object. |
| [OH\_AVSessionCallback\_OnToggleFavorite](#oh_avsessioncallback_ontogglefavorite) callback | Callback for the operation of favoriting a media asset. |

**Returns**

| Type | Description |
| :-- | :-- |
| [AVSession\_ErrCode](../native-avsession-errors-h/document.md#avsession_errcode) | 
**AV\_SESSION\_ERR\_SUCCESS**: The function is executed successfully.

**AV\_SESSION\_ERR\_SERVICE\_EXCEPTION**: The session service is abnormal.

**AV\_SESSION\_ERR\_INVALID\_PARAMETER**:

1\. **avsession** is nullptr.

2\. **callback** is nullptr.

 |
