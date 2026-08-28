# Low-Latency Audio Playback (C/C++)

Starting from API version 10, low-latency audio playback is available.

Low-latency audio playback is an audio rendering solution that leverages software-hardware-chip synergy. By reducing buffer sizes and optimizing the data read/write architecture, this mode delivers significantly lower audio playback latency.

#### Prerequisites

-   Audio output devices support the low-latency mode.
-   You can call [OH\_AudioRenderer\_GetFastStatus()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_getfaststatus) to check whether the current device supports the low-latency mode.

#### Development Guidelines

## Overview

To use the low-latency mode, you need to develop audio playback by referring to [(Recommended) Using OHAudio for Audio Playback (C/C++)](../recommended-using-ohaudio-for-audio-playback-c-c/document.md).

Currently, OHAudio supports two modes: normal mode (**AUDIOSTREAM\_LATENCY\_MODE\_NORMAL**) and low-latency mode (**AUDIOSTREAM\_LATENCY\_MODE\_FAST**).

## Setting the Low-Latency Mode

You can specify which mode the audio stream should use by calling [OH\_AudioStreamBuilder\_SetLatencyMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setlatencymode) to set [OH\_AudioStream\_LatencyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_latencymode).

The following is an example of setting the low-latency mode:

OH\_AudioStream\_LatencyMode latencyMode = AUDIOSTREAM\_LATENCY\_MODE\_FAST;
OH\_AudioStreamBuilder\_SetLatencyMode(builder, latencyMode);

The following sample is provided to help you better understand how to develop audio playback with **OHAudio**:

-   [OHAudio Recording and Playback](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/OHAudio)

#### Precautions

## Low-Latency Mode Restrictions

The system uses the normal mode under the following conditions, even if the low-latency mode is set:

-   The current device does not support the low-latency mode.
-   The current stream format does not support the low-latency mode.
-   All low-latency resources are already in use.
-   A higher-priority stream (for example, cellular call) is active.

Starting from API version 20, low-latency query APIs are available:

-   You can call [OH\_AudioRenderer\_GetFastStatus()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_getfaststatus) to check whether the audio playback stream is operating in low-latency mode.
-   In special scenarios (for example, a higher-priority stream is active or the current device does not support the low-latency mode), you can call [OH\_AudioRenderer\_OnFastStatusChange()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_onfaststatuschange) to subscribe to low-latency status change events.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0a/v3/2QWe3F7AQyqkGnJ5skRsnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3E9AC33B854012E6DC8AA85DD146D5EDE43004ED8B5D38919C6C6C5BCF4C3AF2)

The playback speed cannot be adjusted in low-latency mode.

## Recommended Use Cases

-   For latency-sensitive scenarios such as gaming, karaoke, and live streaming, the low-latency mode is recommended.
-   For non-real-time scenarios such as video playback and music playback, the low-latency mode is not recommended.

## Ensuring Timely Data Supply

In low-latency mode, the application must supply data more frequently than in normal playback mode. Delays in data transmission may cause audio artifacts such as noise. Avoid time-consuming operations in the data callback thread to ensure it returns promptly.

## Data Callback Thread

Audio data to be played is written through the callback API. Implement the callback API and call [OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setrendererwritedatacallback) to set the callback function [OH\_AudioRenderer\_OnWriteDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiorenderer_onwritedatacallback). This function is used to write audio data and supported since API version 12.

For details about the sample code for developing audio playback, please refer to [(Recommended) Using OHAudio for Audio Playback (C/C++)](../recommended-using-ohaudio-for-audio-playback-c-c/document.md).

The following is an example of setting the data callback function:

// Customize a function to write data.
static OH\_AudioData\_Callback\_Result MyOnWriteData(
    OH\_AudioRenderer\* renderer,
    void\* userData,
    void\* audioData,
    int32\_t audioDataSize)
{
    // Write the data to be played to audioData by audioDataSize.
    // If you do not want to play a segment of audioData, return AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID.
    return AUDIO\_DATA\_CALLBACK\_RESULT\_VALID;
}
// Configure the callback function for writing audio data.
OH\_AudioRenderer\_OnWriteDataCallback writeDataCb = MyOnWriteData;
OH\_AudioStreamBuilder\_SetRendererWriteDataCallback(builder, writeDataCb, nullptr);

-   To prevent audio stuttering, do not perform time-consuming operations in the callback function **OH\_AudioRenderer\_OnWriteData**.
    
-   To maintain independence between data writing logic and stream state control, do not call the audio stream control APIs in the callback function **OH\_AudioRenderer\_OnWriteData**.
    
    | Audio Stream Control API | Description |
    | :-- | :-- |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Start(OH\_AudioRenderer\* renderer) | Starts the audio renderer. |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Pause(OH\_AudioRenderer\* renderer) | Pauses the audio renderer. |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Stop(OH\_AudioRenderer\* renderer) | Stops the audio renderer. |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Flush(OH\_AudioRenderer\* renderer) | Flushes obtained audio data. |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Release(OH\_AudioRenderer\* renderer) | Releases the audio renderer. |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c2/v3/JfTiLG6PTn-1YOIcvy8Eig/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F532B652056E1B0B95906BEF720A09A1EFCC18031D9D5702DD3BCC5B21A87293)
    
    The execution of audio stream control APIs is time-consuming (for example, a single execution of **OH\_AudioRenderer\_Stop** generally takes more than 50 ms as it needs to play through the cache). Direct calls to these APIs on the main thread should be avoided to prevent display freezes.
