# Connecting NNRt to an AI Inference Framework

#### When to Use

As a bridge between the AI inference engine and acceleration chip, Neural Network Runtime (NNRt) provides simplified native APIs for the AI inference engine to perform end-to-end inference through the acceleration chip.

This topic uses the Add single-operator model shown in Figure 1 as an example to describe the NNRt development process. The Add operator involves two inputs, one parameter, and one output. Wherein, the activation parameter is used to specify the type of the activation function in the Add operator.

**Figure 1** Add single-operator model

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/Oryq2GvRRMqxRSuMjzJwXA/en-us_image_0000002568765007.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=352BC5E15076FBBFB5AB2AE5D210D77DAFE74B6A38F39C2DA0B84F326387B042)

#### Preparing the Environment

## Environment Requirements

The environment requirements for NNRt are as follows:

-   Development environment: Ubuntu 18.04 or later.
-   Access device: a standard device whose built-in hardware accelerator driver has been connected to NNRt.

NNRt is opened to external systems through native APIs. Therefore, you need to download the corresponding SDK and build NNRt applications using the native development kit. You can use DevEco Studio to set up the environment and compile code.

## Environment Setup

1.  Start the Ubuntu server.
2.  Specify the native toolchain path for compilation.
3.  Download the required SDK. Specifically, choose **File** >\*\* Settings...\*\* on the DevEco Studio project page to navigate to the DevEco Studio installation directory, and search for the required SDK and download it to the local directory.

#### Available APIs

The following table lists the common APIs used in the NNRt development. For details, see [NeuralNetworkRuntime](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neuralnetworkruntime).

## Structs

| Name | Description |
| :-- | :-- |
| typedef struct OH\_NNModel OH\_NNModel | Model handle of NNRt. It is used to construct a model. |
| typedef struct OH\_NNCompilation OH\_NNCompilation | Compiler handle of NNRt. It is used to compile an AI model. |
| typedef struct OH\_NNExecutor OH\_NNExecutor | Executor handle of NNRt. It is used to perform inference computing on a specified device. |
| typedef struct NN\_QuantParam NN\_QuantParam | Quantization parameter handle, which is used to specify the quantization parameter of the tensor during model construction. |
| typedef struct NN\_TensorDesc NN\_TensorDesc | Tensor description handle, which is used to describe tensor attributes, such as the data format, data type, and shape. |
| typedef struct NN\_Tensor NN\_Tensor | Tensor handle, which is used to set the inference input and output tensors of the executor. |

## Model Construction APIs

| Name | Description |
| :-- | :-- |
| OH\_NNModel\_Construct() | Creates a model instance of the OH\_NNModel type. |
| OH\_NN\_ReturnCode OH\_NNModel\_AddTensorToModel(OH\_NNModel \*model, const NN\_TensorDesc \*tensorDesc) | Adds a tensor to a model instance. |
| OH\_NN\_ReturnCode OH\_NNModel\_SetTensorData(OH\_NNModel \*model, uint32\_t index, const void \*dataBuffer, size\_t length) | Sets the tensor value. |
| OH\_NN\_ReturnCode OH\_NNModel\_AddOperation(OH\_NNModel \*model, OH\_NN\_OperationType op, const OH\_NN\_UInt32Array \*paramIndices, const OH\_NN\_UInt32Array \*inputIndices, const OH\_NN\_UInt32Array \*outputIndices) | Adds an operator to a model instance. |
| OH\_NN\_ReturnCode OH\_NNModel\_SpecifyInputsAndOutputs(OH\_NNModel \*model, const OH\_NN\_UInt32Array \*inputIndices, const OH\_NN\_UInt32Array \*outputIndices) | Sets an index value for the input and output tensors of a model. |
| OH\_NN\_ReturnCode OH\_NNModel\_Finish(OH\_NNModel \*model) | Completes model composition. |
| void OH\_NNModel\_Destroy(OH\_NNModel \*\*model) | Destroys a model instance. |

## Model Compilation APIs

