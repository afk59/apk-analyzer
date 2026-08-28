# About This Kit

#### Usage Scenario

Neural Network Runtime (NNRt) functions as a bridge to connect the upper-layer AI inference framework and underlying acceleration chips, implementing cross-chip inference computing for AI models.

NNRt native APIs are intended for developers of the AI inference framework or application developers who want to directly use AI acceleration hardware to accelerate model inference.

The AI inference framework can call the NNRt image composition API to convert its model image into an NNRt internal model image, and then call the NNRt build and execution APIs to perform model inference on the AI acceleration hardware connected to NNRt. This implementation realizes unperceivable cross-AI hardware inference, but model loading is slow at first use.

The AI inference framework or application can also directly use the offline model dedicated to the specific AI hardware to perform model inference on NNRt, without the need to call the NNRt image composition API. This implementation realizes only inference on the specific AI hardware, but the model loading is fast at first use.

#### NNRt Architecture

As shown in Figure 1, in addition to native APIs, NNRt logically consists of the following functional modules:

1.  **Online image composition**: Have the AI inference framework call the NNRt image composition API to convert its model image into an NNRt internal model image. The built-in MindSpore Lite inference framework connects to NNRt through MindIR. For details, see [MindSpore Lite Kit](../../mindspore-lite-kit/model-deployment/using-mindspore-lite-for-model-inference-c-c/document.md). The format of MindIR model images is compatible with that of the NNRt internal model images. Therefore, MindSpore Lite can connect to NNRt without calling the NNRt image composition API.
2.  **Model build**: Build NNRt internal model images or offline model files into hardware-specific model objects on the underlying AI hardware driver through the NNRt build API. This way, model inference can be performed on the AI hardware subsequently.
3.  **Model inference**: Create an executor based on the built model object, set the input and output tensors for inference, and execute model inference on the AI hardware.
4.  **Memory management**: Apply for shared memory on the AI hardware driver and assign the shared memory to tensors. The input and output tensors must contain the corresponding data memory for inference. When a tensor is destroyed, release the shared memory. The shared memory on the AI hardware driver can help implement zero copy of input and output data, improving the inference performance.
5.  **Device management**: Display information about the AI hardware connected to NNRt and allow for selection of the AI hardware.
6.  **Model cache**: Save the built model objects into a file or a segment of memory in the cache. During next model build, model objects can be directly loaded from the file or segment of memory in the cache, greatly improving the build speed.
7.  **Offline model inference**: Directly use model files (offline models for short) dedicated to the AI hardware for inference. Specifically, use the model converter provided by the AI hardware vendor to convert the original training model into the offline model file corresponding to the AI hardware, deploy the offline model file in the application, and pass the model file to the NNRt offline model build API for inference. Offline models can be used only for build and inference on the corresponding AI hardware. That is, inference across AI hardware is not supported. The offline models are specific to the AI hardware and therefore, the build speed is usually fast.

\*\* Figure 1\*\* NNRt architecture

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4b/v3/5_gGih1cRxe7VLbJLUXcQw/en-us_image_0000002568684997.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CC387E43B7B48C48DA9A305C184B361254855BB1D73E663973841AB199B19728)

#### Features

-   Opens unified AI acceleration hardware inference APIs for the AI inference framework to implement unperceivable cross-AI hardware inference.
-   Provides image composition APIs for the AI inference framework to pass internal model images to NNRt.
-   Provides the model cache function. Model objects can be saved as cached files, greatly accelerating model loading.
-   Provides the hardware-specific offline model loading function, which shortens the model build time. However, inference can only be executed on the corresponding AI hardware.
-   Provides common hardware attributes such as the inference priority, performance mode, and FP16 mode, and supports custom extended attributes of specific hardware.
-   Implements zero copy of data by applying for shared memory on the AI hardware driver, improving the inference performance.

#### Available Capabilities

-   NNRt provides only the AI inference capability of the underlying AI acceleration hardware, but not common hardware such as the CPU.
-   NNRt provides only the basic AI inference capabilities and hardware attribute configurations commonly shared by AI hardware, such as build, execution, memory management, priority, and performance mode. If you want to configure the hardware attributes specific to dedicated AI hardware, you can use the custom extended attributes provided by NNRt. For details about the attribute names and values, see the documents provided by the hardware vendor.
-   Currently, NNRt supports 56 common operators. More operators will be supported in later versions. Note that there is no specific implementation for NNRt operators. They are only used as the elements of the internal model image to connect to the underlying AI hardware. The specific operators are implemented in the AI hardware driver.
-   NNRt supports only synchronous inference. Asynchronous inference will be supported in later versions.
-   NNRt does not support multi-thread concurrent image composition. Whether NNRt supports concurrent build and execution depends on underlying hardware driver.

#### Related Kits

The HarmonyOS AI capability openness architecture consists of three hierarchical levels from top to bottom:

-   [MindSpore Lite Kit](../../mindspore-lite-kit/about-this-kit/document.md): A lightweight AI engine built into HarmonyOS that provides unified inference interfaces and multi-backend hardware acceleration capabilities, enabling intelligent applications across all scenarios including smartphones, PCs/2-in-1 devices, and TVs.
    
-   Neural Network Runtime Kit: A cross-chip inference computing runtime designed for AI. It serves as an intermediary bridge connecting upper-layer AI inference frameworks and underlying acceleration chips, enabling cross-chip inference computations for AI models.
    
-   [CANN Kit](../../cann-kit/about-this-kit/document.md): HiSilicon's unified open computational architecture for AI hardware, supporting Ascend C NPU custom programming and cloud-device collaborative reuse. It excels in AI computations for heavy workloads and applications requiring deep performance and power consumption optimization.
    

Neural Network Runtime Kit supports the system's built-in MindSpore Lite inference framework, namely, MindSpore Lite Kit, which has exposed native APIs for configuring NNRt and can interface with NNRt without requiring graph construction.

Since both share the same model graph format (MindIR), using MindSpore Lite Kit to load models on NNRt is faster than other AI inference frameworks. Additionally, MindSpore Lite supports heterogeneous inference across general computing hardware (CPU/GPU) and NNRt AI acceleration hardware.

CANN Kit, which serves as the backend for the Kirin platform, integrates with Neural Network Runtime Kit to deliver AI computing capabilities for Kirin-powered devices. Built upon underlying hardware drivers and optimized computation libraries, CANN Kit offers unified support for the AscendC custom operator programming language and related toolchains across cloud-side Ascend chips. As a key cornerstone of the HarmonyOS AI ecosystem, CANN Kit provides essential support for intelligent applications across various domains.

#### Constraint

NNRt strongly depends on hardware and applies only to devices that support NPUs.

#### Supported Emulators

This kit does not support emulators.
