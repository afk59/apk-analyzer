# native\_audio\_suite\_engine.h

#### Overview

The file declares the functions related to audio creation, including the engine, pipeline, and node.

**File to include**: <ohaudiosuite/native\_audio\_suite\_engine.h>

**Library**: libohaudiosuite.so

**System capability**: SystemCapability.Multimedia.Audio.SuiteEngine

**Since**: 22

**Related module**: [OHAudioSuite](../../modules/ohaudiosuite/document.md)

#### Summary

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_Create(OH\_AudioSuiteEngine\*\* audioSuiteEngine)](#oh_audiosuiteengine_create) | \- | Creates an audio creation engine. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_Destroy(OH\_AudioSuiteEngine\* audioSuiteEngine)](#oh_audiosuiteengine_destroy) | \- | Destroys the handle to an audio creation engine. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_CreatePipeline(OH\_AudioSuiteEngine\* audioSuiteEngine, OH\_AudioSuitePipeline\*\* audioSuitePipeline, OH\_AudioSuite\_PipelineWorkMode workMode)](#oh_audiosuiteengine_createpipeline) | \- | 
Creates a pipeline within the current audio creation engine. A pipeline is the execution unit within the engine responsible for audio creation, and multiple pipelines can be created within a single engine.

Up to 10 pipelines can be created, with a maximum of one real-time rendering pipeline.

Each pipeline must have at least one input node and exactly one output node.

When the pipeline operations in [OH\_AudioSuite\_PipelineWorkMode](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_EDIT\_MODE mode, all effect nodes are supported.

When the pipeline operations in [OH\_AudioSuite\_PipelineWorkMode](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_REALTIME\_MODE mode, only the [OH\_AudioNode\_Type](../native-audio-suite-base-h/document.md#oh_audionode_type).EFFECT\_NODE\_TYPE\_EQUALIZER effect node is supported.

 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DestroyPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)](#oh_audiosuiteengine_destroypipeline) | \- | Destroys the handle to an audio creation pipeline. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_StartPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)](#oh_audiosuiteengine_startpipeline) | \- | Starts the pipeline. The pipeline will enter the [OH\_AudioSuite\_PipelineState](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_RUNNING state. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_StopPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)](#oh_audiosuiteengine_stoppipeline) | \- | Stops the pipeline. The pipeline will enter the [OH\_AudioSuite\_PipelineState](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_STOPPED state. This function does not change the connections between nodes within the pipeline. Once the pipeline is stopped, [OH\_AudioSuiteEngine\_RenderFrame](#oh_audiosuiteengine_renderframe) can no longer perform audio processing. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetPipelineState(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioSuite\_PipelineState\* pipelineState)](#oh_audiosuiteengine_getpipelinestate) | \- | Retrieves the state of the pipeline. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_RenderFrame(OH\_AudioSuitePipeline\* audioSuitePipeline, void\* audioData, int32\_t requestFrameSize, int32\_t\* responseSize, bool\* finishedFlag)](#oh_audiosuiteengine_renderframe) | \- | Obtains the processed audio data from the pipeline (for single-output effect nodes). |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_MultiRenderFrame(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioDataArray\* audioDataArray, int32\_t\* responseSize, bool\* finishedFlag)](#oh_audiosuiteengine_multirenderframe) | \- | Renders the pipeline and obtains the processed audio data. For pipelines with multiple output effect nodes (for example, those containing audio separation nodes), the size of **audioDataArray** must correspond one-to-one with the number of outputs from the effect nodes. (For example, audio separation nodes require two outputs: the first for vocals and the second for background sound.) |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Create(OH\_AudioNodeBuilder\*\* builder)](#oh_audiosuitenodebuilder_create) | \- | Obtains an audio creation node builder, which is used to configure and create audio nodes. The builder can be reused. However, if the properties of the new node differ from those of the previous node, you must use [OH\_AudioSuiteNodeBuilder\_Reset](#oh_audiosuitenodebuilder_reset) to reset the builder. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Destroy(OH\_AudioNodeBuilder\* builder)](#oh_audiosuitenodebuilder_destroy) | \- | Destroys an audio creation node builder. This function must be called after the builder is no longer required. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Reset(OH\_AudioNodeBuilder\* builder)](#oh_audiosuitenodebuilder_reset) | \- | Resets an audio creation node builder, clearing all previously set parameters. If you want to reuse the builder to create a node with different properties, this function must be called to clear all properties (for example, node type). |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetNodeType(OH\_AudioNodeBuilder\* builder, OH\_AudioNode\_Type type)](#oh_audiosuitenodebuilder_setnodetype) | \- | Sets the type of node to be constructed by the current node builder. During node creation, other parameters are verified based on the node type. This property must be set for all node types. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetFormat(OH\_AudioNodeBuilder\* builder, OH\_AudioFormat audioFormat)](#oh_audiosuitenodebuilder_setformat) | \- | 

Configures the audio format for input or output nodes. This function can only be used before node creation. For input nodes, it allows the application to specify the audio format for writing data.

For output nodes, it allows the application to specify the desired audio format for obtaining data.

This function is not supported for other node types.

 |
| [typedef int32\_t (\*OH\_InputNode\_RequestDataCallback)(OH\_AudioNode\* audioNode, void\* userData, void\* audioData, int32\_t audioDataSize, bool\* finished)](#oh_inputnode_requestdatacallback) | OH\_InputNode\_RequestDataCallback | Sets a callback function for the input node to request data. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback(OH\_AudioNodeBuilder\* builder, OH\_InputNode\_RequestDataCallback callback, void\* userData)](#oh_audiosuitenodebuilder_setrequestdatacallback) | \- | Sets a callback function for writing audio data for the current input node builder. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_CreateNode(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioNodeBuilder\* builder, OH\_AudioNode\*\* audioNode)](#oh_audiosuiteengine_createnode) | \- | 

Creates an audio node within the audio pipeline based on the audio creation builder. When this function is executed, the system checks the validity of the parameters based on the node type set in the builder.

Applications can determine the cause of errors based on the return value.

 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DestroyNode(OH\_AudioNode\* audioNode)](#oh_audiosuiteengine_destroynode) | \- | Destroys an audio creation node. To destroy a node, the pipeline must be in the [OH\_AudioSuite\_PipelineState](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_STOPPED state. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetNodeBypassStatus(OH\_AudioNode\* audioNode, bool\* bypassStatus)](#oh_audiosuiteengine_getnodebypassstatus) | \- | 

Obtains the effect bypass status of the current node. This function can be used only on effect nodes.

If it is called on an input or output node, the AUDIOSUITE\_ERROR\_INVALID\_PARAM error code is returned.

 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_BypassEffectNode(OH\_AudioNode\* audioNode, bool bypass)](#oh_audiosuiteengine_bypasseffectnode) | \- | Sets the effect bypass status of the current node (supported only on effect nodes). When **bypass** is set to **true**, the effect node passes data through without any processing. When **bypass** is set to **false**, the effect node performs the corresponding effect processing. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetAudioFormat(OH\_AudioNode\* audioNode, OH\_AudioFormat \*audioFormat)](#oh_audiosuiteengine_setaudioformat) | \- | Sets the audio format for input or output nodes after creation. This function is supported only for input and output nodes. The input node specifies the audio source format, and the output node specifies the target format. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_ConnectNodes(OH\_AudioNode\* sourceAudioNode, OH\_AudioNode\* destAudioNode)](#oh_audiosuiteengine_connectnodes) | \- | 

Connects two nodes, with data flowing from **sourceAudioNode** to **destAudioNode**. Connecting nodes will change the pipeline topology and may cause data loss. You are advised to perform this operation when the engine is stopped.

The connection order of nodes in a pipeline is as follows: input node -> effect node -> output node.

 |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DisconnectNodes(OH\_AudioNode\* sourceAudioNode, OH\_AudioNode\* destAudioNode)](#oh_audiosuiteengine_disconnectnodes) | \- | Disconnect two nodes. This operation will change the pipeline topology and may cause data loss. You are advised to perform this operation when the engine is stopped. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetEqualizerFrequencyBandGains(OH\_AudioNode\* audioNode, OH\_EqualizerFrequencyBandGains frequencyBandGains)](#oh_audiosuiteengine_setequalizerfrequencybandgains) | \- | Sets the band gain effect for the current equalizer node. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetEqualizerFrequencyBandGains(OH\_AudioNode\* audioNode, OH\_EqualizerFrequencyBandGains\* frequencyBandGains)](#oh_audiosuiteengine_getequalizerfrequencybandgains) | \- | Obtains the band gain effect of the current equalizer node. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetSoundFieldType(OH\_AudioNode\* audioNode, OH\_SoundFieldType soundFieldType)](#oh_audiosuiteengine_setsoundfieldtype) | \- | Sets the configuration parameters for the sound field effect node. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetSoundFieldType(OH\_AudioNode\* audioNode, OH\_SoundFieldType\* soundFieldType)](#oh_audiosuiteengine_getsoundfieldtype) | \- | Obtains the configuration parameters of the sound field effect node. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetEnvironmentType(OH\_AudioNode\* audioNode, OH\_EnvironmentType environmentType)](#oh_audiosuiteengine_setenvironmenttype) | \- | Sets the configuration parameters for the environment effect node. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetEnvironmentType(OH\_AudioNode\* audioNode, OH\_EnvironmentType\* environmentType)](#oh_audiosuiteengine_getenvironmenttype) | \- | Obtains the configuration parameters of the environment effect node. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetVoiceBeautifierType(OH\_AudioNode\* audioNode, OH\_VoiceBeautifierType voiceBeautifierType)](#oh_audiosuiteengine_setvoicebeautifiertype) | \- | Sets the configuration parameters for the voice beautifier effect node. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetVoiceBeautifierType(OH\_AudioNode\* audioNode, OH\_VoiceBeautifierType\* voiceBeautifierType)](#oh_audiosuiteengine_getvoicebeautifiertype) | \- | Obtains the configuration parameters of the voice beautifier effect node. |
| [OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_IsNodeTypeSupported(OH\_AudioNode\_Type nodeType, bool\* isSupported)](#oh_audiosuiteengine_isnodetypesupported) | \- | Checks whether the system supports the creation of a specified node type to avoid node creation failure. This function is called independently of engine and pipeline states and is only related to the system, without the need to create an engine or pipeline. |

#### Function Description

#### \[h2\]OH\_AudioSuiteEngine\_Create()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_Create(OH\_AudioSuiteEngine\*\* audioSuiteEngine)

**Description**

Creates an audio creation engine.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuiteEngine](../../structs/oh-audiosuiteenginestruct/document.md)\*\* audioSuiteEngine | Double pointer used to receive the handle to the newly created audio creation engine. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioSuiteEngine** parameter is nullptr.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The engine has been initialized.

**AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED**: Memory allocation fails.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_Destroy()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_Destroy(OH\_AudioSuiteEngine\* audioSuiteEngine)

**Description**

Destroys the handle to an audio creation engine.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e0/v3/339LNALnRTGStt6fgtXQcw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062419Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2CFFF7EF764C0107DD70CC4C9B94667CFB4FA1D93E34471001DDD888B3FB2EFF)

When an engine is destroyed, all pipelines under the engine are destroyed.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuiteEngine](../../structs/oh-audiosuiteenginestruct/document.md)\* audioSuiteEngine | Audio creation engine handle, which is obtained by calling [OH\_AudioSuiteEngine\_Create](#oh_audiosuiteengine_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioSuiteEngine** parameter is nullptr.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The engine has been deinitialized, is not created, or is not initialized.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_CreatePipeline()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_CreatePipeline(OH\_AudioSuiteEngine\* audioSuiteEngine, OH\_AudioSuitePipeline\*\* audioSuitePipeline, OH\_AudioSuite\_PipelineWorkMode workMode)

**Description**

Creates a pipeline within the current audio creation engine. A pipeline is the execution unit within the engine responsible for audio creation, and multiple pipelines can be created within a single engine.

Up to 10 pipelines can be created, with a maximum of one real-time rendering pipeline.

Each pipeline must have at least one input node and exactly one output node.

When the pipeline operations in [OH\_AudioSuite\_PipelineWorkMode](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_EDIT\_MODE mode, all effect nodes are supported.

When the pipeline operations in [OH\_AudioSuite\_PipelineWorkMode](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelineworkmode).AUDIOSUITE\_PIPELINE\_REALTIME\_MODE mode, only the [OH\_AudioNode\_Type](../native-audio-suite-base-h/document.md#oh_audionode_type).EFFECT\_NODE\_TYPE\_EQUALIZER effect node is supported.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuiteEngine](../../structs/oh-audiosuiteenginestruct/document.md)\* audioSuiteEngine | Audio creation engine handle, which is obtained by calling [OH\_AudioSuiteEngine\_Create](#oh_audiosuiteengine_create). |
| [OH\_AudioSuitePipeline](../../structs/oh-audiosuitepipelinestruct/document.md)\*\* audioSuitePipeline | Double pointer used to receive the handle to the newly created audio creation pipeline. |
| [OH\_AudioSuite\_PipelineWorkMode](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelineworkmode) workMode | 
Working mode of the pipeline.

1\. **AUDIOSUITE\_PIPELINE\_EDIT\_MODE**: All effect nodes are supported.

2\. **AUDIOSUITE\_PIPELINE\_REALTIME\_MODE**: Equalizer effect nodes are supported.

 |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioSuiteEngine** or **audioSuitePipeline** parameter is nullptr.

**AUDIOSUITE\_ERROR\_ENGINE\_NOT\_EXIST**: The engine is not initialized.

**AUDIOSUITE\_ERROR\_CREATED\_EXCEED\_SYSTEM\_LIMITS**: The number of pipelines created already reaches the upper limit. (An engine can create a maximum of 10 pipelines.)

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED**: Memory allocation fails.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_DestroyPipeline()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DestroyPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)

**Description**

Destroys the handle to an audio creation pipeline.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/10/v3/HEWMsPqsSk-EgXpOWMhs4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062419Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=000266D1DD4AD83C7BDE976E7CC0EE86050066A2CEC51AFBCDFB314D2EF1EB44)

When a pipeline is destroyed, all nodes under the pipeline are destroyed.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuitePipeline](../../structs/oh-audiosuitepipelinestruct/document.md)\* audioSuitePipeline | Audio creation pipeline handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreatePipeline](#oh_audiosuiteengine_createpipeline). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioSuitePipeline** parameter is nullptr.

**AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST**: The pipeline does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_StartPipeline()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_StartPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)

**Description**

Starts the pipeline. The pipeline will enter the [OH\_AudioSuite\_PipelineState](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_RUNNING state.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuitePipeline](../../structs/oh-audiosuitepipelinestruct/document.md)\* audioSuitePipeline | Audio creation pipeline handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreatePipeline](#oh_audiosuiteengine_createpipeline). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioSuitePipeline** parameter is nullptr.

**AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST**: The pipeline does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The pipeline is running or the node connection is abnormal.

Possible causes are as follows:

1\. The pipeline is already running.

2\. The pipeline does not contain any output node.

3\. The first node is not an input node.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_StopPipeline()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_StopPipeline(OH\_AudioSuitePipeline\* audioSuitePipeline)

**Description**

Stops the pipeline. The pipeline will enter the [OH\_AudioSuite\_PipelineState](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelinestate).AUDIOSUITE\_PIPELINE\_STOPPED state. This function does not change the connections between nodes within the pipeline. Once the pipeline is stopped, [OH\_AudioSuiteEngine\_RenderFrame](#oh_audiosuiteengine_renderframe) can no longer perform audio processing.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuitePipeline](../../structs/oh-audiosuitepipelinestruct/document.md)\* audioSuitePipeline | Audio creation pipeline handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreatePipeline](#oh_audiosuiteengine_createpipeline). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioSuitePipeline** parameter is nullptr.

**AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST**: The pipeline does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The pipeline is already stopped.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_GetPipelineState()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetPipelineState(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioSuite\_PipelineState\* pipelineState)

**Description**

Retrieves the state of the pipeline.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuitePipeline](../../structs/oh-audiosuitepipelinestruct/document.md)\* audioSuitePipeline | Audio creation pipeline handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreatePipeline](#oh_audiosuiteengine_createpipeline). |
| [OH\_AudioSuite\_PipelineState](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelinestate)\* pipelineState | Pointer to the pipeline state. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **audioSuitePipeline** is nullptr.

**AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST**: The pipeline does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_RenderFrame()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_RenderFrame(OH\_AudioSuitePipeline\* audioSuitePipeline, void\* audioData, int32\_t requestFrameSize, int32\_t\* responseSize, bool\* finishedFlag)

**Description**

Obtains the processed audio data from the pipeline (for single-output effect nodes).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f4/v3/UgVzwhrSTcmgZywaNOCKvg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062419Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=99B049E938ED67E684D07B415564490F0762301C54C683D6EC287793CEB4240E)

