# hiai\_aipp\_param.h

#### Overview

APIs for creating dynamic AIPP objects and setting and querying relevant parameters for CANN Kit model inference.

**Library:** libhiai\_foundation.so

**Syscap:** SystemCapability.AI.HiAIFoundationphone,2in1,tablet,tv,car

**Since:** 4.1.0(11)

**Related Modules:**[CANN](../../../modules/cann/document.md)

#### Summary

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) [HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam)

 | 

AIPP parameter object.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_ImageFormat](../../../modules/cann/document.md#hiai_imageformat) {

HIAI\_YUV420SP\_U8 = 0,

HIAI\_XRGB8888\_U8 = 1,

HIAI\_YUV400\_U8 = 2,

HIAI\_ARGB8888\_U8 = 3,

HIAI\_YUYV\_U8 = 4,

HIAI\_YUV422SP\_U8 = 5,

HIAI\_AYUV444\_U8 = 6,

HIAI\_RGB888\_U8 = 7,

HIAI\_BGR888\_U8 = 8,

HIAI\_YUV444SP\_U8 = 9,

HIAI\_YVU444SP\_U8 = 10,

HIAI\_IMAGE\_FORMAT\_INVALID = 255

}

 | 

Image format enums of input and output tensors supported by CANN Kit inference.

 |
| 

[HiAI\_ImageColorSpace](../../../modules/cann/document.md#hiai_imagecolorspace) {

HIAI\_JPEG = 0,

HIAI\_BT\_601\_NARROW = 1,

HIAI\_BT\_601\_FULL = 2, HIAI\_BT\_709\_NARROW = 3,

HIAI\_IMAGE\_COLOR\_SPACE\_INVALID = 4

}

 | 

Image's color space type.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \* [HMS\_HiAIAippParam\_Create](../../../modules/cann/document.md#hms_hiaiaippparam_create) (uint32\_t batchNum)

 | 

Creates a dynamic AippParam object based on batchNum.

 |
| 

