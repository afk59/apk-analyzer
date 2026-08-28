# hiai\_options.h

#### Overview

Defines the API for build options.

Allows you to update model shapes, and set dynamic shapes, data layout formats, operator fusion strategies, quantization configurations, operator-level tuning, model-level tuning, assisted tuning, and bandwidth modes.

**Library:** libhiai\_foundation.so

**Syscap:** SystemCapability.AI.HiAIFoundation

**Since:** 4.1.0(11)

**Related Modules:**[CANN](../../../modules/cann/document.md)

#### Summary

#### \[h2\]Enumerations

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_FormatMode](../../../modules/cann/document.md#hiai_formatmode) {

HIAI\_FORMAT\_MODE\_NCHW = 0,

HIAI\_FORMAT\_MODE\_ORIGIN = 1

}

 | 

Data layout formats during model building.

 |
| 

[HiAI\_DynamicShapeStatus](../../../modules/cann/document.md#hiai_dynamicshapestatus) {

HIAI\_DYNAMIC\_SHAPE\_DISABLED = 0,

HIAI\_DYNAMIC\_SHAPE\_ENABLED = 1

}

 | 

Indicates whether to enable variable shapes before model building.

 |
| 

[HiAI\_DynamicShapeCacheMode](../../../modules/cann/document.md#hiai_dynamicshapecachemode) {

HIAI\_DYNAMIC\_SHAPE\_CACHE\_BUILT\_MODEL = 0,

HIAI\_DYNAMIC\_SHAPE\_CACHE\_LOADED\_MODEL = 1

}

 | 

Modes supported for the variable shapes before model building.

 |
| 

[HiAI\_ExecuteDevice](../../../modules/cann/document.md#hiai_executedevice) {

HIAI\_EXECUTE\_DEVICE\_NPU = 0,

HIAI\_EXECUTE\_DEVICE\_CPU = 1,

HIAI\_EXECUTE\_DEVICE\_GPU = 2

}

 | 

Device types supported for model running.

 |
| 

[HiAI\_FallbackMode](../../../modules/cann/document.md#hiai_fallbackmode) {

HIAI\_FALLBACK\_ENABLED = 0,

HIAI\_FALLBACK\_DISABLED = 1

}

 | 

Indicates whether to allow CANN Kit to select other devices, such as the CPU, when the specified device cannot build a model.

 |
| 

[HiAI\_DeviceMemoryReusePlan](../../../modules/cann/document.md#hiai_devicememoryreuseplan) {

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_UNSET = 0,

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_LOW = 1,

HIAI\_DEVICE\_MEMORY\_REUSE\_PLAN\_HIGH = 2

}

 | 

Device memory overcommitment option.

 |
| 

[HiAI\_TuningStrategy](../../../modules/cann/document.md#hiai_tuningstrategy) {

HIAI\_TUNING\_STRATEGY\_OFF = 0,

HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_TUNING = 1,

HIAI\_TUNING\_STRATEGY\_ON\_DEVICE\_PREPROCESS\_TUNING = 2,

HIAI\_TUNING\_STRATEGY\_ON\_CLOUD\_TUNING = 3

}

 | 

Configuration options of the model tuning strategy.

 |
| 

[HiAI\_TuningMode](../../../modules/cann/document.md#hiai_tuningmode) {

HIAI\_TUNING\_MODE\_UNSET = 0,

HIAI\_TUNING\_MODE\_AUTO = 1,

HIAI\_TUNING\_MODE\_HETER = 2

}

 | 

Assisted tuning mode.

 |
| 

[HiAI\_BandMode](../../../modules/cann/document.md#hiai_bandmode) {

HIAI\_BANDMODE\_UNSET = 0,

HIAI\_BANDMODE\_LOW = 1,

HIAI\_BANDMODE\_NORMAL = 2,

HIAI\_BANDMODE\_HIGH = 3

}

 | 

Defines the inter-device bandwidth mode.

 |
| 

[HiAI\_OmType](../../../modules/cann/document.md#hiai_omtype) {

HIAI\_OM\_TYPE\_OFF = 0,

HIAI\_OM\_TYPE\_PROFILING = 1,

HIAI\_OM\_TYPE\_DUMP = 2

}

 | 

Defines the operating and maintenance type.

 |

