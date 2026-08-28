# @ohos.ai.mindSporeLite (On-device AI Framework)

MindSpore Lite is a lightweight and high-performance on-device AI engine that provides standard model inference and training APIs and built-in universal high-performance operator libraries. It supports Neural Network Runtime Kit for a higher inference efficiency, empowering intelligent applications in all scenarios.

This topic describes the model inference and training capabilities supported by the MindSpore Lite AI engine.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/32/v3/e4Ze4RABRFCG2cOvgRWBnA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062523Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2DFF2DC4487B9640D33F005635FC9F784D4E6CCB09B0CD001ACA1872EF0FE59D)

-   The initial APIs of this module are supported since API version 10. Newly added APIs will be marked with a superscript to indicate their earliest API version. Unless otherwise stated, the MindSpore model is used in the sample code.
    
-   The APIs of this module can be used only in the stage model.
    

#### Modules to Import

import { mindSporeLite } from '@kit.MindSporeLiteKit';

#### mindSporeLite.loadModelFromFile

loadModelFromFile(model: string, callback: Callback<Model>): void

Loads the input model from the full path for CPU inference. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | string | Yes | Complete path of the input model. The string length is subject to the file system. |
| callback | Callback<[Model](#model)\> | Yes | Callback used to return the result, which is a **Model** object. |

**Example**

let modelFile: string = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS\_LITE\_ERR: getInputs failed.')
  } else {
    console.info(modelInputs\[0\].name);
  }
})

#### mindSporeLite.loadModelFromFile

loadModelFromFile(model: string, context: Context, callback: Callback<Model>): void

Loads the input model from the full path for model inference. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | string | Yes | Complete path of the input model. The string length is subject to the file system. |
| context | [Context](#context) | Yes | Configuration information of the running environment. |
| callback | Callback<[Model](#model)\> | Yes | Callback used to return the result, which is a **Model** object. |

**Example**

let context: mindSporeLite.Context = {};
context.target = \['cpu'\];
let modelFile: string = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile, context, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS\_LITE\_ERR: getInputs failed.')
  } else {
    console.info(modelInputs\[0\].name);
  }
})

#### mindSporeLite.loadModelFromFile

loadModelFromFile(model: string, context?: Context): Promise<Model>

Loads the input model from the full path for model inference. This API uses a promise to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | string | Yes | Complete path of the input model. The string length is subject to the file system. |
| context | [Context](#context) | No | Configuration information of the running environment. By default, **CpuDevice** is used for initialization. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Model](#model)\> | Promise used to return the result, which is a **Model** object. |

**Example**

let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS\_LITE\_ERR: getInputs failed.')
  } else {
    console.info(modelInputs\[0\].name);
  }
})

#### mindSporeLite.loadModelFromBuffer

loadModelFromBuffer(model: ArrayBuffer, callback: Callback<Model>): void

