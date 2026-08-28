# Overview

#### Introduction

With model compression algorithms and neural architecture search (NAS) algorithms, the automatic model size reduction tool can optimize deep neural network models according to the NPU architecture, helping you automatically make models more lightweight and generate network architectures. Currently, the non-training mode, plugin-based quantization mode, low-bit quantization for large language models, and NAS training are supported.

-   Non-training mode: You can input a model directly to reduce its size without retraining it. This mode is applicable if you wish to streamline the quantization process.

-   Plugin-based quantization mode: Model quantization APIs are provided for you to calibrate or retrain floating-point models. This mode is easy to use, and is applicable if you have high requirements on the precision.
-   Low-bit quantization of large language models: 4-bit quantization is supported for large language models. This is achieved through a three-stage execution process involving weight quantization, activation quantization, and parameter extraction, enabling model compression.
-   NAS training: The classification, detection, and segmentation networks are supported. After configuring required search parameters and API functions, you can use the NAS tool to search for network models that meet the computing power restrictions. This mode is applicable if you wish to generate network architecture automatically.

| 
Mode

 | 

Supported Framework

 | 

Supported Strategy

 | 

Supported Device

 |
| :-- | :-- | :-- | :-- |
| 

Non-training quantization

 | 

TensorFlow, PyTorch, and ONNX

 | 

Quant\_INT8-8

 | 

Supports both CPU and GPU. When GPU is used, training is supported on a single server with a single graphics card.

 |
| 

Plugin-based quantization

 | 

TensorFlow and PyTorch

 | 

Quant\_INT8-8

 | 

Supports GPUs, on a single server with a single graphics card.

 |
| 

NAS training

 | 

TensorFlow and PyTorch

 | 

NASEA

 | 

Supports GPU, on a single server with a single or multiple graphics cards.

 |
| 

Low-bit quantization for large language models

 | 

PyTorch

 | 

Quant\_INT16-4

 | 

Supports GPUs, on a single server with multiple graphics cards (for quantization distillation).

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/6GhNeTyDSie8CCiB9uqvGw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7941E610E42DE55F7BA80825C28802CFF83702935B8B88966591C9E1E760877B)

**Quant\_INT8-8**: indicates 8-bit quantization for data and 8-bit quantization for weights.

**Quant\_INT16-4**: indicates 16-bit quantization for data and 4-bit quantization for weights.

For details about the model benefits on the NPU through model size reduction and NAS, see [Model Benefits](../model-benefits/document.md).

