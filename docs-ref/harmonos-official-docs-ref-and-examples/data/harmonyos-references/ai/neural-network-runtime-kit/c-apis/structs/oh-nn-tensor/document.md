# OH\_NN\_Tensor

#### Overview

Defines the tensor structure.

It is usually used to construct data nodes and operator parameters in a model diagram. When constructing a tensor, you need to specify the data type, number of dimensions, dimension information, and quantization information.

**Since**: 9

**Deprecated from**: 11

**Substitute**: [NN\_TensorDesc](../nn-tensordesc/document.md)

**Related module**: [NeuralNetworkRuntime](../../modules/neuralnetworkruntime/document.md)

**Header file**: [neural\_network\_runtime\_type.h](../../header-files/neural-network-runtime-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| [OH\_NN\_DataType](../../header-files/neural-network-runtime-type-h/document.md#oh_nn_datatype) dataType | Data type of the specified tensor. The value must be an enum of [OH\_NN\_DataType](../../header-files/neural-network-runtime-type-h/document.md#oh_nn_datatype). |
| uint32\_t dimensionCount | Number of dimensions of the specified tensor. |
| const int32\_t \*dimensions | Dimension information (shape) of the specified tensor. |
| const [OH\_NN\_QuantParam](../oh-nn-quantparam/document.md) \*quantParam | Quantization information of the specified tensor. The value must be an enum of [OH\_NN\_QuantParam](../oh-nn-quantparam/document.md). |
| [OH\_NN\_TensorType](../../header-files/neural-network-runtime-type-h/document.md#oh_nn_tensortype) type | Type of the specified tensor. The value is related to the tensor usage. If the tensor is used as the input or output of the model, set type to [OH\_NN\_TENSOR](../../header-files/neural-network-runtime-type-h/document.md#oh_nn_tensortype). If the tensor is used as an operator parameter, select an enum value other than [OH\_NN\_TENSOR](../../header-files/neural-network-runtime-type-h/document.md#oh_nn_tensortype) from [OH\_NN\_TensorType](../../header-files/neural-network-runtime-type-h/document.md#oh_nn_tensortype). |