Loads the input model from the memory for CPU inference. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | ArrayBuffer | Yes | Memory that contains the input model. |
| callback | Callback<[Model](#model)\> | Yes | Callback used to return the result, which is a **Model** object. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((buffer: Uint8Array) => {
    let modelBuffer = buffer.buffer;
    mindSporeLite.loadModelFromBuffer(modelBuffer, (mindSporeLiteModel: mindSporeLite.Model) => {
      let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
      console.info('MS\_LITE\_LOG: ' + modelInputs\[0\].name);
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### mindSporeLite.loadModelFromBuffer

loadModelFromBuffer(model: ArrayBuffer, context: Context, callback: Callback<Model>): void

Loads the input model from the memory for inference. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | ArrayBuffer | Yes | Memory that contains the input model. |
| context | [Context](#context) | Yes | Configuration information of the running environment. |
| callback | Callback<[Model](#model)\> | Yes | Callback used to return the result, which is a **Model** object. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((buffer: Uint8Array) => {
    let modelBuffer = buffer.buffer;
    let context: mindSporeLite.Context = {};
    context.target = \['cpu'\];
    mindSporeLite.loadModelFromBuffer(modelBuffer, context, (mindSporeLiteModel: mindSporeLite.Model) => {
      let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
      console.info('MS\_LITE\_LOG: ' + modelInputs\[0\].name);
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### mindSporeLite.loadModelFromBuffer

loadModelFromBuffer(model: ArrayBuffer, context?: Context): Promise<Model>

Loads the input model from the memory for inference. This API uses a promise to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | ArrayBuffer | Yes | Memory that contains the input model. |
| context | [Context](#context) | No | Configuration information of the running environment. By default, **CpuDevice** is used for initialization. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Model](#model)\> | Promise used to return the result, which is a **Model** object. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((buffer: Uint8Array) => {
    let modelBuffer = buffer.buffer;
    mindSporeLite.loadModelFromBuffer(modelBuffer).then((mindSporeLiteModel: mindSporeLite.Model) => {
      let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
      console.info('MS\_LITE\_LOG: ' + modelInputs\[0\].name);
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### mindSporeLite.loadModelFromFd

loadModelFromFd(model: number, callback: Callback<Model>): void

Loads the input model based on the specified file descriptor for CPU inference. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | number | Yes | File descriptor of the input model. The **fd** value returned by the file system is passed. |
| callback | Callback<[Model](#model)\> | Yes | Callback used to return the result, which is a **Model** object. |

**Example**

import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ\_ONLY);
mindSporeLite.loadModelFromFd(file.fd, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS\_LITE\_ERR: getInputs failed.')
  } else {
    console.info(modelInputs\[0\].name);
  }
})

#### mindSporeLite.loadModelFromFd

loadModelFromFd(model: number, context: Context, callback: Callback<Model>): void

Loads the input model based on the specified file descriptor for inference. This API uses an asynchronous callback to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | number | Yes | File descriptor of the input model. The **fd** value returned by the file system is passed. |
| context | [Context](#context) | Yes | Configuration information of the running environment. |
| callback | Callback<[Model](#model)\> | Yes | Callback used to return the result, which is a **Model** object. |

**Example**

import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let context: mindSporeLite.Context = {};
context.target = \['cpu'\];
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ\_ONLY);
mindSporeLite.loadModelFromFd(file.fd, context, (mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS\_LITE\_ERR: getInputs failed.')
  } else {
    console.info(modelInputs\[0\].name);
  }
})

#### mindSporeLite.loadModelFromFd

loadModelFromFd(model: number, context?: Context): Promise<Model>

Loads the input model based on the specified file descriptor for inference. This API uses a promise to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | number | Yes | File descriptor of the input model. The **fd** value returned by the file system is passed. |
| context | [Context](#context) | No | Configuration information of the running environment. By default, **CpuDevice** is used for initialization. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Model](#model)\> | Promise used to return the result, which is a **Model** object. |

**Example**

import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ\_ONLY);
mindSporeLite.loadModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS\_LITE\_ERR: getInputs failed.')
  } else {
    console.info(modelInputs\[0\].name);
  }
})

#### mindSporeLite.loadTrainModelFromFile12+

loadTrainModelFromFile(model: string, trainCfg?: TrainCfg, context?: Context): Promise<Model>

Loads the training model file based on the specified path. This API uses a promise to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | string | Yes | Complete path of the input model. The string length is subject to the file system. |
| trainCfg | [TrainCfg](#traincfg12) | No | Model training configuration. The default value is an array of the default values of attributes in **TrainCfg**. |
| context | [Context](#context) | No | Configuration information of the running environment. By default, **CpuDevice** is used for initialization. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Model](#model)\> | Promise used to return the result, which is a **Model** object. |

**Example**

let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS\_LITE\_ERR: getInputs failed.')
  } else {
    console.info(modelInputs\[0\].name);
  }
})

#### mindSporeLite.loadTrainModelFromBuffer12+

loadTrainModelFromBuffer(model: ArrayBuffer, trainCfg?: TrainCfg, context?: Context): Promise<Model>

Loads a training model from the memory buffer. This API uses a promise to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | ArrayBuffer | Yes | Memory accommodating the training model. |
| trainCfg | [TrainCfg](#traincfg12) | No | Model training configuration. The default value is an array of the default values of attributes in **TrainCfg**. |
| context | [Context](#context) | No | Configuration information of the running environment. By default, **CpuDevice** is used for initialization. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Model](#model)\> | Promise used to return the result, which is a **Model** object. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((buffer: Uint8Array) => {
    let modelBuffer = buffer.buffer;
    mindSporeLite.loadTrainModelFromBuffer(modelBuffer).then((mindSporeLiteModel: mindSporeLite.Model) => {
      console.info("MSLITE trainMode: ", mindSporeLiteModel.trainMode);
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### mindSporeLite.loadTrainModelFromFd12+

loadTrainModelFromFd(model: number, trainCfg?: TrainCfg, context?: Context): Promise<Model>

Loads the training model file from the file descriptor. This API uses a promise to return the result.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| model | number | Yes | File descriptor of the training model. The **fd** value returned by the file system is passed. |
| trainCfg | [TrainCfg](#traincfg12) | No | Model training configuration. The default value is an array of the default values of attributes in **TrainCfg**. |
| context | [Context](#context) | No | Configuration information of the running environment. By default, **CpuDevice** is used for initialization. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[Model](#model)\> | Promise used to return the result, which is a **Model** object. |

**Example**

import { fileIo } from '@kit.CoreFileKit';

let modelFile = '/path/to/xxx.ms';
let file = fileIo.openSync(modelFile, fileIo.OpenMode.READ\_ONLY);
mindSporeLite.loadTrainModelFromFd(file.fd).then((mindSporeLiteModel: mindSporeLite.Model) => {
  console.info("MSLITE trainMode: ", mindSporeLiteModel.trainMode);
});

#### mindSporeLite.getAllNNRTDeviceDescriptions12+

getAllNNRTDeviceDescriptions() : NNRTDeviceDescription\[\]

Obtains all device descriptions in NNRt.

**System capability**: SystemCapability.AI.MindSporeLite

**Return value**

| Type | Description |
| :-- | :-- |
| [NNRTDeviceDescription](#nnrtdevicedescription12)\[\] | NNRt device description array. |

**Example**

let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('MS\_LITE\_LOG: getAllNNRTDeviceDescriptions is NULL.');
}

#### Context

Defines the configuration information of the running environment.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| target | string\[\] | No | Yes | Target backend. The value can be **cpu** or **nnrt**. The default value is **cpu**. |
| cpu | [CpuDevice](#cpudevice) | No | Yes | CPU backend device option. Set this parameter set only when **target** is set to **cpu**. The default value is an array of the default values of attributes in **CpuDevice**. |
| nnrt | [NNRTDevice](#nnrtdevice) | No | Yes | NNRt backend device option. Set this parameter set only when **target** is set to **nnrt**. The default value is an array of the default values of attributes in **NNRTDevice**. |

**Example**

let context: mindSporeLite.Context = {};
context.target = \['cpu','nnrt'\];

#### CpuDevice

Defines the CPU backend device option.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| threadNum | number | No | Yes | Number of runtime threads. The default value is **2**. |
| threadAffinityMode | [ThreadAffinityMode](#threadaffinitymode) | No | Yes | Affinity mode for binding runtime threads to CPU cores. The default value is **mindSporeLite.ThreadAffinityMode.NO\_AFFINITIES**. |
| threadAffinityCoreList | number\[\] | No | Yes | List of CPU cores bound to runtime threads. Set this parameter only when **threadAffinityMode** is set. If **threadAffinityMode** is set to **mindSporeLite.ThreadAffinityMode.NO\_AFFINITIES**, this parameter is empty. The number in the list indicates the SN of the CPU core. The default value is **\[\]**. |
| precisionMode | string | No | Yes | Whether to enable the Float16 inference mode. The value **preferred\_fp16** means to enable half-precision inference and the default value **enforce\_fp32** means to disable half-precision inference. Other settings are not supported. |

**Float16 inference mode**: a mode that uses half-precision inference. Float16 uses 16 bits to represent a number and therefore it is also called half-precision.

**Example**

let context: mindSporeLite.Context = {};
context.cpu = {};
context.target = \['cpu'\];
context.cpu.threadNum = 2;
context.cpu.threadAffinityMode = 0;
context.cpu.precisionMode = 'preferred\_fp16';
context.cpu.threadAffinityCoreList = \[0, 1, 2\];

#### ThreadAffinityMode

Specifies the affinity mode for binding runtime threads to CPU cores.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_AFFINITIES | 0 | No affinities. |
| BIG\_CORES\_FIRST | 1 | Big cores first. |
| LITTLE\_CORES\_FIRST | 2 | Medium cores first. |

#### NNRTDevice

Represents an NNRt device. Neural Network Runtime (NNRt) is a bridge that connects the upper-layer AI inference framework to the bottom-layer acceleration chip to implement cross-chip inference and computing of AI models. An NNRt backend can be configured for MindSpore Lite.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| deviceID12+ | bigint | No | Yes | NNRt device ID. The default value is **0**. |
| performanceMode12+ | [PerformanceMode](#performancemode12) | No | Yes | NNRt device performance mode. The default value is **PERFORMANCE\_NONE**. |
| priority12+ | [Priority](#priority12) | No | Yes | NNRt inference task priority. The default value is **PRIORITY\_MEDIUM**. |
| extensions12+ | [Extension](#extension12)\[\] | No | Yes | Extended NNRt device configuration. This parameter is left empty by default. |

#### PerformanceMode12+

Enumerates NNRt device performance modes.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Value | Description |
| :-- | :-- | :-- |
| PERFORMANCE\_NONE | 0 | No special settings. |
| PERFORMANCE\_LOW | 1 | Low power consumption. |
| PERFORMANCE\_MEDIUM | 2 | Power consumption and performance balancing. |
| PERFORMANCE\_HIGH | 3 | High performance. |
| PERFORMANCE\_EXTREME | 4 | Ultimate performance. |

#### Priority12+

Enumerates NNRt inference task priorities.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Value | Description |
| :-- | :-- | :-- |
| PRIORITY\_NONE | 0 | No priority preference. |
| PRIORITY\_LOW | 1 | Low priority. |
| PRIORITY\_MEDIUM | 2 | Medium priority. |
| PRIORITY\_HIGH | 3 | High priority. |

#### Extension12+

Defines the extended NNRt device configuration.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Configuration name. |
| value | ArrayBuffer | No | No | Memory accommodating the extended configuration. |

#### NNRTDeviceDescription12+

Defines NNRt device information, including the device ID and device name.

**System capability**: SystemCapability.AI.MindSporeLite

#### \[h2\]deviceID12+

deviceID() : bigint

Obtains the NNRt device ID.

**System capability**: SystemCapability.AI.MindSporeLite

**Return value**

| Type | Description |
| :-- | :-- |
| bigint | NNRt device ID. |

**Example**

let context: mindSporeLite.Context = {};
context.target = \["nnrt"\];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices\[i\].deviceID().toString());
  }
}

#### \[h2\]deviceType12+

deviceType() : NNRTDeviceType

Obtains the device model.

**System capability**: SystemCapability.AI.MindSporeLite

**Return value**

| Type | Description |
| :-- | :-- |
| [NNRTDeviceType](#nnrtdevicetype12) | NNRt device type. |

**Example**

let context: mindSporeLite.Context = {};
context.target = \["nnrt"\];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices\[i\].deviceType().toString());
  }
}

#### \[h2\]deviceName12+

deviceName() : string

Obtains the NNRt device name.

**System capability**: SystemCapability.AI.MindSporeLite

**Return value**

| Type | Description |
| :-- | :-- |
| string | NNRt device name. |

**Example**

let context: mindSporeLite.Context = {};
context.target = \["nnrt"\];
context.nnrt = {};
let allDevices = mindSporeLite.getAllNNRTDeviceDescriptions();
if (allDevices == null) {
  console.error('getAllNNRTDeviceDescriptions is NULL.');
} else {
  for (let i: number = 0; i < allDevices.length; i++) {
    console.info(allDevices\[i\].deviceName().toString());
  }
}

#### NNRTDeviceType12+

Enumerates NNRt device types.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Value | Description |
| :-- | :-- | :-- |
| NNRTDEVICE\_OTHERS | 0 | Others (any device type except the following three types). |
| NNRTDEVICE\_CPU | 1 | CPU. |
| NNRTDEVICE\_GPU | 2 | GPU. |
| NNRTDEVICE\_ACCELERATOR | 3 | Specific acceleration device. |

#### TrainCfg12+

Defines the configuration for on-device training.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| lossName | string\[\] | No | Yes | List of loss functions. The default value is \["loss\_fct", "\_loss\_fn", "SigmoidCrossEntropy"\]. |
| optimizationLevel | [OptimizationLevel](#optimizationlevel12) | No | Yes | Network optimization level for on-device training. The default value is **O0**. |

**Example**

let cfg: mindSporeLite.TrainCfg = {};
cfg.lossName = \["loss\_fct", "\_loss\_fn", "SigmoidCrossEntropy"\];
cfg.optimizationLevel = mindSporeLite.OptimizationLevel.O0;

#### OptimizationLevel12+

Enumerates network optimization levels for on-device training.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Value | Description |
| :-- | :-- | :-- |
| O0 | 0 | No optimization level. |
| O2 | 2 | Converts the precision type of the network to float16 and keeps the precision type of the batch normalization layer and loss function as float32. |
| O3 | 3 | Converts the precision type of the network (including the batch normalization layer) to float16. |
| AUTO | 4 | Selects an optimization level based on the device. |

#### QuantizationType12+

Enumerates quantization types.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Value | Description |
| :-- | :-- | :-- |
| NO\_QUANT | 0 | No quantification. |
| WEIGHT\_QUANT | 1 | Weight quantization. |
| FULL\_QUANT | 2 | Full quantization. |

#### Model

Represents a **Model** instance, with properties and APIs defined.

In the following sample code, you first need to use [loadModelFromFile()](#mindsporeliteloadmodelfromfile), [loadModelFromBuffer()](#mindsporeliteloadmodelfrombuffer), or [loadModelFromFd()](#mindsporeliteloadmodelfromfd) to obtain a **Model** instance before calling related APIs.

#### \[h2\]Attributes

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| learningRate12+ | number | No | Yes | Learning rate of a training model. The default value is read from the loaded model. |
| trainMode12+ | boolean | No | Yes | Training mode. The value **true** indicates the training mode, and the value **false** indicates the non-training mode. The default value is **true** for a training model and **false** for an inference model. |

#### \[h2\]getInputs

getInputs(): MSTensor\[\]

Obtains the model input for inference.

**System capability**: SystemCapability.AI.MindSporeLite

**Return value**

| Type | Description |
| :-- | :-- |
| [MSTensor](#mstensor)\[\] | **MSTensor** object. |

**Example**

let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  if (modelInputs == null) {
    console.error('MS\_LITE\_ERR: getInputs failed.')
  } else {
    console.info(modelInputs\[0\].name);
  }
})

#### \[h2\]predict

predict(inputs: MSTensor\[\], callback: Callback<MSTensor\[\]>): void

Executes the inference model. This API uses an asynchronous callback to return the result. Ensure that the model object is not reclaimed when being invoked.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputs | [MSTensor](#mstensor)\[\] | Yes | List of input models. |
| callback | Callback<[MSTensor](#mstensor)\[\]> | Yes | Callback used to return the result, which is a list of **MSTensor** objects. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input\_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(inputName)
  .then(async (buffer: Uint8Array) => {
    let inputBuffer = buffer.buffer;
    let modelFile: string = '/path/to/xxx.ms';
    let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
    let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();

    modelInputs\[0\].setData(inputBuffer);
    mindSporeLiteModel.predict(modelInputs, (mindSporeLiteTensor: mindSporeLite.MSTensor\[\]) => {
      let output = new Float32Array(mindSporeLiteTensor\[0\].getData());
      for (let i = 0; i < output.length; i++) {
        console.info('MS\_LITE\_LOG: ' + output\[i\].toString());
      }
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### \[h2\]predict

predict(inputs: MSTensor\[\]): Promise<MSTensor\[\]>

Executes model inference. This API uses a promise to return the result. Ensure that the model object is not reclaimed when being invoked.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputs | [MSTensor](#mstensor)\[\] | Yes | List of input models. |

**Return value**

| Type | Description |
| :-- | :-- |
| Promise<[MSTensor](#mstensor)\[\]> | Promise used to return the result, List of **MSTensor** objects. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input\_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(inputName)
  .then(async (buffer: Uint8Array) => {
    let inputBuffer = buffer.buffer;
    let modelFile = '/path/to/xxx.ms';
    let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
    let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
    modelInputs\[0\].setData(inputBuffer);
    mindSporeLiteModel.predict(modelInputs).then((mindSporeLiteTensor: mindSporeLite.MSTensor\[\]) => {
      let output = new Float32Array(mindSporeLiteTensor\[0\].getData());
      for (let i = 0; i < output.length; i++) {
        console.info(output\[i\].toString());
      }
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### \[h2\]resize

resize(inputs: MSTensor\[\], dims: Array<Array<number>>): boolean

Resets the tensor size.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputs | [MSTensor](#mstensor)\[\] | Yes | List of input models. |
| dims | Array<Array<number>> | Yes | Target tensor size. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the setting is successful. The value **true** indicates that the tensor size is successfully reset, and the value **false** indicates the opposite. |

**Example**

let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  let new\_dim = new Array(\[1, 32, 32, 1\]);
  mindSporeLiteModel.resize(modelInputs, new\_dim);
})

#### \[h2\]runStep12+

runStep(inputs: MSTensor\[\]): boolean

Defines a single-step training model. This API is used only for on-device training.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputs | [MSTensor](#mstensor)\[\] | Yes | List of input models. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the operation is successful. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  mindSporeLiteModel.trainMode = true;
  const modelInputs = mindSporeLiteModel.getInputs();
  let ret = mindSporeLiteModel.runStep(modelInputs);
  if (ret == false) {
    console.error('MS\_LITE\_LOG: runStep failed.')
  }
})

#### \[h2\]getWeights12+

getWeights(): MSTensor\[\]

Obtains all weight tensors of a model. This API is used only for on-device training.

**System capability**: SystemCapability.AI.MindSporeLite

**Return value**

| Type | Description |
| :-- | :-- |
| [MSTensor](#mstensor)\[\] | Weight tensor of the training model. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((modelBuffer: Uint8Array) => {
    mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
      .then((mindSporeLiteModel: mindSporeLite.Model) => {
        mindSporeLiteModel.trainMode = true;
        const weights = mindSporeLiteModel.getWeights();
        for (let i = 0; i < weights.length; i++) {
          let printStr = weights\[i\].name + ", ";
          printStr += weights\[i\].shape + ", ";
          printStr += weights\[i\].dtype + ", ";
          printStr += weights\[i\].dataSize + ", ";
          printStr += weights\[i\].getData();
          console.info("MS\_LITE weights: ", printStr);
        }
      })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### \[h2\]updateWeights12+

updateWeights(weights: MSTensor\[\]): boolean

Weight of the updated model, which is used only for on-device training.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| weights | [MSTensor](#mstensor)\[\] | Yes | List of weight tensors. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the operation is successful. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((modelBuffer: Uint8Array) => {
    mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
      .then((mindSporeLiteModel: mindSporeLite.Model) => {
        mindSporeLiteModel.trainMode = true;
        const weights = mindSporeLiteModel.getWeights();
        let ret = mindSporeLiteModel.updateWeights(weights);
        if (ret == false) {
          console.error('MS\_LITE\_LOG: updateWeights failed.')
        }
      })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### \[h2\]setupVirtualBatch12+

setupVirtualBatch(virtualBatchMultiplier: number, lr: number, momentum: number): boolean

Sets the virtual batch for training. This API is used only for on-device training.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| virtualBatchMultiplier | number | Yes | Virtual batch multiplier. If the value is less than **1**, the virtual batch is disabled. |
| lr | number | Yes | Learning rate. |
| momentum | number | Yes | Momentum. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the operation is successful. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let modelFile = 'xxx.ms';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(modelFile)
  .then((modelBuffer: Uint8Array) => {
    mindSporeLite.loadTrainModelFromBuffer(modelBuffer.buffer.slice(0))
      .then((mindSporeLiteModel: mindSporeLite.Model) => {
        mindSporeLiteModel.trainMode = true;
        let ret = mindSporeLiteModel.setupVirtualBatch(2, -1, -1);
        if (ret == false) {
          console.error('MS\_LITE setupVirtualBatch failed.')
        }
      })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### \[h2\]exportModel12+

exportModel(modelFile: string, quantizationType?: QuantizationType, exportInferenceOnly?: boolean, outputTensorName?: string\[\]): boolean

Exports a training model. This API is used only for on-device training.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| modelFile | string | Yes | File path of the training models. The string length is subject to the file system. |
| quantizationType | [QuantizationType](#quantizationtype12) | No | Quantization type. The default value is **NO\_QUANT**. |
| exportInferenceOnly | boolean | No | Whether to export inference models only. The value **true** means to export only inference models, and the value **false** means to export both training and inference models. The default value is **true**. |
| outputTensorName | string\[\] | No | Name of the output tensor of the exported training model. The default value is an empty string array, which indicates full export. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the operation is successful. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

let modelFile = '/path/to/xxx.ms';
let newPath = '/newpath/to';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  mindSporeLiteModel.trainMode = true;
  let ret = mindSporeLiteModel.exportModel(newPath + "/new\_model.ms", mindSporeLite.QuantizationType.NO\_QUANT, true);
  if (ret == false) {
    console.error('MS\_LITE exportModel failed.')
  }
})

#### \[h2\]exportWeightsCollaborateWithMicro12+

exportWeightsCollaborateWithMicro(weightFile: string, isInference?: boolean, enableFp16?: boolean, changeableWeightsName?: string\[\]): boolean

Exports model weights for micro inference. This API is available only for on-device training.

Micro inference is an ultra-lightweight micro AI deployment solution provided by MindSpore Lite to deploy hardware backends for Micro Controller Units (MCUs). This solution directly converts models into lightweight code in offline mode, eliminating the need for online model parsing and graph compilation.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| weightFile | string | Yes | Path of the weight file. The string length is subject to the file system. |
| isInference | boolean | No | Whether to export weights from the inference model. The value **true** means to export weights from the inference model. The default value is **true**. Currently, only **true** is supported. |
| enableFp16 | boolean | No | Whether to store floating-point weights in float16 format. The value **true** means to store floating-point weights in float16 format, and the value **false** means the opposite. The default value is **false**. |
| changeableWeightsName | string\[\] | No | Name of the variable weight. The default value is an empty string array. |

**Return value**

| Type | Description |
| :-- | :-- |
| boolean | Result indicating whether the operation is successful. The value **true** indicates that the operation is successful, and the value **false** indicates the opposite. |

**Example**

let modelFile = '/path/to/xxx.ms';
let microWeight = '/path/to/xxx.bin';
mindSporeLite.loadTrainModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let ret = mindSporeLiteModel.exportWeightsCollaborateWithMicro(microWeight);
  if (ret == false) {
    console.error('MSLITE exportWeightsCollaborateWithMicro failed.')
  }
})

#### MSTensor

Represents an **MSTensor** instance, with properties and APIs defined. It is a special data structure similar to arrays and matrices. It is the basic data structure used in MindSpore Lite network operations.

In the following sample code, you first need to use [getInputs()](#getinputs) to obtain an **MSTensor** instance before calling related APIs.

#### \[h2\]Attributes

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Type | Read Only | Optional | Description |
| :-- | :-- | :-- | :-- | :-- |
| name | string | No | No | Tensor name. |
| shape | number\[\] | No | No | Tensor dimension array. |
| elementNum | number | No | No | Length of the tensor dimension array. |
| dataSize | number | No | No | Length of tensor data. |
| dtype | [DataType](#datatype) | No | No | Tensor data type. |
| format | [Format](#format) | No | No | Tensor data format. |

**Example**

let modelFile = '/path/to/xxx.ms';
mindSporeLite.loadModelFromFile(modelFile).then((mindSporeLiteModel: mindSporeLite.Model) => {
  let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
  console.info(modelInputs\[0\].name);
  console.info(modelInputs\[0\].shape.toString());
  console.info(modelInputs\[0\].elementNum.toString());
  console.info(modelInputs\[0\].dtype.toString());
  console.info(modelInputs\[0\].format.toString());
  console.info(modelInputs\[0\].dataSize.toString());
})

#### \[h2\]getData

getData(): ArrayBuffer

Obtains tensor data.

**System capability**: SystemCapability.AI.MindSporeLite

**Return value**

| Type | Description |
| :-- | :-- |
| ArrayBuffer | Pointer to the tensor data. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input\_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(inputName)
  .then(async (buffer: Uint8Array) => {
    let inputBuffer = buffer.buffer;
    let modelFile = '/path/to/xxx.ms';
    let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
    let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
    modelInputs\[0\].setData(inputBuffer);
    mindSporeLiteModel.predict(modelInputs).then((mindSporeLiteTensor: mindSporeLite.MSTensor\[\]) => {
      let output = new Float32Array(mindSporeLiteTensor\[0\].getData());
      for (let i = 0; i < output.length; i++) {
        console.info(output\[i\].toString());
      }
    })
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### \[h2\]setData

setData(inputArray: ArrayBuffer): void

Sets the tensor data.

**System capability**: SystemCapability.AI.MindSporeLite

**Parameters**

| Name | Type | Mandatory | Description |
| :-- | :-- | :-- | :-- |
| inputArray | ArrayBuffer | Yes | Input data buffer of the tensor. |

**Example**

import { common } from '@kit.AbilityKit';
import { UIContext } from '@kit.ArkUI';
import { BusinessError } from '@kit.BasicServicesKit';

let inputName = 'input\_data.bin';
let globalContext = new UIContext().getHostContext() as common.UIAbilityContext;
globalContext.getApplicationContext()
  .resourceManager
  .getRawFileContent(inputName)
  .then(async (buffer: Uint8Array) => {
    let inputBuffer = buffer.buffer;
    let modelFile = '/path/to/xxx.ms';
    let mindSporeLiteModel: mindSporeLite.Model = await mindSporeLite.loadModelFromFile(modelFile);
    let modelInputs: mindSporeLite.MSTensor\[\] = mindSporeLiteModel.getInputs();
    modelInputs\[0\].setData(inputBuffer);
  })
  .catch((error: BusinessError) => {
    console.error("getRawFileContent promise error is " + error);
  });

#### DataType

Tensor data type.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Value | Description |
| :-- | :-- | :-- |
| TYPE\_UNKNOWN | 0 | Unknown type. |
| NUMBER\_TYPE\_INT8 | 32 | Int8 type. |
| NUMBER\_TYPE\_INT16 | 33 | Int16 type. |
| NUMBER\_TYPE\_INT32 | 34 | Int32 type. |
| NUMBER\_TYPE\_INT64 | 35 | Int64 type. |
| NUMBER\_TYPE\_UINT8 | 37 | UInt8 type. |
| NUMBER\_TYPE\_UINT16 | 38 | UInt16 type. |
| NUMBER\_TYPE\_UINT32 | 39 | UInt32 type. |
| NUMBER\_TYPE\_UINT64 | 40 | UInt64 type. |
| NUMBER\_TYPE\_FLOAT16 | 42 | Float16 type. |
| NUMBER\_TYPE\_FLOAT32 | 43 | Float32 type. |
| NUMBER\_TYPE\_FLOAT64 | 44 | Float64 type. |

#### Format

Enumerates tensor data formats.

**System capability**: SystemCapability.AI.MindSporeLite

| Name | Value | Description |
| :-- | :-- | :-- |
| DEFAULT\_FORMAT | \-1 | Unknown data format. |
| NCHW | 0 | NCHW format. |
| NHWC | 1 | NHWC format. |
| NHWC4 | 2 | NHWC4 format. |
| HWKC | 3 | HWKC format. |
| HWCK | 4 | HWCK format. |
| KCHW | 5 | KCHW format. |
