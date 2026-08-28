# Non-training Quantization

#### Preparing the Input

## Preparing a Model

-   TensorFlow Developers
    
    Provide the PB model to be quantized.
    
-   PyTorch Developers
    
    Provide the .py model definition file and the .pth model parameter file for the model to be quantized.
    
-   ONNX Developers
    
    Provide the ONNX model to be quantized.
    

## Preparing the Calibration Set

You need to provide the calibration set in the .bin or image format. Input data in .bin format must be stored using the methods described in Table 1. The image data is stored in the folder for storing test images. By default, the input data in image format is read from the BGR channels. The read data format is NCHW, where N indicates the number of provided images.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/eb/v3/hvY7uHLPT2ic0srHDGZloQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=D660E88D0FF605AE031B1DAA2FF2B8FE30571AEA74ACB0136729D2C73FB37F60)

The size reduction tool supports the following image formats: ".bmp", ".dib", ".jpeg", ".jpg", ".jpe", ".png", ".webp", ".pbm", ".pgm", ".ppm", ".tiff", ".tif", ".BMP", ".DIB", ".JPEG", ".JPG", ".JPE", ".PNG", ".WEBP", ".PBM", ".PGM", ".PPM", ".TIFF", and ".TIF".

The input data in .bin format supports two definition modes. One applies to any dimension except 4-dimensional, while the other is tailored for 4-dimensional data. We recommend that you use the arbitrary-dimension definition whenever possible.

For input data of any dimension (excluding 4-dimensional), the .bin file needs to be defined as follows. For example, for 3-dimensional data (50, 100, 300), the resulting data shape after reading is (50, 100, 300).

**Table 1** Binary calibration set for any dimension (excluding 4-dimensional)
| 
**File Header/Data**

 | 

**Address Offset**

 | 

**Type**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

File header (20 bytes in total)

 | 

0000

 | 

32bit int

 | 

610

 | 

Magic number

Verifies the validity of the file when magic number is **610**.

 |
| 

0004

 | 

32bit int

 | 

3

 | 

Input data rank

 |
| 

0008

 | 

32bit int

 | 

50

 | 

Input dimension 1

 |
| 

0012

 | 

32bit int

 | 

100

 | 

Input dimension 2

 |
| 

0016

 | 

32bit int

 | 

300

 | 

Input dimension 3

 |
| 

Data

 | 

...

 | 

Float32

 | 

...

 | 

Data volume = 50 x 100 x 300

 |

The .bin file for 4-dimensional input data can be defined according to Table 1 or Table 2. For example, for 4-dimensional data (50, 3, 28, 28), the resulting data shape after reading is (50, 3, 28, 28).

**Table 2** Four-dimensional binary calibration set
| 
**File Header/Data**

 | 

**Address Offset**

 | 

**Type**

 | 

**Value**

 | 

**Description**

 |
| :-- | :-- | :-- | :-- | :-- |
| 

File header (20 bytes in total)

 | 

0000

 | 

32bit int

 | 

510

 | 

Magic number

Verifies the validity of the file when magic number is **510**.

 |
| 

0004

 | 

32bit int

 | 

50

 | 

Input num

 |
| 

0008

 | 

32bit int

 | 

3

 | 

Input channels

 |
| 

0012

 | 

32bit int

 | 

28

 | 

Input height

 |
| 

0016

 | 

32bit int

 | 

28

 | 

Input width

 |
| 

Data

 | 

...

 | 

Float32

 | 

...

 | 

Data volume = 50 x 3 x 28 x 28

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/69/v3/jwHLTVXkRF2hnTXyNRgMOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=7F4FCD883C6B544B7B63418277F8AD3916A295C946AEF4C46EB1D40AA655A04C)

