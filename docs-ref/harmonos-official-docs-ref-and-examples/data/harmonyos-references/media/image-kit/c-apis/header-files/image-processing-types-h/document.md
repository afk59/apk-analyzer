# image\_processing\_types.h

#### Overview

The file declares the image processing types.

**File to include**: <multimedia/video\_processing\_engine/image\_processing\_types.h>

**Library**: libimage\_processing.so

**System capability**: SystemCapability.Multimedia.VideoProcessingEngine

**Since**: 13

**Related module**: [ImageProcessing](../../modules/imageprocessing/document.md)

#### Summary

#### \[h2\]Structs

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md) | ImageProcessing\_ColorSpaceInfo | Describes the color space information, which is used in Color Space Conversion (CSC) capability query. |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md) | OH\_ImageProcessing | 
Provides the declaration of the OH\_ImageProcessing struct.

To use it, first declare a null pointer of OH\_ImageProcessing, and then initialize it by calling [OH\_ImageProcessing\_Create](../image-processing-h/document.md#oh_imageprocessing_create). This function creates an image processing instance. Multiple instances can be created for different image processing tasks.

 |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md) | OH\_PixelmapNative | Provides the declaration of the OH\_PixelmapNative struct. |
| [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md) | OH\_AVFormat | Provides the declaration of the OH\_AVFormat struct. |

#### \[h2\]Enums