| Name | Description |
| :-- | :-- |
| OH\_NNCompilation \*OH\_NNCompilation\_Construct(const OH\_NNModel \*model) | Creates an **OH\_NNCompilation** instance based on the specified model instance. |
| OH\_NNCompilation \*OH\_NNCompilation\_ConstructWithOfflineModelFile(const char \*modelPath) | Creates an **OH\_NNCompilation** instance based on the specified offline model file path. |
| OH\_NNCompilation \*OH\_NNCompilation\_ConstructWithOfflineModelBuffer(const void \*modelBuffer, size\_t modelSize) | Creates an **OH\_NNCompilation** instance based on the specified offline model buffer. |
| OH\_NNCompilation \*OH\_NNCompilation\_ConstructForCache() | Creates an empty model building instance for later recovery from the model cache. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_ExportCacheToBuffer(OH\_NNCompilation \*compilation, const void \*buffer, size\_t length, size\_t \*modelSize) | Writes the model cache to the specified buffer. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_ImportCacheFromBuffer(OH\_NNCompilation \*compilation, const void \*buffer, size\_t modelSize) | Reads the model cache from the specified buffer. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_AddExtensionConfig(OH\_NNCompilation \*compilation, const char \*configName, const void \*configValue, const size\_t configValueSize) | Adds extended configurations for custom device attributes. For details about the extended attribute names and values, see the documentation that comes with the device. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetDevice(OH\_NNCompilation \*compilation, size\_t deviceID) | Sets the Device for model building and computing, which can be obtained through the device management APIs. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetCache(OH\_NNCompilation \*compilation, const char \*cachePath, uint32\_t version) | Sets the cache directory and version for model building. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetPerformanceMode(OH\_NNCompilation \*compilation, OH\_NN\_PerformanceMode performanceMode) | Sets the performance mode for model computing. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_SetPriority(OH\_NNCompilation \*compilation, OH\_NN\_Priority priority) | Sets the priority for model computing. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_EnableFloat16(OH\_NNCompilation \*compilation, bool enableFloat16) | Enables float16 for computing. |
| OH\_NN\_ReturnCode OH\_NNCompilation\_Build(OH\_NNCompilation \*compilation) | Performs model building. |
| void OH\_NNCompilation\_Destroy(OH\_NNCompilation \*\*compilation) | Destroys a model building instance. |

## Tensor Description APIs

| Name | Description |
| :-- | :-- |
| NN\_TensorDesc \*OH\_NNTensorDesc\_Create() | Creates an **NN\_TensorDesc** instance for creating an **NN\_Tensor** instance at a later time. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetName(NN\_TensorDesc \*tensorDesc, const char \*name) | Sets the name of the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetName(const NN\_TensorDesc \*tensorDesc, const char \*\*name) | Obtains the name of the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetDataType(NN\_TensorDesc \*tensorDesc, OH\_NN\_DataType dataType) | Sets the data type of the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetDataType(const NN\_TensorDesc \*tensorDesc, OH\_NN\_DataType \*dataType) | Obtains the data type of the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetShape(NN\_TensorDesc \*tensorDesc, const int32\_t \*shape, size\_t shapeLength) | Sets the shape of the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetShape(const NN\_TensorDesc \*tensorDesc, int32\_t \*\*shape, size\_t \*shapeLength) | Obtains the shape of the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_SetFormat(NN\_TensorDesc \*tensorDesc, OH\_NN\_Format format) | Sets the data format of the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetFormat(const NN\_TensorDesc \*tensorDesc, OH\_NN\_Format \*format) | Obtains the data format of the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetElementCount(const NN\_TensorDesc \*tensorDesc, size\_t \*elementCount) | Obtains the number of elements in the **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_GetByteSize(const NN\_TensorDesc \*tensorDesc, size\_t \*byteSize) | Obtains the number of bytes occupied by the tensor data obtained through calculation based on the shape and data type of an **NN\_TensorDesc** instance. |
| OH\_NN\_ReturnCode OH\_NNTensorDesc\_Destroy(NN\_TensorDesc \*\*tensorDesc) | Destroys an **NN\_TensorDesc** instance. |

## Tensor APIs

| Name | Description |
| :-- | :-- |
| NN\_Tensor\* OH\_NNTensor\_Create(size\_t deviceID, NN\_TensorDesc \*tensorDesc) | Creates an **NN\_Tensor** instance based on the specified tensor description. This API will request for device shared memory. |
| NN\_Tensor\* OH\_NNTensor\_CreateWithSize(size\_t deviceID, NN\_TensorDesc \*tensorDesc, size\_t size) | Creates an **NN\_Tensor** instance based on the specified memory size and tensor description. This API will request for device shared memory. |
| NN\_Tensor\* OH\_NNTensor\_CreateWithFd(size\_t deviceID, NN\_TensorDesc \*tensorDesc, int fd, size\_t size, size\_t offset) | Creates an **NN\_Tensor** instance based on the specified file descriptor of the shared memory and tensor description. This way, the device shared memory of other tensors can be reused. |
| NN\_TensorDesc\* OH\_NNTensor\_GetTensorDesc(const NN\_Tensor \*tensor) | Obtains the pointer to the **NN\_TensorDesc** instance in a tensor to read tensor attributes, such as the data type and shape. |
| void\* OH\_NNTensor\_GetDataBuffer(const NN\_Tensor \*tensor) | Obtains the memory address of tensor data to read or write tensor data. |
| OH\_NN\_ReturnCode OH\_NNTensor\_GetFd(const NN\_Tensor \*tensor, int \*fd) | Obtains the file descriptor of the shared memory where the tensor data is located. A file descriptor corresponds to a device shared memory block. |
| OH\_NN\_ReturnCode OH\_NNTensor\_GetSize(const NN\_Tensor \*tensor, size\_t \*size) | Obtains the size of the shared memory where tensor data is located. |
| OH\_NN\_ReturnCode OH\_NNTensor\_GetOffset(const NN\_Tensor \*tensor, size\_t \*offset) | Obtains the offset of the tensor data in the shared memory. The available size of the tensor data is the size of the shared memory minus the offset. |
| OH\_NN\_ReturnCode OH\_NNTensor\_Destroy(NN\_Tensor \*\*tensor) | Destroys an **NN\_Tensor** instance. |

