# Plugin-based Quantization

#### Preparing the Dependency Environment

Plugin-based quantization depends on the environment of your training project. Currently, the size reduction tool supports two frameworks for plugin-based quantization: TensorFlow and PyTorch.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/cLdIxrdzQOGBFqoUBRgbIQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=44E1B7661F65C7B65DDBA8503D89941125C9577EF467502479A102540F07F9BE)

After the environment is configured for plugin-based quantization, quantization can be performed in either non-training or retraining mode.

#### TensorFlow Plugin-based Quantization

Perform the following steps for tuning a TensorFlow model:

Prerequisites: The model training datasets and full-precision base model (.ckpt file) have been prepared.

1.  Prepare the TensorFlow environment ([Preparing the TensorFlow Environment](#section103814481178)).
2.  Call the API to generate a strategy template for model tuning ([Obtaining the Template for Quantization Configuration](#section7308624487)).
3.  Configure the tuning strategy file ([Configuring the Tuning Strategy](#section1035414781018)).
4.  Train the model ([Training or Calibrating the Model](#section184938114114)). (Models are trained in retraining mode and calibrated in non-training mode.)
5.  Extract the model and quantization parameters ([Converting the Model](#section11929116113114)).

## Preparing the TensorFlow Environment

Prepare the Linux environment. To use the plugin-based quantization function of the size reduction tool, you need to prepare the following dependencies.

-   Python 3.10
-   Python dependencies:
    
    pip3 install ruamel\_yaml
    pip3 install pathlib
    pip3 install protobuf==3.20.0
    pip3 install opencv-python
    
-   Currently, the size reduction tool supports tensorflow-gpu 2.8.0. Run the following command to install it:
    
    pip3 install tensorflow-gpu==2.8.0
    

## Obtaining the Template for Quantization Configuration

Add **dopt\_tf\_py3** in the decompressed DDK to the Python environment variable:

import sys
sys.path.append(".../dopt\_tf\_py3") ## The path should be an absolute path.

Call the API to generate a JSON quantization configuration file for the PyTorch model to be quantized.

from dopt.dopt\_tf.opt\_main import generate\_config\_file
generate\_config\_file(sess, dst\_path="./config\_gen.json")

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

sess

 | 

Yes

 | 

**sess** is used to load the original floating-point TensorFlow model.

 |
| 

dst\_path

 | 

Yes

 | 

**dst\_path** indicates the path of the generated JSON configuration file.

 |

The generated configuration is as follows:

{
    "quant\_strategy\_for op 'Conv2D'": \[
        "Quant\_INT8-8"
    \],
    "quant\_strategy\_for op 'MatMul'": \[
        "Quant\_INT8-8"
    \],
    "layer\_strategy": {
        "model/resnet\_model/conv2d/Conv2D": {
            "op\_type": "Conv2D",
            "quant\_strategy": "float"
        },
        "model/resnet\_model/conv2d\_1/Conv2D": {
            "op\_type": "Conv2D",
            "quant\_strategy": "float"
        },
        // ...
    }
}

## Configuring the Tuning Strategy

Determine the layer to be quantized based on the configuration file generated above, and change the value of **quant\_strategy** from **float** to the quantization strategy (for example, **Quant\_INT8-8**).

{
    "quant\_strategy\_for op 'Conv2D'": \[
        "Quant\_INT8-8"
    \],
    "quant\_strategy\_for op 'MatMul'": \[
        "Quant\_INT8-8"
    \],
    "layer\_strategy": {
        "model/resnet\_model/conv2d/Conv2D": {
            "op\_type": "Conv2D",
            "quant\_strategy": "Quant\_INT8-8"
        },
        "model/resnet\_model/conv2d\_1/Conv2D": {
            "op\_type": "Conv2D",
            "quant\_strategy": "Quant\_INT8-8"
        },
        // ...
    }
}

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/78/v3/s3U7lbyIRhKqfrknKrWdFw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9CCCD95E903D544DDEC0417EF52F9624095A813CB4D792094705848CE189E01B)

-   _layer\_strategy_ contains all layers that can be quantized in the current version. Please do not add any layers additionally.
-   You need to select a supported quantization strategy based on _op\_type_. If _op\_type_ is set to an unsupported quantization strategy, errors will be reported in subsequent quantization phases.

## Model Training

To perform plugin-based quantization, add the path of the **dopt\_tf\_py3** file in the decompressed DDK to the Python environment variable:

import sys
sys.path.append(".../dopt\_tf\_py3") ## The path should be an absolute path.

from dopt.dopt\_tf.opt\_main import optimize\_model

Call the **optimize\_model** API to construct a model in _session_ and quantize the model based on the configured JSON quantization strategy.

-   Set the flag _is\_train\_flag_, which indicates whether the current quantization parameters will be updated during model training.
-   Set the flag _quant\_flag_, which indicates whether the model uses the quantization mode.
    
    with tf.Session(config=config) as sess:
         ## Graph of the TensorFlow model to be quantized. Only the topology will be built, and the weight will not be loaded.
        build\_tf\_model()
        quant\_flag = tf.placeholder(tf.int32)
        is\_train\_flag = tf.placeholder(tf.bool, name='is\_train')
      ## Quantize the model. The graph will be automatically modified in **tf.get\_default\_graph()**.
        optimize\_model( 
            sess,
            config\_file,
            is\_train\_flag,
            quant\_flag
        )
    
        ## Load the model weight after calling **optimize\_model**.
        saver = tf.Saver()
        saver.restore(ckpt)
        tf.global\_variables\_initializer().run()
    

-   **build\_tf\_model**: model graph to be quantized in **session**. You can define it as needed.
-   **quant\_flag**: tf.int32 type. Value **0** indicates that the floating-point mode (no quantization) is used, and value **1** (or any other positive value) indicates that the quantization mode is used. This parameter works in tandem with **is\_train\_flag**.
-   **is\_train\_flag**: When the value of **quant\_flag** is greater than **0**, this parameter indicates whether the quantization parameters will be updated during model training.
    
    | 
    **Parameter**
    
     | 
    
    **Mandatory**
    
     | 
    
    **Description**
    
     |
    | :-- | :-- | :-- |
    | 
    
    sess
    
     | 
    
    Yes
    
     | 
    
    _sess_ is used to load the original floating-point TensorFlow model.
    
     |
    | 
    
    config\_file
    
     | 
    
    Yes
    
     | 
    
    Path of the JSON file for the layer to be quantized. You need to set this parameter manually.
    
     |
    | 
    
    is\_train\_flag
    
     | 
    
    Yes
    
     | 
    
    Whether the current quantization parameters of the model are updated during model training.
    
     |
    | 
    
    quant\_flag
    
     | 
    
    Yes
    
     | 
    
    Whether the model uses the quantization mode.
    
     |
    

Train the model, and determine whether the model has met the expected results by checking the loss of the loss function. If so, stop the training and save the checkpoint (CKPT) data.

\## ckpt save 
saver = tf.train.Saver() 
saver.save(sess, train\_ckpt\_path)

To perform non-training quantization, call the **set\_calibrate\_state** API to enable the non-training mode.

from dopt.dopt\_tf.opt\_main import set\_calibrate\_state 

calibration\_mode = True
set\_calibrate\_state(sess, calibration\_mode ) 

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

sess

 | 

Yes

 | 

Quantized TensorFlow session.

 |
| 

calibration\_mode

 | 

Yes

 | 

Boolean variable, indicating whether to enable the non-training (calibration) mode.

-   **True**: Enable the non-training (calibration) mode.
-   **False**: Disable the non-training (calibration) mode.

 |

After setting the non-training mode, use the quantized session (**sess**) to perform forward inference on the calibration set. Then you will be able to start non-training quantization.

## Model Conversion

Collect quantization parameters after you have completed model quantization and retraining, or completed forward inference on the calibration set. Extract the quantization parameters from the session to the quantization configuration file, and generate the corresponding PB file.

Add the path of the **dopt\_tf\_py3** file in the decompressed DDK to the Python environment variable.

import sys
sys.path.append(".../dopt\_tf\_py3") ## The path should be an absolute path.

from dopt.dopt\_tf.opt\_main import generate\_final\_model

Initialize the original floating-point model, load the CKPT file used for model quantization and training, and use the provided API to extract parameters.

with tf.Session(config=config) as sess:
    build\_tf\_model()
        generate\_final\_model(
        sess,
        config\_file         = FLAGS.config\_file,
        output\_name\_list    = output\_name\_list,
        ckpt\_file           = train\_ckpt\_path,
        output\_dir          = output\_dir
    )

**build\_tf\_model**: model graph to be quantized in **session**. You can define it as needed.

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

sess

 | 

Yes

 | 

_sess_ is used to load the original floating-point TensorFlow model.

 |
| 

config\_file

 | 

Yes

 | 

Path of the JSON file for the layer to be quantized, which should be the same as the settings when you call **optimize\_model**. You need to set this parameter manually.

 |
| 

output\_name\_list

 | 

Yes

 | 

Name of the output node at the last layer of the PB model. The data type is **list**.

 |
| 

ckpt\_file

 | 

Yes

 | 

CKPT data saved during retraining or calibration.

 |
| 

output\_dir

 | 

No

 | 

Path for saving the extracted PB file and quantization parameters. Make sure that you set a valid path. If this parameter is not set, the model will be saved in the current path.

 |

#### PyTorch Plugin-based Quantization

Perform the following steps for tuning a PyTorch model:

Prerequisites: The model training datasets and full-precision base model (.pth file) have been prepared.

1.  Prepare the PyTorch environment ([Preparing the PyTorch Environment](#section461318612307)).
2.  Call the API to generate a JSON quantization configuration file ([Generating a JSON Quantization Configuration File](#section1374313714435)).
3.  Change the strategy file configuration ([Configuring the Tuning Strategy](#section16522384430)).
4.  Call the API to train and quantize the model ([Training or Calibrating the Model](#section767733515413)).
5.  Call the API to generate the quantized ONNX model and quantization parameter file ([Generating a Quantized Model](#section1567210444438)).

## Preparing the PyTorch Environment

To use the plugin-based quantization function of the size reduction tool, you need to prepare the following dependencies.

-   Python 3.10
-   Python dependencies:
    
    pip3 install ruamel\_yaml
    pip3 install pathlib
    pip3 install protobuf>=3.20.0
    pip3 install onnx==1.14.0
    
-   Currently, the size reduction tool supports only PyTorch 1.11. Run the following command to install it:
    
    pip3 install torch==1.11.0
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9b/v3/rVlZmRZLREGVHeaqcX2g8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2C5CE710DAB1706EE8CA7207AC82B9BA37B53ACC285E2A120B0EB9BBA7D7FC8)

-   The path can contain uppercase letters, lowercase letters, digits, and underscores (\_).
-   The file name can contain uppercase letters, lowercase letters, digits, underscores (\_), and periods (.).

## Generating a JSON Quantization Configuration File

Add the path of the **dopt\_pytorch\_py3** file in the decompressed DDK to the Python environment variable.

import sys
sys.path.append(".../dopt\_pytorch\_py3") ## The path should be an absolute path.

from dopt.dopt\_torch.opt\_main import generate\_config\_file

Call the API to generate a JSON quantization configuration file for the PyTorch model to be quantized.

generate\_config\_file(model, input\_shape, dst\_path="./config\_gen.json") # model: torch.nn.Module, input\_shape : "input1:input1.shape;input2:input2.shape"

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

model

 | 

Yes

 | 

This parameter is of the **torch.nn.Module** type, indicating models not encapsulated by distributed APIs such as **torch.nn.parallel.DistributedDataParallel**.

 |
| 

input\_shape

 | 

Yes

 | 

Shape of the final model to be deployed, not the shape of the training data in the training phase.

 |
| 

dst\_path

 | 

Yes

 | 

Path of the generated JSON configuration file.

 |

## Configuring the Tuning Strategy

The generated configuration is as follows:

{
    "quant\_strategy\_for op '<class 'torch.nn.modules.conv.Conv2d'>'": \[
        "Quant\_INT8-8"
    \],
    "quant\_strategy\_for op '<class 'torch.nn.modules.linear.Linear'>'": \[
        "Quant\_INT8-8"
    \],
    "input\_shape": "x:1,3,224,224",
    "params\_version": "v1", // This parameter is optional. The default value is **v1**. If you want to export the configuration as v2, set this parameter to **v2**.
    "layer\_strategy": {
        "conv1/Conv2D": {
            "op\_type": "<class 'torch.nn.modules.conv.Conv2d'>",
            "quant\_strategy": "float"
        },
        "conv2/Conv2D": {
            "op\_type": "<class 'torch.nn.modules.conv.Conv2d'>",
            "quant\_strategy": "float"
        },
        // ...
    }
}

You can modify the quantization configuration as required.

-   You can set the quantization strategy by layer. The default quantization strategy is **float**.
-   The supported **Quant\_INT8-8** quantization strategy is **8a8w**.

Taking the preceding JSON configuration as an example, you can modify it as follows:

{
    "quant\_strategy\_for op '<class 'torch.nn.modules.conv.Conv2d'>'": \[
        "Quant\_INT8-8"
    \],
    "quant\_strategy\_for op '<class 'torch.nn.modules.linear.Linear'>'": \[
        "Quant\_INT8-8"
    \],
    "input\_shape": "x:1,3,224,224",
    "params\_version": "v1", // This parameter is optional. The default value is **v1**. If you want to export the configuration as v2, set this parameter to **v2**.
    "layer\_strategy": {
        "conv1/Conv2D": {
            "op\_type": "<class 'torch.nn.modules.conv.Conv2d'>",
            "quant\_strategy": "Quant\_INT8-8",
        },
        "conv2/Conv2D": {
            "op\_type": "<class 'torch.nn.modules.conv.Conv2d'>",
            "//": "You can set the quantization strategy by layer, and keep the float strategy for layers not to be quantized."
            "quant\_strategy": "float"
        },
        // ...
    }
}

-   **layer\_strategy** contains all layers that can be quantized in the current version. Please do not add any layers additionally.
-   You need to select a supported quantization strategy based on _op\_type_. If _op\_type_ is set to an unsupported quantization strategy, errors will be reported in subsequent quantization phases.
-   In the JSON file, except the **input\_shape** and **layer\_strategy** keys, other content is for your reference only and will not be parsed.
-   The parameter format has been upgraded to adapt to the new platform. **"params\_version": "v2"** is added under the key at the same level as **input\_shape**.

## Model Training

Add the path of the **dopt\_pytorch\_py3** file in the decompressed DDK to the Python environment variable.

import sys
sys.path.append(".../dopt\_pytorch\_py3") ## The path should be an absolute path.
from dopt.dopt\_torch.opt\_main import optimize\_model

You need to call APIs for model quantization in the phase of defining the PyTorch model.

quant\_model = optimize\_model(model, config\_path) ## **config\_path** indicates the JSON file's absolute path you have modified in the previous step.

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

model

 | 

Yes

 | 

This parameter is of the **torch.nn.Module** type, indicating models not encapsulated by distributed APIs such as **torch.nn.parallel.DistributedDataParallel**.

 |
| 

config\_path

 | 

Yes

 | 

Shape of the final model to be deployed, not the shape of the training data in the training phase.

 |

You can call APIs as required to obtain quantization-related loss functions and add them to the tuning and training job (optional and not recommended for simple jobs).

from dopt.dopt\_torch.opt\_main import get\_quant\_loss
quant\_loss = get\_quant\_loss(quant\_model)
total\_loss = loss + quant\_weight \* quant\_loss ## **quant\_weight** is a hyperparameter of the quantization loss.

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

quant\_model

 | 

Yes

 | 

Quantized model after the **optimize\_model** API is called.

 |

Save the checkpoint of the quantized and trained model.

torch.save(quant\_model.state\_dict(),"quant.pth")

If retraining is not needed, you can perform quantization only in non-training mode. To enable non-training mode, call the **set\_calibrate\_state** API.

from dopt.dopt\_torch.opt\_main import set\_calibrate\_state 
calibrate\_mode = True
set\_calibrate\_state(quant\_model, calibrate\_mode)

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

quant\_model

 | 

Yes

 | 

Quantized PyTorch model.

 |
| 

calibration\_mode

 | 

Yes

 | 

Boolean variable, indicating whether to enable the non-training (calibration) mode.

-   **True**: Enable the non-training (calibration) mode.
-   **False**: Disable the non-training (calibration) mode.

 |

After setting the non-training mode, use the quantized model (**quant\_model**) to perform forward inference on the calibration set. Then you will be able to start non-training quantization.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cb/v3/5oy3h2z4RqGTxyDrFT0j7g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8898611250BC880D872498C4710FE3239D05D36BEEC9CDF2A3E2A455717DC24D)

-   When calling **optimize\_model**, make sure that the input model is not encapsulated by distributed APIs such as **torch.nn.parallel.DistributedDataParallel**, and that the optimizer is used to optimize the **quant\_model** instead of the original floating-point model.
-   The quantization loss is optional. You need to adjust **quant\_loss** based on the actual quantization loss and the original loss, by virtue of hyperparameter tuning. Generally, the proportion between the quantization loss function and the original loss function is 1:20. You can reduce the proportion of the quantization loss, in case of great impact on the optimization.

## Generating a Quantized Model

Add the path of the **dopt\_pytorch\_py3** file in the decompressed DDK to the Python environment variable.

import sys
sys.path.append(".../dopt\_pytorch\_py3") ## The path should be an absolute path.

from dopt.dopt\_torch.opt\_main import generate\_final\_model

After the training is complete, use the corresponding API to generate the final model.

generate\_final\_model(
    model,              ## Floating-point model.
    config\_file,         ## JSON file for quantization configuration.
    pth\_file = "quant.pth",    ## Quantized .pth file.
    output\_dir = "./"   ## Folder for storing the generated quantization parameters and the PyTorch model.
)

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

model

 | 

Yes

 | 

Floating-point model.

 |
| 

config\_file

 | 

Yes

 | 

Path of the JSON configuration file, which should be the same as **config\_path** set when you call the **optimize\_model** API.

 |
| 

pth\_file

 | 

Yes

 | 

Weight file for quantization and training.

 |
| 

output\_dir

 | 

Yes

 | 

Path for storing the PyTorch model and quantization parameters. Make sure that you set a valid path. If this parameter is not set, the model will be saved in the current path by default.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/9SmZkOV6QoGRPAZ6QdPdTA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AD5E8B767DAFE79A48E1435444003937886F037792C510E235042EE93A250BD2)

-   The input model for calling the **generate\_final\_model** function must be a rebuilt floating-point model.
-   The generated PyTorch model does not contain quantization parameters, but some graph fusion and fake-quantization processing are performed.
