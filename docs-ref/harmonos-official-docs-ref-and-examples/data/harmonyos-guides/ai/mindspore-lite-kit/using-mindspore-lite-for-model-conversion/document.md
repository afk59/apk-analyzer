# Using MindSpore Lite for Model Conversion

#### When to Use

The deployment process is as follows:

1.  Use the MindSpore Lite model conversion tool to convert the original model (for example, ONNX or CAFFE) to a .ms model file. You can check the supported ONNX operators against the [MindSpore Lite Kit operator list](../appendix/mindspore-lite-kit-operator-list/document.md) to ensure that the model conversion is successful.
2.  Call APIs of the MindSpore Lite inference engine to perform [model inference](../model-deployment/using-mindspore-lite-for-model-inference-c-c/document.md).

#### Obtaining the Model Conversion Tool

You can obtain the MindSpore Lite model conversion tool in either of the following ways:

## Download

| Component | Hardware Platform | OS | URL | SHA-256 |
| :-- | :-- | :-- | :-- | :-- |
| On-device inference and training benchmark tool, converter tool, and cropper tool | CPU | Linux-x86\_64 | [mindspore-lite-2.3.0-linux-x64.tar.gz](https://ms-release.obs.cn-north-4.myhuaweicloud.com/2.3.0/MindSpore/lite/release/linux/x86_64/mindspore-lite-2.3.0-linux-x64.tar.gz) | 060d698a171b52c38b64c8d65927816daf4b81d8e2b5069718aeb91a9f8a154c |

## Source Code Building

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/59/v3/oFtmtLAJQF2BxPO-cxSeAg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=86F4CA9DB772CFB9B4247DC1F09BF6794BF752D864A6D1780275E0DBB4CFF3C2)

-   The build option that supports PyTorch model conversion is disabled by default. Therefore, the downloaded installation package does not support PyTorch model conversion and can be obtained only by source code building.
    
-   If the transpose and convolution operators are fused in the model, you need to obtain the model through source code compilation. Otherwise, an alarm similar to the following may be displayed: node infer shape failed, node is Default/Conv2DFusion-xxx.
    
-   If the NPU backend is used for inference, you need to determine whether to [disable the fusion of clip operators](#disabling-the-fusion-of-specified-operators) and obtain the model conversion tool through source code compilation. Otherwise, an error similar to the following may be reported: BuildKirinNPUModel# Create full model kernel failed.
    

1.  The environment requirements are as follows:
    
    -   System environment: Linux x86\_64 (Ubuntu 18.04.02LTS recommended)
    -   C++ build dependencies:
        -   GCC >= 7.3.0
        -   CMake >= 3.18.3
        -   Git >= 2.28.0
2.  Obtain the [MindSpore Lite source code](https://gitcode.com/openharmony/third_party_mindspore).
    
    The complete source code of MindSpore Lite is available at mindspore-src/source/.
    
3.  Start building.
    
    To obtain the conversion tool that supports PyTorch model conversion, run export MSLITE\_ENABLE\_CONVERT\_PYTORCH\_MODEL=on && export LIB\_TORCH\_PATH="/home/user/libtorch" before you begin model building. Add the libtorch environment variable by running export LD\_LIBRARY\_PATH="/home/user/libtorch/lib:${LD\_LIBRARY\_PATH}" before conversion. You can download the libtorch package of the CPU version and decompress it to /home/user/libtorch.
    
    cd mindspore-src/source/
    bash build.sh -I x86\_64 -j 8
    
    After the building is complete, you can obtain the MindSpore Lite release package from output/ in the root directory of the source code. The conversion tool is available at tools/converter/converter/ after decompression.
    

#### Configure environment variables.

After obtaining the model conversion tool, you need to add the dynamic link library (DLL) required by the conversion tool to the environment variable LD\_LIBRARY\_PATH.

export LD\_LIBRARY\_PATH=${PACKAGE\_PATH}/tools/converter/lib:${LD\_LIBRARY\_PATH}

**${PACKAGE\_PATH}** indicates the path where the MindSpore Lite release package is decompressed.

#### Parameter Description

The MindSpore Lite model conversion tool provides multiple parameter settings. You can use them as required. In addition, you can run ./converter\_lite --help to obtain the help information in real time.

The following describes the parameters in detail.

| Name | Mandatory | Description | Value Range |
| :-- | :-- | :-- | :-- |
| \--help | No | Displays all help information. | \- |
| \--fmk | Yes | Original format of the input model. This parameter can be set to **MSLITE** only when the MS model is converted to micro code. | MINDIR, CAFFE, TFLITE, TF, ONNX, PYTORCH, or MSLITE |
| \--modelFile | Yes | Path of the input model. | \- |
| \--outputFile | Yes | Path of the output model. You do not need to add an extension because the extension .ms is automatically generated. | \- |
| \--weightFile | Yes for CAFFE model conversion | Path of the model weight file. | \- |
| \--configFile | No | 1) Path of the quantization configuration file after training. 2) Path of the extended function configuration file. | \- |
| \--fp16 | No | 
Whether to store the weights of float32 data as float16 data during model serialization.