#### \[h2\]Functions

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetInputTensorShapes](../../../modules/cann/document.md#hms_hiaioptions_setinputtensorshapes) (OH\_NNCompilation \*compilation, NN\_TensorDesc \*inputTensorDescs\[\], size\_t shapeCount)

 | 

Updates the model input's shape during model building.

 |
| 

size\_t [HMS\_HiAIOptions\_GetInputTensorShapeSize](../../../modules/cann/document.md#hms_hiaioptions_getinputtensorshapesize) (const OH\_NNCompilation \*compilation)

 | 

Queries the number of shape descriptions among the build options.

 |
| 

NN\_TensorDesc \* [HMS\_HiAIOptions\_GetInputTensorShape](../../../modules/cann/document.md#hms_hiaioptions_getinputtensorshape) (const OH\_NNCompilation \*compilation, size\_t index)

 | 

Queries the shape description of a specific index among the build options.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetFormatMode](../../../modules/cann/document.md#hms_hiaioptions_setformatmode) (OH\_NNCompilation \*compilation, [HiAI\_FormatMode](../../../modules/cann/document.md#hiai_formatmode) formatMode)

 | 

Sets the data layout format during model building.

 |
| 

[HiAI\_FormatMode](../../../modules/cann/document.md#hiai_formatmode) [HMS\_HiAIOptions\_GetFormatMode](../../../modules/cann/document.md#hms_hiaioptions_getformatmode) (const OH\_NNCompilation \*compilation)

 | 

Queries the data layout format among build options.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeStatus](../../../modules/cann/document.md#hms_hiaioptions_setdynamicshapestatus) (OH\_NNCompilation \*compilation, [HiAI\_DynamicShapeStatus](../../../modules/cann/document.md#hiai_dynamicshapestatus) status)

 | 

Sets the EnableMode parameter in the variable shape configuration before model building.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeMaxCache](../../../modules/cann/document.md#hms_hiaioptions_setdynamicshapemaxcache) (OH\_NNCompilation \*compilation, size\_t maxCacheCount)

 | 

Sets the maximum number of cached models in the variable shape configuration before model building.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDynamicShapeCacheMode](../../../modules/cann/document.md#hms_hiaioptions_setdynamicshapecachemode) (OH\_NNCompilation \*compilation, [HiAI\_DynamicShapeCacheMode](../../../modules/cann/document.md#hiai_dynamicshapecachemode) mode)

 | 

Sets the cache mode in the variable shape configuration before model building.

 |
| 

[HiAI\_DynamicShapeStatus](../../../modules/cann/document.md#hiai_dynamicshapestatus) [HMS\_HiAIOptions\_GetDynamicShapeStatus](../../../modules/cann/document.md#hms_hiaioptions_getdynamicshapestatus) (const OH\_NNCompilation \*compilation)

 | 

Queries the dynamic shape status parameter in the variable shape configuration before model building.

 |
| 

size\_t [HMS\_HiAIOptions\_GetDynamicShapeMaxCache](../../../modules/cann/document.md#hms_hiaioptions_getdynamicshapemaxcache) (const OH\_NNCompilation \*compilation)

 | 

Queries the maximum number of caches in the variable shape configuration before model building.

 |
| 

[HiAI\_DynamicShapeCacheMode](../../../modules/cann/document.md#hiai_dynamicshapecachemode) [HMS\_HiAIOptions\_GetDynamicShapeCacheMode](../../../modules/cann/document.md#hms_hiaioptions_getdynamicshapecachemode) (const OH\_NNCompilation \*compilation)

 | 

Queries the cacheMode parameter in the variable shape configuration before model building.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetOperatorDeviceOrder](../../../modules/cann/document.md#hms_hiaioptions_setoperatordeviceorder) (OH\_NNCompilation \*compilation, const char \*operatorName, [HiAI\_ExecuteDevice](../../../modules/cann/document.md#hiai_executedevice) \*executeDevices, size\_t deviceCount)

 | 

Sets the list of devices to execute operators in the operator-level tuning configuration.

 |
| 

size\_t [HMS\_HiAIOptions\_GetOperatorDeviceCount](../../../modules/cann/document.md#hms_hiaioptions_getoperatordevicecount) (const OH\_NNCompilation \*compilation, const char \*operatorName)

 | 

Queries the number of devices to execute a specific operator in the model from the operator-level tuning configuration.

 |
| 

[HiAI\_ExecuteDevice](../../../modules/cann/document.md#hiai_executedevice) \* [HMS\_HiAIOptions\_GetOperatorDeviceOrder](../../../modules/cann/document.md#hms_hiaioptions_getoperatordeviceorder) (const OH\_NNCompilation \*compilation, const char \*operatorName)

 | 

Queries the list of devices to execute a specific operator in the model from the operator-level tuning configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetModelDeviceOrder](../../../modules/cann/document.md#hms_hiaioptions_setmodeldeviceorder) (OH\_NNCompilation \*compilation, [HiAI\_ExecuteDevice](../../../modules/cann/document.md#hiai_executedevice) \*executeDevices, size\_t deviceCount)

 | 

Sets the list of devices to execute the model in the model-level tuning configuration.

 |
| 

size\_t [HMS\_HiAIOptions\_GetModelDeviceCount](../../../modules/cann/document.md#hms_hiaioptions_getmodeldevicecount) (const OH\_NNCompilation \*compilation)

 | 

Queries the number of devices to execute the model in the model-level tuning configuration.

 |
| 

[HiAI\_ExecuteDevice](../../../modules/cann/document.md#hiai_executedevice) \* [HMS\_HiAIOptions\_GetModelDeviceOrder](../../../modules/cann/document.md#hms_hiaioptions_getmodeldeviceorder) (const OH\_NNCompilation \*compilation)

 | 

Queries the list of devices to execute the model in the model-level tuning configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetFallbackMode](../../../modules/cann/document.md#hms_hiaioptions_setfallbackmode) (OH\_NNCompilation \*compilation, [HiAI\_FallbackMode](../../../modules/cann/document.md#hiai_fallbackmode) fallbackMode)

 | 

Sets the fallback mode in the tuning configuration.

 |
| 

[HiAI\_FallbackMode](../../../modules/cann/document.md#hiai_fallbackmode) [HMS\_HiAIOptions\_GetFallbackMode](../../../modules/cann/document.md#hms_hiaioptions_getfallbackmode) (const OH\_NNCompilation \*compilation)

 | 

Queries the fallback mode in the tuning configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetDeviceMemoryReusePlan](../../../modules/cann/document.md#hms_hiaioptions_setdevicememoryreuseplan) (OH\_NNCompilation \*compilation, [HiAI\_DeviceMemoryReusePlan](../../../modules/cann/document.md#hiai_devicememoryreuseplan) deviceMemoryReusePlan)

 | 

Sets the device memory overcommitment parameters in the tuning configuration.

 |
| 

[HiAI\_DeviceMemoryReusePlan](../../../modules/cann/document.md#hiai_devicememoryreuseplan) [HMS\_HiAIOptions\_GetDeviceMemoryReusePlan](../../../modules/cann/document.md#hms_hiaioptions_getdevicememoryreuseplan) (const OH\_NNCompilation \*compilation)

 | 

Queries the device memory overcommitment parameters in the tuning configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningStrategy](../../../modules/cann/document.md#hms_hiaioptions_settuningstrategy) (OH\_NNCompilation \*compilation, [HiAI\_TuningStrategy](../../../modules/cann/document.md#hiai_tuningstrategy) tuningStrategy)

 | 

Sets the model tuning strategy during model building.

 |
| 

[HiAI\_TuningStrategy](../../../modules/cann/document.md#hiai_tuningstrategy) [HMS\_HiAIOptions\_GetTuningStrategy](../../../modules/cann/document.md#hms_hiaioptions_gettuningstrategy) (const OH\_NNCompilation \*compilation)

 | 

Queries the model tuning strategy.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetQuantConfig](../../../modules/cann/document.md#hms_hiaioptions_setquantconfig) (OH\_NNCompilation \*compilation, void \*data, size\_t size)

 | 

Sets the quantization configuration during model building.

 |
| 

void \* [HMS\_HiAIOptions\_GetQuantConfigData](../../../modules/cann/document.md#hms_hiaioptions_getquantconfigdata) (const OH\_NNCompilation \*compilation)

 | 

Queries the data address of the quantization configuration.

 |
| 

size\_t [HMS\_HiAIOptions\_GetQuantConfigSize](../../../modules/cann/document.md#hms_hiaioptions_getquantconfigsize) (const OH\_NNCompilation \*compilation)

 | 

Queries the data size of the quantization configuration.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningMode](../../../modules/cann/document.md#hms_hiaioptions_settuningmode) (OH\_NNCompilation \*compilation, [HiAI\_TuningMode](../../../modules/cann/document.md#hiai_tuningmode) tuningMode)

 | 

Selects the assisted tuning mode.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetTuningCacheDir](../../../modules/cann/document.md#hms_hiaioptions_settuningcachedir) (OH\_NNCompilation \*compilation, const char \*cacheDir)

 | 

Sets the cache directory for assisted tuning.

 |
| 

[HiAI\_TuningMode](../../../modules/cann/document.md#hiai_tuningmode) [HMS\_HiAIOptions\_GetTuningMode](../../../modules/cann/document.md#hms_hiaioptions_gettuningmode) (const OH\_NNCompilation \*compilation)

 | 

Queries the assisted tuning mode.

 |
| 

const char \* [HMS\_HiAIOptions\_GetTuningCacheDir](../../../modules/cann/document.md#hms_hiaioptions_gettuningcachedir) (const OH\_NNCompilation \*compilation)

 | 

Queries the cache directory for assisted tuning.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetBandMode](../../../modules/cann/document.md#hms_hiaioptions_setbandmode) (OH\_NNCompilation \*compilation, [HiAI\_BandMode](../../../modules/cann/document.md#hiai_bandmode) bandMode)

 | 

Sets the bandwidth mode for the NPU and peripheral input/output (I/O) devices.

 |
| 

[HiAI\_BandMode](../../../modules/cann/document.md#hiai_bandmode) [HMS\_HiAIOptions\_GetBandMode](../../../modules/cann/document.md#hms_hiaioptions_getbandmode) (const OH\_NNCompilation \*compilation)

 | 

Queries the bandwidth mode.

 |
| 

OH\_NN\_ReturnCode [HMS\_HiAIOptions\_SetOmOptions](../../../modules/cann/document.md#hms_hiaioptions_setomoptions) (OH\_NNCompilation \*compilation, [HiAI\_OmType](../../../modules/cann/document.md#hiai_omtype) type, const char \*outputDir)

 | 

Sets the operating and maintenance options for model loading.

 |
