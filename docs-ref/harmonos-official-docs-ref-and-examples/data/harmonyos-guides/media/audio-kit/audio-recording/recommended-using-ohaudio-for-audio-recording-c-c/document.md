# (Recommended) Using OHAudio for Audio Recording (C/C++)

OHAudio is a set of C APIs introduced in API version 10. These APIs are normalized in design and support both common and low-latency audio channels. They support the PCM format only. They are suitable for applications that implement audio input at the native layer.

OHAudio audio capturer state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0b/v3/oHjg1bnUQYCwAEoYmkXGqw/en-us_image_0000002537925092.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=678654AD45594DFA87CF39625833BF4C4418FFBD5C6AC738CEA23DAECFAF10A3)

#### Prerequisites

To use the recording capability of OHAudio, you must first import the corresponding header files.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC libohaudio.so)

## Adding Header Files

Include the <[native\_audiostreambuilder.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h)\> and <[native\_audiocapturer.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiocapturer-h)\> header files so that the application can use the functions related to audio recording.

#include <ohaudio/native\_audiocapturer.h>
#include <ohaudio/native\_audiostreambuilder.h>

#### How to Develop

Read [OHAudio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio) for the API reference.

## Audio Stream Builder

OHAudio provides the **OH\_AudioStreamBuilder** class, which complies with the builder design pattern and is used to build audio streams. You need to specify [OH\_AudioStream\_Type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_type) based on your service scenarios.

**OH\_AudioStream\_Type** can be set to either of the following:

-   AUDIOSTREAM\_TYPE\_RENDERER
-   AUDIOSTREAM\_TYPE\_CAPTURER

The following code snippet shows how to use [OH\_AudioStreamBuilder\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_create) to create a builder:

OH\_AudioStreamBuilder\* builder;
OH\_AudioStreamBuilder\_Create(&builder, streamType);

After the audio service is complete, call [OH\_AudioStreamBuilder\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_destroy) to destroy the builder.

OH\_AudioStreamBuilder\_Destroy(builder);

The following walks you through how to implement simple recording:

## Implementing Audio Recording

1.  Create an audio stream builder.
    
    OH\_AudioStreamBuilder\* builder;
    OH\_AudioStreamBuilder\_Create(&builder, AUDIOSTREAM\_TYPE\_CAPTURER);
    
