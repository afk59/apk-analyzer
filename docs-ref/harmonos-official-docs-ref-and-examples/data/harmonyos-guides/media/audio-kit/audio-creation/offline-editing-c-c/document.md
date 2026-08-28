# Offline Editing (C/C++)

Starting from API version 22, [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite) provides offline audio editing capabilities, allowing for audio data processing in non-real-time playback scenarios. You can combine multiple audio nodes to implement complex audio processing workflows.

#### Basic Development Configuration

To use the offline editing capabilities provided by [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite), add the corresponding header files.

## Linking the Dynamic Library in the CMake Script

target\_link\_libraries(sample PUBLIC libohaudiosuite.so)

## Adding Header Files

To use APIs related to audio creation, include the <[native\_audio\_suite\_base.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h)\> and <[native\_audio\_suite\_engine.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h)\> header files.

#include <ohaudiosuite/native\_audio\_suite\_base.h>
#include <ohaudiosuite/native\_audio\_suite\_engine.h>

#### How to Develop

For details on the APIs, see [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite).

This section describes how to implement offline audio editing.

## Specifying the Audio Node Type

Call [OH\_AudioSuiteNodeBuilder\_SetNodeType()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuitenodebuilder_setnodetype) to specify the [OH\_AudioNode\_Type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type) based on the service scenario.

## Specifying the Audio Node Format

Call [OH\_AudioSuiteNodeBuilder\_SetFormat()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuitenodebuilder_setformat) or [OH\_AudioSuiteEngine\_SetAudioFormat()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_setaudioformat) to set the audio format based on the service scenario. The audio format includes [bit depth](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_sampleformat), [sample rate](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate), and [channel count](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout).

## Basic Offline Editing

Use effect nodes (for example, equalizer effect node) to process the input Pulse Code Modulation (PCM) audio data and output PCM audio data with the applied audio effects.

**Figure 1** Basic offline editing

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/45/v3/2zewDyf9TJCxs-CPqfdYZA/en-us_image_0000002568764881.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08EBE123D2AFA55A40990763336FA7792408DA548E9204FE61111F488BA13A49)

1.  Create an engine and pipeline.
    
    // Create an engine.
    OH\_AudioSuiteEngine \*audioSuiteEngine = nullptr;
    OH\_AudioSuiteEngine\_Create(&audioSuiteEngine);
    
    // Create a pipeline.
    OH\_AudioSuitePipeline \*audioSuitePipeline = nullptr;
    OH\_AudioSuiteEngine\_CreatePipeline(
        audioSuiteEngine, &audioSuitePipeline, OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_EDIT\_MODE);
    
2.  Create input, output, and equalizer nodes and connect them.
    
    To create an input node, implement a custom callback function **InputNodeWriteDataCallBack** of the type [OH\_InputNode\_RequestDataCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_inputnode_requestdatacallback), and set the callback function using [OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuitenodebuilder_setrequestdatacallback).
    
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
    
3.  Render audio data.
    
    Call [OH\_AudioSuiteEngine\_RenderFrame()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_renderframe) to render and obtain PCM audio data.
    
    int32\_t byteSize = 2; // Byte size of the data corresponding to the OH\_Audio\_SampleFormat::AUDIO\_SAMPLE\_S16LE format.
    // Calculate the size of the data to be processed in a single frame based on the format of the output node.
    // 1000 is the time conversion unit. 20 indicates 20 ms of audio sampling data. If samplingRate is 11025, use 40 ms for calculation.
    int32\_t frameSize = 20 \* audioFormatOutput.samplingRate \* audioFormatOutput.channelCount \* byteSize / 1000;
    // Buffer used to receive the output audio data after rendering.
    uint8\_t \*audioData = (uint8\_t \*)malloc(frameSize);
    int32\_t responseSize = 0;
    bool finished = false;
    
    // Start rendering.
    OH\_AudioSuiteEngine\_StartPipeline(audioSuitePipeline);
    do {
        OH\_AudioSuite\_Result result = OH\_AudioSuiteEngine\_RenderFrame(
            audioSuitePipeline, static\_cast<void \*>(audioData), frameSize, &responseSize, &finished);
        if ((result != OH\_AudioSuite\_Result::AUDIOSUITE\_SUCCESS) || (responseSize <= 0)) {
            // The audio creation rendering fails.
            break;
        } else {
            // audioData is the rendered audio data. responseSize is the audio data length. You can use or save it as required.
        }
    } while (!finished);
    OH\_AudioSuiteEngine\_StopPipeline(audioSuitePipeline);
    free(audioData);
    audioData = nullptr;
    
