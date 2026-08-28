# Model Conversion Example

Before using the CANN Kit SDK, you can use the OMG to convert Caffe, TensorFlow, ONNX, and MindSpore models into offline models (OMs), so that the mobile AI app can directly read the OM for inference. The OMG is located in the **tools/tools\_omg** directory of the [tools](../../../getting-started/document.md#section152959341125). It can run on 64-bit Linux.

#### Caffe Model Conversion

[Caffe](https://gitee.com/mirrors/caffe) 1.0 is currently supported.

See [OMG Parameters](../omg-parameters/document.md) for details about the parameters in the command. The conversion command is as follows:

./omg --model xxx.prototxt --weight yyy.caffemodel --framework 0 --output ./modelname

Conversion example:

./omg --model deploy.prototxt --weight squeezenet\_v1.1.caffemodel --framework 0 --output ./squeezenet

If the log message "OMG generate offline model success" is printed, the model is successfully converted. A **squeezenet.om** file is generated in the current directory.

#### TensorFlow Model Conversion

[TensorFlow](https://www.tensorflow.org/?hl=zh-cn) 2.x is currently supported.

See [OMG Parameters](../omg-parameters/document.md) for details about the parameters in the command. The conversion command is as follows:

./omg --model xxx.pb --framework 3 --output ./modelname --input\_shape "xxx:n,h,w,c" --out\_nodes "node\_name1:0"

Conversion example:

./omg --model mobilenet\_v2\_1.0\_224\_frozen.pb --framework 3 --output ./mobilenet\_v2 --input\_shape "input:1,224,224,3" --out\_nodes "MobilenetV2/Predictions/Reshape\_1:0"

If the log message "OMG generate offline model success" is printed, the model is successfully converted. A **mobilenet\_v2.om** file is generated in the current directory.

#### ONNX Model Conversion

Currently, [ONNX](https://github.com/onnx/onnx) opset versions from 7 to 18 are supported (the latest supported version is V1.13.1).

See [OMG Parameters](../omg-parameters/document.md) for details about the parameters in the command. The conversion command is as follows:

./omg --model xxx.onnx --framework 5 --output ./modelname 

Conversion example:

./omg --model resnet18.onnx --framework 5 --output ./resnet18

If the following logs are printed, the model is successfully converted. A **resnet18.om** file is generated in the current directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/15/v3/5dUSL_3NScSYbRTYn5fxQg/en-us_image_0000002496888540.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8A981FBA2C9E462A825C67B21CC1F83832C9C6841B8D873571BA05D5AB927475 "Click to enlarge")

#### Model Conversion with Quantization (Using the Caffe Model as an Example)

Most models use the 16-bit float type for computation on the NPU. Quantizing models can reduce the model size and thereby accelerate model inference.

Model conversion with quantization depends on the size reduction tool to generate the model and size reduction configuration. The **compress\_conf** parameter is passed to the OMG to generate a quantized model. For details, please refer to [Model Size Reduction](../../../model-optimization/model-size-reduction/overview/document.md).

See [OMG Parameters](../omg-parameters/document.md) for details about the parameters in the command. The conversion command is as follows:

./omg --model xxx.prototxt --weight xxx.caffemodel --framework 0 --output ./modelname  --compress\_conf=param

Conversion example:

./omg --model deploy.prototxt --weight squeezenet\_v1.1.caffemodel --framework 0 --output ./squeezenet --compress\_conf=param

If the message "OMG generate offline model success" is printed, the model is successfully quantized. A quantized model **squeezenet.om** is generated in the current directory.

#### Model Conversion with Variable Shapes Before Inference (Using the ONNX Model as an Example)

If a model needs to be loaded at a time, and different batches or image sizes may appear in different inference processes, you can use the variable shape before the inference.

To do so, before performing model conversion, specify all of the shape types that may appear during model inference through **dynamic\_dims** and **input\_shape**, to generate a standard IR model that carries multiple input shapes.

For details about parameters in the command, see [OMG Parameters](../omg-parameters/document.md).

Conversion example:

./omg --model=./1batch.onnx --input\_shape="inputName:-1,3,128,128" --dynamic\_dims="1;2;5" --framework=5 --output=./FlexibleShapeModelName

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/34/v3/FAK38VrkSwimpxGZ4NBq3A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0E096CD0AB22E50B48224E6745F15E9AA00D0432A8BF393E22AC4C11CBEAE210)

Different input shapes correspond to different output shapes. You can search for the shape information by the keyword "Graph:" in the model conversion log, and describe the output during model inference.

#### MindSpore Model Conversion

MindSpore supports a limited number of operators. You are advised to use [TensorFlow Model Conversion](#section165091091578) or [ONNX Model Conversion](#section59657541256) instead.

#### Model Conversion with AIPP (Using the Caffe Model as an Example)

The AIPP module is introduced for input pre-processing including image cropping and resizing, color space conversion (CSC), mean subtraction and factor multiplication, and much more. Operators are added to the converted model to replace these operations, improving the efficiency.

See [OMG Parameters](../omg-parameters/document.md) for details about the parameters in the command. The conversion command is as follows:

./omg --model xxx.prototxt --weight xxx.caffemodel --framework 0 --insert\_op\_conf aipp\_conf\_static.cfg --output ./modelname

Conversion example:

./omg --model deploy.prototxt --weight squeezenet\_v1.1.caffemodel --framework 0 --insert\_op\_conf aipp\_conf\_static.cfg --output ./squeezenet

If the log message "OMG generate offline model success" is printed, the model is successfully converted. An AIPP model **squeezenet.om** is generated in the current directory.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/2a/v3/2Q8yOvISQtqSsV8Bjf1vqw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F49BD2548F9BB2E3DAC4DC2407D835FCAD7F9159A2471227A93D47A60CB6DDC6)

**aipp\_conf\_static.cfg** in the **tools/tools\_omg/sample** folder is the AIPP configuration file. For details, please refer to [AIPP Configuration File](../../aipp/aipp-configuration-file-used-for-model-conversion/document.md#section1435315264269).
