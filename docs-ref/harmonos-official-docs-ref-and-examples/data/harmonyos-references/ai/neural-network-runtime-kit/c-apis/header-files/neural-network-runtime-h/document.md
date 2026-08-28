# neural\_network\_runtime.h

#### Overview

Defines APIs for Neural Network Runtime. The AI inference framework uses the native APIs provided by the Neural Network Runtime to construct and build models.

Currently, the APIs of Neural Network Runtime do not support multi-thread calling.

**File to include**: <neural\_network\_runtime/neural\_network\_runtime.h>

**Library**: libneural\_network\_runtime.so

**System capability**: SystemCapability.Ai.NeuralNetworkRuntime

**Since**: 9

**Related module**: [NeuralNetworkRuntime](../../modules/neuralnetworkruntime/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [NN\_QuantParam \*OH\_NNQuantParam\_Create()](#oh_nnquantparam_create) | Creates an [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance. |
| [OH\_NN\_ReturnCode OH\_NNQuantParam\_SetScales(NN\_QuantParam \*quantParams, const double \*scales, size\_t quantCount)](#oh_nnquantparam_setscales) | 
Sets the scaling coefficient of the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

**quantCount** is the number of quantization parameters in the tensor. For example, for per-channel quantization, **quantCount** is the number of channels.

 |
| [OH\_NN\_ReturnCode OH\_NNQuantParam\_SetZeroPoints(NN\_QuantParam \*quantParams, const int32\_t \*zeroPoints, size\_t quantCount)](#oh_nnquantparam_setzeropoints) | 

Sets the zero point of the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

**quantCount** is the number of quantization parameters in the tensor. For example, for per-channel quantization, **quantCount** is the number of channels.

 |
| [OH\_NN\_ReturnCode OH\_NNQuantParam\_SetNumBits(NN\_QuantParam \*quantParams, const uint32\_t \*numBits, size\_t quantCount)](#oh_nnquantparam_setnumbits) | 

Sets the quantization bit width of the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

**quantCount** is the number of quantization parameters in the tensor. For example, for per-channel quantization, **quantCount** is the number of channels.

 |
| [OH\_NN\_ReturnCode OH\_NNQuantParam\_Destroy(NN\_QuantParam \*\*quantParams)](#oh_nnquantparam_destroy) | 

Destroys an [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

After an [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance is no longer needed after being passed to [NN\_Tensor](../../structs/nn-tensor/document.md), you need to destroy it to avoid memory leak.

If **quantParams** or \***quantParams** is a null pointer, this API only prints warning logs but does not perform the destruction operation.

 |
| [OH\_NNModel \*OH\_NNModel\_Construct(void)](#oh_nnmodel_construct) | Creates an [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| [OH\_NN\_ReturnCode OH\_NNModel\_AddTensorToModel(OH\_NNModel \*model, const NN\_TensorDesc \*tensorDesc)](#oh_nnmodel_addtensortomodel) | 

Adds a tensor to a model instance.

The data node and operator parameters in the NNRt model are composed of tensors of the model.

 |
| [OH\_NN\_ReturnCode OH\_NNModel\_SetTensorData(OH\_NNModel \*model, uint32\_t index, const void \*dataBuffer, size\_t length)](#oh_nnmodel_settensordata) | Sets the tensor value. For tensors with constant values (such as model weights), you need to use this API in the composition phase. The index value of a tensor is determined by the sequence in which the tensor is added to the model. For details about how to add a tensor, see [OH\_NNModel\_AddTensorToModel](#oh_nnmodel_addtensortomodel). |
| [OH\_NN\_ReturnCode OH\_NNModel\_SetTensorQuantParams(OH\_NNModel \*model, uint32\_t index, NN\_QuantParam \*quantParam)](#oh_nnmodel_settensorquantparams) | Sets the quantization parameters of a tensor. For details, see [NN\_QuantParam](../../structs/nn-quantparam/document.md). |
| [OH\_NN\_ReturnCode OH\_NNModel\_SetTensorType(OH\_NNModel \*model, uint32\_t index, OH\_NN\_TensorType tensorType)](#oh_nnmodel_settensortype) | Sets the tensor type. For details, see [OH\_NN\_TensorType](../neural-network-runtime-type-h/document.md#oh_nn_tensortype). |
| [OH\_NN\_ReturnCode OH\_NNModel\_AddOperation(OH\_NNModel \*model,OH\_NN\_OperationType op,const OH\_NN\_UInt32Array \*paramIndices,const OH\_NN\_UInt32Array \*inputIndices,const OH\_NN\_UInt32Array \*outputIndices)](#oh_nnmodel_addoperation) | Adds an operator to a model instance. |
| [OH\_NN\_ReturnCode OH\_NNModel\_SpecifyInputsAndOutputs(OH\_NNModel \*model,const OH\_NN\_UInt32Array \*inputIndices,const OH\_NN\_UInt32Array \*outputIndices)](#oh_nnmodel_specifyinputsandoutputs) | Sets an index value for the input and output tensors of a model. A tensor must be specified as the end-to-end input and output of a model instance. |
| [OH\_NN\_ReturnCode OH\_NNModel\_Finish(OH\_NNModel \*model)](#oh_nnmodel_finish) | Completes model composition. After the model topology is set up, call this API to indicate that the composition is complete. |
| [void OH\_NNModel\_Destroy(OH\_NNModel \*\*model)](#oh_nnmodel_destroy) | Destroys a model instance. This API needs to be called to destroy the model instance created by calling [OH\_NNModel\_Construct](#oh_nnmodel_construct). Otherwise, memory leak will occur. If **model** or \***model** is a null pointer, this API only prints warning logs but does not perform the destruction operation. |
| [OH\_NN\_ReturnCode OH\_NNModel\_GetAvailableOperations(OH\_NNModel \*model,size\_t deviceID,const bool \*\*isSupported,uint32\_t \*opCount)](#oh_nnmodel_getavailableoperations) | Checks whether all operators in a model are supported by the device. The result is indicated by a Boolean value. |
| [OH\_NN\_ReturnCode OH\_NNModel\_AddTensor(OH\_NNModel \*model, const OH\_NN\_Tensor \*tensor)](#oh_nnmodel_addtensor) | 

Adds a tensor to a model instance.

The data node and operator parameters in the NNRt model are composed of tensors of the model. You can use this API to add tensors to a model instance based on the **tensor** parameter.

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_SetInput(OH\_NNExecutor \*executor,uint32\_t inputIndex,const OH\_NN\_Tensor \*tensor,const void \*dataBuffer,size\_t length)](#oh_nnexecutor_setinput) | Sets the data for a single model input. This API copies the data whose length is specified by **length** (in bytes) in **dataBuffer** to the shared memory of the underlying device. |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_SetOutput(OH\_NNExecutor \*executor,uint32\_t outputIndex,void \*dataBuffer,size\_t length)](#oh_nnexecutor_setoutput) | 

Sets the memory for a single model output.

This API binds the buffer pointed by **dataBuffer** to the output specified by **outputIndex**. The length of the buffer is specified by **length**.

 |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_Run(OH\_NNExecutor \*executor)](#oh_nnexecutor_run) | Perform model inference through This API performs end-to-end model inference and computing on the device associated with the executor. |
| [OH\_NN\_Memory \*OH\_NNExecutor\_AllocateInputMemory(OH\_NNExecutor \*executor, uint32\_t inputIndex, size\_t length)](#oh_nnexecutor_allocateinputmemory) | Applies for shared memory for a single model input on the device. |
| [OH\_NN\_Memory \*OH\_NNExecutor\_AllocateOutputMemory(OH\_NNExecutor \*executor, uint32\_t outputIndex, size\_t length)](#oh_nnexecutor_allocateoutputmemory) | Applies for shared memory for a single model output on the device. |
| [void OH\_NNExecutor\_DestroyInputMemory(OH\_NNExecutor \*executor, uint32\_t inputIndex, OH\_NN\_Memory \*\*memory)](#oh_nnexecutor_destroyinputmemory) | Releases the input memory pointed by the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance. This API is used to release the memory instance created by calling [OH\_NNExecutor\_AllocateInputMemory](#oh_nnexecutor_allocateinputmemory). If this API is not called, memory leakage occurs. |
| [void OH\_NNExecutor\_DestroyOutputMemory(OH\_NNExecutor \*executor, uint32\_t outputIndex, OH\_NN\_Memory \*\*memory)](#oh_nnexecutor_destroyoutputmemory) | Releases the output memory pointed by the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance. This API needs to be called to release the memory instance created by calling [OH\_NNExecutor\_AllocateOutputMemory](#oh_nnexecutor_allocateoutputmemory). Otherwise, memory leak will occur. The mapping between **outputIndex** and **memory** must be the same as that in memory instance creation. If **memory** or \***memory** is a null pointer, this API only prints the warning log and does not execute the release logic. |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_SetInputWithMemory(OH\_NNExecutor \*executor,uint32\_t inputIndex,const OH\_NN\_Tensor \*tensor,const OH\_NN\_Memory \*memory)](#oh_nnexecutor_setinputwithmemory) | Specifies the hardware shared memory pointed by the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance as the shared memory used by a single model input. |
| [OH\_NN\_ReturnCode OH\_NNExecutor\_SetOutputWithMemory(OH\_NNExecutor \*executor,uint32\_t outputIndex,const OH\_NN\_Memory \*memory)](#oh_nnexecutor_setoutputwithmemory) | Specifies the hardware shared memory pointed by the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance as the shared memory used by a single model output. |

#### Function Description

#### \[h2\]OH\_NNQuantParam\_Create()

NN\_QuantParam \*OH\_NNQuantParam\_Create()

**Description**

Creates an [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

After creating an [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance, set its attribute values by calling [OH\_NNQuantParam\_SetScales](#oh_nnquantparam_setscales), [OH\_NNQuantParam\_SetZeroPoints](#oh_nnquantparam_setzeropoints), or [OH\_NNQuantParam\_SetNumBits](#oh_nnquantparam_setnumbits), and pass it to [NN\_Tensor](../../structs/nn-tensor/document.md) by calling [OH\_NNModel\_SetTensorQuantParams](#oh_nnmodel_settensorquantparams). Finally, call [OH\_NNQuantParam\_Destroy](#oh_nnquantparam_destroy) to destroy the instance to prevent a memory leak.

**Since**: 11

**Returns**

| Type | Description |
| :-- | :-- |
| [NN\_QuantParam](../../structs/nn-quantparam/document.md) \* | Pointer to the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNQuantParam\_SetScales()

OH\_NN\_ReturnCode OH\_NNQuantParam\_SetScales(NN\_QuantParam \*quantParams, const double \*scales, size\_t quantCount)

**Description**

Sets the scaling coefficient of the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

**quantCount** is the number of quantization parameters in the tensor. For example, for per-channel quantization, **quantCount** is the number of channels.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_QuantParam](../../structs/nn-quantparam/document.md) \*quantParams | Pointer to the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance. |
| const double \*scales | Array consisting of scaling coefficients of all quantization parameters in the tensor. |
| size\_t quantCount | Number of quantization parameters in a tensor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNQuantParam\_SetZeroPoints()

OH\_NN\_ReturnCode OH\_NNQuantParam\_SetZeroPoints(NN\_QuantParam \*quantParams, const int32\_t \*zeroPoints, size\_t quantCount)

**Description**

Sets the zero point of the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

**quantCount** is the number of quantization parameters in the tensor. For example, for per-channel quantization, **quantCount** is the number of channels.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_QuantParam](../../structs/nn-quantparam/document.md) \*quantParams | Pointer to the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance. |
| const int32\_t \*zeroPoints | Array consisting of zero points of all quantization parameters in a tensor. |
| size\_t quantCount | Number of quantization parameters in a tensor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNQuantParam\_SetNumBits()

OH\_NN\_ReturnCode OH\_NNQuantParam\_SetNumBits(NN\_QuantParam \*quantParams, const uint32\_t \*numBits, size\_t quantCount)

**Description**

Sets the quantization bit width of the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

**quantCount** is the number of quantization parameters in the tensor. For example, for per-channel quantization, **quantCount** is the number of channels.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_QuantParam](../../structs/nn-quantparam/document.md) \*quantParams | Pointer to the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance. |
| const uint32\_t \*numBits | Array consisting of quantization bits of all quantization parameters in a tensor. |
| size\_t quantCount | Number of quantization parameters in a tensor. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNQuantParam\_Destroy()

OH\_NN\_ReturnCode OH\_NNQuantParam\_Destroy(NN\_QuantParam \*\*quantParams)

**Description**

Destroys an [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance.

After an [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance is no longer needed after being passed to [NN\_Tensor](../../structs/nn-tensor/document.md), you need to destroy it to avoid memory leak.

If **quantParams** or \***quantParams** is a null pointer, this API only prints warning logs but does not perform the destruction operation.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [NN\_QuantParam](../../structs/nn-quantparam/document.md) \*\*quantParams | Level-2 pointer to the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_Construct()

OH\_NNModel \*OH\_NNModel\_Construct(void)

**Description**

Creates an [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance.

Before graph composition, call [OH\_NNModel\_Construct](#oh_nnmodel_construct) to create a model instance. Based on the model topology, call [OH\_NNModel\_AddTensorToModel](#oh_nnmodel_addtensortomodel), [OH\_NNModel\_AddOperation](#oh_nnmodel_addoperation), and [OH\_NNModel\_SetTensorData](#oh_nnmodel_settensordata) to fill in the data and operator nodes of the model, and then call [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) to specify the input and output of the model. After the model topology is constructed, call [OH\_NNModel\_Finish](#oh_nnmodel_finish) to build the model.

If a model instance is no longer needed, destroy it by calling [OH\_NNModel\_Destroy](#oh_nnmodel_destroy) to prevent a memory leak.

**Since**: 9

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \* | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNModel\_AddTensorToModel()

OH\_NN\_ReturnCode OH\_NNModel\_AddTensorToModel(OH\_NNModel \*model, const NN\_TensorDesc \*tensorDesc)

**Description**

Adds a tensor to a model instance.

The data node and operator parameters in the NNRt model are composed of tensors of the model.

This API adds tensors to a model instance based on [NN\_TensorDesc](../../structs/nn-tensordesc/document.md). The sequence of adding tensors is specified by the index value recorded in the model. The [OH\_NNModel\_SetTensorData](#oh_nnmodel_settensordata), [OH\_NNModel\_AddOperation](#oh_nnmodel_addoperation), and [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) APIs specify tensors based on the index value.

NNRt supports input and output of dynamic shapes. When adding a data node with a dynamic shape, you need to set the dimensions that support dynamic changes in **tensor.dimensions** to **\-1**. For example, if **tensor.dimensions** of a four-dimensional tensor is set to **\[1, -1, 2, 2\]**, the second dimension supports dynamic changes.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| [const NN\_TensorDesc](../../structs/nn-tensordesc/document.md) \*tensorDesc | Pointer to the [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) tensor, where [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) specify the attributes of the tensor to be added to the model instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_SetTensorData()

OH\_NN\_ReturnCode OH\_NNModel\_SetTensorData(OH\_NNModel \*model, uint32\_t index, const void \*dataBuffer, size\_t length)

**Description**

Sets the tensor value. For tensors with constant values (such as model weights), you need to use this API in the composition phase.

The index value of a tensor is determined by the sequence in which the tensor is added to the model. For details about how to add a tensor, see [OH\_NNModel\_AddTensorToModel](#oh_nnmodel_addtensortomodel).

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| uint32\_t index | Index value of a tensor. |
| const void \*dataBuffer | Pointer to the real data memory. |
| size\_t length | Length of the data memory. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_SetTensorQuantParams()

OH\_NN\_ReturnCode OH\_NNModel\_SetTensorQuantParams(OH\_NNModel \*model, uint32\_t index, NN\_QuantParam \*quantParam)

**Description**

Sets the quantization parameters of a tensor. For details, see [NN\_QuantParam](../../structs/nn-quantparam/document.md).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| uint32\_t index | Index value of a tensor. |
| [NN\_QuantParam](../../structs/nn-quantparam/document.md) \*quantParam | Pointer to the [NN\_QuantParam](../../structs/nn-quantparam/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_SetTensorType()

OH\_NN\_ReturnCode OH\_NNModel\_SetTensorType(OH\_NNModel \*model, uint32\_t index, OH\_NN\_TensorType tensorType)

**Description**

Sets the tensor type. For details, see [OH\_NN\_TensorType](../neural-network-runtime-type-h/document.md#oh_nn_tensortype).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| uint32\_t index | Index value of a tensor. |
| [OH\_NN\_TensorType](../neural-network-runtime-type-h/document.md#oh_nn_tensortype) tensorType | Tensor type. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_AddOperation()

OH\_NN\_ReturnCode OH\_NNModel\_AddOperation(OH\_NNModel \*model,OH\_NN\_OperationType op,const OH\_NN\_UInt32Array \*paramIndices,const OH\_NN\_UInt32Array \*inputIndices,const OH\_NN\_UInt32Array \*outputIndices)

**Description**

Adds an operator to a model instance.

You can use this API to add an operator to a model instance. The operator type is specified by **op**, and the operator parameters, inputs, and outputs are specified by **paramIndices**, **inputIndices**, and **outputIndices** respectively.

This API verifies the attributes of operator parameters and the number of input and output parameters. These attributes must be correctly set when [OH\_NNModel\_AddTensorToModel](#oh_nnmodel_addtensortomodel) is called to add tensors.

For details about the expected parameters, input attributes, and output attributes of each operator, see [OH\_NN\_OperationType](../neural-network-runtime-type-h/document.md#oh_nn_operationtype).

**paramIndices**, **inputIndices**, and **outputIndices** store index values of tensors. Index values are determined by the sequence in which tensors are added to the model.

For details about how to add a tensor, see [OH\_NNModel\_AddTensorToModel](#oh_nnmodel_addtensortomodel).

If unnecessary parameters are added for adding an operator, this API returns the error code [OH\_NN\_INVALID\_PARAMETER](../neural-network-runtime-type-h/document.md#oh_nn_returncode). If no operator parameter is set, the operator uses the default parameter value. For details about the default values, see OH\_NN\_OperationType\](capi-neural-network-runtime-type-h.md#oh\_nn\_operationtype).

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| [OH\_NN\_OperationType](../neural-network-runtime-type-h/document.md#oh_nn_operationtype) op | Type of the operator to be added. For details, see [OH\_NN\_OperationType](../neural-network-runtime-type-h/document.md#oh_nn_operationtype). |
| [const OH\_NN\_UInt32Array](../../structs/oh-nn-uint32array/document.md) \*paramIndices | Pointer to the **OH\_NN\_UInt32Array** instance, which is used to set the parameter tensor index of the operator. |
| [const OH\_NN\_UInt32Array](../../structs/oh-nn-uint32array/document.md) \*inputIndices | Pointer to the **OH\_NN\_UInt32Array** instance, specifying the input tensor index of the operator. |
| [const OH\_NN\_UInt32Array](../../structs/oh-nn-uint32array/document.md) \*outputIndices | Pointer to the **OH\_NN\_UInt32Array** instance, which is used to set the output tensor index of the operator. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_SpecifyInputsAndOutputs()

OH\_NN\_ReturnCode OH\_NNModel\_SpecifyInputsAndOutputs(OH\_NNModel \*model,const OH\_NN\_UInt32Array \*inputIndices,const OH\_NN\_UInt32Array \*outputIndices)

**Description**

Sets an index value for the input and output tensors of a model.

A tensor must be specified as the end-to-end input and output of a model instance. After a tensor is set as the input or output tensor, you are not allowed to set the tensor data by calling [OH\_NNModel\_SetTensorData](#oh_nnmodel_settensordata). Instead, call OH\_NNExecutor in the execution phase to set the input or output tensor data.

The index value of a tensor is determined by the sequence in which the tensor is added to the model. For details about how to add a tensor, see [OH\_NNModel\_AddTensorToModel](#oh_nnmodel_addtensortomodel). Currently, the model input and output cannot be set asynchronously.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| [const OH\_NN\_UInt32Array](../../structs/oh-nn-uint32array/document.md) \*inputIndices | Pointer to the **OH\_NN\_UInt32Array** instance, which is used to set the input tensor of the operator. |
| [const OH\_NN\_UInt32Array](../../structs/oh-nn-uint32array/document.md) \*outputIndices | Pointer to the OH\_NN\_UInt32Array instance, which is used to set the output tensor of the operator. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_Finish()

OH\_NN\_ReturnCode OH\_NNModel\_Finish(OH\_NNModel \*model)

**Description**

Completes model composition.

After the model topology is set up, call this API to indicate that the composition is complete.

After this API is called, additional graph composition cannot be performed. If [OH\_NNModel\_AddTensorToModel](#oh_nnmodel_addtensortomodel), [OH\_NNModel\_AddOperation](#oh_nnmodel_addoperation), [OH\_NNModel\_SetTensorData](#oh_nnmodel_settensordata), or [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called, [OH\_NN\_OPERATION\_FORBIDDEN](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.

Before calling Before calling [OH\_NNModel\_GetAvailableOperations](#oh_nnmodel_getavailableoperations) and [OH\_NNCompilation\_Construct](../neural-network-core-h/document.md#oh_nncompilation_construct), you must call this API to complete composition., you must call this API to complete composition.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_Destroy()

void OH\_NNModel\_Destroy(OH\_NNModel \*\*model)

**Description**

Destroys a model instance.

This API needs to be called to destroy the model instance created by calling [OH\_NNModel\_Construct](#oh_nnmodel_construct). Otherwise, memory leak will occur.

If **model** or \***model** is a null pointer, this API only prints warning logs but does not perform the destruction operation.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*\*model | Level-2 pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. After a model instance is destroyed, this API sets \***model** to a null pointer. |

#### \[h2\]OH\_NNModel\_GetAvailableOperations()

OH\_NN\_ReturnCode OH\_NNModel\_GetAvailableOperations(OH\_NNModel \*model,size\_t deviceID,const bool \*\*isSupported,uint32\_t \*opCount)

**Description**

Checks whether all operators in a model are supported by the device. The result is indicated by a Boolean value.

Checks whether the underlying device supports operators in a model instance. The device is specified by **deviceID**, and the result is represented by the array pointed by **isSupported**.

If the ith operator is supported, the value of **(\*isSupported)**\[i\] is **true**. Otherwise, the value is **false**. After this API is successfully executed, \*\*(isSupported)\* points to the bool array that records the operator support status. The operator quantity for the array length is the same as that for the model instance.

The memory corresponding to this array is managed by NNRt and is automatically destroyed after the model instance is destroyed or this API is called again.

**Since**: 9

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| size\_t deviceID | Device ID to be queried, which can be obtained by using [OH\_NNDevice\_GetAllDevicesID](../neural-network-core-h/document.md#oh_nndevice_getalldevicesid). |
| const bool \*\*isSupported | Pointer to the **bool** array. The input \***isSupported** must be a null pointer. Otherwise, [OH\_NN\_INVALID\_PARAMETER](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned. |
| uint32\_t \*opCount | Number of operators in a model instance, corresponding to the length of the \***isSupported** array. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNModel\_AddTensor()

OH\_NN\_ReturnCode OH\_NNModel\_AddTensor(OH\_NNModel \*model, const OH\_NN\_Tensor \*tensor)

**Description**

Adds a tensor to a model instance.

The data node and operator parameters in the NNRt model are composed of tensors of the model. You can use this API to add tensors to a model instance based on the **tensor** parameter.

The sequence of adding tensors is specified by the index value recorded in the model. The [OH\_NNModel\_SetTensorData](#oh_nnmodel_settensordata), [OH\_NNModel\_AddOperation](#oh_nnmodel_addoperation), and [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) APIs specify tensors based on the index value.

NNRt supports input and output of dynamic shapes.

When adding a data node with a dynamic shape, you need to set the dimensions that support dynamic changes in **tensor.dimensions** to **\-1**. For example, if **tensor.dimensions** of a four-dimensional tensor is set to **\[1, -1, 2, 2\]**, the second dimension supports dynamic changes.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNModel\_AddTensorToModel](#oh_nnmodel_addtensortomodel)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) \*model | Pointer to the [OH\_NNModel](../../structs/oh-nnmodel/document.md) instance. |
| [const OH\_NN\_Tensor](../../structs/oh-nn-tensor/document.md) \*tensor | Pointer to the [OH\_NN\_Tensor](../../structs/oh-nn-tensor/document.md) tensor, where **tensor** specifies the attributes of the tensor to be added to the model instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_SetInput()

OH\_NN\_ReturnCode OH\_NNExecutor\_SetInput(OH\_NNExecutor \*executor,uint32\_t inputIndex,const OH\_NN\_Tensor \*tensor,const void \*dataBuffer,size\_t length)

**Description**

Sets the data for a single model input.

This API copies the data whose length is specified by **length** (in bytes) in **dataBuffer** to the shared memory of the underlying device.

**inputIndex** specifies the input to be set and **tensor** sets tensor information such as the shape, type, and quantization parameters.

NNRt supports models with dynamical shape input. For fixed shape input and dynamic shape input scenarios, this API uses different processing policies.

-   Fixed shape input: The attributes of tensor must be the same as those of the tensor added by calling [OH\_NNModel\_AddTensor](#oh_nnmodel_addtensor) in the build phase.
-   Dynamic shape input: In the composition phase, because the shape is not fixed, each value in **tensor.dimensions** must be greater than **0** in the API calls to determine the shape input in the computing phase. When setting the shape, you can modify only the dimension whose value is **\-1**.
    
    Assume that **\[-1, 224, 224, 3\]** is input as the the dimension of A in the composition phase. When this API is called, you can only change the size of the first dimension, for example, to \[3, 224, 224, 3\]. If other dimensions are adjusted, [OH\_NN\_INVALID\_PARAMETER](../neural-network-runtime-type-h/document.md#oh_nn_returncode) is returned.
    

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNExecutor\_RunSync](../neural-network-core-h/document.md#oh_nnexecutor_runsync)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| uint32\_t inputIndex | 
Input index value, which is the same as the sequence of the input data when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called.

Assume that **inputIndices** is {1, 5, 9} when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called. When you set the input data, set the value of this parameter to {0, 1, 2}.

 |
| [const OH\_NN\_Tensor](../../structs/oh-nn-tensor/document.md) \*tensor | Tensor corresponding to the input data. |
| const void \*dataBuffer | Pointer to the input data. |
| size\_t length | Length of the data memory, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_SetOutput()

OH\_NN\_ReturnCode OH\_NNExecutor\_SetOutput(OH\_NNExecutor \*executor,uint32\_t outputIndex,void \*dataBuffer,size\_t length)

**Description**

Sets the memory for a single model output.

This method binds the buffer pointed by **dataBuffer** to the output specified by **outputIndex**. The length of the buffer is specified by **length**.

After [OH\_NNExecutor\_Run](#oh_nnexecutor_run) is called to complete a single model inference, NNRt compares the length of the buffer pointed by **dataBuffer** with the length of the output data and returns different results based on the actual situation.

-   If the memory size is greater than or equal to the data length, the API copies the inference result to the memory and returns [OH\_NN\_SUCCESS](../neural-network-runtime-type-h/document.md#oh_nn_returncode). You can read the inference result from **dataBuffer**.
-   If the memory size is less than the data length, the [OH\_NNExecutor\_Run](#oh_nnexecutor_run) API returns the error code [OH\_NN\_INVALID\_PARAMETER](../neural-network-runtime-type-h/document.md#oh_nn_returncode) and generates a log indicating that the memory size is too small.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNExecutor\_RunSync](../neural-network-core-h/document.md#oh_nnexecutor_runsync)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| uint32\_t outputIndex | 
Output index value, which is the same as the sequence of the output data when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called.

Assume that **outputIndices** is {4, 6, 8} when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called. When you set the output memory, set the value of this parameter to {0, 1, 2}.

 |
| void \*dataBuffer | Pointer to the output data. |
| size\_t length | Length of the data memory, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_Run()

OH\_NN\_ReturnCode OH\_NNExecutor\_Run(OH\_NNExecutor \*executor)

**Description**

Perform model inference through This API performs end-to-end model inference and computing on the device associated with the executor.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNExecutor\_RunSync](../neural-network-core-h/document.md#oh_nnexecutor_runsync)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_AllocateInputMemory()

OH\_NN\_Memory \*OH\_NNExecutor\_AllocateInputMemory(OH\_NNExecutor \*executor, uint32\_t inputIndex, size\_t length)

**Description**

Applies for shared memory for a single model input on the device.

NNRt provides an API for proactively applying for shared memory on a device.

Based on the specified executor and input index value, this API applies for the shared memory whose size is **length** on the device associated with a single input. Then, it returns the shared memory through the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNTensor\_CreateWithSize](../neural-network-core-h/document.md#oh_nntensor_createwithsize)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| uint32\_t inputIndex | 
Input index value, which is the same as the sequence of the input data when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called.

Assume that **inputIndices** is {1, 5, 9} when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called. When you request the input memory, set the value of this parameter to {0, 1, 2}.

 |
| size\_t length | Memory size to be applied for, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) \* | Pointer to the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNExecutor\_AllocateOutputMemory()

OH\_NN\_Memory \*OH\_NNExecutor\_AllocateOutputMemory(OH\_NNExecutor \*executor, uint32\_t outputIndex, size\_t length)

**Description**

Applies for shared memory for a single model output on the device.

NNRt provides an API for proactively applying for shared memory on a device.

Based on the specified executor and output index value, this API applies for the shared memory whose size is **length** on the device associated with a single output. Then, it returns the shared memory through the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNTensor\_CreateWithSize](../neural-network-core-h/document.md#oh_nntensor_createwithsize)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| uint32\_t outputIndex | 
Output index value, which is the same as the sequence of the output data when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called.

Assume that **outputIndices** is {4, 6, 8} when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called. When you request the output memory, set the value of this parameter to {0, 1, 2}.

 |
| size\_t length | Memory size to be applied for, in bytes. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) \* | Pointer to the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance. If the operation fails, **NULL** is returned. |

#### \[h2\]OH\_NNExecutor\_DestroyInputMemory()

void OH\_NNExecutor\_DestroyInputMemory(OH\_NNExecutor \*executor, uint32\_t inputIndex, OH\_NN\_Memory \*\*memory)

**Description**

Releases the input memory pointed by the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance.

This API is used to release the memory instance created by calling [OH\_NNExecutor\_AllocateInputMemory](#oh_nnexecutor_allocateinputmemory). If this API is not called, memory leakage occurs.

The mapping between **inputIndex** and **memory** must be the same as that in memory instance creation. If **memory** or \***memory** is a null pointer, this API only prints the warning log and does not execute the release logic.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNTensor\_Destroy](../neural-network-core-h/document.md#oh_nntensor_destroy)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| uint32\_t inputIndex | 
Input index value, which is the same as the sequence of the input data when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called.

Assume that **inputIndices** is {1, 5, 9} when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called. When you release the input memory, set the value of this parameter to {0, 1, 2}.

 |
| [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) \*\*memory | Level-2 pointer to the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance. After the shared memory is released, this API sets \***memory** to a null pointer. |

#### \[h2\]OH\_NNExecutor\_DestroyOutputMemory()

void OH\_NNExecutor\_DestroyOutputMemory(OH\_NNExecutor \*executor, uint32\_t outputIndex, OH\_NN\_Memory \*\*memory)

**Description**

Releases the output memory pointed by the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance.

This API needs to be called to release the memory instance created by calling [OH\_NNExecutor\_AllocateOutputMemory](#oh_nnexecutor_allocateoutputmemory). Otherwise, memory leak will occur.

The mapping between **outputIndex** and **memory** must be the same as that in memory instance creation.

If **memory** or \***memory** is a null pointer, this API only prints the warning log and does not execute the release logic.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNTensor\_Destroy](../neural-network-core-h/document.md#oh_nntensor_destroy)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| uint32\_t outputIndex | 
Output index value, which is the same as the sequence of the output data when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called.

Assume that **outputIndices** is {4, 6, 8} when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called. When you release the output memory, set the value of this parameter to {0, 1, 2}.

 |
| [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) \*\*memory | Level-2 pointer to the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance. After the shared memory is released, this API sets \***memory** to a null pointer. |

#### \[h2\]OH\_NNExecutor\_SetInputWithMemory()

OH\_NN\_ReturnCode OH\_NNExecutor\_SetInputWithMemory(OH\_NNExecutor \*executor,uint32\_t inputIndex,const OH\_NN\_Tensor \*tensor,const OH\_NN\_Memory \*memory)

**Description**

Specifies the hardware shared memory pointed by the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance as the shared memory used by a single model input.

In the scenario where the memory needs to be managed by yourself, this API binds the input to the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance.

During computing, the underlying device reads the input data from the shared memory pointed to by the memory instance.

By using this API, you can implement concurrent execution of input setting, computing, and read to improve the data flow inference efficiency.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNExecutor\_RunSync](../neural-network-core-h/document.md#oh_nnexecutor_runsync)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) instance. |
| uint32\_t inputIndex | 
Input index value, which is the same as the sequence of the input data when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called.

Assume that **inputIndices** is {1, 5, 9} when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called. When you specify the input shared memory, set the value of this parameter to {0, 1, 2}.

 |
| [const OH\_NN\_Tensor](../../structs/oh-nn-tensor/document.md) \*tensor | Pointer to the [OH\_NN\_Tensor](../../structs/oh-nn-tensor/document.md) instance, which is used to set the tensor corresponding to a single input. |
| [const OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) \*memory | Pointer to the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |

#### \[h2\]OH\_NNExecutor\_SetOutputWithMemory()

OH\_NN\_ReturnCode OH\_NNExecutor\_SetOutputWithMemory(OH\_NNExecutor \*executor,uint32\_t outputIndex,const OH\_NN\_Memory \*memory)

**Description**

Specifies the hardware shared memory pointed by the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance as the shared memory used by a single model output.

In the scenario where the memory needs to be managed by yourself, this API binds the output to the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance.

During computing, the underlying device writes the computing result to the shared memory pointed by the memory instance.

By using this API, you can implement concurrent execution of input setting, computing, and read to improve the data flow inference efficiency.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [OH\_NNExecutor\_RunSync](../neural-network-core-h/document.md#oh_nnexecutor_runsync)

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) \*executor | Pointer to the executor. |
| uint32\_t outputIndex | 
Output index value, which is the same as the sequence of the output data when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called.

Assume that **outputIndices** is {4, 6, 8} when [OH\_NNModel\_SpecifyInputsAndOutputs](#oh_nnmodel_specifyinputsandoutputs) is called. When you specify the output shared memory, set the value of this parameter to {0, 1, 2}.

 |
| [const OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) \*memory | Pointer to the [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) instance. |

**Returns**

| Type | Description |
| :-- | :-- |
| [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode) | Execution result of the function. If the operation is successful, **OH\_NN\_SUCCESS** is returned. If the operation fails, an error is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../neural-network-runtime-type-h/document.md#oh_nn_returncode). |
