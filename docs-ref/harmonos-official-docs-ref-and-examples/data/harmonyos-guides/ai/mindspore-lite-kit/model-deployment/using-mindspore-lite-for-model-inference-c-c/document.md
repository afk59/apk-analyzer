# Using MindSpore Lite for Model Inference (C/C++)

#### When to Use

MindSpore Lite is an AI engine that provides AI model inference for different hardware devices. It has been used in a wide range of fields, such as image classification, target recognition, facial recognition, and character recognition.

This document describes the general development process for MindSpore Lite model inference.

#### Basic Concepts

Before getting started, you need to understand the following basic concepts:

**Tensor**: a special data structure that is similar to arrays and matrices. It is basic data structure used in MindSpore Lite network operations.

**Float16 inference mode**: an inference mode in half-precision format, where a number is represented with 16 bits.

#### Available APIs

APIs involved in MindSpore Lite model inference are categorized into context APIs, model APIs, and tensor APIs. For details about the APIs, see [MindSpore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-mindspore).

## Context APIs

| API | Description |
| :-- | :-- |
| OH\_AI\_ContextHandle OH\_AI\_ContextCreate() | Creates a context object. This API must be used together with **OH\_AI\_ContextDestroy**. |
| void OH\_AI\_ContextSetThreadNum(OH\_AI\_ContextHandle context, int32\_t thread\_num) | Sets the number of runtime threads. |
| void OH\_AI\_ContextSetThreadAffinityMode(OH\_AI\_ContextHandle context, int mode) | Sets the affinity mode for binding runtime threads to CPU cores, which are classified into large, medium, and small cores based on the CPU frequency. You only need to bind the large or medium cores, but not small cores. |
| OH\_AI\_DeviceInfoHandle OH\_AI\_DeviceInfoCreate(OH\_AI\_DeviceType device\_type) | Creates a runtime device information object. |
| void OH\_AI\_ContextDestroy(OH\_AI\_ContextHandle \*context) | Destroys a context object. |
| void OH\_AI\_DeviceInfoSetEnableFP16(OH\_AI\_DeviceInfoHandle device\_info, bool is\_fp16) | Sets whether to enable float16 inference. This function is available only for CPU and GPU devices. |
| void OH\_AI\_ContextAddDeviceInfo(OH\_AI\_ContextHandle context, OH\_AI\_DeviceInfoHandle device\_info) | Adds a runtime device information object. |

## Model APIs

| API | Description |
| :-- | :-- |
| OH\_AI\_ModelHandle OH\_AI\_ModelCreate() | Creates a model object. |
| OH\_AI\_Status OH\_AI\_ModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path,OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context) | Loads and builds a MindSpore Lite model from a model file. |
| void OH\_AI\_ModelDestroy(OH\_AI\_ModelHandle \*model) | Destroys a model object. |

## Tensor APIs

| API | Description |
| :-- | :-- |
| OH\_AI\_TensorHandleArray OH\_AI\_ModelGetInputs(const OH\_AI\_ModelHandle model) | Obtains the input tensor array structure of a model. |
| int64\_t OH\_AI\_TensorGetElementNum(const OH\_AI\_TensorHandle tensor) | Obtains the number of tensor elements. |
| const char \*OH\_AI\_TensorGetName(const OH\_AI\_TensorHandle tensor) | Obtains the name of a tensor. |
| OH\_AI\_DataType OH\_AI\_TensorGetDataType(const OH\_AI\_TensorHandle tensor) | Obtains the tensor data type. |
| void \*OH\_AI\_TensorGetMutableData(const OH\_AI\_TensorHandle tensor) | Obtains the pointer to mutable tensor data. |

#### How to Develop

The following figure shows the development process for MindSpore Lite model inference.

**Figure 1** Development process for MindSpore Lite model inference

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2c/v3/l0tBQZS5Rb29eFhaivHYQQ/en-us_image_0000002537765276.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7C7BDB31F9A9850E5739F763EC97FC806C12B60A25E32ECA69428C38DA497FB3)

Before moving to the development process, you need to reference related header files and compile functions to generate random input. The sample code is as follows:

#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>
#include "mindspore/model.h"

