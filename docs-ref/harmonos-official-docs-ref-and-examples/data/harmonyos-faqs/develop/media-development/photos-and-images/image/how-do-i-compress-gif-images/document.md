# How do I compress GIF images?

-   **Solution 1**
    
    You can use the [packToDataFromPixelmapSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagepacker#packtodatafrompixelmapsequence18) API to save GIF images, and then adjust the width and height of the PixelMap or reduce the number of frames to compress the GIF images.
    
    **Adjusting the width and height of the PixelMap**
    
    Use [createPixelMapList()](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-imagesource#createpixelmaplist10) to create a PixelMap array and adjust the width and height of the PixelMap by setting the **desiredSize** parameter.
    
    **Reducing the number of frames**
    
    You can use the **frameCount** parameter of [PackingOptionsForSequence](https://developer.huawei.com/consumer/en/doc/harmonyos-references/arkts-apis-image-i#packingoptionsforsequence18) to reduce the number of frames.
    
-   **Solution 2**
    
    You can use the FFmpeg third-party library to decrease the resolution or frame rate of GIF images. The following two methods can be used (or combined) to compress GIF images:
    
    **Decreasing the resolution**
    
    You can use the **\-s** parameter to set the image resolution. For example, to decrease the resolution of a GIF image and set the width and height to 90 x 90 pixels, run the following command:
    
    ffmpeg -i input.gif -s 90x90 -y output.gif (set the width and height to 90 pixels.)
    
    Alternatively, you can use the **\-vf** parameter and the **scale** filter to set the width to 90 pixels and the height to be automatically scaled proportionally.
    
    ffmpeg -i input.gif -vf "scale=90:-1" -y output.gif
    
    The meanings of the parameters in the preceding command are as follows:
    
    **\-s 90x90**: sets the image resolution to 90 x 90 pixels.
    
    **\-y**: overwrites the existing file.
    
    **\-vf "scale=90:-1"**: sets the image filter. The parameter is a single filter or a filter chain separated by commas (,).
    
    **Decreasing the frame rate**
    
    You can use the **\-r** parameter to specify the frame rate of the output image. For example, to decrease the frame rate of a GIF image to 16 fps, run the following command:
    
    ffmpeg -i input.gif -r 16 output.gif
    
    The meanings of the parameters in this command are as follows:
    
    **\-i input.gif**: specifies the input file.
    
    **\-r 16**: sets the frame rate of the image to 16 fps.
    
    **output.gif**: name of the output file.
