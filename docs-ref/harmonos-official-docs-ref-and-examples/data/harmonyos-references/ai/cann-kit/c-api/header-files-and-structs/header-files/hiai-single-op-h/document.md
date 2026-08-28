# hiai\_single\_op.h

#### Overview

Defines the single-operator APIs of CANN Kit, which is used for creating and calculating single operators, and managing tensors and buffers.

**Library:** libhiai\_foundation.so

**Syscap:** SystemCapability.AI.HiAIFoundation

**Since:** 5.0.0(12)

**Related Modules:**[CANN](../../../modules/cann/document.md)

#### Summary

#### \[h2\]Data Structures

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [HiAISingleOpDescriptor\_ConvolutionParam](../../structs/hiaisingleopdescriptor-convolutionparam/document.md)

 | 

[HMS\_HiAISingleOpDescriptor\_CreateConvolution](../../../modules/cann/document.md#hms_hiaisingleopdescriptor_createconvolution) input parameters.

 |
| 

struct [HiAI\_SingleOpExecutorConvolutionParam](../../structs/hiai-singleopexecutorconvolutionparam/document.md)

 | 

[HMS\_HiAISingleOpExecutor\_CreateConvolution](../../../modules/cann/document.md#hms_hiaisingleopexecutor_createconvolution) input parameters.

 |
| 

struct [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md)

 | 

[HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](../../../modules/cann/document.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation) input parameters.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc)

 | 

Single op tensor description handle.

 |
| 

typedef struct [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer)

 | 

Single op buffer handle.

 |
| 

typedef struct [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor)

 | 

Single op tensor handle.

 |
| 

typedef struct [HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions) [HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions)

 | 

Single op option handle.

 |
| 

typedef struct [HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor) [HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor)

 | 

Single op operation description handle.

 |
| 

typedef struct [HiAISingleOpDescriptor\_ConvolutionParam](../../structs/hiaisingleopdescriptor-convolutionparam/document.md) [HiAISingleOpDescriptor\_ConvolutionParam](../../../modules/cann/document.md#hiai_singleopdescriptorconvolutionparam)

 | 

[HMS\_HiAISingleOpDescriptor\_CreateConvolution](../../../modules/cann/document.md#hms_hiaisingleopdescriptor_createconvolution) input parameters.

 |
| 

typedef struct [HiAI\_SingleOpExecutorConvolutionParam](../../structs/hiai-singleopexecutorconvolutionparam/document.md) [HiAI\_SingleOpExecutorConvolutionParam](../../../modules/cann/document.md#hiai_singleopexecutorconvolutionparam)

 | 

[HMS\_HiAISingleOpExecutor\_CreateConvolution](../../../modules/cann/document.md#hms_hiaisingleopexecutor_createconvolution) input parameters.

 |
| 

typedef struct [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md) [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../../modules/cann/document.md#hiai_singleopexecutorfusedconvolutionactivationparam)

 | 

[HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](../../../modules/cann/document.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation) input parameters.

 |
| 

typedef struct [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor)

 | 

Single op executor handle.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_SingleOpDataType](../../../modules/cann/document.md#hiai_singleopdatatype) {

HIAI\_SINGLEOP\_DT\_FLOAT = 0,

HIAI\_SINGLEOP\_DT\_FLOAT16 = 1,

HIAI\_SINGLEOP\_DT\_UNDEFINED = 17

}

 | 

Defines the single op tensor data type enums.

 |
| 

[HiAI\_SingleOpFormat](../../../modules/cann/document.md#hiai_singleopformat) {

HIAI\_SINGLEOP\_FORMAT\_NCHW = 0,

HIAI\_SINGLEOP\_FORMAT\_NHWC = 1,

HIAI\_SINGLEOP\_FORMAT\_ND = 2,

HIAI\_SINGLEOP\_FORMAT\_NC1HWC0 = 3,

HIAI\_SINGLEOP\_FORMAT\_NC4HW4 = 28,

HIAI\_SINGLEOP\_FORMAT\_NC8HW8 = 31,

HIAI\_SINGLEOP\_FORMAT\_RESERVED = 255

}

 | 

Defines the single op tensor formats.

 |
| 

[HiAI\_SingleOpConvMode](../../../modules/cann/document.md#hiai_singleopconvmode) {

HIAI\_SINGLEOP\_CONV\_MODE\_COMMON = 0,

HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED = 1,

HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE = 2

}

 | 

Defines the single op convolution mode enums.

 |
| 

[HiAI\_SingleOpPadMode](../../../modules/cann/document.md#hiai_singleoppadmode) {

HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC = 0,

HIAI\_SINGLEOP\_PAD\_MODE\_SAME = 1,

HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_UPPER = 2,

HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_LOWER = 3,

HIAI\_SINGLEOP\_PAD\_MODE\_VALID = 4

}

 | 

Defines the single op padding mode enums.

 |
| 

[HiAI\_SingleOpActivationType](../../../modules/cann/document.md#hiai_singleopactivationtype) {

HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU = 0,

HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU6 = 1

}

 | 

Defines the single op activation mode enums.

 |
| 

[HiAI\_SingleOpSupportStatus](../../../modules/cann/document.md#hiai_singleopsupportstatus) {

HIAI\_SINGLEOP\_OPTIMIZED = 0,

HIAI\_SINGLEOP\_COMMON = 1,

HIAI\_SINGLEOP\_UNSUPPORTED = 2

}

 | 

Defines the single op support status enums.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \* [HMS\_HiAISingleOpTensorDesc\_Create](../../../modules/cann/document.md#hms_hiaisingleoptensordesc_create) (const int64\_t \*dims, size\_t dimNum, [HiAI\_SingleOpDataType](../../../modules/cann/document.md#hiai_singleopdatatype) dataType, [HiAI\_SingleOpFormat](../../../modules/cann/document.md#hiai_singleopformat) format, bool isVirtual)

 | 

Creates a [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) object.

 |
| 

size\_t [HMS\_HiAISingleOpTensorDesc\_GetDimensionCount](../../../modules/cann/document.md#hms_hiaisingleoptensordesc_getdimensioncount) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries the number of dimensions of the [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) object.

 |
| 

int64\_t [HMS\_HiAISingleOpTensorDesc\_GetDimension](../../../modules/cann/document.md#hms_hiaisingleoptensordesc_getdimension) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*tensorDesc, size\_t index)

 | 

Queries the length of a dimension with a specific index of the [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) object.

 |
| 

[HiAI\_SingleOpDataType](../../../modules/cann/document.md#hiai_singleopdatatype) [HMS\_HiAISingleOpTensorDesc\_GetDataType](../../../modules/cann/document.md#hms_hiaisingleoptensordesc_getdatatype) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries the data type of the [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) object.

 |
| 

[HiAI\_SingleOpFormat](../../../modules/cann/document.md#hiai_singleopformat) [HMS\_HiAISingleOpTensorDesc\_GetFormat](../../../modules/cann/document.md#hms_hiaisingleoptensordesc_getformat) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries format of the [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) object.

 |
| 

bool [HMS\_HiAISingleOpTensorDesc\_IsVirtual](../../../modules/cann/document.md#hms_hiaisingleoptensordesc_isvirtual) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries whether [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) describes a virtual tensor.

 |
| 

size\_t [HMS\_HiAISingleOpTensorDesc\_GetByteSize](../../../modules/cann/document.md#hms_hiaisingleoptensordesc_getbytesize) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries the number of bytes occupied by the data calculated based on the dimension and data type of [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc).

 |
| 

void [HMS\_HiAISingleOpTensorDesc\_Destroy](../../../modules/cann/document.md#hms_hiaisingleoptensordesc_destroy) ([HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*\*tensorDesc)

 | 

Releases a [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) object.

 |
| 

[HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) \* [HMS\_HiAISingleOpBuffer\_Create](../../../modules/cann/document.md#hms_hiaisingleopbuffer_create) (size\_t dataSize)

 | 

Creates a [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) object based on the specific memory size.

 |
| 

size\_t [HMS\_HiAISingleOpBuffer\_GetSize](../../../modules/cann/document.md#hms_hiaisingleopbuffer_getsize) (const [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) \*buffer)

 | 

Queries the byte size of [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer).

 |
| 

void \* [HMS\_HiAISingleOpBuffer\_GetData](../../../modules/cann/document.md#hms_hiaisingleopbuffer_getdata) (const [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) \*buffer)

 | 

Queries the memory address of [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer).

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpBuffer\_Destroy](../../../modules/cann/document.md#hms_hiaisingleopbuffer_destroy) ([HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) \*\*buffer)

 | 

Releases a [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) object.

 |
| 

[HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](../../../modules/cann/document.md#hms_hiaisingleoptensor_createfromtensordesc) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*desc)

 | 

Creates a [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc).

 |
| 

[HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer](../../../modules/cann/document.md#hms_hiaisingleoptensor_createfromsingleopbuffer) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*desc, void \*data, size\_t dataSize)

 | 

Creates a [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc), the memory address from [HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) and data size.

 |
| 

[HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromConst](../../../modules/cann/document.md#hms_hiaisingleoptensor_createfromconst) (const [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*desc, void \*data, size\_t dataSize)

 | 

Creates a [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc), the memory address and the size of constant data (such as the convolution weight and bias).

 |
| 

[HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \* [HMS\_HiAISingleOpTensor\_GetTensorDesc](../../../modules/cann/document.md#hms_hiaisingleoptensor_gettensordesc) (const [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \*tensor)

 | 

Obtains the tensor description of [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor).

 |
| 

[HiAI\_SingleOpBuffer](../../../modules/cann/document.md#hiai_singleopbuffer) \* [HMS\_HiAISingleOpTensor\_GetBuffer](../../../modules/cann/document.md#hms_hiaisingleoptensor_getbuffer) (const [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \*tensor)

 | 

Obtains the buffer of [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor).

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpTensor\_Destroy](../../../modules/cann/document.md#hms_hiaisingleoptensor_destroy) ([HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \*\*tensor)

 | 

Releases a [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) object.

 |
| 

[HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions) \* [HMS\_HiAISingleOpOptions\_Create](../../../modules/cann/document.md#hms_hiaisingleopoptions_create) (void)

 | 

Creates a [HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions) object.

 |
| 

void [HMS\_HiAISingleOpOptions\_Destroy](../../../modules/cann/document.md#hms_hiaisingleopoptions_destroy) ([HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions) \*\*options)

 | 

Releases a [HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions) object.

 |
| 

[HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor) \* [HMS\_HiAISingleOpDescriptor\_CreateConvolution](../../../modules/cann/document.md#hms_hiaisingleopdescriptor_createconvolution) ([HiAISingleOpDescriptor\_ConvolutionParam](../../structs/hiaisingleopdescriptor-convolutionparam/document.md) param)

 | 

Creates a descriptor object of a convolution class (common convolution, transposed convolution, and depthwise convolution).

 |
| 

[HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor) \* [HMS\_HiAISingleOpDescriptor\_CreateActivation](../../../modules/cann/document.md#hms_hiaisingleopdescriptor_createactivation) ([HiAI\_SingleOpActivationType](../../../modules/cann/document.md#hiai_singleopactivationtype) activationType, float coef)

 | 

Creates a descriptor object of the activation function class.

 |
| 

void [HMS\_HiAISingleOpDescriptor\_Destroy](../../../modules/cann/document.md#hms_hiaisingleopdescriptor_destroy) ([HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor) \*\*opDesc)

 | 

Releases a [HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor) object.

 |
| 

[HiAI\_SingleOpSupportStatus](../../../modules/cann/document.md#hiai_singleopsupportstatus) [HMS\_HiAISingleOpExecutor\_PreCheckConvolution](../../../modules/cann/document.md#hms_hiaisingleopexecutor_precheckconvolution) ([HiAI\_SingleOpExecutorConvolutionParam](../../structs/hiai-singleopexecutorconvolutionparam/document.md) param)

 | 

Pre-checks whether a convolution operation is supported or optimized.

 |
| 

[HiAI\_SingleOpSupportStatus](../../../modules/cann/document.md#hiai_singleopsupportstatus) [HMS\_HiAISingleOpExecutor\_PreCheckFusedConvolutionActivation](../../../modules/cann/document.md#hms_hiaisingleopexecutor_precheckfusedconvolutionactivation) ([HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md) param)

 | 

Pre-checks whether a fused convolution-and-activation operation is supported or optimized.

 |
| 

[HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) \* [HMS\_HiAISingleOpExecutor\_CreateConvolution](../../../modules/cann/document.md#hms_hiaisingleopexecutor_createconvolution) ([HiAI\_SingleOpExecutorConvolutionParam](../../structs/hiai-singleopexecutorconvolutionparam/document.md) param)

 | 

Creates a [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) object of a convolution operation.

 |
| 

[HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) \* [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](../../../modules/cann/document.md#hms_hiaisingleopexecutor_createfusedconvolutionactivation) ([HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md) param)

 | 

Creates a [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) object of the fused convolution-and-activation operation.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc](../../../modules/cann/document.md#hms_hiaisingleopexecutor_updateoutputtensordesc) (const [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) \*executor, uint32\_t index, [HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \*output)

 | 

Updates the output tensor description of [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor).

 |
| 

size\_t [HMS\_HiAISingleOpExecutor\_GetWorkspaceSize](../../../modules/cann/document.md#hms_hiaisingleopexecutor_getworkspacesize) (const [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) \*executor)

 | 

Queries the size (in bytes) of the ION workspace memory required by [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor).

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Init](../../../modules/cann/document.md#hms_hiaisingleopexecutor_init) ([HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) \*executor, void \*workspace, size\_t workspaceSize)

 | 

Loads [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor).

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Execute](../../../modules/cann/document.md#hms_hiaisingleopexecutor_execute) ([HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) \*executor, [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \*input\[\], int32\_t inputNum, [HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \*output\[\], int32\_t outputNum)

 | 

Performs synchronous inference.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Destroy](../../../modules/cann/document.md#hms_hiaisingleopexecutor_destroy) ([HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) \*\*executor)

 | 

Destroys the [HiAI\_SingleOpExecutor](../../../modules/cann/document.md#hiai_singleopexecutor) object to release the memory occupied by the executor.

 |
