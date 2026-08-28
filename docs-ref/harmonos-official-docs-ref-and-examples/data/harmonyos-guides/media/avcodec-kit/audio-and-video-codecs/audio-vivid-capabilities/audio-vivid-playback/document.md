# Audio Vivid Playback

After obtaining the decoded PCM data and metadata, call the related playback APIs of **OHAudio** to render and play the audio source in the Audio Vivid format. For details about the APIs, see [OHAudio API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio).

#### Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC libohaudio.so)

#### Adding Header Files

#include <ohaudio/native\_audiorenderer.h>
#include <ohaudio/native\_audiostreambuilder.h>

#### How to Develop

The following walks you through how to implement simple playback.

1.  Create an audio stream builder.
    
    **OHAudio** provides the **OH\_AudioStreamBuilder** class, which complies with the builder design pattern and is used to build audio streams. In the Audio Vivid playback scenario, set **OH\_AudioStream\_Type** to **AUDIOSTREAM\_TYPE\_RENDERER** to create an audio stream builder of the rendering playback type.
    
    OH\_AudioStreamBuilder\* builder;
    OH\_AudioStreamBuilder\_Create(&builder, AUDIOSTREAM\_TYPE\_RENDERER);
    
2.  Set audio stream parameters.
    
    After creating the builder for audio playback, set the parameters required.
    
    The Audio Vivid audio source works with the system spatial audio rendering algorithms to provide an optimal playback effect and experience. The system selects the corresponding spatial audio rendering effect based on the working scenario (specified by **OH\_AudioStream\_Usage**) of the output audio stream. Currently, the supported working scenarios include music, movie, and audiobook.
    
    // Set the audio sampling rate to 48000 Hz.
    OH\_AudioStreamBuilder\_SetSamplingRate(builder, 48000);
    // Set the audio channel to 10. (Assume that the input Audio Vivid audio source is in the format of 5.1.2 sound bed + 2 objects.)
    OH\_AudioStreamBuilder\_SetChannelCount(builder, 10);
    // Set the audio channel layout to 5.1.2. (Only the sound bed is considered for the audio channel layout. To use the default audio channel layout, pass in CH\_LAYOUT\_UNKNOWN.)
    OH\_AudioStreamBuilder\_SetChannelLayout(builder, CH\_LAYOUT\_5POINT1POINT2);
    // Set the audio sampling format.
    OH\_AudioStreamBuilder\_SetSampleFormat(builder, AUDIOSTREAM\_SAMPLE\_S16LE);
    // Set the encoding type of the audio stream to Audio Vivid.
    OH\_AudioStreamBuilder\_SetEncodingType(builder, AUDIOSTREAM\_ENCODING\_TYPE\_AUDIOVIVID);
    // Set the working scenario of the output audio stream. Select the music, movie, or audiobook type based on the actual working scenario.
    OH\_AudioStreamBuilder\_SetRendererInfo(builder, AUDIOSTREAM\_USAGE\_MUSIC);
    
3.  Set the callback functions.
    
    **OHAudio** uses the callback mode to write audio stream data and report audio events. Your application can select the audio events to listen for as required.
    
    // Customize an audio stream event function.
    int32\_t MyOnStreamEvent(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        OH\_AudioStream\_Event event)
    {
        // Update the renderer status and UI based on the audio stream event information indicated by the event.
        return 0;
    }
    // Customize an audio interruption event function.
    int32\_t MyOnInterruptEvent(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        OH\_AudioInterrupt\_ForceType type,
        OH\_AudioInterrupt\_Hint hint)
    {
        // Update the renderer status and UI based on the audio interruption information indicated by type and hint.
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
    
    Call the registration API of the system to configure the callback functions defined above.
    
    To avoid unexpected behavior, ensure that every callback in **OH\_AudioRenderer\_Callbacks** is initialized by a custom callback method or a null pointer when setting the audio callback functions.
    
    In the Audio Vivid playback scenario, **OH\_AudioRenderer\_WriteDataWithMetadataCallback** must be used to write PCM data and metadata.
    
    // Set the callbacks.
    OH\_AudioRenderer\_Callbacks callbacks;
    // During Audio Vivid playback, this callback function can be left empty and data can be written in metadata callback mode.
    callbacks.OH\_AudioRenderer\_OnWriteData = nullptr;
    // Listen for the audio stream event. If the event is not required, it can be assigned with nullptr.
    callbacks.OH\_AudioRenderer\_OnStreamEvent = MyOnStreamEvent;
    // Listen for the audio interruption event. If the event is not required, it can be assigned with nullptr.
    callbacks.OH\_AudioRenderer\_OnInterruptEvent = MyOnInterruptEvent;
    // Listen for the audio exception event. If the event is not required, it can be assigned with nullptr.
    callbacks.OH\_AudioRenderer\_OnError = MyOnError;
    
    // Set callbacks for the audio renderer.
    OH\_AudioStreamBuilder\_SetRendererCallback(builder, callbacks, nullptr);
    
    // Set the callbacks.
    OH\_AudioRenderer\_WriteDataWithMetadataCallback metadataCallback = MyOnWriteDataWithMetadata;
    // Set the callback function for writing both PCM data and metadata.
    OH\_AudioStreamBuilder\_SetWriteDataWithMetadataCallback(builder, metadataCallback, nullptr);
    
4.  Use the configured builder to construct an audio stream to be played.
    
    OH\_AudioRenderer\* audioRenderer;
    OH\_AudioStreamBuilder\_GenerateRenderer(builder, &audioRenderer);
    
5.  Use the audio stream.
    
    You can use the following APIs to control the audio stream and perform basic operations such as starting, pausing, and stopping playback, and clearing the buffer.
    
    When the audio stream is no longer used, the renderer instance can be released to better manage the memory.
    
    | 
    API
    
     | 
    
    Description
    
     |
    | :-- | :-- |
    | 
    
    OH\_AudioRenderer\_Start
    
     | 
    
    Starts playback.
    
     |
    | 
    
    OH\_AudioRenderer\_Pause
    
     | 
    
    Pauses playback.
    
     |
    | 
    
    OH\_AudioRenderer\_Stop
    
     | 
    
    Stops playback.
    
     |
    | 
    
    OH\_AudioRenderer\_Flush
    
     | 
    
    Flushes obtained audio data.
    
     |
    | 
    
    OH\_AudioRenderer\_Release
    
     | 
    
    Releases the audio renderer instance.
    
     |
    
6.  Destroy the audio stream builder.
    
    When the builder is no longer needed, release related resources.
    
    OH\_AudioStreamBuilder\_Destroy(builder);
