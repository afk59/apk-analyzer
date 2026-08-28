# AI Spatial Upscaling

XEngine Kit provides the AI spatial upscaling capability. It uses AI inference to generate filtering parameters for upsampling based on single-frame images. By leveraging the cooperation between GPU and NPU, it achieves better image quality than GPU spatial upscaling. AI spatial upscaling is recommended when the upscaling factor is below 1.5x.

#### Restrictions

-   Phones are supported. Additionally, tablets, PCs/2-in-1 devices, and TVs are supported since version 5.1.0(18).
-   You can check whether an extension is supported as follows:
    
    For OpenGL ES, use the extension query API [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring). If the query result contains [XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_neural_upscale_extension_name), the extension is supported; otherwise, the extension is not supported.
    

#### API Description

The following lists OpenGL ES APIs used for AI spatial upscaling setting. For details about more setting and query APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine).

| 
API Name

 | 

Description

 |
| :-- | :-- |
| 

const GLubyte \* HMS\_XEG\_GetString (GLenum name)

 | 

Queries XEngine OpenGL ES extensions.

 |
| 

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_NeuralUpscaleParameter (GLenum pname, GLvoid \* param)

 | 

Sets the input parameters for AI spatial upscaling.

 |
| 

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderNeuralUpscale (GLuint inputTexture)

 | 

Executes the rendering command for AI spatial upscaling.

 |

#### Development Procedure

This section uses the OpenGL ES graphics API as an example to describe the XEngine integration process.

## Configuring Your Project

When compiling the HAP, add build dependency **libxengine.so** in the NDK for the .so files at the Native layer.

-   Referencing the header files
    
    #include <cstring>
    #include <cstdlib>
    #include <EGL/egl.h>
    #include <EGL/eglext.h>
    #include <GLES2/gl2.h>
    #include <GLES2/gl2ext.h>
    #include <xengine/xeg\_gles\_extension.h>
    #include <xengine/xeg\_gles\_neural\_upscale.h>
    #include <native\_buffer/native\_buffer.h>
    #include <native\_window/external\_window.h>
    
-   Compiling CMakeLists.txt
    
    The following shows part of the sample code in **CMakeLists.txt**. You can find the complete sample code in [Demo (XEngine Kit-GLES)](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp).
    
    find\_library(
        # Set the name of the path variable.
        native-buffer-lib
        # Specify the name of the NDK library that you want CMake to locate.
        native\_buffer
    )
    find\_library(
        # Set the name of the path variable.
        native-window-lib
        # Specify the name of the NDK library that you want CMake to locate.
        native\_window
    )
    find\_library(
        # Set the name of the path variable.
        xengine-lib
        # Specify the name of the NDK library that you want CMake to locate.
        xengine
    )
    find\_library(
        # Set the name of the path variable.
        EGL-lib
        # Specify the name of the NDK library that you want CMake to locate.
        EGL
    )
    find\_library(
        # Set the name of the path variable.
        GLES-lib
        # Specify the name of the NDK library that you want CMake to locate.
        GLESv3
    )
    
    target\_link\_libraries(nativerender PUBLIC
    ${EGL-lib} ${GLES-lib} ${xengine-lib} ${native-window-lib} ${native-buffer-lib})
    

## Integrating the AI Spatial Upscaling Capability of XEngine Kit (OpenGL ES)

Set up the image rendering pipeline using OpenGL ES and XEngine graphics APIs, and integrate AI spatial upscaling at the Native layer. The rendering results are displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

This section describes how to perform AI spatial upscaling by calling OpenGL ES graphics APIs. You can find the complete sample code in [Demo (XEngine Kit-GLES)](https://gitcode.com/harmonyos_samples/xengine-samplecode-gles-demo-cpp).

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring) to obtain the extensions supported by XEngine. The AI spatial upscaling APIs can be used only when the [XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_neural_upscale_extension_name) extension is supported.
    
    // Query GLES extensions supported by XEngine.
    const char\* extensions = (const char\*)HMS\_XEG\_GetString(XEG\_EXTENSIONS);
    // Check whether the extensions support AI spatial upscaling.
    if (!strstr(extensions, XEG\_NEURAL\_UPSCALE\_EXTENSION\_NAME)) {
        exit(1); // return error
    }
    
