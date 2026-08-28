# Using the MindSpore Lite Engine for On-Device Training (C/C++)

#### When to Use

MindSpore Lite is an AI engine that implements AI model inference for different hardware devices. It has been used in a wide range of fields, such as image classification, target recognition, facial recognition, and character recognition. In addition, MindSpore Lite supports deployment of model training on devices, making it possible to adapt to user behavior in actual service scenarios.

This topic describes the general development process for using MindSpore Lite for model training on devices.

#### Available APIs

The following table list some APIs for using MindSpore Lite for model training. For details about the APIs, see [MindSpore](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-mindspore).

| API | Description |
| :-- | :-- |
| OH\_AI\_ContextHandle OH\_AI\_ContextCreate() | Creates a context object. This API must be used together with **OH\_AI\_ContextDestroy**. |
| OH\_AI\_DeviceInfoHandle OH\_AI\_DeviceInfoCreate(OH\_AI\_DeviceType device\_type) | Creates a runtime device information object. |
| void OH\_AI\_ContextDestroy(OH\_AI\_ContextHandle \*context) | Destroys a context object. |
| void OH\_AI\_ContextAddDeviceInfo(OH\_AI\_ContextHandle context, OH\_AI\_DeviceInfoHandle device\_info) | Adds a runtime device information object. |
| OH\_AI\_TrainCfgHandle OH\_AI\_TrainCfgCreate() | Creates the pointer to a training configuration object. |
| void OH\_AI\_TrainCfgDestroy(OH\_AI\_TrainCfgHandle \*train\_cfg) | Destroys the pointer to a training configuration object. |
| OH\_AI\_ModelHandle OH\_AI\_ModelCreate() | Creates a model object. |
| OH\_AI\_Status OH\_AI\_TrainModelBuildFromFile(OH\_AI\_ModelHandle model, const char \*model\_path, OH\_AI\_ModelType model\_type, const OH\_AI\_ContextHandle model\_context, const OH\_AI\_TrainCfgHandle train\_cfg) | Loads and builds a MindSpore Lite training model from a model file. |
| OH\_AI\_Status OH\_AI\_RunStep(OH\_AI\_ModelHandle model, const OH\_AI\_KernelCallBack before, const OH\_AI\_KernelCallBack after) | Runs a single-step training model. |
| OH\_AI\_Status OH\_AI\_ModelSetTrainMode(OH\_AI\_ModelHandle model, bool train) | Sets the training mode. |
| OH\_AI\_Status OH\_AI\_ExportModel(OH\_AI\_ModelHandle model, OH\_AI\_ModelType model\_type, const char \*model\_file, OH\_AI\_QuantizationType quantization\_type, bool export\_inference\_only, char \*\*output\_tensor\_name, size\_t num) | Exports a trained MS model. |
| void OH\_AI\_ModelDestroy(OH\_AI\_ModelHandle \*model) | Destroys a model object. |

#### How to Develop

The following figure shows the development process for MindSpore Lite model training.

**Figure 1** Development process for MindSpore Lite model training

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/c0/v3/V2IeC73jR-K7aLsHpfkx4g/en-us_image_0000002537925216.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=80D7DF402A1750159AFD13ACC91129823C64179DD75D3B3F0171432F842F5CC4)

Before moving to the development process, you need to reference related header files and compile functions to generate random input. The sample code is as follows:

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include "mindspore/model.h"