4.  Destroy resources.
    
    // Destroy the nodes.
    OH\_AudioSuiteEngine\_DestroyNode(inputNode);
    OH\_AudioSuiteEngine\_DestroyNode(eqNode);
    OH\_AudioSuiteEngine\_DestroyNode(outputNode);
    
    // Destroy the pipeline.
    OH\_AudioSuiteEngine\_DestroyPipeline(audioSuitePipeline);
    
    // Destroy the engine.
    OH\_AudioSuiteEngine\_Destroy(audioSuiteEngine);
    

## Source Separation

Use a source separation node to separate input PCM audio data into vocal and background tracks, and then use an output node to output these tracks separately.

**Figure 2** Source separation editing

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e5/v3/4qhTUnnuSHeBOgc3JUq6_Q/en-us_image_0000002537765156.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=046A9C65B4222DC0C78D6AC4F17DCAC60ACCBB735ED8F70296FED222A8485629)

The sample code is as follows:

1.  Create an engine and pipeline.
    
    // Create an engine.
    OH\_AudioSuiteEngine \*audioSuiteEngine = nullptr;
    OH\_AudioSuiteEngine\_Create(&audioSuiteEngine);
    
    // Create a pipeline.
    OH\_AudioSuitePipeline \*audioSuitePipeline = nullptr;
    OH\_AudioSuiteEngine\_CreatePipeline(
        audioSuiteEngine, &audioSuitePipeline, OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_EDIT\_MODE);
    
2.  Create input, output, and source separation nodes and connect them.
    
    To create an input node, implement a custom callback function **InputNodeWriteDataCallBack** of the type [OH\_InputNode\_RequestDataCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_inputnode_requestdatacallback), and set the callback function using [OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuitenodebuilder_setrequestdatacallback).
    
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
    
    struct AudioDataInfo audioInfo;
    audioInfo.buffer = nullptr; // Store the audio data to be processed based on the service scenario.
    audioInfo.bufferSize = 0; // Store the size of the audio data to be processed based on the service scenario.
    audioInfo.totalWriteSize = 0;
    void \*userData = static\_cast<void \*>(&audioInfo);
    // Set the callback for the audio stream.
    OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
    
    // Create an input node.
    OH\_AudioNode \*inputNode = nullptr;
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &inputNode);
    
    // Reset the builder configuration and set the node type to source separation.
    OH\_AudioSuiteNodeBuilder\_Reset(nodeBuilder);
    OH\_AudioSuiteNodeBuilder\_SetNodeType(
        nodeBuilder, OH\_AudioNode\_Type::EFFECT\_MULTII\_OUTPUT\_NODE\_TYPE\_AUDIO\_SEPARATION);
    
    // Create a source separation node.
    OH\_AudioNode \*aissNode = nullptr;
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &aissNode);
    
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
    OH\_AudioSuiteEngine\_ConnectNodes(inputNode, aissNode);
    OH\_AudioSuiteEngine\_ConnectNodes(aissNode, outputNode);
    
3.  Render audio data.
    
    For the pipeline that contains the source separation node , use [OH\_AudioSuiteEngine\_MultiRenderFrame()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_multirenderframe) to render and obtain two streams of PCM audio data.
    
    int32\_t byteSize = 2; // Byte size of the data corresponding to the OH\_Audio\_SampleFormat::AUDIO\_SAMPLE\_S16LE format.
    // Calculate the size of the data to be processed in a single frame based on the format of the output node.
    // 1000 is the time conversion unit. 20 indicates 20 ms of audio sampling data. If samplingRate is 11025, use 40 ms for calculation.
    int32\_t frameSize = 20 \* audioFormatOutput.samplingRate \* audioFormatOutput.channelCount \* byteSize / 1000;
    // Buffer used to receive the output audio data after rendering.
    OH\_AudioDataArray audioDataArray;
    int32\_t outPutNum = 2;
    audioDataArray.audioDataArray = (void \*\*)malloc(outPutNum \* sizeof(void \*));
    for(int32\_t i = 0; i < outPutNum; i++) {
        audioDataArray.audioDataArray\[i\] = (void \*)malloc(frameSize);
    }
    audioDataArray.arraySize = outPutNum;
    audioDataArray.requestFrameSize = frameSize;
    int32\_t responseSize = 0;
    bool finished = false;
    
    // Start rendering.
    OH\_AudioSuiteEngine\_StartPipeline(audioSuitePipeline);
    do {
        OH\_AudioSuite\_Result result = OH\_AudioSuiteEngine\_MultiRenderFrame(
            audioSuitePipeline, &audioDataArray, &responseSize, &finished);
        if ((result != OH\_AudioSuite\_Result::AUDIOSUITE\_SUCCESS) || (responseSize <= 0)) {
            // The audio creation rendering fails.
            break;
        } else {
            // audioDataArray.audioDataArray\[0\] is the extracted vocal track.
            // audioDataArray.audioDataArray\[1\] is the extracted background track.
            // responseSize is the audio data length. You can use or save it as required.
        }
    } while (!finished);
    OH\_AudioSuiteEngine\_StopPipeline(audioSuitePipeline);
    
    for(int32\_t i = 0; i < outPutNum; i++) {
        free(audioDataArray.audioDataArray\[i\]);
        audioDataArray.audioDataArray\[i\] = nullptr;
    }
    free(audioDataArray.audioDataArray);
    audioDataArray.audioDataArray = nullptr;
    
