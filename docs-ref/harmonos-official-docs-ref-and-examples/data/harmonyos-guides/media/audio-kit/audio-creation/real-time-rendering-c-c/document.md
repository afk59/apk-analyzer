# Real-Time Rendering (C/C++)

Starting from API version 22, [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite) provides real-time audio rendering capabilities, allowing for custom audio effects (only equalizer nodes supported) during real-time audio playback. For example, you can use the preset effects in the equalizer to change the style of the music.

#### Basic Development Configuration

To use the real-time rendering capabilities provided by [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite), add the corresponding header files.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC libohaudio.so libohaudiosuite.so)

## Adding Header Files

To use APIs related to audio creation and playback, include the <[native\_audio\_suite\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h)\>, <[native\_audio\_suite\_engine.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h)\>, <[native\_audiostreambuilder.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiostreambuilder-h)\>, and <[native\_audiorenderer.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audiorenderer-h)\> header files.

#include <ohaudiosuite/native\_audio\_suite\_base.h>
#include <ohaudiosuite/native\_audio\_suite\_engine.h>
#include <ohaudio/native\_audiorenderer.h>
#include <ohaudio/native\_audiostreambuilder.h>

#### How to Develop

## Calling Interfaces

For details on the APIs, see [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite).

## Equalizer Effect

**Figure 1** Real-time playback

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/96/v3/q1EXC5HoTkaxx_vpr94CLQ/en-us_image_0000002568684873.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=27BAAC2929C349D198A1B1504E6AD750BD4987E5983935C26F07C61C507121D6)

The following walks you through how to implement a simple equalizer effect node for real-time playback.

