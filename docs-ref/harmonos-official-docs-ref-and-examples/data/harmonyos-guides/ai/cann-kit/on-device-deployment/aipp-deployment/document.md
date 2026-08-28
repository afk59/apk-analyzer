# AIPP Deployment

#### Basic Concepts

AIPP deployment refers to the configuration of dynamic AIPP parameters as required to enable AIPP during dynamic AIPP inference.

#### Process

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/b3/v3/mZCFWviKQwW82yyvODDZkw/en-us_image_0000002528408543.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DA13F19904427D3ED564DC5C880C4BC37C3C8FCBB7AD5FB7FD9700C127B68CC "Click to enlarge")

#### API Description

The following lists APIs for setting AIPP parameters. To learn more setting and query APIs, see [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit).

**Table 1** AIPP setting APIs in CANN Kit for model inference
| 
API

 | 

Description

 |
| :-- | :-- |
| 

HiAI\_AippParam\* HMS\_HiAIAippParam\_Create(uint32\_t batchNum);

 | 

Creates a dynamic AIPP configuration instance.

 |
| 

void HMS\_HiAIAippParam\_Destroy(HiAI\_AippParam\*\* aippParam);

 | 

Destroys a dynamic AIPP configuration instance.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputIndex(HiAI\_AippParam\* aippParam, uint32\_t inputIndex);

 | 

Sets the index of the input on which the dynamic AIPP configuration takes effect.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputAippIndex(HiAI\_AippParam\* aippParam, uint32\_t inputAippIndex);

 | 

Sets the index of the output, on whose input the dynamic AIPP configuration takes effect, where the input has more than one output.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputFormat(HiAI\_AippParam\* aippParam, HiAI\_ImageFormat inputFormat);

 | 

Sets the input image format.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputShape(HiAI\_AippParam\* aippParam, uint32\_t srcImageW, uint32\_t srcImageH);

 | 

Sets the original width and height of the input image.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetCscConfig(HiAI\_AippParam\* aippParam, HiAI\_ImageFormat inputFormat, HiAI\_ImageFormat outputFormat, HiAI\_ImageColorSpace space);

 | 

Sets CSC parameters.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetChannelSwapConfig(HiAI\_AippParam\* aippParam, bool rbuvSwapSwitch, bool axSwapSwitch);

 | 

Sets channel swapping parameters.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetCropConfig(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t startPosW, uint32\_t startPosH, uint32\_t croppedW, uint32\_t croppedH);

 | 

Sets image cropping parameters.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetResizeConfig(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t resizedW, uint32\_t resizedH);

 | 

Sets image resizing parameters.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetPadConfig(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t leftPadSize, uint32\_t rightPadSize, uint32\_t topPadSize, uint32\_t bottomPadSize);

 | 

Sets the number of pixels padded to the left, right, top, and bottom of an image.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetChannelPadding(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t paddingValues\[\], uint32\_t channelCount);

 | 

Sets the padding value for a channel.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetRotationAngle(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, float rotationAngle);

 | 

Sets image rotation parameters.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcMeanPixel(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, uint32\_t meanPixel\[\], uint32\_t channelCount);

 | 

Sets the average pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcMinPixel(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, float minPixel\[\], uint32\_t channelCount);

 | 

Sets the minimum pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcVarReciPixel(HiAI\_AippParam\* aippParam, uint32\_t batchIndex, float varReciPixel\[\], uint32\_t channelCount);

 | 

Sets the pixel value variance of DTC.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAITensor\_SetAippParams(NN\_Tensor\* tensor, HiAI\_AippParam\* aippParams\[\], size\_t aippNum);

 | 

Sets AIPP parameters for the input tensor.

 |

#### Development Procedure

1.  Create a dynamic AIPP configuration instance by calling [HMS\_HiAIAippParam\_Create](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_create).

2.  Set configurations about image computation.
    
    -   Call [HMS\_HiAIAippParam\_SetInputIndex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setinputindex) to set the index of the input on which the dynamic AIPP configuration takes effect.
    -   Call [HMS\_HiAIAippParam\_SetInputAippIndex](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setinputaippindex) to set the index of the output, on whose input the dynamic AIPP configuration takes effect, where the input has more than one output.
    
3.  Set configurations about the input image for dynamic AIPP.
    
    -   Call [HMS\_HiAIAippParam\_SetInputFormat](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setinputformat) to set the input image format.
    -   Call [HMS\_HiAIAippParam\_SetInputShape](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setinputshape) to set the original width and height of the input image.
    
4.  Set the following dynamic AIPP parameters as required.
    
    -   Call [HMS\_HiAIAippParam\_SetChannelSwapConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setchannelswapconfig) to set channel swapping parameters.
    -   Call [HMS\_HiAIAippParam\_SetCscConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setcscconfig) to set CSC parameters.
    -   Call [HMS\_HiAIAippParam\_SetCropConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setcropconfig) to set image cropping parameters.
    -   Call [HMS\_HiAIAippParam\_SetResizeConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setresizeconfig) to set image resizing parameters.
    -   Call [HMS\_HiAIAippParam\_SetPadConfig](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setpadconfig) to set image padding parameters.
    -   Call [HMS\_HiAIAippParam\_SetChannelPadding](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setchannelpadding) to set pixel padding parameters for each channel.
    -   Call [HMS\_HiAIAippParam\_SetRotationAngle](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setrotationangle) to set the rotation angle.
    -   Call [HMS\_HiAIAippParam\_SetDtcMeanPixel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setdtcmeanpixel) to set the average pixel value of DTC.
    -   Call [HMS\_HiAIAippParam\_SetDtcMinPixel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setdtcminpixel) to set the minimum pixel value of DTC.
    -   Call [HMS\_HiAIAippParam\_SetDtcVarReciPixel](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_setdtcvarrecipixel) to set the pixel value variance of DTC.
    
