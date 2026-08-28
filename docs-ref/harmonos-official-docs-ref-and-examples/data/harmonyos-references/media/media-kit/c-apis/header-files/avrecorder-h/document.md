# avrecorder.h

#### Overview

The file declares the AVRecorder APIs. Applications can use the APIs to record media data.

**File to include**: <multimedia/player\_framework/avrecorder.h>

**Library**: libavrecorder.so

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Related module**: [AVRecorder](../../modules/avrecorder/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [OH\_AVRecorder \*OH\_AVRecorder\_Create(void)](#oh_avrecorder_create) | Creates an AVRecorder instance. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_IDLE state. |
| [OH\_AVErrCode OH\_AVRecorder\_Prepare(OH\_AVRecorder \*recorder, OH\_AVRecorder\_Config \*config)](#oh_avrecorder_prepare) | 
Sets AVRecorder parameters to prepare for recording. This function must be called after [OH\_AVRecorder\_Create](#oh_avrecorder_create) is successfully triggered. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_PREPARED state.

To record only audio, you do not need to set video parameters. Similarly, to record only video, you do not need to set audio parameters.

 |
| [OH\_AVErrCode OH\_AVRecorder\_GetAVRecorderConfig(OH\_AVRecorder \*recorder, OH\_AVRecorder\_Config \*\*config)](#oh_avrecorder_getavrecorderconfig) | Obtains the AVRecorder configuration. This function must be called after the recording preparation is complete. **config** must be set to nullptr. The framework layer allocates and releases the memory in a unified manner to avoid issues with memory management, such as leaks or double freeing. |
| [OH\_AVErrCode OH\_AVRecorder\_GetInputSurface(OH\_AVRecorder \*recorder, OHNativeWindow \*\*window)](#oh_avrecorder_getinputsurface) | 

Obtains an input surface. This function must be called after [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) is successfully triggered and before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called.

The caller obtains the **surfaceBuffer** from this surface and fills in the corresponding video data.

 |
| [OH\_AVErrCode OH\_AVRecorder\_UpdateRotation(OH\_AVRecorder \*recorder, int32\_t rotation)](#oh_avrecorder_updaterotation) | Updates the video rotation angle. This function must be called after [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) is successfully triggered and before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called. |
| [OH\_AVErrCode OH\_AVRecorder\_Start(OH\_AVRecorder \*recorder)](#oh_avrecorder_start) | Starts recording. This function must be called after [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) is successfully triggered. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_STARTED state. |
| [OH\_AVErrCode OH\_AVRecorder\_Pause(OH\_AVRecorder \*recorder)](#oh_avrecorder_pause) | 

Pauses recording. This function must be called after [OH\_AVRecorder\_Start](#oh_avrecorder_start) is successfully triggered and the AVRecorder is in the AVRECORDER\_STARTED state. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_PAUSED state.

Then, you can call [OH\_AVRecorder\_Resume](#oh_avrecorder_resume) to resume recording, and the AVRecorder transitions the AVRECORDER\_STARTED state again.

 |
| [OH\_AVErrCode OH\_AVRecorder\_Resume(OH\_AVRecorder \*recorder)](#oh_avrecorder_resume) | Resumes recording. This function must be called after [OH\_AVRecorder\_Pause](#oh_avrecorder_pause) is successfully triggered and the AVRecorder is in the AVRECORDER\_PAUSED state. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_STARTED state. |
| [OH\_AVErrCode OH\_AVRecorder\_Stop(OH\_AVRecorder \*recorder)](#oh_avrecorder_stop) | 

Stops recording. This function must be called after [OH\_AVRecorder\_Start](#oh_avrecorder_start) is successfully triggered. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_STOPPED state.

For audio-only recording, you can call [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) again for re-recording.

For video-only recording or audio and video recording, you can call [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) and [OH\_AVRecorder\_GetInputSurface](#oh_avrecorder_getinputsurface) again for re-recording.

 |
| [OH\_AVErrCode OH\_AVRecorder\_Reset(OH\_AVRecorder \*recorder)](#oh_avrecorder_reset) | 

Resets the recording state. This function must be called when the AVRecorder is not in the AVRECORDER\_RELEASED state. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_IDLE state.

For audio-only recording, you can call [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) again for re-recording.

For video-only recording or audio and video recording, you can call [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) and [OH\_AVRecorder\_GetInputSurface](#oh_avrecorder_getinputsurface) again for re-recording.

 |
| [OH\_AVErrCode OH\_AVRecorder\_Release(OH\_AVRecorder \*recorder)](#oh_avrecorder_release) | 

Releases recording resources. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_RELEASED state.

The recorder memory will be released. The application layer must explicitly set the recorder to nullptr to avoid access to wild pointers. After the resources are released, you can no longer perform any operation on the OH\_AVRecorder instance.

 |
| [OH\_AVErrCode OH\_AVRecorder\_GetAvailableEncoder(OH\_AVRecorder \*recorder, OH\_AVRecorder\_EncoderInfo \*\*info, int32\_t \*length)](#oh_avrecorder_getavailableencoder) | 

Obtains the available encoders and encoder information of the AVRecorder.

**info** must be set to nullptr. The framework layer allocates and releases the memory in a unified manner to avoid issues with memory management, such as leaks or double freeing.

 |
| [OH\_AVErrCode OH\_AVRecorder\_SetStateCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnStateChange callback, void \*userData)](#oh_avrecorder_setstatecallback) | Sets a state callback so that the application can respond to state change events generated by the AVRecorder. This function must be called before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called. |
| [OH\_AVErrCode OH\_AVRecorder\_SetErrorCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnError callback, void \*userData)](#oh_avrecorder_seterrorcallback) | Sets an error callback so that the application can respond to error events generated by the AVRecorder. This function must be called before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called. |
| [OH\_AVErrCode OH\_AVRecorder\_SetUriCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnUri callback, void \*userData)](#oh_avrecorder_seturicallback) | Sets a URI callback so that the application can respond to URI events generated by the AVRecorder. This function must be called before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called. |
| [OH\_AVErrCode OH\_AVRecorder\_SetWillMuteWhenInterrupted(OH\_AVRecorder \*recorder, bool muteWhenInterrupted)](#oh_avrecorder_setwillmutewheninterrupted) | Sets whether to enable the mute interruption mode. |

#### Function Description

#### \[h2\]OH\_AVRecorder\_Create()

OH\_AVRecorder \*OH\_AVRecorder\_Create(void)

**Description**

Creates an AVRecorder instance. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_IDLE state.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) | Pointer to the OH\_AVRecorder instance created if the operation is successful; nullptr otherwise. |

#### \[h2\]OH\_AVRecorder\_Prepare()

OH\_AVErrCode OH\_AVRecorder\_Prepare(OH\_AVRecorder \*recorder, OH\_AVRecorder\_Config \*config)

**Description**

Sets AVRecorder parameters to prepare for recording. This function must be called after [OH\_AVRecorder\_Create](#oh_avrecorder_create) is successfully triggered. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_PREPARED state.

To record only audio, you do not need to set video parameters. Similarly, to record only video, you do not need to set audio parameters.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OH\_AVRecorder\_Config](../../structs/oh-avrecorder-config/document.md) \*config | Pointer to the OH\_AVRecorder\_Config instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr or the preparation fails.

 |

#### \[h2\]OH\_AVRecorder\_GetAVRecorderConfig()

OH\_AVErrCode OH\_AVRecorder\_GetAVRecorderConfig(OH\_AVRecorder \*recorder, OH\_AVRecorder\_Config \*\*config)

**Description**

Obtains the AVRecorder configuration. This function must be called after the recording preparation is complete.

**config** must be set to nullptr. The framework layer allocates and releases the memory in a unified manner to avoid issues with memory management, such as leaks or double freeing.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OH\_AVRecorder\_Config](../../structs/oh-avrecorder-config/document.md) \*\*config | Pointer to the OH\_AVRecorder\_Config instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr or **config** is not nullptr.

**AV\_ERR\_NO\_MEMORY**: The memory fails to be allocated due to insufficient memory.

 |

#### \[h2\]OH\_AVRecorder\_GetInputSurface()

OH\_AVErrCode OH\_AVRecorder\_GetInputSurface(OH\_AVRecorder \*recorder, OHNativeWindow \*\*window)

**Description**

Obtains an input surface. This function must be called after [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) is successfully triggered and before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called.

The caller obtains the **surfaceBuffer** from this surface and fills in the corresponding video data.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OHNativeWindow](../../../../../graphics/arkgraphics-2d/c-apis/structs/nativewindow/document.md) \*\*window | Pointer to the OHNativeWindow instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr.

 |

#### \[h2\]OH\_AVRecorder\_UpdateRotation()

OH\_AVErrCode OH\_AVRecorder\_UpdateRotation(OH\_AVRecorder \*recorder, int32\_t rotation)

**Description**

Updates the video rotation angle. This function must be called after [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) is successfully triggered and before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| int32\_t rotation | Video rotation angle. The value must be an integer in the range \[0, 90, 180, 270\]. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr, **rotation** is invalid, or the update operation fails.

 |

#### \[h2\]OH\_AVRecorder\_Start()

OH\_AVErrCode OH\_AVRecorder\_Start(OH\_AVRecorder \*recorder)

**Description**

Starts recording. This function must be called after [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) is successfully triggered. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_STARTED state.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr or recording fails to start.

 |

#### \[h2\]OH\_AVRecorder\_Pause()

OH\_AVErrCode OH\_AVRecorder\_Pause(OH\_AVRecorder \*recorder)

**Description**

Pauses recording. This function must be called after [OH\_AVRecorder\_Start](#oh_avrecorder_start) is successfully triggered and the AVRecorder is in the AVRECORDER\_STARTED state. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_PAUSED state.

Then, you can call [OH\_AVRecorder\_Resume](#oh_avrecorder_resume) to resume recording, and the AVRecorder transitions the AVRECORDER\_STARTED state again.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr or recording fails to pause.

 |

#### \[h2\]OH\_AVRecorder\_Resume()

OH\_AVErrCode OH\_AVRecorder\_Resume(OH\_AVRecorder \*recorder)

**Description**

Resumes recording. This function must be called after [OH\_AVRecorder\_Pause](#oh_avrecorder_pause) is successfully triggered and the AVRecorder is in the AVRECORDER\_PAUSED state. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_STARTED state.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr or recording fails to resume.

 |

#### \[h2\]OH\_AVRecorder\_Stop()

OH\_AVErrCode OH\_AVRecorder\_Stop(OH\_AVRecorder \*recorder)

**Description**

Stops recording. This function must be called after [OH\_AVRecorder\_Start](#oh_avrecorder_start) is successfully triggered. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_STOPPED state.

For audio-only recording, you can call [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) again for re-recording.

For video-only recording or audio and video recording, you can call [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) and [OH\_AVRecorder\_GetInputSurface](#oh_avrecorder_getinputsurface) again for re-recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr or recording fails to stop.

 |

#### \[h2\]OH\_AVRecorder\_Reset()

OH\_AVErrCode OH\_AVRecorder\_Reset(OH\_AVRecorder \*recorder)

**Description**

Resets the recording state. This function must be called when the AVRecorder is not in the AVRECORDER\_RELEASED state. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_IDLE state.

For audio-only recording, you can call [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) again for re-recording.

For video-only recording or audio and video recording, you can call [OH\_AVRecorder\_Prepare](#oh_avrecorder_prepare) and [OH\_AVRecorder\_GetInputSurface](#oh_avrecorder_getinputsurface) again for re-recording.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr or recording fails to reset.

 |

#### \[h2\]OH\_AVRecorder\_Release()

OH\_AVErrCode OH\_AVRecorder\_Release(OH\_AVRecorder \*recorder)

**Description**

Releases recording resources. After this function is successfully called, the AVRecorder transitions to the AVRECORDER\_RELEASED state.

The recorder memory will be released. The application layer must explicitly set the recorder to nullptr to avoid access to wild pointers. After the resources are released, you can no longer perform any operation on the OH\_AVRecorder instance.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr or recording fails to release.

 |

#### \[h2\]OH\_AVRecorder\_GetAvailableEncoder()

OH\_AVErrCode OH\_AVRecorder\_GetAvailableEncoder(OH\_AVRecorder \*recorder, OH\_AVRecorder\_EncoderInfo \*\*info,int32\_t \*length)

**Description**

Obtains the available encoders and encoder information of the AVRecorder.

**info** must be set to nullptr. The framework layer allocates and releases the memory in a unified manner to avoid issues with memory management, such as leaks or double freeing.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OH\_AVRecorder\_EncoderInfo](../../structs/oh-avrecorder-encoderinfo/document.md) \*\*info | Pointer to the OH\_AVRecorder\_EncoderInfo instance. |
| int32\_t \*length | Pointer to the number of available encoders. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** is nullptr.

**AV\_ERR\_NO\_MEMORY**: The memory fails to be allocated due to insufficient memory.

 |

#### \[h2\]OH\_AVRecorder\_SetStateCallback()

OH\_AVErrCode OH\_AVRecorder\_SetStateCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnStateChange callback, void \*userData)

**Description**

Sets a state callback so that the application can respond to state change events generated by the AVRecorder. This function must be called before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OH\_AVRecorder\_OnStateChange](../avrecorder-base-h/document.md#oh_avrecorder_onstatechange) callback | Status callback function. |
| void \*userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** or **callback** is nullptr.

 |

#### \[h2\]OH\_AVRecorder\_SetErrorCallback()

OH\_AVErrCode OH\_AVRecorder\_SetErrorCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnError callback, void \*userData)

**Description**

Sets an error callback so that the application can respond to error events generated by the AVRecorder. This function must be called before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OH\_AVRecorder\_OnError](../avrecorder-base-h/document.md#oh_avrecorder_onerror) callback | Error callback function. |
| void \*userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** or **callback** is nullptr.

 |

#### \[h2\]OH\_AVRecorder\_SetUriCallback()

OH\_AVErrCode OH\_AVRecorder\_SetUriCallback(OH\_AVRecorder \*recorder, OH\_AVRecorder\_OnUri callback, void \*userData)

**Description**

Sets a URI callback so that the application can respond to URI events generated by the AVRecorder. This function must be called before [OH\_AVRecorder\_Start](#oh_avrecorder_start) is called.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 18

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| [OH\_AVRecorder\_OnUri](../avrecorder-base-h/document.md#oh_avrecorder_onuri) callback | Callback used to return the result. |
| void \*userData | Pointer to user-defined data. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** or **callback** is nullptr.

 |

#### \[h2\]OH\_AVRecorder\_SetWillMuteWhenInterrupted()

OH\_AVErrCode OH\_AVRecorder\_SetWillMuteWhenInterrupted(OH\_AVRecorder \*recorder, bool muteWhenInterrupted)

**Description**

Sets whether to enable the mute interruption mode.

**System capability**: SystemCapability.Multimedia.Media.AVRecorder

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVRecorder](../../structs/oh-avrecorder/document.md) \*recorder | Pointer to the OH\_AVRecorder instance. |
| bool muteWhenInterrupted | Sets whether to enable the mute interruption mode. Setting it to **true** indicates that the application remains muted instead of being interrupted when recording is required. Setting it to false indicates that the application stops recording instead of remain muted when the recording is interrupted. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVErrCode](../../../../avcodec-kit/c-apis/header-files/native-averrors-h/document.md#oh_averrcode) | 
**AV\_ERR\_OK**: The operation is successful.

**AV\_ERR\_INVALID\_VAL**: The input parameter **recorder** or **callback** is nullptr.

**AV\_ERR\_INVALID\_STATE**: The function is called in an invalid state. It must be in the prepared state.

 |
