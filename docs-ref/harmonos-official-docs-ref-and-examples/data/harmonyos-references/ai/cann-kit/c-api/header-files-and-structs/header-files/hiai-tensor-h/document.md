# hiai\_tensor.h

#### Overview

Auxiliary APIs related to input and output memory during CANN Kit model inference.

You can call the following APIs to associate aippParam with a tensor or calculate the tensor memory size required for the image format.

**Library:** libhiai\_foundation.so

**Syscap:** SystemCapability.AI.HiAIFoundation

**Since:** 4.1.0(11)

**Related Modules:**[CANN](../../../modules/cann/document.md)

#### Summary

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

size\_t [HMS\_HiAITensor\_GetSizeWithImageFormat](../../../modules/cann/document.md#hms_hiaitensor_getsizewithimageformat) (NN\_TensorDesc \*desc, [HiAI\_ImageFormat](../../../modules/cann/document.md#hiai_imageformat) format)

 | 

Calculates the size of the tensor to be applied for based on NN\_TensorDesc and HiAI\_ImageFormat.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAITensor\_SetAippParams](../../../modules/cann/document.md#hms_hiaitensor_setaippparams) (NN\_Tensor \*tensor, [HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParams\[\], size\_t aippNum)

 | 

Sets aippParams for NN\_Tensor.

 |
