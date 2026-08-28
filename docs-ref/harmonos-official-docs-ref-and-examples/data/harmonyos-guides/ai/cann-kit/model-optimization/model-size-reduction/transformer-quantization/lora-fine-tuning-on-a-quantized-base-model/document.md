# LoRA Fine-Tuning on a Quantized Base Model

#### Introduction

After a Transformer base model is quantized, a LoRA branch can be attached to the quantized base model for scenario-specific training. This quantized base model + floating-point LoRA structure enables quantization loss recovery and continued training for downstream tasks.

Fine-tuning preparations:

1.  Floating-point model: loaded using the Hugging Face open-source framework.
2.  Quantization strategy file: quantization strategy file of the base model with LoRA configuration added.
3.  Quantized base model weights: **trained.pth** saved during base model quantization.
4.  Fine-tuning framework: Transform Trainer library architecture or user-defined training architecture.

Fine-tuning steps:

1.  Add LoRA configuration to the quantization strategy file of the base model.
2.  Use a plugin-based API to modify the model.
3.  Fine-tune the model.
4.  Save the model parameters after training.
5.  Export quantization parameters.
6.  Export the ONNX model.

#### Modifying the Configuration File of the Base Model

{
    "layer\_strategy": {
        "time\_embedding.linear\_1": {
            "type": "<class 'torch.nn.modules.linear.Linear'>",
            "quant\_strategy": "XXX",  ### Quantization strategy of the base model.
            ### Attach the LoRA branch by adding the following configuration.
            "lora\_config": {
                "rank": 32,
                "alpha": 32,
                "quant\_state": false
            }
        }
   }
}

**quant\_state** indicates whether to enable the quantization of the LoRA structure. You are advised to set it to **false** to use the floating-point LoRA for training.

#### Using the Plugin-based API

import os
import torch
from dopt.dopt\_lm.do\_opt import (
    generate\_config\_file,
    optimize\_model,
    set\_trainable\_lora
)
### dopt lora ####
dopt\_config = "dopt\_config\_withlora.json"
model = "your model define"
if not os.path.exists(dopt\_config):
    generate\_config\_file(model, dopt\_config)
    exit()
model = optimize\_model(model, dopt\_config)     ### Base model quantization strategy file with LoRA configuration added.
model.load\_state\_dict(torch.load('xxx.pth'))   ### Base model quantization weight file **trained.pth**, where **strict** is set to **False**.
model = set\_trainable\_lora(model, initia\_method='gaussian')   
## Obtain the torch model combining a quantized base model with externally attached floating-point LoRA. LoRA parameters are trainable while the remaining parameters are frozen. LoRA fine-tuning is supported.
## **initia\_method**: initialization method. The options are **kaiming**, **gaussian**, and **pissa**. If no value is passed to it, all the weights and biases of the model are set to zero.

#### Fine-Tuning the Model

The following is a simple example. You can design the training framework as required.

import torch
from datasets import load\_dataset
from transformers import (
    AutoModelForCausalLM, # Alternatively, you can use other models, such as **AutoModelForSequenceClassification**.
    AutoTokenizer,
    TrainingArguments,
    Trainer,
    DataCollatorForLanguageModeling
)
from dopt.dopt\_lm.do\_opt import (
    optimize\_model,
    set\_trainable\_lora
)
# -------------------- 1. Define the model and tokenizer. --------------------
# The following is an LLM example for text generation. You can replace it with a model for any other task.
MODEL\_NAME = "facebook/opt-125m" # Replace it with the model you want to fine-tune.
OUTPUT\_DIR = "./opt\_lora\_finetuned"
MAX\_SEQ\_LENGTH = 128
tokenizer = AutoTokenizer.from\_pretrained(MODEL\_NAME)
# Many LLMs do not have **pad\_token**. You need to set it during LoRA/PEFT training.
if tokenizer.pad\_token is None:
    tokenizer.pad\_token = tokenizer.eos\_token 
# Load the base model.
model = AutoModelForCausalLM.from\_pretrained(
    MODEL\_NAME, 
    device\_map="auto"
)
# -------------------- 2. Enable LoRA. --------------------
## Use the base model quantization strategy file with LoRA configuration added.
dopt\_config = "dopt\_config.json"  
model = optimize\_model(model, dopt\_config)
## Base model quantization weight file **trained.pth**, where **strict** is set to **False**.
model.load\_state\_dict(torch.load('xxx.pth'), strict=False)   
model = set\_trainable\_lora(model, initia\_method='gaussian')   
# -------------------- 3. Prepare and preprocess the dataset. --------------------
# Example: Load a simple text dataset.
dataset = load\_dataset("Abirate/english\_quotes", split="train")
def preprocess\_function(examples):
    # Simple formatting: Concatenate **quote** and **author**.
    texts = \[f"Quote: {q}\\nAuthor: {a}" for q, a in zip(examples\["quote"\], examples\["author"\])\]
    # Use the tokenizer to encode the data.
    return tokenizer(texts, 
                     padding="max\_length", 
                     truncation=True, 
                     max\_length=MAX\_SEQ\_LENGTH)
