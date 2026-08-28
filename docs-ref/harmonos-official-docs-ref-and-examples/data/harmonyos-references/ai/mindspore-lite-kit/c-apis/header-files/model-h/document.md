# model.h

#### Overview

Provides model-related APIs for model creation and inference. These APIs are non-thread-safe.

**File to include**: <mindspore/model.h>

**Library**: libmindspore\_lite\_ndk.so

**System capability**: SystemCapability.Ai.MindSpore

**Since**: 9

**Related module**: [MindSpore](../../modules/mindspore/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| OH\_AI\_TensorHandleArray | [OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) | Defines the tensor array structure, which is used to store the tensor array pointer and tensor array length. |
| OH\_AI\_ShapeInfo | [OH\_AI\_ShapeInfo](../../structs/oh-ai-shapeinfo/document.md) | Maximum number of shapes. The maximum value reserved is **32**, and the maximum number currently supported is **8**. |
| OH\_AI\_CallBackParam | [OH\_AI\_CallBackParam](../../structs/oh-ai-callbackparam/document.md) | Defines the operator information passed in a callback. |
| void \* | [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) | Defines the pointer to a model object. |
| void \* | [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) | Defines the pointer to a training configuration object. |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef bool (\*OH\_AI\_KernelCallBack)(const OH\_AI\_TensorHandleArray inputs, const OH\_AI\_TensorHandleArray outputs,const OH\_AI\_CallBackParam kernel\_Info)](#oh_ai_kernelcallback) | OH\_AI\_KernelCallBack | 
Defines the pointer to a callback.

This pointer is used to set the two callback functions in [OH\_AI\_ModelPredict](#oh_ai_modelpredict).

Each callback function must contain three parameters, where **inputs** and **outputs** indicate the input and output tensors of the operator, and **kernel\_Info** indicates information about the current operator.

You can use the callback functions to monitor the operator execution status, for example, operator execution time and the operator correctness.

 |
| [OH\_AI\_API OH\_AI\_ModelHandle OH\_AI\_ModelCreate(void)](#oh_ai_modelcreate) | \- | Creates a model object. |
| [OH\_AI\_API void OH\_AI\_ModelDestroy(OH\_AI\_ModelHandle \*model)](#oh_ai_modeldestroy) | \- | Destroys a model object. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelBuild(OH\_AI\_ModelHandle model, const void \*model\_data, size\_t data\_size,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context)](#oh_ai_modelbuild) | \- | 

Loads and builds a MindSpore Lite model from the memory buffer.

Note that the same [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) object can only be passed to [OH\_AI\_ModelBuild](#oh_ai_modelbuild) or [OH\_AI\_ModelBuildFromFile](#oh_ai_modelbuildfromfile) once. If you call this function multiple times, make sure that you create multiple [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) objects accordingly.

 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context)](#oh_ai_modelbuildfromfile) | \- | 

Loads and builds a MindSpore Lite model from a model file.

Note that the same [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) object can only be passed to [OH\_AI\_ModelBuild](#oh_ai_modelbuild) or [OH\_AI\_ModelBuildFromFile](#oh_ai_modelbuildfromfile) once. If you call this function multiple times, make sure that you create multiple [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) objects accordingly.

 |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelResize(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray inputs,OH\_AI\_ShapeInfo \*shape\_infos, size\_t shape\_info\_num)](#oh_ai_modelresize) | \- | Adjusts the input tensor shapes of a built model. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelPredict(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray inputs,OH\_AI\_TensorHandleArray \*outputs, const OH\_AI\_KernelCallBack before,const OH\_AI\_KernelCallBack after)](#oh_ai_modelpredict) | \- | Performs model inference. |
| [OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetInputs(const OH\_AI\_ModelHandle model)](#oh_ai_modelgetinputs) | \- | Obtains the input tensor array structure of a model. |
| [OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetOutputs(const OH\_AI\_ModelHandle model)](#oh_ai_modelgetoutputs) | \- | Obtains the output tensor array structure of a model. |
| [OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_ModelGetInputByTensorName(const OH\_AI\_ModelHandle model, const char \*tensor\_name)](#oh_ai_modelgetinputbytensorname) | \- | Obtains the input tensor of a model by tensor name. |
| [OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_ModelGetOutputByTensorName(const OH\_AI\_ModelHandle model, const char \*tensor\_name)](#oh_ai_modelgetoutputbytensorname) | \- | Obtains the output tensor of a model by tensor name. |
| [OH\_AI\_API OH\_AI\_TrainCfgHandle OH\_AI\_TrainCfgCreate()](#oh_ai_traincfgcreate) | \- | Creates the pointer to the training configuration object. This API is used only for on-device training. |
| [OH\_AI\_API void OH\_AI\_TrainCfgDestroy(OH\_AI\_TrainCfgHandle \*train\_cfg)](#oh_ai_traincfgdestroy) | \- | Destroys the pointer to the training configuration object. This API is used only for on-device training. |
| [OH\_AI\_API char \*\*OH\_AI\_TrainCfgGetLossName(OH\_AI\_TrainCfgHandle train\_cfg, size\_t \*num)](#oh_ai_traincfggetlossname) | \- | Obtains the list of loss functions, which are used only for on-device training. |
| [OH\_AI\_API void OH\_AI\_TrainCfgSetLossName(OH\_AI\_TrainCfgHandle train\_cfg, const char \*\*loss\_name, size\_t num)](#oh_ai_traincfgsetlossname) | \- | Sets the list of loss functions, which are used only for on-device training. |
| [OH\_AI\_API OH\_AI\_OptimizationLevel OH\_AI\_TrainCfgGetOptimizationLevel(OH\_AI\_TrainCfgHandle train\_cfg)](#oh_ai_traincfggetoptimizationlevel) | \- | Obtains the optimization level of the training configuration object. This API is used only for on-device training. |
| [OH\_AI\_API void OH\_AI\_TrainCfgSetOptimizationLevel(OH\_AI\_TrainCfgHandle train\_cfg, OH\_AI\_OptimizationLevel level)](#oh_ai_traincfgsetoptimizationlevel) | \- | Sets the optimization level of the training configuration object. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_TrainModelBuild(OH\_AI\_ModelHandle model, const void \*model\_data, size\_t data\_size,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context,const OH\_AI\_TrainCfgHandle train\_cfg)](#oh_ai_trainmodelbuild) | \- | Loads a training model from the memory buffer and compiles the model to a state ready for running on the device. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_TrainModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path,OH\_AI\_ModelType model\_type,const OH\_AI\_ContextHandle model\_context,const OH\_AI\_TrainCfgHandle train\_cfg)](#oh_ai_trainmodelbuildfromfile) | \- | Loads the training model from the specified path and compiles the model to a state ready for running on the device. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_RunStep(OH\_AI\_ModelHandle model, const OH\_AI\_KernelCallBack before,const OH\_AI\_KernelCallBack after)](#oh_ai_runstep) | \- | Defines a single-step training model. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetLearningRate(OH\_AI\_ModelHandle model, float learning\_rate)](#oh_ai_modelsetlearningrate) | \- | Sets the learning rate for model training. This API is used only for on-device training. |
| [OH\_AI\_API float OH\_AI\_ModelGetLearningRate(OH\_AI\_ModelHandle model)](#oh_ai_modelgetlearningrate) | \- | Obtains the learning rate for model training. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetWeights(OH\_AI\_ModelHandle model)](#oh_ai_modelgetweights) | \- | Obtains all weight tensors of a model. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelUpdateWeights(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray new\_weights)](#oh_ai_modelupdateweights) | \- | Updates the weight tensors of a model. This API is used only for on-device training. |
| [OH\_AI\_API bool OH\_AI\_ModelGetTrainMode(OH\_AI\_ModelHandle model)](#oh_ai_modelgettrainmode) | \- | Obtains the training mode. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetTrainMode(OH\_AI\_ModelHandle model, bool train)](#oh_ai_modelsettrainmode) | \- | Sets the training mode. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetupVirtualBatch(OH\_AI\_ModelHandle model, int virtual\_batch\_multiplier, float lr,float momentum)](#oh_ai_modelsetupvirtualbatch) | \- | Sets the virtual batch for training. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportModel(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type, const char \*model\_file,OH\_AI\_QuantizationType quantization\_type, bool export\_inference\_only,char \*\*output\_tensor\_name, size\_t num)](#oh_ai_exportmodel) | \- | Exports a training model. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportModelBuffer(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type, void \*model\_data,size\_t \*data\_size, OH\_AI\_QuantizationType quantization\_type,bool export\_inference\_only, char \*\*output\_tensor\_name, size\_t num)](#oh_ai_exportmodelbuffer) | \- | Exports the memory cache of the training model. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportWeightsCollaborateWithMicro(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type,const char \*weight\_file, bool is\_inference,bool enable\_fp16, char \*\*changeable\_weights\_name,size\_t num)](#oh_ai_exportweightscollaboratewithmicro) | \- | Exports the weight file of the training model for micro inference. This API is used only for on-device training. |
| [OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelLoadConfig(OH\_AI\_ModelHandle model, const char \*config\_path)](#oh_ai_modelloadconfig) | \- | Loads the model configuration file. |

#### Function Description

#### \[h2\]OH\_AI\_KernelCallBack()

typedef bool (\*OH\_AI\_KernelCallBack)(const OH\_AI\_TensorHandleArray inputs, const OH\_AI\_TensorHandleArray outputs,const OH\_AI\_CallBackParam kernel\_Info)

**Description**

Defines the pointer to a callback.

This pointer is used to set the two callback functions in [OH\_AI\_ModelPredict](#oh_ai_modelpredict).

Each callback function must contain three parameters, where **inputs** and **outputs** indicate the input and output tensors of the operator, and **kernel\_Info** indicates information about the current operator.

You can use the callback functions to monitor the operator execution status, for example, operator execution time and the operator correctness.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) inputs | Tensor array structure corresponding to the model input. |
| const [OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) outputs | Tensor array structure corresponding to the model output. |
| const [OH\_AI\_CallBackParam](../../structs/oh-ai-callbackparam/document.md) kernel\_Info | Information about the current operator. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | **true** if the operation is successful; **false** otherwise. |

#### \[h2\]OH\_AI\_ModelCreate()

OH\_AI\_API OH\_AI\_ModelHandle OH\_AI\_ModelCreate(void)

**Description**

Creates a model object.

**Since**: 9

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) | Pointer to the model object. |

#### \[h2\]OH\_AI\_ModelDestroy()

OH\_AI\_API void OH\_AI\_ModelDestroy(OH\_AI\_ModelHandle \*model)

**Description**

Destroys a model object.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) \*model | Pointer to the model object. |

#### \[h2\]OH\_AI\_ModelBuild()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelBuild(OH\_AI\_ModelHandle model, const void \*model\_data, size\_t data\_size,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context)

**Description**

Loads and builds a MindSpore Lite model from the memory buffer.

Note that the same [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) object can only be passed to [OH\_AI\_ModelBuild](#oh_ai_modelbuild) or [OH\_AI\_ModelBuildFromFile](#oh_ai_modelbuildfromfile) once. If you call this function multiple times, make sure that you create multiple [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) objects accordingly.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| const void \*model\_data | Address of the loaded model data in the memory. |
| size\_t data\_size | Length of the model data. |
| [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype) model\_type | Model file type, which is specified by [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype). |
| const [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) model\_context | Model runtime context, which is specified by [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelBuildFromFile()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context)

**Description**

Loads and builds a MindSpore Lite model from a model file.

Note that the same [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) object can only be passed to [OH\_AI\_ModelBuild](#oh_ai_modelbuild) or [OH\_AI\_ModelBuildFromFile](#oh_ai_modelbuildfromfile) once. If you call this function multiple times, make sure that you create multiple [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) objects accordingly.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| const char \*model\_path | Path of the model file. The string length is subject to the file system. |
| [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype) model\_type | Model file type, which is specified by [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype). |
| const [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) model\_context | Model runtime context, which is specified by [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md). |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelResize()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelResize(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray inputs,OH\_AI\_ShapeInfo \*shape\_infos, size\_t shape\_info\_num)

**Description**

Adjusts the input tensor shapes of a built model.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| [const OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) inputs | Tensor array structure corresponding to the model input. |
| [OH\_AI\_ShapeInfo](../../structs/oh-ai-shapeinfo/document.md) \*shape\_infos | Input shape information array, which consists of tensor shapes arranged in the model input sequence. The model adjusts the tensor shapes in sequence. |
| size\_t shape\_info\_num | Length of the shape information array. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelPredict()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelPredict(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray inputs,OH\_AI\_TensorHandleArray \*outputs, const OH\_AI\_KernelCallBack before,const OH\_AI\_KernelCallBack after)

**Description**

Performs model inference.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| [const OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) inputs | Tensor array structure corresponding to the model input. |
| [OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) \*outputs | Pointer to the tensor array structure corresponding to the model output. |
| [const OH\_AI\_KernelCallBack](#oh_ai_kernelcallback) before | Callback function executed before model inference. |
| [const OH\_AI\_KernelCallBack](#oh_ai_kernelcallback) after | Callback function executed after model inference. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelGetInputs()

OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetInputs(const OH\_AI\_ModelHandle model)

**Description**

Obtains the input tensor array structure of a model.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) | Tensor array structure corresponding to the model input. |

#### \[h2\]OH\_AI\_ModelGetOutputs()

OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetOutputs(const OH\_AI\_ModelHandle model)

**Description**

Obtains the output tensor array structure of a model.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) | Tensor array structure corresponding to the model output. |

#### \[h2\]OH\_AI\_ModelGetInputByTensorName()

OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_ModelGetInputByTensorName(const OH\_AI\_ModelHandle model, const char \*tensor\_name)

**Description**

Obtains the input tensor of a model by tensor name.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| const char \*tensor\_name | Tensor name. The string length is subject to system restrictions. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) | Pointer to the input tensor indicated by **tensor\_name**. If the tensor does not exist, **null** will be returned. |

#### \[h2\]OH\_AI\_ModelGetOutputByTensorName()

OH\_AI\_API OH\_AI\_TensorHandle OH\_AI\_ModelGetOutputByTensorName(const OH\_AI\_ModelHandle model, const char \*tensor\_name)

**Description**

Obtains the output tensor of a model by tensor name.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| const [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| const char \*tensor\_name | Tensor name. The string length is subject to system restrictions. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_TensorHandle](../../structs/oh-ai-tensorhandle/document.md) | Pointer to the output tensor indicated by **tensor\_name**. If the tensor does not exist, **null** will be returned. |

#### \[h2\]OH\_AI\_TrainCfgCreate()

OH\_AI\_API OH\_AI\_TrainCfgHandle OH\_AI\_TrainCfgCreate()

**Description**

Creates the pointer to the training configuration object. This API is used only for on-device training.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) | Pointer to the training configuration object. |

#### \[h2\]OH\_AI\_TrainCfgDestroy()

OH\_AI\_API void OH\_AI\_TrainCfgDestroy(OH\_AI\_TrainCfgHandle \*train\_cfg)

**Description**

Destroys the pointer to the training configuration object. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) \*train\_cfg | Pointer to the training configuration object. |

#### \[h2\]OH\_AI\_TrainCfgGetLossName()

OH\_AI\_API char \*\*OH\_AI\_TrainCfgGetLossName(OH\_AI\_TrainCfgHandle train\_cfg, size\_t \*num)

**Description**

Obtains the list of loss functions, which are used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) train\_cfg | Pointer to the training configuration object. |
| size\_t \*num | Number of loss functions. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API char \*\* | List of loss functions. |

#### \[h2\]OH\_AI\_TrainCfgSetLossName()

OH\_AI\_API void OH\_AI\_TrainCfgSetLossName(OH\_AI\_TrainCfgHandle train\_cfg, const char \*\*loss\_name, size\_t num)

**Description**

Sets the list of loss functions, which are used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) train\_cfg | Pointer to the training configuration object. |
| const char \*\*loss\_name | List of loss functions. |
| size\_t num | Number of loss functions. |

#### \[h2\]OH\_AI\_TrainCfgGetOptimizationLevel()

OH\_AI\_API OH\_AI\_OptimizationLevel OH\_AI\_TrainCfgGetOptimizationLevel(OH\_AI\_TrainCfgHandle train\_cfg)

**Description**

Obtains the optimization level of the training configuration object. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) train\_cfg | Pointer to the training configuration object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_OptimizationLevel](../types-h/document.md#oh_ai_optimizationlevel) | Optimization level. |

#### \[h2\]OH\_AI\_TrainCfgSetOptimizationLevel()

OH\_AI\_API void OH\_AI\_TrainCfgSetOptimizationLevel(OH\_AI\_TrainCfgHandle train\_cfg, OH\_AI\_OptimizationLevel level)

**Description**

Sets the optimization level of the training configuration object. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) train\_cfg | Pointer to the training configuration object. |
| [OH\_AI\_OptimizationLevel](../types-h/document.md#oh_ai_optimizationlevel) level | Optimization level. |

#### \[h2\]OH\_AI\_TrainModelBuild()

OH\_AI\_API OH\_AI\_Status OH\_AI\_TrainModelBuild(OH\_AI\_ModelHandle model, const void \*model\_data, size\_t data\_size,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context,const OH\_AI\_TrainCfgHandle train\_cfg)

**Description**

Loads a training model from the memory buffer and compiles the model to a state ready for running on the device. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| const void \*model\_data | Pointer to the buffer that stores the model file to be read. |
| size\_t data\_size | Buffer size. |
| [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype) model\_type | Model file type, which is specified by [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype). |
| const [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) model\_context | Model runtime context, which is specified by [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md). |
| const [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) train\_cfg | Pointer to the training configuration object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_TrainModelBuildFromFile()

OH\_AI\_API OH\_AI\_Status OH\_AI\_TrainModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path,OH\_AI\_ModelType model\_type,const OH\_AI\_ContextHandle model\_context,const OH\_AI\_TrainCfgHandle train\_cfg)

**Description**

Loads the training model from the specified path and compiles the model to a state ready for running on the device. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| const char \*model\_path | Path of the model file. The string length is subject to the file system. |
| [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype) model\_type | Model file type, which is specified by [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype). |
| const [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md) model\_context | Model runtime context, which is specified by [OH\_AI\_ContextHandle](../../structs/oh-ai-contexthandle/document.md). |
| const [OH\_AI\_TrainCfgHandle](../../structs/oh-ai-traincfghandle/document.md) train\_cfg | Pointer to the training configuration object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_RunStep()

OH\_AI\_API OH\_AI\_Status OH\_AI\_RunStep(OH\_AI\_ModelHandle model, const OH\_AI\_KernelCallBack before,const OH\_AI\_KernelCallBack after)

**Description**

Defines a single-step training model. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| [const OH\_AI\_KernelCallBack](#oh_ai_kernelcallback) before | Callback function executed before model inference. |
| [const OH\_AI\_KernelCallBack](#oh_ai_kernelcallback) after | Callback function executed after model inference. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelSetLearningRate()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetLearningRate(OH\_AI\_ModelHandle model, float learning\_rate)

**Description**

Sets the learning rate for model training. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| float learning\_rate | Learning rate. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelGetLearningRate()

OH\_AI\_API float OH\_AI\_ModelGetLearningRate(OH\_AI\_ModelHandle model)

**Description**

Obtains the learning rate for model training. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API float | Learning rate. If no optimizer is set, the value is **0.0**. |

#### \[h2\]OH\_AI\_ModelGetWeights()

OH\_AI\_API OH\_AI\_TensorHandleArray OH\_AI\_ModelGetWeights(OH\_AI\_ModelHandle model)

**Description**

Obtains all weight tensors of a model. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) | All weight tensors of the model. |

#### \[h2\]OH\_AI\_ModelUpdateWeights()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelUpdateWeights(OH\_AI\_ModelHandle model, const OH\_AI\_TensorHandleArray new\_weights)

**Description**

Updates the weight tensors of a model. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| [const OH\_AI\_TensorHandleArray](../../structs/oh-ai-tensorhandlearray/document.md) new\_weights | Weight tensors to be updated. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelGetTrainMode()

OH\_AI\_API bool OH\_AI\_ModelGetTrainMode(OH\_AI\_ModelHandle model)

**Description**

Obtains the training mode.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API bool | Whether the training mode is used. The value **true** indicates that the training mode is used, and the value **false** indicates the opposite. |

#### \[h2\]OH\_AI\_ModelSetTrainMode()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetTrainMode(OH\_AI\_ModelHandle model, bool train)

**Description**

Sets the training mode. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| bool train | Whether the training mode is used. The value **true** indicates that the training mode is used, and the value **false** indicates the opposite. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelSetupVirtualBatch()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelSetupVirtualBatch(OH\_AI\_ModelHandle model, int virtual\_batch\_multiplier, float lr,float momentum)

**Description**

Sets the virtual batch for training. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| int virtual\_batch\_multiplier | Virtual batch multiplier. If the value is less than **1**, the virtual batch is disabled. The length is subject to system restrictions. |
| float lr | Learning rate. The default value is **\-1.0f**. |
| float momentum | Momentum. The default value is **\-1.0f**. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ExportModel()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportModel(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type, const char \*model\_file,OH\_AI\_QuantizationType quantization\_type, bool export\_inference\_only,char \*\*output\_tensor\_name, size\_t num)

**Description**

Exports a training model. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype) model\_type | Model file type, which is specified by [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype). |
| const char \*model\_file | Path of the exported model file. The string length is subject to the file system. |
| [OH\_AI\_QuantizationType](../types-h/document.md#oh_ai_quantizationtype) quantization\_type | Quantization type. |
| bool export\_inference\_only | Whether to export an inference model. The value **true** means to export an inference model, and the value **false** means the opposite. |
| char \*\*output\_tensor\_name | Output tensor of the exported model. This parameter is left blank by default, which indicates full export. |
| size\_t num | Number of output tensors. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ExportModelBuffer()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportModelBuffer(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type, void \*model\_data,size\_t \*data\_size, OH\_AI\_QuantizationType quantization\_type,bool export\_inference\_only, char \*\*output\_tensor\_name, size\_t num)

**Description**

Exports the memory cache of the training model. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype) model\_type | Model file type, which is specified by [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype). |
| void \*model\_data | Pointer to the buffer that stores the exported model file. |
| size\_t \*data\_size | Buffer size. |
| [OH\_AI\_QuantizationType](../types-h/document.md#oh_ai_quantizationtype) quantization\_type | Quantization type. |
| bool export\_inference\_only | Whether to export an inference model. The value **true** means to export an inference model, and the value **false** means the opposite. |
| char \*\*output\_tensor\_name | Output tensor of the exported model. This parameter is left blank by default, which indicates full export. |
| size\_t num | Number of output tensors. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ExportWeightsCollaborateWithMicro()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ExportWeightsCollaborateWithMicro(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type,const char \*weight\_file, bool is\_inference,bool enable\_fp16, char \*\*changeable\_weights\_name,size\_t num)

**Description**

Exports the weight file of the training model for micro inference. This API is used only for on-device training.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype) model\_type | Model file type, which is specified by [OH\_AI\_ModelType](../types-h/document.md#oh_ai_modeltype). |
| const char \*weight\_file | Path of the exported weight file. The string length is subject to the file system. |
| bool is\_inference | Whether to export inference models. Currently, this parameter can only be set to **true**. |
| bool enable\_fp16 | Whether to save floating-point weights in float16 format. The value **true** means to save floating-point weights in float16 format, and the value **false** means the opposite. |
| char \*\*changeable\_weights\_name | Name of the weight tensor with a variable shape. |
| size\_t num | Number of weight tensors with a variable shape. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |

#### \[h2\]OH\_AI\_ModelLoadConfig()

OH\_AI\_API OH\_AI\_Status OH\_AI\_ModelLoadConfig(OH\_AI\_ModelHandle model, const char \*config\_path);

**Description**

Loads the model configuration file.

**Since**: 20

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_AI\_ModelHandle](../../structs/oh-ai-modelhandle/document.md) model | Pointer to the model object. |
| const char \*config\_path | Configuration file path. The string length is subject to the file system. |

**Returns**

| Type | Description |
| :-- | :-- |
| OH\_AI\_API [OH\_AI\_Status](../status-h/document.md#oh_ai_status) | Status code enumerated by [OH\_AI\_Status](../status-h/document.md#oh_ai_status). The value **OH\_AI\_STATUS\_SUCCESS** indicates that the operation is successful. If the operation fails, an error code is returned. |
