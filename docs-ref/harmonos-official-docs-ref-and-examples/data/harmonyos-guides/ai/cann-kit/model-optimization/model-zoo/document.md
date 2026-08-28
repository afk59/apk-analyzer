# Model Zoo

#### Overview

Model Zoo provides a model library that you can call directly for the optimal hardware performance. In the library, you can find network models for typical scenarios like image classification, object detection, semantic segmentation, and super resolution. In this section, you will learn how to use CANN to ensure the optimal performance, performance-friendly model architectures, and the recommendation levels. You will be able to quickly learn how to set parameters of operators to achieve the optimal performance and energy efficiency on hardware, and how to optimize the model architecture for high performance and low power consumption.

#### Downloading Models from Model Zoo

In the **Download** column, the .caffemodel, .pb, and .onnx files represent original floating-point models. These models are implemented based on related papers and have been adjusted for NPU hardware affinity. Therefore, the input dimensions of these models may differ from those described in the corresponding papers.

The .om model files are built by standard IR operators, among which **quant8\_8.om** is generated through quantization. All models can be visualized using the [Netron tool](../../appendixes/visualization-tool/document.md).

The following table lists the name, performance, download, and other information of models in Model Zoo.

| 
Scenario

 | 

Network Model (Single-Batch)

 | 

Floating-Point Performance\[1\] (Time Required: ms)

 | 

Quantization Performance\[1\] (Time Required: ms)

 | 

Download

 | 

SHA-256 Checksum

 | 

Reference\[2\]

 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 

Image classification

 | 

Alexnet

 | 

9.92

 | 

4.49

 | 

[CAFFE & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/42/v3/eyPGmahYTnKtskcw6wC7yg/hwhiaimodelzoo-alexnet-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T083009Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=9F85C5C4E2A049C8F6502D37F45E9FF743213331FA837B19F492C961451F5C1E)

 | 

7b01980acf0d16dadc6c9c326cdf757d2166928ae49cfd4091df154a5c512640

 | 