The size reduction tool provides a script to support the conversion of .bin files. For details, see **tools\_dopt/dopt\_tf\_py3/demo/quant8-8/notrain/bin\_data\_preprocessing.py** in [Downloading Tools](../../../getting-started/document.md#section152959341125).

## Editing the config.prototxt File

The following table describes the parameters in **config.prototxt**. In BINARY mode, no pre-processing is performed. In IMAGE mode, pre-processing is performed based on the mean value and variance you have provided.

| 
Parameter

 | 

Description

 | 

Mandatory

 |
| :-- | :-- | :-- |
| 

strategy

 | 

Optimization strategy. Currently, only Quant\_INT8-8 is supported for all frameworks.

 | 

No (default to Quant\_INT8-8)

 |
| 

device

 | 

Whether to use the GPU or CPU for quantization.

-   **USE\_GPU**: GPU mode
-   **USE\_CPU**: CPU mode

 | 

No (default to CPU mode)

 |
| 

exclude\_op

 | 

Quantization operator blocklist. Operators in the blocklist will not be quantized.

You can configure the blocklist using either of the following methods or a combination of the two methods:

-   Uses one **exclude\_op**, which contains multiple **op\_name**, separated by semicolons (;).
-   Uses multiple **exclude\_op**, each of which contains an **op\_name**.

If an **op\_name** does not exist in the model, an error is reported.

NOTE:

The value of **exclude\_op** in ONNX should be the weight name.

 | 

No

 |
| 

preprocess\_parameter

 | 

Path of the calibration data configuration file.

 | 

Yes

 |

The following table describes the sub-parameters of **preprocess\_parameter**. If a model has multiple inputs, **preprocess\_parameter** must be configured for each input.

| 
Parameter

 | 

Description

 | 

Mandatory

 |
| :-- | :-- | :-- |
| 

input\_type

 | 

Whether to use the binary file input or image format input.

-   **BINARY**: binary input
-   **IMAGE**: image input

 | 

No (default to **IMAGE**)

 |
| 

image\_format

 | 

Image format. This parameter is valid only in **IMAGE** mode.

-   **BGR**: BGR image input
-   **RGB**: RGB image input

 | 

No (default to **BGR**)

 |
| 

mean\_value

 | 

Average value parameter for image pre-processing. This parameter takes effect only in **IMAGE** mode.

The value is of the float type and ranges from 0.0 to 255.0.

The number of **mean\_value** must be the same as dimension C of the input.

 | 

No (dimension C of the input is **0.0** by default)

 |
| 

standard\_deviation

 | 

Standard deviation parameter for image pre-processing. This parameter takes effect only in **IMAGE** mode.

The value is of the float type and must be greater than or equal to **0.0**.

 | 

No (default to **0.0**)

 |
| 

input\_file\_path

 | 

Absolute path of the input calibration set, that is, the path of the .bin file, or the folder that stores images.

Example: **/path/to/user/data**.

 | 

Yes

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/ea/v3/neTBgFQrRX690gS47d6x2g/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E9258E49F86614182811987089FE16F7A357DA29F5EEE1C447A5B38FA8C894F2)

-   In **IMAGE** input mode, the toolchain processes images as follows: image = (image - mean\_value) / standard\_deviation
-   In **BINARY** mode, the toolchain does not process the input data. That is, the **image\_format**, **mean\_value**, and **standard\_deviation** parameters are invalid.

The following is a configuration example:

-   BINARY input mode
    
    strategy: "Quant\_INT8-8"
    device: USE\_GPU
    // Provide different .bin files for the multi-input scenario.
    preprocess\_parameter:
    {  
        input\_type: BINARY
        input\_file\_path: "path/to/user/bin/caffe\_inception\_calibrationset1.bin"
    }
    preprocess\_parameter:
    {  
        input\_type: BINARY
        input\_file\_path: "path/to/user/bin/caffe\_inception\_calibrationset2.bin"
    }
    // ...
    exclude\_op:  "conv1"
    exclude\_op:  "conv2;conv3"
    

-   IMAGE input mode
    
    strategy: "Quant\_INT8-8"
    device: USE\_GPU
    // Provide different image paths for the multi-input scenario.
    preprocess\_parameter:
    {
        input\_type: IMAGE
        image\_format: BGR
        mean\_value: 104.0
        mean\_value: 113.0
        mean\_value: 123.0
        standard\_deviation: 0.5
        input\_file\_path: "path/to/user/images1/"
    }
    preprocess\_parameter:
    {
        input\_type: IMAGE
        image\_format: BGR
        mean\_value: 104.0
        mean\_value: 113.0
        mean\_value: 123.0
        standard\_deviation: 0.5
        input\_file\_path: "path/to/user/images2/"
    }
    // ...
    exclude\_op:  "conv1"
    exclude\_op:  "conv2;conv3"
    

#### TensorFlow Model Quantization in Non-Training Mode

## Environment Setup

This function is supported in TensorFlow 2.8 CPU or GPU version. Install the environment as required. Skip this step if the environment is ready.

Install TensorFlow 2.8 as follows:

pip3 install tensorflow-gpu==2.8

## Model Quantization

Run **python3 tools\_dopt/dopt\_tf\_py3/dopt\_so.py** in Python 3.

The parameters for running the script to quantize the TensorFlow model in non-training mode are as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4/v3/px9xUD7sQCmMIH7MDSdXOw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=895004954F6ACAC1EE931088A2BAE741F40D1EE210F1E1DAF1E1E4BC45F4E73F)

-   The path can contain uppercase letters, lowercase letters, digits, and underscores (\_).
-   The file name can contain uppercase letters, lowercase letters, digits, underscores (\_), and periods (.).

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

\-m, --mode

 | 

Yes

 | 

Operating mode.

-   **0**: non-training mode (currently, the value can only be **0**)

 |
| 

\--framework

 | 

Yes

 | 

Deep learning framework.

