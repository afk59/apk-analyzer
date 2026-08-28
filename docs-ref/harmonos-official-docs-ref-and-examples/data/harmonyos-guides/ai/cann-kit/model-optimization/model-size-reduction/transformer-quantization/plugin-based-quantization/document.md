# Plugin-based Quantization

#### Introduction

Plugin-based quantization is model-agnostic, providing support for language and vision models. It enables fast quantization for Transformer models.

#### Overall Process

There are two quantization parameter optimization strategies: post-training quantization (PTQ) and quantization-aware training (QAT). PTQ completes quantization calibration using the inference project, while QAT requires integration with the training project.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ca/v3/soyNORk3QbGdQphO86iT0A/en-us_image_0000002500113940.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3924E81F42DFB30569B5F3DAB2CD3497A39DB92C7E2554672C0F8E6B8B34C1AD "Click to enlarge")

#### API Usage Description

import os
import sys
sys.path.append('path/to/dopt\_torch\_py3')
####  Import APIs.
from dopt.dopt\_lm.do\_opt import (
    generate\_config\_file,   ## Generate a quantization configuration file.
    optimize\_model,         ## Convert the floating-point nn.module into the nn.module with quantization operators inserted using the configured quantization configuration file.
    set\_quant\_state,        ## Enable quantization inference separately for activations and weights.
    set\_calibrate\_state,    ## Set the updatable states of quantization parameters.
    generate\_quant\_params,  ## Export quantization parameters.
)
#### Insert quantization operators. A quantization configuration file is generated when this API is called for the first time. Once the file is configured, execute PTQ or QAT.
def get\_quant\_model(model, dopt\_config):
    ## **model**: nn.module instance object, which is of the floating-point type.
    ## **dopt\_config**: quantization configuration file path. The value is **path/to/config.json**.
    if not os.path.exists(dopt\_config):
        generate\_config\_file(model, dopt\_config)
        exit()
    model = optimize\_model(model, dopt\_config)
    return model

**Quantization strategy configuration:**

{
    "layer\_strategy": {
        "node\_name": {
            "type": "<class 'torch.nn.modules.linear.Linear'>",
            "quant\_strategy": "need to set",
            "weight": {
                "bit": 4,
                "group\_size": 128,
                "weight\_algo": "group\_min\_max",
            },
            "input" : {
                "bit" : 8,
                "input\_algo":  "min\_max",
                "unsigned\_quant": True
            }
        }
    }
}

**Configuration description:**

Each strategy (specified by **quant\_strategy**) has its own default settings. Configure the strategies one by one. The following table describes the parameters.

**Table 1** Parameters
| 
Parameter

 | 

Option

 | 

Description

 |
| :-- | :-- | :-- |
| 

quant\_strategy

 | 

Quant\_aigc\_ptq

Quant\_aigc\_qat

Quant\_act\_weight\_eco

Quant\_lm\_head

Quant\_Embed\_MinMax

 | 

PTQ quantization strategy. The default value is **U8S8**. The quantizer is a **minmax**.

QAT quantization strategy. The default value is **U8S8**. The quantizer is **omni\_minmax**.

16-4 group-linear quantization strategy. The default **group\_size** is set to **128**. This strategy is for LLMs only. The QAT quantizer is used.

16-4 group-linear quantization strategy. The default **group\_size** is set to **128**. This strategy is for LLMs only. The QAT quantizer is used.

8-bit embedding quantization.

 |
| 

weight

 | 

bit

 | 

4, 8

 | 

Weight quantization bit width.

 |
| 

group\_size

 | 

128, 256

 | 

With a weight bit of 4, the model is considered low-bit quantization. In this case, set this key-value pair only when group-linear quantization is used.

 |
| 

weight\_algo

 | 

min\_max

group\_min\_max

omni\_min\_max

omni\_group\_min\_max

 | 

Per-channel quantization. The min-max statistics are used for PTQ.

Per-group quantization. The min-max statistics are used for PTQ.

QAT quantizer, which uses the per-channel quantization granularity.

QAT quantizer, which uses the per-group quantization granularity.

 |
| 

input

 | 

bit

 | 

8, 16

 | 

Activation quantization bit width.

 |
| 

input\_algo

 | 

min\_max

ema

omni\_min\_max

 | 

Per-tensor quantization. The min-max statistics are used for PTQ, resulting in minimal clipping error.

Per-tensor quantization. The moving average statistics are used for PTQ, resulting in minimal rounding error.

Per-tensor quantization. The QAT quantizer is used.

 |
| 

unsigned\_quant

 | 

True

False

 | 

Asymmetric quantization.

Symmetric quantization.

 |

#### PTQ for Quantization Parameter Optimization

In the generated **quant\_config**, the float strategy is used for each layer. Change the strategy to **Quant\_aigc\_ptq**. See the preceding table for advanced parameter settings.

Use the inference project and select a proper amount of data to perform forward inference on the model returned by the **get\_quant\_model** API. This process optimizes the model's quantization. The sample code is provided below:

\## A configuration file is generated upon the first call. You need to manually configure the quantization strategy in the file.
model = get\_quant\_model(model, quant\_config)  
model.eval()
## Enable the quantizer.
set\_quant\_state(model, weight\_state=True, input\_state=True)
## Enable the quantization parameter calibration status.
set\_calibrate\_state(model, True)  
## Use real inference data to perform quantization calibration. ###
for data in datasets:
    model(data)
set\_calibrate\_state(model, False)
torch.save(model.state\_dict(), 'pth\_save\_path')

#### QAT for Quantization Parameter Optimization

In the generated **quant\_config**, the float strategy is used for each layer. Change the strategy to **Quant\_aigc\_qat**. See the preceding table for advanced parameter settings.

Use the training project to train the model with quantization operators.

model = get\_quant\_model(model, quant\_config)
model.train()
set\_quant\_state(model, weight\_state=True, input\_state=True)
set\_calibrate\_state(model, True)
"""
do training
"""
set\_calibrate\_state(model, False)
torch.save(model.state\_dict(), 'pth\_save\_path')

#### Quantization Parameter Extraction and Export

from dopt.dopt\_llm.do\_opt import generate\_quant\_params, optimize\_model
## **model**: floating-point nn.module instance object; **quant\_config**: quantization configuration file.
model = optimize\_model(model, quant\_config)  
## Load the .pth file saved after quantization calibration.
model.load\_state\_dict(
    torch.load('pth\_save\_path', map\_location=torch.device('cpu')),
    strict=True,
)
## Disable quantization parameter update and export quantization parameters.
## Tips: Parameter export can be executed immediately upon the completion of calibration. However, these steps are separated to enhance process integrity, mitigating the risk of errors requiring the repetition of prior stages.
set\_quant\_state(model, weight\_state=True, input\_state=True)
set\_calibrate\_state(model, False)
generate\_quant\_params(
    model,
    output\_dir,
    quant\_param\_2=False,
    embedding\_separate=True,
)
## The **fake\_quant\_weight.pth** file and quantization parameter file are generated in **output\_dir**. **fake\_quant\_weight.pth** is used only to replace weights when the ONNX graph is exported.

**ONNX export:**

Use **torch.onnx.export** to export the floating-point model (**fake\_quant\_weight.pth** needs to be loaded). If necessary, simplify the ONNX model, and ensure that the names of convolution operators and linear operators remain consistent with those defined by **torch**.
