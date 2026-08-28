# native\_avscreen\_capture\_base.h

#### Overview

The file declares the common structs, character constants, and enums used for running screen capture.

**File to include**: <multimedia/player\_framework/native\_avscreen\_capture\_base.h>

**Library**: libnative\_avscreen\_capture.so

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Related module**: [AVScreenCapture](../../modules/avscreencapture/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioCaptureInfo](../../structs/oh-audiocaptureinfo/document.md) | OH\_AudioCaptureInfo | 
Describes the audio capture information.

When both **audioSampleRate** and **audioChannels** are **0**, the audio-related parameters are ignored and the audio data is not recorded.

 |
| [OH\_AudioEncInfo](../../structs/oh-audioencinfo/document.md) | OH\_AudioEncInfo | Describes the audio encoding information. |
| [OH\_AudioInfo](../../structs/oh-audioinfo/document.md) | OH\_AudioInfo | 

Describes the audio information.

To perform both external capture (using microphones) and internal capture, **audioSampleRate** and **audioChannels** must be the same for both audio channels.

 |
| [OH\_VideoCaptureInfo](../../structs/oh-videocaptureinfo/document.md) | OH\_VideoCaptureInfo | Describes the video capture information. When **videoFrameWidth** and **videoFrameHeight** are both **0**, video-related parameters are ignored and screen data is not recorded. |
| [OH\_VideoEncInfo](../../structs/oh-videoencinfo/document.md) | OH\_VideoEncInfo | Describes the video encoding information. |
| [OH\_VideoInfo](../../structs/oh-videoinfo/document.md) | OH\_VideoInfo | Describes the video information. |
| [OH\_RecorderInfo](../../structs/oh-recorderinfo/document.md) | OH\_RecorderInfo | Describes the recording file information. |
| [OH\_AVScreenCaptureConfig](../../structs/oh-avscreencaptureconfig/document.md) | OH\_AVScreenCaptureConfig | Describes the screen capture configuration. |
| [OH\_AVScreenCaptureCallback](../../structs/oh-avscreencapturecallback/document.md) | OH\_AVScreenCaptureCallback | 