-   **3**: TensorFlow
-   **5**: PyTorch or ONNX

 |
| 

\--model

 | 

Yes

 | 

Path of the source model file. PB models are supported.

 |
| 

\--cal\_conf

 | 

Yes

 | 

Path of the quantization configuration file for the calibration mode.

For details about the quantization configuration file, see [Editing the config.prototxt File](#section2065711363111).

 |
| 

\--output

 | 

Yes

 | 

Absolute path of the quantized model file, for example, **/path/to/out/resnet18.pb**.

 |
| 

\--input\_format

 | 

Yes

 | 

Input data format, which can be NHWC or NCHW.

When you select the IMAGE format or the .bin file whose file header is 510 as the input data, and select NHWC as the input data format, the tool automatically adjusts the channel sequence. When you select the .bin file whose file header is 610 as the input data, the tool will not adjust the channel sequence.

 |
| 

\--input\_shape

 | 

Yes

 | 

Shape of the input data.

Example: **input\_name1:n1,c1,h1,w1;input\_name2:n2,c2,h2,w2**. **input\_name** must be the node name in the network model before conversion. If there are multiple input shapes, separate them by using semicolons (;). The input dimensions of **input\_shape** must be consistent with input node specified in the network model. See the following two examples: If the input node is **input\_shape\_network: none, 224, 224, 3;** with the last three dimensions specified before conversion, the second, third, and fourth dimensions of **input\_shape** must be **224**, **224**, and **3**. If the input node is **input\_shape\_network: 1, 224, 224, 3** before conversion, with all the four dimensions specified, **input\_shape** can only be **1, 224, 224, 3**.

 |
| 

\--out\_nodes

 | 

Yes

 | 

Output node.

For example, "node\_name1; node\_name2; node\_name3". **node\_name** must be the node name in the network model before model conversion.

 |
| 

\--compress\_conf

 | 

Yes

 | 

Path of the binary file converted from the model file,

for example, **param\_file**. This file is a size reduction configuration file, and will be used as the input of the **compress\_conf** parameter during OMG-based offline model conversion.

 |
| 

\--device\_idx

 | 

No

 | 

Device ID of the GPU or CPU. The default value is **0**.

 |

After the quantization script is executed, the .pb file and quantization configuration file are output, with the names you have input respectively for **\--output** and **\--compress\_conf**. For example, if you input **quantmodel.pb** for **\--output** and **param** for **\--compress\_conf**, **quantmodel.pb** and **param** will be output.

#### PyTorch Model Quantization in Non-Training Mode

## Environment Setup

This function is only available in PyTorch 1.11. Run the following command to install the dependency:

pip3 install torch==1.11

## Model Quantization

Run **python3 tools\_dopt/dopt\_pytorch\_py3/dopt\_so.py**. The parameters for running the script to quantize the PyTorch model in non-training mode are as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/5a/v3/zeZLZwITTJCjxrxDU7yyaQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=A3E69D2328C12DA5D594D392AA3CBF1F9724539C4315F2375DE2522D1D7E3460)

The path can contain uppercase letters, lowercase letters, digits, and underscores (\_).

The file name can contain uppercase letters, lowercase letters, digits, underscores (\_), and periods (.).

| 
Parameter

 | 

Mandatory

 | 

Description

 |
| :-- | :-- | :-- |
| 

\-m, --mode

 | 

Yes

 | 

Operating mode.

-   **0**: non-training mode (currently, the value can only be **0**)

 |
| 

\--framework

 | 

Yes

 | 

Deep learning framework.

-   **3**: TensorFlow
-   **5**: PyTorch or ONNX

 |
| 

\--model

 | 

Yes

 | 

Path of the PyTorch model definition file.

 |
| 

\--weight

 | 

Yes

 | 

Path of the .pth PyTorch model parameter file.

 |
| 

\--cal\_conf

 | 

Yes

 | 

Path of the quantization configuration file for the calibration mode.

