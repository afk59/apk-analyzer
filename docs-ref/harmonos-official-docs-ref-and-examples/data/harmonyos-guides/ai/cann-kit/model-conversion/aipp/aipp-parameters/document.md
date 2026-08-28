# AIPP Parameters

Static AIPP and dynamic AIPP modes are supported, which are mutually exclusive. Static AIPP models cannot receive AIPP parameters passed during model inference, and are not compatible with dynamic AIPP scenarios. The following table describes the differences between the two AIPP modes.

| 
AIPP

 | 

How to Set AIPP Parameters

 | 

Advantages

 |
| :-- | :-- | :-- |
| 

Static AIPP

 | 

Pre-defined through the configuration file or IR graph construction during model generation.

 | 

More efficient: AIPP initialization can be completed in the model loading phase.

 |
| 

Dynamic AIPP

 | 

The model is only marked with support for AIPP.

 | 

More flexible: Different sets of AIPP parameters can be passed for each inference.

 |

#### Supported AIPP Input Formats

AIPP supports the following image formats:

-   YUV420SP\_U8
-   XRGB8888\_U8
-   ARGB8888\_U8
-   YUYV\_U8
-   YUV422SP\_U8
-   AYUV444\_U8
-   YUV400\_U8
-   RGB888\_U8

The suffix **U8** represents the UINT8 pixel type. The value range is 0–255. When YUV images are input, AIPP pads the image data to the YUV444 format regardless of whether the input format is YUV420, YUV422, or YUYV.

In addition to the preceding image types, AIPP can support more image input formats when channel swapping is enabled.

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/94/v3/K_ZMDsITRwWkVWDEuIs5eg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=770B6D1A7DF5F8082B0074C585BDDD4246714B2BB80B5588A0579069B7283ED5)

-   YUYV\_U8 and AYUV444\_U8 are not supported in the current version.

#### AIPP Functions

The following AIPP functions are supported, listed in the processing sequence of the chip:

-   [Image cropping](#section197711329191913)
-   [Channel swapping](#section8293174872013)
-   [Color space conversion (CSC)](#section89862027112118)
-   [Image resizing](#section4757633132210)
-   [Data type conversion (DTC)](#section12331181152317)
-   [Image rotation](#section127618563124)
-   [Image padding](#section03997455233)

## Cropping

Image cropping in AIPP applies only to input images. The involved parameters are described as follows.

| 
**Name**

 | 

**Description**

 | 

**Value Range**

 |
| :-- | :-- | :-- |
| 

switch

 | 

Cropping switch.

 | 

false/true

 |
| 

load\_start\_pos\_w

 | 

Horizontal coordinate of the cropping start position.

 | 

load\_start\_pos\_w < src\_image\_size\_w

 |
| 

load\_start\_pos\_h

 | 

Vertical coordinate of the cropping start position.

 | 

load\_start\_pos\_h < src\_image\_size\_h

 |
| 

crop\_size\_w

 | 

Width of the cropped out image.

 | 

load\_start\_pos\_w + crop\_size\_w <= src\_image\_size\_w

 |
| 

crop\_size\_h

 | 

Height of the cropped out image.

 | 

load\_start\_pos\_h + crop\_size\_h <= src\_image\_size\_h

 |

For YUV420SP, YUYV, YUV422SP, or AYUV444 image input, the coordinates of the cropping start position and the width and height of the cropped out image must be even numbers. Parameter check will be performed accordingly.

## Channel Swapping

AIPP supports RB/UV channel swapping and AX channel swapping.

RB/UV channel swapping greatly enriches the input image formats. Once RB/UV channel swapping is enabled, input image formats supported by AIPP are double of the configured input formats.

| 
**Configured Format**

 | 

**Image Format**

 |
| :-- | :-- |
| 

YUV420SP\_U8

 | 

YUV420, YVU420 + rbuv\_swap\_switch

 |
| 

XRGB8888\_U8

 | 

XRGB, XBGR + rbuv\_swap\_switch

 |
| 

ARGB8888\_U8

 | 

ARGB, ABGR + rbuv\_swap\_switch

 |
| 

RGB888\_U8

 | 

BGR + rbuv\_swap\_switch

 |
| 

YUYV\_U8

 | 

YUYV, YVYU + rbuv\_swap\_switch

 |
| 

YUV422SP\_U8

 | 

YUV422, YVU422 + rbuv\_swap\_switch

 |
| 

AYUV444\_U8

 | 

AYUV + rbuv\_swap\_switch

 |

AX channel swapping applies to XRGB, ARGB, and AYUV image inputs. Channel swapping moves inputs of the first channel to the fourth channel. That is, with AX channel swapping enabled, XRGB, ARGB, and AYUV data is respectively converted to RGBX, RGBA, and YUVA data.

When the model training set consists of RGB images and the image input for inference is in XRGB or ARGB format, you can enable AX channel swapping to move the RGB channels forward for compatibility.

## Color Space Conversion

Color Space Conversion (CSC) refers to the conversion between the YUV444 and RGB888 image formats. The involved parameters are described as follows.

| 
**Name**

 | 

**Description**

 | 

**Type**

 | 

**Value Range**

 |
| :-- | :-- | :-- | :-- |
| 

csc\_switch

 | 

CSC switch.

 | 

bool

 | 

true/false

 |
| 

matrix\_r0c0

matrix\_r0c1

matrix\_r0c2

matrix\_r1c0

matrix\_r1c1

matrix\_r1c2

matrix\_r2c0

matrix\_r2c1

matrix\_r2c2

 | 

CSC matrix elements.

 | 

int16

 | 

\[-32677, 32676\]

 |
| 

output\_bias\_0

output\_bias\_1

output\_bias\_2

 | 

Output biases for RGB2YUV conversion.

 | 

uint8

 | 

\[0, 255\]

 |
| 

input\_bias\_0

input\_bias\_1

input\_bias\_2

 | 

Input biases for YUV2RGB conversion.

 | 

uint8

 | 

\[0, 255\]

 |

Reference 1: YUV and BGR conversion formulas

-   YUV2BGR:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/9e/v3/HtcduauCSJyS94uIQ_Tj4g/en-us_formulaimage_0000002528408555.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9F32F661AFB4578281CEEC72DEBCFC58A9798B0EAAF85B546CCFB103987A24AD "Click to enlarge")
    

-   BGR2YUV:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/d6/v3/jDxBV1s0RlikcLmO8mHX3A/en-us_formulaimage_0000002496568546.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9710B0D789B4459F90C0038593C5A8E14CDF4168FF297BEC77BE797D409FC090 "Click to enlarge")
    

Reference 2: BT-601NARROW, JPEG, and BT-709NARROW conversion formulas

-   BT-601 narrow
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/1d/v3/UF7q348eSXGtz5zBsHNQ0g/en-us_formulaimage_0000002496888562.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=31BFA32FDCDB3C7A67C5C7A70C48472FA6D935ABC36D82D35E7E4A4292D93D22 "Click to enlarge")
    
-   JPEG
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/25/v3/KYSQYNrvQcG3c6ppBX52UQ/en-us_formulaimage_0000002528408547.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E2DE66CC55E728CD199514A0728A938C4EA88EDE1F6B8824B938707461BB8AF0 "Click to enlarge")
    
-   BT-709 narrow
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3f/v3/KBzhdt5-ShuIzvJQofb7gA/en-us_formulaimage_0000002528648533.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=775CB9609E0BE2EAFB274A44EC46BD7D1568B53988D38AAB63EA8E2F5EDC22D9 "Click to enlarge")
    

To use the configuration file to generate a model with static AIPP, configure the CSC matrix and the value of **input\_bias** or **output\_bias** based on the preceding formulas. To define the AIPP CSC operator in IR mode, or configure the CSC parameters using CANN Kit APIs, pass the target type. The system will fill in the CSC configuration parameters accordingly.

The following describes how to configure the CSC for JPEG and BT-601NARROW images:

-   YUV input (YUV420/YUYV/YUV422SP/AYUV444) and RGB model training set (conversion from YUV400 to RGB not supported)
    
    | 
    JPEG
    
     | 
    
    BT-601NARROW
    
     | 
    
    BT-601FULL
    
     | 
    
    BT-709NARROW
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    matrix\_r0c0 : 256
    
    matrix\_r0c1 : 0
    
    matrix\_r0c2 : 359
    
    matrix\_r1c0 : 256
    
    matrix\_r1c1 : -88
    
    matrix\_r1c2 : -183
    
    matrix\_r2c0 : 256
    
    matrix\_r2c1 : 454
    
    matrix\_r2c2 : 0
    
    input\_bias\_0 : 0
    
    input\_bias\_1 : 128
    
    input\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 298
    
    matrix\_r0c1 : 0
    
    matrix\_r0c2 : 409
    
    matrix\_r1c0 : 298
    
    matrix\_r1c1 : -100
    
    matrix\_r1c2 : -208
    
    matrix\_r2c0 : 298
    
    matrix\_r2c1 : 516
    
    matrix\_r2c2 : 0
    
    input\_bias\_0 : 16
    
    input\_bias\_1 : 128
    
    input\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 256
    
    matrix\_r0c1 : 0
    
    matrix\_r0c2 : 359
    
    matrix\_r1c0 : 256
    
    matrix\_r1c1 : -88
    
    matrix\_r1c2 : -183
    
    matrix\_r2c0 : 256
    
    matrix\_r2c1 : 454
    
    matrix\_r2c2 : 0
    
    input\_bias\_0 : 0
    
    input\_bias\_1 : 128
    
    input\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 298
    
    matrix\_r0c1 : 0
    
    matrix\_r0c2 : 460
    
    matrix\_r1c0 : 298
    
    matrix\_r1c1 : -55
    
    matrix\_r1c2 : -137
    
    matrix\_r2c0 : 298
    
    matrix\_r2c1 : 541
    
    matrix\_r2c2 : 0
    
    input\_bias\_0 : 16
    
    input\_bias\_1 : 128
    
    input\_bias\_2 : 128
    
     |
    
-   YUV input (YUV420/YUYV/YUV422SP/AYUV444) and BGR model training set (conversion from YUV400 to BGR not supported)
    
    | 
    JPEG
    
     | 
    
    BT-601NARROW
    
     | 
    
    BT-601FULL
    
     | 
    
    BT-709NARROW
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    matrix\_r0c0 : 256
    
    matrix\_r0c1 : 454
    
    matrix\_r0c2 : 0
    
    matrix\_r1c0 : 256
    
    matrix\_r1c1 : -88
    
    matrix\_r1c2 : -183
    
    matrix\_r2c0 : 256
    
    matrix\_r2c1 : 0
    
    matrix\_r2c2 : 359
    
    input\_bias\_0 : 0
    
    input\_bias\_1 : 128
    
    input\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 298
    
    matrix\_r0c1 : 516
    
    matrix\_r0c2 : 0
    
    matrix\_r1c0 : 298
    
    matrix\_r1c1 : -100
    
    matrix\_r1c2 : -208
    
    matrix\_r2c0 : 298
    
    matrix\_r2c1 : 0
    
    matrix\_r2c2 : 409
    
    input\_bias\_0 : 16
    
    input\_bias\_1 : 128
    
    input\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 256
    
    matrix\_r0c1 : 454
    
    matrix\_r0c2 : 0
    
    matrix\_r1c0 : 256
    
    matrix\_r1c1 : -88
    
    matrix\_r1c2 : -183
    
    matrix\_r2c0 : 256
    
    matrix\_r2c1 : 0
    
    matrix\_r2c2 : 359
    
    input\_bias\_0 : 0
    
    input\_bias\_1 : 128
    
    input\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 298
    
    matrix\_r0c1 : 541
    
    matrix\_r0c2 : 0
    
    matrix\_r1c0 : 298
    
    matrix\_r1c1 : -55
    
    matrix\_r1c2 : -137
    
    matrix\_r2c0 : 298
    
    matrix\_r2c1 : 0
    
    matrix\_r2c2 : 460
    
    input\_bias\_0 : 16
    
    input\_bias\_1 : 128
    
    input\_bias\_2 : 128
    
     |
    
-   YUV input (YUV420/YUYV/YUV422SP/AYUV444) and grayscale (YUV400\_U8) model training set
    
    <table><tbody><tr><td class="cellrowborder" valign="top" width="100%"><p>matrix_r0c0 : 256</p><p>matrix_r0c1 : 0</p><p>matrix_r0c2 : 0</p><p>matrix_r1c0 : 0</p><p>matrix_r1c1 : 0</p><p>matrix_r1c2 : 0</p><p>matrix_r2c0 : 0</p><p>matrix_r2c1 : 0</p><p>matrix_r2c2 : 0</p></td></tr></tbody></table>
    
-   RGB input (XRGB8888/ARGB8888) and grayscale (YUV400\_U8) model training set
    
    <table><tbody><tr><td class="cellrowborder" valign="top" width="100%"><p>matrix_r0c0 : 76</p><p>matrix_r0c1 : 150</p><p>matrix_r0c2 : 30</p><p>matrix_r1c0 : 0</p><p>matrix_r1c1 : 0</p><p>matrix_r1c2 : 0</p><p>matrix_r2c0 : 0</p><p>matrix_r2c1 : 0</p><p>matrix_r2c2 : 0</p></td></tr></tbody></table>
    
-   RGB input (XRGB8888/ARGB8888) and YUV444SP model training set
    
    | 
    JPEG
    
     | 
    
    BT-601NARROW
    
     | 
    
    BT-601FULL
    
     | 
    
    BT-709NARROW
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    matrix\_r0c0 : 77
    
    matrix\_r0c1 : 150
    
    matrix\_r0c2 : 29
    
    matrix\_r1c0 : -43
    
    matrix\_r1c1 : -85
    
    matrix\_r1c2 : 128
    
    matrix\_r2c0 : 128
    
    matrix\_r2c1 : -107
    
    matrix\_r2c2 : -21
    
    output\_bias\_0 : 0
    
    output\_bias\_1 : 128
    
    output\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 66
    
    matrix\_r0c1 : 129
    
    matrix\_r0c2 : 25
    
    matrix\_r1c0 : -38
    
    matrix\_r1c1 : -74
    
    matrix\_r1c2 : 112
    
    matrix\_r2c0 : 112
    
    matrix\_r2c1 : -94
    
    matrix\_r2c2 : -18
    
    output\_bias\_0 : 16
    
    output\_bias\_1 : 128
    
    output\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 77
    
    matrix\_r0c1 : 150
    
    matrix\_r0c2 : 29
    
    matrix\_r1c0 : -43
    
    matrix\_r1c1 : -85
    
    matrix\_r1c2 : 128
    
    matrix\_r2c0 : 128
    
    matrix\_r2c1 : -107
    
    matrix\_r2c2 : -21
    
    output\_bias\_0 : 0
    
    output\_bias\_1 : 128
    
    output\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 47
    
    matrix\_r0c1 : 157
    
    matrix\_r0c2 : 16
    
    matrix\_r1c0 : -26
    
    matrix\_r1c1 : -87
    
    matrix\_r1c2 : 112
    
    matrix\_r2c0 : 112
    
    matrix\_r2c1 : -102
    
    matrix\_r2c2 : -10
    
    output\_bias\_0 : 16
    
    output\_bias\_1 : 128
    
    output\_bias\_2 : 128
    
     |
    
-   RGB input (XRGB8888/ARGB8888) and YVU444SP model training set
    
    | 
    JPEG
    
     | 
    
    BT-601NARROW
    
     | 
    
    BT-601FULL
    
     | 
    
    BT-709NARROW
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    matrix\_r0c0 : 77
    
    matrix\_r0c1 : 150
    
    matrix\_r0c2 : 29
    
    matrix\_r1c0 : 128
    
    matrix\_r1c1 : -107
    
    matrix\_r1c2 : -21
    
    matrix\_r2c0 : -43
    
    matrix\_r2c1 : -85
    
    matrix\_r2c2 : 128
    
    output\_bias\_0 : 0
    
    output\_bias\_1 : 128
    
    output\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 66
    
    matrix\_r0c1 : 129
    
    matrix\_r0c2 : 25
    
    matrix\_r1c0 : 112
    
    matrix\_r1c1 : -94
    
    matrix\_r1c2 : -18
    
    matrix\_r2c0 : -38
    
    matrix\_r2c1 : -74
    
    matrix\_r2c2 : 112
    
    output\_bias\_0 : 16
    
    output\_bias\_1 : 128
    
    output\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 77
    
    matrix\_r0c1 : 150
    
    matrix\_r0c2 : 29
    
    matrix\_r1c0 : 128
    
    matrix\_r1c1 : -107
    
    matrix\_r1c2 : -21
    
    matrix\_r2c0 : -43
    
    matrix\_r2c1 : -85
    
    matrix\_r2c2 : 128
    
    output\_bias\_0 : 0
    
    output\_bias\_1 : 128
    
    output\_bias\_2 : 128
    
     | 
    
    matrix\_r0c0 : 47
    
    matrix\_r0c1 : 157
    
    matrix\_r0c2 : 16
    
    matrix\_r1c0 : 112
    
    matrix\_r1c1 : -102
    
    matrix\_r1c2 : -10
    
    matrix\_r2c0 : -26
    
    matrix\_r2c1 : -87
    
    matrix\_r2c2 : 112
    
    output\_bias\_0 : 16
    
    output\_bias\_1 : 128
    
    output\_bias\_2 : 128
    
     |
    

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/81/v3/3sBB-U8FS0-OHi47M4UjuA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=2081FD65093975341DB00C550BB76485945559B1EB65E8715DF6A644D0BD0D08)

From the perspective of usage, it is meaningless to convert grayscale images into RGB images. The system does not support CSC for YUV400\_U8 inputs.

## Resizing

The image resizing parameters and restrictions are as listed in the following table.

| 
**Name**

 | 

**Description**

 | 

**Value Range (Static)**

 | 

**Value Range (Dynamic)**

 |
| :-- | :-- | :-- | :-- |
| 

switch

 | 

Resizing switch.

 | 

false/true

 | 

false/true

 |
| 

resize\_input\_w

 | 

Image width prior to resizing.

 | 

\[16, 4096\]

 | 

\[16, 1280\]

 |
| 

resize\_input\_h

 | 

Image height prior to resizing.

 | 

\[16, 4096\]

 | 

\[16, 4096\]

 |
| 

resize\_output\_w

 | 

Width of the resized image.

 | 

\[16, 1280\]

 | 

\[16, 448\]

 |
| 

resize\_output\_h

 | 

Height of the resized image.

 | 

\[16, 4096\]

 | 

\[16, 4096\]

 |

The image resizing ratio and restrictions are as listed in the following table.

| 
Name

 | 

Description

 | 

Range (Dynamic & Static)

 |
| :-- | :-- | :-- |
| 

resize\_output\_w / resize\_input\_w

 | 

Image width resizing ratio.

 | 

\[1/16, 16\]

 |
| 

resize\_output\_h / resize\_input\_h

 | 

Image height resizing ratio.

 | 

\[1/16, 16\]

 |

The resizing type is bilinear interpolation. The **resize\_input\_w** and **resize\_input\_h** parameters are invisible to you.

-   When the cropping function is disabled, the size of the input image is used as the image size before resizing.
-   When the cropping function is enabled, as AIPP resizing is always performed after cropping, the size of the image after cropping is used as the size of the image before resizing. During configuration, you only need to pay attention to the size after resizing.

In static AIPP mode, you do not have to configure **crop\_size\_w** and **crop\_size\_h** (size of the cropped out image) and **resize\_output\_w** and **resize\_output\_h** (size of the resized image) in the configuration file, if their values can be obtained through computation. If **resize\_output\_w** and **resize\_output\_h** are omitted, their values are obtained by subtracting padded values from the image size of the model training set. If the resizing function is disabled, **crop\_size\_w** and **crop\_size\_h** can be omitted.

## Data Type Conversion

Data type conversion (DTC) converts pixel values in input images into the data type used for model training. AIPP allows you to set DTC parameters so that the converted data falls within the expected range. This avoids forcible conversion.

The formula for UINT8 to INT8 conversion is as follows:

pixel\_out\_chx(i) = pixel\_in\_chx(i)-mean\_chn\_i

The formula for UINT8 to FLOAT16 conversion is as follows:

pixel\_out\_chx(i) = \[pixel\_in\_chx(i)-mean\_chn\_i-min\_chn\_i\] \* var\_reci\_chn

The following table describes the DTC parameters.

| 
**Name**

 | 

**Description**

 | 

**Value Range**

 |
| :-- | :-- | :-- |
| 

switch

 | 

DTC switch.

 | 

false/true

 |
| 

mean\_chn\_0

 | 

Mean value of channel 0.

 | 

\[0, 255\]

 |
| 

mean\_chn\_1

 | 

Mean value of channel 1.

 | 

\[0, 255\]

 |
| 

mean\_chn\_2

 | 

Mean value of channel 2.

 | 

\[0, 255\]

 |
| 

mean\_chn\_3

 | 

Mean value of channel 3.

 | 

\[0, 255\]

 |
| 

min\_chn\_0

 | 

Minimum value of channel 0.

 | 

\[-65504, 65504\]

 |
| 

min\_chn\_1

 | 

Minimum value of channel 1.

 | 

\[-65504, 65504\]

 |
| 

min\_chn\_2

 | 

Minimum value of channel 2.

 | 

\[-65504, 65504\]

 |
| 

min\_chn\_3

 | 

Minimum value of channel 3.

 | 

\[-65504, 65504\]

 |
| 

var\_reci\_chn\_0

 | 

Variance of channel 0.

 | 

\[-65504, 65504\]

 |
| 

var\_reci\_chn\_1

 | 

Variance of channel 1.

 | 

\[-65504, 65504\]

 |
| 

var\_reci\_chn\_2

 | 

Variance of channel 2.

 | 

\[-65504, 65504\]

 |
| 

var\_reci\_chn\_3

 | 

Variance of channel 3.

 | 

\[-65504, 65504\]

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/4c/v3/EE5p5lvvTLWIpVXkLDUDAQ/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=F45AAE7B568C7A2984EB285F6D9A966374922B42EF107DD9EB79C8D6DB43A9FF)

