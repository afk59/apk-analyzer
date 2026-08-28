# Using LPP to Play Video (C/C++)

Starting from API version 20, the low power player (LPP) can be used to implement the video path capability from the media source to rendering with low power consumption. This guide walks you through playing a local video file using the LPP APIs.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f0/v3/RjISWj06TUqT4TpG36i0gw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80AF7539F59B64F038D3682C9A5EA81E824E42C8EF52B25293E2A6A04F20005A)

The LPP does not support pure video or audio playback. For details about low-power audio playback, see [Low-Power Audio Playback](../../../../audio-kit/audio-playback/low-power-audio-playback/document.md).

The full playback process includes creating a demuxer, creating a player, setting callback functions, configuring playback parameters (speed and volume), controlling playback (play, pause, resume, stop, and reset), and releasing the player instance.

**Figure 1** Playback state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d7/v3/CgKv3_7RS5mXCosXtkBxQg/en-us_image_0000002537925132.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=163EF7B6396ABE1C18888FC6E613FBE36309855109A027A0EBFF2A93B462C509)

The playback process consists of five phases: created, initialized, ready, decoding, and rendering.

The application calls **CreateByMime** to initialize and create a decoder instance. After the decoder parameters are configured, it is switched to the initialized state.

Then, the decoder resources are preloaded (Prepare), and the video enters the ready state. The decoding process (StartDecode) is then started, the decoder is switched to the decoding state, and the first frame rendering (RenderFirstFrame) is triggered. Finally, the rendering process (StartRender) is started, and the decoder is switched to the rendering state.

During rendering, if the video is paused (Pause), the decoder is switched to the paused state. In this case, the decoding and rendering are temporarily suspended but resources are not released. When rendering resumes (Resume), the video resumes and returns to the rendering state. If the video is stopped (Stop), the decoder is switched to the stopped state. In this case, the decoder stops working, but the instance still exists. When the stream ends (EoS) during rendering, the decoder is switched to the EoS state.

If an error occurs during playback (OnError), the decoder enters an abnormal state and must be reset or switched to the released state to destroy the decoder instance and release all resources.

When the player is in the ready, decoding, rendering, paused, or stopped state, it occupies system resources. Call **reset** or **destroy** to reclaim the resources when it is no longer needed.

#### Development Tips

This topic describes only how to implement the playback of a media asset. In practice, background playback and playback conflicts may be involved. You can refer to the following description to handle the situation based on your service requirements.

