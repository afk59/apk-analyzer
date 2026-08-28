# (Recommended) Using OHAudio for Audio Playback (C/C++)

OHAudio is a set of C APIs introduced in API version 10. These APIs are normalized in design and support both common and low-latency audio channels. They support the PCM format only and are suitable for applications that implement audio output at the native layer.

OHAudio audio playback state transition

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ba/v3/5jQvqilMSeC9rZYp5B2jfA/en-us_image_0000002568764875.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8D14F7E3B0216141B488476A6C40278AD5422772E0347634DB57161C2089C11D)

#### Prerequisites

To use the playback capability of OHAudio, you must first import the corresponding header files.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC libohaudio.so)

## Adding Header Files

Include the <[native\_audiostreambuilder.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h)\> and <[native\_audiorenderer.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h)\> header files so that the application can use the functions related to audio playback.

#include <ohaudio/native\_audiorenderer.h>
#include <ohaudio/native\_audiostreambuilder.h>

#### How to Develop

Read [OHAudio](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio) for the API reference.

## Building Audio Streams

OHAudio provides the **OH\_AudioStreamBuilder** class, which complies with the builder design pattern and is used to build audio streams. You need to specify [OH\_AudioStream\_Type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_type) based on your service scenarios.

**OH\_AudioStream\_Type** can be set to either of the following:

-   AUDIOSTREAM\_TYPE\_RENDERER
-   AUDIOSTREAM\_TYPE\_CAPTURER

The following code snippet shows how to use [OH\_AudioStreamBuilder\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_create) to create a builder:

OH\_AudioStreamBuilder\* builder;
OH\_AudioStreamBuilder\_Create(&builder, streamType);

After the audio service is complete, call [OH\_AudioStreamBuilder\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_destroy) to destroy the builder.

OH\_AudioStreamBuilder\_Destroy(builder);

The following walks you through how to implement simple playback:

## Implementing Audio Playback

1.  Create an audio stream builder.
    
    OH\_AudioStreamBuilder\* builder;
    OH\_AudioStreamBuilder\_Create(&builder, AUDIOSTREAM\_TYPE\_RENDERER);
    
