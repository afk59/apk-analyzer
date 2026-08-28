# About This Kit

Compute Architecture for Neural Networks (CANN) is a heterogeneous computing architecture launched by Huawei, designed for AI with device-cloud consistency. On HarmonyOS devices, the CANN Kit provides a unified access and running environment for various AI models and algorithms, oriented towards the Kirin chipset platform. Your app can leverage CANN Kit's APIs and developer data to perform intelligent inference, model training, and model optimization on the device, fully utilizing the local intelligent processing capabilities.

A model is the result of applying AI algorithms to a large amount of training data. You can use the model to perform intelligent inference and prediction based on new input data. Models can accomplish many complex tasks that are difficult or inefficient to implement with conventional code. For example, you can train a model to perform semantic segmentation on images, recognizing and precisely delineating different object classes within the images, or process voice data to enable voice wake-up, speech recognition, and speech synthesis.

You can use the [CANN](https://www.hiascend.com/software/cann) development platform provided by Huawei Ascend for model construction and training. Trained models can be converted to the format compatible with CANN Kit, allowing seamless integration into your app. Additionally, you can develop models based on other open-source or self-developed machine learning frameworks and then adapt these models to the HarmonyOS ecosystem using the toolchain provided by CANN Kit.

CANN Kit efficiently optimizes on-device intelligent computing performance by coordinating the Neural Network Processing Unit (NPU), CPU, and other hardware resources. While enhancing computing efficiency, it minimizes memory and power consumption. Running models directly on the device reduces network dependency, ensuring the privacy and security of developer data. This allows apps to maintain quick response times in various network environments, providing developers with a smooth and intelligent interaction experience.

CANN Kit is built on underlying hardware and optimized computing libraries, oriented toward the computing core of Huawei-developed Da Vinci NPU. It supports the Ascend C custom operator programming language and related toolchain, in conjunction with the cloud-side Ascend processors. This ensures that NPU-oriented development and optimization can be performed once and deployed across multiple devices.

CANN Kit is a cornerstone of the HarmonyOS intelligent ecosystem, providing core support for intelligent apps across various fields. For example, it supports AI computing acceleration capabilities such as Core Vision Kit for image vision-related tasks and Natural Language Kit for natural language processing. It also supports MindSpore Lite Kit and Neural Network Runtime Kit of HarmonyOS, as well as third-party inference frameworks like MNN and PaddleLite, collectively creating rich intelligent app scenarios.

#### Scenario

## Model Optimization

-   Model Zoo: a model library and tool package that comes with abundant model architectures and operators, enabling you to choose a model architecture that ensures the optimal hardware performance.
-   Model size reduction: optimizes the model size and reduces computing workload, lowering the space usage and computing power required by a model.

## Model Conversion

-   Offline model conversion: CANN Kit is capable of compiling a wide range of neural network operators, including convolution, pooling, activation, and full-connection, into AI instruction sequences dedicated for hardware in offline mode using the OMG tool, with data and weight rearranged to ensure optimized performance. The instructions and data are then integrated to generate an offline model.
-   AI pre-process (AIPP): performs hardware-based pre-processing on input data using AI, which supports image cropping, channel swapping, color space conversion (CSC), image resizing, data type conversion, rotation, and image padding. As AIPP is dedicated to hardware, it helps improve the inference performance. The model conversion configuration file is used to generate dynamic and static AIPP models and set AIPP parameters.
-   Variable **data\_type**: applicable when the model's input and output data types vary. With this feature, you do not need to modify a trained model for different input and output data types. When performing [model conversion](../model-conversion/offline-model-conversion/omg-parameters/document.md) using the OMG tool, specify the input and output data types so that the model can be applicable to different scenarios.

## On-device Deployment

-   Model inference: includes model compilation and inference, which are common in on-device deployment.
-   AIPP deployment: On-device AIPP deployment provides support for the dynamic AIPP feature. That is, it allows a dynamic AIPP model to support inference with different inputs and different AIPP features enabled.

-   Heterogeneity: CANN Kit automatically identifies the computing capability of the running environment, and performs adaptive graph partition and collaborative device scheduling for the neural network. The acceleration provided for NPU and CPU computing can provide higher hardware adaptability only via the CPU, and does not require the presence of an NPU.
-   Zero memory copy: encapsulates ION memory that stores data as input and output tensors for inference and helps avoid data copy of input and output tensors, thereby saving both memory and time required.
-   In-depth fusion: In-depth fusion powered by hardware helps reduce DDR access and improve the energy efficiency ratio (EER) during model inference.

## Single-Operator

During the loading phase of the original model in third-party application frameworks, corresponding single-operator executor objects are created and loaded based on parameters such as input, output, and weight information of the operators. When a third-party application framework performs model inference, the single-operator inference API is called during the operator computation process to complete the operator computation.

#### Basic Concepts

Before you get started with development using CANN Kit, familiarize yourself with the following concepts:

-   NPU
    
    Short for neural network processing unit, NPU is a chip specially used for deep learning and computing.
    
-   Operator
    
    A deep learning algorithm consists of multiple compute units referred to as operators (OPs).
    
-   Heterogeneous computing
    
    The essence of heterogeneous computing is composing a system based on compute units of different instruction sets and architectures. The compute units used by CANN Kit include CPUs and NPUs.
    
-   AIPP
    
    AIPP is a module that pre-processes input data for the purpose of AI inference. Model inference in CANN Kit generally depends on standardized input data formats. However, in common model inference scenarios, the input data can be an image in various formats. With AIPP, images in different formats can be converted to the standard format for NPUs. For a trained model, you do not need to retrain it if its input data formats are not supported by the inference and computing platform. Instead, you can complete the adaptation simply by setting AIPP parameters, or calling AIPP APIs in your app. As AIPP is dedicated to hardware, it helps improve the inference performance.
    
-   Quantization distillation
    
    Quantization distillation is a method that combines model compression techniques to guide the learning of student models by introducing the knowledge of teacher models during the quantization process. It aims to minimize the accuracy loss caused by quantization. The core objective of this approach is to reduce model size and computational complexity while retaining as much of the model's performance as possible.
    

#### Constraints

-   Restrictions on devices
    
    This kit is only applicable to phones, tablets, PCs/2-in-1 devices, and TV devices that are equipped with Kirin NPUs. In 5.1.0(18) and later versions, TV devices are also supported.
    

#### Relationship with Other Kits

The HarmonyOS AI openness layers, from top to bottom, are as follows:

-   MindSpore Lite Kit: a lightweight AI engine built in HarmonyOS, which provides unified inference APIs and multi-backend hardware acceleration capabilities, enabling intelligent applications across all scenarios including mobile phones, PCs/2-in-1 devices, and TVs.
-   Neural Network Runtime Kit (NNRt): bridges the upper-layer AI inference framework and underlying acceleration chips, implementing cross-chip inference computing for AI models.
-   CANN Kit: unified open computing architecture of HiSilicon AI hardware, which supports Ascend C NPU custom programming and device-cloud collaborative reuse. It excels at heavy-load AI computations and scenarios requiring deep optimization of performance and power consumption.

NNRt supports the built-in MindSpore Lite inference framework, that is, MindSpore Lite Kit, which has opened native APIs for NNRt configuration.

Image composition is not required for interconnection between MindSpore Lite Kit and NNRt. They share the same model image format, that is, MindIR. Therefore, using MindSpore Lite to load models on NNRt is faster than using any other AI inference frameworks. In addition, MindSpore Lite supports heterogeneous model inference across general-purpose computing hardware (CPUs/GPUs) and NNRt AI acceleration hardware.

CANN Kit connects to NNRt as the backend of the Kirin platform, facilitating NNRt's AI computing capability on the Kirin platform. CANN Kit is built on the underlying hardware drivers and optimized computing libraries. It works with Ascend chips on the cloud to support the Ascend C custom operator programming language and related tool chains. As an important cornerstone of the HarmonyOS intelligent ecosystem, CANN Kit provides core support for intelligent applications in various fields.
