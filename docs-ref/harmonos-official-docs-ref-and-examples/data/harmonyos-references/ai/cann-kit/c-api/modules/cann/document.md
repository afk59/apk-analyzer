# CANN

#### Overview

Provides APIs for CANN Kit model inference.

**Syscap:** SystemCapability.AI.HiAIFoundation

**Since:** 4.1.0(11)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a2/v3/MGpKt6r9QEa2yexHLOA99A/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062521Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=60D75B3F0F4F4B4918304A2767C3B625915A03F0A29D7F4C9128FF12A441B00A)

The basic function APIs of CANN Kit, including those for model compilation, loading, and inference, have been consolidated into [neural\_network\_core.h](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-core-h/document.md). This section emphasizes advanced functions.

#### Summary

#### \[h2\]Files

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[hiai\_aipp\_param.h](../../header-files-and-structs/header-files/hiai-aipp-param-h/document.md)

 | 

APIs for creating dynamic AIPP objects and setting and querying relevant parameters for CANN Kit model inference.

 |
| 

[hiai\_helper.h](../../header-files-and-structs/header-files/hiai-helper-h/document.md)

 | 

Defines the APIs for querying the CANN Kit version and checking the model compatibility.

 |
| 

[hiai\_options.h](../../header-files-and-structs/header-files/hiai-options-h/document.md)

 | 

Defines the API for build options.

 |
| 

[hiai\_single\_op.h](../../header-files-and-structs/header-files/hiai-single-op-h/document.md)

 | 

Defines the single-operator APIs of CANN Kit, which is used for creating and calculating single operators, and managing tensors and buffers.

 |
| 

[hiai\_tensor.h](../../header-files-and-structs/header-files/hiai-tensor-h/document.md)

 | 

Auxiliary APIs related to input and output memory during CANN Kit model inference.

 |

#### \[h2\]Data Structures

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

struct [HiAISingleOpDescriptor\_ConvolutionParam](../../header-files-and-structs/structs/hiaisingleopdescriptor-convolutionparam/document.md)

 | 