The default value is **off**.

 | on or off |
| \--inputShape | No | Set the input dimensions of the model. Make sure that the sequence of the input dimensions is the same as that of the original model. The model structure can be further optimized for some specific models, but the dynamic shape feature will be unavailable for the converted model. Separate each input name and shape by a colon (:), and separate each pair of input name and shape by a semicolon (;). In addition, enclose them with double quotation marks (""). For example, set this parameter to **"inTensorName\_1: 1,32,32,4;inTensorName\_2:1,64,64,4;"**. | \- |
| \--inputDataFormat | No | 

Input format of the exported model. This parameter is valid only for 4D input.

The default value is **NHWC**.

 | NHWC or NCHW |
| \--inputDataType | No | 

Data type of the input tensor of the quantization model. This parameter is valid only when the quantization parameters (**scale** and **zero point**) are configured for the input tensor. The data type is the same as that of the input tensor of the original model by default.

The default value is **DEFAULT**.

 | FLOAT32, INT8, UINT8, or DEFAULT |
| \--outputDataType | No | 

Data type of the output tensor of the quantization model. This parameter is valid only when the quantization parameters (**scale** and **zero point**) are configured for the output tensor. The data type is the same as that of the output tensor of the original model by default.

The default value is **DEFAULT**.

 | FLOAT32, INT8, UINT8, or DEFAULT |
| \--outputDataFormat | No | Output format of the exported model. This parameter is valid only for 4D output. | NHWC or NCHW |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8d/v3/C3oVfi2mSg-xLCLpA0q1Xg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062128Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=89F065702B67C14A6FC9AD01E47D5E5F662D0F8C043BD2C3BF42F7C6B3650B16)

-   The parameter name and value are separated by an equal sign (=) and no space is allowed between them.
-   Generally, a CAFFE model has two files: the model structure \*.prototxt, which corresponds to the --modelFile parameter, and the model weight \*.caffemodel, which corresponds to the --weightFile parameter.

#### Example

The following conversion command uses the CAFFE model LeNet as an example.

./converter\_lite --fmk=CAFFE --modelFile=lenet.prototxt --weightFile=lenet.caffemodel --outputFile=lenet

In this example, the CAFFE model is used. Therefore, you need to specify two input files: model structure and model weight. In addition, add other mandatory parameters, that is, fmk type and output path.

The command output is as follows:

CONVERT RESULT SUCCESS:0

This indicates that the CAFFE model is successfully converted to the MindSpore Lite model. A new file named **lenet.ms** is generated in the specified path.

#### (Optional) Offline Model Conversion

If you want to reduce the loading delay to meet the requirements of the deployment scenario, you can use offline model-based inference as an alternative. Offline models are network models obtained using the offline model conversion tool of the AI hardware vendor. The hardware vendor is responsible for parsing and inference of offline models.

During inference, MindSpore Lite directly sends the offline model to the AI hardware connected to NNRt. This way, the model can be loaded without the need for online image composition, greatly reducing the model loading delay. In addition, MindSpore Lite can provide additional hardware-specific information to assist the AI hardware in model inference.

## Constraints

-   Offline model inference can only be implemented at the NNRt backend. The AI hardware needs to connect to NNRt and support offline model inference.
-   The offline model conversion tool can be obtained only through source code building.
-   During offline model conversion, fmk must be set to THIRDPARTY.
-   The offline model comes as a black box and cannot be directly parsed by the conversion tool to obtain its input and output tensor information. Therefore, you need to manually configure the tensor information in the extended configuration file of the conversion tool.

## Description of the Extended Configuration File

An example of the extended configuration is as follows:

