# OH\_NN\_QuantParam

#### Overview

Defines the quantization information.

In quantization scenarios, the 32-bit floating-point data type is quantized into the fixed-point data type according to the following formula:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/0/v3/pGnML3W9Q0q5Ws8iFT2h4A/en-us_image_0000002537926384.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062524Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=82D4DDF3C12EFA75F9A1ED170B2786F505A261F2FD4F3C590AD26C8109C2E593)

where, **s** and **z** are quantization parameters, which are stored by **scale** and **zeroPoint** in OH\_NN\_QuanParam. **r** is a floating point number, **q** is the quantization result, **q\_min** is the lower bound of the quantization result, and **q\_max** is the upper bound of the quantization result. The calculation method is as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/8c/v3/-ER3BNhZSkqQFFpNZaCi_Q/en-us_image_0000002568686161.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062524Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=6AC29C206F841A2BE9F2C8D18CF31EEEC92A9F1521FCBFDFBEDEBF95CBC667CF)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/29/v3/vckgEwwXQuCRB-PxL0pm1w/en-us_image_0000002568766171.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062524Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=CFC8FF63AB8F4C3FB80FCD8BA8EE069A16468813E88841D858AD09F78D4B60D2)

The **clamp** function is defined as follows:

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1e/v3/c87ksXuKTUa47b70_fT1Yw/en-us_image_0000002537766446.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062524Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=04A5CC9F80223DB1DEAB3BD9B6C566C68053811C9156C1222982C36D922628EF)

**Since**: 9

**Deprecated from**: 11

**Substitute**: [NN\_QuantParam](../nn-quantparam/document.md)

**Related module**: [NeuralNetworkRuntime](../../modules/neuralnetworkruntime/document.md)

**Header file**: [neural\_network\_runtime\_type.h](../../header-files/neural-network-runtime-type-h/document.md)

#### Summary

#### \[h2\]Member Variables

| Name | Description |
| :-- | :-- |
| uint32\_t quantCount | Length of the numBits, scale, and zeroPoint arrays. In the per-layer quantization scenario, **quantCount** is usually set to **1**. That is, all channels of a tensor share a set of quantization parameters. In the per-channel quantization scenario, **quantCount** is usually the same as the number of tensor channels, and each channel uses its own quantization parameters. |
| const uint32\_t \*numBits | Number of quantization bits. |
| const double \*scale | Pointer to the scale data in the quantization formula. |
| const int32\_t \*zeroPoint | Pointer to the zero point data in the quantization formula. |