1.  Initialize and create an [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite) pipeline (including the input node, equalizer node, and output node).
    
    struct AudioDataInfo {
        uint8\_t \*buffer = nullptr;  // Audio data.
        int32\_t bufferSize = 0;     // Total size of the audio data.
        int32\_t totalWriteSize = 0; // Total size of the processed audio data.
    };
    
    // Callback function for the input node to request data.
    static int32\_t InputNodeWriteDataCallBack(
        OH\_AudioNode \*audioNode,
        void \*userData,
        void \*audioData,
        int32\_t audioDataSize,
        bool \*finished)
    {
        if ((audioNode == nullptr) || (userData == nullptr) ||
            (audioData == nullptr) || (audioDataSize <= 0) || (finished == nullptr)) {
            return -1;
        }
    
        struct AudioDataInfo \*info = static\_cast<struct AudioDataInfo \*>(userData);
        // Size of the audio data to be processed.
        int32\_t actualDataSize = std::min(audioDataSize, info->bufferSize - info->totalWriteSize);
        // Write the PCM audio data into audioData.
        memcpy(static\_cast<void \*>(audioData), info->buffer + info->totalWriteSize, actualDataSize);
        info->totalWriteSize += actualDataSize;
    
        // All audio data has been processed.
        if (info->totalWriteSize >= info->bufferSize) {
            \*finished = true;
        }
        return actualDataSize;
    }
    
    // Create an engine.
    OH\_AudioSuiteEngine \*audioSuiteEngine = nullptr;
    OH\_AudioSuiteEngine\_Create(&audioSuiteEngine);
    
    // Create a real-time rendering pipeline.
    OH\_AudioSuitePipeline \*audioSuitePipeline;
    OH\_AudioSuiteEngine\_CreatePipeline(audioSuiteEngine, &audioSuitePipeline,
        OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_REALTIME\_MODE);
    
    // Create a node builder.
    OH\_AudioNodeBuilder \*nodeBuilder = nullptr;
    OH\_AudioSuiteNodeBuilder\_Create(&nodeBuilder);
    OH\_AudioSuiteNodeBuilder\_SetNodeType(nodeBuilder, OH\_AudioNode\_Type::INPUT\_NODE\_TYPE\_DEFAULT);
    
    // Configure the audio data format. Set the sample rate, channel layout, channel count, bit depth, and encoding type based on the audio data format to be processed.
    OH\_AudioFormat audioFormatInput;
    audioFormatInput.samplingRate = OH\_Audio\_SampleRate::SAMPLE\_RATE\_48000;
    audioFormatInput.channelLayout = OH\_AudioChannelLayout::CH\_LAYOUT\_STEREO;
    audioFormatInput.channelCount = 2;
    audioFormatInput.sampleFormat = OH\_Audio\_SampleFormat::AUDIO\_SAMPLE\_S16LE;
    audioFormatInput.encodingType = OH\_Audio\_EncodingType::AUDIO\_ENCODING\_TYPE\_RAW;
    OH\_AudioSuiteNodeBuilder\_SetFormat(nodeBuilder, audioFormatInput);
    // Set the callback for the audio stream.
    struct AudioDataInfo audioInfo;
    audioInfo.buffer = nullptr; // Store the audio data to be processed based on the service scenario.
    audioInfo.bufferSize = 0; // Store the size of the audio data to be processed based on the service scenario.
    audioInfo.totalWriteSize = 0;
    void \*userData = static\_cast<void \*>(&audioInfo);
    OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
    // Create an input node.
    OH\_AudioNode \*inputNode = nullptr;
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &inputNode);
    
    // Reset the builder configuration and set the node type to equalizer.
    OH\_AudioSuiteNodeBuilder\_Reset(nodeBuilder);
    OH\_AudioSuiteNodeBuilder\_SetNodeType(nodeBuilder, OH\_AudioNode\_Type::EFFECT\_NODE\_TYPE\_EQUALIZER);
    // Create an equalizer node.
    OH\_AudioNode \*eqNode = nullptr;
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &eqNode);
    // Set the effect of the equalizer node to the default value.
    OH\_AudioSuiteEngine\_SetEqualizerFrequencyBandGains(eqNode, OH\_EQUALIZER\_PARAM\_DEFAULT);
    
    // Reset the builder configuration and set the node type to output.
    OH\_AudioSuiteNodeBuilder\_Reset(nodeBuilder);
    OH\_AudioSuiteNodeBuilder\_SetNodeType(nodeBuilder, OH\_AudioNode\_Type::OUTPUT\_NODE\_TYPE\_DEFAULT);
    // Configure the audio data format. Set the sample rate, channel layout, channel count, bit depth, and encoding type based on the expected audio output format.
    OH\_AudioFormat audioFormatOutput;
    audioFormatOutput.samplingRate = OH\_Audio\_SampleRate::SAMPLE\_RATE\_48000;
    audioFormatOutput.channelLayout = OH\_AudioChannelLayout::CH\_LAYOUT\_STEREO;
    audioFormatOutput.channelCount = 2;
    audioFormatOutput.sampleFormat = OH\_Audio\_SampleFormat::AUDIO\_SAMPLE\_S16LE;
    audioFormatOutput.encodingType = OH\_Audio\_EncodingType::AUDIO\_ENCODING\_TYPE\_RAW;
    OH\_AudioSuiteNodeBuilder\_SetFormat(nodeBuilder, audioFormatOutput);
    // Create an output node.
    OH\_AudioNode \*outputNode = nullptr;
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &outputNode);
    
    // Destroy the node builder.
    OH\_AudioSuiteNodeBuilder\_Destroy(nodeBuilder);
    
    // Connect the nodes to form a network.
    OH\_AudioSuiteEngine\_ConnectNodes(inputNode, eqNode);
    OH\_AudioSuiteEngine\_ConnectNodes(eqNode, outputNode);
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Kao-vlU5RVeJU1xFm1MeNg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=78BB5B5F323D0B4C81B0B41BE4EABD9AFE6BAFFEB7F70FB9F1A6701FFCACF1B5)
    
    Offline editing and real-time rendering differ in pipeline creation.
    
    -   Real-time rendering: OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_REALTIME\_MODE
    -   Offline editing: OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_EDIT\_MODE
    
2.  Create an [OH\_AudioRendererStruct](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudio-oh-audiorendererstruct) instance, and call [OH\_AudioSuiteEngine\_RenderFrame()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_renderframe) of the OHAudioSuite pipeline in its **AudioRendererOnWriteData()** callback function to process the data.
    
    For details about how to develop audio playback, see [Using OHAudio for Audio Playback (C/C++)](../../audio-playback/recommended-using-ohaudio-for-audio-playback-c-c/document.md).
    
