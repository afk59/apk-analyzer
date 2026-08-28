# Drawing Images (C/C++)

A bitmap is a data structure used to store and represent images in memory. It is a collection of uncompressed pixels. Images in formats such as JPEG and PNG are compressed and are different from bitmaps. If you want to draw a JPEG or PNG image on the screen, you need to decode the image into a bitmap first. For details, see the image decoding section in Image Kit.

Currently, bitmap drawing in Drawing (C/C++) depends on PixelMap, which can be used to read or write image data and obtain image information. For details about the APIs, see [drawing\_pixel\_map.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-pixel-map-h).

Multiple APIs can be used to create a PixelMap. The following uses OH\_Drawing\_PixelMapGetFromOhPixelMapNative() as an example.

1.  Add the link library.
    
    Add the following link library to src/main/cpp/CMakeLists.txt of the native project:
    
    target\_link\_libraries(entry PUBLIC libnative\_drawing.so)
    target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC libpixelmap.so)
    
2.  Import the related header files.
    
    #include <multimedia/image\_framework/image/pixelmap\_native.h>
    
3.  Create an OH\_PixelmapNative object.
    
    PixelMap needs to be obtained from the pixel map object (OH\_PixelmapNative) defined by the image framework. Therefore, you need to create OH\_PixelmapNative by calling OH\_PixelmapNative\_CreatePixelmap(). This function accepts four parameters. The first parameter is the buffer of image pixel data, which is used to initialize the pixel of PixelMap. The second parameter is the buffer length. The third parameter is the bitmap format (including the length, width, color type, and transparency type). The fourth parameter is the OH\_PixelmapNative object, which is used as the output parameter.
    
    // The image width and height are 600 x 400.
    uint32\_t width = 600;
    uint32\_t height = 400;
    // Byte length. Each pixel of RGBA\_8888 occupies four bytes.
    size\_t bufferSize = width \* height \* 4;
    uint8\_t \*pixels = new uint8\_t\[bufferSize\];
    for (uint32\_t i = 0; i < width \* height; ++i) {
        // Traverse and edit each pixel to form a stripe with red, green, and blue alternating.
        uint32\_t n = i / 20 % 3;
        pixels\[i \* RGBA\_SIZE\] = RGBA\_MIN; // Red channel
        pixels\[i \* RGBA\_SIZE + 1\] = RGBA\_MIN; // +1 indicates the green channel.
        pixels\[i \* RGBA\_SIZE + 2\] = RGBA\_MIN; // +2 indicates the blue channel.
        pixels\[i \* RGBA\_SIZE + 3\] = 0xFF; // +3 indicates the alpha channel.
        if (n == 0) {
            pixels\[i \* RGBA\_SIZE\] = 0xFF; // Assign the red channel. The color is red.
        } else if (n == 1) {
            pixels\[i \* RGBA\_SIZE + 1\] = 0xFF; // +1 indicates that the green channel is assigned a value, and the other channels are 0. The color is green.
        } else {
            pixels\[i \* RGBA\_SIZE + 2\] = 0xFF; // +2 indicates that the blue channel is assigned a value, and other channels are 0. The color is blue.
        }
    }
    // Set the bitmap format (length, width, color type, and transparency type).
    OH\_Pixelmap\_InitializationOptions \*createOps = nullptr;
    OH\_PixelmapInitializationOptions\_Create(&createOps);
    OH\_PixelmapInitializationOptions\_SetWidth(createOps, width);
    OH\_PixelmapInitializationOptions\_SetHeight(createOps, height);
    OH\_PixelmapInitializationOptions\_SetPixelFormat(createOps, PIXEL\_FORMAT\_RGBA\_8888);
    OH\_PixelmapInitializationOptions\_SetAlphaType(createOps, PIXELMAP\_ALPHA\_TYPE\_UNKNOWN);
    // Create an OH\_PixelmapNative object.
    OH\_PixelmapNative \*pixelMapNative = nullptr;
    OH\_PixelmapNative\_CreatePixelmap(pixels, bufferSize, createOps, &pixelMapNative);
    
4.  Create a **PixelMap** instance.
    
    Obtain the PixelMap from OH\_PixelmapNative by using the OH\_Drawing\_PixelMapGetFromOhPixelMapNative() function.
    
    OH\_Drawing\_PixelMap \*pixelMap = OH\_Drawing\_PixelMapGetFromOhPixelMapNative(pixelMapNative);
    
5.  Draw the PixelMap.
    
    You need to use OH\_Drawing\_CanvasDrawPixelMapRect() to draw the PixelMap. The function accepts five parameters: canvas, PixelMap object, pixel cropping area in the PixelMap, display area on the canvas, and sampling option object.
    
    The sampling option object (OH\_Drawing\_SamplingOptions) indicates the specific way of sampling from the original pixel data (that is, Bitmap) to generate new pixel values. For details, see [drawing\_sampling\_options.h](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-drawing-sampling-options-h).
    
    // Pixel cropping area in the PixelMap
    OH\_Drawing\_Rect \*src = OH\_Drawing\_RectCreate(0, 0, 600, 400);
    // Display area on the canvas
    OH\_Drawing\_Rect \*dst = OH\_Drawing\_RectCreate(value200\_, value200\_, value800\_, value600\_);
    // Sampling option object
    OH\_Drawing\_SamplingOptions\* samplingOptions = OH\_Drawing\_SamplingOptionsCreate(
        OH\_Drawing\_FilterMode::FILTER\_MODE\_LINEAR, OH\_Drawing\_MipmapMode::MIPMAP\_MODE\_LINEAR);
    // Draw the PixelMap.
    OH\_Drawing\_CanvasDrawPixelMapRect(canvas, pixelMap, src, dst, samplingOptions);
    
6.  Release related objects after the drawing is complete.
    
    OH\_PixelmapNative\_Release(pixelMapNative);
    delete\[\] pixels;
    
    The drawing effect is as follows:
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/r75XcFfIQaqmpYQTstvynQ/en-us_image_0000002537925172.jpg?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062049Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=3CE1E9BA68566A82A1FB3533C5A25DBEFB7936E77E51D8C2F643021570655559)