## Inference APIs

| Name | Description |
| :-- | :-- |
| OH\_NNExecutor \*OH\_NNExecutor\_Construct(OH\_NNCompilation \*compilation) | Creates an **OH\_NNExecutor** instance. |
| OH\_NN\_ReturnCode OH\_NNExecutor\_GetOutputShape(OH\_NNExecutor \*executor, uint32\_t outputIndex, int32\_t \*\*shape, uint32\_t \*shapeLength) | Obtains the dimension information about the output tensor. This API is applicable only if the output tensor has a dynamic shape. |
| OH\_NN\_ReturnCode OH\_NNExecutor\_GetInputCount(const OH\_NNExecutor \*executor, size\_t \*inputCount) | Obtains the number of input tensors. |
| OH\_NN\_ReturnCode OH\_NNExecutor\_GetOutputCount(const OH\_NNExecutor \*executor, size\_t \*outputCount) | Obtains the number of output tensors. |
| NN\_TensorDesc\* OH\_NNExecutor\_CreateInputTensorDesc(const OH\_NNExecutor \*executor, size\_t index) | Creates an **NN\_TensorDesc** instance for an input tensor based on the specified index value. This instance will be used to read tensor attributes or create **NN\_Tensor** instances. |
| NN\_TensorDesc\* OH\_NNExecutor\_CreateOutputTensorDesc(const OH\_NNExecutor \*executor, size\_t index) | Creates an **NN\_TensorDesc** instance for an output tensor based on the specified index value. This instance will be used to read tensor attributes or create **NN\_Tensor** instances. |
| OH\_NN\_ReturnCode OH\_NNExecutor\_GetInputDimRange(const OH\_NNExecutor \*executor, size\_t index, size\_t \*\*minInputDims, size\_t \*\*maxInputDims, size\_t \*shapeLength) | Obtains the dimension range of all input tensors. If the input tensor has a dynamic shape, the dimension range supported by the tensor may vary according to device. |
| OH\_NN\_ReturnCode OH\_NNExecutor\_SetOnRunDone(OH\_NNExecutor \*executor, NN\_OnRunDone onRunDone) | Sets the callback function invoked when the asynchronous inference ends. For the definition of the callback function, see the API Reference. |
| OH\_NN\_ReturnCode OH\_NNExecutor\_SetOnServiceDied(OH\_NNExecutor \*executor, NN\_OnServiceDied onServiceDied) | Sets the callback function invoked when the device driver service terminates unexpectedly during asynchronous inference. For the definition of the callback function, see the API Reference. |
| OH\_NN\_ReturnCode OH\_NNExecutor\_RunSync(OH\_NNExecutor \*executor, NN\_Tensor \*inputTensor\[\], size\_t inputCount, NN\_Tensor \*outputTensor\[\], size\_t outputCount) | Performs synchronous inference. |
| OH\_NN\_ReturnCode OH\_NNExecutor\_RunAsync(OH\_NNExecutor \*executor, NN\_Tensor \*inputTensor\[\], size\_t inputCount, NN\_Tensor \*outputTensor\[\], size\_t outputCount, int32\_t timeout, void \*userData) | Performs asynchronous inference. |
| void OH\_NNExecutor\_Destroy(OH\_NNExecutor \*\*executor) | Destroys an **OH\_NNExecutor** instance. |

## Device Management APIs

| Name | Description |
| :-- | :-- |
| OH\_NN\_ReturnCode OH\_NNDevice\_GetAllDevicesID(const size\_t \*\*allDevicesID, uint32\_t \*deviceCount) | Obtains the ID of the device connected to NNRt. |
| OH\_NN\_ReturnCode OH\_NNDevice\_GetName(size\_t deviceID, const char \*\*name) | Obtains the name of the specified device. |
| OH\_NN\_ReturnCode OH\_NNDevice\_GetType(size\_t deviceID, OH\_NN\_DeviceType \*deviceType) | Obtains the type of the specified device. |

#### How to Develop

The development process of NNRt consists of three phases: model construction, model compilation, and inference execution. The following uses the Add single-operator model as an example to describe how to call NNRt APIs during application development.

1.  Create an application sample file.
    
    Create the source file of the NNRt application sample. Run the following commands in the project directory to create the nnrt\_example/ directory and create the nnrt\_example.cpp source file in the directory:
    
    mkdir ~/nnrt\_example && cd ~/nnrt\_example
    touch nnrt\_example.cpp
    