| Name | typedef Keyword | Description |
| :-- | :-- | :-- |
| [ImageDetailEnhancer\_QualityLevel](#imagedetailenhancer_qualitylevel) | ImageDetailEnhancer\_QualityLevel | 
Enumerates the quality levels, which are used for detail enhancement.

Corresponding key: IMAGE\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL.

 |
| [ImageProcessing\_ErrorCode](#imageprocessing_errorcode) | ImageProcessing\_ErrorCode | Enumerates the error codes used in image processing. |

#### \[h2\]Variables

| Name | Description |
| :-- | :-- |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION | 
Used to create an image processing instance for CSC.

CSC includes conversion from single-layer HDR images to SDR images, conversion between SDR images, and conversion from SDR images to single-layer HDR images. Some capabilities are supported by vendors. Use [OH\_ImageProcessing\_IsColorSpaceConversionSupported](../image-processing-h/document.md#oh_imageprocessing_iscolorspaceconversionsupported) to check whether a conversion can be performed between single-layer images.

**Since**: 13

**Reference**: [OH\_ImageProcessing\_Create](../image-processing-h/document.md#oh_imageprocessing_create)

 |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_COMPOSITION | 

Used to create an image processing instance for converting a dual-layer HDR image into a single-layer HDR image.

The instance provides the capability of converting dual-layer HDR images into single-layer HDR images. Some capabilities are supported by vendors. Use [OH\_ImageProcessing\_IsCompositionSupported](../image-processing-h/document.md#oh_imageprocessing_iscompositionsupported) to check whether the conversion from a dual-layer HDR image into a single-layer HDR image is supported.

**Since**: 13

**Reference**: [OH\_ImageProcessing\_Create](../image-processing-h/document.md#oh_imageprocessing_create)

 |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_DECOMPOSITION | 

Used to create an image processing instance for converting a single-layer HDR image into a dual-layer HDR image.

The instance provides the capability of converting single-layer HDR images into dual-layer HDR images. Some capabilities are supported by vendors. Use [OH\_ImageProcessing\_IsDecompositionSupported](../image-processing-h/document.md#oh_imageprocessing_isdecompositionsupported) to check whether the conversion from a single-layer HDR image into a dual-layer HDR image is supported.

**Since**: 13

**Reference**: [OH\_ImageProcessing\_Create](../image-processing-h/document.md#oh_imageprocessing_create)

 |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_METADATA\_GENERATION | 

Used to create an image processing instance for metadata generation.

This variable generates the HDR Vivid metadata of a single-layer HDR image. Some capabilities are supported by vendors. If the capability is not supported, [OH\_ImageProcessing\_Create](../image-processing-h/document.md#oh_imageprocessing_create) returns [IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING](#imageprocessing_errorcode).

**Since**: 13

**Reference**: [OH\_ImageProcessing\_Create](../image-processing-h/document.md#oh_imageprocessing_create)

 |
| const int32\_t IMAGE\_PROCESSING\_TYPE\_DETAIL\_ENHANCER | 

Used to create an image processing instance for detail enhancement.

This variable scales or resizes the image based on the specified image quality, or only enhances the image details to render the image without changing the resolution.

**Since**: 13

**Reference**: [OH\_ImageProcessing\_Create](../image-processing-h/document.md#oh_imageprocessing_create)

 |
| const char \* IMAGE\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL | 

Used to set the quality level for image detail enhancement.

Use [ImageDetailEnhancer\_QualityLevel](#imagedetailenhancer_qualitylevel) to obtain the quality level. Use [OH\_ImageProcessing\_SetParameter](../image-processing-h/document.md#oh_imageprocessing_setparameter) to set the quality level. Use [OH\_ImageProcessing\_GetParameter](../image-processing-h/document.md#oh_imageprocessing_getparameter) to obtain the quality level in use.

**Since**: 13

 |

#### Enum Description

#### \[h2\]ImageDetailEnhancer\_QualityLevel

enum ImageDetailEnhancer\_QualityLevel

**Description**

Enumerates the quality levels, which are used for detail enhancement.

Corresponding key: IMAGE\_DETAIL\_ENHANCER\_PARAMETER\_KEY\_QUALITY\_LEVEL.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_NONE | No detail enhancement. |
| IMAGE\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_LOW | Low-quality detail enhancement, which features fast speed. This is the default value. |
| IMAGE\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_MEDIUM | Medium-quality detail enhancement, which features moderate speed. |
| IMAGE\_DETAIL\_ENHANCER\_QUALITY\_LEVEL\_HIGH | High-quality detail enhancement, which features slow speed. |

**See also**

[OH\_ImageProcessing\_SetParameter](../image-processing-h/document.md#oh_imageprocessing_setparameter), [OH\_ImageProcessing\_GetParameter](../image-processing-h/document.md#oh_imageprocessing_getparameter)

#### \[h2\]ImageProcessing\_ErrorCode

enum ImageProcessing\_ErrorCode

**Description**

Enumerates the error codes used in image processing.

**Since**: 13

| Enum Item | Description |
| :-- | :-- |
| IMAGE\_PROCESSING\_SUCCESS | The operation is successful. |
| IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER = 401 | 
An input parameter is invalid.

This error code is returned in the following cases:

1\. The input or output buffer is either invalid or empty.

2\. The provided parameter is invalid or missing.

3\. The type is invalid. For example, the type passed in the creation function does not exist.

 |
| IMAGE\_PROCESSING\_ERROR\_UNKNOWN = 29200001 | An unknown error occurs. For example, the GPU computing or memcpy fails. |
| IMAGE\_PROCESSING\_ERROR\_INITIALIZE\_FAILED | The global environment, for example, the GPU environment, fails to be initialized. |
| IMAGE\_PROCESSING\_ERROR\_CREATE\_FAILED | Creating the image processing instance fails. For example, the total number of instances exceeds the upper limit. |
| IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED | The processing fails. For example, the processing times out. |
| IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING | The processing type is not supported. You can call OH\_ImageProcessing\_IsXXXSupported to check whether a specific processing type is supported. |
| IMAGE\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED | The operation is not allowed. For example, the function is called in an incorrect running state. |
| IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY | Insufficient memory. |
| IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE | The image processing instance is invalid, for example, a null instance. |
| IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE | 

The input value is invalid.

This error code is returned in the following cases:

1\. The input or output image buffer is invalid. For example, the width (height) of the image buffer is too large or the color space is incorrect.

2\. The parameter is invalid. For example, the parameter does not contain valid information, such as invalid quality level for detail enhancement.

 |