2.  Set audio stream parameters.
    
    After creating the builder for audio recording, set the parameters required.
    
    // Set the audio sampling rate.
    OH\_AudioStreamBuilder\_SetSamplingRate(builder, 48000);
    // Set the number of audio channels.
    OH\_AudioStreamBuilder\_SetChannelCount(builder, 2);
    // Set the audio sampling format.
    OH\_AudioStreamBuilder\_SetSampleFormat(builder, AUDIOSTREAM\_SAMPLE\_S16LE);
    // Set the encoding type of the audio stream.
    OH\_AudioStreamBuilder\_SetEncodingType(builder, AUDIOSTREAM\_ENCODING\_TYPE\_RAW);
    // Set the usage scenario of the audio capturer.
    OH\_AudioStreamBuilder\_SetCapturerInfo(builder, AUDIOSTREAM\_SOURCE\_TYPE\_MIC);
    
    The audio data for recording must be read through a callback function, and you must implement the callback function. Starting from API version 12, you can use [OH\_AudioStreamBuilder\_SetCapturerReadDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setcapturerreaddatacallback) to set the callback function. For details about its declaration, see [OH\_AudioCapturer\_OnReadDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiocapturer-h#oh_audiocapturer_onreaddatacallback).
    
3.  Set the callback functions.
    
    For details about concurrent processing of multiple audio streams, see [Processing Audio Interruption Events](../../audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md). The procedure is similar, and the only difference is the API programming language in use.
    
    // Customize a data reading function.
    void MyOnReadData(
        OH\_AudioCapturer\* capturer,
        void\* userData,
        void\* audioData,
        int32\_t audioDataSize)
    {
        // Obtain the recording data of the specified length from the buffer.
    }
    // Customize an audio interruption event function.
    void MyOnInterruptEvent(
        OH\_AudioCapturer\* capturer,
        void\* userData,
        OH\_AudioInterrupt\_ForceType type,
        OH\_AudioInterrupt\_Hint hint)
    {
        // Update the capturer status and UI based on the audio interruption information indicated by type and hint.
    }
    // Customize an exception callback function.
    void MyOnError(
        OH\_AudioCapturer\* capturer,
        void\* userData,
        OH\_AudioStream\_Result error)
    {
        // Perform operations based on the audio exception information indicated by error.
    }
    
    // Configure the callback function for interruption events.
    OH\_AudioCapturer\_OnInterruptCallback onInterruptCb = MyOnInterruptEvent;
    OH\_AudioStreamBuilder\_SetCapturerInterruptCallback(builder, onInterruptCb, nullptr);
    
    // Configure the callback function for audio exceptions.
    OH\_AudioCapturer\_OnErrorCallback onErrorCb = MyOnError;
    OH\_AudioStreamBuilder\_SetCapturerErrorCallback(builder, onErrorCb, nullptr);
    
    // Configure the callback for audio input streams.
    OH\_AudioCapturer\_OnReadDataCallback onReadDataCb = MyOnReadData;
    OH\_AudioStreamBuilder\_SetCapturerReadDataCallback(builder, onReadDataCb, nullptr);
    
4.  Create an audio capturer instance.
    
    OH\_AudioCapturer\* audioCapturer;
    OH\_AudioStreamBuilder\_GenerateCapturer(builder, &audioCapturer);
    
5.  Use the audio capturer.
    
    You can use the APIs listed below to control the audio streams.
    
    | API | Description |
    | :-- | :-- |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Start(OH\_AudioCapturer\* capturer) | Starts the audio capturer. |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Pause(OH\_AudioCapturer\* capturer) | Pauses the audio capturer. |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Stop(OH\_AudioCapturer\* capturer) | Stops the audio capturer. |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Flush(OH\_AudioCapturer\* capturer) | Flushes obtained audio data. |
    | OH\_AudioStream\_Result OH\_AudioCapturer\_Release(OH\_AudioCapturer\* capturer) | Releases the audio capturer instance. |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/06/v3/-OIh20aBStS7WVV1uzyQwA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1061E5B885491ED1839FBCD95719728E95249683F8C61E0738CAE3EDC51D5F7C)
    
    The execution of audio stream control APIs is time-consuming (for example, a single execution of **OH\_AudioCapturer\_Stop** generally takes more than 50 ms). Direct calls to these APIs on the main thread should be avoided to prevent interface display freezes.
    
6.  Destroy the audio stream builder.
    
    When the builder is no longer used, release related resources.
    
    OH\_AudioStreamBuilder\_Destroy(builder);
    

## Setting the Low Latency Mode

If the device supports the low-latency channel, you can use the low-latency mode to create an audio capturer for a low-latency audio experience.