2.  Set audio stream parameters.
    
    For details about the audio sampling rate, see [Configuring the Appropriate Audio Sampling Rate](../using-audiorenderer-for-audio-playback-arkts/document.md#configuring-the-appropriate-audio-sampling-rate).
    
    After creating the builder for audio playback, set the parameters required.
    
    // Set the audio sampling rate.
    OH\_AudioStreamBuilder\_SetSamplingRate(builder, 48000);
    // Set the number of audio channels.
    OH\_AudioStreamBuilder\_SetChannelCount(builder, 2);
    // Set the audio sampling format.
    OH\_AudioStreamBuilder\_SetSampleFormat(builder, AUDIOSTREAM\_SAMPLE\_S16LE);
    // Set the encoding type of the audio stream.
    OH\_AudioStreamBuilder\_SetEncodingType(builder, AUDIOSTREAM\_ENCODING\_TYPE\_RAW);
    // Set the usage scenario of the audio renderer.
    OH\_AudioStreamBuilder\_SetRendererInfo(builder, AUDIOSTREAM\_USAGE\_MUSIC);
    
    The audio data for playback must be written through a callback function, and you must implement the callback function. Starting from API version 12, you can use [OH\_AudioStreamBuilder\_SetRendererWriteDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setrendererwritedatacallback) to set the data callback function. For details about its declaration, see [OH\_AudioRenderer\_OnWriteDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiorenderer_onwritedatacallback).
    
3.  Set the callback functions.
    
    For details about concurrent processing of multiple audio streams, see [Processing Audio Interruption Events](../../audio-focus-and-audio-session-management/introduction-to-audio-focus/document.md). The procedure is similar, and the only difference is the API programming language in use.
    
    -   Starting from API version 12, you are advised to use [OH\_AudioRenderer\_OnWriteDataCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiorenderer_onwritedatacallback) to write audio data.
        
        ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b/v3/Lsr5ah2QSpmdujL45VzXVA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F81C4AA55E0C09E1711F7EC682BF78B2F8DD8C12A83FA120487416B5B7516782)
        
        -   When the amount of data is sufficient to meet the required buffer length of the callback, you should return **AUDIO\_DATA\_CALLBACK\_RESULT\_VALID**, and the system uses the entire data buffer for playback. Do not return **AUDIO\_DATA\_CALLBACK\_RESULT\_VALID** in this case, as this leads to audio artifacts such as noise and playback stuttering.
            
        -   When the amount of data is insufficient to meet the required buffer length of the callback, you are advised to return **AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID**. In this case, the system does not process this portion of audio data but requests data from the application again. Once the buffer is adequately filled, you can return **AUDIO\_DATA\_CALLBACK\_RESULT\_VALID**.
            
        -   Once the callback function finishes its execution, the audio service queues the data in the buffer for playback. Therefore, do not change the buffered data outside the callback. Regarding the last frame, if there is insufficient data to completely fill the buffer, you must concatenate the available data with padding to ensure that the buffer is full. This prevents any residual dirty data in the buffer from adversely affecting the playback effect.
            
        
    -   Starting from API version 12, you can call [OH\_AudioStreamBuilder\_SetFrameSizeInCallback](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setframesizeincallback) to set **audioDataSize**.
        
    
    // Customize a data writing function.
    OH\_AudioData\_Callback\_Result MyOnWriteData(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        void\* audioData,
        int32\_t audioDataSize)
    {
        // Write the data to be played to audioData by audioDataSize.
        // If you do not want to play a segment of audioData, return AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID.
        return AUDIO\_DATA\_CALLBACK\_RESULT\_VALID;
    }
    // Customize an audio interruption event function.
    void MyOnInterruptEvent(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        OH\_AudioInterrupt\_ForceType type,
        OH\_AudioInterrupt\_Hint hint)
    {
        // Update the player status and UI based on the audio interruption information indicated by type and hint.
    }
    // Customize an exception callback function.
    void MyOnError(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        OH\_AudioStream\_Result error)
    {
        // Perform operations based on the audio exception information indicated by error.
    }
    
    // Configure the callback function for interruption events.
    OH\_AudioRenderer\_OnInterruptCallback onInterruptCb = MyOnInterruptEvent;
    OH\_AudioStreamBuilder\_SetRendererInterruptCallback(builder, onInterruptCb, nullptr);
    
    // Configure the callback function for audio exceptions.
    OH\_AudioRenderer\_OnErrorCallback onErrorCb = MyOnError;
    OH\_AudioStreamBuilder\_SetRendererErrorCallback(builder, onErrorCb, nullptr);
    
    // Configure the callback function for writing audio data.
    OH\_AudioRenderer\_OnWriteDataCallback onWriteDataCb = MyOnWriteData;
    OH\_AudioStreamBuilder\_SetRendererWriteDataCallback(builder, onWriteDataCb, nullptr);
    
4.  Create an audio renderer instance.
    
    OH\_AudioRenderer\* audioRenderer;
    OH\_AudioStreamBuilder\_GenerateRenderer(builder, &audioRenderer);
    
5.  Use the audio renderer.
    
    You can use the APIs listed below to control the audio streams.
    
    | API | Description |
    | :-- | :-- |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Start(OH\_AudioRenderer\* renderer) | Starts the audio renderer. |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Pause(OH\_AudioRenderer\* renderer) | Pauses the audio renderer. |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Stop(OH\_AudioRenderer\* renderer) | Stops the audio renderer. |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Flush(OH\_AudioRenderer\* renderer) | Flushes obtained audio data. |
    | OH\_AudioStream\_Result OH\_AudioRenderer\_Release(OH\_AudioRenderer\* renderer) | Releases the audio renderer instance. |
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/3olqmEi9RbSTvbGL9ETH-w/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E74115DE32F117304CAEAF0E89AC7CF765630DCD5DEF4C0FB28933532A7B9E0E)
    
    The execution of audio stream control APIs is time-consuming (for example, a single execution of **OH\_AudioRenderer\_Stop** generally takes more than 50 ms as it needs to play through the cache). Direct calls to these APIs on the main thread should be avoided to prevent interface display freezes.
    
