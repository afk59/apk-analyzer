# neural\_network\_runtime\_type.h

#### Overview

Defines the structure and enums for NNRt.

**File to include**: <neural\_network\_runtime/neural\_network\_runtime\_type.h>

**Library**: libneural\_network\_runtime.so

**System capability**: SystemCapability.Ai.NeuralNetworkRuntime

**Since**: 9

**Related module**: [NeuralNetworkRuntime](../../modules/neuralnetworkruntime/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NN\_UInt32Array](../../structs/oh-nn-uint32array/document.md) | OH\_NN\_UInt32Array | Used to store a 32-bit unsigned integer array. |
| [OH\_NN\_QuantParam](../../structs/oh-nn-quantparam/document.md) | OH\_NN\_QuantParam | Used to define the quantization information. |
| [OH\_NN\_Tensor](../../structs/oh-nn-tensor/document.md) | OH\_NN\_Tensor | 
Used to define the tensor structure.

It is usually used to construct data nodes and operator parameters in a model diagram. When constructing a tensor, you need to specify the data type, number of dimensions, dimension information, and quantization information.

 |
| [OH\_NN\_Memory](../../structs/oh-nn-memory/document.md) | OH\_NN\_Memory | Used to define the memory structure. |
| [OH\_NNModel](../../structs/oh-nnmodel/document.md) | OH\_NNModel | Model handle. |
| [OH\_NNCompilation](../../structs/oh-nncompilation/document.md) | OH\_NNCompilation | Compiler handle. |
| [OH\_NNExecutor](../../structs/oh-nnexecutor/document.md) | OH\_NNExecutor | Executor handle. |
| [NN\_QuantParam](../../structs/nn-quantparam/document.md) | NN\_QuantParam | Quantization parameter handle. |
| [NN\_TensorDesc](../../structs/nn-tensordesc/document.md) | NN\_TensorDesc | Tensor description handle. |
| [NN\_Tensor](../../structs/nn-tensor/document.md) | NN\_Tensor | Tensor handle. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_NN\_PerformanceMode](#oh_nn_performancemode) | OH\_NN\_PerformanceMode | Performance modes of the device. |
| [OH\_NN\_Priority](#oh_nn_priority) | OH\_NN\_Priority | Priorities of a model inference task. |
| [OH\_NN\_ReturnCode](#oh_nn_returncode) | OH\_NN\_ReturnCode | Error codes for NNRt. |
| [OH\_NN\_FuseType](#oh_nn_fusetype) | OH\_NN\_FuseType | Activation function types in the fusion operator for NNRt. |
| [OH\_NN\_Format](#oh_nn_format) | OH\_NN\_Format | Tensor data formats. |
| [OH\_NN\_DeviceType](#oh_nn_devicetype) | OH\_NN\_DeviceType | Device types supported by NNRt. |
| [OH\_NN\_DataType](#oh_nn_datatype) | OH\_NN\_DataType | Data types supported by NNRt. |
| [OH\_NN\_OperationType](#oh_nn_operationtype) | OH\_NN\_OperationType | Operator types supported by NNRt. |
| [OH\_NN\_TensorType](#oh_nn_tensortype) | OH\_NN\_TensorType | 
Tensor types.

Tensors are usually used to set the input, output, and operator parameters of a model. When a tensor is used as the input or output of a model (or operator), set the tensor type to [OH\_NN\_TENSOR](#oh_nn_tensortype). When the tensor is used as an operator parameter, select an enumerated value other than [OH\_NN\_TENSOR](#oh_nn_tensortype) as the tensor type.

Assume that pad of the [OH\_NN\_OPS\_CONV2D](#oh_nn_operationtype) operator is being set. You need to set the type attribute of the [OH\_NN\_Tensor](../../structs/oh-nn-tensor/document.md) instance to [OH\_NN\_CONV2D\_PAD](#oh_nn_tensortype). The settings of other operator parameters are similar. The enumerated values are named in the format OH\_NN\_{**operator-name**}\_{**attribute-name**}.

 |

#### \[h2\]Functions

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [typedef void (\*NN\_OnRunDone)(void \*userData, OH\_NN\_ReturnCode errCode, void \*outputTensor\[\], int32\_t outputCount)](#nn_onrundone) | NN\_OnRunDone | 
Handle of the callback processing function invoked when the asynchronous inference ends.

Use the **userData** parameter to specify the asynchronous inference to query. The value of **userData** is the same as that passed to [OH\_NNExecutor\_RunAsync](../neural-network-core-h/document.md#oh_nnexecutor_runasync). Use the **errCode** parameter to obtain the return result (defined by [OH\_NN\_ReturnCode](#oh_nn_returncode) of the asynchronous inference.

 |
| [typedef void (\*NN\_OnServiceDied)(void \*userData)](#nn_onservicedied) | NN\_OnServiceDied | 

Handle of the callback processing function invoked when the device driver service terminates unexpectedly during asynchronous inference.

You need to rebuild the model if the callback is invoked.

Use the **userData** parameter to specify the asynchronous inference to query. The value of **userData** is the same as that passed to [OH\_NNExecutor\_RunAsync](../neural-network-core-h/document.md#oh_nnexecutor_runasync).

 |

#### Enum Description

#### \[h2\]OH\_NN\_PerformanceMode

enum OH\_NN\_PerformanceMode

**Description**

Defines the performance modes of the device.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_PERFORMANCE\_NONE = 0 | No performance mode preference. |
| OH\_NN\_PERFORMANCE\_LOW = 1 | Low power consumption mode. |
| OH\_NN\_PERFORMANCE\_MEDIUM = 2 | Medium performance mode. |
| OH\_NN\_PERFORMANCE\_HIGH = 3 | High performance. |
| OH\_NN\_PERFORMANCE\_EXTREME = 4 | Ultimate performance. |

#### \[h2\]OH\_NN\_Priority

enum OH\_NN\_Priority

**Description**

Defines the priorities of a model inference task.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_PRIORITY\_NONE = 0 | No priority preference. |
| OH\_NN\_PRIORITY\_LOW = 1 | Low priority. |
| OH\_NN\_PRIORITY\_MEDIUM = 2 | Medium priority. |
| OH\_NN\_PRIORITY\_HIGH = 3 | High priority. |

#### \[h2\]OH\_NN\_ReturnCode

enum OH\_NN\_ReturnCode

**Description**

Defines the error codes for NNRt.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_SUCCESS = 0 | Operation successful. |
| OH\_NN\_FAILED = 1 | Operation failed. |
| OH\_NN\_INVALID\_PARAMETER = 2 | Invalid parameter. |
| OH\_NN\_MEMORY\_ERROR = 3 | Memory-related error, for example, insufficient memory, memory data copy failure, or memory application failure. |
| OH\_NN\_OPERATION\_FORBIDDEN = 4 | Invalid operation. |
| OH\_NN\_NULL\_PTR = 5 | Null pointer. |
| OH\_NN\_INVALID\_FILE = 6 | Invalid file. |
| OH\_NN\_UNAVALIDABLE\_DEVICE = 7 | 
Hardware error, for example, HDL service crash.

**Deprecated from**: 11

**Substitute**: OH\_NN\_UNAVAILABLE\_DEVICE

 |
| OH\_NN\_INVALID\_PATH = 8 | Invalid path. |
| OH\_NN\_TIMEOUT = 9 | 

Operation timed out.

**Since**: 11

 |
| OH\_NN\_UNSUPPORTED = 10 | 

Not supported

**Since**: 11

 |
| OH\_NN\_CONNECTION\_EXCEPTION = 11 | 

Connection error.

**Since**: 11

 |
| OH\_NN\_SAVE\_CACHE\_EXCEPTION = 12 | 

Failed to save the cache.

**Since**: 11

 |
| OH\_NN\_DYNAMIC\_SHAPE = 13 | 

Dynamic shape

**Since**: 11

 |
| OH\_NN\_UNAVAILABLE\_DEVICE = 14 | 

Hardware error, for example, HDL service crash.

**Since**: 11

 |

#### \[h2\]OH\_NN\_FuseType

enum OH\_NN\_FuseType

**Description**

Defines the activation function types in the fusion operator for NNRt.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_FUSED\_NONE = 0 | Fusion activation function not specified. |
| OH\_NN\_FUSED\_RELU = 1 | Fusion relu activation function. |
| OH\_NN\_FUSED\_RELU6 = 2 | Fusion relu6 activation function. |

#### \[h2\]OH\_NN\_Format

enum OH\_NN\_Format

**Description**

Defines the tensor data formats.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_FORMAT\_NONE = 0 | The tensor does not have a specific arrangement type (such as scalar or vector). |
| OH\_NN\_FORMAT\_NCHW = 1 | The tensor arranges data in NCHW format. |
| OH\_NN\_FORMAT\_NHWC = 2 | The tensor arranges data in NHWC format. |
| OH\_NN\_FORMAT\_ND = 3 | 
The tensor arranges data in ND format.

**Since**: 11

 |

#### \[h2\]OH\_NN\_DeviceType

enum OH\_NN\_DeviceType

**Description**

Defines the device types supported by NNRt.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_OTHERS = 0 | Devices that are not CPU, GPU, or dedicated accelerator. |
| OH\_NN\_CPU = 1 | CPU. |
| OH\_NN\_GPU = 2 | GPU. |
| OH\_NN\_ACCELERATOR = 3 | Dedicated device accelerator. |

#### \[h2\]OH\_NN\_DataType

enum OH\_NN\_DataType

**Description**

Defines the data types supported by NNRt.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_UNKNOWN = 0 | Unknown type. |
| OH\_NN\_BOOL = 1 | bool type. |
| OH\_NN\_INT8 = 2 | int8 type. |
| OH\_NN\_INT16 = 3 | int16 type. |
| OH\_NN\_INT32 = 4 | int32 type. |
| OH\_NN\_INT64 = 5 | int64 type. |
| OH\_NN\_UINT8 = 6 | uint8 type. |
| OH\_NN\_UINT16 = 7 | uint16 type. |
| OH\_NN\_UINT32 = 8 | uint32 type. |
| OH\_NN\_UINT64 = 9 | uint64 type. |
| OH\_NN\_FLOAT16 = 10 | float16 type. |
| OH\_NN\_FLOAT32 = 11 | float32 type. |
| OH\_NN\_FLOAT64 = 12 | float64 type. |

#### \[h2\]OH\_NN\_OperationType

enum OH\_NN\_OperationType

**Description**

Defines the operator types supported by NNRt.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_OPS\_ADD = 1 | 
Returns the tensor of the sum of the elements corresponding to two input tensors.

Input:

**input1**: first input tensor, which is of the Boolean or number type.

**input2**: second input tensor, whose data type must be the same as that of the first tensor.

Parameters:

**activationType**: integer constant contained in **OH\_NN\_FuseType**.

The specified activation function is called before output.

Output:

**output**: sum of **input1** and **input2**. The data shape is the same as that of the input after broadcasting, and the data type is the same as that of the input with a higher precision.

 |
| OH\_NN\_OPS\_AVG\_POOL = 2 | 

Applies 2D average pooling to the input tensor, which must be in the NHWC format. The int8 quantization input is supported.

If the input contains the **padMode** parameter:

**input**: a tensor. Parameters:

**kernelSize**: average kernel size. It is an int array with a length of 2 in the format of \[kernelHeight, kernelWeight\], where the first number indicates the kernel height, and the second number indicates the kernel width.

**strides**: kernel moving stride. It is an int array with a length of 2 in the format of \[strideHeight, strideWeight\], where the first number indicates the moving stride in height, and the second number indicates the moving stride in width.

**padMode**: padding mode, which is optional. It is an int value, which can be **0** (same) or **1** (valid). The nearest neighbor value is used for padding.

**0** (same): The height and width of the output are the same as those of the input. The total padding quantity is calculated horizontally and vertically and evenly distributed to the top, bottom, left, and right if possible. Otherwise, the last additional padding will be completed from the bottom and right.

**1** (valid): The possible maximum height and width of the output will be returned in case of no padding. The excessive pixels will be discarded.

**roundMode**: boundary processing mode, which is an optional value of the int type. When the pooling core cannot completely cover the input feature map, the output feature map is rounded down. The value **0** indicates rounding down, and the value **1** indicates rounding up.

**global**: bool value indicating whether to perform the average pooling operation on the entire input tensor.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output. If the input contains the **padList** parameter:

**input**: a tensor.

Parameters:

**kernelSize**: average kernel size. It is an int array with a length of 2 in the format of \[kernelHeight, kernelWeight\], where the first number indicates the kernel height, and the second number indicates the kernel width.

**strides**: kernel moving stride. It is an int array with a length of 2 in the format of \[strideHeight, strideWeight\], where the first number indicates the moving stride in height, and the second number indicates the moving stride in width.

**padList**: padding around **input**. It is an int array with a length of 4 in the format of \[top, bottom, left, right\], and the nearest neighbor values are used for padding.

**roundMode**: boundary processing mode, which is an optional value of the int type. When the pooling core cannot completely cover the input feature map, the output feature map is rounded down. The value **0** indicates rounding down, and the value **1** indicates rounding up.

**global**: bool value indicating whether to perform the average pooling operation on the entire input tensor.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: average pooling result of the input.

 |
| OH\_NN\_OPS\_BATCH\_NORM = 3 | 

The input tensor is normalized in batches, and a transformation is applied to keep the average output close to 0 and the output standard deviation close to 1.

Input:

**input**: n-dimensional tensor in the shape of \[N, ..., C\]. The nth dimension is the number of channels.

**scale**: 1D tensor of the scaling factor used to scale the first normalized tensor.

**offset**: 1D tensor used to move to the first normalized tensor.

**mean**: 1D tensor of the overall mean value. It is used only for inference. In case of training, this parameter must be left empty.

**variance**: 1D tensor used for the overall variance. It is used only for inference. In case of training, this parameter must be left empty.

Parameters:

**epsilon**: fixed small additional value.

Output:

**output**: n-dimensional output tensor whose shape and data type are the same as those of the input.

 |
| OH\_NN\_OPS\_BATCH\_TO\_SPACE\_ND = 4 | 

Divides batch dimension of a 4D tensor into small blocks by **blockSize** and interleaves them into the spatial dimension.

Input:

**input**: input tensor. The dimension will be divided into small blocks, and these blocks will be interleaved into the spatial dimension. Parameters:

**blockSize**: size of blocks to be interleaved into the spatial dimension. The value is an array with a length of 2 in the format of \[heightBlock, weightBlock\].

**crops**: elements truncated from the spatial dimension of the output. The value is a 2D array with the shape of (2, 2) in the format of \[\[crop0Start, crop0End\], \[crop1Start, crop1End\]\].

Output:

**output**: output tensor, where the input shape is (n, h, w, c) and the output shape is (n', h', w', c'), specifically:

n' = n / (blockSize\[0\] \* blockSize\[1\])

h' = h \* blockSize\[0\] - crops\[0\]\[0\] - crops\[0\]\[1\]

w' = w \* blockSize\[1\] - crops\[1\]\[0\] - crops\[1\]\[1\]

c'= c

 |
| OH\_NN\_OPS\_BIAS\_ADD = 5 | 

Offsets the data in each dimension of the input tensor.

Input:

**input**: input tensor, which can have two to five dimensions.

**bias**: offset of the number of input dimensions.

Output:

**output**: sum of the input tensor and the bias in each dimension.

 |
| OH\_NN\_OPS\_CAST = 6 | 

Converts the data type in the input tensor.

Input:

**input**: input tensor.

**type**: converted data type.

Output:

**output**: converted tensor.

 |
| OH\_NN\_OPS\_CONCAT = 7 | 

Connects tensors in a specified dimension.

Input:

**input**: n input tensors.

Parameters:

**axis**: dimension for connecting tensors.

Output:

**output**: result of connecting n tensors along the axis.

 |
| OH\_NN\_OPS\_CONV2D = 8 | 

Sets a 2D convolutional layer. If the input contains the **padMode** parameter:

**input**: input tensor.

**weight**: convolution weight in the format of \[outChannel, kernelHeight, kernelWidth, inChannel/group\]. The value of **inChannel** must be exactly divided by the value of **group**.

**bias**: bias of the convolution. It is an array with a length of \[outChannel\]. In quantization scenarios, the **bias** parameter does not require quantization parameters. The quantization version requires data input of the **OH\_NN\_INT32** type. The actual quantization parameters are determined by **input** and **weight**.

Parameters:

**stride**: moving stride of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[strideHeight, strideWidth\].

**dilation**: dilation size of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[dilationHeight, dilationWidth\]. The value must be greater than or equal to **1** and cannot exceed the height and width of **input**.

**padMode**: padding mode of **input**. The value is of the int type and can be **0** (same) or **1** (valid).

**0** (same): The height and width of the output are the same as those of the input. The total padding quantity is calculated horizontally and vertically and evenly distributed to the top, bottom, left, and right if possible. Otherwise, the last additional padding will be completed from the bottom and right.

**1** (valid): The possible maximum height and width of the output will be returned in case of no padding. The excessive pixels will be discarded.

**group**: number of groups in which the input is divided by **inChannel**. The value is of the int type. If **group** is **1**, it is a conventional convolution. If **group** is greater than **1** and less than or equal to **inChannel**, it is a group convolution.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output. If the input contains the **padList** parameter:

**input**: input tensor.

**weight**: convolution weight in the format of \[outChannel, kernelHeight, kernelWidth, inChannel/group\]. The value of **inChannel** must be exactly divided by the value of **group**.

**bias**: bias of the convolution. It is an array with a length of \[outChannel\]. In quantization scenarios, the **bias** parameter does not require quantization parameters. The quantization version requires data input of the **OH\_NN\_INT32** type. The actual quantization parameters are determined by **input** and **weight**.

Parameters:

**stride**: moving stride of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[strideHeight, strideWidth\].

**dilation**: dilation size of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[dilationHeight, dilationWidth\]. The value must be greater than or equal to **1** and cannot exceed the height and width of **input**.

**padList**: padding around **input**. It is an int array with a length of 4 in the format of \[top, bottom, left, right\].

**group**: number of groups in which the input is divided by **inChannel**. The value is of the int type. If **group** is **1**, it is a conventional convolution. If **group** is equal to **inChannel**, it is a 2D depthwise convolution. In this case, group==inChannel==outChannel. If **group** is greater than **1** and less than **inChannel**, it is a group convolution. In this case, outChannel==group.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: convolution computing result.

 |
| OH\_NN\_OPS\_CONV2D\_TRANSPOSE = 9 | 

Sets 2D convolution transposition. If the input contains the **padMode** parameter:

**input**: input tensor.

**weight**: convolution weight in the format of \[outChannel, kernelHeight, kernelWidth, inChannel/group\]. The value of **inChannel** must be exactly divided by the value of **group**.

**bias**: bias of the convolution. It is an array with a length of \[outChannel\]. In quantization scenarios, the **bias** parameter does not require quantization parameters. The quantization version requires data input of the **OH\_NN\_INT32** type. The actual quantization parameters are determined by **input** and **weight**.

**stride**: moving stride of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[strideHeight, strideWidth\].

Parameters:

**dilation**: dilation size of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[dilationHeight, dilationWidth\]. The value must be greater than or equal to **1** and cannot exceed the height and width of **input**.

**padMode**: padding mode of **input**. The value is of the int type and can be **0** (same) or **1** (valid).

**0** (same): The height and width of the output are the same as those of the input. The total padding quantity is calculated horizontally and vertically and evenly distributed to the top, bottom, left, and right if possible. Otherwise, the last additional padding will be completed from the bottom and right.

**1** (valid): The possible maximum height and width of the output will be returned in case of no padding. The excessive pixels will be discarded.

**group**: number of groups in which the input is divided by **inChannel**. The value is of the int type. If **group** is **1**, it is a conventional convolution. If **group** is greater than **1** and less than or equal to **inChannel**, it is a group convolution.

**outputPads**: padding along the height and width of the output tensor. The value is an int number, a tuple, or a list of two integers. It can be a single integer to specify the same value for all spatial dimensions. The amount of output padding along a dimension must be less than the stride along this dimension.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output. If the input contains the **padList** parameter:

**input**: input tensor.

**weight**: convolution weight in the format of \[outChannel, kernelHeight, kernelWidth, inChannel/group\]. The value of **inChannel** must be exactly divided by the value of **group**.

**bias**: bias of the convolution. It is an array with a length of \[outChannel\]. In quantization scenarios, the **bias** parameter does not require quantization parameters. The quantization version requires data input of the **OH\_NN\_INT32** type. The actual quantization parameters are determined by **input** and **weight**.

Parameters:

**stride**: moving stride of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[strideHeight, strideWidth\].

**dilation**: dilation size of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[dilationHeight, dilationWidth\]. The value must be greater than or equal to **1** and cannot exceed the height and width of **input**.

**padList**: padding around **input**. It is an int array with a length of 4 in the format of \[top, bottom, left, right\].

**group**: number of groups in which the input is divided by **inChannel**. The value is of the int type. If **group** is **1**, it is a conventional convolution. If **group** is greater than **1** and less than or equal to **inChannel**, it is a group convolution.

**outputPads**: padding along the height and width of the output tensor. The value is an int number, a tuple, or a list of two integers. It can be a single integer to specify the same value for all spatial dimensions. The amount of output padding along a dimension must be less than the stride along this dimension.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: computing result after convolution and transposition.

 |
| OH\_NN\_OPS\_DEPTHWISE\_CONV2D\_NATIVE = 10 | 

Sets 2D depthwise separable convolution. If the input contains the **padMode** parameter:

**input**: input tensor.

**weight**: convolution weight in the format of \[outChannel, kernelHeight, kernelWidth, 1\]. **outChannel** is equal to **channelMultiplier** multiplied by **inChannel**.

**bias**: bias of the convolution. It is an array with a length of \[outChannel\]. In quantization scenarios, the **bias** parameter does not require quantization parameters. The quantization version requires data input of the **OH\_NN\_INT32** type. The actual quantization parameters are determined by **input** and **weight**.

Parameters:

**stride**: moving stride of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[strideHeight, strideWidth\].

**dilation**: dilation size of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[dilationHeight, dilationWidth\]. The value must be greater than or equal to **1** and cannot exceed the height and width of **input**.

**padMode**: padding mode of **input**. The value is of the int type and can be **0** (same) or **1** (valid).

**0** (same): The height and width of the output are the same as those of the input. The total padding quantity is calculated horizontally and vertically and evenly distributed to the top, bottom, left, and right if possible. Otherwise, the last additional padding will be completed from the bottom and right.

**1** (valid): The possible maximum height and width of the output will be returned in case of no padding. The excessive pixels will be discarded.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output. If the input contains the **padList** parameter:

**input**: input tensor.

**weight**: convolution weight in the format of \[outChannel, kernelHeight, kernelWidth, 1\]. **outChannel** is equal to **channelMultiplier** multiplied by **inChannel**.

**bias**: bias of the convolution. It is an array with a length of \[outChannel\]. In quantization scenarios, the **bias** parameter does not require quantization parameters. The quantization version requires data input of the **OH\_NN\_INT32** type. The actual quantization parameters are determined by **input** and **weight**.

Parameters:

**stride**: moving stride of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[strideHeight, strideWidth\].

**dilation**: dilation size of the convolution kernel in height and weight. It is an int array with a length of 2 in the format of \[dilationHeight, dilationWidth\]. The value must be greater than or equal to **1** and cannot exceed the height and width of **input**.

**padList**: padding around **input**. It is an int array with a length of 4 in the format of \[top, bottom, left, right\].

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: convolution computing result.

 |
| OH\_NN\_OPS\_DIV = 11 | 

Divides two input scalars or tensors.

Input:

**input1**: first input, which is a number, a Boolean value, or a tensor whose data type is number or Boolean value. **input2**: second input, which must meet the following requirements: If the first input is a tensor, the second input can be a real number, a Boolean value, or a tensor whose data type is real number or Boolean value. If the first input is a real number or Boolean value, the second input must be a tensor whose data type is real number or Boolean value.

Parameters:

**activationType**: integer constant contained in **OH\_NN\_FuseType**.

The specified activation function is called before output.

Output:

**output**: result of dividing **input1** by **input2**.

 |
| OH\_NN\_OPS\_ELTWISE = 12 | 

Sets parameters to perform product (dot product), sum (addition and subtraction), or max (larger value) on the input.

Input:

**input1**: first input tensor.

**input2**: second input tensor. Parameters:

**mode**: operation mode. The value is an enumerated value.

Output:

**output**: computing result, which has the same data type and shape of **output** and **input1**.

 |
| OH\_NN\_OPS\_EXPAND\_DIMS = 13 | 

Adds an additional dimension to a tensor in the given dimension.

Input:

**input**: input tensor.

**axis**: index of the dimension to be added. The value is of the int32\_t type and must be a constant in the range \[-dim-1, dim\].

Output:

**output**: tensor after dimension expansion.

 |
| OH\_NN\_OPS\_FILL = 14 | 

Creates a tensor of the specified dimensions and fills it with a scalar.

Input:

**value**: scalar used to fill the tensor.

**shape**: dimensions of the tensor to be created.

Output:

**output**: generated tensor, which has the same data type as **value**. The tensor shape is specified by the **shape** parameter.

 |
| OH\_NN\_OPS\_FULL\_CONNECTION = 15 | 

Sets a full connection. The entire input is used as the feature map for feature extraction.

Input:

**input**: full-connection input tensor.

**weight**: weight tensor for a full connection.

**bias**: full-connection bias. In quantization scenarios, quantization parameters are not required for **bias**. You only need to input data of the **OH\_NN\_INT32** type. The actual quantization parameters are determined by **input** and **weight**.

Parameters:

**hasBias**: Boolean value indicating whether to use the bias offset.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: computed tensor.

If the input contains the **axis** or **useAxis** parameter:

**input**: full-connection input tensor.

**weight**: weight tensor for a full connection.

**bias**: full-connection bias. In quantization scenarios, quantization parameters are not required for **bias**. You only need to input data of the **OH\_NN\_INT32** type. The actual quantization parameters are determined by **input** and **weight**.

Parameters:

**axis**: axis in which the full connection is applied. The specified axis and its following axes are converted into a 1D tensor for applying the full connection. The default value is **0**.

**useAxis**: Boolean value indicating whether to use the **axis** parameter. If **axis** is set, **useAxis** is automatically set to **true**. If **useAxis** is set to **true** and **axis** is not specified, the default axis is used to expand full connections. You cannot set **useAxis** to **false** and specify **axis** at the same time. The default value is **false**.

**hasBias**: Boolean value indicating whether to use the bias offset.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: computed tensor.

 |
| OH\_NN\_OPS\_GATHER = 16 | 

Returns the slice of the input tensor based on the specified index and axis.

Input:

**input**: tensor to be sliced.

**inputIndices**: indices of the specified input on the axis. The value is an array of the int type and must be in the range \[0,input.shape\[axis\]).

**axis**: axis on which **input** is sliced. The value is an int32\_t array with a length of 1.

Output:

**output**: sliced tensor.

 |
| OH\_NN\_OPS\_HSWISH = 17 | 

Calculates the activation value of the input **Hardswish**.

Input:

An n-dimensional input tensor.

Output:

**output**: n-dimensional **Hardswish** activation value. The data type is the same as that of **shape** and **input**.

 |
| OH\_NN\_OPS\_LESS\_EQUAL = 18 | 

Calculates the result of input1\[i\]<=input2\[i\] for each pair of elements, where **i** is the index of each element in the input tensor. Input:

**input1**: a real number, Boolean value, or tensor whose data type is real number or **OH\_NN\_BOOL**. **input2**: a real number or a Boolean value if **input1** is a tensor, or a tensor whose data type is real number or **OH\_NN\_BOOL** if **input1** is not a tensor. Output:

**output**: a tensor of the **OH\_NN\_BOOL** type. When a quantization model is used, the quantization parameters of the output cannot be omitted. However, values of the quantization parameters do not affect the result.

 |
| OH\_NN\_OPS\_MATMUL = 19 | 

Calculates the inner product of **input1** and **input2**.

Input:

**input1**: n-dimensional input tensor.

**input2**: n-dimensional input tensor.

Parameters:

**TransposeX**: Boolean value indicating whether to transpose **input1**.

**TransposeY**: Boolean value indicating whether to transpose **input2**.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: inner product obtained after calculation. In case of **type!=OH\_NN\_UNKNOWN**, the output data type is determined by **type**. In case of **type==OH\_NN\_UNKNOWN**, the output data type depends on the data type converted during computing of **inputX** and **inputY**.

 |
| OH\_NN\_OPS\_MAXIMUM = 20 | 

Calculates the maximum of **input1** and **input2** element-wise. The inputs of **input1** and **input2** comply with the implicit type conversion rules to make the data types consistent.

The inputs must be two tensors or one tensor and one scalar. If the input contains two tensors, their data types must not be both **OH\_NN\_BOOL**.

Their shapes can be broadcast to the same size. If the input contains one tensor and one scalar, the scalar must be a constant.

Input:

**input1**: n-dimensional input tensor whose data type is real number or **OH\_NN\_BOOL**.

**input2**: n-dimensional input tensor whose data type is real number or **OH\_NN\_BOOL**.

Output:

**output**: n-dimensional output tensor. The **shape** and data type of **output** are the same as those of the two inputs with higher precision or bits.

 |
| OH\_NN\_OPS\_MAX\_POOL = 21 | 

Applies 2D maximum pooling to the input tensor. If the input contains the **padMode** parameter:

**input**: a tensor.

Parameters:

**kernelSize**: maximum kernel size. It is an int array with a length of 2 in the format of \[kernelHeight, kernelWeight\], where the first number indicates the kernel height, and the second number indicates the kernel width.

**strides**: kernel moving stride. It is an int array with a length of 2 in the format of \[strideHeight, strideWeight\], where the first number indicates the moving stride in height, and the second number indicates the moving stride in width.

**padMode**: padding mode, which is optional. It is an int value, which can be **0** (same) or **1** (valid). The nearest neighbor value is used for padding.

**0** (same): The height and width of the output are the same as those of the input. The total padding quantity is calculated horizontally and vertically and evenly distributed to the top, bottom, left, and right if possible. Otherwise, the last additional padding will be completed from the bottom and right.

**1** (valid): The possible maximum height and width of the output will be returned in case of no padding. The excessive pixels will be discarded.

**roundMode**: boundary processing mode, which is an optional value of the int type. When the pooling core cannot completely cover the input feature map, the output feature map is rounded down. The value **0** indicates rounding down, and the value **1** indicates rounding up.

**global**: bool value indicating whether to perform the average pooling operation on the entire input tensor.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output. If the input contains the **padList** parameter:

**input**: a tensor.

Parameters:

**kernelSize**: maximum kernel size. It is an int array with a length of 2 in the format of \[kernelHeight, kernelWeight\], where the first number indicates the kernel height, and the second number indicates the kernel width.

**strides**: kernel moving stride. It is an int array with a length of 2 in the format of \[strideHeight, strideWeight\], where the first number indicates the moving stride in height, and the second number indicates the moving stride in width.

**padList**: padding around **input**. It is an int array with a length of 4 in the format of \[top, bottom, left, right\], and the nearest neighbor values are used for padding.

**roundMode**: boundary processing mode, which is an optional value of the int type. When the pooling core cannot completely cover the input feature map, the output feature map is rounded down. The value **0** indicates rounding down, and the value **1** indicates rounding up.

**global**: bool value indicating whether to perform the average pooling operation on the entire input tensor.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: tensor obtained after maximum pooling is applied to the input.

 |
| OH\_NN\_OPS\_MUL = 22 | 

Multiplies elements in the same locations of **input1** and **input2** to obtain the output. If the shapes of **input1** and **input2** are different, **input1** and **input2** can be extended to the same shape through broadcast for multiplication.

Input:

**input1**: n-dimensional tensor.

**input2**: n-dimensional tensor.

Parameters:

**activationType**: integer constant contained in **OH\_NN\_FuseType**.

The specified activation function is called before output.

Output:

**output**: product of each element of **input1** and **input2**.

 |
| OH\_NN\_OPS\_ONE\_HOT = 23 | 

Generates a one-hot tensor based on the locations specified by **indices**. The locations specified by **indices** are determined by **onValue**, and other locations are determined by **offValue**.

Input:

**indices**: n-dimensional tensor. Each element in **indices** determines the location of **onValue** in each one-hot vector.

**depth**, an integer scalar that determines the depth of the one-hot vector. The value of **depth** must be greater than **0**.

**onValue**: a scalar that specifies a valid value in the one-hot vector.

**offValue**: a scalar that specifies the values of other locations in the one-hot vector except the valid value.

Parameters:

**axis**: integer scalar that specifies the dimension for inserting the one-hot. Assume that the shape of **indices** is \[N, C\], and the value of **depth** is D. When **axis** is **0**, the shape of the output is \[D, N, C\]. When **axis** is **\-1**, the shape of the output is \[N, C, D\]. When **axis** is **1**, the shape of the output is \[N, D, C\].

Output:

**output**: (n+1)-dimensional tensor if **indices** is an n-dimensional tensor. The output shape is determined by **indices** and **axis**.

 |
| OH\_NN\_OPS\_PAD = 24 | 

Pads **inputX** in the specified dimensions.

Input:

**inputX**: n-dimensional tensor in \[BatchSize, ...\] format.

**paddings**: 2D tensor that specifies the length to pad in each dimension. The shape is \[n, 2\]. For example, **paddings\[i\]\[0\]** indicates the number of paddings to be added preceding **inputX** in the nth dimension, and **paddings\[i\]\[1\]** indicates the number of paddings to be added following **inputX** in the nth dimension.

Parameters:

**constantValues**: value to be added to the pad operation. The value is a constant with the same data type as **inputX**.

**paddingMode**: padding mode. The value is of the **OH\_NN\_INT32** type. The value **0** indicates that constant 0 is used for padding. The value **1** indicates mirror padding without the symmetry axis. The value **2** indicates mirror padding with the symmetry axis. The value **3** indicates the reserved padding mode.

Output:

**output**: n-dimensional tensor after padding, with the same dimensions and data type as **inputX**. The shape is determined by **inputX** and **paddings**; that is, output.shape\[i\] = input.shape\[i\] + paddings\[i\]\[0\]+paddings\[i\]\[1\].

 |
| OH\_NN\_OPS\_POW = 25 | 

Calculates the **y** power of each element in **input**. The input must contain two tensors or one tensor and one scalar. If the input contains two tensors, their data types must not be both **OH\_NN\_BOOL**, and their shapes must be the same. If the input contains one tensor and one scalar, the scalar must be a constant.

Input:

**input**: a real number, Boolean value, or tensor whose data type is real number or **OH\_NN\_BOOL**.

**y**: a real number, Boolean value, or tensor whose data type is real number or **OH\_NN\_BOOL**.

Parameters:

**scale**: an **OH\_NN\_FLOAT32** scalar indicating the scaling and fusion factor.

**shift**, an **OH\_NN\_FLOAT32** scalar indicating the offset of scaling blending.

Output:

**output**: tensor, whose shape is determined by the shape of **input** and **y** after broadcasting.

 |
| OH\_NN\_OPS\_SCALE = 26 | 

Scales a tensor.

Input:

**input**: n-dimensional tensor.

**scale**: scaling tensor.

**bias**: bias tensor.

Parameters:

**axis**: dimensions to be scaled.

**activationType**: integer constant contained in **OH\_NN\_FuseType**. The specified activation function is called before output.

Output:

**output**: scaled n-dimensional tensor, whose data type is the same as that of **input** and shape is determined by **axis**.

 |
| OH\_NN\_OPS\_SHAPE = 27 | 

Calculates the shape of the input tensor.

Input:

**input**: n-dimensional tensor.

Output:

**output**: integer array representing the dimensions of the input tensor.

 |
| OH\_NN\_OPS\_SIGMOID = 28 | 

Applies the **sigmoid** operation to the input tensor.

Input:

**input**: n-dimensional tensor.

Output:

**output**: result of the **sigmoid** operation. It is an n-dimensional tensor with the same data type and shape as **input**.

 |
| OH\_NN\_OPS\_SLICE = 29 | 

Slices a tensor of the specified size from the input tensor in each dimension.

Input:

**input**: n-dimensional input tensor.

**begin**: start of the slice, which is an array of integers greater than or equal to 0.

**size**: slice length, which is an array of integers greater than or equal to **1**. Assume that a dimension is **i** and 1<=size\[i\]<=input.shape\[i\]-begin\[i\].

Parameters:

**axes**: axis of a slice.

Output:

**output**: n-dimensional tensor obtained by slicing. The **TensorType**, shape, and size of the output are the same as those of the input.

 |
| OH\_NN\_OPS\_SOFTMAX = 30 | 

Applies the **softmax** operation to the input tensor.

Input:

**input**: n-dimensional input tensor.

Parameters:

**axis**: dimension in which the **softmax** operation is performed. The value is of the int64 type. It is an integer in the range \[-n, n).

Output:

**output**: result of the **softmax** operation. It is an n-dimensional tensor with the same data type and shape as **input**.

 |
| OH\_NN\_OPS\_SPACE\_TO\_BATCH\_ND = 31 | 

Divides a 4D tensor into small blocks and combines these blocks in the original batch. The number of blocks is **blockShape\[0\]** multiplied by **blockShape\[1\]**.

Input:

**input**: 4D tensor.

Parameters:

**blockShape**: a pair of integers. Each of them is greater than or equal to **1**.

**paddings**: a pair of arrays. Each of them consists of two integers. The four integers that form **paddings** must be greater than or equal to **0**. **paddings\[0\]\[0\]** and **paddings\[0\]\[1\]** specify the number of paddings in the third dimension, and **paddings\[1\]\[0\]** and **paddings\[1\]\[1\]** specify the number of paddings in the fourth dimension.

Output:

**output**: 4D tensor with the same data type as **input**. The shape is determined by **input**, **blockShape**, and **paddings**. Assume that the input shape is \[n,c,h,w\], then:

output.shape\[0\] = n \* blockShape\[0\] \* blockShape\[1\]

output.shape\[1\] = c

output.shape\[2\] = (h + paddings\[0\]\[0\] + paddings\[0\]\[1\]) / blockShape\[0\]

output.shape\[3\] = (w + paddings\[1\]\[0\] + paddings\[1\]\[1\]) / blockShape\[1\]

(h + paddings\[0\]\[0\] + paddings\[0\]\[1\]) and (w + paddings\[1\]\[0\] + paddings\[1\]\[1\]) must be exactly divisible by blockShape\[0\] and blockShape\[1\] respectively.

 |
| OH\_NN\_OPS\_SPLIT = 32 | 

Splits the input into multiple tensors along the axis dimension. The number of tensors is specified by **outputNum**.

Input:

**input**: n-dimensional tensor. Parameters:

**outputNum**: number of output tensors. The data type is int.

**sizeSplits**: size of each tensor split from the input. The value is a 1D tensor of the **int** type. If **sizeSplits** is empty, the input will be evenly split into tensors of the same size. In this case, **input.shape\[axis\]** can be exactly divisible by **outputNum**. If **sizeSplits** is not empty, the sum of all its elements must be equal to **input.shape\[axis\]**.

**axis**: splitting dimension of the int type.

Output:

**outputs**: an array of n-dimensional tensors, with the same data type and dimensions. The data type of each tensor is the same as that of **input**.

 |
| OH\_NN\_OPS\_SQRT = 33 | 

Calculates the square root of a tensor.

Input:

**input**: n-dimensional tensor.

Output:

**output**: square root of the input. It is an n-dimensional tensor with the same data type and shape as **input**.

 |
| OH\_NN\_OPS\_SQUARED\_DIFFERENCE = 34 | 

Calculates the square of the difference between two tensors. The **SquaredDifference** operator supports tensor and tensor subtraction.

If two tensors have different **TensorTypes**, the operator converts the low-precision tensor to a high-precision one.

If two tensors have different shapes, the two tensors can be extended to tensors with the same shape through broadcast.

Input:

**input1**: subtractor, which is a tensor of the OH\_NN\_FLOAT16, OH\_NN\_FLOAT32, OH\_NN\_INT32, or OH\_NN\_BOOL type.

**input2**: subtractor, which is a tensor of the OH\_NN\_FLOAT16, OH\_NN\_FLOAT32, OH\_NN\_INT32, or OH\_NN\_BOOL type.

Output:

**output**: square of the difference between two inputs. The output shape is determined by **input1** and **input2**. If they have the same shape, the output tensor has the same shape as them. If they have different shapes, perform the broadcast operation on **input1** and **input2** and perform subtraction. **TensorType** of the output is the same as that of the input tensor with higher precision.

 |
| OH\_NN\_OPS\_SQUEEZE = 35 | 

Removes the dimension with a length of 1 from the specified axis. The int8 quantization input is supported. Assume that the input shape is \[2, 1, 1, 2, 2\] and axis is \[0,1\], the output shape is \[2, 1, 2, 2\], which means the dimension with a length of 0 between dimension 0 and dimension 1 is removed.

Input:

**input**: n-dimensional tensor.

Parameters:

**axis**: dimension to be removed. The value is of int64\_t type and can be an integer in the range \[-n, n) or an array.

Output:

**output**: output tensor.

 |
| OH\_NN\_OPS\_STACK = 36 | 

Stacks multiple tensors along the specified axis. If each tensor has n dimensions before stacking, the output tensor will have n+1 dimensions.

Input:

**input**: input for stacking, which can contain multiple n-dimensional tensors. Each of them must have the same shape and type.

Parameters:

**axis**: dimension for tensor stacking, which is an integer. The value range is \[-(n+1),(n+1)), which means a negative number is allowed.

Output:

**output**: stacking result of the input along the axis dimension. The value is an n+1-dimensional tensor and has the same **TensorType** as the input.

 |
| OH\_NN\_OPS\_STRIDED\_SLICE = 37 | 

Slices a tensor with the specified stride.

Input:

**input**: n-dimensional input tensor.

**begin**: start of slicing, which is a 1D tensor. The length of **begin** is n. **begin\[i\]** specifies the start of slicing in the ith dimension.

**end**: end of slicing, which is a 1D tensor. The length of **end** is n. **end\[i\]** specifies the end of slicing in the ith dimension.

**strides**: slicing stride, which is a 1D tensor. The length of **strides** is n. strides\[i\] specifies the stride at which the tensor is sliced in the ith dimension.

Parameters:

**beginMask**: an integer used to mask **begin**. **beginMask** is represented in binary code. In case of binary(beginMask)\[i\]==1, for the <i>ith dimension, elements are sliced from the first element at **strides\[i\]** until the end\[i\]-1 element.

**endMask**: an integer used to mask **end**. **endMask** is represented in binary code. In case of binary(endMask)\[i\]==1, elements are sliced from the element at the **begin\[i\]** position in the <i>ith dimension until the tensor boundary at **strides\[i\]**.

**ellipsisMask**: integer used to mask **begin** and **end**. **ellipsisMask** is represented in binary code. In case of binary(ellipsisMask)\[i\]==1, elements are sliced from the first element at **strides\[i\]** in the <i>ith dimension until the tensor boundary. Only one bit of **binary(ellipsisMask)** can be a non-zero value.

**newAxisMask**: new dimension, which is an integer. **newAxisMask** is represented in binary code. In case of binary(newAxisMask)\[i\]==1, a new dimension with a length of 1 is inserted into the ith dimension.

**shrinkAxisMask**: shrinking dimension, which is an integer. \* **shrinkAxisMask** is represented in binary code. In the case of binary(shrinkAxisMask)\[i\]==1, all elements in the <i>ith dimension will be discarded, and the length of the <i>ith dimension is shrunk to **1**.

Output:

**output**: a tensor, with the same data type as **input**. The number of dimensions of the output tensor is rank(input\[0\])+1.

 |
| OH\_NN\_OPS\_SUB = 38 | 

Calculates the difference between two tensors.

Input:

**input1**: minuend, which is a tensor.

**input2**: subtrahend, which is a tensor.

Parameters:

**activationType**: integer constant contained in **OH\_NN\_FuseType**.

The specified activation function is called before output.

Output:

**output**: difference between the two tensors. The shape of the output is determined by input1 and input2. When the shapes of input1 and input2 are the same, the shape of the output is the same as that of input1 and input2. If the shapes of input1 and input2 are different, the output is obtained after the broadcast operation is performed on input1 or input2. **TensorType** of the output is the same as that of the input tensor with higher precision.

 |
| OH\_NN\_OPS\_TANH = 39 | 

Computes hyperbolic tangent of the input tensor.

Input:

**input**: n-dimensional tensor.

Output:

**output**: hyperbolic tangent of the input. The **TensorType** and tensor shape are the same as those of the input.

 |
| OH\_NN\_OPS\_TILE = 40 | 

Copies a tensor for the specified number of times.

Input:

**input**: n-dimensional tensor.

**multiples**: number of times that the input tensor is copied in each dimension. The value is a 1D tensor. The length m is not less than the number of dimensions, that is, n.

Parameters:

**dims**: 1D tensor, which specifies the index of the dimension to be copied.

Output:

**output**: an m-dimensional tensor whose **TensorType** is the same as **input**. If **input** and **multiples** have the same length, **input** and **output** have the same number of dimensions. If the length of **multiples** is greater than <i>n, 1 is used to fill the input dimension, and then the input is copied in each dimension the specified times to obtain the <i>m-dimensional tensor.

 |
| OH\_NN\_OPS\_TRANSPOSE = 41 | 

Transposes data of **input** based on **permutation**.

Input:

**input**: n-dimensional tensor to be transposed.

**permutation**: 1D tensor whose length is the same as the number of dimensions of **input**.

Output:

**output**: n-dimensional tensor. **TensorType** of **output** is the same as that of **input**, and the output shape is determined by the shape and **permutation** of **input**.

 |
| OH\_NN\_OPS\_REDUCE\_MEAN = 42 | 

Calculates the average value in the specified dimension. If **keepDims** is set to **false**, the number of dimensions is reduced for the input; if **keepDims** is set to **true**, the number of dimensions is retained.

Input:

**input**: n-dimensional input tensor, where n is less than 8.

**axis**: dimension used to calculate the average value. The value is a 1D tensor. The value range of each element in **axis** is \[–n, n).

Parameters:

**keepDims**: whether to retain the dimension. The value is a Boolean value.

**reduceToEnd**: a Boolean value indicating whether to perform the reduce operation until the last axis.

**coeff**: an **OH\_NN\_FLOAT32** scalar indicating the output scaling factor.

Output:

**output**: m-dimensional output tensor whose data type is the same as that of the input. If **keepDims** is **false**, m < n. If **keepDims** is **true**, m==n.

 |
| OH\_NN\_OPS\_RESIZE\_BILINEAR = 43 | 

The Bilinear method is used to deform the input based on the given parameters.

Input:

**input**: 4D input tensor. Each element in the input cannot be less than 0. The input layout must be \[batchSize, height, width, channels\].

Parameters:

**newHeight**: resized height of the 4D tensor.

**newWidth**: resized width of the 4D tensor.

**preserveAspectRatio**: whether to maintain the height/width ratio of **input** after resizing.

**coordinateTransformMode**: an int32 integer indicating the coordinate transformation method used by the Resize operation. The value 0 indicates **ASYMMETRIC**. The value **1** indicates **ALIGN\_CORNERS**. The value **2** indicates **HALF\_PIXEL**.

**excludeOutside**: an int64 floating point number. When its value is **1**, the sampling weight of the part that exceeds the boundary of **input** is set to **0**, and other weights are normalized.

Output:

**output**: n-dimensional tensor, with the same shape and data type as **input**.

 |
| OH\_NN\_OPS\_RSQRT = 44 | 

Calculates the reciprocal of the square root of an input tensor.

Input:

**input**: n-dimensional tensor, where n is less than 8. Each element of the tensor cannot be less than **0**.

Output:

**output**: n-dimensional tensor, with the same shape and data type as **input**.

 |
| OH\_NN\_OPS\_RESHAPE = 45 | 

Reshapes an input tensor.

Input:

**input**: n-dimensional input tensor.

**inputShape**: shape of the output tensor. The value is a 1D constant tensor.

Output:

**output**: tensor whose data type is the same as that of **input** and shape is determined by **InputShape**.

 |
| OH\_NN\_OPS\_PRELU = 46 | 

Calculates the PReLU activation value of **input** and **weight**.

Input:

**input**: n-dimensional tensor. If n is greater than or equal to **2**, **inputX** must be \[BatchSize, ..., Channels\]. The second dimension is the number of channels.

**weight**: 1D tensor. The length of **weight** must be **1** or equal to the number of channels. If the length of **weight** is **1**, all channels of **input** share the same weight. If the length of **weight** is equal to the number of channels, each channel exclusively has a weight. If n is less than **2** for **input**, the **weight** length must be **1**.

Output:

**output**: PReLU activation value of **input**, with the same shape and data type as **input**.

 |
| OH\_NN\_OPS\_RELU = 47 | 

Calculates the Relu activation value of **input**.

Input:

**input**: n-dimensional input tensor.

Output:

**output**: n-dimensional Relu tensor, with the same data type and shape as the input tensor.

 |
| OH\_NN\_OPS\_RELU6 = 48 | 

Calculates the Relu6 activation value of the input, that is, calculate min(max(x, 0), 6) for each element x in the input.

Input:

**input**: n-dimensional input tensor.

Output:

**output**: n-dimensional Relu6 tensor, with the same data type and shape as the input tensor.

 |
| OH\_NN\_OPS\_LAYER\_NORM = 49 | 

Applies layer normalization for a tensor from the specified axis.

Input:

**input**: n-dimensional input tensor.

**gamma**: m-dimensional tensor. The dimensions of **gamma** must be the same as the shape of the part of the input tensor to normalize.

**beta**: m-dimensional tensor with the same shape as **gamma**. Parameters:

**beginAxis**: an **OH\_NN\_INT32** scalar that specifies the axis from which normalization starts. The value range is \[1, rank(input)).

**epsilon**: an **OH\_NN\_FLOAT32** scalar that represents a tiny amount in the normalization formula. The common value is **1e-5**.

**beginParamsAxis**: the start axis of the input (gamma, beta) to be normalized.

Output:

**output**: n-dimensional tensor, with the same data type and shape as the input tensor.

 |
| OH\_NN\_OPS\_REDUCE\_PROD = 50 | 

Calculates the accumulated value for a tensor along the specified dimension.

Input:

**input**: n-dimensional input tensor, where n is less than 8.

**axis**: dimension used to calculate the product. The value is a 1D tensor. The value range of each element in **axis** is \[–n, n).

Parameters:

**keepDims**: whether to retain the dimension. The value is a Boolean value. If its value is **true**, the number of output dimensions is the same as that of the input. If its value is **false**, the number of output dimensions is reduced.

**reduceToEnd**: a Boolean value indicating whether to perform the reduce operation until the last axis.

**coeff**: an **OH\_NN\_FLOAT32** scalar indicating the output scaling factor.

Output:

**output**: m-dimensional output tensor whose data type is the same as that of the input. If **keepDims** is **false**, m < n. If **keepDims** is **true**, m==n.

 |
| OH\_NN\_OPS\_REDUCE\_ALL = 51 | 

Calculates the logical AND of the specified dimension. If **keepDims** is **false**, the number of input dimensions is reduced. If **keepDims** is **true**, the number of input dimensions is retained.

Input:

**input**: n-dimensional input tensor, where n is less than 8.

A 1D tensor specifying the dimension used to operate the logical OR. The value range of each element in **axis** is \[–n, n).

Parameters:

**keepDims**: whether to retain the dimension. The value is a Boolean value.

**reduceToEnd**: a Boolean value indicating whether to perform the reduce operation until the last axis.

**coeff**: an **OH\_NN\_FLOAT32** scalar indicating the output scaling factor.

Output:

**output**: m-dimensional output tensor whose data type is the same as that of the input. If **keepDims** is **false**, m < n. If **keepDims** is **true**, m==n.

 |
| OH\_NN\_OPS\_QUANT\_DTYPE\_CAST = 52 | 

Converts the data type.

Input:

**input**: n-dimensional tensor. For conversion between the quantization type and floating-point type, the input tensor must contain quantization parameters.

Parameters:

**srcT**: data type of the input.

**dstT**: data type of the output.

**axis**: the dimension for extracting quantization parameters. If the size of the input tensor quantization parameter is **1**, the operator function is used for layer quantization conversion and this parameter does not take effect. If the size of the input tensor quantization parameter is greater than **1**, the operator function is used for channel quantization conversion and this parameter takes effect.

Output:

**output**: n-dimensional tensor. The data type is determined by **dstT**. The output shape is the same as the input shape.

 |
| OH\_NN\_OPS\_TOP\_K = 53 | 

Obtains the values and indices of the largest k entries in the last dimension.

Input:

**input**: n-dimensional tensor.

**k**: first k records of data and their indices.

Parameters:

**sorted**: order of sorting. The value **true** means descending and **false** means ascending.

**axis**: an **OH\_NN\_INT32** scalar that specifies the dimension to be sorted. The default value is **\-1**, pointing to the last dimension.

Output:

**output0**: largest k elements in each slice of the last dimension.

**output1**: index of the value in the last dimension of the input.

 |
| OH\_NN\_OPS\_ARG\_MAX = 54 | 

Returns the index of the maximum tensor value across axes.

Input:

**input**: n-dimensional tensor (N, \*), where \* means any number of additional dimensions.

Parameters:

**axis**: dimension for calculating the index of the maximum.

**keepDims**: a Boolean value indicating whether to maintain the input tensor dimension.

**topK**: number of maximum values to be returned. The default value is **1**. If **topK** is equal to **1**, the index of the max value in the input tensor is returned. If **topK** is greater than **1**, the indices of the first top K max values in the input tensor is returned. If multiple values in the input tensor are the max value, any of them is returned.

**outMaxValue**: whether to output the maximum value. The default value is **false**.

Output:

**output**: index of the maximum input tensor on the axis. The value is a tensor.

 |
| OH\_NN\_OPS\_UNSQUEEZE = 55 | 

Adds a dimension based on the value of **axis**.

Input:

**input**: n-dimensional tensor.

Parameters:

**axis**: dimension to add. The value of **axis** can be an integer or an array of integers. The value range of the integer is \[-n, n).

Output:

**output**: output tensor.

 |
| OH\_NN\_OPS\_GELU = 56 | 

Activates the Gaussian error linear unit. The int quantization input is not supported. output=0.5input(1+tanh(input/2))

Input:

**input**: n-dimensional input tensor.

Parameters:

**approximate**: a Boolean value that represents the option of the approximation function. If the value is **true**, the approximation function is a Tanh function. If the value is **false**, the approximation function is an Erf function.

Output:

**output**: n-dimensional Relu tensor, with the same data type and shape as the input tensor.

 |
| OH\_NN\_OPS\_UNSTACK = 57 | 

Factorizes the input tensor based on the axis.

Input:

**input**: n-dimensional tensor.

Parameters:

**axis**: an **OH\_NN\_INT32** scalar that specifies the axis for matrix factorization. The value range is \[-n, n).

Output:

**output**: a collection of multiple tensors factorized from the input. Each tensor has the same shape.

**Since**: 12

 |
| OH\_NN\_OPS\_ABS = 58 | 

Calculates the absolute value of the input data.

Input:

**input**: n-dimensional tensor.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_ERF = 59 | 

Gaussian error function, which calculates the error of the input data by element.

Input:

input: n-dimensional tensor. The number of dimensions must be less than **8**. The data type can only be **OH\_NN\_FLOAT32** or **OH\_NN\_FLOAT16**.

Output:

**output**: an n-dimensional tensor. The data type and shape are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_EXP = 60 | 

Calculates the input exponent by element. The calculation formula is output = base ^ (shift + scale \* input), in which the base number is **base>0**. The default value is **\-1**, indicating that the base number is a natural constant **e**.

Input:

**input**: n-dimensional tensor.

Parameters:

**base**: base of the exponential function. The default value is **\-1**, indicating that the base is a natural constant **e**.

**scale**: scaling factor of the exponent. The default value is **1**.

**shift**: offset of the exponent. The default value is **0**.

Output:

**output**: an n-dimensional tensor, which is output result of the exponential function.

**Since**: 12

 |
| OH\_NN\_OPS\_LESS = 61 | 

Calculates the result of input1\[i\]<input2\[i\] by element for **input1** and **input2**, where **i** is the index of each element in the input tensor.

Input:

**input1**: a real number, Boolean value, or tensor whose data type is real number or **OH\_NN\_BOOL**. **input2**: a real number or a Boolean value if **input1** is a tensor, or a tensor whose data type is real number or **OH\_NN\_BOOL** if **input1** is not a tensor.

Output:

**output**: a tensor of the **OH\_NN\_BOOL** type. When a quantization model is used, the quantization parameters of the output cannot be omitted. However, values of the quantization parameters do not affect the result.

**Since**: 12

 |
| OH\_NN\_OPS\_SELECT = 62 | 

Determines whether the output is selected from input 1 or input 2 by element based on the input conditions. If the condition is **true**, the output is selected from input 1. If the condition is **false**, the output is selected from input 2. When the condition is a tensor, the shapes of the three inputs must be the same.

Input:

**condition**: decision condition, which can be a real number or an n-dimensional tensor. **input1**: input 1 to be selected. **input2**: input 2 to be selected.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_SQUARE = 63 | 

Calculates the square of the input by element.

Input:

**input**: n-dimensional tensor.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_FLATTEN = 64 | 

Specifies the axis to flatten the input tensor.

Input:

**input**: n-dimensional tensor.

Parameters:

**axis**: axis along which the input is flattened. For a tensor whose input dimension is (d\_0, d\_1, ..., d\_n), the output dimension should be (d\_0\*\\d\_1\*...\*d\_(axis-1), d\_axis\*d\_(axis+1)\*...\*d\_n).

Output:

**output**: 2D tensor after being flattened.

**Since**: 12

 |
| OH\_NN\_OPS\_DEPTH\_TO\_SPACE = 65 | 

Rearranges the depth data blocks of the input tensor into spatial dimensions.

Input:

**input**: 4-dimensional tensor in NHWC or NCHW format. Currently, only NHWC is supported. The shape is \[batchSize, height, width, channels\]. Parameters:

**blockSize**: size of the block to be converted. The value must be an integer.

**mode**: conversion mode. The value **0** indicates DCR, and the value **1** indicates CRD. DCR indicates depth-column-row sequential rearrangement, and CRD indicates column-row-depth sequential rearrangement.

Output:

**output**: a 4-dimensional tensor. The format is the same as that of the input tensor, and the shape is \[batchSize, height \* blockSize, weight \* blockSize, channel / blockSize^2\].

**Since**: 12

 |
| OH\_NN\_OPS\_RANGE = 66 | 

Generates a sequence tensor. The generation range is \[start, limit), and the step is delta.

Input:

**input**: n-dimensional tensor. The output data type is the same as that of the input. Parameters:

**start**: start number of a generated sequence.

**limit**: end number of the generated sequence, excluding this value. **delta**: step. Partial data is skipped from the generated sequence range by step.

Output:

**output**: a 1-dimensional sequence tensor.

**Since**: 12

 |
| OH\_NN\_OPS\_INSTANCE\_NORM = 67 | 

Performs standardization processing on each input channel, so that the average value of each input channel is 0 and the variance is 1.

Input:

**input**: 4-dimensional tensor.

**scale**: 1D tensor. The scaling coefficient and size are the same as the number of input channels.

**bias**: 1D tensor that represents the bias constant. The size is the same as the number of input channels.

Parameters:

**epsilon**: a small value added to the denominator to ensure calculation stability.

Output:

**output**: 4-dimensional tensor with the same shape as the input.

**Since**: 12

 |
| OH\_NN\_OPS\_CONSTANT\_OF\_SHAPE = 68 | 

Generates a tensor with the specified shape.

Input:

**input**: 1D tensor that represents the shape of the target tensor.

Parameters:

**dataType**: data type of the target tensor.

**value**: value of the target tensor, which is a single-element array whose data type is **OH\_NN\_FLOAT32**.

Output:

**output**: target tensor.

**Since**: 12

 |
| OH\_NN\_OPS\_BROADCAST\_TO = 69 | 

Broadcasts a tensor to an adapted shape.

Input:

**input**: n-dimensional tensor. Parameters:

**shape**: 1D tensor that represents the expected output shape.

Output:

**output**: broadcast tensor.

**Since**: 12

 |
| OH\_NN\_OPS\_EQUAL = 70 | 

Calculates the result of input1\[i\] = input2\[i\] by element for **input1** and **input2**, where **i** is the index of each element in the input tensor.

Input:

**input1**: a real number, Boolean value, or tensor whose data type is real number or **OH\_NN\_BOOL**.

**input2**: a real number or a Boolean value if **input1** is a tensor, or a tensor whose data type is real number or **OH\_NN\_BOOL** if **input1** is not a tensor.

Output:

**output**: a tensor of the **OH\_NN\_BOOL** type. When a quantization model is used, the quantization parameters of the output cannot be omitted. However, values of the quantization parameters do not affect the result.

**Since**: 12

 |
| OH\_NN\_OPS\_GREATER = 71 | 

Calculates the result of input1\[i\]>input2\[i\] by element for **input1** and **input2**, where **i** is the index of each element in the input tensor.

Input:

**input1**: a real number, Boolean value, or tensor whose data type is real number or **OH\_NN\_BOOL**.

**input2**: a real number or a Boolean value if **input1** is a tensor, or a tensor whose data type is real number or **OH\_NN\_BOOL** if **input1** is not a tensor.

Output:

**output**: a tensor of the **OH\_NN\_BOOL** type. When a quantization model is used, the quantization parameters of the output cannot be omitted. However, values of the quantization parameters do not affect the result.

**Since**: 12

 |
| OH\_NN\_OPS\_NOT\_EQUAL = 72 | 

Calculates the result of input1\[i\] != input2\[i\] by element for **input1** and **input2**, where **i** is the index of each element in the input tensor.

Input:

**input1**: a real number, Boolean value, or tensor whose data type is real number or **OH\_NN\_BOOL**.

**input2**: a real number or a Boolean value if **input1** is a tensor, or a tensor whose data type is real number or **OH\_NN\_BOOL** if **input1** is not a tensor.

Output:

**output**: a tensor of the **OH\_NN\_BOOL** type. When a quantization model is used, the quantization parameters of the output cannot be omitted. However, values of the quantization parameters do not affect the result.

**Since**: 12

 |
| OH\_NN\_OPS\_GREATER\_EQUAL = 73 | 

Calculates the result of input1\[i\]>=input2\[i\] by element for **input1** and **input2**, where **i** is the index of each element in the input tensor.

Input:

**input1**: a real number, Boolean value, or tensor whose data type is real number or **OH\_NN\_BOOL**.

**input2**: a real number or a Boolean value if **input1** is a tensor, or a tensor whose data type is real number or **OH\_NN\_BOOL** if **input1** is not a tensor.

Output:

**output**: a tensor of the **OH\_NN\_BOOL** type. When a quantization model is used, the quantization parameters of the output cannot be omitted. However, values of the quantization parameters do not affect the result.

**Since**: 12

 |
| OH\_NN\_OPS\_LEAKY\_RELU = 74 | 

Calculates the activation value of the input **leakyRelu**.

Input:

**input**: n-dimensional tensor.

Parameters:

**negativeSlope**: slope when the input is less than **0**, which controls the output size. The data type is **OH\_NN\_FLOAT32**.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_LSTM = 75 | 

Performs long-term and short-term memory (LSTM) network calculations on the input.

Input:

**input**: 3D tensor in the shape of \[seqLen, batchSize, inputSize\].

**wIh**: weight from the input to the hidden layer. The shape is \[numDirections\*numLayers, 4\*hiddenSize, inputSize\].

**wHh**: weight from the hidden layer to the hidden layer. The shape is \[numDirections\*numLayers, 4\*hiddenSize, inputSize\].

**bias**: bias from the input and hidden layers to the hidden layer. The shape is \[numDirections\*numLayers, 8\*hiddenSize\].

**hx**: initial hidden status of the unit gate. The shape is \[numDirections\*numLayers, batchSize, hiddenSize\].

**cx**: initial cell status of the unit gate. The shape is \[numDirections\*numLayers, batchSize, hiddenSize\].

Parameters:

**bidirectional**: Boolean value indicating whether the LSTM is bidirectional.

**hasBias**: Boolean value indicating whether the unit gate has a bias.

**inputSize**: input size.

**hiddenSize**: status size of the hidden layer.

**numLayers**: number of LSTM network layers.

**numDirections**: number of directions of the LSTM network.

**dropout**: drop probability. The probability that the input of each layer except the first layer is discarded is \[0.0, 1.0\].

**zoneoutCell**: probability that the control unit retains the previous state. The default value is **0**.

**zoneoutHidden**: probability that the hidden layer retains the previous state. The default value is **0**.

**projSize**: projection size. If the value is greater than **0**, the LSTM projection is used. The default value is **0**.

Output:

**output**: 3D tensor in the shape of \[seqLen, batchSize, numDirections\*realHiddenSize\]. The channels of all output tensors are stitched for output.

**hy**: output tensor of the last hidden layer. The shape is \[numDirections\*numLayers, batchSize, realHiddenSize\].

**cy**: output tensor of the unit gate at the last layer. The shape is \[numDirections\*numLayers, batchSize, HiddenSize\].

**Since**: 12

 |
| OH\_NN\_OPS\_CLIP = 76 | 

Crops the value of the input tensor to a value between the specified minimum and maximum values.

Input:

**input**: n-dimensional tensor or tensor list or tuple. Tensors of any dimensions are supported.

Parameters:

**min**: minimum cropping value.

**max**: maximum cropping value.

Output:

**output**: tensor after value cropping. The shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_ALL = 77 | 

Checks whether all elements of the specified dimension in the input are non-zero values. If all elements are non-zero values, **true** is returned for the corresponding dimension. Otherwise, **false** is returned for the corresponding dimension.

Input:

**input**: n-dimensional tensor in the shape of (N, \*), where \* indicates any number of additional dimensions.

**axis**: 1D tensor that represents the dimension to be calculated.

Parameters:

**keepDims**: whether to retain the dimension of the output tensor.

Output:

**output**: 1-dimensional or n-dimensional tensor whose data type is **OH\_NN\_BOOL**. It is the tensor output after non-zero judgment.

**Since**: 12

 |
| OH\_NN\_OPS\_ASSERT = 78 | 

Asserts whether the given condition is true. If the result of the given condition is false, the tensor list in **data** is printed, where **summarize** is used to determine the number of tensor entries to be printed.

Input:

**condition**: condition to evaluate.

**data**: tensor to be printed when the condition is false.

Parameters:

**summarize**: number of entries in each tensor to be printed.

Output:

**output**: output result. If the condition is not true, **Error** is returned.

**Since**: 12

 |
| OH\_NN\_OPS\_COS = 79 | 

Calculates the cosine value of the input data by element.

Input:

**input**: n-dimensional tensor whose data type is **OH\_NN\_FLOAT64**, **OH\_NN\_FLOAT32**, or **OH\_NN\_FLOAT16**.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_LOG = 80 | 

Calculates the natural logarithm of the input by element.

Input:

**input**: n-dimensional tensor whose data type is **OH\_NN\_FLOAT64**, **OH\_NN\_FLOAT32**, or **OH\_NN\_FLOAT16**. The value must be greater than **0**.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_LOGICAL\_AND = 81 | 

Calculates the logical AND operation of two input tensors by element.

Input:

**input1**: n-dimensional tensor whose data type is **OH\_NN\_BOOL**. **input2**: n-dimensional tensor whose data type is **OH\_NN\_BOOL** and the shape is the same as that of **input1**.

Output:

**output**: n-dimensional tensor whose data type is **OH\_NN\_BOOL**. It is the result of the logical AND operation.

**Since**: 12

 |
| OH\_NN\_OPS\_LOGICAL\_NOT = 82 | 

Calculates the logical NOT operation of two input tensors by element.

Input:

**input**: n-dimensional tensor whose data type is **OH\_NN\_BOOL**.

Output:

**output**: n-dimensional tensor whose data type is **OH\_NN\_BOOL**. It is the result of the logical NOT operation.

**Since**: 12

 |
| OH\_NN\_OPS\_MOD = 83 | 

Performs the mod operation on the input tensor. **input1** and **input2** must be converted into the same data type based on the data type conversion rules. The input must contain two tensors or contain one tensor and one scalar. If the input contains two tensors, their data types must not be both **OH\_NN\_BOOL** and they can be broadcast to the same shape. If the input contains one tensor and one scalar, the scalar input can only be a constant.

Input:

**input1**: scalar or tensor for the mod operation. The data type is numeric, **OH\_NN\_BOOL**, or n-dimensional numeric tensor.

**input2**: cofactor for the mod operation. When the first input is an n-dimensional tensor, the second input can be a numeric or **OH\_NN\_BOOL** value, or an n-dimensional numeric tensor. If the first input is a numeric or **OH\_NN\_BOOL** value, the second input must be an n-dimensional numeric tensor.

Output:

**output**: an n-dimensional tensor. The shape is the same as that of the broadcast input. The data type is the data type with higher precision in the two inputs.

**Since**: 12

 |
| OH\_NN\_OPS\_NEG = 84 | 

Calculates the opposite number of the input by element.

Input:

**input**: n-dimensional tensor whose data type is numeric.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_RECIPROCAL = 85 | 

Calculates the reciprocal of the input exponent by element.

Input:

**input**: n-dimensional tensor whose data type is **OH\_NN\_FLOAT64**, **OH\_NN\_FLOAT32**, or **OH\_NN\_FLOAT16**.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_SIN = 86 | 

Calculates the sine value of the input by element.

Input:

**input**: n-dimensional tensor whose data type is **OH\_NN\_FLOAT64**, **OH\_NN\_FLOAT32**, or **OH\_NN\_FLOAT16**.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_WHERE = 87 | 

Selects proper elements from **input1** and **input2** based on the specified condition.

Input:

**condition**: n-dimensional tensor whose data type is **OH\_NN\_BOOL**. If the element is **true**, the element corresponding to **input1** is selected. If the element is **false**, the element corresponding to **input2** is selected.

**input1**: n-dimensional tensor to be selected.

**input2**: n-dimensional tensor to be selected.

Output:

**output**: output elements.

**Since**: 12

 |
| OH\_NN\_OPS\_SPARSE\_TO\_DENSE = 88 | 

Converts a sparse tensor to a dense tensor.

Input:

**indices**: 2D tensor indicating the location of an element in the sparse tensor.

**values**: 1D tensor indicating the value mapping to the location in **indices**. **sparseShape**: shape of a tensor, which consists of two positive integers. The shape is (N, C).

Output:

**output**: target tensor after conversion, whose data type is the same as that of **value** and the shape is specified by **sparseShape**.

**Since**: 12

 |
| OH\_NN\_OPS\_LOGICAL\_OR = 89 | 

Calculates the logical OR operation of two input tensors by element.

Input:

**input1**: n-dimensional tensor whose data type is **OH\_NN\_BOOL**.

**input2**: n-dimensional tensor whose data type is **OH\_NN\_BOOL** and the shape is the same as that of **input1**.

Output:

**output**: n-dimensional tensor whose data type is **OH\_NN\_BOOL**. It is the result of the logical OR operation.

**Since**: 12

 |
| OH\_NN\_OPS\_CEIL = 90 | 

Rounds up each input element.

Input:

**input**: n-dimensional tensor whose data type is **OH\_NN\_FLOAT64**, **OH\_NN\_FLOAT32**, or **OH\_NN\_FLOAT16**.

Output:

**output**: n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_CROP = 91 | 

Crops the input tensor with the specified shape based on the specified axis and offset.

Input:

**input**: n-dimensional tensor to be cropped. **shape**: 1D tensor indicating the size of the tensor to be cropped.

Parameters:

**axis**: start axis of the cropped area. The value range is \[0,1, ...,r-1\], where **r** is the rank of the input tensor, and a negative number indicates the reverse value.

**offset**: start offset of the cropped area.

Output:

**output**: cropped tensor.

**Since**: 12

 |
| OH\_NN\_OPS\_DETECTION\_POST\_PROCESS = 92 | 

Performs post-processing on the output of the object detection model. Specific operations include decoding the bounding box, category probability, and score output by the model, performing Non-Max suppression (NMS) to remove the overlapping bounding box, and outputting the detection result.

Input:

**bbox**: bounding box.

**scores**: category score probability.

**anchors**: anchors used to generate coordinates and size of the candidate box of a detection box. In an object detection task, candidate boxes are a series of rectangular boxes preset in an image according to specific rules. These rectangular boxes usually have different sizes and aspect ratios, and are used to preliminarily predict and screen a target in the image.

Parameters:

**inputSize**: size of the input tensor.

**scale**: scaling factor used to convert the output image from the normalized form to the coordinates of the original image.

**nmsIoUThreshold**: Non-Max suppression threshold, which is used to remove duplicate detection boxes.

**nmsScoreThreshold**: confidence threshold, which is used to filter low-confidence detection boxes.

**maxDetections**: maximum number of detection boxes that can be output for each image.

**detectionsPerClass**: maximum number of detections for each category.

**maxClassesPerDetection**: maximum number of detection categories in each detection box.

**numClasses**: total number of detection categories.

**useRegularNms**: Boolean value indicating whether to use the IoU threshold-based Non-Max suppression algorithm. When the value is **true**, the IoU threshold-based Non-Max suppression algorithm is used to filter overlapped target boxes and retain the target box with the highest score. If this parameter is set to **false**, the IoU threshold-based Non-Max suppression algorithm is not applicable. The target boxes are sorted based on the score and the target box with the highest score is retained.

**outQuantized**: Boolean value indicating whether the output needs to be quantized.

Output:

**bboxes**: 3D tensor whose internal array indicates the coordinates of the object detection box.

**classes**: 2D tensor whose internal value indicates the class index corresponding to each detection box.

**confidences**: 2D tensor. The internal value indicates the confidence of the detected object.

**numDetections**: number of detection results.

**Since**: 12

 |
| OH\_NN\_OPS\_FLOOR = 93 | 

Rounds down each input element.

Input:

**input**: n-dimensional tensor whose data type is **OH\_NN\_FLOAT64**, **OH\_NN\_FLOAT32**, or **OH\_NN\_FLOAT16**.

Output:

**output**: n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_L2\_NORMALIZE = 94 | 

Performs L2 regularization on the input tensor based on the specified axis.

Input:

**input**: n-dimensional tensor for L2 regularization.

Parameters:

**axis**: specified dimension for regularization. The value **\-1** indicates the last dimension.

**epsilon**: a small value added to the denominator to ensure calculation stability. The default value is **1e-6**. **activationType**: activation function type.

Output:

**output**: output tensor whose data type and shape are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_LOG\_SOFTMAX = 95 | 

Performs exponential operations on each element of the input tensor and normalizes the operation result to obtain a probability distribution vector.

Input:

**input**: 2D tensor whose shape is \[batchSize, numClasses\] and data type is **OH\_NN\_FLOAT64**, **OH\_NN\_FLOAT32**, or **OH\_NN\_FLOAT16**.

Parameters:

**axis**: dimension for calculation.

Output:

**output**: 2D tensor that represents the probability vector after calculation.

**Since**: 12

 |
| OH\_NN\_OPS\_LRN = 96 | 

Normalizes the local response of the input.

Input:

**input**: 4D tensor to be normalized.

Parameters:

**depthRadius**: scalar type indicating the half width of the normalized window.

**bias**: bias used to avoid division by zero. The default value is **1**.

**alpha**: ratio coefficient. The default value is **1**.

**beta**: exponential variable. The default value is **0.5**.

**normRegion**: normalized region. The default value is **0**, indicating that the normalized region is **ACROSS\_CHANNELS**. Currently, only this mode is supported.

Output:

**output**: normalized output tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_MINIMUM = 97 | 

Calculates the minimum value of two tensors by element. The input must contain two tensors or contain one tensor and one scalar. If the input contains two tensors, their data types must not be both Boolean and they can be broadcast to the same shape. If the input contains one tensor and one scalar, the scalar input can only be a constant.

Input:

**input1**: n-dimensional tensor whose data type can be numeric or Boolean.

**input2**: n-dimensional tensor whose data type can be numeric or Boolean.

Output:

**output**: comparison result tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_RANK = 98 | 

Calculates the rank of a tensor.

Input:

**input**: n-dimensional tensor.

Output:

**output**: 0D tensor indicating the input rank. The data type is int32.

**Since**: 12

 |
| OH\_NN\_OPS\_REDUCE\_MAX = 99 | 

Calculates the maximum value of the input tensors in the specified dimension. If **keepDims** is **false**, the dimension of the output tensor is reduced. If **keepDims** is **true**, the dimension of the output tensor and the input tensor remain unchanged.

Input:

**input**: n-dimensional tensor, where n<8.

**axis**: dimension used to calculate the maximum value.

Parameters:

**keepDims**: whether to retain the dimension. The value is a Boolean value.

**reduceToEnd**: a Boolean value indicating whether to perform the reduce operation until the last axis.

**coeff**: an **OH\_NN\_FLOAT32** scalar indicating the output scaling factor.

Output:

**output**: m-dimensional output tensor whose data type is the same as that of the input. If **keepDims** is **false**, m < n. If **keepDims** is **true**, m==n.

**Since**: 12

 |
| OH\_NN\_OPS\_REDUCE\_MIN = 100 | 

Calculates the minimum value of the input tensors in the specified dimension. If **keepDims** is **false**, the dimension of the output tensor is reduced. If **keepDims** is **true**, the dimension of the output tensor and the input tensor remain unchanged.

Input:

**input**: n-dimensional tensor, where n<8.

**axis**: dimension used to calculate the minimum value.

Parameters:

**keepDims**: whether to retain the dimension. The value is a Boolean value.

**reduceToEnd**: a Boolean value indicating whether to perform the reduce operation until the last axis.

**coeff**: an **OH\_NN\_FLOAT32** scalar indicating the output scaling factor.

Output:

**output**: m-dimensional output tensor whose data type is the same as that of the input. If **keepDims** is **false**, m < n. If **keepDims** is **true**, m==n.

**Since**: 12

 |
| OH\_NN\_OPS\_REDUCE\_SUM = 101 | 

Calculates the sum of the input tensors in the specified dimension. If **keepDims** is **false**, the dimension of the output tensor is reduced. If **keepDims** is **true**, the dimension of the output tensor and the input tensor remain unchanged.

Input:

**input**: n-dimensional tensor, where n<8.

**axis**: dimension used to calculate the sum.

Parameters:

**keepDims**: whether to retain the dimension. The value is a Boolean value.

**reduceToEnd**: a Boolean value indicating whether to perform the reduce operation until the last axis.

**coeff**: an **OH\_NN\_FLOAT32** scalar indicating the output scaling factor.

Output:

**output**: m-dimensional output tensor whose data type is the same as that of the input. If **keepDims** is **false**, m < n. If **keepDims** is **true**, m==n.

**Since**: 12

 |
| OH\_NN\_OPS\_ROUND = 102 | 

Rounds off the input tensor to approximate the value.

Input:

**input**: n-dimensional tensor.

Output:

**output**: an n-dimensional tensor whose shape and data type are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_SCATTER\_ND = 103 | 

Distributes the updated value to a new tensor based on the specified index.

Input:

**indices**: indices scattered in the new tensor. The data type is **OH\_NN\_INT64** or **OH\_NN\_INT32**. The index rank is at least 2, and the value of the last dimension of **indices** is less than the size of the input shape.

**updates**: tensor to be updated.

**shape**: shape of the output tensor. The data type is the same as that of **indices**.

Output:

**output**: updated tensor. The data type is the same as that of **updates**, and the shape is the same as that of **shape**.

**Since**: 12

 |
| OH\_NN\_OPS\_SPACE\_TO\_DEPTH = 104 | 

Rearranges spatial dimension data blocks of the input tensor into depth dimensions.

Input:

**input**: 4-dimensional tensor in NHWC or NCHW format. Currently, only NHWC is supported. The shape is \[batchSize, height, width, channels\]. Parameters:

**blockSize**: size of the block to be converted. The value must be an integer.

Output:

**output**: a 4-dimensional tensor. The format is the same as that of the input tensor, and the shape is \[batchSize, height / blockSize, weight / blockSize, channel \* blockSize^2\].

**Since**: 12

 |
| OH\_NN\_OPS\_SWISH = 105 | 

Calculates Swish activation for the input tensor by element.

Input:

**input**: n-dimensional tensor. Output:

**output**: an n-dimensional tensor. The data type and shape are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_REDUCE\_L2 = 106 | 

Calculates the L2 norm of the input tensors in the specified dimension. If **keepDims** is **false**, the dimension of the output tensor is reduced. If **keepDims** is **true**, the dimension of the output tensor and the input tensor remain unchanged.

Input:

**input**: n-dimensional tensor, where n<8.

**axis**: axis used to calculate the dimension of the L2 norm.

Parameters:

**keepDims**: whether to retain the dimension. The value is a Boolean value.

**reduceToEnd**: a Boolean value indicating whether to perform the reduce operation until the last axis.

**coeff**: an **OH\_NN\_FLOAT32** scalar indicating the output scaling factor.

Output:

**output**: m-dimensional output tensor whose data type is the same as that of the input. If **keepDims** is **false**, m < n. If **keepDims** is **true**, m==n.

**Since**: 12

 |
| OH\_NN\_OPS\_HARD\_SIGMOID = 107 | 

Calculates HardSigmoid activation for the input tensor by element.

Input:

**input**: n-dimensional tensor.

Output:

**output**: an n-dimensional tensor. The data type and shape are the same as those of the input.

**Since**: 12

 |
| OH\_NN\_OPS\_GATHER\_ND = 108 | 

Obtains the element at the specified location of the input tensor based on the specified index.

Input:

**input**: n-dimensional tensor.

**indices**: m-dimensional tensor whose data type is **OH\_NN\_INT64** or **OH\_NN\_INT32**.

Output:

**output**: an n-dimensional tensor. The data type is the same as that of the input. The shape is the concatenation of the first dimension (m-1) of **indices** and the last dimension (size of the last dimension of n-indices) of input.

**Since**: 12

 |

#### \[h2\]OH\_NN\_TensorType

enum OH\_NN\_TensorType

**Description**

Defines tensor types.

Tensors are usually used to set the input, output, and operator parameters of a model. When a tensor is used as the input or output of a model (or operator), set the tensor type to [OH\_NN\_TENSOR](#oh_nn_tensortype). When the tensor is used as an operator parameter, select an enumerated value other than [OH\_NN\_TENSOR](#oh_nn_tensortype) as the tensor type.

Assume that pad of the [OH\_NN\_OPS\_CONV2D](#oh_nn_operationtype) operator is being set. You need to set the type attribute of the [OH\_NN\_Tensor](../../structs/oh-nn-tensor/document.md) instance to [OH\_NN\_CONV2D\_PAD](#oh_nn_tensortype). The settings of other operator parameters are similar. The enumerated values are named in the format OH\_NN\_{Operator name}\_{Attribute name}.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_NN\_TENSOR = 0 | Used when the tensor is used as the input or output of a model (or operator). |
| OH\_NN\_ADD\_ACTIVATIONTYPE = 1 | Used when the tensor is used as the **activationType** parameter of the Add operator. |
| OH\_NN\_AVG\_POOL\_KERNEL\_SIZE = 2 | Used when the tensor is used as the **kernelSize** parameter of the AvgPool operator. |
| OH\_NN\_AVG\_POOL\_STRIDE = 3 | Used when the tensor is used as the **stride** parameter of the AvgPool operator. |
| OH\_NN\_AVG\_POOL\_PAD\_MODE = 4 | Used when the tensor is used as the **AvgPool** parameter of the padMode operator. |
| OH\_NN\_AVG\_POOL\_PAD = 5 | Used when the tensor is used as the **pad** parameter of the AvgPool operator. |
| OH\_NN\_AVG\_POOL\_ACTIVATION\_TYPE = 6 | Used when the tensor is used as the **activationType** parameter of the AvgPool operator. |
| OH\_NN\_BATCH\_NORM\_EPSILON = 7 | Used when the tensor is used as the **epsilon** parameter of the BatchNorm operator. |
| OH\_NN\_BATCH\_TO\_SPACE\_ND\_BLOCKSIZE = 8 | Used when the tensor is used as the **blockSize** parameter of the BatchToSpaceND operator. |
| OH\_NN\_BATCH\_TO\_SPACE\_ND\_CROPS = 9 | Used when the tensor is used as the **crops** parameter of the BatchToSpaceND operator. |
| OH\_NN\_CONCAT\_AXIS = 10 | Used when the tensor is used as the **axis** parameter of the Concat operator. |
| OH\_NN\_CONV2D\_STRIDES = 11 | Used when the tensor is used as the **strides** parameter of the Conv2D operator. |
| OH\_NN\_CONV2D\_PAD = 12 | Used when the tensor is used as the **pad** parameter of the Conv2D operator. |
| OH\_NN\_CONV2D\_DILATION = 13 | Used when the tensor is used as the **dilation** parameter of the Conv2D operator. |
| OH\_NN\_CONV2D\_PAD\_MODE = 14 | Used when the tensor is used as the **padMode** parameter of the Conv2D operator. |
| OH\_NN\_CONV2D\_ACTIVATION\_TYPE = 15 | Used when the tensor is used as the **activationType** parameter of the Conv2D operator. |
| OH\_NN\_CONV2D\_GROUP = 16 | Used when the tensor is used as the **group** parameter of the Conv2D operator. |
| OH\_NN\_CONV2D\_TRANSPOSE\_STRIDES = 17 | Used when the tensor is used as the **strides** parameter of the Conv2DTranspose operator. |
| OH\_NN\_CONV2D\_TRANSPOSE\_PAD = 18 | Used when the tensor is used as the **pad** parameter of the Conv2DTranspose operator. |
| OH\_NN\_CONV2D\_TRANSPOSE\_DILATION = 19 | Used when the tensor is used as the **dilation** parameter of the Conv2DTranspose operator. |
| OH\_NN\_CONV2D\_TRANSPOSE\_OUTPUT\_PADDINGS = 20 | Used when the tensor is used as the **outputPaddings** parameter of the Conv2DTranspose operator. |
| OH\_NN\_CONV2D\_TRANSPOSE\_PAD\_MODE = 21 | Used when the tensor is used as the **padMode** parameter of the Conv2DTranspose operator. |
| OH\_NN\_CONV2D\_TRANSPOSE\_ACTIVATION\_TYPE = 22 | Used when the tensor is used as the **activationType** parameter of the Conv2DTranspose operator. |
| OH\_NN\_CONV2D\_TRANSPOSE\_GROUP = 23 | Used when the tensor is used as the **group** parameter of the Conv2DTranspose operator. |
| OH\_NN\_DEPTHWISE\_CONV2D\_NATIVE\_STRIDES = 24 | Used when the tensor is used as the **strides** parameter of the DepthwiseConv2dNative operator. |
| OH\_NN\_DEPTHWISE\_CONV2D\_NATIVE\_PAD = 25 | Used when the tensor is used as the **pad** parameter of the DepthwiseConv2dNative operator. |
| OH\_NN\_DEPTHWISE\_CONV2D\_NATIVE\_DILATION = 26 | Used when the tensor is used as the **dilation** parameter of the DepthwiseConv2dNative operator. |
| OH\_NN\_DEPTHWISE\_CONV2D\_NATIVE\_PAD\_MODE = 27 | Used when the tensor is used as the **padMode** parameter of the DepthwiseConv2dNative operator. |
| OH\_NN\_DEPTHWISE\_CONV2D\_NATIVE\_ACTIVATION\_TYPE = 28 | Used when the tensor is used as the **activationType** parameter of the DepthwiseConv2dNative operator. |
| OH\_NN\_DIV\_ACTIVATIONTYPE = 29 | Used when the tensor is used as the **activationType** parameter of the Div operator. |
| OH\_NN\_ELTWISE\_MODE = 30 | Used when the tensor is used as the **mode** parameter of the Eltwise operator. |
| OH\_NN\_FULL\_CONNECTION\_AXIS = 31 | Used when the tensor is used as the **axis** parameter of the FullConnection operator. |
| OH\_NN\_FULL\_CONNECTION\_ACTIVATIONTYPE = 32 | Used when the tensor is used as the **activationType** parameter of the FullConnection operator. |
| OH\_NN\_MATMUL\_TRANSPOSE\_A = 33 | Used when the tensor is used as the **transposeA** parameter of the Matmul operator. |
| OH\_NN\_MATMUL\_TRANSPOSE\_B = 34 | Used when the tensor is used as the **transposeB** parameter of the Matmul operator. |
| OH\_NN\_MATMUL\_ACTIVATION\_TYPE = 35 | Used when the tensor is used as the **activationType** parameter of the Matmul operator. |
| OH\_NN\_MAX\_POOL\_KERNEL\_SIZE = 36 | Used when the tensor is used as the **kernelSize** parameter of the MaxPool operator. |
| OH\_NN\_MAX\_POOL\_STRIDE = 37 | Used when the tensor is used as the **stride** parameter of the MaxPool operator. |
| OH\_NN\_MAX\_POOL\_PAD\_MODE = 38 | Used when the tensor is used as the **padMode** parameter of the MaxPool operator. |
| OH\_NN\_MAX\_POOL\_PAD = 39 | Used when the tensor is used as the **pad** parameter of the MaxPool operator. |
| OH\_NN\_MAX\_POOL\_ACTIVATION\_TYPE = 40 | Used when the tensor is used as the **activationType** parameter of the MaxPool operator. |
| OH\_NN\_MUL\_ACTIVATION\_TYPE = 41 | Used when the tensor is used as the **activationType** parameter of the Mul operator. |
| OH\_NN\_ONE\_HOT\_AXIS = 42 | Used when the tensor is used as the **axis** parameter of the OneHot operator. |
| OH\_NN\_PAD\_CONSTANT\_VALUE = 43 | Used when the tensor is used as the **constantValue** parameter of the Pad operator. |
| OH\_NN\_SCALE\_ACTIVATIONTYPE = 44 | Used when the tensor is used as the **activationType** parameter of the Scale operator. |
| OH\_NN\_SCALE\_AXIS = 45 | Used when the tensor is used as the **axis** parameter of the Scale operator. |
| OH\_NN\_SOFTMAX\_AXIS = 46 | Used when the tensor is used as the **axis** parameter of the Softmax operator. |
| OH\_NN\_SPACE\_TO\_BATCH\_ND\_BLOCK\_SHAPE = 47 | Used when the tensor is used as the **BlockShape** parameter of the SpaceToBatchND operator. |
| OH\_NN\_SPACE\_TO\_BATCH\_ND\_PADDINGS = 48 | Used when the tensor is used as the **Paddings** parameter of the SpaceToBatchND operator. |
| OH\_NN\_SPLIT\_AXIS = 49 | Used when the tensor is used as the **Axis** parameter of the Split operator. |
| OH\_NN\_SPLIT\_OUTPUT\_NUM = 50 | Used when the tensor is used as the **OutputNum** parameter of the Split operator. |
| OH\_NN\_SPLIT\_SIZE\_SPLITS = 51 | Used when the tensor is used as the **SizeSplits** parameter of the Split operator. |
| OH\_NN\_SQUEEZE\_AXIS = 52 | Used when the tensor is used as the **Axis** parameter of the Squeeze operator. |
| OH\_NN\_STACK\_AXIS = 53 | Used when the tensor is used as the **Axis** parameter of the Stack operator. |
| OH\_NN\_STRIDED\_SLICE\_BEGIN\_MASK = 54 | Used when the tensor is used as the **BeginMask** parameter of the StridedSlice operator. |
| OH\_NN\_STRIDED\_SLICE\_END\_MASK = 55 | Used when the tensor is used as the **EndMask** parameter of the StridedSlice operator. |
| OH\_NN\_STRIDED\_SLICE\_ELLIPSIS\_MASK = 56 | Used when the tensor is used as the **EllipsisMask** parameter of the StridedSlice operator. |
| OH\_NN\_STRIDED\_SLICE\_NEW\_AXIS\_MASK = 57 | Used when the tensor is used as the **NewAxisMask** parameter of the StridedSlice operator. |
| OH\_NN\_STRIDED\_SLICE\_SHRINK\_AXIS\_MASK = 58 | Used when the tensor is used as the **ShrinkAxisMask** parameter of the StridedSlice operator. |
| OH\_NN\_SUB\_ACTIVATIONTYPE = 59 | Used when the tensor is used as the **ActivationType** parameter of the Sub operator. |
| OH\_NN\_REDUCE\_MEAN\_KEEP\_DIMS = 60 | Used when the tensor is used as the **keepDims** parameter of the ReduceMean operator. |
| OH\_NN\_RESIZE\_BILINEAR\_NEW\_HEIGHT = 61 | Used when the tensor is used as the **newHeight** parameter of the ResizeBilinear operator. |
| OH\_NN\_RESIZE\_BILINEAR\_NEW\_WIDTH = 62 | Used when the tensor is used as the **newWidth** parameter of the ResizeBilinear operator. |
| OH\_NN\_RESIZE\_BILINEAR\_PRESERVE\_ASPECT\_RATIO = 63 | Used when the tensor is used as the **preserveAspectRatio** parameter of the ResizeBilinear operator. |
| OH\_NN\_RESIZE\_BILINEAR\_COORDINATE\_TRANSFORM\_MODE = 64 | Used when the tensor is used as the **coordinateTransformMode** parameter of the ResizeBilinear operator. |
| OH\_NN\_RESIZE\_BILINEAR\_EXCLUDE\_OUTSIDE = 65 | Used when the tensor is used as the **excludeOutside** parameter of the ResizeBilinear operator. |
| OH\_NN\_LAYER\_NORM\_BEGIN\_NORM\_AXIS = 66 | Used when the tensor is used as the **beginNormAxis** parameter of the LayerNorm operator. |
| OH\_NN\_LAYER\_NORM\_EPSILON = 67 | Used when the tensor is used as the **epsilon** parameter of the LayerNorm operator. |
| OH\_NN\_LAYER\_NORM\_BEGIN\_PARAM\_AXIS = 68 | Used when the tensor is used as the **beginParamsAxis** parameter of the LayerNorm operator. |
| OH\_NN\_LAYER\_NORM\_ELEMENTWISE\_AFFINE = 69 | Used when the tensor is used as the **elementwiseAffine** parameter of the LayerNorm operator. |
| OH\_NN\_REDUCE\_PROD\_KEEP\_DIMS = 70 | Used when the tensor is used as the **keepDims** parameter of the ReduceProd operator. |
| OH\_NN\_REDUCE\_ALL\_KEEP\_DIMS = 71 | Used when the tensor is used as the **keepDims** parameter of the ReduceAll operator. |
| OH\_NN\_QUANT\_DTYPE\_CAST\_SRC\_T = 72 | Used when the tensor is used as the **srcT** parameter of the QuantDTypeCast operator. |
| OH\_NN\_QUANT\_DTYPE\_CAST\_DST\_T = 73 | Used when the tensor is used as the **dstT** parameter of the QuantDTypeCast operator. |
| OH\_NN\_TOP\_K\_SORTED = 74 | Used when the tensor is used as the **Sorted** parameter of the Topk operator. |
| OH\_NN\_ARG\_MAX\_AXIS = 75 | Used when the tensor is used as the **axis** parameter of the ArgMax operator. |
| OH\_NN\_ARG\_MAX\_KEEPDIMS = 76 | Used when the tensor is used as the **keepDims** parameter of the ArgMax operator. |
| OH\_NN\_UNSQUEEZE\_AXIS = 77 | Used when the tensor is used as the **Axis** parameter of the Unsqueeze operator. |
| OH\_NN\_UNSTACK\_AXIS = 78 | 
Used when the tensor is used as the **axis** parameter of the Unstack operator.

**Since**: 12

 |
| OH\_NN\_FLATTEN\_AXIS = 79 | 

Used when the tensor is used as the **axis** parameter of the Flatten operator.

**Since**: 12

 |
| OH\_NN\_DEPTH\_TO\_SPACE\_BLOCK\_SIZE = 80 | 

Used when the tensor is used as the **blockSize** parameter of the DepthToSpace operator.

**Since**: 12

 |
| OH\_NN\_DEPTH\_TO\_SPACE\_MODE = 81 | 

Used when the tensor is used as the **mode** parameter of the DepthToSpace operator.

**Since**: 12

 |
| OH\_NN\_RANGE\_START = 82 | 

Used when the tensor is used as the **start** parameter of the Range operator.

**Since**: 12

 |
| OH\_NN\_RANGE\_LIMIT = 83 | 

Used when the tensor is used as the **limit** parameter of the Range operator.

**Since**: 12

 |
| OH\_NN\_RANGE\_DELTA = 84 | 

Used when the tensor is used as the **delta** parameter of the Range operator.

**Since**: 12

 |
| OH\_NN\_CONSTANT\_OF\_SHAPE\_DATA\_TYPE = 85 | 

Used when the tensor is used as the **dataType** parameter of the ConstantOfShape operator.

**Since**: 12

 |
| OH\_NN\_CONSTANT\_OF\_SHAPE\_VALUE = 86 | 

Used when the tensor is used as the **value** parameter of the ConstantOfShape operator.

**Since**: 12

 |
| OH\_NN\_BROADCAST\_TO\_SHAPE = 87 | 

Used when the tensor is used as the **shape** parameter of the BroadcastTo operator.

**Since**: 12

 |
| OH\_NN\_INSTANCE\_NORM\_EPSILON = 88 | 

Used when the tensor is used as the **epsilon** parameter of the InstanceNorm operator.

**Since**: 12

 |
| OH\_NN\_EXP\_BASE = 89 | 

Used when the tensor is used as the **base** parameter of the Exp operator.

**Since**: 12

 |
| OH\_NN\_EXP\_SCALE = 90 | 

Used when the tensor is used as the **scale** parameter of the Exp operator.

**Since**: 12

 |
| OH\_NN\_EXP\_SHIFT = 91 | 

Used when the tensor is used as the **shift** parameter of the Exp operator.

**Since**: 12

 |
| OH\_NN\_LEAKY\_RELU\_NEGATIVE\_SLOPE = 92 | 

Used when the tensor is used as the **negativeSlope** parameter of the LeakyRelu operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_BIDIRECTIONAL = 93 | 

Used when the tensor is used as the **bidirectional** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_HAS\_BIAS = 94 | 

Used when the tensor is used as the **hasBias** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_INPUT\_SIZE = 95 | 

Used when the tensor is used as the **inputSize** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_HIDDEN\_SIZE = 96 | 

Used when the tensor is used as the **hiddenSize** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_NUM\_LAYERS = 97 | 

Used when the tensor is used as the **numLayers** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_NUM\_DIRECTIONS = 98 | 

Used when the tensor is used as the **numDirections** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_DROPOUT = 99 | 

Used when the tensor is used as the **dropout** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_ZONEOUT\_CELL = 100 | 

Used when the tensor is used as the **zoneoutCell** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_ZONEOUT\_HIDDEN = 101 | 

Used when the tensor is used as the **zoneoutHidden** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_LSTM\_PROJ\_SIZE = 102 | 

Used when the tensor is used as the **projSize** parameter of the LSTM operator.

**Since**: 12

 |
| OH\_NN\_CLIP\_MAX = 103 | 

Used when the tensor is used as the **max** parameter of the Clip operator.

**Since**: 12

 |
| OH\_NN\_CLIP\_MIN = 104 | 

Used when the tensor is used as the **min** parameter of the Clip operator.

**Since**: 12

 |
| OH\_NN\_ALL\_KEEP\_DIMS = 105 | 

Used when the tensor is used as the **keepDims** parameter of the All operator.

**Since**: 12

 |
| OH\_NN\_ASSERT\_SUMMARIZE = 106 | 

Used when the tensor is used as the **summarize** parameter of the Assert operator.

**Since**: 12

 |
| OH\_NN\_POW\_SCALE = 107 | 

Used when the tensor is used as the **scale** parameter of the Pow operator.

**Since**: 12

 |
| OH\_NN\_POW\_SHIFT = 108 | 

Used when the tensor is used as the **shift** parameter of the Pow operator.

**Since**: 12

 |
| OH\_NN\_AVG\_POOL\_ROUND\_MODE = 109 | 

Used when the tensor is used as the **RoundMode** parameter of the AvgPool operator.

**Since**: 12

 |
| OH\_NN\_AVG\_POOL\_GLOBAL = 110 | 

Used when the tensor is used as the **global** parameter of the AvgPool operator.

**Since**: 12

 |
| OH\_NN\_FULL\_CONNECTION\_HAS\_BIAS = 111 | 

Used when the tensor is used as the **hasBias** parameter of the FullConnection operator.

**Since**: 12

 |
| OH\_NN\_FULL\_CONNECTION\_USE\_AXIS = 112 | 

Used when the tensor is used as the **useAxis** parameter of the FullConnection operator.

**Since**: 12

 |
| OH\_NN\_GELU\_APPROXIMATE = 113 | 

Used when the tensor is used as the **approximate** parameter of the GeLU operator.

**Since**: 12

 |
| OH\_NN\_MAX\_POOL\_ROUND\_MODE = 114 | 

Used when the tensor is used as the **RoundMode** parameter of the MaxPool operator.

**Since**: 12

 |
| OH\_NN\_MAX\_POOL\_GLOBAL = 115 | 

Used when the tensor is used as the **global** parameter of the MaxPool operator.

**Since**: 12

 |
| OH\_NN\_PAD\_PADDING\_MODE = 116 | 

Used when the tensor is used as the **paddingMode** parameter of the Pad operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_MEAN\_REDUCE\_TO\_END = 117 | 

Used when the tensor is used as the **reduceToEnd** parameter of the ReduceMean operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_MEAN\_COEFF = 118 | 

Used when the tensor is used as the **coeff** parameter of the ReduceMean operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_PROD\_REDUCE\_TO\_END = 119 | 

Used when the tensor is used as the **reduceToEnd** parameter of the ReduceProd operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_PROD\_COEFF = 120 | 

Used when the tensor is used as the **coeff** parameter of the ReduceProd operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_ALL\_REDUCE\_TO\_END = 121 | 

Used when the tensor is used as the **reduceToEnd** parameter of the ReduceAll operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_ALL\_COEFF = 122 | 

Used when the tensor is used as the **coeff** parameter of the ReduceAll operator.

**Since**: 12

 |
| OH\_NN\_TOP\_K\_AXIS = 123 | 

Used when the tensor is used as the **axis** parameter of the TopK operator.

**Since**: 12

 |
| OH\_NN\_ARG\_MAX\_TOP\_K = 124 | 

Used when the tensor is used as the **topK** parameter of the ArgMax operator.

**Since**: 12

 |
| OH\_NN\_ARG\_MAX\_OUT\_MAX\_VALUE = 125 | 

Used when the tensor is used as the **outMaxValue** parameter of the ArgMax operator.

**Since**: 12

 |
| OH\_NN\_QUANT\_DTYPE\_CAST\_AXIS = 126 | 

Used when the tensor is used as the **axis** parameter of the QuantDTypeCast operator.

**Since**: 12

 |
| OH\_NN\_SLICE\_AXES = 127 | 

Used when the tensor is used as the **axes** parameter of the Slice operator.

**Since**: 12

 |
| OH\_NN\_TILE\_DIMS = 128 | 

Used when the tensor is used as the **dims** parameter of the Tile operator.

**Since**: 12

 |
| OH\_NN\_CROP\_AXIS = 129 | 

Used when the tensor is used as the **axis** parameter of the Crop operator.

**Since**: 12

 |
| OH\_NN\_CROP\_OFFSET = 130 | 

Used when the tensor is used as the **offset** parameter of the Crop operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_INPUT\_SIZE = 131 | 

Used when the tensor is used as the **inputSize** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_SCALE = 132 | 

Used when the tensor is used as the **scale** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_NMS\_IOU\_THRESHOLD = 133 | 

Used when the tensor is used as the **nmsIouThreshold** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_NMS\_SCORE\_THRESHOLD = 134 | 

Used when the tensor is used as the **nmsScoreThreshold** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_MAX\_DETECTIONS = 135 | 

Used when the tensor is used as the **maxDetections** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_DETECTIONS\_PER\_CLASS = 136 | 

Used when the tensor is used as the **perClass** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_MAX\_CLASSES\_PER\_DETECTION = 137 | 

Used when the tensor is used as the **maxClassPerDetection** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_NUM\_CLASSES = 138 | 

Used when the tensor is used as the **numClasses** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_USE\_REGULAR\_NMS = 139 | 

Used when the tensor is used as the **useRegularNms** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_DETECTION\_POST\_PROCESS\_OUT\_QUANTIZED = 140 | 

Used when the tensor is used as the **outQuantized** parameter of the DetectionPostProcess operator.

**Since**: 12

 |
| OH\_NN\_L2\_NORMALIZE\_AXIS = 141 | 

Used when the tensor is used as the **axis** parameter of the L2Normalize operator.

**Since**: 12

 |
| OH\_NN\_L2\_NORMALIZE\_EPSILON = 142 | 

Used when the tensor is used as the **epsilon** parameter of the L2Normalize operator.

**Since**: 12

 |
| OH\_NN\_L2\_NORMALIZE\_ACTIVATION\_TYPE = 143 | 

Used when the tensor is used as the **activationType** parameter of the L2Normalize operator.

**Since**: 12

 |
| OH\_NN\_LOG\_SOFTMAX\_AXIS = 144 | 

Used when the tensor is used as the **axis** parameter of the LogSoftmax operator.

**Since**: 12

 |
| OH\_NN\_LRN\_DEPTH\_RADIUS = 145 | 

Used when the tensor is used as the **depthRadius** parameter of the LRN operator.

**Since**: 12

 |
| OH\_NN\_LRN\_BIAS = 146 | 

Used when the tensor is used as the **bias** parameter of the LRN operator.

**Since**: 12

 |
| OH\_NN\_LRN\_ALPHA = 147 | 

Used when the tensor is used as the **alpha** parameter of the LRN operator.

**Since**: 12

 |
| OH\_NN\_LRN\_BETA = 148 | 

Used when the tensor is used as the **beta** parameter of the LRN operator.

**Since**: 12

 |
| OH\_NN\_LRN\_NORM\_REGION = 149 | 

Used when the tensor is used as the **normRegion** parameter of the LRN operator.

**Since**: 12

 |
| OH\_NN\_SPACE\_TO\_DEPTH\_BLOCK\_SIZE = 150 | 

Used when the tensor is used as the **blockSize** parameter of the SpaceToDepth operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_MAX\_KEEP\_DIMS = 151 | 

Used when the tensor is used as the **keepDims** parameter of the ReduceMax operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_MAX\_REDUCE\_TO\_END = 152 | 

Used when the tensor is used as the **reduceToEnd** parameter of the ReduceMax operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_MAX\_COEFF = 153 | 

Used when the tensor is used as the **coeff** parameter of the ReduceMax operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_MIN\_KEEP\_DIMS = 154 | 

Used when the tensor is used as the **keepDims** parameter of the ReduceMin operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_MIN\_REDUCE\_TO\_END = 155 | 

Used when the tensor is used as the **reduceToEnd** parameter of the ReduceMin operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_MIN\_COEFF = 156 | 

Used when the tensor is used as the **coeff** parameter of the ReduceMin operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_SUM\_KEEP\_DIMS = 157 | 

Used when the tensor is used as the **keepDims** parameter of the ReduceSum operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_SUM\_REDUCE\_TO\_END = 158 | 

Used when the tensor is used as the **reduceToEnd** parameter of the ReduceSum operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_SUM\_COEFF = 159 | 

Used when the tensor is used as the **coeff** parameter of the ReduceSum operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_L2\_KEEP\_DIMS = 160 | 

Used when the tensor is used as the **keepDims** parameter of the ReduceL2 operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_L2\_REDUCE\_TO\_END = 161 | 

Used when the tensor is used as the **reduceToEnd** parameter of the ReduceL2 operator.

**Since**: 12

 |
| OH\_NN\_REDUCE\_L2\_COEFF = 162 | 

Used when the tensor is used as the **coeff** parameter of the ReduceL2 operator.

**Since**: 12

 |

#### Function Description

#### \[h2\]NN\_OnRunDone()

typedef void (\*NN\_OnRunDone)(void \*userData, OH\_NN\_ReturnCode errCode, void \*outputTensor\[\], int32\_t outputCount)

**Description**

Defines the handle of the callback function invoked when the asynchronous inference ends.

Use the **userData** parameter to specify the asynchronous inference to query. The value of **userData** is the same as that passed to [OH\_NNExecutor\_RunAsync](../neural-network-core-h/document.md#oh_nnexecutor_runasync). Use the **errCode** parameter to obtain the return result (defined by [OH\_NN\_ReturnCode](#oh_nn_returncode) of the asynchronous inference.

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*userData | Identifier of asynchronous inference. The value is the same as the **userData** parameter passed to [OH\_NNExecutor\_RunAsync](../neural-network-core-h/document.md#oh_nnexecutor_runasync). |
| [OH\_NN\_ReturnCode](#oh_nn_returncode) errCode | Return result (defined by [OH\_NN\_ReturnCode](#oh_nn_returncode) of the asynchronous inference. |
| void \*outputTensor\[\] | Output tensor for asynchronous inference. The value is the same as the **outputTensor** parameter passed to [OH\_NNExecutor\_RunAsync](../neural-network-core-h/document.md#oh_nnexecutor_runasync). |
| int32\_t outputCount | Number of output tensors for asynchronous inference. The value is the same as the **outputCount** parameter passed to [OH\_NNExecutor\_RunAsync](../neural-network-core-h/document.md#oh_nnexecutor_runasync). |

#### \[h2\]NN\_OnServiceDied()

typedef void (\*NN\_OnServiceDied)(void \*userData)

**Description**

Defines the handle of the callback function invoked when the device driver service terminates unexpectedly during asynchronous inference.

You need to rebuild the model if the callback is invoked.

Use the **userData** parameter to specify the asynchronous inference to query. The value of **userData** is the same as that passed to [OH\_NNExecutor\_RunAsync](../neural-network-core-h/document.md#oh_nnexecutor_runasync).

**Since**: 11

**Parameters**

| Name | Description |
| :-- | :-- |
| void \*userData | Identifier of asynchronous inference. The value is the same as the **userData** parameter passed to [OH\_NNExecutor\_RunAsync](../neural-network-core-h/document.md#oh_nnexecutor_runasync). |
