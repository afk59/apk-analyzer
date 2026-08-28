# OMG Parameters

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/a9/v3/2R2zkHl8RKiSxvG8x59mRg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=96A4756DB1EC84AA91A03A5E4356BF61D84284D96E0AAE3D0F1E2906E1B090E0)

-   The path can contain uppercase letters, lowercase letters, digits, and underscores (\_).
-   The file name can contain uppercase letters, lowercase letters, digits, underscores (\_), and periods (.).

| 
Parameter

 | 

Description

 | 

Mandatory

 | 

Default Value

 |
| :-- | :-- | :-- | :-- |
| 

\--h/help

 | 

Help information display.

 | 

No

 | 

N/A

 |
| 

\--mode

 | 

Operating mode.

-   **0**: Generates a Da Vinci model.
-   **1**: Converts a model to JSON. Converting a model to JSON allows you to view the model architecture in text format.

-   **3**: Performs precheck only to check the validity of the model file.

 | 

No

 | 

0

 |
| 

\--model

 | 

Path of the source model file.

 | 

Yes

 | 

N/A

 |
| 

\--framework

 | 

Framework of the source model.

-   **0**: Caffe
-   **3**: TensorFlow
-   **5**: ONNX
-   **6**: MindSpore

NOTE:

-   This parameter is not mandatory when **mode** is set to **1**, and you can specify Caffe, TensorFlow, ONNX, or MindSpore. If this parameter is not set, the offline model is converted to the JSON format by default.
-   This parameter is mandatory when **mode** is set to **0** or **3**. You can specify Caffe, TensorFlow, ONNX, or MindSpore.
-   When the original model format is TensorFlow CheckPoint, SavedModel, or TFLite, it is advised to use the [tf2onnx](https://github.com/onnx/tensorflow-onnx) tool to convert the model into an ONNX model.

 | 

Yes

 | 

N/A

 |
| 

\--weight

 | 

Path of the weight file. This parameter is mandatory when the source model is a Caffe model, and is optional for source models of other frameworks.

 | 

No

 | 

N/A

 |
| 

\--output

 | 

Path for storing the converted offline model file (including the file name), for example, **out/caffe\_resnet18**. The converted model file is automatically suffixed with **.om**.

 | 

Yes

 | 

N/A

 |
| 

\--hiai\_version

 | 

OMG version to be used: **v300** | **v310** | **IR**

 | 

No

 | 

IR

 |
| 

\--om

 | 

Path of the model file. This parameter is mandatory when **mode** is set to **1**.

 | 

No

 | 

N/A

 |
| 

\--json

 | 

Path of the generated JSON model file.

 | 

No

 | 

N/A

 |
| 

\--input\_shape

 | 

Shape of the input data. If this parameter is set to **\-1**, it must be used together with the **\--dynamic\_dims** parameter.

For example, in **input\_name1:n1, c1, h1, w1; input\_name2: n2, c2, h2, w2**, **input\_name** must be the node name in the network model before conversion.

If the source model is an ONNX model, **input\_name** must be the name of the input operator in the network model before model conversion.

NOTE:

-   This parameter is mandatory when the source model is an ONNX model and the input dimension of the ONNX model is dynamic.
-   This parameter is mandatory when the source model is a TensorFlow model and the input dimension of the TensorFlow model is dynamic.

 | 

No

 | 

N/A

 |
| 

\--input\_format

 | 

Input data format, which can be NCHW or NHWC.

NOTE:

-   This parameter does not take effect when the source framework is Caffe, ONNX, or MindSpore.
-   This parameter does not need to be specified in most scenarios when the source model framework is TensorFlow. Specify it as required during conversion.

 | 

No

 | 

N/A

 |
| 

\--input\_type

 | 

Model input (multi-input or single-input) data type. The supported data types include FP32, FP16, INT32, and UINT8. Whether an offline model can be successfully generated depends on whether the source model supports the specified input data type. For the supported model input data types, see [Input Data Types Supported in Non-AIPP Scenarios](#li13442526155) and [Input Data Types Supported in AIPP Scenarios](#li478393817151).

Example: **input\_name1:FP16;input\_name2:UINT8**

**input\_name** must be the node name in the network model before conversion.

If the source model is an ONNX model, **input\_name** must be the name of the input operator in the network model before model conversion.

 | 

No

 | 

FP32

 |
| 

\--input\_fp16\_nodes

 | 

This parameter and **\--input\_type** are exclusive.

Name of the FP16 (NCHW) input node.

Example: **node\_name1;node\_name2**

NOTE:

This parameter does not take effect when the source framework is ONNX or MindSpore.

 | 

No

 | 

N/A

 |
| 

\--out\_nodes

 | 

Output node.

-   Specify the parameter in the following format if the original model is a TensorFlow or Caffe model: "node\_name1:0;node\_name1:1;node\_name2:0".
    
    **node\_name** must be the node name in the network model before model conversion. Outputs of the same node are numbered from 0 in ascending order.
    

-   Specify the parameter in the following format if the original model is an ONNX model: "tensor\_name1;tensor\_name2".
    
    **tensor\_name** must be the tensor name output by the node in the network model before model conversion.
    

 | 

No

 | 

N/A

 |
| 

\--output\_type

 | 

Model output (multi-output or single-output) data type. The supported data types include FP32, FP16, INT32, and UINT8. Whether an offline model can be successfully generated depends on whether the source model supports the specified output data type. For the supported model output data types, see [Input Data Types Supported in Non-AIPP Scenarios](#li13442526155).

Example: **output\_name1:FP16;output\_name2:UINT8**

**output\_name** must be the node name in the network model before conversion.

If the source framework is ONNX, **output\_name** can be the name of the output operator in the network model before model conversion or the **tensor\_name** used in the specified **out\_nodes**.

 | 

No

 | 

FP32

 |
| 

\--is\_output\_fp16

 | 

This parameter and **\--output\_type** are exclusive.

Whether the data type of an output is FP16 (NCHW).

Example: **false, true, false, true**

NOTE:

This parameter does not take effect when the source framework is ONNX or MindSpore.

 | 

No

 | 

false

 |
| 

\--stream\_num

 | 

Number of streams used by the model. The value must be **1**.

 | 

No

 | 

1

 |
| 

\--check\_report

 | 

Path of the precheck result file. If this path is not specified, the precheck result is saved in the current path when the model conversion fails or **mode** is set to **3** (precheck only).

 | 

No

 | 

N/A

 |
| 

\--net\_format

 | 

Preferred data format for network operators.

NOTE:

This parameter is not recommended and can be derived from the network.

 | 

No

 | 

N/A

 |
| 

\--insert\_op\_conf

 | 

Path of the AIPP configuration file. For details, see [AIPP Configuration File Used for Model Conversion](../../aipp/aipp-configuration-file-used-for-model-conversion/document.md).

 | 

No

 | 

N/A

 |
| 

\--op\_name\_map

 | 

Path of the operator mapping configuration file. This parameter is mandatory when the **DetectionOutput** network is used.

For example, a **DetectionOutput** operator can play different roles in different networks. It can specify the mapping from **DetectionOutput** to **FSRDetectionOutput** or to **SSDDetectionOutput**.

NOTE:

The following is a content reference of the operator mapping configuration file:

DetectionOutput: SSDDetectionOutput

 | 

No

 | 

N/A

 |
| 

\--compress\_conf

 | 

Path of the size reduction configuration file. This parameter is automatically generated by the size reduction tool. For details, please refer to [Model Size Reduction](../../../model-optimization/model-size-reduction/overview/document.md).

 | 

No

 | 

N/A

 |
| 

\--weight\_data\_type

 | 

Weight data type, which can be **FP32** or **FP16**.

This parameter takes effect only when the existing weight is of the FP32 type. If the value is FP16 (default), the weight is converted from FP32 to FP16. If the value is FP32, the data type of the weight remains unchanged as FP32.

Example: **weight\_data\_type:FP16**

NOTE:

Set this parameter to **FP32** if you need the model to be compatible with a CPU compute library (CPUCL), which does not support weight of the FP16 type.

 | 

No

 | 

FP16

 |
| 

\--weight\_merge

 | 

Switch for merging weights of offline models. You can specify whether to merge and store weights when generating offline models. If this parameter is set to **true**, the model weights are merged and stored. If this parameter is set to **false**, the weights are stored without being merged, which has no impact on performance. The parameter is set to **true** by default.

 | 

No

 | 

true

 |
| 

\--use\_origin\_format

 | 

The input and output formats of a model can be set to be the same as those of the source model.

NOTE:

This parameter can be set to **true** only for service network conversion based on **yolo** and **inception**. For other network conversion, use the default value **false**.

 | 

No

 | 

false

 |
| 

\--dynamic\_dims

 | 

The same source model can be used to generate Da Vinci models that support different dimensions of the input shape. This parameter specifies the variable dimension (**dim**). It is used together with the **\--input\_shape** parameter. You can use **\-1** to represent the variable **dim** in **input\_shape**.

Values of the variable **dims** in this parameter are separated by semicolons (;), and dimensions are separated by commas (,). Examples:

-   Dynamic batch
    
    \--input\_shape = "input\_name1:-1,c,h,w" --dynamic\_dims = "n1;n2;n3"
    

-   Dynamic image size
    
    \--input\_shape = "input\_name1:n,-1,-1,c" --dynamic\_dims = "h1,w1;h2,w2"
    

NOTE:

Constraints: A maximum of 16 variable shape types are supported.

 | 

No

 | 

N/A

 |
| 

\--platform

 | 

Chip platform. This parameter is mandatory when **--target** is set to **omc**.

 | 

No

 | 

N/A

 |
| 

\--target

 | 

Target model type.

-   om
    
    Hardware-independent Da Vinci model.
    
-   omc
    
    Da Vinci model that is closely related to hardware can be deployed only on the platform specified by **\--platform**.
    

 | 

No

 | 

om

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e7/v3/qkrGxyUhTn2AgJonUm3Sfg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062125Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=940295346F1D2DA16A09164814FAA6682C2A7732EB2382C2590213FE8D0E73FB)

Currently, only the scenarios listed in the following table are supported.

-   Input Data Types Supported in Non-AIPP Scenarios
    
    | 
    **Input of the Source Model**
    
     | 
    
    **Expected Input of the Offline Model (Developer-Defined)**
    
     | 
    
    **OMG Parameter**
    
     |
    | :-- | :-- | :-- |
    | 
    
    FP32
    
     | 
    
    FP16
    
     | 
    
    \--input\_type
    
     |
    | 
    
    FP32
    
     | 
    
    FP32
    
     | 
    
    \--input\_type
    
     |
    | 
    
    FP16
    
     | 
    
    FP16
    
     | 
    
    \--input\_type
    
     |
    | 
    
    UINT8
    
     | 
    
    UINT8
    
     | 
    
    \--input\_type
    
     |
    | 
    
    INT32
    
     | 
    
    INT32
    
     | 
    
    \--input\_type
    
     |
    | 
    
    INT8
    
     | 
    
    INT8
    
     | 
    
    \--input\_type
    
     |
    

-   Input Data Types Supported in AIPP Scenarios
    
    | 
    **Input of the Source Model**
    
     | 
    
    **Expected Input of the Offline Model**
    
     | 
    
    **With AIPP or Not**
    
     | 
    
    **OMG Parameter**
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    FP32
    
     | 
    
    UINT8
    
     | 
    
    Yes
    
     | 
    
    \--input\_type
    
     |
    | 
    
    FP16
    
     | 
    
    UINT8
    
     | 
    
    Yes
    
     | 
    
    \--input\_type
    
     |
    | 
    
    UINT8
    
     | 
    
    UINT8
    
     | 
    
    Yes
    
     | 
    
    \--input\_type
    
     |
    
-   Supported model output data types
    
    | 
    **Source Model**
    
     | 
    
    **Offline Model Output**
    
     | 
    
    **OMG Parameter**
    
     |
    | :-- | :-- | :-- |
    | 
    
    FP32
    
     | 
    
    UINT8
    
     | 
    
    \--output\_type
    
     |
    | 
    
    FP16
    
     | 
    
    UINT8
    
     | 
    
    \--output\_type
    
     |
    | 
    
    UINT8
    
     | 
    
    UINT8
    
     | 
    
    \--output\_type
    
     |
    | 
    
    FP16
    
     | 
    
    FP16
    
     | 
    
    \--output\_type
    
     |
    | 
    
    FP32
    
     | 
    
    FP32
    
     | 
    
    \--output\_type
    
     |
    | 
    
    FP32
    
     | 
    
    FP16
    
     | 
    
    \--output\_type
    
     |
    | 
    
    FP16
    
     | 
    
    FP32
    
     | 
    
    \--output\_type
    
     |
    | 
    
    INT8
    
     | 
    
    INT8
    
     | 
    
    \--output\_type
    
     |
    | 
    
    INT32
    
     | 
    
    INT32
    
     | 
    
    \--output\_type
    
     |
    | 
    
    INT64
    
     | 
    
    INT64
    
     | 
    
    \--output\_type
    
     |