2.  Create an input texture and attach it with an **OH\_NativeBuffer**.
    
    // The rendering width and height, as well as the display width and height, are custom parameters. Here, we'll use an example of upscaling an 800 x 600 resolution by 1.5 times to a 1200 x 900 resolution.
    uint32\_t renderWidth = 800;
    uint32\_t renderHeight = 600;
    uint32\_t displayWidth = 1200;
    uint32\_t displayHeight = 900;
    // Obtain the function pointer.
    PFNEGLCREATEIMAGEKHRPROC fp\_eglCreateImageKHR = reinterpret\_cast<PFNEGLCREATEIMAGEKHRPROC>(eglGetProcAddress("eglCreateImageKHR"));
    PFNEGLDESTROYIMAGEKHRPROC fp\_eglDestroyImageKHR = reinterpret\_cast<PFNEGLDESTROYIMAGEKHRPROC>(eglGetProcAddress("eglDestroyImageKHR"));
    PFNGLEGLIMAGETARGETTEXTURE2DOESPROC fp\_glEGLImageTargetTexture2DOES = reinterpret\_cast<PFNGLEGLIMAGETARGETTEXTURE2DOESPROC>(eglGetProcAddress("glEGLImageTargetTexture2DOES"));
    // Create an **OH\_NativeBuffer**.
    OH\_NativeBuffer\_Config config = {};
    config.width = renderWidth;
    config.height = renderHeight;
    config.usage = NATIVEBUFFER\_USAGE\_CPU\_READ | NATIVEBUFFER\_USAGE\_CPU\_READ\_OFTEN | NATIVEBUFFER\_USAGE\_HW\_TEXTURE | NATIVEBUFFER\_USAGE\_HW\_RENDER| NATIVEBUFFER\_USAGE\_ALIGNMENT\_512;
    config.format = NATIVEBUFFER\_PIXEL\_FMT\_RGBA\_8888;
    OH\_NativeBuffer\* bufferHandle = OH\_NativeBuffer\_Alloc(&config);
    if (bufferHandle == nullptr) {
        // Creation fails. You can customize error handling.
    }
    OHNativeWindowBuffer \*nativeWindowBuffer = OH\_NativeWindow\_CreateNativeWindowBufferFromNativeBuffer(bufferHandle);
    EGLImageKHR eglImage = fp\_eglCreateImageKHR(eglGetCurrentDisplay(), EGL\_NO\_CONTEXT, EGL\_NATIVE\_BUFFER\_OHOS, static\_cast<EGLClientBuffer>(nativeWindowBuffer), nullptr);
    // Create an upscaling input texture.
    GLuint textureID; 
    glGenTextures(1, &textureID);
    glBindTexture(GL\_TEXTURE\_2D, textureID);
    // Set the texture wrapping and filtering parameters.
    glTexParameteri(GL\_TEXTURE\_2D, GL\_TEXTURE\_WRAP\_S, GL\_REPEAT);
    glTexParameteri(GL\_TEXTURE\_2D, GL\_TEXTURE\_WRAP\_T, GL\_REPEAT);
    glTexParameteri(GL\_TEXTURE\_2D, GL\_TEXTURE\_MIN\_FILTER, GL\_NEAREST);
    glTexParameteri(GL\_TEXTURE\_2D, GL\_TEXTURE\_MAG\_FILTER, GL\_NEAREST);
    // Associate the upscaling input texture with **eglImage**.
    fp\_glEGLImageTargetTexture2DOES(GL\_TEXTURE\_2D, eglImage);
    
3.  Render on the upscaling input texture.
    
    GLuint fboID = 0;
    glGenFramebuffers(1, &fboID);
    glBindFramebuffer(GL\_FRAMEBUFFER, fboID);
    glFramebufferTexture2D(GL\_FRAMEBUFFER, GL\_COLOR\_ATTACHMENT0, GL\_TEXTURE\_2D, textureID, 0);
    if (glCheckFramebufferStatus(GL\_FRAMEBUFFER) != GL\_FRAMEBUFFER\_COMPLETE) {
      // Framebuffer creation fails. You can customize error handling.
    }
    glViewport(0, 0, renderWidth, renderHeight);
    
4.  Call [HMS\_XEG\_NeuralUpscaleParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_neuralupscaleparameter) to set the input parameters for AI spatial upscaling.
    
    // **sharpness** indicates the custom sharpening parameter. Here, its value is set to **0.3f** as an example.
    float sharpness = 0.3f;
    HMS\_XEG\_NeuralUpscaleParameter(XEG\_NEURAL\_UPSCALE\_SHARPNESS, &sharpness);
    // **inputScissor** indicates the cropping window parameter of the upscaling input texture.
    GLuint inputScissor\[4\] = {0, 0, renderWidth, renderHeight};
    HMS\_XEG\_NeuralUpscaleParameter(XEG\_NEURAL\_UPSCALE\_SCISSOR, inputScissor);
    // Set the **OH\_NativeBuffer** handle corresponding to the upscaling input texture.
    HMS\_XEG\_NeuralUpscaleParameter(XEG\_NEURAL\_UPSCALE\_INPUT\_HANDLE, bufferHandle);
    
5.  Call [HMS\_XEG\_RenderNeuralUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_renderneuralupscale) to perform AI spatial upscaling.
    
    // Bind the frame buffer for drawing the upscaling result. Here, the default frame buffer is used. You can also customize the frame buffer.
    glBindFramebuffer(GL\_FRAMEBUFFER, 0);
    glViewport(0, 0, displayWidth, displayHeight);
    // Perform AI spatial upscaling.
    HMS\_XEG\_RenderNeuralUpscale(textureID);
    
6.  Destroy the relevant resources when upscaling rendering is not needed.
    
    glDeleteFramebuffers(1, &fboID);
    glDeleteTextures(1, &textureID);
    if (eglImage != nullptr) {
       fp\_eglDestroyImageKHR(eglGetCurrentDisplay(), eglImage);
    }
    if (nativeWindowBuffer != nullptr) {
       OH\_NativeWindow\_DestroyNativeWindowBuffer(nativeWindowBuffer);
    }
    if (bufferHandle != nullptr) {
       OH\_NativeBuffer\_Unreference(bufferHandle);
    }
