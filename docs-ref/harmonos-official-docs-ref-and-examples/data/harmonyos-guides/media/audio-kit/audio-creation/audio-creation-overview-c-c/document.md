# Audio Creation Overview (C/C++)

Starting from API version 22, [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite) is provided for audio creation. OHAudioSuite is a professional audio effects processing interface designed to help you efficiently build audio creation applications. It offers high-quality, low-latency, intelligent audio processing capabilities, and integrates a variety of audio effects such as noise reduction, equalization, and vocal separation. You can easily integrate these features into your application based on specific use cases.

OHAudioSuite is built around three core concepts: engine, pipeline, and node.

**Figure 1** Implementation principle of audio creation

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4e/v3/xX4CFA2RQWGtijZriPOaHg/en-us_image_0000002537925094.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8DE1F05171C9206536C353D3FFD9717B36E81D6854EB14B2CBD76C861603B1F8)

#### Engine

The engine in [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite) centrally manages audio pipelines and controls [offline editing (C/C++)](../offline-editing-c-c/document.md) and [real-time rendering (C/C++)](../real-time-rendering-c-c/document.md). You can build an audio processing chain based on your needs. As shown in the preceding figure, initiated by the application, the process involves calling [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite) APIs to create engines, pipelines, and nodes sequentially. These nodes are then connected within the pipeline to transport Pulse Code Modulation (PCM) audio data, enabling the corresponding effect nodes to implement audio processing capabilities. When the pipeline is stopped, you can connect, disconnect, and remove nodes within certain limits (see [Pipeline Composition and Orchestration](#pipeline-composition-and-orchestration)), and adjust node orchestration to implement complex audio effects.

An engine supports the creation of up to 10 pipelines, with a maximum of 1 dedicated to real-time rendering.

#### Node

## Introduction to Nodes

A node is the minimum unit of audio rendering. It provides the corresponding audio effect processing capability based on its functionality. Nodes themselves cannot be called independently; they must be attached to pipelines and engines for use.

[OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite) supports three types of nodes: input node, output node, and effect node.

| Node Type | Description |
| :-- | :-- |
| INPUT\_NODE | Input node, which allows you to input PCM audio data in various formats. |
| EFFECT\_NODE | Effect node, which allows you to add audio effects. Both single-input single-output and multi-input single-output are supported. |
| OUTPUT\_NODE | Output node, which allows you to set the output format of PCM audio data. |

For details about the complete node types, see [OH\_AudioNode\_Type](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type).

## Functionalities of Nodes

-   Input nodes are responsible for processing the input of PCM audio data and obtaining data from the application side.
    
-   Output nodes are responsible for processing the output of PCM audio data. You can set the output format of audio data.
    
-   In [offline editing (C/C++)](../offline-editing-c-c/document.md) scenarios, audio effect nodes such as equalizers, source separation, sound field effects, noise reduction, voice beautification, environment effects, and audio mixer are supported.
    
-   In [real-time rendering (C/C++)](../real-time-rendering-c-c/document.md) scenarios, equalizer effect nodes are supported.
    
-   Audio effect nodes such as equalizers, source separation, sound field effects, and noise reduction support corresponding audio effect processing functionalities and multi-audio mixing operations. The output format of PCM audio data can be set (such as [OH\_Audio\_SampleFormat (bit depth)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_sampleformat), [OH\_Audio\_SampleRate (sampling rate)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audio_samplerate), and [OH\_AudioChannelLayout (number of channels)](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-channel-layout-h#oh_audiochannellayout)).
    

#### Pipeline

A pipeline centrally manages the connections and configurations of audio nodes. It supports two working modes: [offline editing (C/C++)](../offline-editing-c-c/document.md) and [real-time rendering (C/C++)](../real-time-rendering-c-c/document.md).

The pipeline data processing uses a reverse drive mechanism. Initiated by [OH\_AudioSuiteEngine\_RenderFrame()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_renderframe) or [OH\_AudioSuiteEngine\_MultiRenderFrame()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_multirenderframe), the output node requests data from the upstream connected nodes level by level, ultimately prompting the input node's [OH\_InputNode\_RequestDataCallback()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_inputnode_requestdatacallback) callback function to request the audio data to be processed from the developer.

**Figure 2** Pipeline running state

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/DAQ87hjdSLOq6Luf3HnmQw/en-us_image_0000002568684871.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062035Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=08F77E294C4DEF44E30131C34D71B3A9FA0FD71BFE5CE1197F1FDD1CBB4DBC2C)

The table below describes these states.

| State | Description |
| :-- | :-- |
| stopped | 
The initial state, or the state entered after [OH\_AudioSuiteEngine\_StopPipeline()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_stoppipeline) is executed.

When switching to the stopped state, each node releases its cache.

 |
| running | 

The working state, or the state entered from the initial state by executing [OH\_AudioSuiteEngine\_StartPipeline()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_startpipeline).

This function checks the integrity of the pipeline, including whether there are valid connections and whether nodes are incorrectly connected.

 |

## Functionalities of Pipelines

-   The pipeline is the audio effect chain in [OHAudioSuite](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-ohaudiosuite) that supports applications in rendering PCM audio data. The pipeline supports flexible networking between nodes, providing a richer and more flexible audio creation experience.
    
-   The pipeline is used in the following scenarios:
    
    Create an input node, an effect node (for example, an equalizer node [EFFECT\_NODE\_TYPE\_EQUALIZER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type)), and an output node. Connect them in the sequence of input node -> effect node -> output node to form a pipeline that implements equalizer functionality. (For details about the code example, see [Basic Offline Editing](../offline-editing-c-c/document.md#basic-offline-editing).) In addition, the pipeline supports the multi-input scenario (for details, see [Mixing and Cascading](../offline-editing-c-c/document.md#mixing-and-cascading)), where PCM data from each pipeline input passes through its respective effect nodes and is mixed before output.
    

## Pipeline Composition and Orchestration

A pipeline is composed of nodes. In each pipeline, there can be up to 5 input nodes ([INPUT\_NODE\_TYPE\_DEFAULT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type)), up to 1 output node ([OUTPUT\_NODE\_TYPE\_DEFAULT](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type)), and up to 5 effect nodes, with up to 3 audio mixer nodes ([EFFECT\_NODE\_TYPE\_AUDIO\_MIXER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type)) and up to 1 source separation node ([EFFECT\_MULTII\_OUTPUT\_NODE\_TYPE\_AUDIO\_SEPARATION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type)).

The rules for creating nodes in a pipeline are as follows:

-   If the number of created nodes of a type reaches the limit for that type, further creation of nodes of that type will fail.
-   Each pipeline must have at least one input node and exactly one output node.
-   Before creating a node, call [OH\_AudioSuiteEngine\_IsNodeTypeSupported()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-engine-h#oh_audiosuiteengine_isnodetypesupported) to check whether the node type is supported to avoid node creation failure.
-   Input and output nodes support node format setting, whereas other nodes do not. The input format is the audio format of the audio source, and the output format is the audio format that you expect to output.

The rules for orchestrating nodes in a pipeline are as follows:

-   The connection order of nodes in a pipeline is as follows: input node -> effect node -> output node.
    
-   The source separation effect node [EFFECT\_MULTII\_OUTPUT\_NODE\_TYPE\_AUDIO\_SEPARATION](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type) can only be connected to an output node. There is no such restriction for other effect nodes.
    
-   The audio mixer effect node [EFFECT\_NODE\_TYPE\_AUDIO\_MIXER](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-native-audio-suite-base-h#oh_audionode_type) supports multiple input connections, whereas other nodes do not.
    
-   Node connections are unidirectional, and reverse connections from subsequent nodes to preceding nodes are not supported. The input node is the first node in each pipeline, and the output node is the last node in each pipeline.
