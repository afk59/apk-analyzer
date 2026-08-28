# Heterogeneity

#### Overview

Heterogeneity is a heterogeneous computing capability provided by CANN Kit, enabling your app to take full advantage of the computing acceleration capability of Huawei's hardware platform. It is also compatible with non-Huawei hardware platforms in terms of model computing and computing acceleration. That means, you do not need to develop different models or computing frameworks for different hardware platforms.

As shown in the following diagram, OP1, OP2, and OP5 to OP_n_ are specified for inference on the CPU, and OP3 and OP4 are specified for inference on the NPU.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/19/v3/i4jTUKHMTmGf95h9fnXE8g/en-us_image_0000002496568530.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=17058D2D7EE5517261C5B6DA89FE27780B8E14B6BF1801BC2101186C42B2B262)

Heterogeneity allows for online tuning. The following lists the APIs for online tuning. Click [Online Tuning Development Procedure](#section79081331124811) to learn how to use them. To learn more setting and query APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit).

**Table 1** Online tuning APIs and description
| 
API

 | 

Description

 |
| :-- | :-- |
| 

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningMode(OH\_NNCompilation\* compilation, HiAI\_TuningMode tuningMode);

 | 

Sets the chip tuning mode.

 |
| 

OH\_NN\_ReturnCode HMS\_HiAIOptions\_SetTuningCacheDir(OH\_NNCompilation\* compilation, const char\* cacheDir);

 | 

Sets the cache directory for chip tuning.

 |

#### Online Tuning Development Procedure

1.  Set the chip tuning mode.
    
    -   Call [OH\_NNCompilation\_ConstructWithOfflineModelFile](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_constructwithofflinemodelfile) to read the model buffer and create a model compilation instance.
    -   Call [HMS\_HiAIOptions\_SetTuningMode](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaioptions_settuningmode) to set chip tuning modes in the model compilation instance.
    

2.  Call [HMS\_HiAIOptions\_SetTuningCacheDir](https://developer.huawei.com/consumer/en/doc/harmonyos-references/cannkit#hms_hiaioptions_settuningcachedir) to set the cache directory in the model compilation instance for chip tuning.
3.  Perform model compilation.
    
    Call [OH\_NNCompilation\_Build](https://developer.huawei.com/consumer/cn/doc/harmonyos-references/capi-neural-network-core-h#oh_nncompilation_build) and pass the [model compilation instance you have created](../model-inference/document.md#li810206624) to perform model compilation. A pointer to the compiled model is returned after model compilation is successful. The follow-up procedure is the same as that of [Model Inference](../model-inference/document.md).
    

#### Online Tuning Example

In the following sample code, you will see how to set tuning parameters by calling **SetTuningMode** and **SetTuningCacheDir**, and then perform online tuning.

#include "neural\_network\_runtime/neural\_network\_core.h"
#include "CANNKit/hiai\_options.h"
// Create a model building instance based on an offline model file.
OH\_NNCompilation\* compilation = OH\_NNCompilation\_ConstructWithOfflineModelFile("test.om");
if (compilation == nullptr) {
    return; 
}
// Select the assisted tuning mode.
OH\_NN\_ReturnCode ret = HMS\_HiAIOptions\_SetTuningMode(compilation, HIAI\_TUNING\_MODE\_HETER);
if (ret != OH\_NN\_SUCCESS ) {
    return;
}
// Set the cache directory for assisted tuning.
const char\* cacheDir = "/data/local/tmp";
ret = HMS\_HiAIOptions\_SetTuningCacheDir(compilation, cacheDir);
if (ret != OH\_NN\_SUCCESS ) {
    return;
}
// Compile a model.
ret = OH\_NNCompilation\_Build(compilation);
if (ret != OH\_NN\_SUCCESS ) {
    return;
}
