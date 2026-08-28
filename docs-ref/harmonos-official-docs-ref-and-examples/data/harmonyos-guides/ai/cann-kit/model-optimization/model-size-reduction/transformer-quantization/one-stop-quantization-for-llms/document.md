# One-Stop Quantization for LLMs

#### Introduction

This tool provides the 4-bit quantization capability for large language models (LLMs), which adopts the standard three-phase quantization process including weight quantization, activation quantization, and quantization parameter extraction. The following table describes the three-phase quantization process.

**Table 1** Three-phase quantization process of 4-bit quantization for LLMs
| 
Phase

 | 

Input

 | 

Output

 |
| :-- | :-- | :-- |
| 

Phase 1 (weight quantization)

 | 

-   Provided by you

\- JSON dataset (**text** field as the prompt)

\- HuggingFace model path (your floating-point model)

-   Quantization configuration and execution files

\- config.yaml

\- run.sh

 | 

-   **dopt\_config.json**: After the quantization strategy of this file is configured, perform this phase again.

-   **trained\_quant\_weight.pth**: weight quantization parameters.

NOTE:

You need to manually configure the quantization strategy based on the **dopt\_config.json** file generated in phase 1 and then perform this phase again.

 |
| 

Phase 2 (activation quantization)

 | 

**trained.pth**: used for loading in phase 3 or quantization simulation verification

 |
| 

Phase 3 (quantization parameter extraction)

 | 

-   **fake\_quant\_weight.pth**: used for exporting ONNX models
-   **quant\_params\_file**: weight and activation quantization parameter

 |

#### Preparations for Quantization