Defines all the asynchronous callback function pointers of an OH\_AVScreenCapture instance. To ensure the normal running of OH\_AVScreenCapture, you must register the instance of this struct with the OH\_AVScreenCapture instance and process the information reported by the callback functions.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnError](#oh_avscreencapture_onerror) and [OH\_AVScreenCapture\_OnBufferAvailable](#oh_avscreencapture_onbufferavailable) instead.

 |
| [OH\_Rect](../../structs/oh-rect/document.md) | OH\_Rect | Describes the width, height, and image information of the rectangle used for screen capture. |
| [OH\_AudioBuffer](../../structs/oh-audiobuffer/document.md) | OH\_AudioBuffer | Describes the configuration such as the size, type, and timestamp of audio data. |
| [OH\_AVScreenCaptureHighlightConfig](../../structs/oh-avscreencapturehighlightconfig/document.md) | OH\_AVScreenCaptureHighlightConfig | Describes the style of the highlight border shown during screen capture, including its shape, thickness, and color. |
| [OH\_NativeBuffer](../../structs/oh-nativebuffer/document.md) | OH\_NativeBuffer | Describes the native video stream class for screen capture. |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) | OH\_AVScreenCapture | Describes a screen capture instance used to obtain original video and audio streams. |
| [OH\_AVScreenCapture\_ContentFilter](../../structs/oh-avscreencapture-contentfilter/document.md) | OH\_AVScreenCapture\_ContentFilter | Describes the filter used to filter audio and video content. |
| [OH\_AVScreenCapture\_CaptureStrategy](../../structs/oh-avscreencapture-capturestrategy/document.md) | OH\_AVScreenCapture\_CaptureStrategy | Describes the screen capture strategy configured by using OH\_AVScreenCapture\_CaptureStrategy. |
| [OH\_AVScreenCapture\_UserSelectionInfo](../../structs/oh-avscreencapture-userselectioninfo/document.md) | OH\_AVScreenCapture\_UserSelectionInfo | Describes the parameters selected by the user on the authorization UI (selection UI) by using OH\_AVScreenCapture\_UserSelectionInfo. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_CaptureMode](#oh_capturemode) | OH\_CaptureMode | Enumerates the screen capture modes. |
| [OH\_AudioCaptureSourceType](#oh_audiocapturesourcetype) | OH\_AudioCaptureSourceType | Enumerates the audio source types during screen capture. |
| [OH\_AudioCodecFormat](#oh_audiocodecformat) | OH\_AudioCodecFormat | Enumerates the audio encoding formats. |
| [OH\_VideoCodecFormat](#oh_videocodecformat) | OH\_VideoCodecFormat | Enumerates the video encoding formats. |
| [OH\_DataType](#oh_datatype) | OH\_DataType | Enumerates the data types of screen capture streams. |
| [OH\_VideoSourceType](#oh_videosourcetype) | OH\_VideoSourceType | Enumerates the video source formats. Currently, only the RGBA format is supported. |
| [OH\_ContainerFormatType](#oh_containerformattype) | OH\_ContainerFormatType | Enumerates the types of files generated during screen capture. |
| [OH\_AVScreenCaptureStateCode](#oh_avscreencapturestatecode) | OH\_AVScreenCaptureStateCode | Enumerates the screen capture states. |
| [OH\_AVScreenCaptureBufferType](#oh_avscreencapturebuffertype) | OH\_AVScreenCaptureBufferType | Enumerates the buffer types. |
| [OH\_AVScreenCaptureFilterableAudioContent](#oh_avscreencapturefilterableaudiocontent) | OH\_AVScreenCaptureFilterableAudioContent | Enumerates the types of audio that can be added to a content filter. |
| [OH\_AVScreenCaptureContentChangedEvent](#oh_avscreencapturecontentchangedevent) | OH\_AVScreenCaptureContentChangedEvent | Enumerates the screen capture content change events. |
| [OH\_AVScreenCapture\_FillMode](#oh_avscreencapture_fillmode) | OH\_AVScreenCapture\_FillMode | Enumerates the image fill modes. |
| [OH\_ScreenCaptureHighlightMode](#oh_screencapturehighlightmode) | OH\_ScreenCaptureHighlightMode | Enumerates the shapes of the highlight border shown during screen capture. |
| [OH\_CapturePickerMode](#oh_capturepickermode) | OH\_CapturePickerMode | Enumerates the display modes of the picker. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*OH\_AVScreenCaptureOnError)(OH\_AVScreenCapture \*capture, int32\_t errorCode)](#oh_avscreencaptureonerror) | OH\_AVScreenCaptureOnError | 
Called when an error occurs during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnError](#oh_avscreencapture_onerror) instead.

 |
| [typedef void (\*OH\_AVScreenCaptureOnAudioBufferAvailable)(OH\_AVScreenCapture \*capture, bool isReady, OH\_AudioCaptureSourceType type)](#oh_avscreencaptureonaudiobufferavailable) | OH\_AVScreenCaptureOnAudioBufferAvailable | 

Called when an audio buffer is available during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](#oh_avscreencapture_onbufferavailable) instead.

 |
| [typedef void (\*OH\_AVScreenCaptureOnVideoBufferAvailable)(OH\_AVScreenCapture \*capture, bool isReady)](#oh_avscreencaptureonvideobufferavailable) | OH\_AVScreenCaptureOnVideoBufferAvailable | 

Called when a video buffer is available during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](#oh_avscreencapture_onbufferavailable) instead.

 |
| [typedef void (\*OH\_AVScreenCapture\_OnStateChange)(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureStateCode stateCode, void \*userData)](#oh_avscreencapture_onstatechange) | OH\_AVScreenCapture\_OnStateChange | Called when the state changes during the running of an OH\_AVScreenCapture instance. |
| [typedef void (\*OH\_AVScreenCapture\_OnError)(OH\_AVScreenCapture \*capture, int32\_t errorCode, void \*userData)](#oh_avscreencapture_onerror) | OH\_AVScreenCapture\_OnError | Called when an error occurs during the running of an OH\_AVScreenCapture instance. |
| [typedef void (\*OH\_AVScreenCapture\_OnBufferAvailable)(OH\_AVScreenCapture \*capture, OH\_AVBuffer \*buffer, OH\_AVScreenCaptureBufferType bufferType, int64\_t timestamp, void \*userData)](#oh_avscreencapture_onbufferavailable) | OH\_AVScreenCapture\_OnBufferAvailable | Called when an audio buffer or a video buffer is available during the running of an OH\_AVScreenCapture instance. |
| [typedef void (\*OH\_AVScreenCapture\_OnDisplaySelected)(OH\_AVScreenCapture \*capture, uint64\_t displayId, void \*userData)](#oh_avscreencapture_ondisplayselected) | OH\_AVScreenCapture\_OnDisplaySelected | Called when screen capture starts. |
| [typedef void (\*OH\_AVScreenCapture\_OnCaptureContentChanged)(OH\_AVScreenCapture\* capture, OH\_AVScreenCaptureContentChangedEvent event, OH\_Rect\* area, void \*userData)](#oh_avscreencapture_oncapturecontentchanged) | OH\_AVScreenCapture\_OnCaptureContentChanged | Called when the screen capture content changes during the running of an OH\_AVScreenCapture instance. |
| [typedef void (\*OH\_AVScreenCapture\_OnUserSelected)(OH\_AVScreenCapture\* capture, OH\_AVScreenCapture\_UserSelectionInfo\* selections, void \*userData)](#oh_avscreencapture_onuserselected) | OH\_AVScreenCapture\_OnUserSelected | Called to return the parameters selected by the user on the authorization UI to the application. |

#### Enum Description

#### \[h2\]OH\_CaptureMode

enum OH\_CaptureMode

**Description**

Enumerates the screen capture modes.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_CAPTURE\_HOME\_SCREEN = 0 | Captures the home screen. |
| OH\_CAPTURE\_SPECIFIED\_SCREEN = 1 | Captures a specified screen. |
| OH\_CAPTURE\_SPECIFIED\_WINDOW = 2 | Captures a specified window. |
| OH\_CAPTURE\_INVAILD = -1 | Invalid mode. |

#### \[h2\]OH\_AudioCaptureSourceType

enum OH\_AudioCaptureSourceType

**Description**

Enumerates the audio source types during screen capture.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_SOURCE\_INVALID = -1 | Invalid audio source. |
| OH\_SOURCE\_DEFAULT = 0 | Default audio source. The default value is **OH\_MIC**. |
| OH\_MIC = 1 | External audio streams recorded by the microphone. |
| OH\_ALL\_PLAYBACK = 2 | All internal audio streams played by the system. |
| OH\_APP\_PLAYBACK = 3 | Internal audio streams played by a specified application. |

#### \[h2\]OH\_AudioCodecFormat

enum OH\_AudioCodecFormat

**Description**

Enumerates the audio encoding formats.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_AUDIO\_DEFAULT = 0 | Default audio encoding format. The default value is **AAC\_LC**. |
| OH\_AAC\_LC = 3 | AAC\_LC audio encoding. |
| OH\_AUDIO\_CODEC\_FORMAT\_BUTT | Invalid format. |

#### \[h2\]OH\_VideoCodecFormat

enum OH\_VideoCodecFormat

**Description**

Enumerates the video encoding formats.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_VIDEO\_DEFAULT = 0 | Default video encoding format. The default value is **H.264**. |
| OH\_H264 = 2 | H.264. |
| OH\_H265 = 4 | H.265/HEVC. |
| OH\_MPEG4 = 6 | MPEG4. |
| OH\_VP8 = 8 | VP8. |
| OH\_VP9 = 10 | VP9. |
| OH\_VIDEO\_CODEC\_FORMAT\_BUTT | Invalid format. |

#### \[h2\]OH\_DataType

enum OH\_DataType

**Description**

Enumerates the data types of screen capture streams.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_ORIGINAL\_STREAM = 0 | Original stream format, such as YUV, RGBA, and PCM. |
| OH\_ENCODED\_STREAM = 1 | Encoded stream format, such as H.264 and AAC. This value is not supported yet. |
| OH\_CAPTURE\_FILE = 2 | Format of the recording file. The value can be **mp4**. |
| OH\_INVAILD = -1 | Invalid format. |

#### \[h2\]OH\_VideoSourceType

enum OH\_VideoSourceType

**Description**

Enumerates the video source formats. Currently, only the RGBA format is supported.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_VIDEO\_SOURCE\_SURFACE\_YUV = 0 | YUV format. This value is not supported yet. |
| OH\_VIDEO\_SOURCE\_SURFACE\_ES | Raw format. This value is not supported yet. |
| OH\_VIDEO\_SOURCE\_SURFACE\_RGBA | RGBA format. |
| OH\_VIDEO\_SOURCE\_BUTT | Invalid format. |

#### \[h2\]OH\_ContainerFormatType

enum OH\_ContainerFormatType

**Description**

Enumerates the types of files generated during screen capture.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| CFT\_MPEG\_4A = 0 | Audio format M4A. |
| CFT\_MPEG\_4 = 1 | Video format MP4. |

#### \[h2\]OH\_AVScreenCaptureStateCode

enum OH\_AVScreenCaptureStateCode

**Description**

Enumerates the screen capture states.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| OH\_SCREEN\_CAPTURE\_STATE\_STARTED = 0 | Screen capture is started. |
| OH\_SCREEN\_CAPTURE\_STATE\_CANCELED = 1 | Screen capture is canceled. |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER = 2 | Screen capture is stopped. |
| OH\_SCREEN\_CAPTURE\_STATE\_INTERRUPTED\_BY\_OTHER = 3 | Screen capture is interrupted by another screen capture. |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_CALL = 4 | Screen capture is interrupted by a call. |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_UNAVAILABLE = 5 | The microphone is unavailable. |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_MUTED\_BY\_USER = 6 | The microphone is muted. |
| OH\_SCREEN\_CAPTURE\_STATE\_MIC\_UNMUTED\_BY\_USER = 7 | The microphone is unmuted. |
| OH\_SCREEN\_CAPTURE\_STATE\_ENTER\_PRIVATE\_SCENE = 8 | The system enters a privacy screen. |
| OH\_SCREEN\_CAPTURE\_STATE\_EXIT\_PRIVATE\_SCENE = 9 | The system exits a privacy screen. |
| OH\_SCREEN\_CAPTURE\_STATE\_STOPPED\_BY\_USER\_SWITCHES = 10 | Screen capture is interrupted by system user switching. |

#### \[h2\]OH\_AVScreenCaptureBufferType

enum OH\_AVScreenCaptureBufferType

**Description**

Enumerates the buffer types.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_VIDEO = 0 | Video data. |
| OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_AUDIO\_INNER = 1 | Internal audio capture data. |
| OH\_SCREEN\_CAPTURE\_BUFFERTYPE\_AUDIO\_MIC = 2 | Microphone audio data. |

#### \[h2\]OH\_AVScreenCaptureFilterableAudioContent

enum OH\_AVScreenCaptureFilterableAudioContent

**Description**

Enumerates the types of audio that can be added to a content filter.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

| Enum Item | Description |
| :-- | :-- |
| OH\_SCREEN\_CAPTURE\_NOTIFICATION\_AUDIO = 0 | Notification tone. |
| OH\_SCREEN\_CAPTURE\_CURRENT\_APP\_AUDIO = 1 | Sound of the application itself. |

#### \[h2\]OH\_AVScreenCaptureContentChangedEvent

enum OH\_AVScreenCaptureContentChangedEvent

**Description**

Enumerates the screen capture content change events.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| OH\_SCREEN\_CAPTURE\_CONTENT\_HIDE = 0 | The screen capture content is hidden. |
| OH\_SCREEN\_CAPTURE\_CONTENT\_VISIBLE = 1 | The screen capture content is visible. |
| OH\_SCREEN\_CAPTURE\_CONTENT\_UNAVAILABLE = 2 | The screen capture content becomes unavailable. For example, the screen capture window is closed. |

#### \[h2\]OH\_AVScreenCapture\_FillMode

enum OH\_AVScreenCapture\_FillMode

**Description**

Enumerates the image fill modes.

**Since**: 20

| Enum Item | Description |
| :-- | :-- |
| OH\_SCREENCAPTURE\_FILLMODE\_ASPECT\_SCALE\_FIT = 0 | Keeps the original aspect ratio of the image to fit the target size. Black bars may appear if the aspect ratios differ. |
| OH\_SCREENCAPTURE\_FILLMODE\_SCALE\_TO\_FILL = 1 | Stretches the image to fill the target size. The image may stretch and distort if the aspect ratios differ. |

#### \[h2\]OH\_ScreenCaptureHighlightMode

enum OH\_ScreenCaptureHighlightMode

**Description**

Enumerates the display modes of the highlight border shown during screen capture.

**Since**: 22

| Enum Item | Description |
| :-- | :-- |
| OH\_HIGHLIGHT\_MODE\_CLOSED = 0 | Highlights the capture area with a full square border. This is the default mode. |
| OH\_HIGHLIGHT\_MODE\_CORNER\_WRAP = 1 | Highlights the capture area with a corner-wrapping border. |

#### \[h2\]OH\_CapturePickerMode

enum OH\_CapturePickerMode

**Description**

Enumerates the display modes of the picker.

**Since**: 22

| Enum Item | Description |
| :-- | :-- |
| OH\_CAPTURE\_PICKER\_MODE\_WINDOW\_ONLY = 0 | Displays only a list of windows. |
| OH\_CAPTURE\_PICKER\_MODE\_SCREEN\_ONLY = 1 | Displays only a list of screens. |
| OH\_CAPTURE\_PICKER\_MODE\_SCREEN\_AND\_WINDOW = 2 | Displays both screens and windows. This is the default mode. |

#### Function Description

#### \[h2\]OH\_AVScreenCaptureOnError()

typedef void (\*OH\_AVScreenCaptureOnError)(OH\_AVScreenCapture \*capture, int32\_t errorCode)

**Description**

Called when an error occurs during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnError](#oh_avscreencapture_onerror) instead.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| int32\_t errorCode | Error code. |

#### \[h2\]OH\_AVScreenCaptureOnAudioBufferAvailable()

typedef void (\*OH\_AVScreenCaptureOnAudioBufferAvailable)(OH\_AVScreenCapture \*capture, bool isReady, OH\_AudioCaptureSourceType type)

**Description**

Called when an audio buffer is available during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](#oh_avscreencapture_onbufferavailable) instead.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| bool isReady | Whether the audio buffer is available. The values include **true** (yes) and **false** (no). |
| [OH\_AudioCaptureSourceType](#oh_audiocapturesourcetype) type | Audio source type. |

#### \[h2\]OH\_AVScreenCaptureOnVideoBufferAvailable()

typedef void (\*OH\_AVScreenCaptureOnVideoBufferAvailable)(OH\_AVScreenCapture \*capture, bool isReady)

**Description**

Called when a video buffer is available during the running of an OH\_AVScreenCapture instance.

Starting from API version 12, you are advised to use [OH\_AVScreenCapture\_OnBufferAvailable](#oh_avscreencapture_onbufferavailable) instead.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 10

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| bool isReady | Whether the video buffer is available. The values include **true** (yes) and **false** (no). |

#### \[h2\]OH\_AVScreenCapture\_OnStateChange()

typedef void (\*OH\_AVScreenCapture\_OnStateChange)(struct OH\_AVScreenCapture \*capture, OH\_AVScreenCaptureStateCode stateCode, void \*userData)

**Description**

Called when the state changes during the running of an OH\_AVScreenCapture instance.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| struct [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCaptureStateCode](#oh_avscreencapturestatecode) stateCode | Status code. |
| void \*userData | Pointer to the user-defined data carried in the function. |

#### \[h2\]OH\_AVScreenCapture\_OnError()

typedef void (\*OH\_AVScreenCapture\_OnError)(OH\_AVScreenCapture \*capture, int32\_t errorCode, void \*userData)

**Description**

Called when an error occurs during the running of an OH\_AVScreenCapture instance.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| int32\_t errorCode | Error code. |
| void \*userData | Pointer to the user-defined data carried in the function. |

#### \[h2\]OH\_AVScreenCapture\_OnBufferAvailable()

typedef void (\*OH\_AVScreenCapture\_OnBufferAvailable)(OH\_AVScreenCapture \*capture, OH\_AVBuffer \*buffer, OH\_AVScreenCaptureBufferType bufferType, int64\_t timestamp, void \*userData)

**Description**

Called when an audio buffer or a video buffer is available during the running of an OH\_AVScreenCapture instance.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 12

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVBuffer](../../../../avcodec-kit/c-apis/structs/oh-avbuffer/document.md) \*buffer | Pointer to the OH\_AVBuffer instance. After the callback is triggered, the buffer is no longer valid. |
| [OH\_AVScreenCaptureBufferType](#oh_avscreencapturebuffertype) bufferType | Type of the buffer. |
| int64\_t timestamp | Timestamp, in nanoseconds. |
| void \*userData | Pointer to the user-defined data carried in the function. |

#### \[h2\]OH\_AVScreenCapture\_OnDisplaySelected()

typedef void (\*OH\_AVScreenCapture\_OnDisplaySelected)(OH\_AVScreenCapture \*capture, uint64\_t displayId, void \*userData)

**Description**

Called when screen capture starts.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 15

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md) \*capture | Pointer to the OH\_AVScreenCapture instance. |
| uint64\_t displayId | ID of the screen to capture. |
| void \*userData | Pointer to the user-defined data carried in the function. |

#### \[h2\]OH\_AVScreenCapture\_OnCaptureContentChanged()

typedef void (\*OH\_AVScreenCapture\_OnCaptureContentChanged)(OH\_AVScreenCapture\* capture, OH\_AVScreenCaptureContentChangedEvent event, OH\_Rect\* area, void \*userData)

**Description**

Called when the screen capture content changes during the running of an OH\_AVScreenCapture instance.

**System capability**: SystemCapability.Multimedia.Media.AVScreenCapture

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md)\* capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCaptureContentChangedEvent](#oh_avscreencapturecontentchangedevent) event | Screen capture content change event. |
| [OH\_Rect](../../structs/oh-rect/document.md)\* area | Pointer to the area information when the screen capture content is visible. |
| void \*userData | Pointer to the user-defined data carried in the function. |

#### \[h2\]OH\_AVScreenCapture\_OnUserSelected()

typedef void (\*OH\_AVScreenCapture\_OnUserSelected)(OH\_AVScreenCapture\* capture, OH\_AVScreenCapture\_UserSelectionInfo\* selections, void \*userData)

**Description**

Called to return the parameters selected by the user on the authorization UI to the application.

**Since**: 20

**Parameters**

| Parameter | Description |
| :-- | :-- |
| [OH\_AVScreenCapture](../../structs/oh-avscreencapture/document.md)\* capture | Pointer to the OH\_AVScreenCapture instance. |
| [OH\_AVScreenCapture\_UserSelectionInfo](../../structs/oh-avscreencapture-userselectioninfo/document.md)\* selections | Pointer to capture parameters selected by the user on the authorization UI. |
| void \*userData | Pointer to user-defined data. |
