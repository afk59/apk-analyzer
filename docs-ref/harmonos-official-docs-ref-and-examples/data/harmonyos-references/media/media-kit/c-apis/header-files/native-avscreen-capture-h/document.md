# native\_avscreen\_capture.h

#### Overview

The file declares the APIs used to create an OH\_AVScreenCapture instance.

**File to include**: <multimedia/player\_framework/native\_avscreen\_capture.h>

**Library**: libnative\_avscreen\_capture.so

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture \*OH\_AVScreenCapture\_Create(void)](#oh_avscreencapture_create) | 
Creates an OH\_AVScreenCapture instance.

You can release the instance by calling [OH\_AVScreenCapture\_Release](#oh_avscreencapture_release).

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_Init(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureConfig config)](#oh_avscreencapture_init) | Initializes parameters related to an [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) instance, including audio sampling parameters for external capture using microphones (optional), audio sampling parameters for internal capture, and video resolution parameters. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenCapture(struct OH\_AVScreenCapture \*capture)](#oh_avscreencapture_startscreencapture) | Starts screen capture and collects original streams. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StopScreenCapture(struct OH\_AVScreenCapture \*capture)](#oh_avscreencapture_stopscreencapture) | Stops screen capture. This function is used in pair with [OH\_AVScreenCapture\_StartScreenCapture](#oh_avscreencapture_startscreencapture). After calling this function, the application stops screen capture or screen share and releases the microphone. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenRecording(struct OH\_AVScreenCapture \*capture)](#oh_avscreencapture_startscreenrecording) | Starts screen recording, with recordings saved in files. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StopScreenRecording(struct OH\_AVScreenCapture \*capture)](#oh_avscreencapture_stopscreenrecording) | Stops screen recording. This function is used in pair with [OH\_AVScreenCapture\_StartScreenRecording](#oh_avscreencapture_startscreenrecording). |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_AcquireAudioBuffer(struct OH\_AVScreenCapture \*capture, OH\_AudioBuffer \*\*audiobuffer, OH\_AudioCaptureSourceType type)](#oh_avscreencapture_acquireaudiobuffer) | 

Obtains an audio buffer. When calling this function, the application must allocate the memory of the corresponding struct size to the audio buffer.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

 |
| [OH\_NativeBuffer\* OH\_AVScreenCapture\_AcquireVideoBuffer(struct OH\_AVScreenCapture \*capture, int32\_t \*fence, int64\_t \*timestamp, struct OH\_Rect \*region)](#oh_avscreencapture_acquirevideobuffer) | 

Obtains a video buffer. The application can call this function to obtain information such as the video buffer and timestamp.

When a video buffer is no longer needed, call **OH\_AVScreenCapture\_ReleaseVideoBuffer** to release it.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseAudioBuffer(struct OH\_AVScreenCapture \*capture, OH\_AudioCaptureSourceType type)](#oh_avscreencapture_releaseaudiobuffer) | 

Releases an audio buffer. When an audio buffer is no longer needed, call this function to release it.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseVideoBuffer(struct OH\_AVScreenCapture \*capture)](#oh_avscreencapture_releasevideobuffer) | 

Releases a video buffer. When a video buffer is no longer needed, call this function to release it.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCallback(struct OH\_AVScreenCapture \*capture, struct OH\_AVScreenCaptureCallback callback)](#oh_avscreencapture_setcallback) | 

Sets a callback to listen for available video buffers and audio buffers and errors that occur during the function calling.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_SetErrorCallback](#oh_avscreencapture_seterrorcallback) and [OH\_AVScreenCapture\_SetDataCallback](#oh_avscreencapture_setdatacallback) instead.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_Release(struct OH\_AVScreenCapture \*capture)](#oh_avscreencapture_release) | Releases an OH\_AVScreenCapture instance. This function is used in pair with [OH\_AVScreenCapture\_Create](#oh_avscreencapture_create). |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetMicrophoneEnabled(struct OH\_AVScreenCapture \*capture, bool isMicrophone)](#oh_avscreencapture_setmicrophoneenabled) | 

Enables or disables the microphone.

When **isMicrophone** is set to **true**, the microphone is enabled, and the original PCM data of the microphone can be obtained by calling [OH\_AVScreenCapture\_StartScreenCapture](#oh_avscreencapture_startscreencapture) and [OH\_AVScreenCapture\_AcquireAudioBuffer](#oh_avscreencapture_acquireaudiobuffer). When **isMicrophone** is set to **false**, the obtained audio data is silent data.

By default, the microphone is enabled.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetStateCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnStateChange callback, void \*userData)](#oh_avscreencapture_setstatecallback) | Sets a state change callback. This function must be called before screen capture starts. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetDataCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnBufferAvailable callback, void \*userData)](#oh_avscreencapture_setdatacallback) | Sets a data processing callback. This function must be called before screen capture starts. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetErrorCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnError callback, void \*userData)](#oh_avscreencapture_seterrorcallback) | Sets an error processing callback. This function must be called before screen capture starts. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenCaptureWithSurface(struct OH\_AVScreenCapture \*capture, OHNativeWindow \*window)](#oh_avscreencapture_startscreencapturewithsurface) | Starts screen capture in surface mode. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCanvasRotation(struct OH\_AVScreenCapture \*capture, bool canvasRotation)](#oh_avscreencapture_setcanvasrotation) | 

Sets whether the captured screen data should rotate.

When **canvasRotation** is set to **true**, rotation is enabled and the captured screen data remains upright.

The default value is **false**.

 |
| [struct OH\_AVScreenCapture\_ContentFilter \*OH\_AVScreenCapture\_CreateContentFilter(void)](#oh_avscreencapture_createcontentfilter) | Creates a content filter. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseContentFilter(struct OH\_AVScreenCapture\_ContentFilter \*filter)](#oh_avscreencapture_releasecontentfilter) | Releases a content filter. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ContentFilter\_AddAudioContent(struct OH\_AVScreenCapture\_ContentFilter \*filter, OH\_AVScreenCaptureFilterableAudioContent content)](#oh_avscreencapture_contentfilter_addaudiocontent) | Adds audio content to a content filter. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ExcludeContent(struct OH\_AVScreenCapture \*capture, struct OH\_AVScreenCapture\_ContentFilter \*filter)](#oh_avscreencapture_excludecontent) | Sets a content filter for an OH\_AVScreenCapture instance. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ContentFilter\_AddWindowContent(struct OH\_AVScreenCapture\_ContentFilter \*filter, int32\_t \*windowIDs, int32\_t windowCount)](#oh_avscreencapture_contentfilter_addwindowcontent) | Adds a list of window IDs to a ContentFilter instance. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ResizeCanvas(struct OH\_AVScreenCapture \*capture, int32\_t width, int32\_t height)](#oh_avscreencapture_resizecanvas) | 

Adjusts the screen resolution.

This function is used to set the resolution of screen capture data. **width** indicates the screen width and **height** indicates the screen height.

Currently, this function supports only the scenario of capturing streams, but not the scenario of storing captured files. In addition, the caller of this function and the video data consumer must ensure that they support resolution changes of the received video data.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SkipPrivacyMode(struct OH\_AVScreenCapture \*capture, int32\_t \*windowIDs, int32\_t windowCount)](#oh_avscreencapture_skipprivacymode) | 

Exempts privacy windows during screen capture.

Currently, all the IDs of the subwindows and main windows to skip must be passed in.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetMaxVideoFrameRate(struct OH\_AVScreenCapture \*capture, int32\_t frameRate)](#oh_avscreencapture_setmaxvideoframerate) | 

Sets the maximum frame rate for screen capture.

This function must be called after screen capture starts.

The maximum frame rate that can be configured is subject to the device's limitations and is ultimately governed by the capabilities of the underlying system.

Although there is no limit on the maximum value of the input parameter, the maximum frame rate supported is 60 FPS. If the input parameter value exceeds 60 FPS, 60 FPS is used. If the value does not exceed the upper limit, the passed value is used.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ShowCursor(struct OH\_AVScreenCapture \*capture, bool showCursor)](#oh_avscreencapture_showcursor) | Sets whether to show the cursor. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetDisplayCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnDisplaySelected callback, void \*userData)](#oh_avscreencapture_setdisplaycallback) | Sets a callback function for obtaining the display ID. |
| [OH\_AVScreenCapture\_CaptureStrategy\* OH\_AVScreenCapture\_CreateCaptureStrategy(void)](#oh_avscreencapture_createcapturestrategy) | Creates a screen capture strategy. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseCaptureStrategy(OH\_AVScreenCapture\_CaptureStrategy\* strategy)](#oh_avscreencapture_releasecapturestrategy) | Releases a screen capture strategy. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureStrategy(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_CaptureStrategy \*strategy)](#oh_avscreencapture_setcapturestrategy) | 

Sets a screen capture strategy for an OH\_AVScreenCapture instance.

This function must be called before screen capture starts.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForCanvasFollowRotation(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)](#oh_avscreencapture_strategyforcanvasfollowrotation) | 

Sets the automatic rotation following configuration for screen capture. If the value is set to **true**, the screen capture follows the rotation, and the virtual screen size is automatically adjusted after a rotation to ensure the output image matches the new orientation.

After this setting, there is no need to manually call [OH\_AVScreenCapture\_ResizeCanvas](#oh_avscreencapture_resizecanvas) after rotation notifications.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForKeepCaptureDuringCall(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)](#oh_avscreencapture_strategyforkeepcaptureduringcall) | 

Sets whether to keep screen capture during a cellular call.

When **value** is set to **true** and screen capture is active during a cellular call, for privacy reasons, the voices of both parties (local microphone and remote speaker) are not captured. Other system sounds are captured normally. After the call ends, the screen capture framework resumes microphone recording. If the screen capture application is running in the background when the call ends, microphone recording fails to start because the audio module does not allow background applications to activate microphone recording.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureContentChangedCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnCaptureContentChanged callback, void \*userData)](#oh_avscreencapture_setcapturecontentchangedcallback) | Sets the callback for screen capture content changes. This function must be called before screen capture starts. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureArea(struct OH\_AVScreenCapture \*capture, uint64\_t displayId, OH\_Rect\* area)](#oh_avscreencapture_setcapturearea) | 

Sets or updates the capture area.

This function can be called before or after screen capture starts. The coordinates and dimensions provided must be non-negative, and the capture area must not span multiple screens. If setting the area fails, the previously set area is used for capturing.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForPrivacyMaskMode(OH\_AVScreenCapture\_CaptureStrategy \*strategy, int32\_t value)](#oh_avscreencapture_strategyforprivacymaskmode) | Sets the privacy window masking mode. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetSelectionCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnUserSelected callback, void \*userData)](#oh_avscreencapture_setselectioncallback) | Registers a callback to handle user selection results on the manual confirmation UI. This callback must be invoked before screen capture starts. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_GetCaptureTypeSelected(OH\_AVScreenCapture\_UserSelectionInfo \*selection, int32\_t\* type)](#oh_avscreencapture_getcapturetypeselected) | Obtains the screen capture object type selected by the user on the confirmation UI. This function is used in the [OH\_AVScreenCapture\_OnUserSelected](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onuserselected) callback. The **selection** pointer is destroyed after the callback is complete. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_GetDisplayIdSelected(OH\_AVScreenCapture\_UserSelectionInfo \*selection, uint64\_t\* displayId)](#oh_avscreencapture_getdisplayidselected) | Obtains the display ID of the screen selected by the user for capture. This function is used in the [OH\_AVScreenCapture\_OnUserSelected](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onuserselected) callback. The **selection** pointer is destroyed after the callback is complete. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForBFramesEncoding(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)](#oh_avscreencapture_strategyforbframesencoding) | 

Sets whether to enable B-frame encoding for a CaptureStrategy instance to reduce the size of the recorded file.

For details about the restrictions on B-frame video encoding, see [Constraints in B-Frame Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-b-frame#constraints). If the current environment does not meet the restrictions, B-frames will be skipped during screen capture, and no error will be returned.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForPickerPopUp(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)](#oh_avscreencapture_strategyforpickerpopup) | Sets whether to display the screen capture picker. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForFillMode(OH\_AVScreenCapture\_CaptureStrategy \*strategy, OH\_AVScreenCapture\_FillMode mode)](#oh_avscreencapture_strategyforfillmode) | Sets the fill mode of the captured image in the target region. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_PresentPicker(struct OH\_AVScreenCapture \*capture)](#oh_avscreencapture_presentpicker) | 

Displays the picker once more after the screen capture starts, allowing for dynamic updates to the recording source, such as changing the window or screen being captured. The ongoing capture process remains uninterrupted while updating the recording source.

Following the dynamic update of the recording source through the picker, the capture can proceed with the newly selected source.

 |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureAreaHighlight(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureHighlightConfig config)](#oh_avscreencapture_setcaptureareahighlight) | Sets the highlight style for the screen capture area. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetPickerMode(struct OH\_AVScreenCapture \*capture, OH\_CapturePickerMode pickerMode)](#oh_avscreencapture_setpickermode) | Sets the display mode of the picker. You can define the content type displayed in the picker. The mode change takes effect when [OH\_AVScreenCapture\_PresentPicker](#oh_avscreencapture_presentpicker) is called next time. |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ExcludePickerWindows(struct OH\_AVScreenCapture \*capture, const int32\_t \*excludedWindowIDs, uint32\_t windowCount)](#oh_avscreencapture_excludepickerwindows) | Hides the specified window in the picker. This function is called before the picker is displayed. It is to filter and hide a window. |

#### Function Description

#### \[h2\]OH\_AVScreenCapture\_Create()

struct OH\_AVScreenCapture \*OH\_AVScreenCapture\_Create(void)

**Description**

Creates an OH\_AVScreenCapture instance.

You can release the instance by calling [OH\_AVScreenCapture\_Release](#oh_avscreencapture_release).

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Returns**

| Type | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \* | Pointer to the OH\_AVScreenCapture instance. |

#### \[h2\]OH\_AVScreenCapture\_Init()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_Init(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureConfig config)

**Description**

Initializes parameters related to an [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) instance, including audio sampling parameters for external capture using microphones (optional), audio sampling parameters for internal capture, and video resolution parameters.

In the scenario where screen recording files are stored, the application must ensure that the video encoding parameters, video sampling parameters, audio encoding parameters, audio sampling parameters for internal capture, and audio sampling parameters for external capture using microphones (optional) are valid.

In the scenario where screen capture streams are generated, the application must ensure that either audio sampling parameters for internal capture or video sampling parameters are valid, or both are valid, and audio sampling parameters for external capture using microphones are valid (optional).

The members of the struct variables are not initialized during initialization. Therefore, the application must correctly set the parameters based on the use scenario. You are advised to set all memory bytes of the OH\_AVScreenCaptureConfig struct variables to **0**, and then set valid parameters based on the screen capture scenario.

If both **audioSampleRate** and **audioChannels** in the [OH\_AudioCaptureInfo](../../structs/oh-audiocaptureinfo/document.md) struct are **0**, the OH\_AVScreenCapture instance ignores the corresponding audio parameters and does not collect the audio data.

If both **videoFrameWidth** and **videoFrameHeight** in the [OH\_VideoCaptureInfo](../../structs/oh-videocaptureinfo/document.md) struct are **0**, the OH\_AVScreenCapture instance ignores the corresponding video parameters and does not collect the screen data.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCaptureConfig](../../structs/oh-avscreencaptureconfig/document.md) config | Parameters related to screen capture initialization. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The configuration fails to be initialized.

 |

#### \[h2\]OH\_AVScreenCapture\_StartScreenCapture()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenCapture(struct OH\_AVScreenCapture \*capture)

**Description**

Starts screen capture and collects original streams.

After this function is called, the callback [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) can be used to check whether streams are generated, and the callback [OH\_AVScreenCapture\_OnStateChange](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onstatechange) can be used to check the startup status.

The application can obtain the original streams of screen capture by calling [OH\_AVScreenCapture\_AcquireAudioBuffer](#oh_avscreencapture_acquireaudiobuffer) and [OH\_AVScreenCapture\_AcquireVideoBuffer](#oh_avscreencapture_acquirevideobuffer).

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT** (available since API version 20): The device does not support the operation.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The privacy permission fails to be enabled or screen capture fails to start.

 |

#### \[h2\]OH\_AVScreenCapture\_StopScreenCapture()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StopScreenCapture(struct OH\_AVScreenCapture \*capture)

**Description**

Stops screen capture. This function is used in pair with [OH\_AVScreenCapture\_StartScreenCapture](#oh_avscreencapture_startscreencapture). After calling this function, the application stops screen capture or screen share and releases the microphone.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. Screen capture fails to stop.

 |

#### \[h2\]OH\_AVScreenCapture\_StartScreenRecording()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenRecording(struct OH\_AVScreenCapture \*capture)

**Description**

Starts screen recording, with recordings saved in files.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT** (available since API version 20): The device does not support the operation.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The privacy permission fails to be enabled or screen capture fails to start.

 |

#### \[h2\]OH\_AVScreenCapture\_StopScreenRecording()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StopScreenRecording(struct OH\_AVScreenCapture \*capture)

**Description**

Stops screen recording. This function is used in pair with [OH\_AVScreenCapture\_StartScreenRecording](#oh_avscreencapture_startscreenrecording).

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. Screen capture fails to stop.

 |

#### \[h2\]OH\_AVScreenCapture\_AcquireAudioBuffer()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_AcquireAudioBuffer(struct OH\_AVScreenCapture \*capture, OH\_AudioBuffer \*\*audiobuffer, OH\_AudioCaptureSourceType type)

**Description**

Obtains an audio buffer. When calling this function, the application must allocate the memory of the corresponding struct size to the audio buffer.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AudioBuffer](../../structs/oh-audiobuffer/document.md) \*\*audiobuffer | Pointer to the struct for storing the audio buffer. This struct is used to obtain the information about the audio buffer and the timestamp of the buffer. |
| [OH\_AudioCaptureSourceType](../native-avscreen-capture-base-h/document.md#oh_audiocapturesourcetype) type | Type of the audio buffer, which is used to distinguish external streams recorded by the microphone from internal streams played by the system. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **audiobuffer** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY**: The audio buffer fails to be allocated due to insufficient memory.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The privacy permission fails to be enabled or the audio buffer fails to be obtained.

 |

#### \[h2\]OH\_AVScreenCapture\_AcquireVideoBuffer()

OH\_NativeBuffer\* OH\_AVScreenCapture\_AcquireVideoBuffer(struct OH\_AVScreenCapture \*capture, int32\_t \*fence, int64\_t \*timestamp, struct OH\_Rect \*region)

**Description**

Obtains a video buffer. The application can call this function to obtain information such as the video buffer and timestamp.

When a video buffer is no longer needed, call **OH\_AVScreenCapture\_ReleaseVideoBuffer** to release it.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| int32\_t \*fence | Pointer to parameters for synchronization display. |
| int64\_t \*timestamp | Pointer to the timestamp of the video frame. |
| [struct OH\_Rect](../../structs/oh-rect/document.md) \*region | Pointer to the coordinates related to video display. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md)\* | OH\_NativeBuffer object if the operation is successful. The application can call the APIs provided by the OH\_NativeBuffer object to obtain information such as the video buffer and resolution. |

#### \[h2\]OH\_AVScreenCapture\_ReleaseAudioBuffer()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseAudioBuffer(struct OH\_AVScreenCapture \*capture, OH\_AudioCaptureSourceType type)

**Description**

Releases an audio buffer. When an audio buffer is no longer needed, call this function to release it.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AudioCaptureSourceType](../native-avscreen-capture-base-h/document.md#oh_audiocapturesourcetype) type | Type of the audio buffer, which is used to distinguish external streams recorded by the microphone from internal streams played by the system. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The data callback has been set or the audio buffer fails to be released.

 |

#### \[h2\]OH\_AVScreenCapture\_ReleaseVideoBuffer()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseVideoBuffer(struct OH\_AVScreenCapture \*capture)

**Description**

Releases a video buffer. When a video buffer is no longer needed, call this function to release it.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) instead.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The data callback has been set or the video buffer fails to be released.

 |

#### \[h2\]OH\_AVScreenCapture\_SetCallback()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCallback(struct OH\_AVScreenCapture \*capture, struct OH\_AVScreenCaptureCallback callback)

**Description**

Sets a callback to listen for available video buffers and audio buffers and errors that occur during the function calling.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_SetErrorCallback](#oh_avscreencapture_seterrorcallback) and [OH\_AVScreenCapture\_SetDataCallback](#oh_avscreencapture_setdatacallback) instead.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [struct OH\_AVScreenCaptureCallback](../../structs/oh-avscreencapturecallback/document.md) callback | OH\_AVScreenCaptureCallback struct, which stores related callback function pointers. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **callback** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The callback fails to be set.

 |

#### \[h2\]OH\_AVScreenCapture\_Release()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_Release(struct OH\_AVScreenCapture \*capture)

**Description**

Releases an OH\_AVScreenCapture instance. This function is used in pair with [OH\_AVScreenCapture\_Create](#oh_avscreencapture_create).

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The OH\_AVScreenCapture instance fails to be released.

 |

#### \[h2\]OH\_AVScreenCapture\_SetMicrophoneEnabled()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetMicrophoneEnabled(struct OH\_AVScreenCapture \*capture, bool isMicrophone)

**Description**

Enables or disables the microphone.

When **isMicrophone** is set to **true**, the microphone is enabled, and the original PCM data of the microphone can be obtained by calling [OH\_AVScreenCapture\_StartScreenCapture](#oh_avscreencapture_startscreencapture) and [OH\_AVScreenCapture\_AcquireAudioBuffer](#oh_avscreencapture_acquireaudiobuffer). When **isMicrophone** is set to **false**, the obtained audio data is silent data.

By default, the microphone is enabled.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| bool isMicrophone | 
Whether to enable the microphone.

**true** to enable, **false** to disable.

The default value is **true**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The microphone fails to be enabled or disabled.

 |

#### \[h2\]OH\_AVScreenCapture\_SetStateCallback()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetStateCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnStateChange callback, void \*userData)

**Description**

Sets a state change callback. This function must be called before screen capture starts.

The callback is triggered when the state changes during the running of an OH\_AVScreenCapture instance.

A privacy dialog box is displayed to ask for user consent before screen capture starts. After a successful call to this function, the following scenarios are possible:

1.  If the user agrees, the screen capture startup process starts. If screen capture starts successfully, the state change callback is triggered to report the [OH\_AVScreenCaptureStateCode](../native-avscreen-capture-base-h/document.md#oh_avscreencapturestatecode).OH\_SCREEN\_CAPTURE\_STATE\_STARTED status to notify the application of the startup success, with a screen capture notification displayed. If screen capture fails to start, the state change callback is triggered to report the failure information (for example, [OH\_AVScreenCaptureStateCode](../native-avscreen-capture-base-h/document.md#oh_avscreencapturestatecode).OH\_SCREEN\_CAPTURE\_STATE\_MIC\_UNAVAILABLE if the microphone is unavailable), or the error processing callback [OH\_AVScreenCapture\_OnError](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onerror) is triggered to report the error information.
2.  If the user disagrees, the screen capture startup process stops. The state change callback is triggered to report the [OH\_AVScreenCaptureStateCode](../native-avscreen-capture-base-h/document.md#oh_avscreencapturestatecode).OH\_SCREEN\_CAPTURE\_STATE\_CANCELED status to notify the application of the startup failure due to user rejection.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCapture\_OnStateChange](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onstatechange) callback | State change callback. |
| void \*userData | Pointer to the user-defined data. The data is returned as an input parameter when the state change callback is triggered. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **callback** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY**: The memory fails to be allocated due to insufficient memory.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The state callback fails to be set.

 |

#### \[h2\]OH\_AVScreenCapture\_SetDataCallback()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetDataCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnBufferAvailable callback, void \*userData)

**Description**

Sets a data processing callback. This function must be called before screen capture starts.

The callback is triggered when an audio buffer or a video buffer becomes available during the running of an OH\_AVScreenCapture instance.

The application needs to process microphone audio, internal audio, and video data based on the data type in the callback. After the callback is triggered, the buffer is no longer valid.

A successful call to this function leads to the following scenarios:

1.  The callbacks [OH\_AVScreenCaptureOnAudioBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencaptureonaudiobufferavailable) and [OH\_AVScreenCaptureOnVideoBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencaptureonvideobufferavailable) set by calling [OH\_AVScreenCapture\_SetCallback](#oh_avscreencapture_setcallback) will no longer be triggered, even when an audio buffer or a video buffer becomes available.
2.  A failure message is returned for a call to any of the following functions: [OH\_AVScreenCapture\_AcquireAudioBuffer](#oh_avscreencapture_acquireaudiobuffer), [OH\_AVScreenCapture\_ReleaseAudioBuffer](#oh_avscreencapture_releaseaudiobuffer), [OH\_AVScreenCapture\_AcquireVideoBuffer](#oh_avscreencapture_acquirevideobuffer), and [OH\_AVScreenCapture\_ReleaseVideoBuffer](#oh_avscreencapture_releasevideobuffer).

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCapture\_OnBufferAvailable](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onbufferavailable) callback | Data processing callback. |
| void \*userData | Pointer to the user-defined data. The data is returned as an input parameter when the data processing callback is triggered. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **callback** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY**: The memory fails to be allocated due to insufficient memory.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The data callback fails to be set.

 |

#### \[h2\]OH\_AVScreenCapture\_SetErrorCallback()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetErrorCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnError callback, void \*userData)

**Description**

Sets an error processing callback. This function must be called before screen capture starts.

The callback is triggered when an error occurs during the running of an OH\_AVScreenCapture instance.

After a successful call to this function, the callback [OH\_AVScreenCaptureOnError](../native-avscreen-capture-base-h/document.md#oh_avscreencaptureonerror) set by calling [OH\_AVScreenCapture\_SetCallback](#oh_avscreencapture_setcallback) will no longer be triggered, even when an error occurs in the OH\_AVScreenCapture instance.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCapture\_OnError](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onerror) callback | Error processing callback. |
| void \*userData | Pointer to the user-defined data. The data is returned as an input parameter when the error processing callback is triggered. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **callback** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY**: The memory fails to be allocated due to insufficient memory.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The error callback fails to be set.

 |

#### \[h2\]OH\_AVScreenCapture\_StartScreenCaptureWithSurface()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StartScreenCaptureWithSurface(struct OH\_AVScreenCapture \*capture, OHNativeWindow \*window)

**Description**

Starts screen capture in surface mode.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OHNativeWindow](../../../../../graphics/arkgraphics-2d/c-apis/structs/nativewindow/document.md) \*window | Pointer to the OHNativeWindow instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture**, input parameter **window**, or **windowSurface** pointed to by **window** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT** (available since API version 20): The device does not support the operation.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The privacy permission fails to be enabled or screen capture with a surface fails to start.

 |

#### \[h2\]OH\_AVScreenCapture\_SetCanvasRotation()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCanvasRotation(struct OH\_AVScreenCapture \*capture, bool canvasRotation)

**Description**

Sets whether the captured screen data should rotate.

When **canvasRotation** is set to **true**, rotation is enabled and the captured screen data remains upright. The default value is **false**.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| bool canvasRotation | 
Whether to enable rotation for the captured screen data.

The value **true** means to enable rotation, keeping the screen data upright regardless of the device's orientation. The value **false** means to disable rotation, allowing the screen data to rotate along with the device's orientation.

The default value is **false**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT** (available since API version 20): The device does not support the operation.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. Canvas rotation fails to be set for screen capture.

 |

#### \[h2\]OH\_AVScreenCapture\_CreateContentFilter()

struct OH\_AVScreenCapture\_ContentFilter \*OH\_AVScreenCapture\_CreateContentFilter(void)

**Description**

Creates a content filter.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Returns**

| Type | Description |
| :-- | :-- |
| struct [OH\_AVScreenCapture\_ContentFilter](../../structs/oh-avscreencapture-contentfilter/document.md) \* | OH\_AVScreenCapture\_ContentFilter instance if the operation is successful; nullptr otherwise. |

#### \[h2\]OH\_AVScreenCapture\_ReleaseContentFilter()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseContentFilter(struct OH\_AVScreenCapture\_ContentFilter \*filter)

**Description**

Releases a content filter.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture\_ContentFilter](../../structs/oh-avscreencapture-contentfilter/document.md) \*filter | Pointer to the OH\_AVScreenCapture\_ContentFilter instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **filter** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_ContentFilter\_AddAudioContent()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ContentFilter\_AddAudioContent(struct OH\_AVScreenCapture\_ContentFilter \*filter, OH\_AVScreenCaptureFilterableAudioContent content)

**Description**

Adds audio content to a content filter.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture\_ContentFilter](../../structs/oh-avscreencapture-contentfilter/document.md) \*filter | Pointer to the OH\_AVScreenCapture\_ContentFilter instance. |
| [OH\_AVScreenCaptureFilterableAudioContent](../native-avscreen-capture-base-h/document.md#oh_avscreencapturefilterableaudiocontent) content | Pointer to the OH\_AVScreenCaptureFilterableAudioContent instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **filter** is nullptr or the input parameter **content** is invalid.

 |

#### \[h2\]OH\_AVScreenCapture\_ExcludeContent()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ExcludeContent(struct OH\_AVScreenCapture \*capture, struct OH\_AVScreenCapture\_ContentFilter \*filter)

**Description**

Sets a content filter for an OH\_AVScreenCapture instance.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [struct OH\_AVScreenCapture\_ContentFilter](../../structs/oh-avscreencapture-contentfilter/document.md) \*filter | Pointer to the OH\_AVScreenCapture\_ContentFilter instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **filter** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT**: The operation is not supported. For streams, the AudioCapturer API must be called for the operation to take effect during the start.

For captured files, the Recorder API must be called for the operation to take effect during the start.

 |

#### \[h2\]OH\_AVScreenCapture\_ContentFilter\_AddWindowContent()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ContentFilter\_AddWindowContent(struct OH\_AVScreenCapture\_ContentFilter \*filter, int32\_t \*windowIDs, int32\_t windowCount)

**Description**

Adds a list of window IDs to a ContentFilter instance.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture\_ContentFilter](../../structs/oh-avscreencapture-contentfilter/document.md) \*filter | Pointer to the OH\_AVScreenCapture\_ContentFilter instance. |
| int32\_t \*windowIDs | Pointer to the window IDs. |
| int32\_t windowCount | Length of the window ID list. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | **AV\_SCREEN\_CAPTURE\_ERR\_OK** if the operation is successful; a specific error code if the operation fails. |

#### \[h2\]OH\_AVScreenCapture\_ResizeCanvas()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ResizeCanvas(struct OH\_AVScreenCapture \*capture, int32\_t width, int32\_t height)

**Description**

Adjusts the screen resolution.

This function is used to set the resolution of screen capture data. **width** indicates the screen width and **height** indicates the screen height.

Currently, this function supports only the scenario of capturing streams, but not the scenario of storing captured files. In addition, the caller of this function and the video data consumer must ensure that they support resolution changes of the received video data.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| int32\_t width | Width of the screen to capture. |
| int32\_t height | Height of the screen to capture. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT** (available since API version 20): The device does not support the operation.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed.

 |

#### \[h2\]OH\_AVScreenCapture\_SkipPrivacyMode()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SkipPrivacyMode(struct OH\_AVScreenCapture \*capture, int32\_t \*windowIDs, int32\_t windowCount)

**Description**

Exempts privacy windows during screen capture.

Currently, all the IDs of the subwindows and main windows to skip must be passed in.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| int32\_t \*windowIDs | Pointer to the IDs of the privacy windows to skip. |
| int32\_t windowCount | Length of the privacy window ID list. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT** (available since API version 20): The device does not support the operation.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed.

 |

#### \[h2\]OH\_AVScreenCapture\_SetMaxVideoFrameRate()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetMaxVideoFrameRate(struct OH\_AVScreenCapture \*capture, int32\_t frameRate)

**Description**

Sets the maximum frame rate for screen capture.

This function must be called after screen capture starts.

The maximum frame rate that can be configured is subject to the device's limitations and is ultimately governed by the capabilities of the underlying system.

Although there is no limit on the maximum value of the input parameter, the maximum frame rate supported is 60 FPS. If the input parameter value exceeds 60 FPS, 60 FPS is used. If the value does not exceed the upper limit, the passed value is used.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 14

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| int32\_t frameRate | Maximum frame rate for screen capture. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr, or the input parameter **frameRate** is not supported.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT** (available since API version 20): The device does not support the operation.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed.

 |

#### \[h2\]OH\_AVScreenCapture\_ShowCursor()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ShowCursor(struct OH\_AVScreenCapture \*capture, bool showCursor)

**Description**

Sets whether to show the cursor.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| bool showCursor | 
Whether to show the cursor.

**true** to show, false to hide.

The default value is **true**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_UNSUPPORT** (available since API version 20): The device does not support the operation.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The cursor setting fails.

 |

#### \[h2\]OH\_AVScreenCapture\_SetDisplayCallback()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetDisplayCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnDisplaySelected callback, void \*userData)

**Description**

Sets a callback function for obtaining the display ID.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCapture\_OnDisplaySelected](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_ondisplayselected) callback | Callback function for returning the display ID. |
| void \*userData | Pointer to the user-defined data. The data is returned as an input parameter when the state change callback is triggered. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **callback** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_NO\_MEMORY**: The memory fails to be allocated due to insufficient memory.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_STATE**: The callback must be called before the **start** function.

 |

#### \[h2\]OH\_AVScreenCapture\_CreateCaptureStrategy()

OH\_AVScreenCapture\_CaptureStrategy\* OH\_AVScreenCapture\_CreateCaptureStrategy(void)

**Description**

Creates a screen capture strategy.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md)\* | OH\_AVScreenCapture\_CaptureStrategy instance if the operation is successful; nullptr otherwise. |

#### \[h2\]OH\_AVScreenCapture\_ReleaseCaptureStrategy()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ReleaseCaptureStrategy(OH\_AVScreenCapture\_CaptureStrategy\* strategy)

**Description**

Releases a screen capture strategy.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md)\* strategy | Pointer to the OH\_AVScreenCapture\_CaptureStrategy instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **strategy** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_SetCaptureStrategy()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureStrategy(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_CaptureStrategy \*strategy)

**Description**

Sets a screen capture strategy for an OH\_AVScreenCapture instance.

This function must be called before screen capture starts.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md) \*strategy | Pointer to the OH\_AVScreenCapture\_CaptureStrategy instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **strategy** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_STATE**: This function is called after screen capture starts.

 |

#### \[h2\]OH\_AVScreenCapture\_StrategyForCanvasFollowRotation()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForCanvasFollowRotation(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)

**Description**

Sets the automatic rotation following configuration for screen capture. If the value is set to **true**, the screen capture follows the rotation, and the virtual screen size is automatically adjusted after a rotation to ensure the output image matches the new orientation.

After this setting, there is no need to manually call [OH\_AVScreenCapture\_ResizeCanvas](#oh_avscreencapture_resizecanvas) after rotation notifications.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md) \*strategy | Pointer to the OH\_AVScreenCapture\_CaptureStrategy instance. |
| bool value | 
Whether the width and height of the virtual screen rotate with the screen.

**true** to rotate with the screen, **false** to keep the initial settings.

The default value is **false**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **strategy** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_StrategyForKeepCaptureDuringCall()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForKeepCaptureDuringCall(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)

**Description**

Sets whether to keep screen capture during a cellular call.

When **value** is set to **true** and screen capture is active during a cellular call, for privacy reasons, the voices of both parties (local microphone and remote speaker) are not captured. Other system sounds are captured normally. After the call ends, the screen capture framework resumes microphone recording. If the screen capture application is running in the background when the call ends, microphone recording fails to start because the audio module does not allow background applications to activate microphone recording.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md) \*strategy | Pointer to the OH\_AVScreenCapture\_CaptureStrategy instance. |
| bool value | 
Whether to keep screen capture during a cellular call.

**true** to keep, **false** otherwise.

The default value is **false**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **strategy** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_SetCaptureContentChangedCallback()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureContentChangedCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnCaptureContentChanged callback, void \*userData)

**Description**

Sets the callback for screen capture content changes. This function must be called before screen capture starts.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCapture\_OnCaptureContentChanged](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_oncapturecontentchanged) callback | Pointer to the callback method instance for the screen capture content change event. |
| void \*userData | Pointer to the user-defined data. The data is returned as an input parameter when the error processing callback is triggered. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** or **callback** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed. The screen capture callback fails to be set.

 |

#### \[h2\]OH\_AVScreenCapture\_SetCaptureArea()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureArea(struct OH\_AVScreenCapture \*capture, uint64\_t displayId, OH\_Rect\* area)

**Description**

Sets or updates the capture area.

This function can be called before or after screen capture starts. The coordinates and dimensions provided must be non-negative, and the capture area must not span multiple screens. If setting the area fails, the previously set area is used for capturing.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| uint64\_t displayId | ID of the screen to capture. |
| [OH\_Rect](../../structs/oh-rect/document.md)\* area | Area in the screen to capture. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is a nullptr, the input **displayId** does not exist, or the input **area** is abnormal.

 |

#### \[h2\]OH\_AVScreenCapture\_StrategyForPrivacyMaskMode()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForPrivacyMaskMode(OH\_AVScreenCapture\_CaptureStrategy \*strategy, int32\_t value)

**Description**

Sets the privacy window masking mode.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md) \*strategy | Pointer to the OH\_AVScreenCapture\_CaptureStrategy instance. |
| int32\_t value | 
If this parameter is set to **0**, the full-screen masking mode is used when there is a privacy window.

If this parameter is set to **1**, the privacy window masking mode is used when there is a privacy window. Any other value will result in an error.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **strategy** is nullptr or **value** is invalid.

 |

#### \[h2\]OH\_AVScreenCapture\_SetSelectionCallback()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetSelectionCallback(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCapture\_OnUserSelected callback, void \*userData)

**Description**

Registers a callback to handle user selection results on the manual confirmation UI. This callback must be invoked before screen capture starts.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCapture\_OnUserSelected](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onuserselected) callback | Callback used to instruct the application to carry out the relevant logic processing once the user has confirmed on the UI. |
| void \*userData | Pointer to application-specific data, returned to the application. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_GetCaptureTypeSelected()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_GetCaptureTypeSelected(OH\_AVScreenCapture\_UserSelectionInfo \*selection, int32\_t\* type)

**Description**

Obtains the screen capture object type selected by the user on the confirmation UI. This function is used in the [OH\_AVScreenCapture\_OnUserSelected](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onuserselected) callback. The **selection** pointer is destroyed after the callback is complete.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_UserSelectionInfo](../../structs/oh-avscreencapture-userselectioninfo/document.md) \*selection | Pointer to the OH\_AVScreenCapture\_UserSelectionInfo instance. |
| int32\_t\* type | Pointer to the type of the capture object selected by the user. The value **0** means a screen, and **1** means a window. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **selection** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_GetDisplayIdSelected()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_GetDisplayIdSelected(OH\_AVScreenCapture\_UserSelectionInfo \*selection, uint64\_t\* displayId)

**Description**

Obtains the display ID of the screen selected by the user for capture. This function is used in the [OH\_AVScreenCapture\_OnUserSelected](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_onuserselected) callback. The **selection** pointer is destroyed after the callback is complete.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_UserSelectionInfo](../../structs/oh-avscreencapture-userselectioninfo/document.md) \*selection | Pointer to the OH\_AVScreenCapture\_UserSelectionInfo instance. |
| uint64\_t\* displayId | Pointer to the ID of the screen selected by the user. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **selection** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_StrategyForBFramesEncoding()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForBFramesEncoding(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)