3.  In the callback function of the player, copy the processed data to the buffer of the OH\_AudioRenderer instance to implement real-time rendering during audio playback.
    
    static OH\_AudioData\_Callback\_Result AudioRendererOnWriteData(
        OH\_AudioRenderer\* renderer,
        void\* userData,
        void\* audioData,
        int32\_t audioDataSize)
    {
        bool finishedFlag = false;
        int32\_t writeSize = 0;
        OH\_AudioSuite\_Result result = OH\_AudioSuiteEngine\_RenderFrame(
            static\_cast<OH\_AudioSuitePipeline \*>(userData), audioData, audioDataSize, &writeSize, &finishedFlag);
        if (result != OH\_AudioSuite\_Result::AUDIOSUITE\_SUCCESS) {
            // The audio creation rendering fails.
            return AUDIO\_DATA\_CALLBACK\_RESULT\_INVALID;
        }
        // The audio creation rendering is complete.
        if (finishedFlag) {
            // Developer-defined behavior.
        }
    
        return AUDIO\_DATA\_CALLBACK\_RESULT\_VALID;
     }
    
    // Create a builder.
    OH\_AudioStreamBuilder \*rendererBuilder = nullptr;
    OH\_AudioStreamBuilder\_Create(&rendererBuilder, OH\_AudioStream\_Type::AUDIOSTREAM\_TYPE\_RENDERER);
    OH\_AudioStreamBuilder\_SetSamplingRate(rendererBuilder, 48000);
    OH\_AudioStreamBuilder\_SetChannelCount(rendererBuilder, 2);
    OH\_AudioStreamBuilder\_SetSampleFormat(rendererBuilder, AUDIOSTREAM\_SAMPLE\_S16LE);
    OH\_AudioStreamBuilder\_SetEncodingType(rendererBuilder, AUDIOSTREAM\_ENCODING\_TYPE\_RAW);
    OH\_AudioStreamBuilder\_SetRendererInfo(rendererBuilder, AUDIOSTREAM\_USAGE\_MUSIC);
    
    int32\_t byteSize = 2; // Byte size of the data corresponding to the AUDIOSTREAM\_SAMPLE\_S16LE format.
    // 1000 is the time conversion unit. 20 indicates 20 ms of audio sampling data. If samplingRate is 11025, use 40 ms for calculation.
    int32\_t frameSize = 20 \* audioFormatOutput.samplingRate \* audioFormatOutput.channelCount \* byteSize / 1000;
    // Set audioDataSize (size of the data to be played).
    OH\_AudioStreamBuilder\_SetFrameSizeInCallback(rendererBuilder, frameSize);
    // Configure the callback function for writing audio data.
    OH\_AudioStreamBuilder\_SetRendererWriteDataCallback(
        rendererBuilder, AudioRendererOnWriteData, static\_cast<void \*>(audioSuitePipeline));
    
    // Start the pipeline.
    OH\_AudioSuiteEngine\_StartPipeline(audioSuitePipeline);
    
    // Create a renderer stream to play audio.
    // ...
    
    // Stop the pipeline.
    OH\_AudioSuiteEngine\_StopPipeline(audioSuitePipeline);
    
4.  Destroy resources.
    
    // Destroy the stream builder.
    OH\_AudioStreamBuilder\_Destroy(rendererBuilder);
    
    // Destroy the nodes.
    OH\_AudioSuiteEngine\_DestroyNode(inputNode);
    OH\_AudioSuiteEngine\_DestroyNode(eqNode);
    OH\_AudioSuiteEngine\_DestroyNode(outputNode);
    
    // Destroy the pipeline.
    OH\_AudioSuiteEngine\_DestroyPipeline(audioSuitePipeline);
    
    // Destroy the engine.
    OH\_AudioSuiteEngine\_Destroy(audioSuiteEngine);
    

#### Precautions

-   During real-time audio rendering, you cannot create effect nodes. However, you can modify the parameters of nodes that already exist.
    
-   For details about error codes, see [OH\_AudioSuite\_Result](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audiosuite_result).
