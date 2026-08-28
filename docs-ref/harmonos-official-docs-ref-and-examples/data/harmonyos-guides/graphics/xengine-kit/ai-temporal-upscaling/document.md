# AI Temporal Upscaling

Since version 6.0.0(20), OpenGL ES is supported.

XEngine Kit provides the AI temporal upscaling capability, which leverages the camera jitter to obtain sampling information at different positions, integrates time domain into the sampling data to perform super-sampling and upscaling, and uses the neural network to remove jaggies. The recommended upscaling factor is \[1.25, 2.0\].

#### Restrictions

-   Phones are supported. Additionally, tablets, PCs/2-in-1 devices, and TVs are supported since version 5.1.0(18).
-   You can check whether the relevant extension is supported as follows:
    
    \- For OpenGL ES, use the extension query API [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring).
    
    \- For Vulkan, use the extension query API [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties).
    
    If the query result contains [XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_temporal_upscale_extension_name), the extension is supported; otherwise, the extension is not supported.
    

#### API Description

The following lists OpenGL ES and Vulkan APIs used for AI temporal upscaling setting. For details about more setting and query APIs, please refer to [API Reference](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine).

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

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_TemporalUpscaleParameter(GLenum pname, const GLvoid \*param)

 | 

Sets the input parameters for AI temporal upscaling.

 |
| 

GL\_APICALL void GL\_APIENTRY HMS\_XEG\_RenderTemporalUpscale(

GLuint inputTexture,

GLuint depthTexture,

GLuint motionVectorTexture,

GLuint dynamicMaskTexture,

GLfloat jitterX,

GLfloat jitterY

)

 | 

Executes the rendering command for AI temporal upscaling.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_EnumerateDeviceExtensionProperties (VkPhysicalDevice physicalDevice, uint32\_t \* pPropertyCount, XEG\_ExtensionProperties \* pProperties)

 | 

Queries XEngine Vulkan extensions.

 |
| 

VKAPI\_ATTR VkResult VKAPI\_CALL HMS\_XEG\_CreateTemporalUpscale (VkDevice device, XEG\_TemporalUpscaleCreateInfo \* pTemporalUpscaleInfo, XEG\_TemporalUpscale \* pTemporalUpscale)

 | 

Creates an **XEG\_TemporalUpscale** object.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_CmdRenderTemporalUpscale (VkCommandBuffer commandBuffer, XEG\_TemporalUpscale temporalUpscale, XEG\_TemporalUpscaleDescription \* pDescription)

 | 

Executes the rendering command for AI temporal upscaling.

 |
| 

VKAPI\_ATTR void VKAPI\_CALL HMS\_XEG\_DestroyTemporalUpscale (XEG\_TemporalUpscale temporalUpscale)

 | 

Destroys an **XEG\_TemporalUpscale** object.

 |

#### Development Procedure

This section uses the OpenGL ES and Vulkan graphics APIs as examples to describe the XEngine integration process.

## Configuring Your Project

When compiling the HAP, add build dependency **libxengine.so** in the NDK for the .so files at the Native layer.

-   Referencing the header files
    
    Reference XEngine Kit's header files as required, for example, if your app needs to call OpenGL ES APIs to use the AI temporal upscaling feature.
    
    #include <cstring>
    #include <cstdlib>
    #include <xengine/xeg\_gles\_extension.h>
    #include <xengine/xeg\_gles\_temporal\_upscale.h>
    
    Reference XEngine Kit's header files as required, for example, if your app needs to call Vulkan APIs to use the AI temporal upscaling feature.
    
    #include <algorithm>
    #include <string>
    #include <vector>
    #include "xengine/xeg\_vulkan\_temporal\_upscale.h"
    #include "xengine/xeg\_vulkan\_extension.h"
    