**Description**

Sets whether to enable B-frame encoding for a CaptureStrategy instance to reduce the size of the recorded file.

For details about the restrictions on B-frame video encoding, see [Constraints in B-Frame Video Encoding](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/video-encoding-b-frame#constraints). If the current environment does not meet the restrictions, B-frames will be skipped during screen capture, and no error will be returned.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md) \*strategy | Pointer to the OH\_AVScreenCapture\_CaptureStrategy instance. |
| bool value | 
Whether to enable B-frame encoding for the recorded file.

**true** to enable, **false** otherwise.

The default value is **false**.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **strategy** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_StrategyForPickerPopUp()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForPickerPopUp(OH\_AVScreenCapture\_CaptureStrategy \*strategy, bool value)

**Description**

Sets whether to display the screen capture picker.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md) \*strategy | Pointer to the OH\_AVScreenCapture\_CaptureStrategy instance. |
| bool value | If this parameter is set to **false**, the application has specified the content to capture, and the picker is not displayed after screen capture starts. If this parameter is set to **true**, the picker is displayed after screen capture starts. If this parameter is not set, the system's recommended behavior is used. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **strategy** is nullptr or **value** is invalid.

 |

#### \[h2\]OH\_AVScreenCapture\_StrategyForFillMode()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_StrategyForFillMode(OH\_AVScreenCapture\_CaptureStrategy \*strategy, OH\_AVScreenCapture\_FillMode mode)