-   Due to hardware differences, LPP capabilities are only available on certain smartphones. You are advised to use [OH\_LowPowerAVSink\_GetCapability](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-avsink-base-h#oh_lowpoweravsink_getcapability) to check whether the LPP capabilities are supported. This API is available since API version 21. If they are not supported, use [AVCodec](../../../../avcodec-kit/about-this-kit/document.md) for playback.
    
-   When an application is playing media data that involves audio, it may be interrupted by other applications according to the system audio management policy. (For details, see [Processing Audio Interruption Events](../../../../audio-kit/audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md#handling-audio-focus-changes).) It is recommended that the application proactively listen for audio interruption events through [OH\_LowPowerAudioSinkCallback\_SetInterruptListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosinkcallback_setinterruptlistener) and handle the events accordingly to avoid inconsistencies between the application status and the expected effect.
    
-   When the device is connected to multiple audio output devices, it is recommended that the application listen for audio output device change events through [OH\_LowPowerAudioSinkCallback\_SetDeviceChangeListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosinkcallback_setdevicechangelistener) and handle the events accordingly.
    
-   During application execution, system internal exceptions may occur, such as network exceptions, insufficient memory, or unavailable media services. It is recommended that the application listen for errors through [OH\_LowPowerAudioSinkCallback\_SetErrorListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosinkcallback_seterrorlistener) or [OH\_LowPowerVideoSinkCallback\_SetErrorListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosinkcallback_seterrorlistener) and handle the errors accordingly.
    
-   During playback, the player obtains the buffer of a specified track through [OH\_AVDemuxer\_ReadSampleBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avdemuxer-h#oh_avdemuxer_readsamplebuffer) and encapsulates multiple buffers through [OH\_AVSamplesBuffer\_AppendOneBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-avsink-base-h#oh_avsamplesbuffer_appendonebuffer). Then the player starts consumption through notifications invoked by [OH\_LowPowerAudioSink\_ReturnSamples](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_returnsamples) or [OH\_LowPowerVideoSink\_ReturnSamples](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_returnsamples). When the player needs data, it triggers the callback registered through [OH\_LowPowerAudioSinkCallback\_SetDataNeededListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosinkcallback_setdataneededlistener) or [OH\_LowPowerVideoSinkCallback\_SetDataNeededListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosinkcallback_setdataneededlistener).
    
-   Pay attention to the timing of API calls. Make reasonable calls according to the state diagram and detailed API documentation. After the program execution, call the corresponding OH\_\*\*\*\_Destroy API to release resources.
    
-   When registering a callback, you can configure custom data in the last parameter void \*userData to perform certain settings (such as state changes) in the callback functions.
    
    Other callback functions:
    
    [OH\_LowPowerAudioSinkCallback\_SetPositionUpdateListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosinkcallback_setpositionupdatelistener): called when the playback progress updates.
    
    [OH\_LowPowerAudioSinkCallback\_SetEosListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosinkcallback_seteoslistener) or [OH\_LowPowerVideoSinkCallback\_SetEosListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosinkcallback_seteoslistener): called when the playback is completed.
    
    [OH\_LowPowerVideoSinkCallback\_SetRenderStartListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosinkcallback_setrenderstartlistener): called when video rendering starts.
    
    [OH\_LowPowerVideoSink\_SetTargetStartFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_settargetstartframe): called when the target frame is reached.
    
    [OH\_LowPowerVideoSinkCallback\_SetStreamChangedListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosinkcallback_setstreamchangedlistener): called when the video stream is switched.
    
    [OH\_LowPowerVideoSinkCallback\_SetFirstFrameDecodedListener](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosinkcallback_setfirstframedecodedlistener): called when the first frame of video is decoded.
    

#### How to Develop

Link the dynamic libraries in the CMake script.

target\_link\_libraries(sample PUBLIC liblowpower\_avsink.so)

Include the header files.

#include "multimedia/player\_framework/lowpower\_audio\_sink\_base.h"
#include "multimedia/player\_framework/lowpower\_audio\_sink.h"
#include "multimedia/player\_framework/lowpower\_video\_sink.h"
#include "multimedia/player\_framework/lowpower\_video\_sink\_base.h"

To use system logging, include the following header file:

#include <hilog/log.h>

In addition, link the following dynamic libraries in the CMake script:

target\_link\_libraries(sample PUBLIC libhilog\_ndk.z.so)

Include the following libraries: demuxer, basic decoding, and display rendering.

set(BASE\_LIBRARY
    libnative\_media\_codecbase.so libnative\_media\_core.so libnative\_media\_vdec.so libnative\_window.so
    libnative\_media\_venc.so libnative\_media\_acodec.so libnative\_media\_avdemuxer.so libnative\_media\_avsource.so
    libohaudio.so
)
target\_link\_libraries(sample PUBLIC ${BASE\_LIBRARY})

Include the [lowpower\_audio\_sink\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-base-h), [lowpower\_audio\_sink.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h), [lowpower\_video\_sink.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h) and [lowpower\_video\_sink\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-base-h) header files to use audio and video playback APIs.

1.  Creates a player.
    
    Based on actual service requirements, you can use a self-developed demuxer or create an [OH\_AVSource](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avsource-oh-avsource) instance by calling [OH\_AVSource\_CreateWithDataSource()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avsource-h#oh_avsource_createwithdatasource), [OH\_AVSource\_CreateWithFD()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avsource-h#oh_avsource_createwithfd), or [OH\_AVSource\_CreateWithURI()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avsource-h#oh_avsource_createwithuri). Then call [OH\_AVDemuxer\_CreateWithSource()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-avdemuxer-h#oh_avdemuxer_createwithsource) through the OH\_AVSource instance to create a demuxer and obtain video metadata.
    
    source\_ = OH\_AVSource\_CreateWithFD(info.inputFd, info.inputFileOffset, info.inputFileSize);
    demuxer\_ = OH\_AVDemuxer\_CreateWithSource(source\_);
    int32\_t ret = GetTrackInfo(sourceFormat, info);
    
2.  Based on the video metadata, call [OH\_LowPowerAudioSink\_CreateByMime](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_createbymime) or [OH\_LowPowerVideoSink\_CreateByMime](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_createbymime) to create a player.
    
    lppVideoStreamer\_ = OH\_LowPowerVideoSink\_CreateByMime(codecMime.c\_str());
    lppAudioStreamer\_ = OH\_LowPowerAudioSink\_CreateByMime(codecMime.c\_str());
    
3.  Set callbacks.
    
    Call [OH\_LowPowerAudioSinkCallback\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosinkcallback_create) or [OH\_LowPowerVideoSinkCallback\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosinkcallback_create) to create a callback for [OH\_LowPowerAudioSinkCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/api-lowpoweraudiosink-oh-lowpoweraudiosinkcallback) or [OH\_LowPowerVideoSinkCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/api-lowpowervideosink-oh-lowpowervideosinkcallback). Add the callbacks to the structure via the **setListener** API, and register them with **registerCallback**.
    
    lppAudioStreamerCallback\_ = OH\_LowPowerAudioSinkCallback\_Create();
    OH\_LowPowerAudioSinkCallback\_SetDataNeededListener(lppAudioStreamerCallback\_, LppCallback::OnDataNeeded, lppUserData);
    OH\_LowPowerAudioSinkCallback\_SetPositionUpdateListener(lppAudioStreamerCallback\_, LppCallback::OnPositionUpdated, lppUserData);
    ret = OH\_LowPowerAudioSink\_RegisterCallback(lppAudioStreamer\_, lppAudioStreamerCallback\_);
    
4.  Configure the player.
    
    Based on the metadata obtained through demultiplexing, create and configure [OH\_AVFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-core-oh-avformat). Configure the player by calling [OH\_LowPowerAudioSink\_Configure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_configure) or [OH\_LowPowerVideoSink\_Configure](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_configure). For details about the parameters, see the sample code. For video streams, call [OH\_LowPowerVideoSink\_SetVideoSurface](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_setvideosurface) to set the display window.
    
    OH\_AVFormat \*format = OH\_AVFormat\_Create();
     
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_WIDTH, sampleInfo.videoWidth);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_HEIGHT, sampleInfo.videoHeight);
    OH\_AVFormat\_SetDoubleValue(format, OH\_MD\_KEY\_FRAME\_RATE, sampleInfo.frameRate);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_PIXEL\_FORMAT, sampleInfo.pixelFormat);
    OH\_AVFormat\_SetIntValue(format, OH\_MD\_KEY\_ROTATION, sampleInfo.rotation);
     
    int ret = OH\_LowPowerVideoSink\_Configure(lppVideoStreamer\_, format);
    
5.  Prepare for playback.
    
    Call [OH\_LowPowerVideoSink\_SetSyncAudioSink](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_setsyncaudiosink) to set audio-video synchronization binding. Then, call [OH\_LowPowerAudioSink\_Prepare](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_prepare) or [OH\_LowPowerVideoSink\_Prepare](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_prepare). After a successful call, the player enters the ready state.
    
    OH\_LowPowerVideoSink\_Prepare(lppVideoStreamer\_);
    
6.  Start playback.
    
    Call [OH\_LowPowerAudioSink\_Start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_start) or [OH\_LowPowerVideoSink\_StartRenderer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_startrenderer) to start rendering. For video streams, before rendering, call [OH\_LowPowerVideoSink\_StartDecoder](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_startdecoder) to start decoding, or call [OH\_LowPowerVideoSink\_RenderFirstFrame](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_renderfirstframe) to start decoding and display the first frame, thereby entering the decoding state.
    
    OH\_LowPowerVideoSink\_StartDecoder(lppVideoStreamer\_);
    OH\_LowPowerVideoSink\_StartRenderer(lppVideoStreamer\_);
    
7.  (Optional) Control the playback.
    
    To pause the playback, call [OH\_LowPowerAudioSink\_Pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_pause) or [OH\_LowPowerVideoSink\_Pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_pause).
    
    To resume the playback, call [OH\_LowPowerAudioSink\_Resume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_resume) or [OH\_LowPowerVideoSink\_Resume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_resume).
    
    To stop the playback, call [OH\_LowPowerAudioSink\_Stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_stop) or [OH\_LowPowerVideoSink\_Stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_stop).
    
    To set the playback volume, call [OH\_LowPowerAudioSink\_SetVolume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_setvolume).
    
    To set the playback speed, call [OH\_LowPowerAudioSink\_SetPlaybackSpeed](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_setplaybackspeed) or [OH\_LowPowerVideoSink\_SetPlaybackSpeed](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_setplaybackspeed).
    
    To clear cache data (which can be used for seeking), call [OH\_LowPowerAudioSink\_Flush](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_flush) or [OH\_LowPowerVideoSink\_Flush](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_flush).
    
8.  (Optional) Replace resources.
    
    Call [OH\_LowPowerAudioSink\_Reset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_reset) or [OH\_LowPowerVideoSink\_Reset](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_reset) to reset the resource. You can replace resources and reconfigure the player.
    
9.  Exit the playback.
    
    Call [OH\_LowPowerAudioSink\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-audio-sink-h#oh_lowpoweraudiosink_destroy) or [OH\_LowPowerVideoSink\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-lowpower-video-sink-h#oh_lowpowervideosink_destroy) to destroy the instance. The player enters the released state and exits the playback.
    

#### Running the Sample Project

1.  Create a project. Download the [sample project](https://gitcode.com/HarmonyOS_Samples/guide-snippets/tree/master/MediaKit/LowPowerAVSInk/lowPowerAVSinkSample), and copy its resources to the corresponding directories.
    
    lpp\_demo-sample/entry/src/main/
    ├── cpp                                # Native layer
    │   ├── capbilities                    # Capability interfaces and implementation
    │   │   ├── include                    # Capability interfaces
    │   │   ├── demuxer.cpp                # Demuxer implementation
    │   │   ├── lpp\_audio\_streamer.cpp     # LPP audio stream implementation
    │   │   └── lpp\_video\_streamer.cpp     # LPP video stream implementation
    │   ├── common                         # Common modules
    │   │   ├── dfx                        # Logs
    │   │   ├── lpp\_callback.cpp           # LPP audio and video callback implementation
    │   │   ├── lpp\_callback.h             # LPP audio and video callback interfaces
    │   │   └── sample\_info.h              # Common classes for function implementation
    │   ├── render                         # Render module interfaces and implementation\* Window player settings
    │   │   ├── include                    # Display module interfaces
    │   │   ├── egl\_core.cpp               # Display parameter settings
    │   │   ├── plugin\_manager.cpp         # Display module management implementation
    │   │   └── plugin\_render.cpp          # Display logic implementation
    │   ├── sample                         # Native layer
    │   │   ├── player                     # Player interfaces and implementation at the native layer
    │   │   │   ├── Player.cpp             # Player implementation at the native layer
    │   │   │   ├── Player.h               # Player interfaces at the native layer
    │   │   │   ├── PlayerNative.cpp       # Player entry at the native layer
    │   │   │   └── PlayerNative.h         # Interface exposed by the native layer
    │   ├── types                          #
    │   │   └── libplayer                  # Interfaces exposed by the player to the UI layer
    │   └── CMakeLists.txt                 # Compilation entry
    ├── ets                                # UI layer
    │   ├── common                         # Common modules
    │   │   ├── utils                      # Common utility class
    │   │   │   ├── DateTimeUtils.ets      # Used to obtain the current time
    │   │   │   └── Logger.ts              # Log utility
    │   |   └───CommonConstants.ets        # Common constants
    │   ├── entryability                   # Application entry
    │   │   └── EntryAbility.ts            # Implementation of the permission request dialog box
    │   ├── pages                          # Pages contained in the EntryAbility
    │   │   └── Index.ets                  # Home page/Playback page
    ├── resources                          # Static resources
    │   ├── base                           # Resource files in this directory are assigned unique IDs.
    │   │   ├── element                    # Fonts and colors
    │   │   ├── media                      # Images
    │   │   └── profile                    # Home page of the app entry
    │   ├── en\_US                          # Resources in this directory are preferentially matched when the device language is English (US).
    │   └── zh\_CN                          # Resources in this directory are preferentially matched when the device language is simplified Chinese.
    └── module.json5                       # Module configuration information
    
2.  Compile and run the project.