# Apply preprocessing.
tokenized\_dataset = dataset.map(
    preprocess\_function, 
    batched=True, 
    remove\_columns=\["quote", "author"\]
)
# (Optional) Split the training dataset and validation dataset.
tokenized\_dataset = tokenized\_dataset.train\_test\_split(test\_size=0.1)
train\_dataset = tokenized\_dataset\["train"\]
eval\_dataset = tokenized\_dataset\["test"\]
# Data collator: Use **DataCollatorForLanguageModeling** for LLM training.
data\_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, 
    mlm=False # Set this parameter to **False** for causal LM (GPT-style) training.
)
# -------------------- 4. Train parameters and the trainer. --------------------
training\_args = TrainingArguments(
    output\_dir=OUTPUT\_DIR,
    per\_device\_train\_batch\_size=4,
    gradient\_accumulation\_steps=4, # Simulate a larger batch size (4 \* 4 = 16).
    warmup\_steps=100,
    max\_steps=500, # Limit the number of training steps to speed up the demonstration.
    learning\_rate=2e-4, # LoRA generally uses a higher learning rate.
    logging\_steps=50,
    save\_strategy="steps",
    save\_steps=500,
    do\_eval=True,
    evaluation\_strategy="steps",
    eval\_steps=500,
    fp16=True, # Enable mixed-precision training to improve the speed.
)
# Initialize the trainer.
trainer = Trainer(
    model=model,
    args=training\_args,
    train\_dataset=train\_dataset,
    eval\_dataset=eval\_dataset,
    tokenizer=tokenizer,
    data\_collator=data\_collator,
)
# -------------------- 5. Start training. --------------------
print("\\n" + "="\*20 + "Start LoRA training" + "="\*20)
trainer.train()
print("="\*20 + "Training completed" + "="\*20)
# -------------------- 6. Save the LoRA adapter. --------------------
torch.save(model.state\_dict(), 'trained\_lora.pth')

#### Exporting Quantization Parameters

For details, please refer to [Quantization Parameter Extraction and Export](../plugin-based-quantization/document.md#section29191455173312). The exported files include the quantization file and **fake\_quant\_weight.pth** that will be used by the ONNX model.

#### Exporting the ONNX Model

Example:

import os
import sys
import onnx
import torch
import tempfile
from onnxsim import simplify
sys.path.append('path/to/dopt\_tool')
from dopt.common\_utils.onnx\_helper import OnnxHelper
from dopt.dopt\_lm.do\_opt import (
    optimize\_model,
    set\_quant\_state
)
def aigc\_model\_save(onnx\_model, save\_path):
    model\_size = onnx\_model.ByteSize()
    file\_name = os.path.basename(save\_path)
    if model\_size > 2 \* 1024 \* 1024 \* 1024:
        logging.info(f"Current ONNX model size is over than 2GB")
        onnx.save(onnx\_model, save\_path, save\_as\_external\_data=True,
                        all\_tensors\_to\_one\_file=True, location=f'{file\_name}.data',
                        size\_threshold=1024, convert\_attribute=False
        )
    else:
        from onnx.shape\_inference import infer\_shapes
        onnx\_model = infer\_shapes(onnx\_model)
        onnx.save(onnx\_model, save\_path)
transformer\_model = "your model define"
transformer\_model = optimize\_model(transformer\_model, './dopt\_config.json')
transformer\_model.load\_state\_dict(torch.load('trained\_lora.pth'))
set\_quant\_state(transformer\_model, False, False)
## Randomly generate the input used for exporting the ONNX model based on the model input.
dummy\_input = ()
transformer\_model(\*dummy\_input) ### Check the model forward inference.
## set you onnx input and output node name
input\_names=\["in0\_name", "in1\_name", "..."\]
output\_names=\["out0\_name", "out1\_name", "..."\]
onnx\_save\_path = './xxx.onnx'
with torch.no\_grad():
    with tempfile.NamedTemporaryFile() as f:
        onnx\_1 = f.name
        torch.onnx.export(
            transformer\_model,
            dummy\_input,
            onnx\_1,
            input\_names=input\_names,
            output\_names=output\_names,
            opset\_version=17,
            do\_constant\_folding=True
        )
        onnx\_model = onnx.load(onnx\_1)
    with tempfile.TemporaryDirectory() as temp\_dir:
        onnx\_2 = temp\_dir + '/tmp.onnx'
        aigc\_model\_save(onnx\_model, onnx\_2)
        onnx\_model = onnx.load(onnx\_2)
        onnx\_rename = OnnxHelper(onnx\_model).onnx\_model
    onnx\_simed,\_ = simplify(
        onnx\_rename,
        skipped\_optimizers=\[
            'fuse\_qkv',
            'fuse\_matmul\_add\_bias\_into\_gemm',
            'eliminate\_duplicate\_initializer'
        \]
    )
    aigc\_model\_save(onnx\_simed, onnx\_save\_path)
