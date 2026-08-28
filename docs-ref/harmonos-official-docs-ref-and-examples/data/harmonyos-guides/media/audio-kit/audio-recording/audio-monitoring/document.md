# Audio Monitoring

Audio monitoring enables real-time transmission of audio to headphones, allowing users to hear themselves or other relevant sounds in real time.

This feature is commonly used in karaoke applications, where the recorded vocals and background music are sent to the headphones in real time. This allows users to adjust their performance based on the feedback, enhancing their experience.

#### Prerequisites

-   You can use the playback and recording capabilities provided by OHAudio to implement audio monitoring. The audio data captured during recording is used as the input for playback.
    
    For details, please refer to [(Recommended) Using OHAudio for Audio Playback (C/C++)](../../audio-playback/recommended-using-ohaudio-for-audio-playback-c-c/document.md) and [(Recommended) Using OHAudio for Audio Recording (C/C++)](../recommended-using-ohaudio-for-audio-recording-c-c/document.md).
    
-   Currently, audio monitoring is only supported through wired headphones, where audio is both captured and played back.
    

#### How to Develop

## Creating an Audio Recording Builder

Use the **OH\_AudioStreamBuilder** function provided by OHAudio to create an audio recording builder, following the builder design pattern. Set [OH\_AudioStream\_Type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_type) to **AUDIOSTREAM\_TYPE\_CAPTURER**.

OH\_AudioStreamBuilder\* builder;
OH\_AudioStreamBuilder\_Create(&builder, AUDIOSTREAM\_TYPE\_CAPTURER);

## Creating an Audio Playback Builder

