# Model Benefits

#### Benefits of Quant\_INT8-8

Take ResNet-18 as an example. Using the size reduction tool (Quant\_INT8-8) can yield the following benefits.

| 
Framework

 | 

Dataset

 | 

Model

 | 

Original Precision

 | 

Precision After Retraining

 | 

Non-quantitative OM Offline

Model Size (MB)

 | 

Quant\_INT8-8 Quantized OM

Offline Model Size (MB)

 |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| 

TensorFlow

 | 

ImageNet

 | 

resnet-18(v2)

 | 

70.0%

 | 

70.0%

 | 

22.457

 | 

11.9

 |

#### Benefits of Classification Networks in NAS Mode

Take ResNet-18 as an example. Using the size reduction tool (NAS mode) can yield the following benefits.

| 
Framework

 | 

Dataset

 | 

Model

 | 

Parameter Count (MB)

 | 

Precision

 |
| :-- | :-- | :-- | :-- | :-- |
| 

TensorFlow

 | 

ImageNet

 | 

ResNet-18

 | 

11.69

 | 

70.32%

 |
| 

NASEA

 | 

10.93

 | 

72.13%\[1\]

 |
| 

PyTorch

 | 

ImageNet

 | 

ResNet-18

 | 

11.69

 | 

69.6%

 |
| 

NASEA

 | 

11.4

 | 

72.88%

 |

## Benefits of Detection Networks

| 
Framework

 | 

Dataset

 | 

Model

 | 

Computation Workload (GB)

 | 

mAP@\[.5, .95\]\[2\]

 |
| :-- | :-- | :-- | :-- | :-- |
| 

SSD (backbone: ResNet-18)

 | 

COCO

 | 

ResNet-18

 | 

11.6

 | 

17.8\[3\]

 |
| 

NASEA

 | 

9.25

 | 

18.4\[3\]

 |

## Benefits of Segmentation Networks

| 
Framework

 | 

Dataset

 | 

Model

 | 

Computation Workload (GB)

 | 

mIOU\[4\]

 |
| :-- | :-- | :-- | :-- | :-- |
| 

TensorFlow

 | 

VOC

 | 

ResNet-18 + Deeplab v3

 | 

40.9

 | 

54.1\[5\]

 |
| 

NASEA

 | 

28.3

 | 

56.1\[5\]

 |
| 

PyTorch

 | 

VOC

 | 

ResNet-18 + Deeplab v3

 | 

43.7

 | 

64.2

 |
| 

NASEA

 | 

30.7

 | 

65.1

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/83/v3/39tFJNaBQ0aSmK74IYaHDg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=8C73663CDD8DC710A449CBE4717585D6B52553116E5ECD722F479108264D157A)

\[1\] The precision is obtained by using the Tensorpack retraining model.

\[2\] The indicator is calculated as follows: obtain the APs for IoU from 0.5 to 0.95 with a step of 0.05, and then calculate the average of all APs.

\[3\] The precision is obtained by tests based on the COCO val2017 dataset.

\[4\] This indicator indicates the Mean Intersection over Union (MIoU). The IoU of each category is calculated first, and then the average value is calculated.

\[5\] The precision is obtained by tests based on the VOC val2012 dataset.
