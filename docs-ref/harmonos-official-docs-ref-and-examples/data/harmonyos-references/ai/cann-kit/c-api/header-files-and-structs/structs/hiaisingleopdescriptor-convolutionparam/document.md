# HiAISingleOpDescriptor\_ConvolutionParam

#### Overview

HMS\_HiAISingleOpDescriptor\_CreateConvolution input parameters.

**Since:** 5.0.0(12)

**Related Modules:**[CANN](../../../modules/cann/document.md)

#### Summary

#### \[h2\]Data Fields

| 
Name

 | 

Description

 |
| :-- | :-- |
| 

[HiAI\_SingleOpConvMode](../../../modules/cann/document.md#hiai_singleopconvmode)[convMode](#convmode)

 | 

Convolution mode.

 |
| 

int64\_t [strides](#strides) \[2\]

 | 

Strides of the convolution kernel in terms of height and width. It is an int array \[strideHeight, strideWidth\] with length of 2.

 |
| 

int64\_t [dilations](#dilations) \[2\]

 | 

Dilation rates of the convolution kernel in terms of height and width. It is an int array \[dilationHeight, dilationWidth\] with length of 2.

 |
| 

int64\_t [pads](#pads) \[4\]

 | 

Padding length of the begin and end of each axis. It is an int array \[h\_begin, h\_end, w\_begin, w\_end\] with length of 4. The value is valid only when **padMode** is set to **HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC**.

 |
| 

int64\_t [groups](#groups)

 | 

Number of groups into which the input channels is divided. If **convMode** is set to **HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE**, **groups** does not take effect.

 |
| 

[HiAI\_SingleOpPadMode](../../../modules/cann/document.md#hiai_singleoppadmode)[padMode](#padmode)

 | 

Input padding mode. For **HIAI\_SINGLEOP\_CONV\_MODE\_COMMON** and **HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE**, the value can be **0** (SPECIFIC), **1** (SAME), **2** (SAME\_UPPER), **3** (SAME\_LOWER), or **4** (VALID). For **HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED**, the value can be **0** (SPECIFIC), **1** (SAME), or **4** (VALID).

 |

#### Field

#### \[h2\]convMode

HiAI\_SingleOpConvMode HiAISingleOpDescriptor\_ConvolutionParam::convMode

**Description**

Convolution mode.

#### \[h2\]dilations

int64\_t HiAISingleOpDescriptor\_ConvolutionParam::dilations\[2\]

**Description**

Dilation rates of the convolution kernel in terms of height and width. It is an int array \[dilationHeight, dilationWidth\] with length of 2.

#### \[h2\]groups

int64\_t HiAISingleOpDescriptor\_ConvolutionParam::groups

**Description**

Number of groups into which the input channels is divided. If **convMode** is set to **HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE**, **groups** does not take effect.

#### \[h2\]padMode

HiAI\_SingleOpPadMode HiAISingleOpDescriptor\_ConvolutionParam::padMode

**Description**

Input padding mode. For **HIAI\_SINGLEOP\_CONV\_MODE\_COMMON** and **HIAI\_SINGLEOP\_CONV\_MODE\_DEPTHWISE**, the value can be **0** (SPECIFIC), **1** (SAME), **2** (SAME\_UPPER), **3** (SAME\_LOWER), or **4** (VALID). For **HIAI\_SINGLEOP\_CONV\_MODE\_TRANSPOSED**, the value can be **0** (SPECIFIC), **1** (SAME), or **4** (VALID).

#### \[h2\]pads

int64\_t HiAISingleOpDescriptor\_ConvolutionParam::pads\[4\]

**Description**

Padding length of the begin and end of each axis. It is an int array \[h\_begin, h\_end, w\_begin, w\_end\] with length of 4. The value is valid only when **padMode** is set to **HIAI\_SINGLEOP\_PAD\_MODE\_SPECIFIC**.

#### \[h2\]strides

int64\_t HiAISingleOpDescriptor\_ConvolutionParam::strides\[2\]

**Description**

Strides of the convolution kernel in terms of height and width. It is an int array \[strideHeight, strideWidth\] with length of 2.