[Paper & implementation](https://arxiv.org/abs/1404.5997)

 |
| 

Resnet18

 | 

2.63

 | 

1.24

 | 

[CAFFE & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2b/v3/-3ps6ob3QO6CSom10fi0Gw/hwhiaimodelzoo-resnet18-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T081504Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=1E7889E8F15927FF8198A949D5D9B42CC3CB81F4CE9A1F341CB4E90B77346E45)

 | 

4aa7caaa112f5280cb5c0ab5eed6edf84a16fe9a0b92b9ee333a808c9f07e886

 | 

[Paper & implementation](https://arxiv.org/abs/1512.03385)

 |
| 

VGG16

 | 

16.56

 | 

8.55

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/d3/v3/iCUHL864TRKbqKINLlFKnQ/hwhiaimodelzoo-vgg16-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T081340Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=4F2EA9998432D7CD60710CD7690E3554C71512D6AA74F2E01FAD30A9CD4AC70B)

 | 

f9193765889077e5997ddc8c1e75a563c8a1205e613da9634d3d83277962dd42

 | 

[Paper & implementation](https://arxiv.org/abs/1409.1556)

 |
| 

VGG19

 | 

18.34

 | 

8.73

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/21/v3/gd9SP5_hRG2JfFW-8tgC0Q/hwhiaimodelzoo-vgg19-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T080831Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=C156643FD0B8EC4C829972E8C460EA8FF1CB3AEEBCD7DADD5CD031E98FC301A5)

 | 

d19f363602740ff5859380c40ca6f0bed0cb3744f469873cdf862c71c7007a94

 | 

[Paper & implementation](https://arxiv.org/abs/1409.1556)

 |
| 

Resnet50

 | 

5.15

 | 

3.54

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/10/v3/Q-dHdmq1TQ6FzYOy60u1VQ/hwhiaimodelzoo-resnet50-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T081405Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=BB6F826B1072CDDBA83C6D7351CEF356327EFF7D97EE84C788F9621E1A9A4CE6)

 | 

6dedf4b5c3bfdaf70410236f1f73d942a5231f217e18c51918ba39b3b740b2df

 | 

[Paper & implementation](https://arxiv.org/abs/1512.03385)

 |
| 

Inception\_v3

 | 

6.56

 | 

3.76

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/4f/v3/qtjKvj1sSoK8_ySu6xLE2g/hwhiaimodelzoo-inceptionv3-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082107Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=2788E8301870BD3C1AC15B845CF204B27BA412C976A9670B1DDF984A8AAA0026)

 | 

d06c88a79acd19b10d5f7eddaae6aba3c02372cfdb036296b845aa3a9ccf46be

 | 

[Paper & implementation](https://arxiv.org/abs/1512.00567)

 |
| 

Inception\_v4

 | 

11.90

 | 

7.29

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/5c/v3/HCh4-WFvR6iw4egm2vAvxQ/hwhiaimodelzoo-inceptionv4-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082010Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=194B3E4976AE798E8A887AA69BF9894D30EDA727BF8B9B06428892A2A9BD9918)

 | 

e042f489e6915eb6de5daa4b3200462e76f1bedca7147e2a19e8311a4b05afde

 | 

[Paper & implementation](https://arxiv.org/abs/1602.07261)

 |
| 

Inception\_Resnet\_v2

 | 

15.91

 | 

5.59

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/5c/v3/HCh4-WFvR6iw4egm2vAvxQ/hwhiaimodelzoo-inceptionv4-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082010Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=194B3E4976AE798E8A887AA69BF9894D30EDA727BF8B9B06428892A2A9BD9918)

 | 

229164e49753126357f4a587694ca925afa60d1bfec184dba00085d69b5fc47b

 | 

[Paper & implementation](https://arxiv.org/abs/1602.07261)

 |
| 

Mobilenet\_v1

 | 

2.16

 | 

0.52

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2c/v3/KzMd67g3TSqsCjocI_WCVQ/hwhiaimodelzoo-mobilenetv1-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082701Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=E1B233C47BA93FEE1747A38739840277730B54FC0739D78D79277D72FF5D77BA)

 | 

864ef1d651e7f2cb9de69ce34d81e40783bdac47069b6db22aefb6f4ae17f24b

 | 

[Paper & implementation](https://arxiv.org/abs/1704.04861)

 |
| 

Mobilenet\_v2

 | 

2.49

 | 

1.18

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2/v3/ZSK31G6DQQCZdPN46ialkA/hwhiaimodelzoo-mobilenetv2-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082301Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=8C37AE09586B0DD74C079AE4C3E07E376F66015E4DED2CB1367F22869B92623E)

 | 

362c0169917122e45f4c5aed69ad3b9c8509b51a0531e6912360eff6c8b81cbc

 | 

[Paper & implementation](https://arxiv.org/abs/1801.04381)

 |
| 

Mobilenet\_v2\_1.4

 | 

3.16

 | 

1.67

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/2b/v3/b6CQs3z-TgyxhL2RmM99Gg/hwhiaimodelzoo-mobilenetv2v1p4-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082201Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=638FA2EBD56970A77CEA8ACE1075E6C43AC69890FE7DB3B9FB705E822C10BA15)

 | 

8f1a05a83e813fac16e958ad5436569fe83f75f88137819d52ce2e268ad04126

 | 

[Paper & implementation](https://arxiv.org/abs/1704.04861)

 |
| 

Mobilenet\_v3\_Large

 | 

3.29

 | 

2.33

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/c1/v3/1tgbS5yhSHCVSrT3EZMk8Q/hwhiaimodelzoo-mobilenetv3-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082402Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=991EF094DEC163F2A7E32FBAB61DC3DF6C1D26932357D76B452B725A73CF0B27)

 | 

086640ff192629b6dba33d905ddb0925d612e395703948c6c7221f2e4126b85d

 | 

[Paper & implementation](https://arxiv.org/abs/1905.02244)

 |
| 

Googlenet

 | 

34.69

 | 

1.64

 | 

[ONNX & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/7e/v3/XwBoZqjZSlGr8Qr90k3acA/hwhiaimodelzoo-googlenet-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082502Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=7F5D53B22154CDE1B350367A5A31EAF81780D49DFF0D6C8E070EAAF973958DAC)

 | 

97ef0325be2c3b8824a903abaeea943260d2f349da63d193168c96eff735ad0e

 | 

[Paper & implementation](https://arxiv.org/abs/1409.4842)

 |
| 

Squeezenet\_v1

 | 

2.13

 | 

1.24

 | 

[ONNX & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/22/v3/LsUOWWXqS-Cy7BhWCL6k7w/hwhiaimodelzoo-squeezenetv1-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T081800Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=7A8C3CE1BDD91367BB92DD6A6DDBC3D2F9CE5E1C2C716E4C5B9D687C96997F42)

 | 

e20be44bdaa30b9fa4a22ef876c1e7bd88db49b5d063992ef1595b34d3544997

 | 

[Paper & implementation](https://arxiv.org/abs/1602.07360)

 |
| 

Object detection

 | 

SSD\_mobilenetv2\_voc

 | 

5.02

 | 

2.84

 | 

[CAFFE & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/ee/v3/-DV4ExjOQv6dZPxNyX0UIg/hwhiaimodelzoo-mobilenetv2ssd-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082602Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=9E6FD16BC06F1EE732447C5CA9A0AAC2E559DF42593D22A517CEC6F94D990AB3)

 | 

1d273130a07a6f888f6df1088b478049da9a961a3dbeaca7bfa92e616f0f01e9

 | 

[Paper 1 & implementation 1](https://arxiv.org/abs/1801.04381), [paper 2 & implementation 2](https://arxiv.org/abs/1512.02325)

 |
| 

Yolo\_v5

 | 

4.74

 | 

4.33

 | 

[ONNX & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/b6/v3/XBnjg_e5TMyG31kCCbdp1Q/hwhiaimodelzoo-yolo-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T081602Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=F31AC615FBD3DE8001EB12B9F8D5718EE3BA0BE1DDECF60A51E6901D24EE8E71)

 | 

83a205d70fcd9b31c13530da0b8752a6976b125b02ac07091fd088f58cd5a80f

 | 

[Paper & implementation](https://arxiv.org/abs/1804.02767)

 |
| 

Semantic segmentation

 | 

FCN

 | 

131.23

 | 

62.76

 | 

[CAFFE & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/d8/v3/ZDtRfBLDR86G-UakQBtEPA/hwhiaimodelzoo-fcn-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082927Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=0974C70798D459DBFD9542D65C72FB8B9BD583C14F52837BFED5DABB405719EA)

 | 

0cd87a51c1ea978a68e9cd4790106e99d910f78d5e68ec06e2bdd637aae5a73c

 | 

[Paper & implementation](https://arxiv.org/abs/1605.06211)

 |
| 

DeepLab\_v3

 | 

17.40

 | 

13.87

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/11/v3/qUSCbzzPT82XhxA1bC4HAQ/hwhiaimodelzoo-deeplabv3-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T083100Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=230AD01AEDBE1916683B6BB35BDED9B363EB06276BDF98DA64B2C7EF9B6CC285)

 | 

381f830f6b0154bf086dbc5b15575465a34c1b3d233a6d27bc417077832697c7

 | 

[Paper & implementation](https://arxiv.org/abs/1706.05587)

 |
| 

Super resolution

 | 

VDSR

 | 

17.71

 | 

10.67

 | 

[CAFFE & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/c6/v3/u6c2DYcSQQGHp_-K5pLVIg/hwhiaimodelzoo-vdsr-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T081700Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=358520AA2A16D4C2D7CA6703692D2D1209BFDFC38414C55AF442F89F9ACA6896)

 | 

bf5a699ea55b2d2e42ac40884f2697d807b5b3f37e655ecb342e873c6ba6b844

 | 

[Paper & implementation](https://arxiv.org/abs/1511.04587)

 |
| 

FSRCNN

 | 

17.24

 | 

17.02

 | 

[TF & OM](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_package_901_9/3d/v3/K_eT1fFuQM6vi9zsRe2CDQ/hwhiaimodelzoo-fsr-100.520.020.011.zip?HW-CC-KV=V1&amp;HW-CC-Date=20230423T082800Z&amp;HW-CC-Expire=315360000&amp;HW-CC-Sign=794BA667B6CAC909B5E8EBD672D638C4160971C62FAB237535417E0849713A92)

 | 

03775c806d8d166fd29753ea8eaa3db377246fa469487b7e161a9e405a6ffa1c

 | 

[Paper & implementation](https://arxiv.org/abs/1608.00367)

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/12/v3/Y6NudbtdRZSCiCfLCiDw2A/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062123Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13A80E39E685C070579E64798758B0BE8A87843DDA29A5AFFD0ADC424AFD91A3)

-   \[1\] This performance data test is based on Huawei smartphones equipped with Kirin 9000 chips.
-   \[2\] The original model file is obtained by referring to the paper and model training in the implementation example.

In addition to the network model recommended in Model Zoo, you can also customize a network model. Performance-friendly operators and computing architectures are listed below.

#### CANN Operator Performance Guide

In terms of usability, the provided operator functions are not limited. This guide introduces how to maximize operator performance based on the operator implementation mode.

## NN Operators

| 
IR Operator

 | 

Performance and Guide

 | 

Recommendation Level

 |
| :-- | :-- | :-- |
| 

Activation

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

HardSwish

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

PRelu

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

BNInference

 | 

The current hardware performance is optimal.

When Conv (depthwise) and Bn are used together, image fusion is performed.

 | 

☆☆☆☆☆

 |
| 

Convolution

 | 

The performance is optimal when the values of **Cin** and **Cout** are multiples of 16.

 | 

☆☆☆☆☆

 |
| 

QuantizedConvolution

 | 

The performance is optimal when the values of **Cin** and **Cout** are multiples of 32.

 | 

☆☆☆☆☆

 |
| 

ConvTranspose

 | 

-   The performance is optimal when the values of **Cin** and **Cout** are multiples of 16.

-   The performance is optimal for kernel 1x1, 2x2, 3x3, and 8x8.

 | 

☆☆☆☆☆

 |
| 

BiasAdd

 | 

The current hardware performance is optimal.

When Conv (depthwise) and BiasAdd are used together, image fusion is performed.

 | 

☆☆☆☆☆

 |
| 

Eltwise

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

LRN

 | 

The current hardware performance is good.

-   The average variance is calculated, leading to a heavy computing workload. Therefore, the performance is worse than that of batchNorm.
-   Mainly used for image enhancement and is sensitive to precision calculation. If the NPU uses FP16 for calculation, there may be precision risks.

 | 

☆☆☆

 |
| 

ConvolutionDepthwise

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

QuantizedConvolutionDepthwise

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

FullyConnection

 | 

The performance is limited by the DDR bandwidth. The operator is not limited by the computing power. Set the weight properly during algorithm design.

 | 

☆☆☆☆☆

 |
| 

QuantizedFullyConnection

 | 

The performance is limited by the DDR bandwidth. The operator is not limited by the computing power. Set the weight properly during algorithm design.

 | 

☆☆☆☆☆

 |
| 

PoolingD

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Scale

 | 

The current hardware performance is optimal.

When Conv (depthwise) and Scale are used together, image fusion is performed.

 | 

☆☆☆☆☆

 |
| 

ShuffleChannel

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

ShuffleChannelV2

 | 

Used for supporting operators in ANNs. The function works, but the performance is poor.

 | 

☆

 |
| 

Softmax

 | 

The current hardware performance is optimal.

The performance is optimal for 4-dimensional input, when axis = 1, and softmax is implemented based on channel C.

 | 

☆☆☆☆☆

 |
| 

TopK

 | 

Used for supporting operators in ANNs. The function works, but the performance is poor.

 | 

☆

 |
| 

LogSoftmax

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Rank

 | 

Shape inference operator, which can be canceled during model compilation.

 | 

☆☆☆☆☆

 |
| 

ScatterNd

 | 

Irregular data migration. The performance is poor, and is not recommended for frequent use.

 | 

☆☆☆

 |
| 

LogicalXor

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Threshold

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

AxisAlignedBboxTransform

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Normalize

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

SVDF

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

ReduceMean

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

LayerNorm

 | 

The current hardware performance is optimal.

-   The average variance is calculated, leading to a heavy computing workload. Therefore, the performance is worse than that of batchNorm.
-   Mainly used for image enhancement and is sensitive to precision calculation. If the NPU uses FP16 for calculation, there may be precision risks.

 | 

☆☆☆

 |
| 

InstanceNorm

 | 

The current hardware performance is good.

-   The average variance is calculated, leading to a heavy computing workload. Therefore, the performance is worse than that of batchNorm.
-   Mainly used for image enhancement and is sensitive to precision calculation. If the NPU uses FP16 for calculation, there may be precision risks.

 | 

☆☆☆

 |
| 

PriorBox

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

LSTM

 | 

The current hardware performance is good, but the supported functions are limited.

 | 

☆☆☆☆

 |

## Math Operators

| 
IR Operator

 | 

Performance and Guide

 | 

Recommendation Level

 |
| :-- | :-- | :-- |
| 

Add

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Mul

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Expm1

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Ceil

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Sin

 | 

The function works, but the performance is poor.

 | 

☆

 |
| 

Cos

 | 

The function works, but the performance is poor.

 | 

☆

 |
| 

Floor

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Log1p

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

LogicalAnd

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

LogicalNot

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Maximum

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

Minimum

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

Equal

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Reciprocal

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Sqrt

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Square

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

CastT

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

Sign

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Exp

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

FloorMod

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

GreaterEqual

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Greater

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Less

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

MatMul

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

RealDiv

 | 

The performance is poor. It is recommended that you use mul or Reciprocal+mul.

 | 

☆

 |
| 

Rint

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

Round

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

Rsqrt

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

Sub

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Range

 | 

The performance is optimal during model compilation.

 | 

☆☆☆☆☆

 |
| 

Acos

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Asin

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Log

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

LogicalOr

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Neg

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

ReduceProdD

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

ReduceSum

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Tan

 | 

The function works, but the performance is poor.

 | 

☆

 |
| 

Power

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Pow

 | 

The function works, but the performance is poor.

 | 

☆

 |
| 

ArgMaxExt2

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆

 |
| 

FloorDiv

 | 

The performance is poor. Not recommended.

 | 

☆

 |
| 

NotEqual

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

LessEqual

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

SquaredDifference

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Atan

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

BatchMatMul

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

ClipByValue

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

L2Normalize

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

ReduceMax

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |
| 

ReduceMin

 | 

The performance is better on phones using Kirin 9000 chips. On phones using other chips, the function can merely work, without optimizing the performance.

 | 

☆

 |

## Array Operators

| 
IR Operator

 | 

Performance and Guide

 | 

Recommendation Level

 |
| :-- | :-- | :-- |
| 

ConcatD

 | 

The current hardware performance is optimal.

When **Cin** and **Cout** are both multiples of 16, image fusion is performed to achieve the optimal performance.

 | 

☆☆☆☆☆

 |
| 

FakeQuantWithMinMaxVars

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Reshape

 | 

The current hardware performance is optimal.

In some scenarios, operators are fused and canceled.

 | 

☆☆☆☆☆

 |
| 

SplitD

 | 

The current hardware performance is optimal.

When **Cin** and **Cout** are both multiples of 16, image fusion is performed to achieve the optimal performance.

 | 

☆☆☆☆☆

 |
| 

SplitV

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

Unpack

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

Flatten

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

Slice

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

ExpandDims

 | 

Shape inference operator, which can be canceled during model compilation.

 | 

☆☆☆☆☆

 |
| 

GatherV2D

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

GatherNd

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

Pack

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

SpaceToDepth

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

DepthToSpace

 | 

The performance is poor in most cases due to out-of-order data rearrangement.

The performance is specially optimized and better in the four-grid scenario (**Cin** = **4**, **block** = **1**).

 | 

☆☆

 |
| 

StridedSlice

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

SpaceToBatchND

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

BatchToSpaceND

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

Tile

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

Size

 | 

Shape inference operator, which can be canceled during model compilation.

 | 

☆☆☆☆☆

 |
| 

Fill

 | 

The performance is poor due to out-of-order data rearrangement.

 | 

☆

 |
| 

Select

 | 

The function can merely work.

 | 

☆☆

 |
| 

PadV2

 | 

The performance is good in the scenario where zeros are padded in the height and width directions.

The performance is poor in other scenarios due to out-of-order data rearrangement.

 | 

☆☆☆

 |
| 

Squeeze

 | 

Shape inference operator, which can be canceled during model compilation.

 | 

☆☆☆☆☆

 |
| 

Pad

 | 

The performance is good in the scenario where zeros are padded in the height and width directions.

The performance is poor in other scenarios due to out-of-order data rearrangement.

 | 

☆☆☆

 |
| 

MirrorPad

 | 

The performance is poor in other scenarios due to out-of-order data rearrangement.

 | 

☆

 |
| 

OneHot

 | 

The performance is poor in other scenarios due to out-of-order data rearrangement.

 | 

☆

 |
| 

Shape

 | 

Shape inference operator, which can be canceled during model compilation.

 | 

☆☆☆☆☆

 |
| 

Dequantize

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

Quantize

 | 

The current hardware performance is optimal.

 | 

☆☆☆☆☆

 |

## Detection Operators

| 
IR Operator

 | 

Performance and Guide

 | 

Recommendation Level

 |
| :-- | :-- | :-- |
| 

Permute

 | 

The hardware is not suitable for too many such operations due to out-of-order data rearrangement, although related optimizations have been made.

 | 

☆☆☆

 |
| 

SSDDetectionOutput

 | 

The current performance is optimal.

 | 

☆☆☆☆☆

 |

## Image Operators

| 
IR Operator

 | 

Performance and Guide

 | 

Recommendation Level

 |
| :-- | :-- | :-- |
| 

ImageData

DynamicImageData

ImageCrop

ImageChannelSwap

ImageColorSpaceConvertion

ImageResize

ImageDataTypeConversion

ImagePadding

 | 

Operators related to AIPP image processing. The hardware performance is optimal.

 | 

☆☆☆☆☆

 |
| 

CropAndResize

 | 

The function works, but the performance is poor.

 | 

☆

 |
| 

ResizeBilinear

ResizeBilinearV2

Interp

 | 

The hardware performance is optimal in most scenarios, but needs to be optimized in a few scenarios.

 | 

☆☆☆☆☆

 |
| 

ResizeNearestNeighbor

Upsample

 | 

The hardware performance is optimal in most scenarios, but needs to be optimized in a few scenarios.

 | 

☆☆☆☆☆

 |
| 

Crop

 | 

The function works, but the performance is poor.

 | 

☆

 |
| 

NonMaxSuppressionV3D

 | 

The function works, but the performance is poor.

 | 

☆

 |

#### Performance-Friendly Computing Structure

| 
Application Scenario

 | 

Network Type

 | 

Recommendation Level

 | 

Recommendation Description

 |
| :-- | :-- | :-- | :-- |
| 

Classification network

 | 

AlexNet

 | 

☆☆☆☆

 | 

The weight of the full-connection layer is large, and the bandwidth is limited during inference. You can download the model from [Model Zoo](#section175551381682).

 |
| 

VGG16

 | 

☆☆☆☆

 | 

The weight of the full-connection layer is large, and the bandwidth is limited during inference. You can download the model from [Model Zoo](#section175551381682).

 |
| 

VGG19

 | 

☆☆☆

 | 

The weight of the full-connection layer is large, and the bandwidth is limited during inference. You can download the model from [Model Zoo](#section175551381682).

 |
| 

ResNet18/34/50/101/152

 | 

☆☆☆☆☆

 | 

The weight of the model is moderate, and the hardware computing power usage is close to 100%. You can download ResNet50 from [Model Zoo](#section175551381682).

 |
| 

GoogleNet

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 75%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

InceptionV3

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 85%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

InceptionV4

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 85%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

Inception\_Resnet\_v2

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 90%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

Xception

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 85%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

MobileNet\_v1

 | 

☆☆☆☆☆

 | 

The weight of the model is moderate, and the hardware computing power usage is close to 95%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

MobileNet\_v2

 | 

☆☆☆☆☆

 | 

The weight of the model is moderate, and the hardware computing power usage is close to 95%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

MobileNet\_v3

 | 

☆☆☆☆☆

 | 

The weight of the model is moderate, and the hardware computing power usage is close to 95%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

SqueezeNet

 | 

☆☆☆☆☆

 | 

The weight of the model is moderate, and the hardware computing power usage is close to 95%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

DenseNet

 | 

☆☆☆☆☆

 | 

The weight of the model is moderate, and the hardware computing power usage is close to 95%.

 |
| 

ShuffleNet\_v1

ShuffleNet\_v2

 | 

☆

 | 

A large number of shuffleChannel operations are involved. The model transfers data between memories and is not computing-limited.

The bandwidth of the network is limited. The shuffleChannel supports the function but does not ensure the optimal performance.

 |
| 

Resnext

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 85%.

 |
| 

EfficientNet

 | 

☆☆☆☆☆

 | 

The weight of the model is moderate, and the hardware computing power usage is close to 95%.

 |
| 

SENet

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 75%.

 |
| 

Object detection

 | 

Faster\_RCNN

 | 

☆☆☆☆☆

 | 

The hardware computing power usage is close to 85%.

 |
| 

SSD

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 85%. Can be generated only through the OMG process.

 |
| 

FPN

 | 

☆☆☆☆☆

 | 

The hardware computing power usage is close to 90%. The post-processing is not included in the model, but is implemented by the algorithm independently.

 |
| 

Semantic segmentation

 | 

FCN

 | 

☆☆☆☆☆

 | 

The hardware computing power usage is close to 85%. As the model's computing workload is heavy, parameters need to be tailored during actual deployment. You can download the model from [Model Zoo](#section175551381682).

 |
| 

DeepLabV3

 | 

☆☆☆

 | 

The hardware computing power usage is close to 60%. You can download the model from [Model Zoo](#section175551381682).

 |
| 

Unet

 | 

☆☆☆

 | 

The hardware computing power usage is close to 60%.

 |
| 

MaskRcnn

 | 

☆☆

 | 

The hardware computing power usage is close to 80% (only for the TF-to-OM version, not supported in IR interconnection mode).

 |
| 

PSPNet

 | 

☆☆☆

 | 

The pyramid pooling operators are not supported. The model is equivalent to multiple pools, but the performance is average.

 |
| 

Super resolution

 | 

VDSR

 | 

☆☆☆☆☆

 | 

The hardware computing power usage is close to 85%. The model meets the real-time super-resolution requirements, and can be downloaded from [Model Zoo](#section175551381682).

 |
| 

FSRCNN

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 70%. The model meets partial real-time super-resolution requirements, and can be downloaded from [Model Zoo](#section175551381682).

 |
| 

SRCNN

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 70%. The model meets partial real-time super-resolution requirements.

 |
| 

DnCNN

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 65%. Due to heavy computing workload, only partial real-time super-resolution requirements can be met.

 |
| 

DRCN

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 65%. Due to heavy computing workload, only partial real-time super-resolution requirements can be met.

 |
| 

DRRN

 | 

☆☆☆

 | 

The hardware computing power usage is close to 60%. Due to large computing volume, only partial real-time super-resolution requirements can be met.

 |
| 

EnhanceNet

 | 

☆☆☆

 | 

The hardware computing power usage is close to 60%. Due to large computing volume, only partial real-time super-resolution requirements can be met.

 |
| 

Speech and semantics

 | 

RNN

 | 

☆☆

 | 

Only a few functions are supported.

 |
| 

LSTM

 | 

☆☆

 | 

Only a few functions are supported.

 |
| 

Transformer

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 70%.

 |
| 

Bert

 | 

☆☆☆☆

 | 

The hardware computing power usage is close to 70%.

 |