For details about the quantization configuration file, see [Editing the config.prototxt File](#section2065711363111).

 |
| 

\--output

 | 

Yes

 | 

Absolute path of the quantized model file, for example, **/path\_to\_out/resnet.pt**.

 |
| 

\--input\_shape

 | 

Yes

 | 

Shape of the input data. For example, in **input\_name1:n1, c1, h1, w1; input\_name2: n2, c2, h2, w2**, **input\_name** is the input parameter of the **forward()** function in the model file. **input\_shape** specifies dimension information of the input data, which is used to convert the PyTorch model. The shape must be the same as that of the input node of the actual model.

 |
| 

\--compress\_conf

 | 

Yes

 | 

Path of the binary file converted from the model file,

for example, **param\_file**. This file is a size reduction configuration file, and will be used as the input of the **compress\_conf** parameter during OMG-based offline model conversion.

 |
| 

\--device\_idx

 | 

No

 | 

Device ID of the GPU or CPU. The default value is **0**.

 |
| 

\--input\_format

 | 

No (for PyTorch)

 | 

Input data format, which can be NHWC or NCHW.

When you select the IMAGE format or the .bin file whose file header is 510 as the input data, and select NHWC as the input data format, the tool automatically adjusts the channel sequence. When you select the .bin file whose file header is 610 as the input data, the tool will not adjust the channel sequence.

 |
| 

\--out\_nodes

 | 

No (for PyTorch)

 | 

Output node.

For example, "node\_name1; node\_name2; node\_name3". **node\_name** must be the node name in the network model before model conversion.

 |

After the quantization script is executed, the .pt file and quantization configuration file are output, with the names you have input respectively for **\--output** and **\--compress\_conf**. For example, if you input **quantmodel.pt** for **\--output** and **param** for **\--compress\_conf**, **quantmodel.pt** and **param** will be output.

#### ONNX Model Quantization in Non-Training Mode

## Environment Setup

This function is supported in the ONNX Runtime 1.15 CPU version and the ONNX environment. Install the environment as required. Skip this step if the environment is ready.

Install ONNX as follows:

pip3 install onnx==1.14

Install other dependencies:

pip3 install protobuf==3.20.0

Install the ONNX Runtime CPU version as follows:

pip3 install onnxruntime==1.15

## Model Quantization

Run **python3 tools\_dopt/dopt\_onnx\_py3/dopt\_so.py** in Python 3.

The parameters for running the script to quantize the ONNX model in non-training mode are as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e1/v3/CQ56EKxjSrC59u6WMFTqQg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0C48C5A55CA26BE09BC746F5C37531E3CE5E553AB6FFC62FC66981E3CE2724B8)

-   The path can contain uppercase letters, lowercase letters, digits, and underscores (\_).
-   The file name can contain uppercase letters, lowercase letters, digits, underscores (\_), and periods (.).

| 
**Parameter**

 | 

**Mandatory**

 | 

**Description**

 |
| :-- | :-- | :-- |
| 

\-m, --mode

 | 

Yes

 | 

Operating mode.

-   **0**: non-training mode (currently, the value can only be **0**)

 |
| 

\--framework

 | 

Yes

 | 

Deep learning framework.

-   **3**: TensorFlow
-   **5**: PyTorch or ONNX

 |
| 

\--weight

 | 

No (for ONNX)

 | 

Path of the weight file.

 |
| 

\--model

 | 

Yes

 | 

Path of the source model file. ONNX models are supported.

 |
| 

\--cal\_conf

 | 

Yes

 | 

Path of the quantization configuration file for the calibration mode.

For details about the quantization configuration file, see [Editing the config.prototxt File](#section2065711363111).

 |
| 

\--output

 | 

Yes

 | 

Absolute path of the quantized model file, for example, **/path\_to\_out/resnet.onnx**.

 |
| 

\--input\_format

 | 

Yes

 | 

Input data format, which can be NHWC or NCHW.

When you select the IMAGE format or the .bin file whose file header is 510 as the input data, and select NHWC as the input data format, the tool automatically adjusts the channel sequence. When you select the .bin file whose file header is 610 as the input data, the tool will not adjust the channel sequence.

 |
| 

\--input\_shape

 | 

Yes

 | 

Shape of the input data.

Example: **input\_name1:n1,c1,h1,w1;input\_name2:n2,c2,h2,w2**. **input\_name** must be the node name in the network model before conversion. If there are multiple input shapes, separate them by using semicolons (;). The input dimensions of **input\_shape** must be consistent with input node specified in the network model. See the following two examples: If the input node is **input\_shape\_network: none, 224, 224, 3;** with the last three dimensions specified before conversion, the second, third, and fourth dimensions of **input\_shape** must be **224**, **224**, and **3**. If the input node is **input\_shape\_network: 1, 224, 224, 3** before conversion, with all the four dimensions specified, **input\_shape** can only be **1, 224, 224, 3**.

 |
| 

\--out\_nodes

 | 

Yes

 | 

Output node.

For example, "node\_name1; node\_name2; node\_name3". **node\_name** must be the node name in the network model before model conversion.

 |
| 

\--compress\_conf

 | 

Yes

 | 

Path of the binary file converted from the model file,

for example, **param\_file**. This file is a size reduction configuration file, and will be used as the input of the **compress\_conf** parameter during OMG-based offline model conversion.

 |
| 

\--device\_idx

 | 

No (for ONNX)

 | 

Device ID of the GPU or CPU. The default value is **0**.

 |

After the quantization script is executed, the .onnx file and quantization configuration file are output, with the names you have input respectively for **\--output** and **\--compress\_conf**. For example, if you input **quantmodel.onnx** for **\--output** and **param** for **\--compress\_conf**, **quantmodel.onnx** and **param** will be output.