-   Compiling CMakeLists.txt
    
    Reference the **CMakeLists** file of XEngine Kit as required, for example, when your app needs to call OpenGL ES APIs to use the AI temporal upscaling feature. The following shows part of the sample code in **CMakeLists.txt**.
    
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
    ${EGL-lib} ${GLES-lib} ${xengine-lib})
    
    Reference the **CMakeLists** file of XEngine Kit as required, for example, when your app needs to call Vulkan APIs to use the AI temporal upscaling feature. The following shows part of the sample code in **CMakeLists.txt**. You can find the complete sample code in [Demo (XEngine Kit-Vulkan)](https://gitcode.com/harmonyos_samples/xengine-samplecode-vulkan-temporal-upscale-demo-cpp).
    
    find\_library(
        # Set the name of the path variable.
        hilog-lib
        # Specify the name of the NDK library that
        # you want CMake to locate.
        hilog\_ndk.z
    )
    find\_library(
        # Set the name of the path variable.
        libace-lib
        # Specify the name of the NDK library that
        # you want CMake to locate.
        ace\_ndk.z
    )
    find\_library(
        # Set the name of the path variable.
        libnapi-lib
        # Specify the name of the NDK library that
        # you want CMake to locate.
        ace\_napi.z
    )
    find\_library(
        # Set the name of the path variable.
        libuv-lib
        # Specify the name of the NDK library that
        # you want CMake to locate.
        uv
    )
    add\_library(libassimp SHARED IMPORTED)
    set\_target\_properties(
            libassimp
            PROPERTIES
            IMPORTED\_LOCATION
            ${CMAKE\_CURRENT\_SOURCE\_DIR}/libs/arm64-v8a/libassimp.so
    )
    find\_library(
    # Set the name of the path variable.
    xengine-lib
    # Specify the name of the NDK library that
    # you want CMake to locate.
    xengine
    )
    target\_link\_libraries(nativerender PUBLIC
        ${hilog-lib} ${libace-lib} ${libnapi-lib} ${libuv-lib} libnative\_window.so libc++.a libktx librawfile.z.so libassimp ${xengine-lib})
    

## Integrating the AI Temporal Upscaling Capability of XEngine Kit (OpenGL ES)

Set up the image rendering pipeline using EGL and OpenGL ES graphics APIs, and integrate AI temporal upscaling at the Native layer. The rendering results are displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

This section describes how to perform AI temporal upscaling by calling OpenGL ES graphics APIs.

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_GetString](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_getstring) to obtain the extensions supported by XEngine. The AI temporal upscaling APIs can be used only when the [XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_temporal_upscale_extension_name) extension is supported.
    
    // Query GLES extensions supported by XEngine.
    const char\* extensions = (const char\*)HMS\_XEG\_GetString(XEG\_EXTENSIONS);
    // Check whether the extensions support AI temporal upscaling.
    if (!strstr(extensions, XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME)) {
        exit(1); // return error
    }
    
2.  Call [HMS\_XEG\_TemporalUpscaleParameter](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_temporalupscaleparameter) to set parameters for AI temporal upscaling.
    
    // **m\_lowResWidth** and **m\_lowResHeight** indicate the custom rendering width and height. Here, the resolution is set to 800 x 600 as an example.
    uint32\_t m\_lowResWidth = 800;
    uint32\_t m\_lowResHeight = 600;
    // Set the number of camera jitter cycles. The following uses 8 as an example.
    GLuint jitterNum = 8;
    
    GLsizei inputSize\[2\] = {static\_cast<GLsizei>(m\_lowResWidth), static\_cast<GLsizei>(m\_lowResHeight)};
    // Set the true width and height of the upscaling input texture.
    HMS\_XEG\_TemporalUpscaleParameter(XEG\_TEMPORAL\_UPSCALE\_INPUT\_SIZE, inputSize);
    
    HMS\_XEG\_TemporalUpscaleParameter(XEG\_TEMPORAL\_UPSCALE\_JITTER\_NUM, &jitterNum);
    
    // Set whether depth inversion exists. In this example, depth inversion does not exist.
    GLboolean isDepthReversed = GL\_FALSE;
    HMS\_XEG\_TemporalUpscaleParameter(XEG\_TEMPORAL\_UPSCALE\_DEPTH\_REVERSED, &isDepthReversed);
    
    // Set whether to reset historical frame data. The value **true** indicates that historical frame data is reset, and the value **false** indicates that historical frame data is not reset. You are advised to set this parameter to **true** when upscaling is not used in historical frames but is used in the current frame.
    GLboolean resetHistory = GL\_TRUE;
    HMS\_XEG\_TemporalUpscaleParameter(XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY, &resetHistory);
    
    // Set whether the picture is biased towards the current frame (less ghosting but more flickering) or historical frames (more ghosting but more stable). The following uses 0.5 as an example.
    GLfloat steadyLevel = 0.5;
    HMS\_XEG\_TemporalUpscaleParameter(XEG\_TEMPORAL\_UPSCALE\_STEADY\_LEVEL, &steadyLevel);
    
