# AIPP Configuration File Used for Model Conversion

#### About the AIPP Configuration File Used for Model Conversion

The following is an example of an AIPP configuration file with complete functions:

\# An AIPP configuration starts with the **aipp\_op** flag, which indicates that it is the configuration of an AIPP operator. Multiple **aipp\_op** flags can be configured.
aipp\_op {
# **input\_name** is optional. It specifies the input of the model to be processed with AIPP.
# Type: string
    input\_name: "data"

# **related\_input\_rank** is optional and corresponds to **input\_name**. **input\_name** is preferred if the model's input name is available. If the model's input name is unavailable, **related\_input\_rank** can be used to identify the sequence number of the model input to be processed with AIPP.
    # Type: uint32
    related\_input\_rank: 0

# **node\_after\_aipp** is optional. It is used when an input has multiple branches and different AIPP processing needs to be performed on the branches. You can either configure the parameter for all or none of the branches. Configuring a part of them is not supported.
# Type: string
    node\_after\_aipp: "op\_name"

# **input\_edge\_idx** is optional and corresponds to **node\_after\_aipp**. If the operators after the Data operator have the same name, **input\_edge\_idx** can be used to identify the branch to be processed with AIPP.
    # Type: uint32
    input\_edge\_idx: 0

    input\_para {
# Type of the input image
# Type: enum
# Value range: \[YUV420SP\_U8, XRGB8888\_U8, ARGB8888\_U8, YUYV\_U8, YUV422SP\_U8, AYUV444\_U8, YUV400\_U8, RGB888\_U8\]
        format: AYUV444\_U8

        shape {
# Width and height of the input image
# Type: uint32
            # Value range and constraints: \[0, 4096\]. For YUV images except YUV400, the value must be an even number.
            src\_image\_size\_w: 800
            src\_image\_size\_h: 600
        }

# **max\_src\_image\_size** is used in the dynamic AIPP mode. When the image length, width, or input type is uncertain, use this parameter to set the maximum input image size.
        # Type: uint32
        max\_src\_image\_size: 102400
    }

# == Cropping settings == #
    crop\_func {
        switch: true
        dynamic: true
        load\_start\_pos\_w: 50
        load\_start\_pos\_h: 50
        crop\_size\_w: 400
        crop\_size\_h: 400
    }

# == Channel swapping settings == #
    swap\_func {
        dynamic: true
        rbuv\_swap\_switch: true
        ax\_swap\_switch: true
    }

# == Resizing settings == #
    resize\_func {
        switch: true
        dynamic: true
        resize\_output\_w: 200
        resize\_output\_h: 200
    }

# == Color space conversion settings == #
    csc\_func {
        switch: true
        dynamic: true
        matrix\_r0c0: 256
        matrix\_r0c1: 0
        matrix\_r0c2: 259
        matrix\_r1c0: 256
        matrix\_r1c1: -88
        matrix\_r1c2: -183
        matrix\_r2c0: 256
        matrix\_r2c1: 454
        matrix\_r2c2: 0
        output\_bias\_0: 0
        output\_bias\_1: 0
        output\_bias\_2: 0
        input\_bias\_0: 16
        input\_bias\_1: 128
        input\_bias\_2: 128
    }

# == Data type conversion settings == #
    dtc\_func {
        switch: true
        dynamic: true
        mean\_chn\_0: 0
        mean\_chn\_1: 0
        mean\_chn\_2: 0
        mean\_chn\_3: 0
        min\_chn\_0: 0
        min\_chn\_1: 0
        min\_chn\_2: 0
        min\_chn\_3: 0
        var\_reci\_chn\_0: 1.0
        var\_reci\_chn\_1: 1.0
        var\_reci\_chn\_2: 1.0
        var\_reci\_chn\_3: 1.0
    }

# == Rotation settings == #
    rotation\_func {
        switch: true
        dynamic: true
        rotation\_angle: 0.0
    }

# == Padding settings == #
    padding\_func {
        switch: true
        dynamic: true
        left\_padding\_size: 12
        right\_padding\_size: 12
        top\_padding\_size: 12
        bottom\_padding\_size: 12
        padding\_value\_chn\_0: 20.0
        padding\_value\_chn\_1: 20.0
        padding\_value\_chn\_2: 20.0
        padding\_value\_chn\_3: 20.0
    }
}