The development process is similar to that in the common recording scenario (described in [Implementing Audio Recording](#implementing-audio-recording)). The only difference is that you need to set the low delay mode by calling [OH\_AudioStreamBuilder\_SetLatencyMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setlatencymode) when creating an audio stream builder in step 1.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/Fx2RTyw9QMG_rbzKvgtcFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BE709B7CBA9FEB443F5FF5478C967B43E6C6CCEB38B4EFE1839F441E5327DCF2)

-   In audio recording scenarios, if [OH\_AudioStream\_SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_sourcetype) is set to **AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_COMMUNICATION**, the low-latency mode cannot be set. The system determines the output audio channel based on the device capability.
-   In some scenarios (for example, incoming calls), the system capability is limited and the audio channel mode falls back to the common audio channel mode, and the buffer size changes accordingly. In this case, you need to obtain all data in the buffer at a time based on the buffer size, which is the same as that in the common audio channel mode. Otherwise, the recorded data will be discontinuous, resulting in noises.

OH\_AudioStream\_LatencyMode latencyMode = AUDIOSTREAM\_LATENCY\_MODE\_FAST;
OH\_AudioStreamBuilder\_SetLatencyMode(builder, latencyMode);

## Setting the Mute Interruption Mode

The mute interruption mode allows you to switch the interruption policy from stopping recording to muting recording, so that the recording will not be interrupted by the system based on the focus concurrency rule. In addition, recording of other apps is not affected during the recording. To ensure that the recording is not interrupted by the system's focus concurrency rules, a feature is introduced to change the interruption strategy from stopping the recording to simply muting it. You can control this behavior by calling [OH\_AudioStreamBuilder\_SetCapturerWillMuteWhenInterrupted](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setcapturerwillmutewheninterrupted) when creating an audio stream builder. By default, this mode is disabled, and the audio focus strategy manages the order of concurrent audio streams. When enabled, if the recording is interrupted by another application, it will go into a muted state instead of stopping or pausing. In this state, the audio captured is silent.

## Echo Cancellation

Echo cancellation effectively eliminates echo interference during recording on supported devices, thereby improving audio capture quality. You can enable this feature by specifying particular audio input source types [OH\_AudioStream\_SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_sourcetype) (**AUDIOSTREAM\_SOURCE\_TYPE\_VOICE\_COMMUNICATION** or **AUDIOSTREAM\_SOURCE\_TYPE\_LIVE**). Once enabled, the system automatically processes the captured audio signal to cancel echoes.

Before enabling this feature, you are advised to call [OH\_AudioStreamManager\_IsAcousticEchoCancelerSupported](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-stream-manager-h#oh_audiostreammanager_isacousticechocancelersupported) to check whether the device supports echo cancellation for the audio input source type [OH\_AudioStream\_SourceType](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_sourcetype). (This API is available since API version 20.) If supported, you can activate the echo cancellation processing by calling [OH\_AudioStreamBuilder\_SetCapturerInfo](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setcapturerinfo) to set the corresponding audio input source type when creating the audio capturer.

#### Precautions

Starting from API version 12, the [OH\_AudioCapturer\_Callbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiocapturer-callbacks-struct) API is no longer recommended for setting audio callback functions. If this API must be used, you should ensure that the audio callback function is set properly to avoid unexpected behavior. You can do this in one of two ways:

-   Initialize each callback in [OH\_AudioCapturer\_Callbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiocapturer-callbacks-struct) by a custom callback method or a null pointer.
    
    // Customize a data reading function.
    int32\_t MyOnReadData(
        OH\_AudioCapturer\* capturer,
        void\* userData,
        void\* buffer,
        int32\_t length)
    {
        // Obtain the recording data of the specified length from the buffer.
        return 0;
    }
    // Customize an audio interruption event function.
    int32\_t MyOnInterruptEvent(
        OH\_AudioCapturer\* capturer,
        void\* userData,
        OH\_AudioInterrupt\_ForceType type,
        OH\_AudioInterrupt\_Hint hint)
    {
        // Update the capturer status and UI based on the audio interruption information indicated by type and hint.
        return 0;
    }
    OH\_AudioCapturer\_Callbacks callbacks;
    
    // Configure a callback function. If listening is required, assign a value.
    callbacks.OH\_AudioCapturer\_OnReadData = MyOnReadData;
    callbacks.OH\_AudioCapturer\_OnInterruptEvent = MyOnInterruptEvent;
    
    // (Mandatory) If listening is not required, use a null pointer for initialization.
    callbacks.OH\_AudioCapturer\_OnStreamEvent = nullptr;
    callbacks.OH\_AudioCapturer\_OnError = nullptr;
    
-   Initialize and clear the struct before using it.
    
    // Customize a data reading function.
    int32\_t MyOnReadData(
        OH\_AudioCapturer\* capturer,
        void\* userData,
        void\* buffer,
        int32\_t length)
    {
        // Obtain the recording data of the specified length from the buffer.
        return 0;
    }
    // Customize an audio interruption event function.
    int32\_t MyOnInterruptEvent(
        OH\_AudioCapturer\* capturer,
        void\* userData,
        OH\_AudioInterrupt\_ForceType type,
        OH\_AudioInterrupt\_Hint hint)
    {
        // Update the capturer status and UI based on the audio interruption information indicated by type and hint.
        return 0;
    }
    OH\_AudioCapturer\_Callbacks callbacks;
    
    // Initialize and clear the struct before using it.
    memset(&callbacks, 0, sizeof(OH\_AudioCapturer\_Callbacks));
    
    // Configure the required callback functions.
    callbacks.OH\_AudioCapturer\_OnReadData = MyOnReadData;
    callbacks.OH\_AudioCapturer\_OnInterruptEvent = MyOnInterruptEvent;