After tailoring the model by using the size reduction tool, you can convert the model to an offline model (OM) by using the Offline Model Generator (OMG). For details about how to use the OMG, see [Model Conversion Example](../../../model-conversion/offline-model-conversion/model-conversion-example/document.md#section29012331976).

The size reduction tool is stored in the **tools\_dopt** directory.

| 
Directory

 | 

Description

 |
| :-- | :-- |
| 

tools\_dopt/dopt\_tf\_py3

 | 

Provides the tools and demo of non-training, plugin-based quantization, and NAS modes in the TensorFlow framework.

 |
| 

tools\_dopt/dopt\_pytorch\_py3

 | 

Provides the tools and demo of non-training, plugin-based quantization for large language models, and NAS modes in the PyTorch framework.

 |
| 

tools\_dopt/dopt\_onnx\_py3

 | 

Provides the non-training tool in the ONNX framework.

 |

#### Supported Scope

-   Plugin-based quantization supports GPU training on a single server with a single graphics card.
-   Non-training quantization is supported for CPU and GPU.
-   Large language models now support low-bit quantization on GPUs.
-   The NAS tool supports quantization on a single server with a single or multiple graphics cards, for skeleton search in classification, detection, and segmentation scenarios. For details about the operating environment, see [Preparing the Environment](../nas-training/document.md#section193737375169).

#### System Requirements

-   If you are using TensorFlow, prepare the following before using this tool:
    -   Python 3.10
    -   Ubuntu 22.04
    -   Tensorflow 2.8.0
    -   GPU(s) supporting CUDA® graphics cards (optional for non-training quantization mode)
-   If you are using PyTorch, prepare the following before using this tool:
    -   Python 3.10
    -   Ubuntu 22.04
    -   PyTorch 1.11
    -   opencv-python
    -   GPU(s) supporting CUDA® graphics cards (optional for non-training quantization mode)

-   If you are using ONNX, prepare the following before using this tool:
    -   Python 3.10
    -   Ubuntu 22.04
    -   ONNX Runtime 1.15
    -   ONNX 1.14

#### Developer Guide

The following lists the procedures and toolchain functions in different scenarios. You can select an appropriate optimization method based on the scenarios listed.

## TensorFlow Developers

| 
**Developer Scenario**

 | 

**Dependency**

 | 

**Toolchain Function**

 | 

**Recommended Tool**

 | 

Advantages

 |
| :-- | :-- | :-- | :-- | :-- |
| 

-   Insufficient datasets and training resources
-   High usability requirement

 | 

-   TensorFlow environment
-   Model PB file (manual conversion required)
-   Calibration set

 | 

Quant\_INT8-8

 | 

[TensorFlow non-training quantization](../non-training-quantization/document.md#section293645783311)

 | 

No TensorFlow coding required, friendly to beginners

 |
| 

-   High precision requirement
-   Sufficient datasets and training resources
-   Certain programming capability
-   Model training project in hand

 | 

-   TensorFlow environment
-   Model .ckpt file
-   Training set
-   Test set
-   You need to quantize the model by calling the size reduction tool API and then retrain the model in the training project.

 | 

Quant\_INT8-8

 | 

[TensorFlow plugin-based quantization](../plugin-based-quantization/document.md#section16110815547)

 | 

Guaranteed model precision

 |
| 

-   Automatically generating an applicable network architecture

 | 

-   [Environments](../nas-training/document.md#section193737375169)
-   Training set
-   Test set
-   You need to write the model API code based on the instructions.

 | 

Searches for and generates a network architecture

 | 

[NAS training](../nas-training/document.md)

 | 

Automatically searches for excellent network architectures in specific scenarios based on the configuration information provided

 |

## PyTorch Developers

| 
**Developer Scenario**

 | 

**Dependency**

 | 

**Toolchain Function**

 | 

**Recommended Tool**

 | 

**Advantages**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

-   Insufficient datasets and training resources
-   High usability requirement

 | 

-   PyTorch environment
-   Model parameter .pth file
-   Python model definition
-   Calibration set

 | 

Quant\_INT8-8

 | 

[PyTorch non-training quantization](../non-training-quantization/document.md#section18483131873820)

 | 

No PyTorch coding required, friendly to beginners

 |
| 

-   High precision requirement
-   Sufficient datasets and training resources
-   Certain programming capability

 | 

-   PyTorch environment
-   Model parameter .pth file
-   Training set
-   Test set
-   You need to quantize the model by calling the size reduction tool API and then retrain the model.

 | 

Quant\_INT8-8

 | 

[PyTorch plugin-based quantization](../plugin-based-quantization/document.md#section162431930104618)

 | 

Guaranteed model precision

 |
| 

-   Automatically generating an applicable network architecture

 | 

-   [Environments](../nas-training/document.md#section193737375169)
-   Training set
-   Test set
-   You need to write the model API code based on the instructions.

 | 

Searches for and generates a network architecture

 | 

[NAS training](../nas-training/document.md)

 | 

Automatically searches for excellent network architectures in specific scenarios based on the configuration information provided

 |
| 

-   Performing 4-bit weight quantization for the large language model

 | 

-   Training set
-   You need to generate configuration files and execution scripts based on the instructions.
-   Quantization based on script execution

 | 

Quant\_INT16-4

 | 

[Low-Bit Quantization for Large Language Models](../transformer-quantization/one-stop-quantization-for-llms/document.md)

 | 

Weight compression to as low as 4-bit for ultra-large-scale models

 |

## ONNX Developers

| 
**Developer Scenario**

 | 

**Preparation**

 | 

**Toolchain Function**

 | 

**Recommended Tool**

 | 

Advantages

 |
| :-- | :-- | :-- | :-- | :-- |
| 

-   Insufficient datasets and training resources
-   High usability requirement

 | 

-   ONNX Runtime environment
-   ONNX model
-   Calibration set

 | 

Quant\_INT8-8

 | 

[ONNX non-training quantization](../non-training-quantization/document.md#section1262217244312)

 | 

No coding required, friendly to beginners

 |
