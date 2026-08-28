# types.h

#### Overview

Provides the model file types and device types supported by MindSpore Lite.

**File to include**: <mindspore/types.h>

**Library**: libmindspore\_lite\_ndk.so

**System capability**: SystemCapability.Ai.MindSpore

**Since**: 9

**Related module**: [MindSpore](../../modules/mindspore/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [NNRTDeviceDesc](../../structs/nnrtdevicedesc/document.md) | NNRTDeviceDesc | Defines NNRt device information, including the device ID and device name. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [OH\_AI\_ModelType](#oh_ai_modeltype) | OH\_AI\_ModelType | Defines model file types. |
| [OH\_AI\_DeviceType](#oh_ai_devicetype) | OH\_AI\_DeviceType | Defines supported device types. |
| [OH\_AI\_NNRTDeviceType](#oh_ai_nnrtdevicetype) | OH\_AI\_NNRTDeviceType | Defines NNRt device types. |
| [OH\_AI\_PerformanceMode](#oh_ai_performancemode) | OH\_AI\_PerformanceMode | Defines performance modes of the NNRt device. |
| [OH\_AI\_Priority](#oh_ai_priority) | OH\_AI\_Priority | Defines NNRt inference task priorities. |
| [OH\_AI\_OptimizationLevel](#oh_ai_optimizationlevel) | OH\_AI\_OptimizationLevel | Defines training optimization levels. |
| [OH\_AI\_QuantizationType](#oh_ai_quantizationtype) | OH\_AI\_QuantizationType | Defines quantization types. |

#### Enum Description

#### \[h2\]OH\_AI\_ModelType

enum OH\_AI\_ModelType

**Description**

Defines model file types.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_MODELTYPE\_MINDIR = 0 | Model type of MindIR. The extension of the model file name is **.ms**. |
| OH\_AI\_MODELTYPE\_INVALID = 0xFFFFFFFF | Invalid model type. |

#### \[h2\]OH\_AI\_DeviceType

enum OH\_AI\_DeviceType

**Description**

Defines the supported device types.

**Since**: 9

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_DEVICETYPE\_CPU = 0 | Device type: CPU. |
| OH\_AI\_DEVICETYPE\_GPU | Device type: GPU (reserved). |
| OH\_AI\_DEVICETYPE\_KIRIN\_NPU | Device type: Kirin NPU (reserved). |
| OH\_AI\_DEVICETYPE\_NNRT = 60 | Device type: NNRt |
| OH\_AI\_DEVICETYPE\_INVALID = 100 | Invalid device type. |

#### \[h2\]OH\_AI\_NNRTDeviceType

enum OH\_AI\_NNRTDeviceType

**Description**

Defines NNRt device types.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_NNRTDEVICE\_OTHERS = 0 | Others (any device type except the following three types). |
| OH\_AI\_NNRTDEVICE\_CPU = 1 | CPU. |
| OH\_AI\_NNRTDEVICE\_GPU = 2 | GPU. |
| OH\_AI\_NNRTDEVICE\_ACCELERATOR = 3 | Specific acceleration device. |

#### \[h2\]OH\_AI\_PerformanceMode

enum OH\_AI\_PerformanceMode

**Description**

Defines performance modes of the NNRt device.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_PERFORMANCE\_NONE = 0 | No special settings. |
| OH\_AI\_PERFORMANCE\_LOW = 1 | Low power consumption. |
| OH\_AI\_PERFORMANCE\_MEDIUM = 2 | Power consumption and performance balancing. |
| OH\_AI\_PERFORMANCE\_HIGH = 3 | High performance. |
| OH\_AI\_PERFORMANCE\_EXTREME = 4 | Ultimate performance. |

#### \[h2\]OH\_AI\_Priority

enum OH\_AI\_Priority

**Description**

Defines NNRt inference task priorities.

**Since**: 10

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_PRIORITY\_NONE = 0 | No priority preference. |
| OH\_AI\_PRIORITY\_LOW = 1 | Low priority. |
| OH\_AI\_PRIORITY\_MEDIUM = 2 | Medium priority. |
| OH\_AI\_PRIORITY\_HIGH = 3 | High priority. |

#### \[h2\]OH\_AI\_OptimizationLevel

enum OH\_AI\_OptimizationLevel

**Description**

Defines training optimization levels.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_KO0 = 0 | No optimization level. |
| OH\_AI\_KO2 = 2 | Converts the precision type of the network to float16 and keeps the precision type of the batch normalization layer and loss function as float32. |
| OH\_AI\_KO3 = 3 | Converts the precision type of the network (including the batch normalization layer) to float16. |
| OH\_AI\_KAUTO = 4 | Selects an optimization level based on the device. |
| OH\_AI\_KOPTIMIZATIONTYPE = 0xFFFFFFFF | Invalid optimization level. |

#### \[h2\]OH\_AI\_QuantizationType

enum OH\_AI\_QuantizationType

**Description**

Defines quantization types.

**Since**: 11

| Enum Item | Description |
| :-- | :-- |
| OH\_AI\_NO\_QUANT = 0 | No quantification. |
| OH\_AI\_WEIGHT\_QUANT = 1 | Weight quantization. |
| OH\_AI\_FULL\_QUANT = 2 | Full quantization. |
| OH\_AI\_UNKNOWN\_QUANT\_TYPE = 0xFFFFFFFF | Invalid quantization type. |