Applications need to call this function to obtain audio data that has been processed by effects.

-   When this function is called, the pipeline pulls data backward from the output node, apply effect processing,
-   and fill the processed data into the **audioData** pointer provided by the application.
-   The system attempts to fill the data based on the size specified by **requestFrameSize**, and the actual size of the processed data is returned to the application via **responseSize**.
-   When the application has prepared data for all input nodes and submits the last data through a callback, it should set the finish flag in the callback.
-   Once all inputs in the pipeline have passed the finish flag, the pipeline notifies the application through **finishedFlag** after processing is complete.
-   If **finishedFlag** is **true**, the application should not call this function again.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuitePipeline](../../structs/oh-audiosuitepipelinestruct/document.md)\* audioSuitePipeline | Audio creation pipeline handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreatePipeline](#oh_audiosuiteengine_createpipeline). |
| void\* audioData | Pointer to the address for writing the obtained audio data. |
| int32\_t requestFrameSize | Byte size of the memory allocated for **audioData**. The value must be greater than 0. |
| int32\_t\* responseSize | Pointer to the size of the audio data written to **audioData** by the pipeline. The value cannot be greater than **requestFrameSize**. |
| bool\* finishedFlag | Pointer to the flag indicating whether the current pipeline has completed rendering. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: A parameter is nullptr or has an invalid value.

Possible causes are as follows:

1\. The **audioSuitePipeline** parameter is nullptr.

2\. The **audioData** parameter is nullptr.

3\. The value of **requestFrameSize** is less than or equal to 0.

4\. The **responseSize** parameter is nullptr.

5\. The **finishedFlag** parameter is nullptr.

**AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST**: The pipeline does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The pipeline is not running.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The pipeline rendering is complete. (**finishedFlag** is written as **true** when this function is called.)

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_MultiRenderFrame()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_MultiRenderFrame(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioDataArray\* audioDataArray, int32\_t\* responseSize, bool\* finishedFlag)

**Description**

Renders the pipeline and obtains the processed audio data. For pipelines with multiple output effect nodes (for example, those containing audio separation nodes), the size of **audioDataArray** must correspond one-to-one with the number of outputs from the effect nodes. (For example, audio separation nodes require two outputs: the first for vocals and the second for background sound.)

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuitePipeline](../../structs/oh-audiosuitepipelinestruct/document.md)\* audioSuitePipeline | Audio creation pipeline handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreatePipeline](#oh_audiosuiteengine_createpipeline). |
| [OH\_AudioDataArray](../../structs/oh-audiodataarray/document.md)\* audioDataArray | Pointer to the array used by the user to read audio data. Each element of the array must be of the same size. |
| int32\_t\* responseSize | Pointer to the size of the audio data written into each element of **audioDataArray** by the pipeline. The system ensures consistent data size across all elements. |
| bool\* finishedFlag | Pointer to the flag indicating whether the current pipeline has completed rendering. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: A parameter is nullptr or has an invalid value.

Possible causes are as follows:

1\. The **audioSuitePipeline** parameter is nullptr.

2\. The **audioDataArray** parameter is nullptr.

3\. A member of the **audioDataArray** parameter is nullptr.

4\. The value of **requestFrameSize** in **audioDataArray** is less than or equal to 0.

5\. The **responseSize** parameter is nullptr.

6\. The **finishedFlag** parameter is nullptr.

**AUDIOSUITE\_ERROR\_PIPELINE\_NOT\_EXIST**: The pipeline does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The pipeline is not running.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The pipeline rendering is complete. (**finishedFlag** is written as **true** when this function is called.)

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteNodeBuilder\_Create()

OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Create(OH\_AudioNodeBuilder\*\* builder)

**Description**

Obtains an audio creation node builder, which is used to configure and create audio nodes. The builder can be reused. However, if the properties of the new node differ from those of the previous node, you must use [OH\_AudioSuiteNodeBuilder\_Reset](#oh_audiosuitenodebuilder_reset) to reset the builder.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNodeBuilder](../../structs/oh-audionodebuilderstruct/document.md)\*\* builder | Double pointer used to receive the handle to the audio creation node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **builder** is nullptr.

**AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED**: Memory allocation fails.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteNodeBuilder\_Destroy()

OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Destroy(OH\_AudioNodeBuilder\* builder)

**Description**

Destroys an audio creation node builder. This function must be called after the builder is no longer required.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNodeBuilder](../../structs/oh-audionodebuilderstruct/document.md)\* builder | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteNodeBuilder\_Create](#oh_audiosuitenodebuilder_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **builder** is nullptr.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteNodeBuilder\_Reset()

OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_Reset(OH\_AudioNodeBuilder\* builder)

**Description**

Resets an audio creation node builder, clearing all previously set parameters. If you want to reuse the builder to create a node with different properties, this function must be called to clear all properties (for example, node type).

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNodeBuilder](../../structs/oh-audionodebuilderstruct/document.md)\* builder | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteNodeBuilder\_Create](#oh_audiosuitenodebuilder_create). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **builder** is nullptr.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteNodeBuilder\_SetNodeType()

OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetNodeType(OH\_AudioNodeBuilder\* builder, OH\_AudioNode\_Type type)

**Description**

Sets the type of node to be constructed by the current node builder. During node creation, other parameters are verified based on the node type. This property must be set for all node types.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNodeBuilder](../../structs/oh-audionodebuilderstruct/document.md)\* builder | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteNodeBuilder\_Create](#oh_audiosuitenodebuilder_create). |
| [OH\_AudioNode\_Type](../native-audio-suite-base-h/document.md#oh_audionode_type) type | Node type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The node type is set successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, **builder** is a null pointer.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteNodeBuilder\_SetFormat()

OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetFormat(OH\_AudioNodeBuilder\* builder, OH\_AudioFormat audioFormat)

**Description**

Configures the audio format for input or output nodes. This function can only be used before node creation. For input nodes, it allows the application to specify the audio format for writing data.

For output nodes, it allows the application to specify the desired audio format for obtaining data.

This function is not supported for other node types.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNodeBuilder](../../structs/oh-audionodebuilderstruct/document.md)\* builder | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteNodeBuilder\_Create](#oh_audiosuitenodebuilder_create). |
| [OH\_AudioFormat](../../structs/oh-audioformat/document.md) audioFormat | Audio stream format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: A parameter is invalid. For example, **builder** is a null pointer.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_FORMAT**: The value of **channelCount** in **audioFormat** is not supported.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_InputNode\_RequestDataCallback()

typedef int32\_t (\*OH\_InputNode\_RequestDataCallback)(OH\_AudioNode\* audioNode, void\* userData, void\* audioData, int32\_t audioDataSize, bool\* finished)

**Description**

Sets a callback function for the input node to request data.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/f2/v3/1uxfEVEmSVKvuoQtiq1h4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062419Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1669F3F503E761B2C5BD72A8ADEB0A25E57B85F5A79F4DEE9F5BBF9DC79D4DA0)