**Description**

Sets the fill mode of the captured image in the target region.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md) \*strategy | Pointer to the OH\_AVScreenCapture\_CaptureStrategy instance. |
| [OH\_AVScreenCapture\_FillMode](../native-avscreen-capture-base-h/document.md#oh_avscreencapture_fillmode) mode | Fill mode of the captured image. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **strategy** is nullptr.

 |

#### \[h2\]OH\_AVScreenCapture\_PresentPicker()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_PresentPicker(struct OH\_AVScreenCapture \*capture)

**Description**

Displays the picker once more after the screen capture starts, allowing for dynamic updates to the recording source, such as changing the window or screen being captured. The ongoing capture process remains uninterrupted while updating the recording source.

Following the dynamic update of the recording source through the picker, the capture can proceed with the newly selected source.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed.

 |

#### \[h2\]OH\_AVScreenCapture\_SetCaptureAreaHighlight()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetCaptureAreaHighlight(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureHighlightConfig config)

**Description**

Sets the highlight style for the screen capture area.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCaptureHighlightConfig](../../structs/oh-avscreencapturehighlightconfig/document.md) config | Highlight parameters for the screen capture area. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr or **config** is invalid.

 |

#### \[h2\]OH\_AVScreenCapture\_SetPickerMode()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_SetPickerMode(struct OH\_AVScreenCapture \*capture, OH\_CapturePickerMode pickerMode)