// Generate random input.
int GenerateInputDataWithRandom(OH\_AI\_TensorHandleArray inputs) {
  for (size\_t i = 0; i < inputs.handle\_num; ++i) {
    float \*input\_data = (float \*)OH\_AI\_TensorGetMutableData(inputs.handle\_list\[i\]);
    if (input\_data == NULL) {
      printf("MSTensorGetMutableData failed.\\n");
      return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    int64\_t num = OH\_AI\_TensorGetElementNum(inputs.handle\_list\[i\]);
    const int divisor = 10;
    for (size\_t j = 0; j < num; j++) {
      input\_data\[j\] = (float)(rand() % divisor) / divisor;  // 0--0.9f
    }
  }
  return OH\_AI\_STATUS\_SUCCESS;
}

The development process consists of the following main steps:

1.  Prepare the required model.
    
    The required model can be downloaded directly or obtained using the model conversion tool.
    
    -   If the downloaded model is in the .ms format, you can use it directly for inference. The following uses the **mobilenetv2.ms** model as an example.
    -   If the downloaded model uses a third-party framework, such as TensorFlow, TensorFlow Lite, Caffe, or ONNX, you can use the [model conversion tool](https://www.mindspore.cn/lite/docs/en/master/use/downloads.html#2-3-0) to convert it to the .ms format.
2.  Create a context, and set parameters such as the number of runtime threads and device type.
    
    The following describes two typical scenarios:
    
    Scenario 1: Only the CPU inference context is created.
    
    // Create a context, and set the number of runtime threads to 2 and the thread affinity mode to 1 (big cores first).
    OH\_AI\_ContextHandle context = OH\_AI\_ContextCreate();
    if (context == NULL) {
      printf("OH\_AI\_ContextCreate failed.\\n");
      return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    const int thread\_num = 2;
    OH\_AI\_ContextSetThreadNum(context, thread\_num);
    OH\_AI\_ContextSetThreadAffinityMode(context, 1);
    // Set the device type to CPU, and disable Float16 inference.
    OH\_AI\_DeviceInfoHandle cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
    if (cpu\_device\_info == NULL) {
      printf("OH\_AI\_DeviceInfoCreate failed.\\n");
      OH\_AI\_ContextDestroy(&context);
      return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    OH\_AI\_DeviceInfoSetEnableFP16(cpu\_device\_info, false);
    OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);
    
    Scenario 2: The neural network runtime (NNRT) and CPU heterogeneous inference contexts are created.
    
    NNRT is the runtime for cross-chip inference computing in the AI field. Generally, the acceleration hardware connected to NNRT, such as the NPU, has strong inference capabilities but supports only a limited number of operators, whereas the general-purpose CPU has weak inference capabilities but supports a wide range of operators. MindSpore Lite supports NNRT and CPU heterogeneous inference. Model operators are preferentially scheduled to NNRT for inference. If certain operators are not supported by NNRT, then they are scheduled to the CPU for inference. The following is the sample code for configuring NNRT/CPU heterogeneous inference:
    
    // Create a context, and set the number of runtime threads to 2 and the thread affinity mode to 1 (big cores first).
    OH\_AI\_ContextHandle context = OH\_AI\_ContextCreate();
    if (context == NULL) {
      printf("OH\_AI\_ContextCreate failed.\\n");
      return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    // Preferentially use NNRT inference.
    // Use the NNRT hardware of the first ACCELERATORS class to create the NNRT device information and configure the high-performance inference mode for the NNRT hardware. You can also use OH\_AI\_GetAllNNRTDeviceDescs() to obtain the list of NNRT devices in the current environment, search for a specific device by device name or type, and use the device as the NNRT inference hardware.
    OH\_AI\_DeviceInfoHandle nnrt\_device\_info = OH\_AI\_CreateNNRTDeviceInfoByType(OH\_AI\_NNRTDEVICE\_ACCELERATOR);
    if (nnrt\_device\_info == NULL) {
      printf("OH\_AI\_DeviceInfoCreate failed.\\n");
      OH\_AI\_ContextDestroy(&context);
      return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    OH\_AI\_DeviceInfoSetPerformanceMode(nnrt\_device\_info, OH\_AI\_PERFORMANCE\_HIGH);
    OH\_AI\_ContextAddDeviceInfo(context, nnrt\_device\_info);
    
    // Configure CPU inference.
    OH\_AI\_DeviceInfoHandle cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
    if (cpu\_device\_info == NULL) {
      printf("OH\_AI\_DeviceInfoCreate failed.\\n");
      OH\_AI\_ContextDestroy(&context);
      return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);
    
3.  Create, load, and build the model.
    
    Call **OH\_AI\_ModelBuildFromFile** to load and build the model.
    
    In this example, the **argv\[1\]** parameter passed to **OH\_AI\_ModelBuildFromFile** indicates the specified model file path.
    
    // Create a model.
    OH\_AI\_ModelHandle model = OH\_AI\_ModelCreate();
    if (model == NULL) {
      printf("OH\_AI\_ModelCreate failed.\\n");
      OH\_AI\_ContextDestroy(&context);
      return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    
    // Load and build the inference model. The model type is OH\_AI\_MODELTYPE\_MINDIR.
    if (access(argv\[1\], F\_OK) != 0) {
        printf("model file not exists.\\n");
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    int ret = OH\_AI\_ModelBuildFromFile(model, argv\[1\], OH\_AI\_MODELTYPE\_MINDIR, context);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
      printf("OH\_AI\_ModelBuildFromFile failed, ret: %d.\\n", ret);
      OH\_AI\_ModelDestroy(&model);
      OH\_AI\_ContextDestroy(&context);
      return ret;
    }
    
4.  Input data.
    
    Before executing model inference, you need to populate data to the input tensor. In this example, random data is used to populate the model.
    
    // Obtain the input tensor.
    OH\_AI\_TensorHandleArray inputs = OH\_AI\_ModelGetInputs(model);
    if (inputs.handle\_list == NULL) {
      printf("OH\_AI\_ModelGetInputs failed, ret: %d.\\n", ret);
      OH\_AI\_ModelDestroy(&model);
      OH\_AI\_ContextDestroy(&context);
      return ret;
    }
    // Use random data to populate the tensor.
    ret = GenerateInputDataWithRandom(inputs);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
      printf("GenerateInputDataWithRandom failed, ret: %d.\\n", ret);
      OH\_AI\_ModelDestroy(&model);
      OH\_AI\_ContextDestroy(&context);
      return ret;
    }
    
5.  Execute model inference.
    
    Call **OH\_AI\_ModelPredict** to perform model inference.
    
    // Execute model inference.
    OH\_AI\_TensorHandleArray outputs;
    ret = OH\_AI\_ModelPredict(model, inputs, &outputs, NULL, NULL);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
      printf("OH\_AI\_ModelPredict failed, ret: %d.\\n", ret);
      OH\_AI\_ModelDestroy(&model);
      OH\_AI\_ContextDestroy(&context);
      return ret;
    }
    
6.  Obtain the output.
    
    After model inference is complete, you can obtain the inference result through the output tensor.
    
    // Obtain the output tensor and print the information.
    for (size\_t i = 0; i < outputs.handle\_num; ++i) {
      OH\_AI\_TensorHandle tensor = outputs.handle\_list\[i\];
      long long element\_num = OH\_AI\_TensorGetElementNum(tensor);
      printf("Tensor name: %s, tensor size is %zu ,elements num: %lld.\\n", OH\_AI\_TensorGetName(tensor),
            OH\_AI\_TensorGetDataSize(tensor), element\_num);
      const float \*data = (const float \*)OH\_AI\_TensorGetData(tensor);
      if (data == NULL) {
        printf("OH\_AI\_TensorGetData failed.\\n");
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return OH\_AI\_STATUS\_LITE\_ERROR;
      }
      printf("output data is:\\n");
      const int max\_print\_num = 50;
      for (int j = 0; j < element\_num && j <= max\_print\_num; ++j) {
        printf("%f ", data\[j\]);
      }
      printf("\\n");
    }
    
7.  Destroy the model.
    
    If the MindSpore Lite inference framework is no longer needed, you need to destroy the created model.
    
    // Release the model and context.
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    

#### Verification

1.  Write **CMakeLists.txt**.
    
    cmake\_minimum\_required(VERSION 3.14)
    project(Demo)
    
    add\_executable(demo main.c)
    
    target\_link\_libraries(
            demo
            mindspore\_lite\_ndk
            pthread
            dl
    )
    
    -   To use ohos-sdk for cross compilation, you need to set the toolchain path for the CMake tool as follows: -DCMAKE\_TOOLCHAIN\_FILE="/{sdkPath}/native/build/cmake/ohos.toolchain.cmake".
        
        Where, **sdkPath** indicates the SDK path in the DevEco Studio installation directory. To obtain the SDK path, go to the project page on DevEco Studio, choose **File** > **Settings...** > **HarmonyOS SDK**, and view the information in **Location**.
        
    -   The toolchain builds a 64-bit application by default. To build a 32-bit application, add the following configuration: -DOHOS\_ARCH="armeabi-v7a".
        
2.  Run the CMake tool.
    
    -   Use hdc\_std to connect to the device and put **demo** and **mobilenetv2.ms** to the same directory on the device.
    -   Run the hdc\_std shell command to access the device, go to the directory where **demo** is located, and run the following command:
    
    ./demo mobilenetv2.ms
    
    The inference is successful if the output is similar to the following:
    
    \# ./demo ./mobilenetv2.ms
    Tensor name: Softmax-65, tensor size is 4004 ,elements num: 1001.
    output data is:
    0.000018 0.000012 0.000026 0.000194 0.000156 0.001501 0.000240 0.000825 0.000016 0.000006 0.000007 0.000004 0.000004 0.000004 0.000015 0.000099 0.000011 0.000013 0.000005 0.000023 0.000004 0.000008 0.000003 0.000003 0.000008 0.000014 0.000012 0.000006 0.000019 0.000006 0.000018 0.000024 0.000010 0.000002 0.000028 0.000372 0.000010 0.000017 0.000008 0.000004 0.000007 0.000010 0.000007 0.000012 0.000005 0.000015 0.000007 0.000040 0.000004 0.000085 0.000023
