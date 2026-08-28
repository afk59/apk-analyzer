# Adding Image Effects (C/C++)

#### When to Use

When processing images offline, you can configure various image effects to achieve different visual presentations, such as setting image blur intensity, adjusting brightness and grayscale, and applying color inversion.

Image effects are primarily configured based on filters.

#### Available APIs

Common APIs for setting image effects via filters are listed below. For detailed usage and parameters, see [effect\_filter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/capi-effect-filter-h).

| API | Description |
| :-- | :-- |
| EffectErrorCode OH\_Filter\_CreateEffect(OH\_PixelmapNative\* pixelmap, OH\_Filter\*\* filter) | Creates a filter object based on the pixelmap object. |
| EffectErrorCode OH\_Filter\_Blur(OH\_Filter\* filter, float radius) | Creates a blur effect and adds it to the filter. |
| EffectErrorCode OH\_Filter\_Brighten(OH\_Filter\* filter, float brightness) | Creates a brightening effect and adds it to the filter. |
| EffectErrorCode OH\_Filter\_GrayScale(OH\_Filter\* filter) | Creates a grayscale effect and adds it to the filter. |
| EffectErrorCode OH\_Filter\_Invert(OH\_Filter\* filter) | Creates a color inversion effect and adds it to the filter. |
| EffectErrorCode OH\_Filter\_GetEffectPixelMap(OH\_Filter\* filter, OH\_PixelmapNative\*\* pixelmap) | Obtains the pixelmap object generated after filter processing. |
| EffectErrorCode OH\_Filter\_Release(OH\_Filter\* filter) | Releases the filter object. |

#### How to Develop

1.  Add the following link libraries to **src/main/cpp/CMakeLists.txt** in your Native project.
    
    target\_link\_libraries(entry PUBLIC libnative\_drawing.so)
    target\_link\_libraries(entry PUBLIC libhilog\_ndk.z.so)
    target\_link\_libraries(entry PUBLIC libnative\_effect.so)
    target\_link\_libraries(entry PUBLIC libpixelmap.so)
    
2.  Import the required header files.
    
    #include "multimedia/image\_framework/image/pixelmap\_native.h"
    #include "native\_effect/effect\_filter.h"
    
3.  Create an **OH\_PixelmapNative** object.
    
    A filter requires a PixelMap object (**OH\_PixelmapNative**) defined by the image framework. You can create a custom PixelMap via **OH\_PixelmapNative\_CreatePixelMap()**, or import an external PixelMap via **OH\_PixelmapNative\_ConvertPixelmapNativeFromNapi()**.
    
    This section describes how to create an **OH\_PixelmapNative** object via **OH\_PixelmapNative\_CreatePixelMap()**. This function accepts four parameters: buffer for image pixel data (initializes PixelMap pixels), buffer length, PixelMap format (including width, height, color type, alpha type, etc.), and the **OH\_PixelmapNative** object (used as an output parameter).
    
    // The image width and height are 600 and 400, respectively.
    uint32\_t width = 600;
    uint32\_t height = 400;
    const uint16\_t RGBA\_MIN = 0x00;
    const uint16\_t RGBA\_MAX = 0xFF;
    const uint16\_t RGBA\_SIZE = 4;
    // Byte length. Each RGBA\_8888 pixel occupies four bytes.
    size\_t bufferSize = width \* height \* RGBA\_SIZE;
    uint8\_t \*pixels = new uint8\_t\[bufferSize\];
    for (uint32\_t i = 0; i < width \* height; ++i) {
         // Traverse and edit each pixel to form red-green-blue stripes.
         uint32\_t n = i / 20 % 3;
         pixels\[i \* RGBA\_SIZE\] = RGBA\_MIN; // Red channel.
         pixels\[i \* RGBA\_SIZE + 1\] = RGBA\_MIN; // +1 indicates the green channel.
         pixels\[i \* RGBA\_SIZE + 2\] = RGBA\_MIN; // +2 indicates the blue channel.
         pixels\[i \* RGBA\_SIZE + 3\] = RGBA\_MAX; // +3 indicates the alpha channel.
         if (n == 0) {
             pixels\[i \* RGBA\_SIZE\] = RGBA\_MAX; // Assign value to the red channel, displaying red.
         } else if (n == 1) {
             pixels\[i \* RGBA\_SIZE + 1\] = RGBA\_MAX; // +1 indicates assignment to the green channel, with other channels set to 0, displaying green.
         } else {
             pixels\[i \* RGBA\_SIZE + 2\] = RGBA\_MAX; // +2 indicates assignment to the blue channel, with other channels set to 0, displaying blue.
         }
    }
    // Set the PixelMap format (width, height, color type, and alpha type).
    OH\_Pixelmap\_InitializationOptions \*createOps = nullptr;
    OH\_PixelmapInitializationOptions\_Create(&createOps);
    OH\_PixelmapInitializationOptions\_SetWidth(createOps, width);
    OH\_PixelmapInitializationOptions\_SetHeight(createOps, height);
    OH\_PixelmapInitializationOptions\_SetPixelFormat(createOps, PIXEL\_FORMAT\_RGBA\_8888);
    OH\_PixelmapInitializationOptions\_SetAlphaType(createOps, PIXELMAP\_ALPHA\_TYPE\_UNKNOWN);
    // Create an OH\_PixelmapNative object.
    OH\_PixelmapNative \*pixelMapNative = nullptr;
    OH\_PixelmapNative\_CreatePixelmap(pixels, bufferSize, createOps, &pixelMapNative);
    
