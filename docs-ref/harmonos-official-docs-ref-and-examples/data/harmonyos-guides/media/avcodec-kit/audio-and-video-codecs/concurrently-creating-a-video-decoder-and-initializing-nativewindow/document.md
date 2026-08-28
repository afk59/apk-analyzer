# Concurrently Creating a Video Decoder and Initializing NativeWindow

#### When to Use

To ensure that a video decoder can be created and run properly in surface mode, you can create an empty surface before the **XComponent** is created or the OpenGL post-processing (NativeImage) is initialized.

#### How to Develop

The following describes how to concurrently create a video decoder and initialize NativeWindow. This approach ensures that the video decoder can be set up and executed properly, even before the surface consumer is ready.

**Linking Dynamic Libraries**

target\_link\_libraries(sample PUBLIC libnative\_image.so)
target\_link\_libraries(sample PUBLIC libnative\_window.so)
target\_link\_libraries(sample PUBLIC libnative\_buffer.so)
target\_link\_libraries(sample PUBLIC libnative\_media\_vdec.so)

![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/cd/v3/8zCil9-sRMi2JHCAASKnJg/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=0CD3FAB0A57B4D46A01ADFB21F82EADDD17AD126263AECF939FE2418A9FEDEF5)

The word **sample** in the preceding code snippet is only an example. Use the actual project directory name.

**Including Header Files**

#include <iostream>
#include <string>
#include <native\_image/native\_image.h>
#include <native\_window/external\_window.h>
#include <native\_buffer/native\_buffer.h>
#include <multimedia/player\_framework/native\_avcodec\_videodecoder.h>

1.  Create an OH\_NativeImage instance.
    
    // Create a NativeImage instance as the surface consumer.
    OH\_NativeImage\* image = OH\_ConsumerSurface\_Create();
    
2.  Obtain the NativeWindow instance that functions as the producer.
    
    // Obtain a NativeWindow instance.
    OHNativeWindow\* nativeImageWindow = OH\_NativeImage\_AcquireNativeWindow(image);
    
3.  Set the width and height of the NativeWindow instance.
    
    int code = SET\_BUFFER\_GEOMETRY;
    int32\_t width = 800;
    int32\_t height = 600;
    int32\_t ret = OH\_NativeWindow\_NativeWindowHandleOpt(nativeImageWindow, code, width, height);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
4.  Register a callback function for the NativeImage instance.
    
    Register the **OH\_OnFrameAvailableListener**, which contains the following parameters:
    
    -   **context**: user-defined context information.
    -   **onFrameAvailable**: callback function triggered when a frame is available.
    
    // Implement onFrameAvailable.
    static void onFrameAvailable()
    {
      OHNativeWindowBuffer \*buffer = nullptr;
      int fenceFd;
      // Obtain an OHNativeWindowBuffer instance through the OH\_NativeImage instance on the consumer side.
      OH\_NativeImage\_AcquireNativeWindowBuffer(image, &buffer, &fenceFd);
      // Release the OHNativeWindowBuffer instance through the OH\_NativeImage instance.
      OH\_NativeImage\_ReleaseNativeWindowBuffer(image, buffer, fenceFd);
    }
    
    static void context()
    {
      // Customize the context information.
    }
    
    // Set a listener.
    OH\_OnFrameAvailableListener listener = {&onFrameAvailable, &context};
    // Register the listener to listen for frame availability events.
    ret = OH\_NativeImage\_SetOnFrameAvailableListener(image, listener);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
    ![](https://contentcenter-vali-drcn.dbankcdn.cn/pvt_2/DeveloperAlliance_scene_100_1/22/v3/jNLmRW75R6KZ87KyQKL7lA/note_3.0-en-us.png?HW-CC-KV=V1&amp;HW-CC-Date=20260410T062036Z&amp;HW-CC-Expire=86400&amp;HW-CC-Sign=9205830A6E50885475465C395F43814A4DFA79C686663BE8ED449C9CFC4C5274)
    
    In this example, the callback function just retrieves and releases the buffer. You can customize and expand the callback function based on service requirements.
    
5.  Configure the decoder.
    
    For details, see step 5 in [Video Decoding in Surface Mode](../video-decoding/document.md#surface-mode).
    
6.  Set the surface.
    
    Before the actual surface consumer is created, you can use the temporarily created consumer to connect to the decoder.
    
    In the code snippet below, the following variables are used:
    
    -   **videoDec**: pointer to the video decoder instance. For details, see step 2 in [Video Decoding in Surface Mode](../video-decoding/document.md#surface-mode).
    
    ret = OH\_VideoDecoder\_SetSurface(videoDec, nativeImageWindow);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
7.  Start the decoder.
    
    For details, see step 8 in [Video Decoding in Surface Mode](../video-decoding/document.md#surface-mode).
    
8.  Set the surface.
    
    After the actual surface consumer is created, call **OH\_VideoDecoder\_SetSurface** to redirect the decoded output to the new surface.
    
    You can obtain NativeWindow in either of the following ways:
    
    -   If the image is directly displayed after being decoded, obtain NativeWindow from the **XComponent**. For details about the operation, see [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).
    -   If OpenGL post-processing is performed after decoding, obtain NativeWindow from NativeImage. For details about the operation, see [NativeImage](../../../../graphics/arkgraphics-2d/native-image-development-c-c/document.md).
    
    ret = OH\_VideoDecoder\_SetSurface(videoDec, nativeWindow);
    if (ret != AV\_ERR\_OK) {
        // Handle exceptions.
    }
    
9.  Destroy the OH\_NativeImage instance.
    
    After calling **OH\_VideoDecoder\_Destroy**, call **OH\_NativeImage\_Destroy** to destroy the OH\_NativeImage instance.
    
    // Destroy the OH\_NativeImage instance.
    OH\_NativeImage\_Destroy(&image);