Use the **OH\_AudioStreamBuilder** function provided by **OHAudio** to create an audio playback builder, following the builder design pattern. Set [OH\_AudioStream\_Type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostream-base-h#oh_audiostream_type) to **AUDIOSTREAM\_TYPE\_RENDERER**.

OH\_AudioStreamBuilder\* builder;
OH\_AudioStreamBuilder\_Create(&builder, AUDIOSTREAM\_TYPE\_RENDERER);

## Setting the Low Latency Mode

To achieve better audio monitoring, it is essential to maintain low latency from recording to playback. When the device supports low-latency channels, you should use the low latency mode for both recording and playback.

When creating the audio recording builder, call [OH\_AudioStreamBuilder\_SetLatencyMode()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h#oh_audiostreambuilder_setlatencymode) to set the low latency mode, and apply it to both recording and playback as follows:

OH\_AudioStream\_LatencyMode latencyMode = AUDIOSTREAM\_LATENCY\_MODE\_FAST;
OH\_AudioStreamBuilder\_SetLatencyMode(builder, latencyMode);

To implement real-time audio monitoring, create a shared buffer to store the captured data and promptly retrieve data from this buffer to write to the audio playback builder.

## Defining the Shared Buffer and Recording/Playback Functions

// Create a shared buffer to store captured data and retrieve playback data.

// Customize a function to read captured data.
    int32\_t MyOnReadData(
        OH\_AudioCapturer\* capturer,
        void\* userData,
        void\* buffer,
        int32\_t length)
    {
        // Extract captured data with the specified length from the buffer and place the data in the shared buffer for the renderer to read.
        return 0;
    }

    // Customize a function to write data.
    int32\_t MyOnWriteData(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        void\* buffer,
        int32\_t length)
    {
        // Read data from the shared buffer and write the data with the specified length into the buffer.
        return 0;
    }

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/dd/v3/eWnsqOzvRXi5j03iXAdKsA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0625541CE541AD2ED8FDCCC3CC3B44770E60B0B553CA18CA8DDEBE103439C2F4)

Avoid setting the shared buffer too large, as it can increase audio feedback latency and degrade user experience. You should select a proper buffer size that balances latency and jitter tolerance to maintain optimal performance.

## Setting Audio Stream Parameters

The following provides an example of setting parameters for the audio recording stream:

// Set the audio sampling rate.
OH\_AudioStreamBuilder\_SetSamplingRate(builder, 48000);
// Set the number of audio channels.
OH\_AudioStreamBuilder\_SetChannelCount(builder, 2);
// Set the audio sampling format.
OH\_AudioStreamBuilder\_SetSampleFormat(builder, AUDIOSTREAM\_SAMPLE\_S16LE);
// Set the encoding type of the audio stream.
OH\_AudioStreamBuilder\_SetEncodingType(builder, AUDIOSTREAM\_ENCODING\_TYPE\_RAW);
// Set the usage scenario of the audio renderer.
OH\_AudioStreamBuilder\_SetRendererInfo(builder, AUDIOSTREAM\_SOURCE\_TYPE\_MIC);

For the playback stream, set the same parameters as the recording stream, except for the working scenario.

Set the working scenario parameter as follows:

OH\_AudioStreamBuilder\_SetRendererInfo(builder, AUDIOSTREAM\_USAGE\_MUSIC);

## Setting Recording Callback Functions

// Customize a function to read data.
int32\_t MyOnReadData(
    OH\_AudioCapturer\* capturer,
    void\* userData,
    void\* buffer,
    int32\_t length)
{
    // Obtain captured data of the specified length from the buffer.
    return 0;
}
// Customize an audio stream event function.
int32\_t MyOnStreamEvent(
    OH\_AudioCapturer\* capturer,
    void\* userData,
    OH\_AudioStream\_Event event)
{
    // Update the capturer status and UI based on the audio stream event information indicated by the event.
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
// Customize an exception callback function.
int32\_t MyOnError(
    OH\_AudioCapturer\* capturer,
    void\* userData,
    OH\_AudioStream\_Result error)
{
    // Perform operations based on the audio exception information indicated by error.
    return 0;
}

OH\_AudioCapturer\_Callbacks callbacks;

// Set the callbacks.
callbacks.OH\_AudioCapturer\_OnReadData = MyOnReadData;
callbacks.OH\_AudioCapturer\_OnStreamEvent = MyOnStreamEvent;
callbacks.OH\_AudioCapturer\_OnInterruptEvent = MyOnInterruptEvent;
callbacks.OH\_AudioCapturer\_OnError = MyOnError;

// Set the callbacks for audio input streams.
OH\_AudioStreamBuilder\_SetCapturerCallback(builder, callbacks, nullptr);

## Setting Playback Callback Functions

    // Customize a function to write data.
    int32\_t MyOnWriteData(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        void\* buffer,
        int32\_t length)
    {
        // Read data from the shared buffer and write the data with the specified length into the buffer.
        return 0;
    }
    // Customize an audio stream event function.
    int32\_t MyOnStreamEvent(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        OH\_AudioStream\_Event event)
    {
        // Update the player status and UI based on the audio stream event information indicated by the event.
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
    // Customize an exception callback function.
    int32\_t MyOnError(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        OH\_AudioStream\_Result error)
    {
        // Perform operations based on the audio exception information indicated by error.
        return 0;
    }

    OH\_AudioRenderer\_Callbacks callbacks;

    // Set the callbacks.
    callbacks.OH\_AudioRenderer\_OnWriteData = MyOnWriteData;
    callbacks.OH\_AudioRenderer\_OnStreamEvent = MyOnStreamEvent;
    callbacks.OH\_AudioRenderer\_OnInterruptEvent = MyOnInterruptEvent;
    callbacks.OH\_AudioRenderer\_OnError = MyOnError;

    // Set callbacks for the audio renderer.
    OH\_AudioStreamBuilder\_SetRendererCallback(builder, callbacks, nullptr);

## Creating an Audio Capturer

OH\_AudioCapturer\* audioCapturer;
OH\_AudioStreamBuilder\_GenerateCapturer(builder, &audioCapturer);

## Creating an Audio Renderer

OH\_AudioRenderer\* audioRenderer;
OH\_AudioStreamBuilder\_GenerateRenderer(builder, &audioRenderer);

## Using Audio Streams

The following uses recording as an example. You can use the following APIs to control the start, pause, stop, and release of audio streams.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/47/v3/Cmp2OhtRQUuaxYNUqeSRNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062034Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=C708768B9F6F77DB4FD9957F2540C7A9BB26DC5BE06524D9AA353F7AD4C856DD)

When implementing audio monitoring, you need to control both the recording and playback streams to ensure their synchronization.

| API | Description |
| :-- | :-- |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Start](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_start)(OH\_AudioRenderer\* renderer) | Starts the audio renderer. |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Pause](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_pause)(OH\_AudioRenderer\* renderer) | Pauses the audio renderer. |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Stop](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_stop)(OH\_AudioRenderer\* renderer) | Stops the audio renderer. |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Flush](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_flush)(OH\_AudioRenderer\* renderer) | Flushes obtained audio data. |
| OH\_AudioStream\_Result [OH\_AudioRenderer\_Release](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h#oh_audiorenderer_release)(OH\_AudioRenderer\* renderer) | Releases the audio renderer. |

## Releasing the Builder

When the builder is no longer required, release the resources as follows:

OH\_AudioStreamBuilder\_Destroy(builder);