2.  Import the NNRt module.
    
    Add the following code at the beginning of the nnrt\_example.cpp file to import NNRt:
    
    #include <iostream>
    #include <cstdarg>
    #include "neural\_network\_runtime/neural\_network\_runtime.h"
    
3.  Define auxiliary functions, such as log printing, input data setting, and data printing.
    
    // Macro for checking the return value
    #define CHECKNEQ(realRet, expectRet, retValue, ...) \\
        do { \\
            if ((realRet) != (expectRet)) { \\
                printf(\_\_VA\_ARGS\_\_); \\
                return (retValue); \\
            } \\
        } while (0)
    
    #define CHECKEQ(realRet, expectRet, retValue, ...) \\
        do { \\
            if ((realRet) == (expectRet)) { \\
                printf(\_\_VA\_ARGS\_\_); \\
                return (retValue); \\
            } \\
        } while (0)
    
    // Set the input data for inference.
    OH\_NN\_ReturnCode SetInputData(NN\_Tensor\* inputTensor\[\], size\_t inputSize)
    {
        OH\_NN\_DataType dataType(OH\_NN\_FLOAT32);
        OH\_NN\_ReturnCode ret{OH\_NN\_FAILED};
        size\_t elementCount = 0;
        for (size\_t i = 0; i < inputSize; ++i) {
            // Obtain the data memory of the tensor.
            auto data = OH\_NNTensor\_GetDataBuffer(inputTensor\[i\]);
            CHECKEQ(data, nullptr, OH\_NN\_FAILED, "Failed to get data buffer.");
            // Obtain the tensor description.
            auto desc = OH\_NNTensor\_GetTensorDesc(inputTensor\[i\]);
            CHECKEQ(desc, nullptr, OH\_NN\_FAILED, "Failed to get desc.");
            // Obtain the data type of the tensor.
            ret = OH\_NNTensorDesc\_GetDataType(desc, &dataType);
            CHECKNEQ(ret, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Failed to get data type.");
            // Obtain the number of elements in the tensor.
            ret = OH\_NNTensorDesc\_GetElementCount(desc, &elementCount);
            CHECKNEQ(ret, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Failed to get element count.");
            switch(dataType) {
                case OH\_NN\_FLOAT32: {
                    float\* floatValue = reinterpret\_cast<float\*>(data);
                    for (size\_t j = 0; j < elementCount; ++j) {
                        floatValue\[j\] = static\_cast<float>(j);
                    }
                    break;
                }
                case OH\_NN\_INT32: {
                    int\* intValue = reinterpret\_cast<int\*>(data);
                    for (size\_t j = 0; j < elementCount; ++j) {
                        intValue\[j\] = static\_cast<int>(j);
                    }
                    break;
                }
                default:
                    return OH\_NN\_FAILED;
            }
        }
        return OH\_NN\_SUCCESS;
    }
    
    OH\_NN\_ReturnCode Print(NN\_Tensor\* outputTensor\[\], size\_t outputSize)
    {
        OH\_NN\_DataType dataType(OH\_NN\_FLOAT32);
        OH\_NN\_ReturnCode ret{OH\_NN\_FAILED};
        size\_t elementCount = 0;
        for (size\_t i = 0; i < outputSize; ++i) {
            auto data = OH\_NNTensor\_GetDataBuffer(outputTensor\[i\]);
            CHECKEQ(data, nullptr, OH\_NN\_FAILED, "Failed to get data buffer.");
            auto desc = OH\_NNTensor\_GetTensorDesc(outputTensor\[i\]);
            CHECKEQ(desc, nullptr, OH\_NN\_FAILED, "Failed to get desc.");
            ret = OH\_NNTensorDesc\_GetDataType(desc, &dataType);
            CHECKNEQ(ret, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Failed to get data type.");
            ret = OH\_NNTensorDesc\_GetElementCount(desc, &elementCount);
            CHECKNEQ(ret, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Failed to get element count.");
            switch(dataType) {
                case OH\_NN\_FLOAT32: {
                    float\* floatValue = reinterpret\_cast<float\*>(data);
                    for (size\_t j = 0; j < elementCount; ++j) {
                        std::cout << "Output index: " << j << ", value is: " << floatValue\[j\] << "." << std::endl;
                    }
                    break;
                }
                case OH\_NN\_INT32: {
                    int\* intValue = reinterpret\_cast<int\*>(data);
                    for (size\_t j = 0; j < elementCount; ++j) {
                        std::cout << "Output index: " << j << ", value is: " << intValue\[j\] << "." << std::endl;
                    }
                    break;
                }
                default:
                    return OH\_NN\_FAILED;
            }
        }
    
        return OH\_NN\_SUCCESS;
    }
    
4.  Construct a model.
    
    Use the model construction APIs to construct a single Add operator model.
    
    OH\_NN\_ReturnCode BuildModel(OH\_NNModel\*\* pmodel)
    {
        // Create a model instance and construct a model.
        OH\_NNModel\* model = OH\_NNModel\_Construct();
        CHECKEQ(model, nullptr, OH\_NN\_FAILED, "Create model failed.");
    
        // Add the first input tensor of the float32 type for the Add operator. The tensor shape is \[1, 2, 2, 3\].
        NN\_TensorDesc\* tensorDesc = OH\_NNTensorDesc\_Create();
        CHECKEQ(tensorDesc, nullptr, OH\_NN\_FAILED, "Create TensorDesc failed.");
    
        int32\_t inputDims\[4\] = {1, 2, 2, 3};
        auto returnCode = OH\_NNTensorDesc\_SetShape(tensorDesc, inputDims, 4);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc shape failed.");
    
        returnCode = OH\_NNTensorDesc\_SetDataType(tensorDesc, OH\_NN\_FLOAT32);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc data type failed.");
    
        returnCode = OH\_NNTensorDesc\_SetFormat(tensorDesc, OH\_NN\_FORMAT\_NONE);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc format failed.");
    
        returnCode = OH\_NNModel\_AddTensorToModel(model, tensorDesc);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Add first TensorDesc to model failed.");
    
        returnCode = OH\_NNModel\_SetTensorType(model, 0, OH\_NN\_TENSOR);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set model tensor type failed.");
    
        // Add the second input tensor of the float32 type for the Add operator. The tensor shape is \[1, 2, 2, 3\].
        tensorDesc = OH\_NNTensorDesc\_Create();
        CHECKEQ(tensorDesc, nullptr, OH\_NN\_FAILED, "Create TensorDesc failed.");
    
        returnCode = OH\_NNTensorDesc\_SetShape(tensorDesc, inputDims, 4);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc shape failed.");
    
        returnCode = OH\_NNTensorDesc\_SetDataType(tensorDesc, OH\_NN\_FLOAT32);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc data type failed.");
    
        returnCode = OH\_NNTensorDesc\_SetFormat(tensorDesc, OH\_NN\_FORMAT\_NONE);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc format failed.");
    
        returnCode = OH\_NNModel\_AddTensorToModel(model, tensorDesc);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Add second TensorDesc to model failed.");
    
        returnCode = OH\_NNModel\_SetTensorType(model, 1, OH\_NN\_TENSOR);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set model tensor type failed.");
    
        // Add the parameter tensor of the int8 type for the Add operator. The parameter tensor is used to specify the type of the activation function.
        tensorDesc = OH\_NNTensorDesc\_Create();
        CHECKEQ(tensorDesc, nullptr, OH\_NN\_FAILED, "Create TensorDesc failed.");
    
        int32\_t activationDims = 1;
        returnCode = OH\_NNTensorDesc\_SetShape(tensorDesc, &activationDims, 1);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc shape failed.");
    
        returnCode = OH\_NNTensorDesc\_SetDataType(tensorDesc, OH\_NN\_INT8);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc data type failed.");
    
        returnCode = OH\_NNTensorDesc\_SetFormat(tensorDesc, OH\_NN\_FORMAT\_NONE);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc format failed.");
    
        returnCode = OH\_NNModel\_AddTensorToModel(model, tensorDesc);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Add second TensorDesc to model failed.");
    
        returnCode = OH\_NNModel\_SetTensorType(model, 2, OH\_NN\_ADD\_ACTIVATIONTYPE);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set model tensor type failed.");
    
        // Set the type of the activation function to OH\_NN\_FUSED\_NONE, indicating that no activation function is added to the operator.
        int8\_t activationValue = OH\_NN\_FUSED\_NONE;
        returnCode = OH\_NNModel\_SetTensorData(model, 2, &activationValue, sizeof(int8\_t));
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set model tensor data failed.");
    
        // Add the output tensor of the float32 type for the Add operator. The tensor shape is \[1, 2, 2, 3\].
        tensorDesc = OH\_NNTensorDesc\_Create();
        CHECKEQ(tensorDesc, nullptr, OH\_NN\_FAILED, "Create TensorDesc failed.");
    
        returnCode = OH\_NNTensorDesc\_SetShape(tensorDesc, inputDims, 4);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc shape failed.");
    
        returnCode = OH\_NNTensorDesc\_SetDataType(tensorDesc, OH\_NN\_FLOAT32);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc data type failed.");
    
        returnCode = OH\_NNTensorDesc\_SetFormat(tensorDesc, OH\_NN\_FORMAT\_NONE);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set TensorDesc format failed.");
    
        returnCode = OH\_NNModel\_AddTensorToModel(model, tensorDesc);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Add forth TensorDesc to model failed.");
    
        returnCode = OH\_NNModel\_SetTensorType(model, 3, OH\_NN\_TENSOR);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Set model tensor type failed.");
    
        // Specify index values of the input tensor, parameter tensor, and output tensor for the Add operator.
        uint32\_t inputIndicesValues\[2\] = {0, 1};
        uint32\_t paramIndicesValues = 2;
        uint32\_t outputIndicesValues = 3;
        OH\_NN\_UInt32Array paramIndices = {&paramIndicesValues, 1};
        OH\_NN\_UInt32Array inputIndices = {inputIndicesValues, 2};
        OH\_NN\_UInt32Array outputIndices = {&outputIndicesValues, 1};
    
        // Add the Add operator to the model instance.
        returnCode = OH\_NNModel\_AddOperation(model, OH\_NN\_OPS\_ADD, &paramIndices, &inputIndices, &outputIndices);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Add operation to model failed.");
    
        // Set the index values of the input tensor and output tensor for the model instance.
        returnCode = OH\_NNModel\_SpecifyInputsAndOutputs(model, &inputIndices, &outputIndices);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Specify model inputs and outputs failed.");
    
        // Complete the model instance construction.
        returnCode = OH\_NNModel\_Finish(model);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "Build model failed.");
    
        // Return the model instance.
        \*pmodel = model;
        return OH\_NN\_SUCCESS;
    }
    
5.  Query the AI acceleration chips connected to NNRt.
    
    NNRt can connect to multiple AI acceleration chips through HDIs. Before model building, you need to query the AI acceleration chips connected to NNRt on the current device. Each AI acceleration chip has a unique ID. In the compilation phase, you need to specify the chip for model compilation based on the ID.
    
    void GetAvailableDevices(std::vector<size\_t>& availableDevice)
    {
        availableDevice.clear();
    
        // Obtain the available hardware IDs.
        const size\_t\* devices = nullptr;
        uint32\_t deviceCount = 0;
        OH\_NN\_ReturnCode ret = OH\_NNDevice\_GetAllDevicesID(&devices, &deviceCount);
        if (ret != OH\_NN\_SUCCESS) {
            std::cout << "GetAllDevicesID failed, get no available device." << std::endl;
            return;
        }
    
        for (uint32\_t i = 0; i < deviceCount; i++) {
            availableDevice.emplace\_back(devices\[i\]);
        }
    }
    
6.  Compile a model on the specified device.
    
    NNRt uses abstract model expressions to describe the topology structure of an AI model. Before inference execution on an AI acceleration chip, the build module provided by NNRt needs to deliver the abstract model expressions to the chip driver layer and convert the abstract model expressions into a format that supports inference and computing.
    
    OH\_NN\_ReturnCode CreateCompilation(OH\_NNModel\* model, const std::vector<size\_t>& availableDevice,
                                       OH\_NNCompilation\*\* pCompilation)
    {
        // Create an OH\_NNCompilation instance and pass the image composition model instance or the MindSpore Lite model instance to it.
        OH\_NNCompilation\* compilation = OH\_NNCompilation\_Construct(model);
        CHECKEQ(compilation, nullptr, OH\_NN\_FAILED, "OH\_NNCore\_ConstructCompilationWithNNModel failed.");
    
        // Set compilation options, such as the compilation hardware, cache path, performance mode, computing priority, and whether to enable float16 low-precision computing.
        // Choose to perform model compilation on the first device.
        auto returnCode = OH\_NNCompilation\_SetDevice(compilation, availableDevice\[0\]);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNCompilation\_SetDevice failed.");
    
        // Have the model compilation result cached in the /data/local/tmp directory, with the version number set to 1.
        returnCode = OH\_NNCompilation\_SetCache(compilation, "/data/local/tmp", 1);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNCompilation\_SetCache failed.");
    
        // Set the performance mode of the device.
        returnCode = OH\_NNCompilation\_SetPerformanceMode(compilation, OH\_NN\_PERFORMANCE\_EXTREME);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNCompilation\_SetPerformanceMode failed.");
    
        // Set the inference priority.
        returnCode = OH\_NNCompilation\_SetPriority(compilation, OH\_NN\_PRIORITY\_HIGH);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNCompilation\_SetPriority failed.");
    
        // Specify whether to enable FP16 computing.
        returnCode = OH\_NNCompilation\_EnableFloat16(compilation, false);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNCompilation\_EnableFloat16 failed.");
    
        // Perform model building
        returnCode = OH\_NNCompilation\_Build(compilation);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNCompilation\_Build failed.");
    
        \*pCompilation = compilation;
        return OH\_NN\_SUCCESS;
    }
    
7.  Create an executor.
    
    After the model building is complete, you need to call the NNRt execution module to create an executor. In the inference phase, operations such as setting the model input, obtaining the model output, and triggering inference computing are performed through the executor.
    
    OH\_NNExecutor\* CreateExecutor(OH\_NNCompilation\* compilation)
    {
        // Create an executor based on the specified OH\_NNCompilation instance.
        OH\_NNExecutor \*executor = OH\_NNExecutor\_Construct(compilation);
        CHECKEQ(executor, nullptr, nullptr, "OH\_NNExecutor\_Construct failed.");
        return executor;
    }
    
8.  Perform inference computing, and print the inference result.
    
    The input data required for inference computing is passed to the executor through the API provided by the execution module. This way, the executor is triggered to perform inference computing once to obtain and print the inference computing result.
    
    OH\_NN\_ReturnCode Run(OH\_NNExecutor\* executor, const std::vector<size\_t>& availableDevice)
    {
        // Obtain information about the input and output tensors from the executor.
        // Obtain the number of input tensors.
        size\_t inputCount = 0;
        auto returnCode = OH\_NNExecutor\_GetInputCount(executor, &inputCount);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNExecutor\_GetInputCount failed.");
        std::vector<NN\_TensorDesc\*> inputTensorDescs;
        NN\_TensorDesc\* tensorDescTmp = nullptr;
        for (size\_t i = 0; i < inputCount; ++i) {
            // Create the description of the input tensor.
            tensorDescTmp = OH\_NNExecutor\_CreateInputTensorDesc(executor, i);
            CHECKEQ(tensorDescTmp, nullptr, OH\_NN\_FAILED, "OH\_NNExecutor\_CreateInputTensorDesc failed.");
            inputTensorDescs.emplace\_back(tensorDescTmp);
        }
        // Obtain the number of output tensors.
        size\_t outputCount = 0;
        returnCode = OH\_NNExecutor\_GetOutputCount(executor, &outputCount);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNExecutor\_GetOutputCount failed.");
        std::vector<NN\_TensorDesc\*> outputTensorDescs;
        for (size\_t i = 0; i < outputCount; ++i) {
            // Create the description of the output tensor.
            tensorDescTmp = OH\_NNExecutor\_CreateOutputTensorDesc(executor, i);
            CHECKEQ(tensorDescTmp, nullptr, OH\_NN\_FAILED, "OH\_NNExecutor\_CreateOutputTensorDesc failed.");
            outputTensorDescs.emplace\_back(tensorDescTmp);
        }
    
        // Create input and output tensors.
        NN\_Tensor\* inputTensors\[inputCount\];
        NN\_Tensor\* tensor = nullptr;
        for (size\_t i = 0; i < inputCount; ++i) {
            tensor = nullptr;
            tensor = OH\_NNTensor\_Create(availableDevice\[0\], inputTensorDescs\[i\]);
            CHECKEQ(tensor, nullptr, OH\_NN\_FAILED, "OH\_NNTensor\_Create failed.");
            inputTensors\[i\] = tensor;
        }
        NN\_Tensor\* outputTensors\[outputCount\];
        for (size\_t i = 0; i < outputCount; ++i) {
            tensor = nullptr;
            tensor = OH\_NNTensor\_Create(availableDevice\[0\], outputTensorDescs\[i\]);
            CHECKEQ(tensor, nullptr, OH\_NN\_FAILED, "OH\_NNTensor\_Create failed.");
            outputTensors\[i\] = tensor;
        }
    
        // Set the data of the input tensor.
        returnCode = SetInputData(inputTensors, inputCount);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "SetInputData failed.");
    
        // Perform inference
        returnCode = OH\_NNExecutor\_RunSync(executor, inputTensors, inputCount, outputTensors, outputCount);
        CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNExecutor\_RunSync failed.");
    
        // Print the data of the output tensor.
        Print(outputTensors, outputCount);
    
        // Clear the input and output tensors and tensor description.
        for (size\_t i = 0; i < inputCount; ++i) {
            returnCode = OH\_NNTensor\_Destroy(&inputTensors\[i\]);
            CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNTensor\_Destroy failed.");
            returnCode = OH\_NNTensorDesc\_Destroy(&inputTensorDescs\[i\]);
            CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNTensorDesc\_Destroy failed.");
        }
        for (size\_t i = 0; i < outputCount; ++i) {
            returnCode = OH\_NNTensor\_Destroy(&outputTensors\[i\]);
            CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNTensor\_Destroy failed.");
            returnCode = OH\_NNTensorDesc\_Destroy(&outputTensorDescs\[i\]);
            CHECKNEQ(returnCode, OH\_NN\_SUCCESS, OH\_NN\_FAILED, "OH\_NNTensorDesc\_Destroy failed.");
        }
    
        return OH\_NN\_SUCCESS;
    }
    
9.  Build an end-to-end process from model construction to model compilation and execution.
    
    Steps 4 to 8 implement the model construction, compilation, and execution processes and encapsulates them into multiple functions to facilitate modular development. The following sample code demonstrates how to chain these functions into a complete NNRt workflow.
    
    int main(int argc, char\*\* argv)
    {
        OH\_NNModel\* model = nullptr;
        OH\_NNCompilation\* compilation = nullptr;
        OH\_NNExecutor\* executor = nullptr;
        std::vector<size\_t> availableDevices;
    
        // Construct a model.
        OH\_NN\_ReturnCode ret = BuildModel(&model);
        if (ret != OH\_NN\_SUCCESS) {
            std::cout << "BuildModel failed." << std::endl;
            OH\_NNModel\_Destroy(&model);
            return -1;
        }
    
        // Obtain the available devices.
        GetAvailableDevices(availableDevices);
        if (availableDevices.empty()) {
            std::cout << "No available device." << std::endl;
            OH\_NNModel\_Destroy(&model);
            return -1;
        }
    
        // Build the model.
        ret = CreateCompilation(model, availableDevices, &compilation);
        if (ret != OH\_NN\_SUCCESS) {
            std::cout << "CreateCompilation failed." << std::endl;
            OH\_NNModel\_Destroy(&model);
            OH\_NNCompilation\_Destroy(&compilation);
            return -1;
        }
    
        // Destroy the model instance.
        OH\_NNModel\_Destroy(&model);
    
        // Create an inference executor for the model.
        executor = CreateExecutor(compilation);
        if (executor == nullptr) {
            std::cout << "CreateExecutor failed, no executor is created." << std::endl;
            OH\_NNCompilation\_Destroy(&compilation);
            return -1;
        }
    
        // Destroy the model building instance.
        OH\_NNCompilation\_Destroy(&compilation);
    
        // Use the created executor to perform inference.
        ret = Run(executor, availableDevices);
        if (ret != OH\_NN\_SUCCESS) {
            std::cout << "Run failed." << std::endl;
            OH\_NNExecutor\_Destroy(&executor);
            return -1;
        }
    
        // Destroy the executor instance.
        OH\_NNExecutor\_Destroy(&executor);
    
        return 0;
    }
    

#### Verification

1.  Prepare the compilation configuration file of the application sample.
    
    Create a CMakeLists.txt file, and add compilation configurations to the application sample file nnrt\_example.cpp. The following is a simple example of the CMakeLists.txt file:
    
    cmake\_minimum\_required(VERSION 3.16)
    project(nnrt\_example C CXX)
    
    add\_executable(nnrt\_example
        ./nnrt\_example.cpp
    )
    
    target\_link\_libraries(nnrt\_example
        neural\_network\_runtime
        neural\_network\_core
    )
    
2.  Compile the application sample.
    
    Create the **build/** directory in the current directory, and compile nnrt\\\_example.cpp in the **build/** directory to obtain the binary file nnrt\\\_example:
    
    mkdir build && cd build
    cmake -DCMAKE\_TOOLCHAIN\_FILE={Path of the cross-compilation toolchain}/build/cmake/ohos.toolchain.cmake -DOHOS\_ARCH=arm64-v8a -DOHOS\_PLATFORM=OHOS -DOHOS\_STL=c++\_static ..
    make
    
3.  Push the application sample to the device for execution.
    
    \# Push the \`nnrt\_example\` obtained through compilation to the device, and execute it.
    hdc\_std file send ./nnrt\_example /data/local/tmp/.
    
    # Grant required permissions to the executable file of the test case.
    hdc\_std shell "chmod +x /data/local/tmp/nnrt\_example"
    
    # Execute the test case.
    hdc\_std shell "/data/local/tmp/nnrt\_example"
    
    If the execution is normal, information similar to the following is displayed:
    
    Output index: 0, value is: 0.000000.
    Output index: 1, value is: 2.000000.
    Output index: 2, value is: 4.000000.
    Output index: 3, value is: 6.000000.
    Output index: 4, value is: 8.000000.
    Output index: 5, value is: 10.000000.
    Output index: 6, value is: 12.000000.
    Output index: 7, value is: 14.000000.
    Output index: 8, value is: 16.000000.
    Output index: 9, value is: 18.000000.
    Output index: 10, value is: 20.000000.
    Output index: 11, value is: 22.000000.
    
4.  (Optional) Check the model cache.
    
    If the HDI service connected to NNRt supports the model cache function, you can find the generated cache file in the /data/local/tmp directory after the nnrt\_example is executed successfully.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/17/v3/nPuceJQ7RCe1r2jGUYr9pg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD522C4337AC32A00E71CFFB35541796B3C0B30D4775C4D699CF70184A9E7084)
    
    The IR graphs of the model need to be passed to the hardware driver layer, so that the HDI service compiles the IR graphs into a computing graph dedicated to hardware. The compilation process is time-consuming. The NNRt supports the computing graph cache feature. It can cache the computing graphs compiled by the HDI service to the device storage. If the same model is compiled on the same acceleration chip next time, you can specify the cache path so that NNRt can directly load the computing graphs in the cache file, reducing the compilation time.
    
    Check the cached files in the cache directory.
    
    ls /data/local/tmp
    
    The command output is as follows:
    
    \# 0.nncache 1.nncache 2.nncache cache\_info.nncache
    
    If the cache is no longer used, manually delete the cache files.
    
    rm /data/local/tmp/\*nncache