4.  Initialize an **OH\_Filter** object using **OH\_Filter\_CreateEffect()** based on the **OH\_PixelmapNative** object created above.
    
    OH\_Filter \*filter = nullptr;
    EffectErrorCode errCodeCreate = OH\_Filter\_CreateEffect(pixelMapNative, &filter);
    
5.  Add different image effects to the filter as required.
    
    -   Add blur effect via **OH\_Filter\_Blur()**.
        
        float radius = 20.0; // Blur radius
        EffectErrorCode errCodeEffect = OH\_Filter\_Blur(filter, radius);
        
    -   Add brightening effect via **OH\_Filter\_Brighten()**.
        
        float brightness = 0.5; //Brightening degree (0 to 1)
        EffectErrorCode errCodeEffect = OH\_Filter\_Brighten(filter, brightness);
        
    -   Add grayscale effect via **OH\_Filter\_GrayScale()**.
        
        EffectErrorCode errCodeEffect = OH\_Filter\_GrayScale(filter);
        
    -   Add color inversion effect via **OH\_Filter\_Invert()**.
        
        EffectErrorCode errCodeEffect = OH\_Filter\_Invert(filter);
        
6.  Obtain the **OH\_PixelmapNative** object after filter processing.
    
    OH\_PixelmapNative\* filterResult = nullptr;
    EffectErrorCode errCodeResult = OH\_Filter\_GetEffectPixelMap(filter, &filterResult);
    
7.  Release the **OH\_Filter** object via **OH\_Filter\_Release()** when no longer needed.
    
    EffectErrorCode errCodeRelease = OH\_Filter\_Release(filter);
    
    The following table lists the effects.
    
    | Image Processing | Effect |
    | :-- | :-- |
    | Original image | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/3c/v3/t5rppGLPQiGyrVDw-EKZmg/en-us_image_0000002537765266.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062050Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=DC36ED4427C4F06C583ED4EC26D91A5BD04BDEFF180766A387CEE280F1CCC702) |
    | Blur effect added | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/7b/v3/MH1iMACyTAypQShOu5CwdA/en-us_image_0000002537925206.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062050Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=E81AF050F12ECB90F37E4055827274AD0B97BEB346425DEF60109A8A60C5269E) |
    | Brightening effect added | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/aa/v3/vGW8QCfrT0K3vjEHqbrVgQ/en-us_image_0000002568684983.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062050Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=13A380BA3D85BC032A8046E0073D711260E31BD2821021317496FDE0BFBC6D30) |
    | Grayscale effect added | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/fb/v3/Gct9OcPxTiqAJTog825XMg/en-us_image_0000002568764993.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062050Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=39BEF2B51FE289730E93A4395FCBCA7EBFE5829C7E2E8E17A37E96AF6A9B2B9E) |
    | Color inversion added | ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/e/v3/mQRbhMFFSJ-eaCezyXkcIA/en-us_image_0000002537765268.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062050Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=58D804A5EB7FC2C68E66B14C620822014F1EC5505D219DC24289FCA8EA8F965B) |
