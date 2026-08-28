# Using VideoProcessingEngine to Upscale Images

With the [ArkTS APIs](https://developer.huawei.com/consumer/en/doc/harmonyos-references/js-apis-videoprocessingengine) provided by the VideoProcessingEngine module, you can enhance the detail of images and scale them. The processed data is suitable for use in display and output.

A typical usage scenario is as follows: Obtain an image source from a URL, enhance the image details, and display the image.

#### Constraints

1.  Only an image that meets the following conditions can be processed:
    -   The image is a Standard Dynamic Range (SDR) image.
    -   The image pixel format is RGBA, BGRA, NV12, or NV21, and the output format is the same as the input format.
    -   The memory type for the **PixelMap** object to be processed must be the [DMA memory](../../image-decoding/optimizing-memory-for-image-decoding-arkts/document.md#memory-types).
2.  Four levels of algorithms are provided, each offering better processing outcomes at the expense of increased performance degradation.
    
    | 
    Algorithm Level
    
     | 
    
    Input Resolution
    
    (Unit: Pixel)
    
     | 
    
    Output Resolution
    
    (Unit: Pixel)
    
     | 
    
    Description
    
     |
    | :-- | :-- | :-- | :-- |
    | 
    
    NONE
    
     | 
    
    Width: \[32, 3000\]
    
    Height: \[32, 3000\]
    
     | 
    
    Width: \[32, 3000\]
    
    Height: \[32, 3000\]
    
     | 
    
    Applies only to scaling scenarios. Changing the aspect ratio is supported, but no detail enhancement is provided.
    
     |
    | 
    
    LOW
    
     | 
    
    Width: \[32, 3000\]
    
    Height: \[32, 3000\]
    
     | 
    
    Width: \[32, 3000\]
    
    Height: \[32, 3000\]
    
     | 
    
    Applies only to scaling scenarios. Changing the aspect ratio is supported.
    
    During scaling, a basic level of detail enhancement is provided at a high processing speed.
    
    This quality level is the default setting.
    
     |
    | 
    
    MEDIUM
    
     | 
    
    Width: \[32, 3000\]
    
    Height: \[32, 3000\]
    
     | 
    
    Width: \[32, 3000\]
    
    Height: \[32, 3000\]
    
     | 
    
    Applies only to scaling scenarios. Changing the aspect ratio is supported.
    
    During scaling, a moderate level of detail enhancement is provided at a balanced processing speed.
    
     |
    | 
    
    HIGH
    
     | 
    
    Width: \[512, 2000\]
    
    Height: \[512, 2000\]
    
     | 
    
    Width: \[512, 2000\]
    
    Height: \[512, 2000\]
    
     | 
    
    Applies to scaling and detail enhancement scenarios. Changing the aspect ratio is supported.
    
    During scaling, a high level of detail enhancement is provided at a relatively low processing speed.
    
     |
    

#### How to Develop

1.  Add a reference file.
    
    import { image, videoProcessingEngine } from '@kit.ImageKit';
    
2.  Initialize the environment.
    
    let promise: Promise<void> = videoProcessingEngine.initializeEnvironment();
    
3.  (Optional) Configure the input.
    
    let scale: number = 0.5;
    let width: number = 512; // Sample code. Set the width to 512.
    let height: number = 512;// Sample code. Set the height to 512.
    const color: ArrayBuffer = new ArrayBuffer(width \* height \* 4); // width \* height \* 4 indicates the size of the pixel buffer to be created.
    let opts: image.InitializationOptions = { editable: true, pixelFormat: image.PixelMapFormat.RGBA\_8888, size: { height, width } }
    let sourceImage : image.PixelMap = image.createPixelMapSync(color, opts);
    let level : videoProcessingEngine.QualityLevel = videoProcessingEngine.QualityLevel.LOW;
    
4.  Create an image processing module.
    
    Expected return value: **videoProcessingEngine.ImageProcessor**, an image processing module instance.
    
    // Create an image detail enhancement module instance.
    let imageProcessor = videoProcessingEngine.create() as videoProcessingEngine.ImageProcessor;
    
5.  Start detail enhancement. If the resolutions of the input image **srcImage** and output image **dstImage** are different, the image is scaled.
    
    In the code snippet below, the following variables are used:
    
    **sourceImage:** input image of the PixelMap type. This parameter is mandatory.
    
    **width**: target width (in px). This parameter is mandatory when the target scale ratio is not configured.
    
    **height**: target height (in px). This parameter is mandatory when the target scale ratio is not configured.
    
    **scale**: target scale ratio. This parameter is mandatory when the target resolution is not configured. The target resolution is the width multiplied by the height.
    
    **level**: [algorithm level](#section74721331358). The default value is **LOW**.
    
    -   Method 1: Specify the source image and target resolution.
        
        // Synchronous method.
        let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
        sourceImage, width, height, level);
        
        // Asynchronous method.
        let enhancedPixelmap: Promise<image.PixelMap> = imageProcessor.enhanceDetail(sourceImage, width, height, level);
        
    -   Method 2: Specify the original image and the scale ratio.
        
        // Synchronous method.
        let enhancedPixelmap: image.PixelMap = imageProcessor.enhanceDetailSync(
        sourceImage, scale, level);
        
        // Asynchronous method.
        let enhancedPixelmap: Promise<image.PixelMap> = imageProcessor.enhanceDetail(
        sourceImage, scale, level);
        
6.  Release the video processing resources.
    
    videoProcessingEngine.deinitializeEnvironment();