5.  Set AIPP configuration for [NN\_Tensor](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-neuralnetworkruntime-nn-tensor).
    
    After [constructing the input and output tensors](../model-inference/document.md#li10555614927), call [HMS\_HiAITensor\_SetAippParams](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaitensor_setaippparams) to set AIPP parameters for the input tensor.
    
6.  [Perform model inference](../model-inference/document.md#li510118171220).
7.  Destroy the dynamic AIPP configuration instance by calling [HMS\_HiAIAippParam\_Destroy](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaiaippparam_destroy).

#### Example

Assume that the training set of a model consists of RGB888 images. With dynamic AIPP enabled, YUYV images can be used as the input for model inference. If the sizes of input images for model inference are different from those of images in the training set, you can use AIPP to crop, resize, or pad the images to change their sizes. In the following sample code, you will see how to implement AIPP cropping, resizing, and padding through NDK APIs, and pre-process a 480 x 480 YUYV image into a 224 x 224 input.

#include "neural\_network\_runtime/neural\_network\_core.h"
#include "CANNKit/hiai\_aipp\_param.h"
#include "CANNKit/hiai\_tensor.h"
#include <vector>

constexpr uint32\_t BATCH\_NUM = 1;
// Create a dynamic AIPP configuration instance with a batch size of 1.
HiAI\_AippParam\* aippPara = HMS\_HiAIAippParam\_Create(BATCH\_NUM);
// Set the index of the input linked with the AippParam object, in the case of multiple inputs.
uint32\_t inputIndex = 0;
OH\_NN\_ReturnCode ret = HMS\_HiAIAippParam\_SetInputIndex(aippPara, inputIndex);
// Set the index of an output, in the scenario where the data linked with AippParam has more than one output.
uint32\_t validInputAippIndex = 0;
HMS\_HiAIAippParam\_SetInputAippIndex(aippPara, validInputAippIndex);
// Set the input image format for the AippParam object.
HMS\_HiAIAippParam\_SetInputFormat(aippPara, HIAI\_YUV420SP\_U8);
// Set the input image width and height for the AippParam object.
HMS\_HiAIAippParam\_SetInputShape(aippPara, 224, 224);
// Set the CSC parameters for the AippParam object.
HMS\_HiAIAippParam\_SetCscConfig(aippPara, HIAI\_YUV420SP\_U8, HIAI\_RGB888\_U8, HIAI\_JPEG);
// Set the RB/UV channel swap for the AippParam object.
HMS\_HiAIAippParam\_SetChannelSwapConfig(aippPara, true, false);
// Set the crop parameters for the 0th index batch of the AippParam object.
HMS\_HiAIAippParam\_SetCropConfig(aippPara, 0, 0, 0, 100, 100);
// Set the resize parameters for the 0th index batch of the AippParam object.
HMS\_HiAIAippParam\_SetResizeConfig(aippPara, 0, 110, 110);
// Set the padding value for the 0th index batch of the AippParam object.
HMS\_HiAIAippParam\_SetPadConfig(aippPara, 0, 1, 1, 1, 1);
// Set the rotation angle for the 0th index batch of the AippParam object.
HMS\_HiAIAippParam\_SetRotationAngle(aippPara, 0, 90.0);
// Set the average pixel value of DTC for the 0th batch of the AippParam object.
constexpr unsigned int chnNum = 4;
unsigned int pixelMeanPara\[chnNum\] = {1, 2, 3, 4};
HMS\_HiAIAippParam\_SetDtcMeanPixel(aippPara, 0, pixelMeanPara, chnNum);

// Prepare the input tensor.
size\_t inputCount = 0;
ret = OH\_NNExecutor\_GetInputCount(executor, &inputCount); // Create an executor by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
std::vector<NN\_Tensor \*> inputTensors;
for (size\_t i = 0; i < inputCount; ++i) {
    // For details about how to create an executor, see [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
    NN\_TensorDesc\* desc = OH\_NNExecutor\_CreateInputTensorDesc(executor, i);
    NN\_Tensor\* tensor = OH\_NNTensor\_Create(deviceID, desc); // Obtain the **deviceID** by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
    inputTensors.push\_back(tensor);
}
// Prepare the input tensor for AIPP.
HiAI\_AippParam\* aippParas\[1\] = {aippPara};
NN\_Tensor\* tensor = nullptr;
ret = HMS\_HiAITensor\_SetAippParams(tensor, aippParas, 1);
if (ret != OH\_NN\_SUCCESS ) {
    return;
}
inputTensors.push\_back(tensor);

// Prepare the output tensor.
size\_t outputCount = 0;
ret = OH\_NNExecutor\_GetOutputCount(executor, &outputCount); // Create an executor by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
std::vector<NN\_Tensor \*> outputTensors;
for (size\_t i = 0; i < outputCount; i++) {
    NN\_TensorDesc\* desc = OH\_NNExecutor\_CreateOutputTensorDesc(executor, i); // Create an executor by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
    NN\_Tensor\* tensor = OH\_NNTensor\_Create(deviceID, desc); // Obtain the **deviceID** by referring to [CANN Kit Codelab](https://developer.huawei.com/consumer/en/codelabsPortal/carddetails/tutorials_CANNKit-Image-classification).
    outputTensors.push\_back(tensor);
}
// Perform the inference.
ret = OH\_NNExecutor\_RunSync(executor\_, inputTensors.data(), 1, outputTensors.data(), 1);
if (ret != OH\_NN\_SUCCESS ) {
    return;
}
if (aippPara != nullptr) {
    HMS\_HiAIAippParam\_Destroy(&aippPara);
}
