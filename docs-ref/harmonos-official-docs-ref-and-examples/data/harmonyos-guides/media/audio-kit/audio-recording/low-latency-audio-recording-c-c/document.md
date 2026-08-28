# Low-Latency Audio Recording (C/C++)

Starting from API version 10, low-latency audio recording is available.

Low-latency audio recording is an audio rendering solution that leverages software-hardware-chip synergy. By reducing buffer sizes and optimizing the data read/write architecture, this mode delivers significantly lower audio recording latency.

#### Prerequisites

-   Audio input devices support the low-latency mode.
-   You can call [OH\_AudioCapturer\_GetFastStatus()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_getfaststatus) to check whether the current device supports the low-latency mode.

#### Development Guidelines

## Overview

To use the low-latency mode, you need to develop audio recording by referring to [\[Recommended\] Using OHAudio for Audio Recording (C/C++)](../recommended-using-ohaudio-for-audio-recording-c-c/document.md).

Currently, OHAudio supports two modes: normal mode (**AUDIOSTREAM\_LATENCY\_MODE\_NORMAL**) and low-latency mode (**AUDIOSTREAM\_LATENCY\_MODE\_FAST**).

## Setting the Low-Latency Mode

You can specify which mode the audio stream should use by calling [OH\_AudioStreamBuilder\_SetLatencyMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setlatencymode) to set [OH\_AudioStream\_LatencyMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_latencymode).

The following is an example of setting the low-latency mode:

OH\_AudioStream\_LatencyMode latencyMode = AUDIOSTREAM\_LATENCY\_MODE\_FAST;
OH\_AudioStreamBuilder\_SetLatencyMode(builder, latencyMode);

The following sample is provided to help you better understand how to develop audio recording with OHAudio:

-   [OHAudio Recording and Playback](https://gitcode.com/openharmony/applications_app_samples/tree/master/code/DocsSample/Media/Audio/OHAudio)

#### Precautions

## Low-Latency Mode Restrictions

The system uses the normal mode under the following conditions, even if the low-latency mode is set:

-   The current device does not support the low-latency mode.
-   The current stream format does not support the low-latency mode.
-   All low-latency resources are already in use.
-   A higher-priority stream (for example, VoIP call) is active.

Starting from API version 20, low-latency query APIs are available:

-   You can call [OH\_AudioCapturer\_GetFastStatus()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_getfaststatus) to check whether the audio recording stream is operating in low-latency mode.
-   In special scenarios (for example, a higher-priority stream is active or the current device does not support the low-latency mode), you can call [OH\_AudioCapturer\_OnFastStatusChange()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_onfaststatuschange) to subscribe to low-latency status change events.

## Recommended Use Cases

-   For latency-sensitive scenarios such as karaoke and live streaming, the low-latency mode is recommended.
-   For non-real-time scenarios such as common audio recording, video recording, and screen capture, the low-latency mode is not recommended.

## Ensuring Timely Data Reading

In low-latency mode, the application must read data more frequently than in normal recording mode. Delays in data reading may cause audio artifacts such as noise. Avoid time-consuming operations in the data callback thread to ensure it returns promptly.

## Data Callback Thread

Audio data to be recorded is read through the callback API. Implement the callback API and call [OH\_AudioStreamBuilder\_SetCapturerReadDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setcapturerreaddatacallback) to set the callback function [OH\_AudioCapturer\_OnReadDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_onreaddatacallback). This function is used to read audio data and supported since API version 12.

For details about the sample code for developing audio recording, please refer to [(Recommended) Using OHAudio for Audio Recording (C/C++)](../recommended-using-ohaudio-for-audio-recording-c-c/document.md).

The following is an example of setting the data callback function:

// Customize a function to read data.
static OH\_AudioData\_Callback\_Result MyOnReadData(
    OH\_AudioCapturer\* capturer,
    void\* userData,
    void\* buffer,
    int32\_t length)
{
    // Obtain captured data of the specified length from the buffer.
    return AUDIO\_DATA\_CALLBACK\_RESULT\_VALID0;
}
// Configure the callback function for reading audio data.
OH\_AudioCapturer\_OnReadDataCallback readDataCb = MyOnReadData;
OH\_AudioStreamBuilder\_SetCapturerReadDataCallback(builder, readDataCb, nullptr);

-   To prevent audio stuttering, do not perform time-consuming operations in the callback function **OH\_AudioCapturer\_OnReadData**.
    
-   To maintain independence between data writing logic and stream state control, do not call the audio stream control APIs in the callback function **OH\_AudioCapturer\_OnReadData**.
    
    | Audio Stream Control API | Description |
    | :-- | :-- |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Start(OH\_AudioCapturer\* capturer) | Starts the audio capturer. |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Pause(OH\_AudioCapturer\* capturer) | Pauses the audio capturer. |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Stop(OH\_AudioCapturer\* capturer) | Stops the audio capturer. |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Flush(OH\_AudioCapturer\* capturer) | Flushes obtained audio data. |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Release(OH\_AudioCapturer\* capturer) | Releases the audio capturer instance. |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0d/v3/RNaNsnxUSneJgvjCybqshA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DA211D6253D7BC6E00BD9797863FBDF3DED0BB174E7F75494D04904FB3A8C34C)
    
    The execution of audio stream control APIs is time-consuming (for example, a single execution of **OH\_AudioCapturer\_Stop** generally takes more than 50 ms). Direct calls to these APIs on the main thread should be avoided to prevent interface display freezes.
