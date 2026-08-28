# Model Inference

#### Basic Concepts

Model inference includes model compilation and inference, which is the basics for other extended and enhanced functions.

#### Process

The following figure shows the model inference process:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8a/v3/nB2ljJicTEuZUMAGUNDgEw/en-us_image_0000002528408539.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=ED6E6C07B1BC3CB84940E897FCAEDD8491D4C30D052F48434E09674CCBCA9F09 "Click to enlarge")

#### API Description

The following only lists major APIs in the process. To learn more configurations for compilation, loading, and execution, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit).

**Table 1** Model inference APIs in CANN Kit
| 
API

 | 

Description

 |
| :-- | :-- |
| 

OH\_NNCompilation\* OH\_NNCompilation\_ConstructWithOfflineModelBuffer(const void \*modelBuffer, size\_t modelSize);

 | 

Creates a model compilation instance based on the model buffer.

 |
| 

OH\_NN\_ReturnCode OH\_NNCompilation\_SetDevice(OH\_NNCompilation \*compilation, size\_t deviceID);

 | 

Sets the target device for model compilation and execution.

 |
| 

OH\_NN\_ReturnCode OH\_NNCompilation\_Build(OH\_NNCompilation \*compilation);

 | 

Compiles the model. The generated model is saved in **compilation**.

 |
| 

OH\_NNExecutor\* OH\_NNExecutor\_Construct(OH\_NNCompilation \*compilation);

 | 

Creates an executor for model inference based on the compiled model.

 |
| 

NN\_Tensor\* OH\_NNTensor\_Create(size\_t deviceID, NN\_TensorDesc\* tensorDesc);

 | 

Constructs the input and output tensors.

 |
| 

OH\_NN\_ReturnCode OH\_NNExecutor\_RunSync(OH\_NNExecutor \*executor, NN\_Tensor \*inputTensor\[\], size\_t inputCount, NN\_Tensor \*outputTensor\[\], size\_t outputCount);

 | 

Performs synchronous model inference.

 |
| 

void OH\_NNCompilation\_Destroy(OH\_NNCompilation \*\*compilation);

 | 

Destroys the model compilation instance.

 |
| 

OH\_NN\_ReturnCode OH\_NNTensor\_Destroy(NN\_Tensor\*\* tensor);

 | 

Destroys the input and output tensors.

 |
| 

void OH\_NNExecutor\_Destroy(OH\_NNExecutor \*\*executor);

 | 

Destroys the executor of model inference.

 |

#### Development Procedure

The following describes the main development procedure for model inference. For details, please refer to the [sample code](https://gitcode.com/HarmonyOS_Samples/cannkit-samplecode-clientdemo-cpp).

1.  Prepare the model and development environment.
    
    -   Prepare the OM model, which can be generated using the tools\_omg tool or obtained from [Model Zoo](../../model-optimization/model-zoo/document.md).
    -   Download and configure the [DevEco Studio](https://developer.huawei.com/consumer/en/deveco-studio/) environment for developing and debugging a HarmonyOS app.
    

2.  [Create a DevEco Studio project](../app-integration/creating-a-project/document.md).

3.  Create a model compilation instance.
    
    Call [OH\_NNCompilation\_ConstructWithOfflineModelBuffer](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_constructwithofflinemodelbuffer) to read the model buffer and create a model compilation instance. Alternatively, call [OH\_NNCompilation\_ConstructWithOfflineModelFile](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_constructwithofflinemodelfile) to directly read the model file and create a model compilation instance.
    
4.  Select the target device.
    
    Call [OH\_NNDevice\_GetAllDevicesID](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nndevice_getalldevicesid) to obtain all device IDs, search for the device named "HIAI\_F", record its device ID, and set it to the compilation instance created in [Step 3](#li810206624) through [OH\_NNCompilation\_SetDevice](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_setdevice).
    

5.  Perform model compilation.
    
    Call [OH\_NNCompilation\_Build](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_build) and pass the model compilation instance created in [Step 3](#li810206624) to compile the model. The compiled model data is still stored in the model compilation instance.
    

6.  Create a model executor.
    
    Call [OH\_NNExecutor\_Construct](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nnexecutor_construct) to create an executor instance for the compiled model. After the executor is created, call [OH\_NNCompilation\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_destroy) to destroy the model compilation instance.
    

7.  Construct the input and output tensors.
    
    Call [OH\_NNExecutor\_GetInputCount](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nnexecutor_getinputcount) to query the number of inputs, obtain **TensorDesc** with a specific index by calling [OH\_NNExecutor\_CreateInputTensorDesc](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nnexecutor_createinputtensordesc), and create a tensor based on **TensorDesc** by calling [OH\_NNTensor\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nntensor_create). Then, you'll be able to write data to the tensor. Repeat these steps to construct output tensors.
    

8.  Perform model inference.
    
    Call [OH\_NNExecutor\_RunSync](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nnexecutor_runsync) to perform synchronous model inference. The model's output data is stored in **outputTensors**. Process the output data as required to obtain the expected result.
    

9.  Destroy the instance.
    
    -   Call [OH\_NNExecutor\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nnexecutor_destroy) to destroy the model executor instance.
    -   Call [OH\_NNTensor\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neural-network-core-h#oh_nntensor_destroy) to destroy the input and output tensors.