3.  Call [HMS\_XEG\_RenderTemporalUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_rendertemporalupscale) to perform upscaling for each frame.
    
    The parameters **jitterX** and **jitterY** indicate the camera's jitter in the X and Y directions, respectively, using a low-discrepancy sequence similar to Halton sequences.
    
    In this example, the Halton algorithm is used to calculate the jitter value. Specifically: Use the Halton algorithm to generate a sequence in the range \[0, 1\], then subtract 0.5 to keep the range within \[-0.5, 0.5\]. Finally, divide the range by the resolution of the input image to obtain the Jitter value in UV coordinates.
    
    1.  Generate the camera jitter required by each frame using the Halton algorithm.
        
        // Halton algorithm example
        float GetHaltonSequence(uint32\_t index, uint32\_t base) {
            float result = 0.0;
            float fraction = 1.0 / base;
            while (index > 0) {
                result += fraction \* (index % base);
                index /= base;
                fraction /= base;
            }
            return result;
        }
        // Number of the current frame. The value needs to be increased by 1 to determine the jitter value used by the current frame, until the jitter reaches the value specified by **jitterNum**.
        uint64\_t frameNum = 0;
        // **jitterX** and **jitterY** indicate the camera jitter in the X and Y directions, respectively.
        float jitterX = 0.0;
        float jitterY = 0.0;
        
        // Make sure that the length of the generated low-discrepancy sequence is the same as that of **jitterNum** and is within the range of \[-0.5, 0.5\].
        jitterX = GetHaltonSequence((frameNum % jitterNum) + 1, 2) - 0.5;
        jitterY = GetHaltonSequence((frameNum % jitterNum) + 1, 3) - 0.5;
        // **m\_lowResWidth** and **m\_lowResHeight** indicate the width and height of the input image in Step 2.
        jitterX = jitterX / m\_lowResWidth;
        jitterY = jitterY / m\_lowResHeight;
        
    2.  Call the AI temporal upscaling API for rendering.
        
        // This indicates that **resetHistory** is set to **true** if the first frame uses upscaling, otherwise set to **false**.
        resetHistory = frameNum == 0 ? GL\_TRUE : GL\_FALSE;
        HMS\_XEG\_TemporalUpscaleParameter(XEG\_TEMPORAL\_UPSCALE\_RESET\_HISTORY, &resetHistory);
        
        // **m\_upscaleFBO** indicates the custom framebuffer parameter after upscaling.
        unsigned int m\_upscaleFBO;
        unsigned int m\_highResWidth;
        unsigned int m\_highResHeight;
        unsigned int m\_lowLightColorTexture;
        unsigned int m\_lowGboDepth;
        unsigned int m\_motionVectorTexture, m\_dynamicMaskTexture;
        
        glBindFramebuffer(GL\_FRAMEBUFFER, m\_upscaleFBO);
        glViewport(0, 0, m\_highResWidth, m\_highResHeight);
        glScissor(0, 0, m\_highResWidth, m\_highResHeight);
        
        // **m\_lowLightColorTexture** indicates the upscaling input texture.
        // **m\_lowGboDepth** indicates the depth texture.
        // **m\_motionVectorTexture** indicates a motion vector image. The motion vector is computed by subtracting the X and Y values of the NDC coordinates of the previous frame from those of the current rendered pixel.
        // **m\_dynamicMaskTexture** indicates a dynamic mask image of the object. The format must be **GL\_RED** or its compatible format. The valid value of the R channel is **0.0**, **0.2**, or **1.0**, where **0.0** indicates static objects, **0.2** indicates moving objects such as people, and **1.0** indicates special effects or translucent objects.
        // **jitterX** indicates the camera jitter offset along the X axis.
        // **jitterY** indicates the camera jitter offset along the Y axis.
        HMS\_XEG\_RenderTemporalUpscale(m\_lowLightColorTexture, m\_lowGboDepth, m\_motionVectorTexture, m\_dynamicMaskTexture,
        							 -0.5\*jitterX, -0.5\*j**itterY);**
        
    

