# About This Kit

#### Use Cases

MindSpore Lite is a lightweight AI engine built in HarmonyOS. Its open AI framework comes with a multi-processor architecture to empower intelligent applications in all scenarios. It brings data scientists, algorithm engineers, and developers with friendly development, efficient running, and flexible deployment, helping to build a prosperous open source ecosystem of AI hardware/software applications.

So far, MindSpore Lite has been widely used in applications such as image classification, target recognition, facial recognition, and character recognition. Typical use cases are as follows:

-   Image classification: determines the category to which an image (such as an image of a cat, a dog, an airplane, or a car) belongs. This is the most basic computer vision application and belongs to the supervised learning category.
-   Target recognition: uses the preset object detection model to identify objects in the input frames of a camera, add labels to the objects, and mark them with bounding boxes.
-   Image segmentation: detects the positions of objects in a graph or the object of a specific pixel in the graph.

#### Constraints

-   This kit is applicable to phones, tablets, PCs/2-in-1 devices, and TVs and can be debugged using the Emulator.

#### Advantages

MindSpore Lite provides AI model inference capabilities tailored for different hardware devices. Its key advantages include:

-   High performance: Efficient kernel algorithms and assembly-level optimization support high-performance inference on dedicated CPU and NNRt chips, maximizing computing power while minimizing inference latency and power consumption.
-   Lightweight: Provides an ultra-lightweight solution, and supports model quantization and compression to enable smaller models to run faster and empower AI model deployment in extreme environments.
-   All-scenario support: Supports different types of OS and embedded system to adapt to AI applications on various intelligent devices.
-   Efficient deployment: Supports MindSpore, TensorFlow Lite, Caffe, and ONNX models, provides capabilities such as model compression and data processing, and supports unified training and inference IR.

#### Development Process

**Figure 1** Development process for MindSpore Lite model inference

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/LOcI7ngnRNSS7_kWSQ-aWQ/en-us_image_0000002568765001.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=4C1533F55A2F904514090D0D51F13565B0C29C10BCA83024481271C3F6F8CFD1)

The MindSpore Lite development process consists of two phases:

-   Model conversion
    
    MindSpore Lite uses models in .ms format for inference. You can use the model conversion tool provided by MindSpore Lite to convert third-party framework models, such as TensorFlow, TensorFlow Lite, Caffe, and ONNX, into .ms models. For details, see [Using MindSpore Lite for Model Conversion](../using-mindspore-lite-for-model-conversion/document.md).
    
-   Model deployment
    
    You can call the MindSpore Lite runtime APIs to implement model inference or training. The procedure is as follows:
    
    1.  Create the inference or training context, including the hardware and the number of threads.
    2.  Load the .ms model file.
    3.  Set the model input data.
    4.  Perform inference or training and read the output.

#### Development Mode

MindSpore Lite is built in the HarmonyOS standard system as a system component. You can develop AI applications based on MindSpore Lite in the following ways:

-   Method 1: [Using MindSpore Lite for Image Classification (ArkTS)](../using-mindspore-lite-for-image-classification-arkts/document.md). You can directly call MindSpore Lite ArkTS APIs in the UI code to load the AI model and perform model inference. An advantage of this method is the quick verification of the inference effect.
-   Method 2: [Using MindSpore Lite native APIs to develop AI applications](../using-mindspore-lite-for-image-classification-c-c/document.md). You can encapsulate the algorithm models and the code for calling MindSpore Lite native APIs into a dynamic library, and then use N-API to encapsulate the dynamic library into ArkTS APIs for the UI to call.

#### Relationship with Other Kits

The HarmonyOS AI capability openness architecture consists of three hierarchical levels from top to bottom:

-   MindSpore Lite Kit: A lightweight AI engine built into HarmonyOS that provides unified inference interfaces and multi-backend hardware acceleration capabilities, enabling intelligent applications across all scenarios including smartphones, PCs/2-in-1 devices, and TVs.
    
-   [Neural Network Runtime Kit](../../neural-network-runtime-kit/about-this-kit/document.md): A cross-chip inference computing runtime designed for AI. It serves as an intermediary bridge connecting upper-layer AI inference frameworks and underlying acceleration chips, enabling cross-chip inference computations for AI models.
    
-   [CANN Kit](../../cann-kit/about-this-kit/document.md): HiSilicon's unified open computational architecture for AI hardware, supporting Ascend C NPU custom programming and cloud-device collaborative reuse. It excels in AI computations for heavy workloads and applications requiring deep performance and power consumption optimization.
    

Neural Network Runtime Kit supports the system's built-in MindSpore Lite inference framework, namely, MindSpore Lite Kit, which has exposed native APIs for configuring NNRt and can interface with NNRt without requiring graph construction.

Since both share the same model graph format (MindIR), using MindSpore Lite Kit to load models on NNRt is faster than other AI inference frameworks. Additionally, MindSpore Lite supports heterogeneous inference across general computing hardware (CPU/GPU) and NNRt AI acceleration hardware.

CANN Kit, which serves as the backend for the Kirin platform, integrates with Neural Network Runtime Kit to deliver AI computing capabilities for Kirin-powered devices. Built upon underlying hardware drivers and optimized computation libraries, CANN Kit offers unified support for the AscendC custom operator programming language and related toolchains across cloud-side Ascend chips. As a key cornerstone of the HarmonyOS AI ecosystem, CANN Kit provides essential support for intelligent applications across various domains.