6.  Destroy the audio stream builder.
    
    When the builder is no longer used, release related resources.
    
    Applications must properly manage builders according to their needs, creating them as needed and releasing them promptly. This prevents excessive consumption of audio resources, which can lead to exceptions.
    
    OH\_AudioStreamBuilder\_Destroy(builder);
    

## Setting the Volume for an Audio Stream

You can use [OH\_AudioRenderer\_SetVolume](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_setvolume) to set the volume for the current audio stream.

// Volume to set. The value range is \[0.0, 1.0\].
float volume = 0.5f;

// Set the volume for the audio stream.
OH\_AudioStream\_Result OH\_AudioRenderer\_SetVolume(audioRenderer, volume);

## Setting the Low Latency Mode

If the device supports the low-latency channel and the sampling rate is set to 48000 Hz, you can use the low-latency mode to create a player for a higher-quality audio experience.

The development process is similar to that in the common playback scenario (described in [Implementing Audio Playback](#implementing-audio-playback)). The only difference is that you need to set the low delay mode by calling [OH\_AudioStreamBuilder\_SetLatencyMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setlatencymode) when creating an audio stream builder in step 1.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/mZXv9aMYT7KHTN9cJV8C4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062033Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC9D622A1B34912A3CCC12FBBD9AAD10D81115A69E046F0A866683A1A48093ED)

-   In audio playback scenarios, if [OH\_AudioStream\_Usage](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_usage) is set to **AUDIOSTREAM\_USAGE\_VOICE\_COMMUNICATION** or **AUDIOSTREAM\_USAGE\_VIDEO\_COMMUNICATION**, the low-latency mode cannot be set. The system determines the output audio channel based on the device capability.
-   The low-latency mode requires robust data processing capabilities. If your application generates data slowly, it may lead to lag. Therefore, for typical music and video playback, this mode is not recommended. It is best suited for applications that are sensitive to latency, such as gaming and karaoke.

OH\_AudioStreamBuilder\_SetLatencyMode(builder, AUDIOSTREAM\_LATENCY\_MODE\_FAST);

## Setting the Audio Channel Layout

In the case of audio file playback, you can set the audio channel layout to specify the speaker position during rendering or playing for a better audio experience.

The development process is similar to that in the common playback scenario (described in [Implementing Audio Playback](#implementing-audio-playback)). The only difference is that you need to set the audio channel layout by calling [OH\_AudioStreamBuilder\_SetChannelLayout()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setchannellayout) when creating an audio stream builder in step 1.

If the audio channel layout does not match the number of audio channels, audio streams fail to be created. Therefore, you must ensure that the audio channel layout setting is correct.

If you do not know the accurate audio channel layout or you want to use the default audio channel layout, do not call the API to set the audio channel layout. Alternatively, deliver **CH\_LAYOUT\_UNKNOWN** to use the default audio channel layout, which is specific to the number of audio channels.

For audio in Higher Order Ambisonics (HOA) format, to obtain the correct rendering and playback effect, you must specify the audio channel layout.

OH\_AudioStreamBuilder\_SetChannelLayout(builder, CH\_LAYOUT\_STEREO);

## Playing Audio Files in Audio Vivid Format

In the case of audio file playback in Audio Vivid format, the callback function used for writing data is different from that in the common playback scenario. This callback function can write Pulse Code Modulation (PCM) data and metadata at the same time.

The development process is similar to that in the common playback scenario (described in [Implementing Audio Playback](#implementing-audio-playback)). The only difference is that you need to call [OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setwritedatawithmetadatacallback) to set the callback function and call [OH\_AudioStreamBuilder\_SetEncodingType()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setencodingtype) to set the encoding type to **AUDIOSTREAM\_ENCODING\_TYPE\_AUDIOVIVID** when creating an audio stream builder in step 1.

When an audio file in Audio Vivid format is played, the frame size is fixed. Therefore, do not call [OH\_AudioStreamBuilder\_SetFrameSizeInCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setframesizeincallback) to set the frame size in the callback. In addition, when setting the number of audio channels and the audio channel layout, use the sum of the number of sound beds written into the audio source and the number of objects.

// Customize a callback function for simultaneously writing PCM data and metadata.
int32\_t MyOnWriteDataWithMetadata(
    OH\_AudioRenderer\* renderer,
    void\* userData,
    void\* audioData,
    int32\_t audioDataSize,
    void\* metadata,
    int32\_t metadataSize)
{
    // Write the PCM data and metadata to be played to the buffer by audioDataSize and metadataSize, respectively.
    return 0;
}

// Set the encoding type.
OH\_AudioStreamBuilder\_SetEncodingType(builder, AUDIOSTREAM\_ENCODING\_TYPE\_AUDIOVIVID);
// Set the callbacks.
OH\_AudioRenderer\_WriteDataWithMetadataCallback metadataCallback = MyOnWriteDataWithMetadata;
// Set the callback function for writing both PCM data and metadata.
OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback(builder, metadataCallback, nullptr);

#### Precautions

Starting from API version 12, the [OH\_AudioRenderer\_Callbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct) API is no longer recommended for setting audio callback functions. If this API must be used, you should ensure that the audio callback function is set properly to avoid unexpected behavior. You can do this in one of two ways:

-   Initialize each callback in [OH\_AudioRenderer\_Callbacks](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiorenderer-callbacks-struct) by a custom callback method or a null pointer.
    
    // Customize a data writing function.
    int32\_t MyOnWriteData(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        void\* buffer,
        int32\_t length)
    {
        // Write the data to be played to the buffer by length.
        return 0;
    }
    // Customize an audio interruption event function.
    int32\_t MyOnInterruptEvent(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        OH\_AudioInterrupt\_ForceType type,
        OH\_AudioInterrupt\_Hint hint)
    {
        // Update the player status and UI based on the audio interruption information indicated by type and hint.
        return 0;
    }
    
    OH\_AudioRenderer\_Callbacks callbacks;
    
    // Configure a callback function. If listening is required, assign a value.
    callbacks.OH\_AudioRenderer\_OnWriteData = MyOnWriteData;
    callbacks.OH\_AudioRenderer\_OnInterruptEvent = MyOnInterruptEvent;
    
    // (Mandatory) For scenarios where no callback is triggered, initialize with a null pointer. Starting from API version 11, if you need to listen for device changes, use OH\_AudioRenderer\_OutputDeviceChangeCallback instead.
    callbacks.OH\_AudioRenderer\_OnStreamEvent = nullptr;
    // (Mandatory) If listening is not required, use a null pointer for initialization.
    callbacks.OH\_AudioRenderer\_OnError = nullptr;
    
-   Initialize and clear the struct before using it.
    
    // Customize a data writing function.
    int32\_t MyOnWriteData(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        void\* buffer,
        int32\_t length)
    {
        // Write the data to be played to the buffer by length.
        return 0;
    }
    // Customize an audio interruption event function.
    int32\_t MyOnInterruptEvent(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        OH\_AudioInterrupt\_ForceType type,
        OH\_AudioInterrupt\_Hint hint)
    {
        // Update the player status and UI based on the audio interruption information indicated by type and hint.
        return 0;
    }
    OH\_AudioRenderer\_Callbacks callbacks;
    
    // Initialize and clear the struct before using it.
    memset(&callbacks, 0, sizeof(OH\_AudioRenderer\_Callbacks));
    
    // Configure the required callback functions.
    callbacks.OH\_AudioRenderer\_OnWriteData = MyOnWriteData;
    callbacks.OH\_AudioRenderer\_OnInterruptEvent = MyOnInterruptEvent;
