# image\_processing.h

#### Overview

The file declares the image processing functions. It provides capabilities such as Color Space Conversion (CSC), metadata generation, and image scaling.

**File to include**: <multimedia/video\_processing\_engine/image\_processing.h>

**Library**: libimage\_processing.so

**System capability**: SystemCapability.Multimedia.VideoProcessingEngine

**Since**: 13

**Related module**: [ImageProcessing](../../modules/imageprocessing/document.md)

#### Summary

#### \[h2\]Functions

| Name | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_InitializeEnvironment(void)](#oh_imageprocessing_initializeenvironment) | 
Initializes the global environment of the image processing module.

This function is optional. Generally, this function is called when the main process is started. It is used to initialize the global environment of the image processing module and reduce the time consumed by [OH\_ImageProcessing\_Create](#oh_imageprocessing_create). It must be used in pair with [OH\_ImageProcessing\_DeinitializeEnvironment](#oh_imageprocessing_deinitializeenvironment), which is used to deinitialize the global environment. This function can be used to check whether the GPU works properly.

 |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_DeinitializeEnvironment(void)](#oh_imageprocessing_deinitializeenvironment) | 

Deinitializes the global environment of the image processing module.

This function must be called after [OH\_ImageProcessing\_InitializeEnvironment](#oh_imageprocessing_initializeenvironment) is called. Generally, this function is called when the main process is about to exit. Do not call this function when an image processing instance exists or when [OH\_ImageProcessing\_InitializeEnvironment](#oh_imageprocessing_initializeenvironment) is not called.

 |
| [bool OH\_ImageProcessing\_IsColorSpaceConversionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo, const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo)](#oh_imageprocessing_iscolorspaceconversionsupported) | Checks whether CSC is supported for an image. |
| [bool OH\_ImageProcessing\_IsCompositionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo, const ImageProcessing\_ColorSpaceInfo\* sourceGainmapInfo,const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo)](#oh_imageprocessing_iscompositionsupported) | Checks whether a dual-layer HDR image can be converted into a single-layer HDR image. |
| [bool OH\_ImageProcessing\_IsDecompositionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo, const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo, const ImageProcessing\_ColorSpaceInfo\* destinationGainmapInfo)](#oh_imageprocessing_isdecompositionsupported) | Checks whether a single-layer HDR image can be converted into a dual-layer HDR image. |
| [bool OH\_ImageProcessing\_IsMetadataGenerationSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo)](#oh_imageprocessing_ismetadatagenerationsupported) | Checks whether metadata generation is supported for an image. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_Create(OH\_ImageProcessing\*\* imageProcessor, int32\_t type)](#oh_imageprocessing_create) | Creates an image processing instance. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_Destroy(OH\_ImageProcessing\* imageProcessor)](#oh_imageprocessing_destroy) | Destroys an image processing instance. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_SetParameter(OH\_ImageProcessing\* imageProcessor, const OH\_AVFormat\* parameter)](#oh_imageprocessing_setparameter) | Sets a parameter for the image processing module. This function sets the parameter by key. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_GetParameter(OH\_ImageProcessing\* imageProcessor, OH\_AVFormat\* parameter)](#oh_imageprocessing_getparameter) | Obtains a parameter of the image processing module. This function obtains the parameter by key. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_ConvertColorSpace(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage)](#oh_imageprocessing_convertcolorspace) | Converts the color space for a single-layer image. This function enables CSC from HDR images to SDR images, CSC from SDR images to HDR images, CSC from SDR images to SDR images, and CSC from HDR images to SDR images. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_Compose(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* sourceGainmap, OH\_PixelmapNative\* destinationImage)](#oh_imageprocessing_compose) | Converts a dual-layer HDR image into a single-layer HDR image. This function is used to generate an output image based on an input image and input gain map. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_Decompose(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage, OH\_PixelmapNative\* destinationGainmap)](#oh_imageprocessing_decompose) | Converts a single-layer HDR image into a double-layer HDR image. This function is used to generate an output image and output gain map based on an input image. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_GenerateMetadata(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage)](#oh_imageprocessing_generatemetadata) | Generates metadata for an HDR image. |
| [ImageProcessing\_ErrorCode OH\_ImageProcessing\_EnhanceDetail(OH\_ImageProcessing\* imageProcessor, OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage)](#oh_imageprocessing_enhancedetail) | Enhances the image definition and details. This function performs necessary scaling operations on the source image based on the preset sizes of the input and output images to generate the target image. It uses multiple scaling methods to balance performance and image quality. |

#### Function Description

#### \[h2\]OH\_ImageProcessing\_InitializeEnvironment()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_InitializeEnvironment(void)

**Description**

Initializes the global environment of the image processing module.

This function is optional. Generally, this function is called when the main process is started. It is used to initialize the global environment of the image processing module and reduce the time consumed by [OH\_ImageProcessing\_Create](#oh_imageprocessing_create). It must be used in pair with [OH\_ImageProcessing\_DeinitializeEnvironment](#oh_imageprocessing_deinitializeenvironment), which is used to deinitialize the global environment. This function can be used to check whether the GPU works properly.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: The initialization is successful.

**IMAGE\_PROCESSING\_ERROR\_INITIALIZE\_FAILED**: The initialization fails.

 |

#### \[h2\]OH\_ImageProcessing\_DeinitializeEnvironment()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_DeinitializeEnvironment(void)

**Description**

Deinitializes the global environment of the image processing module.

This function must be called after [OH\_ImageProcessing\_InitializeEnvironment](#oh_imageprocessing_initializeenvironment) is called. Generally, this function is called when the main process is about to exit. Do not call this function when an image processing instance exists or when [OH\_ImageProcessing\_InitializeEnvironment](#oh_imageprocessing_initializeenvironment) is not called.

**Since**: 13

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: Deinitialization is successful.

**IMAGE\_PROCESSING\_ERROR\_OPERATION\_NOT\_PERMITTED**: The image processing instance is not destroyed or [OH\_ImageProcessing\_InitializeEnvironment](#oh_imageprocessing_initializeenvironment) is not called.

 |

#### \[h2\]OH\_ImageProcessing\_IsColorSpaceConversionSupported()

bool OH\_ImageProcessing\_IsColorSpaceConversionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo,const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo)

**Description**

Checks whether CSC is supported for an image.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* sourceImageInfo | Pointer to the color space information of the input image. |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* destinationImageInfo | Pointer to the color space information of the output image. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of CSC. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_ImageProcessing\_IsCompositionSupported()

bool OH\_ImageProcessing\_IsCompositionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo,const ImageProcessing\_ColorSpaceInfo\* sourceGainmapInfo,const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo)

**Description**

Checks whether a dual-layer HDR image can be converted into a single-layer HDR image.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* sourceImageInfo | Pointer to the color space information of the input image. |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* sourceGainmapInfo | Pointer to the color space information of the input gain map. |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* destinationImageInfo | Pointer to the color space information of the output image. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of a conversion from a dual-layer HDR image into a single-layer HDR image. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_ImageProcessing\_IsDecompositionSupported()

bool OH\_ImageProcessing\_IsDecompositionSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo,const ImageProcessing\_ColorSpaceInfo\* destinationImageInfo,const ImageProcessing\_ColorSpaceInfo\* destinationGainmapInfo)

**Description**

Checks whether a single-layer HDR image can be converted into a dual-layer HDR image.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* sourceImageInfo | Pointer to the color space information of the input image. |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* destinationImageInfo | Pointer to the color space information of the output image. |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* destinationGainmapInfo | Pointer to the color space information of the output gain map. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of a conversion from a single-layer HDR image into a dual-layer HDR image. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_ImageProcessing\_IsMetadataGenerationSupported()

bool OH\_ImageProcessing\_IsMetadataGenerationSupported(const ImageProcessing\_ColorSpaceInfo\* sourceImageInfo)

**Description**

Checks whether metadata generation is supported for an image.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| const [ImageProcessing\_ColorSpaceInfo](../../structs/imageprocessing-colorspaceinfo/document.md)\* sourceImageInfo | Pointer to the color space information of the input image. |

**Returns**

| Type | Description |
| :-- | :-- |
| bool | Check result for the support of metadata generation. **true** if supported, **false** otherwise. |

#### \[h2\]OH\_ImageProcessing\_Create()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_Create(OH\_ImageProcessing\*\* imageProcessor, int32\_t type)

**Description**

Creates an image processing instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\*\* imageProcessor | Double pointer to the image processing instance created. The pointer **\*imageProcessor** points to a new image processing object and must be a null pointer before being passed. |
| int32\_t type | Image processing type. The processing type cannot be changed after the instance is created. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: The instance is created successfully.

**IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: The specified image processing type is not supported, for example, if metadata generation is not supported.

**IMAGE\_PROCESSING\_ERROR\_CREATE\_FAILED**: The instance fails to be created.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or the pointer to the instance is null.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The specified image processing type is invalid.

 |

#### \[h2\]OH\_ImageProcessing\_Destroy()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_Destroy(OH\_ImageProcessing\* imageProcessor)

**Description**

Destroys an image processing instance.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\* imageProcessor | Pointer to an image processing instance. You are advised to set the pointer to a null pointer after the instance is destroyed. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: The instance is destroyed.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not an image processing instance.

 |

#### \[h2\]OH\_ImageProcessing\_SetParameter()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_SetParameter(OH\_ImageProcessing\* imageProcessor,const OH\_AVFormat\* parameter)

**Description**

Sets a parameter for the image processing module. This function sets the parameter by key.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\* imageProcessor | Pointer to an image processing instance. |
| const [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* parameter | Pointer to the parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: The operation is successful.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not an image processing instance.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: **parameter** is empty.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE**: **parameter** is invalid, for example, if **parameter** contains an unsupported parameter key or value.

**IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageProcessing\_GetParameter()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_GetParameter(OH\_ImageProcessing\* imageProcessor,OH\_AVFormat\* parameter)

**Description**

Obtains a parameter of the image processing module. This function obtains the parameter by key.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\* imageProcessor | Pointer to an image processing instance. |
| [OH\_AVFormat](../../../../avcodec-kit/c-apis/structs/oh-avformat/document.md)\* parameter | Pointer to the parameter. |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: The operation is successful.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not an image processing instance.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: **parameter** is empty.

 |

#### \[h2\]OH\_ImageProcessing\_ConvertColorSpace()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_ConvertColorSpace(OH\_ImageProcessing\* imageProcessor,OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage)

**Description**

Converts the color space for a single-layer image. This function enables CSC from HDR images to SDR images, CSC from SDR images to HDR images, CSC from SDR images to SDR images, and CSC from HDR images to SDR images.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\* imageProcessor | Pointer to an image processing instance, which is created by **IMAGE\_PROCESSING\_TYPE\_COLOR\_SPACE\_CONVERSION**. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* sourceImage | Pointer to the input image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* destinationImage | Pointer to the output image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: Image processing is successful.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not an image processing instance.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The image is empty.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE**: An image property is invalid, for example, unsupported color space.

**IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: Image processing is not supported.

**IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED**: An error occurs during image processing.

**IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageProcessing\_Compose()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_Compose(OH\_ImageProcessing\* imageProcessor,OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* sourceGainmap, OH\_PixelmapNative\* destinationImage)

**Description**

Converts a dual-layer HDR image into a single-layer HDR image. This function is used to generate an output image based on an input image and input gain map.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\* imageProcessor | Pointer to an image processing instance, which is created by **IMAGE\_PROCESSING\_TYPE\_COMPOSITION**. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* sourceImage | Pointer to the input image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* sourceGainmap | Pointer to the input gain map. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* destinationImage | Pointer to the output image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: Image processing is successful.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not an image processing instance.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The image is empty.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE**: An image property is invalid, for example, unsupported color space.

**IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: Image processing is not supported.

**IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED**: An error occurs during image processing.

**IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageProcessing\_Decompose()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_Decompose(OH\_ImageProcessing\* imageProcessor,OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage, OH\_PixelmapNative\* destinationGainmap)

**Description**

Converts a single-layer HDR image into a double-layer HDR image. This function is used to generate an output image and output gain map based on an input image.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\* imageProcessor | Pointer to an image processing instance, which is created by **IMAGE\_PROCESSING\_TYPE\_DECOMPOSITION**. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* sourceImage | Pointer to the input image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* destinationImage | Pointer to the output image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* destinationGainmap | Pointer to the output gain map. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: Image processing is successful.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not an image processing instance.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The image is empty.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE**: An image property is invalid, for example, unsupported color space.

**IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: Image processing is not supported.

**IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED**: An error occurs during image processing.

**IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageProcessing\_GenerateMetadata()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_GenerateMetadata(OH\_ImageProcessing\* imageProcessor,OH\_PixelmapNative\* sourceImage)

**Description**

Generates metadata for an HDR image. This function is used to generate metadata for HDR images.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\* imageProcessor | Pointer to an image processing instance, which is created by **IMAGE\_PROCESSING\_TYPE\_METADATA\_GENERATION**. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* sourceImage | Pointer to the input image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: Image processing is successful.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not an image processing instance.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The image is empty.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE**: An image property is invalid, for example, unsupported color space.

**IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: Image processing is not supported.

**IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED**: An error occurs during image processing.

**IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY**: Memory allocation fails.

 |

#### \[h2\]OH\_ImageProcessing\_EnhanceDetail()

ImageProcessing\_ErrorCode OH\_ImageProcessing\_EnhanceDetail(OH\_ImageProcessing\* imageProcessor,OH\_PixelmapNative\* sourceImage, OH\_PixelmapNative\* destinationImage)

**Description**

Enhances the image definition and details. This function performs necessary scaling operations on the source image based on the preset sizes of the input and output images to generate the target image. It uses multiple scaling methods to balance performance and image quality.

**Since**: 13

**Parameters**

| Name | Description |
| :-- | :-- |
| [OH\_ImageProcessing](../../structs/oh-imageprocessing/document.md)\* imageProcessor | Pointer to an image processing instance, which is created by **IMAGE\_PROCESSING\_TYPE\_DETAIL\_ENHANCER**. |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* sourceImage | Pointer to the input image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |
| [OH\_PixelmapNative](../../structs/oh-pixelmapnative/document.md)\* destinationImage | Pointer to the output image. The OH\_PixelmapNative it points to must be allocated in DMA memory. For details, see [PixelMap Memory Types](https://developer.huawei.com/consumer/en/doc/harmonyos-guides/image-allocator-type#memory-types). |

**Returns**

| Type | Description |
| :-- | :-- |
| [ImageProcessing\_ErrorCode](../image-processing-types-h/document.md#imageprocessing_errorcode) | 
**IMAGE\_PROCESSING\_SUCCESS**: Image processing is successful.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_INSTANCE**: The instance is null or is not an image processing instance.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_PARAMETER**: The image is empty.

**IMAGE\_PROCESSING\_ERROR\_INVALID\_VALUE**: An image property is invalid, for example, unsupported color space.

**IMAGE\_PROCESSING\_ERROR\_UNSUPPORTED\_PROCESSING**: Image processing is not supported.

**IMAGE\_PROCESSING\_ERROR\_PROCESS\_FAILED**: An error occurs during image processing.

**IMAGE\_PROCESSING\_ERROR\_NO\_MEMORY**: Memory allocation fails.

 |