void \* [HMS\_HiAIAippParam\_GetData](../../../modules/cann/document.md#hms_hiaiaippparam_getdata) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam)

 | 

Obtains the memory address requested for AippParam.

 |
| 

uint32\_t [HMS\_HiAIAippParam\_GetDataSize](../../../modules/cann/document.md#hms_hiaiaippparam_getdatasize) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam)

 | 

Obtains the memory size requested for AippParam.

 |
| 

int [HMS\_HiAIAippParam\_GetInputIndex](../../../modules/cann/document.md#hms_hiaiaippparam_getinputindex) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam)

 | 

Queries the input index of the AippParam object.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputIndex](../../../modules/cann/document.md#hms_hiaiaippparam_setinputindex) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t inputIndex)

 | 

Sets the input index of the AippParam object.

 |
| 

int [HMS\_HiAIAippParam\_GetInputAippIndex](../../../modules/cann/document.md#hms_hiaiaippparam_getinputaippindex) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam)

 | 

Queries the index of an output, in the scenario where the input linked with AippParam has more than one output.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputAippIndex](../../../modules/cann/document.md#hms_hiaiaippparam_setinputaippindex) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t inputAippIndex)

 | 

Sets the index of an output, in the scenario where the input linked with AippParam has more than one output.

 |
| 

void [HMS\_HiAIAippParam\_Destroy](../../../modules/cann/document.md#hms_hiaiaippparam_destroy) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*\*aippParam)

 | 

Releases the AippParam object.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputFormat](../../../modules/cann/document.md#hms_hiaiaippparam_setinputformat) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](../../../modules/cann/document.md#hiai_imageformat) inputFormat)

 | 

Sets the input image format.

 |
| 

[HiAI\_ImageFormat](../../../modules/cann/document.md#hiai_imageformat) [HMS\_HiAIAippParam\_GetInputFormat](../../../modules/cann/document.md#hms_hiaiaippparam_getinputformat) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam)

 | 

Queries the input image format.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputShape](../../../modules/cann/document.md#hms_hiaiaippparam_setinputshape) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t srcImageW, uint32\_t srcImageH)

 | 

Sets the width and height of the input image.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetInputShape](../../../modules/cann/document.md#hms_hiaiaippparam_getinputshape) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t \*srcImageW, uint32\_t \*srcImageH)

 | 

Queries the width and height of the input image.

 |
| 

uint32\_t [HMS\_HiAIAippParam\_GetBatchCount](../../../modules/cann/document.md#hms_hiaiaippparam_getbatchcount) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam)

 | 

Queries the number of images set by AippParam.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetCscConfig](../../../modules/cann/document.md#hms_hiaiaippparam_setcscconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](../../../modules/cann/document.md#hiai_imageformat) inputFormat, [HiAI\_ImageFormat](../../../modules/cann/document.md#hiai_imageformat) outputFormat, [HiAI\_ImageColorSpace](../../../modules/cann/document.md#hiai_imagecolorspace) space)

 | 

Sets Color Space Conversion (CSC) parameters for AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetCscConfig](../../../modules/cann/document.md#hms_hiaiaippparam_getcscconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](../../../modules/cann/document.md#hiai_imageformat) \*inputFormat, [HiAI\_ImageFormat](../../../modules/cann/document.md#hiai_imageformat) \*outputFormat, [HiAI\_ImageColorSpace](../../../modules/cann/document.md#hiai_imagecolorspace) \*space)

 | 

Queries the CSC parameters of AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetChannelSwapConfig](../../../modules/cann/document.md#hms_hiaiaippparam_setchannelswapconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, bool rbuvSwapSwitch, bool axSwapSwitch)

 | 

Sets AIPP channel swapping parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetChannelSwapConfig](../../../modules/cann/document.md#hms_hiaiaippparam_getchannelswapconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, bool \*rbuvSwapSwitch, bool \*axSwapSwitch)

 | 

Queries AIPP channel swapping parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetSingleBatchMultiCrop](../../../modules/cann/document.md#hms_hiaiaippparam_setsinglebatchmulticrop) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, bool singleBatchMultiCrop)

 | 

Sets the SingleBatchMultiCrop flag of AIPP.

 |
| 

bool [HMS\_HiAIAippParam\_GetSingleBatchMultiCrop](../../../modules/cann/document.md#hms_hiaiaippparam_getsinglebatchmulticrop) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam)

 | 

Queries the SingleBatchMultiCrop flag of AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetCropConfig](../../../modules/cann/document.md#hms_hiaiaippparam_setcropconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t startPosW, uint32\_t startPosH, uint32\_t croppedW, uint32\_t croppedH)

 | 

Sets AIPP cropping parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetCropConfig](../../../modules/cann/document.md#hms_hiaiaippparam_getcropconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*startPosW, uint32\_t \*startPosH, uint32\_t \*croppedW, uint32\_t \*croppedH)

 | 

Queries AIPP cropping parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetResizeConfig](../../../modules/cann/document.md#hms_hiaiaippparam_setresizeconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t resizedW, uint32\_t resizedH)

 | 

Sets AIPP image resizing parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetResizeConfig](../../../modules/cann/document.md#hms_hiaiaippparam_getresizeconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*resizedW, uint32\_t \*resizedH)

 | 

Queries AIPP image resizing parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetPadConfig](../../../modules/cann/document.md#hms_hiaiaippparam_setpadconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t leftPadSize, uint32\_t rightPadSize, uint32\_t topPadSize, uint32\_t bottomPadSize)

 | 

Sets the number of pixels padded to the input image by AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetPadConfig](../../../modules/cann/document.md#hms_hiaiaippparam_getpadconfig) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*leftPadSize, uint32\_t \*rightPadSize, uint32\_t \*topPadSize, uint32\_t \*bottomPadSize)

 | 

Queries the number of pixels padded to the input image by AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetChannelPadding](../../../modules/cann/document.md#hms_hiaiaippparam_setchannelpadding) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t paddingValues\[\], uint32\_t channelCount)

 | 

Sets the padding value for a channel during AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetChannelPadding](../../../modules/cann/document.md#hms_hiaiaippparam_getchannelpadding) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t paddingValues\[\], uint32\_t channelCount)

 | 

Queries the padding value for a channel during AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetRotationAngle](../../../modules/cann/document.md#hms_hiaiaippparam_setrotationangle) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float rotationAngle)

 | 

Sets the rotation angle in AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetRotationAngle](../../../modules/cann/document.md#hms_hiaiaippparam_getrotationangle) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float \*rotationAngle)

 | 

Queries the image rotation angle in AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcMeanPixel](../../../modules/cann/document.md#hms_hiaiaippparam_setdtcmeanpixel) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t meanPixel\[\], uint32\_t channelCount)

 | 

Sets the average pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcMeanPixel](../../../modules/cann/document.md#hms_hiaiaippparam_getdtcmeanpixel) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t meanPixel\[\], uint32\_t channelCount)

 | 

Queries the average pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcMinPixel](../../../modules/cann/document.md#hms_hiaiaippparam_setdtcminpixel) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float minPixel\[\], uint32\_t channelCount)

 | 

Sets the minimum pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcMinPixel](../../../modules/cann/document.md#hms_hiaiaippparam_getdtcminpixel) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float minPixel\[\], uint32\_t channelCount)

 | 

Queries the minimum pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcVarReciPixel](../../../modules/cann/document.md#hms_hiaiaippparam_setdtcvarrecipixel) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float varReciPixel\[\], uint32\_t channelCount)

 | 

Sets the pixel variance of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcVarReciPixel](../../../modules/cann/document.md#hms_hiaiaippparam_getdtcvarrecipixel) ([HiAI\_AippParam](../../../modules/cann/document.md#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float varReciPixel\[\], uint32\_t channelCount)

 | 

Queries the pixel variance of DTC.

 |