4.  Destroy resources.
    
    // Destroy the nodes.
    OH\_AudioSuiteEngine\_DestroyNode(inputNode);
    OH\_AudioSuiteEngine\_DestroyNode(aissNode);
    OH\_AudioSuiteEngine\_DestroyNode(outputNode);
    
    // Destroy the pipeline.
    OH\_AudioSuiteEngine\_DestroyPipeline(audioSuitePipeline);
    
    // Destroy the engine.
    OH\_AudioSuiteEngine\_Destroy(audioSuiteEngine);
    

## Mixing and Cascading

Input multiple PCM audio data streams, mix them using an audio mixer node, and output the mixed PCM audio data.

**Figure 3** Cascading editing

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/16/v3/GBSqrQRTSoyuxwxB60eFGg/en-us_image_0000002537925096.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9BD88045CCCD855B75486A122F42BB2C6C07DA7CC9D99BE46447621DB0939BB7)

The sample code is as follows:

1.  Create an engine and pipeline.
    
    // Create an engine.
    OH\_AudioSuiteEngine \*audioSuiteEngine = nullptr;
    OH\_AudioSuiteEngine\_Create(&audioSuiteEngine);
    
    // Create a pipeline.
    OH\_AudioSuitePipeline \*audioSuitePipeline = nullptr;
    OH\_AudioSuiteEngine\_CreatePipeline(
        audioSuiteEngine, &audioSuitePipeline, OH\_AudioSuite\_PipelineWorkMode::AUDIOSUITE\_PIPELINE\_EDIT\_MODE);
    