[HMS\_HiAISingleOpDescriptor\_CreateConvolution](#hms_hiaisingleopdescriptor_createconvolution) input parameters.

 |
| 

struct [HiAI\_SingleOpExecutorConvolutionParam](../../header-files-and-structs/structs/hiai-singleopexecutorconvolutionparam/document.md)

 | 

[HMS\_HiAISingleOpExecutor\_CreateConvolution](#hms_hiaisingleopexecutor_createconvolution) input parameters.

 |
| 

struct [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../header-files-and-structs/structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md)

 | 

[HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](#hms_hiaisingleopexecutor_createfusedconvolutionactivation) input parameters.

 |

#### \[h2\]Typedefs

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

typedef struct [HiAI\_AippParam](#hiai_aippparam) [HiAI\_AippParam](#hiai_aippparam)

 | 

AIPP parameter object.

 |
| 

typedef struct [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc)

 | 

Single op tensor description handle.

 |
| 

typedef struct [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) [HiAI\_SingleOpBuffer](#hiai_singleopbuffer)

 | 

Single op buffer handle.

 |
| 

typedef struct [HiAI\_SingleOpTensor](#hiai_singleoptensor) [HiAI\_SingleOpTensor](#hiai_singleoptensor)

 | 

Single op tensor handle.

 |
| 

typedef struct [HiAI\_SingleOpOptions](#hiai_singleopoptions) [HiAI\_SingleOpOptions](#hiai_singleopoptions)

 | 

Single op option handle.

 |
| 

typedef struct [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor)

 | 

Single op operation description handle.

 |
| 

typedef struct [HiAISingleOpDescriptor\_ConvolutionParam](../../header-files-and-structs/structs/hiaisingleopdescriptor-convolutionparam/document.md) [HiAISingleOpDescriptor\_ConvolutionParam](#hiai_singleopdescriptorconvolutionparam)

 | 

[HMS\_HiAISingleOpDescriptor\_CreateConvolution](#hms_hiaisingleopdescriptor_createconvolution) input parameters.

 |
| 

typedef struct [HiAI\_SingleOpExecutorConvolutionParam](../../header-files-and-structs/structs/hiai-singleopexecutorconvolutionparam/document.md) [HiAI\_SingleOpExecutorConvolutionParam](#hiai_singleopexecutorconvolutionparam)

 | 

[HMS\_HiAISingleOpExecutor\_CreateConvolution](#hms_hiaisingleopexecutor_createconvolution) input parameters.

 |
| 

typedef struct [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../header-files-and-structs/structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md) [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](#hiai_singleopexecutorfusedconvolutionactivationparam)

 | 

[HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](#hms_hiaisingleopexecutor_createfusedconvolutionactivation) input parameters.

 |
| 

typedef struct [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) [HiAI\_SingleOpExecutor](#hiai_singleopexecutor)

 | 

Single op executor handle.

 |

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_ImageFormat](#hiai_imageformat) {

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

[HiAI\_ImageColorSpace](#hiai_imagecolorspace) {

HIAI\_JPEG = 0,

HIAI\_BT\_601\_NARROW = 1,

HIAI\_BT\_601\_FULL = 2,

HIAI\_BT\_709\_NARROW = 3,

HIAI\_IMAGE\_COLOR\_SPACE\_INVALID = 4

}

 | 

Image's color space type.

 |
| 

[HiAI\_Compatibility](#hiai_compatibility) {

HIAI\_COMPATIBILITY\_COMPATIBLE = 0,

HIAI\_COMPATIBILITY\_INCOMPATIBLE = 1

}

 | 

Model compatibility.

 |
| 

[HiAI\_FormatMode](#hiai_formatmode) {

HIAI\_FORMAT\_MODE\_NCHW = 0,

HIAI\_FORMAT\_MODE\_ORIGIN = 1

}

 | 

Data layout formats during model building.

 |
| 

[HiAI\_DynamicShapeStatus](#hiai_dynamicshapestatus) {

HIAI\_DYNAMIC\_SHAPE\_DISABLED = 0,

HIAI\_DYNAMIC\_SHAPE\_ENABLED = 1

}

 | 

Indicates whether to enable variable shapes before model building.

 |
| 

[HiAI\_DynamicShapeCacheMode](#hiai_dynamicshapecachemode) {

HIAI\_DYNAMIC\_SHAPE\_CACHE\_BUILT\_MODEL = 0,

HIAI\_DYNAMIC\_SHAPE\_CACHE\_LOADED\_MODEL = 1

}

 | 

Modes supported for the variable shapes before model building.

 |
| 

[HiAI\_ExecuteDevice](#hiai_executedevice) {

HIAI\_EXECUTE\_DEVICE\_NPU = 0,

HIAI\_EXECUTE\_DEVICE\_CPU = 1,

HIAI\_EXECUTE\_DEVICE\_GPU = 2

}

 | 

Device types supported for model running.

 |
| 

[HiAI\_FallbackMode](#hiai_fallbackmode) {

HIAI\_FALLBACK\_ENABLED = 0,

HIAI\_FALLBACK\_DISABLED = 1

}

 | 

Indicates whether to allow CANN Kit to select other devices, such as the CPU, when the specified device cannot build a model.

 |
| 

[HiAI\_DeviceMemoryReusePlan](#hiai_devicememoryreuseplan) {

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_UNSET = 0,

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_LOW = 1,

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_HIGH = 2

}

 | 

Device memory overcommitment option.

 |
| 

[HiAI\_TuningStrategy](#hiai_tuningstrategy) {

HIAI\_TUNING\_STRATEGY\_OFF = 0,

HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_TUNING = 1,

HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_PREPROCESS\_TUNING = 2,

HIAI\_TUNING\_STRATEGY\_ON\_CLOUD\_TUNING = 3

}

 | 

Configuration options of the model tuning strategy.

 |
| 

[HiAI\_TuningMode](#hiai_tuningmode) {

HIAI\_TUNING\_MODE\_UNSET = 0,

HIAI\_TUNING\_MODE\_AUTO = 1,

HIAI\_TUNING\_MODE\_HETER = 2

}

 | 

Assisted tuning mode.

 |
| 

[HiAI\_BandMode](#hiai_bandmode) {

HIAI\_BANDMODE\_UNSET = 0,

HIAI\_BANDMODE\_LOW = 1,

HIAI\_BANDMODE\_NORMAL = 2,

HIAI\_BANDMODE\_HIGH = 3

}

 | 

Defines the inter-device bandwidth mode.

 |
| 

[HiAI\_OmType](#hiai_omtype) {

HIAI\_OM\_TYPE\_OFF = 0,

HIAI\_OM\_TYPE\_PROFILING = 1,

HIAI\_OM\_TYPE\_DUMP = 2

}

 | 

Defines the operating and maintenance type.

 |
| 

[HiAI\_SingleOpDataType](#hiai_singleopdatatype) {

HIAI\_SINGLEOP\_DT\_FLOAT = 0,

HIAI\_SINGLEOP\_DT\_FLOAT16 = 1,

HIAI\_SINGLEOP\_DT\_UNDEFINED = 17

}

 | 

Defines the single op tensor data type enums.

 |
| 

[HiAI\_SingleOpFormat](#hiai_singleopformat) {

HIAI\_SINGLEOP\_FORMAT\_NCHW = 0,

HIAI\_SINGLEOP\_FORMAT\_NHWC = 1,

HIAI\_SINGLEOP\_FORMAT\_ND = 2,

HIAI\_SINGLEOP\_FORMAT\_NC1HWC0 = 3,

HIAI\_SINGLEOP\_FORMAT\_NC4HW4 = 28,

HIAI\_SINGLEOP\_FORMAT\_NC8HW8 = 31,

HIAI\_SINGLEOP\_FORMAT\_RESERVED = 255

}

 | 

Defines the single op tensor formats.

 |
| 

[HiAI\_SingleOpConvMode](#hiai_singleopconvmode) {

HIAI\_SINGLEOP\_CONV\_MODE\_COMMON = 0,

HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED = 1,

HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE = 2

}

 | 

Defines the single op convolution mode enums.

 |
| 

[HiAI\_SingleOpPadMode](#hiai_singleoppadmode) {

HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC = 0,

HIAI\_SINGLEOP\_PAD\_MODE\_SAME = 1,

HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_UPPER = 2,

HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_LOWER = 3,

HIAI\_SINGLEOP\_PAD\_MODE\_VALID = 4

}

 | 

Defines the single op padding mode enums.

 |
| 

[HiAI\_SingleOpActivationType](#hiai_singleopactivationtype) {

HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU = 0,

HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU6 = 1

}

 | 

Defines the single op activation mode enums.

 |
| 

[HiAI\_SingleOpSupportStatus](#hiai_singleopsupportstatus) {

HIAI\_SINGLEOP\_OPTIMIZED = 0,

HIAI\_SINGLEOP\_COMMON = 1,

HIAI\_SINGLEOP\_UNSUPPORTED = 2

}

 | 

Defines the single op support status enums.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_AippParam](#hiai_aippparam) \* [HMS\_HiAIAippParam\_Create](#hms_hiaiaippparam_create) (uint32\_t batchNum)

 | 

Creates a dynamic AippParam object based on batchNum.

 |
| 

void \* [HMS\_HiAIAippParam\_GetData](#hms_hiaiaippparam_getdata) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam)

 | 

Obtains the memory address requested for AippParam.

 |
| 

uint32\_t [HMS\_HiAIAippParam\_GetDataSize](#hms_hiaiaippparam_getdatasize) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam)

 | 

Obtains the memory size requested for AippParam.

 |
| 

int [HMS\_HiAIAippParam\_GetInputIndex](#hms_hiaiaippparam_getinputindex) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam)

 | 

Queries the input index of the AippParam object.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputIndex](#hms_hiaiaippparam_setinputindex) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t inputIndex)

 | 

Sets the input index of the AippParam object.

 |
| 

int [HMS\_HiAIAippParam\_GetInputAippIndex](#hms_hiaiaippparam_getinputaippindex) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam)

 | 

Queries the index of an output, in the scenario where the input linked with AippParam has more than one output.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputAippIndex](#hms_hiaiaippparam_setinputaippindex) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t inputAippIndex)

 | 

Sets the index of an output, in the scenario where the input linked with AippParam has more than one output.

 |
| 

void [HMS\_HiAIAippParam\_Destroy](#hms_hiaiaippparam_destroy) ([HiAI\_AippParam](#hiai_aippparam) \*\*aippParam)

 | 

Releases the AippParam object.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputFormat](#hms_hiaiaippparam_setinputformat) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](#hiai_imageformat) inputFormat)

 | 

Sets the input image format.

 |
| 

[HiAI\_ImageFormat](#hiai_imageformat) [HMS\_HiAIAippParam\_GetInputFormat](#hms_hiaiaippparam_getinputformat) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam)

 | 

Queries the input image format.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetInputShape](#hms_hiaiaippparam_setinputshape) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t srcImageW, uint32\_t srcImageH)

 | 

Sets the width and height of the input image.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetInputShape](#hms_hiaiaippparam_getinputshape) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t \*srcImageW, uint32\_t \*srcImageH)

 | 

Queries the width and height of the input image.

 |
| 

uint32\_t [HMS\_HiAIAippParam\_GetBatchCount](#hms_hiaiaippparam_getbatchcount) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam)

 | 

Queries the number of images set by AippParam.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetCscConfig](#hms_hiaiaippparam_setcscconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](#hiai_imageformat) inputFormat, [HiAI\_ImageFormat](#hiai_imageformat) outputFormat, [HiAI\_ImageColorSpace](#hiai_imagecolorspace) space)

 | 

Sets Color Space Conversion (CSC) parameters for AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetCscConfig](#hms_hiaiaippparam_getcscconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, [HiAI\_ImageFormat](#hiai_imageformat) \*inputFormat, [HiAI\_ImageFormat](#hiai_imageformat) \*outputFormat, [HiAI\_ImageColorSpace](#hiai_imagecolorspace) \*space)

 | 

Queries the CSC parameters of AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetChannelSwapConfig](#hms_hiaiaippparam_setchannelswapconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, bool rbuvSwapSwitch, bool axSwapSwitch)

 | 

Sets AIPP channel swapping parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetChannelSwapConfig](#hms_hiaiaippparam_getchannelswapconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, bool \*rbuvSwapSwitch, bool \*axSwapSwitch)

 | 

Queries AIPP channel swapping parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetSingleBatchMultiCrop](#hms_hiaiaippparam_setsinglebatchmulticrop) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, bool singleBatchMultiCrop)

 | 

Sets the SingleBatchMultiCrop flag of AIPP.

 |
| 

bool [HMS\_HiAIAippParam\_GetSingleBatchMultiCrop](#hms_hiaiaippparam_getsinglebatchmulticrop) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam)

 | 

Queries the SingleBatchMultiCrop flag of AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetCropConfig](#hms_hiaiaippparam_setcropconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t startPosW, uint32\_t startPosH, uint32\_t croppedW, uint32\_t croppedH)

 | 

Sets AIPP cropping parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetCropConfig](#hms_hiaiaippparam_getcropconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*startPosW, uint32\_t \*startPosH, uint32\_t \*croppedW, uint32\_t \*croppedH)

 | 

Queries AIPP cropping parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetResizeConfig](#hms_hiaiaippparam_setresizeconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t resizedW, uint32\_t resizedH)

 | 

Sets AIPP image resizing parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetResizeConfig](#hms_hiaiaippparam_getresizeconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*resizedW, uint32\_t \*resizedH)

 | 

Queries AIPP image resizing parameters.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetPadConfig](#hms_hiaiaippparam_setpadconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t leftPadSize, uint32\_t rightPadSize, uint32\_t topPadSize, uint32\_t bottomPadSize)

 | 

Sets the number of pixels padded to the input image by AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetPadConfig](#hms_hiaiaippparam_getpadconfig) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t \*leftPadSize, uint32\_t \*rightPadSize, uint32\_t \*topPadSize, uint32\_t \*bottomPadSize)

 | 

Queries the number of pixels padded to the input image by AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetChannelPadding](#hms_hiaiaippparam_setchannelpadding) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t paddingValues\[\], uint32\_t channelCount)

 | 

Sets the padding value for a channel during AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetChannelPadding](#hms_hiaiaippparam_getchannelpadding) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t paddingValues\[\], uint32\_t channelCount)

 | 

Queries the padding value for a channel during AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetRotationAngle](#hms_hiaiaippparam_setrotationangle) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float rotationAngle)

 | 

Sets the rotation angle in AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetRotationAngle](#hms_hiaiaippparam_getrotationangle) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float \*rotationAngle)

 | 

Queries the image rotation angle in AIPP.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcMeanPixel](#hms_hiaiaippparam_setdtcmeanpixel) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t meanPixel\[\], uint32\_t channelCount)

 | 

Sets the average pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcMeanPixel](#hms_hiaiaippparam_getdtcmeanpixel) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, uint32\_t meanPixel\[\], uint32\_t channelCount)

 | 

Queries the average pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcMinPixel](#hms_hiaiaippparam_setdtcminpixel) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float minPixel\[\], uint32\_t channelCount)

 | 

Sets the minimum pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcMinPixel](#hms_hiaiaippparam_getdtcminpixel) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float minPixel\[\], uint32\_t channelCount)

 | 

Queries the minimum pixel value of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_SetDtcVarReciPixel](#hms_hiaiaippparam_setdtcvarrecipixel) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float varReciPixel\[\], uint32\_t channelCount)

 | 

Sets the pixel variance of DTC.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIAippParam\_GetDtcVarReciPixel](#hms_hiaiaippparam_getdtcvarrecipixel) ([HiAI\_AippParam](#hiai_aippparam) \*aippParam, uint32\_t batchIndex, float varReciPixel\[\], uint32\_t channelCount)

 | 

Queries the pixel variance of DTC.

 |
| 

const char \* [HMS\_HiAI\_GetVersion](#hms_hiai_getversion) (void)

 | 

Obtains the CANN Kit version number. The result is in _hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3_ format, where **X****1** indicates whether NPU is supported. The value **0** indicates no and other values indicate yes.

 |
| 

[HiAI\_Compatibility](#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromFile](#hms_hiaicompatibility_checkfromfile) (const char \*file)

 | 

Queries the compatibility of the model stored in the file.

 |
| 

[HiAI\_Compatibility](#hiai_compatibility) [HMS\_HiAICompatibility\_CheckFromBuffer](#hms_hiaicompatibility_checkfrombuffer) (const void \*data, size\_t size)

 | 

Queries the compatibility of the model stored in the memory.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetInputTensorShapes](#hms_hiaioptions_setinputtensorshapes) (OH\_NNCompilation \*compilation, NN\_TensorDesc \*inputTensorDescs\[\], size\_t shapeCount)

 | 

Updates the model input's shape during model building.

 |
| 

size\_t [HMS\_HiAIOptions\_GetInputTensorShapeSize](#hms_hiaioptions_getinputtensorshapesize) (const OH\_NNCompilation \*compilation)

 | 

Queries the number of shape descriptions among the build options.

 |
| 

NN\_TensorDesc \* [HMS\_HiAIOptions\_GetInputTensorShape](#hms_hiaioptions_getinputtensorshape) (const OH\_NNCompilation \*compilation, size\_t index)

 | 

Queries the shape description of a specific index among the build options.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetFormatMode](#hms_hiaioptions_setformatmode) (OH\_NNCompilation \*compilation, [HiAI\_FormatMode](#hiai_formatmode) formatMode)

 | 

Sets the data layout format during model building.

 |
| 

[HiAI\_FormatMode](#hiai_formatmode) [HMS\_HiAIOptions\_GetFormatMode](#hms_hiaioptions_getformatmode) (const OH\_NNCompilation \*compilation)

 | 

Queries the data layout format among build options.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeStatus](#hms_hiaioptions_setdynamicshapestatus) (OH\_NNCompilation \*compilation, [HiAI\_DynamicShapeStatus](#hiai_dynamicshapestatus) status)

 | 

Sets the EnableMode parameter in the variable shape configuration before model building.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeMaxCache](#hms_hiaioptions_setdynamicshapemaxcache) (OH\_NNCompilation \*compilation, size\_t maxCacheCount)

 | 

Sets the maximum number of cached models in the variable shape configuration before model building.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeCacheMode](#hms_hiaioptions_setdynamicshapecachemode) (OH\_NNCompilation \*compilation, [HiAI\_DynamicShapeCacheMode](#hiai_dynamicshapecachemode) mode)

 | 

Sets the cache mode in the variable shape configuration before model building.

 |
| 

[HiAI\_DynamicShapeStatus](#hiai_dynamicshapestatus) [HMS\_HiAIOptions\_GetDynamicShapeStatus](#hms_hiaioptions_getdynamicshapestatus) (const OH\_NNCompilation \*compilation)

 | 

Queries the dynamic shape status parameter in the variable shape configuration before model building.

 |
| 

size\_t [HMS\_HiAIOptions\_GetDynamicShapeMaxCache](#hms_hiaioptions_getdynamicshapemaxcache) (const OH\_NNCompilation \*compilation)

 | 

Queries the maximum number of caches in the variable shape configuration before model building.

 |
| 

[HiAI\_DynamicShapeCacheMode](#hiai_dynamicshapecachemode) [HMS\_HiAIOptions\_GetDynamicShapeCacheMode](#hms_hiaioptions_getdynamicshapecachemode) (const OH\_NNCompilation \*compilation)

 | 

Queries the cacheMode parameter in the variable shape configuration before model building.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetOperatorDeviceOrder](#hms_hiaioptions_setoperatordeviceorder) (OH\_NNCompilation \*compilation, const char \*operatorName, [HiAI\_ExecuteDevice](#hiai_executedevice) \*executeDevices, size\_t deviceCount)

 | 

Sets the list of devices to execute operators in the operator-level tuning configuration.

 |
| 

size\_t [HMS\_HiAIOptions\_GetOperatorDeviceCount](#hms_hiaioptions_getoperatordevicecount) (const OH\_NNCompilation \*compilation, const char \*operatorName)

 | 

Queries the number of devices to execute a specific operator in the model from the operator-level tuning configuration.

 |
| 

[HiAI\_ExecuteDevice](#hiai_executedevice) \* [HMS\_HiAIOptions\_GetOperatorDeviceOrder](#hms_hiaioptions_getoperatordeviceorder) (const OH\_NNCompilation \*compilation, const char \*operatorName)

 | 

Queries the list of devices to execute a specific operator in the model from the operator-level tuning configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetModelDeviceOrder](#hms_hiaioptions_setmodeldeviceorder) (OH\_NNCompilation \*compilation, [HiAI\_ExecuteDevice](#hiai_executedevice) \*executeDevices, size\_t deviceCount)

 | 

Sets the list of devices to execute the model in the model-level tuning configuration.

 |
| 

size\_t [HMS\_HiAIOptions\_GetModelDeviceCount](#hms_hiaioptions_getmodeldevicecount) (const OH\_NNCompilation \*compilation)

 | 

Queries the number of devices to execute the model in the model-level tuning configuration.

 |
| 

[HiAI\_ExecuteDevice](#hiai_executedevice) \* [HMS\_HiAIOptions\_GetModelDeviceOrder](#hms_hiaioptions_getmodeldeviceorder) (const OH\_NNCompilation \*compilation)

 | 

Queries the list of devices to execute the model in the model-level tuning configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetFallbackMode](#hms_hiaioptions_setfallbackmode) (OH\_NNCompilation \*compilation, [HiAI\_FallbackMode](#hiai_fallbackmode) fallbackMode)

 | 

Sets the fallback mode in the tuning configuration.

 |
| 

[HiAI\_FallbackMode](#hiai_fallbackmode) [HMS\_HiAIOptions\_GetFallbackMode](#hms_hiaioptions_getfallbackmode) (const OH\_NNCompilation \*compilation)

 | 

Queries the fallback mode in the tuning configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDeviceMemoryReusePlan](#hms_hiaioptions_setdevicememoryreuseplan) (OH\_NNCompilation \*compilation, [HiAI\_DeviceMemoryReusePlan](#hiai_devicememoryreuseplan) deviceMemoryReusePlan)

 | 

Sets the device memory overcommitment parameters in the tuning configuration.

 |
| 

[HiAI\_DeviceMemoryReusePlan](#hiai_devicememoryreuseplan) [HMS\_HiAIOptions\_GetDeviceMemoryReusePlan](#hms_hiaioptions_getdevicememoryreuseplan) (const OH\_NNCompilation \*compilation)

 | 

Queries the device memory overcommitment parameters in the tuning configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningStrategy](#hms_hiaioptions_settuningstrategy) (OH\_NNCompilation \*compilation, [HiAI\_TuningStrategy](#hiai_tuningstrategy) tuningStrategy)

 | 

Sets the model tuning strategy during model building.

 |
| 

[HiAI\_TuningStrategy](#hiai_tuningstrategy) [HMS\_HiAIOptions\_GetTuningStrategy](#hms_hiaioptions_gettuningstrategy) (const OH\_NNCompilation \*compilation)

 | 

Queries the model tuning strategy.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetQuantConfig](#hms_hiaioptions_setquantconfig) (OH\_NNCompilation \*compilation, void \*data, size\_t size)

 | 

Sets the quantization configuration during model building.

 |
| 

void \* [HMS\_HiAIOptions\_GetQuantConfigData](#hms_hiaioptions_getquantconfigdata) (const OH\_NNCompilation \*compilation)

 | 

Queries the data address of the quantization configuration.

 |
| 

size\_t [HMS\_HiAIOptions\_GetQuantConfigSize](#hms_hiaioptions_getquantconfigsize) (const OH\_NNCompilation \*compilation)

 | 

Queries the data size of the quantization configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningMode](#hms_hiaioptions_settuningmode) (OH\_NNCompilation \*compilation, [HiAI\_TuningMode](#hiai_tuningmode) tuningMode)

 | 

Selects the assisted tuning mode.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningCacheDir](#hms_hiaioptions_settuningcachedir) (OH\_NNCompilation \*compilation, const char \*cacheDir)

 | 

Sets the cache directory for assisted tuning.

 |
| 

[HiAI\_TuningMode](#hiai_tuningmode) [HMS\_HiAIOptions\_GetTuningMode](#hms_hiaioptions_gettuningmode) (const OH\_NNCompilation \*compilation)

 | 

Queries the assisted tuning mode.

 |
| 

const char \* [HMS\_HiAIOptions\_GetTuningCacheDir](#hms_hiaioptions_gettuningcachedir) (const OH\_NNCompilation \*compilation)

 | 

Queries the cache directory for assisted tuning.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetBandMode](#hms_hiaioptions_setbandmode) (OH\_NNCompilation \*compilation, [HiAI\_BandMode](#hiai_bandmode) bandMode)

 | 

Sets the bandwidth mode for the NPU and peripheral input/output (I/O) devices.

 |
| 

[HiAI\_BandMode](#hiai_bandmode) [HMS\_HiAIOptions\_GetBandMode](#hms_hiaioptions_getbandmode) (const OH\_NNCompilation \*compilation)

 | 

Queries the bandwidth mode.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetOmOptions](#hms_hiaioptions_setomoptions) (OH\_NNCompilation \*compilation, [HiAI\_OmType](#hiai_omtype) type, const char \*outputDir)

 | 

Sets the operating and maintenance options for model loading.

 |
| 

[HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \* [HMS\_HiAISingleOpTensorDesc\_Create](#hms_hiaisingleoptensordesc_create) (const int64\_t \*dims, size\_t dimNum, [HiAI\_SingleOpDataType](#hiai_singleopdatatype) dataType, [HiAI\_SingleOpFormat](#hiai_singleopformat) format, bool isVirtual)

 | 

Creates a [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

 |
| 

size\_t [HMS\_HiAISingleOpTensorDesc\_GetDimensionCount](#hms_hiaisingleoptensordesc_getdimensioncount) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries the number of dimensions of the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

 |
| 

int64\_t [HMS\_HiAISingleOpTensorDesc\_GetDimension](#hms_hiaisingleoptensordesc_getdimension) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*tensorDesc, size\_t index)

 | 

Queries the length of a dimension with a specific index of the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

 |
| 

[HiAI\_SingleOpDataType](#hiai_singleopdatatype) [HMS\_HiAISingleOpTensorDesc\_GetDataType](#hms_hiaisingleoptensordesc_getdatatype) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries the data type of the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

 |
| 

[HiAI\_SingleOpFormat](#hiai_singleopformat) [HMS\_HiAISingleOpTensorDesc\_GetFormat](#hms_hiaisingleoptensordesc_getformat) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries format of the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

 |
| 

bool [HMS\_HiAISingleOpTensorDesc\_IsVirtual](#hms_hiaisingleoptensordesc_isvirtual) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries whether [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) describes a virtual tensor.

 |
| 

size\_t [HMS\_HiAISingleOpTensorDesc\_GetByteSize](#hms_hiaisingleoptensordesc_getbytesize) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*tensorDesc)

 | 

Queries the number of bytes occupied by the data calculated based on the dimension and data type of [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc).

 |
| 

void [HMS\_HiAISingleOpTensorDesc\_Destroy](#hms_hiaisingleoptensordesc_destroy) ([HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*\*tensorDesc)

 | 

Releases a [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

 |
| 

[HiAI\_SingleOpBuffer](#hiai_singleopbuffer) \* [HMS\_HiAISingleOpBuffer\_Create](#hms_hiaisingleopbuffer_create) (size\_t dataSize)

 | 

Creates a [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object based on the specific memory size.

 |
| 

size\_t [HMS\_HiAISingleOpBuffer\_GetSize](#hms_hiaisingleopbuffer_getsize) (const [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) \*buffer)

 | 

Queries the byte size of [HiAI\_SingleOpBuffer](#hiai_singleopbuffer).

 |
| 

void \* [HMS\_HiAISingleOpBuffer\_GetData](#hms_hiaisingleopbuffer_getdata) (const [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) \*buffer)

 | 

Queries the memory address of [HiAI\_SingleOpBuffer](#hiai_singleopbuffer).

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpBuffer\_Destroy](#hms_hiaisingleopbuffer_destroy) ([HiAI\_SingleOpBuffer](#hiai_singleopbuffer) \*\*buffer)

 | 

Releases a [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object.

 |
| 

[HiAI\_SingleOpTensor](#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](#hms_hiaisingleoptensor_createfromtensordesc) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*desc)

 | 

Creates a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc).

 |
| 

[HiAI\_SingleOpTensor](#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer](#hms_hiaisingleoptensor_createfromsingleopbuffer) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*desc, void \*data, size\_t dataSize)

 | 

Creates a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc), the memory address from [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) and data size.

 |
| 

[HiAI\_SingleOpTensor](#hiai_singleoptensor) \* [HMS\_HiAISingleOpTensor\_CreateFromConst](#hms_hiaisingleoptensor_createfromconst) (const [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*desc, void \*data, size\_t dataSize)

 | 

Creates a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc), the memory address and the size of constant data (such as the convolution weight and bias).

 |
| 

[HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \* [HMS\_HiAISingleOpTensor\_GetTensorDesc](#hms_hiaisingleoptensor_gettensordesc) (const [HiAI\_SingleOpTensor](#hiai_singleoptensor) \*tensor)

 | 

Obtains the tensor description of [HiAI\_SingleOpTensor](#hiai_singleoptensor).

 |
| 

[HiAI\_SingleOpBuffer](#hiai_singleopbuffer) \* [HMS\_HiAISingleOpTensor\_GetBuffer](#hms_hiaisingleoptensor_getbuffer) (const [HiAI\_SingleOpTensor](#hiai_singleoptensor) \*tensor)

 | 

Obtains the buffer of [HiAI\_SingleOpTensor](#hiai_singleoptensor).

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpTensor\_Destroy](#hms_hiaisingleoptensor_destroy) ([HiAI\_SingleOpTensor](#hiai_singleoptensor) \*\*tensor)

 | 

Releases a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object.

 |
| 

[HiAI\_SingleOpOptions](#hiai_singleopoptions) \* [HMS\_HiAISingleOpOptions\_Create](#hms_hiaisingleopoptions_create) (void)

 | 

Creates a [HiAI\_SingleOpOptions](#hiai_singleopoptions) object.

 |
| 

void [HMS\_HiAISingleOpOptions\_Destroy](#hms_hiaisingleopoptions_destroy) ([HiAI\_SingleOpOptions](#hiai_singleopoptions) \*\*options)

 | 

Releases a [HiAI\_SingleOpOptions](#hiai_singleopoptions) object.

 |
| 

[HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) \* [HMS\_HiAISingleOpDescriptor\_CreateConvolution](#hms_hiaisingleopdescriptor_createconvolution) ([HiAISingleOpDescriptor\_ConvolutionParam](../../header-files-and-structs/structs/hiaisingleopdescriptor-convolutionparam/document.md) param)

 | 

Creates a descriptor object of a convolution class (common convolution, transposed convolution, and depthwise convolution).

 |
| 

[HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) \* [HMS\_HiAISingleOpDescriptor\_CreateActivation](#hms_hiaisingleopdescriptor_createactivation) ([HiAI\_SingleOpActivationType](#hiai_singleopactivationtype) activationType, float coef)

 | 

Creates a descriptor object of the activation function class.

 |
| 

void [HMS\_HiAISingleOpDescriptor\_Destroy](#hms_hiaisingleopdescriptor_destroy) ([HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) \*\*opDesc)

 | 

Releases a [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) object.

 |
| 

[HiAI\_SingleOpSupportStatus](#hiai_singleopsupportstatus) [HMS\_HiAISingleOpExecutor\_PreCheckConvolution](#hms_hiaisingleopexecutor_precheckconvolution) ([HiAI\_SingleOpExecutorConvolutionParam](../../header-files-and-structs/structs/hiai-singleopexecutorconvolutionparam/document.md) param)

 | 

Pre-checks whether a convolution operation is supported or optimized.

 |
| 

[HiAI\_SingleOpSupportStatus](#hiai_singleopsupportstatus) [HMS\_HiAISingleOpExecutor\_PreCheckFusedConvolutionActivation](#hms_hiaisingleopexecutor_precheckfusedconvolutionactivation) ([HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../header-files-and-structs/structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md) param)

 | 

Pre-checks whether a fused convolution-and-activation operation is supported or optimized.

 |
| 

[HiAI\_SingleOpExecutor](#hiai_singleopexecutor) \* [HMS\_HiAISingleOpExecutor\_CreateConvolution](#hms_hiaisingleopexecutor_createconvolution) ([HiAI\_SingleOpExecutorConvolutionParam](../../header-files-and-structs/structs/hiai-singleopexecutorconvolutionparam/document.md) param)

 | 

Creates a [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object of a convolution operation.

 |
| 

[HiAI\_SingleOpExecutor](#hiai_singleopexecutor) \* [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](#hms_hiaisingleopexecutor_createfusedconvolutionactivation) ([HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../header-files-and-structs/structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md) param)

 | 

Creates a [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object of the fused convolution-and-activation operation.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc](#hms_hiaisingleopexecutor_updateoutputtensordesc) (const [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) \*executor, uint32\_t index, [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) \*output)

 | 

Updates the output tensor description of [HiAI\_SingleOpExecutor](#hiai_singleopexecutor).

 |
| 

size\_t [HMS\_HiAISingleOpExecutor\_GetWorkspaceSize](#hms_hiaisingleopexecutor_getworkspacesize) (const [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) \*executor)

 | 

Queries the size (in bytes) of the ION workspace memory required by [HiAI\_SingleOpExecutor](#hiai_singleopexecutor).

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Init](#hms_hiaisingleopexecutor_init) ([HiAI\_SingleOpExecutor](#hiai_singleopexecutor) \*executor, void \*workspace, size\_t workspaceSize)

 | 

Loads [HiAI\_SingleOpExecutor](#hiai_singleopexecutor).

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Execute](#hms_hiaisingleopexecutor_execute) ([HiAI\_SingleOpExecutor](#hiai_singleopexecutor) \*executor, [HiAI\_SingleOpTensor](#hiai_singleoptensor) \*input\[\], int32\_t inputNum, [HiAI\_SingleOpTensor](#hiai_singleoptensor) \*output\[\], int32\_t outputNum)

 | 

Performs synchronous inference.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAISingleOpExecutor\_Destroy](#hms_hiaisingleopexecutor_destroy) ([HiAI\_SingleOpExecutor](#hiai_singleopexecutor) \*\*executor)

 | 

Destroys the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object to release the memory occupied by the executor.

 |
| 

size\_t [HMS\_HiAITensor\_GetSizeWithImageFormat](#hms_hiaitensor_getsizewithimageformat) (NN\_TensorDesc \*desc, [HiAI\_ImageFormat](#hiai_imageformat) format)

 | 

Calculates the size of the tensor to be applied for based on NN\_TensorDesc and HiAI\_ImageFormat.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAITensor\_SetAippParams](#hms_hiaitensor_setaippparams) (NN\_Tensor \*tensor, [HiAI\_AippParam](#hiai_aippparam) \*aippParams\[\], size\_t aippNum)

 | 

Sets aippParams for NN\_Tensor.

 |

#### Typedef

#### \[h2\]HiAI\_AippParam

typedef struct HiAI\_AippParam HiAI\_AippParam

**Description**

AIPP parameter object.

**Since:** 4.1.0(11)

#### \[h2\]HiAI\_SingleOpBuffer

typedef struct HiAI\_SingleOpBuffer HiAI\_SingleOpBuffer

**Description**

Single op buffer handle.

**Since:** 5.0.0(12)

#### \[h2\]HiAI\_SingleOpDescriptor

typedef struct HiAI\_SingleOpDescriptor HiAI\_SingleOpDescriptor

**Description**

Single op operation description handle.

**Since:** 5.0.0(12)

#### \[h2\]HiAISingleOpDescriptor\_ConvolutionParam

typedef struct HiAISingleOpDescriptor\_ConvolutionParam HiAISingleOpDescriptor\_ConvolutionParam

**Description**

HiAISingleOpDescriptor\_CreateConvolution input parameters.

**Since:** 5.0.0(12)

#### \[h2\]HiAI\_SingleOpExecutor

typedef struct HiAI\_SingleOpExecutor HiAI\_SingleOpExecutor

**Description**

Single op executor handle.

**Since:** 5.0.0(12)

#### \[h2\]HiAI\_SingleOpExecutorConvolutionParam

typedef struct HiAI\_SingleOpExecutorConvolutionParam HiAI\_SingleOpExecutorConvolutionParam

**Description**

HMS\_HiAISingleOpExecutor\_CreateConvolution input parameters.

**Since:** 5.0.0(12)

#### \[h2\]HiAI\_SingleOpExecutorFusedConvolutionActivationParam

typedef struct HiAI\_SingleOpExecutorFusedConvolutionActivationParam HiAI\_SingleOpExecutorFusedConvolutionActivationParam

**Description**

HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation input parameters.

**Since:** 5.0.0(12)

#### \[h2\]HiAI\_SingleOpOptions

typedef struct HiAI\_SingleOpOptions HiAI\_SingleOpOptions

**Description**

Single op option handle.

**Since:** 5.0.0(12)

#### \[h2\]HiAI\_SingleOpTensor

typedef struct HiAI\_SingleOpTensor HiAI\_SingleOpTensor

**Description**

Single op tensor handle.

**Since:** 5.0.0(12)

#### \[h2\]HiAI\_SingleOpTensorDesc

typedef struct HiAI\_SingleOpTensorDesc HiAI\_SingleOpTensorDesc

**Description**

Single op tensor description handle.

**Since:** 5.0.0(12)

#### Enumeration Type

#### \[h2\]HiAI\_BandMode

enum HiAI\_BandMode

**Description**

Defines the inter-device bandwidth mode.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_BANDMODE\_UNSET

 | 

Automatically adjusted by the system.

 |
| 

HIAI\_BANDMODE\_LOW

 | 

Low bandwidth mode.

 |
| 

HIAI\_BANDMODE\_NORMAL

 | 

Medium bandwidth mode.

 |
| 

HIAI\_BANDMODE\_HIGH

 | 

High bandwidth mode.

 |

#### \[h2\]HiAI\_Compatibility

enum HiAI\_Compatibility

**Description**

Model compatibility.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_COMPATIBILITY\_COMPATIBLE

 | 

Model compatible.

 |
| 

HIAI\_COMPATIBILITY\_INCOMPATIBLE

 | 

Model incompatible.

 |

#### \[h2\]HiAI\_DeviceMemoryReusePlan

enum HiAI\_DeviceMemoryReusePlan

**Description**

Device memory overcommitment option.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_UNSET

 | 

Not used, which is the default value.

 |
| 

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_LOW

 | 

Low memory overcommitment rate. In this mode, the memory requested by the model is large, but the model inference performance is better.

 |
| 

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_HIGH

 | 

High memory overcommitment rate. In this mode, the memory requested by the model is small, but the model inference performance is inferior.

 |

#### \[h2\]HiAI\_DynamicShapeCacheMode

enum HiAI\_DynamicShapeCacheMode

**Description**

Modes supported for the variable shapes before model building.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_DYNAMIC\_SHAPE\_CACHE\_BUILT\_MODEL

 | 

Caches the built model. This is the default mode and features small memory usage.

 |
| 

HIAI\_DYNAMIC\_SHAPE\_CACHE\_LOADED\_MODEL

 | 

Caches the loaded model. This mode provides better performance.

 |

#### \[h2\]HiAI\_DynamicShapeStatus

enum HiAI\_DynamicShapeStatus

**Description**

Indicates whether to enable variable shapes before model building.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_DYNAMIC\_SHAPE\_DISABLED

 | 

Disables variable shapes before model building. This is the default value.

 |
| 

HIAI\_DYNAMIC\_SHAPE\_ENABLED

 | 

Enables variable shapes before model building.

 |

#### \[h2\]HiAI\_ExecuteDevice

enum HiAI\_ExecuteDevice

**Description**

Device types supported for model running.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_EXECUTE\_DEVICE\_NPU

 | 

NPU, which is the default value.

 |
| 

HIAI\_EXECUTE\_DEVICE\_CPU

 | 

CPU.

 |
| 

HIAI\_EXECUTE\_DEVICE\_GPU

 | 

GPU.

 |

#### \[h2\]HiAI\_FallbackMode

enum HiAI\_FallbackMode

**Description**

Indicates whether to allow CANN Kit to select other devices, such as the CPU, when the specified device cannot build a model.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_FALLBACK\_ENABLED

 | 

Yes, which is the default value.

 |
| 

HIAI\_FALLBACK\_DISABLED

 | 

No.

 |

#### \[h2\]HiAI\_FormatMode

enum HiAI\_FormatMode

**Description**

Data layout formats during model building.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_FORMAT\_MODE\_NCHW

 | 

NCHW format (default value).

 |
| 

HIAI\_FORMAT\_MODE\_ORIGIN

 | 

Original model format.

 |

#### \[h2\]HiAI\_ImageColorSpace

enum HiAI\_ImageColorSpace

**Description**

Image's color space type.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_JPEG

 | 

JPEG's color space.

 |
| 

HIAI\_BT\_601\_NARROW

 | 

BT.601 video range color space.

 |
| 

HIAI\_BT\_601\_FULL

 | 

BT.601 full range color space.

 |
| 

HIAI\_BT\_709\_NARROW

 | 

BT.709 video range color space.

 |
| 

HIAI\_IMAGE\_COLOR\_SPACE\_INVALID

 | 

Invalid color space type.

 |

#### \[h2\]HiAI\_ImageFormat

enum HiAI\_ImageFormat

**Description**

Image format enums of input and output tensors supported by CANN Kit inference.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_YUV420SP\_U8

 | 

YUV420SP\_U8 image.

 |
| 

HIAI\_XRGB8888\_U8

 | 

XRGB8888\_U8 image.

 |
| 

HIAI\_YUV400\_U8

 | 

YUV400\_U8 image.

 |
| 

HIAI\_ARGB8888\_U8

 | 

ARGB8888\_U8 image.

 |
| 

HIAI\_YUYV\_U8

 | 

YUYV\_U8 image.

 |
| 

HIAI\_YUV422SP\_U8

 | 

YUV422SP\_U8 image.

 |
| 

HIAI\_AYUV444\_U8

 | 

AYUV444\_U8 image.

 |
| 

HIAI\_RGB888\_U8

 | 

RGB888\_U8 image.

 |
| 

HIAI\_BGR888\_U8

 | 

BGR888\_U8 image.

 |
| 

HIAI\_YUV444SP\_U8

 | 

YUV444SP\_U8 image.

 |
| 

HIAI\_YVU444SP\_U8

 | 

YVU444SP\_U8 image.

 |
| 

HIAI\_IMAGE\_FORMAT\_INVALID

 | 

not support image.

 |

#### \[h2\]HiAI\_OmType

enum HiAI\_OmType

**Description**

Defines the operating and maintenance type.

**Since:** 5.1.0(18)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_OM\_TYPE\_OFF

 | 

Disables operating and maintenance.

 |
| 

HIAI\_OM\_TYPE\_PROFILING

 | 

Profiling type of operating and maintenance.

 |
| 

HIAI\_OM\_TYPE\_DUMP

 | 

Dump type of operating and maintenance.

**Start version:** 6.0.0(20)

 |

#### \[h2\]HiAI\_SingleOpActivationType

enum HiAI\_SingleOpActivationType

**Description**

Defines the single op activation mode enums.

**Since:** 5.0.0(12)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU

 | 

ReLU.

 |
| 

HIAI\_SINGLEOP\_ACTIVATION\_TYPE\_RELU6

 | 

ReLU6.

 |

#### \[h2\]HiAI\_SingleOpConvMode

enum HiAI\_SingleOpConvMode

**Description**

Defines the single op convolution mode enums.

**Since:** 5.0.0(12)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_SINGLEOP\_CONV\_MODE\_COMMON

 | 

Common convolution.

 |
| 

HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED

 | 

Transposed convolution.

 |
| 

HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE

 | 

Depthwise convolution.

 |

#### \[h2\]HiAI\_SingleOpDataType

enum HiAI\_SingleOpDataType

**Description**

Defines the single op tensor data type enums.

**Since:** 5.0.0(12)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_SINGLEOP\_DT\_FLOAT

 | 

float.

 |
| 

HIAI\_SINGLEOP\_DT\_FLOAT16

 | 

float16.

 |
| 

HIAI\_SINGLEOP\_DT\_UNDEFINED

 | 

Undefined.

 |

#### \[h2\]HiAI\_SingleOpFormat

enum HiAI\_SingleOpFormat

**Description**

Defines the single op tensor formats.

**Since:** 5.0.0(12)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_SINGLEOP\_FORMAT\_NCHW

 | 

NCHW format.

 |
| 

HIAI\_SINGLEOP\_FORMAT\_NHWC

 | 

NHWC format.

 |
| 

HIAI\_SINGLEOP\_FORMAT\_ND

 | 

ND format. Single op tensors in ND format layout are not currently supported.

 |
| 

HIAI\_SINGLEOP\_FORMAT\_NC1HWC0

 | 

NC1HWC0 format.

 |
| 

HIAI\_SINGLEOP\_FORMAT\_NC4HW4

 | 

NC4HW4 format.

 |
| 

HIAI\_SINGLEOP\_FORMAT\_NC8HW8

 | 

NC8HW8 format.

 |
| 

HIAI\_SINGLEOP\_FORMAT\_RESERVED

 | 

Undefined format.

 |

#### \[h2\]HiAI\_SingleOpPadMode

enum HiAI\_SingleOpPadMode

**Description**

Defines the single op padding mode enums.

**Since:** 5.0.0(12)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC

 | 

If no padding algorithm is set, padding settings specified by parameter **pads** will apply.

 |
| 

HIAI\_SINGLEOP\_PAD\_MODE\_SAME

 | 

Pads the input so that the output dimensions are the same as the input dimensions. The output dimensions are determined by ceil(input dimensions/strides).

 |
| 

HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_UPPER

 | 

SAME\_UPPER padding mode. In this mode, when the padding length is an odd number, the beginning padding length is less than or equal to the end padding length.

 |
| 

HIAI\_SINGLEOP\_PAD\_MODE\_SAME\_LOWER

 | 

SAME\_LOWER padding mode. In this mode, when the padding length is an odd number, the beginning padding length is greater than or equal to the end padding length.

 |
| 

HIAI\_SINGLEOP\_PAD\_MODE\_VALID

 | 

No padding is performed. The output dimensions are determined by ceil((input dimensions – filter dimensions + 1)/strides).

 |

#### \[h2\]HiAI\_SingleOpSupportStatus

enum HiAI\_SingleOpSupportStatus

**Description**

Defines the single op support status enums.

**Since:** 5.0.0(12)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_SINGLEOP\_OPTIMIZED

 | 

Performance optimized. It is recommended for user to use single op executor to perform single-operator inference computations.

 |
| 

HIAI\_SINGLEOP\_COMMON

 | 

Common performance. This single op executor is supported but it may yield small performance gains.

 |
| 

HIAI\_SINGLEOP\_UNSUPPORTED

 | 

Not supported. If users create this single op executor, it will fail.

 |

#### \[h2\]HiAI\_TuningMode

enum HiAI\_TuningMode

**Description**

Assisted tuning mode.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_TUNING\_MODE\_UNSET

 | 

Disables the tunning mode.

 |
| 

HIAI\_TUNING\_MODE\_AUTO

 | 

Automatic tuning mode, which is recommended. Tuning is controlled by the internal algorithm.

 |
| 

HIAI\_TUNING\_MODE\_HETER

 | 

Heterogeneous tuning mode.

 |

#### \[h2\]HiAI\_TuningStrategy

enum HiAI\_TuningStrategy

**Description**

Configuration options of the model tuning strategy.

**Since:** 4.1.0(11)

| 
Enumerator

 | 

Description

 |
| :-- | :-- |
| 

HIAI\_TUNING\_STRATEGY\_OFF

 | 

Neither in-depth convergence nor dynamic shape is supported, which is the default value.

 |
| 

HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_TUNING

 | 

In-depth convergence in dynamic shape mode is supported.

 |
| 

HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_PREPROCESS\_TUNING

 | 

In-depth convergence is supported for dynamic update of the NPU operator library.

 |
| 

HIAI\_TUNING\_STRATEGY\_ON\_CLOUD\_TUNING

 | 

Reserved for future uses and not used currently.

 |

#### Function

#### \[h2\]HMS\_HiAI\_GetVersion()

const char\* HMS\_HiAI\_GetVersion (void)

**Description**

Obtains the CANN Kit version number. The result is in _hiaiversion A1A2A3.X1X2X3.Y1Y2Y3.Z1Z2Z3_ format, where **X****1** indicates whether NPU is supported. The value **0** indicates no and other values indicate yes.

**Since:** 4.1.0(11)

**Returns:**

Returns the CANN Kit version number if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAIAippParam\_Create()

HiAI\_AippParam\* HMS\_HiAIAippParam\_Create (uint32\_t batchNum)

**Description**

Creates a dynamic AippParam object based on batchNum.

This method is used to create a dynamic AippParam object. You can apply for memory based on batchNum to store dynamic AIPP parameters. If [HiAI\_AippParam](#hiai_aippparam) not been used, call [HMS\_HiAIAippParam\_Destroy](#hms_hiaiaippparam_destroy) to release the pointer. Otherwise, memory leak may occur.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

batchNum

 | 

Batch size of the model input. The value range is (0, 127\].

 |

**Returns:**

Returns the pointer to [HiAI\_AippParam](#hiai_aippparam) if the operation is successful; returns a null pointer otherwise.

**See also:**

[HMS\_HiAIAippParam\_Destroy](#hms_hiaiaippparam_destroy)

#### \[h2\]HMS\_HiAIAippParam\_Destroy()

void HMS\_HiAIAippParam\_Destroy (HiAI\_AippParam \*\* aippParam)

**Description**

Releases the AippParam object.

This method is used to release [HiAI\_AippParam](#hiai_aippparam) created by using [HMS\_HiAIAippParam\_Create](#hms_hiaiaippparam_create).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null.

 |

#### \[h2\]HMS\_HiAIAippParam\_GetBatchCount()

uint32\_t HMS\_HiAIAippParam\_GetBatchCount (HiAI\_AippParam \* aippParam)

**Description**

Queries the number of images set by AippParam.

This method is used to query the number of images of aippParam based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. In the single-batch multi-crop scenario, this method queries the number of the cropped subimages. In the multi-batch single-crop scenario, this method queries the input batch value.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null.

 |

**Returns:**

Returns the number of images if the operation is successful; returns 0 otherwise.

#### \[h2\]HMS\_HiAIAippParam\_GetChannelPadding()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetChannelPadding (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t paddingValues\[\], uint32\_t channelCount)

**Description**

Queries the padding value for a channel of the AippParam object.

This method is used to query the padding value of a channel with a specific index based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

paddingValues\[\]

 | 

Arrays of channel padding value. The value range is \[-65504, 65504\]. The default value is 0.

 |
| 

channelCount

 | 

Number of channels to be padded. The value range is \[1, 4\]. For example, if channelCount is set to 3, channels chn0, chn1, and chn2 will be queried.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetChannelSwapConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetChannelSwapConfig (HiAI\_AippParam \* aippParam, bool \* rbuvSwapSwitch, bool \* axSwapSwitch)

**Description**

Queries AIPP channel swapping parameters.

This method is used to query channel swapping parameters based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

rbuvSwapSwitch

 | 

Flag indicating RB/UV channel swapping.

 |
| 

axSwapSwitch

 | 

Flag indicating AX channel swapping.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetCropConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetCropConfig (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t \* startPosW, uint32\_t \* startPosH, uint32\_t \* croppedW, uint32\_t \* croppedH)

**Description**

Queries AIPP cropping parameters.

This method is used to query cropping parameters with a specific index based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

startPosW

 | 

Horizontal coordinate of the crop start.

 |
| 

startPosH

 | 

Vertical coordinate of the crop start.

 |
| 

croppedW

 | 

Width of the cropped out image, in pixels.

 |
| 

croppedH

 | 

Height of the cropped out image, in pixels.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetCscConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetCscConfig (HiAI\_AippParam \* aippParam, HiAI\_ImageFormat \* inputFormat, HiAI\_ImageFormat \* outputFormat, HiAI\_ImageColorSpace \* space)

**Description**

Queries the CSC parameters of AIPP.

This method is used to query CSC parameters of AippParam based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

inputFormat

 | 

Image input format. For details, see [HiAI\_ImageFormat](#hiai_imageformat).

 |
| 

outputFormat

 | 

Image output format. For details, see [HiAI\_ImageFormat](#hiai_imageformat).

 |
| 

space

 | 

Image's color space type. For details, see [HiAI\_ImageColorSpace](#hiai_imagecolorspace).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetData()

void\* HMS\_HiAIAippParam\_GetData (HiAI\_AippParam \* aippParam)

**Description**

Obtains the memory address requested for AippParam.

This method is used to obtain the data memory address requested for [HiAI\_AippParam](#hiai_aippparam) through [HMS\_HiAIAippParam\_Create](#hms_hiaiaippparam_create). data points to the memory requested for AIPP parameters.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the memory address requested for AippParam if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAIAippParam\_GetDataSize()

uint32\_t HMS\_HiAIAippParam\_GetDataSize (HiAI\_AippParam \* aippParam)

**Description**

Obtains the memory size requested for AippParam.

This method is used to obtain the memory size requested for [HiAI\_AippParam](#hiai_aippparam) through [HMS\_HiAIAippParam\_Create](#hms_hiaiaippparam_create). size indicates the memory size requested for AIPP parameters.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, 0 is returned.

 |

**Returns:**

Returns the memory size requested for AippParam if the operation is successful; returns 0 otherwise.

#### \[h2\]HMS\_HiAIAippParam\_GetDtcMeanPixel()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetDtcMeanPixel (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t meanPixel\[\], uint32\_t channelCount)

**Description**

Queries the average pixel value of DTC.

This method is used to query the average pixel value of the data type with a specific index during DTC, based on the [HiAI\_AippParam](#hiai_aippparam) object for dynamic AIPP inference. This method must be used together with [HMS\_HiAIAippParam\_GetDtcMinPixel](#hms_hiaiaippparam_getdtcminpixel) and [HMS\_HiAIAippParam\_GetDtcVarReciPixel](#hms_hiaiaippparam_getdtcvarrecipixel), to obtain conversion parameters for all data types.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

meanPixel\[\]

 | 

Array of the average pixel values of channels. The array size is channelCount.

 |
| 

channelCount

 | 

Number of channels. The value range is \[1, 4\], and the channel starts from chn0. For example, if channelCount is 3, the data of channels chn0, chn1, and chn2 will be queried.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetDtcMinPixel()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetDtcMinPixel (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, float minPixel\[\], uint32\_t channelCount)

**Description**

Queries the minimum pixel value of DTC.

This method is used to query the minimum pixel value of the data type with a specific index during DTC, based on the [HiAI\_AippParam](#hiai_aippparam) object for dynamic AIPP inference. This method must be used together with [HMS\_HiAIAippParam\_GetDtcMeanPixel](#hms_hiaiaippparam_getdtcmeanpixel) and [HMS\_HiAIAippParam\_GetDtcVarReciPixel](#hms_hiaiaippparam_getdtcvarrecipixel), to obtain conversion parameters for all data types.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

minPixel\[\]

 | 

Array of the minimum pixel values of channels. The array size is channelCount.

 |
| 

channelCount

 | 

Number of channels. The value range is \[1,4\], and the channel starts from chn0. For example, if channelCount is 3, the data of channels chn0, chn1, and chn2 will be queried.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetDtcVarReciPixel()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetDtcVarReciPixel (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, float varReciPixel\[\], uint32\_t channelCount)

**Description**

Queries the pixel variance of DTC.

This method is used to query the pixel variance of the data type with a specific index during DTC, based on the [HiAI\_AippParam](#hiai_aippparam) object for dynamic AIPP inference. This method must be used together with [HMS\_HiAIAippParam\_GetDtcMeanPixel](#hms_hiaiaippparam_getdtcmeanpixel) and [HMS\_HiAIAippParam\_GetDtcMinPixel](#hms_hiaiaippparam_getdtcminpixel), to obtain conversion parameters for all data types.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

varReciPixel\[\]

 | 

Array of pixel variances of channels. The array size is channelCount.

 |
| 

channelCount

 | 

Number of channels. The value range is \[1, 4\], and the channel starts from chn0. For example, if channelCount is 3, the data of channels chn0, chn1, and chn2 will be queried.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetInputAippIndex()

int HMS\_HiAIAippParam\_GetInputAippIndex (HiAI\_AippParam \* aippParam)

**Description**

Queries the index of an output, in the scenario where the input linked with AippParam has more than one output.

This method is used to query the data node index of the AippParam object, in the case that the data node has more than one index.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, -1 is returned.

 |

**Returns:**

Returns the data node's index of the AippParam object if the operation is successful; returns -1 otherwise.

#### \[h2\]HMS\_HiAIAippParam\_GetInputFormat()

HiAI\_ImageFormat HMS\_HiAIAippParam\_GetInputFormat (HiAI\_AippParam \* aippParam)

**Description**

Queries the input image format.

This method is used to query the input image format based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, HIAI\_IMAGE\_FORMAT\_INVALID is returned.

 |

**Returns:**

Returns [HiAI\_ImageFormat](#hiai_imageformat) if the operation is successful; returns HIAI\_IMAGE\_FORMAT\_INVALID. otherwise.

#### \[h2\]HMS\_HiAIAippParam\_GetInputIndex()

int HMS\_HiAIAippParam\_GetInputIndex (HiAI\_AippParam \* aippParam)

**Description**

Queries the input index of the AippParam object.

This method is used to query the input index of the AippParam object in the case of multiple inputs.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, -1 is returned.

 |

**Returns:**

Returns the input index of the AippParam object if the operation is successful; returns -1 otherwise.

#### \[h2\]HMS\_HiAIAippParam\_GetInputShape()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetInputShape (HiAI\_AippParam \* aippParam, uint32\_t \* srcImageW, uint32\_t \* srcImageH)

**Description**

Queries the width and height of the input image.

This method is used to query the width and height of the input image based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

srcImageW

 | 

Width of the input image, in pixels.

 |
| 

srcImageH

 | 

Height of the input image, in pixels.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetPadConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetPadConfig (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t \* leftPadSize, uint32\_t \* rightPadSize, uint32\_t \* topPadSize, uint32\_t \* bottomPadSize)

**Description**

Queries the number of pixels padded to the input image by AIPP.

This method is used to query the number of pixels padded to an input image with a specific index based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. Also call [HMS\_HiAIAippParam\_GetChannelPadding](#hms_hiaiaippparam_getchannelpadding) if you want to query values padded to channels.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

leftPadSize

 | 

Number of pixels padded on the left of the image.

 |
| 

rightPadSize

 | 

Number of pixels padded on the right of the image.

 |
| 

topPadSize

 | 

Number of pixels padded on the top of the image.

 |
| 

bottomPadSize

 | 

Number of pixels padded on the bottom of the image.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetResizeConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetResizeConfig (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t \* resizedW, uint32\_t \* resizedH)

**Description**

Queries AIPP image resizing parameterst.

This method is used to query the width and height of the resized image with a specific index based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

resizedW

 | 

Width of the resized image, in pixels.

 |
| 

resizedH

 | 

Height of the resized image, in pixels.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetRotationAngle()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_GetRotationAngle (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, float \* rotationAngle)

**Description**

Queries the image rotation angle in AIPP.

This method is used to query the rotation angle of an image with a specific index based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

rotationAngle

 | 

Rotation angle.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_GetSingleBatchMultiCrop()

bool HMS\_HiAIAippParam\_GetSingleBatchMultiCrop (HiAI\_AippParam \* aippParam)

**Description**

Queries the SingleBatchMultiCrop flag of AIPP.

This method is used to query whether the single-batch multi-crop scenario is used based on the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null.

 |

**Returns:**

Returns true if the operation is successful; returns false otherwise.

#### \[h2\]HMS\_HiAIAippParam\_SetChannelPadding()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetChannelPadding (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t paddingValues\[\], uint32\_t channelCount)

**Description**

Sets the padding value for a channel during AIPP.

This method is used to set the padding value for a channel in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

paddingValues\[\]

 | 

Arrays of channel padding value. The value range is \[-65504, 65504\]. The default value is 0.

 |
| 

channelCount

 | 

Number of channels to be padded. The value range is \[1, 4\]. For example, if channelCount is set to 3, channels chn0, chn1, and chn2 will be configured.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetChannelSwapConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetChannelSwapConfig (HiAI\_AippParam \* aippParam, bool rbuvSwapSwitch, bool axSwapSwitch)

**Description**

Sets AIPP channel swapping parameters.

This method is used to set the channel swapping parameters of AippParam in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. AIPP supports RB/UV channel swapping and AX channel swapping. RB/UV channel swapping greatly enriches the input image formats. Once RB/UV channel swapping is enabled, input image formats supported by AIPP are double of the configured input formats.

| 
Configured image formats

 | 

Supported image formats

 |
| :-- | :-- |
| 

YUV420SP\_U8

 | 

YUV420SP\_U8，YVU420 + rbuv\_swap\_switch

 |
| 

XRGB8888\_U8

 | 

XRGB8888\_U8，XBGR + rbuv\_swap\_switch

 |
| 

ARGB8888\_U8

 | 

ARGB8888\_U8，ABGR + rbuv\_swap\_switch

 |
| 

RGB888\_U8

 | 

BGR888\_U8 + rbuv\_swap\_switch

 |
| 

BGR888\_U8

 | 

RGB888\_U8 + rbuv\_swap\_switch

 |
| 

YUYV\_U8

 | 

YUYV\_U8，YVYU\_U8 + rbuv\_swap\_switch

 |
| 

YUV422SP\_U8

 | 

YUV422SP\_U8，YVU422\_U8 + rbuv\_swap\_switch

 |
| 

AYUV444\_U8

 | 

AYUV444\_U8 + rbuv\_swap\_switch

 |

YUV400\_U8 is grayscale image, can't use channel swapping.

AX channel swapping applies to XRGB, ARGB, and AYUV image inputs. AX channel swapping moves the input of the first channel to the fourth channel. That is, with AX channel swapping enabled, XRGB, ARGB, and AYUV data are converted into RGBX, RGBA, and YUVA data. When the model training set consists of RGB images and the image input for inference is in XRGB or ARGB format, you can enable AX channel swapping to move the RGB channels forward for compatibility.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

rbuvSwapSwitch

 | 

Flag indicating RB/UV channel swapping.

 |
| 

axSwapSwitch

 | 

Flag indicating AX channel swapping.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetCropConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetCropConfig (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t startPosW, uint32\_t startPosH, uint32\_t croppedW, uint32\_t croppedH)

**Description**

Sets AIPP cropping parameters.

This method is used to set cropping parameters in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. As restricted by the YUV image type, when the input image type is YUV420SP, YUYV, YUV422SP, or AYUV444, the coordinates of the crop start and the width and height of the cropped out image must be even numbers.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

startPosW

 | 

Horizontal coordinate of the crop start. The value of startPosW must be less than the width of the input image.

 |
| 

startPosH

 | 

Vertical coordinate of the crop start. The value of startPosH must be less than the height of the input image.

 |
| 

croppedW

 | 

Width of the cropped out image. The sum of startPosW and croppedW must be less than or equal to the width of the input image.

 |
| 

croppedH

 | 

Height of the cropped out image. The sum of startPosH and croppedH must be less than or equal to the height of the input image.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetCscConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetCscConfig (HiAI\_AippParam \* aippParam, HiAI\_ImageFormat inputFormat, HiAI\_ImageFormat outputFormat, HiAI\_ImageColorSpace space)

**Description**

Sets Color Space Conversion (CSC) parameters for AIPP.

This method is used to set the CSC parameters in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. CSC refers to the conversion between the YUV and RGB image formats. If the input image is of the YUV (YUV420SP\_U8/YUYV\_U8/YUV422SP\_U8/AYUV444\_U8) format, the training set can consist of RGB888\_U8, BGR888\_U8, or grayscale (YUV400\_U8) images. If the input image is in RGB (XRGB8888\_U8/ARGB8888\_U8/RGB888\_U8/BGR888\_U8) format, the training set can consist of YUV444SP\_U8, YVU444SP\_U8, or grayscale (YUV400\_U8) images. Conversion from YUV400 to RGB or BGR is not supported.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

inputFormat

 | 

Image input format. For details, see [HiAI\_ImageFormat](#hiai_imageformat). HIAI\_YUV444SP\_U8 and HIAI\_YVU444SP\_U8 can't be used for the inputFormat parameter.

 |
| 

outputFormat

 | 

Image output format. For details, see [HiAI\_ImageFormat](#hiai_imageformat).

 |
| 

space

 | 

Image's color space type. For details, see [HiAI\_ImageColorSpace](#hiai_imagecolorspace).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetDtcMeanPixel()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcMeanPixel (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t meanPixel\[\], uint32\_t channelCount)

**Description**

Sets the average pixel value of DTC.

Data type conversion (DTC) is to convert pixel values of input images into data types used for model training. DTC parameters allow the converted data to fall within the expected range, which avoids forcible conversion. DTC is used to convert the input image type to the FP16 format using a conversion formula, and send the converted result to subsequent modules for further calculation. During the conversion, mean subtraction, minimum value subtraction, and multiplying the variance are performed in sequence.

Calculation formula: U8->FP16: pixelOutChn(i) = \[pixelInChn(i)–meanChn(i)–minChn(i)\] \* varReciChn(i), i ∈ \[0, 4) In the formula, pixelOutChn(i) indicates the output value of each channel of the DTC module, pixelInChn(i) indicates the input value of each channel of the DTC module, and meanChn(i) indicates the average input value of each channel. minChn(i) indicates the minimum input value of each channel, and varReciChn(i) indicates the input variance of each channel.

This method is used to set the average pixel value of DTC in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. This method must be used together with [HMS\_HiAIAippParam\_SetDtcMinPixel](#hms_hiaiaippparam_setdtcminpixel) and [HMS\_HiAIAippParam\_SetDtcVarReciPixel](#hms_hiaiaippparam_setdtcvarrecipixel).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

meanPixel\[\]

 | 

Array of the average pixel values of channels. The array size is channelCount. The default value is 0.

 |
| 

channelCount

 | 

Number of channels. The value range is \[1, 4\]. For example, if channelCount is set to 3, channels chn0, chn1, and chn2 will be configured.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetDtcMinPixel()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcMinPixel (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, float minPixel\[\], uint32\_t channelCount)

**Description**

Sets the minimum pixel value of DTC.

This method is used to set the minimum pixel value of DTC in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. This method must be used together with [HMS\_HiAIAippParam\_SetDtcMeanPixel](#hms_hiaiaippparam_setdtcmeanpixel) and [HMS\_HiAIAippParam\_SetDtcVarReciPixel](#hms_hiaiaippparam_setdtcvarrecipixel).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

minPixel\[\]

 | 

Array of the minimum pixel values of channels. The array size is channelCount. The default value is 0.

 |
| 

channelCount

 | 

Number of channels. The value range is \[1, 4\]. For example, if channelCount is set to 3, channels chn0, chn1, and chn2 will be configured.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetDtcVarReciPixel()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetDtcVarReciPixel (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, float varReciPixel\[\], uint32\_t channelCount)

**Description**

Sets the pixel variance of DTC.

This method is used to set the pixel variance of DTC in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. This method must be used together with [HMS\_HiAIAippParam\_SetDtcMeanPixel](#hms_hiaiaippparam_setdtcmeanpixel) and [HMS\_HiAIAippParam\_SetDtcMinPixel](#hms_hiaiaippparam_setdtcminpixel).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

varReciPixel\[\]

 | 

Array of pixel variances of channels. The array size is channelCount. The default value is 1.0.

 |
| 

channelCount

 | 

Number of channels. The value range is \[1, 4\]. For example, if channelCount is set to 3, channels chn0, chn1, and chn2 will be configured.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetInputAippIndex()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputAippIndex (HiAI\_AippParam \* aippParam, uint32\_t inputAippIndex)

**Description**

Sets the index of an output, in the scenario where the input linked with AippParam has more than one output.

This method is used to set the index of an output, in the scenario where the data linked with AippParam has more than one output.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null.

 |
| 

inputAippIndex

 | 

Identifies the output linked with the AIPP configuration, in the scenario where the input data has more than one output. The value starts from 0.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetInputFormat()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputFormat (HiAI\_AippParam \* aippParam, HiAI\_ImageFormat inputFormat)

**Description**

Sets the input image format.

This method is used to set the input image format in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. The image formats supported for AIPP are specified in [HiAI\_ImageFormat](#hiai_imageformat). 8-bit image. The value ranges from 0 to 255. HIAI\_YUV444SP\_U8 and HIAI\_YVU444SP\_U8 can't be used for the inputFormat parameter.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

inputFormat

 | 

Format of the input image. For details, see [HiAI\_ImageFormat](#hiai_imageformat).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetInputIndex()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputIndex (HiAI\_AippParam \* aippParam, uint32\_t inputIndex)

**Description**

Sets the input index of the AippParam object.

This method is used to set the index of the input linked with the AippParam object, in the case of multiple inputs.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null.

 |
| 

inputIndex

 | 

Sequence number of the model input linked with the AIPP parameter. The value starts from 0.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetInputShape()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetInputShape (HiAI\_AippParam \* aippParam, uint32\_t srcImageW, uint32\_t srcImageH)

**Description**

Sets the width and height of the input image.

This method is used to set the width and height of the input image in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

srcImageW

 | 

Width of the input image, in pixels. The value range is \[16, 4096\].

 |
| 

srcImageH

 | 

Height of the input image, in pixels. The value range is \[16, 4096\].

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetPadConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetPadConfig (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t leftPadSize, uint32\_t rightPadSize, uint32\_t topPadSize, uint32\_t bottomPadSize)

**Description**

Sets the number of pixels padded to the input image by AIPP.

This method is used to set the number of pixels padded to the input image in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. Pixels are padded to the left, right, top, and bottom of an image. Also call **HMS\_HiAIAippParam\_SetPadChannelValue** if you want to set values padded to channels.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

leftPadSize

 | 

Number of pixels padded on the left of the image. The width of the padded image must be the same as that in the original model dimension.

 |
| 

rightPadSize

 | 

Number of pixels padded on the right of the image. The width of the padded image must be the same as that in the original model dimension.

 |
| 

topPadSize

 | 

Number of pixels padded on the top of the image. The height of the padded image must be the same as that in the original model dimension.

 |
| 

bottomPadSize

 | 

Number of pixels padded on the bottom of the image. The height of the padded image must be the same as that in the original model dimension.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetResizeConfig()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetResizeConfig (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, uint32\_t resizedW, uint32\_t resizedH)

**Description**

Sets AIPP image resizing parameters.

This method is used to set image resizing parameters in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. Images are resized using the linear interpolation method.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

resizedW

 | 

Width of the resized image, in pixels. The value range is \[16, 448\]. The range of the width resize ratio is \[1/16, 16\].

 |
| 

resizedH

 | 

Height of the resized image, in pixels. The value range is \[16, 4096\]. The range of the height resize ratio is \[1/16, 16\].

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetRotationAngle()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetRotationAngle (HiAI\_AippParam \* aippParam, uint32\_t batchIndex, float rotationAngle)

**Description**

Sets the rotation angle in AIPP.

This method is used to set the rotation angle in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

batchIndex

 | 

Index of the input image in the multi-batch single-crop scenario or index of the cropped image in the single-batch multi-crop scenario.

 |
| 

rotationAngle

 | 

Rotation angle. The value can only be 0, 90, 180, or 270.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIAippParam\_SetSingleBatchMultiCrop()

OH\_NN\_ReturnCode HMS\_HiAIAippParam\_SetSingleBatchMultiCrop (HiAI\_AippParam \* aippParam, bool singleBatchMultiCrop)

**Description**

Sets the SingleBatchMultiCrop flag of AIPP.

This method is used to set the SingleBatchMultiCrop flag of AippParam in the [HiAI\_AippParam](#hiai_aippparam) object during dynamic AIPP inference. In the scenario where a single batch of images are input, multiple groups of AIPP parameters such as crop can be passed at a time. In this way, information about all key points such as the face can be obtained through one inference.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

aippParam

 | 

Pointer to [HiAI\_AippParam](#hiai_aippparam). The value cannot be null. Otherwise, an error code is returned.

 |
| 

singleBatchMultiCrop

 | 

Indicates whether the scenario is single-batch multi-crop.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAICompatibility\_CheckFromBuffer()

HiAI\_Compatibility HMS\_HiAICompatibility\_CheckFromBuffer (const void \* data, size\_t size)

**Description**

Queries the compatibility of the model stored in the memory.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

data

 | 

Model data address. The value cannot be null. Otherwise, a message indicating that the model is incompatible is returned.

 |
| 

size

 | 

Model data size. The value cannot be null. Otherwise, a message indicating that the model is incompatible is returned.

 |

**Returns:**

Returns [HiAI\_Compatibility](#hiai_compatibility) if the operation is successful; returns a message indicating that the model is incompatible otherwise.

#### \[h2\]HMS\_HiAICompatibility\_CheckFromFile()

HiAI\_Compatibility HMS\_HiAICompatibility\_CheckFromFile (const char \* file)

**Description**

Queries the compatibility of the model stored in the file.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

file

 | 

Path and name of the model file. The value cannot be empty, and the process must have the permission to access the model file. Otherwise, a message is returned indicating that the model is incompatible.

 |

**Returns:**

Returns [HiAI\_Compatibility](#hiai_compatibility) if the operation is successful; returns a message indicating that the model is incompatible otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetBandMode()

HiAI\_BandMode HMS\_HiAIOptions\_GetBandMode (const OH\_NNCompilation \* compilation)

**Description**

Queries the bandwidth mode.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, the default value is returned.

 |

**Returns:**

Returns the bandwidth mode [HiAI\_BandMode](#hiai_bandmode) if the operation is successful; returns the default value otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetDeviceMemoryReusePlan()

HiAI\_DeviceMemoryReusePlan HMS\_HiAIOptions\_GetDeviceMemoryReusePlan (const OH\_NNCompilation \* compilation)

**Description**

Queries the device memory overcommitment parameters in the tuning configuration.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, the default value is returned.

 |

**Returns:**

Returns [HiAI\_DeviceMemoryReusePlan](#hiai_devicememoryreuseplan) if the operation is successful; returns the default value otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetDynamicShapeCacheMode()

HiAI\_DynamicShapeCacheMode HMS\_HiAIOptions\_GetDynamicShapeCacheMode (const OH\_NNCompilation \* compilation)

**Description**

Queries the cacheMode parameter in the variable shape configuration before model building.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, the default value is returned.

 |

**Returns:**

Returns [HiAI\_DynamicShapeCacheMode](#hiai_dynamicshapecachemode) if the operation is successful; returns the default value otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetDynamicShapeMaxCache()

size\_t HMS\_HiAIOptions\_GetDynamicShapeMaxCache (const OH\_NNCompilation \* compilation)

**Description**

Queries the maximum number of caches in the variable shape configuration before model building.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, 0 is returned.

 |

**Returns:**

Returns the maximum number of caches if the operation is successful; returns 0 otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetDynamicShapeStatus()

HiAI\_DynamicShapeStatus HMS\_HiAIOptions\_GetDynamicShapeStatus (const OH\_NNCompilation \* compilation)

**Description**

Queries the dynamic shape status parameter in the variable shape configuration before model building.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, the default value is returned.

 |

**Returns:**

Returns [HiAI\_DynamicShapeStatus](#hiai_dynamicshapestatus) if the operation is successful; returns the default value otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetFallbackMode()

HiAI\_FallbackMode HMS\_HiAIOptions\_GetFallbackMode (const OH\_NNCompilation \* compilation)

**Description**

Queries the fallback mode in the tuning configuration.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, the default value is returned.

 |

**Returns:**

Returns [HiAI\_FallbackMode](#hiai_fallbackmode) if the operation is successful; returns the default value otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetFormatMode()

HiAI\_FormatMode HMS\_HiAIOptions\_GetFormatMode (const OH\_NNCompilation \* compilation)

**Description**

Queries the data layout format among build options.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, the default value is returned.

 |

**Returns:**

Returns [HiAI\_FormatMode](#hiai_formatmode) if the operation is successful; returns the default value otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetInputTensorShape()

NN\_TensorDesc\* HMS\_HiAIOptions\_GetInputTensorShape (const OH\_NNCompilation \* compilation, size\_t index)

**Description**

Queries the shape description of a specific index among the build options.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, a null pointer is returned.

 |
| 

index

 | 

Index of the input shape. The value is \[0, [HMS\_HiAIOptions\_GetInputTensorShapeSize](#hms_hiaioptions_getinputtensorshapesize)).

 |

**Returns:**

Returns the shape description among the build options if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetInputTensorShapeSize()

size\_t HMS\_HiAIOptions\_GetInputTensorShapeSize (const OH\_NNCompilation \* compilation)

**Description**

Queries the number of shape descriptions among the build options.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, 0 is returned.

 |

**Returns:**

Returns the number of shape descriptions among the build options if the operation is successful; returns 0 otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetModelDeviceCount()

size\_t HMS\_HiAIOptions\_GetModelDeviceCount (const OH\_NNCompilation \* compilation)

**Description**

Queries the number of devices to execute the model in the model-level tuning configuration.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, 0 is returned.

 |

**Returns:**

Returns the number of devices to execute the model if the operation is successful; returns 0 otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetModelDeviceOrder()

HiAI\_ExecuteDevice\* HMS\_HiAIOptions\_GetModelDeviceOrder (const OH\_NNCompilation \* compilation)

**Description**

Queries the list of devices to execute the model in the model-level tuning configuration.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the device list [HiAI\_ExecuteDevice](#hiai_executedevice) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetOperatorDeviceCount()

size\_t HMS\_HiAIOptions\_GetOperatorDeviceCount (const OH\_NNCompilation \* compilation, const char \* operatorName)

**Description**

Queries the number of devices to execute a specific operator in the model from the operator-level tuning configuration.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, 0 is returned.

 |
| 

operatorName

 | 

Operator name. The value cannot be null. Otherwise, 0 is returned.

 |

**Returns:**

Returns the number of devices to execute the operator if the operation is successful; returns 0 otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetOperatorDeviceOrder()

HiAI\_ExecuteDevice\* HMS\_HiAIOptions\_GetOperatorDeviceOrder (const OH\_NNCompilation \* compilation, const char \* operatorName)

**Description**

Queries the list of devices to execute a specific operator in the model from the operator-level tuning configuration.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, a null pointer is returned.

 |
| 

operatorName

 | 

Operator name. The value cannot be null. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the device list [HiAI\_ExecuteDevice](#hiai_executedevice) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetQuantConfigData()

void\* HMS\_HiAIOptions\_GetQuantConfigData (const OH\_NNCompilation \* compilation)

**Description**

Queries the data address of the quantization configuration.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the data address of the quantization configuration if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetQuantConfigSize()

size\_t HMS\_HiAIOptions\_GetQuantConfigSize (const OH\_NNCompilation \* compilation)

**Description**

Queries the data size of the quantization configuration.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, 0 is returned.

 |

**Returns:**

Returns the data size of the quantization configuration if the operation is successful; returns 0 otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetTuningCacheDir()

const char\* HMS\_HiAIOptions\_GetTuningCacheDir (const OH\_NNCompilation \* compilation)

**Description**

Queries the cache directory for assisted tuning.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the cache directory if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetTuningMode()

HiAI\_TuningMode HMS\_HiAIOptions\_GetTuningMode (const OH\_NNCompilation \* compilation)

**Description**

Queries the assisted tuning mode.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, the default value is returned.

 |

**Returns:**

Returns the assisted tuning mode [HiAI\_TuningMode](#hiai_tuningmode) if the operation is successful; returns the default value otherwise.

#### \[h2\]HMS\_HiAIOptions\_GetTuningStrategy()

HiAI\_TuningStrategy HMS\_HiAIOptions\_GetTuningStrategy (const OH\_NNCompilation \* compilation)

**Description**

Queries the model tuning strategy.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, the default value is returned.

 |

**Returns:**

Returns [HiAI\_TuningStrategy](#hiai_tuningstrategy) if the operation is successful; returns the default value otherwise.

#### \[h2\]HMS\_HiAIOptions\_SetBandMode()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetBandMode (OH\_NNCompilation \* compilation, HiAI\_BandMode bandMode)

**Description**

Sets the bandwidth mode for the NPU and peripheral input/output (I/O) devices.

Set this parameter as required. Note that a high bandwidth will lead to a high consumption.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

bandMode

 | 

Bandwidth mode [HiAI\_BandMode](#hiai_bandmode).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetDeviceMemoryReusePlan()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetDeviceMemoryReusePlan (OH\_NNCompilation \* compilation, HiAI\_DeviceMemoryReusePlan deviceMemoryReusePlan)

**Description**

Sets the device memory overcommitment parameters in the tuning configuration.

This method takes effect only in the model building phase. It specifies the device memory overcommitment mode during tuning.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

deviceMemoryReusePlan

 | 

Device memory overcommitment mode [HiAI\_DeviceMemoryReusePlan](#hiai_devicememoryreuseplan).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetDynamicShapeCacheMode()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetDynamicShapeCacheMode (OH\_NNCompilation \* compilation, HiAI\_DynamicShapeCacheMode mode)

**Description**

Sets the cache mode in the variable shape configuration before model building.

This method takes effect only in the model building phase and applies when the shape is expected to be updated in the inference phase and the number of updated shapes does not exceed 10. This method must be used together with [HMS\_HiAIOptions\_SetDynamicShapeStatus](#hms_hiaioptions_setdynamicshapestatus) and [HMS\_HiAIOptions\_SetDynamicShapeMaxCache](#hms_hiaioptions_setdynamicshapemaxcache).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

mode

 | 

Cache mode for variable shapes before model building ([HiAI\_DynamicShapeCacheMode](#hiai_dynamicshapecachemode)).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetDynamicShapeMaxCache()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetDynamicShapeMaxCache (OH\_NNCompilation \* compilation, size\_t maxCacheCount)

**Description**

Sets the maximum number of cached models in the variable shape configuration before model building.

This method takes effect only in the model building phase and applies when the shape is expected to be updated in the inference phase and the number of updated shapes does not exceed 10. This method must be used together with [HMS\_HiAIOptions\_SetDynamicShapeStatus](#hms_hiaioptions_setdynamicshapestatus) and [HMS\_HiAIOptions\_SetDynamicShapeCacheMode](#hms_hiaioptions_setdynamicshapecachemode).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

maxCacheCount

 | 

Maximum level. The value range is \[1,10\].

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetDynamicShapeStatus()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetDynamicShapeStatus (OH\_NNCompilation \* compilation, HiAI\_DynamicShapeStatus status)

**Description**

Sets the EnableMode parameter in the variable shape configuration before model building.

This method takes effect only in the model building phase and applies when the shape is expected to be updated in the inference phase and the number of updated shapes does not exceed 10. This method must be used together with [HMS\_HiAIOptions\_SetDynamicShapeMaxCache](#hms_hiaioptions_setdynamicshapemaxcache) and [HMS\_HiAIOptions\_SetDynamicShapeCacheMode](#hms_hiaioptions_setdynamicshapecachemode).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

status

 | 

Indicates whether to enable variable shapes before model building ([HiAI\_DynamicShapeStatus](#hiai_dynamicshapestatus)).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetFallbackMode()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetFallbackMode (OH\_NNCompilation \* compilation, HiAI\_FallbackMode fallbackMode)

**Description**

Sets the fallback mode in the tuning configuration.

This method takes effect only in the model building phase. It specifies whether to enable the fallback mode when the specified device list is not supported, in operator-level or model-level tuning.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

fallbackMode

 | 

Indicates whether to enable the fallback mode ([HiAI\_FallbackMode](#hiai_fallbackmode)).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetFormatMode()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetFormatMode (OH\_NNCompilation \* compilation, HiAI\_FormatMode formatMode)

**Description**

Sets the data layout format during model building.

This method takes effect only in the model building phase and applies when the data layout formats are different from the default values.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null.

 |
| 

formatMode

 | 

Data layout formats [HiAI\_FormatMode](#hiai_formatmode).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetInputTensorShapes()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetInputTensorShapes (OH\_NNCompilation \* compilation, NN\_TensorDesc \* inputTensorDescs\[\], size\_t shapeCount)

**Description**

Updates the model input's shape during model building.

This method takes effect only in the model building phase and applies when the model structure and weight remain unchanged but the shapes of model inputs need to be updated. The array size must be the same as the number of model inputs. After the model is compiled, the model inputs' shapes will be updated. During inference, the input and output data must comply with the new input and output description.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null.

 |
| 

inputTensorDescs\[\]

 | 

Array of model inputs' shape list **NN\_TensorDesc**. The value cannot be null.

 |
| 

shapeCount

 | 

Number of input shapes, which must be consistent with the number of model inputs.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetModelDeviceOrder()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetModelDeviceOrder (OH\_NNCompilation \* compilation, HiAI\_ExecuteDevice \* executeDevices, size\_t deviceCount)

**Description**

Sets the list of devices to execute the model in the model-level tuning configuration.

This method takes effect only in the model building phase and cannot be used together with other tuning methods. It specifies the list of devices that execute the model. The devices are sorted by priority. NPU takes the higher priority by default.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

executeDevices

 | 

List of supported device types [HiAI\_ExecuteDevice](#hiai_executedevice). The value cannot be null. Otherwise, an error code is returned.

 |
| 

deviceCount

 | 

Number of supported devices.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetOmOptions()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetOmOptions (OH\_NNCompilation \* compilation, HiAI\_OmType type, const char \* outputDir)

**Description**

Sets the operating and maintenance options for model loading.

This API is optional and takes effect during model loading. It is used to debug model performance.

**Since:** 5.1.0(18)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code will be returned.

 |
| 

type

 | 

Operating and maintenance type [HiAI\_OmType](#hiai_omtype)。

 |
| 

outputDir

 | 

Output directory used to store profiling files.

 |

**Returns:**

Function execution result. If the operation is successful, OH\_NN\_SUCCESS is returned. If the operation fails, an error code is returned. For details about the error codes, please refer to [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetOperatorDeviceOrder()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetOperatorDeviceOrder (OH\_NNCompilation \* compilation, const char \* operatorName, HiAI\_ExecuteDevice \* executeDevices, size\_t deviceCount)

**Description**

Sets the list of devices to execute operators in the operator-level tuning configuration.

This method takes effect only in the model building phase and cannot be used together with other tuning methods. It specifies the list of devices to execute operators in the model. Make sure that the devices are sorted by priority and operator names are unique. You can specify the device for some of the operators in the model. NPU will be used preferentially for operators with no device specified. You can check the operator names using Netron, which is an open-source tool.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

operatorName

 | 

Operator name. The value cannot be null. Otherwise, an error code is returned.

 |
| 

executeDevices

 | 

List of supported device types [HiAI\_ExecuteDevice](#hiai_executedevice). The value cannot be null. Otherwise, an error code is returned.

 |
| 

deviceCount

 | 

Number of supported devices.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetQuantConfig()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetQuantConfig (OH\_NNCompilation \* compilation, void \* data, size\_t size)

**Description**

Sets the quantization configuration during model building.

This method takes effect only in the model building phase and is used for quantization during model building.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

data

 | 

Data address of the quantization configuration. The value cannot be null. Otherwise, an error code is returned.

 |
| 

size

 | 

Data size of the quantization configuration. The value must be greater than 0. Otherwise, an error code is returned.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetTuningCacheDir()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningCacheDir (OH\_NNCompilation \* compilation, const char \* cacheDir)

**Description**

Sets the cache directory for assisted tuning.

The user process must have the read and write permissions on the cache directory. This method must be used together with [HMS\_HiAIOptions\_SetTuningMode](#hms_hiaioptions_settuningmode).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

cacheDir

 | 

Cache directory. The value cannot be null. Otherwise, an error code is returned.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetTuningMode()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningMode (OH\_NNCompilation \* compilation, HiAI\_TuningMode tuningMode)

**Description**

Selects the assisted tuning mode.

This method takes effect only in the model building phase and cannot be used together with other tuning methods. It enables HiAI-assisted tuning. This method must be used together with [HMS\_HiAIOptions\_SetTuningCacheDir](#hms_hiaioptions_settuningcachedir).

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

tuningMode

 | 

Assisted tuning mode [HiAI\_TuningMode](#hiai_tuningmode).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAIOptions\_SetTuningStrategy()

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningStrategy (OH\_NNCompilation \* compilation, HiAI\_TuningStrategy tuningStrategy)

**Description**

Sets the model tuning strategy during model building.

This method takes effect only in the model building phase and applies for in-depth convergence.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

compilation

 | 

Pointer to **OH\_NNCompilation**. The value cannot be null. Otherwise, an error code is returned.

 |
| 

tuningStrategy

 | 

Model tuning strategy [HiAI\_TuningStrategy](#hiai_tuningstrategy).

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAISingleOpBuffer\_Create()

HiAI\_SingleOpBuffer\* HMS\_HiAISingleOpBuffer\_Create (size\_t dataSize)

**Description**

Creates a [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object based on the specific memory size.

This method is used to apply for ION memory based on the specified **dataSize** and create a [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object. When you no longer use [HiAI\_SingleOpBuffer](#hiai_singleopbuffer), call [HMS\_HiAISingleOpBuffer\_Destroy](#hms_hiaisingleopbuffer_destroy) to destroy it. Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

dataSize

 | 

Size of the memory to be applied for, in bytes. The value cannot be 0. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpBuffer\_Destroy()

OH\_NN\_ReturnCode HMS\_HiAISingleOpBuffer\_Destroy (HiAI\_SingleOpBuffer \*\* buffer)

**Description**

Releases a [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object.

This method is used to release the [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object created by calling [HMS\_HiAISingleOpBuffer\_Create](#hms_hiaisingleopbuffer_create).

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

buffer

 | 

Double pointer to the [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object. **buffer** and **\*buffer** cannot be null pointers. Otherwise, an error code is returned.

 |

**Returns:**

Function execution result. If the operation is successful, OH\_NN\_SUCCESS is returned. If the operation fails, an error code is returned. For details about the error codes, please refer to [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAISingleOpBuffer\_GetData()

void\* HMS\_HiAISingleOpBuffer\_GetData (const HiAI\_SingleOpBuffer \* buffer)

**Description**

Queries the memory address of [HiAI\_SingleOpBuffer](#hiai_singleopbuffer).

This method is used to obtain the memory address of the specific [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

buffer

 | 

Pointer to the [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object. The value cannot be a null pointer. Otherwise, a null pointer is returned.

 |

**Returns:**

Memory address of the buffer.

#### \[h2\]HMS\_HiAISingleOpBuffer\_GetSize()

size\_t HMS\_HiAISingleOpBuffer\_GetSize (const HiAI\_SingleOpBuffer \* buffer)

**Description**

Queries the byte size of [HiAI\_SingleOpBuffer](#hiai_singleopbuffer).

This method is used to obtain the byte size of the specific [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

buffer

 | 

Pointer to the [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object. The value cannot be a null pointer. Otherwise, 0 is returned.

 |

**Returns:**

Size of the buffer, in bytes.

#### \[h2\]HMS\_HiAISingleOpDescriptor\_CreateActivation()

HiAI\_SingleOpDescriptor\* HMS\_HiAISingleOpDescriptor\_CreateActivation (HiAI\_SingleOpActivationType activationType, float coef)

**Description**

Creates a descriptor object of the activation function class.

This method is used to create a [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) object of the activation function class according to the input parameters. When you no longer use [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor), call [HMS\_HiAISingleOpDescriptor\_Destroy](#hms_hiaisingleopdescriptor_destroy) to destroy it. Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

activationType

 | 

Activation mode.

 |
| 

coef

 | 

If the activation comes with a coefficient, the value indicates the coefficient. Otherwise, the value does not take effect.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpDescriptor\_CreateConvolution()

HiAI\_SingleOpDescriptor\* HMS\_HiAISingleOpDescriptor\_CreateConvolution (HiAISingleOpDescriptor\_ConvolutionParam param)

**Description**

Creates a descriptor object of a convolution class (common convolution, transposed convolution, and depthwise convolution).

This method is used to create a [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) object of the convolution class according to the input parameters. When you no longer use [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor), call [HMS\_HiAISingleOpDescriptor\_Destroy](#hms_hiaisingleopdescriptor_destroy) to destroy it. Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

param

 | 

Refer to [HiAISingleOpDescriptor\_ConvolutionParam](../../header-files-and-structs/structs/hiaisingleopdescriptor-convolutionparam/document.md) for details of the input parameters.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpDescriptor\_Destroy()

void HMS\_HiAISingleOpDescriptor\_Destroy (HiAI\_SingleOpDescriptor \*\* opDesc)

**Description**

Releases a [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) object.

When you no longer use the [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) object, destroy it by calling the API. Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

opDesc

 | 

Double pointer to the [HiAI\_SingleOpDescriptor](#hiai_singleopdescriptor) object. **opDesc** and **\*opDesc** cannot be null pointers, otherwise the destroying fails.

 |

#### \[h2\]HMS\_HiAISingleOpExecutor\_CreateConvolution()

HiAI\_SingleOpExecutor\* HMS\_HiAISingleOpExecutor\_CreateConvolution (HiAI\_SingleOpExecutorConvolutionParam param)

**Description**

Creates a [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object of a convolution operation.

When you no longer use the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object, call [HMS\_HiAISingleOpExecutor\_Destroy](#hms_hiaisingleopexecutor_destroy) to destroy it. Otherwise, a memory leak may occur.

The data type and format of an output tensor description can respectively be HIAI\_SINGLEOP\_DT\_UNDEFINED and HIAI\_SINGLEOP\_FORMAT\_RESERVED. In this case, the executor sets the output data type and the format to the optimal values that adapt to the hardware. After this API is successfully executed, you can call [HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc](#hms_hiaisingleopexecutor_updateoutputtensordesc) to update the data type and format of the output tensor description.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

param

 | 

Refer to [HiAI\_SingleOpExecutorConvolutionParam](../../header-files-and-structs/structs/hiai-singleopexecutorconvolutionparam/document.md) for details of the input parameters.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation()

HiAI\_SingleOpExecutor\* HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation (HiAI\_SingleOpExecutorFusedConvolutionActivationParam param)

**Description**

Creates a [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object of the fused convolution-and-activation operation.

When you no longer use [HiAI\_SingleOpExecutor](#hiai_singleopexecutor), call [HMS\_HiAISingleOpExecutor\_Destroy](#hms_hiaisingleopexecutor_destroy) to destroy it. Otherwise, a memory leak may occur.

The data type and format of an output tensor description can respectively be HIAI\_SINGLEOP\_DT\_UNDEFINED and HIAI\_SINGLEOP\_FORMAT\_RESERVED. In this case, the executor sets the output data type and format to the optimal values that adapt to the hardware. After this API is successfully executed, you can call [HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc](#hms_hiaisingleopexecutor_updateoutputtensordesc) to update the data type and format of the output tensor description.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

param

 | 

Refer to [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../header-files-and-structs/structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md) for details of the input parameters.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpExecutor\_Destroy()

OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Destroy (HiAI\_SingleOpExecutor \*\* executor)

**Description**

Destroys the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object to release the memory occupied by the executor.

When you no longer use the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object, destroy it by calling the API. Otherwise, a memory leak may occur.

Note: This API does not release the workspace memory passed to [HMS\_HiAISingleOpExecutor\_Init](#hms_hiaisingleopexecutor_init). You need to release the workspace memory of [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) separately.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

executor

 | 

Double pointer to the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object. **executor** and **\*executor** cannot be null pointers. Otherwise, an error code is returned.

 |

**Returns:**

Function execution result. If the operation is successful, OH\_NN\_SUCCESS is returned. If the operation fails, an error code is returned. For details about the error codes, please refer to [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAISingleOpExecutor\_Execute()

OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Execute (HiAI\_SingleOpExecutor \* executor, HiAI\_SingleOpTensor \* input\[\], int32\_t inputNum, HiAI\_SingleOpTensor \* output\[\], int32\_t outputNum)

**Description**

Performs synchronous inference.

Before calling this API, call [HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](#hms_hiaisingleoptensor_createfromtensordesc) or [HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer](#hms_hiaisingleoptensor_createfromsingleopbuffer) to create the input and output tensors and fill the input tensors with data. The executor performs inference, and writes the result to the output tensors.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

executor

 | 

Pointer to the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object. The value cannot be a null pointer. Otherwise, an error code is returned.

 |
| 

input\[\]

 | 

Array of input tensors.

 |
| 

inputNum

 | 

Number of input tensors.

 |
| 

output\[\]

 | 

Array of output tensors.

 |
| 

outputNum

 | 

Number of output tensors.

 |

**Returns:**

Function execution result. If the operation is successful, OH\_NN\_SUCCESS is returned. If the operation fails, an error code is returned. For details about the error codes, please refer to [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAISingleOpExecutor\_GetWorkspaceSize()

size\_t HMS\_HiAISingleOpExecutor\_GetWorkspaceSize (const HiAI\_SingleOpExecutor \* executor)

**Description**

Queries the size (in bytes) of the ION workspace memory required by [HiAI\_SingleOpExecutor](#hiai_singleopexecutor).

After [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) is successfully created, you need call this API to obtain the size (in bytes) of the ION workspace memory required by the executor. You need to call [HMS\_HiAISingleOpBuffer\_Create](#hms_hiaisingleopbuffer_create) to apply for adequate memory, then pass the allocated memory to the [HMS\_HiAISingleOpExecutor\_Init](#hms_hiaisingleopexecutor_init) API.

Note: The workspace memory cannot reuse the input tensor memory and the output tensor memory of the same executor. The workspace memory from different executors can be reused.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

executor

 | 

Pointer to the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object. The value cannot be a null pointer. Otherwise, 0 is returned.

 |

**Returns:**

Size of the workspace, in bytes.

#### \[h2\]HMS\_HiAISingleOpExecutor\_Init()

OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_Init (HiAI\_SingleOpExecutor \* executor, void \* workspace, size\_t workspaceSize)

**Description**

Loads [HiAI\_SingleOpExecutor](#hiai_singleopexecutor).

Before calling this API, you need to apply for the workspace memory required by the executor.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

executor

 | 

Pointer to the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object. The value cannot be a null pointer. Otherwise, an error code is returned.

 |
| 

workspace

 | 

Workspace address. When **workspaceSize** is not 0, the value must be a memory address from [HiAI\_SingleOpBuffer](#hiai_singleopbuffer). Otherwise, an error code is returned.

 |
| 

workspaceSize

 | 

Size of the provided **workspace**, in bytes. The value must be greater than or equal to the size of the required workspace obtained by [HMS\_HiAISingleOpExecutor\_GetWorkspaceSize](#hms_hiaisingleopexecutor_getworkspacesize). Otherwise, an error code is returned.

 |

**Returns:**

Function execution result. If the operation is successful, OH\_NN\_SUCCESS is returned. If the operation fails, an error code is returned. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAISingleOpExecutor\_PreCheckConvolution()

HiAI\_SingleOpSupportStatus HMS\_HiAISingleOpExecutor\_PreCheckConvolution (HiAI\_SingleOpExecutorConvolutionParam param)

**Description**

Pre-checks whether a convolution operation is supported or optimized.

You can determine whether to call [HMS\_HiAISingleOpExecutor\_CreateConvolution](#hms_hiaisingleopexecutor_createconvolution) to create a convolution executor based on the return value of this API. Alternatively, you can also directly call [HMS\_HiAISingleOpExecutor\_CreateConvolution](#hms_hiaisingleopexecutor_createconvolution) to create a convolution executor.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

param

 | 

Refer to [HiAI\_SingleOpExecutorConvolutionParam](../../header-files-and-structs/structs/hiai-singleopexecutorconvolutionparam/document.md) for details of the input parameters.

 |

**Returns:**

Support status. For details about the status, please refer to [HiAI\_SingleOpSupportStatus](#hiai_singleopsupportstatus).

#### \[h2\]HMS\_HiAISingleOpExecutor\_PreCheckFusedConvolutionActivation()

HiAI\_SingleOpSupportStatus HMS\_HiAISingleOpExecutor\_PreCheckFusedConvolutionActivation (HiAI\_SingleOpExecutorFusedConvolutionActivationParam param)

**Description**

Pre-checks whether a fused convolution-and-activation operation is supported or optimized.

You can determine whether to call [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](#hms_hiaisingleopexecutor_createfusedconvolutionactivation) to create a fused convolution-and-activation executor based on the return value of this API. Alternatively, you can also directly call [HMS\_HiAISingleOpExecutor\_CreateFusedConvolutionActivation](#hms_hiaisingleopexecutor_createfusedconvolutionactivation) to create a fused convolution-and-activation executor.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

param

 | 

Refer to [HiAI\_SingleOpExecutorFusedConvolutionActivationParam](../../header-files-and-structs/structs/hiai-singleopexecutorfusedconvolutionactivationparam/document.md) for details of the input parameters.

 |

**Returns:**

Support status. For details about the status, please refer to [HiAI\_SingleOpSupportStatus](#hiai_singleopsupportstatus).

#### \[h2\]HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc()

OH\_NN\_ReturnCode HMS\_HiAISingleOpExecutor\_UpdateOutputTensorDesc (const HiAI\_SingleOpExecutor \* executor, uint32\_t index, HiAI\_SingleOpTensorDesc \* output)

**Description**

Updates the output tensor description of [HiAI\_SingleOpExecutor](#hiai_singleopexecutor).

When creating [HiAI\_SingleOpExecutor](#hiai_singleopexecutor), if you set the data type of input parameter **output** to HIAI\_SINGLEOP\_DT\_UNDEFINED, and set the format to HIAI\_SINGLEOP\_FORMAT\_RESERVED, calling this API will update the data type and format in the output tensor description to the optimal values that adapt to the hardware.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

executor

 | 

Pointer to the [HiAI\_SingleOpExecutor](#hiai_singleopexecutor) object. The value cannot be a null pointer. Otherwise, an error code is returned.

 |
| 

index

 | 

Index of the output tensor description, which is the same as the value specified when the executor is created. The index starts from 0.

 |
| 

output

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object to be updated.

 |

**Returns:**

Function execution result. If the operation is successful, OH\_NN\_SUCCESS is returned. If the operation fails, an error code is returned. For details about the error codes, please refer to [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAISingleOpOptions\_Create()

HiAI\_SingleOpOptions\* HMS\_HiAISingleOpOptions\_Create (void)

**Description**

Creates a [HiAI\_SingleOpOptions](#hiai_singleopoptions) object.

When you no longer use the [HiAI\_SingleOpOptions](#hiai_singleopoptions) object, destroy it by calling [HMS\_HiAISingleOpOptions\_Destroy](#hms_hiaisingleopoptions_destroy). Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Returns:**

Returns the pointer to [HiAI\_SingleOpOptions](#hiai_singleopoptions) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpOptions\_Destroy()

void HMS\_HiAISingleOpOptions\_Destroy (HiAI\_SingleOpOptions \*\* options)

**Description**

Releases a [HiAI\_SingleOpOptions](#hiai_singleopoptions) object.

This method is used to release the [HiAI\_SingleOpOptions](#hiai_singleopoptions) object created by calling [HMS\_HiAISingleOpOptions\_Create](#hms_hiaisingleopoptions_create).

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

options

 | 

Double pointer to the [HiAI\_SingleOpOptions](#hiai_singleopoptions) object. **options** and **\*options** cannot be null pointers, otherwise the destroying fails.

 |

#### \[h2\]HMS\_HiAISingleOpTensor\_CreateFromConst()

HiAI\_SingleOpTensor\* HMS\_HiAISingleOpTensor\_CreateFromConst (const HiAI\_SingleOpTensorDesc \* desc, void \* data, size\_t dataSize)

**Description**

Creates a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc), the memory address and the size of constant data (such as the convolution weight and bias).

This method directly reuses the constant data corresponding to **data** and **dataSize**, without copying data. Therefore, do not release the constant data memory of the tensor if the tensor created by this method is still in use. This method only reads the constant data corresponding to **data** and **dataSize** and does not modify the data.

Note: This API copies **desc** into [HiAI\_SingleOpTensor](#hiai_singleoptensor). Therefore, when you no longer use **desc**, you need destroy **desc** using [HMS\_HiAISingleOpTensorDesc\_Destroy](#hms_hiaisingleoptensordesc_destroy).

When you no longer use the [HiAI\_SingleOpTensor](#hiai_singleoptensor) object, destroy it by calling [HMS\_HiAISingleOpTensor\_Destroy](#hms_hiaisingleoptensor_destroy). Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

desc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, a null pointer is returned.

 |
| 

data

 | 

Constant data address. The value cannot be a null pointer. Otherwise, a null pointer is returned.

 |
| 

dataSize

 | 

Constant data size. The value cannot be 0. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpTensor](#hiai_singleoptensor) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer()

HiAI\_SingleOpTensor\* HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer (const HiAI\_SingleOpTensorDesc \* desc, void \* data, size\_t dataSize)

**Description**

Creates a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc), the memory address from [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) and data size.

This method reuses the ION memory from a spefific [HiAI\_SingleOpBuffer](#hiai_singleopbuffer). The memory address and size are determined by **data** and **dataSize**. The value of **dataSize** must be equal to the byte size of **desc** calculated by calling [HMS\_HiAISingleOpTensorDesc\_GetByteSize](#hms_hiaisingleoptensordesc_getbytesize). When you call [HMS\_HiAISingleOpTensor\_Destroy](#hms_hiaisingleoptensor_destroy) to destroy the tensor created by the API, the tensor data memory will not be released.

Note: This API copies **desc** into [HiAI\_SingleOpTensor](#hiai_singleoptensor). Therefore, when you no longer use **desc**, you need destroy **desc** using [HMS\_HiAISingleOpTensorDesc\_Destroy](#hms_hiaisingleoptensordesc_destroy).

When you no longer use the [HiAI\_SingleOpTensor](#hiai_singleoptensor) object, destroy it by calling [HMS\_HiAISingleOpTensor\_Destroy](#hms_hiaisingleoptensor_destroy). Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

desc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, a null pointer is returned.

 |
| 

data

 | 

Tensor data address. The value must be a memory address from [HiAI\_SingleOpBuffer](#hiai_singleopbuffer). Otherwise, a null pointer is returned.

 |
| 

dataSize

 | 

Tensor data size. The value cannot be 0. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpTensor](#hiai_singleoptensor) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpTensor\_CreateFromTensorDesc()

HiAI\_SingleOpTensor\* HMS\_HiAISingleOpTensor\_CreateFromTensorDesc (const HiAI\_SingleOpTensorDesc \* desc)

**Description**

Creates a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc).

This method is used to create a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object based on [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc).

This method uses [HMS\_HiAISingleOpTensorDesc\_GetByteSize](#hms_hiaisingleoptensordesc_getbytesize) to calculate the number of bytes of tensor data, and uses [HMS\_HiAISingleOpBuffer\_Create](#hms_hiaisingleopbuffer_create) to allocate ION memory for tensor data. The device driver directly obtains tensor data in zero-copy mode.

Note: This API copies **desc** into [HiAI\_SingleOpTensor](#hiai_singleoptensor). Therefore, when you no longer use **desc**, destroy **desc** using [HMS\_HiAISingleOpTensorDesc\_Destroy](#hms_hiaisingleoptensordesc_destroy).

When you no longer use the [HiAI\_SingleOpTensor](#hiai_singleoptensor) object, destroy it by calling [HMS\_HiAISingleOpTensor\_Destroy](#hms_hiaisingleoptensor_destroy). Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

desc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpTensor](#hiai_singleoptensor) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpTensor\_Destroy()

OH\_NN\_ReturnCode HMS\_HiAISingleOpTensor\_Destroy (HiAI\_SingleOpTensor \*\* tensor)

**Description**

Releases a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object.

When you no longer use the [HiAI\_SingleOpTensor](#hiai_singleoptensor) object, call this API to destroy the object. Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensor

 | 

Double pointer to the [HiAI\_SingleOpTensor](#hiai_singleoptensor) object. **tensor** and **\*tensor** cannot be null pointers. Otherwise, an error code is returned.

 |

**Returns:**

Function execution result. If the operation is successful, OH\_NN\_SUCCESS is returned. If the operation fails, an error code is returned. For details about the error codes, please refer to [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).

#### \[h2\]HMS\_HiAISingleOpTensor\_GetBuffer()

HiAI\_SingleOpBuffer\* HMS\_HiAISingleOpTensor\_GetBuffer (const HiAI\_SingleOpTensor \* tensor)

**Description**

Obtains the buffer of [HiAI\_SingleOpTensor](#hiai_singleoptensor).

This method is used to obtain the [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) of the specific [HiAI\_SingleOpTensor](#hiai_singleoptensor) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensor

 | 

Pointer to the [HiAI\_SingleOpTensor](#hiai_singleoptensor) object. The value cannot be a null pointer. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the pointer to the [HiAI\_SingleOpBuffer](#hiai_singleopbuffer) object.

#### \[h2\]HMS\_HiAISingleOpTensor\_GetTensorDesc()

HiAI\_SingleOpTensorDesc\* HMS\_HiAISingleOpTensor\_GetTensorDesc (const HiAI\_SingleOpTensor \* tensor)

**Description**

Obtains the tensor description of [HiAI\_SingleOpTensor](#hiai_singleoptensor).

This method is used to obtain the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) of the specific [HiAI\_SingleOpTensor](#hiai_singleoptensor) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensor

 | 

Pointer to the [HiAI\_SingleOpTensor](#hiai_singleoptensor) object. The value cannot be a null pointer. Otherwise, a null pointer is returned.

 |

**Returns:**

Returns the pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

#### \[h2\]HMS\_HiAISingleOpTensorDesc\_Create()

HiAI\_SingleOpTensorDesc\* HMS\_HiAISingleOpTensorDesc\_Create (const int64\_t \* dims, size\_t dimNum, HiAI\_SingleOpDataType dataType, HiAI\_SingleOpFormat format, bool isVirtual)

**Description**

Creates a [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

This method is used to create a [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object according to the input parameters like dimensions, data type and format.

You can call the following APIs to create a [HiAI\_SingleOpTensor](#hiai_singleoptensor) object based on the pointer to [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc): [HMS\_HiAISingleOpTensor\_CreateFromTensorDesc](#hms_hiaisingleoptensor_createfromtensordesc), [HMS\_HiAISingleOpTensor\_CreateFromSingleOpBuffer](#hms_hiaisingleoptensor_createfromsingleopbuffer), [HMS\_HiAISingleOpTensor\_CreateFromConst](#hms_hiaisingleoptensor_createfromconst).

Note: These APIs copy the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object to [HiAI\_SingleOpTensor](#hiai_singleoptensor). If the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object is no longer used, call [HMS\_HiAISingleOpTensorDesc\_Destroy](#hms_hiaisingleoptensordesc_destroy) to destroy it. Otherwise, a memory leak may occur.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

dims

 | 

Tensor dimension list. The value cannot be a null pointer. Otherwise, a null pointer is returned.

 |
| 

dimNum

 | 

Number of tensor dimensions. The value cannot be 0. Otherwise, a null pointer is returned.

 |
| 

dataType

 | 

Tensor data type.

 |
| 

format

 | 

Tensor format.

 |
| 

isVirtual

 | 

Indicates whether a tensor is a virtual tensor. **true** represents the tensor is a virtual tensor, and **false** represents the tensor is a non-virtual tensor. A virtual tensor is an intermediate tensor between connected single operators of CANN Kit. Data in virtual tensors exists only temporarily. Virtual tensors are only read or written by single operators of CANN Kit. For example, if the output tensor T1 of operator A is used only as the input tensor of operator B, and you only read the output tensor T2 of operator B, without reading or writing T1, then T1 will be a virtual tensor, and T2 will be a non-virtual tensor.

 |

**Returns:**

Returns the pointer to [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) if the operation is successful; returns a null pointer otherwise.

#### \[h2\]HMS\_HiAISingleOpTensorDesc\_Destroy()

void HMS\_HiAISingleOpTensorDesc\_Destroy (HiAI\_SingleOpTensorDesc \*\* tensorDesc)

**Description**

Releases a [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

This method is used to release the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object created by calling [HMS\_HiAISingleOpTensorDesc\_Create](#hms_hiaisingleoptensordesc_create).

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensorDesc

 | 

Double pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. **tensorDesc** and **\*tensorDesc** cannot be null pointers.

 |

#### \[h2\]HMS\_HiAISingleOpTensorDesc\_GetByteSize()

size\_t HMS\_HiAISingleOpTensorDesc\_GetByteSize (const HiAI\_SingleOpTensorDesc \* tensorDesc)

**Description**

Queries the number of bytes occupied by the data calculated based on the dimension and data type of [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc).

This method is used to obtain the number of bytes occupied by the data calculated based on the dimension and data type of [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc).

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensorDesc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, 0 is returned.

 |

**Returns:**

Number of data bytes of the tensor.

#### \[h2\]HMS\_HiAISingleOpTensorDesc\_GetDataType()

HiAI\_SingleOpDataType HMS\_HiAISingleOpTensorDesc\_GetDataType (const HiAI\_SingleOpTensorDesc \* tensorDesc)

**Description**

Queries the data type of the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

This method is used to obtain the data type of a specific [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensorDesc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, HIAI\_SINGLEOP\_DT\_UNDEFINED is returned.

 |

**Returns:**

Data type of the tensor.

#### \[h2\]HMS\_HiAISingleOpTensorDesc\_GetDimension()

int64\_t HMS\_HiAISingleOpTensorDesc\_GetDimension (const HiAI\_SingleOpTensorDesc \* tensorDesc, size\_t index)

**Description**

Queries the length of a dimension with a specific index of the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

This method is used to obtain the length of a specific dimension of a specific [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensorDesc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, 0 is returned.

 |
| 

index

 | 

Index of a dimension. The index starts from 0.

 |

**Returns:**

Length of the dimension whose index is **index**. If the execution fails, 0 is returned.

#### \[h2\]HMS\_HiAISingleOpTensorDesc\_GetDimensionCount()

size\_t HMS\_HiAISingleOpTensorDesc\_GetDimensionCount (const HiAI\_SingleOpTensorDesc \* tensorDesc)

**Description**

Queries the number of dimensions of the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

This method is used to obtain the number of dimensions of a specific [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensorDesc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, 0 is returned.

 |

**Returns:**

Number of dimensions of the tensor. If the execution fails, 0 is returned.

#### \[h2\]HMS\_HiAISingleOpTensorDesc\_GetFormat()

HiAI\_SingleOpFormat HMS\_HiAISingleOpTensorDesc\_GetFormat (const HiAI\_SingleOpTensorDesc \* tensorDesc)

**Description**

Queries format of the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

This method is used to obtain the format of a specific [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensorDesc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, HIAI\_SINGLEOP\_FORMAT\_RESERVED is returned.

 |

**Returns:**

Tensor format.

#### \[h2\]HMS\_HiAISingleOpTensorDesc\_IsVirtual()

bool HMS\_HiAISingleOpTensorDesc\_IsVirtual (const HiAI\_SingleOpTensorDesc \* tensorDesc)

**Description**

Queries whether [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) describes a virtual tensor.

A virtual tensor is an intermediate tensor between connected single operators of CANN Kit. Data in virtual tensors exists only temporarily. Virtual tensors are only read or written by single operators of CANN Kit. For example, if the output tensor T1 of operator A is used only as the input tensor of operator B, and you only read the output tensor T2 of operator B, without reading or writing T1, then T1 will be a virtual tensor, and T2 will be a non-virtual tensor.

**Since:** 5.0.0(12)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensorDesc

 | 

Pointer to the [HiAI\_SingleOpTensorDesc](#hiai_singleoptensordesc) object. The value cannot be a null pointer. Otherwise, false is returned.

 |

**Returns:**

Returns true if the tensor is a virtual tensor; returns false otherwise.

#### \[h2\]HMS\_HiAITensor\_GetSizeWithImageFormat()

size\_t HMS\_HiAITensor\_GetSizeWithImageFormat (NN\_TensorDesc \* desc, HiAI\_ImageFormat format)

**Description**

Calculates the size of the tensor to be applied for based on NN\_TensorDesc and HiAI\_ImageFormat.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

desc

 | 

Pointer to **NN\_TensorDesc**. The value cannot be null. Otherwise, 0 is returned.

 |
| 

format

 | 

Image format [HiAI\_ImageFormat](#hiai_imageformat).

 |

**Returns:**

Returns the size of the tensor to be applied for if the operation is successful; returns 0 otherwise.

#### \[h2\]HMS\_HiAITensor\_SetAippParams()

OH\_NN\_ReturnCode HMS\_HiAITensor\_SetAippParams (NN\_Tensor \* tensor, HiAI\_AippParam \* aippParams\[\], size\_t aippNum)

**Description**

Sets aippParams for NN\_Tensor.

After the AIPP parameters are set for **NN\_Tensor**, release the memory by calling [HMS\_HiAIAippParam\_Destroy](#hms_hiaiaippparam_destroy) after the tensor is used.

**Since:** 4.1.0(11)

**Parameters:**

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

tensor

 | 

Pointer to **NN\_Tensor**. The value cannot be null. Otherwise, a null pointer is returned.

 |
| 

aippParams\[\]

 | 

AIPP parameter array.

 |
| 

aippNum

 | 

Number of AIPP parameters.

 |

**Returns:**

Function execution result. Returns OH\_NN\_SUCCESS if the operation is successful; returns an error code otherwise. For details about the error codes, see [OH\_NN\_ReturnCode](../../../../neural-network-runtime-kit/c-apis/header-files/neural-network-runtime-type-h/document.md#oh_nn_returncode).