When the DTC switch is set to **false** or the DTC parameters are not passed by calling CANN Kit APIs, the system performs forcible conversion on the input images by default, with the mean and minimum values as **0** and the channel variance as **1**.

## Rotation

The rotation function of AIPP rotates input images. The involved parameters are described as follows.

| 
**Name**

 | 

**Description**

 | 

**Value Range**

 |
| :-- | :-- | :-- |
| 

switch

 | 

Rotation switch.

 | 

false/true

 |
| 

rotation\_angle

 | 

Rotation angle of an image.

 | 

\[0, 90, 180, 270\]

 |

## Padding

AIPP padding pads input images. The involved parameters are described as follows.

| 
**Name**

 | 

**Description**

 | 

**Value Range**

 |
| :-- | :-- | :-- |
| 

switch

 | 

Padding switch.

 | 

false/true

 |
| 

left\_padding\_size

 | 

Left padding size, in pixels.

 | 

\-

 |
| 

right\_padding\_size

 | 

Right padding size, in pixels.

 | 

\-

 |
| 

top\_padding\_size

 | 

Top padding size, in pixels.

 | 

\-

 |
| 

bottom\_padding\_size

 | 

Bottom padding size, in pixels.

 | 

\-

 |
| 

padding\_value\_chn\_0

 | 

Padding value of channel 0.

 | 

\[-65504, 65504\]

 |
| 

padding\_value\_chn\_1

 | 

Padding value of channel 1.

 | 

\[-65504, 65504\]

 |
| 

padding\_value\_chn\_2

 | 

Padding value of channel 2.

 | 

\[-65504, 65504\]

 |
| 

padding\_value\_chn\_3

 | 

Padding value of channel 3.

 | 

\[-65504, 65504\]

 |

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3d/v3/t1NAv2zxSGGVf1tjAd8YLw/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062124Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=5B516C0F52A9197B3DD74DD89898C2504E826E1C2D9F5A707247C3FC696544DC)

-   Keep the AIPP padding sizes within 32 pixels. Too large padding has to be implemented by software code, which is less efficient than hardware-based implementation.
-   Currently, parameters from **padding\_value\_chn\_0** to **padding\_value\_chn\_3** are not supported.
