# Using AVPlayer to Play Audio (C/C++)

The [AVPlayer](../../../about-this-kit/document.md#avplayer) is used to play raw media assets in an end-to-end manner. In this topic, you will learn how to use the AVPlayer to play a complete piece of music.

The full playback process includes creating an AVPlayer instance, setting callback functions, setting the media asset to play, setting playback parameters (volume, speed, and focus mode), controlling playback (play, pause, seek, and stop), resetting the playback configuration, and releasing the AVPlayer instance.

During application development, you can obtain the playback process information through the callbacks [OH\_AVPlayerOnInfoCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfocallback) and [OH\_AVPlayerOnErrorCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeronerrorcallback) of the AVPlayer. If the application performs an operation when the AVPlayer is not in the given state, the system may throw an exception or generate other undefined behavior.

**Figure 1** Playback state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3a/v3/0Ztxhm6IRFyKeR-nFSEKzg/en-us_image_0000002537765192.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062043Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F2BC060FCEF83A92D542356A004E0D3AD96E9B703D74EF98DD83E80C2106DF40)

For details about the states, see [AVPlayerState](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#avplayerstate). When the AVPlayer is in the **prepared**, **playing**, **paused**, or **completed** state, the playback engine is working and a large amount of RAM is occupied. If your application does not need to use the AVPlayer, call **OH\_AVPlayer\_Reset()** or **OH\_AVPlayer\_Release()** to release the instance.

#### Development Tips

This topic describes only how to implement the playback of a media asset. In practice, background playback and playback conflicts may be involved. You can refer to the following description to handle the situation based on your service requirements.

-   If you want the application to continue playing the media asset in the background or when the screen is off, use the [AVSession](../../../../avsession-kit/local-avsession/accessing-avsession/document.md) and [continuous task](../../../../../application-framework/background-tasks-kit/continuous-task-arkts/document.md) to prevent the playback from being forcibly interrupted by the system. Only ArkTS APIs are provided.
-   If the media asset being played involves audio, the playback may be interrupted by other applications based on the system audio management policy. (For details, see [Processing Audio Interruption Events](../../../../audio-kit/audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md).) It is recommended that the player application proactively listen for audio interruption events [AV\_INFO\_TYPE\_INTERRUPT\_EVENT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#avplayeroninfotype) through [OH\_AVPlayer\_SetOnInfoCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setoninfocallback) and handle the events accordingly to avoid the inconsistency between the application status and the expected effect.
-   When a device is connected to multiple audio output devices, the application can listen for audio output device changes [AV\_INFO\_TYPE\_AUDIO\_OUTPUT\_DEVICE\_CHANGE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#avplayeroninfotype) through [OH\_AVPlayer\_SetOnInfoCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setoninfocallback) and perform the processing accordingly.
-   During the playback, an internal error may occur, for example, network data download failure or media service unavailability. You are advised to set an error callback through [OH\_AVPlayer\_SetOnErrorCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setonerrorcallback) and handle the error based on the error type.
-   Use [OH\_AVPlayer\_SetOnInfoCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setoninfocallback) and [OH\_AVPlayer\_SetOnErrorCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setonerrorcallback) to set the information callback [OH\_AVPlayerOnInfoCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfocallback) and error callback [OH\_AVPlayerOnErrorCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeronerrorcallback), respectively. After[OH\_AVPlayerOnInfoCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfocallback) is set, the callback [OH\_AVPlayerOnInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeroninfo) set through [OH\_AVPlayer\_SetPlayerCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setplayercallback) is not executed. After [OH\_AVPlayerOnErrorCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeronerrorcallback) is set, the callback[OH\_AVPlayerOnError](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#oh_avplayeronerror) set through [OH\_AVPlayer\_SetPlayerCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setplayercallback) is not executed.

#### How to Develop

Link the dynamic library in the CMake script.

target\_link\_libraries(sample PUBLIC libavplayer.so)

To use [OH\_AVPlayer\_SetOnInfoCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setoninfocallback) and [OH\_AVPlayer\_SetOnErrorCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setonerrorcallback) to set the information callback and error callback, link the following dynamic libraries in the CMake script:

target\_link\_libraries(sample PUBLIC libnative\_media\_core.so)

To use system logging, include the following header file:

#include <hilog/log.h>

In addition, link the following dynamic library in the CMake script:

target\_link\_libraries(sample PUBLIC libhilog\_ndk.z.so)

You can use C/C++ APIs related to audio playback by including the header files [avplayer.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h), [avplayer\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h), and [native\_averrors.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-averrors-h).

Read [AVPlayer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer) for the API reference.

1.  Create an AVPlayer instance by calling [OH\_AVPlayer\_Create()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_create). The AVPlayer is initialized to the [AV\_IDLE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#avplayerstate) state.
    
2.  Set callbacks to listen for events. Specifically, call [OH\_AVPlayer\_SetOnInfoCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setoninfocallback) and [OH\_AVPlayer\_SetOnErrorCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setonerrorcallback) to set the information callback and error callback, which are used in the entire process scenario. The table below lists the supported events.
    
    | Event Type | Description |
    | :-- | :-- |
    | OH\_AVPlayerOnInfoCallback | 
    Mandatory; used to listen for AVPlayer process information.
    
    To ensure proper functionality, the listener must be configured when the AVPlayer is in the **AV\_IDLE** state and before the resource setting API is called. If the listener is set after the resource setting API is called, the **OH\_AVPlayerOnInfoCallback** event reported during resource setting may fail to be received.
    
     |
    | OH\_AVPlayerOnErrorCallback | 
    
    Mandatory; used to listen for AVPlayer errors.
    
    To ensure proper functionality, the listener must be configured when the AVPlayer is in the **AV\_IDLE** state and before the resource setting API is called. If the listener is set after the resource setting API is called, the **OH\_AVPlayerOnErrorCallback** event reported during resource setting may fail to be received.
    
     |
    
    The application can obtain more information from the callbacks set by calling [OH\_AVPlayer\_SetOnInfoCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setoninfocallback) and [OH\_AVPlayer\_SetOnErrorCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setonerrorcallback). In addition, it can set **userData** to distinguish different AVPlayer instances.
    
3.  Set the media asset. Specifically, call [OH\_AVPlayer\_SetURLSource()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_seturlsource) to set the URL of the media asset. The AVPlayer enters the [AV\_INITIALIZED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#avplayerstate) state.
    
4.  (Optional) Set the audio stream type by calling [OH\_AVPlayer\_SetAudioRendererInfo()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setaudiorendererinfo).
    
5.  (Optional) Set the audio interruption mode by calling [OH\_AVPlayer\_SetAudioInterruptMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setaudiointerruptmode).
    
6.  Prepare for the playback by calling [OH\_AVPlayer\_Prepare()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_prepare). The AVPlayer enters the [AV\_PREPARED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#avplayerstate) state. In this case, you can obtain the duration and set the volume.
    
7.  (Optional) Set the audio effect mode of the AVPlayer by calling [OH\_AVPlayer\_SetAudioEffectMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_setaudioeffectmode).
    
8.  Control the playback. You can call [OH\_AVPlayer\_Play()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_play), [OH\_AVPlayer\_Pause()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_pause), [OH\_AVPlayer\_Seek()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_seek), and [OH\_AVPlayer\_Stop()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_stop) to trigger different control operations.
    
9.  (Optional) Reset the media asset by calling [OH\_AVPlayer\_Reset()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_reset). The AVPlayer enters the [AV\_IDLE](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#avplayerstate) state again and you can change the media asset URL.
    
10.  Exit the playback. Specifically, call [OH\_AVPlayer\_Release()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-h#oh_avplayer_release) to destroy the instance. The AVPlayer enters the [AV\_RELEASED](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-avplayer-base-h#avplayerstate) state and exits the playback. Further actions on the AVPlayer instance may lead to undefined behavior, such as the process crashing or the application terminating unexpectedly.
     

#### Running the Sample Project

1.  Create a project, download the [sample project](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/AVPlayer/AVPlayerNDKAudio), and copy its resources to the corresponding directories.
    
    AVPlayerNDKAudio
    entry/src/main/ets/
    └── pages
        └── Index.ets (playback page)
    entry/src/main/
    ├── cpp
    │   ├── types
    │   │   └── libentry
    │   │       └── Index.d.ts (JavaScript mapping of NDK functions)
    │ ├── CMakeLists.txt (CMake script)
    │   └── napi\_init.cpp (NDK functions)
    └── resources
        ├── base
        │   ├── element
        │   │   ├── color.json
        │   │   ├── float.json
        │   │   └── string.json
        │   └── media
        │       ├── ic\_video\_play.svg (play button image resource)
        │       └── ic\_video\_pause.svg (pause button image resource)
        └── rawfile
            └── test\_01.mp3 (audio resource)
    
2.  Compile and run the project.
