# NAS Training

To conduct NAS training, perform the following steps:

1.  Prepare the environment ([Preparing the Environment](#section193737375169)).
2.  Prepare a dataset ([Preparing the Dataset](#section1766391819183)).
3.  Configure search parameters ([Configuring Search Parameters](#section9753193220185)).
4.  Configure custom APIs ([Custom TensorFlow API](#section183452511917) and [Custom PyTorch API](#section56271946125514)).
5.  Search for and train network architectures ([Search and Training](#section05357228205)).

#### Environment Setup

## Linux Environment

1.  Configure the dependencies for the NASEA strategy's running environment:
    
    tensorflow-gpu==2.8
    ruamel.yaml==0.17.28
    PyYAML==5.4.1
    Cython==0.29.35
    pymoo==0.3.2
    pathlib
    mpi4py==3.1.4
    sklearn
    opencv-python
    matplotlib
    numpy==1.23.5
    tqdm==4.43.0
    protobuf==3.20.3
    requests==2.31.0
    Pillow==7.1.2
    
    Use pip or Conda to install the preceding dependencies.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/132f-K7oQU-siQMAprFC8Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=1CD2582CD53F90350E7B0D21FD2DF5EA2173EC42C93B073AB44B3C392402574D)
    
    If you only need to run the tool on a single server with a single graphics card, skip the following steps. To run the tool on a single server with multiple graphics cards, continue the following steps.
    
2.  Install and configure [Horovod](https://github.com/horovod/horovod#instal) and Open MPI.
3.  Install mpi4py.
    
    pip3 install mpi4py
    
4.  Verify the installation.
    
    Download the official [Demo](https://github.com/horovod/horovod/blob/master/examples/tensorflow/tensorflow_mnist.py) of [Horovod](https://github.com/horovod/horovod/blob/master/examples/tensorflow/tensorflow_mnist.py) to the current directory. Run the following command on a server using four accelerator cards:
    
    horovodrun -np 4 -H localhost:4 python3 tensorflow\_mnist.py
    
    If the training can be performed properly, the Horovod environment is successfully deployed.
    

#### Preparing the Dataset

Prepare a dataset or proxy dataset as required.

1.  Define the dataset function in **user\_module.py** and use the function to receive the dataset path passed from **scen.yaml**.
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/31/v3/6cG9yJ7UQe2WXDrhqkn5Pw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=AA2B8A3AC52C675D4E3B38DE749ED6025B8CA824E9276E2A39C10F7C95DCB837)
    
    The function name is **build\_dataset\_search** in TensorFlow and **dataset\_define** in PyTorch.
    
2.  Parse the dataset to read images and tags. Determine the training or evaluation mode based on **is\_training**.
    
    -   In training mode, the **train\_dir** directory set in **scen.yaml** is passed to **dataset\_dir**.
    -   In evaluation mode, the **val\_dir** directory set in **scen.yaml** is passed to **dataset\_dir**.
    
3.  Parse the corresponding data and return the processed data. For details about the API definition, see [Custom TensorFlow API](#section183452511917) and [Custom PyTorch API](#section56271946125514).

#### Configuring Search Parameters

Set proper search parameters to achieve optimal search results. Complete the configuration file (by referring to **tools\_dopt/dopt\_tf\_py3/demo/nas\_ea/ea\_cls\_imagenet/scen.yaml**). The following is an example:

_\## Network architecture search scenario_
scenario:
  strategy:
    name:                NASEA
    framework:           Tensorflow
    batch\_size:          128
    epochs:              60
    constraint:
      application\_type:  "image\_classification"
      constraint\_type:   "size"
      constraint\_value:  11000000
    supernet:
      input\_shape:       (224, 224, 3) 
      data\_format:       "channels\_last" 
      filters:           \[64, 64, 128, 128, 256, 256\] 
      strides:           \[1, 1, 2, 1, 2, 1\] 
      feature\_choose:    \[4, 5\]
    optimizer:
      weights\_optimizer:
        type:            "Adam"
        betas:           \[0.9, 0.999\]
        learning\_rate:   0.0001
    dataset:
      pre\_train\_dir:   "/tmp/tfrecords"
      train\_dir:        "/tmp/ImageNet\_tf/"
      val\_dir:          "/tmp/ImageNet\_tf/"
    searcher:
      generation\_num:    100
      pop\_size:          40
    resource:
      name:              Tensorflow\_standalone
      gpu\_id:            0,1,2,3,4,5,6,7

The following table describes the parameters.

| 
Parameter

 | 

Type

 | 

Value Range

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- | :-- | :-- |
| 

**scenario.strategy**

 |
| 

name

 | 

string

 | 

NASEA

 | 

Yes

 | 

Strategy name.

 |
| 

framework

 | 

string

 | 

TensorFlow and PyTorch

 | 

Yes

 | 

Training framework.

 |
| 

batch\_size

 | 

int

 | 

\-

 | 

Yes

 | 

**batch\_size** of the dataset.

 |
| 

epochs

 | 

int

 | 

\-

 | 

Yes

 | 

Dataset epochs.

 |
| 

**scenario.strategy.supernet**

 |
| 

input\_shape

 | 

tuple

 | 

\-

 | 

No

 | 

Shape (C,H,W) or (H,W,C) of the model input, which is set to **(224,224,3)** by default.

 |
| 

data\_format

 | 

string

 | 

channels\_first/channels\_last

 | 

No

 | 

Data format. The values of **input\_shape** and **data\_format** must match. Example: **channels\_last**. In the PyTorch version, this parameter supports only the **channels\_first** option.

 |
| 

filters

 | 

list

 | 

\-

 | 

No

 | 

Cout of each layer of the search skeleton. It is a list corresponding to strides in format \[cout, ..., cout\]. Example: \[64, 64, 128, 128, 256, 256\]

 |
| 

strides

 | 

list

 | 

\-

 | 

No

 | 

Stride used by each layer of the search skeleton. Example: \[1, 1, 2, 1, 2, 1\]

 |
| 

feature\_choose

 | 

list

 | 

\-

 | 

No

 | 

Layers to be merged, which are separated by commas (,). The value starts from **0**. For example, to merge the layer 4 and layer 6, input **\[3, 5\]**.

Currently, this parameter applies only to the detection scenario of the TensorFlow version and the segmentation scenario of the PyTorch version.

 |
| 

**scenario.strategy.constraint**

 |
| 

application\_type

 | 

string

 | 

image\_classification/object\_detection/ semantic\_segmentation

 | 

Yes

 | 

App type: classification, detection, or segmentation.

 |
| 

constraint\_type

 | 

string

 | 

size/flops/latency

 | 

Yes

 | 

Model constraint type. Currently, **latency** applies only to the classification scenario of the TensorFlow version.

 |
| 

constraint\_value

 | 

int, float

 | 

\-

 | 

Yes

 | 

Model constraint value, that is, the size of the entire network.

 |
| 

processor\_version

 | 

string

 | 

npu\_v1

 | 

No

 | 

Currently, this parameter is supported only when the model constraint type is **latency**.

 |
| 

**scenario.strategy.optimizer**

 |
| 

**scenario.strategy.optimizer.weights\_optimizer**

 |
| 

type

 | 

string

 | 

SGD/Momentum/Adam

 | 

No

 | 

Optimizer\[1\]. The value defaults to **Adam** for classification and detection, and defaults to **Momentum** for segmentation. In the PyTorch version, only the SGD and Adam optimizers are supported. Adam is by default used for classification and segmentation.

 |
| 

betas

 | 

list

 | 

(0, 1)

 | 

No

 | 

Attenuation factor, a parameter of optimizer Adam. The default value is **\[0.9, 0.999\]**.

 |
| 

learning\_rate

 | 

float

 | 

(0, 1)

 | 

No

 | 

Learning rate. If multiple GPUs are used, the value will automatically increase by times based on the GPU count. The value defaults to **0.0001** for classification and detection, and defaults to **0.00001** for segmentation.

 |
| 

momentum

 | 

float

 | 

(0, 1)

 | 

No

 | 

Momentum, a parameter of optimizer Momentum. The value defaults to **0.9**. This parameter applies to the TensorFlow version only.

 |
| 

**scenario.strategy.dataset**

 |
| 

pre\_train\_dir

 | 

string

 | 

\-

 | 

Yes

 | 

Path of the dataset for pre-training or path of CKPT generated by pre-training (see Note \[2\]). This parameter is **mandatory** for detection and segmentation and is not required for classification.

 |
| 

train\_dir

 | 

string

 | 

\-

 | 

Yes

 | 

Path of the training dataset.

 |
| 

val\_dir

 | 

string

 | 

\-

 | 

Yes

 | 

Path of the validation dataset

 |
| 

**scenario.strategy.searcher**

 |
| 

generation\_num

 | 

int

 | 

\-

 | 

No

 | 

Algebra of the evolutionary algorithm. Example: **100**

 |
| 

pop\_size

 | 

int

 | 

\-

 | 

No

 | 

Number of populations in the evolutionary algorithm. The value defaults to **40**.

 |
| 

**scenario.resource**

 |
| 

name

 | 

string

 | 

Tensorflow\_standalone/ pytorch\_standalone

 | 

Yes

 | 

Name of the resource object.

 |
| 

gpu\_id

 | 

string

 | 

\-

 | 

Yes

 | 

GPU ID.

-   If only one GPU ID (such as 0) is entered, training will be performed on a single server with a single graphics card.
-   If multiple GPU IDs (such as 0, 1, 2, and 3) are entered, training will be performed on a single server with multiple graphics cards.

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9c/v3/YnD_4086R129dT-N8FA1Zw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=48E5E28B52DE568B8BF3C1511D22502DC8B06449BA403A2D2F13A3B4A989A8FB)

\[1\] Optimizers SGD, Momentum, and Adam are supported.

-   Optimizer SGD supports the **learning\_rate** parameter.
-   Optimizer Momentum supports the **momentum** and **learning\_rate** parameters. The PyTorch version does not support the optimizer.
-   Optimizer Adam supports the **betas** and **learning\_rate** parameters. **betas** is a list. Elements in this list are numbered from 0. For example, the element with index 0 is **beta1**, and the element with index 1 is **beta2**.

\[2\] If there is no CKPT file, the value indicates the path of the dataset for pre-training. If there is a CKPT file, the value indicates the path of the CKPT file.

#### Custom TensorFlow API

NAS performs training based on the TensorFlow framework. You need to configure the model training file based on the following API definitions.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/n9Cqv5JuQqy0NtqAI1xJGQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=223C5C3BE13932855BAE12614439B9EFDB359A6B475464BF80A754013E08C5EF)

Only **tf.keras** is supported.

## UserModule Class

<table><tbody><tr><th class="firstcol" id="mcps1.3.12.2.1.3.1.1" valign="top" width="26.26%"><p><strong>Class Description</strong></p></th><td class="cellrowborder" valign="top" width="73.74000000000001%"><p>class <strong>UserModule</strong>: Defines the developer-side APIs.</p></td></tr><tr><th class="firstcol" id="mcps1.3.12.2.1.3.2.1" valign="top" width="26.26%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="73.74000000000001%"><p>Constructor.</p></td></tr><tr><th class="firstcol" id="mcps1.3.12.2.1.3.3.1" valign="top" width="26.26%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="73.74000000000001%"><p>def <strong>__init__</strong>(self, epoch, batch_size)</p></td></tr></tbody></table>

This class defines the following functions in the search process:

-   Dataset reading
    
    <table><tbody><tr><th class="firstcol" id="mcps1.3.13.1.1.1.3.1.1" valign="top" width="28.96%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="71.04%"><p>Dataset reading function.</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.1.1.1.3.2.1" valign="top" width="28.96%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="71.04%"><p>In the classification scenario:</p><p>def <strong>build_dataset_search</strong>(self, dataset_dir, is_training)</p><p>In detection and segmentation scenarios:</p><p>def <strong>build_dataset_search</strong>(self, dataset_dir, is_training, is_shuffle)</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.1.1.1.3.3.1" valign="top" width="28.96%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="71.04%"><p><strong>dataset_dir</strong>: Dataset path. If <strong>is_training</strong> is set to <strong>True</strong>, <strong>train_dir</strong> configured in <strong>scen.yaml</strong> is passed. Otherwise, <strong>val_dir</strong> configured in <strong>scen.yaml</strong> is passed.</p><p><strong>is_training</strong>: <strong>True</strong> indicates training, while <strong>False</strong> indicates inference.</p><p><strong>is_shuffle</strong>: Whether the dataset needs to be shuffled. Note: When bn is updated in the evaluation phase, the dataset does not need to be shuffled.</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.1.1.1.3.4.1" valign="top" width="28.96%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="71.04%"><ul><li>For training:<p>In classification and segmentation scenarios:</p><p><strong>dataset</strong>: TensorFlow dataset.</p><p><strong>data_num</strong>: Number of images in the dataset.</p><p>In the detection scenario:</p><p><strong>train_generator</strong>: Training set generator.</p><p><strong>train_dataset_size</strong>: Number of training sets.</p></li></ul><ul><li>For inference:<p>In classification and segmentation scenarios:</p><p><strong>dataset</strong>: TensorFlow dataset.</p><p><strong>data_num</strong>: Number of images in the dataset.</p><p>In the detection scenario:</p><p><strong>val_generator</strong>: Validation set generator.</p><p><strong>val_dataset</strong>: Dataset after JSON file parsing.</p><p><strong>val_dataset_size</strong>: Number of validation sets.</p></li></ul></td></tr></tbody></table>
    
-   Learning rate update strategy
    
    <table><tbody><tr><th class="firstcol" id="mcps1.3.13.2.1.1.3.1.1" valign="top" width="28.63%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>Learning rate update strategy function.</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.2.1.1.3.2.1" valign="top" width="28.63%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>def <strong>lr_scheduler</strong>(self, lr_init, global_step)</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.2.1.1.3.3.1" valign="top" width="28.63%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p><strong>lr_init</strong>: Initial value of the learning rate.</p><p><strong>global_step</strong>: TensorFlow global step.</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.2.1.1.3.4.1" valign="top" width="28.63%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>Updated learning rate.</p></td></tr></tbody></table>
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/BI_-TOWlRWyiNRAugc_H4Q/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E931FDA2D45AA1DF86491C8A4C68CEE6A1E3029ABDE46414826328B182F9829A)
    
    You are advised to set the initial learning rate to a constant.
    
-   Evaluation function
    
    <table><tbody><tr><th class="firstcol" id="mcps1.3.13.3.1.1.3.1.1" valign="top" width="28.63%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>Evaluation function.</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.3.1.1.3.2.1" valign="top" width="28.63%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>def <strong>metrics_op</strong>(self, inputs, outputs)</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.3.1.1.3.3.1" valign="top" width="28.63%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><ul><li>In classification and segmentation scenarios:<p><strong>inputs</strong>: Ground truth label.</p><p><strong>outputs</strong>: Result of forward inference.</p></li></ul><ul><li>In the detection scenario:<p>inputs: [valid_dir, model]</p><p><strong>valid_dir</strong>: Path of the validation set.</p><p><strong>model</strong>: Network model.</p><p><strong>outputs</strong>: [data_generator, proxy_val_image_ids, data_size]</p><p><strong>data_generator</strong>: Dataset generator.</p><p><strong>proxy_val_image_ids</strong>: Image index of the proxy validation set, which is used to select a subset from the validation set to accelerate the evaluation process.</p><p><strong>data_size</strong>: Size of the dataset.</p></li></ul></td></tr><tr><th class="firstcol" id="mcps1.3.13.3.1.1.3.4.1" valign="top" width="28.63%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>Evaluation result.</p></td></tr></tbody></table>
    
-   Loss calculation function
    
    <table><tbody><tr><th class="firstcol" id="mcps1.3.13.4.1.1.3.1.1" valign="top" width="28.63%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>Loss calculation function.</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.4.1.1.3.2.1" valign="top" width="28.63%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>def <strong>loss_op</strong>(self, labels, logits)</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.4.1.1.3.3.1" valign="top" width="28.63%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p><strong>labels</strong>: Ground truth label.</p><p><strong>logits</strong>: Result of forward inference.</p></td></tr><tr><th class="firstcol" id="mcps1.3.13.4.1.1.3.4.1" valign="top" width="28.63%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="71.37%"><p>Loss value, which is a tensor.</p></td></tr></tbody></table>
    

## PreNet Class

The input layer of the model does not require searching. Therefore, it is defined through a fixed network architecture.

<table><tbody><tr><th class="firstcol" id="mcps1.3.15.1.3.1.1" valign="top" width="29.15%"><p><strong>Class Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>Class <strong>PreNet</strong>: Model input layer.</p></td></tr><tr><th class="firstcol" id="mcps1.3.15.1.3.2.1" valign="top" width="29.15%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>PreNet constructor.</p></td></tr><tr><th class="firstcol" id="mcps1.3.15.1.3.3.1" valign="top" width="29.15%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>def <strong>__init__</strong>(self)</p></td></tr><tr><th class="firstcol" id="mcps1.3.15.1.3.4.1" valign="top" width="29.15%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>N/A</p></td></tr><tr><th class="firstcol" id="mcps1.3.15.1.3.5.1" valign="top" width="29.15%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>N/A</p></td></tr><tr><th class="firstcol" id="mcps1.3.15.1.3.6.1" valign="top" width="29.15%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>Builds the model's input architecture.</p></td></tr><tr><th class="firstcol" id="mcps1.3.15.1.3.7.1" valign="top" width="29.15%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>def <strong>call</strong>(self, inputs, training=True)</p></td></tr><tr><th class="firstcol" id="mcps1.3.15.1.3.8.1" valign="top" width="29.15%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p><strong>inputs</strong>: Input data.</p><p><strong>training</strong>: <strong>True</strong> indicates training, while <strong>False</strong> indicates inference.</p></td></tr><tr><th class="firstcol" id="mcps1.3.15.1.3.9.1" valign="top" width="29.15%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>Input of the search skeleton, which is a tensor.</p></td></tr></tbody></table>

## PostNet Class

The output layer of the model does not require searching. Therefore, it is defined through a fixed network architecture.

<table><tbody><tr><th class="firstcol" id="mcps1.3.17.1.3.1.1" valign="top" width="29.15%"><p><strong>Class Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>Class <strong>PostNet</strong>: Model output layer.</p></td></tr><tr><th class="firstcol" id="mcps1.3.17.1.3.2.1" valign="top" width="29.15%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>PostNet constructor.</p></td></tr><tr><th class="firstcol" id="mcps1.3.17.1.3.3.1" valign="top" width="29.15%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>def <strong>__init__</strong>(self)</p></td></tr><tr><th class="firstcol" id="mcps1.3.17.1.3.4.1" valign="top" width="29.15%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>N/A</p></td></tr><tr><th class="firstcol" id="mcps1.3.17.1.3.5.1" valign="top" width="29.15%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>N/A</p></td></tr><tr><th class="firstcol" id="mcps1.3.17.1.3.6.1" valign="top" width="29.15%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>Builds the model's output architecture.</p></td></tr><tr><th class="firstcol" id="mcps1.3.17.1.3.7.1" valign="top" width="29.15%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>def<strong> call</strong>(self, inputs, training=True)</p></td></tr><tr><th class="firstcol" id="mcps1.3.17.1.3.8.1" valign="top" width="29.15%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p><strong>inputs</strong>: Output of the search skeleton.</p><p><strong>training</strong>: <strong>True</strong> indicates training, while <strong>False</strong> indicates inference.</p></td></tr><tr><th class="firstcol" id="mcps1.3.17.1.3.9.1" valign="top" width="29.15%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.85000000000001%"><p>Model output, which is a tensor.</p></td></tr></tbody></table>

#### Custom PyTorch API

NAS performs training based on the PyTorch framework. You need to configure the model training file based on the following API definitions.

## UserModule Class

<table><caption><b>Table 1 </b>UserModule class</caption><tbody><tr><th class="firstcol" id="mcps1.3.19.2.2.3.1.1" valign="top" width="29.5%"><p><strong>Class Description</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>class <strong>UserModule</strong>: Defines the developer-side APIs.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.2.2.3.2.1" valign="top" width="29.5%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>Constructor.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.2.2.3.3.1" valign="top" width="29.5%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>def <strong>__init__</strong>(self, epoch, batch_size)</p></td></tr></tbody></table>

This class defines the following functions in the search process:

<table><caption><b>Table 2 </b>Dataset reading</caption><tbody><tr><th class="firstcol" id="mcps1.3.19.4.2.3.1.1" valign="top" width="29.59%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.41%"><p>Dataset reading function.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.4.2.3.2.1" valign="top" width="29.59%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.41%"><p>def <strong>dataset_define</strong>(self, dataset_dir, is_training)</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.4.2.3.3.1" valign="top" width="29.59%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.41%"><p><strong>dataset_dir</strong>: Dataset directory. If <strong>is_training</strong> is set to <strong>True</strong>, <strong>train_dir</strong> configured in <strong>scen.yaml</strong> is passed. Otherwise, <strong>val_dir</strong> configured in <strong>scen.yaml</strong> is passed.</p><p><strong>is_training</strong>: <strong>True</strong> indicates training, while <strong>False</strong> indicates inference.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.4.2.3.4.1" valign="top" width="29.59%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.41%"><p><strong>torch.utils.data.Dataset</strong> instance of PyTorch.</p></td></tr></tbody></table>

<table><caption><b>Table 3 </b>Learning rate update strategy</caption><tbody><tr><th class="firstcol" id="mcps1.3.19.5.2.3.1.1" valign="top" width="29.849999999999998%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.15%"><p>Learning rate update strategy function.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.5.2.3.2.1" valign="top" width="29.849999999999998%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.15%"><p>def <strong>scheduler_define</strong>(self, optimizer, steps_per_epoch)</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.5.2.3.3.1" valign="top" width="29.849999999999998%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.15%"><p><strong>optimizer</strong>: Optimizer instance.</p><p><strong>steps_per_epoch</strong>: Step of each epoch during training.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.5.2.3.4.1" valign="top" width="29.849999999999998%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.15%"><p><strong>lr_scheduler</strong> instance of PyTorch.</p></td></tr></tbody></table>

<table><caption><b>Table 4 </b>Evaluation function</caption><tbody><tr><th class="firstcol" id="mcps1.3.19.6.2.3.1.1" valign="top" width="29.849999999999998%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.15%"><p>Evaluation function.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.6.2.3.2.1" valign="top" width="29.849999999999998%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.15%"><p>def <strong>metrics_func</strong>(self, eval_dataloader, eval_function)</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.6.2.3.3.1" valign="top" width="29.849999999999998%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.15%"><ul><li><strong>eval_dataloader</strong>: <strong>Dataloader</strong> object of PyTorch, which is used to load the validation dataset.</li><li><strong>eval_function</strong>: Forward inference function. The corresponding inference result can be obtained by inputting the data loaded in <strong>eval_dataloader</strong> to this function.</li></ul></td></tr><tr><th class="firstcol" id="mcps1.3.19.6.2.3.4.1" valign="top" width="29.849999999999998%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.15%"><p>Evaluation result.</p></td></tr></tbody></table>

<table><caption><b>Table 5 </b>Loss calculation function</caption><tbody><tr><th class="firstcol" id="mcps1.3.19.7.2.3.1.1" valign="top" width="29.59%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.41%"><p>Loss calculation function.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.7.2.3.2.1" valign="top" width="29.59%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.41%"><p>def <strong>loss_func</strong>(self, labels, logits)</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.7.2.3.3.1" valign="top" width="29.59%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.41%"><p><strong>labels</strong>: Real label of data.</p><p><strong>logits</strong>: Result of forward inference.</p></td></tr><tr><th class="firstcol" id="mcps1.3.19.7.2.3.4.1" valign="top" width="29.59%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.41%"><p>Loss value.</p></td></tr></tbody></table>

## PreNet Class

The input layer of the model does not require searching. Therefore, it is defined through a fixed network architecture.

<table><tbody><tr><th class="firstcol" id="mcps1.3.21.1.3.1.1" valign="top" width="29.409999999999997%"><p><strong>Class Description</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p>Class <strong>PreNet</strong>: Model input layer.</p></td></tr><tr><th class="firstcol" id="mcps1.3.21.1.3.2.1" valign="top" width="29.409999999999997%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p>PreNet constructor.</p></td></tr><tr><th class="firstcol" id="mcps1.3.21.1.3.3.1" valign="top" width="29.409999999999997%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p>def <strong>__init__</strong>(self)</p></td></tr><tr><th class="firstcol" id="mcps1.3.21.1.3.4.1" valign="top" width="29.409999999999997%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.21.1.3.5.1" valign="top" width="29.409999999999997%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.21.1.3.6.1" valign="top" width="29.409999999999997%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p>Builds the model's input architecture.</p></td></tr><tr><th class="firstcol" id="mcps1.3.21.1.3.7.1" valign="top" width="29.409999999999997%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p>def <strong>forward</strong>(self, inputs)</p></td></tr><tr><th class="firstcol" id="mcps1.3.21.1.3.8.1" valign="top" width="29.409999999999997%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p><strong>inputs</strong>: Input data.</p></td></tr><tr><th class="firstcol" id="mcps1.3.21.1.3.9.1" valign="top" width="29.409999999999997%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.59%"><p>Input of the search skeleton, which is a tensor.</p></td></tr></tbody></table>

## PostNet Class

The output layer of the model does not require searching. Therefore, it is defined through a fixed network architecture.

<table><tbody><tr><th class="firstcol" id="mcps1.3.23.1.3.1.1" valign="top" width="29.5%"><p><strong>Class Description</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>Class <strong>PostNet</strong>: Model output layer.</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.1.3.2.1" valign="top" width="29.5%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>PostNet constructor.</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.1.3.3.1" valign="top" width="29.5%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>def <strong>__init__</strong>(self)</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.1.3.4.1" valign="top" width="29.5%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.1.3.5.1" valign="top" width="29.5%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>NA</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.1.3.6.1" valign="top" width="29.5%"><p><strong>Function Description</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>Builds the model's output architecture.</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.1.3.7.1" valign="top" width="29.5%"><p><strong>API Definition</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>def<strong> forward</strong>(self, inputs)</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.1.3.8.1" valign="top" width="29.5%"><p><strong>Parameter Description</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p><strong>inputs</strong>: Output of the search skeleton. If <strong>feature_choose</strong> is not configured in <strong>scen.yaml</strong>, <strong>inputs</strong> is a tensor. If <strong>feature_choose</strong> is configured in <strong>scen.yaml</strong>, <strong>inputs</strong> is a list, and the content of <strong>inputs</strong> is the output of the corresponding layer configured in <strong>feature_choose</strong> and the output of the last layer of the search framework.</p></td></tr><tr><th class="firstcol" id="mcps1.3.23.1.3.9.1" valign="top" width="29.5%"><p><strong>Returns</strong></p></th><td class="cellrowborder" valign="top" width="70.5%"><p>Model output, which is a tensor.</p></td></tr></tbody></table>

#### Search and Training

This tool is introduced in three aspects: training entry, maintenance and debugging mode, and search result display.

## Training Entry

For TensorFlow, run **python3 tools\_dopt/dopt\_tf\_py3/dopt\_so.py -c scen.yaml** to enable search training. For PyTorch, run **python3 tools\_dopt/dopt\_pytorch\_py3/dopt\_so.py -c scen.yaml**. The corresponding demo directory is provided for each scenario. For details, see [TensorFlow NASEA NAS Demo](../model-size-reduction-example/document.md#section1897718597348).

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/40/v3/_NiHeq7lRDa0ETFXsCPHZA/notice_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=74E78C76DBA67E242A5FE409BE3A3F49A63CC8D30F4F9382F8E3B7CFF6C3385C)

When you run the preceding command, the tool searches for the **user\_module.py** file in the current directory.

## Maintenance and Debugging Mode

During the search and training, you can observe the process information using [TensorBoard](https://www.tensorflow.org/tensorboard). The generated files are stored in the **log\_\*** directory.

-   Model Precision Loss Curve (loss)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/XGT0DDSvSvqdnebuO-ZqrA/en-us_image_0000002496888544.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BB6067DC4223C370C5BAF1C4BBBAFDC64CEEA47894E96C2042A4285EEF2C961C "Click to enlarge")
    
-   Learning Rate Curve (lr)
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7f/v3/azB2gW6bS72YAKP5HswPKg/en-us_image_0000002528648509.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A66944808A40BB9CA312FEF4146B982D5753DD77FB5D2FAE97EC79721C39C2C1 "Click to enlarge")
    
-   Pareto Front Image
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/W2A64qOfRailcQycJQg9nQ/en-us_image_0000002528648511.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82170CFFB599CD1E6C451DD90855A83E27C205025636B361B680DF63B460D73E "Click to enlarge")
    

In the Pareto diagram, the horizontal coordinate indicates the model size or computation workload (a constraint type), and the vertical coordinate indicates the precision after architecture search. The precision in the image is an estimated value in the search process. You are advised to train the search architecture for a higher precision.

Search architectures are different in terms of precision and parameter/computation workload/latency. You can select a proper model as needed.

## Search Result Display

After the search is complete, the tool automatically saves the model architecture in the Pareto diagram to the **results** directory and generates multiple **model\_arch\_result\__$NUM_.py** files. The file index **$NUM** is consistent with that in the Pareto diagram. You can select a proper network architecture based on the **model\_param\_size** and **accuracy** parameters or the Pareto diagram in TensorBoard. The following figure shows the TensorFlow search results (for PyTorch, only the implementation framework is different):

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/84/v3/8jDUbowZQvuJ_sSR1-m7ig/en-us_image_0000002528408533.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=BD8B7FAC58B24016DA8A68E2258D5C7302D522412EC1EB88B37ACA5FD22279AB "Click to enlarge")

Copy the selected model architecture file to the upper-level directory of **results**, and run the following command to execute the file.

python3 model\_arch\_result\_$NUM.py

After the execution, a .pb file and a TensorBoard log file of the model are generated in the current directory. You can view the graph of the model using TensorBoard as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/26/v3/rIkH4kbAQ-iZ6tgW_Ao0Yw/en-us_image_0000002496888542.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6DC593A398C98F1C5EA8B5D26AB2A1C5BDD2A2822AB0975F9662684ECC0D2A2A "Click to enlarge")