-   HuggingFace floating-point model
-   Dataset in JSON format. The text field is used as the prompt keyword.
-   Quantization configuration file [config.yaml](#section19562154641017)
-   Execution script [run.sh](#section11700841124819)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5c/v3/Fw8x0v0XTmSYXagoEzQ0ng/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CCC31C4A2FF2A2A79387871A3D71EB9BAEA3F62C580DDFC450C2FF9B272B671)

-   LLM uses **AutoModelForCausalLM** and **AutoTokenizer** for loading during quantization. Therefore, your HuggingFace floating-point model must meet the requirements of this loading mode.
-   The environment where the **run.sh** script is executed must be the same as your training or inference environment. Otherwise, model loading or inference may fail.

## config.yaml Example

config.yaml is used for model quantization configuration. You can configure it as required. The following example is for reference. For details about the main parameters, please refer to [Configuration Parameters for config.yaml](#section760161441112).

kd:
  enable: False
  loss: mse
  micro\_batch\_size: 2
  gradient\_accumulation\_steps: 4
  weight\_decay: 0.0
  warmup\_steps: 10
  num\_epochs: 3
  learning\_rate: !!float 1e-4
  eval\_step: 1
  logging\_step: 50
  lr\_scheduler\_type: cosine
  trainable\_keys:
    - quant\_alpha
    - norm
  no\_split\_module\_classes:
    - Qwen2DecoderLayer
    - GlmDecoderLayer
    - LlamaDecoderLayer
    - HunYuanDecoderLayer
dataset:
  train\_files: dataset.json
  train\_samples: 1024
  ptq\_samples: 1024
extra\_training\_config:
  fp16: True
cutoff\_len: 128
num\_samples: 256
quant\_param\_2: False
embedding\_separate: True
lm\_head\_size:

## Configuration Parameters for config.yaml

The following table describes the key configuration parameters in the config.yaml file.

| 
Parameter

 | 

Default Value

 | 

Description

 |
| :-- | :-- | :-- |
| 

kd: quantization distillation correlation

 | 

enable

 | 

False

 | 

-   **True:** The distillation quantization strategy is used.
-   **False**: The non-training quantization strategy is used, delivering high efficiency and stable performance.

 |
| 

loss

 | 

mse

 | 

Quantization distillation loss function. Only MSE is supported.

 |
| 

micro\_batch\_size

 | 

2

 | 

Single-graphics card batch.

 |
| 

gradient\_accumulation\_steps

 | 

4

 | 

Gradient accumulated steps.

 |
| 

weight\_decay

 | 

0.0

 | 

Weight decay coefficient.

 |
| 

warmup\_steps

 | 

10

 | 

Warm-up steps.

 |
| 

num\_epochs

 | 

3

 | 

Number of training iterations.

 |
| 

learning\_rate

 | 

1e-4

 | 

Learning rate.

 |
| 

eval\_step

 | 

1

 | 

Number of training steps between evaluations.

 |
| 

logging\_step

 | 

50

 | 

Number of steps for log printing.

 |
| 

lr\_scheduler\_type

 | 

cosine

 | 

Learning rate adjustment strategy.

 |
| 

trainable\_keys

 | 

\-

 | 

Configure trainable parameters.

-   **quant\_alpha**: trainable parameters of the quantization layer.
-   **norm**: trainable parameters of the **layer\_norm** layer.

 |
| 

no\_split\_module\_classes

 | 

\-

 | 

Selects the granularity of multi-graphics card sharding.

-   Qwen2DecoderLayer
-   GlmDecoderLayer
-   LlamaDecoderLayer
-   HunYuanDecoderLayer

 |
| 

dataset

 | 

train\_files

 | 

\-

 | 

Training data file in JSON format, dataset.json.

 |
| 

train\_samples

 | 

1024

 | 

Number of samples in the training dataset when **enable** in **kd** is set to **True**. By default, all samples in the dataset are used.

 |
| 

ptq\_samples

 | 

1024

 | 

Number of PTQ optimization samples. By default, all datasets are used.

 |
| 

extra\_training\_config

 | 

fp16

 | 

True

 | 

Training data type. Only fp16 is supported.

 |
| 

cutoff\_len

 | 

\-

 | 

128

 | 

Activation quantization sample sequence length.

 |
| 

num\_samples

 | 

\-

 | 

256

 | 

Number of activated quantization calibration samples.

 |
| 

quant\_param\_2

 | 

\-

 | 

False

 | 

-   **True**: Kirin 9020
-   **False**: KirinX90

 |
| 

embedding\_separate

 | 

\-

 | 

True

 | 

-   **True**: The dataset is saved separately as a .bin file.
-   **False**: The embedding quantization parameters are exported to the quantization file.

 |
| 

lm\_head\_size

 | 

\-

 | 

\-

 | 

lm\_head length, which must meet the hardware alignment constraint.

 |

#### Performing Three-Phase Quantization

Perform the following steps to run the **run.sh** file (**stagex** is an input parameter). For details, see [run.sh Example](#section11317363241).

1.  Start weight quantization.
    
    1.  Select a quantization strategy.
        
        Generate the plugin-based quantization configuration file [dopt\_config.json](#section15113659191318).
        
        /\*bash run.sh stage1\*/ 
        
        The quantization strategy can be set to:
        
        /\*
        Quant\_act\_weight\_eco   Strategy for the decode layer.
        Quant\_lm\_head          Strategy for the lm\_head layer.
        Quant\_Embed\_MinMax     Strategy for the embedding layer.
        \*/
        
    2.  Perform weight quantization.
        
         /\*bash run.sh stage1\*/
        
    
2.  Activate quantization.
    
    /\*bash run.sh stage2\*/
    
3.  Extract quantization parameters.
    
    /\*bash run.sh stage3\*/
    

## run.sh Example

#!/bin/bash
set -e
qlibs='path/to/dopt\_pytorch\_py3'
export WANDB\_DISABLED=true
export HF\_DATASETS\_OFFLINE=0
export PYTHONPATH=${qlibs}:$PYTHONPATH
# Set the mode to CUDA or NPU.
# CUDA mode.
export DEVICE=cuda
export CUDA\_VISIBLE\_DEVICES=1
# NPU mode.
# export DEVICE=npu
# export ASCEND\_RT\_VISIBLE\_DEVICES=2,3
ROOT=.
testcase='output\_dir'
RUN\_FILE=${qlibs}/dopt/dopt\_lm/opt\_main.py
output\_dir=${ROOT}/${testcase}/train\_output
mkdir -p ${output\_dir}
cp ${ROOT}/config.yaml $output\_dir
model\_path='path/to/model'
dopt\_config=./${testcase}/dopt\_config.json
quant\_stage=$1
block\_size=128 
python -u \\
    ${RUN\_FILE} --model-path $model\_path \\
    --dopt-config $dopt\_config \\
    --optimize-config ${ROOT}/config.yaml \\
    --quant-stage $quant\_stage \\
    --block-size $block\_size \\
    --output-dir ${output\_dir} 2>&1 | tee ${output\_dir}/logs.log

## Quantization Configuration File dopt\_config.json

The following plugin-based LLM quantization specifications can be developer-defined:

-   Bit width (bit) and group size (group\_size) of layer-wise weight quantization.
-   Bit width (bit) of layer-wise activation quantization.
-   Quantization strategy: The decoder layer uses **Quant\_act\_weight\_eco**, the lm\_head layer uses **Quant\_lm\_head**, and the embedding layer uses **Quant\_Embed\_MinMax**.

{
     "layer\_strategy": {
         "model.layers.0.self\_attn.q\_proj": {
             "type": "<class 'torch.nn.modules.linear.Linear'>",
             "quant\_strategy": "Quant\_act\_weight\_eco",
             "weight":{
                 "bit": 4,
                 "group\_size": 64
             }
             "input":{
                 "bit": 16
             }
         }
         // ...
 }

#### Output of Quantization Tools

trained.pth            ### This file can be used for quantization simulation.
fake\_quant\_weight.pth  ### This weight is used for exporting the ONNX file.
trained\_quant\_weight.pth ### Output of phase 1 and input of phase 2.

#### Quantization Simulation

After quantization is complete, you can perform quantization simulation inference to compare the output results of the quantized model with those of the original floating-point model to evaluate whether the accuracy of the quantized model meets the requirements. For details about the inference project for quantization simulation, please refer to [Qwen2 Model Quantization Simulation Inference Demo](#section20831155341215).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/20/v3/YsdASXTzSmGvYc-2tWVTrw/en-us_image_0000002496888566.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DCB2EDF7F01990CB777E05FB83A1D6608E68D8C1727B872A84A245BAD24AD3F4 "Click to enlarge")

## Plugin Method

After the floating-point model is loaded and initialized, use the following APIs to convert the floating-point model into a quantized model. The inference logic of the model remains unchanged. For details, please refer to [Qwen2 Model Quantization Simulation Inference Demo](#section20831155341215).

import sys
sys.path.append("path/to/dopt")
def get\_quanted\_model(base\_model, dopt\_config, quanted\_ckpt):
     from dopt.dopt\_llm.do\_opt import(
         optimize\_model,
         set\_quant\_state,
         set\_calibrate\_state,
         set\_run\_mode,
     )
     model = optimize\_model(base\_model, dopt\_config)
     model.load\_state\_dict(torch.load(quanted\_ckpt, map\_location=torch.device('cpu')), strict=True)
     set\_quant\_state(model, weight\_state=True, input\_state=True)
     set\_calibrate\_state(model, False)    
     model.eval()
     return model

-   **base\_model**: your floating-point model (loaded using the **AutoModelForCausalLM** class in the **transformers** library).
-   **dopt\_config**: quantization configuration file.
-   **quanted\_ckpt**: .pth file after quantization.

## Qwen2 Model Quantization Simulation Inference Demo

import os
import sys
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
sys.path.append('path/to/dopt')
os.environ\["CUDA\_VISIBLE\_DEVICES"\] = "0"
def get\_quanted\_model(base\_model, dopt\_config, quanted\_ckpt):
    """
    Core functions for loading quantized models
    :param base\_model: original HF model object
    :param dopt\_config: path of the quantization configuration file (dopt\_config.json)
    :param quanted\_ckpt: quantization weight path (trained.pth)
    :return: quantized model
    """
    from dopt.dopt\_llm.do\_opt import(
        optimize\_model,
        set\_quant\_state,
        set\_calibrate\_state,
        set\_run\_mode,
    )
    # Optimize model quantization (by applying the 4-bit quantization strategy based on the configuration file).
    model = optimize\_model(base\_model, dopt\_config)
    # Load the quantization weight (force the CPU to load the quantization weight to avoid GPU memory conflicts).
    model.load\_state\_dict(torch.load(quanted\_ckpt, map\_location=torch.device('cpu')), strict=True)
    # Set the quantization status.
    set\_quant\_state(model, weight\_state=True, input\_state=True) # Enable weight and activation quantization.
    set\_calibrate\_state(model, False) #: Disable the calibration mode.
    model.eval()
    return model
def generate(prompt = "Give me a short introduction to large language model."):
    """
    Inference function of the quantized model
    :param prompt: input text (default example: prompt)
    :return: response generated by the model
    """
    # Create a dedicated Qwen2 dialog template.
    messages = \[
        {"role": "system", "content": "You are Qwen, created by Alibaba Cloud..."},
        {"role": "user", "content": prompt}
    \]
    # Apply the template and tokenize it.
    text = tokenizer.apply\_chat\_template(
        messages,
        tokenize=False,
        add\_generation\_prompt=True
    )
    model\_inputs = tokenizer(\[text\], return\_tensors="pt").to(model.device)
    # Execute the generation.
    generated\_ids = model.generate(
        \*\*model\_inputs,
        max\_new\_tokens=512, # Control the maximum generation length.
    )
    # Post-processing: Remove the input part.
    generated\_ids = \[
        output\_ids\[len(input\_ids):\]
        for input\_ids, output\_ids in zip(model\_inputs.input\_ids, generated\_ids)
    \]
    return tokenizer.batch\_decode(generated\_ids, skip\_special\_tokens=True)\[0\]
if \_\_name\_\_ == '\_\_main\_\_':
    # === 1. Load the original model. ===
    model\_name = "path/to/model"  # Replace it with the actual model path.
    model = AutoModelForCausalLM.from\_pretrained(
        model\_name,
        torch\_dtype=torch.float16,  # Half-precision loading.
        device\_map="auto"           # Automatically allocate GPUs.
    )
    tokenizer = AutoTokenizer.from\_pretrained(model\_name)
    # === 2. Load the quantized model. ===
    quant\_res\_root = 'dsr1\_qwen7b\_ptq' # Quantization result directory.
    dopt\_config = f"./{quant\_res\_root}/dopt\_config.json"    # Configuration file generated in phase 1.
    quanted\_ckpt = f"./{quant\_res\_root}/train\_output/trained.pth"  # Weight generated in phase 2.
    model = get\_quanted\_model(
        model,
        dopt\_config,  # Ensure that quantization parameters have been correctly configured.
        quanted\_ckpt  # Must match the current model architecture.
    )
    # === 3. Perform the inference test. ===
    prompt = "who are you?"
    response = generate(prompt)
    print ("Inference result of the quantized model:", response)
    """
    Expected output example:
    "Hi, I am Qwen, ..."
    """