-   \[third\_party\_model\] in the first line is a fixed keyword that indicates the section of offline model configuration.
-   The following lines exhibit the name, data type, shape, and memory format of the input and output tensors of the model respectively. Each field occupies a line and is expressed in the key-value pair format. The sequence of fields is not limited.
-   Among the fields, data type and shape are mandatory, and other parameters are optional.
-   Extended parameters are also provided. They are used to encapsulate custom configuration of the offline model into an .ms file in the key-value pair format. The .ms file is passed to the AI hardware by NNRt during inference.

\[third\_party\_model\]
input\_names=in\_0;in\_1
input\_dtypes=float32;float32
input\_shapes=8,256,256;8,256,256,3
input\_formats=NCHW;NCHW
output\_names=out\_0
output\_dtypes=float32
output\_shapes=8,64
output\_formats=NCHW
extended\_parameters=key\_foo:value\_foo;key\_bar:value\_bar

Field description:

-   input\_names (optional): model input name, which is in the string format. If multiple names are specified, use a semicolon (;) to separate them.
-   input\_dtypes (mandatory): model input data type, which is in the type format. If multiple data types are specified, use a semicolon (;) to separate them.
-   input\_shapes (mandatory): model input shape, which is in the integer array format. If multiple input shapes are specified, use a semicolon (;) to separate them.
-   input\_formats (optional): model input memory format, which is in the string format. If multiple formats are specified, use a semicolon (;) to separate them. The default value is NHWC.
-   output\_names (optional): model output name, which is in the string format. If multiple names are specified, use a semicolon (;) to separate them.
-   output\_dtypes (mandatory): model output data type, which is in the type format. If multiple data types are specified, use a semicolon (;) to separate them.
-   output\_shapes (mandatory): model output shape, which is in the integer array format. If multiple output shapes are specified, use a semicolon (;) to separate them.
-   output\_formats (optional): model output memory format, which is in the string format. If multiple formats are specified, use a semicolon (;) to separate them. The default value is NHWC.
-   extended\_parameters (optional): custom configuration of the inference hardware, which is in the key-value pair format. It is passed to the AI hardware through the NNRt backend during inference.

#### Appendix

## Disabling the Fusion of Specified Operators

If you need to disable the fusion of specified operators, create a configuration file, for example, **converter.cfg**, and configure and file content as follows:

\[registry\]
# If \*\*disable\_fusion\*\* is set to \*\*off\*\*, you can configure \*\*fusion\_blacklists\*\* to disable the fusion of specified operators. If \*\*disable\_fusion\*\* is set to \*\*on\*\*, the fusion of operators is disabled, and \*\*fusion\_blacklists\*\* does not take effect. The default value of \*\*disable\_fusion\*\* is \*\*off\*\*.
disable\_fusion=off
# To disable the fusion of multiple operators, separate the operators with commas (,).
fusion\_blacklists=ConvActivationFusion,MatMulActivationFusion,clip\_convert\_activation\_pass

When running the converter, set **configFile** to **converter.cfg**.

The following lists the operators for which fusion can be disabled:

-   AddConcatActivationFusion
-   SqueezeFusion
-   TransposeFusion
-   ReshapeReshapeFusion
-   ConvBiasaddFusion
-   ConvBatchNormFusion
-   ConvScaleFusion
-   GroupNormFusion
-   TfNormFusion
-   OnnxLayerNormFusion
-   OnnxLayerNormFusion2
-   BatchMatMulFusion
-   BatchNormToScaleFusion
-   SigmoidMulFusion
-   ActivationFusion
-   ConvActivationFusion
-   ConvTupleGetItemFusion
-   ConvTupleActivationFusion
-   TfliteLstmCellFusion
-   TfLstmCellFusion
-   TfBidirectionGruFusion
-   TfGeLUFusion
-   OnnxGeLUFusion
-   TfliteRelPosMultiHeadAttentionFusion
-   GLUFusion
-   ConstFoldPass
-   AffineFusion
-   AffineActivationFusion
-   ConvConvFusion
-   ConvPadFusion
-   MatMulAddFusion
-   MatMulMulFusion
-   TransposeMatMulFusion
-   MulAddFusion
-   ScaleActivationFusion
-   ScaleScaleFusion
-   FullConnectedFusion
-   FullconnectedAddFusion
-   TensorDotFusion
-   MatMulActivationFusion
-   clip\_convert\_activation\_pass