## AIPP Multi-Input Support

Separate AIPP settings for multiple inputs of a multi-input model or for different output branches of an input Data operator are supported.

AIPP multi-input support is controlled by two pairs of parameters: **input\_name** and **related\_input\_rank** specify the input to be processed with AIPP, while **node\_after\_aipp** and **input\_edge\_idx** specify an output of the Data operator to be processed with AIPP.

Between **input\_name** and **related\_input\_rank**, parameter **input\_name** is preferred. Parameter **related\_input\_rank** applies to the scenario where the model input name is uncertain. If both parameters are configured, mutual-check is performed between them. If neither is configured, AIPP is performed on the first input of the model by default.

Between **node\_after\_aipp** and **input\_edge\_idx**, parameter **node\_after\_aipp** is preferred. Parameter **input\_edge\_idx** applies to the scenario where the downstream operators of the Data operator have duplicated or uncertain names. If both parameters are configured, mutual-check is performed between them. If neither is configured, the same AIPP is performed on all output branches of the Data operator.

## Dynamic AIPP and Static AIPP

If **dynamic** is set to **true** for any AIPP subfunction, or no subfunction is enabled, the generated DaVinci model will be a dynamic AIPP model. In this case, you need to pass AIPP configuration parameters during model inference. Otherwise, if **dynamic** is set to **false** for all AIPP subfunctions, and at least one subfunction is enabled, the generated DaVinci model will be a static AIPP model. In this case, use the AIPP configuration parameters defined in the configuration file for model inference.

In dynamic AIPP mode, the input image length, width, and image type can be uncertain. That is, the **src\_image\_size\_w**, **src\_image\_size\_h**, and **input\_format** parameters can be left empty. In this case, you need to set **max\_src\_image\_size** to specify the maximum image size for dynamic AIPP.

#### Image Cropping

The image cropping function allows you to crop an image of a certain size from a specified start point out of the original image.

If **dynamic** is left empty or is set to **false**, it indicates static configuration. If **dynamic** is set to **true**, it indicates dynamic configuration.

-   In static configuration, the shape is output according to the values of **crop\_size\_w** and **crop\_size\_h**.
-   In dynamic configuration, **crop\_size\_w** and **crop\_size\_h** are preset to the maximum shape values. In actual running, the values will not exceed the preset maximum values.

## Static Configuration

crop\_func {
    switch: true
    load\_start\_pos\_w: 50
    load\_start\_pos\_h: 50
    crop\_size\_w: 150
    crop\_size\_h: 150
}

## Dynamic Configuration

crop\_func {
    switch: true
    dynamic: true
    load\_start\_pos\_w: 0
    load\_start\_pos\_h: 0
    crop\_size\_w: 150
    crop\_size\_h: 150
}

#### Channel Swapping (axSwap/uvSwap/rbSwap)

Images can be swapped through channels axSwap, uvSwap, and rbSwap.

-   axSwap: Only the ARGB8888, XRGB8888, and AYUV444 formats are supported.
-   uvSwap: Only the YUV420SP, YUV422SP\_U8, YUYV, and AYUV444 formats are supported.
-   rbSwap: Only the ARGB8888, XRGB8888, and RGB888\_U8 formats are supported.

If **dynamic** is left empty or is set to **false**, it indicates static configuration. If **dynamic** is set to **true**, it indicates dynamic configuration.

## Static Configuration

swap\_func {
    ax\_swap\_switch: true
    rbuv\_swap\_switch: false
}

## Dynamic Configuration

The parameters are optional, and can be specified when the input tensor is created dynamically.

swap\_func {
    dynamic: true
    ax\_swap\_switch: true
    rbuv\_swap\_switch: false
}

#### Color Space Conversion (CSC)

If **dynamic** is left empty or is set to **false**, it indicates static configuration. If **dynamic** is set to **true**, it indicates dynamic configuration.

Supported conversion:

-   From YUV420SP, YUYV, YUV422SP, and AYUV444 to RGB888 and BGR888
-   From XRGB8888, ARGB8888, and RGB888 to YVU444SP, YUV444SP, and YUV400

## Static Configuration

The following is an example of configuring the CSC matrix in static AIPP mode.