int GenerateInputDataWithRandom(OH\_AI\_TensorHandleArray inputs) {
  for (size\_t i = 0; i < inputs.handle\_num; ++i) {
    float \*input\_data = (float \*)OH\_AI\_TensorGetMutableData(inputs.handle\_list\[i\]);
    if (input\_data == NULL) {
      printf("OH\_AI\_TensorGetMutableData failed.\\n");
      return  OH\_AI\_STATUS\_LITE\_ERROR;
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
    
    Ensure that the prepared model is in .ms format. This document uses lenet\_train.ms as an example. The operation procedure is as follows:
    
    -   Use Python to create a network model based on the MindSpore architecture and export the model as a .mindir file. For details, see [Quick Start](https://www.mindspore.cn/tutorials/en/r2.1/beginner/quick_start.html).
    -   Convert the .mindir model file into an .ms file. For details about the conversion procedure, see [Converting MindSpore Lite Models](https://www.mindspore.cn/lite/docs/en/r2.1/use/converter_train.html). The .ms file can be imported to the device to implement training based on the MindSpore Lite framework.
2.  Create a context and set parameters such as the device type and training configuration.
    
    // Create and init context, add CPU device info
    OH\_AI\_ContextHandle context = OH\_AI\_ContextCreate();
    if (context == NULL) {
        printf("OH\_AI\_ContextCreate failed.\\n");
        return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    
    OH\_AI\_DeviceInfoHandle cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
    if (cpu\_device\_info == NULL) {
        printf("OH\_AI\_DeviceInfoCreate failed.\\n");
        OH\_AI\_ContextDestroy(&context);
        return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);
    
    // Create trainCfg
    OH\_AI\_TrainCfgHandle trainCfg = OH\_AI\_TrainCfgCreate();
    if (trainCfg == NULL) {
        printf("OH\_AI\_TrainCfgCreate failed.\\n");
        OH\_AI\_ContextDestroy(&context);
        return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    
3.  Create, load, and build the model.
    
    Call **OH\_AI\_TrainModelBuildFromFile** to load and build the model.
    
    // Create model
    OH\_AI\_ModelHandle model = OH\_AI\_ModelCreate();
    if (model == NULL) {
        printf("OH\_AI\_ModelCreate failed.\\n");
        OH\_AI\_TrainCfgDestroy(&trainCfg);
        OH\_AI\_ContextDestroy(&context);
        return OH\_AI\_STATUS\_LITE\_ERROR;
    }
    
    // Build model
    int ret = OH\_AI\_TrainModelBuildFromFile(model, model\_file, OH\_AI\_MODELTYPE\_MINDIR, context, trainCfg);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
        printf("OH\_AI\_TrainModelBuildFromFile failed, ret: %d.\\n", ret);
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return ret;
    }
    
4.  Input data.
    
    Before executing model training, you need to populate data to the input tensor. In this example, random data is used to populate the model.
    
    // Get Inputs
    OH\_AI\_TensorHandleArray inputs = OH\_AI\_ModelGetInputs(model);
    if (inputs.handle\_list == NULL) {
        printf("OH\_AI\_ModelGetInputs failed, ret: %d.\\n", ret);
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return ret;
    }
    
    // Generate random data as input data.
    ret = GenerateInputDataWithRandom(inputs);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
        printf("GenerateInputDataWithRandom failed, ret: %d.\\n", ret);
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return ret;
    }
    
5.  Execute model training.
    
    Use **OH\_AI\_ModelSetTrainMode** to set the training mode and use **OH\_AI\_RunStep** to run model training.
    
    // Set Train Mode
    ret = OH\_AI\_ModelSetTrainMode(model, true);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
        printf("OH\_AI\_ModelSetTrainMode failed, ret: %d.\\n", ret);
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return ret;
    }
    
    // Model Train Step
    ret = OH\_AI\_RunStep(model, NULL, NULL);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
        printf("OH\_AI\_RunStep failed, ret: %d.\\n", ret);
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return ret;
    }
    printf("Train Step Success.\\n");
    
6.  Export the trained model.
    
    Use **OH\_AI\_ExportModel** to export the trained model.
    
    // Export Train Model
    ret = OH\_AI\_ExportModel(model, OH\_AI\_MODELTYPE\_MINDIR, export\_train\_model, OH\_AI\_NO\_QUANT, false, NULL, 0);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
        printf("OH\_AI\_ExportModel train failed, ret: %d.\\n", ret);
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return ret;
    }
    printf("Export Train Model Success.\\n");
    
    // Export Inference Model
    ret = OH\_AI\_ExportModel(model, OH\_AI\_MODELTYPE\_MINDIR, export\_infer\_model, OH\_AI\_NO\_QUANT, true, NULL, 0);
    if (ret != OH\_AI\_STATUS\_SUCCESS) {
        printf("OH\_AI\_ExportModel inference failed, ret: %d.\\n", ret);
        OH\_AI\_ModelDestroy(&model);
        OH\_AI\_ContextDestroy(&context);
        return ret;
    }
    printf("Export Inference Model Success.\\n");
    
7.  Destroy the model.
    
    If the MindSpore Lite inference framework is no longer needed, you need to destroy the created model.
    
    // Delete model and context.
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    

#### Verification

1.  Write **CMakeLists.txt**.
    
    cmake\_minimum\_required(VERSION 3.14)
    project(TrainDemo)
    
    add\_executable(train\_demo main.c)
    
    target\_link\_libraries(
            train\_demo
            mindspore\_lite\_ndk
    )
    
    -   To use ohos-sdk for cross compilation, you need to set the native toolchain path for the CMake tool as follows: **\-DCMAKE\_TOOLCHAIN\_FILE="/xxx/native/build/cmake/ohos.toolchain.cmake"**.
        
    -   Start cross compilation. When running the compilation command, set **OHOS\_NDK** to the native toolchain path.
        
          mkdir -p build
        
          cd ./build || exit
          OHOS\_NDK=""
          cmake -G "Unix Makefiles" \\
                -S ../ \\
                -DCMAKE\_TOOLCHAIN\_FILE="$OHOS\_NDK/build/cmake/ohos.toolchain.cmake" \\
                -DOHOS\_ARCH=arm64-v8a \\
                -DCMAKE\_BUILD\_TYPE=Release
        
          make
        
2.  Run the executable program for compilation.
    
    -   Use hdc to connect to the device and put **train\_demo** and **lenet\_train.ms** to the same directory on the device.
    -   Use hdc shell to access the device, go to the directory where **train\_demo** is located, and run the following command:
    
    ./train\_demo ./lenet\_train.ms export\_train\_model export\_infer\_model
    
    The operation is successful if the output is similar to the following:
    
    Train Step Success.
    Export Train Model Success.
    Export Inference Model Success.
    Tensor name: Default/network-WithLossCell/\_backbone-LeNet5/fc3-Dense/BiasAdd-op121, tensor size is 80, elements num: 20.
    output data is:
    0.000265 0.000231 0.000254 0.000269 0.000238 0.000228
    
    In the directory where **train\_demo** is located, you can view the exported model files **export\_train\_model.ms** and **export\_infer\_model.ms**.
    

#### Sample

#include <stdlib.h>
#include <stdio.h>
#include <string>
#include "mindspore/model.h"

int GenerateInputDataWithRandom(OH\_AI\_TensorHandleArray inputs) {
  for (size\_t i = 0; i < inputs.handle\_num; ++i) {
    float \*input\_data = (float \*)OH\_AI\_TensorGetMutableData(inputs.handle\_list\[i\]);
    if (input\_data == NULL) {
      printf("OH\_AI\_TensorGetMutableData failed.\\n");
      return  OH\_AI\_STATUS\_LITE\_ERROR;
    }
    int64\_t num = OH\_AI\_TensorGetElementNum(inputs.handle\_list\[i\]);
    const int divisor = 10;
    for (size\_t j = 0; j < num; j++) {
      input\_data\[j\] = (float)(rand() % divisor) / divisor;  // 0--0.9f
    }
  }
  return OH\_AI\_STATUS\_SUCCESS;
}

int ModelPredict(char\* model\_file) {
  // Create and init context, add CPU device info
  OH\_AI\_ContextHandle context = OH\_AI\_ContextCreate();
  if (context == NULL) {
    printf("OH\_AI\_ContextCreate failed.\\n");
    return OH\_AI\_STATUS\_LITE\_ERROR;
  }

  OH\_AI\_DeviceInfoHandle cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
  if (cpu\_device\_info == NULL) {
    printf("OH\_AI\_DeviceInfoCreate failed.\\n");
    OH\_AI\_ContextDestroy(&context);
    return OH\_AI\_STATUS\_LITE\_ERROR;
  }
  OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);

  // Create model
  OH\_AI\_ModelHandle model = OH\_AI\_ModelCreate();
  if (model == NULL) {
    printf("OH\_AI\_ModelCreate failed.\\n");
    OH\_AI\_ContextDestroy(&context);
    return OH\_AI\_STATUS\_LITE\_ERROR;
  }

  // Build model
  int ret = OH\_AI\_ModelBuildFromFile(model, model\_file, OH\_AI\_MODELTYPE\_MINDIR, context);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("OH\_AI\_ModelBuildFromFile failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }

  // Get Inputs
  OH\_AI\_TensorHandleArray inputs = OH\_AI\_ModelGetInputs(model);
  if (inputs.handle\_list == NULL) {
    printf("OH\_AI\_ModelGetInputs failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }

  // Generate random data as input data.
  ret = GenerateInputDataWithRandom(inputs);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("GenerateInputDataWithRandom failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }

  // Model Predict
  OH\_AI\_TensorHandleArray outputs;
  ret = OH\_AI\_ModelPredict(model, inputs, &outputs, NULL, NULL);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("MSModelPredict failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }

  // Print Output Tensor Data.
  for (size\_t i = 0; i < outputs.handle\_num; ++i) {
    OH\_AI\_TensorHandle tensor = outputs.handle\_list\[i\];
    int64\_t element\_num = OH\_AI\_TensorGetElementNum(tensor);
    printf("Tensor name: %s, tensor size is %ld ,elements num: %ld.\\n", OH\_AI\_TensorGetName(tensor),
           OH\_AI\_TensorGetDataSize(tensor), element\_num);
    const float \*data = (const float \*)OH\_AI\_TensorGetData(tensor);
    printf("output data is:\\n");
    const int max\_print\_num = 50;
    for (int j = 0; j < element\_num && j <= max\_print\_num; ++j) {
      printf("%f ", data\[j\]);
    }
    printf("\\n");
  }

  OH\_AI\_ModelDestroy(&model);
  OH\_AI\_ContextDestroy(&context);
  return OH\_AI\_STATUS\_SUCCESS;
}

int TrainDemo(int argc, const char \*\*argv) {
  if (argc < 4) {
    printf("Model file must be provided.\\n");
    printf("Export Train Model path must be provided.\\n");
    printf("Export Inference Model path must be provided.\\n");
    return OH\_AI\_STATUS\_LITE\_ERROR;
  }
  const char \*model\_file = argv\[1\];
  const char \*export\_train\_model = argv\[2\];
  const char \*export\_infer\_model = argv\[3\];

  // Create and init context, add CPU device info
  OH\_AI\_ContextHandle context = OH\_AI\_ContextCreate();
  if (context == NULL) {
    printf("OH\_AI\_ContextCreate failed.\\n");
    return OH\_AI\_STATUS\_LITE\_ERROR;
  }

  OH\_AI\_DeviceInfoHandle cpu\_device\_info = OH\_AI\_DeviceInfoCreate(OH\_AI\_DEVICETYPE\_CPU);
  if (cpu\_device\_info == NULL) {
    printf("OH\_AI\_DeviceInfoCreate failed.\\n");
    OH\_AI\_ContextDestroy(&context);
    return OH\_AI\_STATUS\_LITE\_ERROR;
  }
  OH\_AI\_ContextAddDeviceInfo(context, cpu\_device\_info);

  // Create trainCfg
  OH\_AI\_TrainCfgHandle trainCfg = OH\_AI\_TrainCfgCreate();
  if (trainCfg == NULL) {
    printf("OH\_AI\_TrainCfgCreate failed.\\n");
    OH\_AI\_ContextDestroy(&context);
    return OH\_AI\_STATUS\_LITE\_ERROR;
  }

  // Create model
  OH\_AI\_ModelHandle model = OH\_AI\_ModelCreate();
  if (model == NULL) {
    printf("OH\_AI\_ModelCreate failed.\\n");
    OH\_AI\_TrainCfgDestroy(&trainCfg);
    OH\_AI\_ContextDestroy(&context);
    return OH\_AI\_STATUS\_LITE\_ERROR;
  }

  // Build model
  int ret = OH\_AI\_TrainModelBuildFromFile(model, model\_file, OH\_AI\_MODELTYPE\_MINDIR, context, trainCfg);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("OH\_AI\_TrainModelBuildFromFile failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }

  // Get Inputs
  OH\_AI\_TensorHandleArray inputs = OH\_AI\_ModelGetInputs(model);
  if (inputs.handle\_list == NULL) {
    printf("OH\_AI\_ModelGetInputs failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }

  // Generate random data as input data.
  ret = GenerateInputDataWithRandom(inputs);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("GenerateInputDataWithRandom failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }

  // Set Train Mode
  ret = OH\_AI\_ModelSetTrainMode(model, true);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("OH\_AI\_ModelSetTrainMode failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }

  // Model Train Step
  ret = OH\_AI\_RunStep(model, NULL, NULL);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("OH\_AI\_RunStep failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }
  printf("Train Step Success.\\n");

  // Export Train Model
  ret = OH\_AI\_ExportModel(model, OH\_AI\_MODELTYPE\_MINDIR, export\_train\_model, OH\_AI\_NO\_QUANT, false, NULL, 0);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("OH\_AI\_ExportModel train failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }
  printf("Export Train Model Success.\\n");

  // Export Inference Model
  ret = OH\_AI\_ExportModel(model, OH\_AI\_MODELTYPE\_MINDIR, export\_infer\_model, OH\_AI\_NO\_QUANT, true, NULL, 0);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("OH\_AI\_ExportModel inference failed, ret: %d.\\n", ret);
    OH\_AI\_ModelDestroy(&model);
    OH\_AI\_ContextDestroy(&context);
    return ret;
  }
  printf("Export Inference Model Success.\\n");

  // Delete model and context.
  OH\_AI\_ModelDestroy(&model);
  OH\_AI\_ContextDestroy(&context);

  // Use The Exported Model to predict
  std::string temp\_path = std::string(export\_infer\_model) + ".ms";
  const char \*exported\_model = temp\_path.c\_str();
  ret = ModelPredict(exported\_model);
  if (ret != OH\_AI\_STATUS\_SUCCESS) {
    printf("Exported Model to predict failed, ret: %d.\\n", ret);
    return ret;
  }
  return OH\_AI\_STATUS\_SUCCESS;
}

int main(int argc, const char \*\*argv) { return TrainDemo(argc, argv); }