**Description**

Sets the display mode of the picker. You can define the content type displayed in the picker. The mode change takes effect when [OH\_AVScreenCapture\_PresentPicker](#oh_avscreencapture_presentpicker) is called next time.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_CapturePickerMode](../native-avscreen-capture-base-h/document.md#oh_capturepickermode) pickerMode | Display mode of the picker. For details, see **OH\_CapturePickerMode**. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr or **pickerMode** is invalid.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed.

 |

#### \[h2\]OH\_AVScreenCapture\_ExcludePickerWindows()

OH\_AVSCREEN\_CAPTURE\_ErrCode OH\_AVScreenCapture\_ExcludePickerWindows(struct OH\_AVScreenCapture \*capture, const int32\_t \*excludedWindowIDs, uint32\_t windowCount)

**Description**

Hides the specified window in the picker. This function is called before the picker is displayed. It is to filter and hide a window.

**Since**: 22

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [struct OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| const int32\_t \*excludedWindowIDs | Array of IDs of the windows to be hidden (existing windows). |
| uint32\_t windowCount | Size of the array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AVSCREEN\_CAPTURE\_ErrCode](../native-avscreen-capture-errors-h/document.md#oh_avscreen_capture_errcode) | 
**AV\_SCREEN\_CAPTURE\_ERR\_OK**: The operation is successful.

**AV\_SCREEN\_CAPTURE\_ERR\_INVALID\_VAL**: The input parameter **capture** is nullptr or **excludedWindowIDs** is invalid.

**AV\_SCREEN\_CAPTURE\_ERR\_OPERATE\_NOT\_PERMIT**: The operation is not allowed.

 |