Applications should write the PCM audio data to be processed to **audioData**, from which OHAudioSuite obtains the data for audio creation.

-   Applications should write data to **audioData** that does not exceed the size specified by **audioDataSize**.
-   Once all data has been passed to the pipeline through this callback, the application should set **finished** to **true** in the last callback. After this, the pipeline will no longer call this function.
-   Only input nodes require this configuration; other nodes do not.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| OH\_AudioNode\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| void\* userData | Pointer to user-specific data. When the system calls this callback function, **userData** passed by calling [OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback](#oh_audiosuitenodebuilder_setrequestdatacallback) is used. |
| void\* audioData | Pointer to the memory address provided by the system, where the application should write the audio data stream to be processed (to be filled by the user). |
| int32\_t audioDataSize | Byte size of the memory address allocated for **audioData**. |
| bool\* finished | Pointer to the flag indicating whether the audio data stream for the node specified by **audioNode** has been fully written. **true** if fully written, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| int32\_t | 
Effective length of the data written into the **audioData** buffer (in bytes).

The return value must be in the range of \[0, audioDataSize\]. If the return value is less than 0, the system changes the return value to **0**.

If the return value is greater than **audioDataSize**, the system changes the return value to **audioDataSize**.

 |

#### \[h2\]OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback()

OH\_AudioSuite\_Result OH\_AudioSuiteNodeBuilder\_SetRequestDataCallback(OH\_AudioNodeBuilder\* builder, OH\_InputNode\_RequestDataCallback callback, void\* userData)

**Description**

Sets a callback function for writing audio data for the current input node builder.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNodeBuilder](../../structs/oh-audionodebuilderstruct/document.md)\* builder | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteNodeBuilder\_Create](#oh_audiosuitenodebuilder_create). |
| [OH\_InputNode\_RequestDataCallback](#oh_inputnode_requestdatacallback) callback | Callback for writing audio data. |
| void\* userData | Pointer to user-specific data. The address is passed to the user within the callback function. If it is not used, nullptr can be provided. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**:

Possible causes are as follows:

1\. The **builder** parameter is nullptr.

2\. The **callback** parameter is nullptr.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_CreateNode()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_CreateNode(OH\_AudioSuitePipeline\* audioSuitePipeline, OH\_AudioNodeBuilder\* builder, OH\_AudioNode\*\* audioNode)

**Description**

Creates an audio node within the audio pipeline based on the audio creation builder. When this function is executed, the system checks the validity of the parameters based on the node type set in the builder.

Applications can determine the cause of errors based on the return value.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioSuitePipeline](../../structs/oh-audiosuitepipelinestruct/document.md)\* audioSuitePipeline | Audio creation pipeline handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreatePipeline](#oh_audiosuiteengine_createpipeline). |
| [OH\_AudioNodeBuilder](../../structs/oh-audionodebuilderstruct/document.md)\* builder | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteNodeBuilder\_Create](#oh_audiosuitenodebuilder_create). |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\*\* audioNode | Audio creation node handle, |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: A parameter is nullptr or has an invalid value.

Possible causes are as follows:

1\. The **audioSuitePipeline** parameter is nullptr.

2\. The **builder** parameter is nullptr.

3\. The **audioNode** parameter is nullptr.

**AUDIOSUITE\_ERROR\_CREATED\_EXCEED\_SYSTEM\_LIMITS**: The number of nodes of the current type already reaches the upper limit.

For example, attempting to create more than 5 effect nodes.

**AUDIOSUITE\_ERROR\_REQUIRED\_PARAMETERS\_MISSING**: Mandatory parameters are missing when creating a node of the specified type.

For example, the node type is not set in the builder.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: Unsupported operations. For example, setting a callback function for an output node,

or setting an audio format or callback function for an effect node.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_MEMORY\_ALLOC\_FAILED**: Memory allocation fails.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_DestroyNode()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DestroyNode(OH\_AudioNode\* audioNode)

**Description**

Destroys an audio creation node. Whether a node can be destroyed depends on the state of its associated pipeline. If the pipeline is not in the [OH\_AudioSuite\_PipelineState.AUDIOSUITE\_PIPELINE\_STOPPED](../native-audio-suite-base-h/document.md#oh_audiosuite_pipelinestate) state and the node is in the pipeline processing path, the destruction fails.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioNode** parameter is nullptr.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The pipeline is not in the stopped state.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_GetNodeBypassStatus()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetNodeBypassStatus(OH\_AudioNode\* audioNode, bool\* bypassStatus)

**Description**

Obtains the effect bypass status of the current node. This function can be used only on effect nodes.

If it is called on an input or output node, the AUDIOSUITE\_ERROR\_INVALID\_PARAM error code is returned.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| bool\* bypassStatus | Pointer to the effect bypass status of the current node. **true** means that node processing is bypassed, and **false** means the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**:

The **audioNode** or **bypassStatus** parameter is nullptr.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to an effect node.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_BypassEffectNode()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_BypassEffectNode(OH\_AudioNode\* audioNode, bool bypass)

**Description**

Sets the effect bypass status of the current node (supported only on effect nodes). When **bypass** is set to **true**, the effect node passes data through without any processing. When **bypass** is set to **false**, the effect node performs the corresponding effect processing.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| bool bypass | Effect bypass status of the current node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioNode** parameter is nullptr.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to an effect node.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_SetAudioFormat()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetAudioFormat(OH\_AudioNode\* audioNode, OH\_AudioFormat \*audioFormat)

**Description**

Sets the audio format for input or output nodes after creation. This function is supported only for input and output nodes. The input node specifies the audio source format, and the output node specifies the target format.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_AudioFormat](../../structs/oh-audioformat/document.md) \*audioFormat | Audio stream format. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **audioNode** parameter or **audioFormat** is nullptr.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to an effect node.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The pipeline is not in the stopped state.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_ConnectNodes()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_ConnectNodes(OH\_AudioNode\* sourceAudioNode, OH\_AudioNode\* destAudioNode)

**Description**

Connects two nodes, with data flowing from **sourceAudioNode** to **destAudioNode**. Connecting nodes will change the pipeline topology and may cause data loss. You are advised to perform this operation when the engine is stopped.

The connection order of nodes in a pipeline is as follows: input node -> effect node -> output node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* sourceAudioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* destAudioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **sourceAudioNode** parameter or **destAudioNode** is nullptr.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_CONNECT**: Nodes do not support connection.

Possible causes are as follows:

1\. The **sourceAudioNode** parameter points to an output node.

2\. The **destAudioNode** parameter points to an input node.

3\. The **sourceAudioNode** and **destAudioNode** parameters point to the same node.

4\. The **sourceAudioNode** parameter points to a source separation effect node, but the **destAudioNode** parameter does not point to an output node.

5\. The **sourceAudioNode** and **destAudioNode** parameters point to nodes within different pipelines.

6\. The pipeline is in the running state, but the **destAudioNode** parameter does not point to an audio mixer effect node.

7\. The pipeline is in the running state, the **destAudioNode** parameter points to an audio mixer effect node, but the **sourceAudioNode** parameter does not point to an input node.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The pipeline is in an invalid state. For example, the output node cannot be found.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_DisconnectNodes()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_DisconnectNodes(OH\_AudioNode\* sourceAudioNode, OH\_AudioNode\* destAudioNode)

**Description**

Disconnect two nodes. This operation will change the pipeline topology and may cause data loss. You are advised to perform this operation when the engine is stopped.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* sourceAudioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* destAudioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: The **sourceAudioNode** parameter or **destAudioNode** is nullptr.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: Unsupported operation.

Possible causes are as follows:

1\. The **sourceAudioNode** parameter points to an output node.

2\. The **destAudioNode** parameter points to an input node.

3\. The **sourceAudioNode** and **destAudioNode** parameters point to the same node.

4\. The **sourceAudioNode** and **destAudioNode** parameters point to nodes within different pipelines.

5\. The pipeline is in the running state, but the **destAudioNode** parameter does not point to an audio mixer effect node.

6\. The pipeline is in the running state, the **destAudioNode** parameter points to an audio mixer effect node, but this mixer node is currently connected to only **sourceAudioNode**.

**AUDIOSUITE\_ERROR\_INVALID\_STATE**: The pipeline is in an invalid state. For example, the output node cannot be found.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_SetEqualizerFrequencyBandGains()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetEqualizerFrequencyBandGains(OH\_AudioNode\* audioNode, OH\_EqualizerFrequencyBandGains frequencyBandGains)

**Description**

Sets the band gain effect for the current equalizer node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md) frequencyBandGains | Band gains of the equalizer node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to an equalizer node.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**:

Possible causes are as follows:

1\. The **audioNode** parameter is nullptr.

2\. The value of each member in **frequencyBandGains** is not within the range \[–10, 10\].

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_GetEqualizerFrequencyBandGains()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetEqualizerFrequencyBandGains(OH\_AudioNode\* audioNode, OH\_EqualizerFrequencyBandGains\* frequencyBandGains)

**Description**

Obtains the band gain effect of the current equalizer node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_EqualizerFrequencyBandGains](../../structs/oh-equalizerfrequencybandgains/document.md)\* frequencyBandGains | Band gains of the equalizer node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to an equalizer node.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **audioNode** or **frequencyBandGains** is nullptr.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_SetSoundFieldType()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetSoundFieldType(OH\_AudioNode\* audioNode, OH\_SoundFieldType soundFieldType)

**Description**

Sets the configuration parameters for the sound field effect node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_SoundFieldType](../native-audio-suite-base-h/document.md#oh_soundfieldtype) soundFieldType | Configuration parameters of the sound field effect node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to a sound field effect node.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **audioNode** is nullptr.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_GetSoundFieldType()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetSoundFieldType(OH\_AudioNode\* audioNode, OH\_SoundFieldType\* soundFieldType)

**Description**

Obtains the configuration parameters of the sound field effect node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_SoundFieldType](../native-audio-suite-base-h/document.md#oh_soundfieldtype)\* soundFieldType | Configuration parameters of the sound field effect node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to a sound field effect node.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **audioNode** or **soundFieldType** is nullptr.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_SetEnvironmentType()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetEnvironmentType(OH\_AudioNode\* audioNode, OH\_EnvironmentType environmentType)

**Description**

Sets the configuration parameters for the environment effect node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_EnvironmentType](../native-audio-suite-base-h/document.md#oh_environmenttype) environmentType | Configuration parameters of the environment effect node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to an environment effect node.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **audioNode** is nullptr.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_GetEnvironmentType()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetEnvironmentType(OH\_AudioNode\* audioNode, OH\_EnvironmentType\* environmentType)

**Description**

Obtains the configuration parameters of the environment effect node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_EnvironmentType](../native-audio-suite-base-h/document.md#oh_environmenttype)\* environmentType | Configuration parameters of the environment effect node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to an environment effect node.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **audioNode** or **environmentType** is nullptr.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_SetVoiceBeautifierType()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_SetVoiceBeautifierType(OH\_AudioNode\* audioNode, OH\_VoiceBeautifierType voiceBeautifierType)

**Description**

Sets the configuration parameters for the voice beautifier effect node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_VoiceBeautifierType](../native-audio-suite-base-h/document.md#oh_voicebeautifiertype) voiceBeautifierType | Configuration parameters of the voice beautifier effect node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to a voice beautifier effect node.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters. For example, **audioNode** is nullptr.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_GetVoiceBeautifierType()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_GetVoiceBeautifierType(OH\_AudioNode\* audioNode, OH\_VoiceBeautifierType\* voiceBeautifierType)

**Description**

Obtains the configuration parameters of the voice beautifier effect node.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode](../../structs/oh-audionodestruct/document.md)\* audioNode | Audio creation node handle, which is obtained by calling [OH\_AudioSuiteEngine\_CreateNode](#oh_audiosuiteengine_createnode). |
| [OH\_VoiceBeautifierType](../native-audio-suite-base-h/document.md#oh_voicebeautifiertype)\* voiceBeautifierType | Configuration parameters of the voice beautifier effect node. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_NODE\_NOT\_EXIST**: The node does not exist or has been destroyed.

**AUDIOSUITE\_ERROR\_UNSUPPORTED\_OPERATION**: The **audioNode** parameter does not point to a voice beautifier effect node.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid parameters.

For example, **audioNode** or **voiceBeautifierType** is nullptr.

**AUDIOSUITE\_ERROR\_TIMEOUT**: The operation times out.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |

#### \[h2\]OH\_AudioSuiteEngine\_IsNodeTypeSupported()

OH\_AudioSuite\_Result OH\_AudioSuiteEngine\_IsNodeTypeSupported(OH\_AudioNode\_Type nodeType, bool\* isSupported)

**Description**

Checks whether the system supports the creation of a specified node type to avoid node creation failure. This function is called independently of engine and pipeline states and is only related to the system, without the need to create an engine or pipeline.

**Since**: 22

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AudioNode\_Type](../native-audio-suite-base-h/document.md#oh_audionode_type) nodeType | Type of the node. |
| bool\* isSupported | Pointer to the variable that specifies the support for node creation. **true** if supported, **false** otherwise. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_AudioSuite\_Result](../native-audio-suite-base-h/document.md#oh_audiosuite_result) | 
**AUDIOSUITE\_SUCCESS**: The function is executed successfully.

**AUDIOSUITE\_ERROR\_INVALID\_PARAM**: Invalid input parameter.

For example, the input parameter **nodeType** is not within the range of **OH\_AudioNode\_Type**, or **isSupported** is nullptr.

**AUDIOSUITE\_ERROR\_SYSTEM**: Other system exceptions occur.

 |