csc\_func {
    switch: true
    matrix\_r0c0: 256
    matrix\_r0c1: 454
    matrix\_r0c2: 0
    matrix\_r1c0: 256
    matrix\_r1c1: -88
    matrix\_r1c2: -183
    matrix\_r2c0: 256
    matrix\_r2c1: 0
    matrix\_r2c2: 359
    output\_bias\_0: 0
    output\_bias\_1: 0
    output\_bias\_2: 0
    input\_bias\_0: 0
    input\_bias\_1: 128
    input\_bias\_2: 128
}

## Dynamic Configuration

In dynamic scenarios where **inputFormat** is variable, set the output color space (**output\_format**) to a fixed value. Otherwise, an error will be reported.

csc\_func {
    switch: true
    dynamic: true
    output\_format: RGB888\_U8
    color\_space: JPEG
}

#### Image Resizing

The image resizing function supports image zoom-in and zoom-out in bilinear interpolation mode. The minimum size of the output image is 16 x 16, and the maximum size of the output image is 448 x 448.

If **dynamic** is left empty or is set to **false**, it indicates static configuration. If **dynamic** is set to **true**, it indicates dynamic configuration.

## Static Configuration

resize\_func {
    switch: true
    resize\_output\_w: 182
    resize\_output\_h: 182
}

## Dynamic Configuration

**resize\_output\_w** and **resize\_output\_h** are pre-set to the maximum values.

resize\_func {
    switch: true
    dynamic: true
    resize\_output\_w: 250
    resize\_output\_h: 200
}

#### Data Type Conversion (DTC)

DTC is used to convert input images to the FP16 format using a conversion formula, and send the converted images to subsequent modules for further computation. During the conversion, mean subtraction, minimum value subtraction, and multiplying the variance are performed in sequence.

If **dynamic** is left empty or is set to **false**, it indicates static configuration. If **dynamic** is set to **true**, it indicates dynamic configuration.

## Static Configuration

dtc\_func {
    switch: true
    mean\_chn\_0: 4
    mean\_chn\_1: 4
    mean\_chn\_2: 4
    min\_chn\_0: 2.0
    min\_chn\_1: 2.0
    min\_chn\_2: 2.0
    var\_reci\_chn\_0: 2.0
    var\_reci\_chn\_1: 2.0
    var\_reci\_chn\_2: 2.0
}

## Dynamic Configuration

The parameters are optional, and can be specified when the input tensor is created dynamically.

dtc\_func {
    switch: true
    dynamic: true
}

#### Image Rotation

Images can be rotated by 90°, 180°, or 270° to adapt to image data when the phone is rotated. Currently, the rotation function is supported only in the static single-operator scenario, and is not supported in dynamic or convolutional fusion scenarios. The static configuration is as follows:

rotate\_para {
    switch: true
    dynamic: true    
    rotation\_angle: 0.0
}

#### Image Padding

This function allows you to apply certain size of padding to the left, right, top, or bottom sides of an image. You can apply up to four channels, and set different padding values for each channel. If a channel is not set, **0** will be applied by default. You can apply up to 32 columns or rows respectively to the left, right, top, and bottom sides of an image.

-   When a crop or resize operator is used as the last AIPP operator, the output shape remains unchanged, that is, the output shape cannot be dynamically adjusted. When the operator is followed by a convolution operator, the output shape of the crop or resize operator will be the input shape of the convolution operator.
-   When a crop or resize operator is followed by a padding operator:
    -   If the padding operator is static, the crop or resize operator before the padding operator will also be static, and the output shape remains unchanged. The output shape of the crop or resize operator plus the padding value is the shape of the convolution operator.
    -   If the padding operator is dynamic, the four padding values of the padding operator are set to **0**. In this case, the output of the crop or resize operator before the padding operator is the shape of the subsequent convolution operator. You can adjust the parameter values, but make sure that the final output must be equal to the convolution operator's input.

If **dynamic** is left empty or is set to **false**, it indicates static configuration. If **dynamic** is set to **true**, it indicates dynamic configuration.

## Static Configuration

padding\_func {
    switch: true
    left\_padding\_size: 21
    right\_padding\_size: 21
    top\_padding\_size: 21
    bottom\_padding\_size: 21
    padding\_value\_chn\_0: 20.0
    padding\_value\_chn\_1: 20.0
    padding\_value\_chn\_2: 20.0
    padding\_value\_chn\_3: 20.0
}

## Dynamic Configuration

The padding operator is dynamic. Therefore, the four padding values of the padding operator are set to **0** at first, and then specified when the input tensor is created dynamically.