2.  Create input, output, and effect nodes and connect them.
    
    The audio mixing functionality has multiple input nodes. You need to set the **userData** parameter in the callback function **InputNodeWriteDataCallBack** to distinguish between multiple input nodes, thereby enabling the input of multiple PCM audio data streams. The **InputNodeWriteDataCallBack** function type is [OH\_InputNode\_RequestDataCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_inputnode_requestdatacallback).
    
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
    // Set the callback for the first audio stream.
    struct AudioDataInfo audioInfoForField;
    audioInfoForField.buffer = nullptr; // Store the audio data to be processed based on the service scenario.
    audioInfoForField.bufferSize = 0; // Store the size of the audio data to be processed based on the service scenario.
    audioInfoForField.totalWriteSize = 0;
    void \*userData = static\_cast<void \*>(&audioInfoForField);
    OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
    // Create the first input node.
    OH\_AudioNode \*inputNodeForField = nullptr;
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &inputNodeForField);
    
    // Reset the builder configuration and set the node type to input.
    OH\_AudioSuiteNodeBuilder\_Reset(nodeBuilder);
    OH\_AudioSuiteNodeBuilder\_SetNodeType(nodeBuilder, OH\_AudioNode\_Type::INPUT\_NODE\_TYPE\_DEFAULT);
    OH\_AudioSuiteNodeBuilder\_SetFormat(nodeBuilder, audioFormatInput);
    // Set the callback for the second audio stream.
    struct AudioDataInfo audioInfoForMix;
    audioInfoForMix.buffer = nullptr; // Store the audio data to be processed based on the service scenario.
    audioInfoForMix.bufferSize = 0; // Store the size of the audio data to be processed based on the service scenario.
    audioInfoForMix.totalWriteSize = 0;
    userData = static\_cast<void \*>(&audioInfoForMix);
    OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback(nodeBuilder, InputNodeWriteDataCallBack, userData);
    // Create the second input node.
    OH\_AudioNode \*inputNodeForMix = nullptr;
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &inputNodeForMix);
    
    // Reset the builder configuration and set the node type to input.
    OH\_AudioSuiteNodeBuilder\_Reset(nodeBuilder);
    OH\_AudioSuiteNodeBuilder\_SetNodeType(nodeBuilder, OH\_AudioNode\_Type::EFFECT\_NODE\_TYPE\_SOUND\_FIELD);
    // Create a sound field node and set the sound field mode to listening.
    OH\_AudioNode \*fieldNode = nullptr;
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &fieldNode);
    OH\_AudioSuiteEngine\_SetSoundFieldType(fieldNode, SOUND\_FIELD\_FRONT\_FACING);
    
    // Reset the builder configuration and set the node type to input.
    OH\_AudioSuiteNodeBuilder\_Reset(nodeBuilder);
    OH\_AudioSuiteNodeBuilder\_SetNodeType(nodeBuilder, OH\_AudioNode\_Type::EFFECT\_NODE\_TYPE\_AUDIO\_MIXER);
    OH\_AudioNode \*mixerNode = nullptr;
    // Create a mixer node.
    OH\_AudioSuiteEngine\_CreateNode(audioSuitePipeline, nodeBuilder, &mixerNode);
    
    // Reset the builder configuration and set the node type to input.
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
    
    // Destroy the output node builder.
    OH\_AudioSuiteNodeBuilder\_Destroy(nodeBuilder);
    
    // Connect the nodes to form a network.
    OH\_AudioSuiteEngine\_ConnectNodes(inputNodeForField, fieldNode);
    OH\_AudioSuiteEngine\_ConnectNodes(fieldNode, mixerNode);
    OH\_AudioSuiteEngine\_ConnectNodes(inputNodeForMix, mixerNode);
    OH\_AudioSuiteEngine\_ConnectNodes(mixerNode, outputNode);
    
3.  Render audio data.
    
    Call [OH\_AudioSuiteEngine\_RenderFrame()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_renderframe) to render and obtain PCM audio data.
    
    int32\_t byteSize = 2; // Byte size of the data corresponding to the OH\_Audio\_SampleFormat::AUDIO\_SAMPLE\_S16LE format.
    // Calculate the size of the data to be processed in a single frame based on the format of the output node.
    // 1000 is the time conversion unit. 20 indicates 20 ms of audio sampling data. If samplingRate is 11025, use 40 ms for calculation.
    int32\_t frameSize = 20 \* audioFormatOutput.samplingRate \* audioFormatOutput.channelCount \* byteSize / 1000;
    // Buffer used to receive the output audio data after rendering.
    uint8\_t \*audioData = (uint8\_t \*)malloc(frameSize);
    int32\_t responseSize = 0;
    bool finished = false;
    
    // Start rendering.
    OH\_AudioSuiteEngine\_StartPipeline(audioSuitePipeline);
    do {
        OH\_AudioSuite\_Result result = OH\_AudioSuiteEngine\_RenderFrame(
            audioSuitePipeline, static\_cast<void \*>(audioData), frameSize, &responseSize, &finished);
        if ((result != OH\_AudioSuite\_Result::AUDIOSUITE\_SUCCESS) || (responseSize <= 0)) {
            // The audio creation rendering fails.
            break;
        } else {
            // audioData is the rendered audio data. responseSize is the audio data length. You can use or save it as required.
        }
    } while (!finished);
    OH\_AudioSuiteEngine\_StopPipeline(audioSuitePipeline);
    free(audioData);
    audioData = nullptr;
    
4.  Destroy resources.
    
    // Destroy the nodes.
    OH\_AudioSuiteEngine\_DestroyNode(inputNodeForMix);
    OH\_AudioSuiteEngine\_DestroyNode(inputNodeForField);
    OH\_AudioSuiteEngine\_DestroyNode(fieldNode);
    OH\_AudioSuiteEngine\_DestroyNode(mixerNode);
    OH\_AudioSuiteEngine\_DestroyNode(outputNode);
    
    // Destroy the pipeline.
    OH\_AudioSuiteEngine\_DestroyPipeline(audioSuitePipeline);
    
    // Destroy the engine.
    OH\_AudioSuiteEngine\_Destroy(audioSuiteEngine);
