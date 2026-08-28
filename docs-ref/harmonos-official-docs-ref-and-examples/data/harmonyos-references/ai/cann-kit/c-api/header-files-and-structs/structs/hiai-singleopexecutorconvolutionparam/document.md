# HiAI\_SingleOpExecutorConvolutionParam

#### Overview

HMS\_HiAISingleOpExecutor\_CreateConvolution input parameters.

**Since:** 5.0.0(12)

**Related Modules:**[CANN](../../../modules/cann/document.md)

#### Summary

#### \[h2\]Data Fields

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions) \* [options](#options)

 | 

Pointer to the [HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions) object. The value cannot be a null pointer. Otherwise, the called method fails.

 |
| 

[HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor) \* [opDesc](#opdesc)

 | 

Pointer to the [HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor) object of a convolution operation. The value cannot be a null pointer. Otherwise, the called method fails.

 |
| 

[HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \* [input](#input)

 | 

Pointer to the input tensor description. The value cannot be a null pointer. Otherwise, the called method fails.

 |
| 

[HiAI\_SingleOpTensorDesc](../../../modules/cann/document.md#hiai_singleoptensordesc) \* [output](#output)

 | 

Pointer to the output tensor description. The value cannot be a null pointer. Otherwise, the called method fails.

 |
| 

[HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \* [filter](#filter)

 | 

Pointer to the convolution kernel tensor. The value cannot be a null pointer. Otherwise, the called method fails.

 |
| 

[HiAI\_SingleOpTensor](../../../modules/cann/document.md#hiai_singleoptensor) \* [bias](#bias)

 | 

Pointer to the bias tensor. If the convolution has no bias, the value can be a null pointer.

 |

#### Field

#### \[h2\]bias

HiAI\_SingleOpTensor\* HiAI\_SingleOpExecutorConvolutionParam::bias

**Description**

Pointer to the bias tensor. If the convolution has no bias, the value can be a null pointer.

#### \[h2\]filter

HiAI\_SingleOpTensor\* HiAI\_SingleOpExecutorConvolutionParam::filter

**Description**

Pointer to the convolution kernel tensor. The value cannot be a null pointer. Otherwise, the called method fails.

#### \[h2\]input

HiAI\_SingleOpTensorDesc\* HiAI\_SingleOpExecutorConvolutionParam::input

**Description**

Pointer to the input tensor description. The value cannot be a null pointer. Otherwise, the called method fails.

#### \[h2\]opDesc

HiAI\_SingleOpDescriptor\* HiAI\_SingleOpExecutorConvolutionParam::opDesc

**Description**

Pointer to the [HiAI\_SingleOpDescriptor](../../../modules/cann/document.md#hiai_singleopdescriptor) object of a convolution operation. The value cannot be a null pointer. Otherwise, the called method fails.

#### \[h2\]options

HiAI\_SingleOpOptions\* HiAI\_SingleOpExecutorConvolutionParam::options

**Description**

Pointer to the [HiAI\_SingleOpOptions](../../../modules/cann/document.md#hiai_singleopoptions) object. The value cannot be a null pointer. Otherwise, the called method fails.

#### \[h2\]output

HiAI\_SingleOpTensorDesc\* HiAI\_SingleOpExecutorConvolutionParam::output

**Description**

Pointer to the output tensor description. The value cannot be a null pointer. Otherwise, the called method fails.
