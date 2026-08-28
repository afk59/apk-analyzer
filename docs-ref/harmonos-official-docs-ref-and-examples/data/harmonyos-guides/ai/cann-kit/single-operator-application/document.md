# Single-Operator Application

#### Overview

CANN Kit provides independent operator creation and computation pathways. Third-party frameworks can migrate operators like convolution and depthwise convolution to the NPU through a single-operator interfacing method during model loading and inference. Thanks to accelerated computing by the hardware platform, this approach offers greater flexibility compared to network-wide mode and delivers better performance than network-wide CPU computation.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/79wTM6KWQHafZaMqwAQ14Q/en-us_image_0000002528648517.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6B99E95E4923E18DB37FCEDFBD7C5A440165C9ECB27EBB48A9A74AB4123EA329 "Click to enlarge")

The following describes the APIs for creating a single-operator tensor, and creating, loading, and executing a single-operator executor. For details about how to use these APIs, please refer to [Development Procedure](#section1373122216206). To learn more setting and query APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit).

**Table 1** Single-operator APIs and functions
| 
API

 | 

Description

 |
| :-- | :-- |
| 

HiAI\_SingleOpTensorDesc \* HMS\_HiAISingleOpTensorDesc\_Create (const int64\_t \*dims, size\_t dimNum, HiAI\_SingleOpDataType dataType, HiAI\_SingleOpFormat format, bool isVirtual);

 | 

Creates a **HiAI\_SingleOpTensorDesc** object.

 |
| 

void HMS\_HiAISingleOpTensorDesc\_Destroy (HiAI\_SingleOpTensorDesc \*\*tensorDesc);

 | 

Releases a **HiAI\_SingleOpTensorDesc** object.

 |
| 

HiAI\_SingleOpBuffer \* HMS\_HiAISingleOpBuffer\_Create (size\_t dataSize);

 | 

Creates a **HiAI\_SingleOpBuffer** object based on the specified memory size.

 |
| 

size\_t HMS\_HiAISingleOpBuffer\_GetSize (const HiAI\_SingleOpBuffer \*buffer);

 | 

Queries the byte size of **HiAI\_SingleOpBuffer**.

 |
| 

void \* HMS\_HiAISingleOpBuffer\_GetData (const HiAI\_SingleOpBuffer \*buffer);

 | 

Queries the memory address of **HiAI\_SingleOpBuffer**.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAISingleOpBuffer\_Destroy (HiAI\_SingleOpBuffer \*\*buffer);

 | 

Releases a **HiAI\_SingleOpBuffer** object.

 |
| 

HiAI\_SingleOpTensor \* HMS\_HiAISingleOpTensor\_CreateFromTensorDesc (const HiAI\_SingleOpTensorDesc \*desc);

 | 

Creates a **HiAI\_SingleOpTensor** object based on **HiAI\_SingleOpTensorDesc**.

 |
| 

HiAI\_SingleOpTensor \* HMS\_HiAISingleOpTensor\_CreateFromConst (const HiAI\_SingleOpTensorDesc \*desc, void \*data, size\_t dataSize);

 | 

Creates a **HiAI\_SingleOpTensor** object based on **HiAI\_SingleOpTensorDesc** and the memory address and data size of constant data (such as convolution weight and bias).

 |
| 

HiAI\_SingleOpTensorDesc \* HMS\_HiAISingleOpTensor\_GetTensorDesc (const HiAI\_SingleOpTensor \*tensor);

 | 

Obtains the tensor description of **HiAI\_SingleOpTensor**.

 |
| 

HiAI\_SingleOpBuffer \* HMS\_HiAISingleOpTensor\_GetBuffer (const HiAI\_SingleOpTensor \*tensor);

 | 

Obtains the buffer of **HiAI\_SingleOpTensor**.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAISingleOpTensor\_Destroy (HiAI\_SingleOpTensor \*\*tensor);

 | 

Releases a **HiAI\_SingleOpTensor** object.

 |
| 

HiAI\_SingleOpOptions \* HMS\_HiAISingleOpOptions\_Create (void);

 | 

Creates a **HiAI\_SingleOpOptions** object.

 |
| 

void HMS\_HiAISingleOpOptions\_Destroy (HiAI\_SingleOpOptions \*\*options);

 | 

Releases a **HiAI\_SingleOpOptions** object.

 |
| 

HiAI\_SingleOpDescriptor\* HMS\_HiAISingleOpDescriptor\_CreateConvolution(HiAISingleOpDescriptor\_ConvolutionParam param);

 | 

Creates a descriptor object of a convolution operator (common convolution, transposed convolution, and depthwise convolution).

 |
| 

void HMS\_HiAISingleOpDescriptor\_Destroy (HiAI\_SingleOpDescriptor \*\*opDesc);

 | 

Releases a **HiAI\_SingleOpDescriptor** object.

 |
| 

HiAI\_SingleOpExecutor\* HMS\_HiAISingleOpExecutor\_CreateConvolution(HiAI\_SingleOpExecutorConvolutionParam param);

 | 

Creates a **HiAI\_SingleOpExecutor** object for a convolution operator.

 |
| 

size\_t HMS\_HiAISingleOpExecutor\_GetWorkspaceSize (const HiAI\_SingleOpExecutor \*executor);

 | 

Obtains the size (in bytes) of the ION memory workspace required by **HiAI\_SingleOpExecutor**.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Init (HiAI\_SingleOpExecutor \*executor, void \*workspace, size\_t workspaceSize);

 | 

Loads **HiAI\_SingleOpExecutor**.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Execute (HiAI\_SingleOpExecutor \*executor, HiAI\_SingleOpTensor \*input\[\], int32\_t inputNum, HiAI\_SingleOpTensor \*output\[\], int32\_t outputNum);

 | 

Performs synchronous inference.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Destroy (HiAI\_SingleOpExecutor \*\*executor);

 | 

Destroys **HiAI\_SingleOpExecutor** object to release the memory occupied by the executor.

 |

#### Development Procedure

The following uses a single convolution operator as an example.

1.  Create a single-operator executor.
    
    1.  Call [HMS\_HiAISingleOpOptions\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopoptions_create) to create an object for configuring the single operator.
    2.  Call [HMS\_HiAISingleOpDescriptor\_CreateConvolution](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopdescriptor_createconvolution) to create a descriptor object for the convolution operator.
    3.  Call [HMS\_HiAISingleOpTensor\_CreateFromConst](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleoptensor_createfromconst) to create the weight single-operator tensor and bias single-operator tensor for the convolution operator.
    4.  Call [HMS\_HiAISingleOpTensorDesc\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleoptensordesc_create) to create the description objects for the single operator's input tensor and output tensor.
    5.  Call [HMS\_HiAISingleOpExecutor\_CreateConvolution](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_createconvolution) to create a single-operator executor, by passing the convolution operator's descriptor object, weight tensor, bias tensor, as well as the input tensor description and output tensor description.
        
        To create a fused operator executor for the convolution operator and activation operator, call [HMS\_HiAISingleOpDescriptor\_CreateActivation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopdescriptor_createactivation) to create a descriptor object for the activation operator, then call [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_createfusedconvolutionactivation) to create a fused operator executor.
        
    
    6.  Call [HMS\_HiAISingleOpDescriptor\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopdescriptor_destroy) to release the descriptor object and call [HMS\_HiAISingleOpOptions\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopoptions_destroy) to release the object used for configuring the single operator.
    
2.  Create an input/output tensor.
    
    1.  Call [HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleoptensor_createfromtensordesc) to create an input tensor and an output tensor for the single operator.
    2.  Call [HMS\_HiAISingleOpTensorDesc\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleoptensordesc_destroy) to release the tensor descriptor object.
    3.  Call [HMS\_HiAISingleOpTensor\_GetBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleoptensor_getbuffer) to obtain the internal buffer object of the input/output tensor.
    4.  Call [HMS\_HiAISingleOpBuffer\_GetData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopbuffer_getdata) to obtain the allocated input/output ION memory address. The address can be used to write the input and read the output of a single operator during network-wide model inference.
    
3.  Load the single-operator executor.
    
    1.  Call [HMS\_HiAISingleOpExecutor\_GetWorkspaceSize](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_getworkspacesize) to obtain the size of the ION memory workspace required by the single-operator executor for inference computation.
    2.  Call [HMS\_HiAISingleOpBuffer\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopbuffer_create) to create sufficient workspace based on the size of the ION memory workspace required by the single-operator executor.
    3.  Call [HMS\_HiAISingleOpBuffer\_GetData](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopbuffer_getdata) to obtain the address of the allocated ION memory workspace.
    4.  Call [HMS\_HiAISingleOpExecutor\_Init](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_init) to load the single-operator executor using the workspace address and size.
    
4.  Perform the inference.
    
    Call [HMS\_HiAISingleOpExecutor\_Execute](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_execute) to perform synchronous inference.
    
5.  Uninstall the single-operator executor to release resources.
    
    -   Call [HMS\_HiAISingleOpTensor\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleoptensor_destroy) to release the input and output tensor objects.
    -   Call [HMS\_HiAISingleOpBuffer\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopbuffer_destroy) to release the workspace.
    -   Call [HMS\_HiAISingleOpExecutor\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaisingleopexecutor_destroy) to release the executor object.
    

#### Example

Assuming there is a deep convolution operator with input dimensions of 1x8x224x224 and float32 input data arranged in NCHW format. After preparing the weight and bias data in NCHW format, you can refer to the following sample code for using the single-operator API to perform inference and obtain the float32 output in NCHW format:

#include "CANNKit/hiai\_single\_op.h"
#include <cstdio>
#include <cstdlib>
#include <cstring>
// Example operator parameters
// Single-operator convolution mode.
HiAI\_SingleOpConvMode convMode = HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE;
int64\_t strides\[2\] = {1, 1};
int64\_t dilations\[2\] = {1, 1};
int64\_t pads\[4\] = {0, 0, 0, 0};
int64\_t groups = 1;
// Single-operator padding mode.
HiAI\_SingleOpPadMode padMode = HIAI\_SINGLEOP\_PAD\_MODE\_SAME;
int64\_t filterDims\[4\] = {8, 1, 3, 3};
size\_t filterDataSize = 8 \* 1 \* 3 \* 3 \* sizeof(float);
void\* filterData = malloc(filterDataSize);
int64\_t biasDims\[1\] = {8};
size\_t biasDataSize = 8 \* sizeof(float);
void\* biasData = malloc(biasDataSize);
int64\_t inputDims\[4\] = {1, 8, 224, 224};
HiAI\_SingleOpDataType inputDataType = HIAI\_SINGLEOP\_DT\_FLOAT;
// Single operator tensor layout format.
HiAI\_SingleOpFormat inputFormat = HIAI\_SINGLEOP\_FORMAT\_NCHW;
bool inputIsVirtual = false;
// If the operator's output data type and layout format are not specified, set the data type to **HIAI\_SINGLEOP\_DT\_UNDEFINED** and the layout format to **HIAI\_SINGLEOP\_FORMAT\_RESERVED**.
// After creating a single operator, call **HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc** to update the output tensor description to the optimal data type and layout format suited for the hardware.
int64\_t outputDims\[4\] = {1, 8, 224, 224};
HiAI\_SingleOpDataType outputDataType = HIAI\_SINGLEOP\_DT\_FLOAT;
HiAI\_SingleOpFormat outputFormat = HIAI\_SINGLEOP\_FORMAT\_NCHW;
bool outputIsVirtual = false;

// Create a single-operator executor.
HiAI\_SingleOpOptions\* options = HMS\_HiAISingleOpOptions\_Create();
HiAISingleOpDescriptor\_ConvolutionParam convOpDescCreateParam = {convMode, {0}, {0}, {0}, groups, padMode};
memcpy(convOpDescCreateParam.strides, strides, 2 \* sizeof(int64\_t));
memcpy(convOpDescCreateParam.dilations, dilations, 2 \* sizeof(int64\_t));
memcpy(convOpDescCreateParam.pads, pads, 4 \* sizeof(int64\_t));
// Create a descriptor object for the convolution class.
HiAI\_SingleOpDescriptor\* convOpDesc = HMS\_HiAISingleOpDescriptor\_CreateConvolution(convOpDescCreateParam);
// Create a single-operator tensor descriptor object based on the dimensions, data type, and format.
HiAI\_SingleOpTensorDesc\* filterDesc = HMS\_HiAISingleOpTensorDesc\_Create(filterDims, 4, HIAI\_SINGLEOP\_DT\_FLOAT, HIAI\_SINGLEOP\_FORMAT\_NCHW, false);
// Create a single operator tensor object.
HiAI\_SingleOpTensor\* filter = HMS\_HiAISingleOpTensor\_CreateFromConst(filterDesc, filterData, filterDataSize);
HiAI\_SingleOpTensorDesc\* biasDesc = HMS\_HiAISingleOpTensorDesc\_Create(biasDims, 1, HIAI\_SINGLEOP\_DT\_FLOAT, HIAI\_SINGLEOP\_FORMAT\_NCHW, false);
HiAI\_SingleOpTensor\* bias = HMS\_HiAISingleOpTensor\_CreateFromConst(biasDesc, biasData, biasDataSize);
HiAI\_SingleOpTensorDesc\* inputDesc = HMS\_HiAISingleOpTensorDesc\_Create(inputDims, 4, inputDataType, inputFormat, inputIsVirtual);
HiAI\_SingleOpTensorDesc\* outputDesc = HMS\_HiAISingleOpTensorDesc\_Create(outputDims, 4, outputDataType, outputFormat, outputIsVirtual);
// Construct the parameters for the single operator convolution executor.
HiAI\_SingleOpExecutorConvolutionParam executorCreateParam = {options, convOpDesc, inputDesc, outputDesc, filter, bias};
// Create the single-operator convolution executor.
HiAI\_SingleOpExecutor\* executor = HMS\_HiAISingleOpExecutor\_CreateConvolution(executorCreateParam);
if (executor == nullptr) {
    printf("HMS\_HiAISingleOp executor create failed. \\n");
}
// It is recommended that unnecessary resources be destroyed in a timely manner.
HMS\_HiAISingleOpTensorDesc\_Destroy(&filterDesc);
HMS\_HiAISingleOpTensorDesc\_Destroy(&biasDesc);
HMS\_HiAISingleOpOptions\_Destroy(&options);
HMS\_HiAISingleOpDescriptor\_Destroy(&convOpDesc);
OH\_NN\_ReturnCode ret = HMS\_HiAISingleOpTensor\_Destroy(&filter);
if (ret != OH\_NN\_SUCCESS) {
    printf("HMS\_HiAISingleOp filter destroy failed.\\n");
}
ret = HMS\_HiAISingleOpTensor\_Destroy(&bias);
if (ret != OH\_NN\_SUCCESS) {
    printf("HMS\_HiAISingleOp bias destroy failed.\\n");
}

// Create an input/output tensor.
HiAI\_SingleOpTensor\* input = HMS\_HiAISingleOpTensor\_CreateFromTensorDesc(inputDesc);
HMS\_HiAISingleOpTensorDesc\_Destroy(&inputDesc);
HiAI\_SingleOpTensor\* output = HMS\_HiAISingleOpTensor\_CreateFromTensorDesc(outputDesc);
HMS\_HiAISingleOpTensorDesc\_Destroy(&outputDesc);
// The input and output tensors of the single operator must use ION memory to reduce copy overhead.
// After the input tensor is successfully created, you can use the following method to obtain the ION memory address in the input tensor for input data filling.
// This method also applies for obtaining the ION memory address in the output tensor, which is used to read the output data after the inference and computation are successful.
HiAI\_SingleOpBuffer\* inputBuffer = HMS\_HiAISingleOpTensor\_GetBuffer(input);
void\* inputData = HMS\_HiAISingleOpBuffer\_GetData(inputBuffer);
size\_t inputDataSize = HMS\_HiAISingleOpBuffer\_GetSize(inputBuffer);
memset(inputData, 0, inputDataSize);

// Obtain the size (in bytes) of the ION memory workspace required for the single-operator executor.
size\_t workspaceSize = HMS\_HiAISingleOpExecutor\_GetWorkspaceSize(executor);
// If there are multiple single-operator executors, the workspace memory of each executor can be reused. You only need to apply for the maximum workspace required.
HiAI\_SingleOpBuffer\* workspaceBuffer = HMS\_HiAISingleOpBuffer\_Create(workspaceSize);
void\* workspace = HMS\_HiAISingleOpBuffer\_GetData(workspaceBuffer);
ret = HMS\_HiAISingleOpExecutor\_Init(executor, workspace, workspaceSize);
if (ret != OH\_NN\_SUCCESS) {
    printf("HMS\_HiAISingleOp executor init failed.\\n");
}

// Perform the inference.
HiAI\_SingleOpTensor\* inputs\[\] = {input};
HiAI\_SingleOpTensor\* outputs\[\] = {output};
ret = HMS\_HiAISingleOpExecutor\_Execute(executor, inputs, 1, outputs, 1);
if (ret != OH\_NN\_SUCCESS) {
    printf("HMS\_HiAISingleOp executor execute failed.\\n");
}

// Uninstall the single-operator executor to release resources.
ret = HMS\_HiAISingleOpTensor\_Destroy(&input);
if (ret != OH\_NN\_SUCCESS) {
    printf("HMS\_HiAISingleOp input destroy failed.\\n");
}
ret = HMS\_HiAISingleOpTensor\_Destroy(&output);
if (ret != OH\_NN\_SUCCESS) {
    printf("HMS\_HiAISingleOp output destroy failed.\\n");
}
ret = HMS\_HiAISingleOpBuffer\_Destroy(&workspaceBuffer);
if (ret != OH\_NN\_SUCCESS) {
    printf("HMS\_HiAISingleOp workspaceBuffer destroy failed.\\n");
}
ret = HMS\_HiAISingleOpExecutor\_Destroy(&executor);
if (ret != OH\_NN\_SUCCESS) {
    printf("HMS\_HiAISingleOp executor destroy failed.\\n");
}
free(filterData);
free(biasData);