## Integrating the AI Temporal Upscaling Capability of XEngine Kit (Vulkan)

Set up the image rendering pipeline using Vulkan graphics APIs, and integrate AI temporal upscaling at the Native layer. The rendering results are displayed on the screen through [XComponent](https://developer.huawei.com/consumer/en/doc/harmonyos-references/ts-basic-components-xcomponent).

This section describes how to perform AI temporal upscaling by calling Vulkan graphics APIs. You can find the complete sample code in [Sample Code](https://gitcode.com/harmonyos_samples/xengine-samplecode-vulkan-temporal-upscale-demo-cpp).

Before calling XEngine Kit capabilities, you need to check whether the target device supports the SystemCapability.Graphic.XEngine system capability via [Syscap](https://developer.huawei.com/consumer/en/doc/harmonyos-references/syscap#checking-whether-an-api-is-available).

1.  Call [HMS\_XEG\_EnumerateDeviceExtensionProperties](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_enumeratedeviceextensionproperties) to obtain the extensions supported by XEngine. The AI temporal upscaling APIs can be used only when the [XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#xeg_temporal_upscale_extension_name) extension is supported.
    
    // **physicalDevice** indicates a physical device defined by Vulkan and needs to be initialized.
    VkPhysicalDevice physicalDevice;
    // Query the Vulkan extensions supported by XEngine.
    std::vector<std::string> supportedExtensions;
    uint32\_t pPropertyCount;
    HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount, nullptr);
    if (pPropertyCount > 0) {
        std::vector<XEG\_ExtensionProperties> pProperties(pPropertyCount);
        if (HMS\_XEG\_EnumerateDeviceExtensionProperties(physicalDevice, &pPropertyCount,
            &pProperties.front()) == VK\_SUCCESS) {
            for (auto ext : pProperties) {
                supportedExtensions.push\_back(ext.extensionName);
            }
        }
    }
    // Check whether the extensions support AI temporal upscaling.
    if (std::find(supportedExtensions.begin(), supportedExtensions.end(), XEG\_TEMPORAL\_UPSCALE\_EXTENSION\_NAME) ==
        supportedExtensions.end()) {
        exit(1); // return error;
    }
    
2.  Declare the instance handle.
    
    XEG\_TemporalUpscale xegTemporalUpscale;
    
3.  Call [HMS\_XEG\_CreateTemporalUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_createtemporalupscale) to create an AI temporal upscaling instance.
    
    // The rendering width and height, as well as the width and height after upscaling, are custom parameters. Here, we'll use an example of upscaling an 800 x 600 resolution by 1.5 times to a 1200 x 900 resolution.
    uint32\_t lowResWidth = 800;
    uint32\_t lowResHeight = 600;
    uint32\_t highResWidth = 1200;
    uint32\_t highResHeight = 900;
    const uint32\_t jitterNum = 8;
    // Logical device defined by Vulkan, which needs to be initialized.
    VkDevice device;
    // **XEG\_TemporalUpscaleCreateInfo** indicates the information required for creating an **XEG\_TemporalUpscale** object.
    XEG\_TemporalUpscaleCreateInfo createInfo;
    // Specify the size of the input image, that is, the size of the low-resolution image.
    createInfo.inputSize = {lowResWidth, lowResHeight};
    // Specify the size of the output image, that is, the size of the high-resolution image.
    createInfo.outputSize = {highResWidth, highResHeight};
    // Specify the color format of the output image.
    createInfo.outputFormat = VK\_FORMAT\_R8G8B8A8\_UNORM;
    // **jitterNum** indicates the number of camera jitter cycles.
    createInfo.jitterNum = jitterNum;
    // Specify whether the depth value is inverted.
    createInfo.isDepthReversed = true;
    VkResult res = HMS\_XEG\_CreateTemporalUpscale(device, &createInfo, &xegTemporalUpscale);
    if (res != VK\_SUCCESS) {
        exit(1); // return error;
    }
    
4.  Call [HMS\_XEG\_CmdRenderTemporalUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_cmdrendertemporalupscale) to perform upscaling for each frame.
    
    The parameters **jitterX** and **jitterY** indicate the camera's jitter in the X and Y directions, respectively, using a low-discrepancy sequence similar to Halton sequences.
    
    In this example, the Halton algorithm is used to calculate the jitter value. Specifically: Use the Halton algorithm to generate a sequence in the range \[0, 1\], then subtract 0.5 to keep the range within \[-0.5, 0.5\]. Finally, divide the range by the resolution of the input image to obtain the Jitter value in UV coordinates.
    
    1.  Generate the camera jitter required by each frame using the Halton algorithm.
        
        // Halton algorithm example
        float GetHaltonSequence(uint32\_t index, uint32\_t base) {
            float result = 0.0;
            float fraction = 1.0 / base;
            while (index > 0) {
                result += fraction \* (index % base);
                index /= base;
                fraction /= base;
            }
            return result;
        }
        
    2.  Call the AI temporal upscaling API for rendering.
        
        // Number of the current frame. The value needs to be increased by 1 to determine the jitter value used by the current frame, until the jitter reaches the value specified by **jitterNum**.
        uint64\_t frameNum = 0;
        // **jitterX** and **jitterY** indicate the camera jitter in the X and Y directions, respectively.
        float jitterX = 0.0;
        float jitterY = 0.0;
        // Define an **xegDescription** object for **XEG\_TemporalUpscaleDescription**.
        XEG\_TemporalUpscaleDescription xegDescription;
        // **inputImageView** indicates the **VkImageView** of the upscaling input image. You need to create this **VkImageView**.
        VkImageView inputImageView = VK\_NULL\_HANDLE;
        // **depthImageView** indicates the **VkImageView** of the depth image. You need to create this **VkImageView**.
        VkImageView motionVectorImageView= VK\_NULL\_HANDLE;
        // **motionVectorImageView** indicates the **VkImageView** of the motion vector image. You need to create this **VkImageView**.
        VkImageView depthImageView = VK\_NULL\_HANDLE;
        // **dynamicMaskImageView** indicates the **VkImageView** of an object's dynamic mask image. You need to create this **VkImageView**.
        VkImageView dynamicMaskImageView = VK\_NULL\_HANDLE;
        // **outputImageView** indicates the **VkImageView** of the upscaling output image. You need to create this **VkImageView**.
        VkImageView outputImageView = VK\_NULL\_HANDLE;
        // **commandBuffer** indicates the command buffer and needs to be initialized.
        VkCommandBuffer commandBuffer = VK\_NULL\_HANDLE;
        xegDescription.inputImage = inputImageView;
        xegDescription.depthImage = depthImageView;
        xegDescription.motionVectorImage = motionVectorImageView;
        xegDescription.dynamicMaskImage = dynamicMaskImageView;
        xegDescription.outputImage = outputImageView;
        // Make sure that the length of the generated low-discrepancy sequence is the same as that of **jitterNum** and is within the range of \[-0.5, 0.5\].
        jitterX = GetHaltonSequence((frameNum % jitterNum) + 1, 2) - 0.5;
        jitterY = GetHaltonSequence((frameNum % jitterNum) + 1, 3) - 0.5;
        // **lowResWidth** and **lowResHeight** indicate the width and height of the input image in Step 3.
        jitterX = jitterX / lowResWidth;
        jitterY = jitterY / lowResHeight;
        xegDescription.jitterX = -jitterX;
        xegDescription.jitterY = -jitterY;
        // **resetHistory** indicates whether to reset historical frame data (**true**) or not (**false**). The following uses value **true** as an example.
        xegDescription.resetHistory = (frameNum == 0) ? true : false;
        // **steadyLevel** indicates the image's degree of bias towards the current frame or historical frames. The value range is \[0.0, 1.0\]. The following uses value **0.5** as an example.
        xegDescription.steadyLevel = 0.5;
        HMS\_XEG\_CmdRenderTemporalUpscale(commandBuffer, xegTemporalUpscale, &xegDescription);
        
    
5.  Call [HMS\_XEG\_DestroyTemporalUpscale](https://developer.huawei.com/consumer/en/doc/harmonyos-references/xengine-kit-xengine#hms_xeg_destroytemporalupscale) to destroy the instance.
    
    if (xegTemporalUpscale) {
        HMS\_XEG\_DestroyTemporalUpscale(xegTemporalUpscale);
    }