padding\_func {
    switch: true
    dynamic: true
    left\_padding\_size: 0
    right\_padding\_size: 0
    top\_padding\_size: 0
    bottom\_padding\_size: 0
}

#### Complete AIPP Configuration Example in Dynamic Mode

aipp\_op {
    input\_para {
        shape {
            src\_image\_size\_w: 480
            src\_image\_size\_h: 384
        }
    }
    crop\_func {
        switch: true
        dynamic: true
        load\_start\_pos\_w: 50
        load\_start\_pos\_h: 50
        crop\_size\_w: 150
        crop\_size\_h: 150
    }
    resize\_func {
        switch: true
        dynamic: true
        resize\_output\_w: 250
        resize\_output\_h: 200
    }
    padding\_func {
        switch: true
        dynamic: true
        left\_padding\_size: 0
        right\_padding\_size: 0
        top\_padding\_size: 0
        bottom\_padding\_size: 0
    }
    swap\_func {
        dynamic: true
        ax\_swap\_switch: true
    }
    csc\_func {
        switch: true
        dynamic: true
        output\_format: RGB888\_U8
        color\_space: JPEG
    }
    dtc\_func {
        switch: true
        dynamic: true
    }  
}

#### Complete AIPP Configuration Example in Static Mode

aipp\_op {
    input\_para {
        shape {
            src\_image\_size\_w: 480
            src\_image\_size\_h: 384
        }
        format: AYUV444\_U8
    }
    crop\_func {
        switch: true
        load\_start\_pos\_w: 50
        load\_start\_pos\_h: 50
        crop\_size\_w: 150
        crop\_size\_h: 150
    }
    resize\_func {
        switch: true
        resize\_output\_w: 182
        resize\_output\_h: 182
    }
    padding\_func {
        switch: true
        left\_padding\_size: 21
        right\_padding\_size: 21
        top\_padding\_size: 21
        bottom\_padding\_size: 21
    }
    swap\_func {
        ax\_swap\_switch: true
    }
    csc\_func {
        switch: true
        matrix\_r0c0: 256
        matrix\_r0c1: 454
        matrix\_r0c2: 0
        matrix\_r1c0: 256
        matrix\_r1c1: -88
        matrix\_r1c2: -183
        matrix\_r2c0: 256
        matrix\_r2c1: 0
        matrix\_r2c2: 359
        output\_bias\_0: 0
        output\_bias\_1: 0
        output\_bias\_2: 0
        input\_bias\_0: 0
        input\_bias\_1: 128
        input\_bias\_2: 128
    }
    dtc\_func {
        switch: true
        mean\_chn\_0: 4
        mean\_chn\_1: 4
        mean\_chn\_2: 4
        min\_chn\_0: 2.0
        min\_chn\_1: 2.0
        min\_chn\_2: 2.0
        var\_reci\_chn\_0: 2.0
        var\_reci\_chn\_1: 2.0
        var\_reci\_chn\_2: 2.0
}
    rotate\_func {
        switch: true
        rotate\_angle: 180.0
    }
}

#### AIPP Configuration Example in Hybrid Mode

You cannot set the **rotate** parameter in hybrid mode, as the model is dynamic in this case and the **rotate** parameter is not supported in dynamic mode.

aipp\_op {
    input\_para {
        shape {
            src\_image\_size\_w: 200
            src\_image\_size\_h: 200
        }
        format: ARGB8888\_U8
    }
    crop\_func {
        switch: true
        dynamic: true
        crop\_size\_w: 100
        crop\_size\_h: 100
    }
    resize\_func {
        switch: true
        resize\_output\_w: 200
        resize\_output\_h: 200
    }
    padding\_func {
        switch: true
        right\_padding\_size: 24
        bottom\_padding\_size: 24
    }
    swap\_func {
        rbuv\_swap\_switch: true
        ax\_swap\_switch: true
    }
    dtc\_func {
        switch: true
        mean\_chn\_0: 4
        mean\_chn\_1: 4
        mean\_chn\_2: 4
        min\_chn\_0: 2.0
        min\_chn\_1: 2.0
        min\_chn\_2: 2.0
        var\_reci\_chn\_0: 2.0
        var\_reci\_chn\_1: 2.0
        var\_reci\_chn\_2: 2.0
    }
}
